# Sophistry and fallacy scan: Phimosis

- **Article:** Phimosis
- **URL:** https://grokipedia.com/page/Phimosis
- **Snapshot file:** `articles/phimosis/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 274/274 units read in full (263 paragraphs, 11 table rows).

## Verdict

Run 2 found 3 flags: 2 pro, 1 anti, and 0 neutral. The lean is pro. Main patterns were F011 Hasty Generalization (1); F036 Suppressed Evidence (1); F034 False Cause (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug phimosis` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 7595 |
| Sentences (prose + list items; headings and tables excluded) | 261 |
| Sentences with no citation marker of their own | 69 (26%) |
| Paragraphs/list items with no citation marker at all | 7 of 76 |
| Table rows (not counted as sentences) | 11 |
| Sources listed in sources CSV | 107 |
| Distinct citation numbers used in text | 107 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 7 | 0.9 | only (5), notably (2) |
| MOS:WTW connectives (but/despite/however...) | 58 | 7.6 | but (22), though (21), while (8), however (4), despite (3) |
| MOS:WTW synonyms for 'said' | 5 | 0.7 | confirm (2), expose (2), explain (1) |
| Hyland 2005 hedges | 140 | 18.4 | often (27), may (23), typically (19), approximately (10), rather (10) |
| Hyland 2005 boosters | 20 | 2.6 | found (4), must (4), true (3), demonstrate (2), shows (2) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "A Danish cohort study of uncircumcised boys under a foreskin-preserving policy found surprisingly high morbidity from phimosis, including adhesions and infections, underscoring risks in regions avoiding routine circumcision." | F011 Hasty Generalization | pro | Generalizes from one Danish cohort to all regions without routine circumcision. |
| 2 | "These variations highlight how cultural and religious practices causally shape phimosis epidemiology, with empirical data from global surveys confirming lower morbidity in circumcising societies." | F036 Suppressed Evidence | pro | Treats the absence of foreskin conditions as 'lower morbidity' and leaves out circumcision's own complications, which the article mentions elsewhere. |
| 3 | "Empirical data indicate that in uncircumcised cohorts, self-resolved or conservatively managed cases predominate, challenging claims of universal medical necessity and highlighting how cultural biases—such as parental expectations of early retraction by age 1 in 66% of surveyed families—drive unnecessary interventions despite evidence of natural resolution." | F034 False Cause | anti | Asserts from a survey of parental expectations that these biases cause unnecessary interventions, without establishing the causal link. |

## Both-sides balance note

Run 2 flag counts by side: pro 2, anti 1, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
