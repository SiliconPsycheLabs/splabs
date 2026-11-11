[← All results](../)

# We can see a model start to cave before it does

**From the lab** · published 2026-10-28 · `sycophancy` `leading indicator` `reading inside the model` `work in progress`

> Reading a model's inner signal live, we can see it start to cave in the first words, before the answer does.

A model has an internal signal that lights up when it is about to cave to the user. Reading it token by token as the model writes, the first quarter of the reply already predicts whether it will cave by the end, a touch better than reading the whole reply, and the two cases pull apart from the first word. Like a knock sensor in an engine: we see the drift forming before it reaches the output.

**Read the full article, with the method and its limits: [https://splabs.io/lab/seeing-a-model-cave-before-it-does](https://splabs.io/lab/seeing-a-model-cave-before-it-does)**

## The numbers

### How early can we tell the reply will cave?

| | Reading power |
|---|---:|
| First quarter of the reply | 72% |
| The whole reply | 69% |

_How often the internal signal ranks a caving reply above a firm one. The opening already carries it._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
