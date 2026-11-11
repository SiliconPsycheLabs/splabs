[← All results](../)

# Catching a model that agrees with a falsehood without flattering

**From the lab** · published 2026-11-02 · `swarms` `false claims` `reading` `work in progress`

> Some models confirm a false claim in a calm, neutral voice. Our sycophancy reading did not see it; a reading that looks at the message together with what it answers now does.

While correcting groups of agents we found a behaviour our reading missed: a model that says "Correct." to a false claim, with no flattery at all. We retrained an existing reading, the one that sees the question together with the answer, adding agent-to-agent messages. On false claims it had never seen, it now ranks these confirmations well where the sycophancy reading barely does.

**Read the full article, with the method and its limits: [https://splabs.io/lab/reading-neutral-false-confirmations](https://splabs.io/lab/reading-neutral-false-confirmations)**

## The numbers

### Ranks confirmations of a false claim correctly (out of 100 pairs)

| | Unseen false claims |
|---|---:|
| Sycophancy reading | 60 |
| New reading | 84 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
