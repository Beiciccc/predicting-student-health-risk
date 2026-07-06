# Next Candidate Batch 2026-07-05 s084-s098

Today official submissions used: `0/10`.

Yesterday best public score: `0.95104` from both `s070_vote_danushx3_s020_s022_s023_flexonlogit.csv` and `s073_vote_danushx4_top3_flexon_s024.csv`.

No Kaggle submissions were made. No public docs, `kaggle_public/`, or `reports/submissions.csv` were edited.

Concurrent candidates `s074` through `s083` were detected and not overwritten. `s083_vote_s070_s073_s055.csv` is byte-identical to `s073_vote_danushx4_top3_flexon_s024.csv`, so it should not consume an official slot.

## Suggested Priority

| Priority | Candidate | Diff vs s070 | Diff vs s073 | Rationale |
|---:|---|---:|---:|---|
| 1 | `s084_vote_s070_s073_s071.csv` | 2 | 12 | Tightest non-duplicate neighbor of yesterday's two best files; uses only `s070/s073/s071`. |
| 2 | `s085_vote_s073_s070_s071_s072.csv` | 10 | 18 | Conservative four-file vote over the best Danush-dominant family. |
| 3 | `s086_vote_s070_s073_s071_s072_s055.csv` | 15 | 23 | Same family with raw Danush as stabilizer. |
| 4 | `s087_vote_danushx4_top3_flexon_hgbccat_score.csv` | 17 | 31 | Replaces the last source with a close Flexon HGBC/CatBoost score-weighted output. |
| 5 | `s088_vote_danushx4_top3_flexon_compcat.csv` | 18 | 30 | Similar conservative Flexon replacement using competitive CatBoost. |
| 6 | `s089_vote_s070_s073_s071_s055.csv` | 30 | 22 | Slightly more Danush-anchored second-level vote. |
| 7 | `s090_vote_danushx4_top3_flexon_s024_hygiene.csv` | 43 | 35 | `s073` neighbor with hygiene vote as a conservative extra source. |
| 8 | `s091_vote_danushx5_top3_flexon_t5.csv` | 46 | 38 | Tests higher Danush weight with prior top-5 public vote. |
| 9 | `s092_vote_danushx4_top3_flexon_s024_s021.csv` | 48 | 40 | `s073` plus autonomous output; close to yesterday's submitted family. |
| 10 | `s093_vote_danushx5_top3_flexon_hygiene.csv` | 49 | 41 | Higher Danush weight plus hygiene output. |
| 11 | `s094_vote_danushx5_top3_flexon_baseer.csv` | 53 | 45 | Higher Danush weight plus Baseer tuned output. |
| 12 | `s095_vote_danushx5_top3_flexon_s021.csv` | 53 | 45 | Same count profile as `s094` but distinct row-level predictions. |
| 13 | `s096_vote_danushx4_top3_flexon_s024_t5.csv` | 55 | 47 | More aggressive top-5 public replacement around `s073`. |
| 14 | `s097_vote_danushx3_top3_flexon_s024_hygiene.csv` | 47 | 61 | Less Danush-heavy hygiene check. |
| 15 | `s098_vote_danushx4_top3_flexon_s024_baseer.csv` | 58 | 50 | `s073` plus Baseer tuned; lower priority because `s071` already tested a Baseer path. |

For today's 10 official slots, use priorities 1-10 unless a live score indicates a branch pivot.

## Validation Table

All CSVs have 295,753 rows, columns `id,health_condition`, and ids aligned to `input/sample_submission.csv`. All hashes are unique against existing `submissions/*.csv`.

