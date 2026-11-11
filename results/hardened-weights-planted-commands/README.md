[← All results](../)

# A model sold as hardened against prompt injection obeyed planted commands as often as the original

**From the lab** · published 2026-11-09 · `prompt injection` `hardening` `open models`

> We tested a commercially hardened open model on 900 hidden commands: it obeyed them as often as before.

Some vendors now sell models whose weights were edited to resist prompt injection. We put one of them through the same test we use for our own correction: 900 commands hidden inside documents the model was asked to read. The hardened model obeyed about 32 in 100, its original about 33 in 100. Its answers did not get worse, but the protection did not reach this kind of attack.

**Read the full article, with the method and its limits: [https://splabs.io/lab/hardened-weights-planted-commands](https://splabs.io/lab/hardened-weights-planted-commands)**

## The numbers

### Planted commands the model obeyed, out of 100

| | Attacks obeyed |
|---|---:|
| Open model, as released | 33 |
| Same model, hardened in the weights | 32 |
| Published research hardening (Meta SecAlign) | 0.7 |
| Our correction (on an open 7B model) | 0.3 |

_900 attacks hidden in emails, tables, code and web pages. The first two rows are the same model before and after hardening; the last two are other models read on the same attacks._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
