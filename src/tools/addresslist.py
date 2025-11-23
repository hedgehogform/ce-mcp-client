"""
Address List tools for Cheat Engine MCP
Manage cheat table entries (memory records)
"""

from mcp.server.fastmcp import FastMCP
from client import make_request

# Variable type mappings (same as in scan.py)
VARIABLE_TYPES = {
    "vtByte": 0,
    "vtWord": 1,
    "vtDword": 2,
    "vtQword": 3,
    "vtSingle": 4,
    "vtDouble": 5,
    "vtString": 6,
    "vtByteArray": 7,
    "vtGrouped": 8,
    "vtBinary": 9,
    "vtAll": 10
}


def register_addresslist(mcp: FastMCP):
    """Register all address list tools with the MCP server"""

    @mcp.tool()
    async def get_address_list() -> dict:
        """
        Get all memory records in the cheat table

        Returns:
            {"success": bool, "count": int, "records": [{"id": int, "index": int, "description": str, "address": str, "value": str, "active": bool}]}
            or {"success": bool, "error": str}
        """
        return await make_request("addresslist", "GET")

    @mcp.tool()
    async def add_address_list_entry(
        description: str = "New Entry",
        address: str = "0",
        var_type: str = "vtDword",
        value: str = "0"
    ) -> dict:
        """
        Add a new memory record to the cheat table

        Args:
            description: Description of the entry
            address: Memory address (e.g., "0x12345" or "game.exe+1234")
            var_type: Variable type (vtByte, vtWord, vtDword, vtQword, vtSingle, vtDouble, vtString, vtByteArray)
            value: Initial value

        Returns:
            {"success": bool, "record": {"id": int, "description": str, "address": str, "value": str}}
            or {"success": bool, "error": str}
        """
        var_type_int = VARIABLE_TYPES.get(var_type, var_type)

        return await make_request("addresslist/add", "POST", {
            "description": description,
            "address": address,
            "varType": var_type_int,
            "value": value
        })

    @mcp.tool()
    async def update_address_list_entry(
        id: int | None = None,
        index: int | None = None,
        description: str | None = None,
        new_description: str | None = None,
        new_address: str | None = None,
        new_var_type: str | None = None,
        new_value: str | None = None,
        active: bool | None = None
    ) -> dict:
        """
        Update a memory record in the cheat table (find by id, index, or description)

        Args:
            id: Record ID to find
            index: Record index to find
            description: Record description to find
            new_description: New description to set
            new_address: New address to set
            new_var_type: New variable type to set
            new_value: New value to set
            active: Set active/frozen state (true = frozen)

        Returns:
            {"success": bool, "record": {"id": int, "description": str, "address": str, "value": str, "active": bool}}
            or {"success": bool, "error": str}
        """
        data = {}
        if id is not None:
            data["id"] = id
        if index is not None:
            data["index"] = index
        if description is not None:
            data["description"] = description
        if new_description is not None:
            data["newDescription"] = new_description
        if new_address is not None:
            data["newAddress"] = new_address
        if new_var_type is not None:
            data["newVarType"] = VARIABLE_TYPES.get(new_var_type, new_var_type)
        if new_value is not None:
            data["newValue"] = new_value
        if active is not None:
            data["active"] = active

        return await make_request("addresslist/update", "POST", data)

    @mcp.tool()
    async def delete_address_list_entry(
        id: int | None = None,
        index: int | None = None,
        description: str | None = None
    ) -> dict:
        """
        Delete a memory record from the cheat table (find by id, index, or description)

        Args:
            id: Record ID to delete
            index: Record index to delete
            description: Record description to delete

        Returns:
            {"success": bool} or {"success": bool, "error": str}
        """
        data = {}
        if id is not None:
            data["id"] = id
        if index is not None:
            data["index"] = index
        if description is not None:
            data["description"] = description

        return await make_request("addresslist/delete", "POST", data)

    @mcp.tool()
    async def clear_address_list() -> dict:
        """
        Clear all memory records from the cheat table

        Returns:
            {"success": bool} or {"success": bool, "error": str}
        """
        return await make_request("addresslist/clear", "POST", {})
