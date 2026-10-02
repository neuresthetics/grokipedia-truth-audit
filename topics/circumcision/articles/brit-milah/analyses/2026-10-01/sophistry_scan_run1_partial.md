> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Brit milah

- **Article:** Brit milah
- **URL:** https://grokipedia.com/page/Brit_milah
- **Snapshot file:** `articles/brit-milah/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 275 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The article explains the religious basis of brit milah carefully, and it reports both the case for the practice and the case against it, mostly with attribution. The flagged problems are in the article's own voice and mostly favor the practice. It credits neonatal circumcision with HIV protection that was measured in adult trials. It offers an uncited claim that the eighth-day timing matches clotting physiology as 'evidence of practical wisdom'. It treats the absence of documented complications as showing low risk. It summarizes 'medical bodies' as generally concluding that benefits exceed risks while citing only US bodies. It labels activist critiques 'anecdotal or ideological'. One flag goes the other way: the article calls traditional elements 'archaic'. On the sentences read, the flags lean pro-circumcision (6 of 7). These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug brit-milah` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 9815 |
| Sentences (prose + list items; headings and tables excluded) | 281 |
| Sentences with no citation marker of their own | 47 (17%) |
| Paragraphs/list items with no citation marker at all | 8 of 94 |
| Table rows (not counted as sentences) | 6 |
| Sources listed in sources CSV | 195 |
| Distinct citation numbers used in text | 195 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 5 | 0.5 | great (1), landmark (1), leading (1), notable (1), unique (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.1 | purported (1) |
| MOS:WTW editorializing | 7 | 0.7 | only (7) |
| MOS:WTW connectives (but/despite/however...) | 89 | 9.1 | but (31), though (25), while (24), despite (7), however (2) |
| MOS:WTW synonyms for 'said' | 7 | 0.7 | insist (3), expose (2), claim (1), observe (1) |
| Hyland 2005 hedges | 97 | 9.9 | often (24), may (11), typically (10), rather (6), approximately (5) |
| Hyland 2005 boosters | 27 | 2.8 | certain (8), must (6), known (4), found (2), true (2) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "The ritual has elicited debates over medical ethics, with empirical evidence indicating neonatal circumcision confers protections against urinary tract infections, penile cancer, and heterosexual HIV transmission, yet it is irreversible and carries risks of bleeding, infection, or improper healing. [7] [8]" | F011 Hasty Generalization | pro-circumcision | Lead lists 'heterosexual HIV transmission' as a protection conferred by neonatal circumcision. The article's own sentence 227 says the figure comes from adult trials and is 'extrapolated to infants', but the lead drops that step. (sentence 5) |
| 2 | "While ancient Israelites would not have known this scientifically, the alignment is cited as evidence of practical wisdom in the biblical prescription, making the rite safer in pre-modern conditions without contemporary interventions like vitamin K supplementation." | F035 Texas Sharpshooter | pro-circumcision | Uncited (code count). A modern physiological claim (sentence 16, which needs a source check) is fitted after the fact to an ancient rule and then 'cited as evidence of practical wisdom', with no named source for the inference (passive 'is cited'). (sentence 17) |
| 3 | "Empirical medical data on complications remains sparse due to the procedure's superficial nature, with no documented cases of significant risk in peer-reviewed literature when executed by qualified practitioners. [81]" | F010 Appeal to Ignorance | pro-circumcision | In the same sentence that says the data are 'sparse', the absence of documented cases is offered as evidence that there is no significant risk. Absence of reports is not evidence of safety without an adequate search or surveillance base. (sentence 138) |
| 4 | "Intactivists further allege long-term harms, including reduced penile sensitivity, sexual dysfunction, and psychological trauma, though empirical studies on these effects remain contested and often rely on self-reported data from adults. [124]" | F040 Loaded Language | pro-circumcision | Intactivists 'allege' harms (MOS:WTW expression of doubt), while proponents in sentence 200 'argue'. The asymmetric verbs pre-judge which side is credible. (sentence 211) |
| 5 | "These positions counter activist claims of net harm by prioritizing randomized and cohort data over anecdotal or ideological critiques, acknowledging procedure safety improves with trained practitioners. [126] [153]" | F026 Poisoning the Well | pro-circumcision | Labels the opposing case as 'anecdotal or ideological critiques' and so disqualifies it by category. The sentence does not engage the ethical (non-empirical) objections raised in sentences 201-205. (sentence 229) |
| 6 | "Medical bodies have evaluated neonatal circumcision through empirical lenses, generally concluding preventive benefits exceed procedural risks when performed competently, though without mandating it universally." | F036 Suppressed Evidence | pro-circumcision | Uncited; says medical bodies 'generally' conclude that benefits exceed risks, but the section cites only AAP and CDC (226-227). Bodies the wider article set reports as concluding otherwise (CPS, RACP, KNMG) are left out here. (sentence 225) |
| 7 | "When performed, it includes milah and priah on the eighth day by a mohel or physician, with topical anesthesia standard to ensure minimal distress and metzitzah either absent or executed non-orally if at all, aligning with progressive values that adapt tradition to modern hygiene and consent principles without claiming talmudic mandate for archaic elements. [6] [4]" | F040 Loaded Language | anti-circumcision | The article's own voice calls traditional ritual elements 'archaic', a pejorative label that favors the progressive/critical reading. (sentence 161) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 6.

## Both-sides balance note

Same-standard check: anti-circumcision arguments (sentences 201-217) are consistently attributed to 'secular ethicists', 'activists' or named organizations, and their evidence base is qualified ('contested', 'self-reported'). Pro-side medical claims are often stated in the article's voice (163, 165, 225), and some are uncited. Sentence 212 mixes both directions: activists 'dismiss' (pro-leaning verb) 'purported' benefits (anti-leaning qualifier). It was not flagged. The metzitzah b'peh section reports the HSV link and the religious-freedom defense with comparable attribution. Shortfall: no sentence read gives a pro-side source for the vitamin K claim, and none gives the anti side's reply to 'ideological' (229).

## What wasn't checked

- Sentences outside the reading set (230 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Sentence 252 contains an extraction artifact ('07737-1/fulltext)') from the page; this was not traced to the HTML.
