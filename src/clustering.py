# src/clustering.py

import os
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# ==================================================
# Load Dokumen
# ==================================================

def load_documents(processed_folder: str) -> dict:
    docs = {}
    for filename in os.listdir(processed_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(processed_folder, filename), "r", encoding="utf-8") as f:
                docs[filename] = f.read()
    return docs


# ==================================================
# K-Means Clustering
# ==================================================

def clustering_kmeans(processed_folder: str, k=5) -> dict:
    docs = load_documents(processed_folder)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs.values())

    model = KMeans(n_clusters=k, random_state=42)
    labels = model.fit_predict(tfidf_matrix)

    clusters = {}
    for doc, label in zip(docs.keys(), labels):
        clusters.setdefault(label, []).append(doc)

    return clusters