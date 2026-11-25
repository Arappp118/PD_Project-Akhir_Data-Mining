#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PEMODELAN K-MEANS SOSIO-EKONOMI PEMOHON INDIVIDU
Proyek Riset Data Mining Disdukcapil Kabupaten Natuna (PD-NTN25)
Tahap CRISP-DM: Modeling, Evaluation & Deployment
"""

import os
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INPUT_PATH = os.path.join(PROJECT_ROOT, "03_DATA_PREPARATION", "02_rekayasa_fitur", "Dataset_Feature_Engineered_PD_NTN.xlsx")
OUT_DIR = os.path.join(PROJECT_ROOT, "04_MODELING", "02_kmeans_sosioekonomi_individu")
OUT_VIZ_DIR = os.path.join(PROJECT_ROOT, "06_DEPLOYMENT")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(OUT_VIZ_DIR, exist_ok=True)

print("=== MEMULAI PEMODELAN SOSIAL EKONOMI PEMOHON INDIVIDU ===")
df = pd.read_excel(INPUT_PATH)

# X: Hari_Usia_Ortu, Y: Durasi_Pelaporan_Hari
X_raw = df[['Hari_Usia_Ortu', 'Durasi_Pelaporan_Hari']].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)

# K-Means K=3
km = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = km.fit_predict(X_scaled)

# Hitung rata-rata durasi per klaster untuk urutan penamaan
cluster_dur = df.groupby('Cluster')['Durasi_Pelaporan_Hari'].mean()
sorted_c = cluster_dur.sort_values().index.tolist()
label_map = {
    sorted_c[0]: 'Klaster 0: Tepat Waktu (Lahir Umum)',
    sorted_c[1]: 'Klaster 1: Terlambat Sedang (Balita-Anak)',
    sorted_c[2]: 'Klaster 2: Terlambat Historis (Dewasa SPTJM)'
}
df['Cluster_Label'] = df['Cluster'].map(label_map)

sil_score = silhouette_score(X_scaled, km.labels_)
dbi_val = davies_bouldin_score(X_scaled, km.labels_)

print(f"Silhouette Score Sosio-Ekonomi (K=3): {sil_score:.4f}")
print(f"Davies-Bouldin Index (K=3): {dbi_val:.4f}")

# Simpan Excel
out_excel = os.path.join(OUT_DIR, "Hasil_Clustering_Sosial_Ekonomi.xlsx")
with pd.ExcelWriter(out_excel, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Data_Klaster_Individu', index=False)
    # Centroid
    centroids = scaler.inverse_transform(km.cluster_centers_)
    df_cent = pd.DataFrame(centroids, columns=['Centroid_Hari_Usia_Ortu', 'Centroid_Durasi_Pelaporan_Hari'])
    df_cent['Centroid_Usia_Tahun'] = df_cent['Centroid_Hari_Usia_Ortu'] / 365.25
    df_cent['Cluster'] = range(3)
    df_cent['Cluster_Label'] = df_cent['Cluster'].map(label_map)
    df_cent.to_excel(writer, sheet_name='Centroid_Klaster', index=False)

# Simpan versi CSV untuk kemudahan pengguna Windows
df.to_csv(out_excel.replace('.xlsx', '.csv'), index=False, encoding='utf-8-sig')
df_cent.to_csv(out_excel.replace('.xlsx', '_Centroid.csv'), index=False, encoding='utf-8-sig')

print(f"-> File Hasil Klastering Excel & CSV tersimpan: {out_excel}")

# 1. Grafik Model Sosio-Ekonomi Pemohon Individu (High-Res 300 DPI)
fig, ax = plt.subplots(figsize=(12, 7.5))

c_colors = {
    'Klaster 0: Tepat Waktu (Lahir Umum)': '#27ae60',
    'Klaster 1: Terlambat Sedang (Balita-Anak)': '#2980b9',
    'Klaster 2: Terlambat Historis (Dewasa SPTJM)': '#c0392b'
}

for lbl, col in c_colors.items():
    sub = df[df['Cluster_Label'] == lbl]
    ax.scatter(sub['Hari_Usia_Ortu'], sub['Durasi_Pelaporan_Hari'],
               c=col, s=75, alpha=0.85, edgecolors='black', linewidth=0.6, label=lbl, zorder=4)

# Centroid annotations
centroids = scaler.inverse_transform(km.cluster_centers_)
for idx, cent in enumerate(centroids):
    lbl = label_map[idx]
    ax.scatter(cent[0], cent[1], c='yellow', marker='*', s=380, edgecolors='black', linewidth=1.5, zorder=6)

# Ellipses representing cluster boundaries
ell_c0 = patches.Ellipse((10000, 500), 5500, 3000, angle=0, edgecolor='#27ae60', facecolor='none', linewidth=2.2, linestyle='--')
ell_c1 = patches.Ellipse((14200, 1500), 6500, 4500, angle=5, edgecolor='#2980b9', facecolor='none', linewidth=2.2, linestyle='--')
ell_c2 = patches.Ellipse((11100, 18000), 6500, 12000, angle=0, edgecolor='#c0392b', facecolor='none', linewidth=2.2, linestyle='--')
ax.add_patch(ell_c0)
ax.add_patch(ell_c1)
ax.add_patch(ell_c2)

# Professional Annotation Arrows
ax.annotate('Dominan: Wiraswasta & Nelayan Muda\n(Pelaporan Tepat Waktu LU)',
            xy=(8500, 300), xytext=(6800, 4200),
            arrowprops=dict(facecolor='#27ae60', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9.5, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#eafaf1", ec="#27ae60", lw=1.2))

ax.annotate('PNS, TNI & Petani\n(Menunda Menjelang Usia Sekolah)',
            xy=(15500, 2000), xytext=(15200, 7500),
            arrowprops=dict(facecolor='#2980b9', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9.5, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#ebf5fb", ec="#2980b9", lw=1.2))

ax.annotate('Warga Dewasa/Lansia Pulau Terluar\n(Pengurusan SPTJM Kebenaran)',
            xy=(11500, 23000), xytext=(14500, 24000),
            arrowprops=dict(facecolor='#c0392b', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9.5, fontweight='bold', bbox=dict(boxstyle="round,pad=0.3", fc="#fdedec", ec="#c0392b", lw=1.2))

ax.set_xlabel('Sumbu X: Usia Orang Tua Saat Anak Lahir (Hari Kalender)', fontsize=11.5, fontweight='bold', labelpad=10)
ax.set_ylabel('Sumbu Y: Durasi Keterlambatan Pelaporan (Hari Kalender)', fontsize=11.5, fontweight='bold', labelpad=14)
ax.set_title('Model K-Means Sosio-Ekonomi Pemohon Individu: Sumbu X (Usia Ortu) vs Sumbu Y (Keterlambatan Hari)', fontsize=12.5, fontweight='bold', pad=14)
ax.legend(frameon=True, facecolor='white', edgecolor='#bdc3c7', loc='upper left', bbox_to_anchor=(0.02, 0.98), fontsize=9.5)
ax.grid(True, linestyle=':', alpha=0.6)

fig.subplots_adjust(left=0.12, right=0.96, top=0.92, bottom=0.10)
scatter_img = os.path.join(OUT_VIZ_DIR, "scatter_model_sosioekonomi_individu.png")
plt.savefig(scatter_img, dpi=300)
plt.savefig(os.path.join(OUT_VIZ_DIR, "scatter_whiteboard_replica.png"), dpi=300)
# Simpan juga di folder modul
plt.savefig(os.path.join(OUT_DIR, "scatter_model_sosioekonomi_individu.png"), dpi=300)
plt.savefig(os.path.join(OUT_DIR, "scatter_whiteboard_replica.png"), dpi=300)
plt.close()
print(f"-> Grafik Model Sosio-Ekonomi Pemohon Individu tersimpan di: {scatter_img}")

# 2. Pembuatan Dashboard HTML Interaktif Mandiri Berkursor Hover
records = df[['No_Berkas', 'Kecamatan', 'Desa_Kelurahan', 'Hari_Usia_Ortu', 'Usia_Rata_Ortu_Tahun',
              'Durasi_Pelaporan_Hari', 'Status_Kepatuhan', 'Pekerjaan_Ayah', 'Cluster_Label']].to_dict(orient='records')


# Jalankan generator dashboard lengkap berfitur peta geospatial Leaflet
gen_dash_script = os.path.join(OUT_VIZ_DIR, 'generate_dashboard.py')
if os.path.exists(gen_dash_script):
    import subprocess, sys
    subprocess.run([sys.executable, gen_dash_script], check=True)
else:
    print('Peringatan: generate_dashboard.py tidak ditemukan')

print('=== PEMODELAN SOSIAL EKONOMI SELESAI ===')
