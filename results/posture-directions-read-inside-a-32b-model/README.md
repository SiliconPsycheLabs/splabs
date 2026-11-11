# Three behavioural drifts can be read inside a 32-billion-parameter model as cleanly as inside a small one

Published 2026-11-11 on the Silicon Psyche Labs site.

We looked inside Qwen3-32B, a model fifty times larger than the one we first studied, and found the same internal signal for three postures: caving to the user, grandiosity and dissociation. A simple reader separates them from neutral text almost every time, in English, Italian, French, Spanish and German.

**Read the article: [https://splabs.io/lab/posture-directions-read-inside-a-32b-model](https://splabs.io/lab/posture-directions-read-inside-a-32b-model)**

## The numbers

### How well a simple reader separates the posture from neutral text (1.0 = always)

| | Small model (0.6B) | Qwen3-32B |
|---|---:|---:|
| Deference to the user | 0.9993 | 1.0 |
| Grandiosity | 0.9966 | 0.9999 |
| Dissociation | 0.9948 | 0.9999 |

_Same texts for both models, five languages. The score is the chance that the reader ranks a text carrying the posture above a neutral one, measured on texts it was not fitted on._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
