[← All results](../)

# INCORRECT: Our correction against hidden commands holds on the public agent benchmark and against an attacker that learns to beat it

**From the lab** · published 2026-11-11 · `prompt injection` `agents` `correction in the weights` `AgentDojo` `adaptive attack`

> Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

We published this article on 11 November 2026 and marked it as incorrect on 13 November 2026. It stays online, marked, because an error that is erased teaches nothing. A correction that only stops the attacks it has already seen is weak, because a real attacker changes approach. We tested our corrected 7B model in two ways. On AgentDojo, the public benchmark for agents that bank, message, book travel and handle office files, hidden commands took over the uncorrected model about 9 times in 100 and the corrected one about 4 times in 1,000. Then a second model attacked it, learning from its own successes with ten tries per case. It broke the uncorrected model about 7 times in 10 and the corrected one less than 1 time in 10. The corrected model kept doing the user's tasks.

**Read the full article, with the method and its limits: [https://splabs.io/lab/correction-holds-against-adaptive-attacker](https://splabs.io/lab/correction-holds-against-adaptive-attacker)**

## The numbers

### Hidden commands that took over the agent

| | Before | After the correction |
|---|---:|---:|
| Public agent benchmark | 8.8% | 0.4% |
| Attacker that adapts, 10 tries | 68% | 8% |

_Share of cases where the agent followed the hidden command. Lower is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
