import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

const repository = process.env.GITHUB_REPOSITORY;
const [owner, name] = repository?.split('/') ?? [];
const onPages = Boolean(process.env.GITHUB_ACTIONS && owner && name);

export default defineConfig({
  site: onPages ? `https://${owner}.github.io` : 'http://localhost:4321',
  base: onPages ? `/${name}` : '/',
  devToolbar: { enabled: false },
  integrations: [
    starlight({
      title: 'Statistika Perencanaan',
      description: 'Modul terbuka statistika dan analisis data dengan Python.',
      customCss: ['./src/styles/course.css'],
      locales: { root: { label: 'Bahasa Indonesia', lang: 'id' } },
      sidebar: [
        { label: 'Sebelum mulai', items: [{ label: 'Pendahuluan', link: '/pendahuluan/' }, { label: 'Unduh data', link: '/unduh-data/' }, { label: 'Glosarium', link: '/glosarium/' }, { label: 'Referensi', link: '/rujukan/' }] },
        { label: 'Dasar pengenalan Python', items: [{ label: 'Python dan Google Colab', link: '/python/colab/' }, { label: 'Sintaks dan variabel', link: '/python/dasar/' }, { label: 'Tipe data, teks, dan list', link: '/python/tipe-koleksi/' }, { label: 'Kondisi dan keputusan', link: '/python/alur-kontrol/' }, { label: 'Perulangan', link: '/python/perulangan/' }, { label: 'Fungsi dan modul', link: '/python/fungsi-modul/' }, { label: 'Membaca galat', link: '/python/galat-debugging/' }, { label: 'Tuple, set, dan dictionary', link: '/python/koleksi-lanjutan/' }, { label: 'Membaca CSV dengan pandas', link: '/python/membaca-data/' }, { label: 'Dasar NumPy', link: '/python/numpy-dasar/' }, { label: 'Visualisasi sederhana', link: '/python/visualisasi/' }, { label: 'Lembar ringkas Python', link: '/python/lembar-ringkas/' }, { label: 'Uji pemahaman Python', link: '/python/cek-pemahaman/' }] },
        { label: 'Memahami data', items: [{ label: 'Konsep data statistik', link: '/materi/konsep-data/' }, { label: 'Pengumpulan data', link: '/materi/pengumpulan-data/' }, { label: 'Menilai mutu data', link: '/materi/kualitas-data/' }, { label: 'Pencilan dan noise', link: '/materi/pencilan-noise/' }, { label: 'Uji pemahaman data', link: '/materi/cek-pemahaman-data/' }] },
        { label: 'Statistik deskriptif', items: [{ label: 'Ukuran pemusatan', link: '/materi/deskriptif-pusat/' }, { label: 'Ukuran penyebaran', link: '/materi/deskriptif-sebaran/' }, { label: 'Visualisasi data dengan Matplotlib', link: '/materi/visualisasi-deskriptif/' }, { label: 'Uji praktik deskriptif', link: '/materi/cek-deskriptif/' }] },
        { label: 'Probabilitas', items: [{ label: 'Konsep dasar probabilitas', link: '/materi/probabilitas-dasar/' }, { label: 'Peluang bersyarat dan independensi', link: '/materi/peluang-bersyarat-independensi/' }, { label: 'Menghitung peluang bertahap', link: '/materi/peluang-bertahap/' }, { label: 'Distribusi probabilitas', link: '/materi/distribusi-probabilitas/' }, { label: 'Peluang melalui simulasi', link: '/materi/simulasi-peluang/' }] },
        { label: 'Praktik mandiri', items: [{ label: 'Akses taman', link: '/latihan/akses-taman/' }] }
      ]
    })
  ]
});
