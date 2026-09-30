"""Build two explicitly simulated teaching datasets with fixed, inspectable rows."""

import csv
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "public" / "data"
OUT.mkdir(parents=True, exist_ok=True)

perjalanan = [
    ("Bus", 12), ("Bus", 18),
    ("Motor", 10), ("Motor", 14),
    ("Jalan kaki", 8), ("Jalan kaki", 16),
    ("Sepeda", 12), ("Sepeda", 30),
]

taman = [
    ("A", 6, 450, "Baik"), ("B", 9, 700, "Baik"),
    ("C", 14, 900, "Cukup"), ("D", 8, 600, "Baik"),
    ("E", 17, 1200, "Kurang"), ("F", 11, 800, "Cukup"),
    ("G", 7, 500, "Baik"), ("H", 15, 1000, "Kurang"),
    ("I", 10, 750, "Cukup"), ("J", 12, 850, "Cukup"),
    ("K", 19, 1400, "Kurang"), ("L", 8, 550, "Baik"),
]

with (OUT / "perjalanan_contoh.csv").open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["moda", "waktu_menit"])
    writer.writerows(perjalanan)

with (OUT / "akses_taman_latihan.csv").open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["zona", "jalan_kaki_menit", "jarak_meter", "kondisi_trotoar"])
    writer.writerows(taman)

print("Dibuat: perjalanan_contoh.csv (8 baris), akses_taman_latihan.csv (12 baris)")
