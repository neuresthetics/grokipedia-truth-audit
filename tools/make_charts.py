#!/usr/bin/env python3
"""Draw the three-phase-test charts from the committed flag files.

Run from the repo root (needs matplotlib):
    python3 tools/make_charts.py

Reads (relative to the repo root, nothing is typed in by hand):
  articles/ARTICLE_LIST.md                                      58 article slugs, 24 'Title match'
  articles/<slug>/analyses/2026-10-01/sophistry_scan_run1_partial.md   run 1 flag tables
  articles/SOPHISTRY_RERUN_2026-10-01/flags.csv                 run 2 flags (58 articles)
  articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/flags.csv          run 3 flags (24 title matches)
  articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/comparison_units.csv  sentence-level run 2 vs run 3 match table
  articles/SOPHISTRY_RUN3_TITLE24_2026-10-02/fid_catalog.json   fallacy names
Writes PNGs to docs/img/. Prints every number it draws so it can be checked against the docs.
Every flag counted here is a model's judgment, not a measurement.
"""
import csv
import textwrap
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

sys.dont_write_bytecode = True
ART = Path("articles")
RUN2_DIR = ART / "SOPHISTRY_RERUN_2026-10-01"
RUN3_DIR = ART / "SOPHISTRY_RUN3_TITLE24_2026-10-02"
OUT = Path("docs/img")
if not (ART / "ARTICLE_LIST.md").exists():
    sys.exit("Run this from the repo root: python3 tools/make_charts.py")

SIDES = ("pro", "anti", "neutral")
# Okabe-Ito colorblind-safe palette. Same side colors on every chart.
SIDE_COLOR = {"pro": "#E69F00", "anti": "#0072B2", "neutral": "#B0B0B0"}
SIDE_LABEL = {"pro": "pro (favors circumcision)", "anti": "anti (favors the other side)", "neutral": "neutral"}
RUN_COLOR = {2: "#009E73", 3: "#CC79A7"}  # used only where runs, not sides, are compared
MATCH_COLOR = "#555555"
WIDTH_IN, DPI = 8.0, 150  # 1200 px wide

plt.rcParams.update({
    "figure.dpi": DPI, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
    "font.size": 10, "axes.titlesize": 13, "axes.titleweight": "bold", "axes.labelsize": 10.5,
    "axes.spines.top": False, "axes.spines.right": False, "legend.frameon": False,
})


# ---------------------------------------------------------------- data
def article_list():
    rows = []
    pat = re.compile(r"^\| \d+ \| (.+?) \| (.+?) \| \[snapshot\]\(([^/]+)/snapshots/")
    for ln in (ART / "ARTICLE_LIST.md").read_text(encoding="utf-8").splitlines():
        m = pat.match(ln)
        if m:
            rows.append({"title": m.group(1), "category": m.group(2), "slug": m.group(3)})
    return rows


ARTICLES = article_list()
SLUGS = [a["slug"] for a in ARTICLES]
TITLE = {a["slug"]: a["title"] for a in ARTICLES}
TITLE24 = [a["slug"] for a in ARTICLES if a["category"] == "Title match"]
assert len(SLUGS) == 58 and len(TITLE24) == 24, (len(SLUGS), len(TITLE24))


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


# Run 1 flag rows, same pattern run 2's compare.py used to parse them.
RUN1_ROW = re.compile(r'^\| (\d+) \| "(.*)" \| (F\d{3}) ([^|]+?) \| ([^|]+?) \| (.*) \|\s*$')
RUN1_SIDE = {"pro-circumcision": "pro", "anti-circumcision": "anti", "neutral/structural": "neutral"}


def load_run1():
    flags = []
    for s in SLUGS:
        p = ART / s / "analyses" / "2026-10-01" / "sophistry_scan_run1_partial.md"
        for ln in p.read_text(encoding="utf-8").splitlines():
            m = RUN1_ROW.match(ln)
            if m:
                flags.append({"slug": s, "fid": m.group(3), "side": RUN1_SIDE[m.group(5).strip()]})
    return flags


RUN1 = load_run1()
RUN2 = read_csv(RUN2_DIR / "flags.csv")
RUN3 = read_csv(RUN3_DIR / "flags.csv")
RUN2_24 = [r for r in RUN2 if r["slug"] in TITLE24]
assert {r["slug"] for r in RUN3} <= set(TITLE24)
UNITS = read_csv(RUN3_DIR / "comparison_units.csv")
FNAME = {e["id"]: e["name"] for e in json.load(open(RUN3_DIR / "fid_catalog.json", encoding="utf-8"))["entries"]}


