---
title: Tuple, set, dan dictionary
description: Memilih wadah yang tepat untuk pasangan, anggota unik, dan catatan berkunci.
---

List cocok untuk urutan nilai. Python juga menyediakan wadah lain. Pilih berdasarkan pekerjaan yang ingin dilakukan, bukan karena semua bentuknya perlu dihafalkan.

## Tuple: satu paket nilai yang urutannya tetap

Tuple mirip daftar kecil yang tidak dirancang untuk diganti-ganti. Contohnya sepasang koordinat atau pasangan `(kode zona, nilai)`.

```python
koordinat = (112.75, -7.25)
print(koordinat[0])
print(len(koordinat))
```

Keluaran: `112.75` lalu `2`.

Tuple memakai tanda kurung `()`. Posisi pertamanya tetap di indeks `0`, seperti list. Untuk koordinat, tulis urutan yang dipakai, misalnya `(longitude, latitude)`, agar tidak tertukar.

Nilai tuple dapat dibuka ke beberapa nama sekaligus jika banyak elemennya cocok:

```python
koordinat = (112.75, -7.25)
longitude, latitude = koordinat
print("Longitude:", longitude)
print("Latitude:", latitude)
```

Keluaran: `Longitude: 112.75` lalu `Latitude: -7.25`. Urutan nama di kiri mengikuti urutan nilai di kanan. Tuple satu unsur memerlukan koma: `(112.75,)`; tanpa koma, tanda kurung hanya mengelompokkan angka.

## Set: simpan anggota unik

Set seperti daftar hadir yang hanya mencatat satu kali setiap nama. Duplikat hilang.

```python
moda = ["Bus", "Motor", "Bus", "Sepeda"]
moda_unik = set(moda)
print(len(moda_unik))
print("Bus" in moda_unik)
print(sorted(moda_unik))
```

Keluaran:

```text
3
True
['Bus', 'Motor', 'Sepeda']
```

List awal tetap memiliki empat baris. Set hanya menjawab bahwa ada tiga label berbeda. Set tidak menjamin urutan; `sorted()` dipakai agar tampilan alfabetis.

:::note[Kapan jangan pakai set]
Jangan gunakan set jika urutan baris penting, jumlah kemunculan harus dihitung, atau duplikat merupakan informasi yang ingin dipertahankan.
:::

Set juga dapat membandingkan keanggotaan:

```python
moda_survei = {"Bus", "Sepeda", "Jalan kaki"}
moda_tersedia = {"Bus", "Motor", "Sepeda"}
print(sorted(moda_survei & moda_tersedia))
print(sorted(moda_survei - moda_tersedia))
```

Keluaran:

```text
['Bus', 'Sepeda']
['Jalan kaki']
```

`&` berarti irisan anggota; `-` berarti anggota himpunan kiri yang tidak ada di kanan. Set tidak menyimpan banyaknya kemunculan. Untuk frekuensi, gunakan `collections.Counter` atau pandas `value_counts()`.

## Dictionary: catatan dengan nama bidang

Dictionary memasangkan **kunci** dengan **nilai**. Bayangkan formulir satu zona: setiap jawaban ditempatkan di bawah nama kolomnya.

```python
zona = {
    "kode": "A",
    "waktu_menit": 6,
    "trotoar": "Baik",
}
print(zona["waktu_menit"])
print(zona.keys())
```

Keluaran:

```text
6
dict_keys(['kode', 'waktu_menit', 'trotoar'])
```

Kunci harus cocok persis. Mengakses `zona["jarak"]` akan menghasilkan `KeyError` karena kunci itu belum ada.

```python
print(zona.get("jarak_meter", "belum dicatat"))
zona["waktu_menit"] = 8
print(zona)
```

Keluaran:

```text
belum dicatat
{'kode': 'A', 'waktu_menit': 8, 'trotoar': 'Baik'}
```

`.get()` berguna ketika kunci boleh belum tersedia. Menetapkan nilai pada kunci yang sudah ada mengganti nilai lama.

## Bandingkan wadahnya

| Struktur | Menjaga urutan? | Boleh diubah? | Contoh pekerjaan |
|---|---|---|---|
| `list` | Ya | Ya | kumpulan waktu, termasuk duplikat |
| `tuple` | Ya | Tidak | pasangan koordinat yang tetap |
| `set` | Tidak | Ya | mencari kategori berbeda |
| `dict` | Berdasarkan kunci | Ya | menyimpan satu catatan dengan nama bidang |
| `DataFrame` | Ya, sebagai tabel | Ya | banyak catatan dalam baris dan kolom |

Untuk berkas statistik yang berisi banyak observasi, `pandas.DataFrame` biasanya lebih cocok daripada membuat satu dictionary manual untuk setiap baris.

## Coba sendiri

Buat dictionary untuk satu zona dengan kunci `"zona"`, `"jarak_meter"`, dan `"kondisi_trotoar"`. Cetak jaraknya. Lalu buat set dari `['Baik', 'Cukup', 'Baik']` dan tampilkan kategori unik yang telah diurutkan.

<details>
<summary>Periksa pembahasan</summary>

```python
zona = {"zona": "A", "jarak_meter": 450, "kondisi_trotoar": "Baik"}
print(zona["jarak_meter"])
print(sorted(set(["Baik", "Cukup", "Baik"])))
```

Keluaran: `450` dan `['Baik', 'Cukup']`.

</details>

Lanjut ke [membaca CSV dengan pandas](../membaca-data/) untuk bekerja dengan banyak baris sekaligus.

## Menelusuri pasangan dictionary

Gunakan `.items()` untuk memproses semua nama bidang dan nilainya:

```python
for nama_bidang, nilai in zona.items():
    print(nama_bidang, "=", nilai)
```

Keluaran:

```text
kode = A
waktu_menit = 8
trotoar = Baik
```

Gunakan `.get(kunci, nilai_bawaan)` saat kunci mungkin belum tersedia. Mengakses langsung dengan tanda kurung siku, seperti `zona["jarak"]`, menimbulkan `KeyError` bila kunci tidak ada; ini membantu menemukan salah eja atau bidang yang belum dicatat.
