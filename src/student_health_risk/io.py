from __future__ import annotations

from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"


def load_competition_data(input_dir: str | Path = "input") -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    input_path = Path(input_dir)
    train = pd.read_csv(input_path / "train.csv")
    test = pd.read_csv(input_path / "test.csv")
    sample = pd.read_csv(input_path / "sample_submission.csv")
    return train, test, sample


def feature_columns(train: pd.DataFrame) -> list[str]:
    return [c for c in train.columns if c not in {ID_COL, TARGET}]


def categorical_columns(df: pd.DataFrame) -> list[str]:
    return df.select_dtypes(include=["object", "category"]).columns.tolist()