def sides(flags):
    c = Counter(r["side"] for r in flags)
    assert set(c) <= set(SIDES), c
    return c


def pro_share(c):
    return c["pro"] / (c["pro"] + c["anti"]) if c["pro"] + c["anti"] else float("nan")


def per_article(flags):
    d = defaultdict(Counter)
    for r in flags:
        d[r["slug"]][r["side"]] += 1
    return d


def avg_ranks(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2 + 1
        i = j + 1
    return ranks


def spearman(x, y):
    rx, ry = avg_ranks(x), avg_ranks(y)
    n = len(x)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    vx = sum((a - mx) ** 2 for a in rx) ** 0.5
    vy = sum((b - my) ** 2 for b in ry) ** 0.5
    return cov / (vx * vy)


def titles(fig, title, subtitle=None, top=0.985):
    """Title centered on the whole image, with an optional subtitle 30 px below it."""
    fig.suptitle(title, y=top, va="top", fontsize=13, fontweight="bold")
    if subtitle:
        fig.text(0.5, top - 30 / (fig.get_figheight() * DPI), subtitle, ha="center", va="top", fontsize=8.5,
                 color="#333333")


def footnote(fig, text):
    """One-line data-source note; the font shrinks until the line fits inside the image."""
    t = fig.text(0.01, 0.008, text, ha="left", va="bottom", fontsize=7.5, color="#555555")
    renderer = fig.canvas.get_renderer()
    while t.get_window_extent(renderer).x1 > fig.bbox.width * 0.99 and t.get_fontsize() > 5.5:
        t.set_fontsize(t.get_fontsize() - 0.25)


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / name, dpi=DPI)
    plt.close(fig)
    print(f"wrote {OUT / name}")


def side_legend(ax, **kw):
    handles = [Patch(facecolor=SIDE_COLOR[s], label=SIDE_LABEL[s]) for s in SIDES]
    return ax.legend(handles=handles, **kw)


# ---------------------------------------------------------------- chart 1
def chart_lean_by_run():
    bars = [
        ("Run 1\nall 58 articles\nPARTIAL read (~30%)", sides(RUN1), True),
        ("Run 2\nall 58 articles\nfull read", sides(RUN2), False),
        ("Run 2\n24 title matches\nfull read", sides(RUN2_24), False),
        ("Run 3\n24 title matches\nfull read", sides(RUN3), False),
    ]
    fig, ax = plt.subplots(figsize=(WIDTH_IN, 5.6))
    fig.subplots_adjust(left=0.09, right=0.98, top=0.85, bottom=0.2)
    x = range(len(bars))
    for i, (label, c, partial) in enumerate(bars):
        bottom = 0
        for s in SIDES:
            ax.bar(i, c[s], bottom=bottom, width=0.6, color=SIDE_COLOR[s], edgecolor="white",
                   hatch="///" if partial else None, linewidth=0.8)
            if c[s] >= 12:
                ax.text(i, bottom + c[s] / 2, str(c[s]), ha="center", va="center", fontsize=9,
                        color="white" if s == "anti" else "black",
                        bbox=dict(boxstyle="round,pad=0.2", facecolor=SIDE_COLOR[s], edgecolor="none")
                        if partial else None)
            bottom += c[s]
        total = sum(c.values())
        ax.text(i, total + 4, f"{total} flags\n{pro_share(c):.1%} pro of sided", ha="center",
                va="bottom", fontsize=9.5, fontweight="bold")
        print(f"chart1 {label.splitlines()[0]} {label.splitlines()[1]}: total={total} "
              f"pro={c['pro']} anti={c['anti']} neutral={c['neutral']} pro_share={pro_share(c):.3f}")
    ax.set_xticks(list(x), [b[0] for b in bars])
    ax.set_ylabel("Number of flags")
    ax.set_ylim(0, max(sum(b[1].values()) for b in bars) * 1.25)
    titles(fig, "Side of each flag, by run",
           "'Pro of sided' = pro ÷ (pro + anti). Run 1 (hatched) read only the lead plus script-picked sentences;\n"
           "its third label was 'neutral/structural'. Run 1's total is not comparable with the full reads.")
    side_legend(ax, loc="upper right", fontsize=8.5, ncol=1)
    footnote(fig, "Data: run 1 = articles/*/analyses/2026-10-01/sophistry_scan_run1_partial.md; run 2 and run 3 = "
             "each run folder's flags.csv. Flags are model judgments.")
    save(fig, "lean_by_run.png")


