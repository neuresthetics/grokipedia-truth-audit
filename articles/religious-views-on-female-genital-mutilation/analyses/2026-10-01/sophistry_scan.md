# Sophistry and fallacy scan: Religious views on female genital mutilation

- **Article:** Religious views on female genital mutilation
- **URL:** https://grokipedia.com/page/Religious_views_on_female_genital_mutilation
- **Snapshot file:** `articles/religious-views-on-female-genital-mutilation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 156/156 units read in full (156 paragraphs, 0 table rows).

## Verdict

Run 2 found 2 flags: 0 pro, 0 anti, and 2 neutral. The lean is neutral. Main patterns were F036 Suppressed Evidence (1); F032 Cum Hoc (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug religious-views-on-female-genital-mutilation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5222 |
| Sentences (prose + list items; headings and tables excluded) | 156 |
| Sentences with no citation marker of their own | 40 (26%) |
| Paragraphs/list items with no citation marker at all | 1 of 55 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 108 |
| Distinct citation numbers used in text | 107 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 1: 108 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 4 | 0.8 | honorable (3), leading (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 1 | 0.2 | officially (1) |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 1 | 0.2 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 36 | 6.9 | though (11), while (10), but (7), despite (5), however (3) |
| MOS:WTW synonyms for 'said' | 8 | 1.5 | reveal (5), confirm (3) |
| Hyland 2005 hedges | 53 | 10.1 | rather (21), often (7), indicate (4), typically (4), approximately (3) |
| Hyland 2005 boosters | 14 | 2.7 | certain (3), must (3), known (2), show (2), shows (2) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "The notion that FGM is intrinsically linked to Islam lacks empirical support, as the practice shows higher rates among animist and Christian populations in certain African regions compared to many Muslim-majority areas." | F036 Suppressed Evidence | neutral | Selects counterexamples and leaves out the article's own Burkina Faso data (Muslims about 75% vs Christians 50%) and the lead's note of higher Muslim prevalence. |
| 2 | "Evangelical missions have contributed to FGM's decline in parts of Africa, including through doctrinal prohibitions that emphasize bodily integrity as per New Testament teachings, with historical missionary activities correlating with reduced prevalence in mission-influenced areas." | F032 Cum Hoc | neutral | Infers that missions caused the decline from the correlation stated in the same sentence ('correlating with reduced prevalence'). |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 0, neutral 2. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
