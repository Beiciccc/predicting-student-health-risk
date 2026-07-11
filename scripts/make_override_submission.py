#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


ID_COL = "id"
TARGET = "health_condition"
LABELS = {"at-risk", "fit", "unhealthy"}


def parse_overrides(items: list[str]) -> dict[int, str]:
    overrides: dict[int, str] = {}
    for item in items:
        raw_id, label = item.split("=", 1)
        row_id = int(raw_id)
        if row_id in overrides:
            raise ValueError(f"duplicate override ID: {row_id}")
        if label not in LABELS:
            raise ValueError(f"unknown label for {row_id}: {label}")
        overrides[row_id] = label
    return overrides


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True)
    parser.add_argument("--override", action="append", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--output-dir", default="submissions")
    args = parser.parse_args()

    base_path = Path(args.base)
    submission = pd.read_csv(base_path)
    if list(submission.columns) != [ID_COL, TARGET]:
        raise ValueError(f"unexpected columns in {base_path}: {list(submission.columns)}")
    if not submission[ID_COL].is_unique:
        raise ValueError(f"duplicate IDs in {base_path}")
    if submission.isna().any().any():
        raise ValueError(f"missing values in {base_path}")
    if not set(submission[TARGET]).issubset(LABELS):
        raise ValueError(f"unknown labels in {base_path}")

    overrides = parse_overrides(args.override)
    indexed = submission.set_index(ID_COL)
    missing = sorted(set(overrides) - set(indexed.index))
    if missing:
        raise ValueError(f"override IDs not found in base: {missing}")

    before = indexed.loc[list(overrides), TARGET].copy()
    for row_id, label in overrides.items():
        indexed.loc[row_id, TARGET] = label
    submission = indexed.reset_index()
    changed = int((before != indexed.loc[list(overrides), TARGET]).sum())

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / f"{args.name}.csv"
    json_path = output_dir / f"{args.name}.json"
    submission.to_csv(csv_path, index=False)

    metadata = {
        "name": args.name,
        "source_file": str(base_path),
        "overrides": {str(row_id): label for row_id, label in overrides.items()},
        "changed_rows": changed,
        "test_label_counts": submission[TARGET].value_counts().to_dict(),
        "submission_path": str(csv_path),
    }
    json_path.write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
