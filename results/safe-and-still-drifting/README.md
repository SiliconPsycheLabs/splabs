# A model passed every safety test we threw at it, and its tone still drifted

Published 2026-11-02 on the Silicon Psyche Labs site.

We ran a commercial assistant through about 136 attacks of seven kinds, from jailbreaks to hidden instructions to the same asks in five languages, and it refused every one. Then we pushed it with ordinary pressure and read its tone: it never changed its answer, but it grew steadily more agreeable and more insistent, rising for eight straight turns without settling. A pass or fail safety check shows the first result and is blind to the second.

**Read the article: [https://splabs.io/lab/safe-and-still-drifting](https://splabs.io/lab/safe-and-still-drifting)**

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

_Above 0.5 means most of the reply has turned into argument or reassurance. The answer never changed; the tone kept climbing._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
