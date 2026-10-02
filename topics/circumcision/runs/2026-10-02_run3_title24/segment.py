"""Split a 2026-10-01 snapshot into readable units (prose sentences, table rows, headings).

Shared by verify_quotes.py, make_coverage.py and compare.py so that both runs are mapped
onto the same sentence ids. Snapshots are read from the topic folder (two levels up from here:
topics/circumcision/articles/).
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]  # topics/circumcision
ARTICLES = TOPIC / "articles"
SNAP = "snapshots/2026-10-01.txt"

TITLE24 = [
    "circumcision", "circumcision-and-hiv", "circumcision-and-law", "circumcision-controversies",
    "circumcision-controversy-in-early-christianity", "circumcision-in-africa", "circumcision-in-brunei",
    "circumcision-in-china", "circumcision-in-the-bible", "circumcision-of-jesus",
    "circumcision-surgical-procedure", "cost-of-circumcision-surgery-in-chaozhou",
    "cultural-views-on-circumcision-aesthetics", "ethics-of-circumcision",
    "feast-of-the-circumcision-of-christ", "forced-circumcision",
    "forced-circumcision-of-minors-in-south-korea", "history-of-circumcision", "khitan-circumcision",
    "prevalence-of-circumcision", "prohibition-of-female-circumcision-act-1985",
    "religion-and-circumcision", "stapler-circumcision", "views-on-circumcision",
]

ABBREV = {"e.g.", "i.e.", "etc.", "vs.", "v.", "c.", "ca.", "cf.", "Dr.", "Mr.", "Mrs.", "Ms.", "St.",
          "No.", "Vol.", "pp.", "p.", "al.", "approx.", "Jr.", "Sr.", "Inc.", "Co.", "Fig.", "U.S.",
          "U.K.", "Gen.", "Rev.", "Lk.", "Gal.", "Rom.", "Gen", "Prof.", "Mt.", "Ex.", "Lev.", "Deut.",
          "Josh.", "Acts.", "Col.", "Phil.", "Jn.", "Mk.", "Matt.", "B.C.", "A.D.", "B.C.E.", "C.E."}

# candidate boundary: terminal punctuation, optional closing quote/bracket, optional citation
# markers like " [3] [4]", then whitespace, then something that can start a sentence.
BOUND = re.compile(r'[.!?]["\u201d\u2019)]?((?:\s*\[\d+\])*)\s+(?=["\u201c\u2018(\[]?[A-Z0-9])')


def body_lines(text):
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.startswith("=" * 20):
            return lines[i + 1:], i + 1
    return lines, 0


def split_sentences(par):
    out, start = [], 0
    for m in BOUND.finditer(par):
        end = m.end(1) if m.group(1) else m.start() + 1
        # extend over closing quote/bracket
        while end < len(par) and par[end] in '"\u201d\u2019)':
            end += 1
        cand = par[start:end].strip()
        last = cand.split()[-1] if cand.split() else ""
        last_core = re.sub(r"(\s*\[\d+\])+$", "", cand).split()[-1] if cand else ""
        if last_core in ABBREV or re.fullmatch(r"[A-Z]\.", last_core or ""):
            continue
        if cand:
            out.append(cand)
        start = end
    tail = par[start:].strip()
    if tail:
        out.append(tail)
    return out


def units(slug):
    """Return list of dicts: id, kind (sentence|row|heading), line, text."""
    text = (ARTICLES / slug / SNAP).read_text(encoding="utf-8")
    lines, offset = body_lines(text)
    res = []
    for j, ln in enumerate(lines):
        s = ln.strip()
        if not s:
            continue
        lineno = offset + j + 1
        if s.startswith("#"):
            res.append({"kind": "heading", "line": lineno, "text": s})
        elif " | " in s:
            res.append({"kind": "row", "line": lineno, "text": s})
        else:
            for sent in split_sentences(s):
                res.append({"kind": "sentence", "line": lineno, "text": sent})
    for k, u in enumerate(res):
        u["id"] = f"{slug}#{k:04d}"
    return res


def norm(s):
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip()


def locate(slug, quote, us=None):
    """Return the ids of the sentence/row units that a quote falls in.

    exact=True when the quote occurs verbatim (after whitespace normalisation only) in one unit
    or across consecutive units of the same line."""
    us = us if us is not None else units(slug)
    q = re.sub(r"\s+", " ", quote).strip()
    hits = [u["id"] for u in us if u["kind"] != "heading" and q in re.sub(r"\s+", " ", u["text"])]
    if hits:
        return hits, "exact"
    # spanning several units on the same line
    by_line = {}
    for u in us:
        by_line.setdefault(u["line"], []).append(u)
    for ln, group in by_line.items():
        joined, spans, pos = "", [], 0
        for u in group:
            t = re.sub(r"\s+", " ", u["text"])
            if joined:
                joined += " "
            spans.append((len(joined), len(joined) + len(t), u["id"]))
            joined += t
        i = joined.find(q)
        if i >= 0:
            j = i + len(q)
            return [sid for a, b, sid in spans if a < j and b > i], "exact-span"
    nq = norm(q)
    hits = [u["id"] for u in us if u["kind"] != "heading" and nq in norm(u["text"])]
    if hits:
        return hits, "normalised"
    return [], "missing"
