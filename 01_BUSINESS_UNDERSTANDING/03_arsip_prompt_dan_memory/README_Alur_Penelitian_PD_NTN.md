# README — Alur Penelitian Data Mining PD_NTN

**Judul:** Pengelompokkan Wilayah dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering pada Disdukcapil Kabupaten Natuna

Dokumen ini menjadi panduan kerja setelah dokumen sumber (foto/scan/formulir fisik) ditranskripsikan ke Excel/CSV. Ikuti urutan, jangan melompati audit dan validasi.

## 1. Istilah dan posisi data

- **Data mentah sumber:** foto, scan, atau dokumen fisik `Formulir_Pelaporan` dan `Surat_Keterangan`.
- **Data hasil transkripsi/digitisasi:** isi dokumen diketik ke Excel/CSV. Ini belum otomatis disebut data clean; kesalahan ketik, format, duplikasi, nilai tidak konsisten, dan missing value masih mungkin ada.
- **Data hasil audit/transkripsi tervalidasi:** data digital yang dibandingkan dengan dokumen sumber, kesalahan transkripsi diperiksa/diperbaiki, format diseragamkan, dan perubahan dicatat.
- **Data clean:** data yang telah melewati pemeriksaan kualitas dan cleaning yang terdokumentasi. Clean tidak berarti semua kolom harus terisi; missing yang memang tidak tersedia/ tidak relevan harus tetap dibedakan.
- **Dataset terintegrasi:** data dari dua sumber digabung berdasarkan kunci yang sah (misalnya `ID_Data`), dengan hasil join dan unmatched records diperiksa.
- **Dataset analisis/feature-engineered:** dataset setelah variabel penelitian dan fitur turunan dibuat.
- **Dataset modeling:** hanya fitur yang dipakai K-Means, setelah encoding dan scaling yang sesuai.

> Catatan: nama file `Data_Bersih_Akta_Kelahiran_Lengkap_Imputed.xlsx` mengandung kata *Imputed*. Jangan menganggap seluruh nilai di dalamnya sebagai data asli atau hasil cleaning biasa. Audit asal imputasi: kolom mana, nilai mana, metode, alasan, dan apakah imputasi dilakukan sebelum/selama penelitian. Simpan nilai asli dan nilai hasil imputasi secara terpisah serta beri penanda.

## 2. Alur besar penelitian

```text
FOTO / SCAN / DOKUMEN FISIK
(Formulir_Pelaporan + Surat_Keterangan)
                 |
                 v
TRANSKRIPSI / DIGITISASI
Excel/CSV — data yang diketik, belum otomatis clean
                 |
                 v
AUDIT TRANSKRIPSI
Bandingkan dengan dokumen asli, cek salah ketik,
tanggal, angka, ID, dan kelengkapan
                 |
                 v
DATA HASIL TRANSKRIPSI TERVALIDASI
Simpan koreksi dan bukti audit; jangan timpa raw
                 |
                 v
DATA QUALITY & CLEANING
Cek duplikat, missing, format, rentang, konsistensi,
nilai tidak wajar, dan keseragaman kategori
                 |
                 v
DATA CLEAN / DATA TERVALIDASI
                 |
                 v
DATA UNDERSTANDING (CRISP-DM)
Profil data, statistik deskriptif, distribusi,
pola missing, dan pemahaman variabel
                 |
                 v
DATA INTEGRATION
Join Formulir_Pelaporan + Surat_Keterangan
berdasarkan ID_Data; cek matched/unmatched
                 |
                 v
FEATURE SELECTION + FEATURE ENGINEERING
Tentukan fitur relevan; buat usia ayah/ibu saat anak lahir,
durasi pelaporan (hari), dan fitur lain jika beralasan
                 |
                 v
ANALISIS DATA SIAP MODELING
Cek unit analisis, missing, outlier, variasi, dan kecukupan
                 |
                 v
ENCODING + SCALING
Encoding kategori secara tepat; scaling numerik
sesuai kebutuhan K-Means
                 |
                 v
DATASET MODELING
Fitur final, tanpa ID/nama/NIK/KK sebagai fitur model
                 |
                 v
MODELING K-MEANS
Eksperimen beberapa K, seed/parameter dicatat
                 |
                 v
EVALUASI
Elbow/inertia, Silhouette, Davies-Bouldin,
stabilitas, interpretabilitas, dan keterbatasan
                 |
                 v
INTERPRETASI + VISUALISASI
Jelaskan profil cluster, bukan klaim sebab-akibat
                 |
                 v
LAPORAN + PRESENTASI + LOG KONTRIBUSI
                 |
                 v
FINALISASI DAN ARSIP
```

## 3. Langkah yang harus dilakukan berikutnya

### Tahap A — Bekukan dan lindungi data sumber
1. Simpan foto/scan/dokumen sumber di folder raw yang aksesnya terbatas.
2. Simpan workbook hasil transkripsi sebagai versi terpisah.
3. Jangan mengedit data mentah sumber atau menimpa transkripsi awal.
4. Catat nama file, tanggal penerimaan, jumlah dokumen, dan cakupan sumber.

