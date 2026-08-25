import pandas as pd

def adjust_total_charges(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df["TotalCharges"] = df["TotalCharges"].fillna(0)
    return df

def target_encoding(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    return df

def preprocess_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    df = adjust_total_charges(df)
    df = target_encoding(df)
    return df