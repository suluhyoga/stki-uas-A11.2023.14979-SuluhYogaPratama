# test_vsm.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from src.search import search_vector

query = "ekonomi teknologi digital"

print("\n" + "=" * 60)
print("VECTOR SPACE MODEL (TF-IDF)")
print("=" * 60)
print(f"Query: {query}")
print("-" * 60)

results = search_vector(query)

if not results:
    print("❌ Tidak ada dokumen relevan.")
else:
    for rank, (doc, score) in enumerate(results, start=1):
        print(f"{rank:02d}. {doc}")
        print(f"     Skor Similarity: {score:.4f}")