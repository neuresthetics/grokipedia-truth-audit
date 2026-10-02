> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Female genital mutilation in Sudan

- **Article:** Female genital mutilation in Sudan
- **URL:** https://grokipedia.com/page/female_genital_mutilation_in_sudan
- **Snapshot file:** `articles/female-genital-mutilation-in-sudan/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 45 of 207 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a data-heavy article, largely cited, which describes community motivations and religious arguments on their own terms before testing them. The reasoning flags concern causal attribution about what changes prevalence, not the harm evidence. The lead credits a 'modest decline' to awareness campaigns, while later sections say campaigns had 'limited measurable impact'. The critiques section declares legal bans a failure 'despite widespread implementation', although the article says enforcement is 'negligible' and no national survey has been done since 2014, before the 2020 ban. Universalist positions are labelled 'absolutist mandates'. Lean: 1 pro-cutting, 0 anti, 3 neutral/structural. These are judgment calls.

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

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Prevalence remains near-universal in northern and central regions, such as Northern State (98%) and North Darfur (98%), though lower in western areas like Central Darfur (45%), with urban-rural parity at around 86-87% and a modest decline observed since 2010 due to awareness campaigns. [2] [1]" | F031 Post Hoc | neutral/structural | Attributes 'a modest decline observed since 2010' to 'awareness campaigns'. Sentences 155 and 165 describe minimal decline and limited impact of the campaigns, so the article uses the same data for opposite causal claims. (sentence 3) |
| 2 | "Critiques of anti-FGM strategies in Sudan center on their limited empirical impact, with legal bans failing to substantially reduce prevalence despite widespread implementation." | F010 Appeal to Ignorance | neutral/structural | Uncited (code count). Concludes that legal bans are 'failing to substantially reduce prevalence despite widespread implementation'. Sentence 203 says 'no verified post-ban surveys' exist, the latest national data predate the 2020 ban (94, 155), and sentence 6 calls enforcement 'negligible'. Absence of measurement is treated as evidence of failure. (sentence 201) |
| 3 | "Independent assessments note that while urban awareness increased, rural prevalence stagnated, underscoring causal factors like weak monitoring over ideological persuasion. [17]" | F033 Causal Oversimplification | neutral/structural | From rural stagnation it infers 'causal factors like weak monitoring over ideological persuasion': a single-factor explanation with a loaded label ('ideological') for awareness work. (sentence 158) |
| 4 | "This perception persists despite declining support for severe forms, as evidenced by community-level shifts toward less invasive variants, suggesting that relativist sensitivities to sovereignty may facilitate gradual change more effectively than absolutist mandates, though universalists counter that delays perpetuate non-consensual harms without accountability. [59]" | F040 Loaded Language | pro-circumcision | Universalist prohibition is labelled 'absolutist mandates' in the article's voice, while relativist 'sensitivities' are credited with possibly more effective change. The labelling is the same convention flagged elsewhere in this audit. (sentence 200) |

Flag tally by side (simple count of the table above): neutral/structural 3; pro-circumcision 1.

## Both-sides balance note

Same-standard check: proponents' benefit claims (123) are tested against WHO data (124-126), and their religious arguments (55-57) are paired with reformist Islamic counter-arguments (61); that is balanced handling. The relativist 'hypocrisy' argument about male circumcision (196) is attributed and answered with a universalist position (197-198). No sentence read argues the male/female distinction in the article's voice, so there was nothing to flag on that comparison here.

## What wasn't checked

- Sentences outside the reading set (162 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Medicalization percentages (58%; 72% to 80%) and their definitions were not reconciled with sentence 80 ('full clinical medicalization remains limited').
