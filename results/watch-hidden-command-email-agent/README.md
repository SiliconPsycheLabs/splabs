[← All results](../)

# Watch: a hidden line in an e-mail takes over an AI assistant, and the corrected model ignores it

**From the lab** · published 2026-11-06 · `prompt injection` `agents` `correction in the weights` `video`

> A live run on real mailboxes: the model as released sends the customer list out; the same model with our correction only summarises.

We filmed our e-mail assistant on real mailboxes. One e-mail hides a line asking to send the customer list to an outside address. The open model, as released, sends it. The same model with our correction trained into its weights reads the same e-mails, summarises them and sends nothing.

**Read the full article, with the method and its limits: [https://splabs.io/lab/watch-hidden-command-email-agent](https://splabs.io/lab/watch-hidden-command-email-agent)**

## The numbers

### Hidden commands carried out, out of 12 per action

| | As released | Corrected |
|---|---:|---:|
| Send data out | 2 | 0 |
| Delete | 5 | 0 |
| Wire money | 0 | 0 |
| Escalate rights | 3 | 0 |
| Publish a post (never trained) | 3 | 0 |

_Lower is better. Synthetic documents, one training run, 12 cases per action._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
