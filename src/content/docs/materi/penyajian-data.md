---
title: Penyajian data
description: Tabel frekuensi, proporsi, diagram batang, histogram, dan pilihan grafik.
---

Penyajian data membantu pembaca melihat pola sebelum menghitung satu angka ringkasan. Pilih bentuknya dari **jenis variabel** dan **pertanyaan**, bukan dari grafik yang paling mudah dibuat. Materi ini diringkas dan disatukan ke [visualisasi data dengan Matplotlib](../visualisasi-deskriptif/) agar pemilihan grafik, aturan penyajian, dan cara menggambarnya dapat dipelajari dalam satu alur.

## Periksa tabel mentah

Gunakan [CSV contoh](../../unduh-data/) yang berisi delapan perjalanan simulasi. Satu baris adalah satu perjalanan, `moda` berupa kategori, dan `waktu_menit` berupa besaran.

```python
import pandas as pd
data = pd.read_csv("perjalanan_contoh.csv")
print(data.to_string(index=False))
```

Keluaran:

```text
      moda  waktu_menit
       Bus           12
       Bus           18
     Motor           10
     Motor           14
Jalan kaki            8
Jalan kaki           16
    Sepeda           12
    Sepeda           30
```

Tabel mentah menjaga rincian tiap baris. Ringkasan di bawah mempermudah perbandingan, tetapi rincian itu hilang.

## Tabel frekuensi dan proporsi

Untuk `moda`, hitung berapa baris dalam tiap kategori. Proporsi adalah `frekuensi / jumlah baris`.

```python
frekuensi = data["moda"].value_counts()
proporsi = data["moda"].value_counts(normalize=True)
print(frekuensi.to_string())
print(proporsi.to_string())
```

Keluaran: setiap moda muncul `2` kali dan proporsinya `0.25`. Keempat proporsi berjumlah `1.0`. Persentase diperoleh dengan mengalikan proporsi dengan 100. Tidak perlu memakai diagram lingkaran untuk empat bagian yang sama; tabel kecil menyampaikan angkanya lebih tepat.

:::note[Penyebut harus jelas]
Jika ada nilai `moda` yang kosong, `value_counts()` tidak menghitungnya secara bawaan. Sebutkan apakah penyebutnya seluruh baris atau hanya baris yang mempunyai moda. Gunakan `value_counts(dropna=False)` untuk melihat nilai kosong sebagai kategori pemeriksaan.
:::

## Diagram batang untuk kategori

```python
import matplotlib.pyplot as plt

frekuensi.plot.bar(color="#1459b5")
plt.xlabel("Moda")
plt.ylabel("Jumlah perjalanan")
plt.title("Moda pada delapan perjalanan simulasi")
plt.tight_layout()
plt.show()
```

Diagram batang membandingkan jumlah kategori terpisah. Mulai sumbu jumlah dari nol agar panjang batang tidak membesar-besarkan selisih. Urutan kategori nominal dapat diubah untuk memudahkan pembacaan; perubahan urutan tidak mengubah nilainya.

## Histogram untuk angka

```python
data["waktu_menit"].plot.hist(
    bins=[0, 10, 20, 30, 40], color="#76b9ef", edgecolor="white"
)
plt.xlabel("Waktu perjalanan (menit)")
plt.ylabel("Jumlah perjalanan")
plt.title("Sebaran waktu pada data simulasi")
plt.tight_layout()
plt.show()
```

Histogram menggabungkan nilai ke rentang. Dengan batas di atas, Matplotlib menempatkan nilai 10 pada rentang `[10, 20)` dan nilai 30 pada rentang terakhir `[30, 40]`. Jumlah tiap rentang adalah 1, 6, 0, dan 1. Pilihan batas dapat mengubah tampilan pola, terlebih pada delapan baris. Untuk data sekecil ini, tabel terurut atau titik per nilai juga perlu dilihat.

![Diagram batang moda dan histogram waktu yang dihasilkan dari CSV contoh](../../../assets/grafik-moda-waktu.svg)

## Tabel berurutan dan frekuensi kumulatif

Tabel frekuensi mempertahankan nilai yang diamati; histogram menyatukannya ke dalam rentang. Frekuensi kumulatif menjawab “berapa perjalanan yang 20 menit atau kurang?” Untuk data kecil, tabel terurut sering menjadi pemeriksaan terbaik.

~~~python
batas = [0, 10, 20, 30, 40]
frekuensi = [1, 6, 0, 1]
kumulatif = [1, 7, 7, 8]
print("Batas atas:", batas[1:])
print("Frekuensi:", frekuensi)
print("Kumulatif:", kumulatif)
~~~

Keluaran ringkasnya adalah frekuensi 1, 6, 0, 1 dan frekuensi kumulatif 1, 7, 7, 8. Hingga 20 menit, ada 7 dari 8 perjalanan. Rentang harus saling lepas dan mencakup semua nilai; tentukan juga perlakuan untuk nilai yang tepat pada batas.

