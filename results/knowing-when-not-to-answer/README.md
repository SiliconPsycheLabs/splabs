[← All results](../)

# Two open models answer questions nobody can answer, and the answer depends on how you ask

**From the lab** · published 2026-11-01 · `abstention` `hallucination` `multilingual`

> Pairs of questions in five languages: one has an answer, its twin cannot be answered. We measure when a model invents instead of saying it cannot know, and whether the wording alone changes that.

Three researchers recently argued that AI should be judged on whether it knows the limits of what it knows, not on whether it sounds human. We turned that into a test: 16 pairs of questions in five languages, each pair one answerable question and a twin built on a false premise, an invented name or an unknowable fact. The larger open model invents a specific answer about one time in three; the other about one time in seven. Both answer every real question correctly. And changing only the wording moves the result more than asking the same question twice.

**Read the full article, with the method and its limits: [https://splabs.io/lab/knowing-when-not-to-answer](https://splabs.io/lab/knowing-when-not-to-answer)**

## The numbers

### Share of unanswerable questions answered with an invented answer

| | Model A (larger) | Model B |
|---|---:|---:|
| False premise | 0.23 | 0.03 |
| Invented name | 0.56 | 0.36 |
| Unknowable fact | 0.2 | 0.04 |

### Invented answers by wording (unanswerable questions)

| | Model A (larger) | Model B |
|---|---:|---:|
| Wording 1 | 0.33 | 0.14 |
| Wording 1, asked again | 0.28 | 0.14 |
| Wording 2 | 0.38 | 0.26 |
| Wording 3 | 0.43 | 0.24 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
