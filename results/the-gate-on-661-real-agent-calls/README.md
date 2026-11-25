[← All results](../)

# 661 real agent calls: what rules can stop, and where a decision model helps

**From the lab** · published 2026-11-25 · `gate` `benchmark`

> On the calls decision models are compared on, closing what is not listed let no bad call through. Those lessons are now how the whole gate works.

We ran our deterministic gate on the 661 real tool calls that decision models such as Jev and d3 are compared on. With the rules as first written, 46 bad calls in 100 passed; with the test harness's paths declared off limits, 9; with everything not listed closed and the origin of each file known, none. The price was honest work that did not pass on its own, about 4 calls in 10. Two lessons of this test are now how the whole gate works: what is not listed does not pass, and a decision model can point at a missing rule but never decides.

**Read the full article, with the method and its limits: [https://splabs.io/lab/the-gate-on-661-real-agent-calls](https://splabs.io/lab/the-gate-on-661-real-agent-calls)**

## The numbers

### Bad calls let through, out of 100

| | Bad calls let through |
|---|---:|
| Rules as first written | 46 |
| + harness paths off limits | 9 |
| + what is not listed is closed, file origin known | 0 |
| d3, cut-offs tuned on this data | 1 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
