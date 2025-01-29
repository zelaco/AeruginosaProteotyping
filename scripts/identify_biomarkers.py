import pandas as pd

# File paths
common_accessions_file = 'Common_Protein_Accessions.csv'
annotations_file_path = 'Data/merged_aer_annotations.xlsx'

# Load the common accessions
common_accessions_df = pd.read_csv(common_accessions_file)
common_accessions = common_accessions_df['Common Accessions'].tolist()

# Load the annotations file
annotations_df = pd.read_excel(annotations_file_path)

# Filter annotations to include only rows where 'SeqName' matches the common accessions
filtered_data = annotations_df[annotations_df['SeqName'].isin(common_accessions)]

# Ensure all relevant columns are present and replace missing data with empty strings
filtered_data = filtered_data.reindex(columns=['SeqName', 'GO', 'GO Names', 'KEGG KO', 'KEGG Pathway', 'Description'])
filtered_data.fillna('', inplace=True)

# Save the filtered data to an Excel file
output_file_path = 'Outputs/common_accessions_annotations.xlsx'
filtered_data.to_excel(output_file_path, index=False)

# Debug print for final output
print(f"Filtered annotations saved to '{output_file_path}'. Total: {len(filtered_data)} entries.")
