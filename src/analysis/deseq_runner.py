from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
from itertools import combinations
import os

from src.visualization.plots import volcano_plot, pca_plot, save_vst


def run_deseq(counts_df, meta_df, labels, results_dir):

    dds = DeseqDataSet(
        counts=counts_df.T,
        metadata=meta_df,
        design="~disease_state"
    )

    dds.deseq2()

    # ----------------------------
    # CONTRASTS
    # ----------------------------
    for c in combinations(labels, 2):

        if 'Control' in c:
            control_idx = c.index('Control')
            contrast = ['disease_state', c[1-control_idx], c[control_idx]]

            print(f"\nRunning: {contrast[1]} vs {contrast[2]}")

            stats = DeseqStats(dds, contrast=contrast)
            stats.summary()

            results = stats.results_df.copy()

            # Save results
            fname = f"{contrast[1]}_vs_{contrast[2]}"
            out_csv = os.path.join(results_dir, f"{fname}_DESeq2_results.csv")
            results.to_csv(out_csv)

            # Volcano plot
            volcano_plot(
                results,
                os.path.join(results_dir, f"{fname}_volcano.png"),
                title=f"{contrast[1]} vs {contrast[2]}"
            )

    # ----------------------------
    # VST + PCA
    # ----------------------------
    dds.vst()
    vst_counts = dds.layers["vst_counts"]

    save_vst(vst_counts, results_dir)
    pca_plot(vst_counts, meta_df, results_dir)