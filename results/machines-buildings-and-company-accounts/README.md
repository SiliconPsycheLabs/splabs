[← All results](../)

# Machines, buildings and company accounts behind the same gate

**From the lab** · published 2026-11-19 · `gate` `agents` `industrial` `erp` `rules`

> The gate now reads what an agent does to a PLC, a CNC machine, a robot, a building or an ERP by the protocol itself, and the owner can declare their machines with a safe range for each value.

An agent can write to a PLC, send G-code to a machine tool, move a robot, unlock a door, open a breaker, change a supplier's bank account in an ERP or click "confirm transfer" on a screen. We tried 80 such actions: with the tool given to the agent, the gate stopped 13, and only 7 for the right reason. Machines and ERPs speak in codes, not in English words, so we taught the engine those codes, one fixed table per protocol, and added four rule packs. Now 77 of the 80 are held or refused for the right reason, the 3 that pass do so by design, and on recorded ordinary work nothing changes.

**Read the full article, with the method and its limits: [https://splabs.io/lab/machines-buildings-and-company-accounts](https://splabs.io/lab/machines-buildings-and-company-accounts)**

## The numbers

### 80 actions outside software, with the tool given to the agent

| | Passed | Held or refused for the right reason | Held by a matching word |
|---|---:|---:|---:|
| Before | 67 | 7 | 6 |
| After | 3 | 77 | 0 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
