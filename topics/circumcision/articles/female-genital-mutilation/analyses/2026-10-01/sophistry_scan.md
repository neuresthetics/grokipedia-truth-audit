# Sophistry and fallacy scan: Female genital mutilation

- **Article:** Female genital mutilation
- **URL:** https://grokipedia.com/page/female_genital_mutilation
- **Snapshot file:** `topics/circumcision/articles/female-genital-mutilation/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 303/303 units read in full (293 paragraphs, 10 table rows).

## Verdict

Run 2 found 5 flags: 4 pro, 1 anti, and 0 neutral. The lean is pro. Main patterns were F036 Suppressed Evidence (2); F026 Poisoning the Well (1); F011 Hasty Generalization (1); F040 Loaded Language (1). Flags are judgment calls.

## Code counts

Produced by `python3 tools/sophistry_counts.py --date 2026-10-01 --slug female-genital-mutilation` (deterministic; no judgment). Term lists: `tools/term_lists/` (Wikipedia MOS:Words to watch, rev. 1376702503; Hyland 2005 hedges/boosters). A term hit is a prompt for reading, not evidence of bias.

| Count | Value |
|---|---|
| Words in prose (citations stripped) | 9833 |
| Sentences (prose + list items; headings and tables excluded) | 291 |
| Sentences with no citation marker of their own | 134 (46%) |
| Paragraphs/list items with no citation marker at all | 31 of 88 |
| Table rows (not counted as sentences) | 10 |
| Sources listed in sources CSV | 3 |
| Distinct citation numbers used in text | 76 |
| Dangling citation numbers (used, no source row) | 73: 4–76 |
| Sources listed but never cited | 0: none |

| Term list | Hits | Per 1,000 words | Most frequent |
|---|---|---|---|
| MOS:WTW puffery | 3 | 0.3 | honorable (3) |
| MOS:WTW contentious labels | 0 | 0.0 | none |
| MOS:WTW unsupported attributions | 1 | 0.1 | officially (1) |
| MOS:WTW expressions of doubt | 6 | 0.6 | purported (4), accused (1), alleged (1) |
| MOS:WTW editorializing | 5 | 0.5 | only (5) |
| MOS:WTW connectives (but/despite/however...) | 91 | 9.3 | but (29), though (22), while (22), despite (15), however (3) |
| MOS:WTW synonyms for 'said' | 11 | 1.1 | note (4), reveal (4), find (2), assert (1) |
| Hyland 2005 hedges | 119 | 12.1 | often (34), rather (19), indicate (8), around (6), claims (6) |
| Hyland 2005 boosters | 33 | 3.4 | certain (8), found (7), known (4), show (3), find (2) |

## Flags

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "A subset of ethicists critiques the nomenclature disparity with male genital cutting, positing gender bias in ethical framing—male procedures are normalized as "circumcision" despite non-consensual infant application, while FGM's all forms are pathologized—yet empirical comparisons reveal FGM's greater tissue loss (up to 80% in Type III) and zero net health gains, justifying the terminological distinction on harm-based grounds." | F036 Suppressed Evidence | pro | Uses the most extensive type (Type III) to justify one label for all FGM forms, including Type IV pricking that the article elsewhere calls minimal tissue removal. |
| 2 | "Psychological trauma, manifesting as PTSD symptoms, has been observed in longitudinal studies of survivors, though data quality varies due to underreporting in biased self-reports from advocacy-influenced surveys." | F026 Poisoning the Well | pro | Discounts psychological-trauma evidence by attributing it to advocacy-influenced bias, without specifics. |
| 3 | "Male circumcision, when conducted in clinical settings, has complication rates below 1%, primarily minor bleeding or infection, and is associated with protective effects against urinary tract infections in infancy (reduced by 90%) and heterosexual HIV acquisition (by 60%, per randomized trials in Africa)." | F036 Suppressed Evidence | pro | FGM rates from non-sterile traditional settings in the previous sentence are set against male circumcision in clinical settings only, a mismatched comparison that inflates the contrast. |
| 4 | "These disparities stem from anatomical realities: the clitoris is the primary female sexual organ analogous to the penis, with excision equating to partial penile amputation, whereas foreskin removal affects a protective sheath without excising core genital tissue." | F011 Hasty Generalization | pro | Generalizes from clitoral excision to FGM as a whole, though the article itself describes prepuce-only (Type Ia) and pricking (Type IV) forms that this reasoning does not cover. |
| 5 | "These patterns suggest that global efforts, while data-driven in intent, are undermined by inconsistent application influenced by political correctness and resource allocation priorities." | F040 Loaded Language | anti | Loaded attribution ('political correctness') in the article's own voice, without evidence of the claimed motive. |

## Both-sides balance note

Run 2 flag counts by side: pro 4, anti 1, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
