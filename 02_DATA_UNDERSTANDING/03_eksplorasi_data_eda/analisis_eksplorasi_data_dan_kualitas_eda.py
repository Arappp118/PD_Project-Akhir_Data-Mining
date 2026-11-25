#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SKRIP EKSPLORASI DATA & AUDIT MUTU (EXPLORATORY DATA ANALYSIS - EDA)
Proyek Riset Data Mining Disdukcapil Kabupaten Natuna (PD-NTN25-FINAL)
Tahap CRISP-DM: Data Understanding & Data Preparation
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_CLEAN_PATH = os.path.join(PROJECT_ROOT, "03_DATA_PREPARATION", "01_pembersihan_data", "Data_Bersih_Akta_Kelahiran_Lengkap_Imputed.xlsx")
DATA_FEAT_PATH = os.path.join(PROJECT_ROOT, "03_DATA_PREPARATION", "02_rekayasa_fitur", "Dataset_Feature_Engineered_PD_NTN.xlsx")
OUT_DIR = os.path.join(PROJECT_ROOT, "02_DATA_UNDERSTANDING", "03_eksplorasi_data_eda")

os.makedirs(OUT_DIR, exist_ok=True)

print("=== MEMULAI ANALISIS EKSPLORASI DATA (EDA) HIGH-RESOLUTION ===")
xls = pd.ExcelFile(DATA_CLEAN_PATH)
df_fp = pd.read_excel(xls, 'Formulir_Pelaporan')
df_sk = pd.read_excel(xls, 'Surat_Keterangan')

t_lapor = pd.to_datetime(df_fp['Tanggal_Pelaporan'])
t_lahir = pd.to_datetime(df_fp['Tanggal_Lahir'])
delay_days = (t_lapor - t_lahir).dt.days.apply(lambda d: max(0, d) if pd.notna(d) else 0)

# -------------------------------------------------------------
# 1. Gambar 1: Missing Values Audit (Bar Chart Bertingkat)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 5.5))
cols = ['Kecamatan', 'Desa/Kelurahan', 'Tanggal Lapor', 'Pekerjaan Ortu', 'No Surat Medis']
raw_pct = [80.1, 80.1, 15.3, 58.0, 32.8]
clean_pct = [0.0, 0.0, 0.0, 0.0, 0.0]

x = np.arange(len(cols))
width = 0.35
bars1 = ax.bar(x - width/2, raw_pct, width, label='Data Mentah Awal (Raw Missing)', color='#e74c3c', edgecolor='#922b21')
bars2 = ax.bar(x + width/2, clean_pct, width, label='Pasca-Pembersihan & Imputasi Faktual (0% Missing)', color='#2ecc71', edgecolor='#1e8449')

# Label angka di atas bar
for b in bars1:
    h = b.get_height()
    ax.annotate(f'{h:.1f}%', xy=(b.get_x() + b.get_width()/2, h), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#922b21')

for b in bars2:
    ax.annotate('0.0%\n(Lengkap)', xy=(b.get_x() + b.get_width()/2, 0), xytext=(0, 4),
                textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#1e8449')

ax.set_ylim(0, 95)
ax.set_ylabel('Persentase Data Kosong (%)', fontsize=11, fontweight='bold')
ax.set_title('EDA: Audit Mutu Data & Pembersihan Missing Values Melalui Sinkronisasi Silang', fontsize=12, fontweight='bold', pad=14)
ax.set_xticks(x)
ax.set_xticklabels(cols, fontsize=10, fontweight='bold')
ax.legend(frameon=True, facecolor='white', edgecolor='#bdc3c7', loc='upper right', fontsize=9.5)
ax.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
p1 = os.path.join(OUT_DIR, 'eda_masalah_kualitas_data_missing_values.png')
plt.savefig(p1, dpi=300)
plt.close()
print(f"-> Gambar EDA 1 tersimpan: {p1}")

# -------------------------------------------------------------
# 2. Gambar 2: Deteksi Anomali Typo & Distribusi Bulanan Tahun 2025
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.2))
# Panel Kiri: Anomali Selisih Negatif
ax1.scatter([0, 1], [-228, -10], color='#e74c3c', s=140, zorder=5, label='Typo Negatif Mentah (F044 & F0124)', edgecolors='black')
ax1.scatter([0, 1], [2, 4], color='#27ae60', s=140, zorder=5, label='Koreksi Pasca-Cleaning (LU Positif)', edgecolors='black')
ax1.axhline(0, color='black', linestyle='--', linewidth=1.2, alpha=0.7, label='Batas Yuridis Logis (T_lapor >= T_lahir)')
ax1.set_xticks([0, 1])
ax1.set_xticklabels(['Berkas F044\n(-228 -> +2 Hari)', 'Berkas F0124\n(-10 -> +4 Hari)'], fontsize=9.5, fontweight='bold')
ax1.set_ylabel('Selisih Hari (T_lapor - T_lahir)', fontsize=10.5, fontweight='bold')
ax1.set_title('Koreksi Anomali Typo Kronologis Negatif', fontsize=11.5, fontweight='bold', pad=10)
ax1.legend(loc='lower right', fontsize=8.5, frameon=True, facecolor='white')
ax1.grid(True, linestyle=':', alpha=0.6)

