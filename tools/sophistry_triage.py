#!/usr/bin/env python3
"""Reading-triage helper used for the 2026-10-01 sophistry scans. NOT a measurement.

It decides which sentences the reviewer reads closely. Lead section (text before the
first sub-heading) is always shown in full. Body sentences are scored by the number of
argumentative/evaluative cue-word hits (list below, written for this scan, not a published
list) plus 1 if the sentence carries no [n] citation; the top N are shown in article order,
N = min(body sentences, max(25, round(0.33 * body sentences)), cap) with cap = 45.
Sentences not shown were not read closely. Output: numbered sentences, 'c' = has own citation,
'U' = none; citation markers are stripped in the view only.

Usage: python3 tools/sophistry_triage.py --date 2026-10-01 --slug <slug> [--cap 45]
"""
import argparse, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sophistry_counts as sc

CUES = """critic opponent proponent advocate activist intactiv argue argued argues contend dismiss ideolog myth misconception unfounded debunk overstat exaggerat flawed bias methodolog weak robust strong evidence insufficient conclusiv prove proven demonstrat establish clearly undeniab consensus mainstream fringe outweigh benefit harm mutilat barbar primitive right consent autonomy ethic moral should must ought natural tradition superior inferior hygien clean compar equivalen analog akin unlike sensitiv pleasure trauma despite however although yet nonetheless notwithstanding merely mere so-called purported alleged claim assert insist cause leads result because therefore thus hence never always every universal empirical causal confound selection anecdot self-report survey emotional inflammatory sensational propaganda agenda misrepresent cherry imperialism western colonial racist antisemit islamophob abuse violat cruel safe dangerous necessary unnecessary medicaliz justif legitimate valid invalid scientific unscientific pseudo deny denial refute contradict undermin fail lack minimal negligible significant substantial profound devastat irreversib permanent loss damage suffer pain death deaths fatal complication protect prevent reduc risk lower higher increase""".split()
RX = re.compile(r"\b(" + "|".join(re.escape(c) for c in CUES) + r")", re.I)


def view(slug, date, cap=45):
    _, body = sc.read_body(os.path.join(sc.ARTICLES, slug, "snapshots", f"{date}.txt"))
    sents = sc.sentences_of(sc.parse(body))
    first = sents[0]["section"] if sents else ""
    lead = [s for s in sents if s["section"] == first]
    rest = [s for s in sents if s["section"] != first]
    score = lambda s: len(RX.findall(s["text"])) + (0 if s["cites"] else 1)
    n = min(len(rest), max(25, round(0.33 * len(rest))), cap)
    pick = sorted(sorted(rest, key=lambda s: -score(s))[:n], key=lambda s: s["n"])
    return sents, lead, pick


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--cap", type=int, default=45)
    a = ap.parse_args()
    sents, lead, pick = view(a.slug, a.date, a.cap)
    print(f"## {a.slug}: {len(sents)} sentences; lead {len(lead)} shown in full; "
          f"{len(pick)} of {len(sents) - len(lead)} body sentences shown (top cue score)")
    for s in lead + pick:
        t = re.sub(r"\s*\[\d+\]", "", s["text"])
        print(f"{s['n']}{'c' if s['cites'] else 'U'} [{s['section'][:30]}] {t}")


if __name__ == "__main__":
    main()
