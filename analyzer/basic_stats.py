"""Basic sequence statistics and conversions."""

COMPLEMENT = {"A": "T", "T": "A", "G": "C", "C": "G"}


def nucleotide_counts(seq: str) -> dict:
    return {base: seq.count(base) for base in "ATGC"}


def gc_content(seq: str) -> float:
    """GC percentage (0-100)."""
    if not seq:
        return 0.0
    return round((seq.count("G") + seq.count("C")) / len(seq) * 100, 2)


def reverse_complement(seq: str) -> str:
    return "".join(COMPLEMENT[b] for b in reversed(seq))


def transcribe(seq: str) -> str:
    """DNA coding strand -> mRNA."""
    return seq.replace("T", "U")
