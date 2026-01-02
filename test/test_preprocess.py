# test_preprocess.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from src.preprocess import preprocess_text

sample_text = """
Sistem Temu Kembali Informasi adalah bidang ilmu
yang mempelajari bagaimana menemukan dokumen
yang relevan dari kumpulan data teks.
"""

print("\n" + "=" * 60)
print("TEKS ASLI")
print("=" * 60)
print(sample_text.strip())

tokens = preprocess_text(sample_text)

print("\n" + "=" * 60)
print("HASIL PREPROCESSING")
print("=" * 60)

print(f"Total token: {len(tokens)}\n")
print("10 Token pertama:")
print("-" * 30)

for t in tokens[:10]:
    print(f"- {t}")