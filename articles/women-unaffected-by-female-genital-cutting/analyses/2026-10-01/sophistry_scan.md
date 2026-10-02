# Sophistry and fallacy scan: Women unaffected by female genital cutting

- **Article:** Women unaffected by female genital cutting
- **URL:** https://grokipedia.com/page/Women_unaffected_by_female_genital_cutting
- **Snapshot file:** `articles/women-unaffected-by-female-genital-cutting/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (7 sentences) read in full, plus 45 of 139 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The title and lead describe women who have not been cut. Most of the body, however, argues in the article's own voice that FGC harms are overstated, and the summary step is often uncited. Six flags favor the pro-cutting or 'distinction' side. Type I 'clitoridectomy' is likened to cosmetic hoodectomy. One US diaspora study is taken to 'support' the proponents' view. Harm-focused sources are pre-discounted as 'ideologically aligned NGOs' and 'ethnocentric assumptions in academia'. Survey support for continuation is read as showing no perceived detriment. Female performance of the practice is offered as answering the patriarchy question. The 230 million affected are minimized with 'only'. One flag favors the anti-cutting side: the lead states disputed outcomes (sexual dysfunction, childbirth risks) as settled, procedure-linked complications, while the body grades the same evidence as very low quality. Lean: 6 pro-cutting/distinction, 1 anti-cutting. These are judgment calls. Harm data (bleeding, urine retention, RR figures) are reported in the body and were not disputed here.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug women-unaffected-by-female-genital-cutting` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4854 |
| Sentences (prose + list items; headings and tables excluded) | 146 |
| Sentences with no citation marker of their own | 41 (28%) |
| Paragraphs/list items with no citation marker at all | 1 of 47 |
| Table rows (not counted as sentences) | 4 |
| Sources listed in sources CSV | 56 |
| Distinct citation numbers used in text | 56 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 4 | 0.8 | only (4) |
| MOS:WTW connectives (but/despite/however...) | 31 | 6.4 | while (10), but (8), though (8), despite (4), however (1) |
| MOS:WTW synonyms for 'said' | 7 | 1.4 | reveal (6), assert (1) |
| Hyland 2005 hedges | 89 | 18.3 | often (22), rather (16), may (9), approximately (5), indicate (5) |
| Hyland 2005 boosters | 17 | 3.5 | found (7), showed (3), show (2), believed (1), certain (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Conversely, the cutting narrative differentiates by WHO typology—Type I (clitoridectomy, affecting ~80% of cases in some regions) involves minimal tissue removal analogous to hoodectomy in cosmetic procedures, with longitudinal data showing no consistent links to reduced sexual satisfaction or fertility when controlled for socioeconomic factors. [13]" | F042 False Analogy | pro-circumcision | 'Type I (clitoridectomy ...) involves minimal tissue removal analogous to hoodectomy in cosmetic procedures'. A procedure the sentence itself calls clitoridectomy, performed on girls, is likened to an elective adult cosmetic procedure. The analogy fails on both the tissue involved and consent. (sentence 20) |
| 2 | "This supports cutting proponents' view that pathologizing narratives amplify harm via social exclusion, as institutional emphases on mutilation—often from ideologically aligned NGOs—overlook resilience in unaffected women who report intact pleasure and well-being, per community-based surveys in Mali and Sierra Leone (e.g., 70-80% satisfaction rates in ritual contexts). [13]" | F011 Hasty Generalization | pro-circumcision | 'This supports cutting proponents' view that pathologizing narratives amplify harm'. One 2023 study of 638 Somali women in the US (22) is generalized to practicing communities in general. The sentence then cites 'unaffected women who report intact pleasure', which does not bear on women who were cut. (sentence 23) |
| 3 | "Such distinctions reveal how source biases, including ethnocentric assumptions in academia, skew toward harm amplification over causal disaggregation of cultural versus procedural impacts. [11]" | F026 Poisoning the Well | pro-circumcision | 'Source biases, including ethnocentric assumptions in academia, skew toward harm amplification'. Harm-side research is pre-discounted by attributing bias to its origin (as is 'often from ideologically aligned NGOs' in 23), rather than by engaging specific findings. (sentence 24) |
| 4 | "In Demographic and Health Surveys (DHS) conducted across countries where female genital cutting (FGC) is prevalent, substantial proportions of women who have undergone the procedure express support for its continuation, indicating a lack of perceived personal detriment to well-being." | F034 False Cause | pro-circumcision | Uncited (code count). Women's 'support for its continuation' is read as 'indicating a lack of perceived personal detriment to well-being'. Support for a social norm (see the marriageability and virginity rationales in 42) is a different thing from the absence of perceived harm, so the inference does not follow (also in 64). (sentence 61) |
| 5 | "Empirical links between FGC and systemic patriarchy remain weakly established, as practices are frequently initiated and controlled by women for social cohesion, not male dominance, and reports of fulfilling sexual lives post-cutting contradict narratives of inherent debilitation. [40]" | F003 Red Herring | pro-circumcision | Patriarchy links are said to be 'weakly established, as practices are frequently initiated and controlled by women'. Who performs the practice does not answer whether it serves male-oriented norms. The article's own Guinea rationale (42: 'diminish sexual desire, thereby safeguarding virginity ... reducing infidelity risks') bears on exactly that point. (sentence 108) |
| 6 | "This group comprises the overwhelming majority of the world's approximately four billion females, as female genital cutting affects only over 230 million girls and women alive today, concentrated in about 30 countries across Africa (144 million cases), Asia (over 80 million), and parts of the Middle East. [2] [1]" | F040 Loaded Language | pro-circumcision | 'Female genital cutting affects only over 230 million girls and women alive today'. 'Only' minimizes a very large absolute number by setting it against the world female population, which is the frame the article's title sets up. (sentence 2) |
| 7 | "Women unaffected by female genital cutting are females who have not undergone the culturally motivated procedure involving partial or total removal of, or other injury to, the external female genitalia, a practice that spares the natural anatomy and avoids procedure-linked complications such as hemorrhage, chronic pain, urinary issues, sexual dysfunction, and increased childbirth risks. [1] [2]" | F032 Cum Hoc | anti-circumcision | The lead lists 'sexual dysfunction, and increased childbirth risks' as 'procedure-linked complications' without qualification, while the body (73-74, 81, 86) grades the evidence for long-term outcomes as low or very low quality and says causality is uncertain. This is an internal inconsistency in the opposite direction from the body. Claim needs source check; no verdict is given. (sentence 1) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 6.

## Both-sides balance note

Same-standard check: the body applies a strict standard to harm evidence (GRADE 'very low', confounding, recall bias: 73-75, 81, 86) but takes favorable self-reports at face value (51-53, 61-65, 89-98, 107, 140). Social desirability bias is mentioned once (57). WHO and critics are attributed (143-144), and their position gets two sentences, against several uncited article-voice sentences on the other side. The lead leans the other way (1, 5). Most body sentences read were uncited (code count).

## What wasn't checked

- Sentences outside the reading set (94 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Scope: the title topic (women who were not cut) covers only the lead and prevalence sections. Whether the body belongs under this title is an editorial question and was not scored as a fallacy.
- Extraction artifact '04269-6/fulltext)' in sentence 92.
- Figures not checked: Lightfoot-Klein 94% (53), the 2023 Somali study ORs (22, 75), the Campbell review RRs (127-128), and the Type I '~80% of cases' figure (20).
