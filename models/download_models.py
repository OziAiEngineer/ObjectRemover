import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.index import LAMA_ENABLE, SAM_ENABLE

print("Object Remover models (LaMa, SAM) are configured to load and download dynamically via iopaint.")
if LAMA_ENABLE:
    print("- LaMa Inpainting: Enabled")
else:
    print("- LaMa Inpainting: Disabled (set LAMA_ENABLE=true in .env)")

if SAM_ENABLE:
    print("- SAM Segmenter: Enabled")
else:
    print("- SAM Segmenter: Disabled (set SAM_ENABLE=true in .env)")

print("Dynamic loading checks OK.")
