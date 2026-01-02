# test_summarization.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from src.summarization import summarize_document
import os

folder = "data/raw"
files = [f for f in os.listdir(folder) if f.endswith(".txt")]

file_path = os.path.join(folder, files[0])

with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

print("\n" + "=" * 60)
print("TEST SUMMARIZATION")
print("=" * 60)
print(f"Dokumen: {files[0]}")
print("-" * 60)

summary = summarize_document(raw_text)
print(summary)