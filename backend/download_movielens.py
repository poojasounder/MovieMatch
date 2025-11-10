import os
import urllib.request
import zipfile

DATA_DIR = "data"
DATA_URL = "http://files.grouplens.org/datasets/movielens/ml-100k.zip"
ZIP_PATH = os.path.join(DATA_DIR, "ml-100k.zip")
EXTRACT_PATH = os.path.join(DATA_DIR, "ml-100k")

def download_dataset():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(ZIP_PATH):
        print(f"Downloading dataset from {DATA_URL}...")
        urllib.request.urlretrieve(DATA_URL, ZIP_PATH)
        print("Download complete.")
    else:
        print("Dataset zip already exists. Skipping download.")

def extract_dataset():
    if not os.path.exists(EXTRACT_PATH):
        print(f"Extracting {ZIP_PATH}...")
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)
        print("Extraction complete.")
    else:
        print("Dataset already extracted. Skipping extraction.")

if __name__ == "__main__":
    download_dataset()
    extract_dataset()
