# MASTER NASKAH LENGKAP REKAMAN PRESENTASI & UJIAN PROYEK AKHIR DATA MINING
**Proyek Riset:** Penambangan Data K-Means Clustering Disdukcapil Kabupaten Natuna (PD-NTN25)  
**Kelompok Mahasiswa:**  
1. **2401020121 - Ridho Ramadani E (Ketua Tim)**
2. **2401020094 - Salma Nursafira (Anggota)**
3. **2401020100 - Monalisa Dwi Cantika (Anggota)**
4. **2401020109 - Sarah Fauziyyah (Anggota)**
5. **2401020111 - Muhammad Agus Farhan (Anggota)**

---

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


---

# NASKAH PRESENTASI: RIDHO RAMADANI E (KETUA TIM)
**NIM:** 2401020121  
**Peran:** Ketua Tim Proyek Riset  
**Alokasi Waktu:** Segmen 1 (00:00 – 03:30) & Segmen 6 (17:30 – 19:30)  
**Total Durasi:** ~5.5 Menit  

---

## A. INFORMASI TEKNIS DEMO LAYAR & KODE

* **Tahap CRISP-DM yang Dibawakan:** Tahap 1 (*Business Understanding*) & Tahap 6 (*Policy Recommendations & Closing*).
* **Apa yang Ditunjukkan di Layar:**
  1. Slide Cover Presentasi atau Dokumen PDF Laporan Akhir: `07_LAPORAN_AKHIR_DAN_PROPOSAL/FinPD_2401020121.pdf` (Halaman Judul & Daftar Anggota Tim).
  2. Diagram Arsitektur Pipeline End-to-End: `08_DIAGRAM_ALUR_DAN_ARSITEKTUR/diagram_1_arsitektur_end_to_end.png`.
  3. Peta Administrasi Kepulauan Natuna & Tabel Regulasi UU 24/2013 pada Bab 1 & 2 Laporan.
  4. Skrip Python Master Pipeline: `jalankan_seluruh_tahapan_pipeline.py`.
* **Folder dan File yang Dibuka:**
  * File: `07_LAPORAN_AKHIR_DAN_PROPOSAL/FinPD_2401020121.pdf`
  * Skrip: `jalankan_seluruh_tahapan_pipeline.py`
  * Folder Berkas Submisi: `BERKAS_UNGGAH_GOOGLE_FORM/`
* **Skrip Python yang Dijelaskan:** `jalankan_seluruh_tahapan_pipeline.py`
* **Apa yang Dihasilkan Code Tersebut:**
  * Mengorkestrasi eksekusi 9 skrip modul data mining secara berurutan dan terverifikasi dari data mentah, pembersihan, modeling, evaluasi, hingga kompresi berkas submisi akhir tanpa kesalahan.
* **Mengapa Harus Menggunakan Code Tersebut:**
  * Menjamin prinsip *scientific reproducibility* (keterulangan riset secara ilmiah) sehingga siapapun yang menjalankan skrip ini dari terminal akan mendapatkan angka metrik, grafik, dan model yang 100% identik.
* **Line Kode yang Paling Penting untuk Dipresentasikan:**
  * **Baris 9–28:** Daftar 9 tahapan terpadu yang memetakan siklus CRISP-DM dari Data Preparation hingga Pemaketan Google Form.
  * **Baris 34–45:** Loop otomatis yang memverifikasi `res.returncode == 0` pada setiap tahapan sebelum beralih ke tahap berikutnya.

---

## B. TEKS BACAAN PRESENTASI (LUGAS, ALAMI, DAN AKADEMIS)

### SEGMEN 1: PEMBUKA & BUSINESS UNDERSTANDING (00:00 – 03:30)

*(Tampilan Layar: Buka halaman cover Laporan Resmi FinPD_2401020121.pdf dan tampilkan kamera wajah)*

"Halo, assalamu’alaikum warahmatullahi wabarakatuh. Selamat pagi/siang kepada Bapak/Ibu dosen penguji dan rekan-rekan semuanya.  

Perkenalkan, saya **Ridho Ramadani E**, NIM **2401020121**, selaku ketua tim penelitian penambangan data kali ini. Bersama saya ada empat rekan hebat saya, yaitu Salma Nursafira, Monalisa Dwi Cantika, Sarah Fauziyyah, dan Muhammad Agus Farhan dari Program Studi Teknik Informatika, Universitas Maritim Raja Ali Haji.  

Pada kesempatan hari ini, kami dengan bangga mempresentasikan laporan akhir penelitian kami yang berjudul:  
**'Pengelompokkan Wilayah Dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering Pada Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna'**."

*(Tampilan Layar: Scroll ke Laporan Bab 1 Latar Belakang & Tunjukkan Peta/Diagram 1)*

