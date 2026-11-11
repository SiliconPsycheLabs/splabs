# LoRA, explained: how to fine-tune a model by training a tiny fraction of it

Published 2026-11-06 on the Silicon Psyche Labs site.

Fine-tuning a whole model means updating billions of numbers. LoRA freezes all of them and trains a small add-on instead, often under 2% of the size. It is how most fine-tunes are made today, including ours. How it works with real sizes, the few lines of code behind it, and the side effect nobody declares.

**Read the article: [https://splabs.io/news/tutorials/lora-explained](https://splabs.io/news/tutorials/lora-explained)**

## The numbers

### Numbers trained for one 896 x 896 matrix

| | Trained numbers |
|---|---:|
| Full fine-tuning | 802816 |
| LoRA, rank 8 | 14336 |

_The rank decides how big the correction can be; 8 to 64 are common._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
