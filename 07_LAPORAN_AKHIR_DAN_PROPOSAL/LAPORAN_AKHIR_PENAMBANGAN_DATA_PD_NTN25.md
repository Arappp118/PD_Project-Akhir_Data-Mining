# LAPORAN AKHIR PROJECT PENAMBANGAN DATA

## PENGELOMPOKKAN WILAYAH DAN ANALISIS KETERLAMBATAN PENCATATAN AKTA KELAHIRAN MENGGUNAKAN ALGORITMA K-MEANS CLUSTERING PADA DISDUKCAPIL KABUPATEN NATUNA

**Disusun Oleh Tim Peneliti Mahasiswa:**
1. **Ridho Ramadani E** – NIM: **2401020121** (Ketua Tim)
2. **Salma Nursafira** – NIM: **2401020094** (Anggota)
3. **Monalisa Dwi Cantika** – NIM: **2401020100** (Anggota)
4. **Sarah Fauziyyah** – NIM: **2401020109** (Anggota)
5. **Muhammad Agus Farhan** – NIM: **2401020111** (Anggota)

**Program Studi Teknik Informatika**  
**Fakultas Teknik dan Teknologi Kemaritiman**  
**Universitas Maritim Raja Ali Haji**  
**Tanjungpinang, 2026**

---

---

### KATA PENGANTAR

Puji dan syukur ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan hidayah-Nya, sehingga Tim Peneliti dapat menyelesaikan penyusunan Laporan Akhir Proyek Penambangan Data dengan judul **"Pengelompokkan Wilayah dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering pada Disdukcapil Kabupaten Natuna"** dengan baik, tepat waktu, dan memenuhi seluruh kaidah akademik resmi.

Laporan akhir ini disusun sebagai syarat kelulusan dan pemenuhan luaran mata kuliah Penambangan Data pada Program Studi Teknik Informatika, Fakultas Teknik dan Teknologi Kemaritiman, Universitas Maritim Raja Ali Haji (UMRAH) Tanjungpinang. Penelitian ini dirancang untuk memecahkan problematika nyata disparitas pelayanan administrasi kependudukan di wilayah kepulauan perbatasan terluar Indonesia, khususnya dalam mendeteksi klaster kecamatan yang mengalami keterlambatan pencatatan akta kelahiran.

Dalam pelaksanaan penelitian dan penyusunan laporan akhir ini, Tim Peneliti memperoleh bimbingan, arahan, serta dukungan berharga dari berbagai pihak. Oleh karena itu, rasa hormat dan terima kasih yang tulus kami haturkan kepada:
1. **Rektor Universitas Maritim Raja Ali Haji dan Dekan Fakultas Teknik dan Teknologi Kemaritiman UMRAH** atas fasilitas akademik dan iklim riset yang kondusif.
2. **Bapak/Ibu Dosen Pengampu Mata Kuliah Penambangan Data** atas dedikasi transfer keilmuan, bimbingan metodologi CRISP-DM, serta arahan pemodelan data mining di kelas.
3. **Bapak/Ibu Dosen Reviewer Proposal** atas masukan konstruktif yang sangat berharga dalam memperkuat analisis spasial geospasial 16 kecamatan di Kabupaten Natuna.
4. **Kepala Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna beserta Ibu Julida, S.Sos** (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk) atas izin penelitian, penyediaan 131 arsip pindaian resmi, serta koordinasi faktual di lapangan.
5. **Seluruh rekan mahasiswa Program Studi Teknik Informatika angkatan 2024** yang saling memberikan semangat dan kolaborasi konstruktif.

Tim Peneliti menyadari sepenuhnya bahwa laporan ini masih memiliki keterbatasan. Kritik dan saran yang membangun senantiasa diharapkan guna penyempurnaan karya ilmiah berikutnya. Semoga laporan ini memberikan sumbangsih nyata bagi efektivitas kebijakan Disdukcapil Natuna dan kemajuan teknologi kemaritiman di Kepulauan Riau.

*Tanjungpinang, November 2026*  
**Tim Peneliti Mahasiswa**

---

### RINGKASAN EKSEKUTIF / ABSTRAK

Pencatatan akta kelahiran merupakan dokumen otentik wajib yang melindungi hak sipil dan kewarganegaraan setiap penduduk Indonesia. Berdasarkan Undang-Undang Nomor 24 Tahun 2013 tentang Administrasi Kependudukan, peristiwa kelahiran wajib dilaporkan paling lambat 60 (enam puluh) hari sejak tanggal persalinan. Pelaporan dalam tenggat waktu tersebut diklasifikasikan sebagai Lahir Umum (LU), sedangkan pelaporan yang melampaui 60 hari dikategorikan sebagai Lahir Terlambat (LT) yang memerlukan kelengkapan pembuktian khusus berupa Surat Pernyataan Tanggung Jawab Mutlak (SPTJM). 

Kabupaten Natuna merupakan wilayah kepulauan terluar di Laut Natuna Utara yang menghadapi tantangan geografis berupa disparitas keterjangkauan transportasi antarpulau, ketergantungan cuaca ekstrem, dan rentang kendali menuju ibu kota kabupaten di Ranai. Penelitian ini menerapkan metodologi *Cross-Industry Standard Process for Data Mining* (CRISP-DM) untuk memetakan tingkat kepatuhan dan keterlambatan administrasi kependudukan menggunakan algoritma K-Means Clustering. 

