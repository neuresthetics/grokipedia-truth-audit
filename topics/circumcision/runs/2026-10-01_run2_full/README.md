# Run 2: full read of the 58 circumcision articles (2026-10-01)

Run 2 read every unit (sentence or table row) of the 58 articles and flagged reasoning faults against the [substance_lens](https://github.com/neuresthetics/substance_lens) v0.5.9 catalogue, each tagged by the side it favors. Results are summarized in the [topic README](../../README.md); the comparison with run 1 is in [COMPARISON.md](COMPARISON.md).

| File | What it holds |
|---|---|
| [flags.csv](flags.csv) | All 225 flags, with exact quotes, F-IDs and sides |
| [coverage.tsv](coverage.tsv) | Units read per article |
| [COMPARISON.md](COMPARISON.md) | Run 1 vs run 2, with the tables in [tables.md](tables.md) and the numbers in [comparison.json](comparison.json) |
| [split.py](split.py) | Sentence splitter (regenerates the units, which are not committed) |
| [build_flags.py](build_flags.py) | Builds `flags.csv` from inputs that are not published |
| [compare.py](compare.py) | Computes the run 1 vs run 2 comparison |

The per-article write-ups are `../../articles/<slug>/analyses/2026-10-01/sophistry_scan.md`, rendered from `flags.csv` by [tools/render_run2_scans.py](../../../../tools/render_run2_scans.py). Details on each script are in the Files section of [COMPARISON.md](COMPARISON.md#files).
