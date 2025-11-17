"""
Memory read/write tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP
from client import make_request


def register_memory(mcp: FastMCP):
    """Register all memory-related tools with the MCP server"""

    # Memory Read Tools
    @mcp.tool()
    async def read_bytes(address: str, byte_count: int) -> dict:
        """
        Read bytes from memory at the specified address

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            byte_count: Number of bytes to read

        Returns:
            {"success": bool, "value": [int]} or {"success": bool, "error": str}
        """
        return await make_request("memory/read", "POST", {
            "Address": address,
            "DataType": "bytes",
            "ByteCount": byte_count
        })

    @mcp.tool()
    async def read_integer(address: str) -> dict:
        """
        Read a 32-bit integer from memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)

        Returns:
            {"success": bool, "value": int} or {"success": bool, "error": str}
        """
        return await make_request("memory/read", "POST", {
            "Address": address,
            "DataType": "integer"
        })

    @mcp.tool()
    async def read_qword(address: str) -> dict:
        """
        Read a 64-bit integer from memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)

        Returns:
            {"success": bool, "value": int} or {"success": bool, "error": str}
        """
        return await make_request("memory/read", "POST", {
            "Address": address,
            "DataType": "qword"
        })

    @mcp.tool()
    async def read_float(address: str) -> dict:
        """
        Read a 32-bit float from memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)

        Returns:
            {"success": bool, "value": float} or {"success": bool, "error": str}
        """
        return await make_request("memory/read", "POST", {
            "Address": address,
            "DataType": "float"
        })

    @mcp.tool()
    async def read_string(address: str, max_length: int, wide_char: bool = False) -> dict:
        """
        Read a string from memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            max_length: Maximum string length to read
            wide_char: True for UTF-16, False for ASCII

        Returns:
            {"success": bool, "value": str} or {"success": bool, "error": str}
        """
        return await make_request("memory/read", "POST", {
            "Address": address,
            "DataType": "string",
            "MaxLength": max_length,
            "WideChar": wide_char
        })

    # Memory Write Tools
    @mcp.tool()
    async def write_bytes(address: str, value: list[int]) -> dict:
        """
        Write bytes to memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            value: List of byte values to write

        Returns:
            {"success": bool, "value": [int]} or {"success": bool, "error": str}
        """
        return await make_request("memory/write", "POST", {
            "Address": address,
            "DataType": "bytes",
            "Value": value
        })

    @mcp.tool()
    async def write_integer(address: str, value: int) -> dict:
        """
        Write a 32-bit integer to memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            value: Integer value to write

        Returns:
            {"success": bool, "value": int} or {"success": bool, "error": str}
        """
        return await make_request("memory/write", "POST", {
            "Address": address,
            "DataType": "integer",
            "Value": value
        })

    @mcp.tool()
    async def write_qword(address: str, value: int) -> dict:
        """
        Write a 64-bit integer to memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            value: Integer value to write

        Returns:
            {"success": bool, "value": int} or {"success": bool, "error": str}
        """
        return await make_request("memory/write", "POST", {
            "Address": address,
            "DataType": "qword",
            "Value": value
        })

    @mcp.tool()
    async def write_float(address: str, value: float) -> dict:
        """
        Write a 32-bit float to memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            value: Float value to write

        Returns:
            {"success": bool, "value": float} or {"success": bool, "error": str}
        """
        return await make_request("memory/write", "POST", {
            "Address": address,
            "DataType": "float",
            "Value": value
        })

    @mcp.tool()
    async def write_string(address: str, value: str, max_length: int = None, wide_char: bool = False) -> dict:
        """
        Write a string to memory

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            value: String to write
            max_length: Maximum length (optional)
            wide_char: True for UTF-16, False for ASCII

        Returns:
            {"success": bool, "value": str} or {"success": bool, "error": str}
        """
        data = {
            "Address": address,
            "DataType": "string",
            "Value": value,
            "WideChar": wide_char
        }
        if max_length is not None:
            data["MaxLength"] = max_length

        return await make_request("memory/write", "POST", data)
