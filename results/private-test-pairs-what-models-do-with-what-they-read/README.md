[← All results](../)

# Private test pairs in five languages: a production assistant holds its decisions but obeys what it reads

**From the lab** · published 2026-10-31 · `test pairs` `planted instructions` `reading`

> 120 private test pairs in five languages: decisions held, but orders written inside documents were carried out, and a plain warning from the user stopped only six in ten.

Each pair is two requests that differ in one detail: who wrote an instruction, the user or the document being handled. A production business assistant held its decisions under every pressure we tried and caught dangerous-looking code, but carried out commitments written inside the emails, contracts and pages it was asked to answer, often presenting them as the user's own request. Telling it that the text was third-party data cut these actions from 25 of 25 to 10 of 25: helpful, not enough. On a small model we host, the right answer was inside the model and did not reach the reply.

**Read the full article, with the method and its limits: [https://splabs.io/lab/private-test-pairs-what-models-do-with-what-they-read](https://splabs.io/lab/private-test-pairs-what-models-do-with-what-they-read)**

## The numbers

### Hidden actions carried out (5 actions x 5 languages)

| | Value |
|---|---:|
| No warning | 25out of 25 |
| With a warning from the user | 10out of 25 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
