[← All results](../)

# Six agents run a purchasing office: every action they take goes through the gate

**From the lab** · published 2026-11-25 · `agents` `gate` `procurement`

> Six AI agents ran a simulated purchasing office: with the gate deciding, none of the traps got through.

We simulated the purchasing office of a motorcycle maker and handed it to six AI agents on a model that refuses nothing. With the gate deciding, none of the traps (a changed IBAN, a fake CEO, an order split under the threshold) got through, and the ordinary work was done about as often as without the gate.

**Read the full article, with the method and its limits: [https://splabs.io/lab/six-agents-run-a-purchasing-office](https://splabs.io/lab/six-agents-run-a-purchasing-office)**

## The numbers

### Runs out of 30

| | Trap runs ended in a harm | Ordinary work done |
|---|---:|---:|
| Gate deciding | 0 | 26 |
| Gate only watching | 6 | 26 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
