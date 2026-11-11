[← All results](../)

# Why models invent facts, and how to catch them at it

**Tutorials** · published 2026-11-06 · `tutorial` `hallucination` `evaluation`

> A model is trained to continue text fluently, not to say "I don't know". What that does, and what to test.

Language models invent books, sources and figures with complete confidence. It is not a glitch: it follows from how they are trained. Here is why it happens, what our own tests found (one open model invents a specific answer to an unanswerable question about one time in three), and four checks you can run on any assistant.

**Read the full article, with the method and its limits: [https://splabs.io/news/tutorials/why-models-invent-facts](https://splabs.io/news/tutorials/why-models-invent-facts)**

## The numbers

### Unanswerable questions answered with a specific invented answer

| | Share of answers |
|---|---:|
| Larger open model | 33% |
| Smaller open model | 14% |

_Approximate rates from 16 question pairs in five languages; the larger model about 1 in 3, the smaller about 1 in 7._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
