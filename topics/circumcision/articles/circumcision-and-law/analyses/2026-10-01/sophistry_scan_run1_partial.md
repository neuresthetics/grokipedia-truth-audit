> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Circumcision and law

- **Article:** Circumcision and law
- **URL:** https://grokipedia.com/page/Circumcision_and_law
- **Snapshot file:** `topics/circumcision/articles/circumcision-and-law/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 80 of 314 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 80). Other sentences were not read closely.

## Verdict

This long legal survey mostly reports statutes, cases and rights arguments with attribution, and it gives restriction advocates a full hearing in the human-rights section. The flags are in the article's own voice at transition and summary points. It charges only critics' research with 'source biases'. It treats the absence of international enforcement as evidence that rights instruments permit the practice. It calls integrity arguments 'absolutist'. It answers autonomy objections with complication-rate data. It praises court deference as 'causal realism in law'. One flag goes the other way: the article's own 'purported' for historical benefit claims. On the sentences read, the flags lean pro-circumcision (5 of 6). These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug circumcision-and-law` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 11105 |
| Sentences (prose + list items; headings and tables excluded) | 320 |
| Sentences with no citation marker of their own | 82 (26%) |
| Paragraphs/list items with no citation marker at all | 3 of 109 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 218 |
| Distinct citation numbers used in text | 219 |
| Dangling citation numbers (used, no source row) | 1: 2000 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 6 | 0.5 | leading (2), celebrated (1), landmark (1), notable (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 1 | 0.1 | it is considered (1) |
| MOS:WTW expressions of doubt | 5 | 0.5 | purported (4), alleged (1) |
| MOS:WTW editorializing | 10 | 0.9 | only (9), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 134 | 12.1 | but (48), though (39), while (26), despite (18), however (3) |
| MOS:WTW synonyms for 'said' | 4 | 0.4 | claim (2), assert (1), reveal (1) |
| Hyland 2005 hedges | 112 | 10.1 | claims (18), often (15), rather (13), typically (9), may (8) |
| Hyland 2005 boosters | 20 | 1.8 | certain (7), established (4), found (3), must (3), clear (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "These cases highlight causal trade-offs: while religious communities argue continuity of tradition outweighs deferred consent, critics invoke first-principles of non-maleficence, noting irreversible alteration without immediate medical necessity, amid source biases in advocacy-driven research that often amplify risks or understate cultural contexts. [6]" | F026 Poisoning the Well | pro-circumcision | The lead charges 'advocacy-driven research' with 'source biases' that 'amplify risks'. No parallel caution is attached to research or policy from the other side, so one side's evidence is discounted in advance. (sentence 6) |
| 2 | "These claims, primarily advanced in academic and advocacy literature rather than treaty body jurisprudence, face counterarguments that religious freedoms (e.g., ICCPR Article 18) and parental rights permit the practice, provided risks are minimized, as evidenced by the absence of international enforcement actions or prohibitions despite decades of debate." | F010 Appeal to Ignorance | pro-circumcision | Uncited (code count). 'The absence of international enforcement actions or prohibitions' is offered as evidence that rights instruments permit the practice. Absence of enforcement is not evidence about what a right requires. (sentence 53) |
| 3 | "Empirical data on benefits, such as HIV reduction in high-prevalence areas (60% efficacy per WHO meta-analyses), complicates absolutist integrity claims, though advocates counter that such gains apply to adults in specific epidemics, not routine neonatal use in low-risk settings. [34]" | F040 Loaded Language | pro-circumcision | 'Absolutist integrity claims' is a pejorative label in the article's voice; the pro side's position gets no comparable label. The advocates' counter in the same sentence is noted. (sentence 54) |
| 4 | "Medical performance is often mandated in countries with immigrant Muslim populations, where prevalence can exceed 20% in urban areas, but secular opposition has fueled debates framing it as a violation of autonomy, despite empirical data showing low complication rates (under 1% for trained providers) and no long-term functional deficits in peer-reviewed studies. [56]" | F003 Red Herring | pro-circumcision | An autonomy objection is set against 'empirical data showing low complication rates' with 'despite', as if the data answered it. Autonomy and consent arguments do not depend on complication rates. (sentence 76) |
| 5 | "Such outcomes reflect causal realism in law: where parental intent aligns with prevailing medical literature showing modest aggregate benefits (e.g., CDC estimates of 1 in 100 HIV risk reduction in high-prevalence settings), courts avoid overriding decisions absent acute harm. [200] [201]" | F040 Loaded Language | pro-circumcision | Describes court deference with an approving label ('causal realism in law') in the article's voice. The label is a praise predicate attached to one side's legal outcome, not a description of it. (sentence 296) |
| 6 | "Newborn circumcision rates increased from roughly 10% circa 1900 to peaks exceeding 80% by the 1960s, propelled by endorsements from organizations such as the American Medical Association and American Academy of Pediatrics, which cited purported preventive benefits against conditions like penile cancer and urinary tract infections, though these claims lacked robust randomized trial evidence at the time. [25] [26]" | F040 Loaded Language | anti-circumcision | The article's own 'purported preventive benefits' (MOS:WTW expression of doubt). The historical point that early claims lacked RCT evidence is fair, but 'purported' adds a verdict. (sentence 31) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 5.

## Both-sides balance note

Same-standard check: rights-based arguments for restriction (sentences 37-52) are attributed throughout ('advocates argue', 'critics apply', 'some interpret'), and their non-binding status is noted. Pro-side replies are more often in the article's voice (53, 54, 76, 296). On the anti side, sentence 48 states 'meatal stenosis (occurring in 5-10% of cases)' as an unattributed figure inside an attributed interpretation, and sentence 38 lists 'reduced sexual sensitivity' among risks. Both need a source check; neither was flagged as a reasoning fault, but they are unsourced in the sentence. Court and legislative outcomes are reported with similar detail for restrictive rulings (Cologne, Montana, Boldt) and permissive ones (Hironimus, US deference).

## What wasn't checked

- Sentences outside the reading set (234 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The '[2000]' bracket counted as a dangling citation number is a year rendered as a citation link on the page (see INDEX).
- Sentence 69 contains an extraction artifact ('07737-1/fulltext)').
