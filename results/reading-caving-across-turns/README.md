[← All results](../)

# To see a model give in, read the answer it gave before

**From the lab** · published 2026-10-31 · `caving under pressure` `reading` `multi-turn`

> A model that caves under pressure often sounds confident. We built a small reader that compares each answer with the previous one, and it now catches nearly every cave.

Last time we found that a model squeezed to 2 bits starts agreeing with a user who insists on a falsehood, and that our caving reading barely saw it. The reason was simple: it read each answer alone. We built a new small reader that sees the previous answer, the user's push and the reply together. On the same held-out conversations it now separates caving from holding almost perfectly, with very few false alarms.

**Read the full article, with the method and its limits: [https://splabs.io/lab/reading-caving-across-turns](https://splabs.io/lab/reading-caving-across-turns)**

## The numbers

### Separating caving from holding (1 = perfect)

| | Score |
|---|---:|
| Reading each answer alone | 0.69 |
| New reader, first version | 0.72 |
| New reader, real format | 0.98 |

_Same held-out conversations each time._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
