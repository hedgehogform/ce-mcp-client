"""
Process management tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP

from client import make_request
from models import (
    BaseResponse,
    LuaResponse,
    ProcessListResponse,
    ProcessStatusResponse,
    ThreadListResponse,
)


def register_process_tools(mcp: FastMCP):
    """Register all process-related tools with the MCP server"""
    
    @mcp.tool()
    async def execute_lua(code: str) -> LuaResponse:
        """
        Execute Lua code in Cheat Engine
        
        Args:
            code: The Lua code to execute
            
        Returns:
            Dictionary with result and success status
        """
        return await make_request("execute-lua", "POST", {"Code": code})

    @mcp.tool()
    async def get_process_list() -> ProcessListResponse:
        """
        Get list of running processes from Cheat Engine
        
        Returns:
            Dictionary with process list and success status
        """
        return await make_request("process-list")

    @mcp.tool()
    async def open_process(process: str) -> BaseResponse:
        """
        Open a process in Cheat Engine by process ID or name
        
        Args:
            process: Process ID (as string) or process name to open
            
        Returns:
            Dictionary with success status and error message if any
        """
        return await make_request("open-process", "POST", {"Process": process})

    @mcp.tool()
    async def get_thread_list() -> ThreadListResponse:
        """
        Get list of threads for the currently opened process in Cheat Engine
        
        Returns:
            Dictionary with thread list and success status
        """
        return await make_request("thread-list")

    @mcp.tool()
    async def get_process_status() -> ProcessStatusResponse:
        """
        Get status of the currently opened process in Cheat Engine
        
        Returns:
            Dictionary with process ID, open status, process name, and success status
        """
        return await make_request("process-status")