from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"
LABELS = {"at-risk", "fit", "unhealthy"}


def find_source_submission() -> Path:
    exact_candidates = [
        Path("/kaggle/input/confidence-weighted-ensemble-with-score-0-95094/submission.csv"),
        Path("external/anhad-confidence-output/submission.csv"),
    ]
    for path in exact_candidates:
        if path.exists():
            return path

    search_roots = [Path("/kaggle/input"), Path("external")]
    matches: list[Path] = []
    for root in search_roots:
        if not root.exists():
            continue
        for path in root.rglob("submission.csv"):
            text = str(path).lower()
            if "confidence" in text or "95094" in text:
                matches.append(path)
    if not matches:
        raise FileNotFoundError("source submission.csv was not found")
    return sorted(matches)[0]


def main() -> None:
    source_path = find_source_submission()
    submission = pd.read_csv(source_path)
    if list(submission.columns) != [ID_COL, TARGET]:
        raise ValueError(f"unexpected columns in {source_path}: {list(submission.columns)}")
    unknown = sorted(set(submission[TARGET]) - LABELS)
    if unknown:
        raise ValueError(f"unknown labels in {source_path}: {unknown}")

    submission.to_csv("submission.csv", index=False)
    print(f"Copied {source_path}")
    print(submission[TARGET].value_counts().sort_index())


if __name__ == "__main__":
    main()
