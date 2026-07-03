from collections import Counter
from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"
LABEL_ORDER = {"at-risk": 0, "fit": 1, "unhealthy": 2}
EXCLUDED = {"submission_1.csv", "submission_8.csv"}


def find_public_submission_files() -> list[Path]:
    roots = [
        Path("/kaggle/input/public-notebooks-submissions"),
        Path("external/public-notebooks-submissions"),
    ]
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(sorted(path for path in root.glob("submission_*.csv") if path.name not in EXCLUDED))
    if not files:
        files.extend(
            sorted(
                path
                for path in Path("/kaggle/input").glob("**/submission_*.csv")
                if path.name not in EXCLUDED
            )
        )
    if len(files) != 7:
        raise FileNotFoundError(f"expected 7 public submission files, found {len(files)}")
    return files


def choose_label(labels: list[str]) -> str:
    counts = Counter(labels)
    return sorted(counts.items(), key=lambda item: (item[1], -LABEL_ORDER[item[0]]), reverse=True)[0][0]


def main() -> None:
    files = find_public_submission_files()
    frames = [pd.read_csv(path) for path in files]
    ids = frames[0][ID_COL]
    for path, frame in zip(files, frames, strict=True):
        if list(frame.columns) != [ID_COL, TARGET]:
            raise ValueError(f"unexpected columns in {path}: {list(frame.columns)}")
        if not frame[ID_COL].equals(ids):
            raise ValueError(f"id order mismatch in {path}")
        unknown = sorted(set(frame[TARGET]) - set(LABEL_ORDER))
        if unknown:
            raise ValueError(f"unknown labels in {path}: {unknown}")

    votes = pd.concat([frame[TARGET].astype(str) for frame in frames], axis=1)
    submission = frames[0][[ID_COL]].copy()
    submission[TARGET] = votes.apply(lambda row: choose_label(row.tolist()), axis=1)
    submission.to_csv("submission.csv", index=False)

    print("Used files:")
    for path in files:
        print(f"- {path.name}")
    print(submission[TARGET].value_counts().sort_index())


if __name__ == "__main__":
    main()