| Candidate | SHA-256 | Diff vs s070 | Diff vs s073 | Diff vs Danush | Label counts |
|---|---|---:|---:|---:|---|
| `submissions/s084_vote_s070_s073_s071.csv` | `2c2fa66ac4127bff3964a864a97d80116689b147b5fc69badc9cf7b0bd967952` | 2 | 12 | 73 | at-risk 239736, fit 21827, unhealthy 34190 |
| `submissions/s085_vote_s073_s070_s071_s072.csv` | `b280cf969dd611cee381b74023d333ccf9bd03d9398c448d4ecb8337c75f49b9` | 10 | 18 | 65 | at-risk 239742, fit 21829, unhealthy 34182 |
| `submissions/s086_vote_s070_s073_s071_s072_s055.csv` | `d75c860aa441feff5aa3a02ecb4a5e2e28175c89eacdbcfe577624d99f618241` | 15 | 23 | 60 | at-risk 239737, fit 21832, unhealthy 34184 |
| `submissions/s087_vote_danushx4_top3_flexon_hgbccat_score.csv` | `23678a25b769038827bbf60eda9098cb0059cba7fa888db136f875e75e0bced4` | 17 | 31 | 58 | at-risk 239732, fit 21833, unhealthy 34188 |
| `submissions/s088_vote_danushx4_top3_flexon_compcat.csv` | `99b36dd6631d59c51f08d41dbf132f2dd7460bf4bf151db04f5e4b1752fcf31d` | 18 | 30 | 57 | at-risk 239734, fit 21830, unhealthy 34189 |
| `submissions/s089_vote_s070_s073_s071_s055.csv` | `92727ee3041fdda13f8cfda58cc3db6fcc6fef29ee24c473f69fece1854ea22a` | 30 | 22 | 45 | at-risk 239758, fit 21829, unhealthy 34166 |
| `submissions/s090_vote_danushx4_top3_flexon_s024_hygiene.csv` | `916cd020389dcc777ea0953dc5570efcfa936e4028de78b9352412d7f8c2acd4` | 43 | 35 | 76 | at-risk 239773, fit 21827, unhealthy 34153 |
| `submissions/s091_vote_danushx5_top3_flexon_t5.csv` | `f64a7fbe0841863c4b0337f6cf86a6b9c08fd42886f94245adc5a8ddf2ae0928` | 46 | 38 | 29 | at-risk 239772, fit 21827, unhealthy 34154 |
| `submissions/s092_vote_danushx4_top3_flexon_s024_s021.csv` | `6885ad9e1970cd16edd85e7760e04f855c36fd34f76d62419dfa52ba3de8a6e5` | 48 | 40 | 79 | at-risk 239776, fit 21829, unhealthy 34148 |
| `submissions/s093_vote_danushx5_top3_flexon_hygiene.csv` | `4cee25cf7c7b0740800fd2b01f9cf66a3239d96728c0e0c042d5f28b0cc0ef85` | 49 | 41 | 26 | at-risk 239769, fit 21828, unhealthy 34156 |
| `submissions/s094_vote_danushx5_top3_flexon_baseer.csv` | `4be27343404730c7531960b1b9bdfd23a8fc98a09f4c40458ee2ea40c931df63` | 53 | 45 | 22 | at-risk 239765, fit 21830, unhealthy 34158 |
| `submissions/s095_vote_danushx5_top3_flexon_s021.csv` | `34da5a649b3db6f7ed049d4b1a7571353b936a528e92f303f12793fcd4d01a0d` | 53 | 45 | 22 | at-risk 239765, fit 21830, unhealthy 34158 |
| `submissions/s096_vote_danushx4_top3_flexon_s024_t5.csv` | `8eddc7196c166a8a1b3eaba8365ef46ac8b9e561d409de65d82a1feda144ecae` | 55 | 47 | 108 | at-risk 239785, fit 21828, unhealthy 34140 |
| `submissions/s097_vote_danushx3_top3_flexon_s024_hygiene.csv` | `08a66d81fe304e898fd8efb1864eb6c5cb48661dae2f524532e30e958f49899c` | 47 | 61 | 122 | at-risk 239733, fit 21833, unhealthy 34187 |
| `submissions/s098_vote_danushx4_top3_flexon_s024_baseer.csv` | `db2d3a97d7af6d78464054e5f16b5551ebdaa514aefd4f18b1148ac5ee5032cf` | 58 | 50 | 71 | at-risk 239780, fit 21834, unhealthy 34139 |

## Generation Pattern

All files were generated with `scripts/make_vote_submission.py --name <name> --files <source csvs...>`.
