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
