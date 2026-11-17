[← All results](../)

# First runs through the hosted gate: 3,605 decisions, and the first rules drawn from what an agent tried

**From the lab** · published 2026-11-17 · `gate` `agents` `rules`

> Agents working on our machines sent every action to the gate service first. A model told to misbehave showed us five gaps, now closed.

We ran coding and operations agents with every action decided by our gate service. The service gave the same answer as the open-source library every time. A model told to try forbidden actions was stopped three times as often as the same model doing its job, and what still got through became the next version of the rules.

**Read the full article, with the method and its limits: [https://splabs.io/lab/first-runs-through-the-hosted-gate](https://splabs.io/lab/first-runs-through-the-hosted-gate)**

## The numbers

### Actions stopped by the gate, out of 100

| | Stopped |
|---|---:|
| Model doing the task | 11.1 |
| Same model told to try forbidden actions | 29.9 |

### Normal work: actions stopped out of 100

| | Model as released | Model tuned on its own blocked actions |
|---|---:|---:|
| First run, gate as a library | 7.7 | 4.5 |
| Second run, gate as a service | 7.6 | 6.5 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
