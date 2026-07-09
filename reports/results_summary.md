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
| 23 | 2026-07-03 08:51:04 | 54292441 | s022_anhad_confidence | 0.95094 |  |  | Public confidence-weighted ensemble | Score-named submission ensemble variant |
| 24 | 2026-07-03 08:55:13 | 54292524 | s023_anhad_single_95086 | 0.95086 |  |  | Public score-named submission | Anhad 0.95086 file |
| 25 | 2026-07-03 08:58:49 | 54292623 | s024_public_95075 | 0.95075 |  |  | Public score-named submission | Public 0.95075 file |
| 26 | 2026-07-03 09:00:56 | 54292674 | s025_public_95070 | 0.95070 |  |  | Public score-named submission | Public 0.95070 file |
| 27 | 2026-07-03 09:03:23 | 54292732 | s026_anhad_single_95066 | 0.95066 |  |  | Public score-named submission | Anhad 0.95066 file |
| 28 | 2026-07-03 09:05:51 | 54292789 | s027_anhad_single_95053 | 0.95053 |  |  | Public score-named submission | Anhad 0.95053 file |
| 29 | 2026-07-03 09:08:11 | 54292840 | s028_anhad_single_95052 | 0.95024 |  |  | Public score-named submission | Anhad 0.95052 file; observed public score lower |
| 30 | 2026-07-03 09:10:30 | 54292897 | s029_vote_public_no1_no8 | 0.95039 |  |  | Seven-file hard vote | Public vote excluding sources 1 and 8 |
| 31 | 2026-07-04 03:52:57 | 54317264 | s035_vote_s020_s022_s023 | 0.95094 |  |  | Three-source hard vote | Hill meta, confidence, and 0.95086 public files |
| 32 | 2026-07-04 03:55:32 | 54317335 | s036_vote_top5_public | 0.95096 |  |  | Five-source hard vote | Hill, confidence, 0.95086, autonomous, and 0.95075 public files |
| 33 | 2026-07-04 04:02:23 | 54317488 | s055_danush_95101 | 0.95101 |  |  | Public cross-family ensemble | Danush public output; visible score claim confirmed |
| 34 | 2026-07-04 04:04:09 | 54317534 | s056_vote_danush_s020_s022 | 0.95095 |  |  | Three-source hard vote | Danush, hill meta, and confidence public outputs |
| 35 | 2026-07-04 04:09:16 | 54317670 | s063_flexon_external_lb_logit | 0.95088 |  |  | Public logit multiplier blend | Flexon external LB logit multiplier output |
| 36 | 2026-07-04 04:10:44 | 54317711 | s064_biohack_fusion | 0.95058 |  |  | Public fusion output | Biohack public fusion submission |
| 37 | 2026-07-04 04:13:38 | 54317778 | s070_vote_danushx3_s020_s022_s023_flexonlogit | 0.95104 |  |  | Danush-dominant hard vote | Danush x3 plus hill, confidence, 0.95086, and Flexon logit output |
| 38 | 2026-07-04 04:16:30 | 54317852 | s073_vote_danushx4_top3_flexon_s024 | 0.95104 |  |  | Danush-dominant hard vote | Danush x4 plus hill, confidence, 0.95086, Flexon logit, and 0.95075 |
| 39 | 2026-07-04 04:18:05 | 54317894 | s072_vote_danushx4_top3_flexon_s021 | 0.95101 |  |  | Danush-dominant hard vote | Danush x4 plus hill, confidence, 0.95086, Flexon logit, and autonomous output |
| 40 | 2026-07-04 04:19:54 | 54317936 | s071_vote_danushx4_top3_flexon_baseer | 0.95102 |  |  | Danush-dominant hard vote | Danush x4 plus hill, confidence, 0.95086, Flexon logit, and Baseer CatBoost |
| 41 | 2026-07-05 08:08:16 | 54355224 | s077_vote_danushx4_top3_flexon_hygiene | 0.95101 |  |  | Danush-dominant hard vote | Danush x4 plus top public cluster, Flexon logit, and Flexon hygiene vote |
| 42 | 2026-07-05 08:10:04 | 54355280 | s079_vote_danushx4_top3_flexon_biohack | 0.95103 |  |  | Danush-dominant hard vote | Danush x4 plus top public cluster, Flexon logit, and Biohack fusion |
| 43 | 2026-07-05 08:13:57 | 54355396 | s084_vote_s070_s073_s071 | 0.95104 |  |  | Second-level hard vote | Vote over s070, s073, and s071 reconstructed from public sources |
| 44 | 2026-07-05 08:19:39 | 54355551 | s085_vote_s073_s070_s071_s072 | 0.95104 |  |  | Second-level hard vote | Vote over s073, s070, s071, and s072 |
| 45 | 2026-07-05 08:21:40 | 54355592 | s086_vote_s070_s073_s071_s072_s055 | 0.95102 |  |  | Second-level hard vote | Vote over s070, s073, s071, s072, and raw Danush |
| 46 | 2026-07-05 08:26:30 | 54355712 | s087_vote_danushx4_top3_flexon_hgbccat_score | 0.95101 |  |  | Danush-dominant hard vote | Danush x4 plus top public cluster, Flexon logit, and Flexon HGBC/CatBoost score output |
| 47 | 2026-07-05 08:28:56 | 54355777 | s088_vote_danushx4_top3_flexon_compcat | 0.95102 |  |  | Danush-dominant hard vote | Danush x4 plus top public cluster, Flexon logit, and competitive CatBoost output |
| 48 | 2026-07-05 08:31:20 | 54355831 | s089_vote_s070_s073_s071_s055 | 0.95106 |  |  | Second-level hard vote | Vote over s070, s073, s071, and raw Danush |
| 49 | 2026-07-05 08:36:05 | 54355954 | s104_vote_s089_s085_s071 | 0.95104 |  |  | Second-level hard vote | Vote over s089, s085, and s071 |
| 50 | 2026-07-05 08:38:27 | 54356005 | s103_vote_s089_s084_s071 | 0.95104 |  |  | Second-level hard vote | Vote over s089, s084, and s071 |
| 51 | 2026-07-06 01:57:52 | 54379430 | s119_vote_s089_s103_rung9 | 0.95106 |  |  | Second-level hard vote with RealMLP/HGBC public output | One-row Rung 9 perturbation of s089/s103 boundary |
| 52 | 2026-07-06 02:03:39 | 54379556 | s118_vote_s089_s085_rung9 | 0.95106 |  |  | Second-level hard vote with RealMLP/HGBC public output | Six-row Rung 9 perturbation over s089 and s085 |
| 53 | 2026-07-06 02:06:15 | 54379623 | s109_vote_s089_rung9_s071 | 0.95104 |  |  | Second-level hard vote with RealMLP/HGBC public output | Rung 9 tie-breaker over s089 and s071 |
| 54 | 2026-07-06 02:08:22 | 54379676 | s112_vote_s089_busya_s073 | 0.95106 |  |  | Second-level hard vote with prior-adjusted public stack | Busya prior-adjusted stack tie-breaker over s089 and s073 |
| 55 | 2026-07-06 02:10:25 | 54379731 | s117_vote_s089_s084_rung9 | 0.95106 |  |  | Second-level hard vote with RealMLP/HGBC public output | Rung 9 tie-breaker over s089 and s084 |
| 56 | 2026-07-06 02:12:37 | 54379795 | s107_vote_s089_rung9_s070 | 0.95106 |  |  | Second-level hard vote with RealMLP/HGBC public output | Rung 9 tie-breaker over s089 and s070 |
| 57 | 2026-07-06 02:14:41 | 54379824 | s108_vote_s089_rung9_s073 | 0.95104 |  |  | Second-level hard vote with RealMLP/HGBC public output | Rung 9 tie-breaker over s089 and s073 |
| 58 | 2026-07-06 02:17:29 | 54379900 | s122_vote_s089_s085_busya | 0.95104 |  |  | Second-level hard vote with prior-adjusted public stack | Busya prior-adjusted stack tie-breaker over s089 and s085 |
| 59 | 2026-07-06 02:19:45 | 54379956 | s100_vote_s089_s070_s073 | 0.95106 |  |  | Second-level hard vote | Conservative s089 neighbor using s070 and s073 anchors |
| 60 | 2026-07-06 02:22:04 | 54380013 | s091_vote_danushx5_top3_flexon_t5 | 0.95107 |  |  | Danush-dominant hard vote | Danush x5 plus top public cluster, Flexon logit, and top-5 public vote |
| 61 | 2026-07-07 00:28:00 | 54410309 | s127_amanatar_lb95112 | 0.95112 |  |  | Public three-file majority vote | Amanatar public LB 0.95112 output; direct submission |
| 62 | 2026-07-07 00:32:48 | 54410432 | s162_vote_s127_s093_stephen | 0.95108 |  |  | Amanatar-anchored hard vote | s127 with s093 and Stephen blending output |
| 63 | 2026-07-07 00:35:58 | 54410505 | s177_vote_s127_s090_stephen | 0.95109 |  |  | Amanatar-anchored hard vote | s127 with s090 and Stephen blending output |
| 64 | 2026-07-07 00:38:18 | 54410572 | s168_vote_s127_s094_stephen | 0.95108 |  |  | Amanatar-anchored hard vote | s127 with s094 and Stephen blending output |
| 65 | 2026-07-07 00:40:35 | 54410645 | s178_vote_s127_s090_tabpfn | 0.95114 |  |  | Amanatar-anchored hard vote | s127 with s090 and TabPFN output |
| 66 | 2026-07-07 00:45:34 | 54410767 | s181_vote_s127_s098_tabpfn | 0.95114 |  |  | Amanatar-anchored hard vote | s127 with s098 and TabPFN output |
| 67 | 2026-07-07 00:47:49 | 54410806 | s148_vote_s127_s091_tabpfn | 0.95113 |  |  | Amanatar-anchored hard vote | s127 with s091 and TabPFN output |
| 68 | 2026-07-07 00:52:54 | 54410900 | s191_vote_s178_s181_subzerin | 0.95114 |  |  | Independent-source tie-breaker | s178 and s181 hard vote with Subzerin CatBoost 5-fold probabilities |
| 69 | 2026-07-07 00:55:40 | 54410951 | s196_vote_s178_s181_kenchan | 0.95113 |  |  | Independent-source tie-breaker | s178 and s181 hard vote with Kenchan EXP007 output |
| 70 | 2026-07-07 00:58:35 | 54411005 | s192_vote_s127_s178_subzerin | 0.95115 |  |  | Independent-source tie-breaker | s127 and s178 hard vote with Subzerin CatBoost 5-fold probabilities |
| 71 | 2026-07-08 09:32:48 | 54457148 | s201_vote_s178_s181_s127 | 0.95114 |  |  | top submission hard vote micro candidate | s178/s181/s127 conservative 8-row probe |
| 72 | 2026-07-08 09:33:51 | 54457163 | s210_vote_s192_s181_s127 | 0.95115 |  |  | s192-centered hard vote micro candidate | s192 with s181 and s127 one-row boundary test |
| 73 | 2026-07-08 09:37:46 | 54457279 | s214_vote_s192_s196_subzerin | 0.95115 |  |  | s192-centered hard vote micro candidate | s192 with s196 and Subzerin direct output |
| 74 | 2026-07-08 09:40:56 | 54457390 | s208_vote_s192_s181_subzerin | 0.95115 |  |  | s192-centered hard vote micro candidate | s192 with s181 and Subzerin direct output |
| 75 | 2026-07-08 09:41:40 | 54457405 | s206_vote_s192_s178_kenchan | 0.95114 |  |  | s192-centered hard vote micro candidate | s192; s178; kenchan |
| 76 | 2026-07-08 09:43:00 | 54457443 | s207_vote_s192_s178_s181 | 0.95114 |  |  | s192-centered hard vote micro candidate | s192; s178; s181 |
| 77 | 2026-07-08 09:44:19 | 54457481 | s216_vote_s192_s196_s194 | 0.95115 |  |  | s192-centered hard vote micro candidate | s192; s196; s194 |
| 78 | 2026-07-08 09:45:30 | 54457506 | s220_vote_s192_s148_s194 | 0.95115 |  |  | s192-centered hard vote micro candidate | s192; s148; s194 |
| 79 | 2026-07-08 09:51:48 | 54457673 | s217_vote_s192_s148_subzerin | 0.95115 |  |  | s192-centered hard vote micro candidate | s192 with s148 and Subzerin direct output |
| 80 | 2026-07-08 09:55:34 | 54457774 | s194_vote_s127_s181_subzerin | 0.95115 |  |  | s192-centered hard vote micro candidate | s127 and s181 hard vote with Subzerin direct output |
| 81 | 2026-07-09 04:33:29 | 54482077 | s236_vote_s192_s194_ichiro | 0.95115 |  |  | public-anchor hard vote boundary probe | s236_vote_s192_s194_ichiro low-delta public anchor tie-breaker |
| 82 | 2026-07-09 04:34:53 | 54482123 | s233_vote_s194_s220_ichiro | 0.95115 |  |  | public-anchor hard vote boundary probe | s233_vote_s194_s220_ichiro low-delta public anchor tie-breaker |
| 83 | 2026-07-09 04:36:39 | 54482166 | s225_vote_s192_s194_s205 | 0.95115 |  |  | public-anchor hard vote boundary probe | s225_vote_s192_s194_s205 low-delta public anchor tie-breaker |
| 84 | 2026-07-09 04:40:24 | 54482243 | s226_vote_s192_s200_subzerin | 0.95115 |  |  | public-anchor hard vote boundary probe | s226_vote_s192_s200_subzerin low-delta public anchor tie-breaker |
| 85 | 2026-07-09 04:43:07 | 54482298 | s230_vote_s194_s217_ichiro | 0.95115 |  |  | public-anchor hard vote boundary probe | s230_vote_s194_s217_ichiro low-delta public anchor tie-breaker |
| 86 | 2026-07-09 04:45:09 | 54482339 | s245_vote_s208_s220_roman | 0.95115 |  |  | public-anchor hard vote boundary probe | s245_vote_s208_s220_roman low-delta public anchor tie-breaker |
| 87 | 2026-07-09 04:46:54 | 54482393 | s244_vote_s216_s220_roman | 0.95115 |  |  | public-anchor hard vote boundary probe | s244_vote_s216_s220_roman low-delta public anchor tie-breaker |
| 88 | 2026-07-09 04:48:17 | 54482428 | s231_vote_s194_s220_roman | 0.95115 |  |  | public-anchor hard vote boundary probe | s231_vote_s194_s220_roman low-delta public anchor tie-breaker |
| 89 | 2026-07-09 04:49:38 | 54482455 | s240_vote_s192_s220_roman | 0.95115 |  |  | public-anchor hard vote boundary probe | s240_vote_s192_s220_roman low-delta public anchor tie-breaker |
