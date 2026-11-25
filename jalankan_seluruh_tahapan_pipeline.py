#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

steps = [
    ("Tahap 1 (Data Preparation): Pembersihan Data & Validasi Kohort Pelayanan 2025", 
     os.path.join(BASE_DIR, "03_DATA_PREPARATION", "01_pembersihan_data", "pembersihan_data_dan_validasi_kronologis.py")),
    ("Tahap 2 (Data Preparation): Rekayasa Fitur & Reduksi Dimensi PII",
     os.path.join(BASE_DIR, "03_DATA_PREPARATION", "02_rekayasa_fitur", "rekayasa_fitur_dan_reduksi_dimensi.py")),
    ("Tahap 3 (Modeling Spasial): Pemodelan K-Means Spasial 16 Kecamatan",
     os.path.join(BASE_DIR, "04_MODELING", "01_kmeans_spasial_wilayah", "kmeans_model_spasial_wilayah.py")),
    ("Tahap 4 (Modeling Sosio-Ekonomi): Pemodelan K-Means Sosio-Ekonomi Pemohon Individu",
     os.path.join(BASE_DIR, "04_MODELING", "02_kmeans_sosioekonomi_individu", "pemodelan_kmeans_sosioekonomi_dan_dashboard.py")),
    ("Tahap 5 (Data Understanding): Analisis Eksplorasi Data 8 Visualisasi EDA",
     os.path.join(BASE_DIR, "02_DATA_UNDERSTANDING", "03_eksplorasi_data_eda", "analisis_eksplorasi_data_dan_kualitas_eda.py")),
    ("Tahap 6 (Deployment): Generator Dashboard Interaktif Geospasial Leaflet",
     os.path.join(BASE_DIR, "06_DEPLOYMENT", "generate_dashboard.py")),
    ("Tahap 7 (Laporan Akhir): Generator Laporan Akhir RTM (Word DOCX & PDF FinPD)",
     os.path.join(BASE_DIR, "07_LAPORAN_AKHIR_DAN_PROPOSAL", "build_final_reports.py")),
    ("Tahap 8 (Submisi Google Form): Pemaketan Berkas Arsip Unggah (.7z & PDF)",
     os.path.join(BASE_DIR, "07_LAPORAN_AKHIR_DAN_PROPOSAL", "paketkan_berkas_google_form.py")),
    ("Tahap 9 (Diagram & Arsitektur): Generator 6 Diagram Alur & Arsitektur Sistem",
     os.path.join(BASE_DIR, "08_DIAGRAM_ALUR_DAN_ARSITEKTUR", "generate_diagrams.py"))
]

print("======================================================================")
print("  EKSEKUSI MASTER PIPELINE DATA MINING PD-NTN25-FINAL (TAHUN 2025)   ")
print("======================================================================")

for name, script in steps:
    print(f"\n[RUNNING] {name}...")
    res = subprocess.run([sys.executable, script], capture_output=True, text=True)
    if res.returncode == 0:
        print(f"[SUCCESS] {name}")
        for l in res.stdout.strip().split('\n')[-3:]:
            if l.strip():
                print(f"   -> {l.strip()}")
    else:
        print(f"[FAILED]  {name}")
        print("   Error:", res.stderr)
        sys.exit(1)

print("\n======================================================================")
print("  SELURUH TAHAPAN PIPELINE TELAH TUNTAS DAN BERHASIL 100%!          ")
print("======================================================================")
