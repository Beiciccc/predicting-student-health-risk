#!/usr/bin/env python
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLIC_DIR = REPO_ROOT / "kaggle_public"
CODE_FILE = PUBLIC_DIR / "student-health-risk-public-vote.py"
METADATA_FILE = PUBLIC_DIR / "kernel-metadata.json"


SOURCE_MAP = {
    "s020_anhad_hill_meta.csv": {
        "paths": [
            "/kaggle/input/ps-s6e7-0-95095-hill-climbing-meta-modeling/submission.csv",
            "external/anhad-hill-output/submission.csv",
            "submissions/s020_anhad_hill_meta.csv",
        ],
        "kernel": "anhadmahajan06/ps-s6e7-0-95095-hill-climbing-meta-modeling",
    },
    "s022_anhad_confidence.csv": {
        "paths": [
            "/kaggle/input/confidence-weighted-ensemble-with-score-0-95094/submission.csv",
            "external/anhad-confidence-output/submission.csv",
            "submissions/s022_anhad_confidence.csv",
        ],
        "kernel": "anhadmahajan06/confidence-weighted-ensemble-with-score-0-95094",
    },
    "s023_anhad_single_95086.csv": {
        "paths": [
            "/kaggle/input/predicting-student-health-risk-submissions/0.95086.csv",
            "external/anhad-student-health-submissions/0.95086.csv",
            "submissions/s023_anhad_single_95086.csv",
        ],
        "dataset": "anhadmahajan06/predicting-student-health-risk-submissions",
    },
    "s021_anhad_autonomous.csv": {
        "paths": [
            "/kaggle/input/ps-s6e7-autonomous-ensemble/submission.csv",
            "external/anhad-auto-output/submission.csv",
            "submissions/s021_anhad_autonomous.csv",
        ],
        "kernel": "anhadmahajan06/ps-s6e7-autonomous-ensemble",
    },
    "s024_public_95075.csv": {
        "paths": [
            "/kaggle/input/predicting-student-health-risk-submissions/0.95075.csv",
            "external/anhad-student-health-submissions/0.95075.csv",
            "submissions/s024_public_95075.csv",
        ],
        "dataset": "anhadmahajan06/predicting-student-health-risk-submissions",
    },
    "s032_baseer_catboost_tuned.csv": {
        "paths": [
            "/kaggle/input/pss6e7-stacker/sub_catboost_tuned_0.95009.csv",
            "external/jul4-public-outputs/baseer_stacker/sub_catboost_tuned_0.95009.csv",
            "submissions/s032_baseer_catboost_tuned.csv",
        ],
        "kernel": "baseershah/pss6e7-stacker",
    },
    "s033_baseer_catboost_untuned.csv": {
        "paths": [
            "/kaggle/input/pss6e7-stacker/sub_catboost_untuned_0.95001.csv",
            "external/jul4-public-outputs/baseer_stacker/sub_catboost_untuned_0.95001.csv",
            "submissions/s033_baseer_catboost_untuned.csv",
        ],
        "kernel": "baseershah/pss6e7-stacker",
    },
    "s031_pavlo_logodds.csv": {
        "paths": [
            "/kaggle/input/log-odds-ensemble-lb-guided-calibration/submission.csv",
            "external/jul4-public-outputs/pavlo_logodds/submission.csv",
            "submissions/s031_pavlo_logodds.csv",
        ],
        "kernel": "pavloivanin/log-odds-ensemble-lb-guided-calibration",
    },
    "s030_masaya_logreg_stack.csv": {
        "paths": [
            "/kaggle/input/s6e7-logreg-stacker-cv-0-95052/submission.csv",
            "external/jul4-public-outputs/masaya_logreg/submission.csv",
            "submissions/s030_masaya_logreg_stack.csv",
        ],
        "kernel": "masayakawamata/s6e7-logreg-stacker-cv-0-95052",
    },
    "danush_95101_submission.csv": {
        "paths": [
            "/kaggle/input/ps-s6e7-cross-family-ensemble-calibration/submission.csv",
            "external/2026-07-04-public-outputs/danush_95101/submission.csv",
        ],
        "kernel": "danushkumarv/ps-s6e7-cross-family-ensemble-calibration",
    },
    "biohack_fusion_submission.csv": {
        "paths": [
            "/kaggle/input/predict-health-student-fusion/submission.csv",
            "external/2026-07-04-public-outputs/biohack_fusion/submission.csv",
        ],
        "kernel": "biohack44/predict-health-student-fusion",
    },
    "ravi_stacker_submission.csv": {
        "paths": [
            "/kaggle/input/playgrounds6e7-stacker-v1/submission.csv",
            "external/2026-07-04-public-outputs/ravi_stacker/submission.csv",
        ],
        "kernel": "ravi20076/playgrounds6e7-stacker-v1",
    },
    "flexon_submission.csv": {
        "paths": [
            "/kaggle/input/health-field-trials-pipeline-0-95/submission.csv",
            "external/2026-07-04-public-outputs/flexon_field_trials/submission.csv",
        ],
        "kernel": "flexonafft/health-field-trials-pipeline-0-95",
    },
    "external_lb_logit_multiplier_blend.csv": {
        "paths": [
            "/kaggle/input/health-field-trials-pipeline-0-95/blended/external_lb_logit_multiplier_blend.csv",
            "external/2026-07-04-public-outputs/flexon_field_trials/blended/external_lb_logit_multiplier_blend.csv",
        ],
        "kernel": "flexonafft/health-field-trials-pipeline-0-95",
    },
    "external_hygiene_weighted_vote.csv": {
        "paths": [
            "/kaggle/input/health-field-trials-pipeline-0-95/blended/external_hygiene_weighted_vote.csv",
            "external/2026-07-04-public-outputs/flexon_field_trials/blended/external_hygiene_weighted_vote.csv",
            "submissions/s065_flexon_hygiene_vote.csv",
        ],
        "kernel": "flexonafft/health-field-trials-pipeline-0-95",
    },
    "s064_biohack_fusion.csv": {
        "paths": [
            "/kaggle/input/predict-health-student-fusion/submission.csv",
            "external/2026-07-04-public-outputs/biohack_fusion/submission.csv",
            "submissions/s064_biohack_fusion.csv",
        ],
        "kernel": "biohack44/predict-health-student-fusion",
    },
    "s065_flexon_hygiene_vote.csv": {
        "paths": [
            "/kaggle/input/health-field-trials-pipeline-0-95/blended/external_hygiene_weighted_vote.csv",
            "external/2026-07-04-public-outputs/flexon_field_trials/blended/external_hygiene_weighted_vote.csv",
            "submissions/s065_flexon_hygiene_vote.csv",
        ],
        "kernel": "flexonafft/health-field-trials-pipeline-0-95",
    },
    "s066_ravi_stacker.csv": {
        "paths": [
            "/kaggle/input/playgrounds6e7-stacker-v1/submission.csv",
            "external/2026-07-04-public-outputs/ravi_stacker/submission.csv",
            "submissions/s066_ravi_stacker.csv",
        ],
        "kernel": "ravi20076/playgrounds6e7-stacker-v1",
    },
}


