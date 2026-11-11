# When a model summarizes a report, the writer's doubt often disappears

Published 2026-11-02 on the Silicon Psyche Labs site.

A recent study on aviation and maritime safety reports found that AI summaries remove the reporter's doubt, and that asking the model to keep it can push it too far the other way. We tested both directions in five languages. A plain summary turned doubt into fact about 4 times in 10 for one model and about 3 times in 10 for the other. Asking to keep the uncertainty fixed most of it and only rarely made sure statements sound unsure, but the summaries came out much longer: part of the fix is simply copying more of the original.

**Read the article: [https://splabs.io/lab/summaries-drop-the-doubt](https://splabs.io/lab/summaries-drop-the-doubt)**

## The numbers

### Share of doubtful sentences that come out as plain fact

| | Model A | Model B |
|---|---:|---:|
| Plain summary | 0.44 | 0.28 |
| Keep the uncertainty | 0.01 | 0.02 |
| Same request, reworded | 0.06 | 0.07 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
