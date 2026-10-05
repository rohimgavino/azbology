# Optimasi gambar lokal — baseline 6e15209

## Scope dan sumber kebenaran
Clone authoritative `D:/azbology3-repo`, remote `rohimgavino/azbology`, main, GitHub Pages. Export `D:/azbology3` tidak disentuh. Tidak commit/push/deploy. Produk, klaim dan kontak tidak diubah.

`assets/` tetap menyimpan sumber asli. `assets/optimized/` berisi 86 derivative dari 37 sumber WebP, serta manifest SHA-256/dimensi/bytes. Tidak ada crop baru atau upscale. Pillow 12.3.0 / libwebp 1.6.0, quality 90, method 6, LANCZOS, lebar kandidat 320/640/960/1280 dan lebar asli (dibatasi sumber). Logo PNG/OG tetap asli.

38 background photo menjadi native img absolut dalam wrapper existing: geometry, border, overlay, background-position → object-position, dan contain 78% dipertahankan. Ada srcset/sizes, width/height, decoding async; hanya hero eager/high priority. Hero sizes memperhitungkan cover pada viewport portrait (179vh) agar tidak memilih gambar terlalu kecil. Lazy native tetap mempunyai fallback tanpa JavaScript (browser memuat eager saat JS disabled).

Perbaikan mobile yang diminta: basis 42% header Blend tidak diwariskan ke layout column (`flex-basis:auto` <=900); burger margin-left auto dan basis 44px <=980. Tidak mengubah teks CTA.

## Reproduksi
Jalankan dari root clone dengan Python 3.14 dan Chrome terpasang:

```sh
python -m venv C:/Users/PC/AppData/Local/hermes/cache/scratch/azbo-images-venv
C:/Users/PC/AppData/Local/hermes/cache/scratch/azbo-images-venv/Scripts/python.exe -m pip install -r requirements-images.txt
C:/Users/PC/AppData/Local/hermes/cache/scratch/azbo-images-venv/Scripts/python.exe scripts/build_images.py
C:/Users/PC/AppData/Local/hermes/cache/scratch/azbo-images-venv/Scripts/python.exe -m unittest discover -s tests -v
C:/Users/PC/AppData/Local/hermes/cache/scratch/azbo-images-venv/Scripts/python.exe tests/browser_images.py
C:/Users/PC/AppData/Local/hermes/cache/scratch/azbo-images-venv/Scripts/python.exe tests/browser_layout.py
git diff --check
```

Generator hanya menulis derivatives/manifest, tidak HTML atau source. Hash byte encoder bergantung versi libwebp; manifest mencatat versinya. Tes browser menyajikan baseline melalui `git show 6e15209:index.html`, menggunakan local HTTP server ephemeral dan cold browser context DPR1. Report/screenshot ke Hermes cache scratch `azbo-image-audit` (override `AZBO_REPORT_DIR`), bukan source publik.

## Hasil aktual
Browser Chromium Chrome: 375/768/1280, JS on/off, baseline/current = 12 run. Seluruh 44 img current decode, geometry 38 wrapper sama baseline, tidak overflow horizontal, tidak ada pageerror/tautan PDF/download. Tes layout/menu pada 320/360/375/390/414/520/768/900/901/1280 lulus: Quote bawah kartu minus padding 28px, burger kanan container, menu inert tertutup, buka, Escape/focus kembali. Unit 3 lulus; 86 source hash tetap, dimensi/rasio valid, tidak upscale, derivative lebih kecil. Maksimum channel RMS terhadap sumber resize/composite putih 6.492/255 (<12 gate). Inline JS node --check lulus. Foto/produk/crop tidak diganti; penilaian visual akhir tetap oleh pemilik.

Bytes berikut adalah encodedBodySize resource gambar lokal nyata, bukan Lighthouse, termasuk logo/icon tetapi bukan font/HTML/header/TLS/OG yang tidak dimuat halaman:

| viewport | sebelum awal JS | sesudah awal JS | hemat awal | sebelum semua | sesudah semua | hemat semua |
|---|---:|---:|---:|---:|---:|---:|
|375|4,985,838|806,472|83.82%|5,693,680|2,451,752|56.94%|
|768|4,985,838|933,694|81.27%|5,693,680|3,252,696|42.87%|
|1280|4,985,838|884,060|82.27%|5,693,680|3,180,132|44.15%|

Awal diukur setelah navigation +700ms; lazy threshold browser bisa berubah. Semua diukur setelah scroll seluruh foto dan menunggu decode. JS off memuat semua eager: bytes sama kolom semua. DPR2/3 dan ukuran viewport lain dapat memilih derivative lebih besar. Tidak mengklaim Web Vitals atau skor Lighthouse.

## Publikasi dan keterbatasan
`_config.yml` mengecualikan scripts/tests/docs, dokumen perencanaan/SOP, PDF sumber, JPEG sumber dan manifest dari Jekyll Pages. Source tetap di Git. Konfigurasi ini hanya berlaku bila Pages memakai Jekyll/build-from-branch; parent wajib memeriksa pipeline sebelum publikasi. Jika custom workflow menyalin root mentah, whitelist artifact hanya index.html, assets publik, CNAME, robots/sitemap (bukan dokumen/source PDF). Exclusion bukan kontrol akses untuk repository publik atau URL PDF yang telah terpublikasi sebelumnya.

Tidak memindahkan/menghapus source maupun export; penataan bersifat additive dan documented. Asset tidak terpakai dan OG/logo belum dioptimasi. Source+derivative menambah ukuran repo meskipun network halaman berkurang. Tidak ada build/deploy Jekyll atau verifikasi live dalam scope ini. Parent review diff, kualitas/crop di DPR tinggi, dan artifact exclusions sebelum release.
