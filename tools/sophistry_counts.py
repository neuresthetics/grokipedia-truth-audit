#!/usr/bin/env python3
"""Mechanical text counts for Grokipedia snapshot sophistry scans.

Everything here is deterministic string processing. Nothing in this script
judges whether a sentence is fallacious; it only counts things.

For one snapshot (topics/<topic>/articles/<slug>/snapshots/<date>.txt + <date>_sources.csv) it reports:
  - sentence count (prose paragraphs and list items; headings, the metadata
    header and [Table] blocks are excluded; table rows are counted separately)
  - sentences with no in-text citation marker [n] of their own
  - paragraphs with no citation marker anywhere in them
  - dangling citation numbers: [n] used in the text with no row n in the sources CSV
  - sources listed in the CSV but never cited in the text
  - term counts from the published lists in tools/term_lists/ (whole-word,
    case-insensitive; multi-word phrases matched as phrases)

Usage (--topic defaults to circumcision; output defaults to topics/<topic>/code_counts/):
  python3 tools/sophistry_counts.py --date 2026-10-01 --all            # all article folders, writes CSV + JSON
  python3 tools/sophistry_counts.py --date 2026-10-01 --slug foreskin  # one article, prints JSON
  python3 tools/sophistry_counts.py --date 2026-10-01 --slug foreskin --sentences   # numbered sentence list
  python3 tools/sophistry_counts.py --date 2026-10-01 --verify-quotes   # check every flags-table quote in
                                                                         # analyses/<date>/sophistry_scan.md is a
                                                                         # verbatim sentence of the snapshot

Known limits of the sentence splitter: it is a regex splitter with an abbreviation
guard. It can mis-split on unusual abbreviations or initials, and it treats a
citation marker that follows a sentence's full stop as belonging to that sentence.
A citation at the end of a paragraph may be meant to cover earlier sentences;
"uncited sentence" here means only "no [n] marker attached to this sentence".
"""
import argparse, csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
DEFAULT_TOPIC = "circumcision"
ARTICLES = os.path.join(REPO, "topics", DEFAULT_TOPIC, "articles")


def set_topic(topic):
    """Point ARTICLES at topics/<topic>/articles (used by this script and sophistry_triage.py)."""
    global ARTICLES
    ARTICLES = os.path.join(REPO, "topics", topic, "articles")
TERM_FILES = ["wikipedia_mos_words_to_watch.json", "hyland_2005_hedges_boosters.json"]

CITE = re.compile(r"\[(\d+)\]")
ABBREV = ["v.", "Miss.", "e.g.", "i.e.", "etc.", "vs.", "cf.", "approx.", "c.", "ca.", "Dr.", "Mr.", "Mrs.", "Ms.", "St.",
          "Jr.", "Sr.", "No.", "Nos.", "al.", "Fig.", "Vol.", "vol.", "pp.", "p.", "ch.", "Ch.", "Gen.", "Lev.",
          "Exod.", "Deut.", "Rom.", "Gal.", "Col.", "Phil.", "Matt.", "Acts.", "Prof.", "Rev.", "Inc.", "Ltd.",
          "Co.", "U.S.", "U.K.", "U.N.", "A.D.", "B.C.", "B.C.E.", "C.E.", "a.m.", "p.m.", "viz.", "Sect.", "sec.",
          "art.", "Art.", "para.", "s.", "ss.", "Jan.", "Feb.", "Mar.", "Apr.", "Aug.", "Sept.", "Sep.", "Oct.",
          "Nov.", "Dec.", "Mt.", "Ps.", "Prov.", "Isa.", "Jer.", "Ezek.", "Josh.", "Judg.", "Sam.", "Kgs.",
          "Chron.", "Neh.", "Esth.", "Eccl.", "Hos.", "Mic.", "Mk.", "Lk.", "Jn.", "Cor.", "Eph.", "Thess.",
          "Tim.", "Heb.", "Jas.", "Pet.", "Rep.", "Sen.", "Gov.", "Hon.", "Jud.", "et seq.", "Op.", "op.", "ed.",
          "eds.", "trans.", "repr.", "n.d.", "S.A.", "Sh.", "R.", "b.", "d.", "r."]
_PROT = "\u0000"


def load_terms():
    terms = {}
    for fn in TERM_FILES:
        with open(os.path.join(HERE, "term_lists", fn), encoding="utf-8") as f:
            d = json.load(f)
        src = os.path.splitext(fn)[0]
        for k, v in d.get("context_exclusions", {}).items():
            if not k.startswith("_"):
                EXCL[k.lower()] = v
        for cat, words in d["categories"].items():
            terms[f"{src}:{cat}"] = words
    return terms


EXCL = {}


