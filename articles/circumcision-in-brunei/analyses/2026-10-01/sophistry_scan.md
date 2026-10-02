# Sophistry and fallacy scan: Circumcision in Brunei

- **Article:** Circumcision in Brunei
- **URL:** https://grokipedia.com/page/Circumcision_in_Brunei
- **Snapshot file:** `articles/circumcision-in-brunei/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 42/42 units read in full (42 paragraphs, 0 table rows).

## Verdict

Run 2 found 1 flag: 1 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F022 Accident (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug circumcision-in-brunei` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 1070 |
| Sentences (prose + list items; headings and tables excluded) | 42 |
| Sentences with no citation marker of their own | 19 (45%) |
| Paragraphs/list items with no citation marker at all | 3 of 20 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 24 |
| Distinct citation numbers used in text | 21 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 3: 22–24 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.9 | prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 0 | 0.0 | none |
| MOS:WTW connectives (but/despite/however...) | 6 | 5.6 | while (3), though (2), although (1) |
| MOS:WTW synonyms for 'said' | 1 | 0.9 | confirm (1) |
| Hyland 2005 hedges | 6 | 5.6 | approximately (1), estimated (1), indicate (1), mainly (1), often (1) |
| Hyland 2005 boosters | 3 | 2.8 | known (2), true (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "This approach adapts global evidence to Brunei's context, where male circumcision prevalence is estimated at 51.9% due to religious norms, potentially amplifying protective effects against HIV and other sexually transmitted infections." | F022 Accident | pro | VMMC evidence from high-prevalence heterosexual epidemics is applied to Brunei and said to be 'potentially amplifying protective effects'; the general rule is used outside its stated scope. |

## Both-sides balance note

Run 2 flag counts by side: pro 1, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
