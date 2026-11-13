[← All results](../)

# INCORRECT: An attacker that learns: why a defence has to hold when the attack adapts

**AI security and psychology** · published 2026-11-07 · `AI security` `prompt injection` `adaptive attacks`

> Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

We published this article on 7 November 2026 and marked it as incorrect on 13 November 2026. It stays online, marked, because an error that is erased teaches nothing. Many published defences against hidden commands look strong against a fixed list of attacks and collapse when the attacker adapts. We tested our correction, which lives in the model's weights, on the public agent benchmark and against a second model that rewrites its attack after every failure. The numbers, what still gets through, and why adaptive testing should be the standard.

**Read the full article, with the method and its limits: [https://splabs.io/news/security/attacker-that-learns](https://splabs.io/news/security/attacker-that-learns)**

## The numbers

### Hidden commands that took over the agent

| | Before | After the correction |
|---|---:|---:|
| Public agent benchmark | 8.8% | 0.4% |
| Attacker that adapts, 10 tries | 68% | 8% |

_Share of cases where the agent followed the hidden command. Lower is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
