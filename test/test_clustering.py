# test_clustering.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from src.clustering import clustering_kmeans

clusters = clustering_kmeans("data/processed", k=5)

print("\n" + "=" * 60)
print("HASIL CLUSTERING K-MEANS")
print("=" * 60)

for cluster_id in sorted(clusters.keys()):
    docs = clusters[cluster_id]
    print(f"\nCLUSTER {cluster_id} ({len(docs)} dokumen)")
    print("-" * 40)

    for doc in docs:
        print(f"- {doc}")