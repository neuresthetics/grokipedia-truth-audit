#!/usr/bin/env python3
"""grokaudit.py - structural audit helper for Grokipedia article pages.

Stdlib only (Python 3.9+). Read-only on the web: it only issues HEAD/GET requests
to the article's own cited source URLs (linkcheck / fetch), with a polite delay.

Subcommands
  parse      HTML -> claims.csv (sentence-level, with citation numbers), sources.csv,
             structure.json (dangling cites, uncited sentences, unused / duplicate sources,
             malformed URLs, citation-offset probe).
  linkcheck  HTTP status of every source URL (HEAD, GET fallback), rate-limited per host.
  fetch      Download cited sources (HTML/PDF) into a cache dir as text, for manual claim checking.
  refs       Extract Spinoza work citations (Ethics E1P15-style, TTP/TP chapters, Letters)
             and quoted strings from claims; optional fuzzy quote check against local
             public-domain texts (--corpus file.txt ...).
  soft404    Scan fetched cache for 200-status pages that are really "not found" / bot walls.
  buildlog   Merge worksheet.csv + a hand-written verdicts file (pipe-separated) into the
             full per-claim audit log; unjudged uncited claims -> UNCITED, unjudged cited
             claims -> NOT_CHECKED. Refuses to run if a priority/sample claim lacks a verdict.
  report     Count verdicts in a hand-filled audit log CSV (column 'verdict').

What the script does NOT do: decide whether a source supports a claim. Those verdicts are
human/model judgment and are recorded in the audit log, which `report` merely counts.

Example
  python3 grokaudit.py parse page.html -o out/
  python3 grokaudit.py linkcheck out/sources.csv -o out/linkcheck.csv --delay 1.5
  python3 grokaudit.py refs out/claims.csv -o out/spinoza_refs.csv --corpus ethics_elwes.txt
  python3 grokaudit.py report audit_log.csv
"""
from __future__ import annotations

import argparse
import csv
import difflib
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

UA = "Mozilla/5.0 (X11; Linux x86_64) grokaudit/0.1 (read-only citation checker)"

# ----------------------------------------------------------------------------- parsing
class _PageParser(HTMLParser):
    """Collects article-body blocks (paragraph text with ⟦n⟧ citation markers and the
    current section heading) and the <li id="ref-N"> source list."""

    BLOCK_ATTR = "data-tts-block"

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth_body = 0          # >0 while inside div.article-body
        self.div_stack = []          # track div nesting to find end of article-body
        self.in_block = 0            # span[data-tts-block] nesting
        self.block_tag_depth = 0
        self.cur = []                # current block text pieces
        self.blocks = []             # (section_path, text)
        self.heading = {2: "", 3: ""}
        self.in_heading = None
        self.head_buf = []
        self.sup_depth = 0
        self.sup_href = None
        self.sup_emitted = set()
        # references
        self.in_ref_li = None
        self.ref_buf_title = []
        self.in_ref_link = False
        self.sources = {}            # n -> dict(url,title,domain)
        self.ref_domain_span = False
        self.ref_dom_buf = []
        self.skip = 0                # inside script/style/button/svg

    # helpers
    def _section(self):
        h2, h3 = self.heading[2], self.heading[3]
        return f"{h2} > {h3}" if h3 else h2

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("script", "style", "svg", "button"):
            self.skip += 1
            return
        if self.skip:
            return
        cls = a.get("class", "") or ""
        if tag == "div":
            if "article-body" in cls.split() and not self.depth_body:
                self.depth_body = 1
                self.div_stack = [1]
            elif self.depth_body:
                self.div_stack.append(0)
        if self.depth_body and tag in ("h2", "h3"):
            self.in_heading = int(tag[1]); self.head_buf = []
        if self.depth_body and tag == "span" and a.get(self.BLOCK_ATTR) is not None:
            self.in_block += 1
            if self.in_block == 1:
                self.cur = []
        elif self.in_block and tag == "span":
            self.in_block += 1
        if (self.in_block or self.in_heading) and tag == "sup":
            self.sup_depth += 1
            if self.sup_depth == 1:
                self.sup_emitted = set()
        if tag == "a" and self.sup_depth and self.in_block:
            href = a.get("href", "")
            m = re.match(r"#ref-(\d+)$", href)
            if m and m.group(1) not in self.sup_emitted:
                self.sup_emitted.add(m.group(1))
                self.cur.append(f" ⟦{m.group(1)}⟧")
        # references list
        if tag == "li" and re.match(r"ref-\d+$", a.get("id", "") or ""):
            self.in_ref_li = int(a["id"].split("-")[1])
            self.sources[self.in_ref_li] = {"n": self.in_ref_li, "url": "", "title": "", "domain": ""}
        if self.in_ref_li and tag == "a" and "ref-link" in cls:
            self.sources[self.in_ref_li]["url"] = a.get("href", "")
            self.in_ref_link = True; self.ref_buf_title = []
        if self.in_ref_li and tag == "span" and "type-hint" in cls:
            self.ref_domain_span = True; self.ref_dom_buf = []

    def handle_endtag(self, tag):
        if tag in ("script", "style", "svg", "button"):
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "div" and self.depth_body:
            if self.div_stack:
                top = self.div_stack.pop()
                if top == 1:
                    self.depth_body = 0
        if self.in_heading and tag == f"h{self.in_heading}":
            t = re.sub(r"\s+", " ", "".join(self.head_buf)).strip()
            self.heading[self.in_heading] = t
            if self.in_heading == 2:
                self.heading[3] = ""
            self.in_heading = None
        if tag == "sup" and self.sup_depth:
            self.sup_depth -= 1
        if tag == "span" and self.in_block:
            self.in_block -= 1
            if self.in_block == 0:
                txt = re.sub(r"\s+", " ", "".join(self.cur)).strip()
                if txt:
                    self.blocks.append((self._section(), txt))
        if tag == "span" and self.ref_domain_span:
            self.ref_domain_span = False
            if self.in_ref_li:
                self.sources[self.in_ref_li]["domain"] = "".join(self.ref_dom_buf).strip()
        if tag == "a" and self.in_ref_link:
            self.in_ref_link = False
            self.sources[self.in_ref_li]["title"] = re.sub(r"\s+", " ", "".join(self.ref_buf_title)).strip()
        if tag == "li" and self.in_ref_li:
            self.in_ref_li = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.in_heading:
            self.head_buf.append(data)
        if self.in_block and not self.sup_depth:
            self.cur.append(data)
        if self.in_ref_link:
            self.ref_buf_title.append(data)
        if self.ref_domain_span:
            self.ref_dom_buf.append(data)


