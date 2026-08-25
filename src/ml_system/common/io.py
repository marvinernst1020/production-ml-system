import pandas as pd
from pathlib import Path

def load_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise RuntimeError(f"Failed to load data from {path}") from e