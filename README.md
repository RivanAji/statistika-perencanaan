# Statistik Perencanaan

Modul terbuka berbahasa Indonesia tentang dasar statistik dan analisis data dengan Python.

Penulis: **Rivan Aji Wahyu Dyan Syafitri**, Urban and Regional Planning, ITS, Indonesia.

## Menjalankan situs

Prasyarat: Node.js dan npm yang didukung oleh versi Astro pada `package.json`.

```sh
npm install
npm run dev
```

Buka alamat lokal yang ditampilkan. Pemeriksaan produksi:

```sh
npm run check
npm run build
```

## Isi

- `src/content/docs/`: bab buku. Setiap bab konsep mempunyai contoh kode, keluaran, tafsir, dan latihan dengan pembahasan.
- `public/data/perjalanan_contoh.csv`: delapan baris, dua variabel, untuk contoh terpandu.
- `public/data/akses_taman_latihan.csv`: 12 zona dan empat variabel untuk latihan mandiri.
- `public/notebooks/statistik-perencanaan-python.ipynb`: notebook Colab yang memuat data terpandu dan keluaran kode.
- `src/assets/`: diagram dan hasil grafik dari data simulasi, serta ilustrasi karakter untuk sampul.
- `scripts/build_data.py`, `scripts/build_notebook.py`, `scripts/build_figures.py`, dan `scripts/build_chart_gallery.py`: pembangun ulang berkas praktik dan grafik.

Kedua dataset simulasi; tidak ada klaim survei atau keterwakilan kota. Rujukan buku digunakan untuk merancang penjelasan, tanpa menyalin halaman atau gambar buku.

## Menyiapkan berkas praktik

```sh
python3 scripts/build_data.py
python3 scripts/build_notebook.py
```

Pembangunan ulang notebook memerlukan `pandas`; diagram awal pada `build_figures.py` dibuat dengan pustaka standar Python. Bila angka data berubah, jalankan ulang kode contoh, perbarui keluaran tercetak di halaman, dan periksa ulang seluruh pembahasan. Notebook di `public/notebooks/` menyimpan keluaran eksekusi agar dapat ditinjau sebelum dibuka di Colab.

Galeri grafik baru memakai NumPy, pandas, dan Matplotlib. Untuk membangunnya ulang dalam lingkungan Python terpisah:

```sh
python3 -m pip install -r requirements-figures.txt
python3 scripts/build_chart_gallery.py
```

Setelah mengubah data atau gambar, jalankan `npm run check` dan `npm run build`. Angka keluaran dalam bab perlu diperiksa lagi jika dataset berubah.

## Publikasi

Workflow GitHub Pages tersedia dalam `.github/workflows/deploy.yml`, tetapi belum dipakai untuk menerbitkan situs. Konfigurasi membaca `GITHUB_REPOSITORY` saat berjalan di GitHub Actions dan menyesuaikan awalan alamat repositori. Sebelum publikasi, tentukan nama repositori dan periksa semua tautan pada alamat akhir.