ABBREV = {"e.g", "i.e", "c", "ca", "cf", "no", "nos", "vol", "vols", "st", "dr", "mr", "mrs", "prof",
          "ed", "eds", "trans", "p", "pp", "vs", "viz", "al", "fl", "b", "d", "jr", "sr", "dircksz", "ch",
          "chap", "prop", "def", "ax", "schol", "cor", "esp", "approx", "fig", "ibid", "op", "cit"}

_SENT_END = re.compile(r'([.!?])(["”’\')\]]*)((?:\s*⟦\d+⟧)*)\s+(?=["“‘(\[]?[A-Z0-9])')


def split_sentences(text: str):
    """Split paragraph text (with ⟦n⟧ markers placed after punctuation) into sentences.
    Returns list of (sentence_text_without_markers, [cite numbers])."""
    out, start = [], 0
    for m in _SENT_END.finditer(text):
        end = m.end(3)
        before = text[start:m.start(1)]
        last = re.search(r"([A-Za-z][A-Za-z.]*)$", before)
        tok = last.group(1).lower().rstrip(".") if last else ""
        if tok in ABBREV or (last and len(last.group(1)) == 1 and last.group(1).isupper()):
            continue
        out.append(text[start:end]); start = m.end()
    if start < len(text):
        out.append(text[start:])
    res = []
    for s in out:
        cites = [int(x) for x in re.findall(r"⟦(\d+)⟧", s)]
        clean = re.sub(r"\s*⟦\d+⟧", "", s).strip()
        if clean:
            res.append((clean, cites))
    # markers that start a sentence (rare) belong to the previous sentence
    return res


def parse_page(html_text: str):
    p = _PageParser()
    p.feed(html_text)
    claims = []
    cid = 0
    for bi, (section, txt) in enumerate(p.blocks, 1):
        for si, (sent, cites) in enumerate(split_sentences(txt), 1):
            cid += 1
            claims.append({"claim_id": f"C{cid:03d}", "para": bi, "sent": si, "section": section,
                           "text": sent, "cites": cites})
    # paragraph-level carry: a sentence with no marker inside a paragraph whose LATER sentence
    # carries a marker is often covered by that marker (Wikipedia-style end-of-paragraph cites).
    by_para = defaultdict(list)
    for c in claims:
        by_para[c["para"]].append(c)
    for para, cs in by_para.items():
        nxt = []
        for c in reversed(cs):
            c["para_next_cites"] = list(nxt) if not c["cites"] else []
            if c["cites"]:
                nxt = c["cites"]
    return claims, [p.sources[k] for k in sorted(p.sources)]


def norm_url(u: str) -> str:
    u = html.unescape(u.strip())
    try:
        s = urllib.parse.urlsplit(u)
    except ValueError:
        return u
    host = s.netloc.lower().removeprefix("www.")
    path = urllib.parse.unquote(s.path).rstrip("/")
    return f"{host}{path}?{s.query}" if s.query else f"{host}{path}"


def _tokens(s: str):
    stop = set("the a an of and or in on to for by with from as is are was be his he it its that this which "
               "spinoza spinoza's baruch benedict de pdf university chapter".split())
    return {w for w in re.findall(r"[a-z]{4,}", s.lower()) if w not in stop}


