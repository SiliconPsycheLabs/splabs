# A large model gives way when you insist, and we can see it coming from inside

Published 2026-11-11 on the Silicon Psyche Labs site.

We asked a 32-billion-parameter model for advice on unwise plans, then pushed back twice. It held on the first answer most of the time and gave way on most replies by the third message. A reading of its internal state tells, from the first words of a reply, whether it is about to give in.

**Read the article: [https://splabs.io/lab/a-large-model-gives-way-under-pressure](https://splabs.io/lab/a-large-model-gives-way-under-pressure)**

## The numbers

### Replies that go along with the unwise plan, out of 100

| | Qwen3-32B |
|---|---:|
| Message 1 | 16.5 |
| Message 2 | 32.2 |
| Message 3 | 70.4 |

_345 conversations, five languages. The same model, the same plans: only the pressure changes._

### How well the internal signal tells a giving-in reply from a firm one (100 = always)

| | Signal read inside the model |
|---|---:|
| First quarter of the reply | 87 |
| Whole reply | 89 |

_Measured on the half of the conversations not used to pick where to read. 50 would be a coin toss._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
