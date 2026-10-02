> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Mohel

- **Article:** Mohel
- **URL:** https://grokipedia.com/page/Mohel
- **Snapshot file:** `articles/mohel/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 175 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The article's descriptions of halachic requirements, training and the metzitzah b'peh dispute are mostly attributed and cited, and the MBP section reports both rabbinic defenses and public-health data. Critics' ethical arguments (108-116) are attributed. The four flags, all pro-circumcision, are in the article's own voice. Two are in the 'Evidence-Based Benefits' section: adult HIV trials are extended to 'lifelong protection when performed neonatally', with population prevalence offered as the evidence, and an observational penile-cancer reduction is given a causal attribution. Two are uncited in the media section: opposing views are answered with complication rates, and mainstream portrayals are attributed to 'institutional biases toward secular norms'. Lean: 4 pro, 0 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug mohel` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6477 |
| Sentences (prose + list items; headings and tables excluded) | 181 |
| Sentences with no citation marker of their own | 51 (28%) |
| Paragraphs/list items with no citation marker at all | 4 of 59 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 126 |
| Distinct citation numbers used in text | 126 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.3 | notable (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 2 | 0.3 | only (2) |
| MOS:WTW connectives (but/despite/however...) | 57 | 8.8 | while (19), but (17), though (15), despite (4), although (1) |
| MOS:WTW synonyms for 'said' | 5 | 0.8 | expose (3), confirm (1), note (1) |
| Hyland 2005 hedges | 73 | 11.3 | often (15), may (10), typically (10), approximately (5), rather (4) |
| Hyland 2005 boosters | 15 | 2.3 | must (6), certain (2), demonstrated (2), known (2), demonstrate (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Systematic reviews of these trials and observational data affirm the mechanism involves keratinization of the glans and reduced viral entry sites under the foreskin, conferring lifelong protection when performed neonatally, as evidenced by lower HIV prevalence in circumcised populations. [62] [63]" | F011 Hasty Generalization | pro-circumcision | From adult VMMC trials (93) it concludes the protection is 'lifelong ... when performed neonatally, as evidenced by lower HIV prevalence in circumcised populations'. The trials did not test neonatal circumcision, and population prevalence is confounded. Adult results applied to neonates is the convention flagged elsewhere in this audit. (sentence 94) |
| 2 | "The procedure markedly decreases lifetime penile cancer incidence, which is rare but nearly exclusive to uncircumcised males with chronic inflammation or poor hygiene; epidemiological evidence indicates a 3- to 22-fold risk reduction in circumcised cohorts, attributable to elimination of smegma accumulation and phimosis-related carcinogenesis. [65] [64]" | F032 Cum Hoc | pro-circumcision | 'A 3- to 22-fold risk reduction in circumcised cohorts, attributable to elimination of smegma accumulation and phimosis-related carcinogenesis' gives a causal attribution to epidemiological associations. The wide range is reported without comment. (sentence 97) |
| 3 | "Broader societal views, influenced by secular ethics and medical skepticism, often conflate mohels with infant genital alteration debates, viewing brit milah as unnecessary or harmful despite data showing complication rates under 1% for trained practitioners." | F003 Red Herring | pro-circumcision | Uncited (code count). The view that brit milah is 'unnecessary or harmful' is answered with 'complication rates under 1%'. Low complication rates speak to 'harmful' in the acute sense but not to 'unnecessary' or to the consent-based objection. (sentence 179) |
| 4 | "Mainstream portrayals tend to prioritize autonomy arguments against non-consensual procedures, reflecting institutional biases toward secular norms, while underrepresenting the ritual's centrality to Jewish continuity amid declining circumcision rates among non-religious U.S. Jews (from 90% in the 1970s to about 70% by 2020)." | F026 Poisoning the Well | pro-circumcision | Uncited. Says mainstream autonomy-focused portrayals reflect 'institutional biases toward secular norms', so the opposing coverage is discounted by imputed motive without evidence. (sentence 180) |

Flag tally by side (simple count of the table above): pro-circumcision 4.

## Both-sides balance note

Same-standard check: critics' ethical claims (108-116) are attributed ('Critics contend', 'Ethicists argue', 'Human rights scholars'), and their figures are reported as theirs (the 20,000-70,000 nerve-ending figure, 112, conflicts with the 1,000-10,000 figure in the foreskin article). In the article's voice, benefit claims get causal and lifelong language (94, 97, 98), while opposing views get motive attributions (180). The MBP section holds the ritual defenders to an evidence standard (122-127), and that standard is not applied to the article's own benefit claims.

## What wasn't checked

- Sentences outside the reading set (130 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Cross-article: meatal stenosis '<0.1%' (104) vs 5-20% and below 1% in the meatal-stenosis article.
- The 'benefits-to-risks ratios exceeding 100:1' claim (98) needs a source check; no verdict is given here.