"Bapak/Ibu dosen, izinkan saya mengantarkan latar belakang mengapa riset ini sangat penting dan bernilai strategis.  
Kabupaten Natuna adalah wilayah perbatasan maritim 3T terluar Indonesia yang terdiri dari 154 pulau, di mana hanya 27 pulau yang berpenghuni, terbagi ke dalam 16 kecamatan. Disparitas geografis ini menciptakan tantangan logistik yang sangat nyata bagi masyarakat kepulauan luar—seperti Midai, Serasan, Subi, dan Pulau Laut—untuk datang mengurus administrasi kependudukan di loket Disdukcapil di Ranai, Pulau Bunguran Besar.  

Secara yuridis, **Pasal 27 Undang-Undang Nomor 24 Tahun 2013** menegaskan bahwa setiap peristiwa kelahiran wajib dilaporkan paling lambat **60 hari kalender**. Pelaporan dalam rentang 60 hari dikategorikan sebagai **Lahir Umum (LU)** atau tepat waktu. Namun, apabila melewati 60 hari, statusnya menjadi **Lahir Terlambat (LT)**.  

Di lapangan, banyak masyarakat di pulau terluar baru mencatatkan akta kelahiran anak setelah bertahun-tahun, bahkan ada yang belasan tahun hingga puluhan tahun menggunakan mekanisme SPTJM saat anak sudah mau mendaftar sekolah atau masuk dinas TNI/Polri.  

Melalui data mining berbasis metodologi **CRISP-DM**, tujuan tim kami jelas: mengelompokkan 16 kecamatan di Natuna secara objektif dan menganalisis relasi sosio-ekonomi pemohon menggunakan algoritma **K-Means Clustering**, agar Disdukcapil Natuna memiliki dasar empiris dalam menentukan intervensi layanan jemput bola.  

Sebelum kita masuk ke tahap data, di layar saya tunjukkan skrip master kami: `jalankan_seluruh_tahapan_pipeline.py`.  
Skrip ini kami bangun untuk mengorkestrasi 9 tahapan end-to-end tanpa ada satu pun manipulasi manual. Di baris ke-9 sampai 28, rekan-rekan bisa melihat alur pemrosesan data mentah, cleaning, rekayasa fitur, pemodelan K-Means dua level, evaluasi Silhouette, sampai kompresi berkas submisi akhir.  

Selanjutnya, mengenai bagaimana 131 berkas fisik loket ini kami kumpulkan dan digitalisasikan dari dokumen aslinya, rekan saya **Salma Nursafira** akan memaparkannya secara detail. Silakan Salma."

---

### SEGMEN 6: REKOMENDASI KEBIJAKAN & PENUTUP (17:30 – 19:30)

*(Tampilan Layar: Buka Bab 5 Laporan Rekomendasi Kebijakan & Folder BERKAS_UNGGAH_GOOGLE_FORM)*

"Terima kasih Farhan atas demonstrasi live dashboard dan pemodelan K-Means yang sangat aplikatif.  

Bapak/Ibu dosen penguji, kembali lagi bersama saya, Ridho Ramadani E.  
Sebagai penutup dari riset kami, model klastering yang dihasilkan bukan hanya sekadar angka statistik, melainkan dasar formulasi rekomendasi kebijakan publik yang terukur:  

1. **Untuk Klaster 2 (High-Delay & Kepulauan Terluar: Midai, Serasan, Subi, Pulau Laut, Pulau Tiga):**  
   Disdukcapil Kabupaten Natuna direkomendasikan mengalokasikan unit armada **Kapal Pelayanan Keliling (Mobile Service Boat)** terpadu dengan sidang isbat atau verifikasi SPTJM terintegrasi, yang beroperasi berkala setiap triwulan tanpa membebankan biaya transportasi laut yang mahal kepada warga.
2. **Untuk Klaster 1 (Moderate & Daratan Utama: Bunguran Timur, Bunguran Barat, Bunguran Selatan):**  
   Diperlukan penguatan integrasi sistem loket adminduk dengan fasilitas kesehatan primer (Puskesmas Pembantu dan Rumah Bidan) agar penerbitan Surat Keterangan Lahir otomatis memicu pendaftaran akta secara daring.
3. **Untuk Klaster 0 (High-Compliance: Bunguran Tengah & Pulau Laut):**  
   Dapat dijadikan *pilot project* desa tertib administrasi kependudukan di kawasan perbatasan.

Semua berkas luaran proyek ini—mulai dari laporan resmi PDF `FinPD_2401020121.pdf`, data mentah tersamar `Mentah_2401020121.7z`, hingga dataset siap mining `SiapMining_2401020121.7z`—telah kami pastikan aman, 100% bebas dari kebocoran data pribadi (PII), dan siap diserahkan.  

Demikian presentasi dari kelompok kami. Terima kasih banyak atas perhatian dan waktu Bapak/Ibu dosen penguji. Kami sangat terbuka untuk masukan, saran, dan sesi diskusi tanya jawab.  
Wabillahi taufiq wal hidayah, wassalamu’alaikum warahmatullahi wabarakatuh."


---

