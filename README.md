# AeruginosaProteotyping: Proteomic and Genomic Tools for *Pseudomonas aeruginosa* Analysis

This repository provides Python tools for analyzing genomic and proteomic data of *Pseudomonas aeruginosa*. It includes scripts for ARG and VF analysis, heatmaps, GO term visualization, and biomarker identification.

## Features
- **Genome Metrics**:
  - Calculate genome size, GC content, N50, and other genome metrics.
  - Create hierarchical clustermaps from ANI matrices.

  - **Sequence Retrieval**:
  - Extract protein sequences from a `.faa` file based on accession numbers.
  - Remove duplicate sequences.

- **Annotation Filtering and Merging**:
  - Filter EggNOG and InterPro annotation files based on accessions.
  - Merge filtered annotations, deduplicating Gene Ontology (GO) terms.

- **ARG and VF Analysis**:
  - Generate ARG and VF heatmaps with isolate metadata.
  - Extract ARG sequences from genome FASTA files.

- **Visualization Tools**:
  - Analyze and visualize the top GO terms by species.

- **Biomarker Candidate Identification**:
  - Identify species-specific biomarker proteins.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/zelaco/AeruginosaProteotyping.git
   cd AeruginosaProteotyping
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Genome Metrics Calculation
Calculate genome size statistics (e.g., N50, GC content, genome size):
```bash
python scripts/genome_metrics.py --input-dir /path/to/fasta_files --output-file /path/to/genome_stats.csv
```

Generate a hierarchical clustermap from an ANI matrix:
```bash
python scripts/clustermap.py --matrix /path/to/ANI_matrix.xlsx --output /path/to/clustermap.png
```

### 2. ARG and VF Analysis
#### Generate ARG Heatmap:
Create a heatmap of antibiotic resistance genes (ARG):
```bash
python scripts/arg_heatmap.py --file-path /path/to/paerARG.xlsx --output /path/to/HeatmapARG.png
```

#### Generate VF Heatmap:
Create a heatmap of virulence factors (VF):
```bash
python scripts/vf_heatmap.py --file-path /path/to/paerVF.xlsx --output /path/to/HeatmapVF.png
```

#### Extract ARG Sequences:
Retrieve ARG sequences from genome FASTA files:
```bash
python scripts/retrieve_arg_sequences.py --excel-file /path/to/betalactamases.xlsx --fasta-dir /path/to/Genomes/ --output-nucleotide /path/to/nucleotide_sequences.fasta --output-protein /path/to/protein_sequences.fasta
```

### 3. Sequence Retrieval
Extract sequences based on accession numbers from an `.faa` file:
```bash
python scripts/sequence_retrieval.py --accession-file /path/to/PutidaP.xlsx --proteome-file /path/to/PputidaProteome.faa --output-file /path/to/unique_proteotyping_sequences.faa
```

### 4. Annotation Filtering and Merging
#### Filter Annotations:
Filter EggNOG and InterPro annotation files based on accession numbers:
```bash
python scripts/filter_annotations.py --accession-file /path/to/PutidaP.xlsx --eggnog-file /path/to/putida_eggnog.xlsx --interpro-file /path/to/putida_interpro.xlsx --eggnog-output /path/to/filtered_putida_eggnog.xlsx --interpro-output /path/to/filtered_putida_interpro.xlsx
```

#### Merge Annotations:
Combine filtered annotations:
```bash
python scripts/merge_annotations.py --eggnog-file /path/to/filtered_putida_eggnog.xlsx --interpro-file /path/to/filtered_putida_interpro.xlsx --output-file /path/to/merged_putida_annotations.xlsx
```
### 5. Top GO Terms Analysis
Analyze and visualize the top GO terms by species:
```bash
python scripts/top_go_terms.py --input-file /path/to/Outputs/common_accessions_annotations.xlsx --output /path/to/GOAer.png
```

### 6. Biomarker Candidate Identification
Identify species-specific biomarker candidates:
```bash
python scripts/identify_biomarkers.py --common-accessions /path/to/Common_Protein_Accessions.csv --annotations /path/to/Data/merged_aer_annotations.xlsx --output-file /path/to/Outputs/common_accessions_annotations.xlsx
```

