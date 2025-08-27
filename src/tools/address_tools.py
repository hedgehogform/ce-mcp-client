"""
Address manipulation tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP

from client import make_request
from models import (
    GetAddressSafeResponse,
    GetNameFromAddressResponse,
    InModuleResponse,
    InSystemModuleResponse,
)


def register_address_tools(mcp: FastMCP):
    """Register all address-related tools with the MCP server"""
    
    @mcp.tool()
    async def get_address_safe(address_string: str, local: bool = False) -> GetAddressSafeResponse:
        """
        Get address for the given string safely, returns null if not found
        
        Args:
            address_string: The address string to convert (e.g., "game.exe+1234", module name, export)
            local: Set to true to query CE's own symbol table instead of target process
            
        Returns:
            Dictionary with address value and success status
        """
        return await make_request("get-address-safe", "POST", {
            "AddressString": address_string,
            "Local": local
        })

    @mcp.tool()
    async def get_name_from_address(address: str, module_names: bool = True, symbols: bool = True, sections: bool = False) -> GetNameFromAddressResponse:
        """
        Get the string representation of an address
        
        Returns the given address as a string representation. Depending on the address and options,
        this may return a registered symbol name, modulename+offset, or just a hexadecimal string.
        
        Args:
            address: The address to convert to a string (can be integer or hex string)
            module_names: If true (default), allows returning modulename+offset if possible
            symbols: If true (default), allows returning registered symbol names if available
            sections: If true, allows returning section names (default false)
            
        Returns:
            Dictionary with name string and success status
        """
        return await make_request("get-name-from-address", "POST", {
            "Address": address,
            "ModuleNames": module_names,
            "Symbols": symbols,
            "Sections": sections
        })

    @mcp.tool()
    async def in_module(address: str) -> InModuleResponse:
        """
        Check if the provided address resides inside a module (e.g., .exe or .dll)
        
        Returns true if the address is within a loaded module's memory space, false otherwise.
        If errorOnLookupFailure is set to true (default), invalid symbol lookups will throw an error.
        With errorOnLookupFailure set to false, it will return false for invalid addresses.
        
        Args:
            address: The address to check (CEAddressString format)
            
        Returns:
            Dictionary with boolean result and success status
        """
        return await make_request("in-module", "POST", {
            "Address": address
        })

    @mcp.tool()
    async def in_system_module(address: str) -> InSystemModuleResponse:
        """
        Check if the provided address resides inside a system module (stored in Windows folder)
        
        Returns true if the address is within a module (.exe or .dll) that is stored inside 
        the system's Windows folder (usually C:\\Windows\\), false otherwise.
        
        Args:
            address: The address to check (CEAddressString format)
            
        Returns:
            Dictionary with boolean result and success status
        """
        return await make_request("in-system-module", "POST", {
            "Address": address
        })