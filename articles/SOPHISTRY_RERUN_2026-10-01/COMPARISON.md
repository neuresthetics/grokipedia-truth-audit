# Sophistry scan reproducibility: run 1 vs run 2 (58 Grokipedia snapshots, 2026-10-01)

**Compared:** run 1 (`articles/*/analyses/2026-10-01/sophistry_scan.md`) and run 2 (`flags.csv`).
**Method (both runs):** substance_lens v0.5.9 `fallacyScanPass` (67 kept F-IDs), both sides, the article's own voice only, no outside fact-checking.
**Every number below comes from `compare.py`** (output in `comparison.json`; tables in `tables.md`). The flags themselves are judgment calls by a model in both runs, not measurements.

## How run 2 was done

- **Blinding.** Run 2 was scanned without opening run 1's per-article scans, the run 1 summary, `tools/sophistry_triage.py` or `(unpublished run-1 scratch)`. `flags.csv` was finalized at 2026-10-01 23:14 PT (sha256 `fc6978a1…95d3`), and only then were those files opened for this comparison.
- **Coverage.** Every unit of every article was read: 10,258 units in total (10,088 prose units, including 33 `[Table]` marker lines, and 170 table rows). Text was split by `split.py` and read in citation-stripped views. Per-article counts are in `coverage.tsv`.
  - By contrast, run 1 read the lead plus a cue-word-selected subset: 2,969 of 10,016 sentences (29.6%) by its own sentence count.
- **Quotes.** `build_flags.py` maps each flag to its exact snapshot sentence and asserts the quote is a substring of the snapshot. All 225 quotes passed (223 unique matches; 2 sentences that appear twice in an article were mapped to their first occurrence).
- **Process caveat.** Run 2 was done in several sessions with context summaries between them. Partway through, I found I had been using some F-ID meanings wrongly (e.g. F003 is Red Herring and F036 is Suppressed Evidence). Before the final build I checked every row's F-ID against its note. This was a judgment review, not a computed check.

## Matching rules

1. Flags are matched within the same article on the sentence.
2. Two quotes match if they are:
   - identical after removing `[n]` citation markers and collapsing whitespace;
   - identical after also case-folding and unifying quote and dash characters; or
   - one contains the other (both at least 20 characters).
3. Pairing is one-to-one and greedy, preferring the strongest match type. All 106 matches turned out to be exact.
4. A match counts regardless of F-ID or side. F-ID and side agreement are then measured on the matched pairs.

## Restricted comparison (run 1's read set)

Run 1's read set could be rebuilt exactly.

- **Reproduction.** `tools/sophistry_triage.py` is deterministic: its sort is stable and it uses no randomness. `compare.py` imports its `view()` function with bytecode writing disabled, so nothing was written to the repo. It runs `view()` per article with the cap given on that article's "Reading coverage" line (45 or 80).
- **Check.** For all 58 articles, the rebuilt lead count, picked count and body count equal the numbers stated in the scan file.
- **Result.** All 239 run-1 flags fall inside the rebuilt read set. 127 of run 2's 225 flags do.

## Conclusion (plain English)

1. **Agreement at sentence level is moderate.**
   - Run 2 reproduced 106 of run 1's 239 flagged sentences (44%). Jaccard over all flagged sentences is 0.30.
   - Run 1 read only about 30% of sentences, so most of run 2's 119 extra flags (98 of them) are in sentences run 1 never read closely.
   - Within run 1's read set, 106 of run 2's 127 flags (84%) were also flagged by run 1, and Jaccard rises to 0.41.
   - Run 1 still has 133 flags that run 2 did not raise, even though run 2 read those sentences. In those sentences run 2 was the more conservative reader, plausibly because it spread its attention over all 10,258 units rather than about 3,000.

2. **When both runs flag the same sentence, they mostly agree on the label.**
   - The side label agrees in 90% of matched pairs (95 of 106).
   - No matched sentence flips between pro and anti. All 11 disagreements are run 1 "neutral/structural" against run 2 "anti", mostly in FGM-law and enforcement articles. This looks like a difference in labelling convention (which side a criticism of lax enforcement or "relativism" favours), not a reversal.
   - The F-ID agrees in 67% (71 of 106), and both labels agree in 59%.

