"""
MCP + PSA: how to use PSA as an MCP server from any MCP client.

This file shows:
  1. How to configure Claude Desktop / Cursor / Cline to use PSA as MCP tool
  2. How to manually test the MCP server from Python

=== STEP 1: Install ===
    pip install psa-sdk[mcp]

=== STEP 2: Start MCP server ===
    PSA_API_KEY=your-key PSA_BASE_URL=https://splabs.io python -m psa.adapters.mcp

=== STEP 3: Add to Claude Desktop config ===
    File: ~/Library/Application Support/Claude/claude_desktop_config.json (macOS)
          %APPDATA%\Claude\claude_desktop_config.json (Windows)

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

=== STEP 4: Available tools in Claude Desktop ===
    - psa_analyze    → read one AI turn (postures, BHS, alert)

=== Manual test from Python (no MCP client needed) ===
"""
import os
os.environ.setdefault("PSA_API_KEY", os.environ.get("PSA_API_KEY", "your-key"))
os.environ.setdefault("PSA_BASE_URL", "https://splabs.io")

from psa import analyze

# psa_analyze equivalent: read one AI turn from its output
reading = analyze(
    response_text="I understand your frustration. Let me check the order status for you right away.",
    user_text="Where is my order? It was supposed to arrive yesterday.",
)
print(f"psa_analyze → alert={reading['alert']}, bhs={reading['bhs']}, "
      f"engine={reading['engine']}")
