# test_boolean.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from src.search import search_boolean

queries = [
    "ekonomi",
    "ekonomi AND teknologi",
    "hukum OR sosial",
    "NOT kesehatan"
]

print("\n" + "=" * 60)
print("TEST BOOLEAN INFORMATION RETRIEVAL")
print("=" * 60)

for q in queries:
    print(f"\nQUERY : {q}")
    print("-" * 60)

    results = search_boolean(q)

    if not results:
        print("❌ Tidak ada dokumen ditemukan.")
    else:
        print(f"✅ Ditemukan {len(results)} dokumen:\n")
        for i, doc in enumerate(results[:10], start=1):
            print(f"{i:02d}. {doc}")

        if len(results) > 10:
            print("... (hasil dipotong)")