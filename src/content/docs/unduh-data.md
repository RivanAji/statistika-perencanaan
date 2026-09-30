---
title: Unduh data
description: Dua dataset simulasi, kamus kolom, dan notebook untuk mengikuti contoh.
---

Dua berkas CSV di bawah dapat dibuka di Google Colab. **Keduanya simulasi yang disusun khusus untuk belajar**, sehingga tidak mewakili penduduk atau wilayah nyata.

## Kasus terpandu: perjalanan

- [Unduh perjalanan - contoh.csv](../data/perjalanan_contoh.csv) 
- [Unduh notebook](../notebooks/statistik-perencanaan-python.ipynb)

Satu baris mewakili satu perjalanan ilustratif. Ada delapan baris dan dua kolom. Tidak ada nilai kosong. Angka ditetapkan secara manual agar pembaca dapat memeriksa setiap hitungan. Tidak ada lokasi, tanggal, atau prosedur sampling yang dapat dipakai untuk generalisasi.

| Kolom | Isi dan satuan | Peran |
|---|---|---|
| `moda` | Bus, Motor, Jalan kaki, Sepeda | Kategori nominal |
| `waktu_menit` | Lama perjalanan dalam menit | Besaran rasio |

## Kasus mandiri: akses taman

[Unduh akses taman - latihan.csv](../data/akses_taman_latihan.csv)

Satu baris mewakili satu zona ilustratif. Ada 12 zona, diberi kode A sampai L. Angka dan kategori juga ditetapkan secara manual. Berkas ini disediakan untuk [latihan mandiri](../latihan/akses-taman/), bukan pembuktian kondisi akses taman di suatu kota.

| Kolom | Isi dan satuan | Peran |
|---|---|---|
| `zona` | Kode A sampai L | Penanda nominal |
| `jalan_kaki_menit` | Perkiraan waktu berjalan kaki ke taman, menit | Besaran rasio dalam skenario |
| `jarak_meter` | Jarak ke taman, meter | Besaran rasio dalam skenario |
| `kondisi_trotoar` | Baik, Cukup, Kurang | Kategori berurutan; jaraknya tidak otomatis setara |

:::caution[Makna data simulasi]
Pola di dua tabel sengaja mudah diamati. Hubungan pada tabel tidak membuktikan sebab akibat. Jangan menyebut angka ini sebagai temuan survei atau dasar kebijakan untuk wilayah nyata.
:::

## Memasukkan CSV ke Colab

Di panel **Files** Colab, pilih **Upload** lalu pilih CSV. Berkas yang diunggah ke sesi Colab dapat hilang saat sesi berakhir. Simpan salinan CSV di komputer Anda. Pada notebook unduhan, data contoh sudah tertanam agar latihan pertama dapat langsung berjalan; cara mengunggah CSV tetap dijelaskan di [bab membaca data](../python/membaca-data/).