Sebanyak 131 berkas fisik pendaftaran akta kelahiran resmi loket Disdukcapil Natuna diproses secara komprehensif. Dataset merupakan kohort pelayanan resmi loket Disdukcapil Kabupaten Natuna Tahun Pelaporan 2025 melalui protokol ketat audit *Zero Fabrication*, verifikasi administratif anomali slip loket (F044 dan F0124) terhadap buku register kelahiran, serta penyamaran identitas pribadi (PII) sesuai amanat UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi. Dua model K-Means komplementer dibangun: (1) **Model Spasial Wilayah (16 Kecamatan)** berbasis rasio kepatuhan LU dan median durasi hari (Silhouette Score = 0.6410, Davies-Bouldin Index = 0.4698) yang membagi Natuna menjadi Klaster High-Compliance, Moderate, dan High-Delay; serta (2) **Model Sosio-Ekonomi Pemohon Individu (131 Berkas)** yang menganalisis dimensi mikro bivariat dengan memetakan Sumbu X (Hari Usia Orang Tua Saat Lahir) terhadap Sumbu Y (Hari Keterlambatan Pelaporan) (Silhouette Score = 0.5533, DBI = 0.5905). Temuan riset diwujudkan dalam Dashboard Interaktif berbasis Peta Digital Spasial Leaflet dan melahirkan rekomendasi strategis pengadaan armada Kapal Pelayanan Keliling (*Mobile Service Boat*) bagi klaster kepulauan 3T.

**Kata Kunci:** Data Mining, K-Means Clustering, Akta Kelahiran, Disdukcapil Natuna, Analisis Spasial, CRISP-DM, Evaluasi Silhouette.

---

### DAFTAR ISI
- **HALAMAN JUDUL**
- **KATA PENGANTAR**
- **RINGKASAN EKSEKUTIF / ABSTRAK**
- **DAFTAR ISI**
- **DAFTAR TABEL**
- **DAFTAR GAMBAR**
- **BAB I BUSINESS UNDERSTANDING**
  - I.1 Latar Belakang Mitra Pemilik Data
  - I.2 Permasalahan yang Dihadapi Mitra
  - I.3 Tujuan Penambangan Data
  - I.4 Lini Waktu Pelaksanaan & Gantt Chart
- **BAB II DATA UNDERSTANDING**
  - II.1 Teknik Pengumpulan Data
  - II.2 Jenis Data & Skala Pengukuran
  - II.3 Exploratory Data Analysis (EDA) & Sebaran 8 Plot
- **BAB III PREPROCESS**
  - III.1 Penyelesaian Missing Value & Kebijakan Zero Fabrication
  - III.2 Data Selection & Eliminasi PII (UU No. 27/2022)
  - III.3 Data Transformation & Validasi Format Kronologis
  - III.4 Feature Engineering (Durasi Hari & Usia Orang Tua)
- **BAB IV MODEL**
  - IV.1 Teori Dasar K-Means Clustering
  - IV.2 Detail Perhitungan Matematis K-Means Langkah demi Langkah
  - IV.3 Model 1: K-Means Spasial Wilayah 16 Kecamatan
  - IV.4 Model 2: K-Means Sosio-Ekonomi Pemohon Individu
- **BAB V EVALUASI**
  - V.1 Metode Evaluasi Elbow (Inertia/WCSS)
  - V.2 Silhouette Coefficient Analysis
  - V.3 Davies-Bouldin Index (DBI)
  - V.4 Profiling dan Karakterisasi Klaster
- **BAB VI PENERAPAN**
  - VI.1 Desain Implementasi Sistem Dashboard Web Spasial
  - VI.2 Kesimpulan
  - VI.3 Rekomendasi Kebijakan Disdukcapil Natuna
- **LAMPIRAN**
  - Lampiran 1: Cuplikan Data Mentah Terdigitalisasi
  - Lampiran 2: Dokumentasi Lokasi dan Komunikasi Mitra
  - Lampiran 3: Tangkapan Layar Program & Dashboard

---

---

### DAFTAR TABEL
- **Tabel I.1:** Lini Waktu Pelaksanaan dan Pembagian Tanggung Jawab (Gantt Chart CRISP-DM)
- **Tabel II.1:** Kamus Data Atribut Administrasi Akta Kelahiran Disdukcapil Natuna
- **Tabel III.1:** Log Penanganan Kualitas Data, Koreksi Typo, dan Verifikasi Faktual
- **Tabel IV.1:** Simulasi Perhitungan Numerik Langkah demi Langkah Algoritma K-Means
- **Tabel IV.2:** Koordinat Centroid Model 1 (Spasial Wilayah 16 Kecamatan)
- **Tabel IV.3:** Koordinat Centroid Model 2 (Sosio-Ekonomi Pemohon Individu)
- **Tabel V.1:** Komparasi Validasi Metrik Evaluasi Kedua Model Penambangan Data
- **Tabel V.2:** Rekapitulasi Keanggotaan dan Karakteristik Klaster Spasial 16 Kecamatan
- **Tabel L.1:** Sampel Data Mentah Terdigitalisasi dengan Penyamaran Identitas Pribadi (PII)

---

### DAFTAR GAMBAR
- **Gambar I.1:** Catatan Reviewer Proposal Terkait Kewajiban Analisis Geospasial Wilayah
- **Gambar II.1:** Visualisasi Audit Kualitas Data dan Verifikasi Ketiadaan Fabrikasi
- **Gambar II.2:** Deteksi dan Penyelesaian Anomali Typo Kronologis Penanggalan
- **Gambar II.3:** Distribusi Bimodal Keterlambatan Pelaporan Akta Kelahiran
- **Gambar II.4:** Perbandingan Disparitas Spasial Berkas: Pulau Utama vs Kepulauan Terluar
- **Gambar II.5:** Tren Fluktuasi Bulanan Pelaporan Akta Kelahiran Sepanjang Tahun 2025
- **Gambar II.6:** Boxplot Dispersi dan Outlier Keterlambatan Antar-Kecamatan
- **Gambar II.7:** Scatter Plot Bivariat Usia Orang Tua terhadap Durasi Keterlambatan
- **Gambar II.8:** Heatmap Matriks Korelasi Spearman Antar-Fitur Kependudukan
- **Gambar IV.1:** Peta Geospasial Klaster Kepatuhan 16 Kecamatan Kabupaten Natuna
- **Gambar IV.2:** Visualisasi Model K-Means Sosio-Ekonomi Pemohon Individu
- **Gambar V.1:** Kurva Evaluasi Penentuan Klaster Optimal: Elbow dan Silhouette Score
- **Gambar VI.1:** Purwarupa Sistem Dashboard Web Spasial Interaktif Leaflet & Plotly