3. **The pro lean in the male-circumcision articles is stable.**
   - Pro flags are 77% of directional (pro + anti) flags in run 1 and 85% in run 2. Within run 1's read set, run 2 gives 81%.
   - Of the 28 male articles flagged in both runs, 21 have the same article-level lean, and none reverses between pro and anti.
   - Per-article flag counts correlate well: Spearman 0.85 for the male articles and 0.75 across all 58.

4. **The lean in the FGM (‡) articles is not stable.**
   - Article-level lean agrees in only 5 of the 18 ‡ articles flagged in both runs (no pro↔anti reversals).
   - The group's pro share moves from 43% (run 1) to 53% (run 2).
   - Much of that shift is one article, *Women unaffected by female genital cutting* (run 1: 6 pro flags; run 2: 14). Without it, the ‡ group is 34% pro in run 1 and 39% pro in run 2.
   - Within run 1's read set, run 2's ‡ flags are 72% pro (18 of 25), against run 1's 43%. Run 2 raised fewer of the anti and neutral law and enforcement flags there.
   - Per-article Spearman for the ‡ group is only 0.52.
   - Both runs agree on the broad picture: the FGM articles mix pro (male/female distinction, "absolutism" framing) and anti (crediting campaigns post hoc, loaded framing about immigration and relativism) faults, with *Women unaffected* as the clear pro outlier. The net direction for the group as a whole should not be treated as established.

5. **Stable versus noisy fallacy types.** Stability here means sentences flagged by both runs with the same F-ID, scored with Dice; see Table 4.
   - **Relatively stable** (Dice ≥ 0.5 with at least 7 combined flags):
     - F002 Straw Man (0.71);
     - F026 Poisoning the Well (0.60);
     - F042 False Analogy (0.57);
     - F001 Ad Hominem (0.55);
     - F041 False Equivalence (0.57) and F073 McNamara (0.67), each with fewer than 10 flags.
     - These are fallacies tied to recognisable surface moves: discrediting a source, mischaracterising an opponent, or drawing an explicit analogy.
   - **Moderate:**
     - F036 Suppressed Evidence (0.33);
     - F003 Red Herring (0.31);
     - F031 Post Hoc (0.33);
     - F040 Loaded Language (0.26). This is the most-used type in both runs (39 and 37 flags), but each run picked mostly different sentences.
   - **Noisy:**
     - F011 Hasty Generalization (0.12), F010 Appeal to Ignorance (0.10), F032 Cum Hoc (0.18), F033 Causal Oversimplification (0.21) and F034 False Cause (0.24). On the same sentence, the causal-inference types are often swapped for one another or for F011.
     - F004 Appeal to Authority (13 vs 2) and F061 Is-Ought Jump (10 vs 1) were common in run 1 and nearly absent in run 2.
     - F055 Ecological Fallacy (1 vs 7) and F013 False Dilemma (0 vs 4) went the other way.
     - These look like differences in each run's habits for choosing among overlapping categories, more than differences about whether the sentence is faulty.

6. **Bottom line.**
   - Robust to rerunning: the direction of the male-circumcision findings, which articles are most flagged, and the "surface-move" fallacy types.
   - Not robust: exactly which sentences get flagged (about 30–40% overlap), which of the causal or generalization F-IDs is used, and the net lean of the FGM group.

## Caveats

- **Consistency, not correctness.** Both runs are judgments by the same kind of model applying the same spec. Agreement shows consistency between two readings, not that the flags are correct. Shared blind spots or shared biases would show up as agreement. No human or independent-model check was done.
- **Unequal reading.** Run 1 read about 30% of sentences closely and run 2 read all of them. The restricted comparison controls for which sentences were eligible, but not for how closely each sentence was read.
- **Side convention.** Run 1 labels the third side "neutral/structural" and run 2 labels it "neutral". The two runs drew the line between neutral and anti differently for criticisms of FGM enforcement policy.
- **Matching rules.** Matching is at sentence level only. A flag on a neighbouring sentence making the same point does not count as a match; there are 7 such adjacent near misses. Adjacent misses or splitting differences could therefore understate agreement slightly. All actual matches were exact, so splitting differences caused no partial matches.
- **Sample size and significance.** The permutation p-value for Spearman only says the per-article counts are not independent. It is unsurprising, since longer and more argumentative articles get more flags in both runs.
- **Sessions.** Run 2 spanned several sessions with context summaries, so its own internal consistency may be lower than a single-session run's.

