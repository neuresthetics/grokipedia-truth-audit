# Sophistry and fallacy scan: Ashley Montagu Resolution

- **Article:** Ashley Montagu Resolution
- **URL:** https://grokipedia.com/page/ashley_montagu_resolution
- **Snapshot file:** `articles/ashley-montagu-resolution/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9, `fallacyScanPass` (67 kept entries from geometric_fallacy_engine v0.1.0; engine IDs kept). Both-sides by default. Sophistry and reasoning pass only; no outside fact-checking.
- **Reading coverage:** lead (5 sentences) read in full, plus 45 of 184 body sentences picked by `tools/sophistry_triage.py` (cue-word score, cap 45). Other sentences were not read closely.

## Verdict

The article describes an advocacy document, so much of the anti-circumcision language ('mutilation', 'torture', 'myths') is the resolution's own wording, correctly attributed, and is not flagged here. The problems are in the article's evaluation sections. It answers the resolution's claims about infant circumcision with adult HIV-trial results from high-prevalence settings. It asks for 'robust evidence of causation' for harms but not for benefits. It gives critics of the resolution the last, evaluative word ('ideological parity', 'absolutist integrity claims'). One flag goes the other way: observational FGM cohort data described as showing 'causal harms'. On the sentences read, the flags lean pro-circumcision (7 of 9). These are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug ashley-montagu-resolution` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 6835 |
| Sentences (prose + list items; headings and tables excluded) | 189 |
| Sentences with no citation marker of their own | 40 (21%) |
| Paragraphs/list items with no citation marker at all | 2 of 62 |
| Table rows (not counted as sentences) | 1 |
| Sources listed in sources CSV | 59 |
| Distinct citation numbers used in text | 59 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.1 | notable (1) |
| MOS:WTW contentious labels | 1 | 0.1 | myth (1) |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 3 | 0.4 | purported (3) |
| MOS:WTW editorializing | 3 | 0.4 | only (2), notably (1) |
| MOS:WTW connectives (but/despite/however...) | 55 | 8.0 | while (18), though (16), but (10), despite (7), however (4) |
| MOS:WTW synonyms for 'said' | 2 | 0.3 | confirm (1), expose (1) |
| Hyland 2005 hedges | 52 | 7.6 | rather (16), often (8), claims (7), argue (3), argued (3) |
| Hyland 2005 boosters | 10 | 1.5 | certain (3), show (2), demonstrated (1), established (1), known (1) |

## Flags

