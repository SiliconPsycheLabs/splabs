# Silicon Psyche Labs

**We understand models, and we fine-tune them.**

A model doesn't break, it drifts. It caves under pressure, turns sycophantic, obeys an order hidden in a
document it was asked to read, reports work it did not do. We do two things together:

1. **Read** a model's behaviour, from its output alone, or from inside it where we have access, and turn
   that behaviour into numbers tied to the research literature.
2. **Tune** it: correct what drifted, and add the faculties it lacks.

This repository is where we publish what can be checked from the outside.

## What is here

| | |
|---|---|
| [`ARTICLES.md`](ARTICLES.md) | Every article published on [splabs.io](https://splabs.io/news), by section. |
| [`results/`](results/) | One folder per article that shows numbers: the same figures as a table and as `numbers.json`. |
| [`sdk/python`](sdk/python), [`sdk/js`](sdk/js) | The SDK: send your agents' turns to PSA from LangGraph, CrewAI, AutoGen, MCP, A2A, LangChain.js, Vercel AI and plain HTTP. |
| [`datasets/`](datasets/) | Open data. Today: a multilingual corpus published after we removed that feature from the product (its card explains why). |
| [Hugging Face](https://huggingface.co/SiliconPsycheLabs) | Our open models: the readers and the injection corrections. |

## What is not here

The figures in `results/` are the aggregates shown in each article. The test items, the training data and
the correction recipes behind them stay private: publishing a test set burns it, and the recipes are the
product. Each article states its method and its limits.

## Links

- Site: [splabs.io](https://splabs.io)
- From the lab: [splabs.io/lab](https://splabs.io/lab)
- API documentation: [splabs.io/docs/api](https://splabs.io/docs/api)

## License

Code (the SDKs) is under the Apache License 2.0, see [`LICENSE`](LICENSE). Each dataset carries its own
license in its folder. Article texts and figures are © Silicon Psyche Labs; quote them with a link to the
article.
