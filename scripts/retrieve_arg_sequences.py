import pandas as pd
import os
from Bio import SeqIO
import argparse

def retrieve_arg_sequences(excel_file, fasta_dir, nucleotide_output, protein_output):
    # Read the Excel file
    arg_df = pd.read_excel(excel_file)
    arg_accessions = arg_df['Accession'].tolist()

    # Initialize lists to hold nucleotide and protein sequences
    nucleotide_sequences = []
    protein_sequences = []

    # Iterate through each FASTA file in the directory
    for fasta_file in os.listdir(fasta_dir):
        fasta_path = os.path.join(fasta_dir, fasta_file)
        for record in SeqIO.parse(fasta_path, "fasta"):
            if record.id in arg_accessions:
                nucleotide_sequences.append(record)
                protein_sequences.append(record.translate())

    # Write nucleotide sequences to file
    with open(nucleotide_output, "w") as nucleotide_file:
        SeqIO.write(nucleotide_sequences, nucleotide_file, "fasta")
    print(f"Nucleotide sequences saved to {nucleotide_output}")

    # Write protein sequences to file
    with open(protein_output, "w") as protein_file:
        SeqIO.write(protein_sequences, protein_file, "fasta")
    print(f"Protein sequences saved to {protein_output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve ARG sequences from genome FASTA files.")
    parser.add_argument("--excel-file", required=True, help="Path to the Excel file with ARG metadata.")
    parser.add_argument("--fasta-dir", required=True, help="Path to the directory containing FASTA files.")
    parser.add_argument("--output-nucleotide", required=True, help="Path to save the nucleotide sequences.")
    parser.add_argument("--output-protein", required=True, help="Path to save the protein sequences.")
    args = parser.parse_args()

    retrieve_arg_sequences(args.excel_file, args.fasta_dir, args.output_nucleotide, args.output_protein)
