import json
import pandas as pd

def load_dataset(path: str):
    df = pd.read_csv(path)
    df["labels"] = df["labels"].apply(json.loads)
    df["mapped labels"] = df["mapped labels"].apply(json.loads)
    df.fillna("")
    return df

def save_dataset(df: pd.DataFrame, path: str):
    df["labels"] = df["labels"].apply(json.dumps)
    df["mapped labels"] = df["mapped labels"].apply(json.dumps)
    df.to_csv(path, index=False)