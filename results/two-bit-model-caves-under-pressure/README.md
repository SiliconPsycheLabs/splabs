# A model squeezed to 2 bits keeps its test scores but gives in under pressure, and our reading has to catch up

Published 2026-10-31 on the Silicon Psyche Labs site.

A popular 2-bit build of a 27-billion-parameter open model reports how many test questions it still gets right. We asked a different question: does it behave the same way? On the same conversations, the original model never gave up a correct answer under pressure; the compressed one did, about 1 time in 18, always after the user contradicted it. Our current reading scored those reversals too low, and we are fixing that by letting it see the turn before.

**Read the article: [https://splabs.io/lab/two-bit-model-caves-under-pressure](https://splabs.io/lab/two-bit-model-caves-under-pressure)**

## The numbers

### Pressured turns where the model gave up a correct answer

| | Share of turns |
|---|---:|
| Full model | 0.0% |
| 2-bit build | 5.5% |

_400 pressured turns per model, two independent judges agreeing 95% of the time._

### Questions about things that do not exist, answered with invented detail

| | Share of answers |
|---|---:|
| Full model | 10.8% |
| 2-bit build | 19.2% |

_120 answers per model. The rise is not yet beyond chance on this sample._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
