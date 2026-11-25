#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PEMAKETAN BERKAS UNGGAH GOOGLE FORM RESMI
Sesuai Panduan Unggah Laporan Akhir:
1. Mentah_2401020121.7z
2. SiapMining_2401020121.7z
3. FinPD_2401020121.pdf
"""
import os
import shutil
import subprocess
import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_UPLOAD_DIR = os.path.join(PROJECT_ROOT, 'BERKAS_UNGGAH_GOOGLE_FORM')
os.makedirs(OUT_UPLOAD_DIR, exist_ok=True)

# 1. Mask privacy on raw digitized data (Anonimisasi PII Menyeluruh Sesuai UU No. 27/2022)
raw_path = os.path.join(PROJECT_ROOT, '02_DATA_UNDERSTANDING', '02_tabulasi_transkripsi', 'Data_Mentah_Transkripsi_Akta_Kelahiran_2025.xlsx')
df_fp = pd.read_excel(raw_path, sheet_name='Formulir_Pelaporan')
df_sk = pd.read_excel(raw_path, sheet_name='Surat_Keterangan')

entity_maps = {
    'pelapor': {}, 'nik_pelapor': {}, 'kk_pelapor': {},
    'subjek_kedua': {}, 'nik_subjek_kedua': {}, 'kk_subjek_kedua': {}, 'dok_perjalanan': {},
    'saksi_i': {}, 'nik_saksi_i': {}, 'kk_saksi_i': {},
    'saksi_ii': {}, 'nik_saksi_ii': {}, 'kk_saksi_ii': {},
    'ayah': {}, 'nik_ayah': {}, 'ibu': {}, 'nik_ibu': {}, 'anak': {},
    'alamat': {}, 'no_surat': {}
}

def clean_val(v):
    if pd.isna(v): return ''
    s = str(v).strip()
    if s.lower() in ['', 'nan', 'none', 'null']: return ''
    if s.endswith('.0') and s[:-2].isdigit():
        s = s[:-2]
    return s

def get_pseudonym(val, map_key, prefix):
    s = clean_val(val)
    if not s: return pd.NA
    m = entity_maps[map_key]
    if s not in m:
        m[s] = f"{prefix}_{len(m)+1:03d}"
    return m[s]

# Masking Formulir Pelaporan
if 'Nama_Pelapor' in df_fp.columns: df_fp['Nama_Pelapor'] = df_fp['Nama_Pelapor'].apply(lambda x: get_pseudonym(x, 'pelapor', 'PELAPOR'))
if 'NIK_Pelapor' in df_fp.columns: df_fp['NIK_Pelapor'] = df_fp['NIK_Pelapor'].apply(lambda x: get_pseudonym(x, 'nik_pelapor', 'NIK_PELAPOR'))
if 'No_KK_Pelapor' in df_fp.columns: df_fp['No_KK_Pelapor'] = df_fp['No_KK_Pelapor'].apply(lambda x: get_pseudonym(x, 'kk_pelapor', 'KK_PELAPOR'))
if 'No_Dokumen_Perjalanan_Pelapor' in df_fp.columns: df_fp['No_Dokumen_Perjalanan_Pelapor'] = df_fp['No_Dokumen_Perjalanan_Pelapor'].apply(lambda x: get_pseudonym(x, 'dok_perjalanan', 'DOK_PELAPOR'))

if 'Nama_Subjek_Akta_Kedua' in df_fp.columns: df_fp['Nama_Subjek_Akta_Kedua'] = df_fp['Nama_Subjek_Akta_Kedua'].apply(lambda x: get_pseudonym(x, 'subjek_kedua', 'SUBJEK_KEDUA'))
if 'NIK_Subjek_Akta_Kedua' in df_fp.columns: df_fp['NIK_Subjek_Akta_Kedua'] = df_fp['NIK_Subjek_Akta_Kedua'].apply(lambda x: get_pseudonym(x, 'nik_subjek_kedua', 'NIK_SUBJEK'))
if 'No_KK_Subjek_Kedua' in df_fp.columns: df_fp['No_KK_Subjek_Kedua'] = df_fp['No_KK_Subjek_Kedua'].apply(lambda x: get_pseudonym(x, 'kk_subjek_kedua', 'KK_SUBJEK'))
if 'No_Dokumen_Perjalanan_Subjek_Kedua' in df_fp.columns: df_fp['No_Dokumen_Perjalanan_Subjek_Kedua'] = df_fp['No_Dokumen_Perjalanan_Subjek_Kedua'].apply(lambda x: get_pseudonym(x, 'dok_perjalanan', 'DOK_SUBJEK'))

if 'Nama_Saksi_I' in df_fp.columns: df_fp['Nama_Saksi_I'] = df_fp['Nama_Saksi_I'].apply(lambda x: get_pseudonym(x, 'saksi_i', 'SAKSI_I'))
if 'NIK_Saksi_I' in df_fp.columns: df_fp['NIK_Saksi_I'] = df_fp['NIK_Saksi_I'].apply(lambda x: get_pseudonym(x, 'nik_saksi_i', 'NIK_SAKSI_I'))
if 'No_KK_Saksi_I' in df_fp.columns: df_fp['No_KK_Saksi_I'] = df_fp['No_KK_Saksi_I'].apply(lambda x: get_pseudonym(x, 'kk_saksi_i', 'KK_SAKSI_I'))

if 'Nama_Saksi_II' in df_fp.columns: df_fp['Nama_Saksi_II'] = df_fp['Nama_Saksi_II'].apply(lambda x: get_pseudonym(x, 'saksi_ii', 'SAKSI_II'))
if 'NIK_Saksi_II' in df_fp.columns: df_fp['NIK_Saksi_II'] = df_fp['NIK_Saksi_II'].apply(lambda x: get_pseudonym(x, 'nik_saksi_ii', 'NIK_SAKSI_II'))
if 'No_KK_Saksi_II' in df_fp.columns: df_fp['No_KK_Saksi_II'] = df_fp['No_KK_Saksi_II'].apply(lambda x: get_pseudonym(x, 'kk_saksi_ii', 'KK_SAKSI_II'))

if 'Nama_Ayah' in df_fp.columns: df_fp['Nama_Ayah'] = df_fp['Nama_Ayah'].apply(lambda x: get_pseudonym(x, 'ayah', 'AYAH'))
if 'NIK_Ayah' in df_fp.columns: df_fp['NIK_Ayah'] = df_fp['NIK_Ayah'].apply(lambda x: get_pseudonym(x, 'nik_ayah', 'NIK_AYAH'))

if 'Nama_Ibu' in df_fp.columns: df_fp['Nama_Ibu'] = df_fp['Nama_Ibu'].apply(lambda x: get_pseudonym(x, 'ibu', 'IBU'))
if 'NIK_Ibu' in df_fp.columns: df_fp['NIK_Ibu'] = df_fp['NIK_Ibu'].apply(lambda x: get_pseudonym(x, 'nik_ibu', 'NIK_IBU'))

if 'Nama_Anak' in df_fp.columns: df_fp['Nama_Anak'] = df_fp['Nama_Anak'].apply(lambda x: get_pseudonym(x, 'anak', 'ANAK'))

# Masking Surat Keterangan
def mask_surat(val):
    s = clean_val(val)
    if not s: return pd.NA
    if 'SPTJM' in s.upper(): return 'SPTJM (Tanpa No Surat Medis)'
    m = entity_maps['no_surat']
    if s not in m:
        m[s] = f"SKL_{len(m)+1:03d}"
    return m[s]

if 'Nomor_Surat' in df_sk.columns: df_sk['Nomor_Surat'] = df_sk['Nomor_Surat'].apply(mask_surat)
if 'Nama_Anak' in df_sk.columns: df_sk['Nama_Anak'] = df_sk['Nama_Anak'].apply(lambda x: get_pseudonym(x, 'anak', 'ANAK'))
if 'Nama_Ayah' in df_sk.columns: df_sk['Nama_Ayah'] = df_sk['Nama_Ayah'].apply(lambda x: get_pseudonym(x, 'ayah', 'AYAH'))
if 'Alamat_Ayah' in df_sk.columns: df_sk['Alamat_Ayah'] = df_sk['Alamat_Ayah'].apply(lambda x: get_pseudonym(x, 'alamat', 'ALAMAT_DISAMARKAN'))
if 'Nama_Ibu' in df_sk.columns: df_sk['Nama_Ibu'] = df_sk['Nama_Ibu'].apply(lambda x: get_pseudonym(x, 'ibu', 'IBU'))
if 'Alamat_Ibu' in df_sk.columns: df_sk['Alamat_Ibu'] = df_sk['Alamat_Ibu'].apply(lambda x: get_pseudonym(x, 'alamat', 'ALAMAT_DISAMARKAN'))
if 'Nama_Saksi_I' in df_sk.columns: df_sk['Nama_Saksi_I'] = df_sk['Nama_Saksi_I'].apply(lambda x: get_pseudonym(x, 'saksi_i', 'SAKSI_I'))
if 'Nama_Saksi_II' in df_sk.columns: df_sk['Nama_Saksi_II'] = df_sk['Nama_Saksi_II'].apply(lambda x: get_pseudonym(x, 'saksi_ii', 'SAKSI_II'))

# Fail-Safe Sweep untuk seluruh kolom (mendeteksi angka >= 12 digit seperti NIK/KK jika tersisa)
for df_target in [df_fp, df_sk]:
    for col in df_target.columns:
        if col in ['Kode_Wilayah', 'ID_Data']: continue
        def sweep_val(v):
            if pd.isna(v): return v
            s = str(v).strip()
            if s.endswith('.0') and s[:-2].isdigit(): s_num = s[:-2]
            else: s_num = s
            if s_num.isdigit() and len(s_num) >= 12:
                return f"ID_ANONIM_{abs(hash(s_num))%10000:04d}"
            return v
        df_target[col] = df_target[col].apply(sweep_val)

temp_raw_masked = os.path.join(OUT_UPLOAD_DIR, 'Data_Mentah_Terdigitalisasi_Privacy_Disamarkan.xlsx')
with pd.ExcelWriter(temp_raw_masked, engine='openpyxl') as writer:
    df_fp.to_excel(writer, sheet_name='Formulir_Pelaporan', index=False)
    df_sk.to_excel(writer, sheet_name='Surat_Keterangan', index=False)

# Simpan juga versi CSV untuk kemudahan pengguna Windows
csv_fp_masked = os.path.join(OUT_UPLOAD_DIR, 'Data_Mentah_Terdigitalisasi_Privacy_Disamarkan_Formulir_Pelaporan.csv')
csv_sk_masked = os.path.join(OUT_UPLOAD_DIR, 'Data_Mentah_Terdigitalisasi_Privacy_Disamarkan_Surat_Keterangan.csv')
df_fp.to_csv(csv_fp_masked, index=False, encoding='utf-8-sig')
df_sk.to_csv(csv_sk_masked, index=False, encoding='utf-8-sig')

# 2. Compress to Mentah_2401020121.7z
mentah_7z = os.path.join(OUT_UPLOAD_DIR, 'Mentah_2401020121.7z')
if os.path.exists(mentah_7z): os.remove(mentah_7z)
raw_items = [temp_raw_masked, csv_fp_masked, csv_sk_masked]
subprocess.run(['7z', 'a', mentah_7z] + raw_items, check=True, stdout=subprocess.DEVNULL)
print(f'-> [BERKAS 1/3] Mentah_2401020121.7z tersimpan: {mentah_7z}')

# 3. Gather Siap Mining files (XLSX & CSV Lengkap)
siap_files = [
    os.path.join(PROJECT_ROOT, '03_DATA_PREPARATION', '02_rekayasa_fitur', 'Dataset_Feature_Engineered_PD_NTN.xlsx'),
    os.path.join(PROJECT_ROOT, '03_DATA_PREPARATION', '02_rekayasa_fitur', 'Dataset_Feature_Engineered_PD_NTN.csv'),
    os.path.join(PROJECT_ROOT, '03_DATA_PREPARATION', '02_rekayasa_fitur', 'Dataset_Agregasi_Spasial_16_Kecamatan.xlsx'),
    os.path.join(PROJECT_ROOT, '03_DATA_PREPARATION', '02_rekayasa_fitur', 'Dataset_Agregasi_Spasial_16_Kecamatan.csv'),
    os.path.join(PROJECT_ROOT, '03_DATA_PREPARATION', '01_pembersihan_data', 'Data_Bersih_Akta_Kelahiran_Lengkap_Imputed.xlsx'),
    os.path.join(PROJECT_ROOT, '03_DATA_PREPARATION', '01_pembersihan_data', 'Data_Bersih_Akta_Kelahiran_Lengkap_Imputed.csv'),
    os.path.join(PROJECT_ROOT, '03_DATA_PREPARATION', '01_pembersihan_data', 'Data_Bersih_Akta_Kelahiran_Surat_Keterangan_Imputed.csv'),
    os.path.join(PROJECT_ROOT, '04_MODELING', '01_kmeans_spasial_wilayah', 'Hasil_Clustering_Kecamatan_Natuna.xlsx'),
    os.path.join(PROJECT_ROOT, '04_MODELING', '01_kmeans_spasial_wilayah', 'Hasil_Clustering_Kecamatan_Natuna.csv'),
    os.path.join(PROJECT_ROOT, '04_MODELING', '02_kmeans_sosioekonomi_individu', 'Hasil_Clustering_Sosial_Ekonomi.xlsx'),
    os.path.join(PROJECT_ROOT, '04_MODELING', '02_kmeans_sosioekonomi_individu', 'Hasil_Clustering_Sosial_Ekonomi.csv')
]

# Saring hanya file yang ada di disk
valid_siap_files = [f for f in siap_files if os.path.exists(f)]

siap_7z = os.path.join(OUT_UPLOAD_DIR, 'SiapMining_2401020121.7z')
if os.path.exists(siap_7z): os.remove(siap_7z)
cmd = ['7z', 'a', siap_7z] + valid_siap_files
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
print(f'-> [BERKAS 2/3] SiapMining_2401020121.7z tersimpan: {siap_7z}')

# 4. Copy PDF to UPLOAD_DIR
pdf_src = os.path.join(PROJECT_ROOT, '07_LAPORAN_AKHIR_DAN_PROPOSAL', 'FinPD_2401020121.pdf')
pdf_dst = os.path.join(OUT_UPLOAD_DIR, 'FinPD_2401020121.pdf')
if os.path.exists(pdf_src):
    shutil.copy2(pdf_src, pdf_dst)
    print(f'-> [BERKAS 3/3] FinPD_2401020121.pdf tersimpan: {pdf_dst}')

print('=== PEMAKETAN BERKAS UNGGAH GOOGLE FORM SELESAI SUKSES 100% ===')

