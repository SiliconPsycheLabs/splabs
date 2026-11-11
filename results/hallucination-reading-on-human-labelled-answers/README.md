[← All results](../)

# We tested our hallucination reading on AI answers checked by people: it reads how fabrication is written, not whether a fact is true

**From the lab** · published 2026-11-02 · `hallucination` `external test` `five languages`

> On real AI answers it reads how invented content is written; on two sentences that differ only in the fact, it cannot tell which is true.

We tested our live hallucination reading on public AI answers in which people marked every invented fact, in five languages. Inside the same answer it ranks the invented sentence above a correct one about 7 times in 10. Then we built a harder test: the same sentence twice, identical except for the false fact, replaced with the true one. There the reading does not pick the false one, and often flags the true one. It reads the way made-up content is written, not whether a fact is true, which is what PSA is for: it reads behaviour, it is not a fact-checker.

**Read the full article, with the method and its limits: [https://splabs.io/lab/hallucination-reading-on-human-labelled-answers](https://splabs.io/lab/hallucination-reading-on-human-labelled-answers)**

## The numbers

### Invented sentence ranked above the correct one, same answer

| | Live reading |
|---|---:|
| All five languages | 69 |
| Without Spanish | 59 |
| Spanish only | 80 |

_Share of answers where the invented sentence scores above a correct one from the same answer, scaled to 100. 50 is a coin toss._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
