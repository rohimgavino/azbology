# SOP Pengembangan & Pengelolaan Website AZBOLOGY

Status: pedoman kerja awal berdasarkan audit lokal dan pemeriksaan azbology.id; bukan pernyataan bahwa semua perbaikan telah diterapkan.

## 1. Tujuan dan ruang lingkup

Pertahankan identitas visual yang disukai pemilik sambil meningkatkan kejelasan katalog, aksesibilitas, performa, dan permintaan sampel/penawaran. Website saat ini merupakan company profile dan katalog kopi berbahasa Inggris dalam satu halaman statis.

Dokumen ini mencakup pengembangan kode, konten produk, pengujian dan publikasi. Tidak memberikan izin otomatis untuk mengubah desain, menghubungkan akun, membeli layanan, atau menerbitkan perubahan.

## 2. Prinsip desain yang wajib dijaga

- Pertahankan palet hijau, cream, sage dan kraft, tipografi Barlow/Barlow Condensed, ilustrasi/foto kopi, urutan narasi, serta karakter company profile.
- Jangan mengganti layout keseluruhan, framework, logo, font, atau gaya brand tanpa persetujuan pemilik.
- Perbaikan kontras boleh mengubah nilai warna secukupnya agar terbaca, tanpa mengganti identitas palet.
- Tambahkan CTA yang menyatu dengan tombol, radius, spacing dan tipografi existing.
- Website harus tetap nyaman di mobile. Uji pada lebar 375, 768 dan 1280 px, tanpa horizontal overflow.
- Foto tidak boleh diganti dengan representasi produk/asal yang menyesatkan. Pastikan izin penggunaan aset.

## 3. Kondisi teknis dan sumber kebenaran

- Entry point: `index.html`; CSS dan JavaScript masih inline.
- Foto/logo: `assets/`; katalog PDF: `Katalog English AZBO-2026.pdf`.
- Domain: `https://azbology.id/`.
- Repository yang ditemukan: `https://github.com/rohimgavino/azbology`.
- Folder kerja yang diaudit tidak mempunyai metadata `.git`. Jangan menjalankan `git init`, menimpa folder dengan clone, atau menganggapnya otomatis sinkron dengan repository.
- Sebelum perubahan kode: verifikasi repository, branch sumber deployment, hosting, dan kesamaan file lokal/remote/live. Catat commit dan jalur kerja yang digunakan.
- Bila kode, dokumen dan produksi berbeda, laporkan perbedaannya. Website live merupakan bukti perilaku produksi; repository merupakan riwayat kode, bukan bukti deploy sukses.

## 4. Alur perubahan kode

1. Baca dokumen proyek, inventaris file, dan kode terkait. Catat perubahan lokal yang sudah ada; jangan membuang pekerjaan pemilik.
2. Tentukan satu kebutuhan, scope file, risiko, dan kriteria penerimaan.
3. Simpan backup/checkpoint di luar direktori aset publik. Jangan memasukkan credential atau data pelanggan ke Git.
4. Untuk bug/fungsi baru, buat regresi yang gagal dahulu; implementasikan perubahan minimal dan buktikan tes lulus.
5. Tinjau diff untuk secret, tautan rusak, perubahan desain tak sengaja, klaim tanpa bukti dan kesalahan kontak.
6. Jalankan checklist pengujian pada bagian 8. Dokumen-only tidak memerlukan perubahan HTML atau deployment.
7. Mintakan persetujuan sesuai scope. Commit hanya file yang relevan; gunakan pesan conventional commit.
8. Push ke repository yang sudah terverifikasi. Setelah deploy, baca kembali URL target dan periksa hasilnya, bukan hanya status pipeline.
9. Catat perubahan, hasil tes, commit, versi deploy, dan pekerjaan yang belum selesai.

## 5. SOP informasi produk dan klaim

Pemilik/sales menyediakan data; editor menyusun; reviewer memeriksa; pemilik menyetujui publikasi. Satu orang boleh menjalankan lebih dari satu peran, tetapi bukti persetujuan tetap dicatat.

Untuk setiap SKU/lot, kumpulkan hanya data yang tersedia dan dapat dibuktikan:
- Nama, origin, jenis kopi, proses, bentuk Green Beans/Roasted Beans/Ground Coffee.
- Varietas, crop year, altitude, grade/screen size, moisture, defect, cupping dan tanggal uji jika memang tercatat.
- Untuk roasted: roast profile, pilihan grind, tanggal roasting atau kebijakan kesegaran yang benar.
- Kemasan, MOQ, stok/kapasitas, lead time, sample policy, pembayaran dan pengiriman.
- Basis quotation, mata uang dan Incoterms bila relevan dan benar-benar ditawarkan.

Jangan mengarang angka, harga, legal entity, buyer, sertifikat, histori ekspor atau kapasitas. Harga publik tidak wajib: gunakan request quotation dengan scope produk yang jelas.

Pisahkan komitmen halal/thayyib atau Fair Trade Ethics dari sertifikasi resmi. Klaim certified memerlukan nomor, penerbit, ruang lingkup dan status yang diverifikasi. Klaim speciality, kesehatan atau dampak keberlanjutan memerlukan bukti yang sesuai; lunakkan atau hapus jika tidak dapat dibuktikan. Fakta industri harus diberi sumber dan tahun.

