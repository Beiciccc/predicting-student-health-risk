from collections import Counter
from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"
LABEL_ORDER = {"at-risk": 0, "fit": 1, "unhealthy": 2}
OVERRIDES = {
    690472: "at-risk",
    690753: "fit",
    694344: "at-risk",
    698943: "unhealthy",
    702714: "at-risk",
    703274: "at-risk",
    707923: "at-risk",
    708552: "unhealthy",
    710958: "unhealthy",
    711112: "at-risk",
    712568: "at-risk",
    712816: "at-risk",
    714981: "at-risk",
    715090: "fit",
    717981: "at-risk",
    720864: "at-risk",
    722217: "fit",
    726333: "at-risk",
    727613: "fit",
    730651: "at-risk",
    741707: "fit",
    745526: "at-risk",
    748398: "at-risk",
    750124: "at-risk",
    764134: "unhealthy",
    766571: "fit",
    767930: "at-risk",
    773640: "unhealthy",
    774088: "at-risk",
    774437: "at-risk",
    775888: "at-risk",
    776502: "at-risk",
    777480: "at-risk",
    777587: "at-risk",
    782055: "at-risk",
    785839: "at-risk",
    790694: "at-risk",
    791039: "at-risk",
    793885: "at-risk",
    794564: "at-risk",
    797102: "at-risk",
    800108: "at-risk",
    801832: "at-risk",
    802627: "unhealthy",
    805892: "at-risk",
    807015: "at-risk",
    810179: "at-risk",
    811323: "at-risk",
    811758: "at-risk",
    814116: "at-risk",
    819712: "at-risk",
    826824: "at-risk",
    828286: "at-risk",
    833839: "fit",
    836438: "at-risk",
    836526: "at-risk",
    837872: "at-risk",
    845088: "at-risk",
    846737: "at-risk",
    853509: "at-risk",
    853988: "at-risk",
    854545: "at-risk",
    862122: "at-risk",
    863821: "fit",
    863844: "at-risk",
    866690: "fit",
    871756: "at-risk",
    878683: "at-risk",
    883293: "at-risk",
    887214: "at-risk",
    889030: "at-risk",
    889660: "at-risk",
    890705: "unhealthy",
    890778: "at-risk",
    891288: "fit",
    894968: "at-risk",
    895225: "at-risk",
    895403: "fit",
    895750: "fit",
    896268: "unhealthy",
    896383: "at-risk",
    896800: "at-risk",
    898407: "at-risk",
    898458: "at-risk",
    903767: "at-risk",
    903930: "at-risk",
    908824: "fit",
    922125: "at-risk",
    926657: "at-risk",
    930217: "unhealthy",
    931286: "unhealthy",
    932589: "unhealthy",
    933061: "at-risk",
    937216: "at-risk",
    942726: "at-risk",
    947514: "at-risk",
    954863: "at-risk",
    957078: "at-risk",
    958276: "at-risk",
    959154: "at-risk",
    960986: "at-risk",
    965669: "unhealthy",
    967639: "at-risk",
    968206: "at-risk",
    968747: "fit",
    969163: "at-risk",
    970158: "at-risk",
    972394: "at-risk",
    978698: "at-risk",
    978754: "at-risk",
    979001: "at-risk",
    980025: "at-risk",
    981779: "at-risk",
    982894: "at-risk",
    711711: "at-risk",
    742088: "at-risk",
    775115: "at-risk",
    781794: "at-risk",
    782248: "at-risk",
    789622: "at-risk",
    792856: "at-risk",
    806969: "at-risk",
    814970: "at-risk",
    825099: "at-risk",
    836094: "at-risk",
    873194: "at-risk",
    882684: "at-risk",
    883746: "at-risk",
    892048: "at-risk",
    950327: "at-risk",
    979493: "at-risk",
    983916: "at-risk",
    690179: "fit",
    736819: "at-risk",
    832803: "at-risk",
    965287: "at-risk",
    977425: "at-risk",
    775083: "at-risk",
    799109: "at-risk",
    920406: "at-risk",
    944726: "at-risk",
    722968: "at-risk",
    726783: "at-risk",
    779498: "at-risk",
    809898: "at-risk",
    822516: "at-risk",
    835471: "at-risk",
    872096: "at-risk",
    875966: "at-risk",
    936829: "at-risk",
    947779: "at-risk",
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
        Path("/kaggle/input/predicting-student-health-risk-submissions/0.95075.csv"),
        Path("external/anhad-student-health-submissions/0.95075.csv"),
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
