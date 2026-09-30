---
title: Glosarium
description: Istilah Python dan statistika yang digunakan dalam modul.
---

## Data dan rancangan

- **Observasi:** satu catatan dalam tabel, sesuai unit yang didefinisikan.
- **Unit analisis:** hal yang diwakili satu baris, misalnya perjalanan atau zona-tahun.
- **Variabel:** ciri yang dicatat pada setiap unit; biasanya menjadi kolom.
- **Nilai:** isi satu sel untuk suatu variabel dan unit.
- **Populasi:** seluruh unit yang menjadi sasaran pertanyaan, lengkap dengan batas tempat dan waktu.
- **Sampel:** sebagian unit yang dipilih dari populasi melalui suatu prosedur.
- **Kerangka sampel:** daftar atau mekanisme yang memungkinkan unit populasi dipilih.
- **Bias:** penyimpangan sistematis yang dapat berasal dari pemilihan atau pengukuran.
- **Akurasi:** kedekatan pengukuran dengan besaran yang sebenarnya.
- **Presisi:** kedekatan antarhasil pengukuran berulang.
- **Nilai hilang:** nilai yang tidak tersedia; alasan ketiadaannya perlu dicatat dan tidak sama dengan nol.
- **Duplikat:** catatan yang tampak berulang; statusnya perlu diperiksa terhadap definisi unit dan pengenal.
- **Noise:** variasi pengukuran atau gangguan yang tidak mewakili sinyal yang sedang diteliti.
- **Pencilan:** nilai yang jauh dari sebagian besar nilai lain menurut aturan yang dinyatakan; belum tentu salah.

## Skala dan ringkasan

- **Nominal:** kategori tanpa urutan alami, seperti moda.
- **Ordinal:** kategori berurutan dengan jarak antarkategori yang belum tentu sama.
- **Interval:** besaran dengan selisih bermakna tetapi nol tidak berarti ketiadaan, seperti suhu Celsius.
- **Rasio:** besaran dengan nol bermakna, seperti durasi dan jarak.
- **Frekuensi:** banyak observasi dalam suatu kategori atau rentang.
- **Mean / rata-rata:** jumlah nilai dibagi banyak nilai yang dihitung.
- **Median:** nilai tengah setelah pengurutan.
- **Modus:** nilai atau kategori yang paling sering muncul; dapat lebih dari satu.
- **IQR:** kuartil ketiga dikurangi kuartil pertama; lebar separuh tengah data.
- **Simpangan baku:** ukuran sebaran dengan satuan yang sama seperti variabel asal.
- **Varians:** rata-rata kuadrat selisih nilai dari mean, memakai pembagi yang sesuai untuk sampel atau populasi.
- **Jangkauan:** nilai terbesar dikurangi nilai terkecil.
- **Kuartil:** batas yang membagi data terurut menjadi empat bagian menurut aturan perhitungan tertentu.
- **Median absolute deviation:** median jarak absolut nilai dari median data; definisinya perlu dibedakan dari mean absolute deviation.
- **Mean terpangkas:** mean setelah proporsi yang sama dari kedua ujung data terurut dikeluarkan hanya untuk ringkasan tersebut.

## Probabilitas

- **Ruang sampel:** seluruh hasil yang mungkin menurut suatu percobaan.
- **Kejadian:** bagian dari ruang sampel yang memenuhi suatu syarat.
- **Peluang empiris:** frekuensi relatif kejadian dalam pengamatan.
- **Peluang bersyarat:** peluang suatu kejadian setelah ruang acuan dibatasi oleh kejadian lain.
- **Irisan:** hasil yang memenuhi dua kejadian sekaligus.
- **Gabungan:** hasil yang memenuhi setidaknya satu dari dua kejadian.
- **Independen:** mengetahui satu kejadian tidak mengubah peluang kejadian lain.
- **Saling lepas:** dua kejadian tidak dapat terjadi bersamaan dalam satu percobaan.
- **PMF:** fungsi yang memberi peluang tepat pada suatu nilai diskrit.
- **PDF:** fungsi kepadatan untuk variabel kontinu; peluang rentang diperoleh dari luas di bawah kurva.
- **CDF:** fungsi yang memberi peluang nilai paling banyak sama dengan batas tertentu.
- **Distribusi:** cara nilai atau peluang tersebar di antara hasil yang mungkin.
- **Distribusi sampling:** sebaran suatu statistik dari pengambilan sampel berulang menurut rancangan yang sama.

## Python

- **Variabel Python:** nama yang merujuk ke sebuah nilai dalam program.
- **List:** kumpulan nilai berurutan yang dapat diubah.
- **Tuple:** kumpulan nilai berurutan yang tidak dapat diubah langsung.
- **Set:** kumpulan anggota unik tanpa urutan yang dapat diandalkan.
- **Dictionary:** pasangan kunci dan nilai.
- **Fungsi:** blok kode bernama yang menerima masukan dan dapat mengembalikan hasil.
- **CSV:** berkas teks untuk tabel; kolom umumnya dipisahkan koma.
- **DataFrame:** tabel baris dan kolom dalam pustaka pandas.
- **`NaN` / `<NA>`:** penanda nilai hilang yang dapat dijumpai di pandas.
