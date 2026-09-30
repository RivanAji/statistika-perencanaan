"""Render textbook figures from the public synthetic datasets."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import comb, exp, factorial, pi, sqrt
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src/assets"
journeys = pd.read_csv(ROOT / "public/data/perjalanan_contoh.csv")
parks = pd.read_csv(ROOT / "public/data/akses_taman_latihan.csv")
blue = "#1459b5"
teal = "#76b9ef"
ink = "#173440"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 15,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.labelcolor": ink,
    "text.color": ink,
    "axes.edgecolor": ink,
    "svg.fonttype": "none",
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, format="svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)


fig, ax = plt.subplots(figsize=(5.8, 3.5))
counts = journeys["moda"].value_counts().sort_index()
ax.bar(counts.index, counts.values, color=blue)
ax.set(xlabel="Moda", ylabel="Jumlah perjalanan", ylim=(0, 2.6))
for i, value in enumerate(counts.values):
    ax.text(i, value + .06, str(value), ha="center")
save(fig, "hasil-diagram-batang.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
daily = pd.Series([12, 15, 14, 18, 16], index=["Sen", "Sel", "Rab", "Kam", "Jum"])
ax.plot(daily.index, daily.values, marker="o", color=blue, linewidth=2)
ax.set(xlabel="Hari pengamatan", ylabel="Waktu (menit)", ylim=(0, 21))
save(fig, "hasil-diagram-garis.svg")

fig, ax = plt.subplots(figsize=(5.8, 4))
ax.pie(counts.values, labels=counts.index, autopct="%1.0f%%", colors=[blue, teal, "#347bd0", "#b6dcfb"],
       textprops={"color": ink})
ax.axis("equal")
save(fig, "hasil-diagram-lingkaran.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
ax.hist(journeys["waktu_menit"], bins=[0, 10, 20, 30, 40], color=teal, edgecolor="white")
ax.set(xlabel="Waktu perjalanan (menit)", ylabel="Jumlah perjalanan", xticks=[0, 10, 20, 30, 40], ylim=(0, 7))
save(fig, "hasil-histogram.svg")

fig, ax = plt.subplots(figsize=(5.8, 2.7))
ax.boxplot(journeys["waktu_menit"], vert=False, widths=.35,
           boxprops={"color": blue}, whiskerprops={"color": blue},
           capprops={"color": blue}, medianprops={"color": ink, "linewidth": 2},
           flierprops={"markerfacecolor": teal, "markeredgecolor": blue})
ax.set(xlabel="Waktu perjalanan (menit)", yticks=[], xlim=(0, 35))
save(fig, "hasil-boxplot.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.8))
ax.scatter(parks["jarak_meter"], parks["jalan_kaki_menit"], color=blue, s=60)
ax.set(xlabel="Jarak ke taman (meter)", ylabel="Waktu jalan kaki (menit)")
save(fig, "hasil-diagram-pencar.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
values = journeys["waktu_menit"].sort_values().reset_index(drop=True)
ax.scatter(values, range(1, len(values) + 1), color=blue, s=55)
ax.set(xlabel="Waktu perjalanan (menit)", ylabel="Urutan nilai", yticks=range(1, 9), xlim=(0, 35))
save(fig, "hasil-diagram-titik.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
mean_by_mode = journeys.groupby("moda")["waktu_menit"].mean()
ax.bar(mean_by_mode.index, mean_by_mode.values, color=blue)
ax.set(xlabel="Moda", ylabel="Rata-rata waktu (menit)", ylim=(0, 25))
save(fig, "hasil-rata-rata-moda.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
ordered_means = mean_by_mode.sort_values()
ax.barh(ordered_means.index, ordered_means.values, color=blue)
ax.set(xlabel="Rata-rata waktu (menit)", ylabel="Moda", xlim=(0, 25))
save(fig, "hasil-rata-rata-moda-horizontal.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
p = 0.375
ks = list(range(5))
pmf = [comb(4, k) * p**k * (1 - p)**(4 - k) for k in ks]
ax.bar(ks, pmf, color=blue)
ax.set(xlabel="Banyak hasil ya dari 4 percobaan", ylabel="P(X = k)", xticks=ks, ylim=(0, .45))
save(fig, "hasil-binom.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
xs = [i / 20 for i in range(-70, 71)]
ys = [exp(-x*x/2) / sqrt(2*pi) for x in xs]
ax.plot(xs, ys, color=blue, linewidth=2)
ax.fill_between(xs, ys, where=[x <= 1 for x in xs], color=teal, alpha=.55)
ax.axvline(1, color=ink, linestyle="--", linewidth=1)
ax.set(xlabel="z", ylabel="Kepadatan", xlim=(-3.5, 3.5), ylim=(0, .43))
save(fig, "hasil-normal.svg")

fig, ax = plt.subplots(figsize=(5.8, 3.5))
lam = 2
ks_pois = list(range(8))
probs = [exp(-lam) * lam**k / factorial(k) for k in ks_pois]
ax.bar(ks_pois, probs, color=blue)
ax.set(xlabel="Kejadian per interval", ylabel="P(X = k)", xticks=ks_pois, ylim=(0, .32))
save(fig, "hasil-poisson.svg")

rng = np.random.default_rng(42)
draws = rng.integers(0, 2, size=1000)
running = np.cumsum(draws) / np.arange(1, 1001)
fig, ax = plt.subplots(figsize=(5.8, 3.7))
ax.plot(np.arange(1, 1001), running, color=blue, linewidth=1.5)
ax.axhline(.5, color=ink, linestyle="--", linewidth=1)
ax.set(xlabel="Banyak lemparan simulasi", ylabel="Proporsi angka", xlim=(1, 1000), ylim=(0, 1))
save(fig, "hasil-simulasi-koin.svg")

print("Rendered 13 charts")