def term_regex(term):
    t = re.escape(term.lower()).replace("\\ ", r"\s+").replace("'", "['\u2019]")
    ex = "".join(r"(?!\s+" + re.escape(w) + r"\b)" for w in EXCL.get(term.lower(), []))
    return re.compile(r"(?<![\w-])" + t + r"(?![\w-])" + ex, re.I)


def read_body(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    head, sep, body = text.partition("=" * 78)
    if not sep:
        body = text
    return head, body


def split_sentences(par):
    s = par
    for a in sorted(ABBREV, key=len, reverse=True):
        s = re.sub(r"(?<![\w.])" + re.escape(a), lambda m: m.group(0).replace(".", _PROT), s)
    # dotted capital runs like "J.R.", "H.R.", "U.S.A."
    s = re.sub(r"(?<![\w.])(?:[A-Z]\.){2,}", lambda m: m.group(0).replace(".", _PROT), s)
    # single capital initials like "J. R. Smith" or "H. pylori"
    s = re.sub(r"(?<![\w.])([A-Z])\.(?=\s+[A-Za-z])", lambda m: m.group(1) + _PROT, s)
    # decimal numbers
    s = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + _PROT + m.group(2), s)
    parts = re.split(r"(?:(?<=[.!?])|(?<=[.!?][\"\u201d')]))\s+(?=[\"\u201c'(]?[A-Z0-9\u00C0-\u024F])"
                     r"|(?:(?<=[.!?])|(?<=[.!?][\"\u201d')]))\s+(?=\[\d+\])", s)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        m = re.match(r"^((?:\[\d+\]\s*)+)(.*)$", p, re.S)
        if m and out:  # leading citation markers belong to the previous sentence
            out[-1] = out[-1] + " " + m.group(1).strip()
            p = m.group(2).strip()
            if not p:
                continue
        out.append(p)
    return [o.replace(_PROT, ".") for o in out]


def parse(body):
    """Return list of blocks: dict(kind=heading|para|list|table, text|rows, section)."""
    blocks, section = [], ""
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("#"):
            section = ln.lstrip("#").strip()
            blocks.append({"kind": "heading", "text": section, "section": section})
            i += 1
            continue
        if ln.strip() == "[Table]":
            rows = []
            i += 1
            while i < len(lines) and lines[i].strip():
                rows.append(lines[i].rstrip())
                i += 1
            blocks.append({"kind": "table", "rows": rows, "section": section})
            continue
        if re.match(r"^\s*[-*\u2022]\s+", ln):
            blocks.append({"kind": "list", "text": re.sub(r"^\s*[-*\u2022]\s+", "", ln), "section": section})
            i += 1
            continue
        blocks.append({"kind": "para", "text": ln.strip(), "section": section})
        i += 1
    return blocks


def sentences_of(blocks):
    sents, pid = [], 0
    for b in blocks:
        if b["kind"] in ("para", "list"):
            pid += 1
            for s in split_sentences(b["text"]):
                sents.append({"para": pid, "section": b["section"], "text": s, "kind": b["kind"]})
    for n, s in enumerate(sents, 1):
        s["n"] = n
        s["cites"] = [int(x) for x in CITE.findall(s["text"])]
    return sents


def load_sources(path):
    refs = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                try:
                    refs.add(int(row["ref_number"]))
                except (KeyError, ValueError):
                    pass
    return refs


def strip_cites(t):
    return re.sub(r"\s*\[\d+\]", "", t)


def counts_for(slug, date, terms=None, compiled=None):
    snap = os.path.join(ARTICLES, slug, "snapshots", f"{date}.txt")
    srcs = os.path.join(ARTICLES, slug, "snapshots", f"{date}_sources.csv")
    head, body = read_body(snap)
    title = re.search(r"^Title:\s*(.+)$", head, re.M)
    url = re.search(r"^Grokipedia URL:\s*(.+)$", head, re.M)
    blocks = parse(body)
    sents = sentences_of(blocks)
    refs = load_sources(srcs)
    # body text cites, including tables
    all_cited = [int(x) for x in CITE.findall(body)]
    table_rows = [r for b in blocks if b["kind"] == "table" for r in b["rows"]]
    paras = {}
    for s in sents:
        paras.setdefault(s["para"], []).append(s)
    uncited = [s for s in sents if not s["cites"]]
    uncited_paras = [p for p, ss in paras.items() if not any(x["cites"] for x in ss)]
    used = sorted(set(all_cited))
    dangling = [n for n in used if n not in refs]
    never_cited = sorted(refs - set(used))
    prose = " ".join(strip_cites(s["text"]) for s in sents)
    words = len(re.findall(r"\b[\w'\u2019-]+\b", prose))
    terms = terms or load_terms()
    compiled = compiled or {k: [(w, term_regex(w)) for w in v] for k, v in terms.items()}
    term_counts = {}
    for cat, pats in compiled.items():
        hits = {}
        for w, rx in pats:
            c = len(rx.findall(prose))
            if c:
                hits[w] = c
        term_counts[cat] = {"total": sum(hits.values()), "per_1000_words": round(1000 * sum(hits.values()) / words, 1) if words else 0.0,
                            "top": sorted(hits.items(), key=lambda kv: (-kv[1], kv[0]))[:8]}
    return {
        "slug": slug, "date": date,
        "title": title.group(1).strip() if title else slug,
        "url": url.group(1).strip() if url else "",
        "words_in_prose": words,
        "paragraphs_and_list_items": len(paras),
        "sentences": len(sents),
        "sentences_without_own_citation": len(uncited),
        "uncited_share": round(len(uncited) / len(sents), 3) if sents else 0.0,
        "paragraphs_without_any_citation": len(uncited_paras),
        "table_rows": len(table_rows),
        "sources_listed": len(refs),
        "distinct_citation_numbers_used": len(used),
        "dangling_citation_numbers": dangling,
        "sources_never_cited": never_cited,
        "terms": term_counts,
    }


