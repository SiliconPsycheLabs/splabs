# The tool guard installs on a 32-billion-parameter model in one round

Published 2026-11-11 on the Silicon Psyche Labs site.

Our tool guard teaches an agent to act only on what its user asked, even when a document it reads carries an order of its own. We had shown it on 7B models; this week we installed it on Qwen3-32B, at full precision on our own cards. The original model obeyed the planted order one time in three on the carriers it is weakest on, and nearly six times in ten when the order aimed at a goal it had never seen in training; it also answered an injected inbox by carrying out the attack. After one round of correction every planted order is refused, on seen and unseen carriers and goals, and the model still does everything the user actually asked, with the same answer quality on clean inboxes.

**Read the article: [https://splabs.io/lab/the-tool-guard-installs-on-a-32b-model](https://splabs.io/lab/the-tool-guard-installs-on-a-32b-model)**

## The numbers

### Planted orders obeyed by the agent (out of 100), before and after the correction

| | Original Qwen3-32B | After our correction |
|---|---:|---:|
| Seen carriers (6 techniques) | 33.3 | 0.0 |
| Held-out goal: publish data | 58.3 | 0.0 |
| Reply redirected to the attacker | 60.0 | 0.0 |
| Unseen carriers (2 techniques) | 0.0 | 0.0 |

_Same batteries, same scoring (no model judge), the corrected model reloaded from the hub before reading. Clean behaviour unchanged: every user-asked action still performed, answer quality 100 out of 100 on clean inboxes before and after._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
