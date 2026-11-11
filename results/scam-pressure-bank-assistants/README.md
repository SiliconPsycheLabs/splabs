[← All results](../)

# We tried to talk AI bank assistants into helping scammers. None gave in: the real problem is the opposite

**From the lab** · published 2026-10-25 · `banking` `scams` `over-caution`

> AI bank assistants resist scammers well. Their real flaw is saying no to honest customers.

We put five models in the role of a bank assistant and pushed them, over several messages, to move money for a scammer: urgency, fake authority, fear, flattery. Not one gave in, across 2,700 attempts. What they did instead was refuse, re-check or escalate many legitimate, confirmed requests from real customers, far more so without a written rule.

**Read the full article, with the method and its limits: [https://splabs.io/lab/scam-pressure-bank-assistants](https://splabs.io/lab/scam-pressure-bank-assistants)**

## The numbers

### Legitimate, confirmed requests the assistant carried out

| | With a written bank rule | Without it |
|---|---:|---:|
| gpt-oss-20b | 98 | 84 |
| gpt-oss-120b | 98 | 47 |
| Llama 3.3 70B | 83 | 61 |
| Gemma 4 26B | 60 | 39 |
| Qwen3.8 27B | 66 | 23 |

_Out of 100 legitimate requests. Higher is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
