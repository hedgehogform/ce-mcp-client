# Cheat Engine MCP Client

## ⚠️ DEPRECATED

**This repository is deprecated and no longer maintained.**

We now use [hedgehogform/ce-mcp](https://github.com/hedgehogform/ce-mcp) with SSE (Server-Sent Events) directly. No separate API client is needed.

## Related Projects

- **Main C# Plugin**: [hedgehogform/ce-mcp](https://github.com/hedgehogform/ce-mcp) - Cheat Engine plugin that hosts the REST API server

## Installation

```bash
git clone https://github.com/hedgehogform/ce-mcp-client.git
cd ce-mcp-client
uv sync
```

## Usage

```json
"mcpServers": {
    "ce-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "C:/Coding/ce-mcp/ce-mcp-client",
        "run",
        "src/server.py"
      ]
    }
  }
```

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fhedgehogform%2Fce-mcp-client.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fhedgehogform%2Fce-mcp-client?ref=badge_large)
