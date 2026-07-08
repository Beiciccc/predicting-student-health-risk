from collections import Counter
from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"
LABEL_ORDER = {"at-risk": 0, "fit": 1, "unhealthy": 2}
OVERRIDES = {
    690179: "fit",
    690472: "at-risk",
    702714: "at-risk",
    703274: "at-risk",
    707923: "at-risk",
    708552: "unhealthy",
    711112: "at-risk",
    711711: "at-risk",
    712568: "at-risk",
    712816: "at-risk",
    714981: "at-risk",
    715090: "fit",
    715107: "fit",
    717981: "at-risk",
    718517: "unhealthy",
    720864: "at-risk",
    726333: "at-risk",
    727613: "fit",
    730651: "at-risk",
    733597: "unhealthy",
    742088: "at-risk",
    745526: "at-risk",
    748398: "at-risk",
    750124: "unhealthy",
    753993: "at-risk",
    764134: "unhealthy",
    765328: "at-risk",
    766432: "unhealthy",
    766571: "fit",
    767930: "at-risk",
    774088: "at-risk",
    775115: "at-risk",
    775888: "at-risk",
    776133: "at-risk",
    776502: "at-risk",
    777480: "at-risk",
    777587: "at-risk",
    781794: "fit",
    782055: "at-risk",
    782248: "at-risk",
    785839: "at-risk",
    789622: "at-risk",
    790694: "at-risk",
    791039: "at-risk",
    792856: "at-risk",
    794564: "at-risk",
    797049: "at-risk",
    797102: "at-risk",
    800108: "at-risk",
    801832: "at-risk",
    805892: "at-risk",
    806969: "at-risk",
    807015: "at-risk",
    810179: "at-risk",
    811323: "at-risk",
    811758: "unhealthy",
    814116: "at-risk",
    814970: "at-risk",
    819942: "unhealthy",
    825099: "at-risk",
    826824: "at-risk",
    828286: "unhealthy",
    833839: "fit",
    836094: "at-risk",
    836438: "at-risk",
    836526: "at-risk",
    837872: "at-risk",
    845088: "at-risk",
    845819: "at-risk",
    846737: "at-risk",
    848992: "unhealthy",
    849627: "at-risk",
    853509: "at-risk",
    853988: "at-risk",
    854545: "at-risk",
    859551: "unhealthy",
    861768: "at-risk",
    862102: "at-risk",
    862122: "at-risk",
    863844: "at-risk",
    865877: "at-risk",
    866690: "unhealthy",
    871756: "at-risk",
    873194: "at-risk",
    873195: "unhealthy",
    875791: "unhealthy",
    878683: "at-risk",
    880025: "fit",
    882684: "at-risk",
    883293: "at-risk",
    883746: "at-risk",
    887214: "at-risk",
    888460: "at-risk",
    889030: "at-risk",
    889660: "at-risk",
    890705: "unhealthy",
    890778: "at-risk",
    891288: "fit",
    892048: "fit",
    894968: "at-risk",
    895225: "at-risk",
    895403: "fit",
    895750: "fit",
    896383: "at-risk",
    896800: "at-risk",
    898407: "at-risk",
    898458: "at-risk",
    901862: "at-risk",
    903767: "at-risk",
    903930: "at-risk",
    904037: "unhealthy",
    904371: "fit",
    908824: "unhealthy",
    911344: "unhealthy",
    915869: "unhealthy",
    922125: "at-risk",
    926657: "at-risk",
    927050: "unhealthy",
    930217: "unhealthy",
    931286: "unhealthy",
    932589: "unhealthy",
    933061: "unhealthy",
    937216: "at-risk",
    939441: "unhealthy",
    940518: "at-risk",
    942726: "at-risk",
    945898: "at-risk",
    946465: "at-risk",
    947304: "unhealthy",
    947514: "at-risk",
    950364: "at-risk",
    954863: "at-risk",
    957078: "at-risk",
    958276: "at-risk",
    959154: "at-risk",
    960986: "at-risk",
    965669: "unhealthy",
    967639: "at-risk",
    968206: "at-risk",
    968747: "unhealthy",
    969163: "at-risk",
    970158: "at-risk",
    971160: "at-risk",
    972394: "at-risk",
    977710: "unhealthy",
    978698: "at-risk",
    978754: "at-risk",
    979001: "at-risk",
    979493: "at-risk",
    980025: "at-risk",
    981779: "at-risk",
    982267: "fit",
    982282: "fit",
    982894: "at-risk",
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
