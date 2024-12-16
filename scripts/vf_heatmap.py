import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from matplotlib.patches import Patch
from matplotlib.colors import ListedColormap
import argparse

def generate_vf_heatmap(file_path, output_file):
    df = pd.read_excel(file_path)
    df.set_index('Isolate', inplace=True)

    genes_df = df.drop('ST', axis=1).apply(pd.to_numeric, errors='coerce')
    binary_genes_df = genes_df.applymap(lambda x: 1 if x > 0 else 0)
    binary_genes_df['ST'] = df['ST'].astype(str)

    st_labels = LabelEncoder().fit_transform(binary_genes_df['ST'])
    palette = sns.color_palette("tab10", n_colors=len(set(st_labels)))
    st_colors = dict(zip(binary_genes_df['ST'].unique(), palette))
    row_colors = binary_genes_df['ST'].map(st_colors)

    cmap = ListedColormap(['white', '#031d59'])

    sns.set_context("notebook", font_scale=1.1)
    clustermap = sns.clustermap(
        binary_genes_df.drop('ST', axis=1),
        row_cluster=True,
        col_cluster=False,
        cmap=cmap,
        figsize=(12, 12),
        row_colors=row_colors,
        cbar_pos=None
    )

    clustermap.ax_heatmap.legend(
        handles=[
            Patch(facecolor=st_colors[st], edgecolor='black', label=st)
            for st in st_colors
        ],
        title='ST',
        bbox_to_anchor=(-0.1, 1.25),
        frameon=True
    )
    plt.savefig(output_file, dpi=300)
    print(f"VF heatmap saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a VF heatmap.")
    parser.add_argument("--file-path", required=True, help="Path to the VF data Excel file.")
    parser.add_argument("--output-file", required=True, help="Path to save the heatmap.")
    args = parser.parse_args()

    generate_vf_heatmap(args.file_path, args.output_file)
