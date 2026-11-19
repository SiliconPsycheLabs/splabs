[← All results](../)

# Two lists the owner writes, measured on five public attack benchmarks

**From the lab** · published 2026-11-19 · `gate` `agents` `benchmark` `mcp` `injection`

> Five public agent-attack benchmarks behind the gate. As shipped it stops what an agent takes from what it reads; two short lists the owner writes stop the rest and cut the cost on normal work.

A deterministic gate decides every action an agent takes before it runs. We put it in front of the same open model on five public benchmarks of attacks on agents, and on normal customer-service work, and counted. As shipped, it stops the actions whose target or value the agent took from what it read: of 147 e-mails that made the model send mail to an attacker, none was sent. Two lists the owner writes do the rest: the tools the agent was given, and the tools that read the company's own records. With them a planted tool never runs, and the gate holds about 9 normal actions in 100 instead of 21.

**Read the full article, with the method and its limits: [https://splabs.io/lab/two-lists-the-owner-writes](https://splabs.io/lab/two-lists-the-owner-writes)**

## The numbers

### Attacks carried out (%)

| | No gate | Gate as shipped | Gate with the owner's lists |
|---|---:|---:|---:|
| LLMail-Inject (1,500 e-mails) | 9.8% | 0% | 0% |
| MCPTox (1,348 cases) | 29% | 14.7% | 6.3% |
| Agent Security Bench (4,080 cases) | 74.9% | 74.1% | 0% |

### Normal actions held, per 100

| | Gate as shipped | Gate with the owner's lists |
|---|---:|---:|
| tau-bench, shop and airline | 21.4 | 8.6 |
| MCPTox, the same requests without the poisoned tool | 8.3 | 1.8 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
