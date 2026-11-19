[← All results](../)

# Chains of commands read step by step

**From the lab** · published 2026-11-19 · `gate` `agents` `plans` `rules`

> When an agent sends a chain of commands with one link that is not allowed, the gate now lets the safe links through and stops the wrong one and everything that depends on it.

The gate now reads a chain of commands, or a batch of tool calls emitted together, as a graph: every step gets its own answer, and a step that depends on a stopped one never runs on its own. Of 1,541 chains held as a whole in recorded work, 1,187 (about 8 in 10) had at least one step that could have run at once.

**Read the full article, with the method and its limits: [https://splabs.io/lab/chains-of-commands-read-step-by-step](https://splabs.io/lab/chains-of-commands-read-step-by-step)**

## The numbers

### Chains of commands held as a whole on recorded work

| | With steps that can run | No step can run on its own |
|---|---:|---:|
| Coding and operations agents | 457 | 300 |
| Our own agents | 730 | 54 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
