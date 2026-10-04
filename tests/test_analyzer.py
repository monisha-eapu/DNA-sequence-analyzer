from analyzer.validate import clean_sequence, validate_sequence
from analyzer.basic_stats import nucleotide_counts, gc_content, reverse_complement, transcribe
from analyzer.translate import translate


def test_clean_fasta():
    assert clean_sequence(">seq1\nATG\nCCC\n") == "ATGCCC"


def test_validate():
    assert validate_sequence("ATGC") == (True, [])
    assert validate_sequence("ATGX") == (False, ["X"])
    assert validate_sequence("")[0] is False


def test_counts_and_gc():
    assert nucleotide_counts("AATGC") == {"A": 2, "T": 1, "G": 1, "C": 1}
    assert gc_content("GGCC") == 100.0
    assert gc_content("ATAT") == 0.0


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"


def test_transcribe():
    assert transcribe("ATGT") == "AUGU"


def test_translate():
    assert translate("ATGGCCTAA") == "MA"
    assert translate("ATGGCCTAA", to_stop=False) == "MA*"
