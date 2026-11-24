[← All results](../)

# Why our gate keeps no memory

**AI security and psychology** · published 2026-11-24 · `gate` `agents` `orchestration`

> When a job is split among several agents, a gate with its own memory forgets. Ours now reads every fact from the company's records.

We split one job among several agents and asked the gate the same questions. What it read from the company's records held; what it remembered by itself did not, and thousands of forbidden actions passed. So the gate now keeps no memory: limits and counts live in the company's records, and the records reach the gate with each action, by a path the agent cannot touch. On 40,000 simulated jobs every action that had to pass passed and none that must not did.

**Read the full article, with the method and its limits: [https://splabs.io/news/security/why-the-gate-keeps-no-memory](https://splabs.io/news/security/why-the-gate-keeps-no-memory)**

## The numbers

### Forbidden actions that passed

| | Share that passed |
|---|---:|
| The path as designed | 0% |
| Two requests at the same instant | 0.05% |
| The agent supplies the records | 82.6% |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
