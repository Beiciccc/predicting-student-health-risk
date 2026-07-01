# Results Summary

Balanced accuracy is the competition metric. Local CV is computed from out-of-fold predictions.

| # | Submitted (UTC) | Ref | Name | Public score | Local CV | Beta | Method | Notes |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | 2026-07-01 04:01:18 | 54220164 | s001_xgb_te_beta106 | 0.94992 | 0.949800 | 1.0600 | XGBoost target encoding, prior beta 1.06 | First calibrated XGBoost target-encoding run |
| 2 | 2026-07-01 04:03:41 | 54220213 | s002_xgb_te_beta100 | 0.94970 | 0.949795 | 1.0000 | XGBoost target encoding, prior beta 1.00 | Uniform-prior boundary check |
