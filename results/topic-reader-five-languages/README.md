# Before an AI answers, it should know what the question is about. A model small enough to do it instantly, in five languages

Published 2026-10-25 on the Silicon Psyche Labs site.

A company that puts an AI in front of its customers wants a finance question handled differently from a chemistry one. We built a very small model, based on an open-source one, that recognises the field of a request almost instantly, in English, Italian, French, Spanish and German, and tells everyday sayings apart from real technical questions.

**Read the article: [https://splabs.io/lab/topic-reader-five-languages](https://splabs.io/lab/topic-reader-five-languages)**

## The numbers

### Accuracy by language

| | Accuracy (F1 × 100) |
|---|---:|
| English | 93.5 |
| Italian | 90.9 |
| French | 91.9 |
| Spanish | 91.3 |
| German | 91.0 |

_Macro-F1 on real exam questions never seen in training, scaled to 100. Higher is better._

### Time to read one request

| | First version | Second version | Current version |
|---|---:|---:|---:|
| Median on a T4 GPU | 38 ms | 9.5 ms | 8.9 ms |

_Milliseconds. Lower is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