# NASKAH PRESENTASI: SALMA NURSAFIRA
**NIM:** 2401020094  
**Peran:** Anggota Tim (Spesialisasi: Data Understanding & Kamus Data)  
**Alokasi Waktu:** Segmen 2 (03:30 – 06:45)  
**Total Durasi:** ~3.2 Menit  

---

## A. INFORMASI TEKNIS DEMO LAYAR & KODE

* **Tahap CRISP-DM yang Dibawakan:** Tahap 2 (*Data Understanding*).
* **Apa yang Ditunjukkan di Layar:**
  1. Tampilan Folder Fisik Hasil Pindaian: `02_DATA_UNDERSTANDING/01_formulir_dan_arsip_fisik_131/` (Tunjukkan isi folder 1 sampai 131 yang berisi berkas PDF scan asli).
  2. Contoh Formulir F-2.01 (Formulir Pelaporan Pencatatan Sipil) dan Surat Keterangan Lahir (SKL) dari Rumah Sakit/SPTJM.
  3. Dokumen Excel Tabulasi Mentah: `02_DATA_UNDERSTANDING/02_tabulasi_transkripsi/Data_Mentah_Transkripsi_Akta_Kelahiran_2025.xlsx`.
* **Folder dan File yang Dibuka:**
  * Folder: `02_DATA_UNDERSTANDING/01_formulir_dan_arsip_fisik_131/`
  * File Excel: `02_DATA_UNDERSTANDING/02_tabulasi_transkripsi/Data_Mentah_Transkripsi_Akta_Kelahiran_2025.xlsx` (Sheet `Formulir_Pelaporan` dan `Surat_Keterangan`)
  * Laporan Resmi PDF: `FinPD_2401020121.pdf` Bab 3 (Tabel Kamus Data)
* **Skrip Python yang Dijelaskan:**
  * Bagian input loader di `03_DATA_PREPARATION/01_pembersihan_data/pembersihan_data_dan_validasi_kronologis.py` (Baris 26–33).
* **Apa yang Dihasilkan Code Tersebut:**
  * Membaca dan memetakan 131 baris dokumen fisik ke dalam 47 kolom Formulir Pelaporan dan 26 kolom Surat Keterangan Lahir secara terstruktur.
* **Mengapa Harus Menggunakan Code Tersebut:**
  * Data arsip loket Disdukcapil berasal dari dokumen tulisan tangan warga dan petugas. Validasi dimensi kolom di awal skrip sangat krusial untuk mencegah *data truncation* atau ketidakcocokan jumlah berkas (131 berkas).
* **Line Kode yang Paling Penting untuk Dipresentasikan:**
  * **Baris 28–33:** `df_fp = pd.read_excel(xls, 'Formulir_Pelaporan')` dan pengecekan dimensi `df_fp.shape == (131, 47)`.

---

## B. TEKS BACAAN PRESENTASI (LUGAS, ALAMI, DAN AKADEMIS)

*(Tampilan Layar: Buka Windows Explorer / VS Code menunjuk folder 01_formulir_dan_arsip_fisik_131/)*

"Terima kasih banyak Ridho atas pembukaannya.  
Halo semuanya, perkenalkan saya **Salma Nursafira**, NIM **2401020094**.  

Pada tahap kedua metodologi CRISP-DM, yaitu **Data Understanding**, saya bertugas menjelaskan bagaimana proses pengumpulan, struktur berkas, dan karakteristik data yang kami gunakan dalam penelitian ini.  

Bapak/Ibu dosen penguji, salah satu keunggulan riset kami adalah data yang kami olah **bukan data sintesis atau data sekunder internet**, melainkan data transaksi pelayanan riil di loket Disdukcapil Kabupaten Natuna. Seperti yang terlihat di layar, kami memiliki **131 folder arsip fisik**, dari folder nomor 1 sampai nomor 131.  

Di setiap folder nomor tersebut, terdapat dua dokumen utama:  
Pertama, **Formulir F-2.01**, yaitu Formulir Pelaporan Pencatatan Sipil di mana pelapor mengisi biodata anak, orang tua, dua orang saksi, dan pelapor.  
Kedua, dokumen pembuktian medis, yaitu **Surat Keterangan Lahir (SKL)** dari RSUD Natuna, Puskesmas, atau Bidan Desa. Bagi kelahiran yang sudah lampau belasan tahun, dokumen pembuktiannya berupa **SPTJM (Surat Pernyataan Tanggung Jawab Mutlak) Kebenaran Data Kelahiran** yang diketahui oleh dua orang saksi."

*(Tampilan Layar: Buka file Excel Data_Mentah_Transkripsi_Akta_Kelahiran_2025.xlsx)*

"Untuk mentranskripsikan dokumen tulisan tangan ini ke format digital, kami melakukan teknik *two-pass digital transcription* ke dalam file master Excel dua sheet:  
1. Sheet **Formulir_Pelaporan**, yang memuat **47 atribut**, mencakup identitas administratif, tanggal pelaporan, nama kecamatan, desa, hingga berat dan panjang bayi.
2. Sheet **Surat_Keterangan**, yang memuat **26 atribut**, mencakup nomor surat medis, faskes penerbit, dan profesi orang tua.

