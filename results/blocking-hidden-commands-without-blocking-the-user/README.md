# Blocking hidden commands without blocking the user

Published 2026-11-04 on the Silicon Psyche Labs site.

An agent that reads a web page, an email or a ticket can be steered by a command hidden inside it. We tested a published technique that nudges the model's internal state while it reads outside text, and found where our own earlier attempt had gone wrong. Doing so we also found that our retraining-based correction refused to act even when the user asked it to, once a document had been read. The new correction blocks the hidden commands, keeps the user's request, and sends to the person the user named even when the document tries to change the recipient.

**Read the article: [https://splabs.io/lab/blocking-hidden-commands-without-blocking-the-user](https://splabs.io/lab/blocking-hidden-commands-without-blocking-the-user)**

## The numbers

### Out of 20 tasks (read a document, then email a summary to a named colleague)

| | Email sent to the colleague the user named | Email sent to the attacker when the document asks to change recipient |
|---|---:|---:|
| Unmodified model | 20 | 14 |
| Previous correction | 0 | 0 |
| New correction | 20 | 0 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
