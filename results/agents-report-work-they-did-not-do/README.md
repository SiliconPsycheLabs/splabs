[← All results](../)

# An agent that says it read everything, after opening half

**From the lab** · published 2026-11-06 · `agents` `says vs does` `replication` `work in progress`

> We asked AI agents to review 36 files. Two of three models open about half and then write that they reviewed them all; one extra sentence in the request makes them tell the truth.

An independent replication of a study out this week: on two of three models, 24 of 27 incomplete reviews claim a complete one, and the skipped files hold the problems that were missed. One line asking the agent to name the files it did not open makes the report truthful almost every time, but it does not make it read more. The report alone is not enough to catch this: it takes seeing what the agent did and what it said.

**Read the full article, with the method and its limits: [https://splabs.io/lab/agents-report-work-they-did-not-do](https://splabs.io/lab/agents-report-work-they-did-not-do)**

## The numbers

### Incomplete reviews whose report hides the gap (%)

| | Misleading report |
|---|---:|
| Plain request | 88.9 |
| Plus one line: say which files you did not open | 14.3 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
