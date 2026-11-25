# PROYEK PENAMBANGAN DATA (DATA MINING) DISDUKCAPIL KABUPATEN NATUNA
**Repository: PD-NTN25-FINAL**  
**Tahun Akademik: Semester Ganjil 2026/2027**

## PENGELOMPOKKAN WILAYAH DAN ANALISIS KETERLAMBATAN PENCATATAN AKTA KELAHIRAN MENGGUNAKAN ALGORITMA K-MEANS CLUSTERING PADA DISDUKCAPIL KABUPATEN NATUNA

### Tim Peneliti (Kelompok Mahasiswa):
1. **Ridho Ramadani E** – NIM: **2401020121** (Ketua Tim)
2. **Salma Nursafira** – NIM: **2401020094** (Anggota)
3. **Monalisa Dwi Cantika** – NIM: **2401020100** (Anggota)
4. **Sarah Fauziyyah** – NIM: **2401020109** (Anggota)
5. **Muhammad Agus Farhan** – NIM: **2401020111** (Anggota)

**Instansi Mitra:**  
Dinas Kependudukan dan Pencatatan Sipil (Disdukcapil) Kabupaten Natuna  
*Narasumber Administrator Layanan:* **Ibu Julida, S.Sos**

---

## Struktur Direktori Standar CRISP-DM (Cross-Industry Standard Process for Data Mining)

