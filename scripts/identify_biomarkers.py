import pandas as pd
import argparse

def identify_biomarkers(common_accessions_file, annotations_file, output_file):
    common_accessions_df = pd.read_csv(common_accessions_file)
    common_accessions = common_accessions_df['Common Accessions'].tolist()
    annotations_df = pd.read_excel(annotations_file)

    filtered_data = annotations_df[annotations_df['SeqName'].isin(common_accessions)]
    filtered_data = filtered_data.reindex(columns=['SeqName', 'GO', 'GO Names', 'KEGG KO', 'KEGG Pathway', 'Description'])
    filtered_data.fillna('', inplace=True)

    filtered_data.to_excel(output_file, index=False)
    print(f"Filtered annotations saved to {output_file}. Total: {len(filtered_data)} entries.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Identify biomarker candidates from annotations.")
    parser.add_argument("--common-accessions", required=True, help="Path to the common accessions CSV file.")
    parser.add_argument("--annotations-file", required=True, help="Path to the annotations Excel file.")
    parser.add_argument("--output-file", required=True, help="Path to save the biomarker annotations.")
    args = parser.parse_args()

    identify_biomarkers(args.common_accessions, args.annotations_file, args.output_file)
