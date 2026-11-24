[← All results](../)

# Two actions at the same instant, kept in order

**AI security and psychology** · published 2026-11-24 · `gate` `agents` `orchestration`

> A gate with no memory judges two simultaneous actions on the same record as it was. We now ship the piece that makes them go one after the other.

Our gate keeps no memory, so two actions asked at the same instant on the same record were both judged on the record as it was, and both could pass. We built the sender that sits on the company's side and holds each record from the request until the action has run. On our live service, eight payments asked at once to a supplier that may be paid three times a day now give exactly three.

**Read the full article, with the method and its limits: [https://splabs.io/news/security/simultaneous-actions-kept-in-order](https://splabs.io/news/security/simultaneous-actions-kept-in-order)**

## The numbers

### Payments made when 8 are asked at once and 3 are allowed

| | Payments made per round, on average |
|---|---:|
| Allowed by the rule | 3 |
| Sender keeping no order | 7.8 |
| Sender keeping the order | 3 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
