def calculate_protein_mass(sequence):  
    amino_acid_masses = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08, 
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06, 
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06, 
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }    
    total_mass = 0.0   
    for aa in sequence:
        if aa in amino_acid_masses:
            total_mass += amino_acid_masses[aa]
        else:
            return f"Error: Amino acid '{aa}' is not recognized."
    return total_mass
example_sequence = "MGA"
result = calculate_protein_mass(example_sequence)
if isinstance(result, float):
    print(f"The total mass of the sequence '{example_sequence}' is {result:.2f} amu.")
else:
    print(result)