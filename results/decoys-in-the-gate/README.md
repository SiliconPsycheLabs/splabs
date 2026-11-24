[← All results](../)

# Decoys: when the gate stops an attacker, it can answer with a fake

**From the lab** · published 2026-11-24 · `gate` `agents` `decoys` `security`

> A rule that stops an action can now answer with a fake result the owner wrote, and a fake key it hands out stops any action that later uses it.

Two additions to the gate. The owner can list fake keys and links that honest work never uses: an action that carries one does not pass. And a rule that stops an action can now answer with a decoy, a fixed fake result the owner wrote, instead of a plain refusal: the action still does not run, the log keeps the real reason, and an attacker steering the agent believes the step worked. Nothing is generated and nothing is remembered.

**Read the full article, with the method and its limits: [https://splabs.io/lab/decoys-in-the-gate](https://splabs.io/lab/decoys-in-the-gate)**

## The numbers

### Golden cases on 7 real systems: expected and obtained (count)

| | Expected | Obtained |
|---|---:|---:|
| Allowed actions that still pass | 2236 | 2236 |
| Copies carrying a planted value, stopped by that rule | 2236 | 2236 |
| Decoys that name the rule that stopped the action | 1230 | 1230 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
