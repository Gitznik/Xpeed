import datetime as dt

import pandas as pd


def get_data(user: str, start: dt.date, end: dt.date) -> pd.DataFrame:
    df = pd.read_csv("test_data.csv")
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df[(df["user"] == user) & (df["date"] >= start) & (df["date"] <= end)]  # type: ignore
