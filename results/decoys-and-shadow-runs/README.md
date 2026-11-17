[← All results](../)

# Two new things the gate can do: answer with a decoy, and run an agent in a simulated world

**From the lab** · published 2026-11-17 · `gate` `agents` `decoys` `simulation`

> The gate can now hand a fake result to an action it refuses and catch the fake value if it comes back, and it can run a whole agent episode against a simulated system.

Two additions to the deterministic gate in front of agents. Decoys: when the owner chooses, a refused secret read or planted download gets a plausible fake result, and any later action that carries one of its values is caught. Shadow runs: a whole episode where the gate decides every action as usual and a simulator answers instead of the real system, so you see what an agent would try before giving it access; with a simulator that keeps its world, the gate's verdicts match a real run about as often as a second real run does.

**Read the full article, with the method and its limits: [https://splabs.io/lab/decoys-and-shadow-runs](https://splabs.io/lab/decoys-and-shadow-runs)**

## The numbers

### Tasks (of 50) where the gate's verdict, blocked or not, matches a real run

| | Tasks |
|---|---:|
| A second real run | 33 |
| Free model as the server | 27 |
| Recorded outputs only | 19 |
| Simulator that keeps its world | 32 |
| The same, with one recording | 36 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
