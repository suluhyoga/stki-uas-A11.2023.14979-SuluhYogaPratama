# test/test_summarization_eval.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from src.summarization import summarize_text
from nltk.tokenize import word_tokenize

# =========================
# Simple ROUGE-1
# =========================

def rouge_1(system, reference):
    sys_tokens = set(word_tokenize(system.lower()))
    ref_tokens = set(word_tokenize(reference.lower()))

    overlap = sys_tokens & ref_tokens
    recall = len(overlap) / len(ref_tokens) if ref_tokens else 0
    precision = len(overlap) / len(sys_tokens) if sys_tokens else 0

    return precision, recall

# =========================
# Contoh Evaluasi
# =========================

text = """
Ekonomi digital berkembang pesat di Indonesia.
Transformasi teknologi mendorong pertumbuhan UMKM.
Namun, tantangan regulasi masih menjadi kendala utama.
"""

reference_summary = "Ekonomi digital berkembang pesat dan mendorong UMKM."

system_summary = summarize_text(text, max_sentences=1)

p, r = rouge_1(system_summary, reference_summary)

print("=" * 60)
print("EVALUASI TEXT SUMMARIZATION (ROUGE-1)")
print("=" * 60)
print("System Summary   :", system_summary)
print("Reference Summary:", reference_summary)
print(f"Precision: {p:.3f}")
print(f"Recall   : {r:.3f}")