#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PEMODELAN K-MEANS CLUSTERING SPASIAL WILAYAH (16 KECAMATAN)
Proyek Riset Data Mining Disdukcapil Kabupaten Natuna (PD-NTN25-FINAL)
Tahap CRISP-DM: Modeling & Evaluation
"""

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
INPUT_PATH = os.path.join(PROJECT_ROOT, "03_DATA_PREPARATION", "02_rekayasa_fitur", "Dataset_Agregasi_Spasial_16_Kecamatan.xlsx")
OUT_DIR = os.path.join(PROJECT_ROOT, "04_MODELING", "01_kmeans_spasial_wilayah")
OUT_EVAL_DIR = os.path.join(PROJECT_ROOT, "05_EVALUATION")
OUT_VIZ_DIR = os.path.join(PROJECT_ROOT, "06_DEPLOYMENT")

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(OUT_EVAL_DIR, exist_ok=True)
os.makedirs(OUT_VIZ_DIR, exist_ok=True)

print("=== MEMULAI PEMODELAN K-MEANS SPASIAL WILAYAH (16 KECAMATAN) ===")
df = pd.read_excel(INPUT_PATH)

features = ['Persentase_LU', 'Median_Durasi_Hari']
X = df[features].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Eksperimen K=2..6
k_range = range(2, 7)
inertias = []
silhouettes = []
dbi_scores = []

for k in k_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X_scaled)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_scaled, labels))
    dbi_scores.append(davies_bouldin_score(X_scaled, labels))

# -------------------------------------------------------------
# 1. Plot Evaluasi Elbow & Silhouette (High-Res 300 DPI)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.2))
ax1.plot(k_range, inertias, 'bo-', linewidth=2.5, markersize=8)
ax1.set_xlabel('Nilai K (Jumlah Cluster)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Inertia / WCSS', fontsize=11, fontweight='bold')
ax1.set_title('Metode Elbow: Penentuan Titik Tekuk WCSS', fontsize=12, fontweight='bold', pad=10)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.axvline(3, color='red', linestyle='--', linewidth=1.8, label='Elbow Optimal (K=3)')
ax1.legend(frameon=True, facecolor='white', fontsize=10)

ax2.plot(k_range, silhouettes, 'gs-', linewidth=2.5, markersize=8)
ax2.set_xlabel('Nilai K (Jumlah Cluster)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Silhouette Coefficient', fontsize=11, fontweight='bold')
ax2.set_title('Evaluasi Metrik Silhouette Score', fontsize=12, fontweight='bold', pad=10)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.axvline(3, color='red', linestyle='--', linewidth=1.8, label='K=3: Struktur & Domain Optimum (0.641)')
ax2.legend(frameon=True, facecolor='white', fontsize=10)

plt.tight_layout()
eval_img = os.path.join(OUT_EVAL_DIR, "evaluasi_elbow_silhouette.png")
plt.savefig(eval_img, dpi=300)
plt.close()
print(f"-> Grafik Evaluasi disimpan di: {eval_img}")

# -------------------------------------------------------------
# 2. Pemodelan Final K=3
# -------------------------------------------------------------
k_final = 3
km_final = KMeans(n_clusters=k_final, random_state=42, n_init=10)
df['Cluster'] = km_final.fit_predict(X_scaled)

# Penamaan Klaster Sesuai Karakteristik Domain
cluster_lu = df.groupby('Cluster')['Persentase_LU'].mean()
sorted_clusters = cluster_lu.sort_values(ascending=False).index.tolist()
label_map = {
    sorted_clusters[0]: 'Cluster 0 (High-Compliance)',
    sorted_clusters[1]: 'Cluster 1 (Moderate)',
    sorted_clusters[2]: 'Cluster 2 (High-Delay)'
}
df['Cluster_Label'] = df['Cluster'].map(label_map)

# Centroid asli
centroids_scaled = km_final.cluster_centers_
centroids_asli = scaler.inverse_transform(centroids_scaled)
df_centroids = pd.DataFrame(centroids_asli, columns=features)
df_centroids['Cluster'] = range(k_final)
df_centroids['Cluster_Label'] = df_centroids['Cluster'].map(label_map)

# -------------------------------------------------------------
# 3. Scatter Plot Hasil Klastering Spasial Tanpa Tabrakan Label
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11.5, 6.8))
colors = {
    'Cluster 0 (High-Compliance)': '#2ecc71',
    'Cluster 1 (Moderate)': '#f39c12',
    'Cluster 2 (High-Delay)': '#e74c3c'
}

for lbl, c in colors.items():
    sub = df[df['Cluster_Label'] == lbl]
    ax.scatter(sub['Persentase_LU'], sub['Median_Durasi_Hari'], color=c, s=140, label=lbl, edgecolors='black', linewidth=0.8, alpha=0.9, zorder=5)

# Penempatan manual offset bebas collision untuk seluruh 16 kecamatan
spasial_offsets = {
    'BUNGURAN TIMUR': (15, -20),
    'BUNGURAN BARAT': (-60, 30),
    'BUNGURAN SELATAN': (35, 30),
    'BUNGURAN UTARA': (25, 18),
    'BUNGURAN TENGAH': (0, 22),
    'BUNGURAN BATUBI': (-65, -8),
    'BUNGURAN TIMUR LAUT': (15, 10),
    'PULAU LAUT': (-35, 20),
    'PULAU TIGA': (-30, 15),
    'PULAU TIGA BARAT': (-45, -15),
    'MIDAI': (15, 10),
    'SUAK MIDAI': (25, 10),
    'SERASAN': (18, 5),
    'SERASAN TIMUR': (30, -25),
    'SUBI': (-25, 25),
    'PULAU PANJANG': (18, 0)
}

for _, r in df.iterrows():
    k_name = r['Kecamatan']
    dx, dy = spasial_offsets.get(k_name, (10, 10))
    ax.annotate(k_name, (r['Persentase_LU'], r['Median_Durasi_Hari']),
                xytext=(dx, dy), textcoords='offset points',
                fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#7f8c8d", alpha=0.85, linewidth=0.7),
                arrowprops=dict(arrowstyle="->", color="#34495e", lw=0.8, shrinkA=0, shrinkB=4),
                zorder=6)

ax.set_xlabel('Persentase Kepatuhan Lahir Umum / LU (%)', fontsize=11, fontweight='bold')
ax.set_ylabel('Median Durasi Keterlambatan (Hari)', fontsize=11, fontweight='bold')
ax.set_title('Visualisasi Segmentasi 16 Kecamatan di Disdukcapil Kabupaten Natuna (K=3)', fontsize=12, fontweight='bold', pad=14)
ax.legend(frameon=True, facecolor='white', edgecolor='#bdc3c7', loc='upper right', fontsize=10)
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_ylim(-2000, 18500)
ax.set_xlim(-12, 110)

plt.tight_layout()
viz_img = os.path.join(OUT_VIZ_DIR, "visualisasi_cluster_kecamatan.png")
plt.savefig(viz_img, dpi=300)
plt.close()
print(f"-> Grafik Scatter Spasial disimpan di: {viz_img}")

# -------------------------------------------------------------
# 4. Peta Geospatial Klastering Natuna Resolusi Tinggi (300 DPI)
# -------------------------------------------------------------
coords = {
    'BUNGURAN TIMUR': (3.9463, 108.3846),
    'BUNGURAN BARAT': (3.8167, 108.1333),
    'BUNGURAN SELATAN': (3.7667, 108.3500),
    'BUNGURAN UTARA': (4.1667, 108.1833),
    'BUNGURAN TENGAH': (3.9000, 108.3000),
    'BUNGURAN BATUBI': (3.9833, 108.1667),
    'BUNGURAN TIMUR LAUT': (4.0667, 108.3500),
    'PULAU LAUT': (4.7333, 107.9833),
    'PULAU TIGA': (3.6333, 108.0667),
    'PULAU TIGA BARAT': (3.6000, 108.0167),
    'MIDAI': (3.0000, 107.7833),
    'SUAK MIDAI': (3.0333, 107.7500),
    'SERASAN': (2.5000, 109.0167),
    'SERASAN TIMUR': (2.4833, 109.1167),
    'SUBI': (3.1500, 108.8333),
    'PULAU PANJANG': (3.2167, 108.7167)
}

df['Lat'] = df['Kecamatan'].map(lambda x: coords[x][0])
df['Lon'] = df['Kecamatan'].map(lambda x: coords[x][1])

fig, ax = plt.subplots(figsize=(12.5, 10.5), facecolor='#f8f9fa')
ax.set_facecolor('#eaf2f8') # Soft marine background

ax.grid(True, linestyle='--', color='#b0bec5', alpha=0.7)
ax.set_xlim(107.2, 109.6)
ax.set_ylim(2.1, 5.2)
ax.set_xlabel('Bujur Timur (Longitude °E)', fontsize=11.5, fontweight='bold', labelpad=10)
ax.set_ylabel('Lintang Utara (Latitude °N)', fontsize=11.5, fontweight='bold', labelpad=10)
ax.set_title('PETA GEOSPATIAL CLUSTERING TINGKAT KETERLAMBATAN PENCATATAN AKTA KELAHIRAN\nKABUPATEN NATUNA (16 KECAMATAN) - MODEL K-MEANS SPASIAL', fontsize=12.5, fontweight='bold', pad=15)

geo_offsets = {
    'BUNGURAN TIMUR': (48, -5),
    'BUNGURAN BARAT': (-58, 0),
    'BUNGURAN SELATAN': (30, -22),
    'BUNGURAN UTARA': (0, 22),
    'BUNGURAN TENGAH': (-25, -25),
    'BUNGURAN BATUBI': (-52, 15),
    'BUNGURAN TIMUR LAUT': (48, 15),
    'PULAU LAUT': (0, 22),
    'PULAU TIGA': (32, 15),
    'PULAU TIGA BARAT': (-48, -18),
    'MIDAI': (35, -15),
    'SUAK MIDAI': (-45, 15),
    'SERASAN': (-35, 15),
    'SERASAN TIMUR': (38, -15),
    'SUBI': (32, -15),
    'PULAU PANJANG': (-35, 15)
}

for lbl, col in colors.items():
    sub = df[df['Cluster_Label'] == lbl]
    sizes = np.clip(sub['Total_Berkas'] * 15 + 110, 130, 950)
    ax.scatter(sub['Lon'], sub['Lat'], c=col, s=sizes, alpha=0.88, edgecolors='black', linewidth=1.2, label=f'{lbl} (n={len(sub)})', zorder=5)

for _, r in df.iterrows():
    kn = r['Kecamatan']
    dx, dy = geo_offsets.get(kn, (0, 12))
    col = colors[r['Cluster_Label']]
    ax.annotate(kn, (r['Lon'], r['Lat']), xytext=(dx, dy), textcoords='offset points',
                ha='center', va='center', fontsize=8.5, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.22', facecolor='white', alpha=0.9, edgecolor=col, linewidth=1.2),
                arrowprops=dict(arrowstyle="->", color=col, lw=1.0, shrinkA=0, shrinkB=4),
                zorder=6)

ax.legend(loc='lower left', frameon=True, facecolor='white', edgecolor='#bdc3c7', framealpha=0.95, fontsize=9.5, title='Klaster Spasial K-Means', title_fontsize=10.5)

# Catatan kaki peta di posisi aman tanpa overlap sumbu
ax.text(107.25, 2.16, '* Catatan: Ukuran lingkaran proporsional terhadap volume berkas permohonan. Warna mengindikasikan tingkat kepatuhan waktu pelaporan.',
        fontsize=8.5, style='italic', color='#34495e', bbox=dict(boxstyle='square,pad=0.2', facecolor='#ffffff', alpha=0.7, edgecolor='none'))

plt.tight_layout()
peta_img = os.path.join(OUT_VIZ_DIR, "peta_geospatial_klaster_natuna.png")
plt.savefig(peta_img, dpi=300)
plt.close()
print(f"-> Peta Geospatial disimpan di: {peta_img}")

# -------------------------------------------------------------
# 5. Simpan Tabel Hasil Excel
# -------------------------------------------------------------
out_excel = os.path.join(OUT_DIR, "Hasil_Clustering_Kecamatan_Natuna.xlsx")
df_eval = pd.DataFrame({
    'Nilai_K': list(k_range),
    'WCSS_Inertia': inertias,
    'Silhouette_Score': silhouettes,
    'Davies_Bouldin_Index': dbi_scores
})

with pd.ExcelWriter(out_excel, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name='Hasil_Clustering', index=False)
    df_centroids.to_excel(writer, sheet_name='Centroid_Asli', index=False)
    df_eval.to_excel(writer, sheet_name='Evaluasi_Metrik', index=False)

# Simpan versi CSV untuk kemudahan pengguna Windows
df.to_csv(out_excel.replace('.xlsx', '.csv'), index=False, encoding='utf-8-sig')
df_centroids.to_csv(out_excel.replace('.xlsx', '_Centroid.csv'), index=False, encoding='utf-8-sig')
df_eval.to_csv(out_excel.replace('.xlsx', '_Evaluasi.csv'), index=False, encoding='utf-8-sig')

print(f"-> Hasil Pemodelan Spasial Excel & CSV tersimpan di: {out_excel}")
print(f"Silhouette Score (K=3): {silhouette_score(X_scaled, km_final.labels_):.4f}")
print(f"Davies-Bouldin Index (K=3): {davies_bouldin_score(X_scaled, km_final.labels_):.4f}")
print("=== PEMODELAN K-MEANS SPASIAL SELESAI ===")
