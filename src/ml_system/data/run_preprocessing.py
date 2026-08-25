from ml_system.common.io import save_parquet
from ml_system.common.settings import PROCESSED_DATA_PATH
from ml_system.data.load_data import load_raw_data
from ml_system.data.preprocess import preprocess_raw_data


def main():
    raw_df = load_raw_data()
    processed_df = preprocess_raw_data(raw_df)
    save_parquet(processed_df, PROCESSED_DATA_PATH)
    print(f"Saved processed data to {PROCESSED_DATA_PATH}")


if __name__ == "__main__":
    main()