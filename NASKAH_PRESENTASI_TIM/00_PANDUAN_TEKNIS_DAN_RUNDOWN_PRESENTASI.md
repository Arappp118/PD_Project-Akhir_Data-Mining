# PANDUAN TEKNIS REKAMAN VIDEO PRESENTASI, RUNDOWN WAKTU & QA/QC AKHIR
**Mata Kuliah:** Penambangan Data (Data Mining) – Semester Ganjil 2026/2027  
**Program Studi:** Teknik Informatika, Universitas Maritim Raja Ali Haji (UMRAH)  
**Judul Riset:** *Pengelompokkan Wilayah Dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering Pada Disdukcapil Kabupaten Natuna*  
**NIM Ketua / Folder Submisi:** 2401020121 / PD-NTN25-FINAL  

---

## 1. PERNYATAAN HASIL AUDIT KELAYAKAN AKHIR (FINAL QA & QC STATEMENT)

Berdasarkan audit komprehensif terhadap 6 tahapan siklus hidup data mining CRISP-DM pada proyek ini:

1. **Relevansi Regulasi & Masalah Nyata (100% RELEVAN):**
   * Masalah keterlambatan pencatatan akta kelahiran diuji langsung berdasarkan batas yuridis 60 hari kalender sesuai amanat **UU No. 24 Tahun 2013 tentang Administrasi Kependudukan**.
   * Karakteristik wilayah 3T maritim (tertinggal, terdepan, terluar) Kepulauan Natuna dipetakan secara objektif.

2. **Integritas Data & Zero Fabrication (100% VALID & DAPAT DIPERTANGGUNGJAWABKAN):**
   * Berbasis **131 folder berkas fisik loket asli** (Formulir F-2.01, Surat Keterangan Lahir dari RSUD/Puskesmas/Bidan, dan SPTJM Kebenaran Data Kelahiran).
   * Seluruh penanganan data kosong dilakukan melalui pencocokan silang faktual (cross-referencing) dan penamaan transparan `Tanpa Keterangan (Template RSUD)` tanpa rekayasa angka sintetis.

