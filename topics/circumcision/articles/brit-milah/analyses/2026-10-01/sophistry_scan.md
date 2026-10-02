# Sophistry and fallacy scan: Brit milah

- **Article:** Brit milah
- **URL:** https://grokipedia.com/page/Brit_milah
- **Snapshot file:** `articles/brit-milah/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 289/289 units read in full (283 paragraphs, 6 table rows).

## Verdict

Run 2 found 4 flags: 4 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F040 Loaded Language (2); F011 Hasty Generalization (1); F035 Texas Sharpshooter (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug brit-milah` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 9815 |
| Sentences (prose + list items; headings and tables excluded) | 281 |
| Sentences with no citation marker of their own | 47 (17%) |
| Paragraphs/list items with no citation marker at all | 8 of 94 |
| Table rows (not counted as sentences) | 6 |
| Sources listed in sources CSV | 195 |
| Distinct citation numbers used in text | 195 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 5 | 0.5 | great (1), landmark (1), leading (1), notable (1), unique (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.1 | purported (1) |
| MOS:WTW editorializing | 7 | 0.7 | only (7) |
| MOS:WTW connectives (but/despite/however...) | 89 | 9.1 | but (31), though (25), while (24), despite (7), however (2) |
| MOS:WTW synonyms for 'said' | 7 | 0.7 | insist (3), expose (2), claim (1), observe (1) |
| Hyland 2005 hedges | 97 | 9.9 | often (24), may (11), typically (10), rather (6), approximately (5) |
| Hyland 2005 boosters | 27 | 2.8 | certain (8), must (6), known (4), found (2), true (2) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "The ritual has elicited debates over medical ethics, with empirical evidence indicating neonatal circumcision confers protections against urinary tract infections, penile cancer, and heterosexual HIV transmission, yet it is irreversible and carries risks of bleeding, infection, or improper healing." | F011 Hasty Generalization | pro | HIV protection comes from adult RCTs in high-prevalence settings and is attributed to neonatal circumcision in general. |
| 2 | "While ancient Israelites would not have known this scientifically, the alignment is cited as evidence of practical wisdom in the biblical prescription, making the rite safer in pre-modern conditions without contemporary interventions like vitamin K supplementation." | F035 Texas Sharpshooter | pro | A modern physiological coincidence is fitted after the fact to the ancient eighth-day rule as evidence of its wisdom, with the 'safer' conclusion stated in the article's own voice. |
| 3 | "These positions counter activist claims of net harm by prioritizing randomized and cohort data over anecdotal or ideological critiques, acknowledging procedure safety improves with trained practitioners." | F040 Loaded Language | pro | Dismisses critics as 'anecdotal or ideological', though the critiques reported include consent-based ethical arguments that are not answered by outcome data. |
| 4 | "Overall, while brit milah bolsters resilience in observant enclaves, persistent secular encroachments in Europe risk marginalizing Orthodox communities, prompting some families to relocate to more permissive jurisdictions like the UK or Israel, where the practice enjoys broader societal acceptance." | F040 Loaded Language | pro | Loaded framing ('encroachments') of child-rights regulation in the article's own voice. |

## Both-sides balance note

Run 2 flag counts by side: pro 4, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
