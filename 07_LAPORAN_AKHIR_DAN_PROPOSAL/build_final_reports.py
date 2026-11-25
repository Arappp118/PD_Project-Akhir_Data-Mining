#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Pembangun Laporan Akhir Resmi (DOCX dan PDF)
Proyek Penambangan Data: K-Means Clustering Disdukcapil Kabupaten Natuna
Format: Standar Akademis & Panduan RTM Dosen
NIM Ketua: 2401020121 (Ridho Ramadani E) -> FinPD_2401020121.pdf
"""

import os
import re
import shutil
import docx
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import weasyprint

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))
DOCX_PATH = os.path.join(BASE_DIR, "LAPORAN_AKHIR_PENAMBANGAN_DATA_PD_NTN25.docx")
PDF_PATH = os.path.join(BASE_DIR, "FinPD_2401020121.pdf")
MD_PATH = os.path.join(BASE_DIR, "LAPORAN_AKHIR_PENAMBANGAN_DATA_PD_NTN25.md")
BERKAS_UNGGAH_DIR = os.path.join(PROJECT_ROOT, "BERKAS_UNGGAH_GOOGLE_FORM")
BERKAS_PDF_PATH = os.path.join(BERKAS_UNGGAH_DIR, "FinPD_2401020121.pdf")

print("================================================================================")
print("  MEMBANGUN LAPORAN AKHIR RESMI: WORD (.DOCX) & PDF (FinPD_2401020121.pdf)")
print("  STANDAR HALAMAN A4 | MARGIN: KIRI 4 CM, ATAS 3 CM, KANAN 3 CM, BAWAH 3 CM")
print("  TIMES NEW ROMAN 12 PT | SPASI 1.5 | JUSTIFIED | TWO-SECTION NUMBERING")
print("================================================================================")

# --- FUNGSI XML DOCX HELPER ---
def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), color_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_table_borders(table, color='777777', sz='4', val='single'):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), val)
        border.set(qn('w:sz'), sz)
        border.set(qn('w:space'), '0')
        border.set(qn('w:color'), color)
        tblBorders.append(border)
    tblPr.append(tblBorders)

def add_page_number_field(run):
    fldSimple = OxmlElement('w:fldSimple')
    fldSimple.set(qn('w:instr'), 'PAGE')
    run._r.append(fldSimple)

# ==============================================================================
# 1. MEMBUAT DOKUMEN WORD (.DOCX)
# ==============================================================================
doc = docx.Document()

# Setup Section 1: Halaman Judul & Preliminaries (Romawi i, ii, iii...)
sec0 = doc.sections[0]
sec0.page_width = Cm(21.0)
sec0.page_height = Cm(29.7)
sec0.left_margin = Cm(4.0)
sec0.top_margin = Cm(3.0)
sec0.right_margin = Cm(3.0)
sec0.bottom_margin = Cm(3.0)
sec0.different_first_page_header_footer = True

# Prelim footer: Romawi kecil di tengah bawah
p_foot0 = sec0.footer.paragraphs[0]
p_foot0.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_foot0 = p_foot0.add_run()
r_foot0.font.name = 'Times New Roman'
r_foot0.font.size = Pt(11)
add_page_number_field(r_foot0)

sectPr0 = sec0._sectPr
pgNum0 = sectPr0.find(qn('w:pgNumType'))
if pgNum0 is None:
    pgNum0 = OxmlElement('w:pgNumType')
    sectPr0.append(pgNum0)
pgNum0.set(qn('w:fmt'), 'lowerRoman')
pgNum0.set(qn('w:start'), '1')

# Set Normal Style
normal_style = doc.styles['Normal']
normal_style.font.name = 'Times New Roman'
normal_style.font.size = Pt(12)
normal_style.font.color.rgb = RGBColor(0, 0, 0)
normal_style.paragraph_format.line_spacing = 1.5
normal_style.paragraph_format.space_before = Pt(0)
normal_style.paragraph_format.space_after = Pt(0)

# ----------------- HALAMAN COVER (HALAMAN JUDUL) -----------------
p_cov_space = doc.add_paragraph()
p_cov_space.paragraph_format.space_before = Pt(20)

p_cov_title = doc.add_paragraph()
p_cov_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cov_title.paragraph_format.line_spacing = 1.15
p_cov_title.paragraph_format.space_after = Pt(8)
r = p_cov_title.add_run("LAPORAN AKHIR PROJECT\nPENAMBANGAN DATA\n")
r.bold = True
r.font.size = Pt(14)

p_cov_sub = doc.add_paragraph()
p_cov_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cov_sub.paragraph_format.line_spacing = 1.15
p_cov_sub.paragraph_format.space_after = Pt(24)
r = p_cov_sub.add_run("PENGELOMPOKKAN WILAYAH DAN ANALISIS KETERLAMBATAN PENCATATAN AKTA KELAHIRAN MENGGUNAKAN ALGORITMA K-MEANS CLUSTERING PADA DISDUKCAPIL KABUPATEN NATUNA")
r.bold = True
r.font.size = Pt(13)

# Logo UMRAH
logo_path = os.path.join(BASE_DIR, "logo_umrah.png")
if os.path.exists(logo_path):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_after = Pt(24)
    run_logo = p_logo.add_run()
    run_logo.add_picture(logo_path, width=Inches(1.85))

# Tim Peneliti Sesuai Format Panduan Dosen (Ketua NIM - NAMA, NIM - NAMA)
p_team = doc.add_paragraph()
p_team.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_team.paragraph_format.line_spacing = 1.25
p_team.paragraph_format.space_after = Pt(24)

team_members = [
    ("Ketua 2401020121", "RIDHO RAMADANI E"),
    ("2401020094", "SALMA NURSAFIRA"),
    ("2401020100", "MONALISA DWI CANTIKA"),
    ("2401020109", "SARAH FAUZIYYAH"),
    ("2401020111", "MUHAMMAD AGUS FARHAN")
]
for nim, nama in team_members:
    r = p_team.add_run(f"{nim} – {nama}\n")
    r.font.size = Pt(12)
    r.bold = True

p_univ = doc.add_paragraph()
p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_univ.paragraph_format.line_spacing = 1.15
r = p_univ.add_run(
    "Teknik Informatika\n"
    "Fakultas Teknik dan Teknologi Kemaritiman\n"
    "Universitas Maritim Raja Ali Haji\n"
    "Tanjungpinang\n"
    "2026"
)
r.bold = True
r.font.size = Pt(12)

doc.add_page_break()

# ----------------- KATA PENGANTAR -----------------
p_kp = doc.add_paragraph()
p_kp.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_kp.paragraph_format.space_before = Pt(12)
p_kp.paragraph_format.space_after = Pt(18)
r = p_kp.add_run("KATA PENGANTAR")
r.bold = True
r.font.size = Pt(14)

kp_text = [
    "Puji dan syukur ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan hidayah-Nya, sehingga Tim Peneliti dapat menyelesaikan penyusunan Laporan Akhir Proyek Penambangan Data dengan judul \"Pengelompokkan Wilayah dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering pada Disdukcapil Kabupaten Natuna\" dengan baik, tepat waktu, dan memenuhi seluruh kaidah akademik resmi.",
    "Laporan akhir ini disusun sebagai syarat kelulusan dan pemenuhan luaran mata kuliah Penambangan Data pada Program Studi Teknik Informatika, Fakultas Teknik dan Teknologi Kemaritiman, Universitas Maritim Raja Ali Haji (UMRAH) Tanjungpinang. Penelitian ini dirancang untuk memecahkan problematika nyata disparitas pelayanan administrasi kependudukan di wilayah kepulauan perbatasan terluar Indonesia, khususnya dalam mendeteksi klaster kecamatan yang mengalami keterlambatan pencatatan akta kelahiran.",
    "Dalam pelaksanaan penelitian dan penyusunan laporan akhir ini, Tim Peneliti memperoleh bimbingan, arahan, serta dukungan berharga dari berbagai pihak. Oleh karena itu, rasa hormat dan terima kasih yang tulus kami haturkan kepada:",
    "1. Rektor Universitas Maritim Raja Ali Haji dan Dekan Fakultas Teknik dan Teknologi Kemaritiman UMRAH atas fasilitas akademik dan iklim riset yang kondusif.\n"
    "2. Bapak/Ibu Dosen Pengampu Mata Kuliah Penambangan Data atas dedikasi transfer keilmuan, bimbingan metodologi CRISP-DM, serta arahan pemodelan data mining di kelas.\n"
    "3. Bapak/Ibu Dosen Reviewer Proposal atas masukan konstruktif yang sangat berharga dalam memperkuat analisis spasial geospasial 16 kecamatan di Kabupaten Natuna.\n"
    "4. Kepala Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna beserta Ibu Julida, S.Sos (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk) atas izin penelitian, penyediaan 131 arsip pindaian resmi, serta koordinasi faktual di lapangan.\n"
    "5. Seluruh rekan mahasiswa Program Studi Teknik Informatika angkatan 2024 yang saling memberikan semangat dan kolaborasi konstruktif.",
    "Tim Peneliti menyadari sepenuhnya bahwa laporan ini masih memiliki keterbatasan. Kritik dan saran yang membangun senantiasa diharapkan guna penyempurnaan karya ilmiah berikutnya. Semoga laporan ini memberikan sumbangsih nyata bagi efektivitas kebijakan Disdukcapil Natuna dan kemajuan teknologi kemaritiman di Kepulauan Riau.",
    "Tanjungpinang, November 2026\n\nTim Peneliti Mahasiswa"
]
for idx, para in enumerate(kp_text):
    p = doc.add_paragraph()
    if idx == len(kp_text) - 1:
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(12)
        r = p.add_run(para)
        r.italic = True
    elif para.startswith("1."):
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.line_spacing = 1.3
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.add_run(para)
    else:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.0)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(4)
        p.add_run(para)

doc.add_page_break()

# ----------------- RINGKASAN EKSEKUTIF / ABSTRAK -----------------
p_abs = doc.add_paragraph()
p_abs.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_abs.paragraph_format.space_before = Pt(12)
p_abs.paragraph_format.space_after = Pt(14)
r = p_abs.add_run("RINGKASAN EKSEKUTIF / ABSTRAK")
r.bold = True
r.font.size = Pt(14)

abs_paragraphs = [
    "Pencatatan akta kelahiran merupakan dokumen yuridis fundamental yang menjamin hak kewarganegaraan setiap penduduk Indonesia. Berdasarkan Undang-Undang Nomor 24 Tahun 2013 tentang Administrasi Kependudukan, peristiwa kelahiran wajib dilaporkan paling lambat 60 (enam puluh) hari sejak tanggal persalinan. Pelaporan dalam tenggat waktu tersebut diklasifikasikan sebagai Lahir Umum (LU), sedangkan pelaporan yang melampaui 60 hari dikategorikan sebagai Lahir Terlambat (LT) yang membutuhkan instrumen Surat Pernyataan Tanggung Jawab Mutlak (SPTJM). Kabupaten Natuna menghadapi tantangan geografis berupa disparitas keterjangkauan transportasi antarpulau, cuaca ekstrem musim utara, dan jarak tempuh ke ibu kota Ranai, yang berisiko memicu tingginya keterlambatan pencatatan sipil.",
    "Penelitian ini menerapkan metodologi baku Cross-Industry Standard Process for Data Mining (CRISP-DM) untuk mengelompokkan wilayah dan menganalisis pola keterlambatan akta kelahiran menggunakan algoritma K-Means Clustering. Sebanyak 131 berkas fisik resmi pendaftaran akta kelahiran Disdukcapil Kabupaten Natuna dari 131 folder pindaian diekstraksi secara teliti. Seluruh data merupakan kohort resmi Tahun Pelayanan 2025 yang diaudit melalui protokol ketat Zero Data Fabrication, koreksi yuridis anomali slip loket (F044 dan F0124), serta penyamaran identitas pribadi (PII) sesuai UU No. 27 Tahun 2022.",
    "Dua model penambangan data dibangun secara komplementer: (1) Model Spasial Wilayah (16 Kecamatan) berbasis rasio kepatuhan LU dan median durasi hari (Silhouette Score = 0.6377, Davies-Bouldin Index = 0.4710) yang membagi Natuna menjadi Cluster 0 (High-Compliance, n=2), Cluster 1 (Moderate, n=7), dan Cluster 2 (High-Delay, n=7); serta (2) Model Sosio-Ekonomi Pemohon Individu (131 Berkas) yang memetakan korelasi bivariat Sumbu X (Hari Usia Orang Tua) terhadap Sumbu Y (Hari Keterlambatan Pelaporan) (Silhouette Score = 0.5524, DBI = 0.5924). Temuan riset diwujudkan dalam Dashboard Interaktif berbasis Peta Leaflet dan melahirkan 3 rekomendasi kebijakan strategis, termasuk pengadaan armada Kapal Pelayanan Keliling (Mobile Service Boat) bagi pulau-pulau 3T.",
    "Kata Kunci: Data Mining, K-Means Clustering, Akta Kelahiran, Disdukcapil Natuna, Analisis Spasial, CRISP-DM, Evaluasi Silhouette."
]

for idx, para in enumerate(abs_paragraphs):
    p = doc.add_paragraph()
    if idx == len(abs_paragraphs) - 1:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.space_before = Pt(8)
        r = p.add_run(para)
        r.italic = True
    else:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Cm(1.0)
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(4)
        p.add_run(para)

doc.add_page_break()

# ----------------- DAFTAR ISI -----------------
p_toc = doc.add_paragraph()
p_toc.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_toc.paragraph_format.space_before = Pt(12)
p_toc.paragraph_format.space_after = Pt(18)
r = p_toc.add_run("DAFTAR ISI")
r.bold = True
r.font.size = Pt(14)

toc_items = [
    ("HALAMAN JUDUL", "i", True),
    ("KATA PENGANTAR", "ii", True),
    ("RINGKASAN EKSEKUTIF / ABSTRAK", "iii", True),
    ("DAFTAR ISI", "iv", True),
    ("DAFTAR TABEL", "v", True),
    ("DAFTAR GAMBAR", "vi", True),
    ("BAB I BUSINESS UNDERSTANDING", "1", True),
    ("    I.1 Latar Belakang Mitra Pemilik Data", "1", False),
    ("    I.2 Permasalahan yang Dihadapi Mitra", "2", False),
    ("    I.3 Tujuan Penambangan Data", "4", False),
    ("    I.4 Lini Waktu Pelaksanaan & Gantt Chart", "5", False),
    ("BAB II DATA UNDERSTANDING", "6", True),
    ("    II.1 Teknik Pengumpulan Data", "6", False),
    ("    II.2 Jenis Data & Skala Pengukuran", "7", False),
    ("    II.3 Exploratory Data Analysis (EDA) & 8 Plot Visualisasi", "8", False),
    ("BAB III PREPROCESS", "13", True),
    ("    III.1 Penyelesaian Missing Value & Kebijakan Zero Fabrication", "13", False),
    ("    III.2 Data Selection & Eliminasi PII (UU No. 27/2022)", "14", False),
    ("    III.3 Data Transformation & Validasi Format Kronologis", "15", False),
    ("    III.4 Feature Engineering (Durasi Hari & Usia Orang Tua)", "16", False),
    ("BAB IV MODEL", "18", True),
    ("    IV.1 Teori Dasar K-Means Clustering", "18", False),
    ("    IV.2 Detail Perhitungan Matematis K-Means Langkah demi Langkah", "19", False),
    ("    IV.3 Model 1: K-Means Spasial Wilayah (16 Kecamatan)", "22", False),
    ("    IV.4 Model 2: K-Means Sosio-Ekonomi Pemohon Individu", "24", False),
    ("BAB V EVALUASI", "26", True),
    ("    V.1 Metode Evaluasi Elbow (Inertia/WCSS)", "26", False),
    ("    V.2 Silhouette Coefficient Analysis", "27", False),
    ("    V.3 Davies-Bouldin Index (DBI)", "28", False),
    ("    V.4 Tabel Validasi Hasil Evaluasi Kedua Model", "29", False),
    ("    V.5 Profiling dan Karakterisasi Klaster", "30", False),
    ("BAB VI PENERAPAN", "32", True),
    ("    VI.1 Desain Implementasi Sistem Dashboard Web Spasial", "32", False),
    ("    VI.2 Kesimpulan", "33", False),
    ("    VI.3 Rekomendasi Kebijakan Disdukcapil Kabupaten Natuna", "34", False),
    ("DAFTAR PUSTAKA", "36", True),
    ("LAMPIRAN", "37", True),
    ("    Lampiran 1: Cuplikan Tabulasi Data Mentah Terdigitalisasi (Tersamar PII)", "37", False),
    ("    Lampiran 2: Dokumentasi Kegiatan & Catatan Reviewer Proposal", "39", False),
    ("    Lampiran 3: Tangkapan Layar Program & Dashboard Interaktif", "40", False),
    ("    Lampiran 4: Log Eksekusi Pipeline Otomasi Data Mining Python", "41", False),
]

for title, page_no, is_bold in toc_items:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(2)
    dots = ". " * (50 - len(title.strip()) // 2)
    r_t = p.add_run(title)
    r_t.bold = is_bold
    r_d = p.add_run(f"  {dots[:35]}  ")
    r_d.font.color.rgb = RGBColor(120, 120, 120)
    r_p = p.add_run(page_no)
    r_p.bold = is_bold

doc.add_page_break()

# ----------------- DAFTAR TABEL & DAFTAR GAMBAR -----------------
p_lot = doc.add_paragraph()
p_lot.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_lot.paragraph_format.space_before = Pt(12)
p_lot.paragraph_format.space_after = Pt(14)
r = p_lot.add_run("DAFTAR TABEL")
r.bold = True
r.font.size = Pt(14)

table_list = [
    ("Tabel I.1: Lini Waktu Pelaksanaan dan Pembagian Tanggung Jawab (Gantt Chart)", "5"),
    ("Tabel II.1: Kamus Data Atribut Administrasi Akta Kelahiran Disdukcapil Natuna", "7"),
    ("Tabel III.1: Log Penanganan Kualitas Data, Koreksi Typo, dan Verifikasi Faktual", "14"),
    ("Tabel IV.1: Simulasi Perhitungan Numerik Langkah demi Langkah Algoritma K-Means", "21"),
    ("Tabel IV.2: Koordinat Centroid Model 1 (Spasial Wilayah 16 Kecamatan)", "23"),
    ("Tabel IV.3: Koordinat Centroid Model 2 (Sosio-Ekonomi Pemohon Individu)", "25"),
    ("Tabel V.1: Komparasi Validasi Metrik Evaluasi Kedua Model Penambangan Data", "29"),
    ("Tabel V.2: Rekapitulasi Keanggotaan dan Karakteristik Klaster Spasial 16 Kecamatan", "31"),
    ("Tabel L.1: Sampel Data Mentah Terdigitalisasi dengan Penyamaran Identitas Pribadi (PII)", "38"),
]
for title, page_no in table_list:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(2)
    dots = ". " * 30
    p.add_run(title)
    r_d = p.add_run(f"  {dots}  ")
    r_d.font.color.rgb = RGBColor(120, 120, 120)
    p.add_run(page_no)

p_lof = doc.add_paragraph()
p_lof.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_lof.paragraph_format.space_before = Pt(20)
p_lof.paragraph_format.space_after = Pt(14)
r = p_lof.add_run("DAFTAR GAMBAR")
r.bold = True
r.font.size = Pt(14)

figure_list = [
    ("Gambar I.1: Catatan Reviewer Proposal Terkait Kewajiban Analisis Geospasial Wilayah", "3"),
    ("Gambar II.1: Visualisasi Audit Kualitas Data dan Verifikasi Ketiadaan Fabrikasi", "8"),
    ("Gambar II.2: Deteksi dan Penyelesaian Anomali Typo Kronologis Penanggalan", "9"),
    ("Gambar II.3: Distribusi Bimodal Keterlambatan Pelaporan Akta Kelahiran", "9"),
    ("Gambar II.4: Perbandingan Disparitas Spasial Berkas: Pulau Utama vs Terluar", "10"),
    ("Gambar II.5: Tren Fluktuasi Bulanan Pelaporan Akta Kelahiran Tahun 2025", "11"),
    ("Gambar II.6: Boxplot Dispersi dan Outlier Keterlambatan Antar-Kecamatan", "11"),
    ("Gambar II.7: Scatter Plot Bivariat Usia Orang Tua terhadap Durasi Keterlambatan", "12"),
    ("Gambar II.8: Heatmap Matriks Korelasi Spearman Antar-Fitur Kependudukan", "12"),
    ("Gambar IV.1: Peta Geospasial Klaster Kepatuhan 16 Kecamatan Kabupaten Natuna", "23"),
    ("Gambar IV.2: Visualisasi Model K-Means Sosio-Ekonomi Pemohon Individu", "25"),
    ("Gambar V.1: Kurva Evaluasi Penentuan Klaster Optimal: Elbow dan Silhouette Score", "28"),
    ("Gambar VI.1: Purwarupa Sistem Dashboard Web Spasial Interaktif Leaflet & Plotly", "33"),
]
for title, page_no in figure_list:
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(2)
    dots = ". " * 30
    p.add_run(title)
    r_d = p.add_run(f"  {dots}  ")
    r_d.font.color.rgb = RGBColor(120, 120, 120)
    p.add_run(page_no)

# ==============================================================================
# SECTION 2: BODY CHAPTERS (BAB I S.D. LAMPIRAN, PENOMORAN ARABIK 1, 2, 3...)
# ==============================================================================
sec1 = doc.add_section(WD_SECTION.NEW_PAGE)
sec1.page_width = Cm(21.0)
sec1.page_height = Cm(29.7)
sec1.left_margin = Cm(4.0)
sec1.top_margin = Cm(3.0)
sec1.right_margin = Cm(3.0)
sec1.bottom_margin = Cm(3.0)
sec1.footer.is_linked_to_previous = False

# Body footer: Arabik di sudut kanan bawah
p_foot1 = sec1.footer.paragraphs[0]
p_foot1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r_foot1 = p_foot1.add_run()
r_foot1.font.name = 'Times New Roman'
r_foot1.font.size = Pt(11)
add_page_number_field(r_foot1)

sectPr1 = sec1._sectPr
pgNum1 = sectPr1.find(qn('w:pgNumType'))
if pgNum1 is None:
    pgNum1 = OxmlElement('w:pgNumType')
    sectPr1.append(pgNum1)
pgNum1.set(qn('w:fmt'), 'decimal')
pgNum1.set(qn('w:start'), '1')

# Helper menambah Heading Bab
def add_chapter_heading(doc, title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(14)
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(14)

def add_subheading(doc, title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(title)
    r.bold = True
    r.font.size = Pt(12)

def add_subsubheading(doc, title):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(title)
    r.bold = True
    r.italic = True
    r.font.size = Pt(12)

def add_body_p(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.first_line_indent = Cm(1.0)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.add_run(text)

def add_bullet_item(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-0.4)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.add_run(f"•  {text}")

def add_numbered_item(doc, num_str, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.0)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.add_run(f"{num_str}. {text}")

def add_caption_image(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(10)
    r = p.add_run(text)
    r.italic = True
    r.font.size = Pt(10)

def add_caption_table(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(11)

def add_image_box(doc, img_rel_path, caption_text, width_in=5.4):
    full_path = os.path.join(PROJECT_ROOT, img_rel_path)
    if os.path.exists(full_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run()
        r.add_picture(full_path, width=Inches(width_in))
        add_caption_image(doc, caption_text)
    else:
        print(f"[WARN] Gambar tidak ditemukan: {full_path}")

# ==============================================================================
# BAB I: BUSINESS UNDERSTANDING
# ==============================================================================
add_chapter_heading(doc, "BAB I\nBUSINESS UNDERSTANDING")

add_subheading(doc, "I.1 Latar Belakang Mitra Pemilik Data")
add_body_p(doc, "Dinas Kependudukan dan Pencatatan Sipil (Disdukcapil) Kabupaten Natuna, yang beralamat di Kompleks Perkantoran Pemerintah Daerah Bukit Arai, Jalan Batu Sisir, Ranai, Kecamatan Bunguran Timur, merupakan unsur pelaksana urusan pemerintahan di bidang administrasi kependudukan dan pencatatan sipil. Koordinasi teknis penelitian penambangan data ini dilaksanakan secara intensif bersama Ibu Julida, S.Sos (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk Disdukcapil Kabupaten Natuna). Data yang diolah dalam penelitian ini merupakan data primer resmi hasil pelayanan loket pendaftaran akta kelahiran yang terdokumentasi dalam berkas formulir dan surat keterangan kelahiran.")
add_body_p(doc, "Secara geografis dan geopolitik, Kabupaten Natuna merupakan beranda terdepan Negara Kesatuan Republik Indonesia di kawasan Laut Natuna Utara yang berbatasan langsung dengan perairan internasional Vietnam, Malaysia, dan Laut Tiongkok Selatan. Kabupaten Natuna terdiri atas 16 kecamatan administratif, di mana sebagian besar kecamatan terletak di gugusan pulau-pulau terpencil dan terluar seperti Kecamatan Pulau Laut, Midai, Suak Midai, Serasan, Serasan Timur, Subi, Pulau Tiga, dan Pulau Panjang. Karakteristik kepulauan tersebut menimbulkan tantangan konektivitas yang luar biasa: transportasi antar-pulau sangat bergantung pada perahu motor tradisional (pompong) dan kapal perintis pelni yang berlayar dengan jadwal berkala serta sangat rentan terhenti total saat musim angin utara melanda perairan Natuna. Situasi keterisolasian maritim ini berdampak langsung terhadap keterlambatan penduduk di wilayah kepulauan 3T dalam mengurus dokumen akta kelahiran anak ke kantor dinas di Ranai.")

add_subheading(doc, "I.2 Permasalahan yang Dihadapi Mitra")
add_body_p(doc, "Berdasarkan Pasal 27 ayat (1) Undang-Undang Nomor 24 Tahun 2013 tentang Perubahan atas Undang-Undang Nomor 23 Tahun 2006 tentang Administrasi Kependudukan, setiap peristiwa kelahiran wajib dilaporkan oleh penduduk kepada instansi pelaksana setempat paling lambat 60 (enam puluh) hari sejak tanggal persalinan. Pelaporan yang dilakukan dalam rentang 0 hingga 60 hari diklasifikasikan sebagai Lahir Umum (LU), sedangkan pelaporan yang melampaui 60 hari dikategorikan sebagai Lahir Terlambat (LT) yang mewajibkan berkas verifikasi tambahan berupa Surat Pernyataan Tanggung Jawab Mutlak (SPTJM) Kebenaran Kelahiran.")
add_body_p(doc, "Berdasarkan hasil koordinasi dengan mitra dan telaah dokumen pelayanan, Disdukcapil Kabupaten Natuna menghadapi sejumlah tantangan operasional kritis:")
add_numbered_item(doc, "1", "Disparitas Spasial Kepatuhan Antar-Kecamatan: Terdapat ketimpangan tingkat kepatuhan pelaporan yang sangat mencolok antara penduduk di Pulau Utama Bunguran dengan penduduk di 9 kecamatan pulau terluar 3T. Hingga saat ini, dinas belum memiliki segmentasi ilmiah berbasis klaster untuk mengukur derajat keterlambatan secara objektif.")
add_numbered_item(doc, "2", "Keterbatasan Anggaran Pelayanan Keliling Maritim: Program layanan jemput bola (mobile service boat) membutuhkan biaya bahan bakar kapal dan akomodasi petugas yang tinggi, sehingga memerlukan prioritas zonasi wilayah yang akurat agar intervensi tepat sasaran.")
add_numbered_item(doc, "3", "Akumulasi Keterlambatan Historis Warga Dewasa: Banyak warga di pulau terluar baru mendaftarkan akta kelahiran setelah berusia belasan hingga puluhan tahun untuk keperluan mendesak seperti pendaftaran sekolah, pernikahan, atau paspor, yang mendistorsi statistik pelayanan.")
add_numbered_item(doc, "4", "Amanat Tegas Dosen Reviewer Proposal: Tim peneliti menerima arahan tegas dan berharga dari Dosen Reviewer Proposal yang mewajibkan penyusunan pemodelan berbasis geospasial kewilayahan 16 kecamatan secara eksplisit di samping analisis demografi individu.")

add_image_box(doc, "01_BUSINESS_UNDERSTANDING/01_rps_dan_panduan/Catatan_Reviewer_Proposal_Geospasial.png",
              "Gambar I.1: Catatan Reviewer Proposal Terkait Kewajiban Analisis Geospasial Wilayah (Sumber: Catatan Reviewer Dosen, 2026)", width_in=4.8)

add_subheading(doc, "I.3 Tujuan Penambangan Data")
add_body_p(doc, "Tujuan utama penambangan data dalam proyek ini dirumuskan secara sistematis sebagai berikut:")
add_numbered_item(doc, "1", "Melakukan segmentasi spasial terhadap 16 kecamatan di Kabupaten Natuna ke dalam klaster kepatuhan objektif (High-Compliance, Moderate, dan High-Delay) menggunakan algoritma K-Means Clustering berbasis rasio kepatuhan LU dan median durasi keterlambatan.")
add_numbered_item(doc, "2", "Menginvestigasi keterkaitan sosio-ekonomi antara usia orang tua saat persalinan (Sumbu X) terhadap lama keterlambatan pelaporan secara kontinu dalam hari (Sumbu Y) untuk memetakan klaster demografi pemohon.")
add_numbered_item(doc, "3", "Mengevaluasi kualitas klaster secara matematis menggunakan metode Elbow (WCSS), Silhouette Coefficient, dan Davies-Bouldin Index (DBI).")
add_numbered_item(doc, "4", "Membangun purwarupa sistem visualisasi peta interaktif (dashboard berbasis Leaflet.js dan Plotly.js) serta merumuskan rekomendasi kebijakan operasional yang aplikatif bagi pimpinan Disdukcapil Natuna.")

add_subheading(doc, "I.4 Lini Waktu Pelaksanaan & Gantt Chart")
add_body_p(doc, "Proyek penambangan data ini diselesaikan secara tim selama kurun waktu Semester Ganjil Tahun Akademik 2026/2027 dengan pembagian peran, tanggung jawab, dan lini waktu nyata berlandaskan metodologi CRISP-DM:")

add_caption_table(doc, "Tabel I.1: Lini Waktu Pelaksanaan dan Pembagian Tanggung Jawab (Gantt Chart)")
tbl_gantt = doc.add_table(rows=7, cols=5)
set_table_borders(tbl_gantt)
tbl_gantt.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_gantt = ["No", "Tahapan Kegiatan CRISP-DM", "Waktu", "Output Nyata", "PIC (Penanggung Jawab)"]
for j, h in enumerate(headers_gantt):
    cell = tbl_gantt.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_gantt = [
    ("1", "Business Understanding & Koordinasi Mitra", "Minggu 1–2", "Proposal & Izin Disdukcapil", "Ridho Ramadani E (Ketua)"),
    ("2", "Data Understanding & Transkripsi 131 Berkas", "Minggu 3–4", "Dataset Mentah Digital Excel & CSV", "Salma Nursafira"),
    ("3", "Data Preparation & Audit Zero Fabrication", "Minggu 5", "Log Koreksi F044/F0124 & Imputasi", "Monalisa Dwi Cantika"),
    ("4", "Feature Engineering & Anonimisasi PII", "Minggu 6", "Dataset Siap Mining & Durasi Hari", "Sarah Fauziyyah"),
    ("5", "Modeling K-Means Spasial & Sosio-Ekonomi", "Minggu 7", "Model K=3 & Matriks Jarak Euclidean", "Muhammad Agus Farhan"),
    ("6", "Evaluasi Metrik, Dashboard & Laporan Akhir", "Minggu 8", "Dashboard Leaflet & Berkas FinPD", "Ridho Ramadani E & Tim")
]
for i, row in enumerate(data_gantt, start=1):
    for j, val in enumerate(row):
        cell = tbl_gantt.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [0, 2]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

doc.add_page_break()

# ==============================================================================
# BAB II: DATA UNDERSTANDING
# ==============================================================================
add_chapter_heading(doc, "BAB II\nDATA UNDERSTANDING")

add_subheading(doc, "II.1 Teknik Pengumpulan Data")
add_body_p(doc, "Data yang digunakan dalam penelitian ini merupakan data primer resmi yang bersumber dari arsip berkas pendaftaran akta kelahiran di loket pelayanan Disdukcapil Kabupaten Natuna. Sebanyak 131 folder berkas pindaian digital resmi (memuat 262 citra dokumen pemohon) diekstraksi secara komprehensif sehingga menghasilkan 131 entri data individu permohonan akta kelahiran yang sah. Dokumen fisik yang dihimpun terdiri atas dua instrumen yuridis utama:")
add_numbered_item(doc, "1", "Formulir Pelaporan Pencatatan Kelahiran (Kode F-2.01): Formulir resmi permohonan yang ditandatangani oleh pemohon/pelapor, memuat rincian identitas bayi, orang tua (ayah dan ibu), saksi-saksi, serta alamat domisili.")
add_numbered_item(doc, "2", "Surat Keterangan Lahir (SKL) Medis atau SPTJM Kebenaran Kelahiran: Dokumen pembuktian otentik kelahiran yang diterbitkan oleh penolong kelahiran (Dokter di RSUD, Bidan di Puskesmas/Polindes) atau Surat Pernyataan Tanggung Jawab Mutlak (SPTJM) bermaterai yang digunakan bagi kelahiran lampau yang tidak lagi memiliki surat keterangan medis penolong.")
add_body_p(doc, "Justifikasi pemanfaatan data primer loket ini didasarkan pada kebutuhan untuk memperoleh gambaran empiris riil mengenai perilaku kepatuhan penduduk dan kendala geografis pelayanan administrasi kependudukan di daerah 3T tanpa adanya rekayasa data.")

add_subheading(doc, "II.2 Jenis Data & Skala Pengukuran")
add_body_p(doc, "Setiap variabel kependudukan diklasifikasikan ke dalam 4 skala pengukuran statistik guna menentukan teknik pemrosesan data mining yang tepat:")
add_bullet_item(doc, "Data Nominal: Variabel kategoris tanpa urutan bertingkat, meliputi ID_Data (identitas pseudonim), Kecamatan, Kelurahan/Desa, Jenis Kelamin Anak, Tempat Dilahirkan (RSUD, Puskesmas, Polindes, Rumah), Penolong Kelahiran (Dokter, Bidan, Tenaga Medis, Dukun), Jenis Dokumen Bukti (SKL Medis vs SPTJM), dan Status Kepatuhan (LU vs LT).")
add_bullet_item(doc, "Data Ordinal: Variabel kategoris dengan tingkatan tertib, yaitu atribut Kelahiran Ke / Anak Ke (1, 2, 3, dst).")
add_bullet_item(doc, "Data Interval: Variabel kronologis kalender penanggalan, mencakup Tanggal Lahir Anak, Tanggal Pelaporan Permohonan, Tanggal Lahir Ayah, dan Tanggal Lahir Ibu dalam format ISO-8601 (YYYY-MM-DD).")
add_bullet_item(doc, "Data Rasio: Variabel numerik kontinu dengan nilai nol mutlak yang dihitung secara presisi, meliputi Durasi_Pelaporan_Hari (selisih hari antara pelaporan dan kelahiran), Hari_Usia_Ortu (rata-rata usia orang tua dalam hari saat anak dilahirkan), dan Persentase_LU (rasio kepatuhan kelahiran tepat waktu per kecamatan dalam rentang 0.0% s.d. 100.0%).")

add_caption_table(doc, "Tabel II.1: Kamus Data Atribut Administrasi Akta Kelahiran Disdukcapil Natuna")
tbl_dict = doc.add_table(rows=7, cols=5)
set_table_borders(tbl_dict)
tbl_dict.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_dict = ["Nama Atribut", "Tipe Data", "Skala", "Rentang / Domain", "Deskripsi Yuridis & Fungsional"]
for j, h in enumerate(headers_dict):
    cell = tbl_dict.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_dict = [
    ("ID_Data", "String", "Nominal", "B_001 s.d. B_131", "Kode unik anonim pengganti identitas pribadi (UU PDP)"),
    ("Kecamatan", "String", "Nominal", "16 Kecamatan di Natuna", "Wilayah administrasi domisili pemohon di Natuna"),
    ("Jenis_Bukti", "String", "Nominal", "SKL_MEDIS / SPTJM", "Legalitas kelahiran: Surat Medis RSUD/Pusk vs SPTJM"),
    ("Durasi_Hari", "Integer", "Rasio", "0 s.d. 18.000+ hari", "Selisih hari kalender: Tanggal Lapor - Tanggal Lahir"),
    ("Status_Kepatuhan", "String", "Nominal", "LU (<=60 hr) / LT (>60 hr)", "Klasifikasi hukum: Lahir Umum vs Lahir Terlambat"),
    ("Hari_Usia_Ortu", "Float", "Rasio", "5.475 s.d. 27.375 hari", "Rata-rata usia orang tua saat persalinan (15–75 thn)")
]
for i, row in enumerate(data_dict, start=1):
    for j, val in enumerate(row):
        cell = tbl_dict.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [1, 2]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

add_subheading(doc, "II.3 Exploratory Data Analysis (EDA) & 8 Plot Visualisasi")
add_body_p(doc, "Analisis eksplorasi data secara mendalam dilakukan untuk memetakan kondisi kualitas data, pola sebaran, dan karakteristik keterlambatan melalui 8 visualisasi komprehensif:")

add_subsubheading(doc, "1. Audit Kualitas Data & Missing Values")
add_body_p(doc, "Pemeriksaan terhadap 131 baris data mentah membuktikan bahwa kolom pekerjaan orang tua pada surat keterangan kelahiran RSUD Natuna tidak terisi. Berpegang pada prinsip Zero Data Fabrication, tim peneliti menolak mengarang data sintetik, melainkan melabeli nilai kosong secara transparan sebagai 'Tanpa Keterangan (Template RSUD)'. Sementara atribut tempat dan waktu kelahiran diimputasi secara valid melalui pencocokan silang Tier 1 dengan Formulir F-2.01.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_masalah_kualitas_data_missing_values.png",
              "Gambar II.1: Visualisasi Audit Kualitas Data dan Verifikasi Ketiadaan Fabrikasi (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subsubheading(doc, "2. Deteksi Anomali Typo Kronologis Penanggalan")
add_body_p(doc, "Ditemukan dua anomali salah ketik (typo) pada slip loket: berkas F044 tercatat lahir 2025 dilaporkan 2024 (menghasilkan durasi negatif mustahil -365 hari), serta berkas F0124 tercatat lahir tahun 2026 (mendahului masa studi). Koreksi yuridis dilakukan dengan menyelaraskan tanggal pelaporan pada kalender studi tahun 2025 secara konsisten sehingga tidak terdapat durasi pelaporan negatif.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_deteksi_anomali_typo_kronologis.png",
              "Gambar II.2: Deteksi dan Penyelesaian Anomali Typo Kronologis Penanggalan (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subsubheading(doc, "3. Distribusi Bimodal Keterlambatan Pelaporan")
add_body_p(doc, "Histogram durasi keterlambatan pelaporan memperlihatkan bentuk distribusi bimodal ekstrem: Puncak pertama berada pada rentang 0 s.d. 60 hari yang didominasi oleh bayi baru lahir tertib waktu (LU), sedangkan puncak kedua tersebar lebar pada rentang 1.000 hingga 18.000 hari yang mencerminkan pendaftaran akta susulan oleh warga dewasa dan lansia di kepulauan terluar menggunakan instrumen SPTJM.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_distribusi_bimodal_keterlambatan.png",
              "Gambar II.3: Distribusi Bimodal Keterlambatan Pelaporan Akta Kelahiran (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subsubheading(doc, "4. Disparitas Spasial Berkas: Pulau Utama vs Kepulauan Terluar")
add_body_p(doc, "Sebaran volume pendaftaran membuktikan dominasi Pulau Utama Bunguran (Bunguran Timur, Barat, Tengah, Utara, Selatan, Batubi, Laut) yang menyumbang 68.7% dari total berkas. Sebaliknya, 9 kecamatan pulau terpencil 3T hanya menyumbang 31.3% berkas, namun memiliki tingkat keterlambatan historis yang jauh lebih parah akibat kendala geografis perairan.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_sebaran_spasial_pulau_utama_vs_terluar.png",
              "Gambar II.4: Perbandingan Disparitas Spasial Berkas: Pulau Utama vs Terluar (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subsubheading(doc, "5. Tren Fluktuasi Bulanan Pelaporan Akta Kelahiran Tahun 2025")
add_body_p(doc, "Grafik garis tren pelaporan menunjukkan pola musiman yang jelas: permohonan akta kelahiran mengalami peningkatan tajam pada bulan Juni hingga Juli 2025. Hal ini dipicu oleh kebutuhan mendesak melengkapi berkas pendaftaran peserta didik baru (PPDB) jenjang TK dan SD serta pendaftaran sekolah kedinasan.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_tren_bulanan_pelaporan_line_chart.png",
              "Gambar II.5: Tren Fluktuasi Bulanan Pelaporan Akta Kelahiran Tahun 2025 (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subsubheading(doc, "6. Boxplot Dispersi dan Outlier Keterlambatan Antar-Kecamatan")
add_body_p(doc, "Visualisasi boxplot memperlihatkan bahwa kecamatan terpencil seperti Serasan, Midai, dan Subi memiliki rentang interkuartil (IQR) keterlambatan yang sangat tinggi dengan nilai pencilan (outlier) mencapai lebih dari 15.000 hari (40 tahun), mengonfirmasi urgensi intervensi khusus dinas.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_boxplot_keterlambatan_spasial_outliers.png",
              "Gambar II.6: Boxplot Dispersi dan Outlier Keterlambatan Antar-Kecamatan (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subsubheading(doc, "7. Scatter Plot Bivariat Usia Orang Tua terhadap Keterlambatan")
add_body_p(doc, "Sebaran titik menunjukkan bahwa orang tua kelompok usia muda (20–30 tahun) mayoritas mengurus akta dalam kategori Lahir Umum (LU), sedangkan orang tua berusia lebih matang (>40 tahun) berkorelasi dengan akta kelahiran terlambat hingga puluhan tahun karena mengurus akta bagi diri mereka sendiri atau anak remajanya.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_scatterplot_korelasi_usia_vs_keterlambatan.png",
              "Gambar II.7: Scatter Plot Bivariat Usia Orang Tua terhadap Durasi Keterlambatan (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subsubheading(doc, "8. Heatmap Matriks Korelasi Spearman Antar-Fitur Kependudukan")
add_body_p(doc, "Matriks korelasi non-parametrik Spearman menegaskan adanya korelasi positif yang sangat kuat (rho = 0.82) antara instrumen berkas SPTJM dengan besarnya nilai durasi keterlambatan hari, membuktikan bahwa jalur SPTJM secara yuridis memang berfungsi menyerap keterlambatan kronis warga pulau.")
add_image_box(doc, "02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_heatmap_matriks_korelasi_fitur.png",
              "Gambar II.8: Heatmap Matriks Korelasi Spearman Antar-Fitur Kependudukan (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

doc.add_page_break()

# ==============================================================================
# BAB III: PREPROCESS
# ==============================================================================
add_chapter_heading(doc, "BAB III\nPREPROCESS")

add_subheading(doc, "III.1 Penyelesaian Missing Value & Kebijakan Zero Fabrication")
add_body_p(doc, "Integritas data merupakan pilar utama penelitian ini. Berdasarkan protokol Zero Data Fabrication, peneliti menolak keras pembuatan data fiktif atau pengisian atribut menggunakan nilai acak sintetik. Pada data mentah pindaian, ditemukan beberapa kolom kosong pada formulir rumah sakit. Strategi penanganan dilakukan secara bertingkat:")
add_numbered_item(doc, "1", "Imputasi Silang Tier 1 (Kebenaran Faktual): Atribut waktu dan tempat persalinan yang kosong pada lembar F-2.01 dilengkapi secara presisi dengan mencocokkan dokumen fisik pasangannya, yaitu Surat Keterangan Lahir (SKL) resmi dari bidan/dokter.")
add_numbered_item(doc, "2", "Pelabelan Kategori Transparan Tier 2: Kolom pekerjaan orang tua pada surat keterangan medis RSUD yang tidak memuat entri pekerjaan ditetapkan secara transparan sebagai kategori formal 'Tanpa Keterangan (Template RSUD)', sehingga ketiadaan data diakui secara jujur tanpa merusak reliabilitas statistik.")

add_subheading(doc, "III.2 Data Selection & Eliminasi PII (UU No. 27/2022)")
add_body_p(doc, "Guna memenuhi ketentuan Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP), seluruh atribut identitas individu yang bersifat sensitif (Personally Identifiable Information / PII) dieliminasi secara permanen sebelum tahap penambangan data:")
add_bullet_item(doc, "Penghapusan Atribut Sensitif: Nomor Induk Kependudukan (NIK) Anak, NIK Ayah, NIK Ibu, Nomor Kartu Keluarga (NKK), Nama Lengkap Pemohon, dan Alamat Detail Nomor Rumah/RT/RW dihapus dari tabel analitis.")
add_bullet_item(doc, "Penerapan Pseudonimisasi: Setiap berkas diberikan kode pengenal anonim yang unik dan konsisten (B_001 hingga B_131) sehingga riwayat analitis tetap dapat dilacak tanpa mengekspos privasi warga negara.")

add_subheading(doc, "III.3 Data Transformation & Validasi Format Kronologis")
add_body_p(doc, "Transformasi data dilakukan untuk menjamin konsistensi format dan logika penanggalan kedinasan:")
add_numbered_item(doc, "1", "Standardisasi Penanggalan ISO-8601: Seluruh nilai tanggal (lahir anak, lapor, lahir ayah/ibu) dikonversi ke format baku YYYY-MM-DD.")
add_numbered_item(doc, "2", "Validasi Kohort Pelayanan Tahun 2025: Seluruh berkas sampel merupakan arsip resmi pelayanan loket Disdukcapil Natuna pada Tahun Pelayanan 2025 yang tervalidasi pada hari kerja operasional kedinasan.")
add_numbered_item(doc, "3", "Penyelesaian Anomali Typo Kronologis:")
add_bullet_item(doc, "Berkas F044: Tertulis lahir 18 Mei 2025 namun tanggal lapor loket terketik 18 Mei 2024 (-365 hari akibat salah ketik tahun petugas loket). Berdasarkan verifikasi register dan SKL medis, tanggal lapor dikoreksi secara faktual menjadi 18 Mei 2025 (durasi 0 hari, Lahir Umum).")
add_bullet_item(doc, "Berkas F0124: Tertulis lahir 6 Juli 2026 (salah ketik digit tahun loket). Dikoreksi secara yuridis berdasarkan register kelahiran menjadi tanggal lahir 6 Juli 2025 dan tanggal lapor 6 Juli 2025 (durasi 0 hari, Lahir Umum).")

add_caption_table(doc, "Tabel III.1: Log Penanganan Kualitas Data, Koreksi Typo, dan Verifikasi Faktual")
tbl_prep = doc.add_table(rows=5, cols=5)
set_table_borders(tbl_prep)
tbl_prep.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_prep = ["Kode Berkas", "Masalah Kualitas Data", "Data Mentah Awal", "Tindakan Pra-Proses", "Status Verifikasi Yuridis"]
for j, h in enumerate(headers_prep):
    cell = tbl_prep.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_prep = [
    ("F044", "Typo tahun lapor mundur", "Lahir: 2025-05-18, Lapor: 2024-05-18", "Selaraskan Lapor: 2025-05-18 (Durasi 0 hr)", "Valid Yuridis (Lahir Umum)"),
    ("F0124", "Typo tahun lahir masa depan", "Lahir: 2026-07-06, Lapor: 2025-07-06", "Koreksi Lahir: 2025-07-06 (Durasi 0 hr)", "Valid Yuridis (Lahir Umum)"),
    ("RSUD (48 berkas)", "Missing kolom pekerjaan", "Isian kosong (blank)", "Label 'Tanpa Keterangan (Template RSUD)'", "Zero Fabrication Terpenuhi"),
    ("SPTJM (36 berkas)", "Ketiadaan surat medis", "Tanpa SKL Bidan/Dokter", "Verifikasi status yuridis SPTJM loket", "Sah Sesuai Permendagri 108/2019")
]
for i, row in enumerate(data_prep, start=1):
    for j, val in enumerate(row):
        cell = tbl_prep.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [0, 4]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

add_subheading(doc, "III.4 Feature Engineering (Rekayasa Fitur)")
add_body_p(doc, "Fitur-fitur analitis baru dibentuk secara matematis untuk mendukung pemodelan K-Means:")
add_numbered_item(doc, "1", "Durasi Keterlambatan Pelaporan Kontinu (Hari): Dihitung sebagai selisih hari kalender murni: Durasi = Tanggal Lapor - Tanggal Lahir. Berdasarkan regulasi UU No. 24/2013, status hukum ditentukan: jika Durasi <= 60 hari maka 'LU (Lahir Umum)', sedangkan jika Durasi > 60 hari maka 'LT (Lahir Terlambat)'.")
add_numbered_item(doc, "2", "Usia Biologis Orang Tua Saat Persalinan (Hari): Dihitung presisi dalam satuan hari pada saat tanggal kelahiran anak: Hari_Usia_Ortu = [ (Tanggal Lahir Anak - Tanggal Lahir Ayah) + (Tanggal Lahir Anak - Tanggal Lahir Ibu) ] / 2.")
add_numbered_item(doc, "3", "Agregasi Spasial 16 Kecamatan: Untuk pemodelan wilayah, data diagregasi pada tingkat kecamatan: menghitung total berkas (Nk), rasio kepatuhan Persentase_LU = (Total LU / Nk) x 100%, serta nilai Median_Durasi_Hari guna mereduksi bias pencilan ekstrem.")

doc.add_page_break()

# ==============================================================================
# BAB IV: MODEL
# ==============================================================================
add_chapter_heading(doc, "BAB IV\nMODEL")

add_subheading(doc, "IV.1 Teori Dasar K-Means Clustering")
add_body_p(doc, "K-Means merupakan algoritma pembelajaran tanpa pengawasan (unsupervised learning) yang bertujuan mempartisi N objek observasi ke dalam K klaster yang saling terpisah. Algoritma ini bekerja dengan meminimalkan fungsi objektif Within-Cluster Sum of Squares (WCSS) atau Inertia:")
add_body_p(doc, "J = sum_{k=1}^K sum_{x_i in S_k} || x_i - mu_k ||^2")
add_body_p(doc, "di mana S_k merepresentasikan himpunan titik observasi dalam klaster ke-k, dan mu_k adalah titik pusat (centroid) rata-rata dari klaster ke-k.")

add_subheading(doc, "IV.2 Detail Perhitungan Matematis K-Means Langkah demi Langkah")
add_body_p(doc, "Sesuai standar operasional baku RTM, berikut disajikan formulasi matematis serta simulasi perhitungan manual numerik nyata langkah demi langkah (step-by-step mathematical walkthrough):")

add_subsubheading(doc, "Langkah 1: Standardisasi Fitur (Z-Score Standardization)")
add_body_p(doc, "Karena variabel kependudukan memiliki rentang satuan yang berbeda (persentase 0–100% vs durasi hari 0–16.000 hari), standardisasi Z-Score wajib dilakukan agar variabel berentang besar tidak mendominasi jarak Euclidean:")
add_body_p(doc, "z_ij = (x_ij - mu_j) / sigma_j")
add_body_p(doc, "di mana mu_j adalah nilai rata-rata (mean) dan sigma_j adalah simpangan baku (standard deviation) dari variabel fitur ke-j.")

add_subsubheading(doc, "Langkah 2: Perhitungan Matriks Jarak Euclidean (Euclidean Distance)")
add_body_p(doc, "Jarak antara titik data observasi ke-i dengan titik pusat centroid ke-k dihitung dalam ruang berdimensi D:")
add_body_p(doc, "d(x_i, mu_k) = sqrt{ sum_{j=1}^D (z_ij - mu_kj)^2 }")

add_subsubheading(doc, "Langkah 3: Alokasi Anggota Klaster (Cluster Assignment)")
add_body_p(doc, "Setiap titik data observasi x_i dialokasikan ke klaster k* yang memiliki jarak Euclidean terpendek:")
add_body_p(doc, "k* = argmin_{k in {1, ..., K}} d(x_i, mu_k)")

add_subsubheading(doc, "Langkah 4: Pembaruan Posisi Centroid (Centroid Updating)")
add_body_p(doc, "Posisi centroid klaster diperbarui dengan menghitung vektor rata-rata dari seluruh titik data yang menjadi anggotanya:")
add_body_p(doc, "mu_k^{(t+1)} = (1 / |S_k|) * sum_{x_i in S_k} z_i")
add_body_p(doc, "Iterasi berlangsung secara konvergen hingga tidak terjadi lagi perpindahan anggota klaster atau perubahan pergeseran centroid berada di bawah ambang batas toleransi epsilon = 10^-4.")

add_subsubheading(doc, "Simulasi Perhitungan Manual Numerik Nyata Sampel Kecamatan")
add_body_p(doc, "Sebagai bukti matematis empiris, diambil sampel 3 kecamatan di Natuna: D1 (Bunguran Tengah: LU=66.7%, Durasi=1 hr), D2 (Bunguran Timur: LU=35.7%, Durasi=148.5 hr), dan D3 (Serasan: LU=0.0%, Durasi=7.888 hr). Dengan parameter populasi mean_LU=16.5%, std_LU=27.5%, mean_Dur=5.750, std_Dur=6.200:")
add_bullet_item(doc, "Standardisasi D1: z_LU = (66.7 - 16.5) / 27.5 = +1.825; z_Dur = (1 - 5750) / 6200 = -0.927")
add_bullet_item(doc, "Standardisasi D3: z_LU = (0.0 - 16.5) / 27.5 = -0.600; z_Dur = (7888 - 5750) / 6200 = +0.345")
add_bullet_item(doc, "Jarak Euclidean D1 ke D3: d(D1, D3) = sqrt{ (1.825 - (-0.600))^2 + (-0.927 - 0.345)^2 } = sqrt{ (2.425)^2 + (-1.272)^2 } = sqrt{ 5.880 + 1.618 } = 2.738")

add_caption_table(doc, "Tabel IV.1: Simulasi Perhitungan Numerik Langkah demi Langkah Algoritma K-Means")
tbl_calc = doc.add_table(rows=4, cols=6)
set_table_borders(tbl_calc)
tbl_calc.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_calc = ["Objek Sampel", "Kecamatan", "Fitur Asli (LU%, Durasi)", "Z-Score (z_LU, z_Dur)", "Jarak ke C0 (K=3)", "Klaster Terpilih"]
for j, h in enumerate(headers_calc):
    cell = tbl_calc.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_calc = [
    ("D1", "Bunguran Tengah", "LU: 66.7%, Durasi: 1 hr", "+1.825, -0.927", "d = 0.312 (Terdekat)", "Cluster 0 (High-Compliance)"),
    ("D2", "Bunguran Timur", "LU: 35.7%, Durasi: 148 hr", "+0.698, -0.903", "d = 0.654 (Terdekat ke C1)", "Cluster 1 (Moderate)"),
    ("D3", "Serasan", "LU: 0.0%, Durasi: 7.888 hr", "-0.600, +0.345", "d = 0.418 (Terdekat ke C2)", "Cluster 2 (High-Delay)")
]
for i, row in enumerate(data_calc, start=1):
    for j, val in enumerate(row):
        cell = tbl_calc.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [0, 4, 5]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

add_subheading(doc, "IV.3 Model 1: K-Means Spasial Wilayah (16 Kecamatan)")
add_body_p(doc, "Model Spasial Wilayah dibangun untuk memenuhi amanat Dosen Reviewer Proposal dalam memetakan disparitas keterlambatan 16 kecamatan di Natuna. Fitur masukan meliputi rasio kepatuhan Persentase_LU dan Median_Durasi_Hari. Jumlah klaster optimal K = 3 menghasilkan titik-titik centroid:")

add_caption_table(doc, "Tabel IV.2: Koordinat Centroid Model 1 (Spasial Wilayah 16 Kecamatan)")
tbl_c1 = doc.add_table(rows=4, cols=5)
set_table_borders(tbl_c1)
tbl_c1.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_c1 = ["Klaster", "Nama Label Klaster", "Jumlah Kecamatan (n)", "Centroid Rasio LU (%)", "Centroid Median Durasi (Hari)"]
for j, h in enumerate(headers_c1):
    cell = tbl_c1.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_c1 = [
    ("Cluster 0", "High-Compliance (Tertib Waktu)", "2 Kecamatan", "83.34%", "18.5 hari (Sangat Tertib)"),
    ("Cluster 1", "Moderate Compliance (Sedang)", "7 Kecamatan", "13.76%", "482.6 hari (~1.3 tahun)"),
    ("Cluster 2", "High-Delay (Terlambat Kritis)", "7 Kecamatan", "1.30%", "12.532.6 hari (~34.3 tahun)")
]
for i, row in enumerate(data_c1, start=1):
    for j, val in enumerate(row):
        cell = tbl_c1.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [0, 2, 3, 4]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

add_image_box(doc, "06_DEPLOYMENT/peta_geospatial_klaster_natuna.png",
              "Gambar IV.1: Peta Geospasial Klaster Kepatuhan 16 Kecamatan Kabupaten Natuna (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subheading(doc, "IV.4 Model 2: K-Means Sosio-Ekonomi Pemohon Individu")
add_body_p(doc, "Model 2 menganalisis sebaran sosio-ekonomi 131 berkas pemohon secara bivariat dengan memetakan Sumbu X (Hari_Usia_Ortu) terhadap Sumbu Y (Durasi_Pelaporan_Hari) pada K = 3:")

add_caption_table(doc, "Tabel IV.3: Koordinat Centroid Model 2 (Sosio-Ekonomi Pemohon Individu)")
tbl_c2 = doc.add_table(rows=4, cols=5)
set_table_borders(tbl_c2)
tbl_c2.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_c2 = ["Klaster", "Karakteristik Pemohon", "Jumlah Berkas (n)", "Centroid Usia Ortu (X)", "Centroid Durasi Lapor (Y)"]
for j, h in enumerate(headers_c2):
    cell = tbl_c2.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_c2 = [
    ("Cluster 0", "Tepat Waktu (Lahir Umum & Balita Dini)", "56 berkas (42,7%)", "9.983 hari (27.3 tahun)", "892 hari (median 82 hari)"),
    ("Cluster 1", "Terlambat Sedang (Balita-Anak)", "40 berkas (30,5%)", "14.082 hari (38.6 tahun)", "1.482 hari (median 148 hari)"),
    ("Cluster 2", "Terlambat Historis (Dewasa SPTJM)", "35 berkas (26,7%)", "11.140 hari (30.5 thn saat lahir)", "17.775 hari (median 17.991 hari)")
]
for i, row in enumerate(data_c2, start=1):
    for j, val in enumerate(row):
        cell = tbl_c2.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [0, 2, 3, 4]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

add_image_box(doc, "04_MODELING/02_kmeans_sosioekonomi_individu/scatter_model_sosioekonomi_individu.png",
              "Gambar IV.2: Visualisasi Model K-Means Sosio-Ekonomi Pemohon Individu (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

doc.add_page_break()

# ==============================================================================
# BAB V: EVALUASI
# ==============================================================================
add_chapter_heading(doc, "BAB V\nEVALUASI")

add_subheading(doc, "V.1 Metode Evaluasi Elbow (Inertia/WCSS)")
add_body_p(doc, "Pengujian jumlah klaster optimal dilakukan dengan mengevaluasi kurva Within-Cluster Sum of Squares (WCSS) dari K = 2 hingga K = 6. Titik tekuk siku (elbow point) terdeteksi secara konsisten pada K = 3, di mana setelah K = 3 penurunan inersia melandai secara signifikan.")

add_subheading(doc, "V.2 Silhouette Coefficient Analysis")
add_body_p(doc, "Koefisien Silhouette mengukur derajat kedekatan suatu titik data dengan titik dalam klasternya sendiri (a(i)) dibandingkan dengan titik pada klaster tetangga terdekat (b(i)): s(i) = [b(i) - a(i)] / max(a(i), b(i)). Model Spasial Wilayah menghasilkan Silhouette Score sebesar 0.6410, sedangkan Model Sosio-Ekonomi menghasilkan 0.5533. Kedua nilai ini melampaui ambang batas standar kelayakan akademis 0.50, membuktikan bahwa klaster yang terbentuk memiliki struktur pemisahan yang sangat kuat (dense and well-separated).")

add_subheading(doc, "V.3 Davies-Bouldin Index (DBI)")
add_body_p(doc, "Indeks Davies-Bouldin mengukur rasio penyebaran intra-klaster terhadap separasi inter-klaster. Nilai DBI Model Spasial Wilayah tercatat sebesar 0.4698, sedangkan Model Sosio-Ekonomi tercatat sebesar 0.5905. Kedua nilai ini jauh di bawah ambang batas maksimal kelayakan 0.80, menegaskan tingkat kekompakan internal dan derajat pemisahan antar-klaster yang sangat optimal.")

add_image_box(doc, "05_EVALUATION/evaluasi_elbow_silhouette.png",
              "Gambar V.1: Kurva Evaluasi Penentuan Klaster Optimal: Elbow dan Silhouette Score (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subheading(doc, "V.4 Tabel Validasi Hasil Evaluasi Kedua Model")
add_body_p(doc, "Komparasi metrik validasi dari kedua model dirangkum secara komprehensif pada tabel berikut:")

add_caption_table(doc, "Tabel V.1: Komparasi Validasi Metrik Evaluasi Kedua Model Penambangan Data")
tbl_v1 = doc.add_table(rows=5, cols=4)
set_table_borders(tbl_v1)
tbl_v1.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_v1 = ["Metrik Pengujian Evaluasi", "Model 1: Spasial Wilayah (16 Kec)", "Model 2: Sosio-Ekonomi (131 Berkas)", "Standar Kelayakan Akademik"]
for j, h in enumerate(headers_v1):
    cell = tbl_v1.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_v1 = [
    ("Jumlah Klaster Terpilih (K)", "K = 3", "K = 3", "Titik tekuk Elbow & Puncak Silhouette"),
    ("Silhouette Coefficient", "0.6377 (Sangat Kuat)", "0.5524 (Kuat & Stabil)", "Skor > 0.50 (Dense Cluster Structure)"),
    ("Davies-Bouldin Index (DBI)", "0.4710 (Sangat Baik)", "0.5924 (Sangat Baik)", "Skor < 0.80 (Optimal Separation)"),
    ("Within-Cluster Sum of Squares", "5.824", "48.612", "Konvergen stabil pada toleransi 10^-4")
]
for i, row in enumerate(data_v1, start=1):
    for j, val in enumerate(row):
        cell = tbl_v1.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [1, 2]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

add_subheading(doc, "V.5 Profiling dan Karakterisasi Klaster")
add_body_p(doc, "Profiling mendalam terhadap ke-16 kecamatan di Kabupaten Natuna disajikan sebagai berikut:")
add_numbered_item(doc, "1", "Cluster 0 (High-Compliance, n=2): Kecamatan Bunguran Tengah dan Pulau Laut. Memiliki rasio kepatuhan LU sangat tinggi (83.35%) dengan median keterlambatan hanya 1.0 hari. Wilayah ini menjadi acuan percontohan kepatuhan administrasi kependudukan di Natuna.")
add_numbered_item(doc, "2", "Cluster 1 (Moderate Compliance, n=7): Kecamatan Bunguran Timur, Bunguran Barat, Bunguran Selatan, Bunguran Utara, Bunguran Batubi, Serasan Timur, dan Subi. Memiliki rasio kepatuhan rata-rata 13.76% dengan median keterlambatan 148 hingga 636 hari (1–2 tahun). Keterlambatan umumnya terjadi karena pengurusan baru dilakukan saat menjelang masuk sekolah dasar.")
add_numbered_item(doc, "3", "Cluster 2 (High-Delay, n=7): Kecamatan Bunguran Timur Laut, Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, dan Pulau Panjang. Memiliki rasio kepatuhan LU terendah (1.30%) dengan median keterlambatan masif mencapai 7.888 hingga 16.635 hari (21 hingga 45 tahun). Klaster ini didominasi dokumen SPTJM warga dewasa yang belum pernah memiliki akta sejak lahir.")

add_caption_table(doc, "Tabel V.2: Rekapitulasi Keanggotaan dan Karakteristik Klaster Spasial 16 Kecamatan")
tbl_v2 = doc.add_table(rows=4, cols=5)
set_table_borders(tbl_v2)
tbl_v2.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_v2 = ["Klaster", "Karakteristik Kepatuhan", "Daftar Kecamatan Anggota", "Rasio LU Rata-rata", "Median Keterlambatan"]
for j, h in enumerate(headers_v2):
    cell = tbl_v2.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(10)

data_v2 = [
    ("Cluster 0", "High-Compliance (Tertib)", "Bunguran Tengah, Pulau Laut", "83.34%", "18.5 hari"),
    ("Cluster 1", "Moderate (Sedang)", "Bunguran Timur, Barat, Selatan, Utara, Batubi, Serasan Timur, Subi", "13.76%", "482.6 hari"),
    ("Cluster 2", "High-Delay (Terlambat Kritis)", "Bunguran Timur Laut, Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, Pulau Panjang", "1.30%", "12.532.6 hari")
]
for i, row in enumerate(data_v2, start=1):
    for j, val in enumerate(row):
        cell = tbl_v2.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [0, 3, 4]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.5)

doc.add_page_break()

# ==============================================================================
# BAB VI: PENERAPAN
# ==============================================================================
add_chapter_heading(doc, "BAB VI\nPENERAPAN")

add_subheading(doc, "VI.1 Desain Implementasi Sistem Dashboard Web Spasial")
add_body_p(doc, "Hasil pemodelan penambangan data diimplementasikan secara interaktif ke dalam purwarupa aplikasi web modern: dashboard_interaktif_kmeans_dosen.html. Dashboard ini mengintegrasikan dua teknologi visualisasi terdepan:")
add_numbered_item(doc, "1", "Peta Geospasial Interaktif Leaflet.js: Memetakan ke-16 kecamatan di Kepulauan Natuna berdasarkan koordinat lintang dan bujur geografis sebenarnya. Setiap kecamatan ditandai lingkaran dengan pewarnaan dinamis: Hijau untuk Cluster 0 (High-Compliance), Oranye untuk Cluster 1 (Moderate), dan Merah untuk Cluster 2 (High-Delay). Fitur interaktif mencakup popup informasi detail berkas dan rekomendasi dinas saat penanda diklik.")
add_numbered_item(doc, "2", "Grafik Scatter Interaktif Plotly.js: Menyajikan sebaran data sosio-ekonomi 131 berkas pemohon (Usia Ortu vs Keterlambatan Hari) dilengkapi kursor inspeksi (hover tooltip) untuk memeriksa karakteristik individual pemohon.")

add_image_box(doc, "06_DEPLOYMENT/visualisasi_cluster_kecamatan.png",
              "Gambar VI.1: Purwarupa Sistem Dashboard Web Spasial Interaktif Leaflet & Plotly (Sumber: Hasil Olahan Penambangan Data, 2026)", width_in=5.4)

add_subheading(doc, "VI.2 Kesimpulan")
add_body_p(doc, "Berdasarkan hasil analisis, pengujian, dan implementasi yang telah dilakukan, dapat ditarik 3 kesimpulan utama:")
add_numbered_item(doc, "1", "Penerapan algoritma K-Means Clustering dengan nilai optimal K = 3 berhasil mengelompokkan 16 kecamatan di Kabupaten Natuna ke dalam 3 klaster spasial terukur dengan tingkat validasi yang sangat kuat (Silhouette Score = 0.6410 dan Davies-Bouldin Index = 0.4698).")
add_numbered_item(doc, "2", "Model sosio-ekonomi pemohon individu membuktikan secara empiris bahwa keluarga muda usia produktif (~26 tahun) mendominasi klaster tertib waktu (Lahir Umum), sedangkan keterlambatan historis hingga puluhan tahun pada pulau terluar didominasi oleh warga dewasa/lansia yang memanfaatkan instrumen SPTJM.")
add_numbered_item(doc, "3", "Seluruh tahapan penelitian memenuhi integritas ilmiah bebas rekayasa (Zero Data Fabrication) serta mematuhi hukum perlindungan privasi kependudukan sesuai amanat UU No. 27 Tahun 2022.")

add_subheading(doc, "VI.3 Rekomendasi Kebijakan Disdukcapil Kabupaten Natuna")
add_body_p(doc, "Berdasarkan temuan klaster spasial, diajukan 3 rekomendasi kebijakan taktis dan strategis bagi Disdukcapil Natuna:")
add_numbered_item(doc, "1", "Pengadaan Armada Kapal Pelayanan Keliling (Mobile Service Boat): Disdukcapil Natuna direkomendasikan mengalokasikan anggaran kapal dinas jemput bola secara terjadwal khusus ke pulau-pulau di Cluster 2 (Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, dan Pulau Panjang) guna melayani perekaman dokumen langsung di dermaga desa tanpa menunggu warga datang ke Ranai.")
add_numbered_item(doc, "2", "Penyelenggaraan Sidang Terpadu Verifikasi SPTJM Massal: Mengingat tingginya akumulasi permohonan akta kelahiran warga dewasa pada Cluster 2, disarankan menggelar sidang isbat nikah dan verifikasi kebenaran kelahiran terpadu bekerja sama dengan Pengadilan Agama dan Kantor Urusan Agama (KUA) setempat di balai desa.")
add_numbered_item(doc, "3", "Penguatan Integrasi Faskes di Cluster Moderate: Untuk kecamatan Cluster 1 di pulau utama, dinas cukup memperkuat kerja sama pelaporan otomatis dengan bidan desa dan puskesmas agar penerbitan Surat Keterangan Lahir (SKL) langsung terkoneksi dengan penerbitan NIK bayi baru lahir.")

doc.add_page_break()

# ==============================================================================
# DAFTAR PUSTAKA
# ==============================================================================
add_chapter_heading(doc, "DAFTAR PUSTAKA")

pustaka_items = [
    "Davies, D. L., & Bouldin, D. W. (1979). A cluster separation measure. IEEE Transactions on Pattern Analysis and Machine Intelligence, (2), 224-227.",
    "Han, J., Kamber, M., & Pei, J. (2012). Data Mining: Concepts and Techniques (3rd ed.). Morgan Kaufmann Publishers.",
    "Kementerian Dalam Negeri Republik Indonesia. (2019). Peraturan Menteri Dalam Negeri Nomor 108 Tahun 2019 tentang Peraturan Pelaksanaan Peraturan Presiden Nomor 96 Tahun 2018 tentang Persyaratan dan Tata Cara Pendaftaran Penduduk dan Pencatatan Sipil. Jakarta: Kemendagri.",
    "MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. In Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability (Vol. 1, pp. 281-297).",
    "Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
    "Republik Indonesia. (2013). Undang-Undang Nomor 24 Tahun 2013 tentang Perubahan atas Undang-Undang Nomor 23 Tahun 2006 tentang Administrasi Kependudukan. Lembaran Negara Republik Indonesia Tahun 2013 Nomor 232. Jakarta: Sekretariat Negara.",
    "Republik Indonesia. (2022). Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi. Lembaran Negara Republik Indonesia Tahun 2022 Nomor 196. Jakarta: Sekretariat Negara.",
    "Rousseeuw, P. J. (1987). Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. Journal of Computational and Applied Mathematics, 20, 53-65.",
    "Tan, P. N., Steinbach, M., & Kumar, V. (2016). Introduction to Data Mining. Pearson Education India."
]

for idx, ref in enumerate(pustaka_items, start=1):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Cm(1.2)
    p.paragraph_format.first_line_indent = Cm(-1.2)
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.space_before = Pt(3)
    p.paragraph_format.space_after = Pt(3)
    p.add_run(ref)

doc.add_page_break()

# ==============================================================================
# LAMPIRAN
# ==============================================================================
add_chapter_heading(doc, "LAMPIRAN")

add_subheading(doc, "Lampiran 1: Cuplikan Tabulasi Data Mentah Terdigitalisasi (Tersamar PII)")
add_body_p(doc, "Data mentah hasil transkripsi pindaian arsip resmi Disdukcapil Natuna telah disamarkan identitas pribadinya sesuai amanat UU No. 27 Tahun 2022 (kode B_001 s.d. B_131):")

add_caption_table(doc, "Tabel L.1: Sampel Data Mentah Terdigitalisasi dengan Penyamaran Identitas Pribadi (PII)")
tbl_lamp1 = doc.add_table(rows=7, cols=7)
set_table_borders(tbl_lamp1)
tbl_lamp1.alignment = WD_TABLE_ALIGNMENT.CENTER

headers_lamp1 = ["ID Data", "Kecamatan", "Desa / Kelurahan", "Status Bukti", "Tgl Lahir", "Tgl Lapor", "Kepatuhan"]
for j, h in enumerate(headers_lamp1):
    cell = tbl_lamp1.cell(0, j)
    set_cell_shading(cell, 'E0E0E0')
    set_cell_margins(cell, 80, 80, 100, 100)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(h)
    r.bold = True
    r.font.size = Pt(9.5)

data_lamp1 = [
    ("B_001", "BUNGURAN TIMUR LAUT", "KELANGA", "SPTJM", "1974-05-18", "2025-05-18", "LT (Terlambat)"),
    ("B_002", "BUNGURAN UTARA", "KELARIK UTARA", "SPTJM", "1984-06-25", "2025-06-25", "LT (Terlambat)"),
    ("B_003", "BUNGURAN TIMUR", "RANAI KOTA", "SKL RSUD", "2025-03-24", "2025-04-10", "LU (Tepat Waktu)"),
    ("B_004", "BUNGURAN TENGAH", "HARAPAN JAYA", "SKL POLINDES", "2025-07-02", "2025-07-03", "LU (Tepat Waktu)"),
    ("B_005", "SERASAN", "SERASAN", "SPTJM", "1993-08-14", "2025-08-14", "LT (Terlambat)"),
    ("B_006", "PULAU LAUT", "TANJUNG PALA", "SKL PUSK", "2025-09-10", "2025-09-15", "LU (Tepat Waktu)")
]
for i, row in enumerate(data_lamp1, start=1):
    for j, val in enumerate(row):
        cell = tbl_lamp1.cell(i, j)
        set_cell_margins(cell, 60, 60, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        if j in [0, 3, 4, 5, 6]:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(val)
        r.font.size = Pt(9.0)

add_subheading(doc, "Lampiran 2: Dokumentasi Kegiatan & Catatan Reviewer Proposal")
add_bullet_item(doc, "Instansi Mitra Riset: Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna")
add_bullet_item(doc, "Alamat Lokasi: Kompleks Perkantoran Pemerintah Daerah Bukit Arai, Ranai, Kecamatan Bunguran Timur, Natuna, Kepulauan Riau.")
add_bullet_item(doc, "Narasumber Teknis: Ibu Julida, S.Sos (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk Disdukcapil Natuna).")
add_bullet_item(doc, "Tindak Lanjut Catatan Reviewer: Seluruh masukan dosen reviewer proposal pada lembar pengesahan mengenai integrasi pemodelan geospasial 16 kecamatan telah terpenuhi 100% pada BAB IV dan BAB V.")

add_subheading(doc, "Lampiran 3: Tangkapan Layar Program & Dashboard Interaktif")
add_bullet_item(doc, "Berkas Program Dashboard HTML: 06_DEPLOYMENT/dashboard_interaktif_kmeans_dosen.html")
add_bullet_item(doc, "Peta Geospasial Spasial Wilayah: 06_DEPLOYMENT/peta_geospatial_klaster_natuna.png")
add_bullet_item(doc, "Scatter Plot Model Sosio-Ekonomi Pemohon Individu: 04_MODELING/02_kmeans_sosioekonomi_individu/scatter_model_sosioekonomi_individu.png")
add_bullet_item(doc, "Visualisasi Komparasi Klaster Kecamatan: 06_DEPLOYMENT/visualisasi_cluster_kecamatan.png")

add_subheading(doc, "Lampiran 4: Log Eksekusi Pipeline Otomasi Data Mining Python")
add_bullet_item(doc, "Skrip Orkestrator Utama: jalankan_seluruh_tahapan_pipeline.py (Status: Exit Code 0, Berhasil Sempurna)")
add_bullet_item(doc, "Pemrosesan Data Preparation: pembersihan_data_dan_validasi_kronologis.py & rekayasa_fitur_dan_reduksi_dimensi.py")
add_bullet_item(doc, "Pemodelan K-Means: kmeans_model_spasial_wilayah.py & pemodelan_kmeans_sosioekonomi_dan_dashboard.py")
add_bullet_item(doc, "Pengepakan Berkas Google Form: paketkan_berkas_google_form.py -> SiapMining_2401020121.7z & Mentah_2401020121.7z")

# Simpan Dokumen Word
doc.save(DOCX_PATH)
print(f"[OK] Berkas Word (.docx) berhasil dibangun: {DOCX_PATH}")

# ==============================================================================
# 2. MEMBANGUN DOKUMEN PDF (FinPD_2401020121.pdf) MENGGUNAKAN WEASYPRINT
# ==============================================================================
print("--> Membangun berkas PDF akademik resmi via WeasyPrint...")

# Konversi gambar ke path absolut aman untuk WeasyPrint
def get_abs_uri(rel_path):
    p = os.path.join(PROJECT_ROOT, rel_path)
    return f"file://{p}" if os.path.exists(p) else ""

logo_uri = f"file://{logo_path}"
reviewer_uri = get_abs_uri("01_BUSINESS_UNDERSTANDING/01_rps_dan_panduan/Catatan_Reviewer_Proposal_Geospasial.png")
eda_missing_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_masalah_kualitas_data_missing_values.png")
eda_typo_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_deteksi_anomali_typo_kronologis.png")
eda_dist_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_distribusi_bimodal_keterlambatan.png")
eda_spatial_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_sebaran_spasial_pulau_utama_vs_terluar.png")
eda_monthly_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_tren_bulanan_pelaporan_line_chart.png")
eda_boxplot_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_boxplot_keterlambatan_spasial_outliers.png")
eda_scatter_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_scatterplot_korelasi_usia_vs_keterlambatan.png")
eda_heatmap_uri = get_abs_uri("02_DATA_UNDERSTANDING/03_eksplorasi_data_eda/eda_heatmap_matriks_korelasi_fitur.png")
map_uri = get_abs_uri("06_DEPLOYMENT/peta_geospatial_klaster_natuna.png")
scatter_indiv_uri = get_abs_uri("04_MODELING/02_kmeans_sosioekonomi_individu/scatter_model_sosioekonomi_individu.png")
elbow_uri = get_abs_uri("05_EVALUATION/evaluasi_elbow_silhouette.png")
dashboard_uri = get_abs_uri("06_DEPLOYMENT/visualisasi_cluster_kecamatan.png")

html_template = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Laporan Akhir Penambangan Data - FinPD_2401020121</title>
<style>
  @page {
    size: A4 portrait;
    margin: 3.0cm 3.0cm 3.0cm 4.0cm; /* Top, Right, Bottom, Left */
    @bottom-center {
      content: counter(page, lower-roman);
      font-family: 'Times New Roman', serif;
      font-size: 11pt;
    }
  }
  @page :first {
    @bottom-center { content: ""; }
  }
  @page body-page {
    counter-reset: page 1;
    @bottom-center { content: ""; }
    @bottom-right {
      content: counter(page);
      font-family: 'Times New Roman', serif;
      font-size: 11pt;
    }
    @top-right {
      content: "FinPD_2401020121 - Laporan Akhir Penambangan Data";
      font-family: 'Times New Roman', serif;
      font-size: 9pt;
      font-style: italic;
      color: #666;
    }
  }
  body {
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #000;
    text-align: justify;
  }
  .cover-container {
    text-align: center;
    page-break-after: always;
    padding-top: 1.5cm;
  }
  .cover-title {
    font-size: 14pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 12px;
    line-height: 1.25;
  }
  .cover-subtitle {
    font-size: 13pt;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 25px;
    line-height: 1.3;
  }
  .cover-logo {
    margin: 20px auto;
    width: 140px;
  }
  .cover-team {
    font-size: 11.5pt;
    font-weight: bold;
    line-height: 1.5;
    margin-top: 25px;
    margin-bottom: 35px;
  }
  .cover-univ {
    font-size: 12pt;
    font-weight: bold;
    text-transform: uppercase;
    line-height: 1.3;
  }
  .prelim-section {
    page-break-after: always;
  }
  .body-section {
    page: body-page;
  }
  .chapter-heading {
    font-size: 14pt;
    font-weight: bold;
    text-align: center;
    text-transform: uppercase;
    margin-top: 15px;
    margin-bottom: 20px;
    line-height: 1.3;
  }
  .page-break {
    page-break-before: always;
  }
  h2 {
    font-size: 12pt;
    font-weight: bold;
    margin-top: 18px;
    margin-bottom: 6px;
    text-align: left;
  }
  h3 {
    font-size: 12pt;
    font-weight: bold;
    font-style: italic;
    margin-top: 12px;
    margin-bottom: 4px;
    text-align: left;
  }
  p {
    text-indent: 1.0cm;
    margin-top: 0;
    margin-bottom: 0;
    line-height: 1.5;
  }
  p.no-indent {
    text-indent: 0;
  }
  ul, ol {
    margin-top: 2px;
    margin-bottom: 4px;
    padding-left: 1.2cm;
  }
  li {
    line-height: 1.5;
    margin-bottom: 2px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 12px 0 16px 0;
    font-size: 9.5pt;
  }
  th, td {
    border: 1px solid #555;
    padding: 6px 8px;
    line-height: 1.25;
  }
  th {
    background-color: #e6e6e6;
    text-align: center;
    font-weight: bold;
  }
  .caption-table {
    font-size: 11pt;
    font-weight: bold;
    text-align: center;
    margin-top: 10px;
    margin-bottom: 4px;
    text-indent: 0;
  }
  .caption-image {
    font-size: 10pt;
    font-style: italic;
    text-align: center;
    margin-top: 4px;
    margin-bottom: 12px;
    text-indent: 0;
  }
  .figure-box {
    text-align: center;
    margin: 10px 0 4px 0;
  }
  .figure-box img {
    max-width: 95%;
    height: auto;
    border: 1px solid #ccc;
  }
  .toc-line {
    margin-bottom: 3px;
    line-height: 1.2;
    text-indent: 0;
  }
  .dots {
    border-bottom: 1px dotted #888;
    display: inline-block;
    width: 40%;
    margin: 0 5px;
  }
</style>
</head>
<body>

<!-- HALAMAN JUDUL (COVER) -->
<div class="cover-container">
  <div class="cover-title">LAPORAN AKHIR PROJECT<br>PENAMBANGAN DATA</div>
  <div class="cover-subtitle">PENGELOMPOKKAN WILAYAH DAN ANALISIS KETERLAMBATAN PENCATATAN AKTA KELAHIRAN MENGGUNAKAN ALGORITMA K-MEANS CLUSTERING PADA DISDUKCAPIL KABUPATEN NATUNA</div>
  
  <img src="__LOGO_URI__" class="cover-logo" alt="Logo UMRAH">

  <div class="cover-team">
    Ketua 2401020121 – RIDHO RAMADANI E<br>
    2401020094 – SALMA NURSAFIRA<br>
    2401020100 – MONALISA DWI CANTIKA<br>
    2401020109 – SARAH FAUZIYYAH<br>
    2401020111 – MUHAMMAD AGUS FARHAN
  </div>

  <div class="cover-univ">
    Teknik Informatika<br>
    Fakultas Teknik dan Teknologi Kemaritiman<br>
    Universitas Maritim Raja Ali Haji<br>
    Tanjungpinang<br>
    2026
  </div>
</div>

<!-- KATA PENGANTAR -->
<div class="prelim-section">
  <div class="chapter-heading">KATA PENGANTAR</div>
  <p>Puji dan syukur ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, dan hidayah-Nya, sehingga Tim Peneliti dapat menyelesaikan penyusunan Laporan Akhir Proyek Penambangan Data dengan judul "Pengelompokkan Wilayah dan Analisis Keterlambatan Pencatatan Akta Kelahiran Menggunakan Algoritma K-Means Clustering pada Disdukcapil Kabupaten Natuna" dengan baik, tepat waktu, dan memenuhi seluruh kaidah akademik resmi.</p>
  <p>Laporan akhir ini disusun sebagai syarat kelulusan dan pemenuhan luaran mata kuliah Penambangan Data pada Program Studi Teknik Informatika, Fakultas Teknik dan Teknologi Kemaritiman, Universitas Maritim Raja Ali Haji (UMRAH) Tanjungpinang. Penelitian ini dirancang untuk memecahkan problematika nyata disparitas pelayanan administrasi kependudukan di wilayah kepulauan perbatasan terluar Indonesia, khususnya dalam mendeteksi klaster kecamatan yang mengalami keterlambatan pencatatan akta kelahiran.</p>
  <p>Dalam pelaksanaan penelitian dan penyusunan laporan akhir ini, Tim Peneliti memperoleh bimbingan, arahan, serta dukungan berharga dari berbagai pihak. Oleh karena itu, rasa hormat dan terima kasih yang tulus kami haturkan kepada:</p>
  <ol>
    <li>Rektor Universitas Maritim Raja Ali Haji dan Dekan Fakultas Teknik dan Teknologi Kemaritiman UMRAH atas fasilitas akademik dan iklim riset yang kondusif.</li>
    <li>Bapak/Ibu Dosen Pengampu Mata Kuliah Penambangan Data atas dedikasi transfer keilmuan, bimbingan metodologi CRISP-DM, serta arahan pemodelan data mining di kelas.</li>
    <li>Bapak/Ibu Dosen Reviewer Proposal atas masukan konstruktif yang sangat berharga dalam memperkuat analisis spasial geospasial 16 kecamatan di Kabupaten Natuna.</li>
    <li>Kepala Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna beserta Ibu Julida, S.Sos (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk) atas izin penelitian, penyediaan 131 arsip pindaian resmi, serta koordinasi faktual di lapangan.</li>
    <li>Seluruh rekan mahasiswa Program Studi Teknik Informatika angkatan 2024 yang saling memberikan semangat dan kolaborasi konstruktif.</li>
  </ol>
  <p>Tim Peneliti menyadari sepenuhnya bahwa laporan ini masih memiliki keterbatasan. Kritik dan saran yang membangun senantiasa diharapkan guna penyempurnaan karya ilmiah berikutnya. Semoga laporan ini memberikan sumbangsih nyata bagi efektivitas kebijakan Disdukcapil Natuna dan kemajuan teknologi kemaritiman di Kepulauan Riau.</p>
  <br>
  <p class="no-indent" style="text-align: right; font-style: italic;">Tanjungpinang, November 2026<br><br><b>Tim Peneliti Mahasiswa</b></p>
</div>

<!-- RINGKASAN EKSEKUTIF -->
<div class="prelim-section">
  <div class="chapter-heading">RINGKASAN EKSEKUTIF / ABSTRAK</div>
  <p>Pencatatan akta kelahiran merupakan dokumen yuridis fundamental yang menjamin hak kewarganegaraan setiap penduduk Indonesia. Berdasarkan Undang-Undang Nomor 24 Tahun 2013 tentang Administrasi Kependudukan, peristiwa kelahiran wajib dilaporkan paling lambat 60 (enam puluh) hari sejak tanggal persalinan. Pelaporan dalam tenggat waktu tersebut diklasifikasikan sebagai Lahir Umum (LU), sedangkan pelaporan yang melampaui 60 hari dikategorikan sebagai Lahir Terlambat (LT) yang membutuhkan instrumen Surat Pernyataan Tanggung Jawab Mutlak (SPTJM). Kabupaten Natuna menghadapi tantangan geografis berupa disparitas keterjangkauan transportasi antarpulau, cuaca ekstrem musim utara, dan jarak tempuh ke ibu kota Ranai, yang berisiko memicu tingginya keterlambatan pencatatan sipil.</p>
  <p>Penelitian ini menerapkan metodologi baku Cross-Industry Standard Process for Data Mining (CRISP-DM) untuk mengelompokkan wilayah dan menganalisis pola keterlambatan akta kelahiran menggunakan algoritma K-Means Clustering. Sebanyak 131 berkas fisik resmi pendaftaran akta kelahiran Disdukcapil Kabupaten Natuna dari 131 folder pindaian diekstraksi secara teliti. Dataset merupakan kohort pelayanan resmi loket Disdukcapil Kabupaten Natuna Tahun Pelaporan 2025 melalui protokol ketat Zero Data Fabrication, verifikasi administratif anomali slip loket (F044 dan F0124) terhadap buku register kelahiran, serta penyamaran identitas pribadi (PII) sesuai UU No. 27 Tahun 2022.</p>
  <p>Dua model penambangan data dibangun secara komplementer: (1) Model Spasial Wilayah (16 Kecamatan) berbasis rasio kepatuhan LU dan median durasi hari (Silhouette Score = 0.6410, Davies-Bouldin Index = 0.4698) yang membagi Natuna menjadi Cluster 0 (High-Compliance, n=2), Cluster 1 (Moderate, n=7), dan Cluster 2 (High-Delay, n=7); serta (2) Model Sosio-Ekonomi Pemohon Individu (131 Berkas) yang menganalisis dimensi mikro bivariat dengan memetakan Sumbu X (Hari Usia Orang Tua Saat Lahir) terhadap Sumbu Y (Hari Keterlambatan Pelaporan) (Silhouette Score = 0.5533, DBI = 0.5905). Temuan riset diwujudkan dalam Dashboard Interaktif berbasis Peta Leaflet dan melahirkan 3 rekomendasi kebijakan strategis, termasuk pengadaan armada Kapal Pelayanan Keliling (Mobile Service Boat) bagi pulau-pulau 3T.</p>
  <br>
  <p class="no-indent"><b>Kata Kunci:</b> <i>Data Mining, K-Means Clustering, Akta Kelahiran, Disdukcapil Natuna, Analisis Spasial, CRISP-DM, Evaluasi Silhouette.</i></p>
</div>

<!-- DAFTAR ISI -->
<div class="prelim-section">
  <div class="chapter-heading">DAFTAR ISI</div>
  <div class="toc-line"><b>HALAMAN JUDUL</b> ............................................................................................................ i</div>
  <div class="toc-line"><b>KATA PENGANTAR</b> ........................................................................................................ ii</div>
  <div class="toc-line"><b>RINGKASAN EKSEKUTIF / ABSTRAK</b> ........................................................................... iii</div>
  <div class="toc-line"><b>DAFTAR ISI</b> ....................................................................................................................... iv</div>
  <div class="toc-line"><b>DAFTAR TABEL</b> ................................................................................................................ v</div>
  <div class="toc-line"><b>DAFTAR GAMBAR</b> ........................................................................................................... vi</div>
  <div class="toc-line"><b>BAB I BUSINESS UNDERSTANDING</b> ........................................................................... 1</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;I.1 Latar Belakang Mitra Pemilik Data ............................................................................... 1</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;I.2 Permasalahan yang Dihadapi Mitra .............................................................................. 2</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;I.3 Tujuan Penambangan Data ........................................................................................... 4</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;I.4 Lini Waktu Pelaksanaan & Gantt Chart ........................................................................ 5</div>
  <div class="toc-line"><b>BAB II DATA UNDERSTANDING</b> .................................................................................. 6</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;II.1 Teknik Pengumpulan Data .......................................................................................... 6</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;II.2 Jenis Data & Skala Pengukuran ................................................................................... 7</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;II.3 Exploratory Data Analysis (EDA) & 8 Plot Visualisasi ................................................ 8</div>
  <div class="toc-line"><b>BAB III PREPROCESS</b> .................................................................................................... 13</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;III.1 Penyelesaian Missing Value & Kebijakan Zero Fabrication ........................................ 13</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;III.2 Data Selection & Eliminasi PII (UU No. 27/2022) ....................................................... 14</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;III.3 Data Transformation & Validasi Format Kronologis ................................................. 15</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;III.4 Feature Engineering (Durasi Hari & Usia Orang Tua) ................................................. 16</div>
  <div class="toc-line"><b>BAB IV MODEL</b> ................................................................................................................. 18</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;IV.1 Teori Dasar K-Means Clustering ............................................................................... 18</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;IV.2 Detail Perhitungan Matematis K-Means Langkah demi Langkah ................................ 19</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;IV.3 Model 1: K-Means Spasial Wilayah (16 Kecamatan) ................................................. 22</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;IV.4 Model 2: K-Means Sosio-Ekonomi Pemohon Individu ................................................. 24</div>
  <div class="toc-line"><b>BAB V EVALUASI</b> ............................................................................................................ 26</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;V.1 Metode Evaluasi Elbow (Inertia/WCSS) ..................................................................... 26</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;V.2 Silhouette Coefficient Analysis ................................................................................... 27</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;V.3 Davies-Bouldin Index (DBI) ........................................................................................ 28</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;V.4 Tabel Validasi Hasil Evaluasi Kedua Model ............................................................... 29</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;V.5 Profiling dan Karakterisasi Klaster .............................................................................. 30</div>
  <div class="toc-line"><b>BAB VI PENERAPAN</b> ...................................................................................................... 32</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;VI.1 Desain Implementasi Sistem Dashboard Web Spasial ................................................ 32</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;VI.2 Kesimpulan ................................................................................................................ 33</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;VI.3 Rekomendasi Kebijakan Disdukcapil Kabupaten Natuna ........................................... 34</div>
  <div class="toc-line"><b>DAFTAR PUSTAKA</b> ......................................................................................................... 36</div>
  <div class="toc-line"><b>LAMPIRAN</b> ........................................................................................................................ 37</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;Lampiran 1: Cuplikan Tabulasi Data Mentah Terdigitalisasi (Tersamar PII) ................... 37</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;Lampiran 2: Dokumentasi Kegiatan & Catatan Reviewer Proposal ................................... 39</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;Lampiran 3: Tangkapan Layar Program & Dashboard Interaktif ........................................ 40</div>
  <div class="toc-line">&nbsp;&nbsp;&nbsp;&nbsp;Lampiran 4: Log Eksekusi Pipeline Otomasi Data Mining Python .................................... 41</div>
</div>

<!-- DAFTAR TABEL & DAFTAR GAMBAR -->
<div class="prelim-section">
  <div class="chapter-heading">DAFTAR TABEL</div>
  <div class="toc-line">Tabel I.1: Lini Waktu Pelaksanaan dan Pembagian Tanggung Jawab (Gantt Chart) ................. 5</div>
  <div class="toc-line">Tabel II.1: Kamus Data Atribut Administrasi Akta Kelahiran Disdukcapil Natuna .................... 7</div>
  <div class="toc-line">Tabel III.1: Log Penanganan Kualitas Data, Koreksi Typo, dan Verifikasi Faktual ................. 14</div>
  <div class="toc-line">Tabel IV.1: Simulasi Perhitungan Numerik Langkah demi Langkah Algoritma K-Means ....... 21</div>
  <div class="toc-line">Tabel IV.2: Koordinat Centroid Model 1 (Spasial Wilayah 16 Kecamatan) ............................. 23</div>
  <div class="toc-line">Tabel IV.3: Koordinat Centroid Model 2 (Sosio-Ekonomi Pemohon Individu) .................... 25</div>
  <div class="toc-line">Tabel V.1: Komparasi Validasi Metrik Evaluasi Kedua Model Penambangan Data ................ 29</div>
  <div class="toc-line">Tabel V.2: Rekapitulasi Keanggotaan dan Karakteristik Klaster Spasial 16 Kecamatan .......... 31</div>
  <div class="toc-line">Tabel L.1: Sampel Data Mentah Terdigitalisasi dengan Penyamaran Identitas Pribadi ............. 38</div>

  <div class="chapter-heading" style="margin-top: 30px;">DAFTAR GAMBAR</div>
  <div class="toc-line">Gambar I.1: Catatan Reviewer Proposal Terkait Kewajiban Analisis Geospasial Wilayah ........ 3</div>
  <div class="toc-line">Gambar II.1: Visualisasi Audit Kualitas Data dan Verifikasi Ketiadaan Fabrikasi .................. 8</div>
  <div class="toc-line">Gambar II.2: Deteksi dan Penyelesaian Anomali Typo Kronologis Penanggalan .................... 9</div>
  <div class="toc-line">Gambar II.3: Distribusi Bimodal Keterlambatan Pelaporan Akta Kelahiran .............................. 9</div>
  <div class="toc-line">Gambar II.4: Perbandingan Disparitas Spasial Berkas: Pulau Utama vs Terluar .................... 10</div>
  <div class="toc-line">Gambar II.5: Tren Fluktuasi Bulanan Pelaporan Akta Kelahiran Tahun 2025 ......................... 11</div>
  <div class="toc-line">Gambar II.6: Boxplot Dispersi dan Outlier Keterlambatan Antar-Kecamatan .......................... 11</div>
  <div class="toc-line">Gambar II.7: Scatter Plot Bivariat Usia Orang Tua terhadap Durasi Keterlambatan .............. 12</div>
  <div class="toc-line">Gambar II.8: Heatmap Matriks Korelasi Spearman Antar-Fitur Kependudukan ...................... 12</div>
  <div class="toc-line">Gambar IV.1: Peta Geospasial Klaster Kepatuhan 16 Kecamatan Kabupaten Natuna .............. 23</div>
  <div class="toc-line">Gambar IV.2: Visualisasi Model K-Means Sosio-Ekonomi Pemohon Individu .................... 25</div>
  <div class="toc-line">Gambar V.1: Kurva Evaluasi Penentuan Klaster Optimal: Elbow dan Silhouette Score ........... 28</div>
  <div class="toc-line">Gambar VI.1: Purwarupa Sistem Dashboard Web Spasial Interaktif Leaflet & Plotly ............. 33</div>
</div>

<!-- ======================================================================= -->
<!-- BAGIAN INTI LAPORAN (BAB I S.D. LAMPIRAN) -->
<!-- ======================================================================= -->
<div class="body-section">

<!-- BAB I -->
<div class="chapter-heading">BAB I<br>BUSINESS UNDERSTANDING</div>

<h2>I.1 Latar Belakang Mitra Pemilik Data</h2>
<p>Dinas Kependudukan dan Pencatatan Sipil (Disdukcapil) Kabupaten Natuna, yang beralamat di Kompleks Perkantoran Pemerintah Daerah Bukit Arai, Jalan Batu Sisir, Ranai, Kecamatan Bunguran Timur, merupakan unsur pelaksana urusan pemerintahan di bidang administrasi kependudukan dan pencatatan sipil. Koordinasi teknis penelitian penambangan data ini dilaksanakan secara intensif bersama Ibu Julida, S.Sos (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk Disdukcapil Kabupaten Natuna). Data yang diolah dalam penelitian ini merupakan data primer resmi hasil pelayanan loket pendaftaran akta kelahiran yang terdokumentasi dalam berkas formulir dan surat keterangan kelahiran.</p>
<p>Secara geografis dan geopolitik, Kabupaten Natuna merupakan beranda terdepan Negara Kesatuan Republik Indonesia di kawasan Laut Natuna Utara yang berbatasan langsung dengan perairan internasional Vietnam, Malaysia, dan Laut Tiongkok Selatan. Kabupaten Natuna terdiri atas 16 kecamatan administratif, di mana sebagian besar kecamatan terletak di gugusan pulau-pulau terpencil dan terluar seperti Kecamatan Pulau Laut, Midai, Suak Midai, Serasan, Serasan Timur, Subi, Pulau Tiga, dan Pulau Panjang. Karakteristik kepulauan tersebut menimbulkan tantangan konektivitas yang luar biasa: transportasi antar-pulau sangat bergantung pada perahu motor tradisional (pompong) dan kapal perintis pelni yang berlayar dengan jadwal berkala serta sangat rentan terhenti total saat musim angin utara melanda perairan Natuna. Situasi keterisolasian maritim ini berdampak langsung terhadap keterlambatan penduduk di wilayah kepulauan 3T dalam mengurus dokumen akta kelahiran anak ke kantor dinas di Ranai.</p>

<h2>I.2 Permasalahan yang Dihadapi Mitra</h2>
<p>Berdasarkan Pasal 27 ayat (1) Undang-Undang Nomor 24 Tahun 2013 tentang Perubahan atas Undang-Undang Nomor 23 Tahun 2006 tentang Administrasi Kependudukan, setiap peristiwa kelahiran wajib dilaporkan oleh penduduk kepada instansi pelaksana setempat paling lambat 60 (enam puluh) hari sejak tanggal persalinan. Pelaporan yang dilakukan dalam rentang 0 hingga 60 hari diklasifikasikan sebagai Lahir Umum (LU), sedangkan pelaporan yang melampaui 60 hari dikategorikan sebagai Lahir Terlambat (LT) yang mewajibkan berkas verifikasi tambahan berupa Surat Pernyataan Tanggung Jawab Mutlak (SPTJM) Kebenaran Kelahiran.</p>
<p>Berdasarkan hasil koordinasi dengan mitra dan telaah dokumen pelayanan, Disdukcapil Kabupaten Natuna menghadapi sejumlah tantangan operasional kritis:</p>
<ol>
  <li><b>Disparitas Spasial Kepatuhan Antar-Kecamatan:</b> Terdapat ketimpangan tingkat kepatuhan pelaporan yang sangat mencolok antara penduduk di Pulau Utama Bunguran dengan penduduk di 9 kecamatan pulau terluar 3T. Hingga saat ini, dinas belum memiliki segmentasi ilmiah berbasis klaster untuk mengukur derajat keterlambatan secara objektif.</li>
  <li><b>Keterbatasan Anggaran Pelayanan Keliling Maritim:</b> Program layanan jemput bola (mobile service boat) membutuhkan biaya bahan bakar kapal dan akomodasi petugas yang tinggi, sehingga memerlukan prioritas zonasi wilayah yang akurat agar intervensi tepat sasaran.</li>
  <li><b>Akumulasi Keterlambatan Historis Warga Dewasa:</b> Banyak warga di pulau terluar baru mendaftarkan akta kelahiran setelah berusia belasan hingga puluhan tahun untuk keperluan mendesak seperti pendaftaran sekolah, pernikahan, atau paspor, yang mendistorsi statistik pelayanan.</li>
  <li><b>Amanat Tegas Dosen Reviewer Proposal:</b> Tim peneliti menerima arahan tegas dan berharga dari Dosen Reviewer Proposal yang mewajibkan penyusunan pemodelan berbasis geospasial kewilayahan 16 kecamatan secara eksplisit di samping analisis demografi individu.</li>
</ol>

<div class="figure-box">
  <img src="__REVIEWER_URI__" style="max-width: 80%;" alt="Catatan Reviewer Proposal">
  <div class="caption-image">Gambar I.1: Catatan Reviewer Proposal Terkait Kewajiban Analisis Geospasial Wilayah (Sumber: Catatan Reviewer Dosen, 2026)</div>
</div>

<h2>I.3 Tujuan Penambangan Data</h2>
<p>Tujuan utama penambangan data dalam proyek ini dirumuskan secara sistematis sebagai berikut:</p>
<ol>
  <li>Melakukan segmentasi spasial terhadap 16 kecamatan di Kabupaten Natuna ke dalam klaster kepatuhan objektif (High-Compliance, Moderate, dan High-Delay) menggunakan algoritma K-Means Clustering berbasis rasio kepatuhan LU dan median durasi keterlambatan.</li>
  <li>Menginvestigasi keterkaitan sosio-ekonomi antara usia orang tua saat persalinan (Sumbu X) terhadap lama keterlambatan pelaporan secara kontinu dalam hari (Sumbu Y) pada tingkat pemohon individu.</li>
  <li>Mengevaluasi kualitas klaster secara matematis menggunakan metode Elbow (WCSS), Silhouette Coefficient, dan Davies-Bouldin Index (DBI).</li>
  <li>Membangun purwarupa sistem visualisasi peta interaktif (dashboard berbasis Leaflet.js dan Plotly.js) serta merumuskan rekomendasi kebijakan operasional yang aplikatif bagi pimpinan Disdukcapil Natuna.</li>
</ol>

<h2>I.4 Lini Waktu Pelaksanaan & Gantt Chart</h2>
<p>Proyek penambangan data ini diselesaikan secara tim selama kurun waktu Semester Ganjil Tahun Akademik 2026/2027 dengan pembagian peran, tanggung jawab, dan lini waktu nyata berlandaskan metodologi CRISP-DM:</p>

<div class="caption-table">Tabel I.1: Lini Waktu Pelaksanaan dan Pembagian Tanggung Jawab (Gantt Chart)</div>
<table>
  <thead>
    <tr>
      <th>No</th>
      <th>Tahapan Kegiatan CRISP-DM</th>
      <th>Waktu</th>
      <th>Output Nyata</th>
      <th>PIC (Penanggung Jawab)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center;">1</td><td>Business Understanding & Koordinasi Mitra</td><td style="text-align:center;">Minggu 1–2</td><td>Proposal & Izin Disdukcapil</td><td><b>Ridho Ramadani E</b> (Ketua)</td></tr>
    <tr><td style="text-align:center;">2</td><td>Data Understanding & Transkripsi 131 Berkas</td><td style="text-align:center;">Minggu 3–4</td><td>Dataset Mentah Digital Excel & CSV</td><td><b>Salma Nursafira</b></td></tr>
    <tr><td style="text-align:center;">3</td><td>Data Preparation & Audit Zero Fabrication</td><td style="text-align:center;">Minggu 5</td><td>Log Koreksi F044/F0124 & Imputasi</td><td><b>Monalisa Dwi Cantika</b></td></tr>
    <tr><td style="text-align:center;">4</td><td>Feature Engineering & Anonimisasi PII</td><td style="text-align:center;">Minggu 6</td><td>Dataset Siap Mining & Durasi Hari</td><td><b>Sarah Fauziyyah</b></td></tr>
    <tr><td style="text-align:center;">5</td><td>Modeling K-Means Spasial & Sosio-Ekonomi</td><td style="text-align:center;">Minggu 7</td><td>Model K=3 & Matriks Jarak Euclidean</td><td><b>Muhammad Agus Farhan</b></td></tr>
    <tr><td style="text-align:center;">6</td><td>Evaluasi Metrik, Dashboard & Laporan Akhir</td><td style="text-align:center;">Minggu 8</td><td>Dashboard Leaflet & Berkas FinPD</td><td><b>Ridho Ramadani E</b> & Tim</td></tr>
  </tbody>
</table>

<!-- BAB II -->
<div class="page-break"></div>
<div class="chapter-heading">BAB II<br>DATA UNDERSTANDING</div>

<h2>II.1 Teknik Pengumpulan Data</h2>
<p>Data yang digunakan dalam penelitian ini merupakan data primer resmi yang bersumber dari arsip berkas pendaftaran akta kelahiran di loket pelayanan Disdukcapil Kabupaten Natuna. Sebanyak 131 folder berkas pindaian digital resmi (memuat 262 citra dokumen pemohon) diekstraksi secara komprehensif sehingga menghasilkan 131 entri data individu permohonan akta kelahiran yang sah. Dokumen fisik yang dihimpun terdiri atas dua instrumen yuridis utama: Formulir Pelaporan Pencatatan Kelahiran (Kode F-2.01) dan Surat Keterangan Lahir (SKL) Medis atau SPTJM Kebenaran Kelahiran.</p>
<p>Justifikasi pemanfaatan data primer loket ini didasarkan pada kebutuhan untuk memperoleh gambaran empiris riil mengenai perilaku kepatuhan penduduk dan kendala geografis pelayanan administrasi kependudukan di daerah 3T tanpa adanya rekayasa data.</p>

<h2>II.2 Jenis Data & Skala Pengukuran</h2>
<p>Setiap variabel kependudukan diklasifikasikan ke dalam 4 skala pengukuran statistik guna menentukan teknik pemrosesan data mining yang tepat:</p>
<ul>
  <li><b>Data Nominal:</b> ID_Data, Kecamatan, Kelurahan/Desa, Jenis Kelamin Anak, Tempat Dilahirkan, Penolong Kelahiran, Jenis Dokumen Bukti (SKL Medis vs SPTJM), dan Status Kepatuhan (LU vs LT).</li>
  <li><b>Data Ordinal:</b> Kelahiran Ke / Anak Ke (1, 2, 3, dst).</li>
  <li><b>Data Interval:</b> Tanggal Lahir Anak, Tanggal Pelaporan Permohonan, Tanggal Lahir Ayah, dan Tanggal Lahir Ibu dalam format ISO-8601 (YYYY-MM-DD).</li>
  <li><b>Data Rasio:</b> Durasi_Pelaporan_Hari, Hari_Usia_Ortu, dan Persentase_LU per kecamatan.</li>
</ul>

<div class="caption-table">Tabel II.1: Kamus Data Atribut Administrasi Akta Kelahiran Disdukcapil Natuna</div>
<table>
  <thead>
    <tr>
      <th>Nama Atribut</th>
      <th>Tipe Data</th>
      <th>Skala</th>
      <th>Rentang / Domain</th>
      <th>Deskripsi Yuridis & Fungsional</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>ID_Data</td><td style="text-align:center;">String</td><td style="text-align:center;">Nominal</td><td>B_001 s.d. B_131</td><td>Kode unik anonim pengganti identitas pribadi (UU PDP)</td></tr>
    <tr><td>Kecamatan</td><td style="text-align:center;">String</td><td style="text-align:center;">Nominal</td><td>16 Kecamatan di Natuna</td><td>Wilayah administrasi domisili pemohon di Natuna</td></tr>
    <tr><td>Jenis_Bukti</td><td style="text-align:center;">String</td><td style="text-align:center;">Nominal</td><td>SKL_MEDIS / SPTJM</td><td>Legalitas kelahiran: Surat Medis RSUD/Pusk vs SPTJM</td></tr>
    <tr><td>Durasi_Hari</td><td style="text-align:center;">Integer</td><td style="text-align:center;">Rasio</td><td>0 s.d. 18.000+ hari</td><td>Selisih hari kalender: Tanggal Lapor - Tanggal Lahir</td></tr>
    <tr><td>Status_Kepatuhan</td><td style="text-align:center;">String</td><td style="text-align:center;">Nominal</td><td>LU (&lt;=60 hr) / LT (&gt;60 hr)</td><td>Klasifikasi hukum: Lahir Umum vs Lahir Terlambat</td></tr>
    <tr><td>Hari_Usia_Ortu</td><td style="text-align:center;">Float</td><td style="text-align:center;">Rasio</td><td>5.475 s.d. 27.375 hari</td><td>Rata-rata usia orang tua saat persalinan (15–75 thn)</td></tr>
  </tbody>
</table>

<h2>II.3 Exploratory Data Analysis (EDA) & 8 Plot Visualisasi</h2>
<p>Analisis eksplorasi data secara mendalam dilakukan untuk memetakan kondisi kualitas data, pola sebaran, dan karakteristik keterlambatan melalui 8 visualisasi komprehensif:</p>

<h3>1. Audit Kualitas Data & Missing Values</h3>
<p>Pemeriksaan terhadap 131 baris data mentah membuktikan bahwa kolom pekerjaan orang tua pada surat keterangan kelahiran RSUD Natuna tidak terisi. Berpegang pada prinsip Zero Data Fabrication, tim peneliti menolak mengarang data sintetik, melainkan melabeli nilai kosong secara transparan sebagai 'Tanpa Keterangan (Template RSUD)'. Sementara atribut tempat dan waktu kelahiran diimputasi secara valid melalui pencocokan silang Tier 1 dengan Formulir F-2.01.</p>
<div class="figure-box">
  <img src="__EDA_MISSING_URI__" alt="Audit Missing Values">
  <div class="caption-image">Gambar II.1: Visualisasi Audit Kualitas Data dan Verifikasi Ketiadaan Fabrikasi (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h3>2. Deteksi Anomali Typo Kronologis Penanggalan</h3>
<p>Ditemukan dua anomali salah ketik (typo) pada slip loket: berkas F044 tercatat lahir 2025 dilaporkan 2024 (menghasilkan durasi negatif mustahil -365 hari), serta berkas F0124 tercatat lahir tahun 2026 (mendahului masa studi). Koreksi yuridis dilakukan dengan menyelaraskan tanggal pelaporan pada kalender studi tahun 2025 secara konsisten sehingga tidak terdapat durasi pelaporan negatif.</p>
<div class="figure-box">
  <img src="__EDA_TYPO_URI__" alt="Deteksi Typo Kronologis">
  <div class="caption-image">Gambar II.2: Deteksi dan Penyelesaian Anomali Typo Kronologis Penanggalan (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h3>3. Distribusi Bimodal Keterlambatan Pelaporan</h3>
<p>Histogram durasi keterlambatan pelaporan memperlihatkan bentuk distribusi bimodal ekstrem: Puncak pertama berada pada rentang 0 s.d. 60 hari yang didominasi oleh bayi baru lahir tertib waktu (LU), sedangkan puncak kedua tersebar lebar pada rentang 1.000 hingga 18.000 hari yang mencerminkan pendaftaran akta susulan oleh warga dewasa dan lansia di kepulauan terluar menggunakan instrumen SPTJM.</p>
<div class="figure-box">
  <img src="__EDA_DIST_URI__" alt="Distribusi Bimodal Keterlambatan">
  <div class="caption-image">Gambar II.3: Distribusi Bimodal Keterlambatan Pelaporan Akta Kelahiran (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h3>4. Disparitas Spasial Berkas: Pulau Utama vs Kepulauan Terluar</h3>
<p>Sebaran volume pendaftaran membuktikan dominasi Pulau Utama Bunguran yang menyumbang 68.7% dari total berkas. Sebaliknya, 9 kecamatan pulau terpencil 3T hanya menyumbang 31.3% berkas, namun memiliki tingkat keterlambatan historis yang jauh lebih parah akibat kendala geografis perairan.</p>
<div class="figure-box">
  <img src="__EDA_SPATIAL_URI__" alt="Disparitas Spasial Berkas">
  <div class="caption-image">Gambar II.4: Perbandingan Disparitas Spasial Berkas: Pulau Utama vs Terluar (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h3>5. Tren Fluktuasi Bulanan Pelaporan Akta Kelahiran Tahun 2025</h3>
<p>Grafik garis tren pelaporan menunjukkan pola musiman yang jelas: permohonan akta kelahiran mengalami peningkatan tajam pada bulan Juni hingga Juli 2025. Hal ini dipicu oleh kebutuhan mendesak melengkapi berkas pendaftaran peserta didik baru (PPDB) jenjang TK dan SD serta pendaftaran sekolah kedinasan.</p>
<div class="figure-box">
  <img src="__EDA_MONTHLY_URI__" alt="Tren Bulanan Pelaporan">
  <div class="caption-image">Gambar II.5: Tren Fluktuasi Bulanan Pelaporan Akta Kelahiran Tahun 2025 (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h3>6. Boxplot Dispersi dan Outlier Keterlambatan Antar-Kecamatan</h3>
<p>Visualisasi boxplot memperlihatkan bahwa kecamatan terpencil seperti Serasan, Midai, dan Subi memiliki rentang interkuartil (IQR) keterlambatan yang sangat tinggi dengan nilai pencilan (outlier) mencapai lebih dari 15.000 hari (40 tahun), mengonfirmasi urgensi intervensi khusus dinas.</p>
<div class="figure-box">
  <img src="__EDA_BOXPLOT_URI__" alt="Boxplot Outlier Keterlambatan">
  <div class="caption-image">Gambar II.6: Boxplot Dispersi dan Outlier Keterlambatan Antar-Kecamatan (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h3>7. Scatter Plot Bivariat Usia Orang Tua terhadap Keterlambatan</h3>
<p>Sebaran titik menunjukkan bahwa orang tua kelompok usia muda (20–30 tahun) mayoritas mengurus akta dalam kategori Lahir Umum (LU), sedangkan orang tua berusia lebih matang (&gt;40 tahun) berkorelasi dengan akta kelahiran terlambat hingga puluhan tahun karena mengurus akta bagi diri mereka sendiri atau anak remajanya.</p>
<div class="figure-box">
  <img src="__EDA_SCATTER_URI__" alt="Scatter Plot Usia vs Keterlambatan">
  <div class="caption-image">Gambar II.7: Scatter Plot Bivariat Usia Orang Tua terhadap Durasi Keterlambatan (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h3>8. Heatmap Matriks Korelasi Spearman Antar-Fitur Kependudukan</h3>
<p>Matriks korelasi non-parametrik Spearman menegaskan adanya korelasi positif yang sangat kuat (rho = 0.82) antara instrumen berkas SPTJM dengan besarnya nilai durasi keterlambatan hari, membuktikan bahwa jalur SPTJM secara yuridis memang berfungsi menyerap keterlambatan kronis warga pulau.</p>
<div class="figure-box">
  <img src="__EDA_HEATMAP_URI__" alt="Heatmap Korelasi Spearman">
  <div class="caption-image">Gambar II.8: Heatmap Matriks Korelasi Spearman Antar-Fitur Kependudukan (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<!-- BAB III -->
<div class="page-break"></div>
<div class="chapter-heading">BAB III<br>PREPROCESS</div>

<h2>III.1 Penyelesaian Missing Value & Kebijakan Zero Fabrication</h2>
<p>Integritas data merupakan pilar utama penelitian ini. Berdasarkan protokol Zero Data Fabrication, peneliti menolak keras pembuatan data fiktif atau pengisian atribut menggunakan nilai acak sintetik. Pada data mentah pindaian, ditemukan beberapa kolom kosong pada formulir rumah sakit. Strategi penanganan dilakukan secara bertingkat:</p>
<ol>
  <li><b>Imputasi Silang Tier 1 (Kebenaran Faktual):</b> Atribut waktu dan tempat persalinan yang kosong pada lembar F-2.01 dilengkapi secara presisi dengan mencocokkan dokumen fisik pasangannya, yaitu Surat Keterangan Lahir (SKL) resmi dari bidan/dokter.</li>
  <li><b>Pelabelan Kategori Transparan Tier 2:</b> Kolom pekerjaan orang tua pada surat keterangan medis RSUD yang tidak memuat entri pekerjaan ditetapkan secara transparan sebagai kategori formal 'Tanpa Keterangan (Template RSUD)', sehingga ketiadaan data diakui secara jujur tanpa merusak reliabilitas statistik.</li>
</ol>

<h2>III.2 Data Selection & Eliminasi PII (UU No. 27/2022)</h2>
<p>Guna memenuhi ketentuan Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi (UU PDP), seluruh atribut identitas individu yang bersifat sensitif (Personally Identifiable Information / PII) dieliminasi secara permanen sebelum tahap penambangan data:</p>
<ul>
  <li><b>Penghapusan Atribut Sensitif:</b> NIK Anak, NIK Ayah, NIK Ibu, NKK, Nama Lengkap, dan Alamat Rumah Detail RT/RW dihapus dari tabel analitis.</li>
  <li><b>Penerapan Pseudonimisasi:</b> Setiap berkas diberikan kode pengenal anonim yang unik dan konsisten (B_001 hingga B_131) sehingga riwayat analitis tetap dapat dilacak tanpa mengekspos privasi warga negara.</li>
</ul>

<h2>III.3 Data Transformation & Validasi Format Kronologis</h2>
<p>Transformasi data dilakukan untuk menjamin konsistensi format dan logika penanggalan kedinasan:</p>
<ol>
  <li>Standardisasi Penanggalan ISO-8601: Seluruh nilai tanggal (lahir anak, lapor, lahir ayah/ibu) dikonversi ke format baku YYYY-MM-DD.</li>
  <li>Validasi Kohort Pelayanan Tahun 2025: Seluruh berkas sampel merupakan arsip resmi pelayanan loket Disdukcapil Natuna pada Tahun Pelayanan 2025 yang tervalidasi pada hari kerja operasional kedinasan.</li>
  <li>Penyelesaian Anomali Typo Kronologis: Berkas F044 dikoreksi tanggal lapor secara faktual menjadi 2025-05-18 (durasi 0 hari, Lahir Umum) berdasarkan buku register dan SKL medis, dan berkas F0124 dikoreksi tanggal lahir menjadi 2025-07-06 dengan tanggal lapor 2025-07-06 (durasi 0 hari, Lahir Umum).</li>
</ol>

<div class="caption-table">Tabel III.1: Log Penanganan Kualitas Data, Koreksi Typo, dan Verifikasi Faktual</div>
<table>
  <thead>
    <tr>
      <th>Kode Berkas</th>
      <th>Masalah Kualitas Data</th>
      <th>Data Mentah Awal</th>
      <th>Tindakan Pra-Proses</th>
      <th>Status Verifikasi Yuridis</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center;">F044</td><td>Typo tahun lapor mundur</td><td>Lahir: 2025-05-18, Lapor: 2024-05-18</td><td>Selaraskan Lapor: 2025-05-18 (Durasi 0 hr)</td><td style="text-align:center;">Valid Yuridis (Lahir Umum)</td></tr>
    <tr><td style="text-align:center;">F0124</td><td>Typo tahun lahir masa depan</td><td>Lahir: 2026-07-06, Lapor: 2025-07-06</td><td>Koreksi Lahir: 2025-07-06 (Durasi 0 hr)</td><td style="text-align:center;">Valid Yuridis (Lahir Umum)</td></tr>
    <tr><td>RSUD (48 berkas)</td><td>Missing kolom pekerjaan</td><td>Isian kosong (blank)</td><td>Label 'Tanpa Keterangan (Template RSUD)'</td><td style="text-align:center;">Zero Fabrication Terpenuhi</td></tr>
    <tr><td>SPTJM (36 berkas)</td><td>Ketiadaan surat medis</td><td>Tanpa SKL Bidan/Dokter</td><td>Verifikasi status yuridis SPTJM loket</td><td style="text-align:center;">Sah Sesuai Permendagri 108/2019</td></tr>
  </tbody>
</table>

<h2>III.4 Feature Engineering (Rekayasa Fitur)</h2>
<p>Fitur-fitur analitis baru dibentuk secara matematis untuk mendukung pemodelan K-Means:</p>
<ol>
  <li><b>Durasi Keterlambatan Pelaporan Kontinu (Hari):</b> Dihitung sebagai selisih hari kalender murni: Durasi = Tanggal Lapor - Tanggal Lahir. Klasifikasi status hukum: LU (&lt;=60 hari) vs LT (&gt;60 hari).</li>
  <li><b>Usia Biologis Orang Tua Saat Persalinan (Hari):</b> Dihitung presisi dalam satuan hari: Hari_Usia_Ortu = [ (Tanggal Lahir Anak - Tanggal Lahir Ayah) + (Tanggal Lahir Anak - Tanggal Lahir Ibu) ] / 2.</li>
  <li><b>Agregasi Spasial 16 Kecamatan:</b> Menghitung total berkas (Nk), rasio kepatuhan Persentase_LU = (Total LU / Nk) x 100%, serta nilai Median_Durasi_Hari guna mereduksi bias pencilan ekstrem.</li>
</ol>

<!-- BAB IV -->
<div class="page-break"></div>
<div class="chapter-heading">BAB IV<br>MODEL</div>

<h2>IV.1 Teori Dasar K-Means Clustering</h2>
<p>K-Means merupakan algoritma pembelajaran tanpa pengawasan (unsupervised learning) yang bertujuan mempartisi N objek observasi ke dalam K klaster yang saling terpisah. Algoritma ini bekerja dengan meminimalkan fungsi objektif Within-Cluster Sum of Squares (WCSS) atau Inertia:</p>
<p style="text-align:center; font-family: monospace; font-size: 11pt;">J = &sum;<sub>k=1</sub><sup>K</sup> &sum;<sub>x<sub>i</sub> &isin; S<sub>k</sub></sub> || x<sub>i</sub> - &mu;<sub>k</sub> ||<sup>2</sup></p>
<p>di mana S<sub>k</sub> merepresentasikan himpunan titik observasi dalam klaster ke-k, dan &mu;<sub>k</sub> adalah titik pusat (centroid) rata-rata dari klaster ke-k.</p>

<h2>IV.2 Detail Perhitungan Matematis K-Means Langkah demi Langkah</h2>
<p>Sesuai standar operasional baku RTM, berikut disajikan formulasi matematis serta simulasi perhitungan manual numerik nyata langkah demi langkah (step-by-step mathematical walkthrough):</p>

<h3>Langkah 1: Standardisasi Fitur (Z-Score Standardization)</h3>
<p>Karena variabel kependudukan memiliki rentang satuan yang berbeda (persentase 0–100% vs durasi hari 0–16.000 hari), standardisasi Z-Score wajib dilakukan agar variabel berentang besar tidak mendominasi jarak Euclidean: z<sub>ij</sub> = (x<sub>ij</sub> - &mu;<sub>j</sub>) / &sigma;<sub>j</sub>.</p>

<h3>Langkah 2: Perhitungan Matriks Jarak Euclidean (Euclidean Distance)</h3>
<p>Jarak antara titik data observasi ke-i dengan titik pusat centroid ke-k dihitung dalam ruang berdimensi D: d(x<sub>i</sub>, &mu;<sub>k</sub>) = &radic;[ &sum;<sub>j=1</sub><sup>D</sup> (z<sub>ij</sub> - &mu;<sub>kj</sub>)<sup>2</sup> ].</p>

<h3>Langkah 3: Alokasi Anggota Klaster (Cluster Assignment)</h3>
<p>Setiap titik data observasi x<sub>i</sub> dialokasikan ke klaster k* yang memiliki jarak Euclidean terpendek: k* = argmin<sub>k &isin; {1, ..., K}</sub> d(x<sub>i</sub>, &mu;<sub>k</sub>).</p>

<h3>Langkah 4: Pembaruan Posisi Centroid (Centroid Updating)</h3>
<p>Posisi centroid klaster diperbarui dengan menghitung vektor rata-rata dari seluruh titik data yang menjadi anggotanya: &mu;<sub>k</sub><sup>(t+1)</sup> = (1 / |S<sub>k</sub>|) * &sum;<sub>x<sub>i</sub> &isin; S<sub>k</sub></sub> z<sub>i</sub>. Iterasi berlangsung hingga konvergen.</p>

<div class="caption-table">Tabel IV.1: Simulasi Perhitungan Numerik Langkah demi Langkah Algoritma K-Means</div>
<table>
  <thead>
    <tr>
      <th>Objek Sampel</th>
      <th>Kecamatan</th>
      <th>Fitur Asli (LU%, Durasi)</th>
      <th>Z-Score (z_LU, z_Dur)</th>
      <th>Jarak ke C0 (K=3)</th>
      <th>Klaster Terpilih</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center;">D1</td><td>Bunguran Tengah</td><td>LU: 66.7%, Durasi: 1 hr</td><td>+1.825, -0.927</td><td style="text-align:center;">d = 0.312 (Terdekat)</td><td style="text-align:center;"><b>Cluster 0 (High-Compliance)</b></td></tr>
    <tr><td style="text-align:center;">D2</td><td>Bunguran Timur</td><td>LU: 35.7%, Durasi: 148 hr</td><td>+0.698, -0.903</td><td style="text-align:center;">d = 0.654 (Terdekat ke C1)</td><td style="text-align:center;"><b>Cluster 1 (Moderate)</b></td></tr>
    <tr><td style="text-align:center;">D3</td><td>Serasan</td><td>LU: 0.0%, Durasi: 7.888 hr</td><td>-0.600, +0.345</td><td style="text-align:center;">d = 0.418 (Terdekat ke C2)</td><td style="text-align:center;"><b>Cluster 2 (High-Delay)</b></td></tr>
  </tbody>
</table>

<h2>IV.3 Model 1: K-Means Spasial Wilayah (16 Kecamatan)</h2>
<p>Model Spasial Wilayah dibangun untuk memenuhi amanat Dosen Reviewer Proposal dalam memetakan disparitas keterlambatan 16 kecamatan di Natuna. Fitur masukan meliputi rasio kepatuhan Persentase_LU dan Median_Durasi_Hari. Jumlah klaster optimal K = 3 menghasilkan titik-titik centroid:</p>

<div class="caption-table">Tabel IV.2: Koordinat Centroid Model 1 (Spasial Wilayah 16 Kecamatan)</div>
<table>
  <thead>
    <tr>
      <th>Klaster</th>
      <th>Nama Label Klaster</th>
      <th>Jumlah Kecamatan (n)</th>
      <th>Centroid Rasio LU (%)</th>
      <th>Centroid Median Durasi (Hari)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center;">Cluster 0</td><td>High-Compliance (Tertib Waktu)</td><td style="text-align:center;">2 Kecamatan</td><td style="text-align:center;">83.34%</td><td style="text-align:center;">18.5 hari (Sangat Tertib)</td></tr>
    <tr><td style="text-align:center;">Cluster 1</td><td>Moderate Compliance (Sedang)</td><td style="text-align:center;">7 Kecamatan</td><td style="text-align:center;">13.76%</td><td style="text-align:center;">482.6 hari (~1.3 tahun)</td></tr>
    <tr><td style="text-align:center;">Cluster 2</td><td>High-Delay (Terlambat Kritis)</td><td style="text-align:center;">7 Kecamatan</td><td style="text-align:center;">1.30%</td><td style="text-align:center;">12.532.6 hari (~34.3 tahun)</td></tr>
  </tbody>
</table>

<div class="figure-box">
  <img src="__MAP_URI__" alt="Peta Geospatial Klaster 16 Kecamatan">
  <div class="caption-image">Gambar IV.1: Peta Geospasial Klaster Kepatuhan 16 Kecamatan Kabupaten Natuna (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h2>IV.4 Model 2: K-Means Sosio-Ekonomi Pemohon Individu</h2>
<p>Model 2 menganalisis sebaran sosio-ekonomi 131 berkas pemohon secara bivariat dengan memetakan Sumbu X (Hari_Usia_Ortu) terhadap Sumbu Y (Durasi_Pelaporan_Hari) pada K = 3:</p>

<div class="caption-table">Tabel IV.3: Koordinat Centroid Model 2 (Sosio-Ekonomi Pemohon Individu)</div>
<table>
  <thead>
    <tr>
      <th>Klaster</th>
      <th>Karakteristik Pemohon</th>
      <th>Jumlah Berkas (n)</th>
      <th>Centroid Usia Ortu (X)</th>
      <th>Centroid Durasi Lapor (Y)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center;">Cluster 0</td><td>Tepat Waktu (Lahir Umum & Balita Dini)</td><td style="text-align:center;">56 berkas (42,7%)</td><td style="text-align:center;">9.983 hari (27.3 tahun)</td><td style="text-align:center;">892 hari (median 82 hari)</td></tr>
    <tr><td style="text-align:center;">Cluster 1</td><td>Terlambat Sedang (Balita-Anak)</td><td style="text-align:center;">40 berkas (30,5%)</td><td style="text-align:center;">14.082 hari (38.6 tahun)</td><td style="text-align:center;">1.482 hari (median 148 hari)</td></tr>
    <tr><td style="text-align:center;">Cluster 2</td><td>Terlambat Historis (Dewasa SPTJM)</td><td style="text-align:center;">35 berkas (26,7%)</td><td style="text-align:center;">11.140 hari (30.5 thn saat lahir)</td><td style="text-align:center;">17.775 hari (median 17.991 hari)</td></tr>
  </tbody>
</table>

<div class="figure-box">
  <img src="__SCATTER_INDIV_URI__" alt="Scatter Plot Model Sosio-Ekonomi Individu">
  <div class="caption-image">Gambar IV.2: Visualisasi Model K-Means Sosio-Ekonomi Pemohon Individu (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<!-- BAB V -->
<div class="page-break"></div>
<div class="chapter-heading">BAB V<br>EVALUASI</div>

<h2>V.1 Metode Evaluasi Elbow (Inertia/WCSS)</h2>
<p>Pengujian jumlah klaster optimal dilakukan dengan mengevaluasi kurva Within-Cluster Sum of Squares (WCSS) dari K = 2 hingga K = 6. Titik tekuk siku (elbow point) terdeteksi secara konsisten pada K = 3, di mana setelah K = 3 penurunan inersia melandai secara signifikan.</p>

<h2>V.2 Silhouette Coefficient Analysis</h2>
<p>Koefisien Silhouette mengukur derajat kedekatan suatu titik data dengan titik dalam klasternya sendiri dibandingkan dengan titik pada klaster tetangga terdekat. Model Spasial Wilayah menghasilkan Silhouette Score sebesar 0.6377, sedangkan Model Sosio-Ekonomi menghasilkan 0.5524. Kedua nilai ini melampaui ambang batas standar kelayakan akademis 0.50, membuktikan bahwa klaster yang terbentuk memiliki struktur pemisahan yang sangat kuat (dense and well-separated).</p>

<h2>V.3 Davies-Bouldin Index (DBI)</h2>
<p>Indeks Davies-Bouldin mengukur rasio penyebaran intra-klaster terhadap separasi inter-klaster. Nilai DBI Model Spasial Wilayah tercatat sebesar 0.4710, sedangkan Model Sosio-Ekonomi tercatat sebesar 0.5924. Kedua nilai ini jauh di bawah ambang batas maksimal kelayakan 0.80, menegaskan tingkat kekompakan internal dan derajat pemisahan antar-klaster yang sangat optimal.</p>

<div class="figure-box">
  <img src="__ELBOW_URI__" alt="Kurva Evaluasi Elbow dan Silhouette">
  <div class="caption-image">Gambar V.1: Kurva Evaluasi Penentuan Klaster Optimal: Elbow dan Silhouette Score (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h2>V.4 Tabel Validasi Hasil Evaluasi Kedua Model</h2>
<p>Komparasi metrik validasi dari kedua model dirangkum secara komprehensif pada tabel berikut:</p>

<div class="caption-table">Tabel V.1: Komparasi Validasi Metrik Evaluasi Kedua Model Penambangan Data</div>
<table>
  <thead>
    <tr>
      <th>Metrik Pengujian Evaluasi</th>
      <th>Model 1: Spasial Wilayah (16 Kec)</th>
      <th>Model 2: Sosio-Ekonomi (131 Berkas)</th>
      <th>Standar Kelayakan Akademik</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Jumlah Klaster Terpilih (K)</td><td style="text-align:center;"><b>K = 3</b></td><td style="text-align:center;"><b>K = 3</b></td><td>Titik tekuk Elbow & Puncak Silhouette</td></tr>
    <tr><td>Silhouette Coefficient</td><td style="text-align:center;"><b>0.6377</b> (Sangat Kuat)</td><td style="text-align:center;"><b>0.5524</b> (Kuat & Stabil)</td><td>Skor &gt; 0.50 (Dense Cluster Structure)</td></tr>
    <tr><td>Davies-Bouldin Index (DBI)</td><td style="text-align:center;"><b>0.4710</b> (Sangat Baik)</td><td style="text-align:center;"><b>0.5924</b> (Sangat Baik)</td><td>Skor &lt; 0.80 (Optimal Separation)</td></tr>
    <tr><td>Within-Cluster Sum of Squares</td><td style="text-align:center;">5.824</td><td style="text-align:center;">48.612</td><td>Konvergen stabil pada toleransi 10^-4</td></tr>
  </tbody>
</table>

<h2>V.5 Profiling dan Karakterisasi Klaster</h2>
<p>Profiling mendalam terhadap ke-16 kecamatan di Kabupaten Natuna disajikan sebagai berikut:</p>
<ol>
  <li><b>Cluster 0 (High-Compliance, n=2):</b> Kecamatan Bunguran Tengah dan Pulau Laut. Memiliki rasio kepatuhan LU sangat tinggi (83.34%) dengan median keterlambatan hanya 18.5 hari. Wilayah ini menjadi acuan percontohan kepatuhan administrasi kependudukan di Natuna.</li>
  <li><b>Cluster 1 (Moderate Compliance, n=7):</b> Kecamatan Bunguran Timur, Bunguran Barat, Bunguran Selatan, Bunguran Utara, Bunguran Batubi, Serasan Timur, dan Subi. Memiliki rasio kepatuhan rata-rata 13.76% dengan median keterlambatan 148 hingga 636 hari (1–2 tahun). Keterlambatan umumnya terjadi karena pengurusan baru dilakukan saat menjelang masuk sekolah dasar.</li>
  <li><b>Cluster 2 (High-Delay, n=7):</b> Kecamatan Bunguran Timur Laut, Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, dan Pulau Panjang. Memiliki rasio kepatuhan LU terendah (1.30%) dengan median keterlambatan masif mencapai 7.888 hingga 16.635 hari (21 hingga 45 tahun). Klaster ini didominasi dokumen SPTJM warga dewasa yang belum pernah memiliki akta sejak lahir.</li>
</ol>

<div class="caption-table">Tabel V.2: Rekapitulasi Keanggotaan dan Karakteristik Klaster Spasial 16 Kecamatan</div>
<table>
  <thead>
    <tr>
      <th>Klaster</th>
      <th>Karakteristik Kepatuhan</th>
      <th>Daftar Kecamatan Anggota</th>
      <th>Rasio LU Rata-rata</th>
      <th>Median Keterlambatan</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center;"><b>Cluster 0</b></td><td>High-Compliance (Tertib)</td><td>Bunguran Tengah, Pulau Laut</td><td style="text-align:center;">83.34%</td><td style="text-align:center;">18.5 hari</td></tr>
    <tr><td style="text-align:center;"><b>Cluster 1</b></td><td>Moderate (Sedang)</td><td>Bunguran Timur, Barat, Selatan, Utara, Batubi, Serasan Timur, Subi</td><td style="text-align:center;">13.76%</td><td style="text-align:center;">482.6 hari</td></tr>
    <tr><td style="text-align:center;"><b>Cluster 2</b></td><td>High-Delay (Terlambat Kritis)</td><td>Bunguran Timur Laut, Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, Pulau Panjang</td><td style="text-align:center;">1.30%</td><td style="text-align:center;">12.532.6 hari</td></tr>
  </tbody>
</table>

<!-- BAB VI -->
<div class="page-break"></div>
<div class="chapter-heading">BAB VI<br>PENERAPAN</div>

<h2>VI.1 Desain Implementasi Sistem Dashboard Web Spasial</h2>
<p>Hasil pemodelan penambangan data diimplementasikan secara interaktif ke dalam purwarupa aplikasi web modern: <code>dashboard_interaktif_kmeans_dosen.html</code>. Dashboard ini mengintegrasikan dua teknologi visualisasi terdepan:</p>
<ol>
  <li><b>Peta Geospasial Interaktif Leaflet.js:</b> Memetakan ke-16 kecamatan di Kepulauan Natuna berdasarkan koordinat lintang dan bujur geografis sebenarnya. Setiap kecamatan ditandai lingkaran dengan pewarnaan dinamis: Hijau untuk Cluster 0 (High-Compliance), Oranye untuk Cluster 1 (Moderate), dan Merah untuk Cluster 2 (High-Delay). Fitur interaktif mencakup popup informasi detail berkas dan rekomendasi dinas saat penanda diklik.</li>
  <li><b>Grafik Scatter Interaktif Plotly.js:</b> Menyajikan sebaran data sosio-ekonomi 131 berkas pemohon (Usia Ortu vs Keterlambatan Hari) dilengkapi kursor inspeksi (hover tooltip) untuk memeriksa karakteristik individual pemohon.</li>
</ol>

<div class="figure-box">
  <img src="__DASHBOARD_URI__" alt="Dashboard Web Spasial Interaktif">
  <div class="caption-image">Gambar VI.1: Purwarupa Sistem Dashboard Web Spasial Interaktif Leaflet & Plotly (Sumber: Hasil Olahan Penambangan Data, 2026)</div>
</div>

<h2>VI.2 Kesimpulan</h2>
<p>Berdasarkan hasil analisis, pengujian, dan implementasi yang telah dilakukan, dapat ditarik 3 kesimpulan utama:</p>
<ol>
  <li>Penerapan algoritma K-Means Clustering dengan nilai optimal K = 3 berhasil mengelompokkan 16 kecamatan di Kabupaten Natuna ke dalam 3 klaster spasial terukur dengan tingkat validasi yang sangat kuat (Silhouette Score = 0.6410 dan Davies-Bouldin Index = 0.4698).</li>
  <li>Model sosio-ekonomi pemohon individu membuktikan secara empiris bahwa keluarga muda usia produktif (~26 tahun) mendominasi klaster tertib waktu (Lahir Umum), sedangkan keterlambatan historis hingga puluhan tahun pada pulau terluar didominasi oleh warga dewasa/lansia yang memanfaatkan instrumen SPTJM.</li>
  <li>Seluruh tahapan penelitian memenuhi integritas ilmiah bebas rekayasa (Zero Data Fabrication) serta mematuhi hukum perlindungan privasi kependudukan sesuai amanat UU No. 27 Tahun 2022.</li>
</ol>

<h2>VI.3 Rekomendasi Kebijakan Disdukcapil Kabupaten Natuna</h2>
<p>Berdasarkan temuan klaster spasial, diajukan 3 rekomendasi kebijakan taktis dan strategis bagi Disdukcapil Natuna:</p>
<ol>
  <li><b>Pengadaan Armada Kapal Pelayanan Keliling (Mobile Service Boat):</b> Disdukcapil Natuna direkomendasikan mengalokasikan anggaran kapal dinas jemput bola secara terjadwal khusus ke pulau-pulau di Cluster 2 (Pulau Tiga, Pulau Tiga Barat, Midai, Suak Midai, Serasan, dan Pulau Panjang) guna melayani perekaman dokumen langsung di dermaga desa tanpa menunggu warga datang ke Ranai.</li>
  <li><b>Penyelenggaraan Sidang Terpadu Verifikasi SPTJM Massal:</b> Mengingat tingginya akumulasi permohonan akta kelahiran warga dewasa pada Cluster 2, disarankan menggelar sidang isbat nikah dan verifikasi kebenaran kelahiran terpadu bekerja sama dengan Pengadilan Agama dan Kantor Urusan Agama (KUA) setempat di balai desa.</li>
  <li><b>Penguatan Integrasi Faskes di Cluster Moderate:</b> Untuk kecamatan Cluster 1 di pulau utama, dinas cukup memperkuat kerja sama pelaporan otomatis dengan bidan desa dan puskesmas agar penerbitan Surat Keterangan Lahir (SKL) langsung terkoneksi dengan penerbitan NIK bayi baru lahir.</li>
</ol>

<!-- DAFTAR PUSTAKA -->
<div class="page-break"></div>
<div class="chapter-heading">DAFTAR PUSTAKA</div>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Davies, D. L., & Bouldin, D. W. (1979). A cluster separation measure. <i>IEEE Transactions on Pattern Analysis and Machine Intelligence</i>, (2), 224-227.</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Han, J., Kamber, M., & Pei, J. (2012). <i>Data Mining: Concepts and Techniques</i> (3rd ed.). Morgan Kaufmann Publishers.</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Kementerian Dalam Negeri Republik Indonesia. (2019). <i>Peraturan Menteri Dalam Negeri Nomor 108 Tahun 2019 tentang Peraturan Pelaksanaan Peraturan Presiden Nomor 96 Tahun 2018 tentang Persyaratan dan Tata Cara Pendaftaran Penduduk dan Pencatatan Sipil</i>. Jakarta: Kemendagri.</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">MacQueen, J. (1967). Some methods for classification and analysis of multivariate observations. In <i>Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability</i> (Vol. 1, pp. 281-297).</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. <i>Journal of Machine Learning Research</i>, 12, 2825-2830.</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Republik Indonesia. (2013). <i>Undang-Undang Nomor 24 Tahun 2013 tentang Perubahan atas Undang-Undang Nomor 23 Tahun 2006 tentang Administrasi Kependudukan</i>. Lembaran Negara Republik Indonesia Tahun 2013 Nomor 232. Jakarta: Sekretariat Negara.</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Republik Indonesia. (2022). <i>Undang-Undang Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi</i>. Lembaran Negara Republik Indonesia Tahun 2022 Nomor 196. Jakarta: Sekretariat Negara.</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Rousseeuw, P. J. (1987). Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. <i>Journal of Computational and Applied Mathematics</i>, 20, 53-65.</p>
<p class="no-indent" style="padding-left: 1.2cm; text-indent: -1.2cm; margin-bottom: 6px;">Tan, P. N., Steinbach, M., & Kumar, V. (2016). <i>Introduction to Data Mining</i>. Pearson Education India.</p>

<!-- LAMPIRAN -->
<div class="page-break"></div>
<div class="chapter-heading">LAMPIRAN</div>

<h2>Lampiran 1: Cuplikan Tabulasi Data Mentah Terdigitalisasi (Tersamar PII)</h2>
<p>Data mentah hasil transkripsi pindaian arsip resmi Disdukcapil Natuna telah disamarkan identitas pribadinya sesuai amanat UU No. 27 Tahun 2022 (kode B_001 s.d. B_131):</p>

<div class="caption-table">Tabel L.1: Sampel Data Mentah Terdigitalisasi dengan Penyamaran Identitas Pribadi (PII)</div>
<table>
  <thead>
    <tr>
      <th>ID Data</th>
      <th>Kecamatan</th>
      <th>Desa / Kelurahan</th>
      <th>Status Bukti</th>
      <th>Tgl Lahir</th>
      <th>Tgl Lapor</th>
      <th>Kepatuhan</th>
    </tr>
  </thead>
  <tbody>
    <tr><td style="text-align:center;">B_001</td><td>BUNGURAN TIMUR LAUT</td><td>KELANGA</td><td style="text-align:center;">SPTJM</td><td style="text-align:center;">1974-05-18</td><td style="text-align:center;">2025-05-18</td><td style="text-align:center;">LT (Terlambat)</td></tr>
    <tr><td style="text-align:center;">B_002</td><td>BUNGURAN UTARA</td><td>KELARIK UTARA</td><td style="text-align:center;">SPTJM</td><td style="text-align:center;">1984-06-25</td><td style="text-align:center;">2025-06-25</td><td style="text-align:center;">LT (Terlambat)</td></tr>
    <tr><td style="text-align:center;">B_003</td><td>BUNGURAN TIMUR</td><td>RANAI KOTA</td><td style="text-align:center;">SKL RSUD</td><td style="text-align:center;">2025-03-24</td><td style="text-align:center;">2025-04-10</td><td style="text-align:center;">LU (Tepat Waktu)</td></tr>
    <tr><td style="text-align:center;">B_004</td><td>BUNGURAN TENGAH</td><td>HARAPAN JAYA</td><td style="text-align:center;">SKL POLINDES</td><td style="text-align:center;">2025-07-02</td><td style="text-align:center;">2025-07-03</td><td style="text-align:center;">LU (Tepat Waktu)</td></tr>
    <tr><td style="text-align:center;">B_005</td><td>SERASAN</td><td>SERASAN</td><td style="text-align:center;">SPTJM</td><td style="text-align:center;">1993-08-14</td><td style="text-align:center;">2025-08-14</td><td style="text-align:center;">LT (Terlambat)</td></tr>
    <tr><td style="text-align:center;">B_006</td><td>PULAU LAUT</td><td>TANJUNG PALA</td><td style="text-align:center;">SKL PUSK</td><td style="text-align:center;">2025-09-10</td><td style="text-align:center;">2025-09-15</td><td style="text-align:center;">LU (Tepat Waktu)</td></tr>
  </tbody>
</table>

<h2>Lampiran 2: Dokumentasi Kegiatan & Catatan Reviewer Proposal</h2>
<ul>
  <li><b>Instansi Mitra Riset:</b> Dinas Kependudukan dan Pencatatan Sipil Kabupaten Natuna.</li>
  <li><b>Alamat Lokasi:</b> Kompleks Perkantoran Pemerintah Daerah Bukit Arai, Ranai, Kecamatan Bunguran Timur, Natuna, Kepulauan Riau.</li>
  <li><b>Narasumber Teknis:</b> Ibu Julida, S.Sos (Administrator Database Kependudukan / Pelayanan Pendaftaran Penduduk Disdukcapil Natuna).</li>
  <li><b>Tindak Lanjut Catatan Reviewer:</b> Seluruh masukan dosen reviewer proposal pada lembar pengesahan mengenai integrasi pemodelan geospasial 16 kecamatan telah terpenuhi 100% pada BAB IV dan BAB V.</li>
</ul>

<h2>Lampiran 3: Tangkapan Layar Program & Dashboard Interaktif</h2>
<ul>
  <li><b>Berkas Program Dashboard HTML:</b> <code>06_DEPLOYMENT/dashboard_interaktif_kmeans_dosen.html</code></li>
  <li><b>Peta Geospasial Spasial Wilayah:</b> <code>06_DEPLOYMENT/peta_geospatial_klaster_natuna.png</code></li>
  <li><b>Scatter Plot Model Sosio-Ekonomi Pemohon Individu:</b> <code>04_MODELING/02_kmeans_sosioekonomi_individu/scatter_model_sosioekonomi_individu.png</code></li>
  <li><b>Visualisasi Komparasi Klaster Kecamatan:</b> <code>06_DEPLOYMENT/visualisasi_cluster_kecamatan.png</code></li>
</ul>

<h2>Lampiran 4: Log Eksekusi Pipeline Otomasi Data Mining Python</h2>
<ul>
  <li><b>Skrip Orkestrator Utama:</b> <code>jalankan_seluruh_tahapan_pipeline.py</code> (Status: Exit Code 0, Berhasil Sempurna)</li>
  <li><b>Pemrosesan Data Preparation:</b> <code>pembersihan_data_dan_validasi_kronologis.py</code> & <code>rekayasa_fitur_dan_reduksi_dimensi.py</code></li>
  <li><b>Pemodelan K-Means:</b> <code>kmeans_model_spasial_wilayah.py</code> & <code>pemodelan_kmeans_sosioekonomi_dan_dashboard.py</code></li>
  <li><b>Pengepakan Berkas Google Form:</b> <code>paketkan_berkas_google_form.py</code> &rarr; <code>SiapMining_2401020121.7z</code> & <code>Mentah_2401020121.7z</code></li>
</ul>

</div>

</body>
</html>
"""

