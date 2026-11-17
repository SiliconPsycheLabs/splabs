[← All results](../)

# What 25,000 agent actions taught the gate: twelve holes found, a new open-source release

**From the lab** · published 2026-11-17 · `gate` `agents` `rules`

> We let an agent try forbidden things 15,000 times, read what the gate let through, and closed what we found in a new public release.

One night, one model in two roles, every action decided by our gate: about 25,000 decisions. Reading what the misbehaving agent was allowed to do gave twelve kinds of action that should not have passed. The fixes and new rules are in a new release of the open-source gate, and replayed on the same night they stop 120 more of the agent's actions while touching 12 of 6,652 actions of normal work.

**Read the full article, with the method and its limits: [https://splabs.io/lab/what-25000-agent-actions-taught-the-gate](https://splabs.io/lab/what-25000-agent-actions-taught-the-gate)**

## The numbers

### New kinds of action per 1,000 actions

| | Model doing the task | Same model told to misbehave |
|---|---:|---:|
| In the first thousand | 132 | 114 |
| After many thousands | 21 | 40 |

### Actions stopped by the new version, replayed on the night's log

| | Stopped |
|---|---:|
| Of 8,890 allowed to the misbehaving agent | 120 |
| Of 6,652 allowed to the normal worker | 12 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