## Files

- `flags.csv`: run 2 flags (slug, quote, fid, fname, side, note)
- `raw_flags.tsv`: the snippets the flags were built from
- `build_flags.py`: builds the flags and verifies the quotes
- `coverage.tsv`: per-article units read
- `split.py`, `sentences.jsonl` and `read/`: the sentence units and reading views
- `compare.py`: this comparison
- `comparison.json`: all computed values, including every matched pair
- `tables.md`: the tables below

## Tables

### Table 1. Sentence-level agreement

| Scope | Run 1 flags | Run 2 flags | Matched | Run 1 only | Run 2 only | Jaccard | Share of run 1 reproduced | Share of run 2 also in run 1 |
|---|---|---|---|---|---|---|---|---|
| All sentences | 239 | 225 | 106 | 133 | 119 | 0.296 | 44.4% | 47.1% |
| Restricted to run 1's read set | 239 | 127 | 106 | 133 | 21 | 0.408 | 44.4% | 83.5% |

Match types: {'exact': 106}. Run 1 flags outside the reconstructed read set: 0. Articles whose read set was rebuilt with exactly the lead/picked/body counts the scan file states: 58 of 58. Run 1 read set: 2969 of 10016 run-1 sentences (29.6%); 2980 of 10055 run-2 prose units fall in it.

### Table 2. Labels on matched sentences

| Measure | Count | Share of matched |
|---|---|---|
| Same F-ID | 71 of 106 | 67.0% |
| Same side label | 95 of 106 | 89.6% |
| Same F-ID and same side | 63 of 106 | 59.4% |

Side labels on matched sentences (run 1 → run 2):

| Run 1 → Run 2 | Count |
|---|---|
| anti->anti | 11 |
| neutral->anti | 11 |
| neutral->neutral | 8 |
| pro->pro | 76 |

Most common F-ID pairs on matched sentences (run 1 → run 2):

| Run 1 → Run 2 | Count |
|---|---|
| F040->F040 | 10 |
| F026->F026 | 9 |
| F036->F036 | 7 |
| F002->F002 | 6 |
| F003->F003 | 4 |
| F042->F042 | 4 |
| F073->F073 | 3 |
| F031->F031 | 3 |
| F001->F001 | 3 |
| F034->F034 | 3 |
| F032->F032 | 3 |
| F026->F040 | 2 |
| F041->F041 | 2 |
| F033->F033 | 2 |
| F004->F004 | 2 |
| F003->F040 | 2 |
| F040->F002 | 2 |
| F011->F011 | 2 |
| F003->F036 | 2 |
| F026->F001 | 2 |
| F055->F055 | 1 |
| F032->F055 | 1 |
| F010->F010 | 1 |
| F032->F011 | 1 |
| F061->F061 | 1 |

### Table 3. Side split per run

| Run | Group | Pro | Anti | Neutral | Total | Pro share of pro+anti |
|---|---|---|---|---|---|---|
| run1 | male (non-‡) | 108 | 32 | 30 | 170 | 77.1% |
| run1 | FGM (‡) | 18 | 24 | 27 | 69 | 42.9% |
| run1 | all | 126 | 56 | 57 | 239 | 69.2% |
| run2 | male (non-‡) | 123 | 22 | 9 | 154 | 84.8% |
| run2 | FGM (‡) | 31 | 27 | 13 | 71 | 53.4% |
| run2 | all | 154 | 49 | 22 | 225 | 75.9% |
| run2 (run-1 read set only) | male (non-‡) | 75 | 18 | 2 | 95 | 80.6% |
| run2 (run-1 read set only) | FGM (‡) | 18 | 7 | 7 | 32 | 72.0% |
| run2 (run-1 read set only) | all | 93 | 25 | 9 | 127 | 78.8% |

FGM (‡) group without *Women unaffected by female genital cutting*: run 1 pro 12 / anti 23 (34.3% pro); run 2 pro 17 / anti 27 (38.6% pro). ‡ set = the 19 articles marked ‡ in run 1's summary; it is identical to run 2's FGM set.

### Table 4. Fallacy-type distribution and per-type agreement

Dice = 2 × (sentences flagged by both runs with this same F-ID) / (run 1 count + run 2 count). Types are sorted by combined count.

