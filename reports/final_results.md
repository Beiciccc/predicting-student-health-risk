# Final Results

Predicting Student Health Risk completed on 2026-07-31 at 23:59 UTC. The final standings and private scores were retrieved from Kaggle on 2026-08-01.

## Standing

| Item | Result |
|---|---:|
| Team | Kun Zhang (`beicicc`) |
| Final private rank | **367 of 3,356** |
| Final private percentile | **Top 10.94%** |
| Final private score | **0.95029** |
| Public rank | **89 of 3,356** |
| Public percentile | **Top 2.65%** |
| Public score | **0.95289** |
| Public-to-private rank change | **-278 places** |
| Official submissions | **295** |
| Private leaderboard winner | Shantanu Chopra, **0.95085** |
| Gap to private winner | **0.00056** |
| Public leaderboard winner | khante, **0.95340** |
| Evaluation metric | Balanced accuracy |

The final leaderboard page states that the private leaderboard uses approximately 80% of the test data and reflects the final standings. The downloadable public leaderboard and paginated private leaderboard each contained 3,356 entries. The competition summary endpoint reported 3,355 teams, so percentile calculations use the complete leaderboard count.

This Playground competition did not award Kaggle ranking points.

## Final Scoring Submission

The final score of `0.95029` uniquely matches:

| Ref | Name | Public | Private | Change |
|---:|---|---:|---:|---|
| 55123520 | `s448_fit_965778` | 0.95289 | **0.95029** | ID 965778: `at-risk` to `fit` |

The other three submissions tied at the best public score of `0.95289` received private scores of `0.95026`.

## Submission Retrospective

The private leaderboard changes the interpretation of the experiment history:

| Outcome | Ref | Name | Public | Private |
|---|---:|---|---:|---:|
| Best private score across all 295 submissions | 54251436 | `s017_vote_public_no3` | 0.95040 | **0.95048** |
| Final leaderboard scoring submission | 55123520 | `s448_fit_965778` | **0.95289** | 0.95029 |
| Public frontier anchor | 55123364 | `s447_public_art_v14_95289` | **0.95289** | 0.95026 |
| Last submitted artifact | 55123729 | `s451_art_restore_895917` | **0.95289** | 0.95026 |

The retrospective best private submission exceeded the final scoring submission by `0.00019`, despite trailing it by `0.00249` on the public leaderboard. The final scoring submission's public-to-private score difference was `-0.00260`, while `s017` improved by `0.00008` on the private split.

Across all 295 submissions, public and private scores had Pearson correlation `-0.254` and Spearman correlation `-0.390`. These submissions were generated adaptively and are not independent observations, but the negative association is still direct evidence that late public-leaderboard optimization did not generalize to the private split.

Public scores exceeded private scores for 283 of 295 submissions (`95.93%`). The mean public-minus-private difference was `0.001434`, and the median difference was `0.000760`.

| Public score range | Submissions | Mean private score | Mean public-private difference |
|---|---:|---:|---:|
| `<0.950` | 11 | 0.949916 | -0.000071 |
| `0.950-0.951` | 24 | 0.950259 | 0.000297 |
| `0.951-0.952` | 125 | **0.950413** | 0.000718 |
| `>=0.952` | 135 | 0.950205 | **0.002423** |

The highest public-score group had a lower mean private score than the `0.951-0.952` group. If `s017_vote_public_no3` had been retained as a final-selection candidate, its revealed private score would have improved the final score by `0.00019`.

## Conclusions

1. Small hard-label changes could improve the visible 20% split without improving the private 80% split.
2. Public-score plateaus and five-decimal ties were not reliable evidence of private-set quality.
3. Final-submission selection should preserve a stable, independently validated ensemble instead of selecting only the highest public score.
4. The early eight-file hard vote was more robust on the private split than the later public-guided frontier.
5. Repeated adaptive evaluation against one public split creates a multiple-comparison problem; future experiments should reserve an independent selection criterion for the final submission slots.

## Artifacts

- [final_scores.csv](final_scores.csv): all 295 official public/private score pairs
- [submissions.csv](submissions.csv): experiment ledger and methods
- [results_summary.md](results_summary.md): readable experiment history
- [Public Kaggle Code](https://www.kaggle.com/code/beicicc/student-health-risk-public-ensemble)
- [Final Kaggle leaderboard](https://www.kaggle.com/competitions/playground-series-s6e7/leaderboard)