def unique(items: list[str]) -> list[str]:
    seen = set()
    output = []
    for item in items:
        if item and item not in seen:
            seen.add(item)
            output.append(item)
    return output


def source_entry(raw_path: str) -> dict[str, object]:
    path = Path(raw_path)
    if "danush_95101/submission.csv" in raw_path:
        key = "danush_95101_submission.csv"
    elif "biohack_fusion/submission.csv" in raw_path:
        key = "biohack_fusion_submission.csv"
    elif "ravi_stacker/submission.csv" in raw_path:
        key = "ravi_stacker_submission.csv"
    elif "flexon_field_trials/submission.csv" in raw_path:
        key = "flexon_submission.csv"
    else:
        key = path.name
    if key not in SOURCE_MAP:
        raise KeyError(f"no public source mapping for {raw_path}")
    entry = dict(SOURCE_MAP[key])
    entry["local_path"] = raw_path
    paths = list(entry["paths"])
    if raw_path not in paths:
        paths.append(raw_path)
    entry["paths"] = paths
    return entry


def render_code(entries: list[dict[str, object]]) -> str:
    rendered_sources = []
    for entry in entries:
        paths = ",\n        ".join(f"Path({path!r})" for path in entry["paths"])
        rendered_sources.append(f"    [\n        {paths},\n    ]")
    source_text = ",\n".join(rendered_sources)
    return f"""from collections import Counter
from pathlib import Path

import pandas as pd


TARGET = "health_condition"
ID_COL = "id"
LABEL_ORDER = {{"at-risk": 0, "fit": 1, "unhealthy": 2}}


SOURCE_CANDIDATES = [
{source_text}
]


def resolve_source(candidates: list[Path]) -> Path:
    for path in candidates:
        if path.exists():
            return path
    raise FileNotFoundError(f"none of these source files were found: {{[str(path) for path in candidates]}}")


def choose_label(labels: list[str]) -> str:
    counts = Counter(labels)
    return sorted(counts.items(), key=lambda item: (item[1], -LABEL_ORDER[item[0]]), reverse=True)[0][0]


def main() -> None:
    files = [resolve_source(candidates) for candidates in SOURCE_CANDIDATES]
    frames = [pd.read_csv(path) for path in files]
    ids = frames[0][ID_COL]
    for path, frame in zip(files, frames, strict=True):
        if list(frame.columns) != [ID_COL, TARGET]:
            raise ValueError(f"unexpected columns in {{path}}: {{list(frame.columns)}}")
        if not frame[ID_COL].equals(ids):
            raise ValueError(f"id order mismatch in {{path}}")
        unknown = sorted(set(frame[TARGET]) - set(LABEL_ORDER))
        if unknown:
            raise ValueError(f"unknown labels in {{path}}: {{unknown}}")

    votes = pd.concat([frame[TARGET].astype(str) for frame in frames], axis=1)
    submission = frames[0][[ID_COL]].copy()
    submission[TARGET] = votes.apply(lambda row: choose_label(row.tolist()), axis=1)
    submission.to_csv("submission.csv", index=False)

    print("Used files:")
    for path in files:
        print(f"- {{path}}")
    print(submission[TARGET].value_counts().sort_index())


if __name__ == "__main__":
    main()
"""