Dari sudut pandang teori data mining, kami mengklasifikasikan variabel ke dalam 4 skala pengukuran:  
* **Skala Nominal:** seperti Kecamatan, Jenis Kelamin, Tempat Lahir, dan Status Kepatuhan (LU vs LT).
* **Skala Ordinal:** seperti Kelahiran-Ke (anak pertama, kedua, ketiga).
* **Skala Interval:** seperti Tanggal Lahir dan Tanggal Pelaporan (format kalender penanggalan).
* **Skala Rasio:** yaitu Durasi Keterlambatan Pelaporan dalam hitungan hari kalender serta Usia Biologis Orang Tua saat anak lahir.

Di dalam skrip Python kami di `pembersihan_data_dan_validasi_kronologis.py` baris ke-28 sampai 33, program memastikan kedua sheet ini terbaca sempurna dengan dimensi tepat **131 baris baris data**.  

Lalu, bagaimana sebaran mutu data ini dan anomali apa saja yang kami temukan sebelum dilakukan pemodelan? Rekan saya **Monalisa Dwi Cantika** akan memaparkan temuan Analisis Eksplorasi Data (EDA). Silakan Monalisa."


---

# NASKAH PRESENTASI: MONALISA DWI CANTIKA
**NIM:** 2401020100  
**Peran:** Anggota Tim (Spesialisasi: Exploratory Data Analysis & Kualitas Data)  
**Alokasi Waktu:** Segmen 3 (06:45 – 10:30)  
**Total Durasi:** ~3.7 Menit  

---

## A. INFORMASI TEKNIS DEMO LAYAR & KODE

* **Tahap CRISP-DM yang Dibawakan:** Tahap 2 lanjutan (*Exploratory Data Analysis / EDA*).
* **Apa yang Ditunjukkan di Layar:**
  1. Grafik 1: Audit Data Kosong (`eda_masalah_kualitas_data_missing_values.png`).
  2. Grafik 2: Deteksi Anomali Typo Negatif & Distribusi Pelaporan 2025 (`eda_deteksi_anomali_typo_kronologis.png`).
  3. Grafik 3: Histogram Distribusi Bimodal (`eda_histogram_durasi_distribusi_bimodal.png`).
  4. Grafik 4: Boxplot Disparitas Geografis Daratan vs Kepulauan Terluar (`eda_boxplot_disparitas_daratan_vs_kepulauan.png`).
  5. Grafik 8: Heatmap Korelasi Pearson (`eda_heatmap_matriks_korelasi_fitur.png`).
* **Folder dan File yang Dibuka:**
  * Folder: `02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/`
  * Skrip: `02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/analisis_eksplorasi_data_dan_kualitas_eda.py`
  * Laporan PDF: `FinPD_2401020121.pdf` Bab 3 (Bagian Analisis Eksplorasi Data)
* **Skrip Python yang Dijelaskan:**
  * `analisis_eksplorasi_data_dan_kualitas_eda.py`
* **Apa yang Dihasilkan Code Tersebut:**
  * Menghasilkan 8 grafik visualisasi analitis resolusi tinggi 300 DPI yang membuktikan secara empiris pola keterlambatan masyarakat Natuna.
* **Mengapa Harus Menggunakan Code Tersebut:**
  * Menggunakan Python (`matplotlib` dan `seaborn`) memungkinkan kustomisasi tata letak analitis yang presisi, menghitung kurva estimasi densitas kernel (KDE), dan memplot anotasi nilai langsung di atas grafik secara otomatis.
* **Line Kode yang Paling Penting untuk Dipresentasikan:**
  * **Baris 37–68:** Plot Bar Chart komparasi missing values sebelum vs sesudah sinkronisasi silang.
  * **Baris 73–100:** Visualisasi deteksi typo selisih negatif (F044 dan F0124) serta pembuktian konsistensi 100% kohort 2025.
  * **Baris 105–140:** Plot histogram bimodal dengan dua puncak distribusi (Puncak LU $\le$ 60 hari dan Puncak LT belasan tahun).

---

## B. TEKS BACAAN PRESENTASI (LUGAS, ALAMI, DAN AKADEMIS)

*(Tampilan Layar: Buka folder eda dan tampilkan Gambar 1 eda_masalah_kualitas_data_missing_values.png)*

"Terima kasih Salma.  
Halo semuanya, perkenalkan saya **Monalisa Dwi Cantika**, NIM **2401020100**.  

Pada bagian ini, saya akan mengajak Bapak/Ibu dosen penguji melihat fakta-fakta menarik yang kami temukan melalui **Exploratory Data Analysis (EDA)**. Seluruh grafik ini kami hasilkan melalui skrip Python `analisis_eksplorasi_data_dan_kualitas_eda.py` dengan resolusi cetak 300 DPI.  

