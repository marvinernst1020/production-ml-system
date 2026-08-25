import pandas as pd
from pathlib import Path

def load_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except Exception as e:
        raise RuntimeError(f"Failed to load data from {path}") from e

def save_parquet(df: pd.DataFrame, path: Path) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(path, index=False, engine='pyarrow')
    except Exception as e:
        raise RuntimeError(f"Failed to save data to {path}") from e