#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from student_health_risk.io import ID_COL, TARGET, load_competition_data
from student_health_risk.metrics import label_counts


LABEL_ORDER = {"at-risk": 0, "fit": 1, "unhealthy": 2}


def choose_label(labels: list[str]) -> str:
    counts = Counter(labels)
    return sorted(counts.items(), key=lambda kv: (kv[1], -LABEL_ORDER[kv[0]]), reverse=True)[0][0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--input-dir", default="input")
    parser.add_argument("--output-dir", default="submissions")
    args = parser.parse_args()

    _, _, sample = load_competition_data(args.input_dir)
    frames = []
    for raw_path in args.files:
        path = Path(raw_path)
        df = pd.read_csv(path)
        if list(df.columns) != [ID_COL, TARGET]:
            raise ValueError(f"{path} has invalid columns: {list(df.columns)}")
        if len(df) != len(sample):
            raise ValueError(f"{path} has {len(df)} rows, expected {len(sample)}")
        if not df[ID_COL].equals(sample[ID_COL]):
            raise ValueError(f"{path} ids do not match sample_submission")
        frames.append(df[TARGET].astype(str))

    vote_df = pd.concat(frames, axis=1)
    labels = vote_df.apply(lambda row: choose_label(row.tolist()), axis=1)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_csv = output_dir / f"{args.name}.csv"
    out_json = output_dir / f"{args.name}.json"

    submission = sample.copy()
    submission[TARGET] = labels
    submission.to_csv(out_csv, index=False)

    info = {
        "name": args.name,
        "source_files": [str(Path(p)) for p in args.files],
        "vote_count": len(args.files),
        "test_label_counts": label_counts(labels),
        "submission_path": str(out_csv),
    }
    out_json.write_text(json.dumps(info, indent=2) + "\n")
    print(json.dumps(info, indent=2))


if __name__ == "__main__":
    main()
