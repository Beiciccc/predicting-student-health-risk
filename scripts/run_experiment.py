#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
from catboost import CatBoostClassifier, Pool
from catstat import TargetEncoder
from lightgbm import LGBMClassifier, early_stopping
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from student_health_risk.io import ID_COL, TARGET, categorical_columns, feature_columns, load_competition_data
from student_health_risk.metrics import label_counts, tune_prior_beta


PRESETS = {
    "xgb_te": {
        "family": "xgb_te",
        "params": {
            "objective": "multi:softprob",
            "eval_metric": "mlogloss",
            "tree_method": "hist",
            "n_estimators": 1600,
            "learning_rate": 0.05,
            "max_depth": 6,
            "min_child_weight": 1.0,
            "subsample": 0.80,
            "colsample_bytree": 0.80,
            "gamma": 0.0,
            "reg_lambda": 1.0,
            "early_stopping_rounds": 60,
        },
    },
    "xgb_te_depth4": {
        "family": "xgb_te",
        "params": {
            "objective": "multi:softprob",
            "eval_metric": "mlogloss",
            "tree_method": "hist",
            "n_estimators": 1800,
            "learning_rate": 0.04,
            "max_depth": 4,
            "min_child_weight": 2.0,
            "subsample": 0.85,
            "colsample_bytree": 0.90,
            "gamma": 0.0,
            "reg_lambda": 1.5,
            "early_stopping_rounds": 70,
        },
    },
    "xgb_native": {
        "family": "xgb_native",
        "params": {
            "objective": "multi:softprob",
            "eval_metric": "mlogloss",
            "tree_method": "hist",
            "enable_categorical": True,
            "n_estimators": 900,
            "learning_rate": 0.05,
            "max_depth": 6,
            "min_child_weight": 1.0,
            "subsample": 0.85,
            "colsample_bytree": 0.85,
            "reg_lambda": 1.0,
            "early_stopping_rounds": 50,
        },
    },
    "lgbm": {
        "family": "lgbm",
        "params": {
            "objective": "multiclass",
            "n_estimators": 1200,
            "learning_rate": 0.05,
            "num_leaves": 64,
            "min_child_samples": 40,
            "subsample": 0.85,
            "colsample_bytree": 0.85,
            "reg_lambda": 1.0,
            "n_jobs": -1,
            "verbosity": -1,
        },
    },
    "catboost": {
        "family": "catboost",
        "params": {
            "loss_function": "MultiClass",
            "eval_metric": "MultiClass",
            "iterations": 1200,
            "learning_rate": 0.05,
            "depth": 6,
            "l2_leaf_reg": 3.0,
            "random_strength": 0.5,
            "od_type": "Iter",
            "od_wait": 80,
            "verbose": False,
            "allow_writing_files": False,
        },
    },
}


class TargetEncodedXGB:
    def __init__(self, params: dict, seed: int, classes: np.ndarray):
        self.params = params
        self.seed = seed
        self.classes_ = classes

    def _compose(self, X: pd.DataFrame, encoded: np.ndarray) -> np.ndarray:
        X = X.reset_index(drop=True)
        numeric = X[self.num_cols_].to_numpy(dtype=float)
        return np.hstack([numeric, encoded])

    def _encode(self, X: pd.DataFrame, fit: bool = False, y: np.ndarray | None = None) -> np.ndarray:
        X_cat = X[self.cat_cols_].reset_index(drop=True)
        if fit:
            out = self.encoder_.fit_transform(X_cat, y)
        else:
            out = self.encoder_.transform(X_cat)
        return np.asarray(out, dtype=float)

    def fit(
        self,
        X_train: pd.DataFrame,
        y_train: np.ndarray,
        X_valid: pd.DataFrame,
        y_valid: np.ndarray,
    ) -> "TargetEncodedXGB":
        self.cat_cols_ = categorical_columns(X_train)
        self.num_cols_ = [c for c in X_train.columns if c not in self.cat_cols_]
        self.encoder_ = TargetEncoder(
            cols=self.cat_cols_,
            target_type="multiclass",
            smooth="auto",
            random_state=self.seed,
        )
        xtr = self._compose(X_train, self._encode(X_train, fit=True, y=y_train))
        xva = self._compose(X_valid, self._encode(X_valid))
        self.model_ = XGBClassifier(**self.params, random_state=self.seed, n_jobs=-1)
        self.model_.fit(xtr, y_train, eval_set=[(xva, y_valid)], verbose=False)
        return self

    def predict_proba(self, X: pd.DataFrame) -> np.ndarray:
        return self.model_.predict_proba(self._compose(X, self._encode(X)))


