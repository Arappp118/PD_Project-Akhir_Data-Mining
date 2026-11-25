# PANDUAN SKENARIO PRESENTASI & PEMBAGIAN KONTRIBUSI TIM
## Proyek Penambangan Data (PD-NTN25-FINAL)
**"Pengelompokkan Wilayah dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering pada Disdukcapil Kabupaten Natuna"**

**Program Studi Teknik Informatika — Fakultas Teknik dan Teknologi Kemaritiman**  
**Universitas Maritim Raja Ali Haji (UMRAH) — Tahun 2026**

---

### SUSUNAN TIM PENELITI & PEMBAGIAN PERAN UTAMA

| No | NIM | Nama Mahasiswa | Peran Utama Proyek | Tanggung Jawab Bab Presentasi |
|:---:|:---:|:---|:---|:---|
| 1 | **2401020121** | **Ridho Ramadani E** | **Ketua Tim (Project Leader)** | Pembukaan, BAB I (Business Understanding), BAB VI (Deployment & Rekomendasi), Penutup & Q&A Lead |
| 2 | **2401020094** | **Salma Nursafira** | **Data Analyst** | BAB II (Data Understanding, Digitalisasi 131 Berkas, Kamus Data, & 8 Visualisasi EDA) |
| 3 | **2401020100** | **Monalisa Dwi Cantika** | **Data Preprocessing Specialist** | BAB III.1 & III.3 (Data Preparation: Audit Kualitas, Zero Data Fabrication, Verifikasi Faktual Typo Loket F044/F0124 & Validasi Kohort 2025) |
| 4 | **2401020109** | **Sarah Fauziyyah** | **Feature Engineer & Compliance** | BAB III.2 & III.4 (Anonimisasi PII UU No. 27/2022, Feature Engineering Hari & Agregasi Spasial 16 Kecamatan) |
| 5 | **2401020111** | **Muhammad Agus Farhan** | **Machine Learning & Modeling Specialist** | BAB IV & BAB V (Pemodelan K-Means Spasial & Sosio-Ekonomi Individu, Hitungan Manual Euclidean, & Validasi Metrik Evaluasi) |

---

### RANCANGAN STRUKTUR SLIDE PRESENTASI (ESTIMASI 15 MENIT)

* **Slide 1:** Judul Proyek, Logo UMRAH, Nama & NIM Tim Peneliti *(Ridho)*
* **Slide 2:** Latar Belakang Mitra Disdukcapil Natuna & Problematika Geografis Kemaritiman *(Ridho)*
* **Slide 3:** Permasalahan (UU No. 24/2013 Batas 60 Hari LU/LT) & Catatan Reviewer Proposal *(Ridho)*
* **Slide 4:** Tujuan Penambangan Data & Metodologi CRISP-DM *(Ridho)*
* **Slide 5:** Pengumpulan Data: Dari 131 Folder Berkas Fisik Menjadi 131 Berkas Digital *(Salma)*
* **Slide 6:** Kamus Data Atribut & Analisis Eksplorasi Data (8 Visualisasi EDA) *(Salma)*
* **Slide 7:** Preprocessing: Zero Data Fabrication & Koreksi Anomali Kronologis (F044 & F0124) *(Monalisa)*
* **Slide 8:** Validasi Kohort Pelayanan 2025 & Penanganan Missing Value *(Monalisa)*
* **Slide 9:** Kepatuhan Regulasi PII (UU No. 27/2022) & Rekayasa Fitur Kontinu Hari *(Sarah)*
* **Slide 10:** Reduksi Dimensi & Agregasi Spasial 16 Kecamatan Natuna *(Sarah)*
* **Slide 11:** Algoritma K-Means: Detail Perhitungan Manual Jarak Euclidean & Centroid Baru *(Farhan)*
* **Slide 12:** Model 1: K-Means Spasial 16 Kecamatan (Peta Zonasi Kepatuhan) *(Farhan)*
* **Slide 13:** Model 2: K-Means Sosio-Ekonomi Pemohon Individu (Sumbu X Usia Ortu vs Sumbu Y Keterlambatan) *(Farhan)*
* **Slide 14:** Evaluasi Model: Analisis Elbow, Silhouette Score, & Davies-Bouldin Index *(Farhan)*
* **Slide 15:** Demonstrasi Langsung Purwarupa Dashboard Web Interaktif (Leaflet & Plotly) *(Ridho & Farhan)*
* **Slide 16:** Kesimpulan Ilmiah & 3 Rekomendasi Kebijakan Disdukcapil Natuna *(Ridho)*
* **Slide 17:** Penutup & Sesi Diskusi / Tanya Jawab *(Seluruh Tim)*

