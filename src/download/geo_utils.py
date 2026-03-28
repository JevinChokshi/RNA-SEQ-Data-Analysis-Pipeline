import requests
import re
import html

def build_ncbi_download_page(gse):
    return f"https://www.ncbi.nlm.nih.gov/geo/download/?acc={gse}"

def build_geo_supplement_url(gse):
    prefix = gse[:-3] + "nnn"
    return f"https://ftp.ncbi.nlm.nih.gov/geo/series/{prefix}/{gse}/suppl/"

def find_ncbi_raw_counts(url):
    r = requests.get(url)
    r.raise_for_status()

    pattern = r'href="([^"]*raw_counts[^"]*\.tsv\.gz)"'
    matches = re.findall(pattern, r.text)

    for m in matches:
        clean = html.unescape(m)
        if not clean.startswith("/"):
            clean = "/" + clean
        return clean
    return None

def list_files(url):
    r = requests.get(url)
    r.raise_for_status()

    files = []
    for line in r.text.split("\n"):
        if "href=" in line:
            part = line.split("href=")[1].split(">")[0]
            fname = part.replace('"', '')
            if not fname.startswith("?") and fname != "../":
                files.append(fname)
    return files