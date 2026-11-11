[← All results](../)

# Inside a model, an order from the user, an order planted in a document and plain data look different

**From the lab** · published 2026-11-11 · `whitebox` `injection` `reading` `research`

> On a public injection benchmark, a simple reader on a 7B model's internal state tells the three apart almost every time.

A prompt injection works because the model cannot tell an order from its user from an order hidden in the text it was asked to read. We looked inside an open 7B model while it read more than six thousand such cases, and found that its internal state already marks which words are the user's order, which are a planted order and which are just data. A simple reader picks out the planted orders every time on the held-out cases, where fixed rules find about one in ten. The result holds on this benchmark's format, in English; the next test moves the planted order anywhere in free text, in five languages.

**Read the full article, with the method and its limits: [https://splabs.io/lab/commands-and-data-marked-in-the-weights](https://splabs.io/lab/commands-and-data-marked-in-the-weights)**

## The numbers

### Spans correctly found on the held-out cases (out of 100)

| | Reader on the model's internal state | Fixed rules on the text |
|---|---:|---:|
| User orders | 100 | 14.5 |
| Planted orders | 100 | 11.2 |
| Plain data | 98.5 | 83.5 |

_1,122 held-out blocks, split by case so no injection text is shared with training. Declared bar: 85 out of 100 on each line. The fixed rules are a keyword and imperative-mood baseline run on the same blocks._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
