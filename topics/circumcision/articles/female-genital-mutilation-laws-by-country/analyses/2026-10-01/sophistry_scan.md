# Sophistry and fallacy scan: Female genital mutilation laws by country

- **Article:** Female genital mutilation laws by country
- **URL:** https://grokipedia.com/page/Female_genital_mutilation_laws_by_country
- **Snapshot file:** `articles/female-genital-mutilation-laws-by-country/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 283/283 units read in full (249 paragraphs, 34 table rows).

## Verdict

Run 2 found 3 flags: 0 pro, 3 anti, and 0 neutral. The lean is anti. Main patterns were F031 Post Hoc (2); F034 False Cause (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-laws-by-country` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 8547 |
| Sentences (prose + list items; headings and tables excluded) | 243 |
| Sentences with no citation marker of their own | 71 (29%) |
| Paragraphs/list items with no citation marker at all | 3 of 77 |
| Table rows (not counted as sentences) | 34 |
| Sources listed in sources CSV | 155 |
| Distinct citation numbers used in text | 155 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 4 | 0.5 | landmark (2), leading (1), pioneering (1) |
| MOS:WTW contentious labels | 1 | 0.1 | controversial (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 6 | 0.7 | only (6) |
| MOS:WTW connectives (but/despite/however...) | 92 | 10.8 | but (30), though (21), despite (19), while (17), however (4) |
| MOS:WTW synonyms for 'said' | 1 | 0.1 | confirm (1) |
| Hyland 2005 hedges | 80 | 9.4 | often (26), rather (12), indicate (6), may (6), estimated (5) |
| Hyland 2005 boosters | 22 | 2.6 | certain (5), show (5), known (3), established (2), found (2) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Universalist frameworks have driven binding instruments like the 2003 Maputo Protocol (African Union, 55 signatories), mandating bans while incorporating community sensitization, yielding prevalence drops (e.g., 25% reduction in Kenya from 1998-2014 per DHS surveys)." | F031 Post Hoc | anti | Credits universalist instruments (the 2003 Maputo Protocol) with a Kenyan decline spanning 1998-2014, based on timing alone. The article elsewhere says causal evidence on laws is scarce. |
| 2 | "Academic relativism, while highlighting implementation pitfalls like elite hypocrisy in urban-rural divides, is countered by evidence that sustained universalist pressure correlates with attitude shifts, as in Burkina Faso's 92% support for bans by 2010 surveys post-2005 laws." | F031 Post Hoc | anti | Survey support measured after a law is offered as evidence that universalist pressure works, based on timing alone. |
| 3 | "From 2020 to 2025, global FGM cases rose 15% to over 230 million, partly fueled by medicalized forms in urbanizing areas, underscoring how professional involvement legitimizes the practice rather than eroding it, as confirmed by WHO and UNICEF analyses rejecting "safer" variants." | F034 False Cause | anti | Attributes the rise in survivor counts to medicalization without support, then uses it to show that medical involvement 'legitimizes' the practice. Population growth, the obvious alternative, is not considered. |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 3, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
