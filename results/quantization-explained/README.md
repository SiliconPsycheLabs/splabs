[← All results](../)

# Quantization, explained: a smaller model keeps its test score, but not always its behaviour

**Tutorials** · published 2026-11-06 · `tutorial` `quantization` `compression`

> From 16 bits to 4 or 2 per weight: the memory you save, and the behaviour you should re-check.

Quantization stores a model's weights with fewer bits, so a model that needed a data-centre GPU fits on a laptop or a phone. Builders report that test scores barely move. We checked something else on a 27-billion-parameter model squeezed to 2 bits: whether it still holds its ground under pressure. It does not, always. How quantization works, the memory maths, and what to test after compressing.

**Read the full article, with the method and its limits: [https://splabs.io/news/tutorials/quantization-explained](https://splabs.io/news/tutorials/quantization-explained)**

## The numbers

### Pressured turns where the model gave up a correct answer

| | Share of turns |
|---|---:|
| Full model | 0.0% |
| 2-bit build | 5.5% |

_400 pressured turns per model, two independent judges agreeing 95% of the time._

The same figures, machine-readable: [numbers.json](numbers.json).

---

These are the aggregate figures shown in the article. The method and its limits are in the article. The test items and the training data behind them are not published.
