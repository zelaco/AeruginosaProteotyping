import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the base font size
plt.rcParams.update({'font.size': 20})

# Load the annotations file
file_path = 'Outputs/common_accessions_annotations.xlsx'  
annotations_data = pd.read_excel(file_path)

# Parse GO Names and categorize by prefix (F, P, C)
go_names = annotations_data['GO Names'].dropna().str.split(';', expand=True).stack()
go_categories = go_names.str.split(':', n=1, expand=True)  # Split only into two parts: 'Category' and 'Name'

# Ensure that only rows with valid splits are kept
go_categories.columns = ['Category', 'Name']
go_categories = go_categories.dropna()

# Count top GO terms by category
top_molecular_function = go_categories[go_categories['Category'] == 'F']['Name'].value_counts().head(10)
top_biological_process = go_categories[go_categories['Category'] == 'P']['Name'].value_counts().head(10)
top_cellular_component = go_categories[go_categories['Category'] == 'C']['Name'].value_counts().head(10)

# Combine top GO terms into a single DataFrame for plotting
top_terms = pd.concat([
    top_molecular_function.rename("Count").reset_index().assign(Category="Molecular Function"),
    top_biological_process.rename("Count").reset_index().assign(Category="Biological Process"),
    top_cellular_component.rename("Count").reset_index().assign(Category="Cellular Component")
], ignore_index=True)

# Ensure proper column names
top_terms.rename(columns={"index": "Name"}, inplace=True)

# Define color palette for full category names
palette = {'Molecular Function': '#2a62c9', 'Biological Process': '#439447', 'Cellular Component': '#a84832'}

# Plot using Seaborn
plt.figure(figsize=(22, 15))
sns.barplot(
    data=top_terms, 
    y="Name", 
    x="Count", 
    hue="Category", 
    dodge=False,
    palette=palette
)
plt.xlabel("Nr. of Proteins")  
plt.ylabel("GO Term")          
plt.legend(title="Category")   
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig("Outputs/GOAer.png", dpi=300)