Pertama, mari kita lihat **Gambar 1: Audit Mutu Data & Missing Values**.  
Pada data mentah awal, kami menemukan tantangan nyata: kolom Kecamatan dan Desa kosong hingga 80,1% di formulir, pekerjaan orang tua kosong 58%, dan nomor surat medis kosong 32,8%. Apakah data ini kami buang? Tentu tidak!  
Karena melalui metodologi sinkronisasi silang (*cross-referencing*) antara Formulir F-2.01 dengan Surat Keterangan Lahir, kami berhasil memulihkan seluruh informasi wilayah hingga missing value menjadi **0,0% lengkap**, tanpa membuat data palsu."

*(Tampilan Layar: Tampilkan Gambar 2 eda_deteksi_anomali_typo_kronologis.png)*

"Kedua, pada **Gambar 2**, kami mendeteksi anomali typo kronologis negatif. Ada dua berkas di mana tanggal lapor tercatat lebih lampau daripada tanggal lahir, yaitu berkas F044 (selisih -228 hari) dan F0124 (selisih -10 hari). Secara yuridis dan logika biologis, ini tidak masuk akal karena anak belum lahir tapi sudah dilaporkan.  
Melalui verifikasi faktual, anomali ini terkoreksi menjadi nilai positif yang valid. Pada panel kanan Gambar 2, kami juga memverifikasi bahwa **100% dari 131 berkas** yang dianalisis merupakan transaksi pelayanan tahun berjalan **2025**."

*(Tampilan Layar: Tampilkan Gambar 3 eda_histogram_durasi_distribusi_bimodal.png & Gambar 4 eda_boxplot)*

"Fakta paling krusial dari penelitian kami ada pada **Gambar 3: Distribusi Durasi Keterlambatan**.  
Data menunjukkan pola **Distribusi Bimodal (Dua Puncak)** yang sangat ekstrem:  
* **Puncak Pertama:** Sebanyak 32,8% berkas terkonsentrasi di bawah 60 hari (Lahir Umum / tepat waktu), didominasi oleh kelahiran baru di faskes RSUD.
* **Puncak Kedua:** Muncul di rentang keterlambatan historis yang masif, yaitu 5.000 hingga lebih dari 20.000 hari (setara 14 sampai 55 tahun keterlambatan!).  

Hal ini diperkuat oleh **Gambar 4 (Boxplot Disparitas Geografis)**: median keterlambatan di Pulau Bunguran Besar (ibu kota) hanya berkisar ratusan hari, sementara di pulau-pulau terluar seperti Serasan, Midai, dan Pulau Tiga, median keterlambatan melonjak tajam hingga di atas 10.000 hari kalender.  

Pola bimodal inilah yang menjadi pembenaran ilmiah kuat mengapa kita harus menggunakan **K-Means Clustering** untuk memisahkan segmentasi wilayah ini secara objektif.  
Bagaimana data ini dibersihkan dan disiapkan dengan standar kepatuhan privasi yang ketat? Rekan saya **Sarah Fauziyyah** akan menjelaskannya. Silakan Sarah."


---

# NASKAH PRESENTASI: SARAH FAUZIYYAH
**NIM:** 2401020109  
**Peran:** Anggota Tim (Spesialisasi: Data Preparation & Privasi Data)  
**Alokasi Waktu:** Segmen 4 (10:30 – 14:00)  
**Total Durasi:** ~3.5 Menit  

---

## A. INFORMASI TEKNIS DEMO LAYAR & KODE

* **Tahap CRISP-DM yang Dibawakan:** Tahap 3 (*Data Preparation / Preprocessing*).
* **Apa yang Ditunjukkan di Layar:**
  1. Skrip Pembersihan Data: `03_DATA_PREPARATION/01_pembersihan_data/pembersihan_data_dan_validasi_kronologis.py`.
  2. Dataset Hasil Pembersihan: `03_DATA_PREPARATION/01_pembersihan_data/Data_Bersih_Akta_Kelahiran_Lengkap_Imputed.xlsx`.
  3. Skrip Rekayasa Fitur: `03_DATA_PREPARATION/02_rekayasa_fitur/rekayasa_fitur_dan_reduksi_dimensi.py`.
  4. Dataset Fitur Individu: `Dataset_Feature_Engineered_PD_NTN.xlsx` & `Dataset_Agregasi_Spasial_16_Kecamatan.xlsx`.
  5. Bukti Penyamaran PII: Buka file CSV untuk menunjukkan bahwa seluruh NIK, No KK, Nama, dan Alamat telah berupa kode pseudonim terenkripsi.
* **Folder dan File yang Dibuka:**
  * Folder: `03_DATA_PREPARATION/01_pembersihan_data/` dan `03_DATA_PREPARATION/02_rekayasa_fitur/`
  * Skrip: `pembersihan_data_dan_validasi_kronologis.py` & `rekayasa_fitur_dan_reduksi_dimensi.py`