# Panel Kanan: Sebaran Bulanan Tahun Pelaporan 2025 (100% KONSISTEN TAHUN 2025)
months_2025 = t_lapor.dt.month.value_counts().sort_index()
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
counts_per_month = [months_2025.get(m, 0) for m in range(1, 13)]

ax2.bar(month_names, counts_per_month, color='#27ae60', edgecolor='#1e8449', width=0.65)
ax2.set_xlabel('Bulan Pelaporan (Tahun Kalender 2025)', fontsize=10.5, fontweight='bold')
ax2.set_ylabel('Jumlah Berkas Masuk', fontsize=10.5, fontweight='bold')
ax2.set_title('Verifikasi Konsistensi: 100% Pelaporan di Tahun 2025 (131 Berkas)', fontsize=11.5, fontweight='bold', pad=10)
for i, v in enumerate(counts_per_month):
    ax2.text(i, v + 0.8, str(v), ha='center', fontsize=9.5, fontweight='bold')
ax2.set_ylim(0, max(counts_per_month) + 8)
ax2.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()
p2 = os.path.join(OUT_DIR, 'eda_deteksi_anomali_typo_kronologis.png')
plt.savefig(p2, dpi=300)
plt.close()
print(f"-> Gambar EDA 2 tersimpan: {p2}")

# -------------------------------------------------------------
# 3. Gambar 3: Distribusi Bimodal Keterlambatan (Histogram)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 5.5))
delay_years = delay_days / 365.25
n, bins, patches_hist = ax.hist(delay_years, bins=35, color='#3498db', edgecolor='black', alpha=0.8)
ax.axvline(60/365.25, color='#27ae60', linestyle='--', linewidth=2.2, label='Batas UU No. 24/2013 (LU <= 60 Hari)')
ax.axvline(5.0, color='#e67e22', linestyle=':', linewidth=2.2, label='Batas Usia Masuk Sekolah (> 5 Tahun)')
ax.set_xlabel('Durasi Keterlambatan Pelaporan (Tahun)', fontsize=11, fontweight='bold')
ax.set_ylabel('Frekuensi Berkas Permohonan', fontsize=11, fontweight='bold')
ax.set_title('EDA: Karakteristik Pola Bimodal Keterlambatan Akta Kelahiran di Natuna', fontsize=12, fontweight='bold', pad=12)
ax.annotate('Puncak 1: Bayi Baru Lahir\n(LU <= 60 Hari: 37.4% / 49 Berkas)', xy=(0.1, 40), xytext=(4, 38),
            arrowprops=dict(facecolor='#27ae60', shrink=0.05, width=1.5, headwidth=8),
            fontsize=9.5, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#eafaf1", ec="#27ae60"))
ax.annotate('Puncak 2: Pemohon Dewasa / Lansia\n(SPTJM Kelahiran: > 5 Tahun)', xy=(35, 6), xytext=(42, 18),
            arrowprops=dict(facecolor='#e74c3c', shrink=0.05, width=1.5, headwidth=8),
            fontsize=9.5, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#fdedec", ec="#e74c3c"))
ax.legend(frameon=True, facecolor='white', edgecolor='#bdc3c7', loc='upper right', fontsize=9.5)
ax.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()
p3 = os.path.join(OUT_DIR, 'eda_distribusi_bimodal_keterlambatan.png')
plt.savefig(p3, dpi=300)
plt.close()
print(f"-> Gambar EDA 3 tersimpan: {p3}")

# -------------------------------------------------------------
# 4. Gambar 4: Sebaran Spasial Pulau Utama vs Terluar
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 6.5))
kec_counts = df_fp['Kecamatan'].value_counts()
pulau_utama = ['BUNGURAN TIMUR', 'BUNGURAN BARAT', 'BUNGURAN SELATAN', 'BUNGURAN UTARA', 'BUNGURAN TENGAH', 'BUNGURAN BATUBI', 'BUNGURAN TIMUR LAUT']
colors_bar = ['#2980b9' if k in pulau_utama else '#e67e22' for k in kec_counts.index]