---

## BAB I: BUSINESS UNDERSTANDING

### I.1 Latar Belakang Mitra Pemilik Data
Dinas Kependudukan dan Pencatatan Sipil (Disdukcapil) Kabupaten Natuna, beralamat di Kompleks Perkantoran Pemerintah Daerah Bukit Arai, Jalan Batu Sisir, Ranai, Kecamatan Bunguran Timur, merupakan institusi pelaksana pemerintah daerah yang bertugas menyelenggarakan urusan administrasi kependudukan dan pencatatan sipil. Koordinasi teknis penelitian ini dilakukan bersama **Ibu Julida, S.Sos** (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk Disdukcapil Kabupaten Natuna).

Kabupaten Natuna merupakan kabupaten kepulauan terluar di wilayah Provinsi Kepulauan Riau yang berbatasan langsung dengan Vietnam, Malaysia, dan Laut Natuna Utara. Wilayah ini terbagi ke dalam 16 kecamatan administratif, di mana sebagian besar kecamatan terletak di gugusan pulau-pulau terpencil (seperti Kecamatan Pulau Laut, Midai, Suak Midai, Serasan, Serasan Timur, Subi, Pulau Tiga, dan Pulau Panjang). Aksesibilitas antar-pulau sangat bergantung pada moda transportasi laut tradisional (*pompong*) dan kapal perintis yang beroperasi dengan frekuensi terbatas serta sangat rentan terhenti oleh gelombang laut tinggi saat musim angin utara. Kondisi kemaritiman tersebut berdampak langsung terhadap kecepatan warga melaporkan peristiwa kelahiran anak ke loket Disdukcapil.

### I.2 Permasalahan yang Dihadapi Mitra
Berdasarkan Pasal 27 ayat (1) UU No. 24 Tahun 2013 tentang Perubahan atas UU No. 23 Tahun 2006 tentang Administrasi Kependudukan, setiap kelahiran wajib dilaporkan kepada instansi pelaksana paling lambat **60 (enam puluh) hari** sejak tanggal persalinan. Pelaporan yang melampaui 60 hari dikategorikan sebagai Lahir Terlambat (LT) dan mewajibkan verifikasi tambahan, termasuk pengisian Surat Pernyataan Tanggung Jawab Mutlak (SPTJM). 

Permasalahan nyata yang dihadapi Disdukcapil Kabupaten Natuna adalah:
1. **Disparitas Spasial Kepatuhan:** Terdapat ketimpangan tingkat kepatuhan pelaporan antara penduduk di Pulau Utama (Bunguran) dengan penduduk di pulau-pulau 3T (Terdepan, Terluar, Tertinggal). Ketiadaan pemetaan ilmiah membuat dinas kesulitan menentukan kecamatan prioritas intervensi.
2. **Keterbatasan Anggaran Pelayanan Keliling:** Layanan jemput bola (*mobile service*) membutuhkan alokasi bahan bakar kapal dan operasional petugas yang mahal, sehingga harus diarahkan tepat sasaran ke kantong-kantong wilayah berisiko tinggi (*High-Delay*).
3. **Akumulasi Keterlambatan Historis Warga Dewasa:** Banyak warga di kepulauan terluar baru mengajukan akta kelahiran setelah berusia belasan hingga puluhan tahun untuk keperluan paspor, pernikahan, atau pendaftaran sekolah, sehingga mendistorsi profil kepatuhan bayi baru lahir.

### I.3 Tujuan Penambangan Data
Tujuan penambangan data (*data mining*) dalam proyek ini adalah:
1. Melakukan segmentasi spasial terhadap 16 kecamatan di Natuna ke dalam klaster kepatuhan objektif (*High-Compliance*, *Moderate*, dan *High-Delay*) menggunakan algoritma K-Means Clustering.
2. Menginvestigasi hubungan multidimensi antara karakteristik usia orang tua saat persalinan (Sumbu X) terhadap lama keterlambatan pelaporan secara kontinu dalam hari (Sumbu Y) pada tingkat pemohon individu.
3. Membangun purwarupa *dashboard* peta digital interaktif sebagai instrumen pendukung keputusan (*Decision Support System*) pimpinan Disdukcapil Natuna dalam mengalokasikan armada pelayanan keliling perairan.

### I.4 Lini Waktu Pelaksanaan & Gantt Chart
Proyek riset penambangan data ini diselesaikan secara tim selama kurun waktu Semester Ganjil Tahun Akademik 2026/2027 dengan pembagian peran dan penanggung jawab (*Person in Charge / PIC*) yang jelas:

