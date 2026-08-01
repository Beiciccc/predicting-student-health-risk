# Predicting Student Health Risk

This repository contains code and experiment notes for Kaggle Playground Series S6E7, Predicting Student Health Risk.

Competition: https://www.kaggle.com/competitions/playground-series-s6e7

## Final Standing

The competition finished on 2026-07-31 at 23:59 UTC.

- Final private leaderboard: **367 of 3,356** (top 10.94%), score **0.95029**
- Public leaderboard: **89 of 3,356** (top 2.65%), score **0.95289**
- Rank change after the private leaderboard reveal: **-278 places**
- Official submissions: **295**
- Final scoring submission: `s448_fit_965778`, ref `55123520`
- Best retrospective private score across all submissions: **0.95048** from `s017_vote_public_no3`

See [reports/final_results.md](reports/final_results.md) for the full post-competition analysis.

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
Official public/private score pairs are available in [reports/final_scores.csv](reports/final_scores.csv).

## Public Code

Kaggle Code version: https://www.kaggle.com/code/beicicc/student-health-risk-public-ensemble

The Kaggle script source is stored in [kaggle_public/student-health-risk-public-vote.py](kaggle_public/student-health-risk-public-vote.py).