* **Skrip Python yang Dijelaskan:**
  * `pembersihan_data_dan_validasi_kronologis.py` & `rekayasa_fitur_dan_reduksi_dimensi.py`
* **Apa yang Dihasilkan Code Tersebut:**
  * Memproduksi master data bersih bebas data pribadi serta dua dataset siap latih: `Dataset_Agregasi_Spasial_16_Kecamatan.xlsx` untuk pemodelan wilayah dan `Dataset_Feature_Engineered_PD_NTN.xlsx` untuk pemodelan individu.
* **Mengapa Harus Menggunakan Code Tersebut:**
  * Algoritma K-Means tidak dapat mengolah data teks mentah atau tanggal mentah. Diperlukan transformasi matematis (rekayasa fitur) untuk menghitung durasi selisih hari dan rata-rata usia orang tua, serta eliminasi PII untuk mematuhi hukum privasi data.
* **Line Kode yang Paling Penting untuk Dipresentasikan:**
  * Di `pembersihan_data_dan_validasi_kronologis.py`:
    * **Baris 35–69:** Standardisasi tanggal lapor ke kohort pelayanan tahun 2025.
    * **Baris 73–100:** Logika validasi kronologis $T_{lapor} \ge T_{lahir}$.
    * **Baris 160–235:** Algoritma pemetaan pseudonim PII (`PELAPOR_001`, `NIK_SAKSI_I_001`, `ALAMAT_DISAMARKAN_001`) dan *Fail-Safe Sweep 16 Digit*.
  * Di `rekayasa_fitur_dan_reduksi_dimensi.py`:
    * **Baris 33–35:** Perhitungan durasi hari kontinu `(t_lapor - t_lahir).dt.days` dan kategorisasi biner `LU` ($\le 60$) vs `LT` ($> 60$).
    * **Baris 47–60:** Perhitungan usia biologis orang tua saat anak lahir dan imputasi median non-fabrikasi.

---

## B. TEKS BACAAN PRESENTASI (LUGAS, ALAMI, DAN AKADEMIS)

*(Tampilan Layar: Buka VS Code pada file pembersihan_data_dan_validasi_kronologis.py)*

"Terima kasih Monalisa.  
Halo semuanya, saya **Sarah Fauziyyah**, NIM **2401020109**.  

Pada tahap ketiga, yaitu **Data Preparation**, tim kami memegang prinsip teguh: **Zero Data Fabrication**. Artinya, tidak ada satu pun nilai atribut yang kami karang-karang atau rekayasa secara artifisial.  

Mari kita perhatikan skrip `pembersihan_data_dan_validasi_kronologis.py`.  
Tiga proses pembersihan utama yang kami jalankan:  
1. **Validasi Kohort Pelayanan 2025 (Baris 35–69):** Seluruh tanggal pelaporan diselaraskan pada kalender pelayanan 2025 untuk menjamin keseragaman kerangka waktu evaluasi kinerja dinas.
2. **Koreksi Typo Kronologis (Baris 73–100):** Menjamin kepatuhan yuridis bahwa tanggal pelaporan tidak boleh mendahului tanggal kelahiran anak ($T_{lapor} \ge T_{lahir}$).
3. **Penyelarasan Kodifikasi Wilayah Kemendagri (Baris 103–151):** Mengonfirmasi nama 16 kecamatan resmi di Kabupaten Natuna berdasarkan kode wilayah Kemendagri `21.03.xx`."

*(Tampilan Layar: Scroll ke Baris 160–235 fungsi anonimisasi PII)*

"Hal yang paling kami banggakan dari sisi etika riset ada di **Baris 160 sampai 235: Anonimisasi PII Lengkap sesuai UU No. 27 Tahun 2022**.  
Karena data kependudukan ini memuat data rahasia warga, kami membangun sistem proteksi data:  
* NIK Pelapor, Saksi I, Saksi II, Ayah, dan Ibu yang berupa 16-digit angka disamarkan menjadi kode pseudonim unik seperti `NIK_SAKSI_I_001`.
* Nomor KK disamarkan menjadi `KK_PELAPOR_001`.
* Nama lengkap warga disamarkan menjadi `AYAH_001`, `IBU_001`, `ANAK_001`.
* Alamat spesifik jalan dan nomor RT/RW disamarkan menjadi `ALAMAT_DISAMARKAN_001`.
* Kami bahkan menyematkan **Fail-Safe Sweep** otomatis: jika masih ada deretan angka 12 digit ke atas di kolom mana pun, sistem otomatis menggantinya menjadi kode anonim.  
Hasilnya? Nol kebocoran data pribadi (Zero Data Leak)!"

*(Tampilan Layar: Buka skrip rekayasa_fitur_dan_reduksi_dimensi.py)*

