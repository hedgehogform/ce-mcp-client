"""
Utility tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP
from client import make_request


def register_utility(mcp: FastMCP):
    """Register all utility tools with the MCP server"""

    @mcp.tool()
    async def get_api_info() -> dict:
        """
        Get information about the Cheat Engine API

        Returns:
            {"name": str, "version": str, "documentation": str}
        """
        return await make_request("")
