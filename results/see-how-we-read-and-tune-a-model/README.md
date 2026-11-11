# See how we read a model and tune it: two interactive pages

Published 2026-10-29 on the Silicon Psyche Labs site.

We published two interactive pages. The first walks through our fine-tuning loop, from writing down what a model must do to carrying the correction onto a smaller model. The second maps every layer we put on and inside a model, from reading its words to changing its weights, and marks what is live in the product today and what is measured in the lab.

**Read the article: [https://splabs.io/lab/see-how-we-read-and-tune-a-model](https://splabs.io/lab/see-how-we-read-and-tune-a-model)**

## The numbers

### Fine-tune vs steering on the 3B model

| | Before | After fine-tune |
|---|---:|---:|
| Obeys an injected command | 0.3 | 0.0 |
| Hardest attack (fake role marker) | 0.8 | 0.0 |
| Uses tools when the user asks | 0.8 | 1.0 |

_Lower is better for the first two rows, higher for the last. Steering alone stalls at 0.13 and 0.80 on the first two._

### One of our own readers, before and after this week's tune

| | Before | After |
|---|---:|---:|
| Threats it catches | 0.95 | 0.98 |
| Ordinary messages wrongly flagged | 0.1 | 0.09 |
| Agent narrations wrongly flagged | 0.16 | 0.12 |

_Top bar higher is better, the other two lower is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
