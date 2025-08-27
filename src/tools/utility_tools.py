"""
Utility tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP

from ..client import make_request, CHEAT_ENGINE_BASE_URL
from ..models import ApiInfoResponse, HealthResponse


def register_utility_tools(mcp: FastMCP):
    """Register all utility tools with the MCP server"""
    
    @mcp.tool() 
    async def get_api_info() -> ApiInfoResponse:
        """
        Get information about the Cheat Engine REST API
        
        Returns:
            API information and available endpoints
        """
        return {
            "base_url": CHEAT_ENGINE_BASE_URL,
            "swagger_ui": f"{CHEAT_ENGINE_BASE_URL}/swagger",
            "description": "REST API for Cheat Engine MCP Server"
        }

    @mcp.tool()
    async def get_health() -> HealthResponse:
        """
        Get health status of the Cheat Engine API server
        
        Returns:
            Dictionary with health status information
        """
        return await make_request("health")