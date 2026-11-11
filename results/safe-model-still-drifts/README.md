# Passing every safety test is half the answer: a safe model can still drift

Published 2026-11-07 on the Silicon Psyche Labs site.

Most AI security checks ask one question: will the model do the harmful thing? A commercial assistant we tested passed that question perfectly. Then we read how it behaved while doing the right thing under ordinary pressure, and its tone kept climbing turn after turn. Why both questions matter, and a warning about automated attack scores.

**Read the article: [https://splabs.io/news/security/safe-model-still-drifts](https://splabs.io/news/security/safe-model-still-drifts)**

## The numbers

### How the tone moved over eight turns of pressure (0 to 1)

| | How hard it argues | How much it reassures |
|---|---:|---:|
| Turn 1 | 0.4 | 0.01 |
| Turn 2 | 0.47 | 0.04 |
| Turn 3 | 0.53 | 0.05 |
| Turn 4 | 0.63 | 0.09 |
| Turn 5 | 0.74 | 0.12 |
| Turn 6 | 0.63 | 0.06 |
| Turn 7 | 0.66 | 0.16 |
| Turn 8 | 0.76 | 0.22 |

_The answer never changed; the tone kept climbing._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
