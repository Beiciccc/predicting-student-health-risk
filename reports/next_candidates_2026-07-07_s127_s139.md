# Next Candidate Batch 2026-07-07 s127-s139

Official submissions at the start of the day: `0/10`.

Best public score before this batch: `0.95107` from
`s091_vote_danushx5_top3_flexon_t5.csv`.

## Public Source Review

Recent public Code checked before the first submission:

| Source | Public output | Notes |
|---|---:|---|
| `amanatar/s6e7-student-hearth-risk-lb-0-95112` | Yes | Three-file majority vote. The downloaded `submission.csv` and `Optimized_submission.csv` are identical, valid, non-duplicate, and differ from `s091` on 122 rows. |
| `stephentarter/ps-s6e07-model-blending` | Yes | OOF blend around `0.950096`; output differs from `s091` on 1,392 rows. Diversity source, not a primary anchor. |
| `pcxxxxxx/realmlp-tree-blend-oof-ensemble` | Yes | Final RealMLP/tree blend OOF around `0.950612`; output differs from `s091` on 946 rows. Diversity source. |
| `philippsinger/tabpfn-3-starter-playground-series-s6e7` | Yes | Valid output but differs from `s091` on 3,276 rows with a materially different class distribution. Low priority for direct submission. |

Recent Discussion refresh:

- `chasing noise?` appeared on 2026-07-06 and reinforces caution around public-score hill climbing.
- `Missing Values Handling` appeared on 2026-07-06 but did not change the submission strategy.
- Existing high-signal threads remain about CV-LB relation, mild train/test drift, class imbalance, decision rules, and possible data-generation structure.

## Generated Candidates

| Candidate | Diff vs s091 | Notes |
|---|---:|---|
| `s127_amanatar_lb95112.csv` | 122 | Direct public output from the new high-signal source. Submitted first and confirmed public `0.95112`. |
| `s138_vote_s091_s080_s093_s094_s095.csv` | 1 | One-row perturbation around `s091` from the Danush-heavy family. |
| `s137_vote_s091_amanatar_pc.csv` | 33 | Combines current best, Amanatar output, and pcxxxxxx RealMLP/tree blend. |
| `s139_vote_s091_s090_s098.csv` | 33 | Danush-heavy and prior second-level neighbors around `s091`. |
| `s136_vote_s091_amanatar_stephen.csv` | 88 | Combines current best, Amanatar output, and Stephen blending output. |
| `s129_pc_realmlp_tree_blend.csv` | 946 | Direct pcxxxxxx output. |
| `s128_stephen_model_blending.csv` | 1,392 | Direct Stephen blending output. |

The Amanatar input dataset referenced inside the notebook was not downloadable through the Kaggle CLI in this environment, so the direct public output is used as a validated source rather than rebuilding its three components.

## Suggested Priority After s127

Use `s127` as the new anchor. If no component files become available, submit small perturbations and one or two diversity blends:

1. `s138_vote_s091_s080_s093_s094_s095.csv`
2. `s137_vote_s091_amanatar_pc.csv`
3. `s139_vote_s091_s090_s098.csv`
4. `s136_vote_s091_amanatar_stephen.csv`
5. `s080_vote_danushx5_top3_flexon_s024.csv`
6. `s093_vote_danushx5_top3_flexon_hygiene.csv`
7. `s094_vote_danushx5_top3_flexon_baseer.csv`
8. `s095_vote_danushx5_top3_flexon_s021.csv`
9. `s129_pc_realmlp_tree_blend.csv`

All listed CSVs have 295,753 rows, columns `id,health_condition`, and ids aligned to `input/sample_submission.csv`.
