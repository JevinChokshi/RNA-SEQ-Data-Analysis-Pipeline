import os
import gzip
import shutil

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def unzip_gz(gz_path):
    out_path = gz_path.replace(".gz", "")
    with gzip.open(gz_path, "rb") as f_in:
        with open(out_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    return out_path