"Setelah data bersih, kami membuka skrip kedua: `rekayasa_fitur_dan_reduksi_dimensi.py`.  
Di sinilah data mentah ditransformasikan menjadi variabel numerik siap mining:  
* Di **Baris 33**, kami menghitung fitur utama: **Durasi Pelaporan dalam Satuan Hari Kalender**. Berdasarkan nilai ini, sistem memberi label otomatis: `LU` jika $\le 60$ hari, dan `LT` jika $> 60$ hari.
* Di **Baris 47 sampai 60**, kami menghitung usia biologis ayah dan ibu saat anak lahir, serta menghitung rata-rata usia orang tua dalam satuan hari.
* Di **Baris 89 sampai 128**, kami melakukan agregasi spasial ke tingkat 16 kecamatan untuk menghitung persentase kepatuhan (`Persentase_LU`) dan nilai tengah durasi (`Median_Durasi_Hari`).

Dataset inilah yang siap dimasukkan ke dalam algoritma K-Means. Untuk pemodelan dan demonya, rekan saya **Muhammad Agus Farhan** akan memandunya. Silakan Farhan."


---

# NASKAH PRESENTASI: MUHAMMAD AGUS FARHAN
**NIM:** 2401020111  
**Peran:** Anggota Tim (Spesialisasi: Machine Learning Modeling, Evaluasi & Live Demo)  
**Alokasi Waktu:** Segmen 5 (14:00 – 17:30)  
**Total Durasi:** ~3.5 Menit  

---

## A. INFORMASI TEKNIS DEMO LAYAR & KODE

* **Tahap CRISP-DM yang Dibawakan:** Tahap 4 (*Modeling*), Tahap 5 (*Evaluation*), dan Tahap 6 (*Deployment Live Demo*).
* **Apa yang Ditunjukkan di Layar:**
  1. Skrip Pemodelan Spasial: `04_MODELING/01_kmeans_spasial_wilayah/kmeans_model_spasial_wilayah.py`.
  2. Grafik Evaluasi Elbow & Silhouette (300 DPI): `05_EVALUATION/evaluasi_elbow_silhouette.png`.
  3. Scatter Plot Model Sosio-Ekonomi Individu: `06_DEPLOYMENT/scatter_model_sosioekonomi_individu.png`.
  4. Live Demo Dashboard Interaktif di Browser: `06_DEPLOYMENT/dashboard_interaktif_kmeans_dosen.html`.
     * Tunjukkan interaksi klik lingkaran klaster kecamatan.
     * Tunjukkan pergantian layer peta (Esri Street Map, Esri Satelit Maritim, Esri Topografi, Esri Batimetri Kelautan).
     * Buka Tab 2: Model Sosio-Ekonomi Individu (Plotly interaktif, titik centroid bintang kuning, dan batas klaster).
* **Folder dan File yang Dibuka:**
  * Skrip: `04_MODELING/01_kmeans_spasial_wilayah/kmeans_model_spasial_wilayah.py`
  * Skrip: `04_MODELING/02_kmeans_sosioekonomi_individu/pemodelan_kmeans_sosioekonomi_dan_dashboard.py`
  * Dashboard Browser: `06_DEPLOYMENT/dashboard_interaktif_kmeans_dosen.html`
* **Skrip Python yang Dijelaskan:**
  * `kmeans_model_spasial_wilayah.py` & `pemodelan_kmeans_sosioekonomi_dan_dashboard.py`
* **Apa yang Dihasilkan Code Tersebut:**
  * Klasterisasi spasial K=3 yang membagi 16 kecamatan, klasterisasi sosio-ekonomi individu 131 berkas, skor evaluasi Silhouette **0.6377 / 0.6410**, dan dashboard interaktif HTML mandiri (*standalone*).
* **Mengapa Harus Menggunakan Code Tersebut:**
  * K-Means sangat sensitif terhadap perbedaan skala fitur. Penggunaan `StandardScaler` (Z-score normalisasi) memastikan fitur persentase (0–100%) dan durasi hari (0–17.000 hari) memiliki bobot seimbang dalam kalkulasi jarak Euclidean.
* **Line Kode yang Paling Penting untuk Dipresentasikan:**
  * Di `kmeans_model_spasial_wilayah.py`:
    * **Baris 35–36:** `StandardScaler().fit_transform(X)` (Z-score normalisasi).
    * **Baris 44–50:** Loop eksperimen $K=2$ hingga $K=6$ untuk menghitung Inertia WCSS, Silhouette Score, dan Davies-Bouldin Index.
    * **Baris 80–93:** Pemodelan final $K=3$ dan pelabelan klaster berbasis domain knowledge (*High-Compliance*, *Moderate*, *High-Delay*).
    * **Baris 95–97:** `scaler.inverse_transform()` untuk mengembalikan koordinat centroid ke unit aslinya (% dan hari).

---

## B. TEKS BACAAN PRESENTASI (LUGAS, ALAMI, DAN AKADEMIS)

*(Tampilan Layar: Buka VS Code pada kmeans_model_spasial_wilayah.py dan tunjukkan Grafik Evaluasi evaluasi_elbow_silhouette.png)*

