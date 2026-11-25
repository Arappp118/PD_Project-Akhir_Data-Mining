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
