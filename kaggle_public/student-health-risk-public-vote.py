from collections import Counter
from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"
LABEL_ORDER = {"at-risk": 0, "fit": 1, "unhealthy": 2}


SOURCE_CANDIDATES = [
    [
        Path('/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv'),
        Path('external/2026-07-04-public-outputs/danush_95101/submission.csv'),
    ],
    [
        Path('/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv'),
        Path('external/2026-07-04-public-outputs/danush_95101/submission.csv'),
    ],
    [
        Path('/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv'),
        Path('external/2026-07-04-public-outputs/danush_95101/submission.csv'),
    ],
    [
        Path('/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv'),
        Path('external/2026-07-04-public-outputs/danush_95101/submission.csv'),
    ],
    [
        Path('/kaggle/input/ps-s6e7-0-95095-hill-climbing-meta-modeling/submission.csv'),
        Path('external/anhad-hill-output/submission.csv'),
        Path('submissions/s020_anhad_hill_meta.csv'),
    ],
    [
        Path('/kaggle/input/confidence-weighted-ensemble-with-score-0-95094/submission.csv'),
        Path('external/anhad-confidence-output/submission.csv'),
        Path('submissions/s022_anhad_confidence.csv'),
    ],
    [
        Path('/kaggle/input/predicting-student-health-risk-submissions/0.95086.csv'),
        Path('external/anhad-student-health-submissions/0.95086.csv'),
        Path('submissions/s023_anhad_single_95086.csv'),
    ],
    [
        Path('/kaggle/input/health-field-trials-pipeline-0-95/blended/external_lb_logit_multiplier_blend.csv'),
        Path('external/2026-07-04-public-outputs/flexon_field_trials/blended/external_lb_logit_multiplier_blend.csv'),
    ],
    [
        Path('/kaggle/input/health-field-trials-pipeline-0-95/blended/external_hygiene_weighted_vote.csv'),
        Path('external/2026-07-04-public-outputs/flexon_field_trials/blended/external_hygiene_weighted_vote.csv'),
        Path('submissions/s065_flexon_hygiene_vote.csv'),
    ]
]


def resolve_source(candidates: list[Path]) -> Path:
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"none of these source files were found: {[str(path) for path in candidates]}")


def choose_label(labels: list[str]) -> str:
    counts = Counter(labels)
    return sorted(counts.items(), key=lambda item: (item[1], -LABEL_ORDER[item[0]]), reverse=True)[0][0]


def main() -> None:
    files = [resolve_source(candidates) for candidates in SOURCE_CANDIDATES]
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
        print(f"- {path}")
    print(submission[TARGET].value_counts().sort_index())


if __name__ == "__main__":
    main()
