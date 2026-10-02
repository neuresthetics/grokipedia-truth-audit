> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: _Khitan_ (circumcision)

- **Article:** _Khitan_ (circumcision)
- **URL:** https://grokipedia.com/page/Khitan_(circumcision)
- **Snapshot file:** `topics/circumcision/articles/khitan-circumcision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 45 of 170 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The religious and jurisprudential sections attribute positions to the schools that hold them (Hanbali, Shafi'i, Twelver Shia, Bohra, Ahmadiyya), and the consent debate gives both critics and proponents attributed space (130-148). The four flags are mostly in the article's own statements about medical evidence. The lead applies adult HIV-trial results to a 'benefits outweighing ... when performed neonatally' conclusion, and it dismisses sexual-function harm claims as 'anecdotal assertions'. The FGC-distinction section credits RCTs with UTI and penile-cancer findings that come from observational data. On the other side, one sentence pre-discredits existing pain research as shaped by 'institutional biases favoring minimal intervention narratives'. Lean: 3 pro, 1 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug khitan-circumcision` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5961 |
| Sentences (prose + list items; headings and tables excluded) | 178 |
| Sentences with no citation marker of their own | 32 (18%) |
| Paragraphs/list items with no citation marker at all | 0 of 64 |
| Table rows (not counted as sentences) | 5 |
| Sources listed in sources CSV | 111 |
| Distinct citation numbers used in text | 111 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 7 | 1.2 | celebrated (2), leading (2), honorable (1), notable (1), prominent (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 1 | 0.2 | is widely regarded as (1) |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 4 | 0.7 | only (4) |
| MOS:WTW connectives (but/despite/however...) | 64 | 10.7 | though (22), but (19), while (16), despite (4), however (3) |
| MOS:WTW synonyms for 'said' | 4 | 0.7 | confirm (2), note (1), observe (1) |
| Hyland 2005 hedges | 67 | 11.2 | often (16), rather (8), approximately (5), around (5), typically (5) |
| Hyland 2005 boosters | 20 | 3.4 | certain (4), known (4), established (3), demonstrated (2), must (2) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Empirical medical evidence indicates that male circumcision reduces risks of urinary tract infections in infancy, penile cancer, and heterosexual HIV acquisition by up to 60% in high-prevalence areas, with benefits outweighing rare complications like bleeding or adhesions when performed neonatally under sterile conditions. [3] [4]" | F011 Hasty Generalization | pro-circumcision | Lists HIV reduction 'by up to 60% in high-prevalence areas' (adult VMMC trials) among the benefits, then concludes 'benefits outweighing rare complications ... when performed neonatally'. Adult trial results feed a neonatal conclusion, following the convention flagged elsewhere in this audit. (sentence 5) |
| 2 | "No robust data supports claims of diminished sexual function or satisfaction post-circumcision, countering anecdotal assertions of harm. [5]" | F026 Poisoning the Well | pro-circumcision | 'No robust data supports claims of diminished sexual function ... countering anecdotal assertions of harm'. The opposing evidence is pre-labelled 'anecdotal' in the article's voice. Elsewhere in this set (foreskin 9, foreskin-man 70), the evidence is described as 'mixed' or 'conflicting'. (sentence 6) |
| 3 | "Empirical health outcomes further delineate the practices: randomized controlled trials demonstrate that male circumcision, including khitan when performed medically, reduces heterosexual HIV acquisition by approximately 60%, lowers urinary tract infection rates in infancy by up to 90%, and decreases risks of penile cancer and certain sexually transmitted infections like herpes (28-34% reduction). [66] [97]" | F032 Cum Hoc | pro-circumcision | 'Randomized controlled trials demonstrate that male circumcision ... lowers urinary tract infection rates in infancy by up to 90%, and decreases risks of penile cancer'. UTI and penile-cancer figures come from observational and meta-analytic data (see 111-112 in this article), so RCT-level causal standing is extended to them. Only the HIV and herpes figures are from trials. (sentence 152) |
| 4 | "Despite these advancements, gaps persist in resource-limited areas where traditional practitioners may prioritize ritual speed over analgesia, underscoring the need for education on evidence-based methods; peer-reviewed analyses indicate that unaddressed pain in khitan correlates with higher incidence of immediate behavioral sequelae, though long-term psychological impacts require further longitudinal research free from institutional biases favoring minimal intervention narratives. [44]" | F026 Poisoning the Well | anti-circumcision | Calls for research 'free from institutional biases favoring minimal intervention narratives', which pre-discredits the existing literature by alleged motive without identifying a specific bias. (sentence 85) |

Flag tally by side (simple count of the table above): anti-circumcision 1; pro-circumcision 3.

## Both-sides balance note

Same-standard check: harm-side claims in this article are hedged ('potential', 'requires further longitudinal research', 81, 85, 128), while benefit claims are stated firmly and, in sentence 152, given the wrong evidence tier. Critics' rights arguments (130-132, 145-146) and proponents' counters (147) are both attributed, including the proponents' 'absolutist interpretations' phrase (147), which is attributed and not counted. Sentence 135's 'negligible psychological regret' is attributed to the religious perspective and needs a source check.

## What wasn't checked

- Sentences outside the reading set (125 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Extraction artifact in sentence 118 ('00113-8/abstract)').
- The Kashmiri cohort complication figures (67, 70) were not checked.
