---
title: Membaca galat dan mencari kesalahan
description: Memakai pesan Python sebagai petunjuk untuk memperbaiki kode selangkah demi selangkah.
---

Galat bukan nilai untuk dihafal. Anggap pesan galat seperti catatan di tepi resep: Python memberi tahu langkah yang tidak dapat dikerjakan. Baca pesan dari bagian bawah, lalu periksa baris yang disebutkan.

## Mulai dari tiga petunjuk

1. **Jenis galat** biasanya tertulis di baris paling bawah.
2. **Baris kode** yang ditunjuk menunjukkan tempat Python berhenti.
3. **Nama atau nilai** pada pesan memberi petunjuk yang lebih khusus.

| Pesan | Arti sederhana | Pemeriksaan awal |
|---|---|---|
| `SyntaxError` | Susunan kode belum sesuai tata bahasa | Kurung dan kutip berpasangan? Tanda `:` ada? |
| `NameError` | Nama yang dipakai belum dikenal | Sel pembuat variabel sudah dijalankan? Ejaannya sama? |
| `TypeError` | Operasi tidak cocok dengan jenis nilai | Apakah angka tercampur dengan teks? |
| `ValueError` | Jenis nilai benar, tetapi isinya tidak sesuai | Apakah semua karakter dapat diubah menjadi angka? |
| `IndexError` | Posisi list yang diminta tidak tersedia | Berapa panjang list? Ingat indeks mulai dari 0. |
| `KeyError` | Nama kunci atau kolom tidak ditemukan | Periksa ejaan dengan `.columns` atau `dict.keys()`. |
| `ZeroDivisionError` | Perhitungan membagi dengan nol | Periksa penyebut dan jumlah data. |

## Contoh: nama belum dibuat

Kode berikut menghasilkan `NameError` karena nama `waktu_menit` belum pernah diberi nilai pada sesi ini:

```python
print(waktu_menit)
```

Cara memperbaiki: jalankan sel yang membuat variabel, atau buat nilainya lebih dahulu.

```python
waktu_menit = 18
print(waktu_menit)
```

Keluaran: `18`.

## Contoh: tipe nilai tidak cocok

```python
teks = "18"
angka = int(teks)
print(angka + 2)
```

Keluaran: `20`. Teks `"18"` terlihat seperti angka, tetapi Python memperlakukannya sebagai `str`. `int()` mengubahnya menjadi bilangan bulat. Jika teksnya `"18 menit"`, konversi gagal karena kata-katanya bukan bagian dari bilangan.

## Perbaiki satu hal dalam satu waktu

Jika hasil tidak sesuai dugaan:

1. Baca baris paling bawah dari pesan galat.
2. Periksa nama dan tanda baca pada baris yang ditunjuk.
3. Tampilkan nilai perantara dengan `print()` atau periksa tipe dengan `type()`.
4. Ubah satu bagian kecil, lalu jalankan ulang.
5. Setelah benar, jalankan notebook dari atas untuk memastikan tidak bergantung pada nilai lama.

Contoh pemeriksaan:

```python
nilai = "18"
print(type(nilai).__name__)
print(nilai)
```

Keluaran:

```text
str
18
```

Jika hasil perhitungan salah tetapi tidak ada galat, Python mungkin menjalankan perintah yang sah dengan rumus yang tidak sesuai maksud. Periksa satuan, tanda pembanding (`>` atau `>=`), urutan kolom, dan ukuran penyebut.

:::caution[Jangan menutupi galat terlalu cepat]
Jangan menghapus baris atau mengganti nilai hanya supaya kode berjalan. Cari dulu penyebabnya dan catat keputusan yang mengubah data. Kesalahan kode dan masalah mutu data adalah dua hal berbeda.
:::

## Coba sendiri

Perhatikan kode ini:

```python
jarak_km = "2.5"
waktu_jam = 0.5
print(jarak_km / waktu_jam)
```

Tentukan jenis galat yang mungkin muncul. Perbaiki kode dengan konversi tipe yang sesuai, lalu hitung kecepatan.

<details>
<summary>Periksa pembahasan</summary>

`TypeError` muncul karena teks dibagi dengan angka. Ubah jarak menjadi bilangan desimal:

```python
jarak_km = float("2.5")
waktu_jam = 0.5
print(jarak_km / waktu_jam)
```

Keluaran: `5.0` km/jam.

</details>

Lanjut ke [koleksi lanjutan](../koleksi-lanjutan/) untuk melihat tuple, set, dan dictionary.
