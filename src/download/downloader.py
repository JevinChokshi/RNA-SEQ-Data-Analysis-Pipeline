import os
import requests
from .geo_utils import *
from ..utils.file_utils import unzip_gz, ensure_dir

def download_file(url, out_path, chunk_size=8192):
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(out_path, "wb") as f:
        for chunk in r.iter_content(chunk_size):
            if chunk:
                f.write(chunk)

def download_gse_dataset(gse, outdir):
    print(f"\nProcessing {gse}")
    gse_dir = os.path.join(outdir, gse)
    ensure_dir(gse_dir)

    try:
        ncbi_page = build_ncbi_download_page(gse)
        raw_counts_link = find_ncbi_raw_counts(ncbi_page)

        if raw_counts_link:
            print("Using NCBI raw counts")
            download_url = "https://www.ncbi.nlm.nih.gov" + raw_counts_link
            fname = raw_counts_link.split("file=")[-1]
            out_path = os.path.join(gse_dir, fname)

            download_file(download_url, out_path)

            if out_path.endswith(".gz"):
                parsed = unzip_gz(out_path)
                os.remove(out_path)
                return parsed

        else:
            print("Fallback to supplements")

    except Exception as e:
        print("NCBI failed:", e)

    # fallback
    url = build_geo_supplement_url(gse)
    files = list_files(url)

    for file in files:
        download_url = url + file
        out_path = os.path.join(gse_dir, file)

        download_file(download_url, out_path)

        if out_path.endswith(".gz"):
            parsed = unzip_gz(out_path)
            os.remove(out_path)