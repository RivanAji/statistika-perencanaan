---
title: Sintaks dan variabel
description: Membaca perintah Python, menyimpan nilai, dan menulis hitungan sederhana.
---

Python menjalankan instruksi dari atas ke bawah. Bayangkan daftar langkah untuk menghitung waktu perjalanan: simpan angka, lakukan operasi, lalu tampilkan hasilnya. Setiap baris memberi satu instruksi.

## 1. Tampilkan sesuatu

```python
print("Halo, data!")
```

Keluaran:

```text
Halo, data!
```

`print` adalah nama perintah untuk menampilkan sesuatu. Tanda kurung membungkus isi yang akan ditampilkan. Tanda kutip memberi tahu Python bahwa `Halo, data!` adalah teks.

```python
print(2 + 3)
print("2 + 3")
```

Keluaran:

```text
5
2 + 3
```

Tanpa tanda kutip, Python menghitung. Dengan tanda kutip, Python menampilkan tulisan apa adanya.

:::note[Huruf besar dan kecil]
Python membedakan huruf besar dan kecil. `print` dikenali, tetapi `Print` dianggap nama yang berbeda.
:::

## 2. Simpan nilai dalam variabel

Variabel adalah nama untuk nilai yang ingin dipakai lagi. Bayangkan label pada wadah: label `waktu_menit` membantu kita tahu angka di dalamnya.

```python
waktu_menit = 18
moda = "Bus"
print(moda)
print(waktu_menit)
```

Keluaran:

```text
Bus
18
```

Tanda `=` berarti **simpan nilai di sebelah kanan dengan nama di sebelah kiri**. Nama variabel sebaiknya menjelaskan isinya. Gunakan huruf kecil dan garis bawah; nama tidak boleh diawali angka.

```python
waktu_menit = waktu_menit + 2
print(waktu_menit)
```

Keluaran: `20`.

Python membaca nilai lama, menambah 2, lalu menyimpan hasilnya kembali dengan nama yang sama. Menjalankan sel itu sekali lagi akan menghasilkan 22. Jika urutan sel notebook membingungkan, jalankan ulang dari atas agar nilai dimulai dari keadaan awal.

## 3. Hitung dengan operator

| Tanda | Arti | Contoh | Hasil |
|---|---|---|---:|
| `+` | tambah | `12 + 3` | 15 |
| `-` | kurang | `12 - 3` | 9 |
| `*` | kali | `12 * 3` | 36 |
| `/` | bagi | `7 / 2` | 3.5 |
| `//` | bagi bulat | `7 // 2` | 3 |
| `%` | sisa pembagian | `7 % 2` | 1 |
| `**` | pangkat | `2 ** 3` | 8 |

Python mengikuti urutan operasi matematika: perkalian dan pembagian lebih dahulu daripada penjumlahan dan pengurangan. Pakai tanda kurung untuk memperjelas urutan.

```python
jarak_km = 3
waktu_menit = 15
waktu_jam = waktu_menit / 60
kecepatan_km_jam = jarak_km / waktu_jam
print(kecepatan_km_jam)
```

Keluaran: `12.0` km/jam. Kode memecah rumus menjadi beberapa langkah bernama, sehingga satuan dan perhitungannya lebih mudah diperiksa.

## 4. Kenali nilai angka dan teks

Angka dapat dihitung, sedangkan teks dipakai untuk label. Python membedakan keduanya. Kelak Anda akan mempelajari nama tipe datanya: bilangan bulat (`int`), bilangan desimal (`float`), teks (`str`), dan benar/salah (`bool`). Untuk saat ini, perhatikan hasil operasi berikut.

```python
print(8 + 2)
print("8" + "2")
```

Keluaran:

```text
10
82
```

Angka di dalam tanda kutip adalah teks; tanda `+` menyambung teks. Jika nilai angka datang sebagai teks, ubah dengan sengaja:

```python
jumlah_teks = "8"
jumlah = int(jumlah_teks)
print(jumlah + 2)
print(float("2.5") * 2)
```

Keluaran:

```text
10
5.0
```

Konversi hanya berhasil jika teks memang berbentuk angka. `int("delapan")` tidak dapat ditebak Python dan akan memunculkan galat.

## 5. Baca keluaran sebelum melanjutkan

```python
jarak_km = 2.4
waktu_menit = 12
kecepatan_km_jam = jarak_km / (waktu_menit / 60)
print("Kecepatan:", kecepatan_km_jam, "km/jam")
```

Keluaran:

```text
Kecepatan: 12.0 km/jam
```

Koma di dalam `print()` menampilkan beberapa nilai berurutan. Keluaran adalah petunjuk untuk memeriksa hasil, bukan sekadar hiasan. Tanyakan: apakah besar angkanya masuk akal, apakah satuannya benar, dan apakah rumus menjawab pertanyaan?

## 6. Tambahkan komentar seperlunya

```python
# Ubah menit menjadi jam sebelum menghitung kecepatan.
waktu_jam = waktu_menit / 60
```

Tanda `#` membuat sisa baris menjadi catatan untuk pembaca; Python tidak menjalankannya. Komentar paling berguna untuk menjelaskan alasan atau asumsi, bukan mengulang kode dengan kata-kata lain.

:::caution[Spasi dan tanda baca punya arti]
Tanda kutip yang tidak berpasangan, kurung yang belum ditutup, atau salah eja nama dapat menghentikan kode. Baca pesan galat dari baris terakhir, lalu periksa baris yang disebutkan. Ada panduan khusus di [Membaca galat](../galat-debugging/).
:::

## Coba sendiri

Simpan `jarak_km = 2.4` dan `waktu_menit = 12`. Hitung kecepatan dalam km/jam. Sebelum menjalankan kode, tulis perkiraan hasilnya. Lalu ubah waktu menjadi 24 menit dan jelaskan perubahan keluaran.

<details><summary>Periksa pembahasan</summary>

```python
jarak_km = 2.4
waktu_menit = 12
print(jarak_km / (waktu_menit / 60))
```

Hasil pertama `12.0` km/jam. Pada jarak sama dan waktu 24 menit, hasilnya `6.0` km/jam. Waktu menjadi dua kali lipat, sehingga kecepatan rata-ratanya menjadi setengah.

</details>

Berikutnya: [tipe data, teks, dan list](../tipe-koleksi/).
