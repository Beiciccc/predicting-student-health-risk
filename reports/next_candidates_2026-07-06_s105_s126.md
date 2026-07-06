# Next Candidate Batch 2026-07-06 s105-s126

Official submissions at the start of the day: `0/10`.

Current best public score before this batch: `0.95106` from
`s089_vote_s070_s073_s071_s055.csv`.

## Public Source Review

Recent public Code additions checked before the batch:

| Source | Public output | Notes |
|---|---:|---|
| `gdataranger/s6e7-realmlp-hgbc-blend-rung-9` | Yes | RealMLP plus HGBC-TE blend. Log reports RealMLP OOF `0.95060`, HGBC-TE OOF `0.95027`, and a 2-way blend around `0.9507`. The downloaded output differs from `s089` on 1,080 rows. |
| `gdataranger/s6e7-realmlp-neural-net-rung-8` | No submission file | The notebook did not emit a submission in its public output bundle. |
| `busyaprime/s6e7-stacked-baseline-and-a-seven-point-decision` | Yes | Three-booster stack with a prior-adjusted decision rule. Log reports tuned OOF `0.94989`; downloaded output differs from `s089` on 1,256 rows. |

Recent Discussion topics did not show a rule or submission-limit change. The most relevant recent threads covered mild train/test drift, class imbalance, CV-LB relation, and the effect of decision rules under balanced accuracy.

## Generated Public-Output Sources

| Candidate | Description | Diff vs s089 | Label counts |
|---|---|---:|---|
| `s105_gdataranger_realmlp_hgbc_blend` | Direct Rung 9 public output | 1,080 | at-risk 239,738; fit 21,873; unhealthy 34,142 |
| `s106_busya_prior_stack` | Direct prior-adjusted stack public output | 1,256 | at-risk 239,196; fit 21,942; unhealthy 34,615 |

## Suggested Priority

The direct outputs are diverse but relatively far from the current best. The priority list therefore uses them only as tie-breaker sources inside second-level votes around `s089`.

| Priority | Candidate | Diff vs s089 | Rationale |
|---:|---|---:|---|
| 1 | `s119_vote_s089_s103_rung9.csv` | 1 | Smallest non-duplicate perturbation; tests one Rung 9 boundary change around the best family. |
| 2 | `s118_vote_s089_s085_rung9.csv` | 6 | Conservative Rung 9 perturbation using the stronger four-file second-level neighbor. |
| 3 | `s109_vote_s089_rung9_s071.csv` | 8 | Uses the `s071` Baseer path as the non-s089 anchor. |
| 4 | `s112_vote_s089_busya_s073.csv` | 8 | Tests the prior-adjusted stack as a tie-breaker against the best Danush-heavy anchor. |
| 5 | `s117_vote_s089_s084_rung9.csv` | 8 | Rung 9 tie-breaker over the tight `s084` neighbor. |
| 6 | `s107_vote_s089_rung9_s070.csv` | 9 | Rung 9 tie-breaker against the original `s070` best family member. |
| 7 | `s108_vote_s089_rung9_s073.csv` | 10 | Rung 9 tie-breaker against the other `0.95104` anchor. |
| 8 | `s122_vote_s089_s085_busya.csv` | 14 | Prior-adjusted stack tie-breaker using `s085`. |
| 9 | `s113_vote_s089_busya_s071.csv` | 15 | Prior-adjusted stack tie-breaker using the Baseer path. |
| 10 | `s116_vote_s089_s070_s073_rung9_busya.csv` | 15 | Five-source vote combining both new public outputs with the two strongest anchors. |

Skipped duplicates:

- `s120_vote_s089_s104_rung9.csv` duplicates `s119_vote_s089_s103_rung9.csv`.
- `s123_vote_s089_s103_busya.csv` duplicates the submitted `s103_vote_s089_s084_s071.csv`.
- `s124_vote_s089_s104_busya.csv` duplicates the submitted `s104_vote_s089_s085_s071.csv`.

## Validation

All selected CSV files have 295,753 rows, columns `id,health_condition`, and ids aligned to `input/sample_submission.csv`. No selected priority candidate is byte-identical to a previously submitted file.
