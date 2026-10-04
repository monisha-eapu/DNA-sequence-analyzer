import pandas as pd
import streamlit as st

from analyzer.validate import clean_sequence, validate_sequence
from analyzer.basic_stats import nucleotide_counts, gc_content, reverse_complement, transcribe
from analyzer.translate import translate

st.set_page_config(page_title="DNA Sequence Analyzer", page_icon="🧬", layout="wide")
st.title("🧬 DNA Sequence Analyzer")
st.caption("Paste a DNA sequence or upload a FASTA file to analyze it.")

# ---------- Input ----------
with st.sidebar:
    st.header("Input")
    uploaded = st.file_uploader("Upload FASTA / TXT", type=["fasta", "fa", "txt"])
    use_sample = st.button("Load sample (HBB gene fragment)")
    default = ""
    if use_sample:
        with open("data/sample.fasta") as f:
            default = f.read()
    text = st.text_area("...or paste sequence", value=default, height=200)

raw = uploaded.read().decode("utf-8") if uploaded else text
seq = clean_sequence(raw)

if not seq:
    st.info("👈 Add a sequence in the sidebar to begin.")
    st.stop()

ok, invalid = validate_sequence(seq)
if not ok:
    st.error(f"Invalid characters found: {', '.join(invalid)}. Only A, T, G, C are allowed.")
    st.stop()

# ---------- Analysis ----------
tab1, tab2 = st.tabs(["📊 Overview", "🔬 Transcription & Translation"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("Length (bp)", len(seq))
    c2.metric("GC content", f"{gc_content(seq)}%")
    c3.metric("AT content", f"{round(100 - gc_content(seq), 2)}%")

    counts = nucleotide_counts(seq)
    st.subheader("Nucleotide composition")
    st.bar_chart(pd.DataFrame({"Count": counts}))

    st.subheader("Reverse complement")
    st.code(reverse_complement(seq), language=None)

with tab2:
    st.subheader("mRNA (transcription)")
    st.code(transcribe(seq), language=None)
    st.subheader("Protein (translation, frame 1)")
    st.code(translate(seq) or "No protein (sequence too short or starts with a stop codon)", language=None)
    st.caption("Translation stops at the first stop codon.")
