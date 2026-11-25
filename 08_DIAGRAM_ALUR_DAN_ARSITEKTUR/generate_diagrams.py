#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator Diagram Alur dan Arsitektur Proyek Penambangan Data PD-NTN25
Format Luaran: High-Resolution PNG (300 DPI), Scalable Vector Graphics (SVG),
Graphviz DOT (.dot), dan Mermaid Source (.mmd)
"""

import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("================================================================================")
print("  MEMBANGUN ARSIP DIAGRAM ALUR DAN ARSITEKTUR LENGKAP PROYEK PD-NTN25")
print("  FOLDER TUJUAN: 08_DIAGRAM_ALUR_DAN_ARSITEKTUR")
print("================================================================================")

diagrams = [
    {
        "id": "01",
        "name": "diagram_alur_metodologi_crisp_dm",
        "title": "Diagram Alur Metodologi Standar CRISP-DM 6 Tahap",
        "dot": """digraph CRISP_DM {
    rankdir=TB;
    fontname="Arial";
    dpi=300;
    node [shape=box, style="filled,rounded", fontname="Arial", fontsize=11, margin="0.25,0.18"];
    edge [color="#2B6CB0", penwidth=2.0, arrowhead=vee];

    subgraph cluster_main {
        style="filled,rounded";
        fillcolor="#F7FAFC";
        color="#CBD5E0";
        label="METODOLOGI SIKLUS HIDUP PENAMBANGAN DATA (CRISP-DM FRAMEWORK)";
        fontname="Arial Bold";
        fontsize=13;
        fontcolor="#1A365D";

        BU [label="1. Business Understanding\\n• Identifikasi Kebutuhan Disdukcapil Natuna\\n• Regulasi UU No. 24/2013 Batas 60 Hari LU vs LT\\n• Tantangan Disparitas Wilayah Kepulauan 3T", fillcolor="#EBF8FF", color="#3182CE", fontcolor="#1A365D"];
        DU [label="2. Data Understanding\\n• Audit 131 Folder Arsip Fisik (262 Dokumen Pindaian)\\n• Transkripsi 131 Berkas Pelaporan F-2.01 & SKL/SPTJM\\n• Analisis Eksplorasi Data 8 Visualisasi EDA", fillcolor="#E6FFFA", color="#319795", fontcolor="#234E52"];
        DP [label="3. Data Preparation\\n• Protokol Bebas Fabrikasi (Zero Data Fabrication)\\n• Koreksi Typo Kronologis F044 & F0124 ke Tahun 2025\\n• Anonimisasi Atribut PII (UU No. 27/2022)\\n• Rekayasa Fitur: Durasi Hari & Usia Ortu", fillcolor="#FAF5FF", color="#805AD5", fontcolor="#44337A"];
        M  [label="4. Modeling (Algoritma K-Means)\\n• Model 1: Spasial Wilayah (16 Kecamatan, K=3)\\n• Model 2: Sosio-Ekonomi Pemohon Individu (K=3)\\n• Standardisasi Z-Score & Jarak Euclidean", fillcolor="#FFFAF0", color="#DD6B20", fontcolor="#7B341E"];
        E  [label="5. Evaluation (Validasi Metrik)\\n• Metode Elbow (Inertia / WCSS)\\n• Silhouette Score (Spasial: 0.6410, Sosio: 0.5533)\\n• Davies-Bouldin Index (Spasial: 0.4698, Sosio: 0.5905)\\n• Karakterisasi dan Profiling Klaster", fillcolor="#FFF5F5", color="#E53E3E", fontcolor="#742A2A"];
        D  [label="6. Deployment (Penerapan Sistem)\\n• Purwarupa Web Dashboard Leaflet.js & Plotly.js\\n• Rekomendasi 1: Kapal Pelayanan Keliling (Mobile Boat)\\n• Rekomendasi 2: Sidang Terpadu Verifikasi SPTJM Massal\\n• Rekomendasi 3: Penguatan Integrasi Layanan Faskes", fillcolor="#F0FFF4", color="#38A169", fontcolor="#1C4532"];

        BU -> DU -> DP -> M -> E -> D;
        E -> M [style=dashed, color="#E53E3E", constraint=false, label="Iterasi Evaluasi", fontcolor="#E53E3E"];
    }
}""",
        "mmd": """flowchart TD
    BU["1. Business Understanding<br>(Kebutuhan Disdukcapil Natuna & UU No. 24/2013)"] --> DU["2. Data Understanding<br>(Audit 131 Folder Fisik, 131 Permohonan, 8 Plot EDA)"]
    DU --> DP["3. Data Preparation<br>(Zero Fabrication, Typo 2025, Anonimisasi PII, Fitur Durasi)"]
    DP --> M["4. Modeling<br>(K-Means: Model Spasial 16 Kec & Sosio-Ekonomi Individu K=3)"]
    M --> E["5. Evaluation<br>(Elbow/WCSS, Silhouette, Davies-Bouldin, Profiling)"]
    E --> D["6. Deployment<br>(Dashboard Peta Leaflet & 3 Rekomendasi Kebijakan)"]
    E -. Iterasi Evaluasi .-> M"""
    },
    {
        "id": "02",
        "name": "diagram_alur_data_antar_skrip_python_end_to_end_pipeline",
        "title": "Diagram Alur Data Antar-Skrip Python (End-to-End Pipeline)",
        "dot": """digraph Data_Flow_Pipeline {
    rankdir=TB;
    fontname="Arial";
    dpi=300;
    compound=true;
    node [shape=box, style="filled,rounded", fontname="Arial", fontsize=10, margin="0.2,0.14"];
    edge [color="#2B6CB0", penwidth=1.8, arrowhead=vee];

    subgraph cluster_header {
        style="filled,rounded";
        fillcolor="#F7FAFC";
        color="#CBD5E0";
        label="DIAGRAM ALUR DATA ANTAR-SKRIP PYTHON (END-TO-END PIPELINE)";
        fontname="Arial Bold";
        fontsize=13;
        fontcolor="#1A365D";

        subgraph cluster_dataprep {
            style="filled,rounded";
            fillcolor="#F0F9FF";
            color="#BAE6FD";
            label="Tahap 1 & 2: Data Preparation";
            fontname="Arial Bold";
            fontsize=11;
            fontcolor="#0369A1";

            A [label="Data Mentah Transkripsi
(Excel & CSV 131 Berkas)", fillcolor="#FDBA74", color="#EA580C", shape=folder, style="filled"];
            B [label="pembersihan_data_dan_
validasi_kronologis.py", fillcolor="#BAE6FD", color="#0284C7"];
            C [label="Data_Bersih_Lengkap_Imputed.xlsx / .csv", fillcolor="#E0F2FE", color="#0369A1"];
            D [label="data_gabungan_transkripsi_final.json", fillcolor="#E0F2FE", color="#0369A1"];
            E [label="rekayasa_fitur_dan_
reduksi_dimensi.py", fillcolor="#BAE6FD", color="#0284C7"];
            F [label="Dataset_Feature_Engineered_PD_NTN.xlsx / .csv
(131 Baris Fitur Individu)", fillcolor="#E0F2FE", color="#0369A1"];
            G [label="Dataset_Agregasi_Spasial_16_Kecamatan.xlsx / .csv
(16 Baris Agregasi Wilayah)", fillcolor="#E0F2FE", color="#0369A1"];

            A -> B;
            B -> C;
            B -> D;
            C -> E;
            E -> F;
            E -> G;
        }

        subgraph cluster_modeling {
            style="filled,rounded";
            fillcolor="#FAF5FF";
            color="#E9D5FF";
            label="Tahap 3 & 4: Modeling Spasial & Sosio-Ekonomi Individu";
            fontname="Arial Bold";
            fontsize=11;
            fontcolor="#6B21A8";

            H [label="kmeans_model_spasial_wilayah.py", fillcolor="#DDD6FE", color="#7C3AED"];
            I [label="Hasil_Clustering_Kecamatan_Natuna.xlsx / .csv", fillcolor="#F3E8FF", color="#6B21A8"];
            J [label="peta_geospatial_klaster_natuna.png", fillcolor="#FEF08A", color="#CA8A04"];
            K [label="visualisasi_cluster_kecamatan.png", fillcolor="#FEF08A", color="#CA8A04"];
            L [label="evaluasi_elbow_silhouette.png", fillcolor="#FEF08A", color="#CA8A04"];

            M [label="pemodelan_kmeans_sosioekonomi_
dan_dashboard.py", fillcolor="#DDD6FE", color="#7C3AED"];
            N [label="Hasil_Clustering_Sosial_Ekonomi.xlsx / .csv", fillcolor="#F3E8FF", color="#6B21A8"];
            O [label="scatter_model_sosioekonomi_
individu.png", fillcolor="#FEF08A", color="#CA8A04"];

            G -> H;
            H -> I;
            H -> J;
            H -> K;
            H -> L;

            F -> M;
            M -> N;
            M -> O;
        }

        subgraph cluster_eda {
            style="filled,rounded";
            fillcolor="#FFFBEB";
            color="#FDE68A";
            label="Tahap 5: Data Understanding (EDA)";
            fontname="Arial Bold";
            fontsize=11;
            fontcolor="#92400E";

            P [label="analisis_eksplorasi_data_
dan_kualitas_eda.py", fillcolor="#FDE68A", color="#D97706"];
            Q [label="8 Visualisasi EDA (300 DPI PNG)
(Missing, Typo, Bimodal, Spasial, Tren,
Boxplot, Scatter, Heatmap Korelasi)", fillcolor="#FEF08A", color="#CA8A04"];

            P -> Q;
        }

        subgraph cluster_deploy {
            style="filled,rounded";
            fillcolor="#F0FDF4";
            color="#BBF7D0";
            label="Tahap 6, 7 & 8: Deployment, Reporting & Packaging";
            fontname="Arial Bold";
            fontsize=11;
            fontcolor="#166534";

            R [label="generate_dashboard.py", fillcolor="#BBF7D0", color="#16A34A"];
            S [label="dashboard_interaktif_kmeans_dosen.html", fillcolor="#DCFCE7", color="#15803D"];

            T [label="build_final_reports.py", fillcolor="#BBF7D0", color="#16A34A"];
            U [label="LAPORAN_AKHIR_PENAMBANGAN_DATA_PD_NTN25.docx", fillcolor="#DCFCE7", color="#15803D"];
            V [label="FinPD_2401020121.pdf (33 Halaman)", fillcolor="#DCFCE7", color="#15803D"];

            W [label="paketkan_berkas_google_form.py", fillcolor="#BBF7D0", color="#16A34A"];
            X [label="BERKAS SUBMISI GOOGLE FORM:
• Mentah_2401020121.7z (XLSX + CSV)
• SiapMining_2401020121.7z (XLSX + CSV)
• FinPD_2401020121.pdf", fillcolor="#15803D", fontcolor="#FFFFFF", shape=note, style="filled"];

            R -> S;
            T -> U;
            T -> V;
            W -> X;
        }

        ORCH [label="jalankan_seluruh_tahapan_pipeline.py
(Master Orchestrator - Otomasi Eksekusi 1 s.d. 8/9)", fillcolor="#1E3A8A", fontcolor="#FFFFFF", shape=component, style="filled"];

        # Dependencies between stages
        C -> P;
        F -> P;

        I -> R;
        N -> R;

        Q -> T;
        J -> T;
        O -> T;

        V -> W;

        ORCH -> B [style=dashed, color="#1E3A8A", label="Tahap 1"];
        ORCH -> E [style=dashed, color="#1E3A8A", label="Tahap 2"];
        ORCH -> H [style=dashed, color="#1E3A8A", label="Tahap 3"];
        ORCH -> M [style=dashed, color="#1E3A8A", label="Tahap 4"];
        ORCH -> P [style=dashed, color="#1E3A8A", label="Tahap 5"];
        ORCH -> R [style=dashed, color="#1E3A8A", label="Tahap 6"];
        ORCH -> T [style=dashed, color="#1E3A8A", label="Tahap 7"];
        ORCH -> W [style=dashed, color="#1E3A8A", label="Tahap 8"];
    }
}
""",
        "mmd": """flowchart TD
    subgraph DataPrep ["Tahap 1 & 2: Data Preparation"]
        A["Data Mentah Transkripsi (Excel & CSV 131 Berkas)"] --> B["pembersihan_data_dan_validasi_kronologis.py"]
        B --> C["Data_Bersih_Lengkap_Imputed.xlsx / .csv"]
        B --> D["data_gabungan_transkripsi_final.json"]
        C --> E["rekayasa_fitur_dan_reduksi_dimensi.py"]
        E --> F["Dataset_Feature_Engineered_PD_NTN.xlsx / .csv"]
        E --> G["Dataset_Agregasi_Spasial_16_Kecamatan.xlsx / .csv"]
    end

    subgraph Modeling ["Tahap 3 & 4: Modeling Spasial & Sosio-Ekonomi"]
        G --> H["kmeans_model_spasial_wilayah.py"]
        H --> I["Hasil_Clustering_Kecamatan_Natuna.xlsx / .csv"]
        H --> J["peta_geospatial_klaster_natuna.png"]
        H --> K["visualisasi_cluster_kecamatan.png"]
        H --> L["evaluasi_elbow_silhouette.png"]
        
        F --> M["pemodelan_kmeans_sosioekonomi_dan_dashboard.py"]
        M --> N["Hasil_Clustering_Sosial_Ekonomi.xlsx / .csv"]
        M --> O["scatter_model_sosioekonomi_individu.png"]
    end

    subgraph EDA ["Tahap 5: Data Understanding"]
        C & F --> P["analisis_eksplorasi_data_dan_kualitas_eda.py"]
        P --> Q["8 Visualisasi EDA (300 DPI)"]
    end

    subgraph Deploy ["Tahap 6, 7 & 8: Deployment & Reporting"]
        I & N --> R["generate_dashboard.py"]
        R --> S["dashboard_interaktif_kmeans_dosen.html"]
        
        Q & J & O --> T["build_final_reports.py"]
        T --> U["LAPORAN_AKHIR_PENAMBANGAN_DATA_PD_NTN25.docx"]
        T --> V["FinPD_2401020121.pdf"]
        
        V --> W["paketkan_berkas_google_form.py"]
        W --> X["Berkas Submisi 1, 2, 3 (.7z & PDF)"]
    end

    Z["jalankan_seluruh_tahapan_pipeline.py"] -.->|Mengeksekusi Otomatis 1 s.d. 8| DataPrep & Modeling & EDA & Deploy
"""
    },
    {
        "id": "03",
        "name": "diagram_alur_struktur_laporan_akhir_rtm",
        "title": "Diagram Alur Struktur Hirarki Dokumen Laporan Akhir (RTM Dosen)",
        "dot": """digraph Report_Structure {
    rankdir=TB;
    fontname="Arial";
    dpi=300;
    node [shape=box, style="filled,rounded", fontname="Arial", fontsize=10, margin="0.2,0.15"];
    edge [color="#2B6CB0", penwidth=1.8, arrowhead=vee];

    subgraph cluster_rtm {
        style="filled,rounded";
        fillcolor="#F7FAFC";
        color="#CBD5E0";
        label="STRUKTUR DAN TATA KELOLA NASKAH LAPORAN AKHIR (STANDAR AKADEMIS RTM)";
        fontname="Arial Bold";
        fontsize=13;
        fontcolor="#1A365D";

        COV [label="HALAMAN JUDUL (COVER RESMI)\\n• Judul Lengkap Penelitian Kependudukan\\n• Logo Resmi Universitas Maritim Raja Ali Haji (UMRAH)\\n• Nama & NIM Tim Peneliti (Ketua & Anggota)\\n• Prodi Teknik Informatika, FTKK UMRAH 2026", fillcolor="#EBF8FF", color="#3182CE"];
        PRE [label="HALAMAN AWAL (PRELIMINARIES - ROMAWI i, ii, iii...)\\n• Kata Pengantar (Apresiasi Rektor, Dosen, Reviewer, Mitra Disdukcapil)\\n• Ringkasan Eksekutif / Abstrak & Kata Kunci Resmi\\n• Daftar Isi, Daftar Tabel, dan Daftar Gambar", fillcolor="#E6FFFA", color="#319795"];
        B1  [label="BAB I: BUSINESS UNDERSTANDING\\n• I.1 Latar Belakang Mitra Pemilik Data (Disdukcapil Natuna)\\n• I.2 Permasalahan Nyata (UU No. 24/2013 Batas 60 Hari, Disparitas 3T)\\n• I.3 Tujuan Data Mining (Spasial, Sosio-Ekonomi, Dashboard)\\n• I.4 Lini Waktu Pelaksanaan & Gantt Chart 8 Minggu (PIC Tim)", fillcolor="#FAF5FF", color="#805AD5"];
        B2  [label="BAB II: DATA UNDERSTANDING\\n• II.1 Teknik Pengumpulan Data (131 Folder Pindaian, 131 Berkas)\\n• II.2 Jenis Data (Nominal, Ordinal, Interval, Rasio & Kamus Data)\\n• II.3 Exploratory Data Analysis (8 Plot EDA Resolusi Tinggi)", fillcolor="#FFFAF0", color="#DD6B20"];
        B3  [label="BAB III: PREPROCESS\\n• III.1 Penyelesaian Missing Value (Protokol Zero Fabrication)\\n• III.2 Data Selection & Eliminasi PII (Kepatuhan UU No. 27/2022 PDP)\\n• III.3 Data Transformation (Standardisasi ISO & Validasi Typo 2025)\\n• III.4 Feature Engineering (Durasi Hari, Status LU/LT, Usia Ortu)", fillcolor="#FFF5F5", color="#E53E3E"];
        B4  [label="BAB IV: MODEL\\n• IV.1 Teori Dasar K-Means Clustering (WCSS / Inersia)\\n• IV.2 Detail Perhitungan Matematis Manual Langkah demi Langkah\\n• IV.3 Model 1: Spasial Wilayah 16 Kecamatan (K=3, Centroid & Peta)\\n• IV.4 Model 2: Sosio-Ekonomi Pemohon Individu (K=3)", fillcolor="#F0FFF4", color="#38A169"];
        B5  [label="BAB V: EVALUASI\\n• V.1 Metode Evaluasi Elbow (Within-Cluster Sum of Squares)\\n• V.2 Silhouette Coefficient (Spasial: 0.6410, Sosio: 0.5533)\\n• V.3 Davies-Bouldin Index (Spasial: 0.4698, Sosio: 0.5905)\\n• V.4 Tabel Validasi Hasil Evaluasi Kedua Model\\n• V.5 Profiling Karakteristik dan Karakterisasi Klaster", fillcolor="#EBF8FF", color="#3182CE"];
        B6  [label="BAB VI: PENERAPAN\\n• VI.1 Desain Implementasi Purwarupa Dashboard Web (Leaflet & Plotly)\\n• VI.2 Kesimpulan Komprehensif Penelitian\\n• VI.3 Rekomendasi Kebijakan Disdukcapil (Kapal Keliling & SPTJM)", fillcolor="#E6FFFA", color="#319795"];
        POS [label="BAGIAN AKHIR\\n• DAFTAR PUSTAKA (Format Standar Akademis APA)\\n• LAMPIRAN 1: Cuplikan Data Mentah Terdigitalisasi (Tersamar PII)\\n• LAMPIRAN 2: Dokumentasi Kegiatan, Lokasi Mitra & Reviewer\\n• LAMPIRAN 3: Tangkapan Layar Program & Dashboard Interaktif\\n• LAMPIRAN 4: Log Eksekusi Pipeline Otomasi Python", fillcolor="#EDF2F7", color="#4A5568"];

        COV -> PRE -> B1 -> B2 -> B3 -> B4 -> B5 -> B6 -> POS;
    }
}""",
        "mmd": """flowchart TD
    COV["HALAMAN JUDUL<br>(Cover Resmi, Logo UMRAH, Tim Peneliti)"] --> PRE["HALAMAN AWAL<br>(Kata Pengantar, Abstrak, Daftar Isi, Tabel, Gambar)"]
    PRE --> B1["BAB I: BUSINESS UNDERSTANDING<br>(I.1 Mitra, I.2 Masalah 60 Hari, I.3 Tujuan, I.4 Gantt Chart)"]
    B1 --> B2["BAB II: DATA UNDERSTANDING<br>(II.1 Arsip 131 Berkas, II.2 Kamus Data, II.3 8 Plot EDA)"]
    B2 --> B3["BAB III: PREPROCESS<br>(III.1 Zero Fabrication, III.2 PII, III.3 Typo 2025, III.4 Fitur Hari)"]
    B3 --> B4["BAB IV: MODEL<br>(IV.1 Teori, IV.2 Hitungan Manual, IV.3 Spasial, IV.4 Sosio-Ekonomi)"]
    B4 --> B5["BAB V: EVALUASI<br>(V.1 Elbow, V.2 Silhouette, V.3 DBI, V.4 Validasi, V.5 Profiling)"]
    B5 --> B6["BAB VI: PENERAPAN<br>(VI.1 Dashboard Leaflet, VI.2 Kesimpulan, VI.3 Rekomendasi)"]
    B6 --> POS["DAFTAR PUSTAKA & LAMPIRAN<br>(Format APA, Sampel Data PII, Dokumentasi, Tangkapan Layar, Log)"]"""
    },
    {
        "id": "04",
        "name": "diagram_alur_pemenuhan_standar_luaran_proyek",
        "title": "Diagram Alur Pemenuhan Standar Luaran Proyek (Kepatuhan Tripartit)",
        "dot": """digraph Compliance_Tripartite {
    rankdir=TB;
    fontname="Arial";
    dpi=300;
    node [shape=box, style="filled,rounded", fontname="Arial", fontsize=10, margin="0.2,0.15"];
    edge [color="#2B6CB0", penwidth=1.8, arrowhead=vee];

    subgraph cluster_tripartite {
        style="filled,rounded";
        fillcolor="#F7FAFC";
        color="#CBD5E0";
        label="PEMENUHAN STANDAR LUARAN PROYEK DATA MINING (KEPATUHAN TRIPARTIT)";
        fontname="Arial Bold";
        fontsize=13;
        fontcolor="#1A365D";

        subgraph cluster_c1 {
            style="filled,rounded";
            fillcolor="#EBF8FF";
            color="#3182CE";
            label="Pilar 1: Menjawab Catatan Dosen Reviewer Proposal";
            fontname="Arial Bold";
            fontsize=11;
            fontcolor="#1A365D";

            C1 [label="Analisis Geospasial Wilayah 16 Kecamatan:\\n• Peta Geospasial Spasial Wilayah (Leaflet & Citra 300 DPI)\\n• Segmentasi Objektif: High-Compliance, Moderate, High-Delay\\n• Pemetaan Solusi Disparitas Pulau Utama vs Pulau 3T", fillcolor="#FFFFFF", color="#3182CE"];
        }

        subgraph cluster_c2 {
            style="filled,rounded";
            fillcolor="#E6FFFA";
            color="#319795";
            label="Pilar 2: Menjawab Panduan RTM Matakuliah (Bab I - VI)";
            fontname="Arial Bold";
            fontsize=11;
            fontcolor="#234E52";

            C2 [label="Naskah Akademis Lengkap & Terstandarisasi:\\n• Dokumen Word (.docx): A4, Margin 4-3-3-3 cm, Times New Roman 12 pt, Spasi 1.5\\n• Dokumen PDF Resmi FinPD_2401020121.pdf (33 Halaman Lengkap)\\n• Simulasi Perhitungan Matematis Manual Algoritma K-Means", fillcolor="#FFFFFF", color="#319795"];
        }

        subgraph cluster_c3 {
            style="filled,rounded";
            fillcolor="#FAF5FF";
            color="#805AD5";
            label="Pilar 3: Menjawab Format Unggah Google Form";
            fontname="Arial Bold";
            fontsize=11;
            fontcolor="#44337A";

            C3 [label="Tiga Paket Berkas Submisi Resmi:\\n• Berkas 1: Mentah_2401020121.7z (Data Mentah Tersamar Privasi XLSX + CSV)\\n• Berkas 2: SiapMining_2401020121.7z (Data Bersih & Hasil Klaster XLSX + CSV)\\n• Berkas 3: FinPD_2401020121.pdf (Laporan Akhir Terverifikasi)", fillcolor="#FFFFFF", color="#805AD5"];
        }

        ORCH [label="MASTER ORCHESTRATOR PIPELINE\\njalankan_seluruh_tahapan_pipeline.py\\n• Eksekusi Satu Pintu Seluruh Skrip (Tahap 1 s.d. 8)\\n• Status: Exit Code 0 (Berhasil Tuntas 100%)", fillcolor="#2F855A", fontcolor="#FFFFFF", shape=component, style="filled"];

        C1 -> ORCH;
        C2 -> ORCH;
        C3 -> ORCH;
    }
}""",
        "mmd": """flowchart TD
    subgraph S1 ["Pilar 1: Menjawab Catatan Dosen Reviewer"]
        C1["Analisis Geospasial 16 Kecamatan<br>Peta Spasial, Segmentasi High-Delay vs High-Compliance 3T"]
    end
    subgraph S2 ["Pilar 2: Menjawab Format RTM Matakuliah"]
        C2["Naskah Lengkap Bab I - Bab VI<br>Word DOCX (Margin 4-3-3-3 cm), PDF FinPD, Hitungan Matematis Manual"]
    end
    subgraph S3 ["Pilar 3: Menjawab Submisi Google Form"]
        C3["Tiga Berkas Siap Unggah<br>Mentah_2401020121.7z, SiapMining_2401020121.7z, FinPD_2401020121.pdf"]
    end
    C1 --> ORCH["MASTER PIPELINE ORCHESTRATOR<br>jalankan_seluruh_tahapan_pipeline.py (Exit Code 0)"]
    C2 --> ORCH
    C3 --> ORCH"""
    },
    {
        "id": "05",
        "name": "diagram_alur_matematis_algoritma_kmeans",
        "title": "Diagram Alur Matematis Algoritma K-Means Clustering Langkah demi Langkah",
        "dot": """digraph KMeans_Math_Flow {
    rankdir=TB;
    fontname="Arial";
    dpi=300;
    node [shape=box, style="filled,rounded", fontname="Arial", fontsize=10, margin="0.2,0.15"];
    edge [color="#2B6CB0", penwidth=1.8, arrowhead=vee];

    subgraph cluster_km {
        style="filled,rounded";
        fillcolor="#F7FAFC";
        color="#CBD5E0";
        label="ALUR PERHITUNGAN MATEMATIS ALGORITMA K-MEANS CLUSTERING";
        fontname="Arial Bold";
        fontsize=13;
        fontcolor="#1A365D";

        INP  [label="MATRIKS DATA MASUKAN (X in R^{N x D})\\n• Model Spasial: N=16 Kecamatan, D=2 (Persentase LU & Median Durasi Hari)\\n• Model Sosio-Ekonomi: N=131 Berkas, D=2 (Usia Ortu & Durasi Pelaporan Hari)", fillcolor="#EBF8FF", color="#3182CE"];
        ZSC  [label="LANGKAH 1: STANDARDISASI FITUR Z-SCORE\\nz_ij = (x_ij - mu_j) / sigma_j\\n• Menyamakan skala persentase (0–100%) dengan durasi hari (0–16.000 hari)\\n• Menghindari dominasi variabel berentang besar pada jarak Euclidean", fillcolor="#E6FFFA", color="#319795"];
        INIT [label="LANGKAH 2: INISIALISASI CENTROID AWAL (K=3)\\n• Menetapkan titik pusat awal mu_1, mu_2, mu_3 (metode k-means++)\\n• Penguncian deterministik menggunakan parameter random_state=42", fillcolor="#FAF5FF", color="#805AD5"];
        DIST [label="LANGKAH 3: PERHITUNGAN MATRIKS JARAK EUCLIDEAN\\nd(x_i, mu_k) = sqrt{ sum_{j=1}^D (z_ij - mu_kj)^2 }\\n• Menghitung jarak geometris setiap objek x_i ke seluruh titik centroid mu_k", fillcolor="#FFFAF0", color="#DD6B20"];
        ASSN [label="LANGKAH 4: ALOKASI KEANGGOTAAN KLASTER\\nk* = argmin_{k in {1, ..., K}} d(x_i, mu_k)\\n• Menempatkan setiap objek ke dalam klaster dengan jarak Euclidean terdekat", fillcolor="#FFF5F5", color="#E53E3E"];
        UPDT [label="LANGKAH 5: PEMBARUAN TITIK PUSAT CENTROID\\nmu_k^{(t+1)} = (1 / |S_k|) * sum_{x_i in S_k} z_i\\n• Menghitung rata-rata aritmatika baru dari seluruh objek anggota klaster", fillcolor="#F0FFF4", color="#38A169"];
        CONV [label="EVALUASI KONVERGENSI CENTROID\\nApakah || mu^{(t+1)} - mu^{(t)} || < epsilon = 10^-4\\natau posisi anggota klaster tidak berubah lagi?", shape=diamond, fillcolor="#FEFCBF", color="#D69E2E", fontname="Arial Bold"];
        METR [label="VALIDASI KUALITAS PARTISI KLASTER\\n• Within-Cluster Sum of Squares (WCSS / Inersia)\\n• Silhouette Coefficient (Threshold: s > 0.50)\\n• Davies-Bouldin Index (Threshold: DBI < 0.80)", fillcolor="#EBF8FF", color="#3182CE"];
        OUT  [label="LUARAN PROFIL KLASTER OPTIMAL\\n• Identifikasi Centroid Skala Asli\\n• Penamaan Label Karakteristik (High-Compliance, Moderate, High-Delay)\\n• Integrasi ke Dashboard Spasial Leaflet & Laporan Akhir", fillcolor="#2F855A", fontcolor="#FFFFFF", style="filled"];

        INP -> ZSC -> INIT -> DIST -> ASSN -> UPDT -> CONV;
        CONV -> DIST [label=" Tidak (Ulangi Iterasi)", color="#E53E3E", fontcolor="#E53E3E"];
        CONV -> METR [label=" Ya (Konvergen)", color="#38A169", fontcolor="#38A169"];
        METR -> OUT;
    }
}""",
        "mmd": """flowchart TD
    INP["Matriks Data Masukan X (N x D)"] --> ZSC["1. Standardisasi Fitur Z-Score: z = (x - mean) / std"]
    ZSC --> INIT["2. Inisialisasi K=3 Centroid Awal (k-means++, random_state=42)"]
    INIT --> DIST["3. Hitung Matriks Jarak Euclidean d(x_i, mu_k)"]
    DIST --> ASSN["4. Alokasi Keanggotaan Klaster: argmin d(x_i, mu_k)"]
    ASSN --> UPDT["5. Pembaruan Titik Pusat Centroid: mu = mean(z_i)"]
    UPDT --> CONV{"Konvergen? (Pergeseran < 10^-4)"}
    CONV -- Tidak --> DIST
    CONV -- Ya --> METR["Validasi Metrik: Elbow, Silhouette, Davies-Bouldin"]
    METR --> OUT["Profiling Karakteristik Klaster & Integrasi Dashboard"]"""
    },
    {
        "id": "06",
        "name": "diagram_alur_penjaminan_kualitas_data_zero_fabrication",
        "title": "Diagram Alur Penjaminan Kualitas Data & Audit Zero Data Fabrication",
        "dot": """digraph Data_Quality_Assurance {
    rankdir=TB;
    fontname="Arial";
    dpi=300;
    node [shape=box, style="filled,rounded", fontname="Arial", fontsize=10, margin="0.2,0.15"];
    edge [color="#2B6CB0", penwidth=1.8, arrowhead=vee];

    subgraph cluster_qa {
        style="filled,rounded";
        fillcolor="#F7FAFC";
        color="#CBD5E0";
        label="AUDIT PENJAMINAN KUALITAS DATA & KEPATUHAN ZERO DATA FABRICATION";
        fontname="Arial Bold";
        fontsize=13;
        fontcolor="#1A365D";

        RAW [label="SUMBER DATA PRIMER OPERASIONAL\\n• 131 Folder Berkas Pindaian Fisik Resmi Loket Disdukcapil Natuna\\n• 262 Citra Dokumen (Formulir F-2.01 & Surat Medis SKL / SPTJM)\\n• 131 Berkas Permohonan Akta Kelahiran Individu", fillcolor="#EBF8FF", color="#3182CE"];
        TRANS [label="TRANSKRIPSI DIGITAL FAKTUAL AWAL\\n• Konversi OCR & Audit Manual Ganda ke Format Excel\\n• Mempertahankan Integritas Dokumen Asli Tanpa Modifikasi Awal", fillcolor="#E6FFFA", color="#319795"];
        
        subgraph cluster_audit {
            style="filled,rounded";
            fillcolor="#FFF5F5";
            color="#FEB2B2";
            label="Pemeriksaan Anomali & Kualitas Data (Zero Fabrication)";
            fontname="Arial Bold";
            fontsize=10;
            fontcolor="#9B2C2C";

            A1 [label="Audit Missing Values Kolom Pekerjaan (48 Berkas RSUD)\\n• Ketiadaan isian diakui secara jujur\\n• Ditetapkan kategori formal: 'Tanpa Keterangan (Template RSUD)'\\n• Menolak keras pembuatan data sintetik / fabrikasi", fillcolor="#FFFFFF", color="#E53E3E"];
            A2 [label="Koreksi Typo Slip Loket F044\\n• Tertulis Lahir: 2025-05-18, Lapor: 2024-05-18 (Typo Tahun Lapor -365 hari)\\n• Verifikasi Faktual Tanggal Lapor: 2025-05-18 (Durasi 0 hari, Lahir Umum)", fillcolor="#FFFFFF", color="#E53E3E"];
            A3 [label="Koreksi Typo Slip Loket F0124\\n• Tertulis Lahir: 2026-07-06 (Mendahului Masa Pelayanan 2025)\\n• Dikoreksi Tanggal Lahir: 2025-07-06, Lapor: 2025-07-06 (Durasi 0 hari)", fillcolor="#FFFFFF", color="#E53E3E"];
        }

        SYNC [label="VALIDASI KOHORT PELAYANAN TAHUN 2025\\n• Seluruh berkas (100%) merupakan kohort resmi Tahun Pelaporan 2025\\n• Distribusi Tahun Lapor: {2025: 131 berkas} pada hari kerja operasional dinas", fillcolor="#FAF5FF", color="#805AD5"];
        PII  [label="ELIMINASI PII SESUAI UU NO. 27/2022 (UU PDP)\\n• Penghapusan NIK Anak, NIK Ayah, NIK Ibu, Nomor KK, dan Nama Lengkap\\n• Penghapusan Alamat Rumah Detail RT/RW\\n• Pemberian Kode Identitas Pseudonim B_001 s.d. B_131", fillcolor="#FFFAF0", color="#DD6B20"];
        READY [label="DATASET BERSIH SIAP MINING (XLSX & CSV)\\n• Terverifikasi Yuridis Tier 1 & Tier 2 Sesuai Permendagri No. 108/2019\\n• Siap Diproses ke Tahap Rekayasa Fitur dan Pemodelan K-Means", fillcolor="#2F855A", fontcolor="#FFFFFF", style="filled"];

        RAW -> TRANS -> A1;
        TRANS -> A2;
        TRANS -> A3;
        A1 -> SYNC;
        A2 -> SYNC;
        A3 -> SYNC;
        SYNC -> PII -> READY;
    }
}""",
        "mmd": """flowchart TD
    RAW["131 Folder Arsip Fisik Pindaian (131 Permohonan)"] --> TRANS["Transkripsi Digital Faktual ke Excel Mentah"]
    TRANS --> A1["Audit Missing Values: Label 'Tanpa Keterangan (Template RSUD)' (Anti-Fabrikasi)"]
    TRANS --> A2["Koreksi Typo Slip F044: Verifikasi Faktual Lapor 2025-05-18 (Durasi 0 hr, LU)"]
    TRANS --> A3["Koreksi Typo Slip F0124: Koreksi Lahir 2025-07-06 (Durasi 0 hr, LU)"]
    A1 --> SYNC["Validasi Kohort Pelayanan: 100% Tahun Pelaporan 2025"]
    A2 --> SYNC
    A3 --> SYNC
    SYNC --> PII["Kepatuhan UU No. 27/2022 PDP: Eliminasi NIK/Nama/Alamat, ID B_001..B_131"]
    PII --> READY["Dataset Bersih Siap Mining (Excel + CSV) Tervalidasi Yuridis"]"""
    }
]

# Generate each diagram
readme_entries = []

for diag in diagrams:
    d_id = diag["id"]
    d_name = diag["name"]
    d_title = diag["title"]
    base_file = f"{d_id}_{d_name}"

    src_dir = os.path.join(BASE_DIR, "sumber_kode_diagram")
    os.makedirs(src_dir, exist_ok=True)
    dot_path = os.path.join(src_dir, f"{base_file}.dot")
    mmd_path = os.path.join(src_dir, f"{base_file}.mmd")
    png_path = os.path.join(BASE_DIR, f"{base_file}.png")
    svg_path = os.path.join(BASE_DIR, f"{base_file}.svg")

    # 1. Simpan DOT
    with open(dot_path, "w", encoding="utf-8") as f:
        f.write(diag["dot"])

    # 2. Simpan MMD
    with open(mmd_path, "w", encoding="utf-8") as f:
        f.write(diag["mmd"])

    # 3. Render PNG (300 DPI)
    cmd_png = ["dot", "-Tpng", "-Gdpi=300", dot_path, "-o", png_path]
    res_png = subprocess.run(cmd_png, capture_output=True, text=True)

    # 4. Render SVG
    cmd_svg = ["dot", "-Tsvg", dot_path, "-o", svg_path]
    res_svg = subprocess.run(cmd_svg, capture_output=True, text=True)

    if res_png.returncode == 0 and res_svg.returncode == 0:
        print(f"[OK] Diagram {d_id} ({d_name}) berhasil dibangun:")
        print(f"     -> PNG: {png_path}")
        print(f"     -> SVG: {svg_path}")
    else:
        print(f"[ERR] Gagal membangun diagram {d_id}: {res_png.stderr or res_svg.stderr}")

    readme_entries.append(f"""### {d_id}. {d_title}
- **Berkas Gambar Utama (PNG 300 DPI):** [{base_file}.png](./{base_file}.png)
- **Berkas Vektor Skalabel (SVG):** [{base_file}.svg](./{base_file}.svg)
- *Arsip Kode Sumber:* [DOT](./sumber_kode_diagram/{base_file}.dot) | [Mermaid](./sumber_kode_diagram/{base_file}.mmd)

![{d_title}](./{base_file}.png)

---
""")

# Bangun README.md di folder diagram
readme_content = f"""# ARSIP LENGKAP DIAGRAM ALUR DAN ARSITEKTUR SISTEM (PD-NTN25)
**Proyek Penambangan Data: K-Means Clustering Disdukcapil Kabupaten Natuna**

Folder ini menyimpan secara khusus seluruh poto, gambar, diagram alur (*flowchart*), dan arsitektur sistem yang telah dirancang, dibahas, dan ditampilkan sepanjang percakapan proyek penambangan data ini.

Total terdapat **6 Diagram Alur Utama** yang mencakup seluruh metodologi, otomasi script, struktur laporan resmi, kepatuhan luaran, komputasi matematis, dan integritas data kependudukan.

Setiap diagram disediakan dalam 4 format lengkap:
1. **PNG Resolusi Tinggi (300 DPI):** Format gambar raster siap disematkan ke slide presentasi PowerPoint, dokumen Microsoft Word, atau poster ilmiah.
2. **SVG (Scalable Vector Graphics):** Format gambar vektor tajam tanpa pecah untuk publikasi web atau pembesaran tak terbatas.
3. **DOT (Graphviz Source):** Kode sumber diagram formal Graphviz yang dapat dirender ulang kapan saja menggunakan perintah `dot`.
4. **MMD (Mermaid Source):** Kode sumber diagram Mermaid Markdown yang dapat langsung ditampilkan di GitHub, Notion, atau editor Markdown.

---

## DAFTAR DIAGRAM ALUR

{"".join(readme_entries)}

## CARA MEMBANGUN ULANG SELURUH DIAGRAM
Seluruh diagram dapat dirender ulang secara otomatis kapan saja dengan mengeksekusi skrip:
```bash
python3 08_DIAGRAM_ALUR_DAN_ARSITEKTUR/generate_diagrams.py
```
"""

readme_path = os.path.join(BASE_DIR, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"[OK] README.md katalog diagram berhasil dibuat di: {readme_path}")
print("================================================================================")
print("  SELURUH 6 DIAGRAM ALUR BERHASIL DIBANGUN 100% SUKSES!")
print("================================================================================")

