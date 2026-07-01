from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import balanced_accuracy_score


def _balanced_accuracy_from_indices(y_idx: np.ndarray, pred_idx: np.ndarray, n_classes: int) -> float:
    recalls = []
    for class_idx in range(n_classes):
        mask = y_idx == class_idx
        recalls.append(float(np.mean(pred_idx[mask] == class_idx)))
    return float(np.mean(recalls))


def tune_prior_beta(
    oof_proba: np.ndarray,
    y_true: np.ndarray,
    classes: np.ndarray,
    prior: np.ndarray,
    beta_grid: np.ndarray | None = None,
) -> tuple[float, float, dict[str, float]]:
    if beta_grid is None:
        beta_grid = np.unique(np.r_[0.0, np.linspace(0.60, 1.60, 101), np.linspace(1.65, 2.50, 18)])

    scores: dict[str, float] = {}
    best_beta = 0.0
    best_score = -1.0
    class_to_idx = {label: idx for idx, label in enumerate(classes)}
    y_idx = np.array([class_to_idx[label] for label in y_true], dtype=np.int16)
    for beta in beta_grid:
        pred_idx = (oof_proba / np.power(prior, beta)).argmax(axis=1)
        score = _balanced_accuracy_from_indices(y_idx, pred_idx, len(classes))
        scores[f"{beta:.4f}"] = float(score)
        if score > best_score:
            best_score = float(score)
            best_beta = float(beta)
    return best_beta, best_score, scores


def label_counts(labels: np.ndarray | pd.Series) -> dict[str, int]:
    counts = pd.Series(labels).value_counts().sort_index()
    return {str(k): int(v) for k, v in counts.items()}
