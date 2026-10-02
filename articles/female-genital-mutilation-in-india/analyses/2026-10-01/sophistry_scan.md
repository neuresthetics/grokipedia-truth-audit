# Sophistry and fallacy scan: Female genital mutilation in India

- **Article:** Female genital mutilation in India
- **URL:** https://grokipedia.com/page/Female_genital_mutilation_in_India
- **Snapshot file:** `articles/female-genital-mutilation-in-india/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (6 sentences) read in full, plus 45 of 195 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

This article is more two-sided than most in the set. It describes Bohra community framing ('small prick', 'minuscule nick') and survivor-led data, and it notes selection bias on both sides (sentences 83, 196). The reasoning faults run both ways. On the anti-cutting side, global Type I studies are used to state that hood-only khatna 'yields the same core harms', and a data-gap sentence still 'affirms' a conclusion. On the pro-practice side, the UN position is labelled 'absolutism', and the closing sentences make policy wait for randomized or decades-long cohort evidence, which is a standard nothing in this area can meet. An uncited 'exclusively' claim rests on absence of evidence, and other sentences say data elsewhere is 'undocumented'. Lean: 2 pro-cutting, 2 anti, 1 neutral/structural. These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-india` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 7243 |
| Sentences (prose + list items; headings and tables excluded) | 201 |
| Sentences with no citation marker of their own | 35 (17%) |
| Paragraphs/list items with no citation marker at all | 0 of 74 |
| Table rows (not counted as sentences) | 0 |
| Sources listed in sources CSV | 96 |
| Distinct citation numbers used in text | 97 |
| Dangling citation numbers (used, no source row) | 1: 97 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.1 | unique (1) |
| MOS:WTW contentious labels | 8 | 1.1 | sect (8) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.3 | purported (2) |
| MOS:WTW editorializing | 3 | 0.4 | only (3) |
| MOS:WTW connectives (but/despite/however...) | 50 | 6.9 | despite (15), though (12), while (11), but (9), however (3) |
| MOS:WTW synonyms for 'said' | 8 | 1.1 | assert (2), claim (2), confirm (2), deny (1), reveal (1) |
| Hyland 2005 hedges | 103 | 14.2 | rather (19), often (17), may (11), claims (10), indicate (9) |
| Hyland 2005 boosters | 16 | 2.2 | known (8), established (4), certain (2), demonstrated (1), found (1) |

## Flags

Side labels: the task's three labels are kept. In this article, which is mainly about female genital cutting, 'pro-circumcision' marks a flag whose reasoning makes genital cutting (or male circumcision, where it is compared) look more acceptable or benign, or makes its critics look less credible. 'anti-circumcision' marks a flag whose reasoning makes genital cutting look worse or its defenders less credible. 'neutral/structural' marks flags that favor neither.

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "This tension underscores a causal divide: UN absolutism assumes uniform harm across contexts, yet empirical gaps in Asia-specific prevalence data—reliant on self-reported surveys—limit verification, with India's non-endorsement of targeted conventions preserving space for community defenses rooted in religious freedom. [13]" | F040 Loaded Language | pro-circumcision | The article's voice labels the UN position 'UN absolutism' that 'assumes uniform harm'. This applies, in reverse, the same convention used across this audit for 'absolutist' labels on integrity arguments. (sentence 173) |
| 2 | "Resolving these debates demands rigorous, ideologically neutral investigations prioritizing causal inference—such as randomized or cohort designs assessing fertility, sexual function, and mental health metrics over decades—over reliance on polarized narratives from either rights advocates or cultural defenders." | F080 Nirvana Fallacy | pro-circumcision | Uncited. Asks for 'randomized or cohort designs ... over decades' before the debate can be resolved; with sentence 201, policy is to wait until such evidence exists. Randomizing girls to cutting is not ethically possible, so the standard cannot be met, and existing evidence is set aside for want of a perfect study. (sentence 199) |
| 3 | "Despite these trends, gaps in standardized prevalence surveys—reliant on self-reported data from biased community sources—persist, complicating causal attribution but affirming that medical involvement does not alter the procedure's inherent risks. [58]" | F034 False Cause | anti-circumcision | The sentence grants that data gaps are 'complicating causal attribution', then draws a firm conclusion from the same gap ('affirming that medical involvement does not alter the procedure's inherent risks'). The conclusion does not follow from the premise given. (sentence 182) |
| 4 | "Despite these shifts, medicalized khatna—typically involving clitoral hood removal—yields the same core harms as non-medical forms, including acute pain, bleeding, infection risks, and long-term complications like scarring, sexual dysfunction, and psychological trauma, as evidenced by global studies on Type I FGM/C. [92]" | F022 Accident | anti-circumcision | Hood-only khatna is said to yield 'the same core harms' as non-medical forms, 'as evidenced by global studies on Type I FGM/C'. Type I includes clitoridectomy, so findings from the broader category are applied to the narrower hood-only case. Sentence 196 says India-specific outcome data are scarce. (sentence 189) |
| 5 | "No credible evidence links FGM to non-Muslim communities, including Hindu castes or tribal groups, despite occasional unsubstantiated assertions in advocacy literature; the practice's persistence is tied exclusively to specific Islamic interpretive traditions within insular sects like the Dawoodi Bohras, without extension to broader Indian Muslim demographics or other religious groups." | F010 Appeal to Ignorance | neutral/structural | Uncited. 'No credible evidence links...' is turned into 'tied exclusively to specific Islamic interpretive traditions', a strong universal claim drawn from absence of evidence. Sentence 43 calls prevalence elsewhere 'negligible or undocumented', and sentence 197 mentions 'other Muslim subgroups'. (sentence 44) |

Flag tally by side (simple count of the table above): anti-circumcision 2; neutral/structural 1; pro-circumcision 2.

## Both-sides balance note

Same-standard check: this article applies its selection-bias caveat to both sides: activist-led surveys (83) and community-insider reports (196). That is the even-handed treatment several other articles lack. The asymmetry left over is the closing evidentiary bar (199-201), which works in favor of the status quo (the practice continuing). Male-circumcision comparisons: sentence 12 states MC benefits with a 'high-prevalence settings' scope qualifier, which is properly limited; sentence 163 attributes to the defending organization the argument that MC remains 'unregulated despite analogous bodily alteration'. Neither was flagged.

## What wasn't checked

- Sentences outside the reading set (150 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- The 2025 events (CJI remarks, WHO/FIGO 'Do No Harm' statement) were not checked against sources.
