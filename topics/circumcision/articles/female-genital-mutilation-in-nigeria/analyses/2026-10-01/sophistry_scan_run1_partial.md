> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Female genital mutilation in Nigeria

- **Article:** Female genital mutilation in Nigeria
- **URL:** https://grokipedia.com/page/Female_genital_mutilation_in_Nigeria
- **Snapshot file:** `articles/female-genital-mutilation-in-nigeria/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (5 sentences) read in full, plus 45 of 149 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This article is mostly a cited epidemiological and legal survey, and it attributes community justifications fairly before setting the evidence against them. Five reasoning flags were found in the sentences read. Two are anti-cutting causal overreaches: fistula is attributed to FGM in northern regions the article elsewhere describes as low-prevalence and practicing milder forms, and 'intergenerational transmission of trauma' is inferred from a correlation. Two are neutral or structural: education and modernization are named as 'primary causal drivers' from correlations, and there is a garbled, overgeneralized claim about communities abandoning customs. One labels anti-FGM prohibitionists as 'absolutism', favoring the harm-reduction or medicalization side. Lean: 1 pro-cutting, 2 anti, 2 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-nigeria` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5403 |
| Sentences (prose + list items; headings and tables excluded) | 154 |
| Sentences with no citation marker of their own | 33 (21%) |
| Paragraphs/list items with no citation marker at all | 0 of 56 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 71 |
| Distinct citation numbers used in text | 71 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | respected (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 1 | 0.2 | purported (1) |
| MOS:WTW editorializing | 3 | 0.6 | only (3) |
| MOS:WTW connectives (but/despite/however...) | 40 | 7.4 | though (14), but (8), despite (7), while (7), however (4) |
| MOS:WTW synonyms for 'said' | 5 | 0.9 | confirm (2), reveal (2), note (1) |
| Hyland 2005 hedges | 73 | 13.5 | often (15), rather (11), around (7), approximately (6), indicate (5) |
| Hyland 2005 boosters | 16 | 3.0 | certain (6), show (5), shows (2), demonstrate (1), demonstrated (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Vesicovaginal fistulas, resulting from ischemic necrosis during obstructed labor, show 20-30% higher prevalence among Nigerian women with FGM, particularly in northern regions practicing more severe forms." | F033 Causal Oversimplification | anti-circumcision | Uncited (code count). Attributes 20-30% higher fistula prevalence to FGM 'particularly in northern regions practicing more severe forms'. Sentence 30 says northern Hausa-Fulani practice 'less severe' sunna forms, and sentence 102 gives northern prevalence 'under 5%'. Other drivers of obstructed labor are not considered, and the regional claim conflicts with the article's own data. (sentence 89) |
| 2 | "In Nigerian surveys, FGM correlates with 25-35% increased anxiety prevalence, exacerbated by perceptions of familial betrayal and normalized violence, fostering intergenerational transmission of trauma through perpetuated acceptance of ritual harm. [42] [44]" | F032 Cum Hoc | anti-circumcision | 'FGM correlates with 25-35% increased anxiety prevalence ... fostering intergenerational transmission of trauma'. A cross-sectional correlation is extended to a causal, multigenerational mechanism. (sentence 96) |
| 3 | "Empirical patterns reveal stronger correlations between reduced FGM rates and socioeconomic factors such as higher maternal education and urban residence—where prevalence drops to 13% versus 24% in rural areas—than with targeted campaigns alone, underscoring education and modernization as primary causal drivers. [9]" | F032 Cum Hoc | neutral/structural | From 'stronger correlations' with education and urban residence, it concludes these are the 'primary causal drivers'. Education and urbanity are confounded with many other factors. (sentence 135) |
| 4 | "Elders' insistence on tradition contrasts with evidence that communities historically abandon injurious customs through internal reckoning, as seen in declining voluntary cessation rates predating formal bans in select Nigerian locales, prioritizing causal evidence of suffering over unsubstantiated cultural imperatives. [19] [68]" | F011 Hasty Generalization | neutral/structural | 'Communities historically abandon injurious customs through internal reckoning' is generalized from 'select Nigerian locales'. The evidence phrase ('declining voluntary cessation rates') would, read literally, mean less cessation, so the support offered is unclear. (sentence 146) |
| 5 | "Proponents of absolutism emphasize causal links between FGM and irreversible harms, rejecting medicalization as a false safeguard that sustains demand, while enforcement advocates call for enhanced surveillance of clinics and community reporting incentives to avoid underground proliferation without excusing the practice's persistence. [70] [69]" | F040 Loaded Language | pro-circumcision | Labels anti-FGM prohibitionists 'Proponents of absolutism' (and sentence 153 'absolute prohibitions'), framing the strict side pejoratively against 'pragmatic harm reduction'. This is the same label convention flagged elsewhere in this audit. (sentence 154) |

Flag tally by side (simple count of the table above): anti-circumcision 2; neutral/structural 2; pro-circumcision 1.

## Both-sides balance note

Same-standard check: traditional justifications (38, 139) are stated and then tested against evidence (43, 141, 143), and the article applies 'no controlled studies demonstrate causal reductions' (141) to the pro-practice side. Harm claims, by contrast, are sometimes stated causally from cross-sectional data (96) or uncited (77-91 includes several uncited sentences). The standard is therefore somewhat stricter for pro-practice claims than for harm claims, though the harm side has much more evidence cited overall. Sentence 148, that medicalization does not remove long-term harms 'as these stem from the procedure's inherent tissue damage', is a mechanism claim and was not flagged.

## What wasn't checked

- Sentences outside the reading set (104 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The regional inconsistency (northern prevalence and severity: 30, 89, 102) was noted, not resolved against sources.
