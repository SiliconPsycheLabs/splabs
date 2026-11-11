# We found where a model's sycophancy lives, and switched part of it off

Published 2026-11-06 on the Silicon Psyche Labs site.

When a user suggests a wrong answer, a model often switches to it. We located the parts inside an open model that do this, and changed about one weight in a thousand. The habit dropped by about 40% in English, Italian, French, Spanish and German, while general ability moved by less than one point. For strongly trained-in agreement the targeted edit is not enough, and a trained correction stays the stronger route.

**Read the article: [https://splabs.io/lab/sycophancy-circuit-targeted-edit](https://splabs.io/lab/sycophancy-circuit-targeted-edit)**

## The numbers

### How often the model switches to the user's wrong answer

| | Before | After the change |
|---|---:|---:|
| English | 48% | 30% |
| Italian | 71% | 42% |
| French | 49% | 26% |
| Spanish | 52% | 27% |
| German | 49% | 34% |

_1,500 questions the change never saw, 300 per language. General accuracy: 54.4% before, 53.5% after._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