| No | Tahapan Kegiatan (CRISP-DM) | Waktu Pelaksanaan | Output Nyata | PIC (Penanggung Jawab) |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Koordinasi Mitra & Perumusan Masalah | Minggu 1–2 (Okt 2026) | Berkas Proposal & Izin Disdukcapil | **Ridho Ramadani E** (Ketua) |
| 2 | Pengumpulan Arsip Fisik & Digitisasi | Minggu 3–4 (Okt 2026) | 131 Berkas Pindaian Transkripsi Excel | **Salma Nursafira** |
| 3 | Audit Kualitas Data & Zero Fabrication | Minggu 5 (Nov 2026) | Log Koreksi F044/F0124 & Imputasi Faktual | **Monalisa Dwi Cantika** |
| 4 | Preprocessing & Eliminasi PII (UU PDP) | Minggu 6 (Nov 2026) | Dataset Bersih & Fitur Durasi Hari | **Sarah Fauziyyah** |
| 5 | Pemodelan K-Means & Validasi Metrik | Minggu 7 (Nov 2026) | Model Spasial & Sosio-Ekonomi (K=3) | **Muhammad Agus Farhan** |
| 6 | Pembuatan Dashboard & Laporan Akhir | Minggu 8 (Nov 2026) | Dashboard Peta Leaflet & Dokumen FinPD | **Ridho Ramadani E** & Tim |

---

## BAB II: DATA UNDERSTANDING

### II.1 Teknik Pengumpulan Data
Data penelitian bersumber dari data primer operasional pelayanan loket pendaftaran akta kelahiran Disdukcapil Kabupaten Natuna. Sebanyak 131 folder berkas pindaian resmi (memuat 262 citra dokumen) yang mencakup 131 berkas permohonan individu diekstraksi dan ditranskripsikan secara cermat. Dokumen terdiri dari dua jenis berkas yuridis utama:
1. **Formulir Pelaporan Pencatatan Kelahiran (Kode F-2.01):** Memuat data demografi pemohon, data orang tua (ayah dan ibu), saksi, dan anak.
2. **Surat Keterangan Lahir (SKL) / SPTJM Kebenaran Kelahiran:** Memuat bukti medis penolong persalinan (Dokter, Bidan, Tenaga Medis, atau Dukun) dan faskes tempat dilahirkan (RSUD, Puskesmas, Polindes, atau Rumah Pribadi).

### II.2 Jenis Data & Skala Pengukuran
Data yang dikumpulkan dianalisis berdasarkan skala pengukuran data mining:
1. **Data Nominal:** Nomor Berkas Anonim (`ID_Data`), Kecamatan, Desa/Kelurahan, Jenis Kelamin Bayi, Tempat Dilahirkan (`RSUD`, `PUSKESMAS`, `POLINDES`, `RUMAH`), Penolong Kelahiran (`DOKTER`, `BIDAN`, `DUKUN`), Jenis Dokumen Bukti (`SKL_MEDIS` vs `SPTJM`), dan Status Kepatuhan (`LU` vs `LT`).
2. **Data Ordinal:** Kelahiran Ke / Anak Ke (`1, 2, 3, ...`).
3. **Data Interval:** Tanggal Lahir Anak, Tanggal Pelaporan Permohonan, Tanggal Lahir Ayah, dan Tanggal Lahir Ibu (format *Date/Datetime*).
4. **Data Rasio:** 
   - `Durasi_Pelaporan_Hari`: Selisih hari kontinu antara tanggal pelaporan dan tanggal lahir ($T_{ext{lapor}} - T_{ext{lahir}}$), rentang 0 s.d. 18.000+ hari.
   - `Hari_Usia_Ortu`: Usia rata-rata orang tua saat anak lahir dihitung tepat dalam satuan hari ($15 \le ext{Usia} \le 75$ tahun).
   - `Persentase_LU`: Rasio persentase kelahiran tepat waktu per kecamatan (rentang 0.0% s.d. 100.0%).

### II.3 Exploratory Data Analysis (EDA)
Analisis eksplorasi data komprehensif didukung oleh delapan (8) plot visualisasi mendalam:
1. **Audit Ketiadaan Fabrikasi (Missing Values):** Pemeriksaan 131 baris membuktikan kolom pekerjaan pada formulir RSUD yang kosong secara transparan dipertahankan apa adanya dengan label *"Tanpa Keterangan (Template RSUD)"* tanpa mereka-reka data sintetik.
2. **Deteksi Anomali Typo Kronologis:** Berkas F044 (tertulis lahir 2025 dilaporkan 2024) dan F0124 (tertulis lahir 2026 dilaporkan 2025) terbukti merupakan kesalahan pengetikan slip loket (*human error*). Dilakukan koreksi yuridis konsisten sehingga tidak ada durasi negatif ($T_{ext{lapor}} \ge T_{ext{lahir}}$) dan seluruh data berada pada kalender studi **Tahun Pelaporan 2025**.
3. **Distribusi Bimodal Keterlambatan:** Grafik histogram menunjukkan kurva memiliki dua puncak ekstrem (*bimodal distribution*): Puncak pertama pada rentang 0–60 hari (bayi baru lahir tepat waktu LU), dan puncak kedua pada rentang 1.000–18.000 hari (warga dewasa yang baru mengurus akta kelahiran menggunakan instrumen SPTJM).
4. **Disparitas Spasial:** Perbandingan volume berkas membuktikan Pulau Utama Bunguran menyumbang 68.7% berkas, sementara 9 kecamatan pulau terluar menyumbang 31.3% berkas dengan rata-rata keterlambatan yang jauh lebih masif.
5. **Tren Bulanan Pelaporan 2025:** Pengajuan akta kelahiran meningkat tajam pada bulan Juni–Juli menjelang tahun ajaran baru sekolah dan momentum pendaftaran beasiswa/kedinasan.
6. **Boxplot Outlier Antar-Kecamatan:** Kecamatan kepulauan terluar (seperti Serasan dan Midai) menunjukkan dispersi kuartil keterlambatan ekstrem di atas 10.000 hari.
7. **Scatter Plot Bivariat Usia vs Keterlambatan:** Menunjukkan korelasi bahwa orang tua muda usia 20–30 tahun memiliki rasio kepatuhan LU tinggi, sedangkan orang tua usia di atas 45 tahun berkorelasi dengan akta kelahiran terlambat puluhan tahun.
8. **Matriks Korelasi Spearman:** Mengonfirmasi korelasi kuat positif antara instrumen SPTJM dengan besarnya nilai `Durasi_Pelaporan_Hari` ($
ho = 0.82$).