```text
PD-NTN25-FINAL/
│
├── 01_BUSINESS_UNDERSTANDING/             [FASE 1: PEMAHAMAN BISNIS & REGULASI]
│   ├── 01_rps_dan_panduan/                -> RTM Penambangan Data, Panduan Unggah, & Arsip Acuan Proyek
│   ├── 02_jurnal_referensi/               -> Jurnal-jurnal acuan K-Means Kependudukan
│   ├── 03_arsip_prompt_dan_memory/        -> Master Research Memory V4, V5, V6 & Panduan Alur
│   └── PropPD_2401020121.pdf              -> Dokumen Proposal Resmi (Status: Lolos)
│
├── 02_DATA_UNDERSTANDING/                 [FASE 2: AUDIT, TRANSKRIPSI & EXPLORATORY DATA ANALYSIS]
│   ├── 01_arsip_scan_mentah/              -> 131 folder fisik pindaian formulir F-2.01 & SKL/SPTJM
│   ├── 02_tabulasi_transkripsi/           -> Master tabulasi Excel/CSV 131 entri & ekstraksi digital JSON/CSV
│   │   ├── Data_Mentah_Transkripsi_Akta_Kelahiran_2025.xlsx -> Master Data Mentah Digital 131 Berkas
│   │   ├── Data_Mentah_Transkripsi_Formulir_Pelaporan_2025.csv -> CSV Formulir Pelaporan (Windows Ready)
│   │   ├── Data_Mentah_Transkripsi_Surat_Keterangan_2025.csv   -> CSV Surat Keterangan Lahir (Windows Ready)
│   │   └── data_ekstraksi_json_csv/
│   │       ├── formulir_pelaporan.json               -> Transkripsi 131 Formulir F-2.01
│   │       ├── surat_keterangan.json                 -> Transkripsi 131 Surat Keterangan Lahir (SKL)
│   │       ├── data_gabungan_transkripsi_final.json  -> Versi full/final gabungan terpadu 131 berkas
│   │       ├── formulir_pelaporan_2025.csv           -> Tabel CSV Formulir Pelaporan
│   │       └── surat_keterangan_2025.csv             -> Tabel CSV Surat Keterangan Lahir
│   └── 03_eksplorasi_data_eda/            -> 8 Grafik Visualisasi EDA 300 DPI
│       ├── analisis_eksplorasi_data_dan_kualitas_eda.py
│       └── LAPORAN_EDA_EXPLORATORY_DATA_ANALYSIS.md
│
├── 03_DATA_PREPARATION/                  [FASE 3: PERSIAPAN DATA, PEMBERSIHAN & REKAYASA FITUR]
│   ├── 01_pembersihan_data/               -> Validasi kronologis kohort 2025, perbaikan typo slip, imputasi faktual
│   │   ├── Data_Bersih_Akta_Kelahiran_Lengkap_Imputed.xlsx
│   │   ├── Data_Bersih_Akta_Kelahiran_Lengkap_Imputed.csv
│   │   ├── Data_Bersih_Akta_Kelahiran_Surat_Keterangan_Imputed.csv
│   │   └── pembersihan_data_dan_validasi_kronologis.py
│   └── 02_rekayasa_fitur/                 -> Rekayasa durasi hari kontinu & anonimisasi PII (UU PDP No. 27/2022)
│       ├── Dataset_Feature_Engineered_PD_NTN.xlsx (131 baris siap mining individu)
│       ├── Dataset_Feature_Engineered_PD_NTN.csv  (Versi CSV siap buka di Windows)
│       ├── Dataset_Agregasi_Spasial_16_Kecamatan.xlsx (16 baris agregasi spasial)
│       ├── Dataset_Agregasi_Spasial_16_Kecamatan.csv  (Versi CSV siap buka di Windows)
│       └── rekayasa_fitur_dan_reduksi_dimensi.py
│
├── 04_MODELING/                           [FASE 4: PEMODELAN K-MEANS CLUSTERING]
│   ├── 01_kmeans_spasial_wilayah/         -> Model 1: K-Means Spasial 16 Kecamatan (Menjawab Reviewer)
│   │   ├── Hasil_Clustering_Kecamatan_Natuna.xlsx
│   │   ├── Hasil_Clustering_Kecamatan_Natuna.csv
│   │   ├── Hasil_Clustering_Kecamatan_Natuna_Centroid.csv
│   │   ├── Hasil_Clustering_Kecamatan_Natuna_Evaluasi.csv
│   │   └── kmeans_model_spasial_wilayah.py
│   └── 02_kmeans_sosioekonomi_individu/   -> Model 2: K-Means Sosio-Ekonomi Individu 131 Berkas
│       ├── Hasil_Clustering_Sosial_Ekonomi.xlsx
│       ├── Hasil_Clustering_Sosial_Ekonomi.csv
│       ├── Hasil_Clustering_Sosial_Ekonomi_Centroid.csv
│       ├── pemodelan_kmeans_sosioekonomi_dan_dashboard.py
│       └── scatter_model_sosioekonomi_individu.png
│
├── 05_EVALUATION/                         [FASE 5: EVALUASI VALIDITAS & METRIK MODEL]
│   ├── evaluasi_elbow_silhouette.png      -> Grafik Evaluasi K=2..6 (Silhouette Spasial = 0.6410, Sosio-Ekonomi = 0.5533)
│   └── QA_QC_VERIFICATION_VALIDATION_REPORT.md -> Laporan Audit Kualitas, DBI & Uji Konsistensi
│
├── 06_DEPLOYMENT/                         [FASE 6: PENYEBARAN, DASHBOARD DIGITAL & PETA]
│   ├── dashboard_interaktif_kmeans_dosen.html -> Dashboard Interaktif Leaflet (Esri Street Map, Satelit, Topografi Bebas Watermark/API Key) & Plotly
│   ├── generate_dashboard.py              -> Skrip kompilasi dashboard
│   ├── peta_geospatial_klaster_natuna.png -> Peta spasial resolusi tinggi 300 DPI
│   ├── scatter_model_sosioekonomi_individu.png -> Grafik Model Sosio-Ekonomi Individu 300 DPI (Centroid ⭐ & Elips)
│   └── visualisasi_cluster_kecamatan.png  -> Grafik klaster spasial 300 DPI
│
├── 07_LAPORAN_AKHIR_DAN_PROPOSAL/         [DOKUMEN AKADEMIK RESMI SESUAI RTM]
│   ├── FinPD_2401020121.pdf               -> Naskah Laporan Akhir Resmi 33 Halaman (Format RTM BAB I-VI, Margin 4-3-3-3 cm)
│   ├── LAPORAN_AKHIR_PENAMBANGAN_DATA_PD_NTN25.docx -> Naskah Microsoft Word TNR 12pt, 1.5 Spasi
│   ├── LAPORAN_AKHIR_PENAMBANGAN_DATA_PD_NTN25.md   -> Naskah Markdown lengkap
│   ├── PropPD_2401020121.pdf              -> Dokumen Proposal Awal
│   └── build_final_reports.py             -> Generator otomatis naskah Word & PDF
│
├── 08_DIAGRAM_ALUR_DAN_ARSITEKTUR/         [ARSIP 6 DIAGRAM ALUR & ARSITEKTUR SISTEM]
│   ├── 01_diagram_alur_metodologi_crisp_dm.png / .svg / .dot / .mmd
│   ├── 02_diagram_alur_pipeline_otomasi_data_mining.png / .svg / .dot / .mmd
│   ├── 03_diagram_alur_struktur_laporan_akhir_rtm.png / .svg / .dot / .mmd
│   ├── 04_diagram_alur_pemenuhan_standar_luaran_proyek.png / .svg / .dot / .mmd
│   ├── 05_diagram_alur_matematis_algoritma_kmeans.png / .svg / .dot / .mmd
│   ├── 06_diagram_alur_penjaminan_kualitas_data_zero_fabrication.png / .svg / .dot / .mmd
│   ├── generate_diagrams.py               -> Skrip otomatis perender 6 diagram alur (300 DPI)
│   └── README.md                          -> Katalog penjelasan detil setiap diagram
│
├── BERKAS_UNGGAH_GOOGLE_FORM/             [BERKAS FINAL SIAP UNGGAH DEADLINE 20 NOV 2026]
│   ├── FinPD_2401020121.pdf               -> [Berkas 3/3] Laporan Akhir PDF Resmi
│   ├── Mentah_2401020121.7z               -> [Berkas 1/3] Data mentah terdigitalisasi tersamarkan privasi (UU PDP)
│   ├── SiapMining_2401020121.7z           -> [Berkas 2/3] Seluruh dataset bersih, fitur, model & visualisasi (XLSX & CSV)
│   ├── Data_Mentah_Terdigitalisasi_Privacy_Disamarkan.xlsx
│   ├── Data_Mentah_Terdigitalisasi_Privacy_Disamarkan_Formulir_Pelaporan.csv
│   ├── Data_Mentah_Terdigitalisasi_Privacy_Disamarkan_Surat_Keterangan.csv
│   ├── PANDUAN_PRESENTASI_YOUTUBE_DAN_GITHUB.md -> Panduan video 10-15 menit & perintah push GitHub
│   └── paketkan_berkas_google_form.py     -> Skrip pemaketan arsip .7z otomatis
│
├── NASKAH_PRESENTASI_TIM/                 [NASKAH BACAAN REKAMAN PRESENTASI VIDEO YOUTUBE & SIDANG]
│   ├── 00_PANDUAN_TEKNIS_DAN_RUNDOWN_PRESENTASI.md -> Rundown waktu per menit & checklist rekaman
│   ├── 01_NASKAH_RIDHO_RAMADANI_E_KETUA.md         -> Naskah Pembuka, Kebijakan, & Penutup (Ridho - 2401020121)
│   ├── 02_NASKAH_SALMA_NURSAFIRA.md               -> Naskah Data Understanding & Kamus Data (Salma - 2401020094)
│   ├── 03_NASKAH_MONALISA_DWI_CANTIKA.md          -> Naskah 8 Grafik Visualisasi EDA (Monalisa - 2401020100)
│   ├── 04_NASKAH_SARAH_FAUZIYYAH.md               -> Naskah Data Preprocessing & UU PDP (Sarah - 2401020109)
│   ├── 05_NASKAH_MUHAMMAD_AGUS_FARHAN.md          -> Naskah K-Means & Demo Dashboard (Farhan - 2401020111)
│   └── MASTER_NASKAH_LENGKAP_SATU_DOKUMEN.md      -> Naskah utuh gabungan untuk teleprompter
│
├── jalankan_seluruh_tahapan_pipeline.py   -> Master Pipeline 1-Klik untuk menguji seluruh tahapan
└── README.md                              -> Dokumentasi Induk Proyek (Panduan Navigasi CRISP-DM)
```

## Eksekusi Cepat Pipeline
Untuk menjalankan seluruh tahapan dari awal hingga akhir dalam satu perintah:
```bash
python3 jalankan_seluruh_tahapan_pipeline.py
```
