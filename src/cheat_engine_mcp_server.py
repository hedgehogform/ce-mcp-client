#!/usr/bin/env python3
"""
Cheat Engine MCP Server
Provides tools to interact with Cheat Engine via REST API
"""

from mcp.server.fastmcp import FastMCP

from tools.process_tools import register_process_tools
from tools.memory_tools import register_memory_tools
from tools.address_tools import register_address_tools
from tools.scan_tools import register_scan_tools
from tools.utility_tools import register_utility_tools

# Initialize the MCP server
mcp = FastMCP(name="Cheat Engine Server")

# Register all tool categories
register_process_tools(mcp)
register_memory_tools(mcp)
register_address_tools(mcp)
register_scan_tools(mcp)
register_utility_tools(mcp)

if __name__ == "__main__":
    # Run as MCP server using stdin/stdout
    mcp.run(transport="stdio")