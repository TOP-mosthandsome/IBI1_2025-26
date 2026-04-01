
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"
stop_codons = ["TAA", "TAG", "TGA"]
def find_stops(sequence):
    longest_orf =""
    stop_used = ""
    for i in range(len(sequence)):
        if sequence[i:i+3] == "ATG":
            for j in range(i+3, len(sequence), 3):
                codon = sequence[j:j+3]
                if len(codon) < 3:
                    break
                if codon in ["TAA", "TAG", "TGA"]:
                    orf = sequence[i:j+3]
                    if len(orf) > len(longest_orf):
                        longest_orf = orf
                        stop_used = codon
                    break
    if stop_used == "":
        return []
    else:
        return [stop_used]
infile = open(input_file, "r")
outfile = open(output_file, "w")

sequence = ""
header = ""

for line in infile:

    line = line.strip()

    if line.startswith(">"):

        # process previous sequence
        if sequence != "":
            stops = find_stops(sequence)

            if len(stops) > 0:
                gene_name = header.split()[0][1:]
                outfile.write(">" + gene_name + " " + " ".join(stops) + "\n")
                outfile.write(sequence + "\n")

        header = line
        sequence = ""

    else:
        sequence = sequence + line

# process last sequence
if sequence != "":
    stops = find_stops(sequence)

    if len(stops) > 0:
        gene_name = header.split()[0][1:]
        outfile.write(">" + gene_name + " " + " ".join(stops) + "\n")
        outfile.write(sequence + "\n")

infile.close()
outfile.close()

print("Finished! Check stop_genes.fa")