---

### DETAIL SKENARIO & NASKAH BERBICARA (TALKING POINTS)

#### 🎙️ PEMBICARA 1: Ridho Ramadani E (Ketua Tim / NIM 2401020121)
* **Waktu Alokasi:** 3 Menit (Bagian Awal)
* **Materi:** Pembukaan, BAB I (Business Understanding), Latar Belakang, Permasalahan, & Tujuan.
* **Contoh Naskah Bicara:**
  > *"Selamat pagi/siang kepada Bapak/Ibu Dosen Penguji dan Rekan-rekan sekalian. Saya Ridho Ramadani E, selaku ketua tim peneliti, bersama rekan-rekan saya: Salma, Monalisa, Sarah, dan Farhan, akan mempresentasikan hasil akhir proyek penambangan data kami yang berjudul: **Pengelompokkan Wilayah dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering pada Disdukcapil Kabupaten Natuna**."*
  > 
  > *"Sebagai daerah kepulauan terdepan di Laut Natuna Utara dengan 16 kecamatan, Disdukcapil Natuna menghadapi tantangan maritim yang luar biasa: keterbatasan akses transportasi pompong dan kapal perintis saat musim utara. Berdasarkan amanat UU No. 24 Tahun 2013, setiap kelahiran wajib dicatatkan maksimal 60 hari (Lahir Umum). Lewat dari itu berstatus Lahir Terlambat dan membutuhkan dokumen SPTJM. Proyek ini hadir untuk menjawab dua hal: pertama, menindaklanjuti arahan tegas Dosen Reviewer Proposal untuk memetakan zonasi kepatuhan 16 kecamatan; dan kedua, menganalisis dimensi mikro sosio-ekonomi pemohon individu mengenai korelasi usia orang tua terhadap durasi keterlambatan secara objektif."*

---

#### 🎙️ PEMBICARA 2: Salma Nursafira (NIM 2401020094)
* **Waktu Alokasi:** 2.5 Menit
* **Materi:** BAB II (Data Understanding), Digitalisasi 131 Berkas, Kamus Data, & Temuan Kunci EDA.
* **Contoh Naskah Bicara:**
  > *"Terima kasih Ketua. Melanjutkan ke Bab II Data Understanding, data yang kami teliti merupakan data primer resmi hasil digitalisasi 131 folder arsip pindaian fisik loket pelayanan Disdukcapil Natuna (memuat 262 dokumen), yang menghasilkan 131 entri data individu permohonan akta kelahiran yang sah."*
  > 
  > *"Dari 131 berkas tersebut, kami menyusun kamus data yang membedah atribut demografi anak, orang tua, status yuridis, dan durasi pelaporan. Melalui 8 grafik visualisasi EDA yang kami bangun menggunakan Python Seaborn dan Matplotlib, kami menemukan fakta krusial: distribusi keterlambatan memiliki pola bimodal ekstrem. Puncak pertama adalah kelahiran baru usia 0–60 hari, sedangkan puncak kedua adalah warga dewasa berusia belasan hingga puluhan tahun yang baru mengurus akta karena kebutuhan administrasi mendesak. Selain itu, terdapat disparitas mencolok antara pulau utama Bunguran dengan kecamatan kepulauan 3T seperti Midai dan Serasan."*

---

#### 🎙️ PEMBICARA 3: Monalisa Dwi Cantika (NIM 2401020100)
* **Waktu Alokasi:** 2.5 Menit
* **Materi:** BAB III (Data Preprocessing Bagian 1), Audit Kualitas Data, Zero Data Fabrication, & Validasi Kohort Pelayanan 2025.
* **Contoh Naskah Bicara:**
  > *"Terima kasih Salma. Pada Bab III Preprocess, prinsip fundamental yang kami pegang teguh adalah **Zero Data Fabrication** — kami menolak keras melakukan fabrikasi atau manipulasi data dummy."*
  > 
  > *"Dalam penanganan missing value, misalnya pada kolom pekerjaan orang tua dari arsip RSUD, kami tidak mengarang isian, melainkan melabelinya secara transparan sebagai 'Tanpa Keterangan (Template RSUD)'. Selanjutnya, kami melakukan audit konsistensi kronologis dan menemukan anomali salah ketik pada slip loket fisik: berkas F044 tertulis lahir 2025 tetapi tanggal lapor loket terketik 2024, yang secara logika mustahil dilaporkan sebelum lahir. Kami memverifikasi silang dengan Surat Keterangan Lahir (SKL) dokter dan register arsip dinas, lalu mengoreksinya secara faktual. Seluruh berkas merupakan kohort resmi pelayanan loket Disdukcapil Natuna Tahun Pelaporan 2025 yang tervalidasi secara konsisten."*

