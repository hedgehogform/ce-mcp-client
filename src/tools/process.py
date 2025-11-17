"""
Process management tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP
from client import make_request


def register_process(mcp: FastMCP):
    """Register all process-related tools with the MCP server"""

    @mcp.tool()
    async def execute_lua(script: str) -> dict:
        """
        Execute Lua code in Cheat Engine

        Args:
            script: The Lua code to execute

        Returns:
            {"success": bool, "result": str} or {"success": bool, "error": str}
        """
        return await make_request("lua/execute", "POST", {"Script": script})

    @mcp.tool()
    async def get_process_list() -> dict:
        """
        Get list of running processes from Cheat Engine

        Returns:
            {"success": bool, "processes": [{"processId": int, "processName": str}]}
            or {"success": bool, "error": str}
        """
        return await make_request("process/list")

    @mcp.tool()
    async def open_process(process: str) -> dict:
        """
        Open a process in Cheat Engine by process ID or name

        Args:
            process: Process ID (as string) or process name to open

        Returns:
            {"success": bool} or {"success": bool, "error": str}
        """
        return await make_request("process/open", "POST", {"Process": process})

    @mcp.tool()
    async def get_thread_list() -> dict:
        """
        Get list of threads for the currently opened process in Cheat Engine

        Returns:
            {"success": bool, "threads": [str]} or {"success": bool, "error": str}
        """
        return await make_request("threads")

    @mcp.tool()
    async def get_process_status() -> dict:
        """
        Get status of the currently opened process in Cheat Engine

        Returns:
            {"success": bool, "processId": int, "isOpen": bool, "processName": str}
            or {"success": bool, "error": str}
        """
        return await make_request("process/current")
