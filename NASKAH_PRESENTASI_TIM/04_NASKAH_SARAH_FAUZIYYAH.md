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
