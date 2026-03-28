from src.download.downloader import download_gse_dataset
from src.config import DATA_DIR

DATASETS = ["GSE81965", "GSE135251"]

for gse in DATASETS:
    download_gse_dataset(gse, DATA_DIR)
    