### Poligon frekuensi

Poligon menghubungkan titik tengah rentang dengan tinggi yang menyatakan frekuensi. Ia membantu membandingkan bentuk beberapa distribusi yang memakai batas sama. Untuk sedikit pengamatan, histogram biasanya lebih mudah ditafsirkan.

~~~python
import matplotlib.pyplot as plt

titik_tengah = [5, 15, 25, 35]
frekuensi = [1, 6, 0, 1]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(titik_tengah, frekuensi, marker="o", color="#1876b8")
ax.set_xlabel("Titik tengah rentang waktu (menit)")
ax.set_ylabel("Frekuensi perjalanan")
ax.set_title("Poligon frekuensi waktu perjalanan")
ax.set_ylim(bottom=0)
fig.tight_layout()
plt.show()
~~~

titik_tengah meletakkan setiap rentang pada posisi tengahnya. marker="o" menampilkan titik yang dihitung; garis membantu mata mengikuti perubahan antartitik. Garis tidak berarti perjalanan dengan waktu di antara dua titik benar-benar tercatat.

### Ogive: grafik kumulatif

Ogive menghubungkan batas rentang dengan jumlah pengamatan sampai batas itu. Ia dapat membantu menjawab berapa banyak nilai berada di bawah suatu batas. Jangan membacanya sebagai rekaman tiap pengamatan.

~~~python
batas = [0, 10, 20, 30, 40]
frekuensi_kumulatif = [0, 1, 7, 7, 8]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(batas, frekuensi_kumulatif, marker="o", color="#1876b8")
ax.set_xlabel("Waktu (menit), batas rentang")
ax.set_ylabel("Jumlah perjalanan sampai batas")
ax.set_title("Frekuensi kumulatif waktu perjalanan")
ax.set_ylim(bottom=0)
fig.tight_layout()
plt.show()
~~~

Angka awal 0 berarti belum ada perjalanan sebelum batas pertama. Pada batas 20 menit, grafik menunjukkan 7 perjalanan. Nilai akhir harus sama dengan jumlah observasi yang masuk rentang.

## Bandingkan dua kategori sekaligus

Jika data memiliki dua variabel kategori, gunakan batang berkelompok atau bertumpuk untuk membandingkan jumlah maupun komposisi. Contoh berikut membagi delapan perjalanan menjadi waktu paling lama 15 menit dan lebih dari 15 menit. Angka setiap sel dapat dilacak kembali ke tabel perjalanan.

~~~python
import matplotlib.pyplot as plt

moda = ["Bus", "Jalan kaki", "Motor", "Sepeda"]
hingga_15 = [1, 1, 2, 1]
lebih_15 = [1, 1, 0, 1]
posisi = range(len(moda))
lebar = 0.38
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar([i - lebar / 2 for i in posisi], hingga_15, lebar, label="≤15 menit", color="#1876b8")
ax.bar([i + lebar / 2 for i in posisi], lebih_15, lebar, label=">15 menit", color="#e4b83f")
ax.set_xticks(list(posisi))
ax.set_xticklabels(moda)
ax.set_ylabel("Jumlah perjalanan")
ax.set_title("Waktu perjalanan menurut moda")
ax.set_ylim(0, 3)
ax.legend()
fig.tight_layout()
plt.show()
~~~

posisi memberi lokasi tetap untuk setiap moda. Setiap kelompok digeser setengah lebar ke kiri atau kanan agar dua batang berdampingan. label memberi nama seri pada legenda; set_xticks menaruh nama moda di bawah kelompok.

Batang berkelompok memudahkan membandingkan jumlah per moda. Batang bertumpuk lebih menonjolkan total dan bagian penyusunnya; diagram 100% bertumpuk menormalkan setiap moda menjadi 100% untuk membandingkan proporsi. Proporsi dari kelompok berisi satu atau dua pengamatan sangat tidak stabil, jadi tampilkan juga jumlahnya.

Dalam keluaran ini, tiap moda berjumlah dua perjalanan. Motor memiliki dua perjalanan sampai 15 menit dan tidak ada perjalanan di atas 15 menit; tiga moda lainnya masing-masing memiliki satu perjalanan pada tiap kelompok. Itu hanya menggambarkan delapan baris simulasi.

Untuk batang bertumpuk, tambahkan deret kedua ke atas tinggi deret pertama dengan argumen bottom:

~~~python
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(moda, hingga_15, label="≤15 menit", color="#1876b8")
ax.bar(moda, lebih_15, bottom=hingga_15, label=">15 menit", color="#e4b83f")
ax.set_ylabel("Jumlah perjalanan")
ax.legend()
plt.show()
~~~

Argumen bottom menentukan tinggi dasar seri kedua untuk tiap moda. Jika ingin batang bertumpuk 100%, hitung proporsi di dalam setiap moda terlebih dahulu; jangan tumpuk frekuensi mentah lalu menyebutnya persentase.

## Diagram lingkaran: pilihan terbatas