---

#### 🎙️ PEMBICARA 4: Sarah Fauziyyah (NIM 2401020109)
* **Waktu Alokasi:** 2 Menit
* **Materi:** BAB III (Data Preprocessing Bagian 2), Eliminasi PII UU No. 27/2022, Rekayasa Fitur Hari, & Agregasi Spasial.
* **Contoh Naskah Bicara:**
  > *"Melanjutkan tahapan preprocessing, kami memastikan aspek kepatuhan hukum privasi penduduk sesuai **UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi**. Seluruh atribut identitas privat seperti nama lengkap orang tua, nama bayi, NIK, dan alamat rumah spesifik kami eliminasi dari tabel pemodelan dan disamarkan menjadi kode anonim B_001 hingga B_131."*
  > 
  > *"Selanjutnya, kami melakukan **Feature Engineering** dengan membentuk dua atribut numerik kontinu berbasis hari kalender presisi: `Durasi_Pelaporan_Hari` (selisih tanggal lapor dengan tanggal lahir) dan `Hari_Usia_Ortu` (usia orang tua saat persalinan). Terakhir, kami membangun dataset agregasi spasial 16 kecamatan berdasarkan persentase kelahiran tepat waktu dan median durasi keterlambatan, di mana kecamatan pemekaran baru seperti Pulau Tiga Barat dicatat 0 berkas secara jujur."*

---

#### 🎙️ PEMBICARA 5: Muhammad Agus Farhan (NIM 2401020111)
* **Waktu Alokasi:** 3 Menit
* **Materi:** BAB IV & BAB V (Modeling & Evaluasi), Algoritma K-Means, Perhitungan Langkah demi Langkah, dan Pembuktian Metrik Evaluasi.
* **Contoh Naskah Bicara:**
  > *"Terima kasih Sarah. Memasuki Bab IV dan Bab V, kami mengimplementasikan algoritma K-Means Clustering melalui dua model komplementer dengan detail perhitungan matematis manual menggunakan jarak Euclidean:"*
  > 
  > *"1. **Model 1 (Spasial Wilayah 16 Kecamatan):** Membagi Natuna menjadi 3 klaster kepatuhan: Cluster 0 (High-Compliance, n=2 yaitu Bunguran Tengah dan Pulau Laut), Cluster 1 (Moderate, n=7), dan Cluster 2 (High-Delay, n=7 di pulau-pulau 3T). Model ini sangat kokoh dengan **Silhouette Score 0.6377** dan **Davies-Bouldin Index 0.4710**."*
  > 
  > *"2. **Model 2 (K-Means Sosio-Ekonomi Pemohon Individu):** Memetakan 131 berkas dengan Sumbu X (Hari Usia Ortu) terhadap Sumbu Y (Hari Keterlambatan). Model ini menghasilkan Klaster 0 (Tepat Waktu & Balita Dini, n=56), Klaster 1 (Terlambat Sedang Balita-Anak, n=40), dan Klaster 2 (Terlambat Historis Dewasa SPTJM, n=35). Evaluasinya membuktikan **Silhouette Score 0.5524** dan **DBI 0.5924**, membuktikan bahwa struktur klaster sangat padat dan terpisah optimal."*

---