# ---------------------------------------------------------------- chart 2
def chart_per_article():
    a2, a3 = per_article(RUN2_24), per_article(RUN3)
    order = sorted(TITLE24, key=lambda s: (-sum(a2[s].values()), -sum(a3[s].values()), TITLE[s]))
    fig, ax = plt.subplots(figsize=(WIDTH_IN, 11.5))
    fig.subplots_adjust(left=0.31, right=0.97, top=0.935, bottom=0.07)
    h = 0.38
    for i, s in enumerate(order):
        y = len(order) - 1 - i
        for run, c, dy in ((2, a2[s], h / 2), (3, a3[s], -h / 2)):
            left = 0
            for side in SIDES:
                if c[side]:
                    ax.barh(y + dy, c[side], left=left, height=h * 0.92, color=SIDE_COLOR[side],
                            edgecolor="white", hatch="..." if run == 3 else None, linewidth=0.6)
                left += c[side]
            ax.text(left + 0.25, y + dy, f"R{run}: {left}", va="center", fontsize=7.5, color="#333333")
        print(f"chart2 {s}: run2 {a2[s]['pro']}/{a2[s]['anti']}/{a2[s]['neutral']} "
              f"run3 {a3[s]['pro']}/{a3[s]['anti']}/{a3[s]['neutral']}")
    ax.set_yticks(range(len(order)), [textwrap.fill(TITLE[s], 30) for s in reversed(order)], fontsize=9)
    ax.set_xlabel("Number of flags (upper bar = run 2, lower dotted bar = run 3)")
    ax.set_xlim(0, max(max(sum(a2[s].values()), sum(a3[s].values())) for s in order) + 3.5)
    ax.set_ylim(-0.7, len(order) - 0.3)
    titles(fig, "Flags per article, run 2 vs run 3 (24 title-match articles)",
           "Each article has two bars: run 2 on top (plain), run 3 below (dotted). Colors show the side of each flag.",
           top=0.985)
    handles = [Patch(facecolor=SIDE_COLOR[s], label=SIDE_LABEL[s]) for s in SIDES]
    handles += [Patch(facecolor="white", edgecolor="#333333", label="run 2 (plain)"),
                Patch(facecolor="white", edgecolor="#333333", hatch="...", label="run 3 (dotted)")]
    ax.legend(handles=handles, loc="lower right", fontsize=8.5)
    footnote(fig, "Data: SOPHISTRY_RERUN_2026-10-01/flags.csv (24 title matches only) and "
             "SOPHISTRY_RUN3_TITLE24_2026-10-02/flags.csv. Sorted by run 2 count.")
    save(fig, "title24_per_article.png")


