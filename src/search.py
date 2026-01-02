# src/search.py

from src.boolean_ir import load_processed_docs, build_inverted_index, boolean_search
from src.vsm_ir import compute_tfidf, search_vsm

# ==================================================
# Load Data Sekali di Awal
# ==================================================

docs = load_processed_docs("data/processed")

index = build_inverted_index(docs)
all_docs = list(docs.keys())

tfidf_docs, idf = compute_tfidf(docs)


# ==================================================
# Interface Search
# ==================================================

def search_boolean(query: str):
    return sorted(boolean_search(query, index, all_docs))


def search_vector(query: str):
    return search_vsm(query, tfidf_docs, idf)