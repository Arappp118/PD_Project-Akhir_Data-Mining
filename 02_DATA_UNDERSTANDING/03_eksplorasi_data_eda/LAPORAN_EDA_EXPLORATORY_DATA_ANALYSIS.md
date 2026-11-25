# LAPORAN ANALISIS EKSPLORASI DATA (EXPLORATORY DATA ANALYSIS - EDA)
**Proyek Riset Data Mining Disdukcapil Kabupaten Natuna (PD-NTN25-FINAL)**  
*Metodologi CRISP-DM: Tahap Data Understanding (Pemahaman Data) & Data Preparation (Penyiapan Data)*

---

## 1. Ringkasan Eksekutif EDA
Tahap Exploratory Data Analysis (EDA) dilakukan secara komprehensif terhadap **131 berkas fisik permohonan pendaftaran akta kelahiran resmi** Disdukcapil Kabupaten Natuna yang diselaraskan secara konsisten pada **Tahun Pelaporan 2025**.

EDA ini berorientasi pada pencarian pola substantif, pendeteksian anomali transkripsi (*human clerical error*), audit integritas data kosong (*missing values*), pengujian batas yuridis kepatuhan **UU No. 24 Tahun 2013** ($\le 60\text{ hari}$), serta verifikasi disparitas sosio-demografis dan geospasial kepulauan terluar (3T).

---

## 2. Audit dan Rincian 8 Visualisasi EDA (300 DPI)

### Gambar 1: `eda_masalah_kualitas_data_missing_values.png`
- **Tujuan Analisis**: Mengaudit rasio kekosongan atribut penting sebelum dan sesudah tahapan pembersihan berbasis *cross-referencing* antara Formulir Pelaporan (F-2.01) dan Surat Keterangan Lahir Medis.
- **Hasil Kuantitatif**:
  - Kolom *Kecamatan* dan *Desa/Kelurahan*: Mengalami kekosongan awal sebesar **80.1%** pada formulir mentah akibat pemohon hanya menuliskan kode wilayah atau nama pulau. Melalui imputasi silang dengan Surat Keterangan Medis dan penelusuran kodifikasi Kemendagri, tingkat kekosongan turun menjadi **0.0% (Lengkap)**.
  - Kolom *Pekerjaan Orang Tua*: Awalnya kosong **58.0%** karena template RSUD tidak mencantumkan pekerjaan; dilabeli secara ilmiah menjadi `'Tanpa Keterangan (Template RSUD)'` tanpa rekayasa sintetik.
  - Kolom *Nomor Surat Medis*: Mengalami missing **32.8%** karena pemohon dewasa/lansia menggunakan mekanisme **SPTJM Kebenaran Data Kelahiran**.
- **Relevansi Penyajian**: Membuktikan integritas dan transparansi audit data sesuai prinsip *Zero Fabrication*.

### Gambar 2: `eda_deteksi_anomali_typo_kronologis.png`
- **Tujuan Analisis**: Memvalidasi akurasi waktu pelaporan dan mendeteksi anomali negatif klerikal.
- **Panel Kiri (Koreksi Typo Negatif)**: 
  - Terdeteksi 2 berkas mentah dengan selisih hari negatif: **F044 (-228 hari)** dan **F0124 (-10 hari)** akibat petugas transkripsi salah mengetikkan tanggal pelaporan mendahului tanggal kelahiran anak.
  - Dikoreksi berdasarkan tanggal stempel dinas menjadi durasi yuridis positif logis ($T_{\text{lapor}} \ge T_{\text{lahir}}$) yaitu F044 (+2 hari) dan F0124 (+4 hari).
- **Panel Kanan (Konsistensi 100% Tahun 2025)**:
  - Verifikasi bahwa seluruh **131 berkas (100.0%)** didaftarkan dalam kurun kalender tahun **2025**, dengan puncak kedatangan berkas pada bulan Januari (56 berkas), Februari (37 berkas), dan Agustus (19 berkas). Tidak ada data tahun 2024 maupun 2026 yang bocor ke dalam kohort analisis.

### Gambar 3: `eda_distribusi_bimodal_keterlambatan.png`
- **Tujuan Analisis**: Mengidentifikasi bentuk kurva sebaran keterlambatan pengurusan akta kelahiran di Kabupaten Natuna.
- **Hasil Kuantitatif & Bentuk Sebaran**:
  - Kurva keterlambatan membentuk **distribusi bimodal ekstrem** (dua puncak terpisah):
    1. **Puncak Pertama (Bayi Baru Lahir / LU)**: 49 berkas (**37.4%**) didaftarkan tepat waktu sesuai batas aman UU No. 24/2013 ($\le 60\text{ hari}$), dengan median 14 hari.
    2. **Puncak Kedua (Pemohon Dewasa & Lansia / SPTJM)**: 82 berkas (**62.6%**) didaftarkan terlambat (LT), di mana banyak di antaranya memiliki durasi keterlambatan $> 5\text{ tahun}$ bahkan mencapai $> 50 - 84\text{ tahun}$ (terlambat historis).
- **Insight Kebijakan**: Mengindikasikan bahwa Disdukcapil Natuna tidak hanya melayani pencatatan kelahiran baru, melainkan juga menanggung beban pemutihan dokumen kependudukan historis generasi tua kepulauan.

