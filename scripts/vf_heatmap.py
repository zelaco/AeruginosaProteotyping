import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from matplotlib.patches import Patch
from matplotlib.colors import ListedColormap

# Load the data
file_path = 'paerVF.xlsx'  
df = pd.read_excel(file_path)

# Set 'Isolate' as the index to display isolate names on the heatmap
df.set_index('Isolate', inplace=True)

# Convert gene columns to numeric, assuming 'ST' is a column in your DataFrame
genes_df = df.drop('ST', axis=1).apply(pd.to_numeric, errors='coerce')

# Convert to binary presence/absence (any value > 0 is presence)
binary_genes_df = genes_df.applymap(lambda x: 1 if x > 0 else 0)

# Exclude genes present in all isolates (genes where all values are 1)
binary_genes_df = binary_genes_df.loc[:, (binary_genes_df.sum(axis=0) < len(binary_genes_df))]

# Add 'ST' column back to the DataFrame
binary_genes_df['ST'] = df['ST'].astype(str)

# Generate a color palette for 'ST'
st_labels = LabelEncoder().fit_transform(binary_genes_df['ST'])
palette = sns.color_palette("tab10", n_colors=len(set(st_labels)))
st_colors = dict(zip(binary_genes_df['ST'].unique(), palette))
row_colors = binary_genes_df['ST'].map(st_colors)

# Create a custom colormap for presence (1) and absence (0)
cmap = ListedColormap(['white', '#031d59'])  # Presence is dark blue, absence is white

# Generate the clustermap without the top dendrogram and without the colorbar
sns.set_context("notebook", font_scale=1.1)
clustermap = sns.clustermap(
    binary_genes_df.drop('ST', axis=1),
    row_cluster=True,
    col_cluster=False,  # Remove the top dendrogram
    cmap=cmap,
    figsize=(12, 12),
    row_colors=row_colors,
    cbar_pos=None,  # Remove the colorbar
)

# Adjust row labels (isolate names) font size for better visibility
clustermap.ax_heatmap.set_yticklabels(
    clustermap.ax_heatmap.get_ymajorticklabels(), fontsize=12
)

# Create legend patches for 'ST'
legend_handles = [
    Patch(facecolor=st_colors[st], edgecolor='black', label=st) for st in st_colors
]

# Add the legend to the heatmap, positioned to avoid overlap
clustermap.ax_heatmap.legend(
    handles=legend_handles,
    title='ST',
    bbox_to_anchor=(-0.1, 1.25),
    frameon=True
)

# Save the plot as a PNG file
plt.savefig("Outputs/HeatmapVF.png", dpi=300)

