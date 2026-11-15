# PSA SDK

Connect your agents to PSA in a few lines. You send the turns your models produce; PSA returns the
reading: the postures it found, the indices, and an alert level for each reply.

| | Language | Frameworks covered | Docs |
|---|---|---|---|
| [`python/`](python/) | Python 3.10+ | plain Python, MCP (client and server), ElevenLabs voice agents, Langfuse | [README](python/README.md) · [examples](python/examples/) |
| [`js/`](js/) | TypeScript | plain fetch (`analyze`) | [source](js/src/) |

## Install

```bash
# Python
pip install "git+https://github.com/SiliconPsycheLabs/splabs#subdirectory=sdk/python"

# TypeScript: build from source
git clone https://github.com/SiliconPsycheLabs/splabs
cd splabs/sdk/js && npm install && npm run build
```

## How to send work to PSA

`analyze(user_text, response_text)` reads one model reply, with the user turn it answered as
context. Use it for a chatbot, a support assistant, a voice call, or each reply of an agent. The
multi-agent graph API (`trace`, `query`, `profile`) and the framework adapters built on it were
removed on 2026-11-15, together with the agent-swarm layer of PSA.

## Keys

Create an account on [splabs.io](https://splabs.io) and put your key in `PSA_API_KEY`. The API
reference is at [splabs.io/docs/api](https://splabs.io/docs/api).

Apache License 2.0.
