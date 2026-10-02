#!/usr/bin/env python3
"""Build the cross-article summary table for the sophistry scans.

It reads each topics/circumcision/articles/<slug>/analyses/<date>/sophistry_scan.md (flags table),
topics/circumcision/code_counts/sophistry_counts_<date>.json (code counts) and
topics/circumcision/SNAPSHOT_INDEX.md (article order and titles).

Everything in the table is a simple tally of the per-article files. The flags
themselves are judgment calls (see each file). The uncited share is a code
count from sophistry_counts.py.

Usage:
  python3 tools/sophistry_summary.py --date 2026-10-01 [--notes notes.md] [--out FILE]
"""
import argparse, collections, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPIC = ROOT / "topics/circumcision"
ROW = re.compile(r'^\| \d+ \| ".*\| (F\d{3}) ([^|]+?) \| (pro-circumcision|anti-circumcision|neutral/structural) \|')
SHORT = {"pro-circumcision": "pro", "anti-circumcision": "anti", "neutral/structural": "neu"}


def index_rows():
    rows = []
    for line in (TOPIC / "SNAPSHOT_INDEX.md").read_text().splitlines():
        m = re.match(r'^\| (\d+) \| (.+?) \| (https://\S+) \| `([^`]+)` \|', line)
        if m:
            rows.append((int(m.group(1)), m.group(2), m.group(4)))
    return rows


def parse_scan(path):
    flags, fgm = [], False
    for line in path.read_text().splitlines():
        if "mainly about female genital cutting" in line:
            fgm = True
        m = ROW.match(line)
        if m:
            flags.append((m.group(1), m.group(2).strip(), SHORT[m.group(3)]))
    return flags, fgm


