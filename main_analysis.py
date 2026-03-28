from src.preprocessing.data_loader import load_data
from src.analysis.deseq_runner import run_deseq
from src.config import DATA_DIR, RESULTS_DIR
import glob
import os

DATASETS = {
    'GSE81965': ['disease', 'ngt'],
    'GSE135251' : ['disease', 'Control'],
}

for ds, params in DATASETS.items():

    counts_files = glob.glob(os.path.join(DATA_DIR, ds, "*count*.tsv"))
    if not counts_files:
        raise FileNotFoundError(f"No count file found in {ds}") 
    counts = counts_files[0]
    meta = os.path.join(DATA_DIR, ds, "SraRunTable.csv")

    counts_df, meta_df = load_data(meta, counts, params[0], params[1])

    outdir = os.path.join(RESULTS_DIR, ds)
    os.makedirs(outdir, exist_ok=True)

    labels = meta_df['disease_state'].unique()

    run_deseq(counts_df, meta_df, labels, outdir)