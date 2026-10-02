# grokaudit: standing truth-audit method for Grokipedia pages

`grokaudit.py` uses only the Python 3.9+ standard library. It is read-only on the web: the only requests it makes are GET/HEAD to the page's own cited URLs, with a polite per-host delay.

## Pipeline

1. **Parse the page.**
   `parse page.html -o out/` produces `claims.csv`, `sources.csv` and `structure.json`. The structure file covers dangling cites, uncited sentences, duplicate/unused/malformed sources and markup leaks.
2. **Check and fetch sources.**
   - `linkcheck out/sources.csv -o out/linkcheck.csv` records the HTTP status of every source.
   - `fetch out/sources.csv --cache out/cache` saves source text (HTML or PDF via pdftotext).
   - `soft404 --cache out/cache` lists 200-status "not found" pages, bot walls and near-empty fetches.
3. **Look for a renumbering shift.**
   `offset out/claims.csv --cache out/cache` compares claim/source word overlap at n and n±k. On the Spinoza page this found a −9 shift for [90]–[161].
4. **Build the worksheet.**
   `priority out/claims.csv -o out/worksheet.csv --sample 40 --seed 1656` tags priority claims (P) and draws a seeded sample (S).
5. **Gather evidence.**
   - `evidence out/worksheet.csv --cache out/cache --only-priority --shift 90-161:-9` gives the best-matching passages per cited source.
   - `refs out/claims.csv --corpus <primary texts>` extracts Spinoza locators and fuzzy-matches quotes against the primary texts.
6. **Judge (human/model).**
   Write a verdicts file with one line per claim and 8 pipe-separated fields:
   `claim_id|check_depth|verdict|verdict_vs_intended|reason|correct_fact|correct_link|factual_issue(Y/N)`
   The Spinoza run's file is `verdicts_spinoza.psv`.
7. **Build the log and count.**
   - `buildlog out/worksheet.csv verdicts.psv out/sources.csv --shift 90-161:-9 -o audit_log.csv`
   - `report audit_log.csv` gives the counts.

## Notes

- Verdicts are judgments. The script never decides support; it only counts.
- Fallacy flags (substance_lens fallacyScanPass) are written up in prose, per side, with no scores.
- `g.sh N 'regex' [ctx]` greps cached source N.
Source-text cache (out/cache) is not published: it holds copies of third-party pages. Rebuild it with `fetch`.
