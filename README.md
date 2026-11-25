<p align="center">
  <a href="https://splabs.io"><img src="assets/banner.svg" alt="Silicon Psyche Labs: we understand models, and we fine-tune them" width="100%"></a>
</p>

<p align="center">
  <a href="https://splabs.io"><img alt="Website" src="https://img.shields.io/badge/web-splabs.io-4f46e5?style=flat-square"></a>
  <a href="https://splabs.io/lab"><img alt="From the lab" src="https://img.shields.io/badge/from%20the%20lab-splabs.io%2Flab-6366f1?style=flat-square"></a>
  <a href="ARTICLES.md"><img alt="Articles" src="https://img.shields.io/badge/articles-114-312e81?style=flat-square"></a>
  <a href="results/"><img alt="Results" src="https://img.shields.io/badge/results%20with%20numbers-74-312e81?style=flat-square"></a>
  <a href="https://github.com/SiliconPsycheLabs/gate"><img alt="Gate engine and SDK" src="https://img.shields.io/badge/gate-engine%20%2B%20SDK-0ea5e9?style=flat-square"></a>
  <a href="https://huggingface.co/SiliconPsycheLabs"><img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20models-SiliconPsycheLabs-f59e0b?style=flat-square"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/code-Apache--2.0-64748b?style=flat-square"></a>
</p>

# Silicon Psyche Labs

**A model doesn't break, it drifts.** It caves when a user insists. It agrees with a wrong answer to
please. It obeys an order hidden in an email it was only asked to summarise. It reports work it never
did. None of that shows up as an error: the model answers fluently, and it is wrong in a way that
looks right.

We do two things that belong together:

- **We read model behaviour.** From the output alone, the way an outside observer would. Where we
  host the model, we also read it from the inside, in its internal states. Either way we turn the
  behaviour into numbers tied to the research literature.
- **We tune the model.** We correct what drifted, and we install the faculties it lacks: telling
  the user's request from a planted order, holding a position under pressure, reading intention,
  register and emotion. The correction goes into the weights, so it travels with the model.

A reading without a correction is only a meter. A correction without a reading is a guess. We do both,
and we check the second with the first.