#### 🎙️ PEMBICARA 6 / PENUTUP: Ridho Ramadani E (bersama Farhan)
* **Waktu Alokasi:** 2 Menit (Bagian Akhir)
* **Materi:** BAB VI (Deployment Dashboard Interaktif, Kesimpulan, Rekomendasi Kebijakan, & Penutup).
* **Contoh Naskah Bicara:**
  > *"Sebagai wujud hilirisasi penerapan pada Bab VI, kami membangun purwarupa **Dashboard Interaktif Web Mandiri** menggunakan Leaflet.js dengan basemap Esri ArcGIS Online yang bebas watermark dan bebas hambatan akses lokal, serta Plotly.js yang interaktif dilengkapi garis elips klaster, centroid bintang kuning, dan anotasi sosio-ekonomi."*
  > 
  > *"Dari temuan riset ini, kami menyimpulkan bahwa keterlambatan akta kelahiran di Natuna didorong oleh dua faktor utama: isolasi geografis antarpulau dan rendahnya urgensi administratif sebelum anak masuk sekolah. Kami merekomendasikan 3 kebijakan strategis bagi Disdukcapil Natuna: pengadaan armada Kapal Pelayanan Keliling (Mobile Service Boat) terjadwal bagi 7 kecamatan Klaster 2, integrasi loket digital faskes rumah sakit bagi Klaster 0 dan 1, serta dispensasi pemutihan berkas SPTJM bagi warga dewasa di wilayah perbatasan. Demikian presentasi dari kelompok kami, kami membuka ruang diskusi dan masukan berharga dari Bapak/Ibu Dosen sekalian. Terima kasih."*

---

### PANDUAN MENJAWAB PERTANYAAN DOSEN (DEFENSE Q&A GUIDE)

#### Q1: "Mengapa memilih $K=3$ pada kedua model? Bagaimana pembuktian matematisnya?"
* **Penjawab yang Disarankan:** **Muhammad Agus Farhan**
* **Jawaban Kunci:**
  > *"Berdasarkan pengujian kurva Elbow (WCSS) dari K=2 hingga K=6, titik tekuk siku (*elbow point*) terdeteksi paling signifikan pada K=3, di mana penurunan inersia melandai setelah K=3. Selain itu, nilai koefisien Silhouette mencapai puncak tertinggi yang stabil di atas ambang batas 0.50 (0.6377 pada Model Spasial dan 0.5524 pada Model Individu), serta DBI terendah di bawah 0.80 (0.4710 dan 0.5924), yang membuktikan K=3 menghasilkan pemisahan klaster terbaik."*

#### Q2: "Mengapa ada pemohon yang keterlambatan pelaporannya mencapai 40 hingga 80 tahun? Apakah itu tidak merusak model?"
* **Penjawab yang Disarankan:** **Salma Nursafira** atau **Ridho Ramadani E**
* **Jawaban Kunci:**
  > *"Data tersebut bukan kesalahan input atau outlier acak yang harus dibuang, melainkan representasi fakta historis administrasi kependudukan di wilayah kepulauan 3T. Warga generasi terdahulu belum memiliki akta kelahiran saat lahir dan baru mengurusnya ketika dewasa untuk kebutuhan paspor, ibadah haji, pernikahan, atau pensiun dengan melampirkan instrumen yuridis SPTJM Kebenaran Kelahiran. Dengan model K-Means, data historis ini secara alamiah terisolasi ke dalam Klaster 2 (Terlambat Historis) sehingga tidak mengotori atau mendistorsi statistik kelahiran bayi baru di Klaster 0."*

#### Q3: "Mengapa Pulau Tiga Barat tercatat 0 berkas pada tabel spasial?"
* **Penjawab yang Disarankan:** **Monalisa Dwi Cantika** atau **Sarah Fauziyyah**
* **Jawaban Kunci:**
  > *"Kecamatan Pulau Tiga Barat merupakan kecamatan pemekaran administratif baru. Pada periode sampel 131 berkas loket yang terdokumentasi, warga di wilayah tersebut teradministrasi melalui kantor perwakilan kecamatan induk (Pulau Tiga). Berpegang teguh pada prinsip **Zero Data Fabrication**, kami tidak mengarang angka dummy 1 atau 2, melainkan mencatatnya 0 berkas secara jujur dan transparan."*

#### Q4: "Bagaimana perlindungan data pribadi pemohon dalam dashboard yang dapat diakses publik?"
* **Penjawab yang Disarankan:** **Sarah Fauziyyah**
* **Jawaban Kunci:**
  > *"Sesuai amanat UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi (PDP), seluruh atribut identitas personal seperti NIK, nomor KK, nama lengkap pemohon, dan nama bayi telah dieliminasi dan digantikan dengan kode indeks unik acak (B_001 s.d. B_131). Atribut yang ditampilkan dalam dashboard hanya mencakup data agregat demografi (usia orang tua dalam hari dan kelompok profesi) sehingga tidak ada kebocoran data privat warga."*

