# app/main.py

import sys
import os

# ==================================================
# Tambahkan root project ke PYTHONPATH
# ==================================================
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT_DIR)

import streamlit as st
from src.search import search_boolean, search_vector
from src.summarization import summarize_document
from src.clustering import clustering_kmeans

# ==================================================
# Konfigurasi Halaman
# ==================================================
st.set_page_config(
    page_title="UAS STKI - Suluh Yoga Pratama",
    layout="centered"
)

# ==================================================
# HEADER
# ==================================================
st.title("📰 UAS Sistem Temu Kembali Informasi Tema Berita Indonesia")

st.markdown(
    """
    Proyek **UAS Sistem Temu Kembali Informasi (STKI)** oleh **Suluh Yoga Pratama**

    **Fitur Utama:**
    - Boolean Information Retrieval  
    - Vector Space Model (TF-IDF)  
    - Text Summarization  
    - Document Clustering (K-Means)
    """
)

st.markdown("---")

# ==================================================
# TAB NAVIGASI
# ==================================================
tab_search, tab_cluster = st.tabs([
    "🔍 Pencarian Dokumen",
    "📊 Clustering Dokumen"
])

# ==================================================
# TAB 1 — PENCARIAN
# ==================================================
with tab_search:
    st.subheader("🔎 Pencarian Dokumen Berita")

    query = st.text_input(
        "Masukkan Query Pencarian",
        placeholder="contoh: ekonomi AND digital"
    )

    model = st.radio(
        "Pilih Model Pencarian",
        ["Boolean Model", "Vector Space Model (TF-IDF)"],
        horizontal=True
    )

    run_btn = st.button("Cari Dokumen 🔍")

    st.markdown("---")

    if run_btn:
        if not query.strip():
            st.warning("⚠️ Query tidak boleh kosong.")
        else:
            # =========================
            # BOOLEAN IR
            # =========================
            if model == "Boolean Model":
                st.markdown("### 📌 Hasil Boolean Retrieval")

                results = search_boolean(query)

                if not results:
                    st.error("Tidak ada dokumen yang ditemukan.")
                else:
                    st.success(f"Ditemukan {len(results)} dokumen")
                    for doc in results:
                        st.write(f"- **{doc}**")

            # =========================
            # VSM IR
            # =========================
            else:
                st.markdown("### 🏆 Hasil Vector Space Model (TF-IDF)")

                results = search_vector(query)

                if not results:
                    st.error("Tidak ada dokumen relevan.")
                else:
                    for rank, (doc, score) in enumerate(results, start=1):
                        st.markdown(
                            f"**{rank}. {doc}**  \n"
                            f"Skor Similaritas: `{score:.4f}`"
                        )

                        # =========================
                        # Summarization
                        # =========================
                        try:
                            raw_path = os.path.join("data", "raw", doc)
                            with open(raw_path, "r", encoding="utf-8") as f:
                                raw_text = f.read()

                            summary = summarize_document(raw_text)

                            with st.expander("📄 Lihat Ringkasan Dokumen"):
                                st.write(summary)

                        except Exception:
                            st.warning("Gagal memuat ringkasan dokumen.")

# ==================================================
# TAB 2 — CLUSTERING
# ==================================================
with tab_cluster:
    st.subheader("📊 Clustering Dokumen Berita")

    st.markdown(
        """
        Dokumen berita dikelompokkan berdasarkan **kemiripan konten**
        menggunakan **TF-IDF** dan algoritma **K-Means**.
        """
    )

    k = st.slider(
        "Jumlah Cluster (K)",
        min_value=2,
        max_value=10,
        value=5
    )

    if st.button("Proses Clustering"):
        with st.spinner("Melakukan clustering dokumen..."):
            clusters = clustering_kmeans("data/processed", k=k)

        st.success("Clustering selesai!")

        for cluster_id in sorted(clusters.keys()):
            docs = clusters[cluster_id]
            with st.expander(f"Cluster {cluster_id} ({len(docs)} dokumen)"):
                for doc in docs:
                    st.write(f"- {doc}")

# ==================================================
# FOOTER
# ==================================================
st.markdown("---")
st.caption(
    "UAS Sistem Temu Kembali Informasi | "
    "Suluh Yoga Pratama"
)