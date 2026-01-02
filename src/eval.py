# src/eval.py

def precision_recall(system_result, gold_relevant):
    """
    Hitung Precision & Recall
    """
    system_result = set(system_result)
    gold_relevant = set(gold_relevant)

    tp = len(system_result & gold_relevant)
    fp = len(system_result - gold_relevant)
    fn = len(gold_relevant - system_result)

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0

    return precision, recall, tp, fp, fn