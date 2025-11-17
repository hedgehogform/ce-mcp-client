"""
Address resolution tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP
from client import make_request


def register_address(mcp: FastMCP):
    """Register all address-related tools with the MCP server"""

    @mcp.tool()
    async def resolve_address(address_string: str, local: bool = False) -> dict:
        """
        Resolve an address from a string expression

        Args:
            address_string: Address string to resolve (e.g., "game.exe+12345", "MyModule+offset")
            local: Whether to resolve in CE's own process memory

        Returns:
            {"success": bool, "address": str} or {"success": bool, "error": str}
        """
        return await make_request("address/resolve", "POST", {
            "AddressString": address_string,
            "Local": local
        })
