
from pathlib import Path
def read_fasta(path):
    #Return the FASTA header and sequence as strings.
    header = ""
    seq_parts = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                header = line[1:]
            else:
                seq_parts.append(line.upper())
    return header, "".join(seq_parts)
def read_blosum(path):
    #Read a square substitution matrix into a dictionary keyed by aa pairs.
    rows = []
    with open(path, "r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line and not line.startswith("#"):
                rows.append(line.split())
    amino_acids = rows[0]
    matrix = {}
    for row in rows[1:]:
        row_aa = row[0]
        scores = list(map(int, row[1:]))
        for col_aa, score in zip(amino_acids, scores):
            matrix[(row_aa, col_aa)] = score
    return matrix
def compare(seq1, seq2, matrix):
    #Compare two equal-length sequences using a non-gapped global alignment.
    if len(seq1) != len(seq2):
        raise ValueError("This simple non-gapped alignment requires equal-length sequences.")

    position_scores = []
    identities = 0
    for aa1, aa2 in zip(seq1, seq2):
        if aa1 == aa2:
            identities += 1
        position_scores.append(matrix[(aa1, aa2)])

    raw_score = sum(position_scores)
    length = len(seq1)
    percent_identity = identities / length * 100
    score_per_residue = raw_score / length
    return raw_score, score_per_residue, identities, percent_identity, position_scores


def print_result(name, header1, seq1, header2, seq2, result):
    raw_score, score_per_residue, identities, percent_identity, _ = result
    print("=" * 72)
    print(name)
    print("Sequence 1:", header1)
    print(seq1)
    print("Sequence 2:", header2)
    print(seq2)
    print(f"Length: {len(seq1)} amino acids")
    print(f"BLOSUM62 raw score: {raw_score}")
    print(f"BLOSUM62 score per residue: {score_per_residue:.3f}")
    print(f"Identical amino acids: {identities}/{len(seq1)}")
    print(f"Percentage identity: {percent_identity:.2f}%")
    print()


if __name__ == "__main__":
    base = Path(__file__).resolve().parent
    matrix = read_blosum(base / "blosum62.txt")

    human_h, human = read_fasta(base / "human_DLX5_P56178.fasta")
    mouse_h, mouse = read_fasta(base / "mouse_DLX5_P70396.fasta")
    random_h, random_seq = read_fasta(base / "random_protein_seed13.fasta")

    comparisons = [
        ("Human DLX5 vs mouse DLX5", human_h, human, mouse_h, mouse),
        ("Human DLX5 vs random protein", human_h, human, random_h, random_seq),
        ("Mouse DLX5 vs random protein", mouse_h, mouse, random_h, random_seq),
    ]

    for name, h1, s1, h2, s2 in comparisons:
        result = compare(s1, s2, matrix)
        print_result(name, h1, s1, h2, s2, result)
