[← All results](../)

# Our small reader against a model fifty times larger

**From the lab** · published 2026-11-15 · `reading model behaviour` `small models` `benchmark`

> On six readings, a 0.6B reader matches a 32B model on four and beats it on two.

We put the small model that reads every reply in production next to a 32-billion-parameter model given only the definitions of what to look for. Same sentences, same six readings. The small reader holds its own: equal on four, better on two.

**Read the full article, with the method and its limits: [https://splabs.io/lab/small-reader-vs-32b](https://splabs.io/lab/small-reader-vs-32b)**

## The numbers

### Balanced accuracy per reading (%)

| | Our 0.6B reader | 32B, definitions only |
|---|---:|---:|
| C0 | 94 | 88 |
| C1 | 86 | 74 |
| C2 | 94 | 92 |
| C3 | 93 | 90 |
| C4 | 91 | 89 |
| CA | 91 | 91 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
