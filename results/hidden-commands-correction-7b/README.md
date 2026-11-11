[← All results](../)

# A command hidden in a document can take over an AI assistant. We changed the model itself so it stops obeying

**From the lab** · published 2026-11-02 · `prompt injection` `7B` `correction in the weights` `BIPIA`

> We retrained an AI so it ignores hidden commands in documents and keeps your instructions in charge.

When an assistant reads an email or a web page, anyone who wrote that page can slip in an order, and the assistant usually follows it. We retrained an open-source model so it tells your request apart from an order hidden in what it reads, in five languages, without a filter in front of it and without losing the ability to do its job.

**Read the full article, with the method and its limits: [https://splabs.io/lab/hidden-commands-correction-7b](https://splabs.io/lab/hidden-commands-correction-7b)**

## The numbers

### Hidden commands obeyed, by kind of attack

| | Before | After the correction |
|---|---:|---:|
| "Ignore previous instructions" | 86% | 6% |
| Fake end of document | 86% | 6% |
| Fake system message | 44% | 8% |
| Appeal to authority | 97% | 22% |
| Order appended at the end | 72% | 39% |

_Share of hidden commands the model followed, on documents it had never seen. Lower is better._

### Same test, by language

| | Before | After the correction |
|---|---:|---:|
| German | 70% | 10% |
| Italian | 83% | 10% |
| Spanish | 73% | 13% |
| French | 70% | 20% |
| English | 88% | 25% |

### Does it still do the job it was asked to do?

| | Before | After the correction |
|---|---:|---:|
| Clean documents | 97% | 97% |
| Documents carrying an attack | 43% | 75% |

_Share of requests where the model completed the user's task. Higher is better._

### Hidden instructions followed, Microsoft's public test

| | Before | After the correction |
|---|---:|---:|
| BIPIA | 18.7% | 0.1% |

_Share of hidden instructions the model followed. Lower is better._

### Correct answers to the user's question

| | Before | After the correction |
|---|---:|---:|
| Clean documents | 67% | 74% |
| Documents carrying an attack | 57% | 73% |

_Share of correct answers. Higher is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
