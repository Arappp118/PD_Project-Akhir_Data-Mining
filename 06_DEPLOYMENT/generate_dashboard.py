import os, json
import pandas as pd

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
df_spasial = pd.read_excel(os.path.join(PROJECT_ROOT, '04_MODELING', '01_kmeans_spasial_wilayah', 'Hasil_Clustering_Kecamatan_Natuna.xlsx'))
df_indiv = pd.read_excel(os.path.join(PROJECT_ROOT, '04_MODELING', '02_kmeans_sosioekonomi_individu', 'Hasil_Clustering_Sosial_Ekonomi.xlsx'))
df_cent = pd.read_excel(os.path.join(PROJECT_ROOT, '04_MODELING', '02_kmeans_sosioekonomi_individu', 'Hasil_Clustering_Sosial_Ekonomi.xlsx'), sheet_name='Centroid_Klaster')

coords = {
    'BUNGURAN TIMUR': [3.9463, 108.3846],
    'BUNGURAN BARAT': [3.8167, 108.1333],
    'BUNGURAN SELATAN': [3.7667, 108.3500],
    'BUNGURAN UTARA': [4.1667, 108.1833],
    'BUNGURAN TENGAH': [3.9000, 108.3000],
    'BUNGURAN BATUBI': [3.9833, 108.1667],
    'BUNGURAN TIMUR LAUT': [4.0667, 108.3500],
    'PULAU LAUT': [4.7333, 107.9833],
    'PULAU TIGA': [3.6333, 108.0667],
    'PULAU TIGA BARAT': [3.6000, 108.0167],
    'MIDAI': [3.0000, 107.7833],
    'SUAK MIDAI': [3.0333, 107.7500],
    'SERASAN': [2.5000, 109.0167],
    'SERASAN TIMUR': [2.4833, 109.1167],
    'SUBI': [3.1500, 108.8333],
    'PULAU PANJANG': [3.2167, 108.7167]
}

spasial_list = []
for idx, r in df_spasial.iterrows():
    c_name = r['Kecamatan']
    lat, lon = coords.get(c_name, [3.9463, 108.3846])
    spasial_list.append({
        'kecamatan': c_name,
        'lat': lat,
        'lon': lon,
        'cluster': int(r['Cluster']),
        'cluster_label': r['Cluster_Label'],
        'total_berkas': int(r['Total_Berkas']),
        'persentase_lu': float(r['Persentase_LU']),
        'median_durasi': float(r['Median_Durasi_Hari']),
        'mean_durasi': float(r['Mean_Durasi_Hari'])
    })

indiv_cols = ['No_Berkas', 'Kecamatan', 'Desa_Kelurahan', 'Hari_Usia_Ortu', 'Usia_Rata_Ortu_Tahun', 
              'Durasi_Pelaporan_Hari', 'Status_Kepatuhan', 'Pekerjaan_Ayah', 'Cluster', 'Cluster_Label']
indiv_list = df_indiv[indiv_cols].to_dict(orient='records')

# Centroids for Model 2
cent_list = []
for idx, r in df_cent.iterrows():
    cent_list.append({
        'cluster': int(r['Cluster']),
        'cluster_label': str(r['Cluster_Label']),
        'centroid_x': float(r['Centroid_Hari_Usia_Ortu']),
        'centroid_y': float(r['Centroid_Durasi_Pelaporan_Hari']),
        'usia_tahun': float(r['Centroid_Usia_Tahun']),
        'durasi_tahun': float(r['Centroid_Durasi_Pelaporan_Hari'] / 365.25)
    })

rows_html = ""
for s in spasial_list:
    c_lbl = s['cluster_label']
    if 'High-Compliance' in c_lbl:
        badge_cls = 'bc-green'
        rekom = 'Layanan Loket Reguler & Percontohan Desa Tertib Adminduk'
    elif 'Moderate' in c_lbl:
        badge_cls = 'bc-orange'
        rekom = 'Penguatan Sosialisasi Desa & Integrasi Puskesmas Pembantu (Pustu)'
    else:
        badge_cls = 'bc-red'
        rekom = 'Prioritas Armada Mobile Service Boat & Pelayanan Sidang Terpadu SPTJM'

    tb_str = f"{s['total_berkas']} berkas" if s['total_berkas'] > 0 else "0 berkas <small style='color:#718096;'>(Pemekaran P. Tiga)</small>"
    rows_html += f"""
        <tr>
          <td><b>{s['kecamatan']}</b></td>
          <td><span class="badge-cluster {badge_cls}">{c_lbl}</span></td>
          <td>{tb_str}</td>
          <td>{s['persentase_lu']:.1f}%</td>
          <td>{s['median_durasi']:.0f} hari ({s['median_durasi']/365.25:.1f} thn)</td>
          <td>{rekom}</td>
        </tr>"""