| F-ID | Name | Run 1 | Run 2 | Same sentence, same F-ID | Dice | Run 2 within run-1 read set | Dice (read set only) |
|---|---|---|---|---|---|---|---|
| F040 | Loaded Language | 39 | 37 | 10 | 0.26 | 19 | 0.34 |
| F036 | Suppressed Evidence | 16 | 26 | 7 | 0.33 | 17 | 0.42 |
| F011 | Hasty Generalization | 20 | 14 | 2 | 0.12 | 5 | 0.16 |
| F032 | Cum Hoc | 19 | 15 | 3 | 0.18 | 6 | 0.24 |
| F026 | Poisoning the Well | 16 | 14 | 9 | 0.60 | 12 | 0.64 |
| F003 | Red Herring | 16 | 10 | 4 | 0.31 | 7 | 0.35 |
| F034 | False Cause | 17 | 8 | 3 | 0.24 | 4 | 0.29 |
| F010 | Appeal to Ignorance | 7 | 13 | 1 | 0.10 | 3 | 0.20 |
| F033 | Causal Oversimplification | 13 | 6 | 2 | 0.21 | 3 | 0.25 |
| F031 | Post Hoc | 6 | 12 | 3 | 0.33 | 3 | 0.67 |
| F002 | Straw Man | 7 | 10 | 6 | 0.71 | 9 | 0.75 |
| F004 | Appeal to Authority | 13 | 2 | 2 | 0.27 | 2 | 0.27 |
| F042 | False Analogy | 6 | 8 | 4 | 0.57 | 6 | 0.67 |
| F001 | Ad Hominem | 3 | 8 | 3 | 0.55 | 5 | 0.75 |
| F061 | Is-Ought Jump | 10 | 1 | 1 | 0.18 | 1 | 0.18 |
| F022 | Accident | 6 | 3 | 1 | 0.22 | 3 | 0.22 |
| F073 | McNamara Fallacy | 4 | 5 | 3 | 0.67 | 5 | 0.67 |
| F055 | Ecological Fallacy | 1 | 7 | 1 | 0.25 | 2 | 0.67 |
| F041 | False Equivalence | 4 | 3 | 2 | 0.57 | 3 | 0.57 |
| F005 | Appeal to Popularity | 2 | 3 | 0 | 0.00 | 2 | 0.00 |
| F028 | Appeal to Tradition | 1 | 4 | 1 | 0.40 | 2 | 0.67 |
| F013 | False Dilemma | 0 | 4 | 0 | 0.00 | 2 | 0.00 |
| F025 | Guilt by Association | 2 | 2 | 1 | 0.50 | 1 | 0.67 |
| F027 | Genetic Fallacy | 1 | 3 | 0 | 0.00 | 2 | 0.00 |
| F056 | Exception Fallacy | 2 | 1 | 1 | 0.67 | 1 | 0.67 |
| F020 | Division | 2 | 0 | 0 | 0.00 | 0 | 0.00 |
| F035 | Texas Sharpshooter | 1 | 1 | 1 | 1.00 | 1 | 1.00 |
| F039 | No True Scotsman | 0 | 2 | 0 | 0.00 | 1 | 0.00 |
| F053 | Argument from Repetition | 1 | 1 | 0 | 0.00 | 0 | 0.00 |
| F019 | Composition | 0 | 1 | 0 | 0.00 | 0 | n/a |
| F058 | Presentism | 1 | 0 | 0 | 0.00 | 0 | 0.00 |
| F071 | Base Rate Neglect | 1 | 0 | 0 | 0.00 | 0 | 0.00 |
| F075 | Appeal to Consequences | 1 | 0 | 0 | 0.00 | 0 | 0.00 |
| F077 | Fallacy of Relative Privation | 0 | 1 | 0 | 0.00 | 0 | n/a |
| F080 | Nirvana Fallacy | 1 | 0 | 0 | 0.00 | 0 | 0.00 |

### Table 5. Per-article flag counts

