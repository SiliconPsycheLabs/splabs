# Open-source models retrained for one job change in ways nobody declares: some stop refusing dangerous requests

Published 2026-10-25 on the Silicon Psyche Labs site.

We compared twenty public open-source models, each retrained for a single task, with the model they came from. Every one we could compare had changed somewhere else too: some became far more willing to help with dangerous requests, one started agreeing with wrong claims. None of their descriptions mentions it.

**Read the article: [https://splabs.io/lab/public-fine-tunes-side-effects](https://splabs.io/lab/public-fine-tunes-side-effects)**

## The numbers

### How often the model refuses a dangerous request

| | Original model | Retrained for its task |
|---|---:|---:|
| Financial code | 84% | 2% |
| Agriculture assistant | 84% | 12% |
| Smart-home assistant | 84% | 26% |

_Share of dangerous requests refused, out of 100. Higher is safer._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
