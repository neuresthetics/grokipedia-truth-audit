> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Brit shalom (naming ceremony)

- **Article:** Brit shalom (naming ceremony)
- **URL:** https://grokipedia.com/page/brit_shalom_naming_ceremony
- **Snapshot file:** `topics/circumcision/articles/brit-shalom-naming-ceremony/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (3 sentences) read in full, plus 34 of 103 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a mostly descriptive article about a minority ritual. It attributes positions fairly evenly: proponents' ethical and health reasons on one side, Orthodox and halakhic objections and AAP benefit claims on the other. Three reasoning flags were found in the sentences read. One discounts pro-Brit Shalom sources by their ties to advocacy (favors circumcision). Two favor the critical side: an ecological 'no epidemic' reply that answers a stronger claim than the critics made, and the article's own 'purported' attached to health benefits. On the sentences read, the flags lean slightly anti-circumcision (2 of 3). These are judgment calls, and the sample is small.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug brit-shalom-naming-ceremony` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 3826 |
| Sentences (prose + list items; headings and tables excluded) | 106 |
| Sentences with no citation marker of their own | 36 (34%) |
| Paragraphs/list items with no citation marker at all | 4 of 39 |
| Table rows (not counted as sentences) | 6 |
| Sources listed in sources CSV | 39 |
| Distinct citation numbers used in text | 39 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 2 | 0.5 | leading (1), unique (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 1 | 0.3 | officially (1) |
| MOS:WTW expressions of doubt | 1 | 0.3 | purported (1) |
| MOS:WTW editorializing | 0 | 0.0 | none |
| MOS:WTW connectives (but/despite/however...) | 33 | 8.6 | while (13), but (9), though (8), however (2), despite (1) |
| MOS:WTW synonyms for 'said' | 0 | 0.0 | none |
| Hyland 2005 hedges | 54 | 14.1 | often (12), rather (11), may (9), around (4), approximately (3) |
| Hyland 2005 boosters | 7 | 1.8 | show (2), certain (1), established (1), known (1), must (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Sources promoting Brit Shalom, often tied to anti-circumcision advocacy, highlight its alignment with modern ethics, yet Orthodox Judaism uniformly rejects it as insufficient for covenantal entry. [9] [10]" | F025 Guilt by Association | pro-circumcision | Sources are characterized by their association ('often tied to anti-circumcision advocacy') before their content is reported, and 'yet' sets Orthodox rejection against them. Association is offered as a reason for doubt. (sentence 13) |
| 2 | "Critics of Brit Shalom highlight that uncircumcised males face elevated risks of conditions like balanitis and phimosis, potentially requiring later interventions with higher complication rates, though long-term population studies in low-circumcision regions like Europe show no epidemic of such issues attributable to intact status. [30]" | F002 Straw Man | anti-circumcision | Critics claim elevated individual risk of balanitis/phimosis; the article's rebuttal is that Europe shows 'no epidemic' of such issues. That answers a stronger claim than the one made, and it uses population-level absence to answer an individual-risk point. (sentence 81) |
| 3 | "They contend that purported health benefits, such as reduced urinary tract infections (UTIs) in infancy and lower heterosexual HIV transmission rates later in life, can be mitigated through hygiene practices and safe sex, rendering the intervention unnecessary and disproportionate to its harms. [31]" | F040 Loaded Language | anti-circumcision | In paraphrasing proponents, the article's own wording 'purported health benefits' (MOS:WTW expression of doubt) casts doubt on benefits that sentence 80 reports as AAP findings. (sentence 79) |

Flag tally by side (simple count of the table above): anti-circumcision 2; pro-circumcision 1.

## Both-sides balance note

Same-standard check: the article attributes both sides' positions with similar verbs ('argue', 'contend', 'counter', 'maintain') in the sentences read. The AAP figures in sentence 80 ('randomized trials and meta-analyses shows ... 90% reduction in penile cancer') are attributed to AAP but need a source check, since the sentence does not say which outcomes the trials measured. Proponents' complication figure in sentence 78 ('rare but severe complications ... approximately 1-2%') reads as if severe complications occur at 1-2%; the sentence is ambiguous and needs a source check. Neither side's figures were verified here.

## What wasn't checked

- Sentences outside the reading set (69 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
