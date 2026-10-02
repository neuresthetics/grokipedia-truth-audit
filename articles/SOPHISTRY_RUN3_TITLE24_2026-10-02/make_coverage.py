"""Write coverage.tsv for run 3.

Unit counts come from segment.units(). 'units_read' records the scanner's self-report
that every sentence and table row was read in full (a statement of procedure, not a
measurement of attention). Flag counts and flagged-unit counts come from flags.csv.
"""
import csv
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import segment  # noqa: E402

HERE = Path(__file__).resolve().parent


def main():
    flags = list(csv.DictReader(open(HERE / "flags.csv", encoding="utf-8")))
    out = [["slug", "sentences", "table_rows", "headings", "units_scanned",
            "units_read_selfreport", "flags", "flagged_units"]]
    tot = [0, 0, 0, 0, 0, 0]
    for slug in segment.TITLE24:
        us = segment.units(slug)
        s = sum(u["kind"] == "sentence" for u in us)
        r = sum(u["kind"] == "row" for u in us)
        h = sum(u["kind"] == "heading" for u in us)
        fl = [f for f in flags if f["slug"] == slug]
        ids = set()
        for f in fl:
            hits, _ = segment.locate(slug, f["quote"], us)
            ids.update(hits[:1] if len(hits) > 1 else hits)
        out.append([slug, s, r, h, s + r, "all", len(fl), len(ids)])
        for i, v in enumerate([s, r, h, s + r, len(fl), len(ids)]):
            tot[i] += v
    out.append(["TOTAL", tot[0], tot[1], tot[2], tot[3], "all", tot[4], tot[5]])
    with open(HERE / "coverage.tsv", "w", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter="\t").writerows(out)
    for row in out:
        print("\t".join(map(str, row)))


if __name__ == "__main__":
    main()
