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
