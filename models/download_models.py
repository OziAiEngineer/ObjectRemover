import sys
import os
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import gdown
from config.index import LAMA_ENABLE, SAM_ENABLE
from models.url_paths import LAMA_MODEL_PATH, SAM_MODEL_PATH

MODELS_DIR = os.path.join(os.path.dirname(__file__), "weights")
os.makedirs(MODELS_DIR, exist_ok=True)

LAMA_OUTPUT = os.path.join(MODELS_DIR, "lama_model.pt")
SAM_OUTPUT  = os.path.join(MODELS_DIR, "sam_model.pth")


def extract_gdrive_id(url: str) -> str:
    """Extract the file ID from a Google Drive share URL."""
    match = re.search(r"/d/([a-zA-Z0-9_-]+)", url)
    if not match:
        raise ValueError(f"Could not extract Google Drive file ID from URL: {url}")
    return match.group(1)


def download_if_missing(url: str, output_path: str, label: str):
    if os.path.exists(output_path):
        print(f"  ✔  {label} already downloaded — skipping.")
        return
    print(f"  ↓  Downloading {label} from Google Drive …")
    file_id = extract_gdrive_id(url)
    gdown.download(id=file_id, output=output_path, quiet=False)
    print(f"  ✔  {label} saved to: {output_path}")


if __name__ == "__main__":
    print("Object Remover — model download utility\n")

    if LAMA_ENABLE:
        print("LaMa Inpainting: Enabled")
        download_if_missing(LAMA_MODEL_PATH, LAMA_OUTPUT, "LaMa model")
    else:
        print("LaMa Inpainting: Disabled (set LAMA_ENABLE=true in .env)")

    if SAM_ENABLE:
        print("SAM Segmenter: Enabled")
        download_if_missing(SAM_MODEL_PATH, SAM_OUTPUT, "SAM model")
    else:
        print("SAM Segmenter: Disabled (set SAM_ENABLE=true in .env)")

    print("\nDone.")
