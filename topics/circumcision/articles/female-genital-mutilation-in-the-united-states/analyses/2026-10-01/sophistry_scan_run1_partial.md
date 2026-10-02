> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Female genital mutilation in the United States

- **Article:** Female genital mutilation in the United States
- **URL:** https://grokipedia.com/page/Female_genital_mutilation_in_the_United_States
- **Snapshot file:** `articles/female-genital-mutilation-in-the-united-states/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 45 of 179 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a legal, demographic and professional-position overview, mostly cited and descriptive. It reports the 2010 AAP 'ritual nick' episode and the backlash against it neutrally. Two flags were found, both in the 'Multicultural Relativism Critiques' section. One is an uncited sentence claiming that a correlation between integration and lower prevalence 'counters relativist tolerance', which does not address the relativist argument. The other answers relativism by asserting that no parental right extends to 'mutilating minors', so the loaded term carries the argument. That section also states a general principle (no consent, no medical necessity, irreversible alteration of a child) without saying whether it applies only to girls; see the balance note. Lean: 0 pro, 1 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-the-united-states` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6380 |
| Sentences (prose + list items; headings and tables excluded) | 187 |
| Sentences with no citation marker of their own | 28 (15%) |
| Paragraphs/list items with no citation marker at all | 1 of 67 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 103 |
| Distinct citation numbers used in text | 103 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | notable (1) |
| MOS:WTW contentious labels | 1 | 0.2 | sect (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 1 | 0.2 | only (1) |
| MOS:WTW connectives (but/despite/however...) | 36 | 5.6 | despite (13), though (9), but (6), while (6), however (2) |
| MOS:WTW synonyms for 'said' | 10 | 1.6 | reveal (6), expose (2), claim (1), clarify (1) |
| Hyland 2005 hedges | 77 | 12.1 | often (10), rather (10), claims (7), approximately (6), estimated (6) |
| Hyland 2005 boosters | 20 | 3.1 | certain (5), show (5), established (3), demonstrate (1), demonstrated (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Empirical data counters relativist tolerance by demonstrating that greater integration into host societies correlates with reduced FGM prevalence and support." | F003 Red Herring | neutral/structural | Uncited (code count). An empirical correlation between integration and reduced FGM is said to 'counter relativist tolerance'. Relativism is a normative claim about the standing of cultural norms; a demographic trend does not refute it, so the reply shifts the question. (sentence 151) |
| 2 | "Relativism's claim of cultural equivalence debunks under scrutiny, as no parental "right" extends to mutilating minors, paralleling the historical rejection of other traditions like Chinese foot-binding or Indian sati, which were prohibited despite entrenched rationales of honor and purity. [88] [89]" | F040 Loaded Language | anti-circumcision | 'No parental "right" extends to mutilating minors': the conclusion is built into the loaded description, so the term does the arguing (question-begging). The foot-binding and sati parallels are offered as precedent without the analogy being argued. (sentence 155) |

Flag tally by side (simple count of the table above): anti-circumcision 1; neutral/structural 1.

## Both-sides balance note

Same-standard check: sentences 150 and 156 justify overriding relativist defenses with a stated principle: 'irreversible bodily alteration without the child's agency', 'lacking consent or medical necessity', 'child autonomy and bodily integrity'. The article does not say whether, or why, the principle is limited to girls. Male circumcision is not discussed in the sentences read, so there was nothing to flag. As written, though, the principle's scope is open, which is relevant to the cross-article pattern of different standards for male and female cutting. Relativist and enforcement positions (148, 159-166) are both attributed.

## What wasn't checked

- Sentences outside the reading set (134 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The Nagarwala case history (80, 159) was not checked against sources.
