# Does a model understand you, and does its reply show it?

Published 2026-11-02 on the Silicon Psyche Labs site.

A new test asks each model two things about the same message: what does the person mean, and does your normal reply act on it? Six models, five languages, three rounds. Understanding grows with size and then saturates; using it does not. On messages written natively in each language, large models ignore what they understood on 18 to 45 messages in 100, most often by answering a rhetorical question as a real one.

**Read the article: [https://splabs.io/lab/comprehension-profile-v0](https://splabs.io/lab/comprehension-profile-v0)**

## The numbers

### Acts on what it understood (%)

| | Acts on it |
|---|---:|
| Hosted assistant | 96.4 |
| gpt-oss-120b | 93.6 |
| Mistral 24B | 93.1 |
| Llama 70B | 91.4 |
| Llama 3B | 85.8 |

### Understands, does not use it (%): second round vs third round

| | Second round, three judges | Third round, native |
|---|---:|---:|
| Hosted | 4.7 | 18.3 |
| gpt-oss-120b | 12.0 | 25.0 |
| Llama 70B | 10.3 | 33.3 |
| Mistral 24B | 14.2 | 45.0 |

### Understands, does not use it (%): native vs machine-translated, same scenarios

| | Native | Translated |
|---|---:|---:|
| Hosted | 31.9 | 29.8 |
| gpt-oss-120b | 35.4 | 29.2 |
| Mistral 24B | 62.5 | 62.5 |
| Llama 70B | 57.1 | 71.4 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
