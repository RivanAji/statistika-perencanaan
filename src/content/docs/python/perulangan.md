---
title: Perulangan
description: Mengulangi langkah untuk setiap nilai dan membuat hitungan sederhana.
---

Jika daftar berisi banyak zona, menulis perintah yang sama berkali-kali melelahkan dan mudah salah. **Perulangan** meminta Python melakukan langkah yang sama untuk setiap nilai.

## Baca satu per satu dengan `for`

```python
waktu_menit = [12, 18, 10]
for waktu in waktu_menit:
    print(waktu)
```

Keluaran:

```text
12
18
10
```

Bacanya: untuk setiap nilai di `waktu_menit`, sebut nilai itu sementara dengan nama `waktu`, lalu jalankan baris yang menjorok. Python mengulangi baris tersebut tiga kali.

| Putaran | `waktu` berisi | Yang dicetak |
|---:|---:|---:|
| 1 | 12 | 12 |
| 2 | 18 | 18 |
| 3 | 10 | 10 |

Nama `waktu` hanya berlaku untuk nilai yang sedang diproses. Anda dapat memilih nama lain, tetapi pilih yang menjelaskan isi.

## Tambahkan keputusan di dalam perulangan

```python
waktu_menit = [12, 18, 10]
jumlah_lama = 0

for waktu in waktu_menit:
    if waktu > 15:
        jumlah_lama = jumlah_lama + 1

print(jumlah_lama)
```

Keluaran: `1`.

`jumlah_lama` mulai dari 0. Setiap kali syarat benar, Python menambah nilainya satu. Trace singkatnya:

| Putaran | `waktu` | `waktu > 15` | `jumlah_lama` setelah pemeriksaan |
|---:|---:|---|---:|
| 1 | 12 | `False` | 0 |
| 2 | 18 | `True` | 1 |
| 3 | 10 | `False` | 1 |

`jumlah_lama += 1` adalah bentuk singkat dari `jumlah_lama = jumlah_lama + 1`.

## Gunakan `range()` untuk mengulang hitungan

```python
for nomor in range(3):
    print(nomor)
```

Keluaran: `0`, `1`, `2`. `range(3)` berhenti sebelum angka 3. Jika nomor yang terlihat ingin mulai dari 1, gunakan `range(1, 4)`.

Gunakan `enumerate()` jika memerlukan nomor dan nilai sekaligus:

```python
moda = ["Bus", "Motor", "Sepeda"]
for nomor, nama_moda in enumerate(moda, start=1):
    print(nomor, nama_moda)
```

Keluaran:

```text
1 Bus
2 Motor
3 Sepeda
```

Untuk mengolah isi list, biasanya tidak perlu membuat nomor sendiri. `for nilai in daftar` lebih mudah dibaca daripada mengakses posisi satu per satu.

## Pola pengulangan yang sering dipakai

### Mengumpulkan jumlah dan rata-rata

Akumulator menyimpan hasil sementara. Mulai dari nilai awal yang sesuai, lalu perbarui pada setiap putaran.

```python
waktu = [12, 18, 10]
jumlah = 0

for menit in waktu:
    jumlah += menit

rata_rata = jumlah / len(waktu)
print("Jumlah:", jumlah)
print("Rata-rata:", rata_rata)
```

Keluaran:

```text
Jumlah: 40
Rata-rata: 13.333333333333334
```

`jumlah` bertambah 12, lalu 18, lalu 10. `len(waktu)` menghitung banyak observasi. Untuk hasil tampilan yang rapi, `round(rata_rata, 2)` menghasilkan `13.33`.

### Memproses beberapa list berpasangan

`zip()` mengambil nilai dengan posisi sama secara bersamaan. Pastikan kedua list memang sebaris dan panjangnya cocok.

```python
zona = ["A", "B", "C"]
waktu = [12, 18, 10]

for nama_zona, menit in zip(zona, waktu):
    print(nama_zona, menit)
```

Keluaran:

```text
A 12
B 18
C 10
```

Jika panjang list berbeda, `zip()` berhenti pada list yang lebih pendek. Periksa panjangnya sebelum memasangkan data agar nilai tidak hilang tanpa disadari.

### Berhenti atau lewati satu putaran

`continue` melewati sisa instruksi pada putaran itu; `break` menghentikan seluruh perulangan. Kenali dulu perulangan dasar sebelum memakai keduanya.

```python
nilai = [12, None, 18, 10]
for menit in nilai:
    if menit is None:
        continue
    if menit > 15:
        print(menit)
```

Keluaran: `18`. `None` berarti nilai belum tersedia; ia tidak sama dengan 0. Pada data nyata, catat berapa nilai yang dilewati dan mengapa.

## `while`: ulangi selama syarat masih benar

Gunakan `while` ketika berhenti bergantung pada syarat, bukan jumlah anggota list.

```python
nomor = 1
while nomor <= 3:
    print(nomor)
    nomor += 1
```

Keluaran: `1`, `2`, `3`. Setiap putaran menambah `nomor`, sampai syarat `nomor <= 3` salah.

:::caution[Hati-hati dengan pengulangan tanpa akhir]
Jika lupa mengubah `nomor`, syarat bisa terus benar dan sel tidak berhenti. Di Colab, tekan tombol berhenti pada sel yang masih berjalan. Untuk latihan awal, gunakan `for` jika jumlah pengulangan sudah diketahui.
:::

### Hindari kesalahan batas

`range(1, 4)` menghasilkan 1, 2, 3; angka batas akhir tidak ikut. Pada indeks list, posisi pertama adalah 0. Saat memakai penghitung, pastikan ia berubah pada tiap putaran yang diperlukan, dan uji dengan list kecil yang hasilnya dapat diperiksa.

## Baca list comprehension setelah memahami `for`

Python dapat menulis pengulangan sederhana dalam bentuk ringkas. Bentuk ini bukan sihir baru: ia melakukan pekerjaan `for` dan `if` yang sudah dipelajari.

```python
waktu_menit = [12, 18, 10, 30]
waktu_lama = [waktu for waktu in waktu_menit if waktu > 15]
print(waktu_lama)
```

Keluaran: `[18, 30]`. Bacanya: hasilkan `waktu` untuk setiap nilai di `waktu_menit`, tetapi ambil hanya yang lebih dari 15.

Untuk pemula, gunakan perulangan biasa jika bentuk satu baris sulit dibaca.

## Coba sendiri

Gunakan `jarak = [450, 700, 900]`. Cetak setiap jarak, lalu hitung berapa jarak yang lebih dari 600 meter.

<details>
<summary>Periksa pembahasan</summary>

```python
jarak = [450, 700, 900]
jumlah_jauh = 0
for meter in jarak:
    print(meter)
    if meter > 600:
        jumlah_jauh += 1
print("Lebih dari 600 meter:", jumlah_jauh)
```

Keluaran akhirnya `Lebih dari 600 meter: 2`. Nilai 700 dan 900 memenuhi syarat.

</details>

Lanjut ke [fungsi](../fungsi-modul/) untuk memberi nama pada langkah yang ingin digunakan berulang.