---

## BAB III: PREPROCESS

### III.1 Penyelesaian Missing Value & Kebijakan Zero Fabrication
Sesuai protokol integritas ilmiah, tim peneliti menolak keras pembuatan data fiktif (*zero data fabrication*). Pada data mentah pindaian, kolom `Pekerjaan_Ayah` dan `Pekerjaan_Ibu` pada surat keterangan medis RSUD Natuna tidak memuat isian pekerjaan. Tindakan pra-proses yang dilakukan adalah mengisi nilai kosong tersebut dengan kategori formal `'Tanpa Keterangan (Template RSUD)'`. Sementara itu, data missing pada atribut `Tempat_Lahir` atau `Jam_Lahir` dilengkapi melalui sinkronisasi silang faktual Tier 1 antara Formulir F-2.01 dan Surat Keterangan Lahir fisik.

### III.2 Data Selection & Eliminasi PII (UU No. 27/2022)
Untuk mematuhi Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP), seluruh atribut pengidentifikasi langsung (*Personally Identifiable Information / PII*) seperti NIK Anak, NIK Ayah/Ibu, Nama Lengkap, Nomor Kartu Keluarga (NKK), dan Alamat Rumah Nomor RT/RW dieliminasi dari dataset pemodelan. Setiap pemohon diberikan identitas anonim unik (`B_001` s.d. `B_131`).

### III.3 Data Transformation & Validasi Format Kronologis
1. **Penetapan Format Penanggalan ISO:** Seluruh tanggal ditransformasikan ke format standar ISO-8601 (`YYYY-MM-DD`).
2. **Validasi Kohort Pelayanan Tahun 2025:** Seluruh berkas sampel merupakan arsip resmi pelayanan loket Disdukcapil Natuna pada Tahun Pelayanan 2025 yang tervalidasi pada hari kerja operasional kedinasan.
3. **Penyelesaian Anomali Typo Kronologis:**
   - Berkas `F044`: Tertulis lahir 18 Mei 2025 namun tanggal lapor terketik 18 Mei 2024 (-365 hari akibat salah ketik digit tahun petugas loket). Berdasarkan verifikasi buku register dan SKL medis, tanggal lapor dikoreksi secara faktual menjadi 2025-05-18 (Lahir Umum, durasi 0 hari).
   - Berkas `F0124`: Tertulis lahir 6 Juli 2026 (salah ketik digit tahun loket ke depan). Dikoreksi secara yuridis berdasarkan register kelahiran menjadi tanggal lahir 2025-07-06 dengan tanggal lapor 2025-07-06 (Lahir Umum, durasi 0 hari).

### III.4 Feature Engineering (Rekayasa Fitur)
Dua fitur analitis utama direkayasa berdasarkan landasan yuridis dan biologis:
1. **Durasi Pelaporan Kontinu (Hari):**
   $$ext{Durasi\_Pelaporan\_Hari} = T_{ext{Pelaporan}} - T_{ext{Lahir}}$$
   Status kepatuhan ditentukan secara deterministik:
   $$ext{Status} = \begin{cases} ext{LU (Lahir Umum)}, & ext{jika Durasi} \le 60 ext{ hari} \ ext{LT (Lahir Terlambat)}, & ext{jika Durasi} > 60 ext{ hari} \end{cases}$$
2. **Usia Biologis Orang Tua Saat Anak Lahir (Hari):**
   Dihitung secara presisi pada saat tanggal kelahiran anak:
   $$ext{Hari\_Usia\_Ortu} = \frac{(T_{ext{Lahir Anak}} - T_{ext{Lahir Ayah}}) + (T_{ext{Lahir Anak}} - T_{ext{Lahir Ibu}})}{2}$$
3. **Agregasi Spasial 16 Kecamatan:**
   Setiap kecamatan dihitung total berkas ($N_k$), rasio kepatuhan $ext{Persentase\_LU}_k = \frac{\sum ext{LU}}{N_k} imes 100\%$, serta nilai median durasi keterlambatan ($ext{Median\_Durasi}_k$).

---

## BAB IV: MODEL

### IV.1 Teori Dasar K-Means Clustering
K-Means merupakan algoritma *unsupervised learning* yang bertujuan mempartisi $N$ objek data ke dalam $K$ klaster, di mana setiap objek ditempatkan ke dalam klaster dengan *centroid* (titik pusat) terdekat. K-Means meminimalkan fungsi objektif *Within-Cluster Sum of Squares* (WCSS) / *Inertia*:
$$J = \sum_{k=1}^K \sum_{x_i \in S_k} \| x_i - \mu_k \|^2$$
di mana $S_k$ adalah himpunan objek dalam klaster ke-$k$, dan $\mu_k$ adalah titik pusat (*centroid*) klaster ke-$k$.

### IV.2 Detail Perhitungan Matematis K-Means Langkah demi Langkah

Sesuai instruksi baku RTM Bab IV, berikut disajikan formulasi matematis dan simulasi perhitungan numerik langkah demi langkah (*step-by-step mathematical walkthrough*):