# ---------------------------------------------------------------- chart 3
def chart_scatter():
    a2, a3 = per_article(RUN2_24), per_article(RUN3)
    x = [sum(a2[s].values()) for s in TITLE24]
    y = [sum(a3[s].values()) for s in TITLE24]
    rho = spearman(x, y)
    print(f"chart3 spearman={rho:.3f} n={len(x)}")
    pts = Counter(zip(x, y))
    fig, ax = plt.subplots(figsize=(WIDTH_IN, 6.6))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.89, bottom=0.11)
    lim = max(x + y) + 2
    ax.plot([0, lim], [0, lim], color="#999999", ls="--", lw=1, zorder=1)
    ax.text(lim - 3.5, lim - 1.2, "y = x (same count)", ha="right", va="center", fontsize=8.5, color="#777777")
    for (px, py), n in pts.items():
        ax.scatter(px, py, s=45 + 45 * (n - 1), color="#333333", alpha=0.8, zorder=3, edgecolor="white")
        if n > 1:
            ax.text(px + 0.35, py - 0.55, f"×{n}", fontsize=7.5, color="#555555")
    # label the articles with the most flags in either run
    top = sorted(TITLE24, key=lambda s: -max(sum(a2[s].values()), sum(a3[s].values())))[:7]
    # label offsets (in data units) are layout only; the point positions come from the data
    offsets = {"ethics-of-circumcision": (-0.3, -3.6, "center"), "circumcision-controversies": (0.0, -1.8, "center"),
               "circumcision": (1.5, -2.0, "left"), "views-on-circumcision": (1.5, 3.0, "left"),
               "circumcision-in-africa": (2.0, -2.2, "left"), "forced-circumcision": (-1.4, 3.5, "right"),
               "circumcision-and-law": (3.0, 2.3, "left")}
    for s in top:
        dx, dy, ha = offsets.get(s, (0.8, 0.8, "left"))
        xi, yi = sum(a2[s].values()), sum(a3[s].values())
        sep = "\n" if s == "ethics-of-circumcision" else " "
        ax.annotate(f"{TITLE[s]}{sep}({xi}, {yi})", xy=(xi, yi), xytext=(xi + dx, yi + dy), fontsize=8.5, ha=ha,
                    va="center", arrowprops=dict(arrowstyle="-", color="#999999", lw=0.8, shrinkB=4))
    ax.set_xlim(-1, lim)
    ax.set_ylim(-1, lim)
    ax.set_xlabel("Flags in run 2 (per article)")
    ax.set_ylabel("Flags in run 3 (per article)")
    titles(fig, "Per-article flag counts, run 2 vs run 3 (24 title matches)",
           "One dot per article. Larger dots with ×n mark n articles with the same pair of counts.")
    ax.text(0.03, 0.96, f"Spearman rank correlation = {rho:.3f} (n = {len(x)})\n"
            "Dots below the line: run 3 flagged fewer than run 2", transform=ax.transAxes, va="top", fontsize=9.5,
            bbox=dict(facecolor="white", edgecolor="#CCCCCC"))
    footnote(fig, "Data: SOPHISTRY_RERUN_2026-10-01/flags.csv and SOPHISTRY_RUN3_TITLE24_2026-10-02/flags.csv. "
             "Spearman computed by this script (ties get average ranks).")
    save(fig, "run2_vs_run3_scatter.png")


# ---------------------------------------------------------------- chart 4
def split(v):
    return set(v.split(";")) if v else set()


def chart_overlap():
    st = Counter(u["status"] for u in UNITS)
    matched = [u for u in UNITS if u["status"] == "matched"]
    same_fid = sum(bool(split(u["run2_fids"]) & split(u["run3_fids"])) for u in matched)
    same_side = sum(bool(split(u["run2_sides"]) & split(u["run3_sides"])) for u in matched)
    n2 = st["matched"] + st["run2_only"]
    n3 = st["matched"] + st["run3_only"]
    union = n2 + st["run3_only"]
    print(f"chart4 matched={st['matched']} run2_only={st['run2_only']} run3_only={st['run3_only']} "
          f"jaccard={st['matched'] / union:.3f} reproduced={st['matched'] / n2:.3f} "
          f"same_fid={same_fid}/{len(matched)} same_side={same_side}/{len(matched)}")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(WIDTH_IN, 4.6), gridspec_kw={"width_ratios": [2.2, 1]})
    fig.subplots_adjust(left=0.04, right=0.95, top=0.8, bottom=0.2, wspace=0.35)
    # left: one horizontal bar of all sentences flagged by either run
    segs = [("only run 2", st["run2_only"], RUN_COLOR[2]), ("both runs", st["matched"], MATCH_COLOR),
            ("only run 3", st["run3_only"], RUN_COLOR[3])]
    left = 0
    for name, n, col in segs:
        ax1.barh(0, n, left=left, color=col, height=0.5, edgecolor="white")
        ax1.text(left + n / 2, 0, f"{name}\n{n}", ha="center", va="center", color="white", fontsize=10,
                 fontweight="bold")
        left += n
    ax1.annotate("", xy=(0, 0.42), xytext=(n2, 0.42), arrowprops=dict(arrowstyle="<->", color=RUN_COLOR[2]))
    ax1.text(n2 / 2, 0.5, f"run 2 flagged {n2} sentences", ha="center", va="bottom", fontsize=8.5)
    ax1.annotate("", xy=(st["run2_only"], -0.42), xytext=(union, -0.42),
                 arrowprops=dict(arrowstyle="<->", color=RUN_COLOR[3]))
    ax1.text(st["run2_only"] + n3 / 2, -0.5, f"run 3 flagged {n3} sentences", ha="center", va="top", fontsize=8.5)
    ax1.set_xlim(0, union)
    ax1.set_ylim(-0.9, 0.9)
    ax1.set_yticks([])
    ax1.spines["left"].set_visible(False)
    ax1.set_xlabel(f"Sentences flagged by either run ({union})")
    ax1.set_title(f"Which sentences were flagged\n(Jaccard {st['matched'] / union:.3f}; run 3 found "
                  f"{st['matched'] / n2:.0%} of run 2's)", fontsize=10.5)
    # right: agreement on matched sentences
    vals = [("same side", same_side), ("same F-ID", same_fid)]
    for i, (name, n) in enumerate(vals):
        ax2.barh(i, len(matched), color="#E8E8E8", height=0.55)
        ax2.barh(i, n, color=MATCH_COLOR, height=0.55)
        ax2.text(n - 1, i, f"{n / len(matched):.0%} ({n}/{len(matched)})", ha="right", va="center",
                 color="white", fontsize=9, fontweight="bold")
    ax2.set_yticks(range(len(vals)), [v[0] for v in vals])
    ax2.set_xlim(0, len(matched))
    ax2.set_xlabel(f"Sentences flagged by both ({len(matched)})")
    ax2.set_title("Agreement where\nboth runs flagged", fontsize=10.5)
    fig.suptitle("Sentence-level overlap, run 2 vs run 3 (24 title matches)", fontsize=13, fontweight="bold")
    footnote(fig, "Data: SOPHISTRY_RUN3_TITLE24_2026-10-02/comparison_units.csv (from both runs' flags.csv). "
             "A unit is one sentence or table row.")
    save(fig, "flag_overlap.png")