def article_slugs():
    return sorted(d for d in os.listdir(ARTICLES) if os.path.isdir(os.path.join(ARTICLES, d)))


def compress(nums):
    if not nums:
        return "none"
    out, start, prev = [], nums[0], nums[0]
    for n in nums[1:] + [None]:
        if n is not None and n == prev + 1:
            prev = n
            continue
        out.append(str(start) if start == prev else f"{start}\u2013{prev}")
        if n is not None:
            start = prev = n
    return ", ".join(out)


def verify_quotes(date):
    """Check that every quoted sentence in a sophistry_scan.md flags table is a verbatim snapshot sentence."""
    bad, total = [], 0
    for slug in article_slugs():
        md = os.path.join(ARTICLES, slug, "analyses", date, "sophistry_scan.md")
        snap = os.path.join(ARTICLES, slug, "snapshots", f"{date}.txt")
        if not (os.path.exists(md) and os.path.exists(snap)):
            continue
        _, body = read_body(snap)
        sents = {s["text"] for s in sentences_of(parse(body))}
        with open(md, encoding="utf-8") as f:
            for ln in f:
                m = re.match(r"^\|\s*(\d+)\s*\|\s*(.+?)\s*\|\s*F\d{3}", ln)
                if not m:
                    continue
                total += 1
                q = m.group(2).strip()
                q = q[1:-1] if q.startswith('"') and q.endswith('"') else q
                q = q.replace("\\|", "|")
                if q not in sents:
                    bad.append((slug, m.group(1), q[:90]))
    return total, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--slug")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--sentences", action="store_true")
    ap.add_argument("--verify-quotes", action="store_true")
    ap.add_argument("--topic", default=DEFAULT_TOPIC, help="topic folder under topics/ (default: circumcision)")
    ap.add_argument("--out", help="output folder for --all (default: topics/<topic>/code_counts)")
    a = ap.parse_args()
    set_topic(a.topic)
    if a.out is None:
        a.out = os.path.join(REPO, "topics", a.topic, "code_counts")
    if a.verify_quotes:
        total, bad = verify_quotes(a.date)
        print(f"quotes checked: {total}; not verbatim snapshot sentences: {len(bad)}")
        for b in bad:
            print("  MISMATCH", *b)
        sys.exit(1 if bad else 0)
    if a.slug and a.sentences:
        _, body = read_body(os.path.join(ARTICLES, a.slug, "snapshots", f"{a.date}.txt"))
        for s in sentences_of(parse(body)):
            print(f"{s['n']}\t{s['para']}\t{s['section']}\t{s['text']}")
        return
    terms = load_terms()
    compiled = {k: [(w, term_regex(w)) for w in v] for k, v in terms.items()}
    slugs = article_slugs() if a.all else [a.slug]
    results = [counts_for(s, a.date, terms, compiled) for s in slugs
               if os.path.exists(os.path.join(ARTICLES, s, "snapshots", f"{a.date}.txt"))]
    if not a.all:
        print(json.dumps(results[0], indent=1))
        return
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, f"sophistry_counts_{a.date}.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    cats = list(terms.keys())
    with open(os.path.join(a.out, f"sophistry_counts_{a.date}.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["slug", "title", "words_in_prose", "sentences", "sentences_without_own_citation", "uncited_share",
                    "paragraphs_without_any_citation", "table_rows", "sources_listed", "dangling_citation_numbers",
                    "sources_never_cited"] + cats)
        for r in results:
            w.writerow([r["slug"], r["title"], r["words_in_prose"], r["sentences"], r["sentences_without_own_citation"],
                        r["uncited_share"], r["paragraphs_without_any_citation"], r["table_rows"], r["sources_listed"],
                        compress(r["dangling_citation_numbers"]), compress(r["sources_never_cited"])] +
                       [r["terms"][c]["total"] for c in cats])
    print(f"wrote {len(results)} rows to {a.out}")


if __name__ == "__main__":
    main()