def offset_probe(claims, sources, window=12):
    """Heuristic hint only: for each cited number n, compare the claim's words with the TITLE of
    source n+k for k in [-window, window]. A real offset (inline numbers pointing k places away
    from the intended source) shows up as k != 0 winning repeatedly in a contiguous number range.
    Output is a hint for a human, not a verdict."""
    src = {s["n"]: _tokens(s["title"] + " " + s["url"]) for s in sources}
    rows = []
    for c in claims:
        ct = _tokens(c["text"])
        for n in c["cites"]:
            best_k, best = 0, len(ct & src.get(n, set()))
            for k in range(-window, window + 1):
                ov = len(ct & src.get(n + k, set()))
                if ov > best:
                    best_k, best = k, ov
            rows.append({"claim_id": c["claim_id"], "cite": n, "overlap_at_n": len(ct & src.get(n, set())),
                         "best_k": best_k, "overlap_at_best": best})
    return rows


def cmd_parse(args):
    h = Path(args.html).read_text(encoding="utf-8", errors="replace")
    claims, sources = parse_page(h)
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    ns = {s["n"] for s in sources}
    cited = Counter(n for c in claims for n in c["cites"])
    dangling = sorted(n for n in cited if n not in ns)
    unused = sorted(n for n in ns if n not in cited)
    dup = defaultdict(list)
    for s in sources:
        dup[norm_url(s["url"])].append(s["n"])
    dups = {u: v for u, v in dup.items() if len(v) > 1}
    malformed = [s["n"] for s in sources
                 if s["url"].count("(") != s["url"].count(")") or not re.match(r"https?://", s["url"])]
    leaks = [c["claim_id"] for c in claims if re.search(r"\.\/[A-Z][\w_]*#|\]\(|\)\s*$", c["text"]) and "/" in c["text"]]
    uncited = [c for c in claims if not c["cites"]]
    uncited_strict = [c for c in uncited if not c["para_next_cites"]]
    probe = offset_probe(claims, sources)
    with open(out / "claims.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["claim_id", "para", "sent", "section", "cites", "dangling_cites", "para_next_cites", "text"])
        for c in claims:
            w.writerow([c["claim_id"], c["para"], c["sent"], c["section"], " ".join(map(str, c["cites"])),
                        " ".join(str(n) for n in c["cites"] if n not in ns),
                        " ".join(map(str, c["para_next_cites"])), c["text"]])
    with open(out / "sources.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "times_cited", "domain", "title", "url", "duplicate_of", "malformed_url"])
        for s in sources:
            d = [x for x in dup[norm_url(s["url"])] if x != s["n"]]
            w.writerow([s["n"], cited.get(s["n"], 0), s["domain"], s["title"], s["url"],
                        " ".join(map(str, d)), "yes" if s["n"] in malformed else ""])
    with open(out / "offset_probe.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(probe[0].keys()) if probe else ["claim_id"])
        w.writeheader(); w.writerows(probe)
    summary = {
        "paragraphs": len({c["para"] for c in claims}),
        "sentences": len(claims),
        "cited_sentences": len(claims) - len(uncited),
        "uncited_sentences": len(uncited),
        "uncited_sentences_no_later_cite_in_paragraph": len(uncited_strict),
        "citation_markers": sum(len(c["cites"]) for c in claims),
        "distinct_numbers_cited": len(cited),
        "sources_listed": len(sources),
        "max_number_cited": max(cited) if cited else 0,
        "dangling_numbers": dangling,
        "dangling_marker_count": sum(cited[n] for n in dangling),
        "claims_with_dangling": [c["claim_id"] for c in claims if any(n not in ns for n in c["cites"])],
        "unused_sources": unused,
        "duplicate_source_urls": dups,
        "malformed_source_urls": malformed,
        "markup_leak_claims": leaks,
    }
    (out / "structure.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items()}, indent=2))


# ----------------------------------------------------------------------------- linkcheck
PAYWALL_HINT = ("jstor.org", "wsj.com", "tandfonline.com", "onlinelibrary.wiley.com", "compass.onlinelibrary.wiley.com",
                "cambridge.org/core", "academic.oup.com", "muse.jhu.edu", "newyorker.com", "jamanetwork.com",
                "ajo.com", "psycnet.apa.org", "read.dukeupress.edu")


def _request(url, method, timeout):
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read(4096) if method == "GET" else b""
        return r.status, r.geturl(), r.headers.get("Content-Type", ""), body


def check_url(url, timeout=20):
    note = ""
    for method in ("HEAD", "GET"):
        try:
            st, final, ctype, body = _request(url, method, timeout)
            return {"status": st, "final_url": final, "content_type": ctype, "method": method, "error": ""}
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (400, 403, 405, 406, 429, 500, 501, 503):
                note = f"HEAD {e.code}"
                continue
            return {"status": e.code, "final_url": url, "content_type": "", "method": method, "error": note}
        except Exception as e:  # DNS, TLS, timeout
            if method == "HEAD":
                note = f"HEAD {type(e).__name__}"
                continue
            return {"status": "", "final_url": url, "content_type": "", "method": method,
                    "error": f"{type(e).__name__}: {e}"[:200]}


def classify_status(st, url):
    paywall = any(p in url for p in PAYWALL_HINT)
    if st == "":
        return "unreachable"
    st = int(st)
    if 200 <= st < 400:
        return "ok" + (" (likely paywalled/abstract-only)" if paywall else "")
    if st in (404, 410):
        return "dead"
    if st in (401, 402, 403, 429, 451) or st >= 500:
        return "blocked/paywall?" if paywall else "blocked-or-error (bot block likely; recheck in browser)"
    return f"http-{st}"


def cmd_linkcheck(args):
    rows = list(csv.DictReader(open(args.sources, encoding="utf-8")))
    last_hit = {}
    out = []
    for r in rows:
        url = r["url"]
        host = urllib.parse.urlsplit(url).netloc
        wait = args.delay - (time.time() - last_hit.get(host, 0))
        if wait > 0:
            time.sleep(wait)
        res = check_url(url, args.timeout)
        last_hit[host] = time.time()
        res.update({"n": r["n"], "url": url, "verdict": classify_status(res["status"], url)})
        out.append(res)
        print(f'{r["n"]:>4} {str(res["status"]):>4} {res["verdict"][:30]:<30} {url[:90]}', flush=True)
        time.sleep(args.global_delay)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["n", "status", "verdict", "method", "content_type", "final_url", "url", "error"])
        w.writeheader(); w.writerows(out)
    print(Counter(o["verdict"] for o in out))


# ----------------------------------------------------------------------------- fetch
class _Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.buf = []; self.skip = 0

    def handle_starttag(self, t, a):
        if t in ("script", "style", "noscript", "svg"): self.skip += 1
        if t in ("p", "br", "div", "li", "h1", "h2", "h3", "h4", "tr"): self.buf.append("\n")

    def handle_endtag(self, t):
        if t in ("script", "style", "noscript", "svg"): self.skip = max(0, self.skip - 1)

    def handle_data(self, d):
        if not self.skip: self.buf.append(d)


def html_to_text(h):
    p = _Text(); p.feed(h)
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", "".join(p.buf))).strip()


def cmd_fetch(args):
    import shutil, subprocess, tempfile
    rows = list(csv.DictReader(open(args.sources, encoding="utf-8")))
    want = set(int(x) for x in args.only.split(",")) if args.only else None
    cache = Path(args.cache); cache.mkdir(parents=True, exist_ok=True)
    for r in rows:
        n = int(r["n"])
        if want and n not in want:
            continue
        dest = cache / f"ref{n:03d}.txt"
        if dest.exists() and dest.stat().st_size > 200:
            continue
        try:
            req = urllib.request.Request(r["url"], headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=args.timeout) as resp:
                data = resp.read(); ctype = resp.headers.get("Content-Type", "")
                if resp.headers.get("Content-Encoding", "") == "gzip" or data[:2] == b"\x1f\x8b":
                    import gzip; data = gzip.decompress(data)
            if data[:4] == b"%PDF" and shutil.which("pdftotext"):
                with tempfile.NamedTemporaryFile(suffix=".pdf") as tf:
                    tf.write(data); tf.flush()
                    txt = subprocess.run(["pdftotext", "-layout", tf.name, "-"], capture_output=True, text=True).stdout
            else:
                txt = html_to_text(data.decode("utf-8", errors="replace"))
            dest.write_text(f"URL: {r['url']}\nCONTENT-TYPE: {ctype}\n\n{txt}", encoding="utf-8")
            print(n, "ok", len(txt))
        except Exception as e:
            dest.with_suffix(".err").write_text(f"{r['url']}\n{type(e).__name__}: {e}", encoding="utf-8")
            print(n, "ERR", type(e).__name__, str(e)[:80])
        time.sleep(args.delay)


# ----------------------------------------------------------------------------- refs
ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5}
PAT_ETHICS = [
    # "Ethics Part II, Proposition 40, Scholium 2" / "Part III, Proposition 6" / "Proposition 7 in Part I"
    (re.compile(r"(?:Ethics\s+)?Part\s+(I{1,3}|IV|V)\b,?\s*(Proposition|Definition|Axiom|Appendix|Preface)s?\s*(\d+)?"
                r"(?:\s*(?:and|,)\s*(\d+))?(?:,?\s*(Scholium|Corollary)\s*(\d+)?)?", re.I), "part_first"),
    (re.compile(r"(Proposition|Definition|Axiom)\s+(\d+)\s+(?:of|in)\s+(?:Ethics\s+)?Part\s+(I{1,3}|IV|V)\b", re.I), "prop_first"),
    (re.compile(r"(Definition|Proposition)\s+(\d+)\s+of\s+Ethics\s+Part\s+(I{1,3}|IV|V)\b", re.I), "prop_first"),
    # "Ethics I, Definition 6" / "Ethics I, Proposition 29" / "Ethics I, Appendix" / "Ethics I, p16" / "Ethics II, p2"
    (re.compile(r"Ethics\s+(I{1,3}|IV|V),\s*(Definition|Proposition|Appendix|p)\s*(\d+)?", re.I), "ethics_roman"),
    # "Ethics IIp25", "IIp28", "(IIp35)", "Ethics 2p7", "Ethics 1d4"
    (re.compile(r"\b(?:Ethics\s+)?(I{1,3}|IV|V|[1-5])(p|d|a)(\d+)(s|c)?(\d+)?\b"), "compact"),
]


def _part(x):
    x = x.lower()
    return ROMAN.get(x, int(x) if x.isdigit() else None)


def extract_spinoza_refs(text):
    hits = []
    for pat, kind in PAT_ETHICS:
        for m in pat.finditer(text):
            g = m.groups()
            if kind == "part_first":
                part, typ, num, num2, sub, subn = g
            elif kind == "prop_first":
                typ, num, part = g; num2 = sub = subn = None
            elif kind == "ethics_roman":
                part, typ, num = g; num2 = sub = subn = None
                typ = "Proposition" if typ.lower() == "p" else typ
            else:
                part, t, num, sub, subn = g; num2 = None
                typ = {"p": "Proposition", "d": "Definition", "a": "Axiom"}[t]
                sub = {"s": "Scholium", "c": "Corollary"}.get(sub or "", None)
            P = _part(part)
            if not P:
                continue
            letter = {"proposition": "P", "definition": "D", "axiom": "A", "appendix": "App", "preface": "Pref"}[typ.lower()]
            code = f"E{P}{letter}{num or ''}"
            if sub:
                code += ("S" if sub.lower().startswith("s") else "C") + (subn or "")
            hits.append({"span": m.group(0), "kisner_style": code, "pos": m.start()})
            if num2:
                hits.append({"span": m.group(0), "kisner_style": f"E{P}{letter}{num2}", "pos": m.start()})
    # TP / TTP / Letters
    for m in re.finditer(r"\bTP\s+(\d+)[.:](\d+)(?:[–-](\d+))?|\(TP\s+(\d+)(?:[–-](\d+))?\)", text):
        hits.append({"span": m.group(0), "kisner_style": m.group(0).strip("()"), "pos": m.start()})
    for m in re.finditer(r"\bLetters?\s+(\d+)(?:\s*[–-]\s*(\d+))?", text):
        hits.append({"span": m.group(0), "kisner_style": m.group(0), "pos": m.start()})
    for m in re.finditer(r"\bchapters?\s+(\d+)(?:\s*(?:and|[–-])\s*(\d+))?", text, re.I):
        hits.append({"span": m.group(0), "kisner_style": m.group(0), "pos": m.start()})
    # de-dup overlapping spans
    seen, res = set(), []
    for h in sorted(hits, key=lambda h: h["pos"]):
        key = (h["kisner_style"], h["pos"])
        if key not in seen:
            seen.add(key); res.append(h)
    return res


def extract_quotes(text):
    return [q for q in re.findall(r'[“"]([^”"]{12,})[”"]', text)]


def _norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def best_match(quote, corpus_norm, step=None):
    """Return (ratio, matched_text) of best fuzzy window match of quote in corpus."""
    q = _norm(quote)
    if not q:
        return 0.0, ""
    if q in corpus_norm:
        return 1.0, q
    words = corpus_norm.split()
    qn = len(q.split())
    qset = set(q.split())
    best = (0.0, "")
    step = step or max(1, qn // 4)
    for i in range(0, max(1, len(words) - qn + 1), step):
        win = words[i:i + qn + 3]
        if len(qset & set(win)) < 0.5 * len(qset):
            continue
        r = difflib.SequenceMatcher(None, q, " ".join(win)).ratio()
        if r > best[0]:
            best = (r, " ".join(win))
    return best


def cmd_refs(args):
    claims = list(csv.DictReader(open(args.claims, encoding="utf-8")))
    corpora = {Path(p).name: _norm(Path(p).read_text(encoding="utf-8", errors="replace")) for p in (args.corpus or [])}
    rows = []
    for c in claims:
        refs = extract_spinoza_refs(c["text"])
        quotes = extract_quotes(c["text"])
        if not refs and not quotes:
            continue
        qres = []
        for q in quotes:
            if corpora:
                scored = sorted(((best_match(q, cn), name) for name, cn in corpora.items()), key=lambda x: -x[0][0])
                (ratio, txt), name = scored[0]
                qres.append(f'"{q}" -> best {ratio:.2f} in {name}: {txt[:120]}')
            else:
                qres.append(f'"{q}"')
        rows.append({"claim_id": c["claim_id"], "section": c["section"], "cites": c["cites"],
                     "work_refs": "; ".join(f'{h["span"]} => {h["kisner_style"]}' for h in refs),
                     "quotes": " || ".join(qres), "text": c["text"]})
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["claim_id", "section", "cites", "work_refs", "quotes", "text"])
        w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} claims with Spinoza work references or quotes -> {args.out}")



# ----------------------------------------------------------------------------- offset (full text)
_STOP = set("the a an of and or in on to for by with from as is are was be his he it its that this which also not but "
            "their they such into than more most through while whose other these those".split())


def _ftoks(s, extra_stop=()):
    return {w for w in re.findall(r"[a-z]{5,}", s.lower()) if w not in _STOP and w not in extra_stop}


def cmd_offset(args):
    """Full-text offset probe: for each citation marker n, share of the claim's content words found in the
    cached text of source n versus source n+k. A real numbering shift shows up as a contiguous range of n
    where n+k wins by a wide margin. Hint only; confirm by reading."""
    rows = list(csv.DictReader(open(args.claims, encoding="utf-8")))
    stop = set(w.lower() for w in (args.stop or "").split(","))
    cache = {}

    def src(n):
        if n not in cache:
            f = Path(args.cache) / f"ref{n:03d}.txt"
            cache[n] = _ftoks(f.read_text(encoding="utf-8", errors="replace"), stop) \
                if f.exists() and f.stat().st_size > 1500 else None
        return cache[n]
    ks = [int(k) for k in args.k.split(",")]
    per = []
    for c in rows:
        ct = _ftoks(c["text"], stop)
        if not ct:
            continue
        for n in map(int, c["cites"].split()):
            rec = {"claim_id": c["claim_id"], "cite": n}
            for k in [0] + ks:
                t = src(n + k) if n + k > 0 else None
                rec[f"ov_k{k:+d}"] = "" if t is None else round(len(ct & t) / len(ct), 2)
            per.append(rec)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(per[0].keys())); w.writeheader(); w.writerows(per)
    width = args.block
    top = max(r["cite"] for r in per)
    print(f"block      n   mean_ov(k=0) " + " ".join(f"mean_ov(k={k:+d}) wins" for k in ks))
    for lo in range(1, top + 1, width):
        hi = lo + width - 1
        B = [r for r in per if lo <= r["cite"] <= hi and r["ov_k+0"] != ""]
        if not B:
            continue
        line = f"{lo:>3}-{hi:<4} {len(B):>4}   {sum(r['ov_k+0'] for r in B)/len(B):.2f}       "
        for k in ks:
            Bk = [r for r in B if r[f"ov_k{k:+d}"] != ""]
            if Bk:
                m = sum(r[f"ov_k{k:+d}"] for r in Bk) / len(Bk)
                wins = sum(1 for r in Bk if r[f"ov_k{k:+d}"] > r["ov_k+0"])
                line += f"   {m:.2f}        {wins}/{len(Bk)}"
        print(line)


