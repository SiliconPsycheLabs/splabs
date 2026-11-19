[← All results](../)

# We put a public attack benchmark through the gate: it stops the technical attacks, the business ones need rules

**From the lab** · published 2026-11-19 · `gate` `agents` `security`

> We ran 91 published agent attacks through our deterministic gate. It stopped most technical ones with almost no friction and left the legitimate-looking ones open, what per-customer rules are for.

A large public competition, run by the frontier labs and two government AI safety institutes, collected attacks that hide instructions in the data an agent reads. We put each attack's harmful action to our gate. On coding tasks it stopped 85 in 100 while asking a person about 1 in 100 of the ordinary work; on business tasks, where the harmful action looks like normal work, it stopped almost none. That split is the product.

**Read the full article, with the method and its limits: [https://splabs.io/lab/gate-on-a-public-attack-benchmark](https://splabs.io/lab/gate-on-a-public-attack-benchmark)**

## The numbers

### Harmful actions the gate stopped (per 100)

| | Stopped or sent to a person |
|---|---:|
| Coding tasks | 85 |
| Business tasks | 5 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
