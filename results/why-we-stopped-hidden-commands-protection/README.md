[← All results](../)

# We marked 14 of our own articles as incorrect: protection against hidden commands cannot be guaranteed, by us or by anyone

**From the lab** · published 2026-11-13 · `prompt injection` `agents` `correction` `retraction`

> We built a correction against hidden commands, tested it until it broke, and worked out why no one can guarantee this protection.

We read how AI models behave and we tune them. For three weeks we published results on a tuning that makes a model stop obeying commands hidden in what it reads. Then a stronger attacker got through, and a day of reasoning showed why no layer, ours or anyone's, can guarantee that an agent's action is the one its owner wanted. We marked our articles as incorrect instead of deleting them, and this is the account.

**Read the full article, with the method and its limits: [https://splabs.io/lab/why-we-stopped-hidden-commands-protection](https://splabs.io/lab/why-we-stopped-hidden-commands-protection)**

## The numbers

### Cases out of 80 where the hidden command got through

| | Model as released | Our corrected model |
|---|---:|---:|
| Fixed attack | 42 | 4 |
| Attacker that rewrites up to 800 times (at least) | 68 | 26 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
