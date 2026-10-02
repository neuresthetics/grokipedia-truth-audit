# Sophistry and fallacy scan: Meatal stenosis

- **Article:** Meatal stenosis
- **URL:** https://grokipedia.com/page/Meatal_stenosis
- **Snapshot file:** `articles/meatal-stenosis/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 41 of 124 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This clinical article attributes meatal stenosis mainly to circumcision and gives a petroleum-jelly RCT (65). The incidence reporting is inconsistent across sentences: 5-20% in small cohorts versus below 1% in large database analyses (4), '8% to 20%' (40), '5-10%' (63), and an analysis concluding circumcision 'does not substantially increase the likelihood' (125). Two flags were found, both favoring the anti-circumcision side. The risk-factor sentence quotes only the high-range figures, and the proponents' argument is reported with the article's 'purported' inserted. Separately, sentence 20 says 'doubles the risk (39% vs. 23%)'; that ratio is 1.70, not 2 (simple arithmetic, not a flag). Lean: 0 pro, 2 anti, 0 neutral/structural. These are judgment calls.

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

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "The primary risk factor for meatal stenosis is neonatal or infant circumcision, with reported incidences ranging from 8% to 20% among circumcised males, compared to rare occurrence in uncircumcised individuals. [6] [11]" | F036 Suppressed Evidence | anti-circumcision | Gives 'reported incidences ranging from 8% to 20% among circumcised males' as the primary risk figure. The lead (4) reports large database analyses 'indicating an incidence below 1%' and suggests overestimation in referral samples, but here only the high range is used. (sentence 40) |
| 2 | "Proponents of routine circumcision, citing such aggregated data, argue that meatal stenosis represents a minor and infrequent adverse event, often asymptomatic and manageable, outweighed by purported benefits like reduced urinary tract infections or sexually transmitted diseases in other contexts.30770-7/abstract)" | F040 Loaded Language | anti-circumcision | Uncited (code count). Reporting proponents' argument: '... outweighed by purported benefits like reduced urinary tract infections'. Proponents would not call their own benefits 'purported', so the article's skeptical word is inserted into the attributed position, following the convention used elsewhere in this audit. The sentence also ends in an extraction artifact ('30770-7/abstract)'). (sentence 126) |

Flag tally by side (simple count of the table above): anti-circumcision 2.

## Both-sides balance note

Same-standard check: the article does give the opposing analysis (119, 125) and caveats on causation from both sides (119, 129: 'causation remains correlative'). The asymmetry is in which incidence figure is foregrounded in the risk-factor and prevention sections (40, 63). Prevention advice (63: 'Refraining from neonatal circumcision substantially reduces the risk') follows from the article's own causal framing and was not separately flagged.

## What wasn't checked

- Sentences outside the reading set (83 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The incidence figures (below 1% vs 5-20% vs 8-20% vs 5-10%) were not reconciled with sources.
- Sentence 20's '39% vs. 23%' figures look implausible as incidence rates; this needs a source check. 39/23 = 1.70 (simple arithmetic).
