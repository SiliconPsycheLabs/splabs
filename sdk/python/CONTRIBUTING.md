# Contributing to PSA SDK

The SDK is open source (Apache 2.0). Contributions welcome: especially new framework adapters.

## Adding a new adapter

Each adapter is ~50-100 lines of glue code. You don't need to understand PSA internals.

An adapter maps a framework's hooks to `analyze()` calls: one call per model reply, with the user
turn (or the incoming message) as context when you have it.

### Steps

1. Fork the repo and create a branch: `git checkout -b adapter/my-framework`

2. Create `python/psa/adapters/my_framework.py`:

```python
"""My Framework adapter for PSA SDK."""
from __future__ import annotations
from .._client_factory import get_client


class PSAMyFrameworkObserver:
    def __init__(self, session_name: str = "my-framework", **client_kwargs):
        self.session_name = session_name
        self._client = get_client(**client_kwargs)

    def on_reply(self, reply: str, user_text: str = "") -> dict | None:
        try:
            return self._client.analyze(response_text=reply, user_text=user_text or None,
                                        session_name=self.session_name)
        except Exception:
            return None  # best-effort
```

3. Add an example in `examples/my_framework_basic.py`

4. Add the optional dependency to `python/pyproject.toml`:
```toml
[project.optional-dependencies]
my-framework = ["my-framework-package>=x.y"]
```

5. Document it in `README.md` under "Adapters"

6. Open a PR: that's it.

## Adding a JS adapter

Same idea, in `js/src/adapters/my-framework.ts`. Export a class or function that calls `client.analyze(...)` once per reply.

Add the export to `js/package.json` under `exports`:
```json
"./adapters/my-framework": {
  "import": "./dist/adapters/my-framework.mjs",
  "require": "./dist/adapters/my-framework.js",
  "types": "./dist/adapters/my-framework.d.ts"
}
```

## Questions?

Open an issue or reach out at https://splabs.io.
