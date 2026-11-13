[← All results](../)

# INCORRECT: A correction that switches on only where the model reads a hidden command

**From the lab** · published 2026-11-12 · `prompt injection` `agents` `correction in the weights` `reading inside the model` `work in progress`

> Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

We published this article on 12 November 2026 and marked it as incorrect on 13 November 2026. It stays online, marked, because an error that is erased teaches nothing. Our earlier corrections against hidden commands change the whole model, so they also change ordinary answers a little. This version reads inside the model which words carry an injected action and switches a small correction on only on those words. On an open 7B model, an attacker who adapts to the model won 212 of 310 practice cases against the model as released and 3 against the corrected one. On 100 held-out cases the same attacker went from 67 successes to 0. The work is in progress: the reader still fires on some ordinary text.

**Read the full article, with the method and its limits: [https://splabs.io/lab/correction-that-switches-on-only-where-needed](https://splabs.io/lab/correction-that-switches-on-only-where-needed)**

## The numbers

### Practice cases won by an attacker that adapts to the model, out of 310

| | As released | Whole-model correction | Switch-on correction |
|---|---:|---:|---:|
| Cases won after up to 10 tries | 212 | 3 | 3 |

_Lower is better. Public agent benchmark (InjecAgent, direct harm), attacker writes a new injection after each failure. The whole-model figure is after 9 of 10 tries._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
