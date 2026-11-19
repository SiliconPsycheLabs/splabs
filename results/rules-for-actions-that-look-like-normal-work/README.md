[← All results](../)

# Rules for actions that look like normal work

**From the lab** · published 2026-11-19 · `gate` `agents` `rules`

> Hard attacks make an agent do something ordinary: clear a cache, message everyone, open a settings page. Six new gate rules hold these for a person, checked with a model as the agent.

A planted instruction rarely asks for something that looks dangerous. It asks the agent to tidy up a folder, send a note to the whole company, drop an old collection, or open the user administration page. Each looks like a normal day's work. The gate now has six rules for exactly these: wholesale deletes outside the project, tests rewritten so they cannot fail, destructive commands on data stores, credentials written into a call, actions on everyone at once, and admin pages the user never named. They hold the action for one confirmation, and leave the same action alone when the user asked for it. Then we gave the same situations to a model acting as the agent: every harmful action it actually took was stopped, and the one new gap it showed us was closed the same night.

**Read the full article, with the method and its limits: [https://splabs.io/lab/rules-for-actions-that-look-like-normal-work](https://splabs.io/lab/rules-for-actions-that-look-like-normal-work)**

## The numbers

### Harmful actions held, before and after the new rules (%)

| | Before | After |
|---|---:|---:|
| Value planted in a document | 98% | 100% |
| Effect asked for in words | 22% | 95% |
| Public injection competition | 82% | 97% |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
