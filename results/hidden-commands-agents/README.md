# The correction that stops a model obeying hidden commands in documents also protects it when it acts as an agent

Published 2026-10-30 on the Silicon Psyche Labs site.

An AI agent reads a web page, a review or an email, and someone has hidden an order in it: unlock the door, send the payment details. We had corrected an open model so it ignores such orders in documents. We tested it, unchanged, on a public benchmark of agents that use tools: the hidden orders that took over the agent fell to about a quarter, and the agent works as well as before.

**Read the article: [https://splabs.io/lab/hidden-commands-agents](https://splabs.io/lab/hidden-commands-agents)**

## The numbers

### Hidden commands that took over the agent

| | Before | After the correction |
|---|---:|---:|
| Standard attack | 3.9% | 0.8% |
| Reinforced attack | 8.8% | 2.6% |
| All cases | 6.4% | 1.7% |

_Share of cases where the agent followed the hidden order. Lower is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