# ----------------------------------------------------------------------------- priority / sample
PRIORITY_RE = re.compile(
    r"\b1[5-9]\d\d\b|\b20[0-2]\d\b|[\"“]|Ethics\s+(I|II|III|IV|V|[1-5])\b|Part\s+(I|II|III|IV|V)\b|\b(I{1,3}|IV|V|[1-5])[pd]\d|"
    r"Proposition|Definition|Scholium|Corollary|Appendix|Letters?\s+\d|chapters?\s+\d|\bTP\b|Tractatus|TTP|Emendation|"
    r"cherem|herem|excommunic|\bban\b|banned|published|publication|Opera Posthuma|\bborn\b|\bdied\b|death|buried|interred|"
    r"moved|relocated|Rijnsburg|Voorburg|Hague", re.I)


def cmd_priority(args):
    """Tag priority claims (dates, quotes, work citations, cherem, publication history, places) and draw a
    seeded random sample of the remaining cited claims. Extra name patterns can be added with --names."""
    import random
    rows = list(csv.DictReader(open(args.claims, encoding="utf-8")))
    names = re.compile(args.names, re.I) if args.names else None
    rest = []
    for r in rows:
        pri = bool(PRIORITY_RE.search(r["text"]) or (names and names.search(r["text"])))
        r["priority"] = "P" if pri else ""
        if not pri and r["cites"].strip():
            rest.append(r["claim_id"])
    rnd = random.Random(args.seed)
    sample = set(rnd.sample(rest, min(args.sample, len(rest))))
    for r in rows:
        if r["claim_id"] in sample:
            r["priority"] = "S"
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
    c = Counter(r["priority"] or "-" for r in rows)
    print(f"priority={c['P']} sampled={c['S']} (of {len(rest)} non-priority cited; seed={args.seed}) other={c['-']}")



