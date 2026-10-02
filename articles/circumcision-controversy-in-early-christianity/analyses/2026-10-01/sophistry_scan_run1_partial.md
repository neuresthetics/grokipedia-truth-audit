> Run 1: partial read (about 30% of sentences, script-selected). Superseded by sophistry_scan.md (run 2, full read).
# Sophistry and fallacy scan: Circumcision controversy in early Christianity

- **Article:** Circumcision controversy in early Christianity
- **URL:** https://grokipedia.com/page/Circumcision_controversy_in_early_Christianity
- **Snapshot file:** `articles/circumcision-controversy-in-early-christianity/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (8 sentences) read in full, plus 45 of 153 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This is a history-of-religion article about whether Gentile converts had to be circumcised. It does not take a side in the modern medical or ethical debate, and Paul's harsh language ('mutilation', 'dogs') is correctly attributed to Paul. The reasoning flags are structural. The article presents theological narrative as empirical demonstration ('demonstrated empirically that God accepted uncircumcised Gentiles'). It credits the Council with a single causal role in Christianity's growth. It presents an interpretive reading as 'confirmed' by unnamed scholarship. It claims burial evidence supports 'universal male observance' even though, as the same sentence notes, soft tissue does not survive. All 5 flags are neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug circumcision-controversy-in-early-christianity` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 5636 |
| Sentences (prose + list items; headings and tables excluded) | 161 |
| Sentences with no citation marker of their own | 32 (20%) |
| Paragraphs/list items with no citation marker at all | 1 of 55 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 101 |
| Distinct citation numbers used in text | 101 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 4 | 0.7 | great (1), leading (1), unique (1), visionary (1) |
| MOS:WTW contentious labels | 3 | 0.5 | sect (3) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 0 | 0.0 | none |
| MOS:WTW editorializing | 6 | 1.1 | only (5), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 39 | 6.9 | but (20), while (13), though (4), despite (1), however (1) |
| MOS:WTW synonyms for 'said' | 3 | 0.5 | confirm (2), observe (1) |
| Hyland 2005 hedges | 51 | 9.0 | around (16), rather (13), would (6), often (4), likely (3) |
| Hyland 2005 boosters | 21 | 3.7 | true (6), certain (3), must (3), demonstrated (2), established (2) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This resolution, rooted in empirical observations of the Holy Spirit's work among uncircumcised believers, marked a causal pivot enabling Christianity's detachment from Judaism as a proselytizing sect, fostering exponential growth among pagans unbound by ritual prerequisites. [1]" | F033 Causal Oversimplification | neutral/structural | Attributes Christianity's separation from Judaism and its 'exponential growth' to this one resolution ('a causal pivot'), and calls observations of 'the Holy Spirit's work' empirical. Many other causes of the split are known and not mentioned in the sentence. (sentence 6) |
| 2 | "This event, occurring around AD 40, demonstrated empirically that God accepted uncircumcised Gentiles into the covenant community based on faith alone." | F004 Appeal to Authority | neutral/structural | Uncited (code count). The article's own voice says the Acts narrative 'demonstrated empirically that God accepted uncircumcised Gentiles'. A scriptural account is the only warrant for a claim presented as an empirical fact rather than as the text's or the participants' view. (sentence 111) |
| 3 | "The policy's causal effect was the acceleration of Christianity's demographic shift toward Gentile majorities, as evidenced by the proliferation of house churches in Asia Minor and Greece by the 50s CE, unhindered by the proselytizing bottlenecks that limited Judaism's convert pool to those willing to endure circumcision and dietary rigors. [91]" | F031 Post Hoc | neutral/structural | 'The policy's causal effect was the acceleration' of Gentile majorities, 'as evidenced by' the later spread of house churches. Growth that came after the decree is treated as caused by it, with no comparison. (sentence 140) |
| 4 | "In the Israelite context, however, it acquired unique covenantal significance, distinguishing Abraham's descendants from neighboring Semitic groups like Mesopotamians who did not practice it routinely; archaeological confirmation in Israelite remains is sparse due to the perishable nature of soft tissue, but textual and osteological inferences from burial practices align with biblical descriptions of universal male observance. [8] [11]" | F011 Hasty Generalization | neutral/structural | Concludes 'universal male observance' from 'textual and osteological inferences', in a sentence that itself says the evidence is 'sparse' because soft tissue perishes. The conclusion is stated more strongly than the evidence the sentence describes. Claim needs source check. (sentence 13) |
| 5 | "Scholarly analyses confirm this act as Jesus' initial shedding of blood in obedience to the law, prefiguring his ultimate sacrificial death. [28]" | F004 Appeal to Authority | neutral/structural | A theological interpretation (first shedding of blood 'prefiguring' the crucifixion) is presented as something 'scholarly analyses confirm'. Unnamed authority is used to turn an interpretive reading into a confirmed fact. (sentence 32) |

Flag tally by side (simple count of the table above): neutral/structural 5.

## Both-sides balance note

Same-standard check across the two historical parties: the Judaizers' position (sentences 57-62) and Paul's position (67-86) are both described largely through their own texts, and the Judaizers' view is not caricatured in the sentences read. The article does lean toward the Pauline/Council outcome in its own voice ('decisive', 'pragmatic minimalism', 'preserving the universality'), which reflects the subject's history rather than the modern circumcision debate. No sentence read argues for or against present-day circumcision, so the pro/anti-circumcision lean is not applicable here.

## What wasn't checked

- Sentences outside the reading set (108 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Biblical verse citations in the text were not checked against the texts cited.
