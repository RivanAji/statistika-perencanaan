---
title: Lembar ringkas Python
description: Rujukan cepat untuk sintaks Python yang dipakai dalam analisis data.
---

Lembar ini untuk **mengingat kembali**, bukan menggantikan latihan. Setiap contoh dapat ditempel ke sel kode Colab. Jalankan dari atas ke bawah agar nama variabel sudah tersedia.

## Nilai, tipe, dan ekspresi

```python
nama = "Taman Utara"           # str: teks
jumlah_pengunjung = 18          # int: bilangan bulat
waktu_menit = 12.5              # float: bilangan desimal
akses_mudah = True              # bool: benar atau salah
nilai_belum_dicatat = None      # None: belum ada nilai

print(type(waktu_menit))        # tipe objek
print(jumlah_pengunjung + 2)    # penjumlahan
print(waktu_menit > 10)         # perbandingan menghasilkan bool
```

`=` memberi nilai pada nama; `==` membandingkan dua nilai. Gunakan nama yang menjelaskan isi dan satuan, misalnya `jarak_meter`, bukan `x`.

| Kebutuhan | Pola | Contoh |
|---|---|---|
| Mengubah teks angka | `int(teks)` / `float(teks)` | `float("12.5")` |
| Menggabungkan teks dan nilai | f-string | `f"Waktu: {waktu_menit} menit"` |
| Pembagian biasa | `/` | `5 / 2` menghasilkan `2.5` |
| Pembagian bulat | `//` | `5 // 2` menghasilkan `2` |
| Sisa pembagian | `%` | `5 % 2` menghasilkan `1` |
| Pangkat | `**` | `3 ** 2` menghasilkan `9` |

## List dan pengindeksan

```python
waktu = [12, 18, 10, 14]
print(waktu[0])       # 12: indeks dimulai dari nol
print(waktu[-1])      # 14: nilai terakhir
print(waktu[1:3])     # [18, 10]: indeks 1 dan 2, batas kanan tidak ikut
waktu.append(16)      # tambah satu nilai di akhir
print(len(waktu))     # banyak nilai
print(sum(waktu))     # jumlah nilai
```

List menjaga urutan dan boleh memiliki nilai berulang. Indeks `[1:3]` berarti mulai dari posisi 1 dan berhenti sebelum posisi 3.

## Keputusan dan perulangan

```python
for menit in waktu:
    if menit > 15:
        print(menit)
```

Pola umumnya:

```python
for nilai in daftar:
    if syarat:
        # lakukan sesuatu
        pass
```

`for` mengambil nilai satu per satu; `if` memilih tindakan; indentasi menunjukkan baris yang termasuk ke dalam blok.

```python
jumlah_lama = 0
for menit in waktu:
    if menit > 15:
        jumlah_lama += 1
print(jumlah_lama)
```

`+= 1` menambah penghitung satu kali. Gunakan `range(1, 5)` untuk urutan `1, 2, 3, 4` dan `enumerate(daftar, start=1)` jika nomor urut perlu ditampilkan.

## Tuple, set, dan dictionary

```python
koordinat = (-7.25, 112.75)                   # tuple: pasangan berurutan
moda_unik = set(["Bus", "Bus", "Sepeda"])   # set: hanya anggota unik
zona = {"kode": "A", "waktu_menit": 12}     # dict: kunci dipasangkan dengan nilai

print(koordinat[0])
print(sorted(moda_unik))
print(zona["waktu_menit"])
print(zona.get("jarak_meter", "belum tersedia"))
```

Gunakan list bila urutan dan pengulangan penting; tuple untuk pasangan tetap; set untuk keanggotaan unik; dictionary untuk satu catatan bernama. Untuk banyak baris data, gunakan DataFrame pandas.

## Fungsi dan galat dasar

```python
def rata_rata(nilai):
    return sum(nilai) / len(nilai)

print(rata_rata([10, 12, 14]))  # 12.0
```

`def` membuat fungsi, `nilai` adalah masukan, dan `return` mengirim hasil kembali. `print()` hanya menampilkan; ia tidak menggantikan `return`.

Jika muncul galat, baca baris terakhir pesannya, cek nama variabel dan tanda kurung, lalu jalankan contoh kecil. Indentasi yang salah biasanya menghasilkan `IndentationError`; nama yang belum dibuat menghasilkan `NameError`; tipe yang tidak cocok bisa menghasilkan `TypeError`.

## Membaca dan memeriksa CSV dengan pandas

```python
import pandas as pd

data = pd.read_csv("perjalanan_contoh.csv")
print(data.shape)                         # (jumlah baris, jumlah kolom)
print(data.head())                        # contoh lima baris pertama
print(data.columns.tolist())              # nama kolom
print(data.dtypes)                        # tipe kolom
print(data.isna().sum())                  # banyak nilai kosong per kolom
print(data["moda"].value_counts())         # frekuensi kategori
print(data["waktu_menit"].mean())         # rata-rata
print(data["waktu_menit"].median())       # median
print(data["waktu_menit"].std())          # simpangan baku sampel
```

| Kode | Makna |
|---|---|
| `import pandas as pd` | Memuat pustaka tabel dengan nama pendek `pd`. |
| `pd.read_csv(...)` | Membaca CSV menjadi DataFrame. Nama/lokasi berkas harus benar. |
| `.shape` | Menampilkan jumlah baris dan kolom sebagai pasangan. |
| `.head()` | Membantu memeriksa nilai dan nama kolom sebelum analisis. |
| `.dtypes` | Memeriksa apakah angka terbaca sebagai angka atau teks. |
| `.isna().sum()` | Menghitung sel kosong; belum memutuskan bagaimana menanganinya. |
| `.value_counts()` | Menghitung frekuensi setiap label. |

## NumPy dan Matplotlib

```python
import numpy as np
nilai = np.array([8, 10, 12, 14, 16])
print(nilai.mean())
print(nilai[nilai > 12])       # pilih nilai yang memenuhi syarat
```

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.bar(["Bus", "Sepeda"], [12, 7])
ax.set_ylabel("Jumlah perjalanan")
ax.set_title("Jumlah menurut moda")
fig.tight_layout()
plt.show()
```

`fig` adalah keseluruhan gambar; `ax` adalah bidang berisi grafik. `bar()` membuat batang kategori. Judul, nama sumbu, dan satuan memberi konteks kepada pembaca. Pada lab interaktif situs, simpan grafik dengan `fig.savefig("/tmp/statistik-plot.svg")` agar gambar tampil di halaman.

## Pemeriksaan sebelum mengumpulkan analisis

- Apakah setiap nama variabel menjelaskan nilai dan satuannya?
- Apakah kode dijalankan berurutan dari awal tanpa mengandalkan sel lama?
- Apakah jumlah baris, tipe data, dan nilai kosong sudah diperiksa?
- Apakah ringkasan dan grafik menjawab pertanyaan yang sama?
- Apakah kesimpulan membedakan apa yang terlihat pada data dan apa yang belum bisa dipastikan?

Lanjut ke [latihan fundamental Python](../cek-pemahaman/) untuk menguji pemahaman dengan lab yang dapat diubah dan dijalankan.
