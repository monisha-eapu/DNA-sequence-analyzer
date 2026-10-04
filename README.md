# 🧬 DNA Sequence Analyzer

A web app to analyze DNA sequences, built with Python and Streamlit.

## Features (current)
- Paste a sequence or upload a FASTA file, with input validation
- Length, nucleotide counts, GC/AT content, composition chart
- Reverse complement
- Transcription (DNA → mRNA) and translation (mRNA → protein)

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Run tests
```bash
pytest
```

## Project structure
```
app.py            # Streamlit UI
analyzer/         # Core logic (validate, basic_stats, translate)
tests/            # Unit tests
data/             # Sample FASTA
```

## Roadmap
- Mutation detection with alignment
- ORF finder
- NCBI gene fetch
- PDF/CSV report export