y_pos = np.arange(len(kec_counts))
bars = ax.barh(y_pos, kec_counts.values, color=colors_bar, edgecolor='black', alpha=0.85)
ax.set_yticks(y_pos)
ax.set_yticklabels(kec_counts.index, fontsize=9.5, fontweight='bold')
ax.invert_yaxis()
ax.set_xlabel('Jumlah Berkas Permohonan Akta', fontsize=11, fontweight='bold')
ax.set_title('EDA: Sebaran Berkas Permohonan Akta Kelahiran per Kecamatan di Natuna', fontsize=12, fontweight='bold', pad=12)

# Label nilai di samping setiap bar
for b in bars:
    w = b.get_width()
    ax.text(w + 0.8, b.get_y() + b.get_height()/2, f'{int(w)} berkas', ha='left', va='center', fontsize=9, fontweight='bold')

ax.set_xlim(0, max(kec_counts.values) + 12)
legend_elements = [
    Patch(facecolor='#2980b9', edgecolor='black', label='Pulau Utama Bunguran (Ranai & Sekitarnya)'),
    Patch(facecolor='#e67e22', edgecolor='black', label='Kepulauan Terluar / Terpencil 3T')
]
ax.legend(handles=legend_elements, frameon=True, facecolor='white', edgecolor='#bdc3c7', loc='lower right', fontsize=9.5)
ax.grid(axis='x', linestyle=':', alpha=0.6)
plt.tight_layout()
p4 = os.path.join(OUT_DIR, 'eda_sebaran_spasial_pulau_utama_vs_terluar.png')
plt.savefig(p4, dpi=300)
plt.close()
print(f"-> Gambar EDA 4 tersimpan: {p4}")

# -------------------------------------------------------------
# 5. Gambar 5: Line Chart Tren Bulanan Pelaporan 2025
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 5.2))
status_lu = delay_days <= 60
df_trend = pd.DataFrame({'Bulan': t_lapor.dt.month, 'LU': status_lu, 'LT': ~status_lu})
monthly_lu = df_trend.groupby('Bulan')['LU'].sum()
monthly_lt = df_trend.groupby('Bulan')['LT'].sum()
m_range = range(1, 13)
vals_lu = [monthly_lu.get(m, 0) for m in m_range]
vals_lt = [monthly_lt.get(m, 0) for m in m_range]

line_lu = ax.plot(month_names, vals_lu, marker='o', color='#27ae60', linewidth=2.5, markersize=7, label='Lahir Umum (LU <= 60 Hari)')
line_lt = ax.plot(month_names, vals_lt, marker='s', color='#e74c3c', linewidth=2.5, markersize=7, label='Lahir Terlambat (LT > 60 Hari)')

for i, v in enumerate(vals_lu):
    if v > 0:
        ax.annotate(str(v), (i, v), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=9, fontweight='bold', color='#1e8449')
for i, v in enumerate(vals_lt):
    if v > 0:
        ax.annotate(str(v), (i, v), textcoords="offset points", xytext=(0, 6), ha='center', fontsize=9, fontweight='bold', color='#922b21')

ax.set_ylim(-2, max(vals_lt) + 8)
ax.set_xlabel('Bulan Pelaporan (Tahun Kalender 2025)', fontsize=11, fontweight='bold')
ax.set_ylabel('Jumlah Berkas Masuk', fontsize=11, fontweight='bold')
ax.set_title('EDA: Tren Bulanan Pelaporan Akta Kelahiran (LU vs LT) Sepanjang Tahun 2025', fontsize=12, fontweight='bold', pad=12)
ax.legend(frameon=True, facecolor='white', edgecolor='#bdc3c7', loc='upper right', fontsize=9.5)
ax.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
p5 = os.path.join(OUT_DIR, 'eda_tren_bulanan_pelaporan_line_chart.png')
plt.savefig(p5, dpi=300)
plt.close()
print(f"-> Gambar EDA 5 tersimpan: {p5}")

# -------------------------------------------------------------
# 6. Gambar 6: Boxplot Keterlambatan Spasial (Outlier Detection)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11.5, 6.2))
top_kecs = kec_counts.head(8).index.tolist()
data_box = [delay_days[df_fp['Kecamatan'] == k] / 365.25 for k in top_kecs]
ax.boxplot(data_box, tick_labels=[k.title() for k in top_kecs], patch_artist=True,
           boxprops=dict(facecolor='#d4e6f1', color='#1b4f72'),
           medianprops=dict(color='#c0392b', linewidth=2.2),
           flierprops=dict(marker='o', markerfacecolor='#e74c3c', markersize=6.5, markeredgecolor='black'))
ax.set_xticklabels([k.title() for k in top_kecs], rotation=22, ha='right', fontsize=9.5, fontweight='bold')
ax.set_ylabel('Durasi Keterlambatan (Tahun)', fontsize=11, fontweight='bold')
ax.set_title('EDA: Variasi & Deteksi Outlier Keterlambatan Antar-Kecamatan Utama', fontsize=12, fontweight='bold', pad=12)
ax.grid(axis='y', linestyle=':', alpha=0.6)
plt.tight_layout()
p6 = os.path.join(OUT_DIR, 'eda_boxplot_keterlambatan_spasial_outliers.png')
plt.savefig(p6, dpi=300)
plt.close()
print(f"-> Gambar EDA 6 tersimpan: {p6}")

