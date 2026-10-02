# Sophistry and fallacy scan: Female genital mutilation in Sudan

- **Article:** Female genital mutilation in Sudan
- **URL:** https://grokipedia.com/page/female_genital_mutilation_in_sudan
- **Snapshot file:** `articles/female-genital-mutilation-in-sudan/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 215/215 units read in full (215 paragraphs, 0 table rows).

## Verdict

Run 2 found 4 flags: 2 pro, 0 anti, and 2 neutral. The lean is mixed (pro/neutral tie). Main patterns were F042 False Analogy (1); F001 Ad Hominem (1); F011 Hasty Generalization (1); F032 Cum Hoc (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-sudan` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 7621 |
| Sentences (prose + list items; headings and tables excluded) | 215 |
| Sentences with no citation marker of their own | 24 (11%) |
| Paragraphs/list items with no citation marker at all | 0 of 79 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 67 |
| Distinct citation numbers used in text | 67 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 3 | 0.4 | only (3) |
| MOS:WTW connectives (but/despite/however...) | 69 | 9.1 | while (22), despite (16), but (13), though (13), however (4) |
| MOS:WTW synonyms for 'said' | 13 | 1.7 | reveal (5), note (3), assert (2), confirm (2), claim (1) |
| Hyland 2005 hedges | 89 | 11.7 | often (21), rather (15), indicate (9), approximately (8), may (7) |
| Hyland 2005 boosters | 13 | 1.7 | certain (3), found (2), show (2), believed (1), demonstrate (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Sunna is distinguished as a ritualistic procedure akin to male circumcision, often promoted by health advocates and communities as a culturally acceptable substitute to eradicate infibulation while retaining perceived purity benefits." | F042 False Analogy | pro | In the article's own voice, calls Sunna 'akin to male circumcision', though the previous sentence defines it as removal of the clitoral prepuce and/or glans. The analogy downplays it as a substitute. |
| 2 | "International NGOs and media, often institutionally inclined toward highlighting legislative "wins" to sustain funding and narratives, have overstated progress—e.g., touting the 2020 ban as transformative—while downplaying persistent high rates and enforcement voids, potentially reflecting biases that prioritize symbolic victories over rigorous outcome tracking." | F001 Ad Hominem | pro | Discounts anti-FGM organisations' reports by pointing to a funding motive instead of engaging the evidence. |
| 3 | "Such approaches, integrating education with accountability frameworks and indirect economic support via donor-funded trainings, avoid resistance by addressing practitioners' motivations, outperforming bans that drive underground activity; scaling similar incentive-based models, potentially including subsidies for alternative livelihoods, could yield more sustainable reductions than prohibition alone." | F011 Hasty Generalization | neutral | Concludes that incentive models outperform bans from a single pilot that measured pledges, not prevalence. |
| 4 | "Evidence indicates a slow, organic decline in FGM prevalence linked to urbanization and education, with urban rates at 85.5% compared to 87.2% in rural areas, and support for continuation dropping below 24% in Khartoum versus a national average of 41%, driven by greater access to awareness campaigns and professional opportunities." | F032 Cum Hoc | neutral | A 1.7-point cross-sectional urban/rural gap is offered as evidence of a decline over time driven by urbanization. |

## Both-sides balance note

Run 2 flag counts by side: pro 2, anti 0, neutral 2. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../SOPHISTRY_RERUN_2026-10-01/COMPARISON.md).