# ----------------------------------------------------------------------------- evidence
def best_passages(claim, text, win=60, top=1):
    """Slide a window of `win` words over the source text; score = share of the claim's content words present.
    Returns [(score, passage)]. A retrieval aid for the human checker, not a verdict."""
    ct = _ftoks(claim)
    words = text.split()
    if not ct or not words:
        return []
    res = []
    step = max(1, win // 3)
    for i in range(0, max(1, len(words) - win + 1), step):
        seg = " ".join(words[i:i + win])
        sc = len(ct & _ftoks(seg)) / len(ct)
        res.append((sc, seg))
    res.sort(key=lambda x: -x[0])
    return res[:top]


def cmd_evidence(args):
    rows = list(csv.DictReader(open(args.claims, encoding="utf-8")))
    want = set(args.ids.split(",")) if args.ids else None
    shift = {}
    for spec in (args.shift or []):           # e.g. 90-161:-9
        rng, k = spec.split(":"); lo, hi = map(int, rng.split("-"))
        for n in range(lo, hi + 1):
            shift[n] = int(k)
    out = open(args.out, "w", encoding="utf-8") if args.out else sys.stdout
    for r in rows:
        if want and r["claim_id"] not in want:
            continue
        if args.only_priority and r.get("priority", "") not in ("P", "S"):
            continue
        cites = [int(x) for x in r["cites"].split()]
        if not cites:
            continue
        print(f"\n=== {r['claim_id']} [{r['cites']}] {r['text']}", file=out)
        targets = []
        for n in cites:
            targets.append((n, "as-linked"))
            if n in shift:
                targets.append((n + shift[n], f"shifted from {n}"))
        for n, label in targets:
            f = Path(args.cache) / f"ref{n:03d}.txt"
            if not f.exists() or f.stat().st_size < 400:
                print(f"   ref {n} ({label}): no cached text", file=out); continue
            t = re.sub(r"\s+", " ", f.read_text(encoding="utf-8", errors="replace"))
            for sc, seg in best_passages(r["text"], t, win=args.win):
                print(f"   ref {n} ({label}) best={sc:.2f}: …{seg[:args.chars]}…", file=out)


# ----------------------------------------------------------------------------- report
SOFT404_RX = re.compile(r"page not found|404 not found|error 404|not be found|does not exist|"
                        r"making sure you'?re not a bot|just a moment|access denied|enable javascript", re.I)


def cmd_soft404(args):
    from pathlib import Path as _P
    hits = []
    for f in sorted(_P(args.cache).glob("ref*.txt")):
        t = f.read_text(encoding="utf-8", errors="replace")
        head = t[:1500]
        m = SOFT404_RX.search(head)
        if m or len(t) < args.min_len:
            hits.append((f.stem, len(t), m.group(0) if m else f"short<{args.min_len}"))
    for h in hits:
        print(f"{h[0]:>8} len={h[1]:>7} {h[2]}")
    print(f"{len(hits)} suspect cached sources (soft-404 / bot wall / near-empty)")


def cmd_buildlog(args):
    ws = list(csv.DictReader(open(args.worksheet, encoding="utf-8")))
    src = {r["n"]: r for r in csv.DictReader(open(args.sources, encoding="utf-8"))}
    nsrc = len(src)
    ver = {}
    for line in open(args.verdicts, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        parts = line.split("|")
        if len(parts) != 8:
            sys.exit(f"bad verdict line ({len(parts)} fields): {line[:80]}")
        ver[parts[0]] = parts
    missing = [r["claim_id"] for r in ws if r.get("priority") in ("P", "S") and r["claim_id"] not in ver]
    if missing:
        sys.exit(f"priority/sample claims without verdict: {missing}")
    shift = None
    if args.shift:
        a, k = args.shift.split(":"); lo, hi = map(int, a.split("-")); shift = (lo, hi, int(k))
    cols = ["claim_id", "section", "priority", "text", "cites", "linked_source_urls", "intended_sources_if_shifted",
            "dangling_cites", "check_depth", "verdict", "verdict_vs_intended", "reason", "correct_fact",
            "correct_link", "factual_issue"]
    out = []
    for r in ws:
        cites = r["cites"].split()
        linked = [src[c]["url"] for c in cites if c in src]
        intended = []
        if shift:
            for c in cites:
                ci = int(c)
                if shift[0] <= ci <= shift[1] and str(ci + shift[2]) in src:
                    intended.append(f"{c}->{ci + shift[2]}: {src[str(ci + shift[2])]['url']}")
        row = {"claim_id": r["claim_id"], "section": r["section"], "priority": r.get("priority") or "-",
               "text": r["text"], "cites": r["cites"], "linked_source_urls": " ; ".join(linked),
               "intended_sources_if_shifted": " ; ".join(intended), "dangling_cites": r.get("dangling_cites", "")}
        if r["claim_id"] in ver:
            _, depth, v, vi, reason, fact, link, fi = ver[r["claim_id"]]
            row.update(check_depth=depth, verdict=v, verdict_vs_intended=vi, reason=reason,
                       correct_fact=fact, correct_link=link, factual_issue=fi)
        elif not cites:
            nxt = r.get("para_next_cites", "")
            row.update(check_depth="script", verdict="UNCITED", verdict_vs_intended="-",
                       reason=("no citation; a later sentence in the same paragraph cites " + nxt) if nxt
                       else "no citation anywhere later in its paragraph",
                       correct_fact="", correct_link="", factual_issue="")
        else:
            row.update(check_depth="none", verdict="NOT_CHECKED", verdict_vs_intended="-",
                       reason="outside priority set and not in the random sample", correct_fact="",
                       correct_link="", factual_issue="")
        out.append(row)
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
    print(f"wrote {len(out)} rows -> {args.out} ({len(ver)} hand verdicts, {nsrc} sources)")


def cmd_report(args):
    rows = list(csv.DictReader(open(args.log, encoding="utf-8")))
    c = Counter(r["verdict"].strip().upper() for r in rows)
    print(f"rows: {len(rows)}")
    for k in ("SUPPORTED", "MISCITED", "UNSUPPORTED", "UNCITED", "UNVERIFIABLE"):
        print(f"  {k:<13} {c.get(k, 0)}")
    other = {k: v for k, v in c.items() if k not in ("SUPPORTED", "MISCITED", "UNSUPPORTED", "UNCITED", "UNVERIFIABLE")}
    if other:
        print("  other:", other)
    if "NOT_CHECKED" in c:
        pass
    if "verdict_vs_intended" in rows[0]:
        vi = Counter(r["verdict_vs_intended"] for r in rows if r["verdict_vs_intended"] not in ("", "-"))
        print("verdict_vs_intended (shifted cites only):", dict(vi))
    if "factual_issue" in rows[0]:
        print("factual_issue=Y:", sum(r["factual_issue"] == "Y" for r in rows))
    if "priority" in rows[0]:
        print("verdict x priority:", dict(Counter((r["priority"], r["verdict"]) for r in rows)))
    if "check_depth" in rows[0]:
        print("by check_depth:", Counter(r["check_depth"] for r in rows))
        print("verdict x depth:", Counter((r["check_depth"], r["verdict"]) for r in rows))
    if args.json:
        Path(args.json).write_text(json.dumps({"rows": len(rows), "verdicts": dict(c)}, indent=2))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("soft404"); a.add_argument("--cache", default="cache"); a.add_argument("--min-len", type=int, default=400)
    a.set_defaults(fn=cmd_soft404)
    a = sub.add_parser("buildlog"); a.add_argument("worksheet"); a.add_argument("verdicts"); a.add_argument("sources")
    a.add_argument("-o", "--out", default="audit_log.csv"); a.add_argument("--shift", default="", help="e.g. 81-161:-9")
    a.set_defaults(fn=cmd_buildlog)
    a = sub.add_parser("parse"); a.add_argument("html"); a.add_argument("-o", "--out", default="out")
    a.set_defaults(fn=cmd_parse)
    a = sub.add_parser("linkcheck"); a.add_argument("sources"); a.add_argument("-o", "--out", default="linkcheck.csv")
    a.add_argument("--delay", type=float, default=2.0, help="min seconds between hits on the same host")
    a.add_argument("--global-delay", type=float, default=0.5, help="pause after every request")
    a.add_argument("--timeout", type=float, default=20); a.set_defaults(fn=cmd_linkcheck)
    a = sub.add_parser("fetch"); a.add_argument("sources"); a.add_argument("--cache", default="cache")
    a.add_argument("--only", default="", help="comma list of source numbers")
    a.add_argument("--delay", type=float, default=1.5); a.add_argument("--timeout", type=float, default=30)
    a.set_defaults(fn=cmd_fetch)
    a = sub.add_parser("refs"); a.add_argument("claims"); a.add_argument("-o", "--out", default="spinoza_refs.csv")
    a.add_argument("--corpus", nargs="*"); a.set_defaults(fn=cmd_refs)
    a = sub.add_parser("offset"); a.add_argument("claims"); a.add_argument("--cache", default="cache")
    a.add_argument("-o", "--out", default="offset_fulltext.csv"); a.add_argument("--k", default="-9,-1,1")
    a.add_argument("--block", type=int, default=10); a.add_argument("--stop", default="spinoza,baruch,benedict")
    a.set_defaults(fn=cmd_offset)
    a = sub.add_parser("priority"); a.add_argument("claims"); a.add_argument("-o", "--out", default="worksheet.csv")
    a.add_argument("--sample", type=int, default=40); a.add_argument("--seed", type=int, default=1656)
    a.add_argument("--names", default=""); a.set_defaults(fn=cmd_priority)
    a = sub.add_parser("evidence"); a.add_argument("claims"); a.add_argument("--cache", default="cache")
    a.add_argument("--ids", default=""); a.add_argument("--only-priority", action="store_true")
    a.add_argument("--shift", nargs="*", help="e.g. 90-161:-9 also shows source n+k"); a.add_argument("--win", type=int, default=60)
    a.add_argument("--chars", type=int, default=420); a.add_argument("-o", "--out", default="")
    a.set_defaults(fn=cmd_evidence)
    a = sub.add_parser("report"); a.add_argument("log"); a.add_argument("--json"); a.set_defaults(fn=cmd_report)
    args = ap.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
