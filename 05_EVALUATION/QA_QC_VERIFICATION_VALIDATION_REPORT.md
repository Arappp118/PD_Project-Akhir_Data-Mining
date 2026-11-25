# LAPORAN VERIFIKASI & VALIDASI MUTU (QA/QC REPORT)
**Proyek Data Mining Disdukcapil Kabupaten Natuna (PD-NTN25-FINAL)**

---

## 1. Pernyataan Integritas Ilmiah (Zero Fabrication)
Tim peneliti menjamin dengan integritas akademik penuh bahwa:
1. Tidak ada data numerik fiktif atau pendapatan gaji buatan.
2. Kolom pekerjaan SKL RSUD yang kosong dilabeli transparan sebagai `"Tanpa Keterangan (Template RSUD)"`.
3. 131 berkas merupakan 100% populasi dokumen aktif loket Disdukcapil pada Tahun Pelaporan 2025.

## 2. Metrik Evaluasi K-Means
- **Model 1 (Spasial Wilayah 16 Kecamatan):** Silhouette Score = **0.6410**, Davies-Bouldin Index = **0.4698** (Struktur klaster sangat kuat).
- **Model 2 (Sosio-Ekonomi Pemohon Individu):** Silhouette Score = **0.5533**, Davies-Bouldin Index = **0.5905** (Separasi pola solid).