#### Langkah 1: Standardisasi Fitur (Z-Score Standardization)
Karena variabel dalam data mining memiliki skala satuan yang berbeda (misalnya rasio persen 0–100% vs durasi hari 0–16.000 hari), fitur wajib ditransformasikan menggunakan Z-Score agar fitur berentang besar tidak mendominasi perhitungan jarak Euclidean:
$$z_{ij} = \frac{x_{ij} - \mu_j}{\sigma_j}$$
di mana $\mu_j$ adalah nilai rata-rata (*mean*) fitur ke-$j$, dan $\sigma_j$ adalah simpangan baku (*standard deviation*) fitur ke-$j$:
$$\mu_j = \frac{1}{N} \sum_{i=1}^N x_{ij}, \quad \sigma_j = \sqrt{\frac{1}{N} \sum_{i=1}^N (x_{ij} - \mu_j)^2}$$

#### Langkah 2: Perhitungan Matriks Jarak Euclidean (Euclidean Distance)
Jarak antara titik data ke-$i$ ($x_i$) dengan centroid klaster ke-$k$ ($\mu_k$) dihitung dalam ruang berdimensi $D$:
$$d(x_i, \mu_k) = \sqrt{\sum_{j=1}^D (z_{ij} - \mu_{kj})^2}$$

#### Langkah 3: Pengalokasian Anggota Klaster (Cluster Assignment)
Setiap objek $x_i$ dimasukkan ke dalam klaster $k^*$ yang memiliki jarak Euclidean terpendek:
$$k^* = \arg\min_{k \in \{1, \dots, K\}} d(x_i, \mu_k)$$

#### Langkah 4: Pembaruan Titik Pusat Centroid (Centroid Updating)
Centroid baru dihitung sebagai rata-rata aritmatika dari seluruh objek yang menjadi anggota klaster tersebut:
$$\mu_k^{(t+1)} = \frac{1}{|S_k|} \sum_{x_i \in S_k} z_i$$
Proses diulang hingga konvergen (posisi centroid tidak berubah atau perubahan berada di bawah ambang batas toleransi $\epsilon = 10^{-4}$).

#### Contoh Simulasi Perhitungan Manual Numerik Nyata:
Diberikan 3 kecamatan sampel dari Kabupaten Natuna:
1. $D_1$ (Bunguran Tengah): $ext{LU} = 66.7\%$, $ext{Median Durasi} = 1ext{ hari}$
2. $D_2$ (Bunguran Timur): $ext{LU} = 35.7\%$, $ext{Median Durasi} = 148.5ext{ hari}$
3. $D_3$ (Serasan): $ext{LU} = 0.0\%$, $ext{Median Durasi} = 7.888ext{ hari}$

Misalkan nilai statistik populasi: $\mu_{ext{LU}} = 16.5\%$, $\sigma_{ext{LU}} = 27.5\%$, $\mu_{ext{Durasi}} = 5.750$, $\sigma_{ext{Durasi}} = 6.200$.
- Standardisasi $D_1$:
  $$z_{ext{LU}} = \frac{66.7 - 16.5}{27.5} = +1.825, \quad z_{ext{Dur}} = \frac{1 - 5750}{6200} = -0.927$$
- Standardisasi $D_3$:
  $$z_{ext{LU}} = \frac{0 - 16.5}{27.5} = -0.600, \quad z_{ext{Dur}} = \frac{7888 - 5750}{6200} = +0.345$$
- Jarak Euclidean antara $D_1$ dan $D_3$:
  $$d(D_1, D_3) = \sqrt{(1.825 - (-0.600))^2 + (-0.927 - 0.345)^2} = \sqrt{(2.425)^2 + (-1.272)^2} = \sqrt{5.880 + 1.618} = 2.738$$
Perhitungan deterministik ini dijalankan secara otomatis oleh pustaka `scikit-learn` dengan parameter penguncian `random_state=42`.

### IV.3 Model 1: K-Means Spasial Wilayah (16 Kecamatan)
Model 1 dirancang khusus untuk merespons **Peringatan Keras Dosen Reviewer** agar memetakan disparitas keterlambatan antar-wilayah di Kabupaten Natuna.
- **Entitas:** 16 Kecamatan di Kabupaten Natuna.
- **Fitur Masukan:** $ext{Persentase\_LU}$ dan $ext{Median\_Durasi\_Hari}$.
- **Jumlah Klaster Optimal:** $K = 3$.
- **Centroid Skala Asli:**
  - *Centroid Klaster 0 (High-Compliance):* Rasio LU = 83.35%, Median Durasi = 1.0 hari.
  - *Centroid Klaster 1 (Moderate):* Rasio LU = 13.76%, Median Durasi = 424.1 hari.
  - *Centroid Klaster 2 (High-Delay):* Rasio LU = 1.30%, Median Durasi = 12.532.6 hari (~34.3 tahun).

### IV.4 Model 2: K-Means Sosio-Ekonomi Pemohon Individu
Model 2 menganalisis karakteristik demografis dan sosio-ekonomi pemohon secara bivariat pada tingkat individu:
- **Entitas:** 131 Berkas Permohonan Aktif.
- **Fitur Masukan:** Sumbu X (`Hari_Usia_Ortu`) vs Sumbu Y (`Durasi_Pelaporan_Hari`).
- **Jumlah Klaster Optimal:** $K = 3$.
- **Centroid Skala Asli:**
  - *Klaster 0: Tepat Waktu (Lahir Umum) (n=49):* Usia Rata-rata Ortu = 9.480 hari (26.0 tahun), Durasi Keterlambatan = 22 hari. Karakteristik: Didominasi keluarga muda usia produktif awal dengan profesi wiraswasta, nelayan modern, dan pedagang.
  - *Klaster 1: Terlambat Sedang (Balita-Anak) (n=46):* Usia Rata-rata Ortu = 13.820 hari (37.8 tahun), Durasi Keterlambatan = 1.840 hari (5.0 tahun). Karakteristik: PNS/TNI/Polri dan petani yang baru mengurus akta kelahiran saat anak menjelang masuk bangku sekolah dasar.
  - *Klaster 2: Terlambat Historis (Dewasa SPTJM) (n=36):* Usia Rata-rata Ortu = 10.450 hari (28.6 tahun saat anak lahir), Durasi Keterlambatan = 15.680 hari (42.9 tahun). Karakteristik: Warga dewasa dan lansia di kepulauan terluar yang belum pernah memiliki dokumen kependudukan resmi sejak lahir.

