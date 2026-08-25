from ml_system.common.io import load_csv
from ml_system.common.settings import RAW_DATA_PATH

def load_raw_data():
    df = load_csv(RAW_DATA_PATH)
    return df

