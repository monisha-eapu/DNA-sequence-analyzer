"""Input cleaning and validation."""

VALID_BASES = set("ATGC")


def clean_sequence(raw: str) -> str:
    """Accept plain text or FASTA; return an uppercase sequence with no headers/whitespace."""
    lines = [l.strip() for l in raw.splitlines() if l.strip() and not l.startswith(">")]
    return "".join(lines).replace(" ", "").upper()


def validate_sequence(seq: str):
    """Return (is_valid, sorted list of invalid characters)."""
    invalid = sorted(set(seq) - VALID_BASES)
    return (len(seq) > 0 and not invalid), invalid