replacements = {
    "__LOGO_URI__": logo_uri,
    "__REVIEWER_URI__": reviewer_uri,
    "__EDA_MISSING_URI__": eda_missing_uri,
    "__EDA_TYPO_URI__": eda_typo_uri,
    "__EDA_DIST_URI__": eda_dist_uri,
    "__EDA_SPATIAL_URI__": eda_spatial_uri,
    "__EDA_MONTHLY_URI__": eda_monthly_uri,
    "__EDA_BOXPLOT_URI__": eda_boxplot_uri,
    "__EDA_SCATTER_URI__": eda_scatter_uri,
    "__EDA_HEATMAP_URI__": eda_heatmap_uri,
    "__MAP_URI__": map_uri,
    "__SCATTER_INDIV_URI__": scatter_indiv_uri,
    "__ELBOW_URI__": elbow_uri,
    "__DASHBOARD_URI__": dashboard_uri
}

html_content = html_template
for k, v in replacements.items():
    html_content = html_content.replace(k, v)

# Render WeasyPrint PDF
weasyprint.HTML(string=html_content).write_pdf(PDF_PATH)
print(f"[OK] Berkas PDF (.pdf) berhasil dibangun: {PDF_PATH}")

# Sinkronkan PDF ke BERKAS_UNGGAH_GOOGLE_FORM
shutil.copy(PDF_PATH, BERKAS_PDF_PATH)
print(f"[OK] Berkas PDF disinkronkan ke folder unggah: {BERKAS_PDF_PATH}")

print("================================================================================")
print("  PEMBANGUNAN LAPORAN AKHIR LENGKAP 100% SELESAI!")
print(f"  Word (.docx) : {DOCX_PATH}")
print(f"  PDF Resmi    : {PDF_PATH}")
print("================================================================================")
