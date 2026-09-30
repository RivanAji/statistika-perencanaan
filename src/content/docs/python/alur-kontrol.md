---
title: Kondisi dan keputusan
description: Membuat Python memilih langkah berdasarkan syarat yang jelas.
---

Program sering perlu mengambil keputusan. Misalnya, beri label “lebih dari 15 menit” hanya jika waktu benar-benar melewati batas itu. Dalam Python, kondisi menghasilkan `True` atau `False`; `if` memakai jawaban itu untuk memilih langkah.

## Baca syarat sebagai pertanyaan

```python
waktu = 18
print(waktu > 15)
print(waktu == 15)
```

Keluaran:

```text
True
False
```

`>` bertanya “lebih besar dari?”. `==` bertanya “sama dengan?”. Satu tanda `=` menyimpan nilai; dua tanda `==` membandingkan nilai.

| Tanda | Pertanyaan |
|---|---|
| `>` | lebih besar dari? |
| `<` | lebih kecil dari? |
| `>=` | lebih besar atau sama dengan? |
| `<=` | lebih kecil atau sama dengan? |
| `==` | sama dengan? |
| `!=` | tidak sama dengan? |

## Minta Python memilih

```python
waktu = 18
if waktu > 15:
    print("Lebih dari 15 menit")
else:
    print("Paling lama 15 menit")
```

Keluaran: `Lebih dari 15 menit`.

Bacanya: jika syarat `waktu > 15` benar, jalankan baris yang menjorok di bawah `if`. Jika salah, jalankan baris di bawah `else`. Titik dua `:` membuka cabang. Empat spasi menandai baris yang menjadi bagian cabang.

```text
Apakah waktu > 15?
├── Ya   → cetak "Lebih dari 15 menit"
└── Tidak → cetak "Paling lama 15 menit"
```

## Beberapa pilihan dengan `elif`

```python
waktu = 18
if waktu > 20:
    print("Lebih dari 20 menit")
elif waktu > 10:
    print("Lebih dari 10 menit")
else:
    print("10 menit atau kurang")
```

Keluaran: `Lebih dari 10 menit`. Python memeriksa dari atas. Setelah satu syarat benar, cabang berikutnya dilewati.

Urutan syarat berpengaruh. Jika `waktu > 10` ditulis pertama, nilai 25 juga memenuhi syarat itu dan tidak pernah sampai ke cabang `waktu > 20`.

## Batas kategori harus tepat

Misalkan aturan mengatakan “15 menit atau lebih”. Gunakan `>= 15`, bukan `> 15`.

```python
print(14, 14 >= 15)
print(15, 15 >= 15)
print(16, 16 >= 15)
```

Keluaran:

```text
14 False
15 True
16 True
```

Kata “lebih dari” berarti `>`. Frasa “sekurang-kurangnya”, “atau lebih”, dan “tidak kurang dari” berarti `>=`. Pada analisis data, uji nilai yang tepat pada batas sebelum mengelompokkan seluruh kolom.

## Menggabungkan dua syarat

`and` meminta **semua** syarat benar. `or` meminta **setidaknya satu** syarat benar. `not` membalik benar menjadi salah atau sebaliknya.

```python
moda = "Bus"
waktu = 18
print(moda == "Bus" and waktu > 15)
print(moda == "Bus" or waktu > 20)
print(not waktu > 15)
```

Keluaran: `True`, `True`, `False`.

:::caution[Periksa kata “dan” serta “atau”]
“Bus dan lebih dari 15 menit” memerlukan dua syarat sekaligus. “Bus atau lebih dari 15 menit” juga menerima perjalanan yang memenuhi salah satu syarat saja. Artinya berbeda; tuliskan ulang aturan dengan kata-kata sebelum menerjemahkannya ke kode.
:::

## Coba sendiri

Buat `waktu = 15`. Cetak `"Memenuhi batas"` jika waktu 15 menit atau lebih, dan `"Di bawah batas"` jika tidak. Ulangi dengan 14 dan 16.

<details>
<summary>Periksa pembahasan</summary>

```python
waktu = 15
if waktu >= 15:
    print("Memenuhi batas")
else:
    print("Di bawah batas")
```

Untuk 14 hasilnya `Di bawah batas`. Untuk 15 dan 16 hasilnya `Memenuhi batas`.

</details>

Lanjut ke [perulangan](../perulangan/) untuk menerapkan syarat pada banyak nilai.
