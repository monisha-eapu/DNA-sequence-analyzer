"""mRNA/DNA -> protein using the standard genetic code."""

_BASES = "TCAG"
_AMINO = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE = {
    a + b + c: _AMINO[i]
    for i, (a, b, c) in enumerate((a, b, c) for a in _BASES for b in _BASES for c in _BASES)
}


def translate(dna: str, to_stop: bool = True) -> str:
    """Translate DNA (reading frame 1). '*' marks a stop codon."""
    protein = []
    for i in range(0, len(dna) - len(dna) % 3, 3):
        aa = CODON_TABLE[dna[i:i + 3]]
        if aa == "*" and to_stop:
            break
        protein.append(aa)
    return "".join(protein)
