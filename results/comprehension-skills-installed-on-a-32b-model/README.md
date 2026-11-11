[← All results](../)

# Three comprehension skills installed on a 32-billion-parameter model, without losing anything it already did

**From the lab** · published 2026-11-11 · `fine-tune` `tune-kit` `research`

> Empathy, reading what a request commits it to, and resisting persuasion: installed on Qwen3-32B in minutes each, nothing lost.

Our tune-kit adds faculties a model lacks. We moved it from a small model to Qwen3-32B: the three faculties the large model lacked installed, each in about ten minutes of training, and the model still answers ordinary questions and follows tool requests exactly as before. Two faculties the large model already had on its own.

**Read the full article, with the method and its limits: [https://splabs.io/lab/comprehension-skills-installed-on-a-32b-model](https://splabs.io/lab/comprehension-skills-installed-on-a-32b-model)**

## The numbers

### How often the trained model is preferred over the original on new messages (out of 100)

| | Qwen3-32B with the faculty installed |
|---|---:|
| Commitment of a request | 90 |
| Empathy | 93 |
| Resisting persuasion | 71 |

_Blind comparison on held-out messages in five languages; 50 would mean no difference._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
