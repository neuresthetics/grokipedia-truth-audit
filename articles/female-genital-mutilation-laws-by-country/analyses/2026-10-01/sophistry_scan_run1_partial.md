> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Female genital mutilation laws by country

- **Article:** Female genital mutilation laws by country
- **URL:** https://grokipedia.com/page/Female_genital_mutilation_laws_by_country
- **Snapshot file:** `articles/female-genital-mutilation-laws-by-country/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (5 sentences) read in full, plus 45 of 238 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is mostly a legal survey (international instruments, national bans, extraterritorial laws, prosecution data) and largely descriptive. Its 'Empirical Evidence on Impact' section is notably balanced: it reports the 2012 Campbell review's null finding, the 2023 review's 'legislation alone fails', and a time-series study estimating a 7.6-point reduction, each with limitations (171-177). One flag was found in the sentences read: an uncited article-voice conclusion that 'causal analysis favors universalism'. An internal inconsistency was noted: sentence 4 says Gambian 'courts upheld criminalization in 2024', while sentence 228 says the National Assembly rejected the repeal bill. Lean: 0 pro, 1 anti, 0 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-laws-by-country` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 8547 |
| Sentences (prose + list items; headings and tables excluded) | 243 |
| Sentences with no citation marker of their own | 71 (29%) |
| Paragraphs/list items with no citation marker at all | 3 of 77 |
| Table rows (not counted as sentences) | 34 |
| Sources listed in sources CSV | 155 |
| Distinct citation numbers used in text | 155 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 4 | 0.5 | landmark (2), leading (1), pioneering (1) |
| MOS:WTW contentious labels | 1 | 0.1 | controversial (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 6 | 0.7 | only (6) |
| MOS:WTW connectives (but/despite/however...) | 92 | 10.8 | but (30), though (21), despite (19), while (17), however (4) |
| MOS:WTW synonyms for 'said' | 1 | 0.1 | confirm (1) |
| Hyland 2005 hedges | 80 | 9.4 | often (26), rather (12), indicate (6), may (6), estimated (5) |
| Hyland 2005 boosters | 22 | 2.6 | certain (5), show (5), known (3), established (2), found (2) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Ultimately, causal analysis favors universalism, as relativist tolerance sustains intergenerational harm without verifiable compensatory cultural gains." | F061 Is-Ought Jump | anti-circumcision | Uncited (code count). 'Ultimately, causal analysis favors universalism'. Universalism versus relativism is a normative question; causal findings about harm feed into it but cannot settle it, and no causal analysis of the two policies is presented. (sentence 203) |

Flag tally by side (simple count of the table above): anti-circumcision 1.

## Both-sides balance note

Same-standard check: evidence that laws do not work (171, 172) and evidence that they do (174) are both reported with caveats, which is the even-handed treatment. Harm-reduction ('symbolic pricking', 28) and pro-medicalization (32) positions are attributed and then answered. Sentence 32's 'gender-based control mechanisms absent in male counterparts' asserts male/female non-equivalence in passing; it is cited and was not flagged, but it is the same kind of aside flagged as uncited in the New Zealand and FGM Act 2003 articles.

## What wasn't checked

- Sentences outside the reading set (193 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Gambia 2024: 'courts upheld' (4) vs Assembly rejected the bill (228). This needs a source check; no verdict is given here.
- Per-country legal details (penalties, dates) in the country sections were not individually checked.
