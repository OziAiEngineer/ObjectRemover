import os
import traceback
import torch

from config.index import (
    LAMA_ENABLE,
    SAM_ENABLE,
    SAM_MODEL_TYPE,
)

# Shared device for LaMa and SAM
FORCE_CPU = os.environ.get("FORCE_CPU", "false").lower() == "true"
_INPAINT_DEVICE = torch.device("cpu" if FORCE_CPU else ("cuda" if torch.cuda.is_available() else "cpu"))

# ===========================================================================================================================

# Load LaMa Inpainting Model
LAMA_MODEL = None
if LAMA_ENABLE:
    try:
        from iopaint.model_manager import ModelManager
        print(f"[load_models] Loading LaMa model on {_INPAINT_DEVICE}...")
        LAMA_MODEL = ModelManager(
            name="lama",
            device=_INPAINT_DEVICE,
            no_half=False,
            low_mem=False,
            disable_nsfw=False,
            sd_cpu_textencoder=False,
            local_files_only=False,
            cpu_offload=False,
        )
        print("[load_models] LaMa model loaded successfully!")
    except Exception as e:
        print(f"[ERROR] Failed to load LaMa model: {e}")
        print(traceback.format_exc())
        LAMA_MODEL = None

# ===========================================================================================================================

# Load SAM Segmentation Model
SAM_PROCESSOR = None
if SAM_ENABLE:
    try:
        from utils.sam_process import SAMProcessor
        print(f"[load_models] Loading SAM model ({SAM_MODEL_TYPE}) on {_INPAINT_DEVICE}...")
        SAM_PROCESSOR = SAMProcessor(
            model_type=SAM_MODEL_TYPE,
            device=str(_INPAINT_DEVICE),
        )
        print("[load_models] SAM model loaded successfully!")
    except Exception as e:
        print(f"[ERROR] Failed to load SAM model: {e}")
        print(traceback.format_exc())
        SAM_PROCESSOR = None