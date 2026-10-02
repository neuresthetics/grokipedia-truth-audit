# Sophistry and fallacy scan: Clitoridectomy

- **Article:** Clitoridectomy
- **URL:** https://grokipedia.com/page/Clitoridectomy
- **Snapshot file:** `articles/clitoridectomy/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (7 sentences) read in full, plus 45 of 197 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The article covers both therapeutic clitoridectomy (cancer, clitoromegaly) and FGM Type I. On the cultural practice it is firmly critical, and it reports proponents' stated rationales (hygiene, fidelity, fertility) before answering them with cited evidence, which is sound procedure. The flags all go one way, toward the anti-cutting conclusion. The article uses causal language for observational odds ratios. It attributes evidence about infibulation and FGM generally to Type I. It moves from 'no benefit' to 'discriminatory violence' with no stated value premise. One lead sentence draws a causal conclusion that does not follow from its premise. On the sentences read, all 4 flags favor anti-circumcision (anti-cutting). These are judgment calls; the strong evidence of harm is not in question here, only these inference steps.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug clitoridectomy` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6855 |
| Sentences (prose + list items; headings and tables excluded) | 204 |
| Sentences with no citation marker of their own | 30 (15%) |
| Paragraphs/list items with no citation marker at all | 0 of 66 |
| Table rows (not counted as sentences) | 5 |
| Sources listed in sources CSV | 127 |
| Distinct citation numbers used in text | 127 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.1 | prominent (1) |
| MOS:WTW contentious labels | 1 | 0.1 | controversial (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.3 | purported (2) |
| MOS:WTW editorializing | 1 | 0.1 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 72 | 10.5 | though (23), but (21), while (15), despite (8), however (5) |
| MOS:WTW synonyms for 'said' | 11 | 1.6 | reveal (4), claim (2), confirm (2), find (2), expose (1) |
| Hyland 2005 hedges | 95 | 13.9 | often (24), may (10), indicate (9), rather (9), typically (8) |
| Hyland 2005 boosters | 15 | 2.2 | show (4), certain (2), established (2), find (2), always (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Medicalization by clinicians in some regions has been proposed to mitigate harms but empirically fails to eliminate risks and may normalize the practice, underscoring causal links between the procedure's irreversibility and lifelong physiological and psychological detriment. [10] [4]" | F034 False Cause | anti-circumcision | From 'medicalization ... fails to eliminate risks and may normalize the practice' the sentence concludes 'causal links between the procedure's irreversibility and lifelong ... detriment'. The premise is about medicalization; the causal conclusion about irreversibility does not follow from it. (sentence 7) |
| 2 | "These effects arise causally from acute pain, loss of bodily autonomy, and cultural stigmatization, with severity correlating to procedural invasiveness, though even Type I cases show adjusted odds ratios of 1.5-2.0 for mood disorders relative to non-mutilated peers. [102] [72]" | F032 Cum Hoc | anti-circumcision | 'These effects arise causally from' pain, loss of autonomy and stigma, supported by adjusted odds ratios. That is observational data stated as an established causal pathway, the same step flagged on the pro side in other articles. (sentence 158) |
| 3 | "Prospective studies, including those tracking sexual function in over 1,000 women across Mali and Sierra Leone, find no improvement in obstetric outcomes—infant mortality remains comparable or higher due to infibulation complications—and report diminished clitoral sensation in 70-80% of cases, challenging moderation claims without substantiating fidelity effects. [96]" | F020 Division | anti-circumcision | In an article about Type I, cites outcomes 'due to infibulation complications' (Type III) and FGM-wide figures as evidence against Type I-specific moderation claims. A property of the whole category is assigned to one type. (sentence 149) |
| 4 | "Empirical assessments reveal no evidence of purported benefits like reduced promiscuity, positioning the practice as discriminatory violence rather than neutral tradition. [105] [8]" | F061 Is-Ought Jump | anti-circumcision | From 'no evidence of purported benefits' to 'positioning the practice as discriminatory violence rather than neutral tradition'. The absence of benefit does not by itself yield that classification; the normative premise (e.g., a rights standard, given in sentence 159) is not connected to this conclusion. (sentence 161) |

Flag tally by side (simple count of the table above): anti-circumcision 4.

## Both-sides balance note

Same-standard check: proponents' rationales (sentences 135, 145, 150, 151) are attributed and then answered with cited evidence, and the article notes when evidence is weak even on its own side (203, on reconstruction studies). Pro-practice arguments are not caricatured in the sentences read. The asymmetry is in causal wording: observational harms are described as causal (158, 7), while the pro side's evidence is judged by trial standards (150, 153: 'no randomized or controlled data'). Sentence 130's 'despite lacking endorsement from major religious authorities' is a claim that needs a source check. The comparison with male circumcision raised by practitioners (12) is reported but not examined.

## What wasn't checked

- Sentences outside the reading set (152 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
