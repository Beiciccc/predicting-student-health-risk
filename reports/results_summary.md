# Results Summary

Balanced accuracy is the competition metric. Local CV is computed from out-of-fold predictions.

| # | Submitted (UTC) | Ref | Name | Public score | Local CV | Beta | Method | Notes |
|---:|---|---|---|---:|---:|---:|---|---|
| 1 | 2026-07-01 04:01:18 | 54220164 | s001_xgb_te_beta106 | 0.94992 | 0.949800 | 1.0600 | XGBoost target encoding, prior beta 1.06 | First calibrated XGBoost target-encoding run |
| 2 | 2026-07-01 04:03:41 | 54220213 | s002_xgb_te_beta100 | 0.94970 | 0.949795 | 1.0000 | XGBoost target encoding, prior beta 1.00 | Uniform-prior boundary check |
| 3 | 2026-07-01 04:05:25 | 54220253 | s003_xgb_te_beta108 | 0.95001 | 0.949748 | 1.0800 | XGBoost target encoding, prior beta 1.08 | Higher-beta boundary check; best so far |
| 4 | 2026-07-01 04:07:35 | 54220286 | s004_xgb_te_beta110 | 0.94990 | 0.949752 | 1.1000 | XGBoost target encoding, prior beta 1.10 | Higher-beta check; below beta 1.08 |
| 5 | 2026-07-01 04:10:46 | 54220347 | s005_lgbm_beta102 | 0.94939 | 0.949721 | 1.0200 | LightGBM, prior beta 1.02 | Single-model LGBM check; below XGB |
| 6 | 2026-07-01 04:12:02 | 54220364 | s006_xgb_te_beta1085 | 0.94998 | 0.949761 | 1.0850 | XGBoost target encoding, prior beta 1.085 | Fine beta check; below beta 1.08 |
| 7 | 2026-07-01 04:13:12 | 54220393 | s007_blend_xgb80_lgbm20 | 0.94989 | 0.949913 | 1.0200 | XGBoost/LightGBM blend 0.80/0.20 | Blend check; below best single XGB |
| 8 | 2026-07-01 04:14:18 | 54220424 | s008_xgb_te_beta1075 | 0.94991 | 0.949766 | 1.0750 | XGBoost target encoding, prior beta 1.075 | Fine beta check; below beta 1.08 |
| 9 | 2026-07-01 04:15:23 | 54220463 | s009_xgb_te_beta109 | 0.94990 | 0.949739 | 1.0900 | XGBoost target encoding, prior beta 1.09 | Fine beta check; below beta 1.08 |
| 10 | 2026-07-01 04:16:35 | 54220481 | s010_xgb_te_beta1081 | 0.95001 | 0.949745 | 1.0810 | XGBoost target encoding, prior beta 1.081 | Near-best micro perturbation; tied best public score |
| 11 | 2026-07-02 03:06:57 | 54251011 | s011_vote_public_0_4 | 0.95025 |  |  | Five-file hard vote | Public vote baseline |
| 12 | 2026-07-02 03:10:34 | 54251097 | s012_vote_public_0_8 | 0.95034 |  |  | Nine-file hard vote | Full public vote set |
| 13 | 2026-07-02 03:13:29 | 54251168 | s013_vote_public_no7 | 0.95024 |  |  | Eight-file hard vote | Leave-one-out vote check |
| 14 | 2026-07-02 03:16:55 | 54251274 | s014_vote_public_no0 | 0.94987 |  |  | Eight-file hard vote | Leave-one-out vote check |
| 15 | 2026-07-02 03:18:41 | 54251317 | s015_vote_public_no1 | 0.95043 |  |  | Eight-file hard vote | Leave-one-out vote check |
| 16 | 2026-07-02 03:21:23 | 54251364 | s016_vote_public_no2 | 0.95035 |  |  | Eight-file hard vote | Leave-one-out vote check |
| 17 | 2026-07-02 03:24:08 | 54251436 | s017_vote_public_no3 | 0.95040 |  |  | Eight-file hard vote | Leave-one-out vote check |
| 18 | 2026-07-02 03:26:06 | 54251480 | s018_vote_public_no4 | 0.94992 |  |  | Eight-file hard vote | Leave-one-out vote check |
| 19 | 2026-07-02 03:26:07 | 54251505 | s018_vote_public_no4 | 0.94992 |  |  | Eight-file hard vote | Same no4 vote file |
| 20 | 2026-07-02 03:27:57 | 54251545 | s019_vote_public_no5 | 0.95017 |  |  | Eight-file hard vote | Leave-one-out vote check |
| 21 | 2026-07-03 08:39:25 | 54292076 | s020_anhad_hill_meta | 0.95095 |  |  | Public hill meta ensemble | Score-named submission ensemble |
| 22 | 2026-07-03 08:47:02 | 54292311 | s021_anhad_autonomous | 0.95081 |  |  | Public autonomous ensemble | Score-named submission ensemble variant |
