# PANDUAN REKAMAN VIDEO PRESENTASI YOUTUBE & REPOSITORI GITHUB
**Proyek Akhir Penambangan Data (PD-NTN25) Ganjil 2026/2027**  
**Universitas Maritim Raja Ali Haji (UMRAH)**

---

## 1. PANDUAN PENGUNGGAHAN VIDEO YOUTUBE (PENGGANTI PRESENTASI LANGSUNG)

Sesuai **Panduan Unggah Laporan Akhir**, video YouTube berfungsi sebagai pengganti ujian/presentasi langsung tatap muka.

### A. Judul Video YouTube (Wajib Sama dengan Judul Laporan):
```text
Final Project – Pengelompokkan Wilayah Dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering Pada Disdukcapil Kabupaten Natuna
```

### B. Format Teks Deskripsi Video YouTube (Wajib Disalin Persis):
```text
© Project Data Mining Course 2026
Universitas Maritim Raja Ali Haji
2401020121 - Ridho Ramadani E
2401020094 - Salma Nursafira
2401020100 - Monalisa Dwi Cantika
2401020109 - Sarah Fauziyyah
2401020111 - Muhammad Agus Farhan

Video Segment:
00:00 Pendahuluan & Profil Mitra Disdukcapil Kabupaten Natuna
01:45 Business Understanding: Regulasi UU 24/2013 & UU PDP 27/2022
03:30 Data Understanding & Audit 131 Berkas Fisik Loket 2025
05:15 Analisis Eksplorasi Data (EDA) & Deteksi Distribusi Bimodal
07:30 Data Preparation: Protokol Zero Fabrication & Eliminasi PII
09:20 Formulasi Matematis K-Means & Standardisasi Z-Score
11:00 Model 1: Segmentasi Spasial 16 Kecamatan Natuna
13:10 Model 2: Model Sosio-Ekonomi Pemohon Individu (Usia Ortu vs Delay)
14:50 Evaluasi Model: Silhouette Score (0.6410) & Davies-Bouldin
16:30 Demonstrasi Dashboard Interaktif (Peta Leaflet & Scatter)
18:15 Rekomendasi Kebijakan: Kapal Pelayanan Keliling (Mobile Boat)
19:30 Kesimpulan & Penutup
```

### C. Alur Pembagian Bicara Anggota Tim (15–20 Menit):
> **CATATAN NASKAH LENGKAP:** Naskah bacaan kata demi kata, panduan layar, dan baris kode Python yang dijelaskan per anggota telah tersedia di folder:  
> - Di dalam proyek: `NASKAH_PRESENTASI_TIM/`  
> - Di luar proyek: `../NASKAH_PRESENTASI_TIM_PD_NTN25/`  

1. **Ridho Ramadani E (Ketua Tim):**
   - Pembuka, Latar Belakang Mitra Disdukcapil Natuna, Masalah Disparitas Geografis Kepulauan 3T, Regulasi batas 60 hari LU vs LT, dan Kesimpulan/Rekomendasi Kebijakan Kapal Pelayanan Keliling (Buka file: `01_NASKAH_RIDHO_RAMADANI_E_KETUA.md`).
2. **Salma Nursafira:**
   - Data Understanding: Mekanisme pengumpulan 131 folder berkas fisik loket (Formulir F-2.01, SKL Faskes, SPTJM), jenis data, dan skala pengukuran nominal/rasio (Buka file: `02_NASKAH_SALMA_NURSAFIRA.md`).
3. **Monalisa Dwi Cantika:**
   - Analisis Eksplorasi Data (EDA): Menjelaskan temuan distribusi bimodal, perbandingan pulau utama vs pulau terluar, tren pengajuan bulanan, dan audit non-fabrikasi (Buka file: `03_NASKAH_MONALISA_DWI_CANTIKA.md`).
4. **Sarah Fauziyyah:**
   - Data Preprocessing: Penanganan missing value tanpa rekayasa data, verifikasi faktual typo kronologis (F044 & F0124), validasi kohort pelayanan 2025, dan eliminasi data pribadi PII UU PDP (Buka file: `04_NASKAH_SARAH_FAUZIYYAH.md`).
5. **Muhammad Agus Farhan:**
   - Modeling & Evaluasi: Menjelaskan rumus jarak Euclidean, standardisasi Z-score, hasil clustering Model 1 Spasial 16 Kecamatan, Model 2 Sosio-Ekonomi Individu, skor Silhouette (0.6410 & 0.5533), dan live demo Dashboard Interaktif Leaflet (Buka file: `05_NASKAH_MUHAMMAD_AGUS_FARHAN.md`).

---

## 2. PANDUAN REPOSITORI GITHUB (KODE PUBLIK)

### Perintah Git untuk Push Repositori ke GitHub:
```bash
# Inisialisasi git di folder repositori
git init
git branch -M main

# Tambahkan seluruh file proyek
git add .
git commit -m "feat: complete final project data mining PD-NTN25 Disdukcapil Natuna"

# Tambahkan remote repository publik Anda (ganti URL dengan repo Anda di GitHub)
git remote add origin https://github.com/USERNAME/PD-NTN25-FINAL.git

# Push ke branch main
git push -u origin main
```

---

## 3. CHECKLIST KELENGKAPAN UNGGAH GOOGLE FORM
Tautan Google Form Resmi: **https://forms.gle/W4WMb4yNMmb2Qsgn8**  
Batas Akhir Pengunggahan: **Jumat, 20 November 2026**

- [x] **1. File Dokumen Laporan Akhir (PDF):** `FinPD_2401020121.pdf` (Lokasi: `BERKAS_UNGGAH_GOOGLE_FORM/FinPD_2401020121.pdf`)
- [x] **2. File Data Mentah Tersamar (.7z):** `Mentah_2401020121.7z` (Lokasi: `BERKAS_UNGGAH_GOOGLE_FORM/Mentah_2401020121.7z`)
- [x] **3. File Data Siap Mining (.7z):** `SiapMining_2401020121.7z` (Lokasi: `BERKAS_UNGGAH_GOOGLE_FORM/SiapMining_2401020121.7z`)
- [ ] **4. Tautan GitHub Publik:** `https://github.com/USERNAME/PD-NTN25-FINAL`
- [ ] **5. Tautan Video YouTube:** `https://youtu.be/...`

