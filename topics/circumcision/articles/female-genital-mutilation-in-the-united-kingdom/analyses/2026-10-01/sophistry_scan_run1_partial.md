> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Female genital mutilation in the United Kingdom

- **Article:** Female genital mutilation in the United Kingdom
- **URL:** https://grokipedia.com/page/female_genital_mutilation_in_the_united_kingdom
- **Snapshot file:** `articles/female-genital-mutilation-in-the-united-kingdom/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 45 of 160 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is mainly a legal, statistical and safeguarding description. Most legal-history sentences carry no citation of their own (see code counts), but the claims are mostly descriptive. The three flags found are all neutral/structural, in the 'Evolution of Criminal Law' section, and written in the article's voice. Law reform is said to be 'driven by evidence of rising prevalence' when the evidence given is counts of hospital visits, which reflect identification and could equally show rising awareness. The section asserts 'causal links' between lax enforcement and persistence. And it contrasts the reforms with 'unsubstantiated claims of rarity' that no sentence read attributes to anyone. The article does not argue the male-circumcision comparison. Lean: 0 pro, 0 anti, 3 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-the-united-kingdom` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5906 |
| Sentences (prose + list items; headings and tables excluded) | 168 |
| Sentences with no citation marker of their own | 51 (30%) |
| Paragraphs/list items with no citation marker at all | 10 of 59 |
| Table rows (not counted as sentences) | 4 |
| Sources listed in sources CSV | 54 |
| Distinct citation numbers used in text | 54 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 5 | 0.8 | notable (3), landmark (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | accused (1) |
| MOS:WTW editorializing | 10 | 1.7 | only (10) |
| MOS:WTW connectives (but/despite/however...) | 44 | 7.5 | though (15), despite (13), but (10), while (5), however (1) |
| MOS:WTW synonyms for 'said' | 2 | 0.3 | confirm (1), reveal (1) |
| Hyland 2005 hedges | 73 | 12.4 | often (13), rather (13), estimated (11), indicate (7), may (6) |
| Hyland 2005 boosters | 15 | 2.5 | known (5), found (3), showed (3), demonstrates (1), must (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This evolution was driven by evidence of rising prevalence, including NHS data showing hundreds of FGM-related hospital visits annually, underscoring the need for stronger deterrence against "holiday" cuttings." | F034 False Cause | neutral/structural | Uncited (code count). Takes 'hundreds of FGM-related hospital visits annually' as 'evidence of rising prevalence'. Visit counts measure identification. Sentence 66 itself attributes more visible documentation to 'heightened awareness following the ... Act', so a rise in detection is read as a rise in occurrence. (sentence 78) |
| 2 | "These changes reflected causal links between lax prior enforcement—zero convictions from 1985 to 2014—and persistent cultural practices, prioritizing empirical deterrence over multicultural relativism." | F033 Causal Oversimplification | neutral/structural | Uncited. Asserts 'causal links' between zero convictions and 'persistent cultural practices', and frames the reform as 'empirical deterrence over multicultural relativism'. One cause is assumed, and the same section (83) says convictions remain a handful after reform. (sentence 81) |
| 3 | "The evolution demonstrates a shift from narrow prohibition to comprehensive risk-based criminalization, grounded in verifiable prevalence data rather than unsubstantiated claims of rarity." | F002 Straw Man | neutral/structural | Uncited. Contrasts the reforms with 'unsubstantiated claims of rarity', a position no sentence read attributes to anyone, so the target appears to be constructed for the contrast. (sentence 84) |

Flag tally by side (simple count of the table above): neutral/structural 3.

## Both-sides balance note

Same-standard check: critics' arguments that enforcement reflects reluctance to challenge multiculturalism (103) and the BMA's critique (122) are attributed, and the CPS's evidence-threshold rationale (167) is given alongside them. The harm sentences (138-140) are cited and descriptive. There is no circumcision comparison to check.

## What wasn't checked

- Sentences outside the reading set (115 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Internal inconsistency on penalties: sentence 3 gives 'up to 14 years', while uncited sentence 19 says the 2015 Act 'raised the criminal penalty ... to life imprisonment if the victim is under the age of 16'. This needs a source check; no verdict is given here.
