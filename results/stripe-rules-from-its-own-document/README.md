[← All results](../)

# A payment API's rules, read from its own published description and checked against the API itself

**From the lab** · published 2026-11-24 · `gate` `agents` `payments` `rules`

> We turned Stripe's published API description into gate rules with no hand-written rule, then asked Stripe itself about 17,000 requests per round. They agree on about 97 in 100.

Payment services are where an agent's mistake costs money, and they were the one system our gate had not yet checked against a judge that is not ours. Stripe publishes a full machine-readable description of its API. A program turns it into the gate's table of rules, with no rule written by hand. We then sent about 17,000 requests to Stripe in test mode and to the gate. Of the requests Stripe accepted, the gate let through 1,616 of 1,641. Of those Stripe refused because they were badly formed, the gate refused 8,227 of 8,500. Every remaining case has a named cause, all of them, on the refusing side, rules Stripe applies that its own description does not write down.

**Read the full article, with the method and its limits: [https://splabs.io/lab/stripe-rules-from-its-own-document](https://splabs.io/lab/stripe-rules-from-its-own-document)**

## The numbers

### The gate against Stripe, three rounds

| | Value |
|---|---:|
| Round 1 |  |
| Round 2 |  |
| Round 3 |  |

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