Lingkaran menampilkan bagian dari satu total. Gunakan hanya jika kategori sedikit, saling terpisah, mencakup seluruh total, dan pembaca perlu memahami komposisi. Ukuran sektor adalah frekuensi kategori dibagi jumlah seluruh kategori; data negatif dan penyebut tidak jelas tidak sesuai.

~~~python
frekuensi = [5, 4, 3]
kelas_trotoar = ["Baik", "Cukup", "Kurang"]
fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(frekuensi, labels=kelas_trotoar, autopct="%.0f%%", startangle=90)
ax.set_title("Komposisi kelas trotoar pada 12 zona simulasi")
plt.show()
~~~

labels menamai sektor; autopct menulis persentase pada sektor; startangle memutar titik awal. Matplotlib menormalisasi nilai menjadi bagian dari total. Untuk membandingkan kategori dengan presisi, diagram batang lebih akurat daripada sudut atau luas sektor. Lihat [dokumentasi pie Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html).

Hasil acuan untuk 12 zona adalah Baik 5/12 (42%), Cukup 4/12 (33%), dan Kurang 3/12 (25%). Pembulatan menyebabkan persentase yang ditampilkan bisa berjumlah 100% atau sedikit berbeda pada data lain.

## Pilih bentuk dari jenis pertanyaannya

| Bentuk data dan pertanyaan | Pilihan awal | Pertimbangan |
|---|---|---|
| Satu kategori: berapa banyak per kelompok? | Tabel frekuensi atau batang | Tampilkan kategori kosong bila penting; urutkan dengan alasan yang jelas. |
| Satu kategori: bagaimana bagian dari total? | Lingkaran untuk sedikit kategori; batang 100% bertumpuk untuk perbandingan kelompok | Bagian harus saling lepas dan membentuk satu keseluruhan. |
| Satu angka: nilai apa yang muncul dan berapa kali? | Tabel terurut atau diagram titik | Terbaik untuk data kecil karena nilai mentah tetap terlihat. |
| Satu angka: bagaimana bentuk sebarannya? | Histogram atau boxplot | Histogram sensitif pada batas rentang; boxplot menyembunyikan rincian. |
| Satu angka berkelompok: sampai batas mana nilai terkumpul? | Ogive | Menunjukkan kumulatif, bukan rincian per individu. |
| Perbandingan frekuensi beberapa rentang | Poligon frekuensi | Kelompokkan dengan batas yang sama. |
| Kategori berubah sepanjang waktu | Diagram garis | Hanya jika urutan waktu bermakna. |
| Dua variabel numerik pada unit yang sama | Diagram pencar | Tiap titik adalah satu unit; hubungan bukan bukti sebab-akibat. |
| Angka dibandingkan antar kategori | Titik atau boxplot per kelompok | Sertakan jumlah tiap kelompok dan distribusi datanya. |

Gunakan batang horizontal untuk label panjang; hindari garis untuk kategori nominal; mulai batang jumlah dari nol; jangan memilih batas histogram hanya untuk menonjolkan pola; jangan memakai efek 3D untuk mempercantik perbedaan. Judul harus menyatakan isi, cakupan, dan waktu data.

## Bentuk lain dan batasnya

| Pertanyaan | Bentuk yang masuk akal | Hal yang diperiksa |
|---|---|---|
| Berapa banyak tiap kategori? | Tabel frekuensi atau diagram batang | Penyebut dan kategori kosong |
| Bagaimana sebaran satu angka? | Tabel terurut, titik, histogram, boxplot | Satuan dan pilihan interval |
| Bagaimana nilai berubah menurut waktu? | Grafik garis | Urutan waktu benar dan jeda data |
| Apakah dua angka berhubungan? | Diagram pencar | Satuan, pencilan, serta faktor lain |

Diagram garis tidak cocok untuk empat moda karena Bus, Motor, Jalan kaki, dan Sepeda tidak membentuk sumbu waktu. Diagram pencar memerlukan dua variabel numerik; dataset terpandu ini hanya memiliki satu.

## Mini test

1. Mengapa diagram batang lebih cocok untuk `moda` dan histogram lebih cocok untuk `waktu_menit`?
2. Jika satu perjalanan tidak mencatat moda, apa yang perlu dijelaskan sebelum menyebut “25% menggunakan Bus”?
3. Ubah batas histogram menjadi `[0, 15, 25, 35]`. Bandingkan bentuknya tanpa mengubah datanya.

<details><summary>Periksa pembahasan</summary>

`moda` memiliki kategori terpisah, sedangkan `waktu_menit` berupa besaran yang dapat dikelompokkan ke rentang. Jika satu moda kosong, tentukan apakah proporsi Bus memakai penyebut delapan perjalanan atau tujuh perjalanan dengan moda tercatat. Histogram berubah karena pengelompokan berubah, meski delapan waktu aslinya tetap sama.

</details>

Lanjut ke [ukuran pemusatan](../deskriptif-pusat/).
