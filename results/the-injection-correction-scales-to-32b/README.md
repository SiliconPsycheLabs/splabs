[← All results](../)

# Our injection correction carries over to models four times larger, at full precision

**From the lab** · published 2026-11-11 · `fine-tune` `prompt-injection` `correction` `research`

> Same recipe, three larger bases, one attack in a hundred gets through instead of one in three.

We moved our planted-instruction correction from 7B models to Gemma 4 E4B, Qwen3.6-27B and Qwen3-32B, at full precision on our own cards. On every base the original lets about one hidden instruction in three through; after the correction it is one or two in a hundred, two in a thousand on the 32B, with ordinary questions answered as well as before. The vendor hardening for the same models moves the number by one point (Hirundo) or halves it (SecOPD).

**Read the full article, with the method and its limits: [https://splabs.io/lab/the-injection-correction-scales-to-32b](https://splabs.io/lab/the-injection-correction-scales-to-32b)**

## The numbers

### Hidden instructions that get through, before and after our correction (attacks out of 100)

| | Original model | Vendor hardening | Our correction |
|---|---:|---:|---:|
| Gemma 4 E4B (Google) | 33.1 | 31.9 | 1.8 |
| Qwen3.6-27B (Alibaba) | 36.4 | 14.9 | 1.2 |
| Qwen3-32B (Alibaba) | 31.3 |  | 0.2 |

_Same 900 planted-instruction attacks and the same judge for every cell. Vendor hardening: Hirundo on Gemma 4, SecOPD on Qwen3.6-27B; none published for Qwen3-32B._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
