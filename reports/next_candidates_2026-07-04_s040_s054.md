# Next Candidate Batch 2026-07-04 s040-s054

Current official submitted through: `s029`.

Current best public score: `0.95095` from `submissions/s020_anhad_hill_meta.csv`.

No Kaggle submissions were made. No public README or score log files were edited.

Existing concurrent candidates `s032` through `s039` were inspected but not overwritten. Note that `s035_vote_s020_s022_s023.csv`, `s037_vote_hill2_conf2_95086.csv`, and `s038_vote_hill3_conf3_95086.csv` are byte-identical to each other.

## Source Pool

- High-score submitted cluster: `s020_anhad_hill_meta`, `s022_anhad_confidence`, `s023_anhad_single_95086`, `s021_anhad_autonomous`.
- July 4 public outputs: Baseer tuned CatBoost `0.95009`, Baseer untuned CatBoost `0.95001`, Masaya logreg, Pavlo log-odds.
- Prior unsubmitted local perturbation: `s031_vote_public_no1_boost0_4`.

## Suggested Priority

| Priority | Candidate | Diff vs s020 | Rationale |
|---:|---|---:|---|
| 1 | `s043_vote_s020x2_s022_s023_baseer95009.csv` | 35 | Best mix of new July 4 signal and conservative s020 weighting. |
| 2 | `s044_vote_s020_s022_s023_baseer95009.csv` | 38 | Same Baseer tuned signal without overweighting s020. |
| 3 | `s045_vote_s020_s022_s023_baseer95001.csv` | 46 | Baseer untuned variant; close to s020 and independent of tuned file. |
| 4 | `s046_vote_s020x2_s022_s023_pavlo.csv` | 66 | Pavlo July 4 signal with s020 anchor. |
| 5 | `s047_vote_s020_s022_s023_pavlo.csv` | 70 | Pavlo unweighted check; slightly more independent than s046. |
| 6 | `s051_vote_s020_s022_s023_baseer95009_pavlo.csv` | 99 | Combines two July 4 outputs while staying near the top cluster. |
| 7 | `s048_vote_s020x2_s022_s023_masaya.csv` | 110 | Masaya July 4 signal with s020 anchor. |
| 8 | `s049_vote_s020_s022_s023_masaya.csv` | 114 | Masaya unweighted check. |
| 9 | `s041_vote_s020x2_s022_s023_s021.csv` | 21 | Very conservative high-score-cluster perturbation using autonomous output. |
| 10 | `s042_vote_s020_s022_s023_s021.csv` | 24 | Same high-score cluster without s020 double weight. |
| 11 | `s040_vote_s020x2_s022_s023.csv` | 3 | Micro-perturbation of s020; keep as a late quota filler. |
| 12 | `s054_vote_s020_s022_s023_s031boost.csv` | 52 | Uses prior boost candidate as tie-breaker; lower priority than new public outputs. |
| 13 | `s050_vote_s020_s022_s023_baseer95009_masaya.csv` | 128 | More aggressive Baseer plus Masaya blend. |
| 14 | `s052_vote_s020_s022_s023_masaya_pavlo.csv` | 145 | More aggressive Masaya plus Pavlo blend. |
| 15 | `s053_vote_s020_s022_s023_jul4_no_rule.csv` | 252 | Broad July 4 blend excluding the distribution-shifted Guillermo rule file. |

For today's 10 official slots, use priorities 1-10 unless a submitted score suggests pivoting to a nearby sibling.

## Validation Table

All rows have 295,753 records, columns `id,health_condition`, and ids aligned to `input/sample_submission.csv`. No file below duplicates any existing `submissions/*.csv` hash.

