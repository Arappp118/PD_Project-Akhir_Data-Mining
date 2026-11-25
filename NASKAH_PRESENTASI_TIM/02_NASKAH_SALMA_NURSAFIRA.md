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
