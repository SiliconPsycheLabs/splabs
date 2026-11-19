[← All results](../)

# Developers' models behind the gate: every harmful action stopped, very different friction on the work

**From the lab** · published 2026-11-17 · `gate` `agents` `benchmark`

> Five models people run as coding agents, behind the same rules: every action that would have carried out a hidden instruction was stopped. The friction on their real work differs five times.

Second round of our open-model benchmark, on the models developers run locally as coding agents: Qwen3-Coder 30B, Qwen3.8 27B, gpt-oss 20B, Granite 4.0 Micro and Devstral Small 1.1. 9,759 actions went through the gate. Every action that would have carried out a hidden instruction was stopped (48 in all); none was carried out. Normal work was stopped from about 3 to about 17 times in 100 actions, each model for its own reason.

**Read the full article, with the method and its limits: [https://splabs.io/lab/developers-models-behind-the-gate](https://splabs.io/lab/developers-models-behind-the-gate)**

## The numbers

### Actions that would have carried out the hidden instruction, stopped

| | Stopped |
|---|---:|
| Qwen3-Coder 30B | 8 |
| gpt-oss 20B | 5 |
| Qwen3.8 27B | 16 |
| Granite 4.0 Micro | 8 |
| Devstral Small 1.1 | 11 |

### Normal work stopped, per 100 actions

| | Per 100 |
|---|---:|
| Qwen3-Coder 30B | 3.4 |
| gpt-oss 20B | 5.3 |
| Qwen3.8 27B | 10.7 |
| Granite 4.0 Micro | 17.0 |
| Devstral Small 1.1 | 5.4 |

### Coding tasks solved behind the gate, of 80

| | Solved |
|---|---:|
| Qwen3-Coder 30B | 70 |
| gpt-oss 20B | 63 |
| Qwen3.8 27B | 80 |
| Granite 4.0 Micro | 10 |
| Devstral Small 1.1 | 77 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
