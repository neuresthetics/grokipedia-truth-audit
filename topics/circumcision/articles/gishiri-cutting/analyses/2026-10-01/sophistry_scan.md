# Sophistry and fallacy scan: Gishiri cutting

- **Article:** Gishiri cutting
- **URL:** https://grokipedia.com/page/Gishiri_cutting
- **Snapshot file:** `topics/circumcision/articles/gishiri-cutting/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 147/147 units read in full (147 paragraphs, 0 table rows).

## Verdict

Run 2 found 1 flag: 0 pro, 1 anti, and 0 neutral. The lean is anti. Main patterns were F011 Hasty Generalization (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug gishiri-cutting` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4972 |
| Sentences (prose + list items; headings and tables excluded) | 147 |
| Sentences with no citation marker of their own | 10 (7%) |
| Paragraphs/list items with no citation marker at all | 0 of 55 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 58 |
| Distinct citation numbers used in text | 58 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | notable (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 3 | 0.6 | purported (2), supposed (1) |
| MOS:WTW editorializing | 1 | 0.2 | notably (1) |
| MOS:WTW connectives (but/despite/however...) | 29 | 5.8 | though (12), but (8), despite (5), while (3), however (1) |
| MOS:WTW synonyms for 'said' | 4 | 0.8 | assert (1), claim (1), expose (1), reveal (1) |
| Hyland 2005 hedges | 71 | 14.3 | often (20), rather (13), typically (9), approximately (4), claims (4) |
| Hyland 2005 boosters | 12 | 2.4 | known (4), believed (3), certain (1), demonstrate (1), demonstrated (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Absence of efficacy is further inferred from fistula repair success rates, where gishiri-induced lesions require surgical correction without prior functional gains." | F011 Hasty Generalization | anti | Infers that the procedure has no efficacy in general from a sample selected for harm (women presenting with fistulas). |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 1, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
