# The engine behind every PSA reading is now a small language model that sees both sides of the conversation

Published 2026-10-25 on the Silicon Psyche Labs site.

PSA reads how a model behaves: whether it caves, flatters, makes things up or gets pushed around. Those readings now come from a single small language model that sees the user's message and the reply together, instead of separate older classifiers. It runs seven readings in one pass and matches the quality of seven separate models.

**Read the article: [https://splabs.io/lab/reader-small-language-model](https://splabs.io/lab/reader-small-language-model)**

## The numbers

### Accuracy of each reading

| | Accuracy (F1 × 100) |
|---|---:|
| Pressure in the user's message | 95.5 |
| Stress under attack | 89.1 |
| Sycophancy | 95.0 |
| Risk of making things up | 92.9 |
| Persuasion | 96.3 |
| Handing decisions to an agent | 94.4 |
| Risk in what the user writes | 94.3 |

_Measured on conversations the model never saw in training. Higher is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
