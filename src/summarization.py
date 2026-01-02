# src/summarization.py

import re
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words("indonesian"))

# ==================================================
# Utility
# ==================================================

def clean_sentence(sentence: str) -> str:
    sentence = sentence.lower()
    sentence = re.sub(r"\d+", "", sentence)
    sentence = re.sub(r"[^\w\s]", "", sentence)
    return sentence


# ==================================================
# Sentence Scoring
# ==================================================

def sentence_score(sentences: list) -> dict:
    freq = Counter()

    for sent in sentences:
        words = word_tokenize(clean_sentence(sent))
        words = [w for w in words if w not in stop_words]
        freq.update(words)

    scores = {}
    for sent in sentences:
        words = word_tokenize(clean_sentence(sent))
        words = [w for w in words if w not in stop_words]
        if words:
            scores[sent] = sum(freq[w] for w in words) / len(words)

    return scores


# ==================================================
# Summarization Core
# ==================================================

def summarize_text(text: str, max_sentences=2) -> str:
    sentences = sent_tokenize(text)

    if len(sentences) <= max_sentences:
        return text

    scores = sentence_score(sentences)
    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    selected = [s[0] for s in ranked[:max_sentences]]
    return " ".join(selected)


# ==================================================
# Document Summarization
# ==================================================

def summarize_document(raw_text: str) -> str:
    """
    Format dataset:
    Baris pertama : Judul
    Sisanya       : Isi artikel
    """

    lines = [l.strip() for l in raw_text.split("\n") if l.strip()]

    if len(lines) < 2:
        return raw_text

    # Ambil judul dari baris pertama
    title = lines[0]
    title = re.sub(r"^judul\s*:\s*", "", title, flags=re.IGNORECASE)

    # Isi artikel tanpa judul
    content = " ".join(lines[1:])

    summary = summarize_text(content, max_sentences=2)

    return (
        f"📌 Judul:\n{title}\n\n"
        f"📝 Ringkasan Artikel:\n{summary}"
    )