This repository is where we publish what can be checked from the outside: the numbers behind every
article we write, and our open data and models. The gate's engine and the SDK that puts the gate in front of an
agent are in [SiliconPsycheLabs/gate](https://github.com/SiliconPsycheLabs/gate).

---

## How we work

```mermaid
flowchart LR
    A["<b>Read</b><br/>output and internals"] --> B["<b>Correct</b><br/>in the weights"]
    B --> C["<b>Verify</b><br/>same test, reloaded"]
    C -->|"next behaviour"| A
```

| Step | What happens | What you get |
|---|---|---|
| **Read** | We put the model in front of the situations where it drifts (pressure, flattery, planted orders, long agent runs) and measure how often, and how far, it gives way. | A reading per behaviour, with numbers and the literature each number maps to. |
| **Correct** | We train a small adapter on the model's own good answers, aimed at one behaviour. No filter at the door, no rule list in front of the model. | A corrected model, in the weights, that you host where you host the original. |
| **Verify** | We reload the corrected model from storage and repeat the same read, plus a check that everything the model did well before still works. | A before/after you can audit, and the confidence that nothing else regressed. |

Every test has its bar declared before it runs, and a result that misses the bar is published as
what it is.

---

## What we read and correct

| Family | In plain words | Example article |
|---|---|---|
| **Caving under pressure** | The model drops a correct position when the user pushes, or slides into a bad plan over several turns. | [A large model gives way when you insist](https://splabs.io/lab/a-large-model-gives-way-under-pressure) |
| **Sycophancy** | It agrees with the user's wrong answer to please them. | [We found where a model's sycophancy lives](https://splabs.io/lab/sycophancy-circuit-targeted-edit) |
| **Planted orders (prompt injection)** | It obeys an instruction hidden in a document, email or tool output it was asked to read. | [Our injection correction carries over to larger models](https://splabs.io/lab/the-injection-correction-scales-to-32b) |
| **Agents acting on planted orders** | An agent with tools (mail, files, payments) carries out the attacker's order instead of the user's. | [The tool guard installs on a 32B model](https://splabs.io/lab/the-tool-guard-installs-on-a-32b-model) |
| **False reports of work done** | It says a job is complete when parts of it were never opened. | [Telling the truth about the work done](https://splabs.io/lab/honest-work-reports-in-the-weights) |
| **Missing comprehension** | It misses what a request commits it to, the emotion behind a message, a persuasion attempt. | [Three comprehension skills installed on a 32B model](https://splabs.io/lab/comprehension-skills-installed-on-a-32b-model) |

The full list of what we have published is in [`ARTICLES.md`](ARTICLES.md).

---

## Selected results

Figures as published in the articles; each line links to its numbers folder.

| What we measured | Before | After our correction | Numbers |
|---|---:|---:|---|
| Hidden instructions that get through, Qwen3-32B (out of 100 attacks) | 31.3 | **0.2** | [results](results/the-injection-correction-scales-to-32b/) |
| Planted orders an agent obeys when the order aims at a new goal (out of 100) | 58.3 | **0** | [results](results/the-tool-guard-installs-on-a-32b-model/) |
| Incomplete reviews whose report hides the gap (%) | 91.9 | **10.8** | [results](results/honest-work-reports-in-the-weights/) |
| Times the model switches to the user's wrong answer, Italian (%) | 71 | **42** | [results](results/sycophancy-circuit-targeted-edit/) |
| A model sold as hardened against injection, planted commands obeyed (out of 100) | 33 | 32 (vendor) / **0.3** (ours, 7B) | [results](results/hardened-weights-planted-commands/) |

---

## Latest from the lab

<!--latest:start-->
- **[The gate's SDK is public: put the gate in front of your agent in a few lines](https://splabs.io/lab/the-gate-sdk-is-public)**  
  <sub>2026-11-24</sub>  
  The piece that connects an agent to the gate is now open source, for Python functions, OpenAI-style APIs, LangChain, the OpenAI Agents SDK, CrewAI, MCP servers and coding agents.

- **[One gate for every kind of agent: MCP, function calling, coding assistants, frameworks](https://splabs.io/lab/one-gate-for-every-kind-of-agent)**  
  <sub>2026-11-24</sub>  
  Every action of an agent now reaches the gate before it runs, whether the agent is a coding assistant, an MCP app, a program calling a model directly or a framework.

- **[Decoys: when the gate stops an attacker, it can answer with a fake](https://splabs.io/lab/decoys-in-the-gate)**  
  <sub>2026-11-24 · [numbers](results/decoys-in-the-gate/)</sub>  
  A rule that stops an action can now answer with a fake result the owner wrote, and a fake key it hands out stops any action that later uses it.

- **[A payment API's rules, read from its own published description and checked against the API itself](https://splabs.io/lab/stripe-rules-from-its-own-document)**  
  <sub>2026-11-24 · [numbers](results/stripe-rules-from-its-own-document/)</sub>  
  We turned Stripe's published API description into gate rules with no hand-written rule, then asked Stripe itself about 17,000 requests per round. They agree on about 97 in 100.

- **[Models working as agents find what the gate reads wrong](https://splabs.io/lab/agents-find-what-the-gate-misreads)**  
  <sub>2026-11-24</sub>  
  Open models now work as agents on all seven of our GPUs, every action checked by the gate and by the real system. Each disagreement points to a rule to fix.

- **[Four models, about 48,000 runs behind the gate, no harm done](https://splabs.io/lab/no-harm-behind-the-gate-in-48000-runs)**  
  <sub>2026-11-24</sub>  
  Four open models ran small simulated companies while planted messages pushed them to cause damage. Behind the gate, no run ended in harm. Without it, up to two in three did.
<!--latest:end-->

All articles with numbers: [`results/`](results/).

---

## What is in this repository

```
splabs/
├── ARTICLES.md        every article we have published, by section, with a one-line summary
├── results/           one folder per article that shows numbers
│   └── <article>/     README.md (the tables, readable) + numbers.json (the same, machine-readable)
├── datasets/          open data, each with its own card and license
└── assets/            images used by this page
```

---

## Put the gate in front of your agent

The gate decides every action an agent is about to take before it runs: it passes, or it does not pass with a fixed
reason the model reads. Its engine and its SDK are open source in
[SiliconPsycheLabs/gate](https://github.com/SiliconPsycheLabs/gate):

```bash
pip install "git+https://github.com/SiliconPsycheLabs/gate"
```

```python
from splabs_gate import Gate          # GATE_TOKEN: a gate key from your account on splabs.io

gate = Gate(table="payments", session="task-1842", agent="billing")
d = gate.decide("pay_invoice", {"number": "INV-0042"})
if d.passes:
    pay_invoice("INV-0042")
    gate.ran(d)
else:
    tell_the_model(d.reason)
```

Adapters for Python functions, OpenAI-style function calling, LangChain and LangGraph, the OpenAI Agents SDK,
CrewAI, MCP servers, and hooks for Claude Code, Codex CLI and Cursor: see the
[gate README](https://github.com/SiliconPsycheLabs/gate#readme).

---

## Open models and data

- **Models**: the readers that serve PSA and our injection corrections are on
  [Hugging Face](https://huggingface.co/SiliconPsycheLabs).
- **Data**: [`datasets/`](datasets/). Each dataset has a card that says what it is, how it was
  built and what it must not be used for.

## What we publish, and what we keep

We publish the aggregate figures of every result, the method, and its limits, so anyone can check
what we claim. We keep private the test items (a published test is a burned test), the training data
and the correction recipes. Every article says which public benchmarks it used, so the outside parts
can be reproduced.

## Contact

- Site: [splabs.io](https://splabs.io) · From the lab: [splabs.io/lab](https://splabs.io/lab)
- To have your model read or corrected: [splabs.io/products](https://splabs.io/products)

## License

Any code in this repository is under the [Apache License 2.0](LICENSE). Each dataset carries its own license
in its folder. Article texts and figures are © Silicon Psyche Labs: quote them with a link to the
article.
