---
title: Membaca CSV dengan pandas
description: Memuat tabel, memeriksa kolom, nilai kosong, dan kesalahan yang umum.
---

Pustaka `pandas` menyediakan bentuk tabel bernama `DataFrame`. Contoh di bawah memakai delapan baris data simulasi yang sama dengan [CSV perjalanan](../../unduh-data/). `StringIO` membuat contoh dapat langsung dijalankan tanpa mengatur lokasi berkas lebih dahulu.

```python
from io import StringIO
import pandas as pd

csv_text = """moda,waktu_menit
Bus,12
Bus,18
Motor,10
Motor,14
Jalan kaki,8
Jalan kaki,16
Sepeda,12
Sepeda,30
"""

data = pd.read_csv(StringIO(csv_text))
print(data.shape)
print(data.columns.tolist())
```

Keluaran:

```text
(8, 2)
['moda', 'waktu_menit']
```

`import` memuat pustaka. `as pd` memberi nama singkat. `read_csv` membaca CSV dari objek teks. `shape` menampilkan `(jumlah baris, jumlah kolom)`. Nama kolom harus sama persis ketika digunakan di kode.

Jika CSV sudah diunggah ke Colab, ganti baris pembacaan dengan:

```python
data = pd.read_csv("perjalanan_contoh.csv")
```

Pastikan nama berkas sama dengan yang terlihat pada panel Files.

## Pandas setelah Python dasar

`DataFrame` adalah tabel. Satu kolom yang dipilih, misalnya `data["waktu_menit"]`, berupa `Series`. Banyak operasi pandas bekerja pada seluruh kolom sekaligus sehingga Anda tidak perlu menulis loop untuk setiap baris.

```python
print(data.head(3).to_string(index=False))
```

Keluaran:

```text
 moda  waktu_menit
  Bus           12
  Bus           18
Motor           10
```

Satu baris berarti satu perjalanan ilustratif. Urutan baris tidak menyatakan urutan waktu kejadian.

```python
print(data.isna().sum().to_string())
```

Keluaran:

```text
moda            0
waktu_menit     0
```

Nol berarti tidak ada sel kosong pada kolom tersebut. Pemeriksaan ini tidak membuktikan bahwa seluruh nilai benar; angka 30 menit, misalnya, masih perlu diperiksa dalam konteks.

Periksa tipe kolom numerik dan jumlah tiap kategori:

```python
print(data["waktu_menit"].dtype == "int64")
print(data["moda"].value_counts().sort_index().to_string())
```

Keluaran:

```text
True
Bus           2
Jalan kaki    2
Motor         2
Sepeda        2
```

Pemeriksaan tipe membantu menemukan angka yang terbaca sebagai teks. `value_counts()` menghitung banyak baris per kategori, sedangkan `sort_index()` membuat urutan label konsisten saat dibaca.

## Periksa tipe dan ringkasan

```python
print(data.dtypes.to_string())
print(data["waktu_menit"].describe().to_string())
```

`dtypes` membantu memastikan angka tidak terbaca sebagai teks. `describe()` memberi hitungan, mean, simpangan baku, minimum, kuartil, dan maksimum untuk kolom numerik. Gunakan hasilnya sebagai pemeriksaan awal, lalu baca arti setiap ukuran pada bab statistik deskriptif.

Keluaran `describe()` untuk delapan waktu:

```text
count     8.000000
mean     15.000000
std       6.845228
min       8.000000
25%      11.500000
50%      13.000000
75%      16.500000
max      30.000000
```

Tipe kolom teks dapat tampil sebagai `object` atau `str`, bergantung versi pandas. Kolom `waktu_menit` harus terbaca sebagai bilangan.

## Pilih kolom, baris, dan syarat

```python
print(data[["moda", "waktu_menit"]].head(2).to_string(index=False))
print(data.loc[data["waktu_menit"] > 15, ["moda", "waktu_menit"]].to_string(index=False))
```

Keluaran bagian kedua:

```text
      moda  waktu_menit
       Bus           18
Jalan kaki           16
    Sepeda           30
```

`data["waktu_menit"] > 15` menghasilkan deret `True` atau `False`. `.loc[syarat, kolom]` mengambil baris yang benar dan kolom yang disebutkan. `> 15` tidak memasukkan nilai tepat 15.

## Kelompokkan tanpa menghilangkan konteks

```python
ringkasan = data.groupby("moda")["waktu_menit"].mean()
print(ringkasan.to_string())
```

Keluaran:

```text
moda
Bus           15.0
Jalan kaki    12.0
Motor         12.0
Sepeda        21.0
```

Rata-rata Sepeda lebih tinggi karena dua nilainya 12 dan 30. Tiap moda hanya memiliki dua baris ilustratif; perbedaan ini tidak menjelaskan kinerja moda di luar tabel. Selalu tampilkan jumlah per kelompok ketika bekerja dengan data nyata.

Gabungkan jumlah dan rata-rata agar ukuran kelompok tetap terlihat:

```python
ringkasan_lengkap = data.groupby("moda")["waktu_menit"].agg(["count", "mean"])
print(ringkasan_lengkap.to_string())
```

Keluaran:

```text
            count  mean
moda                   
Bus             2  15.0
Jalan kaki      2  12.0
Motor           2  12.0
Sepeda          2  21.0
```

Jumlah `2` pada setiap baris adalah ukuran kelompok dalam tabel simulasi. Pada data nyata, tuliskan jumlah ini bersama rata-rata agar pembaca dapat menilai dasar perbandingannya.

## Mengurutkan dan membuat kolom turunan

`sort_values()` mengubah urutan tampilan tanpa mengubah makna kolom. Kolom baru dapat menandai aturan analisis yang sudah ditulis dengan jelas.

```python
terlama = data.sort_values("waktu_menit", ascending=False)
print(terlama[["moda", "waktu_menit"]].head(3).to_string(index=False))

data["lebih_15_menit"] = data["waktu_menit"] > 15
print(data["lebih_15_menit"].sum())
```

Keluaran:

```text
      moda  waktu_menit
    Sepeda           30
       Bus           18
Jalan kaki           16
3
```

Kolom `lebih_15_menit` berisi `True` atau `False`. Menjumlahkan boolean menghitung banyak nilai `True`, sehingga hasilnya 3.

## Simpan hasil turunan

```python
data.to_csv("perjalanan_dengan_label.csv", index=False)
```

Berkas keluaran baru memuat kolom boolean. `index=False` mencegah indeks pandas menjadi kolom tambahan dalam CSV. Simpan berkas mentah terpisah dan beri nama jelas pada hasil turunan.

:::caution[Kesalahan nama berkas]
`FileNotFoundError` berarti Python tidak menemukan CSV pada lokasi yang Anda tulis. Lihat panel Files dan cocokkan huruf serta akhiran `.csv`. `KeyError` biasanya berarti nama kolom salah eja. Jalankan `print(data.columns.tolist())` untuk melihat nama yang tersedia.
:::

## Coba sendiri

Tampilkan dua baris terakhir dengan `data.tail(2)`. Berapa waktu pada baris terakhir? Sebutkan satu alasan mengapa nilai itu tidak boleh langsung dihapus.

<details><summary>Periksa jawaban</summary>

```python
print(data.tail(2).to_string(index=False))
```

Baris terakhir berisi 30 menit. Nilai itu lebih tinggi daripada banyak baris lain, tetapi CSV tidak menyediakan bukti bahwa nilainya salah. Periksa sumber dan definisinya sebelum mengubah data.

</details>
