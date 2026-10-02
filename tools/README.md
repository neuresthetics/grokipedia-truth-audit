# tools

Shared scripts. Run them from the repo root. All use the Python standard library except `make_charts.py` (needs matplotlib).

| Script | What it does | Topic |
|---|---|---|
| [sophistry_counts.py](sophistry_counts.py) | Deterministic text counts per snapshot: sentences, uncited sentences, dangling citations, term-list hits ([term_lists/](term_lists/)). `--all --date 2026-10-01` writes `topics/<topic>/code_counts/` | any (`--topic`, default `circumcision`) |
| [sophistry_triage.py](sophistry_triage.py) | Run 1's reading triage: picks which sentences get read closely. Not a measurement | any (`--topic`) |
| [sophistry_summary.py](sophistry_summary.py) | Builds run 1's cross-article summary table from the per-article run 1 scans | circumcision |
| [render_run2_scans.py](render_run2_scans.py) | Renders the per-article run 2 write-ups (`sophistry_scan.md`) from run 2's `flags.csv` | circumcision |
| [verify_run2_scan_quotes.py](verify_run2_scan_quotes.py) | Checks that every run 2 flag quote occurs verbatim in its snapshot | circumcision |
| [make_charts.py](make_charts.py) | Draws the five charts in [docs/img/circumcision/](../docs/img/circumcision/) from the committed flag files and prints every number it draws | circumcision |
| [grokaudit/](grokaudit/README.md) | Citation and fact-check pipeline (parse a saved page, check links, find renumbering shifts, build the audit log) | any; used for Spinoza |

Examples:

```
python3 tools/sophistry_counts.py --all --date 2026-10-01
python3 tools/sophistry_counts.py --slug circumcision --date 2026-10-01 --sentences
python3 tools/render_run2_scans.py
python3 tools/verify_run2_scan_quotes.py
python3 tools/make_charts.py
```

Scripts that belong to one scan run (sentence splitters, comparisons) live in that run's folder under `topics/<topic>/runs/`.
