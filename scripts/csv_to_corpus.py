# scripts/csv_to_corpus.py

import os
import pandas as pd
import re

# =========================
# Konfigurasi
# =========================

CSV_PATH = "data/dataset/artikel_alwi.csv"
OUTPUT_DIR = "data/raw"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# Helper
# =========================

def clean_filename(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", "_", text)
    return text[:50]  # biar tidak kepanjangan

# =========================
# Load CSV
# =========================

df = pd.read_csv(CSV_PATH)

# pastikan kolom ada
required_cols = ["Bidang", "Judul", "Isi"]
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Kolom '{col}' tidak ditemukan!")

# =========================
# Konversi ke dokumen teks
# =========================

for i, row in df.iterrows():
    kategori = str(row["Bidang"])
    judul = str(row["Judul"])
    isi = str(row["Isi"])

    filename = f"{clean_filename(kategori)}_{clean_filename(judul)}_{i+1:03}.txt"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Judul: {judul}\n")
        f.write(f"Kategori: {kategori}\n\n")
        f.write("Isi:\n")
        f.write(isi)

print(f"[SELESAI] {len(df)} dokumen berhasil dibuat di '{OUTPUT_DIR}'")