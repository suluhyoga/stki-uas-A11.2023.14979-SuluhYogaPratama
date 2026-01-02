# src/vsm_ir.py

import math
from collections import Counter
from src.preprocess import preprocess_text

# ==================================================
# Term Frequency
# ==================================================

def compute_tf(tokens: list) -> dict:
    tf = Counter(tokens)
    total = len(tokens)
    return {t: f / total for t, f in tf.items()}


# ==================================================
# Inverse Document Frequency
# ==================================================

def compute_idf(docs: dict) -> dict:
    N = len(docs)
    df = Counter()

    for tokens in docs.values():
        for t in set(tokens):
            df[t] += 1

    return {t: math.log((N + 1) / (df[t] + 1)) + 1 for t in df}


# ==================================================
# TF-IDF
# ==================================================

def compute_tfidf(docs: dict):
    idf = compute_idf(docs)
    tfidf_docs = {}

    for doc, tokens in docs.items():
        tf = compute_tf(tokens)
        tfidf_docs[doc] = {t: tf[t] * idf.get(t, 0) for t in tf}

    return tfidf_docs, idf


# ==================================================
# Cosine Similarity
# ==================================================

def cosine_similarity(v1: dict, v2: dict) -> float:
    common = set(v1) & set(v2)
    numerator = sum(v1[t] * v2[t] for t in common)

    denom1 = math.sqrt(sum(v ** 2 for v in v1.values()))
    denom2 = math.sqrt(sum(v ** 2 for v in v2.values()))

    if denom1 == 0 or denom2 == 0:
        return 0.0
    return numerator / (denom1 * denom2)


# ==================================================
# Search VSM
# ==================================================

def search_vsm(query: str, tfidf_docs: dict, idf: dict, top_k=10):
    query_tokens = preprocess_text(query)
    tf_query = compute_tf(query_tokens)
    tfidf_query = {t: tf_query[t] * idf.get(t, 0) for t in tf_query}

    scores = {
        doc: cosine_similarity(tfidf_query, vec)
        for doc, vec in tfidf_docs.items()
    }

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [(d, s) for d, s in ranked if s > 0][:top_k]