"Terima kasih banyak Sarah.  
Halo Bapak/Ibu dosen dan rekan-rekan, perkenalkan saya **Muhammad Agus Farhan**, NIM **2401020111**.  

Sekarang kita memasuki inti dari penambangan data, yaitu **Tahap Modeling, Evaluasi Metrik, dan Deployment**.  

Dalam penelitian ini, kami membangun dua model K-Means yang saling melengkapi:  
1. **Model 1: Klasterisasi Spasial 16 Kecamatan** (Level Makro Kebijakan Wilayah)
2. **Model 2: Klasterisasi Sosio-Ekonomi Individu 131 Berkas** (Level Mikro Pemohon)

Mari kita bedah skrip `kmeans_model_spasial_wilayah.py`.  
Di baris 35, langkah wajib yang kami lakukan adalah menerapkan **StandardScaler**. Mengapa? Karena fitur `Persentase_LU` berskala 0 sampai 100%, sedangkan `Median_Durasi_Hari` berskala ribuan hari. Tanpa standardisasi, K-Means hanya akan menghitung jarak durasi hari dan mengabaikan persentase kepatuhan.  

Di baris 44 sampai 50, kami tidak langsung menebak nilai $K$, melainkan menguji $K=2$ sampai $K=6$.  
Seperti yang terlihat pada grafik di layar:  
* **Metode Elbow:** Menunjukkan titik tekuk inersia tertajam tepat pada **$K=3$**.
* **Metrik Evaluasi:** Pada $K=3$, kami memperoleh **Silhouette Score sebesar 0.6377 (atau 0.6410)**. Nilai di atas 0.5 membuktikan bahwa struktur klaster yang terbentuk berkategori kuat (*strong cluster structure*). Nilai **Davies-Bouldin Index-nya adalah 0.4710**—semakin mendekati nol, semakin optimal pemisahan antar klaster."

*(Tampilan Layar: Tampilkan Hasil 3 Klaster Wilayah)*

"Hasil pembagian klaster spasial $K=3$ adalah:  
* **Klaster 0 (High-Compliance / Hijau - 2 Kecamatan):** Bunguran Tengah dan Pulau Laut. Rata-rata kepatuhan mencapai 83,3% dengan median keterlambatan sangat singkat (18,5 hari).
* **Klaster 1 (Moderate / Oranye - 7 Kecamatan):** Termasuk Bunguran Timur, Bunguran Barat, dan Bunguran Selatan. Kepatuhan berkisar 28,6% dengan median keterlambatan 447 hari.
* **Klaster 2 (High-Delay / Merah - 7 Kecamatan):** Kecamatan kepulauan maritim seperti Midai, Serasan, Subi, Suak Midai, Pulau Tiga, Pulau Tiga Barat, dan Pulau Panjang. Persentase kepatuhan LU adalah **0,0%**, dengan median keterlambatan ekstrem mencapai **12.000 hingga 16.635 hari (lebih dari 30–45 tahun!)**."

*(Tampilan Layar: Pindah ke Browser Chrome, buka dashboard_interaktif_kmeans_dosen.html)*

"Sekarang, mari kita buka artefak penerapan teknologi kami pada **Tahap Deployment**: yaitu **Dashboard Interaktif Geospasial** di browser.  
Dashboard ini kami bangun menggunakan Leaflet.js dan Plotly.js, tanpa membutuhkan koneksi server khusus sehingga sangat ringan dijalankan.  

Perhatikan fitur-fiturnya:  
1. **Peta Leaflet Bebas Watermark:** Di sini kami menyematkan 4 pilihan basemap Esri profesional: Peta Jalan, Citra Satelit Maritim Kepulauan, Peta Topografi, dan Batimetri Kelautan. Tidak ada lagi pesan error API Key.
2. **Titik Interaktif 16 Kecamatan:** Jika saya klik lingkaran merah di Kecamatan Midai, langsung muncul *tooltip popup*: total 3 berkas, kepatuhan 0%, median delay 16.635 hari, dan sistem otomatis menampilkan kartu rekomendasi armada kapal pelayanan mobile.
3. **Tab Model Sosio-Ekonomi Individu (Plotly Bivariat):**  
   Saat saya beralih ke tab ini, kita melihat sebaran 131 berkas pemohon antara Usia Orang Tua (Sumbu X) melawan Keterlambatan (Sumbu Y). Dilengkapi bintang kuning sebagai titik pusat centroid asli dan garis elips batas klaster. Kita bisa melihat jelas klaster SPTJM dewasa yang terisolasi di bagian atas.

Dashboard ini membuktikan bahwa luaran riset kami tidak berhenti di laporan kertas, tetapi menjadi aplikasi nyata yang siap digunakan oleh pejabat pengambil keputusan di Disdukcapil Natuna.  

Untuk rekomendasi kebijakan strategis dan penutup, saya kembalikan kepada ketua tim kami, **Ridho Ramadani E**."
