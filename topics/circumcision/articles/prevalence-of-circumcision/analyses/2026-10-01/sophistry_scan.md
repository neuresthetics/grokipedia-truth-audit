# Sophistry and fallacy scan: Prevalence of circumcision

- **Article:** Prevalence of circumcision
- **URL:** https://grokipedia.com/page/Prevalence_of_circumcision
- **Snapshot file:** `topics/circumcision/articles/prevalence-of-circumcision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 193/193 units read in full (186 paragraphs, 7 table rows).

## Verdict

Run 2 found 1 flag: 1 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F032 Cum Hoc (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug prevalence-of-circumcision` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5906 |
| Sentences (prose + list items; headings and tables excluded) | 185 |
| Sentences with no citation marker of their own | 58 (31%) |
| Paragraphs/list items with no citation marker at all | 4 of 60 |
| Table rows (not counted as sentences) | 7 |
| Sources listed in sources CSV | 105 |
| Distinct citation numbers used in text | 105 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.5 | celebrated (1), leading (1), notable (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.3 | purported (1), supposed (1) |
| MOS:WTW editorializing | 0 | 0.0 | none |
| MOS:WTW connectives (but/despite/however...) | 51 | 8.6 | though (21), but (11), despite (10), while (6), however (3) |
| MOS:WTW synonyms for 'said' | 3 | 0.5 | confirm (1), observe (1), reveal (1) |
| Hyland 2005 hedges | 115 | 19.5 | rather (20), around (17), approximately (15), often (14), typically (10) |
| Hyland 2005 boosters | 17 | 2.9 | show (7), showed (3), shown (2), shows (2), certain (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Program evaluations confirm population-level HIV incidence declines correlating with VMMC scale-up, independent of confounding factors like antiretroviral therapy expansion." | F032 Cum Hoc | pro | A population-level correlation is presented as causal, with confounding by concurrent ART expansion declared away and no method given for isolating it. |

## Both-sides balance note

Run 2 flag counts by side: pro 1, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