---

## BAB V: EVALUASI

### V.1 Metode Evaluasi Elbow (Inertia/WCSS)
Pengujian nilai $K$ dari rentang $K=2$ hingga $K=6$ dievaluasi menggunakan metode Elbow (*Inertia / Within-Cluster Sum of Squares*). Pada Model Spasial Wilayah, penurunan nilai WCSS paling drastis terjadi saat transisi dari $K=2$ ke $K=3$, dan mengalami kelandaian (*elbow point*) setelah $K=3$.

### V.2 Silhouette Coefficient Analysis
Koefisien Silhouette mengukur seberapa dekat suatu titik dengan titik-titik di klasternya sendiri dibandingkan dengan titik di klaster tetangga terdekat:
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$
di mana $a(i)$ adalah rata-rata jarak intra-klaster, dan $b(i)$ adalah rata-rata jarak inter-klaster terdekat. Nilai berkisar antara $-1$ hingga $+1$.

### V.3 Davies-Bouldin Index (DBI)
Davies-Bouldin Index mengukur rasio antara penyebaran intra-klaster dengan pemisahan inter-klaster:
$$R_{ij} = \frac{s_i + s_j}{d(c_i, c_j)}, \quad DBI = \frac{1}{K} \sum_{i=1}^K \max_{j 
eq i} R_{ij}$$
Nilai DBI yang semakin mendekati nol (0) menandakan partisi klaster yang semakin kompak dan terpisah secara optimal.

### V.4 Tabel Validasi Hasil Evaluasi Kedua Model

| Metrik Evaluasi | Model 1: Spasial Wilayah (16 Kecamatan) | Model 2: Sosio-Ekonomi Individu (131 Berkas) | Standar Kelayakan Akademik |
| :--- | :---: | :---: | :--- |
| **Nilai K Terpilih** | **K = 3** | **K = 3** | Titik tekuk Elbow & Puncak Silhouette |
| **Silhouette Score** | **0.6410** | **0.5533** | $> 0.50$ (Struktur Klaster Sangat Kuat / *Dense*) |
| **Davies-Bouldin Index**| **0.4698** | **0.5905** | $< 0.80$ (Separasi Antar-Klaster Sangat Baik) |
| **Inertia / WCSS** | 5.824 | 48.612 | Minimum stabil pada titik Elbow |

### V.5 Profiling dan Karakterisasi Klaster

#### 1. Profiling Klaster Spasial 16 Kecamatan:
- **Cluster 0 (High-Compliance, n=2):** Bunguran Tengah dan Pulau Laut. Memiliki tingkat kepatuhan pelaporan $\le 60$ hari tertinggi (rata-rata 83.35%) dengan median keterlambatan hanya 1.0 hari. Wilayah ini menjadi percontohan tertib adminduk.
- **Cluster 1 (Moderate Compliance, n=7):** Bunguran Timur, Bunguran Barat, Bunguran Selatan, Bunguran Utara, Bunguran Batubi, Serasan Timur, dan Subi. Memiliki rasio kepatuhan LU 13.76% dengan median keterlambatan berkisar 148 s.d. 636 hari (1–2 tahun). Keterlambatan umumnya terkait urusan administratif masuk sekolah.
- **Cluster 2 (High-Delay, n=7):** Bunguran Timur Laut, Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, dan Pulau Panjang. Memiliki rasio LU terendah (rata-rata 1.30%) dengan median keterlambatan sangat tinggi (7.888 hingga 16.635 hari, atau 21 hingga 45 tahun). Klaster ini didominasi dokumen SPTJM permohonan akta kelahiran susulan bagi warga dewasa/lansia.

---

## BAB VI: PENERAPAN

### VI.1 Desain Implementasi Sistem Dashboard Web Spasial
Hasil pemodelan penambangan data diimplementasikan ke dalam purwarupa aplikasi web interaktif mandiri: `dashboard_interaktif_kmeans_dosen.html`. Sistem ini mengintegrasikan dua teknologi visualisasi terdepan:
1. **Leaflet.js & OpenStreetMap:** Memetakan ke-16 kecamatan di kepulauan Natuna secara geografis menggunakan koordinat lintang/bujur riil. Setiap kecamatan diberi penanda lingkaran (*circle marker*) dengan kode warna dinamis:
   - 🟢 **Hijau:** Cluster 0 (High-Compliance)
   - 🟠 **Oranye:** Cluster 1 (Moderate)
   - 🔴 **Merah:** Cluster 2 (High-Delay)
   Saat penanda diklik, pop-up interaktif menampilkan rincian persentase LU, median hari, jumlah berkas, dan rekomendasi operasional dinas.
2. **Plotly.js Interactive Scatter:** Menampilkan visualisasi interaktif Sumbu X (Usia Ortu) vs Sumbu Y (Keterlambatan Hari) dengan kursor inspeksi (*hover tooltip*) per berkas pemohon.

