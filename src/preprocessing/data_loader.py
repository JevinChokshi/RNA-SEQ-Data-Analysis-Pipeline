import pandas as pd

def load_data(meta_file, counts_file, label_col, control_label):

    meta_df = pd.read_csv(meta_file, index_col='Sample Name')
    counts_df = pd.read_csv(counts_file, sep='\t', index_col='GeneID')

    # Rename label
    meta_df.rename(columns={label_col: 'disease_state'}, inplace=True)

    # Normalize control label
    meta_df.loc[meta_df['disease_state'] == control_label, 'disease_state'] = 'Control'

    # Drop missing labels
    meta_df = meta_df.dropna(subset=['disease_state'])

    # Remove duplicates
    meta_df = meta_df[~meta_df.index.duplicated(keep="first")]

    # 🔥 CRITICAL: align samples
    common_samples = counts_df.columns.intersection(meta_df.index)

    counts_df = counts_df[common_samples]
    meta_df = meta_df.loc[common_samples]

    # 🔥 Ensure same order
    meta_df = meta_df.loc[counts_df.columns]

    # Optional filtering (restore your logic)
    counts_df = counts_df.loc[(counts_df.sum(axis=1) > 0), :]
    counts_df = counts_df[(counts_df >= 10).sum(axis=1) >= 2]

    print(f"Final aligned samples: {len(common_samples)}")
    print(f"Counts shape: {counts_df.shape}")
    print(f"Meta shape: {meta_df.shape}")

    return counts_df, meta_df