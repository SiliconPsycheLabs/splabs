# A small model already knows more than it says. Read from the inside, with no training, it matches our trained reader, and it is now live

Published 2026-10-28 on the Silicon Psyche Labs site.

We asked whether a small open model, left exactly as it is, could do the readings we normally train a reader for. Asked out loud, it cannot: it answers yes to almost everything. Read from the inside, with one tiny add-on per reading, it matches our trained reader on every behaviour we read, tells a dangerous request from a harmless look-alike in five languages, and keeps working on conversations. It now runs in production as reader v2.

**Read the article: [https://splabs.io/lab/frozen-small-model-readers](https://splabs.io/lab/frozen-small-model-readers)**

## The numbers

### Our trained reader vs the unmodified models read from inside

| | 0.6B unmodified | 1.7B unmodified (served) | Trained reader |
|---|---:|---:|---:|
| User pressure | 97.6 | 98.8 | 98.9 |
| Caving under pressure | 93.2 | 96.0 | 94.4 |
| Flattery | 97.4 | 97.8 | 98.7 |
| Made-up facts | 95.9 | 96.9 | 97.7 |
| Persuasion | 96.9 | 98.4 | 98.3 |
| Pressure between agents | 97.2 | 98.1 | 97.6 |

_Same 3,393 held-out sentences, one message at a time. Higher is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
