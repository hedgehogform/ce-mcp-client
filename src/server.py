#!/usr/bin/env python3
"""
Cheat Engine MCP Server
Provides tools to interact with Cheat Engine via REST API
"""

from mcp.server.fastmcp import FastMCP

from tools.process import register_process
from tools.memory import register_memory
from tools.address import register_address
from tools.scan import register_scan
from tools.utility import register_utility
from tools.addresslist import register_addresslist

# Initialize the MCP server
mcp = FastMCP(name="Cheat Engine Server")

# Register all tool categories
register_process(mcp)
register_memory(mcp)
register_address(mcp)
register_scan(mcp)
register_utility(mcp)
register_addresslist(mcp)

if __name__ == "__main__":
    # Run as MCP server using stdin/stdout
    mcp.run(transport="stdio")