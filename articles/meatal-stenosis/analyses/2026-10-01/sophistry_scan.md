# Sophistry and fallacy scan: Meatal stenosis

- **Article:** Meatal stenosis
- **URL:** https://grokipedia.com/page/Meatal_stenosis
- **Snapshot file:** `articles/meatal-stenosis/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 130/130 units read in full (130 paragraphs, 0 table rows).

## Verdict

Run 2 found 2 flags: 0 pro, 2 anti, and 0 neutral. The lean is anti. Main patterns were F032 Cum Hoc (1); F036 Suppressed Evidence (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug meatal-stenosis` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 3940 |
| Sentences (prose + list items; headings and tables excluded) | 130 |
| Sentences with no citation marker of their own | 16 (12%) |
| Paragraphs/list items with no citation marker at all | 0 of 43 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 60 |
| Distinct citation numbers used in text | 58 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 2: 59–60 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.3 | leading (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.3 | purported (1) |
| MOS:WTW editorializing | 1 | 0.3 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 36 | 9.1 | though (16), but (8), while (7), however (5) |
| MOS:WTW synonyms for 'said' | 5 | 1.3 | note (2), confirm (1), expose (1), observe (1) |
| Hyland 2005 hedges | 80 | 20.3 | may (16), often (13), typically (13), rather (11), approximately (4) |
| Hyland 2005 boosters | 10 | 2.5 | found (3), established (2), demonstrate (1), demonstrated (1), must (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "The condition is exceptionally rare in uncircumcised males, highlighting the causal role of surgical denudation of the prepuce in exposing vulnerable tissue to environmental irritants." | F032 Cum Hoc | anti | Infers causation from a correlation. The article's own 2017 meta-analysis found no significant difference between circumcised and uncircumcised rates. |
| 2 | "Refraining from neonatal circumcision substantially reduces the risk, as the condition is rare in uncircumcised males and occurs in approximately 5-10% of circumcised boys, often due to post-procedural meatal exposure to urine-soaked diapers and resultant chemical irritation." | F036 Suppressed Evidence | anti | A flat preventive claim that leaves out the article's own meta-analytic evidence of no significant difference (0.66% vs 0.92%). |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 2, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
