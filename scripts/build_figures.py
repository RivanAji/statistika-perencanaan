"""Build the two-part descriptive SVG from the public example CSV."""

import csv
from collections import Counter
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
with (ROOT / "public/data/perjalanan_contoh.csv").open(encoding="utf-8", newline="") as stream:
    rows = list(csv.DictReader(stream))

moda_counts = Counter(row["moda"] for row in rows)
times = [float(row["waktu_menit"]) for row in rows]
edges = [0, 10, 20, 30, 40]
hist_counts = [
    sum((low <= value <= high if index == len(edges) - 2 else low <= value < high) for value in times)
    for index, (low, high) in enumerate(zip(edges[:-1], edges[1:]))
]

parts = [
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 560" role="img" aria-labelledby="title desc">',
    '<title id="title">Frekuensi moda dan histogram waktu perjalanan</title>',
    '<desc id="desc">Diagram batang moda dan histogram waktu dari delapan perjalanan simulasi.</desc>',
    '<rect width="800" height="560" fill="#f7fbfc"/>',
    '<g font-family="Arial,Helvetica,sans-serif" fill="#173440">',
    '<text x="44" y="48" font-size="23" font-weight="700">Moda pada delapan perjalanan</text>',
    '<text x="44" y="84" font-size="15">Jumlah perjalanan</text>',
    '<path d="M120 100v165h620" stroke="#58727a" stroke-width="2" fill="none"/>',
]
for index, (name, count) in enumerate(moda_counts.items()):
    x = 155 + index * 150
    height = count * 55
    parts.extend([
        f'<rect x="{x}" y="{265-height}" width="96" height="{height}" fill="#1459b5"/>',
        f'<text x="{x+48}" y="{255-height}" font-size="18" text-anchor="middle">{count}</text>',
        f'<text x="{x+48}" y="292" font-size="18" text-anchor="middle">{escape(name)}</text>',
    ])
parts.extend([
    '<text x="44" y="353" font-size="23" font-weight="700">Waktu perjalanan</text>',
    '<text x="44" y="385" font-size="15">Jumlah perjalanan per rentang menit</text>',
    '<path d="M120 402v105h620" stroke="#58727a" stroke-width="2" fill="none"/>',
])
for index, count in enumerate(hist_counts):
    x = 150 + index * 155
    height = count * 15
    if count:
        parts.append(f'<rect x="{x}" y="{507-height}" width="115" height="{height}" fill="#76b9ef"/>')
    parts.extend([
        f'<text x="{x+57}" y="{497-height}" font-size="17" text-anchor="middle">{count}</text>',
        f'<text x="{x+57}" y="536" font-size="17" text-anchor="middle">{edges[index]}-{edges[index+1]}</text>',
    ])
parts.extend(['</g>', '</svg>'])
output = ROOT / "src/assets/grafik-moda-waktu.svg"
output.write_text("\n".join(parts) + "\n", encoding="utf-8")
print(output)