3. **Perlindungan Data Pribadi / PII (100% BEBAS BOCORAN / ZERO LEAK):**
   * Seluruh NIK (16 digit), No KK (16 digit), Nama Lengkap warga/saksi/anak/orang tua, dan Alamat jalan/RT/RW telah disamarkan dengan pseudonim terstruktur sesuai **UU No. 27 Tahun 2022 tentang Perlindungan Data Pribadi (UU PDP)**.
   * Berkas terbuka maupun arsip `.7z` ([Mentah_2401020121.7z](file:///home/wh4mi/Dokumen/S5/jumat/data_mining/projek/DISDUKCAPIL_NTN/PD-NTN25-FINAL/BERKAS_UNGGAH_GOOGLE_FORM/Mentah_2401020121.7z) & [SiapMining_2401020121.7z](file:///home/wh4mi/Dokumen/S5/jumat/data_mining/projek/DISDUKCAPIL_NTN/PD-NTN25-FINAL/BERKAS_UNGGAH_GOOGLE_FORM/SiapMining_2401020121.7z)) telah lolos uji audit regex 16-digit.

4. **Kualitas Metrik Algoritma K-Means (100% MEMENUHI SYARAT EVALUASI AKADEMIK):**
   * **Model 1 (Spasial 16 Kecamatan):** Silhouette Score = **0.6377 / 0.6410** (Struktur Kuat / *Strong Cluster Structure*), Davies-Bouldin Index = **0.4710** (Separasi antar-klaster sangat tajam).
   * **Model 2 (Sosio-Ekonomi Individu 131 Berkas):** Silhouette Score = **0.5533**, Davies-Bouldin Index = **0.6128** (Klaster terpisah secara wajar dan representatif).

5. **Kesiapan Artefak & Deployment (100% LAYAK PRESENTASI & UJIAN):**
   * Dashboard interaktif berbasis Leaflet & Plotly ([dashboard_interaktif_kmeans_dosen.html](file:///home/wh4mi/Dokumen/S5/jumat/data_mining/projek/DISDUKCAPIL_NTN/PD-NTN25-FINAL/06_DEPLOYMENT/dashboard_interaktif_kmeans_dosen.html)) menggunakan basemap Esri profesional, bebas dari kebutuhan API Key, bebas tanda air (watermark), dan responsif.
   * Laporan resmi dalam format PDF standar nasional ([FinPD_2401020121.pdf](file:///home/wh4mi/Dokumen/S5/jumat/data_mining/projek/DISDUKCAPIL_NTN/PD-NTN25-FINAL/BERKAS_UNGGAH_GOOGLE_FORM/FinPD_2401020121.pdf)) dan naskah Word lengkap.

> **KESIMPULAN AUDITOR:**  
> Proyek **PD-NTN25-FINAL** dinyatakan **SANGAT LAYAK, VALID, DAN SIAP DIPRESENTASIKAN** untuk rekaman video YouTube maupun sidang pengujian akademik di hadapan dosen pengampu.

---

## 2. RUNDOWN DAN SUSUNAN PEMBAGIAN WAKTU PRESENTASI (TOTAL 18–20 MENIT)

| No | Pembicara | NIM | Peran Tim | Segmen Waktu | Topik Bahasan Utama |
| :---: | :--- | :---: | :--- | :---: | :--- |
| 1 | **Ridho Ramadani E** | 2401020121 | Ketua Tim | 00:00 – 03:30 (3.5 Menit) | Pembuka, Latar Belakang Geografis 3T Natuna, Regulasi UU 24/2013 & UU PDP 27/2022, Profil Disdukcapil Natuna |
| 2 | **Salma Nursafira** | 2401020094 | Anggota | 03:30 – 06:45 (3.2 Menit) | Data Understanding: Digitalisasi 131 Berkas Fisik (F-2.01 & SKL/SPTJM), Kamus Data, Skala Pengukuran |
| 3 | **Monalisa Dwi Cantika** | 2401020100 | Anggota | 06:45 – 10:30 (3.7 Menit) | Exploratory Data Analysis (EDA): 8 Grafik Analitis, Deteksi Distribusi Bimodal, Disparitas Daratan vs Pulau |
| 4 | **Sarah Fauziyyah** | 2401020109 | Anggota | 10:30 – 14:00 (3.5 Menit) | Data Preparation: Protokol Zero Fabrication, Koreksi Typo Kronologis, Sinkronisasi 2025, Penyamaran PII |
| 5 | **Muhammad Agus Farhan**| 2401020111 | Anggota | 14:00 – 17:30 (3.5 Menit) | Modeling K-Means (Spasial & Sosio-Ekonomi), Evaluasi Silhouette (0.641 & 0.553), Live Demo Dashboard Leaflet |
| 6 | **Ridho Ramadani E** | 2401020121 | Ketua Tim | 17:30 – 19:30 (2.0 Menit) | Rekomendasi Kebijakan (Kapal Pelayanan Keliling / Mobile Service Boat), Lesson Learned & Penutup Resmi |

---

## 3. CHECKLIST SETUP TEKNIS SEBELUM REKAMAN VIDEO

1. **Aplikasi Perekam:** Gunakan OBS Studio, Bandicam, atau Zoom Recording dengan resolusi minimal Full HD 1080p (1920x1080) pada 30/60 fps.
2. **Audio:** Gunakan headset/mikrofon clip-on agar suara jernih, bebas noise, dan bervolume seimbang antar anggota tim.
3. **Persiapan Jendela Layar yang Dibuka:**
   * **Jendela 1 (Browser Google Chrome):** Buka file dashboard interaktif `06_DEPLOYMENT/dashboard_interaktif_kmeans_dosen.html`.
   * **Jendela 2 (PDF Viewer / Adobe Acrobat):** Buka dokumen laporan resmi `07_LAPORAN_AKHIR_DAN_PROPOSAL/FinPD_2401020121.pdf`.
   * **Jendela 3 (VS Code Editor):** Buka folder workspace `PD-NTN25-FINAL` dengan tab skrip Python yang siap ditunjukkan per anggota.
   * **Jendela 4 (File Manager / Explorer):** Tunjukkan folder `02_DATA_UNDERSTANDING/01_formulir_dan_arsip_fisik_131` dan `BERKAS_UNGGAH_GOOGLE_FORM`.
4. **Format Video YouTube Saat Diunggah:**
   * Judul Video: `Final Project – Pengelompokkan Wilayah Dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering Pada Disdukcapil Kabupaten Natuna`
   * Deskripsi Video: Cantumkan identitas lengkap 5 anggota tim beserta *timestamp* segmentasi waktu (sesuai panduan).
