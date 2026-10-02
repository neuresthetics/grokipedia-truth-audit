> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: International Day of Zero Tolerance for Female Genital Mutilation

- **Article:** International Day of Zero Tolerance for Female Genital Mutilation
- **URL:** https://grokipedia.com/page/International_Day_of_Zero_Tolerance_for_Female_Genital_Mutilation
- **Snapshot file:** `articles/international-day-of-zero-tolerance-for-female-genital-mutilation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 185 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This article on a UN observance is largely descriptive. It includes a 'Criticisms of Zero-Tolerance' section (175-179) and says that intervention evidence is weak (4, 172). Two flags were found. In the article's voice, the closing sentence calls the zero-tolerance stance 'ideological absolutism' and draws a policy conclusion from data discrepancies. In the cultural-relativism passage, the claim about social benefits (marriage prospects) is answered with health data. Extraction artifacts ('00542-9/fulltext)') are embedded in sentences 100 and 102. Lean: 1 pro-cutting (pro-harm-reduction), 1 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug international-day-of-zero-tolerance-for-female-genital-mutilation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6395 |
| Sentences (prose + list items; headings and tables excluded) | 191 |
| Sentences with no citation marker of their own | 18 (9%) |
| Paragraphs/list items with no citation marker at all | 0 of 67 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 97 |
| Distinct citation numbers used in text | 97 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.3 | leading (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 3 | 0.5 | only (3) |
| MOS:WTW connectives (but/despite/however...) | 59 | 9.2 | though (19), while (17), but (10), despite (9), however (4) |
| MOS:WTW synonyms for 'said' | 3 | 0.5 | assert (1), note (1), reveal (1) |
| Hyland 2005 hedges | 64 | 10.0 | often (20), rather (7), typically (6), about (4), estimated (4) |
| Hyland 2005 boosters | 20 | 3.1 | certain (4), established (4), found (3), known (2), show (2) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Despite global commitments like SDG 5.3 targeting elimination by 2030, discrepancies in prevalence data—due to self-reporting biases and varying definitions—fuel skepticism about progress metrics, underscoring the need for culturally attuned, evidence-based hybrids over ideological absolutism. [97]" | F040 Loaded Language | pro-circumcision | Article voice: data discrepancies are said to underscore 'the need for culturally attuned, evidence-based hybrids over ideological absolutism'. A pejorative label is applied to the zero-tolerance position, and a policy preference is drawn from a point about measurement. The 'absolutist' label convention is applied as elsewhere in this audit. (sentence 191) |
| 2 | "Further debate involves cultural relativism, where some anthropologists contend that universal condemnation ignores contextual benefits communities attribute to FGM, such as enhanced marriage prospects, potentially alienating participants from reform efforts; however, empirical data consistently affirm no health benefits and severe long-term harms like obstetric fistula and psychological trauma. [95] [96]" | F003 Red Herring | anti-circumcision | Anthropologists' point concerns 'contextual benefits communities attribute', specifically 'enhanced marriage prospects'. The reply ('empirical data consistently affirm no health benefits') addresses health, a different claim, and does not engage the social-benefit claim. (sentence 189) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 1.

## Both-sides balance note

Same-standard check: critics of zero tolerance (175-179, 186-188) are given space and attributed. The article does not overstate intervention effects (172: 'weak causal inferences'), so the evidence standard is applied to the anti-FGM side's own programs. Harm sentences (85-102) are cited.

## What wasn't checked

- Sentences outside the reading set (140 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Extraction artifacts in sentences 100 and 102 mean the cited source behind them could not be identified.
