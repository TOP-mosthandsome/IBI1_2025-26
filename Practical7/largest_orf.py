seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
start_codon = "AUG"
stop_codons = ["UAA", "UAG", "UGA"]
longest_orf = ""
max_length = 0
for i in range(len(seq)):# loop through sequence to find start codons
    if seq[i:i+3] == start_codon:
        # search for stop codon in-frame
        for j in range(i + 3, len(seq), 3):
            codon = seq[j:j+3]
            if codon in stop_codons:
                orf = seq[i:j+3]
                if len(orf) > max_length:
                    longest_orf = orf
                    max_length = len(orf)
                break  # stop at first in-frame stop codon
print("Longest ORF:", longest_orf)
print("Length:", max_length)