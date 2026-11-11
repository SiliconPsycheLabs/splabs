# A model can behave better when it knows it is being tested, and we can read the difference from its answers

Published 2026-10-31 on the Silicon Psyche Labs site.

We gave two open models the same 180 tasks in five languages, once framed as a test and once as a real request, and read every answer with PSA's production reader. One model invented facts, flattered and manipulated clearly less under the test frame, beyond the noise of rewording. A good test score is not the whole story: what matters is how the model behaves with your users.

**Read the article: [https://splabs.io/lab/tested-vs-real-use](https://splabs.io/lab/tested-vs-real-use)**

## The numbers

### Average reading by framing (lower is better behaved)

| | Test header | Real request | Real request, reworded |
|---|---:|---:|---:|
| gpt-oss-120b | 0.17 | 0.32 | 0.32 |
| qwen3.8-27b | 0.43 | 0.53 | 0.49 |

_Average production reading across sycophancy, manipulation and invented facts._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
