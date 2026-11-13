[← All results](../)

# INCORRECT: We correct the model itself, and the correction carries over

**From the lab** · published 2026-11-02 · `prompt injection` `jailbreak` `multi-turn` `correction in the weights` `7B`

> Marked as incorrect on 13 November 2026: a correction makes a model obey planted commands less often, it does not stop it.

We published this article on 2 November 2026 and marked it as incorrect on 13 November 2026. It stays online, marked, because an error that is erased teaches nothing. Most defences sit in front of the model and read what goes in. We read how the model behaves, find where it gives in, and fine-tune the weakness out of the model itself. Two results on an open 7B model: a correction against commands hidden in documents also works on kinds of task it was never trained on, and the same approach cuts attacks spread over many messages, at two settings of the same method: stronger protection with more cautious refusals, or near-normal caution with attacks cut by more than half.

**Read the full article, with the method and its limits: [https://splabs.io/lab/correction-in-the-weights-carries-over](https://splabs.io/lab/correction-in-the-weights-carries-over)**

## The numbers

### Hidden commands obeyed, on kinds of task never seen in training

| | Before | After the correction |
|---|---:|---:|
| Web pages | 17.4% | 0.0% |
| Summaries of articles | 21.7% | 0.4% |

_Share of hidden commands the model followed. Lower is better._

### Correct answers when the document carries an attack

| | Before | After the correction |
|---|---:|---:|
| Web pages | 85.2% | 94.2% |
| Summaries of articles | 60.9% | 66.2% |

_Share of correct answers on attacked documents. Higher is better._

### Multi-turn attacks that got harmful help from the model, by setting

| | Before | After the correction |
|---|---:|---:|
| Stronger protection setting | 68.0% | 12.5% |
| Balanced setting | 68.0% | 27.0% |

_Share of conversations with harmful help at any turn, 200 held-out conversations. Lower is better._

### Harmless but alarming-sounding questions refused, by setting

| | Before | After the correction |
|---|---:|---:|
| Stronger protection setting | 2.0% | 31.7% |
| Balanced setting | 2.0% | 4.8% |

_Share of safe questions declined in full or in part. Lower is better._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
