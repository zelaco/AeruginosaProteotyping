import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data 
data = pd.read_excel("Data/Proteome_simple.xlsx")

# Extract the Accession column and dynamically select heatmap data columns
accession_column = 'Accession'  

# Identify columns that contain the specific substring for heatmap data
heatmap_columns = [col for col in data.columns if 'UCE_D' in col or 'ICU_D' in col or 'H_D' in col or 'GM_D' in col or 'UCE_R' in col]

# Subset the data
heatmap_data = data[[accession_column] + heatmap_columns].set_index(accession_column)

# Remove rows where any value in heatmap_columns is zero or NaN
heatmap_data = heatmap_data[(heatmap_data != 0).all(axis=1)].dropna(subset=heatmap_columns)

# Plot the clustermap
sns.clustermap(
    heatmap_data,
    cmap='magma_r',       # Choose a colormap
    metric='euclidean',   # Distance metric for clustering
    method='average',     # Clustering method
    figsize=(12, 12),     # Adjust the size of the plot
    yticklabels=False,    # Remove y-axis labels
    row_cluster=False,    # Disable row clustering
    dendrogram_ratio=(.1, .1), # Adjust the size of the dendrogram
    cbar_pos=(0, .2, .03, .4)  # Position of the colorbar
)


# Save the plot
plt.savefig('Outputs/heatmap.png', dpi=300, bbox_inches='tight')
