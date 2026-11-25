#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Penerus otomatis: Menjalankan build_final_reports.py untuk menjamin naskah
Laporan Akhir (Word DOCX, Markdown MD, dan PDF FinPD) selalu selaras 100%
dengan format RTM terbaru.
"""
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
script = os.path.join(BASE_DIR, "build_final_reports.py")
res = subprocess.run([sys.executable, script])
sys.exit(res.returncode)
