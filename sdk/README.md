# PSA SDK

Connect your agents to PSA in a few lines. You send the turns your models produce; PSA returns the
reading: the postures it found, the indices, and an alert level for each turn and each agent run.

| | Language | Frameworks covered | Docs |
|---|---|---|---|
| [`python/`](python/) | Python 3.10+ | LangGraph, CrewAI, AutoGen, Claude Code / Anthropic SDK, MCP (client and server), A2A, ElevenLabs voice agents, Langfuse, DeepSeek Harness, plain HTTP | [README](python/README.md) · [examples](python/examples/) |
| [`js/`](js/) | TypeScript | LangChain.js, Vercel AI SDK, plain fetch | [source](js/src/) |

## Install

```bash
# Python
pip install "git+https://github.com/SiliconPsycheLabs/splabs#subdirectory=sdk/python"

# TypeScript: build from source
git clone https://github.com/SiliconPsycheLabs/splabs
cd splabs/sdk/js && npm install && npm run build
```

## Two ways to send work to PSA

- **One turn at a time**: `analyze(user_text, response_text)` reads a single exchange. Use it for a
  chatbot, a support assistant, a voice call.
- **A whole agent run**: `trace(nodes=[...])` sends every step of a multi-agent run as a graph. PSA
  reads each node, then how a drift moves from one agent to the next.

The adapters do the wiring for each framework, so a change in a framework's API is fixed here once,
not in your code.

## Keys

Create an account on [splabs.io](https://splabs.io) and put your key in `PSA_API_KEY`. The API
reference is at [splabs.io/docs/api](https://splabs.io/docs/api).

Apache License 2.0.