### Tahap B — Audit transkripsi (prioritas pertama)
1. Buat daftar ID dokumen dan cocokkan dengan baris Excel.
2. Periksa ulang nilai yang rawan salah: tanggal, NIK/nomor, berat/panjang, nama wilayah, pekerjaan, dan nomor surat.
3. Catat koreksi: ID, sheet, kolom, nilai sebelumnya, nilai koreksi, alasan, dan bukti sumber.
4. Bedakan `kosong di dokumen`, `tidak relevan`, `tidak terbaca`, `belum ditranskripsi`, dan `missing akibat kesalahan`.
5. Jangan menebak nilai yang tidak terbaca.

**Output:** data transkripsi tervalidasi + `LOG_AUDIT_TRANSKRIPSI.md` + tabel koreksi.

### Tahap C — Data quality dan cleaning
Lakukan pemeriksaan:
- ID kosong/duplikat dan keunikan kunci.
- Jumlah baris, kolom, serta baris kosong.
- Format tanggal dan waktu.
- Nilai di luar rentang yang masuk akal.
- Konsistensi penulisan kecamatan/desa/jenis kelamin/pekerjaan.
- Missing value per kolom dan alasan missing.
- Nilai yang berbeda antara dua sumber untuk informasi yang sama.
- Nilai hasil imputasi dan asalnya.

Jangan menghapus semua baris yang memiliki missing. Tentukan penanganan berdasarkan makna kolom, tujuan analisis, dan bukti.

**Output:** dataset clean/tervalidasi, laporan data quality, dan log cleaning.

### Tahap D — Data Understanding
- Buat data dictionary: nama kolom, definisi, sumber, tipe, satuan, dan peran.
- Hitung statistik deskriptif dan distribusi.
- Analisis missingness dan variasi.
- Identifikasi kolom identitas, administratif, kandidat fitur, dan kolom yang tidak relevan.
- Periksa apakah unit analisis adalah anak/kasus atau agregat wilayah. Jangan mencampur unit tanpa rancangan yang jelas.

**Output:** `DATA_DICTIONARY.xlsx`, tabel profil data, grafik, dan laporan Data Understanding.

### Tahap E — Integrasi dua sheet
- Tentukan kunci join (`ID_Data`) dan validasi keunikannya.
- Hitung jumlah ID yang match, hanya ada di Formululir, dan hanya ada di Surat_Keterangan.
- Cek konflik kolom yang sama (misalnya tanggal lahir, nama, atau wilayah).
- Tentukan sumber utama setiap variabel berdasarkan dokumen dan definisi.
- Jangan menggabungkan secara membabi buta atau menghapus unmatched records tanpa alasan.

**Output:** dataset terintegrasi dan `LOG_DATA_INTEGRATION.md`.

### Tahap F — Feature Selection dan Feature Engineering
- **Feature selection:** memilih kolom yang sudah ada dan relevan untuk analisis.
- **Feature engineering:** membentuk fitur baru dari data yang ada.
- Kandidat yang pernah dibahas: usia ayah saat anak lahir, usia ibu saat anak lahir, durasi pelaporan (tanggal pelaporan − tanggal lahir anak dalam hari), serta pekerjaan ayah/ibu sebagai kategori/proksi karakteristik sosial.
- Usia orang tua dihitung pada tanggal lahir anak, bukan tanggal pelaporan.
- Durasi harus valid dan tidak negatif; periksa tanggal dan kasus khusus.
- Pekerjaan bukan pendapatan aktual; jangan menyimpulkan kekayaan/kemiskinan.
- Jangan menetapkan fitur final sebelum meninjau kualitas, variasi, missing, relevansi, dan risiko bias.

**Output:** dataset feature-engineered, tabel fitur (definisi/rumus/sumber), dan log.

### Tahap G — Menyiapkan dataset modeling
- Tentukan fitur final dan unit analisis.
- ID, nama, NIK, KK, dan informasi identitas langsung tidak menjadi fitur K-Means.
- Tangani missing dengan metode yang beralasan dan terdokumentasi.
- Kategorikal: pilih encoding yang sesuai; jangan ordinal-encode kategori nominal secara sembarang.
- Numerik: evaluasi scaling karena K-Means berbasis jarak.
- One-hot encoding dapat memperbesar dimensi dan memengaruhi jarak; jelaskan dampaknya.
- Jika data campuran kategori-numerik, dokumentasikan keterbatasan Euclidean/K-Means.
- Simpan pipeline preprocessing agar dapat direproduksi.

**Output:** dataset modeling, pipeline/script, daftar fitur final, dan log.

### Tahap H — Modeling dan evaluasi
- K-Means sesuai ketentuan mata kuliah; jangan menganggap K=3 sudah pasti.
- Uji beberapa nilai K dan catat parameter/random seed.
- Evaluasi menggunakan inertia/Elbow, Silhouette, Davies-Bouldin, stabilitas, dan interpretabilitas.
- Jelaskan bahwa cluster menunjukkan kemiripan, bukan sebab-akibat.
- Jangan menggeneralisasi sampel loket menjadi seluruh wilayah tanpa dukungan desain data.
- Jika unit analisis individu, hasil cluster individu tidak otomatis sama dengan cluster kecamatan.

