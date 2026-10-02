# Sophistry and fallacy scan: Prevalence of female genital mutilation

- **Article:** Prevalence of female genital mutilation
- **URL:** https://grokipedia.com/page/Prevalence_of_female_genital_mutilation
- **Snapshot file:** `topics/circumcision/articles/prevalence-of-female-genital-mutilation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 204/204 units read in full (199 paragraphs, 5 table rows).

## Verdict

Run 2 found 4 flags: 0 pro, 1 anti, and 3 neutral. The lean is neutral. Main patterns were F032 Cum Hoc (3); F031 Post Hoc (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug prevalence-of-female-genital-mutilation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6257 |
| Sentences (prose + list items; headings and tables excluded) | 198 |
| Sentences with no citation marker of their own | 36 (18%) |
| Paragraphs/list items with no citation marker at all | 0 of 66 |
| Table rows (not counted as sentences) | 5 |
| Sources listed in sources CSV | 129 |
| Distinct citation numbers used in text | 128 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 1: 129 |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.5 | honorable (1), leading (1), notable (1) |
| MOS:WTW contentious labels | 1 | 0.2 | sect (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | apparent (1) |
| MOS:WTW editorializing | 5 | 0.8 | only (5) |
| MOS:WTW connectives (but/despite/however...) | 77 | 12.3 | though (23), despite (19), while (17), but (14), however (4) |
| MOS:WTW synonyms for 'said' | 6 | 1.0 | confirm (3), claim (1), deny (1), note (1) |
| Hyland 2005 hedges | 100 | 16.0 | often (21), approximately (13), indicate (12), estimated (9), rather (9) |
| Hyland 2005 boosters | 18 | 2.9 | certain (6), found (4), show (4), known (2), shown (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "Empirical data from repeated cross-sectional surveys underscore that while absolute numbers grow with demographics, targeted interventions have reduced type III procedures (infibulation) in some cohorts, highlighting causal links between education, legal enforcement, and attitude shifts over blanket prohibitions." | F032 Cum Hoc | neutral | Repeated cross-sectional surveys are said to establish 'causal links'. |
| 2 | "Shia Islam, by contrast, lacks such hadith endorsements and explicitly rejects FGM, with negligible prevalence in Shia-dominant regions like Iran (under 1% nationally, though pockets exist in Sunni-influenced provinces), highlighting doctrinal variance as a causal factor in distribution." | F032 Cum Hoc | neutral | Infers that doctrine causes the distribution from a Shia/Sunni correlation. The article itself later notes Shia Ismaili (Bohra) practice. |
| 3 | "This fusion underscores how religious frameworks have causally entrenched the rite, countering claims of pure cultural autonomy." | F032 Cum Hoc | neutral | Prevalence differences by religion are presented as proof of religious causation, with confounders such as ethnicity and region ignored. |
| 4 | "Recent declines in younger cohorts underscore campaign impacts, with under-15 prevalence below 5% in Uganda and Rwanda due to community-led initiatives, religious leader involvement, and enforcement of anti-FGM laws, though adult women retain higher legacy rates from prior generations." | F031 Post Hoc | anti | Credits campaigns with low youth prevalence in countries the article describes as having been below 1% for over 30 years (Uganda) or negligible (Rwanda). |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 1, neutral 3. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
