# Sophistry and fallacy scan: Infibulation

- **Article:** Infibulation
- **URL:** https://grokipedia.com/page/Infibulation
- **Snapshot file:** `articles/infibulation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (5 sentences) read in full, plus 45 of 182 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This article sets out the cultural defenses (119-127) and the rights and health critiques (128-137) fairly; both are mostly attributed, and the harm evidence is cited. Two flags were found in the sentences read. The male-comparison section says in the article's voice that male circumcision is 'routine and medically endorsed in contexts like the U.S. ... for its net benefits'. Other articles in this set report the AAP and CDC as stopping short of a routine recommendation, and that qualification is missing here. The diaspora section cites cumulative NHS service-access counts as evidence that Type III cases are 'often performed clandestinely by healthcare providers'. Lean: 1 pro, 1 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug infibulation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6294 |
| Sentences (prose + list items; headings and tables excluded) | 187 |
| Sentences with no citation marker of their own | 25 (13%) |
| Paragraphs/list items with no citation marker at all | 0 of 69 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 126 |
| Distinct citation numbers used in text | 126 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | landmark (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 4 | 0.6 | only (3), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 53 | 8.4 | but (15), though (14), while (11), despite (10), however (2) |
| MOS:WTW synonyms for 'said' | 7 | 1.1 | reveal (3), confirm (2), claim (1), insist (1) |
| Hyland 2005 hedges | 72 | 11.4 | rather (15), often (14), typically (8), indicate (5), could (4) |
| Hyland 2005 boosters | 19 | 3.0 | certain (4), show (3), shows (3), believe (1), believed (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "These disparities in procedure, evidence profile, and physiological impact underpin differing societal and legal treatments: male circumcision remains routine and medically endorsed in contexts like the U.S. and religious communities for its net benefits, while infibulation faces universal condemnation and prohibition under international human rights frameworks due to its demonstrable harm without offsetting gains. [92] [93]" | F036 Suppressed Evidence | pro-circumcision | States that male circumcision 'remains routine and medically endorsed in contexts like the U.S. ... for its net benefits'. The qualification reported in other articles in this set (for example, foreskin-man 72, history-of-circumcision 155) is left out: the AAP and CDC say benefits outweigh risks but do not recommend routine universal circumcision. This needs a source check; no verdict is given here. (sentence 143) |
| 2 | "Among diasporas in Europe, medicalized infibulation has emerged as a concerning adaptation, with 2023–2025 evidence documenting persistence in African migrant groups despite legal bans; for instance, UK NHS data recorded 37,615 FGM-affected women and girls accessing services cumulatively through March 2024, including Type III cases often performed clandestinely by healthcare providers to evade detection. [116]" | F034 False Cause | anti-circumcision | NHS data on '37,615 FGM-affected women and girls accessing services' (mostly cut before migration) is offered as evidence for 'Type III cases often performed clandestinely by healthcare providers to evade detection' in Europe. Service-access counts do not show where or by whom the procedures were performed. (sentence 174) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 1.

## Both-sides balance note

Same-standard check: the comparison section (139-144) uses the most severe FGM type, which is appropriate for an article about infibulation. Its claims about male circumcision are, however, stated more firmly than elsewhere in this set ('does not fundamentally alter ... sensory functions', 142, which is cited and contested elsewhere, and 143). Relativist parallels to piercings and tattoos (124) are attributed and answered with severity and benefit data (144). That reply addresses the severity argument but not the consent-parity argument, though in this section the relativist argument is framed around 'selective moral outrage', so the reply is mostly on point.

## What wasn't checked

- Sentences outside the reading set (137 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Middle East: 'Modern instances are negligible' (74, uncited) vs Oman continuing practice (68) was not resolved.
