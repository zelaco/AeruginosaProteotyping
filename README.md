# *Pseudomonas aeruginosa* Proteotyping

## Code supplement

This repository provides Python tools for analyzing genomic and proteomic data of *Pseudomonas aeruginosa*, for chapter V of my doctoral thesis. It includes scripts for ARG and VF analysis, heatmaps, GO term visualization, and biomarker identification.

## Script explanation
### `genome_metrics.py`:
* Parses multiple FASTA files in a directory.
* Calculates genome statistics including:
    - Genome size
    - GC content
    - Number of contigs
    - N50
    - Longest and shortest contig lengths
    - Average contig length
* Saves results to a CSV file.

### `arg_heatmap.py`:
* Generate a heatmap of Antibiotic Resistance Genes (ARGs) found in all isolates and relates with Sequence type (ST).

### `retrieve_arg_sequences.py`:
* Extract ARG sequences from genome FASTA files. Based on the output from ABRicate.

### `vf_heatmap.py`:
* Generate a heatmap for differences in Virulence Factors (VF) in all isolates, relating with ST. 

### `expression_heatmap.py`:
* Create expression heatmaps from proteomic data.

### `sequence_retrieval.py`:
* Extract protein sequences from a `.faa` file based on accession numbers.
* Remove duplicate sequences.

### `filter_annotations.py`:
* Filter EggNOG and InterPro annotation files based on accessions.

### `merge_annotations.py`:
* Merge filtered annotations outputs from previous script, deduplicating Gene Ontology (GO) terms.

### `top_goterms.py`:
* Analyze and visualize the top GO terms by species, based on the file with the merged annotations.

### `biomarker_candidates.py`:
* Identify common proteins shared across all isolates.

## Contact

If you have any questions or need further information, feel free to reach out:

    Email: [j.serpa@uib.es]
    GitHub: [github.com/zelaco]