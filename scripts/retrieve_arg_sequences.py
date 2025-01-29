import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
import os

# Input files
excel_file = "Data/betalactamases.xlsx"  
fasta_dir = "Data/Genomes/"               
# Output files
nucleotide_output = "nucleotide_sequences.fasta"
protein_output = "protein_sequences.fasta"

# Load the Excel file
data = pd.read_excel(excel_file)

# Open output FASTA files
with open(nucleotide_output, "w") as nuc_out, open(protein_output, "w") as prot_out:
    # Process each line in the Excel file
    for index, row in data.iterrows():
        # Extract details from the row
        file_name = row["#FILE"]
        fasta_file = os.path.join(fasta_dir, f"{file_name}.fasta")  # Dynamically select the FASTA file
        sequence_id = row["SEQUENCE"]
        start = int(row["START"])
        end = int(row["END"])
        strand = row["STRAND"]
        gene = row["GENE"]
        
        # Check if the FASTA file exists
        if not os.path.exists(fasta_file):
            print(f"FASTA file {fasta_file} not found. Skipping.")
            continue
        
        # Parse the FASTA file and search for the sequence
        fasta_sequences = {record.id: record for record in SeqIO.parse(fasta_file, "fasta")}
        
        if sequence_id in fasta_sequences:
            genome_seq = fasta_sequences[sequence_id].seq
            extracted_seq = genome_seq[start-1:end]  # Adjust for 1-based indexing
            
            # Reverse complement if the strand is "-"
            if strand == "-":
                extracted_seq = extracted_seq.reverse_complement()
            
            # Construct the FASTA header
            fasta_header = f">{file_name}_{gene}"
            
            # Write nucleotide sequence to the nucleotide FASTA file
            nuc_out.write(f"{fasta_header}\n{extracted_seq}\n")
            
            # Translate to protein and write to the protein FASTA file
            protein_seq = extracted_seq.translate()
            prot_out.write(f"{fasta_header}\n{protein_seq}\n")
        else:
            print(f"Sequence ID {sequence_id} not found in {fasta_file}.")