def lean(c):
    if not sum(c.values()):
        return "none (0 flags)"
    top = max(c.values())
    winners = [k for k in ("pro", "anti", "neu") if c[k] == top]
    if len(winners) > 1:
        return "mixed (" + "/".join(winners) + " tie)"
    return winners[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--notes")
    ap.add_argument("--out")
    a = ap.parse_args()
    counts = {d["slug"]: d for d in json.loads((TOPIC / f"code_counts/sophistry_counts_{a.date}.json").read_text())}
    out, tot_side, tot_type, names, per = [], collections.Counter(), collections.Counter(), {}, []
    for n, title, slug in index_rows():
        p = TOPIC / f"articles/{slug}/analyses/{a.date}/sophistry_scan.md"
        if not p.exists():
            sys.exit(f"missing scan: {p}")
        flags, fgm = parse_scan(p)
        side = collections.Counter(s for _, _, s in flags)
        typ = collections.Counter(i for i, _, _ in flags)
        for i, nm, _ in flags:
            names[i] = nm
        tot_side.update(side); tot_type.update(typ)
        if typ:
            m = max(typ.values()); tops = sorted(k for k, v in typ.items() if v == m)
            top = "; ".join(f"{k} {names[k]}" for k in tops) + (f" ({m})" if m > 1 else "") + (" (tie)" if len(tops) > 1 else "")
        else:
            top = "n/a"
        c = counts[slug]
        per.append(dict(n=n, title=title, slug=slug, flags=len(flags), side=dict(side), fgm=fgm, top=top,
                        lean=lean(side), uncited=c["sentences_without_own_citation"], sentences=c["sentences"],
                        dangling=len(c["dangling_citation_numbers"])))
    L = []
    L.append("| # | Article | Flags | pro / anti / neu | Top flag type (engine ID, name) | Lean of flags | Uncited sentences (code count) | Dangling cite numbers (code count) |")
    L.append("|---|---|---|---|---|---|---|---|")
    for r in per:
        s = r["side"]
        lean_txt = r["lean"] + (" ‡" if r["fgm"] else "")
        L.append(f"| {r['n']} | [{r['title']}](../../articles/{r['slug']}/analyses/{a.date}/sophistry_scan.md) | {r['flags']} | "
                 f"{s.get('pro',0)} / {s.get('anti',0)} / {s.get('neu',0)} | {r['top']} | {lean_txt} | "
                 f"{r['uncited']}/{r['sentences']} ({100*r['uncited']/r['sentences']:.0f}%) | {r['dangling']} |")
    total = sum(r["flags"] for r in per)
    fl = [r["flags"] for r in per]
    agg = [f"- Articles: {len(per)}. Flags in total: {total} (pro {tot_side['pro']}, anti {tot_side['anti']}, neu {tot_side['neu']}).",
           f"- Flags per article: min {min(fl)}, max {max(fl)}, median {sorted(fl)[len(fl)//2]}. Articles with zero flags: {sum(1 for x in fl if x == 0)}.",
           f"- Articles by lean of their flags: pro {sum(1 for r in per if r['lean']=='pro')}, anti {sum(1 for r in per if r['lean']=='anti')}, neu {sum(1 for r in per if r['lean']=='neu')}, mixed/tie {sum(1 for r in per if r['lean'].startswith('mixed'))}, none {sum(1 for r in per if r['flags']==0)}.",
           f"- Uncited sentences across all 58 articles (code count): {sum(r['uncited'] for r in per)} of {sum(r['sentences'] for r in per)} ({100*sum(r['uncited'] for r in per)/sum(r['sentences'] for r in per):.0f}%).",
           "- Most used flag types: " + ", ".join(f"{k} {names[k]} ({v})" for k, v in tot_type.most_common(8)) + "."]
    srt = sorted(per, key=lambda r: (-r["flags"], r["n"]))
    cut = srt[4]["flags"]
    top5 = [r for r in srt if r["flags"] >= cut]
    agg.append(f"- Most-flagged articles (top 5, including ties at {cut}): " + ", ".join(f"{r['title']} ({r['flags']})" for r in top5) + ".")
    for grp, lab in ((False, "articles not marked ‡ (male circumcision and related)"), (True, "‡ articles (female genital cutting)")):
        g = collections.Counter()
        for r in per:
            if r["fgm"] == grp:
                g.update(r["side"])
        agg.append(f"- Side split, {lab}: pro {g['pro']}, anti {g['anti']}, neu {g['neu']}.")
    text = (f"# Sophistry scan summary: 58 circumcision-related Grokipedia articles ({a.date})\n\n"
            f"Generated by `python3 tools/sophistry_summary.py --date {a.date}` from the per-article `sophistry_scan.md` files and "
            f"`topics/circumcision/code_counts/sophistry_counts_{a.date}.json`. Method: substance_lens v0.5.9 `fallacyScanPass` (67 kept geometric_fallacy_engine entries), both-sides. "
            "**Flags are judgment calls** (a model reading each sentence against the engine entry's detection cue), not measurements. Uncited and dangling counts are code counts from `tools/sophistry_counts.py`.\n\n"
            "## Per-article table\n\n"
            "Lean is the side with the most flags in that article (ties shown as mixed). ‡ = article mainly about female genital cutting: there 'pro' means the flag's reasoning makes cutting look more benign or acceptable, or supports the male/female distinction, and 'anti' means it makes cutting look worse. "
            "Flag counts depend on article length and on how much of the article was read (lead plus a cue-scored subset; see each file), so they are not comparable as rates.\n\n"
            + "\n".join(L) + "\n\n## Totals (simple tallies)\n\n" + "\n".join(agg) + "\n")
    if a.notes:
        text += "\n" + Path(a.notes).read_text()
    if a.out:
        Path(a.out).write_text(text)
    else:
        sys.stdout.write(text)
    json.dump(per, sys.stderr if not a.out else open(TOPIC / f"runs/{a.date}_run1_partial/sophistry_summary_{a.date}.json", "w"), indent=1)


if __name__ == "__main__":
    main()
