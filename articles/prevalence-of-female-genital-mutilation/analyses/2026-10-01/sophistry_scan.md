# Sophistry and fallacy scan: Prevalence of female genital mutilation

- **Article:** Prevalence of female genital mutilation
- **URL:** https://grokipedia.com/page/Prevalence_of_female_genital_mutilation
- **Snapshot file:** `articles/prevalence-of-female-genital-mutilation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 192 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a survey-methodology and regional-prevalence article. It is careful about measurement limits: self-report bias in both directions (19, 27, 84, 88), validation studies (85), sampling gaps (91), and critics' concerns about how minimal forms affect global estimates (23-24, 28) and about funding incentives (92, attributed). Two neutral/structural flags were found, both moving from repeated or cross-sectional survey correlations to causal conclusions in the article's voice: one in the lead about which interventions work, one about religion having 'causally entrenched' the practice. Lean: 0 pro, 0 anti, 2 neutral/structural. These are judgment calls.

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

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Empirical data from repeated cross-sectional surveys underscore that while absolute numbers grow with demographics, targeted interventions have reduced type III procedures (infibulation) in some cohorts, highlighting causal links between education, legal enforcement, and attitude shifts over blanket prohibitions. [5]" | F032 Cum Hoc | neutral/structural | From 'repeated cross-sectional surveys' it concludes 'causal links between education, legal enforcement, and attitude shifts over blanket prohibitions'. Repeated cross-sections show co-movement, not causation, and the contrast between 'legal enforcement' and 'blanket prohibitions' is not explained. (sentence 6) |
| 2 | "This fusion underscores how religious frameworks have causally entrenched the rite, countering claims of pure cultural autonomy. [39]" | F032 Cum Hoc | neutral/structural | From the correlations in 75 and 79 (Sunni adherence and Islamized groups with higher prevalence), it concludes 'religious frameworks have causally entrenched the rite, countering claims of pure cultural autonomy'. Ethnicity, region and religion are confounded in these comparisons. (sentence 80) |

Flag tally by side (simple count of the table above): neutral/structural 2.

## Both-sides balance note

Same-standard check: both directions of measurement bias are acknowledged: underreporting through stigma and normalization (18, 25, 88) and inflation through inclusive definitions or advocacy incentives (24, 92). That is even-handed. The 'critics' who allege funding incentives (92) are not named, which is an unsupported attribution, but the sentence is attributed and was not counted.

## What wasn't checked

- Sentences outside the reading set (147 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Sentence 134's projections ('trending toward 7-2% by 2030') read as garbled and were not checked.
