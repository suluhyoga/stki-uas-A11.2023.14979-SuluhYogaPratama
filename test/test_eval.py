# test/test_eval.py

import sys
import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(ROOT_DIR)

from src.search import search_boolean, search_vector
from src.eval import precision_recall

# =========================
# Contoh Query & Ground Truth
# =========================

query = "ekonomi"

# dokumen yang dianggap relevan (contoh manual)
gold_relevant = {
    "ekonomi_bank_mandiri_prediksi_ekonomi_indonesia_tumbuh_44__003.txt",
    "ekonomi_di_forum_internasional_sri_mulyani_cerita_ekonomi__009.txt",
    "ekonomi_ekonomi_bakal_pulih_usai_penemuan_vaksin_covid19_b_008.txt"
}

# =========================
# Boolean IR Evaluation
# =========================

boolean_result = search_boolean(query)
p, r, tp, fp, fn = precision_recall(boolean_result, gold_relevant)

print("=" * 60)
print("EVALUASI BOOLEAN IR")
print("=" * 60)
print(f"Query     : {query}")
print(f"Precision : {p:.3f}")
print(f"Recall    : {r:.3f}")
print(f"TP={tp}, FP={fp}, FN={fn}")

# =========================
# VSM Evaluation
# =========================

vsm_result = [doc for doc, _ in search_vector(query)]
p, r, tp, fp, fn = precision_recall(vsm_result, gold_relevant)

print("\n" + "=" * 60)
print("EVALUASI VECTOR SPACE MODEL")
print("=" * 60)
print(f"Precision : {p:.3f}")
print(f"Recall    : {r:.3f}")
print(f"TP={tp}, FP={fp}, FN={fn}")