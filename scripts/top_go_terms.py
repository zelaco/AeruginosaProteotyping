import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def analyze_go_terms(input_file, output_file):
    annotations_data = pd.read_excel(input_file)
    go_names = annotations_data['GO Names'].dropna().str.split(';', expand=True).stack()
    go_categories = go_names.str.split(':', n=1, expand=True)
    go_categories.columns = ['Category', 'Name']
    go_categories = go_categories.dropna()

    top_terms = pd.concat([
        go_categories[go_categories['Category'] == 'F']['Name'].value_counts().head(10).rename("Count").reset_index().assign(Category="Molecular Function"),
        go_categories[go_categories['Category'] == 'P']['Name'].value_counts().head(10).rename("Count").reset_index().assign(Category="Biological Process"),
        go_categories[go_categories['Category'] == 'C']['Name'].value_counts().head(10).rename("Count").reset_index().assign(Category="Cellular Component")
    ], ignore_index=True)
    top_terms.rename(columns={"index": "Name"}, inplace=True)

    palette = {'Molecular Function': '#2a62c9', 'Biological Process': '#439447', 'Cellular Component': '#a84832'}

    plt.figure(figsize=(22, 15))
    sns.barplot(data=top_terms, y="Name", x="Count", hue="Category", dodge=False, palette=palette)
    plt.xlabel("Nr. of Proteins")
    plt.ylabel("GO Term")
    plt.legend(title="Category")
    plt.tight_layout()
    plt.savefig(output_file, dpi=300)
    print(f"GO term plot saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze and visualize top GO terms.")
    parser.add_argument("--input-file", required=True, help="Path to the GO annotations Excel file.")
    parser.add_argument("--output-file", required=True, help="Path to save the GO terms plot.")
    args = parser.parse_args()

    analyze_go_terms(args.input_file, args.output_file)
