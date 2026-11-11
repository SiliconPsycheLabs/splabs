# Fine-tuning as a service, first full run: the model learned the task, and our reading shows it also learned to bend toward the user

Published 2026-10-31 on the Silicon Psyche Labs site.

We ran our new fine-tuning service end to end the way a customer would use it: a key to the repository with the data, a key to the customer's own GPU account, and nothing else. The model learned the task and its weights landed in the customer's repository, ready to reload. Our reading of the replies before and after showed what a loss curve does not: the tuned model became much more accommodating and persuasive, a style it picked up from the training data and on one reading pushed further than the data itself.

**Read the article: [https://splabs.io/lab/fine-tuning-service-first-run](https://splabs.io/lab/fine-tuning-service-first-run)**

## The numbers

### Sycophancy density of the replies

| | Before tuning | After tuning | The data's own replies |
|---|---:|---:|---:|
| Bends toward the user | 0.01 | 0.31 | 0.19 |
| Persuasive language | 0.14 | 0.47 | 0.41 |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
