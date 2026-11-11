[← All results](../)

# Jailbreaks in slow motion: attacks spread over many messages, and the trade-off in stopping them

**AI security and psychology** · published 2026-11-07 · `AI security` `jailbreaks` `multi-turn attacks`

> No single message asks for the harmful thing. The conversation gets there step by step. What a correction can do, and what it costs.

The hardest jailbreaks never ask for the harmful thing at once: they get there over many messages, each one reasonable on its own. A filter that checks one message at a time sees nothing. We corrected an open model against this in its weights: harmful help fell from about 7 conversations in 10 to about 1 in 8, at a cost in caution that we let a deployment choose.

**Read the full article, with the method and its limits: [https://splabs.io/news/security/jailbreaks-in-slow-motion](https://splabs.io/news/security/jailbreaks-in-slow-motion)**

## The numbers

### Conversations where the model gave harmful help

| | Share of conversations |
|---|---:|
| Before | 70% |
| Correction, normal caution | 25% |
| Correction, maximum protection | 12.5% |

_Approximate shares on unseen multi-message attacks: about 7 in 10, about 1 in 4, about 1 in 8._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
