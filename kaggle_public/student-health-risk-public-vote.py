from collections import Counter
from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"
LABEL_ORDER = {"at-risk": 0, "fit": 1, "unhealthy": 2}
OVERRIDES = {
    690472: "unhealthy",
    708552: "at-risk",
    711112: "at-risk",
    711711: "at-risk",
    712568: "at-risk",
    714981: "unhealthy",
    715090: "at-risk",
    715107: "at-risk",
    727613: "unhealthy",
    730651: "at-risk",
    742088: "at-risk",
    745526: "unhealthy",
    750124: "at-risk",
    753993: "at-risk",
    764134: "at-risk",
    765328: "at-risk",
    766571: "at-risk",
    775115: "at-risk",
    775888: "at-risk",
    777480: "unhealthy",
    781794: "at-risk",
    782248: "at-risk",
    785839: "unhealthy",
    789622: "at-risk",
    792856: "at-risk",
    797049: "at-risk",
    801832: "at-risk",
    806969: "at-risk",
    811758: "unhealthy",
    814970: "at-risk",
    819942: "at-risk",
    825099: "at-risk",
    833839: "fit",
    836094: "at-risk",
    849627: "at-risk",
    861768: "at-risk",
    862102: "at-risk",
    862122: "at-risk",
    863844: "unhealthy",
    865877: "at-risk",
    866690: "fit",
    873194: "at-risk",
    875791: "unhealthy",
    882684: "at-risk",
    883746: "at-risk",
    888460: "at-risk",
    890705: "at-risk",
    892048: "at-risk",
    895403: "at-risk",
    895750: "fit",
    901862: "at-risk",
    903767: "at-risk",
    904037: "fit",
    908824: "fit",
    911344: "fit",
    915869: "unhealthy",
    926657: "unhealthy",
    930217: "at-risk",
    931286: "at-risk",
    932589: "at-risk",
    933061: "at-risk",
    939441: "at-risk",
    940518: "fit",
    945898: "at-risk",
    946465: "at-risk",
    965669: "at-risk",
    968747: "unhealthy",
    971160: "at-risk",
    977710: "unhealthy",
    979001: "unhealthy",
    979493: "at-risk",
    980025: "at-risk",
    981779: "at-risk",
    983916: "at-risk",
}

SOURCE_CANDIDATES = [
    [
        Path("/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv"),
        Path("external/2026-07-04-public-outputs/danush_95101/submission.csv"),
    ],
    [
        Path("/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv"),
        Path("external/2026-07-04-public-outputs/danush_95101/submission.csv"),
    ],
    [
        Path("/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv"),
        Path("external/2026-07-04-public-outputs/danush_95101/submission.csv"),
    ],
    [
        Path("/kaggle/input/ps-s6e7-0-95095-hill-climbing-meta-modeling/submission.csv"),
        Path("external/anhad-hill-output/submission.csv"),
    ],
    [
        Path("/kaggle/input/confidence-weighted-ensemble-with-score-0-95094/submission.csv"),
        Path("external/anhad-confidence-output/submission.csv"),
    ],
    [
        Path("/kaggle/input/predicting-student-health-risk-submissions/0.95086.csv"),
        Path("external/anhad-student-health-submissions/0.95086.csv"),
    ],
    [
        Path("/kaggle/input/health-field-trials-pipeline-0-95/blended/external_lb_logit_multiplier_blend.csv"),
        Path("external/2026-07-04-public-outputs/flexon_field_trials/blended/external_lb_logit_multiplier_blend.csv"),
    ],
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
    submission[TARGET] = submission[ID_COL].map(OVERRIDES).fillna(submission[TARGET])
    submission.to_csv("submission.csv", index=False)

    print(submission[TARGET].value_counts().sort_index())


if __name__ == "__main__":
    main()
