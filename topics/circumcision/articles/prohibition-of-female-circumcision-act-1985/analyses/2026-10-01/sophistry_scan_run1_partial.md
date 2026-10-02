> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Prohibition of Female Circumcision Act 1985

- **Article:** Prohibition of Female Circumcision Act 1985
- **URL:** https://grokipedia.com/page/prohibition_of_female_circumcision_act_1985
- **Snapshot file:** `articles/prohibition-of-female-circumcision-act-1985/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (9 sentences) read in full, plus 37 of 113 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The statutory description (offences, exceptions, the absent extraterritorial reach, repeal) is clear and cited. Most reasoning flags are in the uncited 'Enforcement Failures' section, which gives single-cause, politically framed explanations: 'diversity training', 'non-integrated enclaves', and a straw-manned 'solely' poverty narrative. It also reads zero convictions as proof of no deterrent effect. On the male-circumcision comparison, the article's uncited closing sentence denies 'cultural or gender bias' by assertion and calls the analogy 'superficial'. On the anti-cutting side, studies are said to show that 'no compensatory cultural gains' outweigh the injuries, which is a normative weighing presented as empirical. Lean: 1 pro, 1 anti, 3 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug prohibition-of-female-circumcision-act-1985` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4486 |
| Sentences (prose + list items; headings and tables excluded) | 122 |
| Sentences with no citation marker of their own | 34 (28%) |
| Paragraphs/list items with no citation marker at all | 5 of 47 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 43 |
| Distinct citation numbers used in text | 43 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 5 | 1.1 | only (5) |
| MOS:WTW connectives (but/despite/however...) | 29 | 6.5 | while (9), despite (8), though (5), but (4), although (2) |
| MOS:WTW synonyms for 'said' | 1 | 0.2 | assert (1) |
| Hyland 2005 hedges | 39 | 8.7 | rather (9), often (8), typically (5), could (3), indicate (3) |
| Hyland 2005 boosters | 8 | 1.8 | certain (3), demonstrated (1), incontrovertible (1), known (1), realized (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This distinction reflects causal prioritization of documented outcomes over superficial procedural analogies, rather than cultural or gender bias." | F040 Loaded Language | pro-circumcision | Uncited (code count). 'This distinction reflects causal prioritization of documented outcomes over superficial procedural analogies, rather than cultural or gender bias'. The opposing analogy is dismissed as 'superficial', and the bias explanation is ruled out by assertion. The critics' point (102) concerns consent and legal parity, which the harm comparison does not address. (sentence 109) |
| 2 | "The World Health Organization classifies all forms as mutilation due to the absence of health benefits and violation of bodily integrity, with studies showing no compensatory cultural gains outweighing these non-consensual injuries to minors. [10]" | F061 Is-Ought Jump | anti-circumcision | 'Studies showing no compensatory cultural gains outweighing these non-consensual injuries' presents as an empirical finding what is a normative weighing of cultural against physical goods. Studies can measure harms; whether cultural gains 'outweigh' them is a value judgment. (sentence 97) |
| 3 | "The empirical record of zero convictions under the Act demonstrated its primarily symbolic function, with no deterrent effect evidenced in court outcomes." | F034 False Cause | neutral/structural | Uncited. 'Zero convictions ... demonstrated its primarily symbolic function, with no deterrent effect evidenced in court outcomes'. Conviction counts measure enforcement, not deterrence; a deterrent effect would show up as cases that did not happen. (sentence 84) |
| 4 | "Cultural relativism influenced enforcement shortcomings, with police and social services often prioritizing community cohesion over child protection, influenced by diversity training that emphasized sensitivity to immigrant customs and discouraged interventions perceived as culturally insensitive." | F033 Causal Oversimplification | neutral/structural | Uncited. Attributes enforcement shortfalls to 'diversity training that emphasized sensitivity to immigrant customs', a single politically framed cause with no evidence given. Sentence 87 lists other causes (detection limits, reluctance to prosecute). (sentence 88) |
| 5 | "Narratives attributing FGM persistence solely to socioeconomic factors like poverty have been overstated, as empirical data show the practice occurring across income levels within affected diasporas, driven fundamentally by ritualistic and patriarchal traditions rather than economic deprivation alone." | F002 Straw Man | neutral/structural | Uncited. Rebuts 'narratives attributing FGM persistence solely to socioeconomic factors like poverty', a position no sentence read attributes to anyone. Sentence 94 has cultural-rights advocates naming poverty as one 'root cause' among others, so 'solely' overstates the target. (sentence 91) |

Flag tally by side (simple count of the table above): anti-circumcision 1; neutral/structural 3; pro-circumcision 1.

## Both-sides balance note

Same-standard check: on male circumcision, the critics' hypocrisy argument (102) is attributed, and the article's reply rests on comparative morbidity (105-108). Sentence 106 does note that MC benefits are 'debated and not universally endorsed', which is a fair qualification. The closing sentence (109) moves from the harm comparison to denying bias without evidence, and this is the only pro-side flag. The cultural-rights view (94-95) is attributed, while the article's voice takes the universalist side (99-101).

## What wasn't checked

- Sentences outside the reading set (76 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Sentence 106 gives the UTI reduction as '50-60%', while other articles in this set give about 90%. This was not resolved.