**Output:** kode Python, model/label cluster, tabel metrik, grafik, interpretasi, dan log.

### Tahap I — Dokumentasi, laporan, dan presentasi
Setiap pekerjaan menghasilkan:
- file output di folder yang sesuai;
- log aktivitas (input, proses, output, validasi, status);
- penjelasan kode Python (input–proses–output, walkthrough, dan cara menjelaskan);
- update `PROJECT_STATUS.md` dan `CHANGELOG.md` bila relevan.

Saat final, siapkan laporan `.docx` dan `.pdf`, PowerPoint `.pptx`, log kontribusi tim berdasarkan bukti, serta arsip output yang tervalidasi.

## 4. Struktur folder kerja yang disarankan

```text
PD_NTN/
├── 00_PROJECT_MANAGEMENT/
│   ├── README.md
│   ├── PROJECT_STATUS.md
│   ├── DECISION_LOG.md
│   ├── CHANGELOG.md
│   └── CONTRIBUTION_LOG.md
├── 01_DATA_RAW/
│   ├── documents_original/       # foto/scan; akses terbatas
│   └── transcription_original/   # salinan transkripsi awal
├── 02_DATA_AUDIT/
│   ├── audit_transcription/
│   ├── data_quality/
│   └── audit_logs/
├── 03_DATA_PREPARATION/
│   ├── data_clean/
│   ├── data_integration/
│   ├── feature_selection/
│   ├── feature_engineering/
│   ├── encoding_scaling/
│   └── preparation_logs/
├── 04_DATA_UNDERSTANDING/
│   ├── descriptive_analysis/
│   ├── visualizations/
│   └── analysis_logs/
├── 05_MODELING/
│   ├── code/
│   ├── experiments/
│   ├── model_outputs/
│   └── modeling_logs/
├── 06_EVALUATION/
│   ├── metrics/
│   ├── cluster_interpretation/
│   └── evaluation_logs/
├── 07_VISUALIZATION/
├── 08_RESEARCH_REPORT/
│   ├── draft/
│   ├── review/
│   └── final/
├── 09_PRESENTATION/
│   ├── draft/
│   ├── final/
│   ├── presentation_notes/
│   └── contribution_log/
├── 10_FINAL_DELIVERABLES/
│   ├── DOCX/
│   ├── PDF/
│   └── PPTX/
└── 11_ARCHIVE/
```

Sesuaikan dengan folder yang telah ada. Jangan membuat duplikasi folder atau memindahkan file tanpa pemeriksaan.

## 5. Log minimum setiap output

Setiap output harus mencatat:
- tanggal;
- tahapan;
- tujuan;
- input;
- proses/metode;
- output dan lokasi;
- validasi;
- status (DRAFT/REVIEW/VALIDATED/FINAL);
- kendala dan tindak lanjut.

Untuk Python, tambahkan: script/notebook, library/versi, parameter, input-output trace, penjelasan kode, dan catatan presentasi.

## 6. Privasi dan keamanan
- Jangan memasukkan NIK, No. KK, nama lengkap, alamat detail, atau identitas sensitif ke dataset modeling, grafik, log, maupun presentasi.
- Gunakan ID anonim.
- File dokumen sumber tetap terbatas dan tidak ikut dibagikan publik.
- Pastikan output yang dibagikan telah diperiksa dari kebocoran identitas.

## 7. Status awal dan keputusan
README ini adalah **rencana alur**, bukan bukti bahwa semua tahap sudah dilakukan.

Status awal yang disarankan:
- Transkripsi: perlu audit terhadap dokumen sumber.
- Data clean: belum dinyatakan final sebelum audit dan cleaning terdokumentasi.
- Imputasi: perlu audit asal/metode/kolom yang diimputasi.
- Integrasi: perlu validasi join dan konflik sumber.
- Feature selection/engineering: perlu keputusan final berbasis kualitas dan relevansi.
- Modeling: belum dilakukan sampai dataset modeling tervalidasi.
- Evaluasi dan laporan final: menunggu hasil yang benar-benar terverifikasi.

## 8. Checklist langkah terdekat
- [ ] Lindungi dan bekukan data sumber serta transkripsi awal.
- [ ] Audit provenance file yang berlabel `Imputed`.
- [ ] Audit transkripsi baris demi baris terhadap dokumen.
- [ ] Buat log koreksi.
- [ ] Jalankan data quality checks.
- [ ] Tetapkan definisi missing value.
- [ ] Buat data dictionary.
- [ ] Validasi integrasi dua sheet.
- [ ] Lakukan Data Understanding.
- [ ] Tentukan unit analisis dan fitur kandidat.
- [ ] Dokumentasikan Feature Selection dan Feature Engineering.
- [ ] Siapkan dataset modeling.
- [ ] Baru lanjut K-Means, evaluasi, interpretasi, dan luaran final.

**Prinsip:** jangan melompat ke K-Means sebelum data, unit analisis, fitur, dan preprocessing dapat dipertanggungjawabkan.
