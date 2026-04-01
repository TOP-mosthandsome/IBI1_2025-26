import matplotlib.pyplot as plt
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
stop_codon = input("Enter stop codon (TAA, TAG, TGA): ")
stop_codon = stop_codon.upper()
if stop_codon not in ["TAA", "TAG", "TGA"]:
    print("Wrong input!")
    exit()
codon_counts = {}
def process_sequence(sequence):
    longest_orf = ""
    for i in range(len(sequence)):
        if sequence[i:i+3] == "ATG":
            for j in range(i+3, len(sequence), 3):
                codon = sequence[j:j+3]
                if len(codon) < 3:
                    break
                if codon == stop_codon:
                    orf = sequence[i:j+3]
                    if len(orf) > len(longest_orf):
                        longest_orf = orf
                        break
    for i in range(0, len(longest_orf)-3, 3):
        codon = longest_orf[i:i+3]
        if codon != stop_codon:
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1
infile = open(input_file, "r")
sequence = ""
for line in infile:
    line = line.strip()
    if line.startswith(">"):
        if sequence != "":
            process_sequence(sequence)
        sequence = ""
    else:
        sequence = sequence + line
# last sequence
if sequence != "":
    process_sequence(sequence)
infile.close()
# check if empty
if len(codon_counts) == 0:
    print("No data found.")
    exit()
labels = list(codon_counts.keys())
sizes = list(codon_counts.values())
plt.figure()
plt.pie(sizes, labels=labels)
plt.title("Codon usage for " + stop_codon)
plt.savefig("codon_chart.png")
print("Chart saved as codon_chart.png")