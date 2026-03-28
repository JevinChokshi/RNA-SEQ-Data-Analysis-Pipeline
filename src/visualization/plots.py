import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def volcano_plot(results_df, out_path, title="Volcano Plot"):
    df = results_df.copy()
    df['-log10(padj)'] = -np.log10(df['padj'] + 1e-10)

    plt.figure(figsize=(8,6))

    # background
    plt.scatter(df['log2FoldChange'], df['-log10(padj)'],
                color='grey', alpha=0.5)

    # significant points
    sig = (df['padj'] < 0.05) & (abs(df['log2FoldChange']) >= 1.5)
    plt.scatter(df.loc[sig, 'log2FoldChange'],
                df.loc[sig, '-log10(padj)'],
                color='red', alpha=0.7)

    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10(padj)")
    plt.title(title)

    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()


def pca_plot(vst_counts, meta_df, out_dir):
    scaler = StandardScaler()
    scaled = scaler.fit_transform(vst_counts)

    pca = PCA(n_components=2)
    pcs = pca.fit_transform(scaled)

    df_pca = pd.DataFrame({
        "PC1": pcs[:, 0],
        "PC2": pcs[:, 1],
        "condition": meta_df['disease_state'].values
    })

    # df_pca.to_csv(os.path.join(out_dir, "PCA_coordinates.csv"), index=False)

    plt.figure(figsize=(7,6))
    sns.scatterplot(data=df_pca, x="PC1", y="PC2", hue="condition", s=100)

    plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
    plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
    plt.title("PCA (VST normalized counts)")

    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "PCA_plot.png"), dpi=300)
    plt.close()


def save_vst(vst_counts, out_dir):
    df = pd.DataFrame(vst_counts)
    path = os.path.join(out_dir, "VST_counts.csv")
    df.to_csv(path, index=False)
    return path