# ---------------------------------------------------------------- chart 5
def chart_fallacy_types(top_n=15):
    c2 = Counter(r["fid"] for r in RUN2_24)
    c3 = Counter(r["fid"] for r in RUN3)
    both = Counter()
    for u in UNITS:
        for f in split(u["run2_fids"]) & split(u["run3_fids"]):
            both[f] += 1
    ranked = sorted(set(c2) | set(c3), key=lambda f: (-(c2[f] + c3[f]), f))
    cut = c2[ranked[top_n - 1]] + c3[ranked[top_n - 1]]
    fids = [f for f in ranked if c2[f] + c3[f] >= cut]  # top_n, plus any tied with the last one
    fig, ax = plt.subplots(figsize=(WIDTH_IN, 9.0))
    fig.subplots_adjust(left=0.3, right=0.97, top=0.9, bottom=0.08)
    h = 0.27
    for i, f in enumerate(fids):
        y = len(fids) - 1 - i
        for dy, n, col in ((h, c2[f], RUN_COLOR[2]), (0, c3[f], RUN_COLOR[3]), (-h, both[f], MATCH_COLOR)):
            ax.barh(y + dy, n, height=h * 0.95, color=col)
            ax.text(n + 0.2, y + dy, str(n), va="center", fontsize=7.5)
        print(f"chart5 {f} {FNAME[f]}: run2={c2[f]} run3={c3[f]} same_sentence_same_fid={both[f]}")
    ax.set_yticks(range(len(fids)), [f"{f} {FNAME[f]}" for f in reversed(fids)], fontsize=9)
    ax.set_xlabel("Number of flags")
    ax.set_xlim(0, max(max(c2[f], c3[f]) for f in fids) + 2)
    ax.set_ylim(-0.6, len(fids) - 0.4)
    titles(fig, f"Fallacy types, run 2 vs run 3 (24 title matches)",
           f"The {len(fids)} most-used types (at least {cut} flags across both runs). Dark bar: sentences where both runs "
           "gave this same F-ID.")
    handles = [Patch(color=RUN_COLOR[2], label="run 2"), Patch(color=RUN_COLOR[3], label="run 3"),
               Patch(color=MATCH_COLOR, label="same sentence, same F-ID")]
    ax.legend(handles=handles, loc="lower right", fontsize=8.5)
    footnote(fig, "Data: both runs' flags.csv (run 2: 24 title matches only) and comparison_units.csv; names from "
             "fid_catalog.json (substance_lens v0.5.9).")
    save(fig, "fallacy_types_stability.png")


if __name__ == "__main__":
    print(f"run1 flags={len(RUN1)} run2 flags={len(RUN2)} run2 on 24={len(RUN2_24)} run3 flags={len(RUN3)}")
    chart_lean_by_run()
    chart_per_article()
    chart_scatter()
    chart_overlap()
    chart_fallacy_types()
