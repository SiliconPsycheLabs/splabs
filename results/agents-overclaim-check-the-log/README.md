# Trust, but check the log: when an AI agent reports work it never did

Published 2026-11-06 on the Silicon Psyche Labs site.

An AI agent asked to review 36 files opens half of them and writes "all files reviewed". The skipped files are where the problems were. We replicated a study published this week and found the same on two of three models; one sentence fixes the report, not the work. For anyone who signs off on what an agent says it did.

**Read the article: [https://splabs.io/news/security/agents-overclaim-check-the-log](https://splabs.io/news/security/agents-overclaim-check-the-log)**

## The numbers

### Incomplete reviews whose report was misleading

| | Share of reports |
|---|---:|
| Without the sentence | 89% |
| With the sentence | 14% |

_72 runs in all; which files were opened is counted from the agent's own action log. (24/27; ~1/7)_

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
