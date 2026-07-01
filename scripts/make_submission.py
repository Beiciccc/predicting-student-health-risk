#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import balanced_accuracy_score

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from student_health_risk.io import ID_COL, TARGET, load_competition_data
from student_health_risk.metrics import label_counts, tune_prior_beta


def load_probs(run_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    oof = pd.read_csv(run_dir / "oof_probs.csv")
    test = pd.read_csv(run_dir / "test_probs.csv")
    metrics_path = run_dir / "metrics.json"
    metrics = json.loads(metrics_path.read_text()) if metrics_path.exists() else {}
    return oof, test, metrics


def parse_weights(raw: str | None, n: int) -> np.ndarray:
    if raw is None:
        return np.repeat(1.0 / n, n)
    weights = np.array([float(x) for x in raw.split(",")], dtype=float)
    if len(weights) != n:
        raise ValueError(f"Expected {n} weights, got {len(weights)}")
    if weights.sum() <= 0:
        raise ValueError("Weights must sum to a positive value")
    return weights / weights.sum()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", nargs="+", required=True, help="Run directories containing oof_probs.csv and test_probs.csv.")
    parser.add_argument("--weights", default=None, help="Comma-separated blend weights. Defaults to equal weights.")
    parser.add_argument("--beta", default="tune", help="Use 'tune' or a numeric beta value.")
    parser.add_argument("--name", required=True)
    parser.add_argument("--input-dir", default="input")
    parser.add_argument("--output-dir", default="submissions")
    args = parser.parse_args()

    run_dirs = [Path(p) for p in args.runs]
    weights = parse_weights(args.weights, len(run_dirs))
    _, _, sample = load_competition_data(args.input_dir)

    oofs = []
    tests = []
    metrics = []
    for run_dir in run_dirs:
        oof, test, metric = load_probs(run_dir)
        oofs.append(oof)
        tests.append(test)
        metrics.append(metric)

    classes = [c for c in oofs[0].columns if c not in {ID_COL, TARGET}]
    y_true = oofs[0][TARGET].to_numpy()
    ids = oofs[0][ID_COL].to_numpy()
    test_ids = tests[0][ID_COL].to_numpy()
    for oof, test in zip(oofs[1:], tests[1:]):
        if not np.array_equal(ids, oof[ID_COL].to_numpy()):
            raise ValueError("OOF ids are not aligned")
        if not np.array_equal(test_ids, test[ID_COL].to_numpy()):
            raise ValueError("Test ids are not aligned")

    oof_proba = sum(w * df[classes].to_numpy(dtype=float) for w, df in zip(weights, oofs))
    test_proba = sum(w * df[classes].to_numpy(dtype=float) for w, df in zip(weights, tests))

    class_arr = np.array(classes)
    prior = pd.Series(y_true).value_counts(normalize=True).reindex(class_arr).to_numpy()
    raw_pred = class_arr[oof_proba.argmax(axis=1)]
    raw_score = balanced_accuracy_score(y_true, raw_pred)

    if args.beta == "tune":
        beta, cv_score, beta_scores = tune_prior_beta(oof_proba, y_true, class_arr, prior)
    else:
        beta = float(args.beta)
        pred = class_arr[(oof_proba / np.power(prior, beta)).argmax(axis=1)]
        cv_score = float(balanced_accuracy_score(y_true, pred))
        beta_scores = {f"{beta:.4f}": cv_score}

    test_labels = class_arr[(test_proba / np.power(prior, beta)).argmax(axis=1)]
    submission = sample.copy()
    submission[TARGET] = test_labels

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    out_csv = output_dir / f"{args.name}.csv"
    out_json = output_dir / f"{args.name}.json"
    submission.to_csv(out_csv, index=False)

    info = {
        "name": args.name,
        "runs": [str(p) for p in run_dirs],
        "run_ids": [m.get("run_id", str(p)) for m, p in zip(metrics, run_dirs)],
        "weights": weights.tolist(),
        "beta": float(beta),
        "raw_oof_balanced_accuracy": float(raw_score),
        "oof_balanced_accuracy": float(cv_score),
        "test_label_counts": label_counts(test_labels),
        "beta_scores": beta_scores,
        "submission_path": str(out_csv),
    }
    out_json.write_text(json.dumps(info, indent=2) + "\n")
    print(json.dumps(info, indent=2))


if __name__ == "__main__":
    main()
