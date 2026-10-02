# Sophistry and fallacy scan: Female genital mutilation in New Zealand

- **Article:** Female genital mutilation in New Zealand
- **URL:** https://grokipedia.com/page/female_genital_mutilation_in_new_zealand
- **Snapshot file:** `topics/circumcision/articles/female-genital-mutilation-in-new-zealand/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 126/126 units read in full (126 paragraphs, 0 table rows).

## Verdict

Run 2 found 5 flags: 0 pro, 5 anti, and 0 neutral. The lean is anti. Main patterns were F040 Loaded Language (2); F034 False Cause (1); F010 Appeal to Ignorance (1); F026 Poisoning the Well (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation-in-new-zealand` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 4316 |
| Sentences (prose + list items; headings and tables excluded) | 121 |
| Sentences with no citation marker of their own | 27 (22%) |
| Paragraphs/list items with no citation marker at all | 6 of 45 |
| Table rows (not counted as sentences) | 4 |
| Sources listed in sources CSV | 34 |
| Distinct citation numbers used in text | 34 |
| Dangling citation numbers (used, no source row) | 0: none |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 1 | 0.2 | unique (1) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 0 | 0.0 | none |
| MOS:WTW expressions of doubt | 2 | 0.5 | purported (2) |
| MOS:WTW editorializing | 4 | 0.9 | only (4) |
| MOS:WTW connectives (but/despite/however...) | 28 | 6.5 | but (8), while (7), though (6), despite (5), although (1) |
| MOS:WTW synonyms for 'said' | 7 | 1.6 | confirm (2), reveal (2), assert (1), claim (1), note (1) |
| Hyland 2005 hedges | 34 | 7.9 | often (8), rather (8), claims (6), may (3), argue (2) |
| Hyland 2005 boosters | 8 | 1.9 | must (2), establish (1), established (1), never (1), shown (1) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "This scarcity reflects effective legal deterrence and low cultural entrenchment, though latent risks persist without rigorous enforcement of assimilation norms for harmful imported traditions." | F034 False Cause | anti | Credits the absence of documented cases to legal deterrence without evidence. The article later concedes zero convictions suggest 'either rarity or effective concealment'. |
| 2 | "General criminal laws against assault existed but did not explicitly address FGM, permitting unchecked perpetuation among unassimilated groups and revealing early policy shortcomings in monitoring cultural practices incompatible with New Zealand's legal norms." | F040 Loaded Language | anti | Claims 'unchecked perpetuation' before 1996 while the article itself reports no documented instances, so the loaded framing outruns the evidence. |
| 3 | "Such caution is warranted, as anecdotal reports and international precedents indicate that low detection rates often mask ongoing occurrences in diaspora settings, necessitating better integration of immigration data with health and welfare records to address evidentiary voids." | F010 Appeal to Ignorance | anti | Treats the lack of detected cases as a sign of hidden cases, a position the evidence cannot falsify. |
| 4 | "In practice, community-led dialogues in New Zealand, often promoted by left-leaning tolerance advocates, have yielded mixed results; while some Somali leaders collaborated with health educators to reframe FGM as unnecessary for cultural identity, achieving near-universal rejection within targeted groups, others reveal persistent rationalizations that excuse harm under diversity guises, eroding protections for girls by deferring to offender communities rather than enforcing assimilation to host norms." | F026 Poisoning the Well | anti | Discredits community-dialogue approaches by a political label rather than by their results, which the same sentence reports as partly successful. |
| 5 | "Downplaying views, prevalent in advocacy circles, rely on rarity claims but overlook how policy-driven inflows from non-assimilating sources inherently heighten odds, prioritizing volume over vetting efficacy." | F040 Loaded Language | anti | In the article's own voice, loaded framing ('non-assimilating sources', 'inherently') dismisses the rarity evidence, which is the article's own official data. |

## Both-sides balance note

Run 2 flag counts by side: pro 0, anti 5, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
