# Sophistry and fallacy scan: _Khitan_ (circumcision)

- **Article:** _Khitan_ (circumcision)
- **URL:** https://grokipedia.com/page/Khitan_(circumcision)
- **Snapshot file:** `topics/circumcision/articles/khitan-circumcision/snapshots/2026-10-01.txt` (sources: `2026-10-01_sources.csv`)
- **Snapshot date / scan date:** 2026-10-01 / 2026-10-01 (PT)
- **Method:** substance_lens v0.5.9 fallacy scan, run 2 (full read, blind rerun). Both-sides by default; no outside fact-checking.
- **Reading coverage:** 184/184 units read in full (179 paragraphs, 5 table rows).

## Verdict

Run 2 found 4 flags: 3 pro, 1 anti, and 0 neutral. The lean is pro. Main patterns were F010 Appeal to Ignorance (1); F026 Poisoning the Well (1); F040 Loaded Language (1); F036 Suppressed Evidence (1). Flags are judgment calls.

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

Every flag below is a **judgment call** based on the run 2 reading, not a computed result. A flag withdraws warrant from that sentence's inference; it does not show the claim is false.

| n | quote | Fxxx Name | side | note |
|---:|---|---|---|---|
| 1 | "No robust data supports claims of diminished sexual function or satisfaction post-circumcision, countering anecdotal assertions of harm." | F010 Appeal to Ignorance | pro | Treats an absence of robust data as a refutation of harm claims, and labels contrary claims 'anecdotal' without engaging them. |
| 2 | "Despite these advancements, gaps persist in resource-limited areas where traditional practitioners may prioritize ritual speed over analgesia, underscoring the need for education on evidence-based methods; peer-reviewed analyses indicate that unaddressed pain in khitan correlates with higher incidence of immediate behavioral sequelae, though long-term psychological impacts require further longitudinal research free from institutional biases favoring minimal intervention narratives." | F026 Poisoning the Well | anti | Pre-emptively discredits existing research as institutionally biased, so evidence of limited harm is discounted in advance. |
| 3 | "Khitan, the Islamic practice of male circumcision, surgically excises the foreskin covering the glans penis, preserving the organ's primary erectile and urinary functions while removing a non-vital cutaneous layer." | F040 Loaded Language | pro | Minimizing description ('non-vital cutaneous layer') contrasts with FGC tissue described as 'erogenous tissue essential for sexual sensation' in the next sentence; the asymmetric wording builds in the distinction. |
| 4 | "Complication rates for medically supervised male circumcision remain below 1% for serious adverse events, whereas FGC, predominantly non-sterile and non-clinical, correlates with morbidity rates exceeding 20% in untreated cases." | F036 Suppressed Evidence | pro | Compares serious-only male rates in medical settings with all-morbidity FGC rates in non-clinical settings. The article's own 3.84% overall rate and its higher traditional-setting rates go unused in this contrast. |

## Both-sides balance note

Run 2 flag counts by side: pro 3, anti 1, neutral 0. These are judgment-based labels, not measurements.

## What wasn't checked

- No outside fact-checking or source verification was performed.
- Labels are judgment-based flags, not computed findings.
- Reproducibility comparison: [COMPARISON.md](../../../../runs/2026-10-01_run2_full/COMPARISON.md).
