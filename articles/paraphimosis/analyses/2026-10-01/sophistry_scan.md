# Sophistry and fallacy scan: Paraphimosis

- **Article:** Paraphimosis
- **URL:** https://grokipedia.com/page/Paraphimosis
- **Snapshot file:** `articles/paraphimosis/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 157/157 units read in full (157 paragraphs, 0 table rows).

## Verdict

Run 2 found 1 flag: 1 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F003 Red Herring (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug paraphimosis` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4249 |
| Sentences (prose + list items; headings and tables excluded) | 157 |
| Sentences with no citation marker of their own | 49 (31%) |
| Paragraphs/list items with no citation marker at all | 0 of 56 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 49 |
| Distinct citation numbers used in text | 45 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 4: 46–49 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.5 | landmark (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 4 | 0.9 | only (3), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 22 | 5.2 | but (11), though (8), while (3) |
| MOS:WTW synonyms for 'said' | 1 | 0.2 | confirm (1) |
| Hyland 2005 hedges | 82 | 19.3 | may (23), typically (10), often (8), should (8), around (6) |
| Hyland 2005 boosters | 5 | 1.2 | must (3), certain (1), clear (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "This procedure serves as a reliable prophylactic strategy, nearly eliminating paraphimosis risk while also offering broader benefits like reduced penile carcinoma incidence, though it is typically reserved for cases where non-surgical options fail." | F003 Red Herring | pro | Brings in an unrelated claimed benefit (penile cancer) while discussing prophylaxis for paraphimosis, which tilts the case toward circumcision. |

## Both-sides balance note

Run 2 flag counts by side: pro 1, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
