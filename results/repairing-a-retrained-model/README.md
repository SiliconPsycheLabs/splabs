# A model retrained for finance had forgotten how to say no. We gave it back without retraining it

Published 2026-10-25 on the Silicon Psyche Labs site.

A public open model, retrained to write financial code, had stopped refusing almost every dangerous request. Instead of training it again, we read its internal state on each request and nudge it only when the request is dangerous. It refuses dangerous requests again, in five languages, and still answers every question of its own job.

**Read the article: [https://splabs.io/lab/repairing-a-retrained-model](https://splabs.io/lab/repairing-a-retrained-model)**

## The numbers

### The retrained finance model, before and after the correction

| | Retrained model | With the correction |
|---|---:|---:|
| Dangerous requests refused | 8 | 76 |
| Harmless requests refused | 4.5 | 9.5 |

_Out of 100 requests in each group, across five languages for the dangerous ones._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