### VI.2 Kesimpulan
1. Proyek penambangan data berhasil mengelompokkan 16 kecamatan di Disdukcapil Kabupaten Natuna ke dalam 3 klaster kepatuhan terukur berbasis rasio Lahir Umum dan median durasi hari (Silhouette Score = 0.6410, DBI = 0.4698).
2. Model sosio-ekonomi pemohon individu membuktikan secara empiris bahwa keluarga muda usia produktif (~26 tahun) mendominasi klaster tertib waktu (Lahir Umum), sedangkan keterlambatan puluhan tahun pada pulau terluar didominasi oleh warga dewasa/lansia melalui instrumen hukum SPTJM.
3. Seluruh tahapan penelitian mematuhi metodologi standar CRISP-DM, prinsip *Zero Data Fabrication*, serta perlindungan kerahasiaan data kependudukan sesuai UU No. 27 Tahun 2022.

### VI.3 Rekomendasi Kebijakan Disdukcapil Kabupaten Natuna
Berdasarkan hasil temuan klaster spasial, diajukan 3 rekomendasi kebijakan konkret:
1. **Pengadaan Armada Kapal Pelayanan Keliling (*Mobile Service Boat*):**
   Disdukcapil Natuna direkomendasikan mengalokasikan anggaran kapal dinas keliling secara terjadwal khusus untuk kecamatan Klaster 2 (Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, dan Pulau Panjang) guna menjemput berkas dan perekaman dokumen di pulau-pulau tanpa menunggu warga datang ke Ranai.
2. **Pelayanan Sidang Terpadu Verifikasi SPTJM Massal Tingkat Desa:**
   Mengingat tingginya akumulasi permohonan akta kelahiran terlambat puluhan tahun pada warga dewasa di Klaster 2, disarankan menyelenggarakan sidang isbat nikah dan verifikasi kebenaran kelahiran SPTJM terpadu bekerja sama dengan Pengadilan Agama dan Kementerian Agama setempat di balai desa.
3. **Penguatan Kerja Sama Faskes di Klaster Moderate:**
   Untuk kecamatan Klaster 1, dinas cukup meningkatkan integrasi pelaporan otomatis dengan bidan desa dan Puskesmas Pembantu (Pustu) sehingga penerbitan Surat Keterangan Lahir (SKL) langsung terkoneksi dengan penerbitan Nomor Identitas Kependudukan (NIK) bayi baru lahir.

---

---

## DAFTAR PUSTAKA

1. Davies, D. L., & Bouldin, D. W. (1979). A cluster separation measure. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, (2), 224-227.
2. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann Publishers.
3. Kementerian Dalam Negeri Republik Indonesia. (2019). *Peraturan Menteri Dalam Negeri Nomor 108 Tahun 2019 tentang Peraturan Pelaksanaan Peraturan Presiden Nomor 96 Tahun 2018 tentang Persyaratan dan Tata Cara Pendaftaran Penduduk dan Pencatatan Sipil*. Jakarta: Kemendagri.
4. MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. In *Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability* (Vol. 1, pp. 281-297).
5. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.
6. Republik Indonesia. (2013). *Undang-Undang Nomor 24 Tahun 2013 tentang Perubahan atas Undang-Undang Nomor 23 Tahun 2006 tentang Administrasi Kependudukan*. Lembaran Negara Republik Indonesia Tahun 2013 Nomor 232. Jakarta: Sekretariat Negara.
7. Republik Indonesia. (2022). *Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi*. Lembaran Negara Republik Indonesia Tahun 2022 Nomor 196. Jakarta: Sekretariat Negara.
8. Rousseeuw, P. J. (1987). Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. *Journal of Computational and Applied Mathematics*, 20, 53-65.
9. Tan, P. N., Steinbach, M., & Kumar, V. (2016). *Introduction to Data Mining*. Pearson Education India.

---

## LAMPIRAN

### Lampiran 1: Cuplikan Tabulasi Data Mentah Terdigitalisasi (Tersamar Sesuai Panduan)
Data mentah telah disamarkan privasinya secara konsisten (Nama X001, NIK X001, dsb.):

| ID Data | Kecamatan | Kelurahan/Desa | Status Dokumen | Tgl Lahir | Tgl Pelaporan | Kepatuhan |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| B_001 | BUNGURAN TIMUR LAUT | KELANGA | SPTJM | 1974-05-18 | 2025-05-18 | LT (Terlambat) |
| B_002 | BUNGURAN UTARA | KELARIK UTARA | SPTJM | 1984-06-25 | 2025-06-25 | LT (Terlambat) |
| B_003 | BUNGURAN TIMUR | RANAI KOTA | SKL RSUD | 2025-03-24 | 2025-04-10 | LU (Umum) |
| B_004 | BUNGURAN TENGAH | HARAPAN JAYA | SKL POLINDES | 2025-07-02 | 2025-07-03 | LU (Umum) |
| B_005 | SERASAN | SERASAN | SPTJM | 1993-08-14 | 2025-08-14 | LT (Terlambat) |

### Lampiran 2: Dokumentasi Kegiatan & Komunikasi Mitra
- **Instansi Mitra:** Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna
- **Alamat:** Kompleks Perkantoran Bukit Arai, Ranai, Kepulauan Riau
- **Narasumber:** Ibu Julida, S.Sos (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk)
- **Status Koordinasi:** Data berasal dari arsip pelayanan loket registrasi akta kelahiran aktif.

### Lampiran 3: Tangkapan Layar Program & Dashboard
1. Peta Geospatial Klaster 16 Kecamatan Natuna: `07_VISUALISASI_DAN_DASHBOARD/peta_geospatial_klaster_natuna.png`
2. Grafik Scatter Model Sosio-Ekonomi Pemohon Individu: `04_MODELING/02_kmeans_sosioekonomi_individu/scatter_model_sosioekonomi_individu.png`
3. Grafik Evaluasi Elbow & Silhouette: `06_EVALUASI_DAN_VALIDASI_MODEL/evaluasi_elbow_silhouette.png`
4. Berkas Interaktif HTML: `07_VISUALISASI_DAN_DASHBOARD/dashboard_interaktif_kmeans_dosen.html`
