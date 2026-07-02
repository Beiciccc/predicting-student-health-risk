from collections import Counter
from pathlib import Path

import pandas as pd


LABEL_ORDER = ["at-risk", "fit", "unhealthy"]
TARGET = "health_condition"
ID_COL = "id"
EXCLUDED_PUBLIC_FILE = "submission_1.csv"


def find_sample_submission() -> Path | None:
    candidates = [
        Path("/kaggle/input/playground-series-s6e7/sample_submission.csv"),
        Path("../input/playground-series-s6e7/sample_submission.csv"),
        Path("input/sample_submission.csv"),
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def find_public_submission_files() -> list[Path]:
    roots = [
        Path("/kaggle/input/public-notebooks-submissions"),
        Path("../input/public-notebooks-submissions"),
        Path("external/public-notebooks-submissions"),
    ]
    files: list[Path] = []
    for root in roots:
        if root.exists():
            files.extend(sorted(root.glob("submission_*.csv")))
    if not files:
        files.extend(sorted(Path("/kaggle/input").glob("**/submission_*.csv")))
    selected = [path for path in files if path.name != EXCLUDED_PUBLIC_FILE]
    if len(selected) < 2:
        raise FileNotFoundError("not enough public submission files were found")
    return selected


def read_prediction_file(path: Path, sample: pd.DataFrame) -> pd.Series:
    frame = pd.read_csv(path)
    missing = {ID_COL, TARGET} - set(frame.columns)
    if missing:
        raise ValueError(f"{path} is missing columns: {sorted(missing)}")
    frame = frame[[ID_COL, TARGET]]
    if not frame[ID_COL].equals(sample[ID_COL]):
        frame = sample[[ID_COL]].merge(frame, on=ID_COL, how="left")
    if frame[TARGET].isna().any():
        raise ValueError(f"{path} has missing predictions after id alignment")
    unknown = sorted(set(frame[TARGET]) - set(LABEL_ORDER))
    if unknown:
        raise ValueError(f"{path} has unknown labels: {unknown}")
    return frame[TARGET]


def vote_row(labels: tuple[str, ...]) -> str:
    counts = Counter(labels)
    return min(LABEL_ORDER, key=lambda label: (-counts[label], LABEL_ORDER.index(label)))


def load_template(prediction_files: list[Path]) -> pd.DataFrame:
    sample_path = find_sample_submission()
    if sample_path is not None:
        sample = pd.read_csv(sample_path)
    else:
        sample = pd.read_csv(prediction_files[0])[[ID_COL, TARGET]]
    if list(sample.columns) != [ID_COL, TARGET]:
        raise ValueError(f"unexpected sample columns: {list(sample.columns)}")
    return sample


def main() -> None:
    prediction_files = find_public_submission_files()
    sample = load_template(prediction_files)

    prediction_columns = [
        read_prediction_file(path, sample).rename(path.stem) for path in prediction_files
    ]
    votes = pd.concat(prediction_columns, axis=1)

    submission = sample.copy()
    submission[TARGET] = [vote_row(tuple(row)) for row in votes.itertuples(index=False, name=None)]
    submission.to_csv("submission.csv", index=False)

    print("Used files:")
    for path in prediction_files:
        print(f"- {path.name}")
    print(submission[TARGET].value_counts().sort_index())


if __name__ == "__main__":
    main()
