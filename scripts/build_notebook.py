"""Build one self-contained introductory Colab notebook from the public CSV."""

import json
import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
CSV = (ROOT / "public/data/perjalanan_contoh.csv").read_text(encoding="utf-8")
OUT = ROOT / "public/notebooks/statistik-perencanaan-python.ipynb"
OUT.parent.mkdir(parents=True, exist_ok=True)


def cell(kind, source, number):
    result = {"cell_type": kind, "id": f"cell-{number:02d}", "metadata": {}, "source": source.splitlines(keepends=True)}
    if kind == "code":
        result.update({"execution_count": None, "outputs": []})
    return result


items = [
    ("markdown", "# Statistik Perencanaan: contoh pertama dengan Python\n\nData ini **simulasi**. Jalankan sel dari atas ke bawah, prediksi keluaran, lalu bandingkan hasil. Delapan baris mewakili delapan perjalanan ilustratif."),
    ("code", "print('Halo, statistik!')"),
    ("markdown", "## Baca CSV\n\nSel ini menyimpan data kecil sebagai CSV di sesi notebook, lalu membacanya dengan pandas. Pada latihan mandiri, unggah CSV lain melalui panel Files."),
    ("code", "from pathlib import Path\nimport pandas as pd\nCSV_TEXT = " + repr(CSV) + "\nPath('perjalanan_contoh.csv').write_text(CSV_TEXT, encoding='utf-8')\ndata = pd.read_csv('perjalanan_contoh.csv')\nprint(data.shape)\nprint(data.to_string(index=False))"),
    ("markdown", "## Periksa kualitas awal\n\nNol nilai kosong tidak membuktikan data ini mewakili suatu kota."),
    ("code", "print(data.isna().sum().to_string())\nprint('Baris duplikat:', data.duplicated().sum())"),
    ("markdown", "## Ringkas kategori dan waktu\n\nCoba hitung rata-rata dengan tangan: jumlah delapan waktu dibagi delapan."),
    ("code", "waktu = data['waktu_menit']\nprint(data['moda'].value_counts().to_string())\nprint('Rata-rata:', waktu.mean())\nprint('Median:', waktu.median())\nprint('Simpangan baku sampel:', round(waktu.std(), 2))"),
    ("markdown", "## Peluang empiris\n\nA adalah Bus. B adalah waktu lebih dari 15 menit. Sebutkan penyebut sebelum menghitung peluang bersyarat."),
    ("code", "A = data['moda'] == 'Bus'\nB = data['waktu_menit'] > 15\nprint('A, B, A dan B:', A.sum(), B.sum(), (A & B).sum())\nprint('P(B | A):', (A & B).sum() / A.sum())"),
    ("markdown", "## Coba sendiri\n\nUbah batas waktu dari `> 15` menjadi `> 20`. Prediksi banyak baris yang terpilih. Tulis kesimpulan yang menyebut bahwa data ini simulasi."),
]

notebook = {
    "cells": [cell(kind, source, number) for number, (kind, source) in enumerate(items, 1)],
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3"}, "colab": {"provenance": []}},
    "nbformat": 4,
    "nbformat_minor": 5,
}
namespace = {}
previous_directory = Path.cwd()
with TemporaryDirectory() as directory:
    os.chdir(directory)
    try:
        execution_count = 0
        for item in notebook["cells"]:
            if item["cell_type"] != "code":
                continue
            execution_count += 1
            output = StringIO()
            with redirect_stdout(output):
                exec("".join(item["source"]), namespace)
            item["execution_count"] = execution_count
            item["outputs"] = [{
                "output_type": "stream", "name": "stdout",
                "text": output.getvalue().splitlines(keepends=True),
            }]
    finally:
        os.chdir(previous_directory)
OUT.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(OUT)
