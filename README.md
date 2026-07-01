# Predicting Student Health Risk

This repository contains code and experiment notes for Kaggle Playground Series S6E7, Predicting Student Health Risk.

Competition: https://www.kaggle.com/competitions/playground-series-s6e7

## Task

Predict the `health_condition` label for each student:

- `at-risk`
- `fit`
- `unhealthy`

The evaluation metric is balanced accuracy, so minority-class recall matters as much as majority-class recall.

## Data

The competition provides `train.csv`, `test.csv`, and `sample_submission.csv` through Kaggle. Raw competition files are not stored in this repository.

To download the data locally:

```bash
bash scripts/download_data.sh
```

## Training

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run a model experiment:

```bash
python scripts/run_experiment.py --preset xgb_te --folds 5 --seed 42
```

Build a submission from saved probability files:

```bash
python scripts/make_submission.py --runs runs/xgb_te_seed42_f5 --name xgb_te_seed42
```

## Results

Experiment outcomes are tracked in [reports/results_summary.md](reports/results_summary.md).
