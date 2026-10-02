> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Female genital mutilation in New Zealand

- **Article:** Female genital mutilation in New Zealand
- **URL:** https://grokipedia.com/page/female_genital_mutilation_in_new_zealand
- **Snapshot file:** `articles/female-genital-mutilation-in-new-zealand/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 37 of 113 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The legal description (section 204A, the defences excluded, Oranga Tamariki protocols) is clear and cited. The reasoning problems are mostly structural and political rather than about circumcision. The article explains New Zealand's lack of documented cases two incompatible ways, as 'effective legal deterrence' (uncited) and as prohibition that 'merely displaces' harm, while also saying there is no baseline data. It infers sustained domestic risk from migrant women's pre-arrival sequelae. It uses assimilationist framing in its own voice ('left-leaning tolerance advocates', 'diversity guises'). An uncited aside asserts that male circumcision has no equivalent effect on pleasure. Anti-cutting overreach appears in two article-voice sentences, a sweeping 'no evidence of female agency' and an is-ought conclusion. An extraction artifact ('68589-5/fulltext)') sits inside sentence 21. Lean: 1 pro, 2 anti, 4 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-new-zealand` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4316 |
| Sentences (prose + list items; headings and tables excluded) | 121 |
| Sentences with no citation marker of their own | 27 (22%) |
| Paragraphs/list items with no citation marker at all | 6 of 45 |
| Table rows (not counted as sentences) | 4 |
| Sources listed in sources CSV | 34 |
| Distinct citation numbers used in text | 34 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | unique (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.5 | purported (2) |
| MOS:WTW editorializing | 4 | 0.9 | only (4) |
| MOS:WTW connectives (but/despite/however...) | 28 | 6.5 | but (8), while (7), though (6), despite (5), although (1) |
| MOS:WTW synonyms for 'said' | 7 | 1.6 | confirm (2), reveal (2), assert (1), claim (1), note (1) |
| Hyland 2005 hedges | 34 | 7.9 | often (8), rather (8), claims (6), may (3), argue (2) |
| Hyland 2005 boosters | 8 | 1.9 | must (2), establish (1), established (1), never (1), shown (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This scarcity reflects effective legal deterrence and low cultural entrenchment, though latent risks persist without rigorous enforcement of assimilation norms for harmful imported traditions." | F034 False Cause | neutral/structural | Uncited (code count). Credits scarcity to 'effective legal deterrence', yet sentence 8 records no prosecutions and sentence 114 says no prevalence surveys exist to establish a baseline. Sentence 121 then says prohibition 'merely displace[s]' harm, so the article gives two contradictory causal stories for the same absence of data. (sentence 6) |
| 2 | "This continuity challenges assumptions of rapid cultural assimilation, with empirical observations from obstetric surveys indicating rising encounters with FGM sequelae among migrant patients, underscoring causal links between selective immigration from FGM-endemic regions and sustained vulnerability. [16]" | F034 False Cause | neutral/structural | Obstetric encounters with FGM 'sequelae among migrant patients' (cut before arrival) are taken to show 'causal links between selective immigration ... and sustained vulnerability' of resident girls. Sentence 5 states there are no documented instances in the country, so the evidence offered does not reach the conclusion. (sentence 48) |
| 3 | "Without these, optimistic assessments risk complacency, as causal analysis reveals that legal prohibitions without robust monitoring merely displace rather than eliminate the harm, underscoring the empirical imperative for escalated, evidence-based enforcement over passive initiatives. [34]" | F033 Causal Oversimplification | neutral/structural | 'Causal analysis reveals' a single mechanism (displacement), but no analysis is presented, and the same section says there is no data to measure change. (sentence 121) |
| 4 | "In practice, community-led dialogues in New Zealand, often promoted by left-leaning tolerance advocates, have yielded mixed results; while some Somali leaders collaborated with health educators to reframe FGM as unnecessary for cultural identity, achieving near-universal rejection within targeted groups, others reveal persistent rationalizations that excuse harm under diversity guises, eroding protections for girls by deferring to offender communities rather than enforcing assimilation to host norms. [27]" | F040 Loaded Language | neutral/structural | Article voice: 'left-leaning tolerance advocates', 'excuse harm under diversity guises', 'offender communities', 'enforcing assimilation'. These are political labels used in place of evaluating the 'mixed results' the sentence itself reports. (sentence 92) |
| 5 | "A core motivation is the deliberate reduction of female sexual pleasure to promote premarital virginity and postmarital fidelity, distinguishing FGM from male circumcision, which lacks equivalent intent or physiological impact on pleasure." | F003 Red Herring | pro-circumcision | Uncited. An aside in an FGM-in-New-Zealand article asserts that male circumcision 'lacks equivalent intent or physiological impact on pleasure', a contested comparative claim stated as settled and off-topic here. It needs a source check, and no verdict is given here. (sentence 20) |
| 6 | "Ethnographic analyses reveal no evidence of female agency in initiations, which occur pre-puberty without informed consent, contrasting voluntary practices; instead, FGM causally entrenches dependency by linking women's social value to mutilated bodies, incompatible with individual autonomy principles." | F011 Hasty Generalization | anti-circumcision | Uncited. 'No evidence of female agency' and 'causally entrenches dependency' are sweeping claims stated without the analyses being named. Sentence 89 reports some women recounting the practice as a family ritual, which complicates the universal claim. (sentence 23) |
| 7 | "This clash underscores a causal reality: cultural practices causing verifiable injury cannot claim moral equivalence, as first-hand accounts from reformed community members affirm that abandoning FGM preserves heritage without mutilation, aligning with bodily integrity as a universal baseline uncompromised by multiculturalism's excesses. [28]" | F061 Is-Ought Jump | anti-circumcision | Article voice: 'This clash underscores a causal reality: cultural practices causing verifiable injury cannot claim moral equivalence'. A normative conclusion is presented as a causal fact. (sentence 95) |

Flag tally by side (simple count of the table above): anti-circumcision 2; neutral/structural 4; pro-circumcision 1.

## Both-sides balance note

Same-standard check: 'Critics' of relativism (94) and 'multicultural proponents' (102) are both attributed. The article's voice, though, takes the assimilationist side (6, 32, 92, 93, 95), so the opposite side gets labels where the favored side gets its arguments. On male circumcision: 20, 21 and 24 assert non-equivalence without any equivalence argument being presented. The pro-distinction claims ('effects absent in male counterparts') are not held to the citation standard the article applies to FGM harms (13-14, which are cited).

## What wasn't checked

- Sentences outside the reading set (76 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The extraction artifact in sentence 21 ('68589-5/fulltext)') suggests a broken link, and the cited source behind it could not be identified.
