# src/preprocess.py

import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# ==================================================
# SAFE NLTK SETUP (UNTUK STREAMLIT CLOUD)
# ==================================================

def ensure_nltk():
    try:
        stopwords.words("indonesian")
    except LookupError:
        nltk.download("stopwords")
        nltk.download("punkt_tab")
        nltk.download("punkt")

ensure_nltk()

# ==================================================
# INISIALISASI NLP TOOLS
# ==================================================

factory = StemmerFactory()
stemmer = factory.create_stemmer()
stop_words = set(stopwords.words("indonesian"))

# ==================================================
# TAHAPAN PREPROCESSING
# ==================================================

def clean(text: str) -> str:
    """
    Case folding, hapus angka & tanda baca
    """
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str) -> list:
    """
    Tokenisasi teks
    """
    return word_tokenize(text)


def remove_stopwords(tokens: list) -> list:
    """
    Menghapus stopword Bahasa Indonesia
    """
    return [t for t in tokens if t not in stop_words]


def stem(tokens: list) -> list:
    """
    Stemming Bahasa Indonesia
    """
    return [stemmer.stem(t) for t in tokens]


def preprocess_text(text: str) -> list:
    """
    Pipeline preprocessing lengkap
    """
    text = clean(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens)
    tokens = stem(tokens)
    return tokens


# ==================================================
# PROSES FOLDER (RAW → PROCESSED)
# ==================================================

def process_folder(input_folder: str, output_folder: str):
    """
    Preprocessing seluruh file .txt (raw → processed)
    """
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                text = f.read()

            tokens = preprocess_text(text)

            with open(os.path.join(output_folder, filename), "w", encoding="utf-8") as f:
                f.write(" ".join(tokens))

            print(f"[OK] {filename} → {len(tokens)} tokens")