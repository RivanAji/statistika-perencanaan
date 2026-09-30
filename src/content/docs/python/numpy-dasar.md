---
title: Dasar NumPy
description: Array numerik, operasi per elemen, bentuk data, dan penyaringan untuk statistik.
---

NumPy menyediakan array numerik yang cocok untuk perhitungan berulang. Pandas memakai NumPy di banyak bagian internalnya, tetapi Anda dapat memakai NumPy langsung ketika data sudah berbentuk deret angka.

## Membuat array

```python
import numpy as np

waktu = np.array([12, 18, 10, 14, 8, 16, 12, 30])
print(waktu.shape)
print(waktu.dtype)
```

Keluaran:

```text
(8,)
int64
```

`shape` menunjukkan delapan nilai dalam satu dimensi. `dtype` menjelaskan tipe angka yang disimpan. Tipe dapat berbeda pada sistem tertentu, tetapi operasi dan bentuk array tetap sama.

## Operasi pada seluruh array

Operasi NumPy diterapkan pada setiap elemen tanpa menulis `for` secara manual.

```python
print(waktu + 2)
print(waktu / 2)
print(waktu.mean())
```

Keluaran:

```text
[14 20 12 16 10 18 14 32]
[ 6.   9.   5.   7.   4.   8.   6.  15. ]
15.0
```

`waktu + 2` menambah dua menit pada setiap nilai. Operasi ini menghasilkan array baru; `waktu` tetap berisi data awal kecuali Anda menetapkan hasilnya kembali.

## Indeks dan mask boolean

Indeks dimulai dari 0, seperti pada list. Perbandingan terhadap array menghasilkan mask boolean yang dapat dipakai untuk memilih nilai.

```python
print(waktu[0], waktu[-1])
mask = waktu > 15
print(mask)
print(waktu[mask])
```

Keluaran:

```text
12 30
[False  True False False False  True False  True]
[18 16 30]
```

Mask menjaga posisi setiap pemeriksaan. Hasil `[18, 16, 30]` berisi waktu yang lebih dari 15 menit, termasuk 18, 16, dan 30.

## Array dua dimensi

Array dua dimensi dapat mewakili baris dan kolom. Parameter `axis=0` menghitung ringkasan per kolom, sedangkan `axis=1` menghitung per baris.

```python
pasangan = np.array([
    [12, 450],
    [18, 700],
    [10, 600],
])
print(pasangan.shape)
print(pasangan.mean(axis=0))
```

Keluaran:

```text
(3, 2)
[ 13.33333333 583.33333333]
```

Kolom pertama berisi waktu, kolom kedua berisi jarak. Jangan menghitung rata-rata pada kolom berbeda satuan tanpa memberi makna yang jelas. Untuk tabel dengan nama kolom dan kategori, gunakan `DataFrame` pandas agar nama dan tipe lebih mudah ditelusuri.

## Fungsi ringkasan dan nilai hilang

Gunakan fungsi NumPy untuk ringkasan yang eksplisit. `np.nan` menandai angka yang hilang, lalu `np.nanmean()` mengabaikannya saat menghitung rata-rata.

```python
nilai = np.array([12.0, np.nan, 18.0, 10.0])
print(np.isnan(nilai))
print(np.nanmean(nilai))
```

Keluaran:

```text
[False  True False False]
13.333333333333334
```

Mengabaikan nilai hilang adalah keputusan analisis. Periksa mengapa nilai hilang muncul sebelum memilih fungsi ringkasan.

## Mini test

Buat array `np.array([8, 15, 22])`. Pilih nilai yang lebih besar atau sama dengan 15, lalu hitung rata-ratanya.

<details><summary>Periksa pembahasan</summary>

```python
nilai = np.array([8, 15, 22])
terpilih = nilai[nilai >= 15]
print(terpilih)
print(terpilih.mean())
```

Keluaran:

```text
[15 22]
18.5
```

Operator `>=` memasukkan nilai tepat 15. Tulis batas kategori dengan hati-hati karena mengganti `>=` menjadi `>` akan mengubah anggota yang dipilih.

</details>

Lanjutkan ke [visualisasi sederhana](../visualisasi/) atau kembali ke [pandas untuk membaca CSV](../membaca-data/).