json_spasial = json.dumps(spasial_list)
json_indiv = json.dumps(indiv_list)
json_cent = json.dumps(cent_list)

template = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dashboard Geospasial & Penambangan Data K-Means - Disdukcapil Natuna</title>
<!-- Leaflet CSS & JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<!-- Plotly.js -->
<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
<style>
  * { box-sizing: border-box; }
  body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 20px; background-color: #f0f3f7; color: #2c3e50; }
  
  .header { background: linear-gradient(135deg, #0d3b66, #1f618d); color: white; padding: 22px 25px; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
  .header h1 { margin: 0 0 6px 0; font-size: 22px; font-weight: 700; letter-spacing: -0.3px; }
  .header p { margin: 0; opacity: 0.92; font-size: 13.5px; }
  .badges-row { margin-top: 10px; display: flex; gap: 8px; flex-wrap: wrap; }
  .badge-tag { display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 11.5px; font-weight: 700; }
  .bg-tag-red { background: #e74c3c; color: white; }
  .bg-tag-blue { background: #2980b9; color: white; }
  .bg-tag-green { background: #27ae60; color: white; }

  .grid-stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; margin-bottom: 20px; }
  .stat-box { padding: 16px; border-radius: 10px; color: white; text-align: center; box-shadow: 0 3px 10px rgba(0,0,0,0.07); transition: transform 0.2s; }
  .stat-box:hover { transform: translateY(-2px); }
  .bg-navy { background: linear-gradient(135deg, #1f2d3d, #111a24); }
  .bg-green { background: linear-gradient(135deg, #27ae60, #2ecc71); }
  .bg-orange { background: linear-gradient(135deg, #d35400, #f39c12); }
  .bg-red { background: linear-gradient(135deg, #c0392b, #e74c3c); }
  .stat-box h3 { margin: 0; font-size: 24px; font-weight: bold; }
  .stat-box p { margin: 4px 0 0 0; font-size: 12px; opacity: 0.95; }

  .tab-container { background: white; border-radius: 12px; padding: 18px; box-shadow: 0 2px 12px rgba(0,0,0,0.05); }
  .tab-nav { display: flex; gap: 10px; border-bottom: 2px solid #e9ecef; padding-bottom: 12px; margin-bottom: 18px; flex-wrap: wrap; }
  .tab-btn { padding: 10px 18px; border: none; background: #eef2f7; color: #495057; font-weight: 700; font-size: 13px; border-radius: 8px; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 6px; }
  .tab-btn:hover { background: #dfe5ec; }
  .tab-btn.active { background: #1f618d; color: white; box-shadow: 0 3px 8px rgba(31,97,141,0.3); }
  .tab-content { display: none; }
  .tab-content.active { display: block; }

  /* MAP STYLES */
  #map { height: 620px; width: 100%; border-radius: 10px; border: 1px solid #dcdfe6; }
  .map-toolbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 10px; }
  .filter-group { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: bold; }
  .filter-select { padding: 6px 12px; border-radius: 6px; border: 1px solid #ced4da; font-size: 12.5px; }

  /* SOSIO-EKONOMI DETAIL STYLES */
  .detail-cards-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; margin-top: 20px; }
  .cluster-card { border-radius: 10px; padding: 16px; border-top: 5px solid #ccc; background: #fafbfc; box-shadow: 0 2px 8px rgba(0,0,0,0.04); font-size: 12.8px; line-height: 1.5; }
  .card-c0 { border-top-color: #27ae60; background: #f4fbf7; }
  .card-c1 { border-top-color: #2980b9; background: #f4f8fb; }
  .card-c2 { border-top-color: #c0392b; background: #fdf5f4; }
  .cluster-card h4 { margin: 0 0 8px 0; font-size: 15px; font-weight: 700; }
  .metric-pill { display: inline-block; padding: 3px 8px; border-radius: 4px; font-weight: 700; font-size: 11.5px; margin-bottom: 6px; }
  .pill-green { background: #d4efdf; color: #196f3d; }
  .pill-blue { background: #d4e6f1; color: #1a5276; }
  .pill-red { background: #fadbd8; color: #922b21; }

  #plotDiv { height: 620px; width: 100%; }

  table.data-table { width: 100%; border-collapse: collapse; margin-top: 15px; font-size: 12.8px; }
  table.data-table th, table.data-table td { border: 1px solid #e2e8f0; padding: 9px 12px; text-align: left; }
  table.data-table th { background: #1f618d; color: white; font-weight: 600; }
  table.data-table tr:nth-child(even) { background: #f8fafc; }
  .badge-cluster { padding: 3px 8px; border-radius: 4px; font-weight: 700; font-size: 11px; color: white; }
  .bc-green { background: #27ae60; }
  .bc-orange { background: #f39c12; }
  .bc-red { background: #e74c3c; }
  .bc-blue { background: #2980b9; }

  .btn-toggle-img { padding: 6px 12px; background: #34495e; color: white; border: none; border-radius: 6px; font-size: 12px; cursor: pointer; font-weight: bold; }
  .btn-toggle-img:hover { background: #2c3e50; }
  .img-preview-box { text-align: center; margin-top: 15px; padding: 12px; background: #eaeded; border-radius: 8px; display: none; }
  .img-preview-box img { max-width: 100%; border-radius: 6px; box-shadow: 0 3px 10px rgba(0,0,0,0.15); }

  .footer { text-align: center; color: #7f8c8d; font-size: 12px; margin-top: 25px; line-height: 1.6; }
</style>
</head>
<body>

<div class="header">
  <h1>Dashboard Geospasial & Penambangan Data K-Means Clustering</h1>
  <p>Analisis Multidimensi Tingkat Keterlambatan Pencatatan Akta Kelahiran pada Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna (Tahun Pelayanan 2025)</p>
  <div class="badges-row">
    <span class="badge-tag bg-tag-red">✓ Analisis Spasial: Peta Geospasial 16 Kecamatan (Esri Suite)</span>
    <span class="badge-tag bg-tag-blue">✓ Model Sosio-Ekonomi: Centroid Bintang, Elips & Anotasi Bivariat</span>
    <span class="badge-tag bg-tag-green">✓ Evaluasi Valid: Spasial Silh = 0.6377 & Individu Silh = 0.5524</span>
  </div>
</div>

<div class="grid-stats">
  <div class="stat-box bg-navy">
    <h3>131 Berkas</h3>
    <p>Total Berkas Pelayanan 2025</p>
  </div>
  <div class="stat-box bg-green">
    <h3>Cluster 0 (Compliance)</h3>
    <p>2 Kecamatan (B. Tengah, P. Laut)</p>
  </div>
  <div class="stat-box bg-orange">
    <h3>Cluster 1 (Moderate)</h3>
    <p>7 Kecamatan (B. Timur, Barat, dll)</p>
  </div>
  <div class="stat-box bg-red">
    <h3>Cluster 2 (High-Delay)</h3>
    <p>7 Kecamatan (Midai, Serasan, dll)</p>
  </div>
</div>

<div class="tab-container">
  <div class="tab-nav">
    <button class="tab-btn active" onclick="openTab(event, 'tabMap')">🗺️ PETA GEOSPATIAL 16 KECAMATAN (LEAFLET)</button>
    <button class="tab-btn" onclick="openTab(event, 'tabScatter')">📈 MODEL SOSIO-EKONOMI INDIVIDU (131 BERKAS)</button>
    <button class="tab-btn" onclick="openTab(event, 'tabTable')">📋 TABEL DATA & AUDIT METRIK MODEL</button>
  </div>

  <!-- TAB 1: PETA GEOSPATIAL (LEAFLET ESRI SUITE 100% BEBAS WATERMARK & API KEY) -->
  <div id="tabMap" class="tab-content active">
    <div class="map-toolbar">
      <div style="font-size: 13px; color: #2c3e50;">
        <b>Peta Interaktif Kepulauan Natuna:</b> Menggunakan basemap <i>Esri World Street Map, Citra Satelit & Topografi</i> yang 100% bebas dari pembatasan akses lokal (403 block) dan tanpa memerlukan API Key (bebas watermark). Klik lingkaran kecamatan untuk melihat statistik lengkap.
      </div>
      <div class="filter-group">
        <label for="filterClusterMap">Filter Klaster Peta:</label>
        <select id="filterClusterMap" class="filter-select" onchange="filterMapMarkers(this.value)">
          <option value="ALL">Semua Klaster (16 Kecamatan)</option>
          <option value="Cluster 0 (High-Compliance)">🟢 Cluster 0: High-Compliance</option>
          <option value="Cluster 1 (Moderate)">🟠 Cluster 1: Moderate</option>
          <option value="Cluster 2 (High-Delay)">🔴 Cluster 2: High-Delay</option>
        </select>
        <button class="btn-toggle-img" onclick="toggleImg('boxPetaPng')">🖼️ Lihat Peta Cetak 300 DPI</button>
      </div>
    </div>

    <div id="boxPetaPng" class="img-preview-box">
      <p style="margin: 0 0 8px 0; font-weight: bold; font-size: 13px;">Peta Geospatial Resolusi Tinggi 300 DPI (Sesuai Naskah Laporan Akhir FinPD):</p>
      <img src="peta_geospatial_klaster_natuna.png" alt="Peta Geospatial Klaster Natuna 300 DPI" />
    </div>

    <div id="map"></div>

    <div style="margin-top: 12px; display: flex; gap: 15px; font-size: 12px; flex-wrap: wrap;">
      <div><b>Legenda Warna:</b></div>
      <div><span style="color: #27ae60; font-size: 15px;">●</span> <b>Cluster 0:</b> Tingkat Kepatuhan Tinggi (LU &gt; 65%, Median 1 hari)</div>
      <div><span style="color: #f39c12; font-size: 15px;">●</span> <b>Cluster 1:</b> Kepatuhan Sedang (Median 148–636 hari / 1–2 tahun)</div>
      <div><span style="color: #e74c3c; font-size: 15px;">●</span> <b>Cluster 2:</b> Keterlambatan Kronis/SPTJM (Median &gt; 7.800 hari / belasan tahun)</div>
      <div style="margin-left: auto; color: #7f8c8d;">*Ukuran lingkaran proporsional terhadap volume berkas permohonan.</div>
    </div>
  </div>

  <!-- TAB 2: SCATTER PLOT MODEL SOSIO-EKONOMI INDIVIDU -->
  <div id="tabScatter" class="tab-content">
    <div class="map-toolbar">
      <div style="font-size: 13px; color: #2c3e50;">
        <b>Model Sosio-Ekonomi Individu (131 Berkas):</b> Analisis bivariat Sumbu X (Hari Usia Orang Tua) vs Sumbu Y (Hari Keterlambatan Pelaporan). Dilengkapi <b>Centroid Bintang Kuning (⭐)</b>, <b>Garis Elips Klaster</b>, dan <b>Anotasi Penjelasan Karakteristik Profesi</b>.
      </div>
      <button class="btn-toggle-img" onclick="toggleImg('boxScatterPng')">🖼️ Lihat Grafik Klaster Sosio-Ekonomi (300 DPI)</button>
    </div>

    <div id="boxScatterPng" class="img-preview-box">
      <p style="margin: 0 0 8px 0; font-weight: bold; font-size: 13px;">Grafik Klaster Sosio-Ekonomi Individu 300 DPI (Sumbu X vs Sumbu Y):</p>
      <img src="scatter_model_sosioekonomi_individu.png" alt="Grafik Model Sosio-Ekonomi Individu" />
    </div>

    <div id="plotDiv"></div>

    <!-- DETAIL KARTU SOSIO-EKONOMI PER KLASTER -->
    <h3 style="margin: 25px 0 12px 0; font-size: 16px;">Detail Karakteristik Sosio-Ekonomi & Profil Yuridis Per Klaster</h3>
    <div class="detail-cards-grid">
      <!-- KLASTER 0 -->
      <div class="cluster-card card-c0">
        <h4>🟢 Klaster 0: Tepat Waktu & Balita Dini (Dominan Lahir Umum)</h4>
        <div class="metric-pill pill-green">Ukuran: n = 56 Berkas (42.7%)</div>
        <p><b>Profil Demografi Orang Tua:</b><br>
        Rata-rata Usia Ortu: <b>27.3 Tahun</b> (9.983 Hari)<br>
        Rentang Usia: 20.6 s.d. 32.6 Tahun (Usia biologis produktif awal).</p>
        
        <p><b>Karakteristik Keterlambatan:</b><br>
        Median Keterlambatan: <b>82 Hari</b> (~0.2 Tahun / Rata-rata 2.4 Tahun). Memuat seluruh kelahiran baru tepat waktu (&le;60 hari).</p>

        <p><b>Sosio-Ekonomi & Profesi Dominan:</b><br>
        Didominasi wiraswasta muda, nelayan modern pulau utama, dan pedagang. Kesadaran administrasi tinggi sejak persalinan di faskes (RSUD / Polindes).</p>

        <p><b>Instrumen Yuridis & Bukti:</b><br>
        Mayoritas melampirkan Surat Keterangan Lahir (SKL) Medis dokter/bidan resmi tanpa memerlukan surat pernyataan SPTJM.</p>
        
        <p><b>Rekomendasi Kebijakan:</b><br>
        Dipertahankan melalui pelayanan loket reguler dan integrasi pelaporan faskes rumah sakit/puskesmas.</p>
      </div>

      <!-- KLASTER 1 -->
      <div class="cluster-card card-c1">
        <h4>🔵 Klaster 1: Terlambat Sedang (Balita - Menjelang Sekolah)</h4>
        <div class="metric-pill pill-blue">Ukuran: n = 40 Berkas (30.5%)</div>
        <p><b>Profil Demografi Orang Tua:</b><br>
        Rata-rata Usia Ortu: <b>38.6 Tahun</b> (14.082 Hari)<br>
        Rentang Usia: 33.1 s.d. 47.6 Tahun (Keluarga matang/dewasa).</p>
        
        <p><b>Karakteristik Keterlambatan:</b><br>
        Median Keterlambatan: <b>148 Hari</b> (~0.4 Tahun / Rata-rata 4.1 Tahun). Keterlambatan anak usia prasekolah menjelang jenjang PAUD/SD.</p>

        <p><b>Sosio-Ekonomi & Profesi Dominan:</b><br>
        Didominasi pegawai negeri (PNS), honorer daerah, prajurit TNI/Polri, dan petani kebun. Mengurus akta secara reaktif ketika anak dipersyaratkan masuk sekolah.</p>

        <p><b>Instrumen Yuridis & Bukti:</b><br>
        Kombinasi SKL faskes dan surat keterangan desa dengan kelengkapan buku nikah resmi orang tua.</p>

        <p><b>Rekomendasi Kebijakan:</b><br>
        Kerja sama lintas instansi dengan Dinas Pendidikan untuk integrasi pendaftaran PPDB berbasis akta lahir otomatis.</p>
      </div>

      <!-- KLASTER 2 -->
      <div class="cluster-card card-c2">
        <h4>🔴 Klaster 2: Terlambat Historis (Dewasa SPTJM)</h4>
        <div class="metric-pill pill-red">Ukuran: n = 35 Berkas (26.7%)</div>
        <p><b>Profil Demografi Orang Tua:</b><br>
        Usia Ortu Saat Anak Lahir: <b>30.5 Tahun</b> (11.140 Hari)<br>
        Usia Pemohon Saat Mengurus: <b>32 s.d. 85 Tahun</b> (Warga Dewasa s.d. Lansia).</p>
        
        <p><b>Karakteristik Keterlambatan:</b><br>
        Median Keterlambatan: <b>17.991 Hari</b> (~49.3 Tahun), Rata-rata <b>17.775 Hari</b> (~48.7 Tahun). Rekor tertinggi mencapai 31.057 hari (~85 tahun).</p>

        <p><b>Sosio-Ekonomi & Profesi Dominan:</b><br>
        Penduduk asli pulau-pulau 3T (Midai, Suak Midai, Serasan, Subi, Pulau Tiga) berprofesi nelayan tradisional dan buruh lepas. Terkendala biaya transportasi kapal ke Ranai selama puluhan tahun.</p>

        <p><b>Instrumen Yuridis & Bukti:</b><br>
        100% menggunakan Surat Pernyataan Tanggung Jawab Mutlak (SPTJM Kebenaran Kelahiran) karena penolong lahir masa lampau (dukun beranak) telah wafat.</p>

        <p><b>Rekomendasi Kebijakan:</b><br>
        Intervensi darurat melalui <b>Kapal Pelayanan Keliling (Mobile Service Boat)</b> dan <b>Sidang Terpadu Isbat/SPTJM Massal</b> tingkat desa.</p>
      </div>
    </div>
  </div>

  <!-- TAB 3: TABEL -->
  <div id="tabTable" class="tab-content">
    <h3>Tabel Hasil Pengelompokkan 16 Kecamatan Kabupaten Natuna</h3>
    <table class="data-table">
      <thead>
        <tr>
          <th>Kecamatan</th>
          <th>Klaster Spasial</th>
          <th>Total Berkas</th>
          <th>Rasio Lahir Umum (LU)</th>
          <th>Median Keterlambatan</th>
          <th>Rekomendasi Kebijakan Disdukcapil</th>
        </tr>
      </thead>
      <tbody>
        __TABLE_ROWS__
      </tbody>
    </table>

    <h3 style="margin-top: 30px;">Ringkasan Validasi Metrik Evaluasi Model K-Means</h3>
    <table class="data-table">
      <thead>
        <tr>
          <th>Model Data Mining</th>
          <th>Entitas Data (N)</th>
          <th>Fitur Masukan</th>
          <th>Nilai K</th>
          <th>Silhouette Score</th>
          <th>Davies-Bouldin Index</th>
          <th>Status Kelayakan</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><b>Model 1 (Spasial Wilayah 16 Kecamatan)</b></td>
          <td>16 Kecamatan</td>
          <td>Persentase LU, Median Durasi Hari</td>
          <td>K = 3</td>
          <td><b>0.6377</b></td>
          <td><b>0.4710</b></td>
          <td><span class="badge-cluster bc-green">Sangat Baik (Dense & Well-Separated)</span></td>
        </tr>
        <tr>
          <td><b>Model 2 (Sosio-Ekonomi Pemohon Individu)</b></td>
          <td>131 Berkas</td>
          <td>Hari Usia Ortu (X), Durasi Keterlambatan (Y)</td>
          <td>K = 3</td>
          <td><b>0.5524</b></td>
          <td><b>0.5924</b></td>
          <td><span class="badge-cluster bc-green">Valid & Optimal (Dense & Well-Separated)</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<div class="footer">
  &copy; 2026 Tim Penambangan Data PD-NTN25 | Universitas Maritim Raja Ali Haji (UMRAH) Tanjungpinang<br>
  Ketua Tim: Ridho Ramadani E (2401020121) | Narasumber Mitra: Ibu Julida, S.Sos (Disdukcapil Kabupaten Natuna)
</div>

<script>
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].classList.remove("active");
  }
  tablinks = document.getElementsByClassName("tab-btn");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].classList.remove("active");
  }
  document.getElementById(tabName).classList.add("active");
  evt.currentTarget.classList.add("active");

  if (tabName === 'tabMap') {
    setTimeout(function() { map.invalidateSize(); }, 250);
  }
  if (tabName === 'tabScatter') {
    setTimeout(function() { Plotly.Plots.resize('plotDiv'); }, 250);
  }
}

function toggleImg(elemId) {
  var el = document.getElementById(elemId);
  if (el.style.display === "block") {
    el.style.display = "none";
  } else {
    el.style.display = "block";
  }
}

// ==============================================================================
// 1. LEAFLET MAP INITIALIZATION (ESRI PROFESSIONAL BASEMAPS - 100% BEBAS WATERMARK & BEBAS API KEY)
// ==============================================================================
const map = L.map('map').setView([3.8, 108.4], 8);

// Basemap 1: Esri World Street Map (Peta Administrasi & Wilayah Bebas Watermark / API Key)
const esriStreet = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, TomTom | Disdukcapil Natuna',
  maxZoom: 18
}).addTo(map);

// Basemap 2: Esri World Imagery (Citra Satelit Asli Kepulauan Maritim)
const esriSat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
  maxZoom: 18
});

// Basemap 3: Esri World Topographic (Topografi & Kontur Wilayah)
const esriTopo = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: USGS, Esri, TANA, DeLorme, NAVTEQ',
  maxZoom: 18
});

// Basemap 4: Esri Ocean Basemap (Batimetri Kelautan & Kepulauan Maritim 3T)
const esriOcean = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: GEBCO, NOAA, CHS, OSU, UNH, CSUMB, National Geographic, DeLorme, NAVTEQ, and Esri',
  maxZoom: 13
});

L.control.layers({
  "Peta Wilayah & Jalan (Esri Street Map)": esriStreet,
  "Citra Satelit Maritim (Esri Satellite)": esriSat,
  "Peta Topografi & Kontur (Esri Topo)": esriTopo,
  "Batimetri Kelautan (Esri Ocean)": esriOcean
}).addTo(map);

const spasialData = __SPASIAL_DATA__;
let markerLayerGroup = L.layerGroup().addTo(map);

function renderMarkers(dataToShow) {
  markerLayerGroup.clearLayers();
  dataToShow.forEach(d => {
    let color = '#27ae60';
    if (d.cluster_label.includes('Moderate')) color = '#f39c12';
    if (d.cluster_label.includes('High-Delay')) color = '#e74c3c';

    let radius = Math.max(12, Math.min(32, d.total_berkas * 1.5 + 10));

    const circle = L.circleMarker([d.lat, d.lon], {
      color: '#1a202c',
      weight: 1.5,
      fillColor: color,
      fillOpacity: 0.88,
      radius: radius
    });

    const popupContent = `
      <div style="font-size: 13px; line-height: 1.45; min-width: 200px;">
        <h4 style="margin: 0 0 5px 0; color: #1a365d; border-bottom: 2px solid ${color}; padding-bottom: 3px;">${d.kecamatan}</h4>
        <b>Klaster:</b> <span style="color: ${color}; font-weight: bold;">${d.cluster_label}</span><br>
        <b>Total Berkas:</b> ${d.total_berkas > 0 ? d.total_berkas + ' permohonan' : '0 permohonan (Kecamatan Pemekaran)'}<br>
        <b>Lahir Tepat Waktu (LU):</b> ${d.persentase_lu.toFixed(1)}%<br>
        <b>Median Keterlambatan:</b> ${d.median_durasi.toFixed(0)} hari (${(d.median_durasi/365.25).toFixed(1)} tahun)<br>
        <hr style="margin: 6px 0;">
        <small><b>Rekomendasi Disdukcapil:</b><br>${d.cluster_label.includes('High-Delay') ? '🚢 Prioritas Kapal Pelayanan Keliling & Verifikasi SPTJM' : '🏛️ Pelayanan Loket Terpadu Reguler'}</small>
      </div>
    `;
    circle.bindPopup(popupContent);
    markerLayerGroup.addLayer(circle);
  });
}

renderMarkers(spasialData);

function filterMapMarkers(clusterChoice) {
  if (clusterChoice === 'ALL') {
    renderMarkers(spasialData);
  } else {
    const filtered = spasialData.filter(d => d.cluster_label === clusterChoice);
    renderMarkers(filtered);
  }
}

// ==============================================================================
// 2. PLOTLY SCATTER PLOT INITIALIZATION (MODEL SOSIO-EKONOMI INDIVIDU)
// ==============================================================================
const dataRaw = __INDIV_DATA__;
const centroidsRaw = __CENTROID_DATA__;

const clusterNames = [
  'Klaster 0: Tepat Waktu (Lahir Umum)',
  'Klaster 1: Terlambat Sedang (Balita-Anak)',
  'Klaster 2: Terlambat Historis (Dewasa SPTJM)'
];
const colors = ['#27ae60', '#2980b9', '#c0392b'];

// 1. Data Points Traces
const traces = clusterNames.map((cName, idx) => {
  const filtered = dataRaw.filter(d => d.Cluster_Label === cName);
  return {
    x: filtered.map(d => d.Hari_Usia_Ortu),
    y: filtered.map(d => d.Durasi_Pelaporan_Hari),
    mode: 'markers',
    type: 'scatter',
    name: cName,
    marker: { size: 10, color: colors[idx], opacity: 0.82, line: { color: '#1a252f', width: 1 } },
    text: filtered.map(d => `<b>Berkas:</b> ${d.No_Berkas}<br><b>Kecamatan:</b> ${d.Kecamatan}<br><b>Desa:</b> ${d.Desa_Kelurahan}<br><b>Usia Ortu:</b> ${d.Usia_Rata_Ortu_Tahun} Tahun (${d.Hari_Usia_Ortu} Hari)<br><b>Keterlambatan:</b> ${d.Durasi_Pelaporan_Hari} Hari (${(d.Durasi_Pelaporan_Hari/365.25).toFixed(1)} Thn)<br><b>Status:</b> ${d.Status_Kepatuhan}<br><b>Profesi:</b> ${d.Pekerjaan_Ayah}`),
    hoverinfo: 'text'
  };
});

// 2. Centroid Star Markers Trace
const centroidTrace = {
  x: centroidsRaw.map(c => c.centroid_x),
  y: centroidsRaw.map(c => c.centroid_y),
  mode: 'markers',
  type: 'scatter',
  name: 'Titik Pusat (Centroid ⭐)',
  marker: {
    symbol: 'star',
    size: 22,
    color: '#f1c40f',
    line: { color: '#000000', width: 2 }
  },
  text: centroidsRaw.map(c => `<b>⭐ CENTROID ${c.cluster_label}</b><br>Usia Ortu: ${c.usia_tahun.toFixed(1)} Tahun (${c.centroid_x.toFixed(0)} Hari)<br>Rata-rata Keterlambatan: ${c.durasi_tahun.toFixed(1)} Tahun (${c.centroid_y.toFixed(0)} Hari)`),
  hoverinfo: 'text'
};
traces.push(centroidTrace);

const layout = {
  title: { 
    text: 'Analisis Klaster Sosio-Ekonomi: Sumbu X (Usia Ortu Hari) vs Sumbu Y (Keterlambatan Hari)', 
    font: { size: 15, weight: 'bold', color: '#1a365d' } 
  },
  xaxis: { 
    title: 'Sumbu X: Usia Orang Tua Saat Anak Lahir (Hari Kalender)', 
    gridcolor: '#e9ecef',
    zeroline: true,
    zerolinecolor: '#95a5a6'
  },
  yaxis: { 
    title: 'Sumbu Y: Durasi Keterlambatan Pelaporan (Hari Kalender)', 
    gridcolor: '#e9ecef',
    zeroline: true,
    zerolinecolor: '#95a5a6'
  },
  hovermode: 'closest',
  plot_bgcolor: '#ffffff',
  paper_bgcolor: '#ffffff',
  legend: { orientation: 'h', y: -0.18, x: 0.05 },
  
  // GARIS ELIPS BATAS KLASTER SOSIO-EKONOMI
  shapes: [
    // Elips Klaster 0 (Tepat Waktu & Balita Dini)
    {
      type: 'circle',
      xref: 'x', yref: 'y',
      x0: 7000, y0: -1000,
      x1: 12500, y1: 11500,
      line: { color: '#27ae60', width: 2, dash: 'dash' },
      fillcolor: 'rgba(39, 174, 96, 0.05)'
    },
    // Elips Klaster 1 (Terlambat Sedang Balita-Anak)
    {
      type: 'circle',
      xref: 'x', yref: 'y',
      x0: 11800, y0: -1000,
      x1: 17800, y1: 14500,
      line: { color: '#2980b9', width: 2, dash: 'dash' },
      fillcolor: 'rgba(41, 128, 185, 0.05)'
    },
    // Elips Klaster 2 (Terlambat Historis Dewasa SPTJM)
    {
      type: 'circle',
      xref: 'x', yref: 'y',
      x0: 5500, y0: 11000,
      x1: 14000, y1: 32000,
      line: { color: '#c0392b', width: 2, dash: 'dash' },
      fillcolor: 'rgba(192, 57, 43, 0.05)'
    }
  ],

  // ANOTASI PANAH KARAKTERISTIK SOSIO-EKONOMI
  annotations: [
    {
      x: 9983, y: 892,
      xref: 'x', yref: 'y',
      text: '<b>Wiraswasta & Nelayan Muda</b><br>(Pelaporan Tertib LU/Balita Dini)',
      showarrow: true,
      arrowhead: 2,
      arrowsize: 1,
      arrowwidth: 1.5,
      arrowcolor: '#27ae60',
      ax: -70, ay: -50,
      bordercolor: '#27ae60',
      borderwidth: 1.5,
      borderpad: 4,
      bgcolor: '#eafaf1',
      font: { size: 11, color: '#196f3d' }
    },
    {
      x: 14082, y: 1482,
      xref: 'x', yref: 'y',
      text: '<b>PNS, TNI & Petani</b><br>(Menunda Menjelang Usia Sekolah)',
      showarrow: true,
      arrowhead: 2,
      arrowsize: 1,
      arrowwidth: 1.5,
      arrowcolor: '#2980b9',
      ax: 80, ay: -50,
      bordercolor: '#2980b9',
      borderwidth: 1.5,
      borderpad: 4,
      bgcolor: '#ebf5fb',
      font: { size: 11, color: '#1a5276' }
    },
    {
      x: 11140, y: 17775,
      xref: 'x', yref: 'y',
      text: '<b>Warga Dewasa/Lansia Pulau 3T</b><br>(100% Instrumen SPTJM)',
      showarrow: true,
      arrowhead: 2,
      arrowsize: 1,
      arrowwidth: 1.5,
      arrowcolor: '#c0392b',
      ax: 90, ay: 30,
      bordercolor: '#c0392b',
      borderwidth: 1.5,
      borderpad: 4,
      bgcolor: '#fdedec',
      font: { size: 11, color: '#922b21' }
    }
  ]
};

Plotly.newPlot('plotDiv', traces, layout);
</script>
</body>
</html>
"""

final_html = template.replace("__TABLE_ROWS__", rows_html)
final_html = final_html.replace("__SPASIAL_DATA__", json_spasial)
final_html = final_html.replace("__INDIV_DATA__", json_indiv)
final_html = final_html.replace("__CENTROID_DATA__", json_cent)

out_file = os.path.join(PROJECT_ROOT, '06_DEPLOYMENT', 'dashboard_interaktif_kmeans_dosen.html')
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Dashboard berhasil diperbarui dengan sukses di:", out_file)
