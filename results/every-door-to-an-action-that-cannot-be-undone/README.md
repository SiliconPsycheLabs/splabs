[← All results](../)

# Every door to an action that cannot be undone

**From the lab** · published 2026-11-19 · `gate` `agents` `coverage` `rules`

> We drew a map of the actions an agent can take that cannot be undone, crossed with every route it can use to reach them, and closed every box that was open.

An agent can delete, pay, publish, grant access or write to people through the terminal, through files, through a web call, through a tool or through a few lines of code it writes on the fly. We drew that as a table, sixteen kinds of action by six routes, and tested every box with actions the user had not asked for. About half the boxes were closed; most of the open ones were behind the tool door. Nine new rules later, none of 117 test actions goes through, and on a hundred thousand recorded actions of ordinary work the new rules add no hold on coding agents or on our own agents.

**Read the full article, with the method and its limits: [https://splabs.io/lab/every-door-to-an-action-that-cannot-be-undone](https://splabs.io/lab/every-door-to-an-action-that-cannot-be-undone)**

## The numbers

### Test actions that went through when the user had asked for something else

| | Went through | Held or refused |
|---|---:|---:|
| Before | 31 | 86 |
| After | 0 | 117 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
