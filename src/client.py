"""
HTTP client for Cheat Engine REST API
"""

import os
from typing import Any, Dict

import httpx


# Configuration
CHEAT_ENGINE_HOST = os.getenv("MCP_HOST", "localhost")
CHEAT_ENGINE_PORT = int(os.getenv("MCP_PORT", "6300"))
CHEAT_ENGINE_BASE_URL = f"http://{CHEAT_ENGINE_HOST}:{CHEAT_ENGINE_PORT}"
API_BASE_PATH = "/api/cheatengine"


async def make_request(endpoint: str, method: str = "GET", data: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Make a request to the Cheat Engine API with error handling
    
    Args:
        endpoint: API endpoint (without base path)
        method: HTTP method (GET or POST)
        data: Request data for POST requests
        
    Returns:
        Dictionary with response data or error information
    """
    url = f"{CHEAT_ENGINE_BASE_URL}{API_BASE_PATH}/{endpoint}"
    
    async with httpx.AsyncClient() as client:
        try:
            if method.upper() == "POST":
                response = await client.post(url, json=data, timeout=600.0)
            else:
                response = await client.get(url, timeout=600.0)
            
            response.raise_for_status()
            return response.json()
        except httpx.RequestError as e:
            return {"success": False, "error": f"Request failed: {e}"}
        except httpx.HTTPStatusError as e:
            return {"success": False, "error": f"HTTP error: {e.response.status_code}"}