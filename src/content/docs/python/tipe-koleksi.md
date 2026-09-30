---
title: Tipe data, teks, dan list
description: Mengenali angka, teks, benar-salah, nilai kosong, dan urutan data sederhana.
---

Nilai dalam Python memiliki **tipe**, seperti barang yang punya jenis dan kegunaan berbeda. Angka dapat dihitung, teks dapat dibaca, dan `True` atau `False` dapat dipakai untuk memilih langkah.

## Empat tipe yang sering ditemui

```python
jumlah_zona = 8
jarak_km = 2.5
nama_zona = "Kenjeran"
terpantau = True

print(type(jumlah_zona).__name__)
print(type(jarak_km).__name__)
print(type(nama_zona).__name__)
print(type(terpantau).__name__)
```

Keluaran:

```text
int
float
str
bool
```

| Tipe | Contoh | Dipakai untuk |
|---|---|---|
| `int` | `8` | hitungan bilangan bulat |
| `float` | `2.5` | ukuran yang dapat memiliki pecahan |
| `str` | `"Kenjeran"` | teks atau label |
| `bool` | `True` | hasil pemeriksaan benar atau salah |

`type()` seperti kaca pembesar: ia menunjukkan jenis nilai yang sedang diperiksa. Angka `8` dan teks `"8"` tampak mirip, tetapi berbeda bagi Python.

```python
print(8 + 2)
print("8" + "2")
```

Keluaran:

```text
10
82
```

Baris pertama menjumlahkan angka. Baris kedua menyambung dua potong teks.

## Mengubah tipe dengan sengaja

```python
teks_jumlah = "8"
jumlah = int(teks_jumlah)
jarak = float("2.5")
print(jumlah + 2)
print(jarak * 2)
```

Keluaran:

```text
10
5.0
```

Gunakan `int()` untuk bilangan bulat dan `float()` untuk bilangan desimal. `int("8 zona")` akan gagal karena seluruh teks tidak bisa dibaca sebagai angka. Cari tahu arti isi kolom sebelum mengubahnya.

## Teks sebagai label

Teks disebut **string** (`str`). Letakkan teks di antara tanda kutip tunggal atau ganda. Beberapa metode menghasilkan teks baru yang sudah dirapikan.

```python
label = "  Zona A  "
print(label.strip())
print(label.strip().lower())
print("Bus,Motor,Sepeda".split(","))
```

Keluaran:

```text
Zona A
zona a
['Bus', 'Motor', 'Sepeda']
```

`strip()` membuang spasi di awal dan akhir. `lower()` membuat huruf kecil. `split(",")` memecah teks setiap kali menemukan koma. Saat membaca CSV, pandas biasanya memisahkan kolom untuk kita.

## List menyimpan urutan

List adalah seperti daftar baris pengamatan pada kertas: urutannya terjaga dan satu nilai boleh muncul berulang.

```python
waktu_menit = [12, 18, 10]
print(len(waktu_menit))
print(waktu_menit[0])
print(waktu_menit[-1])
```

Keluaran:

```text
3
12
10
```

`len()` menghitung banyak nilai. Python mulai menghitung posisi dari **0**, jadi `[0]` adalah nilai pertama. Posisi `[-1]` berarti nilai terakhir.

```text
Nilai:    12    18    10
Posisi:    0     1     2
Posisi:   -3    -2    -1
```

Potongan list memakai bentuk `[awal:berhenti]`. Nilai pada posisi berhenti tidak ikut diambil.

```python
waktu_menit = [12, 18, 10, 14]
print(waktu_menit[1:3])
waktu_menit.append(8)
print(waktu_menit)
```

Keluaran:

```text
[18, 10]
[12, 18, 10, 14, 8]
```

`append()` menambah satu nilai di akhir. Fungsi `sum()` menjumlahkan angka dalam list, tetapi tidak bermakna jika list berisi label teks.

```python
waktu_menit = [12, 18, 10, 14]
print(sum(waktu_menit))
print(sum(waktu_menit) / len(waktu_menit))
```

Keluaran: `54` lalu `13.5`. Inilah cara menghitung mean secara langsung pada daftar kecil. Nanti pandas akan melakukan operasi serupa pada satu kolom penuh.

:::caution[Indeks di luar daftar]
Pada list berisi tiga nilai, posisi yang sah adalah `0`, `1`, dan `2`. Meminta `waktu_menit[3]` menghasilkan `IndexError`. Gunakan `len(waktu_menit)` untuk memeriksa panjangnya.
:::

## Nilai kosong dan benar-salah

`None` berarti belum ada nilai yang disimpan. Ia berbeda dari nol (`0`) dan teks kosong (`""`). `True` dan `False` biasanya muncul setelah Python membandingkan nilai.

```python
waktu = None
print(waktu is None)
print(18 > 15)
print(12 > 15)
```

Keluaran:

```text
True
True
False
```

## Coba sendiri

Buat list `waktu = [8, 12, 16]`. Tampilkan nilai pertama, nilai terakhir, banyak nilai, dan rata-ratanya. Lalu tambahkan `20` dan hitung ulang.

<details>
<summary>Periksa pembahasan</summary>

```python
waktu = [8, 12, 16]
print(waktu[0], waktu[-1], len(waktu))
print(sum(waktu) / len(waktu))
waktu.append(20)
print(sum(waktu) / len(waktu))
```

Keluaran: `8 16 3`, `12.0`, dan `14.0`. Setelah nilai 20 ditambahkan, jumlah menjadi 56 dan banyak nilai menjadi 4.

</details>

Lanjut ke [kondisi dan keputusan](../alur-kontrol/).
