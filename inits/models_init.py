from config.index import LAMA_ENABLE, SAM_ENABLE
from models import load_models

# ── Object Remover ────────────────────────────────────────────────────────────
lama_model = None
if LAMA_ENABLE:
    lama_model = load_models.LAMA_MODEL

sam_processor = None
if SAM_ENABLE:
    sam_processor = load_models.SAM_PROCESSOR
