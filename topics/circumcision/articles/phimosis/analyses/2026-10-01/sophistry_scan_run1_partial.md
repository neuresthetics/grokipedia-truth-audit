> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Phimosis

- **Article:** Phimosis
- **URL:** https://grokipedia.com/page/Phimosis
- **Snapshot file:** `topics/circumcision/articles/phimosis/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 255 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This clinical article is mostly guideline-based, emphasizing conservative management of physiological phimosis and recommending against forced retraction, with surgery reserved for refractory cases. The circumcision debate (221-229) and the medical-versus-cultural section (232-239) give both sides attributed space. Three flags were found. Two are pro-circumcision: general infant circumcision UTI data is applied to phimosis 'affected age groups', and the article concludes that circumcising societies have 'lower morbidity' and that culture 'causally shape[s]' epidemiology. Part of that conclusion is true by definition, since circumcised males cannot have phimosis. One is anti-circumcision: a survey of parental expectations is taken as showing that cultural bias 'drive[s] unnecessary interventions'. Lean: 2 pro, 1 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug phimosis` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 7595 |
| Sentences (prose + list items; headings and tables excluded) | 261 |
| Sentences with no citation marker of their own | 69 (26%) |
| Paragraphs/list items with no citation marker at all | 7 of 76 |
| Table rows (not counted as sentences) | 11 |
| Sources listed in sources CSV | 107 |
| Distinct citation numbers used in text | 107 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 0 | 0.0 | none |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 7 | 0.9 | only (5), notably (2) |
| MOS:WTW connectives (but/despite/however...) | 58 | 7.6 | but (22), though (21), while (8), however (4), despite (3) |
| MOS:WTW synonyms for 'said' | 5 | 0.7 | confirm (2), expose (2), explain (1) |
| Hyland 2005 hedges | 140 | 18.4 | often (27), may (23), typically (19), approximately (10), rather (10) |
| Hyland 2005 boosters | 20 | 2.6 | found (4), must (4), true (3), demonstrate (2), shows (2) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Over time, phimosis elevates the risk of urinary tract infections (UTIs), particularly in males, as incomplete foreskin retraction impedes hygiene and allows bacterial colonization under the prepuce, with studies indicating a protective effect from circumcision reducing UTI incidence by factors of 6.6- to 10-fold in affected age groups. [36] [37]" | F022 Accident | pro-circumcision | Phimosis-related UTI risk is supported with 'a protective effect from circumcision reducing UTI incidence by factors of 6.6- to 10-fold'. These are general infant and child circumcision figures (compare the foreskin article, 139-141), and they are applied to phimosis without phimosis-specific data. (sentence 106) |
| 2 | "These variations highlight how cultural and religious practices causally shape phimosis epidemiology, with empirical data from global surveys confirming lower morbidity in circumcising societies. [81] [83]" | F032 Cum Hoc | pro-circumcision | 'Cultural and religious practices causally shape phimosis epidemiology, with empirical data ... confirming lower morbidity in circumcising societies'. Fewer phimosis cases among circumcised people is true by definition (see 205), and the jump to general 'lower morbidity' and causal language goes beyond what the article shows. (sentence 216) |
| 3 | "Empirical data indicate that in uncircumcised cohorts, self-resolved or conservatively managed cases predominate, challenging claims of universal medical necessity and highlighting how cultural biases—such as parental expectations of early retraction by age 1 in 66% of surveyed families—drive unnecessary interventions despite evidence of natural resolution. [91] [83]" | F034 False Cause | anti-circumcision | From a survey that '66% of surveyed families' expected early retraction, it concludes 'cultural biases ... drive unnecessary interventions'. Parental expectations are not shown to cause interventions, and no intervention-rate data is tied to them in the sentence. (sentence 238) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 2.

## Both-sides balance note

Same-standard check: the circumcision subsection presents critics (224, 225) and proponents (228) with attribution. Sentence 229 then sides with the critics in the article's voice ('evidence from controlled trials indicating minimal long-term health gains'); this was not flagged but needs a source check. Pro-side scope transfer (106) and anti-side causal inference (238) were each counted once. Harm claims (222: 'as reported in some studies') are hedged.

## What wasn't checked

- Sentences outside the reading set (210 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Phimosis prevalence figures ('1% to 3.4%', 232, vs 'around 13-14%', 235) were not reconciled.
- The controlled-trial evidence claimed in 229 needs a source check; no verdict is given here.
