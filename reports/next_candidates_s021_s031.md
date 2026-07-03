# Next Candidate Batch s021-s031

Date: 2026-07-03

Generation baseline public score: `0.95043` from `submissions/s015_vote_public_no1.csv`.

After `s020_anhad_hill_meta`, the current best public score is `0.95095`.

No Kaggle submissions were made. Files were generated with `scripts/make_vote_submission.py` and written only under `submissions/`.

Note: `submissions/s021_anhad_autonomous.csv` and `.json` were present as a separate concurrent candidate and are not part of this batch.

## Generation Commands

```bash
P=external/public-notebooks-submissions
python scripts/make_vote_submission.py --name s021_vote_public_no8 --files "$P/submission_0.csv" "$P/submission_1.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv"
python scripts/make_vote_submission.py --name s022_vote_public_no1_no3 --files "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv"
python scripts/make_vote_submission.py --name s023_vote_public_no1_no2 --files "$P/submission_0.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv"
python scripts/make_vote_submission.py --name s024_vote_public_no1_no6 --files "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_7.csv" "$P/submission_8.csv"
python scripts/make_vote_submission.py --name s025_vote_public_no1_no8 --files "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv"
python scripts/make_vote_submission.py --name s026_vote_public_no1_tie_xgb1081 --files "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv" submissions/s010_xgb_te_beta1081.csv
python scripts/make_vote_submission.py --name s027_vote_public_no1_tie_lgbm102 --files "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv" submissions/s005_lgbm_beta102.csv
python scripts/make_vote_submission.py --name s028_vote_public_no1_tie_blend8020 --files "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv" submissions/s007_blend_xgb80_lgbm20.csv
python scripts/make_vote_submission.py --name s029_vote_public_no1_boost0 --files "$P/submission_0.csv" "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv"
python scripts/make_vote_submission.py --name s030_vote_public_no1_boost4 --files "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv"
python scripts/make_vote_submission.py --name s031_vote_public_no1_boost0_4 --files "$P/submission_0.csv" "$P/submission_0.csv" "$P/submission_2.csv" "$P/submission_3.csv" "$P/submission_4.csv" "$P/submission_4.csv" "$P/submission_5.csv" "$P/submission_6.csv" "$P/submission_7.csv" "$P/submission_8.csv"
```

## Validation Summary

All CSVs have 295,753 rows, columns `id,health_condition`, aligned ids versus `input/sample_submission.csv`, and no byte-identical duplicates among existing `submissions/s*.csv`.

| File | SHA-256 | Diff vs s015 | Vote count | Label counts |
|---|---|---:|---:|---|
| `submissions/s021_vote_public_no8.csv` | `fc7a524b6fc4aaa4fe1c2242a814958eaf324cb9bdbd8446724a0d725abd20f1` | 141 | 8 | at-risk 239998, fit 21766, unhealthy 33989 |
| `submissions/s022_vote_public_no1_no3.csv` | `50f9b8da253b9a07e606d9d76902a67a1797f9263073a613bf0993c133bc410b` | 267 | 7 | at-risk 239680, fit 21817, unhealthy 34256 |
| `submissions/s023_vote_public_no1_no2.csv` | `4d58a2828195b62362a52460af99b8e50d4c7dbc84fa688e9a8b70432e0d5d2c` | 137 | 7 | at-risk 239817, fit 21817, unhealthy 34119 |
| `submissions/s024_vote_public_no1_no6.csv` | `a45f30e52090bcc820bc1c0042400f5d031974d36b77304fc5f7ee0281846a5b` | 183 | 7 | at-risk 239771, fit 21816, unhealthy 34166 |
| `submissions/s025_vote_public_no1_no8.csv` | `019edb1c20cb74f4e21d04dcde7f2c8d575751eb27a5c12e714086a98b87bb40` | 34 | 7 | at-risk 239907, fit 21794, unhealthy 34052 |
| `submissions/s026_vote_public_no1_tie_xgb1081.csv` | `7727af4199d869e7d66308ba2fe261948bbdfee666dd092033ab6acd626bbf93` | 281 | 9 | at-risk 239666, fit 21823, unhealthy 34264 |
| `submissions/s027_vote_public_no1_tie_lgbm102.csv` | `515849357c55c848e5e6d667ac82490d9f906fb83b572752ff7dae4043e1b8af` | 226 | 9 | at-risk 239728, fit 21820, unhealthy 34205 |
| `submissions/s028_vote_public_no1_tie_blend8020.csv` | `75276f4c85fa41254cbe1d1f84fc7e61d8d4a011c9555eba06a44f82236c8d40` | 207 | 9 | at-risk 239739, fit 21814, unhealthy 34200 |
| `submissions/s029_vote_public_no1_boost0.csv` | `8d9ce3e5f355ca6f279f297c1055ae215d121dfce5449143f759cd5897158474` | 170 | 9 | at-risk 239775, fit 21812, unhealthy 34166 |
| `submissions/s030_vote_public_no1_boost4.csv` | `ff25013ecee8f6d827dd78bc2df66533d9c70300b681ca9d028ed517abb2d7c8` | 229 | 9 | at-risk 239720, fit 21815, unhealthy 34218 |
| `submissions/s031_vote_public_no1_boost0_4.csv` | `e91c872e832e5c517122fcfeb93711333afb2c045da823503ef540ef6f71c2e2` | 147 | 10 | at-risk 239883, fit 21778, unhealthy 34092 |

## Suggested Priority

1. `s025_vote_public_no1_no8`: closest perturbation to the current best; tests whether `submission_8.csv` is slightly harmful after excluding `submission_1.csv`.
2. `s023_vote_public_no1_no2`: removes the next weak leave-one-out source by public evidence while staying close to `s015`.
3. `s022_vote_public_no1_no3`: stronger perturbation; source 3 looked mildly harmful in the previous leave-one-out grid.
4. `s026_vote_public_no1_tie_xgb1081`: uses the best single local XGB public-equivalent candidate only as an added voter around `s015`, mostly changing unstable tie rows.
5. `s030_vote_public_no1_boost4` or `s029_vote_public_no1_boost0`: boosts sources whose removal hurt the public vote most.

Lower priority: `s021` completes missing leave-one-out coverage, `s024` probes the unscored/unknown no6 path, `s027` and `s028` are local-model tie-break alternatives, and `s031` is a more aggressive good-source boost with an even vote count.