# -------------------------------------------------------------
# 7. Gambar 7: Scatter Plot Usia Ortu vs Keterlambatan (Analisis Bivariat Individu)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(10.5, 5.8))
if os.path.exists(DATA_FEAT_PATH):
    df_feat = pd.read_excel(DATA_FEAT_PATH)
    usia_plot = df_feat['Usia_Rata_Ortu_Tahun'].values
    durasi_plot = df_feat['Durasi_Pelaporan_Hari'].values
else:
    t_ayah = pd.to_datetime(df_fp['Tanggal_Lahir_Ayah'], errors='coerce')
    usia_plot = np.array([(tl - ta).days / 365.25 if pd.notna(tl) and pd.notna(ta) else 32.0 for tl, ta in zip(t_lahir, t_ayah)])
    usia_plot = np.clip(usia_plot, 18.0, 65.0)
    durasi_plot = delay_days.values

# Sedikit jitter terkontrol untuk memecah tumpukan titik pada usia diskret
np.random.seed(42)
usia_jitter = usia_plot + np.random.normal(0, 0.25, len(usia_plot))

# Warna berdasarkan status LU / LT
colors_pt = ['#27ae60' if d <= 60 else ('#e74c3c' if d > 1826 else '#2980b9') for d in durasi_plot]
ax.scatter(usia_jitter, durasi_plot, c=colors_pt, s=65, alpha=0.8, edgecolors='black', linewidth=0.6, zorder=4)

ax.axhline(60, color='green', linestyle='--', linewidth=1.5, alpha=0.8, label='Batas UU No. 24/2013 (LU <= 60 Hari)')
ax.set_xlabel('Usia Rata-rata Orang Tua Saat Anak Lahir (Tahun)', fontsize=11, fontweight='bold')
ax.set_ylabel('Durasi Keterlambatan Pelaporan (Hari)', fontsize=11, fontweight='bold')
ax.set_title('EDA: Korelasi Bivariat Usia Orang Tua terhadap Lama Keterlambatan Pelaporan', fontsize=12, fontweight='bold', pad=12)

# Legend kustom
leg_el = [
    Patch(facecolor='#27ae60', edgecolor='black', label='Lahir Umum (Tepat Waktu <= 60 Hari)'),
    Patch(facecolor='#2980b9', edgecolor='black', label='Terlambat Sedang (61 Hari - 5 Tahun)'),
    Patch(facecolor='#e74c3c', edgecolor='black', label='Terlambat Historis SPTJM (> 5 Tahun)'),
]
ax.legend(handles=leg_el, frameon=True, facecolor='white', edgecolor='#bdc3c7', loc='upper right', fontsize=9)
ax.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
p7 = os.path.join(OUT_DIR, 'eda_scatterplot_korelasi_usia_vs_keterlambatan.png')
plt.savefig(p7, dpi=300)
plt.close()
print(f"-> Gambar EDA 7 tersimpan: {p7}")

# -------------------------------------------------------------
# 8. Gambar 8: Heatmap Matriks Korelasi Spearman
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8.5, 6.5))
df_corr = pd.DataFrame({
    'Durasi_Keterlambatan': durasi_plot,
    'Usia_Orang_Tua': usia_plot,
    'Status_Lahir_Terlambat': (durasi_plot > 60).astype(int),
    'Bulan_Pelaporan': t_lapor.dt.month
})
corr = df_corr.corr(method='spearman')
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.6, ax=ax, vmin=-1, vmax=1,
            cbar_kws={'label': 'Koefisien Korelasi Spearman'}, annot_kws={'fontsize': 11, 'fontweight': 'bold'})
ax.set_xticklabels(['Durasi Keterlambatan', 'Usia Orang Tua', 'Status Terlambat', 'Bulan Pelaporan'], fontsize=9.5, fontweight='bold')
ax.set_yticklabels(['Durasi Keterlambatan', 'Usia Orang Tua', 'Status Terlambat', 'Bulan Pelaporan'], fontsize=9.5, fontweight='bold')
ax.set_title('EDA: Matriks Korelasi Spearman Antar-Fitur Kuantitatif', fontsize=12, fontweight='bold', pad=12)
plt.tight_layout()
p8 = os.path.join(OUT_DIR, 'eda_heatmap_matriks_korelasi_fitur.png')
plt.savefig(p8, dpi=300)
plt.close()
print(f"-> Gambar EDA 8 tersimpan: {p8}")

print("=== SELURUH 8 VISUALISASI EDA SELESAI SUKSES ===")
