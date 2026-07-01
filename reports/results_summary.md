# Results Summary

Balanced accuracy is the competition metric. Local CV is computed from out-of-fold predictions.

| # | Submitted (UTC) | Ref | Name | Public score | Local CV | Beta | Method | Notes |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | 2026-07-01 04:01:18 | 54220164 | s001_xgb_te_beta106 | 0.94992 | 0.949800 | 1.0600 | XGBoost target encoding, prior beta 1.06 | First calibrated XGBoost target-encoding run |
| 2 | 2026-07-01 04:03:41 | 54220213 | s002_xgb_te_beta100 | 0.94970 | 0.949795 | 1.0000 | XGBoost target encoding, prior beta 1.00 | Uniform-prior boundary check |
| 3 | 2026-07-01 04:05:25 | 54220253 | s003_xgb_te_beta108 | 0.95001 | 0.949748 | 1.0800 | XGBoost target encoding, prior beta 1.08 | Higher-beta boundary check; best so far |
| 4 | 2026-07-01 04:07:35 | 54220286 | s004_xgb_te_beta110 | 0.94990 | 0.949752 | 1.1000 | XGBoost target encoding, prior beta 1.10 | Higher-beta check; below beta 1.08 |
| 5 | 2026-07-01 04:10:46 | 54220347 | s005_lgbm_beta102 | 0.94939 | 0.949721 | 1.0200 | LightGBM, prior beta 1.02 | Single-model LGBM check; below XGB |
