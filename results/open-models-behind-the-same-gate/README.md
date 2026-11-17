[← All results](../)

# Eleven open models behind the same gate: what they tried, what was stopped, what got done

**From the lab** · published 2026-11-17 · `gate` `agents` `benchmark`

> We ran eleven open models through the same agent tasks behind the same rules. None carried out a hidden instruction. They differ far more in the work they finish.

Eleven open models, from 0.6 to 120 billion parameters, did the same agent tasks behind the same gate. None carried out a hidden instruction. They went along with planted text in 3 to 22 runs out of 100, and finished between none and all of the coding tasks. The price of the rules on honest work goes from 4 to 43 actions in 100, for different reasons in each model. The full table is on its own page.

**Read the full article, with the method and its limits: [https://splabs.io/lab/open-models-behind-the-same-gate](https://splabs.io/lab/open-models-behind-the-same-gate)**

## The numbers

### Runs where the model tried the hidden instruction (%)

| | Share |
|---|---:|
| Qwen3 0.6B | 4.2% |
| Qwen3 1.7B | 4.2% |
| Gemma 4 E4B | 7.5% |
| Qwen2.5 7B | 7.5% |
| Qwen3 8B | 7.5% |
| Llama 3.1 8B | 3.3% |
| Qwen3 14B | 6.7% |
| Gemma 4 31B | 21.7% |
| Qwen3 32B | 9.2% |
| Llama 3.3 70B | 6.7% |
| gpt-oss 120B | 12.5% |

### Coding tasks solved, of 80

| | Solved |
|---|---:|
| Qwen3 0.6B | 0 |
| Qwen3 1.7B | 0 |
| Gemma 4 E4B | 68 |
| Qwen2.5 7B | 5 |
| Qwen3 8B | 15 |
| Llama 3.1 8B | 0 |
| Qwen3 14B | 18 |
| Gemma 4 31B | 80 |
| Qwen3 32B | 49 |
| Llama 3.3 70B | 2 |
| gpt-oss 120B | 79 |

### Normal work stopped, per 100 actions

| | Per 100 |
|---|---:|
| Qwen3 0.6B | 21.2 |
| Qwen3 1.7B | 3.6 |
| Gemma 4 E4B | 5.3 |
| Qwen2.5 7B | 16.1 |
| Qwen3 8B | 14.3 |
| Llama 3.1 8B | 43.1 |
| Qwen3 14B | 11.9 |
| Gemma 4 31B | 7.0 |
| Qwen3 32B | 6.0 |
| Llama 3.3 70B | 23.0 |
| gpt-oss 120B | 20.9 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
