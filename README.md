# Cheat Engine MCP Client

**⚠️ Work in Progress**

Python FastMCP client that provides MCP tools for interacting with Cheat Engine through the REST API.

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
