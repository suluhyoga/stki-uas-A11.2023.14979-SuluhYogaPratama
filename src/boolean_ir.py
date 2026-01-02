# src/boolean_ir.py

import os
from collections import defaultdict

# ==================================================
# Load dokumen hasil preprocessing
# ==================================================

def load_processed_docs(folder_path):
    docs = {}
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                docs[file] = f.read().split()
    return docs


# ==================================================
# Inverted Index
# ==================================================

def build_inverted_index(docs):
    index = defaultdict(set)
    for doc, tokens in docs.items():
        for token in set(tokens):
            index[token].add(doc)
    return index


# ==================================================
# Boolean Search (STABIL & AMAN)
# ==================================================

def boolean_search(query, index, all_docs):
    """
    Mendukung:
    - term
    - term AND term
    - term OR term
    - NOT term
    """

    tokens = query.lower().split()

    # ===== NOT =====
    if "not" in tokens and len(tokens) == 2:
        term = tokens[1]
        return set(all_docs) - index.get(term, set())

    # ===== AND =====
    if "and" in tokens:
        pos = tokens.index("and")
        if pos > 0 and pos < len(tokens) - 1:
            t1 = tokens[pos - 1]
            t2 = tokens[pos + 1]
            return index.get(t1, set()) & index.get(t2, set())

    # ===== OR =====
    if "or" in tokens:
        pos = tokens.index("or")
        if pos > 0 and pos < len(tokens) - 1:
            t1 = tokens[pos - 1]
            t2 = tokens[pos + 1]
            return index.get(t1, set()) | index.get(t2, set())

    # ===== single term =====
    return index.get(tokens[0], set())