Spearman rank correlation of per-article counts (58 articles): **0.749** (two-sided permutation p ≈ 0.00005, 20,000 permutations, seed 20261001; scipy not installed, so the rank correlation was computed with the script's own average-rank Pearson). Restricted counts (run-1 read set only): 0.730. Male articles only (39): 0.847; ‡ articles only (19): 0.519.

Article lean (side with most flags; ties = mixed): 46 articles have flags in both runs; same lean in 26; pro↔anti reversals: 0. Same lean, male articles: 21 of 28; ‡ articles: 5 of 18. Flagged in one run only: 11; zero in both: 1. Run-1-only flags with a run-2-only flag on an adjacent sentence (possible near misses, not counted as matches): 7.

| # | Article | ‡ | Run 1 | Run 2 | Matched | Run 2 in run-1 read set | Run 1 lean | Run 2 lean | Run 1 pro/anti | Run 2 pro/anti |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | circumcision |  | 14 | 15 | 6 | 7 | pro | pro | 12/2 | 12/2 |
| 2 | circumcision-and-hiv |  | 8 | 5 | 5 | 5 | pro | pro | 7/1 | 5/0 |
| 3 | circumcision-and-law |  | 6 | 8 | 5 | 5 | pro | pro | 5/1 | 8/0 |
| 4 | circumcision-controversies |  | 15 | 21 | 11 | 11 | pro | pro | 13/2 | 19/1 |
| 5 | circumcision-controversy-in-early-christianity |  | 5 | 5 | 4 | 4 | neutral | anti | 0/0 | 1/3 |
| 6 | circumcision-in-africa |  | 6 | 9 | 5 | 7 | pro | pro | 6/0 | 9/0 |
| 7 | circumcision-in-brunei |  | 1 | 1 | 1 | 1 | pro | pro | 1/0 | 1/0 |
| 8 | circumcision-in-china |  | 2 | 0 | 0 | 0 | mixed | none | 1/0 | 0/0 |
| 9 | circumcision-in-the-bible |  | 3 | 0 | 0 | 0 | neutral | none | 0/0 | 0/0 |
| 10 | circumcision-of-jesus |  | 3 | 1 | 0 | 0 | neutral | neutral | 0/0 | 0/0 |
| 11 | circumcision-surgical-procedure |  | 4 | 4 | 1 | 1 | pro | pro | 2/1 | 2/1 |
| 12 | cost-of-circumcision-surgery-in-chaozhou |  | 2 | 1 | 1 | 1 | mixed | pro | 1/0 | 1/0 |
| 13 | cultural-views-on-circumcision-aesthetics |  | 3 | 2 | 1 | 1 | mixed | mixed | 1/1 | 0/1 |
| 14 | ethics-of-circumcision |  | 11 | 24 | 11 | 14 | pro | pro | 11/0 | 24/0 |
| 15 | feast-of-the-circumcision-of-christ |  | 1 | 0 | 0 | 0 | neutral | none | 0/0 | 0/0 |
| 16 | forced-circumcision |  | 6 | 7 | 5 | 7 | anti | anti | 1/5 | 0/7 |
| 17 | forced-circumcision-of-minors-in-south-korea |  | 3 | 1 | 1 | 1 | neutral | anti | 0/1 | 0/1 |
| 18 | history-of-circumcision |  | 4 | 0 | 0 | 0 | pro | none | 2/1 | 0/0 |
| 19 | khitan-circumcision |  | 4 | 4 | 2 | 2 | pro | pro | 3/1 | 3/1 |
| 20 | prevalence-of-circumcision |  | 3 | 1 | 0 | 0 | pro | pro | 2/0 | 1/0 |
| 21 | prohibition-of-female-circumcision-act-1985 | ‡ | 5 | 6 | 4 | 6 | neutral | pro | 1/1 | 3/2 |
| 22 | religion-and-circumcision |  | 3 | 2 | 2 | 2 | pro | pro | 2/0 | 2/0 |
| 23 | stapler-circumcision |  | 2 | 0 | 0 | 0 | neutral | none | 0/0 | 0/0 |
| 24 | views-on-circumcision |  | 8 | 9 | 6 | 7 | pro | pro | 7/0 | 9/0 |
| 25 | ashley-montagu-resolution |  | 9 | 4 | 1 | 1 | pro | mixed | 7/2 | 2/0 |
| 26 | brit-milah |  | 7 | 4 | 3 | 3 | pro | pro | 6/1 | 4/0 |
| 27 | children-act-1989-amendment-female-genital-mutilation-act-2019 | ‡ | 2 | 1 | 1 | 1 | mixed | neutral | 0/1 | 0/0 |
| 28 | clitoridectomy | ‡ | 4 | 0 | 0 | 0 | anti | none | 0/4 | 0/0 |
| 29 | female-genital-mutilation | ‡ | 7 | 5 | 1 | 2 | mixed | pro | 3/3 | 4/1 |
| 30 | female-genital-mutilation-act-2003 | ‡ | 5 | 5 | 2 | 2 | mixed | anti | 1/2 | 2/3 |
| 31 | female-genital-mutilation-in-india | ‡ | 5 | 3 | 1 | 2 | mixed | pro | 2/2 | 3/0 |
| 32 | female-genital-mutilation-in-new-zealand | ‡ | 7 | 5 | 2 | 2 | neutral | anti | 1/2 | 0/5 |
| 33 | female-genital-mutilation-in-nigeria | ‡ | 5 | 2 | 1 | 1 | mixed | mixed | 1/2 | 0/1 |
| 34 | female-genital-mutilation-in-sudan | ‡ | 4 | 4 | 0 | 1 | neutral | mixed | 1/0 | 2/0 |
| 35 | female-genital-mutilation-in-the-gambia | ‡ | 2 | 1 | 0 | 0 | mixed | neutral | 0/1 | 0/0 |
| 36 | female-genital-mutilation-in-the-united-kingdom | ‡ | 3 | 3 | 2 | 2 | neutral | anti | 0/0 | 0/3 |
| 37 | female-genital-mutilation-in-the-united-states | ‡ | 2 | 5 | 0 | 0 | mixed | anti | 0/1 | 0/5 |
| 38 | female-genital-mutilation-laws-by-country | ‡ | 1 | 3 | 0 | 0 | anti | anti | 0/1 | 0/3 |
| 39 | foreskin |  | 8 | 5 | 1 | 2 | pro | pro | 6/2 | 5/0 |
| 40 | foreskin-man |  | 1 | 0 | 0 | 0 | neutral | none | 0/0 | 0/0 |
| 41 | foreskin-restoration |  | 2 | 1 | 1 | 1 | mixed | pro | 1/1 | 1/0 |
| 42 | gishiri-cutting | ‡ | 1 | 1 | 0 | 0 | neutral | anti | 0/0 | 0/1 |
| 43 | infibulation | ‡ | 2 | 3 | 0 | 1 | mixed | pro | 1/1 | 2/0 |
| 44 | international-day-of-zero-tolerance-for-female-genital-mutilation | ‡ | 2 | 4 | 1 | 1 | mixed | anti | 1/1 | 1/2 |
| 45 | meatal-stenosis |  | 2 | 2 | 0 | 1 | anti | anti | 0/2 | 0/2 |
| 46 | mohel |  | 4 | 4 | 3 | 3 | pro | pro | 4/0 | 4/0 |
| 47 | penile-subincision |  | 3 | 0 | 0 | 0 | anti | none | 0/3 | 0/0 |
| 48 | prevalence-of-female-genital-mutilation | ‡ | 2 | 4 | 2 | 3 | neutral | neutral | 0/0 | 0/1 |
| 49 | religious-views-on-female-genital-mutilation | ‡ | 3 | 2 | 1 | 1 | neutral | neutral | 0/1 | 0/0 |
| 50 | restoration-device |  | 3 | 2 | 2 | 2 | anti | mixed | 1/2 | 1/1 |
| 51 | ulwaluko |  | 5 | 6 | 2 | 2 | pro | pro | 3/0 | 5/0 |
| 52 | women-unaffected-by-female-genital-cutting | ‡ | 7 | 14 | 5 | 7 | pro | pro | 6/1 | 14/0 |
| 53 | brit-shalom-naming-ceremony |  | 3 | 2 | 1 | 1 | anti | mixed | 1/2 | 1/1 |
| 54 | holy-prepuce |  | 2 | 0 | 0 | 0 | neutral | none | 0/0 | 0/0 |
| 55 | lipodermos |  | 1 | 0 | 0 | 0 | neutral | none | 0/0 | 0/0 |
| 56 | paraphimosis |  | 0 | 1 | 0 | 1 | none | pro | 0/0 | 1/0 |
| 57 | phimosis |  | 3 | 3 | 2 | 2 | pro | pro | 2/1 | 2/1 |
| 58 | redundant-prepuce |  | 0 | 0 | 0 | 0 | none | none | 0/0 | 0/0 |
| | **Total** | | **239** | **225** | **106** | **127** | | | | |
