import pandas as pd
from Bio import SeqIO

# Read the Excel file
df = pd.read_excel('Data/Proteome_simple.xlsx')
accession_numbers = df.iloc[:, 2].tolist()

print(f"Total accession numbers in Excel file: {len(accession_numbers)}")

# Extract sequences from the .faa file
faa_file = 'Data/PaeruginosaProteome.faa'  
output_sequences = []
seq_dict = SeqIO.to_dict(SeqIO.parse(faa_file, "fasta"))

for acc in accession_numbers:
    if acc in seq_dict:
        output_sequences.append(seq_dict[acc])

print(f"Total sequences extracted: {len(output_sequences)}")

# Save extracted sequences to a new file
output_file = 'Outputs/proteotyping_sequences.faa'
with open(output_file, 'w') as output_handle:
    SeqIO.write(output_sequences, output_handle, "fasta")

# Remove duplicate sequences
extracted_sequences = list(SeqIO.parse(output_file, "fasta"))
unique_sequences_dict = {str(seq.seq): seq for seq in extracted_sequences}
unique_sequences = list(unique_sequences_dict.values())

print(f"Total unique sequences: {len(unique_sequences)}")

# Save unique sequences to a new file
unique_output_file = 'Outputs/unique_proteotyping_sequences.faa'
with open(unique_output_file, 'w') as unique_output_handle:
    SeqIO.write(unique_sequences, unique_output_handle, "fasta")

print(f"Unique sequences have been saved to {unique_output_file}")
