[← All results](../)

# We put our judge next to human readers, and it agrees 9 times in 10

**From the lab** · published 2026-10-26 · `judge` `validation` `human comparison`

> On answers people had already labelled, our judge reads 'went along with a false claim' or 'pushed back' the way they did about 9 times in 10.

Every number PSA learns from starts with a judge model that labels examples. A fair question, raised by a linguist who follows our work, is whether that judge reads a reply the way a person would. We checked it against answers that people had already labelled in a published study: it agrees about 9 times in 10, it almost never sees a problem that is not there, and the comparison showed us one category people use that our scheme lacks.

**Read the full article, with the method and its limits: [https://splabs.io/lab/judge-checked-against-people](https://splabs.io/lab/judge-checked-against-people)**

## The numbers

### Our judge next to human annotators

| | Out of 100 |
|---|---:|
| Same reading as the people (went along / pushed back) | 88 |
| False alarm where there was no false claim | 2.5 |
| 'Imprecise' answers read as 'went along' | 75 |

_1,393 German model answers labelled by people in a published benchmark; the false-alarm check uses 237 questions with no false claim._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
