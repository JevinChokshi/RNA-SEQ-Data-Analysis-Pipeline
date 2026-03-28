# 📊 RNA-seq Data Analytics Pipeline

## Overview

This project is an end-to-end data analytics pipeline for processing RNA-seq datasets and extracting meaningful patterns from gene expression data.

It automates the workflow from raw data acquisition to statistical analysis and visualization, enabling efficient exploration of high-dimensional biological datasets.

---

## What this project does

* Downloads RNA-seq count data from GEO datasets
* Cleans and aligns raw counts with sample metadata
* Performs differential expression analysis
* Applies normalization (VST) for downstream analysis
* Generates:

  * Volcano plots
  * PCA visualizations
  * Structured result tables

---

## Key Features

* Automated data download from public repositories
* Handles multiple datasets in a single pipeline
* Robust preprocessing and sample alignment
* Statistical analysis using DESeq2 framework
* Built-in visualization (Volcano + PCA)
* Modular and reusable code structure

---

## Project Structure

```id="k9s8dm"
rna-seq-data-analytics-pipeline/
│
├── main_download.py
├── main_analysis.py
├── requirements.txt
├── README.md
│
├── data/
│   └── raw/
│
├── results/
│   └── sample_results/
│
└── src/
    ├── config.py
    ├── download/
    ├── preprocessing/
    ├── analysis/
    ├── visualization/
    └── utils/
```

---

## Installation

```id="h3sd82"
pip install -r requirements.txt
```

---

## Usage

### 1. Download datasets

```id="x4ad92"
python main_download.py
```

### 2. Run analysis

```id="c0k2mz"
python main_analysis.py
```

---

## Outputs

For each dataset, the pipeline generates:

* **Differential expression results (CSV)**
* **Volcano plot**
* **PCA plot**
* **VST-normalized counts**
* PCA coordinate file for further analysis

---

## ⚠️ Important Note (Metadata Requirement)

This pipeline requires a metadata file:

**`SraRunTable.csv`**

➡️ This file must be downloaded manually from the NCBI GEO website for each dataset.

Steps:

1. Open the dataset page on NCBI GEO
2. Navigate to **SRA Run Selector**
3. Download the metadata table (`SraRunTable.csv`)
4. Place it inside the corresponding dataset folder:

```id="y1f3qs"
data/raw/<DATASET_ID>/SraRunTable.csv
```

---

## Approach (Simplified)

1. Download raw count data
2. Load counts and metadata
3. Perform differential analysis
4. Apply normalization (VST)
5. Generate visual insights

---

## Tech Stack

* Python
* Pandas / NumPy
* Scikit-learn
* PyDESeq2
* Matplotlib / Seaborn
* Requests

---

## Notes

* Sample outputs are included for demonstration
* The pipeline is designed to handle varying dataset formats
* Some dataset-specific adjustments may be required
* This pipeline is a submodule of a larger high-dimensional research workflow. It focuses on a specific analytical task while the overarching project remains confidential.

---

## Author

Jevin Chokshi
