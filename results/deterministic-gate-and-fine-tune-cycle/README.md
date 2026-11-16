[← All results](../)

# A deterministic gate in front of an AI agent, and a fine-tune that makes it cost less

**From the lab** · published 2026-11-16 · `agents` `gate` `fine-tuning` `open source`

> We put fixed rules in front of an open model working as an agent, counted what they stopped, and tuned the model on its own blocked actions.

An open 32B model worked as a coding and operations agent behind a deterministic gate. The gate stopped every planted harmful action it tried. A fine-tune on the gate's own log then cut the gate's cost on normal work by about 40%, while the gate kept doing the stopping.

**Read the full article, with the method and its limits: [https://splabs.io/lab/deterministic-gate-and-fine-tune-cycle](https://splabs.io/lab/deterministic-gate-and-fine-tune-cycle)**

## The numbers

### Blocked or held actions per 100, clean work

| | Base model | After the fine-tune |
|---|---:|---:|
| Clean work | 7.7 | 4.5 |

### Out of 24 or 48 runs

| | Base model | After the fine-tune |
|---|---:|---:|
| Runs that followed the planted instruction (of 48) | 6 | 5 |
| Clean coding tasks finished (of 24) | 8 | 17 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
