# Sophistry and fallacy scan: Mohel

- **Article:** Mohel
- **URL:** https://grokipedia.com/page/Mohel
- **Snapshot file:** `articles/mohel/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 181/181 units read in full (181 paragraphs, 0 table rows).

## Verdict

Run 2 found 4 flags: 4 pro, 0 anti, and 0 neutral. The lean is pro. Main patterns were F032 Cum Hoc (1); F040 Loaded Language (1); F003 Red Herring (1); F001 Ad Hominem (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug mohel` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6477 |
| Sentences (prose + list items; headings and tables excluded) | 181 |
| Sentences with no citation marker of their own | 51 (28%) |
| Paragraphs/list items with no citation marker at all | 4 of 59 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 126 |
| Distinct citation numbers used in text | 126 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.3 | notable (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 2 | 0.3 | only (2) |
| MOS:WTW connectives (but/despite/however...) | 57 | 8.8 | while (19), but (17), though (15), despite (4), although (1) |
| MOS:WTW synonyms for 'said' | 5 | 0.8 | expose (3), confirm (1), note (1) |
| Hyland 2005 hedges | 73 | 11.3 | often (15), may (10), typically (10), approximately (5), rather (4) |
| Hyland 2005 boosters | 15 | 2.3 | must (6), certain (2), demonstrated (2), known (2), demonstrate (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Systematic reviews of these trials and observational data affirm the mechanism involves keratinization of the glans and reduced viral entry sites under the foreskin, conferring lifelong protection when performed neonatally, as evidenced by lower HIV prevalence in circumcised populations." | F032 Cum Hoc | pro | Takes population-level correlation as proof of lifelong neonatal protection, an extrapolation from adult RCTs. |
| 2 | "News media coverage of mohels predominantly focuses on controversies surrounding brit milah, particularly rare health risks from metzitzah b'peh (direct oral suction), amplifying isolated incidents like neonatal herpes cases in New York City between 2000 and 2012, which involved a small number of ultra-Orthodox practitioners." | F040 Loaded Language | pro | Calls cases 'isolated incidents' and coverage 'amplifying', although the article itself reports 24 cases with deaths and a 3.4-fold excess rate. |
| 3 | "Broader societal views, influenced by secular ethics and medical skepticism, often conflate mohels with infant genital alteration debates, viewing brit milah as unnecessary or harmful despite data showing complication rates under 1% for trained practitioners." | F003 Red Herring | pro | Answers the 'unnecessary' objection with complication rates, which do not address it. |
| 4 | "Mainstream portrayals tend to prioritize autonomy arguments against non-consensual procedures, reflecting institutional biases toward secular norms, while underrepresenting the ritual's centrality to Jewish continuity amid declining circumcision rates among non-religious U.S. Jews (from 90% in the 1970s to about 70% by 2020)." | F001 Ad Hominem | pro | Dismisses autonomy-based portrayals by pointing to the alleged bias of their sources instead of their arguments. |

## Both-sides balance note

Run 2 flag counts by side: pro 4, anti 0, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