Every flag below is a **judgment call** (model reading against the engine entry's detection cue), not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false. Quotes are verbatim snapshot sentences, citation markers included (checked by `sophistry_counts.py --verify-quotes`).

| # | Quoted sentence | Type (engine ID, name) | Favors | Explanation (judgment call) |
|---|---|---|---|---|
| 1 | "Though it secured endorsements from figures like Francis Crick and Jonas Salk and aimed to mobilize heads of state and organizations like Amnesty International, the petition yielded no formal ICJ ruling, and its undifferentiated condemnation of male neonatal circumcision as mutilation has drawn criticism for overlooking empirical evidence of benefits, including a 50–60% reduction in heterosexual HIV acquisition and lower urinary tract infection rates, as affirmed by health authorities in high-prevalence contexts. [2] [3] [4]" | F011 Hasty Generalization | pro-circumcision | Lead rebuts a condemnation of male neonatal circumcision with a 50-60% HIV reduction found in adult heterosexual trials in high-prevalence settings. The finding is moved from its population to infants generally without a bridging step (converse accident). (sentence 5) |
| 2 | "Key limitations stemmed from evidentiary and framing challenges: the resolution's categorical condemnation overlooked systematic reviews documenting net health benefits for neonatal male circumcision, including 50-60% reductions in heterosexual HIV acquisition and lower urinary tract infection risks in infancy." | F011 Hasty Generalization | pro-circumcision | Uncited (code count); same move in the article's own voice: 'net health benefits for neonatal male circumcision, including 50-60% reductions in heterosexual HIV acquisition', a figure from adult trials. (sentence 134) |
| 3 | "Long-term risks, such as meatal stenosis or reduced sexual sensitivity, lack robust evidence of causation; meta-analyses of sexual function studies show no significant differences between circumcised and uncircumcised men. [43]" | F036 Suppressed Evidence | pro-circumcision | Requires 'robust evidence of causation' for long-term risks, but sentence 171 accepts 'net health benefits' from meta-analyses that include observational data. The evidence standard differs by side. (sentence 156) |
| 4 | "Proponents invoke John Stuart Mill's harm principle, noting male circumcision's net health benefits—reduced urinary tract infections, penile cancer, and STIs per meta-analyses—outweigh speculative autonomy violations, unlike FGM's universally condemned harms, and argue state bans erode multicultural tolerance without empirical evidence of widespread regret among circumcised adults. [52]" | F040 Loaded Language | pro-circumcision | Proponents are said to be 'noting' net benefits (MOS:WTW: 'note' implies the statement is true), while autonomy concerns are described inside the same sentence as 'speculative'. Attribution softens this, but the verb choice is the article's. (sentence 171) |
| 5 | "Ultimately, while the resolution amplified calls for universal genital autonomy, opponents maintained that causal realism demands proportionate condemnation based on verifiable harms, not ideological parity. [38]" | F040 Loaded Language | pro-circumcision | 'Ultimately' gives the closing, evaluative word to opponents, and their framing ('causal realism' vs 'ideological parity') labels the resolution's position as ideology rather than describing it. (sentence 149) |
| 6 | "Thus, while sharing rhetorical appeals to universal children's rights, the Montagu Resolution's comprehensive scope has limited uptake compared to siloed FGM advocacy, highlighting tensions between cultural relativism and absolutist integrity claims." | F040 Loaded Language | pro-circumcision | Uncited summary calls the resolution's position 'absolutist integrity claims': a pejorative label in the article's own voice, with no comparable label for the other side. (sentence 189) |
| 7 | "It contributed to the rhetorical foundation of intactivism, influencing niche discourse on infant bodily autonomy, yet failed to spur measurable declines in global practices; for instance, male circumcision rates persisted at approximately 38% worldwide as of 2007 estimates, driven by religious traditions in Judaism, Islam, and select African contexts." | F034 False Cause | pro-circumcision | Uncited; concludes the resolution 'failed to spur measurable declines' from a single 2007 global estimate, with no baseline, trend or counterfactual. (sentence 132) |
| 8 | "Empirical data from cohort studies, such as increased cesarean needs (OR 1.3-2.0) in cut women, underscored causal harms, shifting discourse from relativism to rights-based realism. [16]" | F032 Cum Hoc | anti-circumcision | Cohort (observational) odds ratios are said to have 'underscored causal harms'. This is the same correlation-to-cause step the scan flags on the pro side; it is applied here to FGM harms. (sentence 29) |
| 9 | "Intactivist networks in the U.S. and Europe petitioned against non-consensual procedures, while global FGM campaigns, supported by Egyptian feminist Nawal El Saadawi's exposés on lifelong dyspareunia and obstetric fistula risks (prevalence up to 30% in infibulated women), gained traction despite biases in some UN-affiliated reports that conflated criticism with imperialism. [15]" | F040 Loaded Language | anti-circumcision | Asserts 'biases in some UN-affiliated reports that conflated criticism with imperialism' without naming the reports or the bias. This discounts the relativist side by label rather than by content. (sentence 28) |

Flag tally by side (simple count of the table above): anti-circumcision 2; pro-circumcision 7.

## Both-sides balance note

Same-standard check: the resolution's anti-circumcision assertions ('all forms of child genital modification inflict irreversible physical and psychological harm', 'unsubstantiated benefits') are reported as the resolution's claims and not endorsed in the article's voice, so they are not flagged. The pro side's rebuttals are often stated in the article's voice (sentences 134, 156, 189), and some are uncited. The FGM/male-circumcision distinction is presented mostly through critics (sentences 140, 143, 187), which is attribution, not a fallacy; but no sentence read gives the resolution's reply to the 'false equivalence' objection. Shortfall: the pro side gets institutional backing (AAP, CDC, WHO) in several places, while the resolution's evidence is described only as 'symposium proceedings' and 'anecdotal and preliminary survey data'.

## What wasn't checked

- Sentences outside the reading set (139 body sentences) were not read closely; flags may exist there.
- No claim was fact-checked against outside sources, and no cited source was opened. Where a flag says a claim needs a source check, no verdict is given.
- Whether a cited source actually supports the sentence it is attached to.
- Tables were not scanned for flags (their rows are counted only).
- No gate, XNOR or truth-table computation was run on any argument; no fallacy flag is a computed result. No scores or confidence grids are given.
- Code-checkable engine entries (F063-F070, F072) were not run: no argument here was put into formal syllogistic or probabilistic shape.
- Whether the resolution text itself says what the article attributes to it (no primary text was opened).
