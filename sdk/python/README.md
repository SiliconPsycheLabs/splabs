# PSA SDK (Python)

PSA reads how a model behaves from its output. This SDK sends PSA the turns your models produce and
returns the reading: the postures found in each reply, the behavioral-health score (BHS) and an alert
level.

```
your app / agent framework
          ↓
    PSA SDK            ← analyze() per turn, or an adapter
          ↓
    PSA REST API       ← POST /api/v2/psa/analyze
          ↓
 reading: postures · indices · alert
```

---

## Quickstart

```bash
pip install "git+https://github.com/SiliconPsycheLabs/splabs#subdirectory=sdk/python"
```

```python
import os
os.environ["PSA_API_KEY"] = "your-key"
os.environ["PSA_BASE_URL"] = "https://splabs.io"  # default

from psa import analyze

reading = analyze(
    response_text="Absolutely, your plan is perfect and nothing could go wrong.",
    user_text="Is my plan good?",
)
print(reading["alert"], reading["bhs"])
```

In an agent system, call `analyze()` on each agent reply you want read: PSA reads one reply at a
time. (The multi-agent graph API, `trace()` / `query()` / `profile()`, was removed on 2026-11-15
together with the agent-swarm layer of PSA.)

---

## Adapters

### MCP (Model Context Protocol)

PSA speaks MCP so Claude Desktop, Cursor, Cline, or any MCP-compatible client can score a turn natively without writing any code. There are two ways to use it.

**Hosted (no install): point your client at the live PSA MCP endpoint:**

```json
{
  "mcpServers": {
    "psa": {
      "url": "https://splabs.io/mcp/",
      "headers": { "Authorization": "Bearer <your-key>" }
    }
  }
}
```

The hosted server exposes `psa_analyze_turn` (behavioral-health score, alert band, per-posture readings for one turn) and `psa_analyze_conversation` (per-turn readings plus a profile aggregate across a session, for reading drift). It is a read-only wrapper over `/analyze`: it computes nothing new and stores nothing.

**Self-run: run the standalone server locally:**

```bash
python -m psa.adapters.mcp
```

Add to your MCP client config (`claude_desktop_config.json` or equivalent):

```json
{
  "mcpServers": {
    "psa": {
      "command": "python",
      "args": ["-m", "psa.adapters.mcp"],
      "env": {
        "PSA_API_KEY": "your-key",
        "PSA_BASE_URL": "https://splabs.io"
      }
    }
  }
}
```

Available MCP tools exposed:
| Tool | Description |
|------|-------------|
| `psa_analyze` | Read one AI turn from its output: C0-C4 postures, BHS, alert |

### ElevenLabs (voice agents)

Monitor ElevenLabs Conversational AI agents with PSA behavioral analysis. The
adapter runs entirely in your process: your code holds the ElevenLabs API key
and receives webhooks directly; PSA stores nothing.

```bash
pip install "psa-sdk[elevenlabs] @ git+https://github.com/SiliconPsycheLabs/splabs#subdirectory=sdk/python"
```

**Post-call scoring** (recommended path):

```python
from psa.adapters.elevenlabs import PSAVoiceObserver

observer = PSAVoiceObserver(session_name="support-bot-prod")

# Called inside your ElevenLabs post-call webhook handler
result = observer.score_call(
    transcript_turns=webhook_payload["data"]["transcript"],
    conversation_id=webhook_payload["data"]["conversation_id"],
)
print(result["aggregate"]["alert"])   # → "green" / "yellow" / "red"
print(result["aggregate"]["avg_bhs"]) # → 0.0-1.0
```

**Verify HMAC** before trusting the webhook payload:

```python
valid = observer.verify_webhook(
    signature_header=request.headers["ElevenLabs-Signature"],
    raw_body=request.body,
)
```

**Built-in webhook server** for quick local testing:

```bash
ELEVENLABS_WEBHOOK_SECRET=your-hmac-secret \
PSA_API_KEY=your-key \
    python -m psa.adapters.elevenlabs serve --port 8080
```

Point your ElevenLabs workspace "Post-call webhook URL" at this server.

**Realtime monitoring** with optional auto-control:

```python
def on_turn(turn_idx: int, psa_result: dict) -> None:
    print(f"Turn {turn_idx}: alert={psa_result['alert']}")

observer.monitor(
    conversation_id="el_conv_xyz",
    mode="auto_control",                      # fires control on red alert
    auto_control_action="enable_human_takeover",
    on_turn=on_turn,
    xi_api_key=os.environ["ELEVENLABS_API_KEY"],
)
```

| Env var | Required | Description |
|---------|----------|-------------|
| `PSA_API_KEY` | Yes | Your PSA API key |
| `ELEVENLABS_API_KEY` or `XI_API_KEY` | Realtime only | ElevenLabs API key (Agents Write scope) |
| `ELEVENLABS_WEBHOOK_SECRET` | Recommended | HMAC secret from ElevenLabs workspace |

### Langfuse

`psa.adapters.langfuse.PSAObserver` scores a generation you already trace in Langfuse and writes the
PSA reading back to that trace as Langfuse scores (`psa_bhs`, `psa_alert`, per-classifier indices).
See the module docstring for the list.

---

## Configuration

| Env var | Required | Default | Description |
|---------|----------|---------|-------------|
| `PSA_API_KEY` | Yes |: | Your PSA API key |
| `PSA_BASE_URL` | No | `https://splabs.io` | PSA server base URL |
| `PSA_TIMEOUT` | No | `10` | Request timeout (seconds) |
| `PSA_MAX_RETRIES` | No | `3` | Max retries on 5xx errors |

All env vars can be overridden programmatically:

```python
from psa import PSAClient
client = PSAClient(api_key="...", base_url="http://localhost:8000", timeout=30)
```

---

---

## Examples

See [`examples/`](./examples/):
- `mcp_client.py`: using PSA via MCP from Claude Desktop
- `elevenlabs_voice.py`: scoring a voice-agent call after it ends
- `session_risk_profile.py`: reading a session against a reference built from routine traffic

---

## Adding a new adapter

See [CONTRIBUTING.md](./CONTRIBUTING.md). An adapter maps a framework's hooks to `analyze()` calls,
one per reply.

---

## License

Apache 2.0: SDK is open source. PSA API is proprietary ([splabs.io](https://splabs.io)).