def prepare_features(train: pd.DataFrame, test: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    cols = feature_columns(train)
    X = train[cols].copy()
    X_test = test[cols].copy()
    return X, X_test


def fit_predict_fold(
    family: str,
    params: dict,
    X_train: pd.DataFrame,
    y_train: np.ndarray,
    X_valid: pd.DataFrame,
    y_valid: np.ndarray,
    X_test: pd.DataFrame,
    seed: int,
    classes: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    if family == "xgb_te":
        model = TargetEncodedXGB(params=params, seed=seed, classes=classes)
        model.fit(X_train, y_train, X_valid, y_valid)
        return model.predict_proba(X_valid), model.predict_proba(X_test)

    if family == "xgb_native":
        train_part = X_train.copy()
        valid_part = X_valid.copy()
        test_part = X_test.copy()
        for col in categorical_columns(train_part):
            categories = pd.Index(pd.concat([train_part[col], valid_part[col], test_part[col]], ignore_index=True).dropna().unique())
            dtype = pd.CategoricalDtype(categories=categories)
            train_part[col] = train_part[col].astype(dtype)
            valid_part[col] = valid_part[col].astype(dtype)
            test_part[col] = test_part[col].astype(dtype)
        model = XGBClassifier(**params, random_state=seed, n_jobs=-1)
        model.fit(train_part, y_train, eval_set=[(valid_part, y_valid)], verbose=False)
        return model.predict_proba(valid_part), model.predict_proba(test_part)

    if family == "lgbm":
        train_part = X_train.copy()
        valid_part = X_valid.copy()
        test_part = X_test.copy()
        cat_cols = categorical_columns(train_part)
        for col in cat_cols:
            categories = pd.Index(pd.concat([train_part[col], valid_part[col], test_part[col]], ignore_index=True).dropna().unique())
            dtype = pd.CategoricalDtype(categories=categories)
            train_part[col] = train_part[col].astype(dtype)
            valid_part[col] = valid_part[col].astype(dtype)
            test_part[col] = test_part[col].astype(dtype)
        model = LGBMClassifier(**params, random_state=seed)
        model.fit(
            train_part,
            y_train,
            eval_set=[(valid_part, y_valid)],
            categorical_feature=cat_cols,
            callbacks=[early_stopping(60, verbose=False)],
        )
        return model.predict_proba(valid_part), model.predict_proba(test_part)

    if family == "catboost":
        train_part = X_train.copy()
        valid_part = X_valid.copy()
        test_part = X_test.copy()
        cat_cols = categorical_columns(train_part)
        for col in cat_cols:
            train_part[col] = train_part[col].astype("string").fillna("__MISSING__")
            valid_part[col] = valid_part[col].astype("string").fillna("__MISSING__")
            test_part[col] = test_part[col].astype("string").fillna("__MISSING__")
        cat_idx = [train_part.columns.get_loc(c) for c in cat_cols]
        model = CatBoostClassifier(**params, random_seed=seed)
        model.fit(
            Pool(train_part, y_train, cat_features=cat_idx),
            eval_set=Pool(valid_part, y_valid, cat_features=cat_idx),
            use_best_model=True,
        )
        return model.predict_proba(valid_part), model.predict_proba(test_part)

    raise ValueError(f"Unknown family: {family}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preset", choices=sorted(PRESETS), default="xgb_te")
    parser.add_argument("--input-dir", default="input")
    parser.add_argument("--output-dir", default="runs")
    parser.add_argument("--folds", type=int, default=5)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--sample", type=int, default=0, help="Optional stratified sample size for quick checks.")
    args = parser.parse_args()

    started = time.time()
    train, test, _ = load_competition_data(args.input_dir)
    if args.sample:
        train = (
            train.groupby(TARGET, group_keys=False)
            .apply(lambda x: x.sample(max(1, round(args.sample * len(x) / len(train))), random_state=args.seed))
            .sample(frac=1.0, random_state=args.seed)
            .reset_index(drop=True)
        )

    X, X_test = prepare_features(train, test)
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(train[TARGET])
    classes = label_encoder.classes_
    y_labels = train[TARGET].to_numpy()
    prior = pd.Series(y_labels).value_counts(normalize=True).reindex(classes).to_numpy()

    preset = PRESETS[args.preset]
    family = preset["family"]
    params = dict(preset["params"])

    run_id = f"{args.preset}_seed{args.seed}_f{args.folds}"
    if args.sample:
        run_id += f"_sample{args.sample}"
    run_dir = Path(args.output_dir) / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    skf = StratifiedKFold(n_splits=args.folds, shuffle=True, random_state=args.seed)
    oof = np.zeros((len(train), len(classes)), dtype=float)
    test_proba = np.zeros((len(test), len(classes)), dtype=float)
    fold_scores = []

    for fold, (tr_idx, va_idx) in enumerate(skf.split(X, y), start=1):
        fold_start = time.time()
        va_proba, te_proba = fit_predict_fold(
            family=family,
            params=params,
            X_train=X.iloc[tr_idx],
            y_train=y[tr_idx],
            X_valid=X.iloc[va_idx],
            y_valid=y[va_idx],
            X_test=X_test,
            seed=args.seed + fold - 1,
            classes=classes,
        )
        oof[va_idx] = va_proba
        test_proba += te_proba / args.folds
        raw_pred = classes[va_proba.argmax(axis=1)]
        fold_score = balanced_accuracy_score(y_labels[va_idx], raw_pred)
        fold_scores.append(float(fold_score))
        print(json.dumps({"fold": fold, "raw_balanced_accuracy": fold_score, "seconds": round(time.time() - fold_start, 2)}))

    raw_pred = classes[oof.argmax(axis=1)]
    raw_score = balanced_accuracy_score(y_labels, raw_pred)
    best_beta, calibrated_score, beta_scores = tune_prior_beta(oof, y_labels, classes, prior)
    calibrated_pred = classes[(oof / np.power(prior, best_beta)).argmax(axis=1)]

    oof_df = pd.DataFrame(oof, columns=classes)
    oof_df.insert(0, TARGET, y_labels)
    oof_df.insert(0, ID_COL, train[ID_COL].to_numpy())
    oof_df.to_csv(run_dir / "oof_probs.csv", index=False)

    test_df = pd.DataFrame(test_proba, columns=classes)
    test_df.insert(0, ID_COL, test[ID_COL].to_numpy())
    test_df.to_csv(run_dir / "test_probs.csv", index=False)

    metrics = {
        "run_id": run_id,
        "preset": args.preset,
        "family": family,
        "seed": args.seed,
        "folds": args.folds,
        "sample": args.sample,
        "classes": classes.tolist(),
        "prior": {str(k): float(v) for k, v in zip(classes, prior)},
        "fold_raw_balanced_accuracy": fold_scores,
        "raw_balanced_accuracy": float(raw_score),
        "best_beta": float(best_beta),
        "calibrated_balanced_accuracy": float(calibrated_score),
        "raw_label_counts": label_counts(raw_pred),
        "calibrated_label_counts": label_counts(calibrated_pred),
        "beta_scores": beta_scores,
        "seconds": round(time.time() - started, 2),
    }
    (run_dir / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