def render_metadata(entries: list[dict[str, object]]) -> str:
    metadata = {
        "id": "beicicc/student-health-risk-public-ensemble",
        "title": "Student Health Risk Public Ensemble",
        "code_file": "student-health-risk-public-vote.py",
        "language": "python",
        "kernel_type": "script",
        "is_private": False,
        "enable_gpu": False,
        "enable_tpu": False,
        "enable_internet": False,
        "dataset_sources": unique([str(entry.get("dataset", "")) for entry in entries]),
        "kernel_sources": unique([str(entry.get("kernel", "")) for entry in entries]),
        "competition_sources": ["playground-series-s6e7"],
    }
    return json.dumps(metadata, indent=2) + "\n"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-json", required=True)
    parser.add_argument("--candidate-csv", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    candidate = json.loads(Path(args.candidate_json).read_text())
    source_files = candidate.get("source_files") or [candidate.get("source_file", "")]
    if not source_files or not source_files[0]:
        raise ValueError("candidate JSON must contain source_files or source_file")

    entries = [source_entry(str(path)) for path in source_files]
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    CODE_FILE.write_text(render_code(entries))
    METADATA_FILE.write_text(render_metadata(entries))

    if args.check:
        output = REPO_ROOT / "submission.csv"
        if output.exists():
            output.unlink()
        subprocess.run([sys.executable, str(CODE_FILE)], cwd=REPO_ROOT, check=True)
        expected = sha256(Path(args.candidate_csv))
        observed = sha256(output)
        print(json.dumps({"expected_sha256": expected, "observed_sha256": observed}, indent=2))
        if expected != observed:
            raise SystemExit("generated submission does not match candidate")
        output.unlink()


if __name__ == "__main__":
    main()
