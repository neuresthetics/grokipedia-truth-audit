> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: History of circumcision

- **Article:** History of circumcision
- **URL:** https://grokipedia.com/page/History_of_circumcision
- **Snapshot file:** `topics/circumcision/articles/history-of-circumcision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (7 sentences) read in full, plus 45 of 173 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This history article is cautious about early evidence. It marks Egyptian prehistoric evidence as 'inferential', and it criticizes 19th- and 20th-century medical claims as correlational, anecdotal or lacking controls (119, 122, 128, 130, 131). Four flags were found. Two are pro-circumcision: in the modern-benefits section, mechanism and causal language ('due to reduced phimosis', 'causal reduction of viral entry points') is stated for findings the article does not show to be mechanistic, so the correlational standard applied to historical claims is not applied to modern ones. One is anti: 'medical entrepreneurship' is named as a cause of US prevalence. One is structural: the lead states the Abrahamic covenant as a dated historical event. Lean: 2 pro, 1 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug history-of-circumcision` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6036 |
| Sentences (prose + list items; headings and tables excluded) | 180 |
| Sentences with no citation marker of their own | 34 (19%) |
| Paragraphs/list items with no citation marker at all | 1 of 56 |
| Table rows (not counted as sentences) | 6 |
| Sources listed in sources CSV | 119 |
| Distinct citation numbers used in text | 119 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.5 | prominent (2), great (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 3 | 0.5 | alleged (1), apparent (1), purported (1) |
| MOS:WTW editorializing | 4 | 0.7 | only (4) |
| MOS:WTW connectives (but/despite/however...) | 61 | 10.1 | but (20), though (17), while (12), despite (7), however (4) |
| MOS:WTW synonyms for 'said' | 3 | 0.5 | confirm (1), expose (1), reveal (1) |
| Hyland 2005 hedges | 76 | 12.6 | rather (16), around (11), approximately (9), often (8), typically (5) |
| Hyland 2005 boosters | 13 | 2.2 | shows (3), clear (2), demonstrated (2), known (2), certain (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Parallel research reaffirmed broader health benefits, including a 10-fold reduction in urinary tract infections (UTIs) in infancy, lower incidence of human papillomavirus (HPV) and herpes simplex virus type 2 (HSV-2) infections (30-40% and 28-34% reductions, respectively), and decreased penile cancer risk due to reduced phimosis and chronic inflammation. [93]" | F032 Cum Hoc | pro-circumcision | 'Decreased penile cancer risk due to reduced phimosis and chronic inflammation': a causal pathway is stated for an observational association. Sentence 131 rejects earlier cancer claims for resting 'on correlational data ... rather than causal trials', a standard not applied here. (sentence 154) |
| 2 | "Despite implementation challenges like supply shortages and demand generation, the evidence prompted integrations with other HIV strategies, including pre-exposure prophylaxis, underscoring circumcision's role in causal reduction of viral entry points rather than mere correlation. [96]" | F034 False Cause | pro-circumcision | Programme integration with PrEP is said to underscore 'circumcision's role in causal reduction of viral entry points rather than mere correlation'. Policy uptake is not evidence of a mechanism. The trials established an effect, and the 'viral entry points' mechanism is asserted rather than shown. (sentence 158) |
| 3 | "This divergence highlighted US exceptionalism, where cultural momentum and medical entrepreneurship entrenched the practice despite sparse empirical support for universal application, contrasting with earlier declines in other Anglophone contexts. [81]" | F033 Causal Oversimplification | anti-circumcision | Attributes US persistence to 'cultural momentum and medical entrepreneurship'. A motive-laden single explanation ('entrepreneurship') is given in the article's voice, without evidence shown for that cause over others. (sentence 136) |
| 4 | "The practice spread among Semitic peoples and was formalized in Judaism as the brit milah, a covenantal commandment given to Abraham around 1800 BCE, mandating the procedure on the eighth day after birth as an eternal sign of God's pact with the Jewish people. [2]" | F004 Appeal to Authority | neutral/structural | States as dated history that brit milah was 'a covenantal commandment given to Abraham around 1800 BCE ... an eternal sign of God's pact'. Tradition's authority is used as the source for a historical claim; it is not marked as the tradition's own account. Sentence 44 acknowledges that the archaeological evidence is indirect. (sentence 2) |

Flag tally by side (simple count of the table above): anti-circumcision 1; neutral/structural 1; pro-circumcision 2.

## Both-sides balance note

Same-standard check: historical pro-circumcision claims are held to a strict standard (correlational, no RCTs, anecdotal: 119-131), but modern observational benefits (HPV, HSV-2, penile cancer: 138-139, 154) are reported without that caveat. The HIV RCTs (141-149) are accurately described as adult VMMC trials. Ethical critics and proponents (159-161) are both attributed, and the proponents' benefits are qualified 'in high-prevalence areas'.

## What wasn't checked

- Sentences outside the reading set (128 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The claim that PACE Resolution 1952 'was later rescinded in 2015' (165) needs a source check; no verdict is given here.
- The 2011 San Francisco measure is named 'Proposition F' here; other articles in this set call it 'Proposition B'. This was not resolved.
