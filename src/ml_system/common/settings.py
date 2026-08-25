from pathlib import Path
import yaml

PROJECT_ROOT = Path(__file__).resolve().parents[3]

CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

CONFIG = load_config()

RAW_DATA_PATH = PROJECT_ROOT / CONFIG["raw_data"]
PROCESSED_DATA_PATH = PROJECT_ROOT / CONFIG["processed_data"]