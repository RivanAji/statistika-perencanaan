---
title: Fungsi dan modul
description: Membungkus langkah yang berulang, memakai modul, dan membaca pesan galat.
---

Fungsi memberi nama pada sebuah pekerjaan. Ketika aturan hitung berubah, Anda cukup memperbaiki satu tempat.

## Menulis fungsi sederhana

```python
def rata_rata(nilai):
    return sum(nilai) / len(nilai)

menit = [12, 18, 10, 14]
print(rata_rata(menit))
```

Keluaran: `13.5`. `def` mendefinisikan fungsi, `nilai` adalah parameter, dan `return` mengirim hasil ke pemanggil. `print` hanya menampilkan; `return` membuat hasil dapat dipakai lagi.

```python
hasil = rata_rata([8, 16, 30])
print(round(hasil, 2))
```

Keluaran: `18.0`. `round(..., 2)` mengatur tampilan sampai dua tempat desimal; ia tidak mengubah cara rata-rata dihitung.

## Argumen dengan nilai bawaan

Nilai bawaan membuat satu fungsi tetap mudah dipakai untuk kebutuhan umum, tetapi masih dapat diatur saat diperlukan.

```python
def rata_rata_bulat(nilai, digit=2):
    if len(nilai) == 0:
        raise ValueError("Daftar nilai tidak boleh kosong")
    return round(sum(nilai) / len(nilai), digit)

print(rata_rata_bulat([12, 18, 10]))
print(rata_rata_bulat([12, 18, 10], digit=1))
```

Keluaran:

```text
13.33
13.3
```

`digit=2` dipakai jika pemanggil tidak memberi nilai lain. Nama `digit=1` membuat maksud argumen terlihat tanpa bergantung pada urutan posisi.

## Periksa masukan yang tidak sah

List kosong tidak memiliki rata-rata. Pesan yang jelas lebih berguna daripada `ZeroDivisionError` yang muncul belakangan.

```python
def rata_rata(nilai):
    if len(nilai) == 0:
        raise ValueError("Daftar nilai tidak boleh kosong")
    return sum(nilai) / len(nilai)
```

`raise` menghentikan fungsi dan memberi alasan. Untuk pembelajar awal, cukup pahami bahwa galat adalah informasi tentang langkah yang gagal, bukan tanda bahwa seluruh notebook rusak.

## Memakai modul

Modul adalah kumpulan fungsi. Python menyediakan `statistics` dan `math` tanpa instalasi tambahan.

```python
import statistics as st
from math import comb

nilai = [12, 18, 10, 14]
print(st.mean(nilai))
print(st.median(nilai))
print(comb(4, 2))
```

Keluaran: `13.5`, `13.0`, dan `6`. `st.mean` mencari rata-rata; `comb(4, 2)` menghitung banyak cara memilih dua dari empat. Bentuk `import ... as ...` membuat nama singkat, sedangkan `from ... import ...` mengambil fungsi tertentu.

Beberapa fungsi bawaan berguna saat menata data sebelum analisis. `zip()` memasangkan nilai pada posisi yang sama, lalu `dict()` dapat membentuk catatan berkunci.

```python
nama = ["A", "B", "C"]
waktu = [12, 18, 10]
catatan = dict(zip(nama, waktu))
print(catatan)
```

Keluaran: `{'A': 12, 'B': 18, 'C': 10}`. Jika panjang dua list berbeda, `zip()` berhenti pada list yang lebih pendek. Periksa panjang input ketika setiap pasangan wajib lengkap.

## Argumen dan hasil

```python
def proporsi(jumlah_kejadian, jumlah_total):
    if jumlah_total <= 0:
        raise ValueError("Penyebut harus positif")
    return jumlah_kejadian / jumlah_total

print(proporsi(2, 8))
```

Keluaran: `0.25`. Argumen pertama adalah pembilang, kedua penyebut. Nama yang jelas mengurangi risiko menukar keduanya. Fungsi ini tidak memeriksa apakah pembilang lebih besar dari penyebut; pada analisis nyata, definisi kejadian tetap harus diperiksa.

## Saat kode gagal

| Pesan | Arti yang mungkin | Pemeriksaan pertama |
|---|---|---|
| `NameError` | Nama belum didefinisikan | Jalankan sel sebelumnya, periksa ejaan |
| `SyntaxError` | Bentuk kode salah | Periksa `:`, kurung, dan tanda kutip |
| `IndentationError` | Blok tidak rapi | Samakan empat spasi di dalam blok |
| `TypeError` | Operasi tidak cocok dengan tipe | Jalankan `type(nilai)` |
| `ValueError` | Bentuk nilai tidak sesuai | Periksa isi nilai dan aturan fungsi |
| `FileNotFoundError` | Berkas tidak ditemukan | Periksa nama dan lokasi berkas |

:::tip[Bantuan di notebook]
Ketik `help(st.mean)` untuk membaca dokumentasi fungsi. Di Colab, `st.mean?` juga menampilkan bantuan singkat. Coba contoh kecil sebelum menerapkan fungsi pada satu tabel penuh.
:::

## Mini test

Tuliskan fungsi `selisih(akhir, awal)` yang mengembalikan perubahan nilai. Jalankan untuk `akhir=18` dan `awal=12`. Apa arti hasil negatif?

<details><summary>Periksa pembahasan</summary>

```python
def selisih(akhir, awal):
    return akhir - awal

print(selisih(18, 12))
```

Keluaran: `6`. Hasil negatif berarti nilai akhir lebih kecil daripada nilai awal, selama kedua nilai memakai satuan dan definisi yang sama.

</details>

Lanjut ke [membaca galat](../galat-debugging/) untuk belajar memecahkan masalah selangkah demi selangkah.