### Gambar 4: `eda_sebaran_spasial_pulau_utama_vs_terluar.png`
- **Tujuan Analisis**: Mengukur disparitas permohonan antara Pulau Utama Bunguran dengan kecamatan kepulauan 3T.
- **Hasil Kuantitatif**:
  - **Pulau Utama Bunguran (Ranai & Sekitarnya)**: Mendominasi total permohonan dengan **113 berkas (86.3%)**, dipimpin oleh Bunguran Timur (70 berkas), Bunguran Timur Laut (11 berkas), Bunguran Barat (11 berkas), Bunguran Utara (8 berkas), Bunguran Selatan (6 berkas), Bunguran Batubi (4 berkas), dan Bunguran Tengah (3 berkas).
  - **Kepulauan Terluar 3T**: Mencakup Serasan Timur (5 berkas), Serasan (3 berkas), Subi (3 berkas), Midai (3 berkas), Suak Midai (1 berkas), Pulau Tiga (1 berkas), Pulau Panjang (1 berkas), dan Pulau Laut (1 berkas).
- **Catatan Kodifikasi Wilayah**: Berkas F0115 yang sebelumnya tertulis 'PEMANGKAT' telah diverifikasi secara akurat melalui kode wilayah Kemendagri `2103062001` sebagai bagian resmi dari **Kecamatan Subi**, sehingga seluruh data 100% tepat terpetakan ke dalam 16 kecamatan Kabupaten Natuna.

### Gambar 5: `eda_tren_bulanan_pelaporan_line_chart.png`
- **Tujuan Analisis**: Memetakan dinamika pengajuan Lahir Umum (LU) vs Lahir Terlambat (LT) sepanjang Januari s.d. Desember 2025.
- **Hasil Kuantitatif**:
  - Pengajuan awal tahun (Januari - Februari) didominasi oleh berkas Lahir Terlambat (LT) dengan puncak 54 berkas pada Januari.
  - Pengajuan Lahir Umum (LU tepat waktu) melonjak tajam pada bulan Agustus (18 berkas), yang bertepatan dengan momentum tahun ajaran baru sekolah dan gencarnya program sosialisasi adminduk terpadu.

### Gambar 6: `eda_boxplot_keterlambatan_spasial_outliers.png`
- **Tujuan Analisis**: Mendeteksi nilai pencilan (*outliers*) dan variabilitas durasi antar-kecamatan utama.
- **Hasil Kuantitatif**:
  - Bunguran Timur memiliki sebaran kuartil interkuartil (IQR) yang rapat di rentang 0 - 20 tahun, dengan beberapa pencilan usia 50 - 62 tahun.
  - Kecamatan Bunguran Selatan dan Bunguran Batubi memiliki pencilan ekstrem masing-masing pada keterlambatan **84.8 tahun** (31.057 hari) dan **68.4 tahun**, merefleksikan permohonan akta pertama kali bagi sesepuh / lansia daerah perbatasan.

### Gambar 7: `eda_scatterplot_korelasi_usia_vs_keterlambatan.png`
- **Tujuan Analisis**: Menguji korelasi bivariat antara usia orang tua saat anak dilahirkan terhadap durasi keterlambatan pelaporan pada tingkat pemohon individu.
- **Hasil Kuantitatif**:
  - Orang tua usia muda (20 - 32 tahun) yang baru melahirkan anak memiliki kecenderungan sangat tinggi untuk melapor tepat waktu ($\le 60\text{ hari}$ / titik hijau).
  - Kasus keterlambatan puluhan tahun (titik merah) terkonsentrasi pada pengurusan mandiri oleh subjek akta yang kini telah dewasa, di mana usia orang tua saat mereka lahir berada di rentang normal reproduksi (25 - 38 tahun).

### Gambar 8: `eda_heatmap_matriks_korelasi_fitur.png`
- **Tujuan Analisis**: Menilai keeratan hubungan linier dan monotonik non-parametrik menggunakan koefisien korelasi peringkat Spearman ($r_s$).
- **Hasil Matriks Korelasi**:
  - Hubungan *Durasi Keterlambatan* dengan *Status Lahir Terlambat (LT)* bernilai **+0.76** (korelasi positif sangat kuat, valid secara konseptual).
  - Hubungan *Bulan Pelaporan* dengan *Durasi Keterlambatan* bernilai **-0.43** (korelasi negatif sedang, menunjukkan berkas awal tahun lebih banyak memuat permohonan tertunda historis).
  - Hubungan *Usia Orang Tua* dengan *Durasi Keterlambatan* mendekati netral (**-0.02**), mengindikasikan bahwa keterlambatan akta di Natuna tidak didorong oleh usia biologis orang tua semata, melainkan oleh faktor struktural geografis maritim dan jarak tempuh ke pusat Disdukcapil di Ranai.

---

## 3. Kesimpulan Verifikasi EDA
1. Seluruh 8 file visualisasi PNG tersimpan dengan format penamaan standar CRISP-DM yang jelas, intuitif, dan deskriptif.
2. Resolusi seluruh grafik adalah **300 DPI** dengan tata letak teks berjarak aman, bebas dari tabrakan sumbu (*no label overlap/clipping*).
3. Integritas data terverifikasi **100% konsisten tahun pelaporan 2025 (131 berkas fisik)** dan **100% terpetakan ke dalam 16 kecamatan resmi Kabupaten Natuna**.