Gunakan English yang konsisten: Green Beans, Anaerobic Process, Fully Washed, Arabica. Tandai produk upcoming sebagai belum tersedia, bukan dapat dipesan.

## 6. SOP inquiry dan kontak

- Konfirmasi nomor lengkap dengan pemilik sebelum memperbaiki telepon; jangan menebak nomor yang bertopeng.
- Nomor WhatsApp dalam kode audit: `62816652714`; ini referensi kode, bukan verifikasi kepemilikan/keaktifan.
- CTA yang disarankan: Request Samples, Request Wholesale Quote, Download Catalogue.
- Pesan inquiry mencantumkan produk/bentuk biji, jumlah yang diinginkan dan negara tujuan. Jangan membuat permintaan palsu ke nomor/email produksi saat tes.
- Form tidak wajib; WhatsApp/email boleh menjadi jalur utama bila langkahnya jelas.
- Jika ada form: minimalkan data, validasi server-side, batasi spam, sediakan status sukses/gagal dan privacy notice sesuai pemrosesan yang nyata.
- Sales menetapkan PIC, jam layanan, target waktu respons dan metode pencatatan inquiry; jangan menjanjikan SLA sebelum disetujui.
- Tambahkan identitas badan usaha, alamat dengan Indonesia, email domain dan informasi ekspor hanya setelah dikonfirmasi.

## 7. SOP SEO dan aset

- Title/H1 menjelaskan supplier/origin/produk yang benar-benar dijual; jangan keyword stuffing atau menjamin ranking.
- Canonical harus cocok URL produksi. Metadata sosial harus memakai gambar yang dapat diakses.
- Sitemap hanya berisi URL publik yang benar; robots.txt tidak boleh memblokir halaman pemasaran tanpa alasan yang disetujui.
- Structured data mencerminkan konten terlihat; jangan membuat review/rating/harga/sertifikasi palsu.
- Halaman produk terpisah dibuat jika punya informasi substantif; hindari duplikasi tipis.
- Buat varian foto mobile dan lazy load foto bawah fold; hero tidak dilazy load. Pertahankan kualitas produk dan dimensi/aspect ratio.
- Beri ukuran pada image untuk mengurangi pergeseran layout. Ukur hasil nyata, jangan mengklaim skor Lighthouse tanpa menjalankannya.
- PDF katalog diberi tautan, format/ukuran, dan versi. Optimalkan tanpa mengorbankan legibilitas; bagian raster perlu OCR/lapisan teks bila memungkinkan.
- Analytics hanya setelah kebutuhan dan privacy disepakati; ukur inquiry/download, bukan hanya pageview.

## 8. Checklist penerimaan sebelum publikasi

- [ ] Semua local asset dan anchor punya target; tidak ada gambar/tautan internal rusak.
- [ ] JavaScript lulus syntax check; tidak ada error console pada flow yang diuji.
- [ ] Teks utama terlihat ketika JavaScript mati atau IntersectionObserver tidak tersedia.
- [ ] Menu mobile tertutup tidak menerima fokus; Escape menutup dan fokus kembali ke tombol menu.
- [ ] Keyboard, fokus terlihat, alt/accessibility label, reduced motion dan kontras diperiksa.
- [ ] Teks normal minimal kontras 4.5:1; teks besar minimal 3:1.
- [ ] Layout 375/768/1280 px dan CTA telah diuji tanpa mengirim inquiry produksi.
- [ ] Kontak, produk, MOQ/lead time dan klaim yang berubah disetujui pemilik.
- [ ] PDF dapat diunduh dan sesuai versi; ekstensi download cocok format file.
- [ ] Metadata, canonical, sitemap dan structured data valid bila diubah.
- [ ] Tidak ada secret, backup, source internal sensitif atau data inquiry yang dipublikasikan.
- [ ] Deploy dibaca kembali dari domain; URL target/status/isi tercatat.

## 9. Backlog berdasarkan audit, bukan fitur yang sudah selesai

P1: verifikasi Git/deployment; nomor telepon; CTA inquiry produk/hero; link katalog; fallback reveal tanpa JavaScript; konfirmasi data B2B dan bukti klaim.

P2: menu keyboard/kontras; responsive images dan PDF; SEO teknis dan positioning; identitas sales.

P3: halaman produk, bilingual bila dibutuhkan pasar, serta tracking konversi dengan aturan privacy.

Audit menemukan referensi aset/anchor lokal valid dan JS syntax valid. Di produksi, robots.txt/sitemap.xml 404, structured data belum ada, dan tombol tel masih bertopeng. Pada sampel viewport 375 px tidak ditemukan horizontal overflow. Temuan ini baseline, bukan sertifikasi seluruh website.

## 10. Rollback dan pemeliharaan

Jika release merusak kontak, visibilitas konten, aksesibilitas atau inquiry: hentikan perubahan lanjutan, identifikasi commit/deploy, rollback menggunakan mekanisme hosting yang sudah diverifikasi, lalu uji domain kembali. Jangan force-push atau menghapus data tanpa izin.

Periksa kontak, link katalog dan produk saat data berubah; setelah setiap release periksa domain, console dan CTA. Revisi SOP bila workflow nyata berubah. Dokumen internal tidak perlu ditampilkan sebagai konten marketing atau dipublikasikan melalui hosting.