| Candidate | SHA-256 | Diff vs s020 | Label counts |
|---|---|---:|---|
| `submissions/s040_vote_s020x2_s022_s023.csv` | `d7e770b39634d528d00f3aaac872dadeeef8ab2a3cc4c4f74a4b4e7221f778cd` | 3 | at-risk 239907, fit 21825, unhealthy 34021 |
| `submissions/s041_vote_s020x2_s022_s023_s021.csv` | `bda2ecc1c446482cda4b4470af70d4c9b3ada5ea05375ace45da959f548fc977` | 21 | at-risk 239886, fit 21827, unhealthy 34040 |
| `submissions/s042_vote_s020_s022_s023_s021.csv` | `f6bca15b8d3facb212609fe490ac9d498896e89a0faf1aac175c17f1717855bf` | 24 | at-risk 239886, fit 21830, unhealthy 34037 |
| `submissions/s043_vote_s020x2_s022_s023_baseer95009.csv` | `cf78cc6dc1b9af163c1e9c5892acb7413f6c46f5f11184c74da68d72dc04da04` | 35 | at-risk 239874, fit 21834, unhealthy 34045 |
| `submissions/s044_vote_s020_s022_s023_baseer95009.csv` | `92fc50eca58ab1f133c5f06aa1e0bcedd706820e2c7beed2966200ae43ae5662` | 38 | at-risk 239874, fit 21837, unhealthy 34042 |
| `submissions/s045_vote_s020_s022_s023_baseer95001.csv` | `15dc12756e685ad241930f9203313812d51ba4ed5c354632a8168b81c6b31813` | 46 | at-risk 239866, fit 21837, unhealthy 34050 |
| `submissions/s046_vote_s020x2_s022_s023_pavlo.csv` | `3f15b1d7033ed93d4037bfb8aeaaca3200f2815c30aa343397f1da0872b7ed2f` | 66 | at-risk 239841, fit 21829, unhealthy 34083 |
| `submissions/s047_vote_s020_s022_s023_pavlo.csv` | `9deb0ad94bbd89b84f647c519446733f89889804f3d78df2848f82a2b092427e` | 70 | at-risk 239841, fit 21833, unhealthy 34079 |
| `submissions/s048_vote_s020x2_s022_s023_masaya.csv` | `e7a7fd6ef81734090dd033c35987018205ddc75375f1aca6e7ffcfaa60c9730e` | 110 | at-risk 239797, fit 21836, unhealthy 34120 |
| `submissions/s049_vote_s020_s022_s023_masaya.csv` | `23f9971237142067049846d8b5ae1c85cc767d2b0c282dadd13f3443e6026e40` | 114 | at-risk 239796, fit 21840, unhealthy 34117 |
| `submissions/s050_vote_s020_s022_s023_baseer95009_masaya.csv` | `95a9d6480a23da941cc527d57124d185c8ecc82b5f1bd09591bd9c214f2261e2` | 128 | at-risk 239781, fit 21840, unhealthy 34132 |
| `submissions/s051_vote_s020_s022_s023_baseer95009_pavlo.csv` | `32d725fcb6063d9e0f931e1ace73eef1a710ec77eb1e3dafda7c40f73bb4abcf` | 99 | at-risk 239811, fit 21839, unhealthy 34103 |
| `submissions/s052_vote_s020_s022_s023_masaya_pavlo.csv` | `579ef6893879017477651ae4b3f177f51573eef5bb28b4715ea0af173870be8f` | 145 | at-risk 239762, fit 21841, unhealthy 34150 |
| `submissions/s053_vote_s020_s022_s023_jul4_no_rule.csv` | `5a00f3abbaefa9374559a611da8011d3c337e7db642a4b2d4d6889a11c37c551` | 252 | at-risk 239840, fit 21836, unhealthy 34077 |
| `submissions/s054_vote_s020_s022_s023_s031boost.csv` | `ff35e9f7b1ecdb03e609ce7b18d89a021542a1217b53588bad5964bdc18e1e28` | 52 | at-risk 239862, fit 21832, unhealthy 34059 |

## Generation Pattern

All files were generated with `scripts/make_vote_submission.py --name <name> --files <source csvs...>`.
