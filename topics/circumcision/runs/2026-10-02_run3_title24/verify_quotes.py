"""Check every run-3 quote against its 2026-10-01 snapshot.

Usage (from the repo root or anywhere):
    python3 topics/circumcision/runs/2026-10-02_run3_title24/verify_quotes.py [flags.csv]

Exits non-zero if any quote cannot be found, if a slug is outside the 24-article set,
or if an F-ID is not one of the 67 kept entries in fid_catalog.json.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import segment  # noqa: E402

HERE = Path(__file__).resolve().parent


def load_rows(path):
    path = Path(path)
    delim = "\t" if path.suffix == ".tsv" else ","
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=delim))


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else HERE / "flags.csv"
    rows = load_rows(src)
    cat = {e["id"]: e for e in json.load(open(HERE / "fid_catalog.json"))["entries"]}
    cache, bad, status_count = {}, [], {}
    for i, r in enumerate(rows, 1):
        slug = r["slug"]
        if slug not in segment.TITLE24:
            bad.append((i, slug, "slug not in TITLE24"))
            continue
        if r["fid"] not in cat:
            bad.append((i, slug, f"fid {r['fid']} not in catalog"))
        if r["side"] not in {"pro", "anti", "neutral"}:
            bad.append((i, slug, f"bad side {r['side']}"))
        us = cache.setdefault(slug, segment.units(slug))
        hits, status = segment.locate(slug, r["quote"], us)
        status_count[status] = status_count.get(status, 0) + 1
        if status == "missing":
            bad.append((i, slug, "quote not found: " + r["quote"][:80]))
        elif len(hits) > 1 and status != "exact-span":
            print(f"note: row {i} ({slug}) quote occurs in {len(hits)} units: {hits}")
    print(f"{len(rows)} flags checked; status counts: {status_count}")
    for b in bad:
        print("PROBLEM", b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
