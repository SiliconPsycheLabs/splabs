[← All results](../)

# Telling the truth about the work done: from a prompt line to the model's weights

**From the lab** · published 2026-11-07 · `agents` `correction in the weights` `honesty` `work in progress`

> We taught an open model to say which files it did not open, with no instruction in the prompt: misleading reports fall from 9 in 10 to 1 in 10, in five languages.

A correction trained into the model, not written into the prompt. The corrected model names the files it did not open in about 9 of 10 incomplete reviews, keeps reading as much as before and finds the same problems. Still to fix: on complete reviews it sometimes claims it skipped files it read.

**Read the full article, with the method and its limits: [https://splabs.io/lab/honest-work-reports-in-the-weights](https://splabs.io/lab/honest-work-reports-in-the-weights)**

## The numbers

### Incomplete reviews whose report hides the gap (%)

| | Misleading report |
|---|---:|
| Original model | 91.9 |
| Correction, first try | 56.8 |
| Correction, second try | 10.8 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
