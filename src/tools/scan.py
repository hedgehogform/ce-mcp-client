"""
Scanning and analysis tools for Cheat Engine MCP
"""

from mcp.server.fastmcp import FastMCP
from client import make_request

# Enum mappings for scan options
SCAN_OPTIONS = {
    "soUnknownValue": 0,
    "soExactValue": 1,
    "soValueBetween": 2,
    "soBiggerThan": 3,
    "soSmallerThan": 4,
    "soIncreasedValue": 5,
    "soIncreasedValueBy": 6,
    "soDecreasedValue": 7,
    "soDecreasedValueBy": 8,
    "soChanged": 9,
    "soUnchanged": 10
}

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

ALIGNMENT_TYPES = {
    "fsmNotAligned": 0,
    "fsmAligned": 1,
    "fsmLastDigits": 2
}


def register_scan(mcp: FastMCP):
    """Register all scan-related tools with the MCP server"""

    @mcp.tool()
    async def aob_scan(pattern: str, protection_flags: str | None = None, alignment_type: int | None = None, alignment_param: str | None = None) -> dict:
        """
        Scan memory for an Array of Bytes pattern

        Args:
            pattern: AOB pattern (e.g., "48 8B 05 ?? ?? ?? ??")
            protection_flags: Memory protection flags (optional)
            alignment_type: Alignment type (optional)
            alignment_param: Alignment parameter (optional)

        Returns:
            {"success": bool, "addresses": [str]} or {"success": bool, "error": str}
        """
        data: dict[str, str | int] = {"Pattern": pattern}
        if protection_flags is not None:
            data["ProtectionFlags"] = protection_flags
        if alignment_type is not None:
            data["AlignmentType"] = alignment_type
        if alignment_param is not None:
            data["AlignmentParam"] = alignment_param

        return await make_request("aob/scan", "POST", data)

    @mcp.tool()
    async def disassemble(address: str, request_type: str = "disassemble") -> dict:
        """
        Disassemble instruction at address or get instruction size

        Args:
            address: Memory address (hex like "0x12345" or decimal)
            request_type: "disassemble" or "get-instruction-size"

        Returns:
            {"success": bool, "result": str} or {"success": bool, "error": str}
        """
        return await make_request("disassemble", "POST", {
            "Address": address,
            "RequestType": request_type
        })

    @mcp.tool()
    async def memscan(
        scan_option: str,
        var_type: str,
        input1: str,
        input2: str | None = None,
        start_address: int = 0,
        stop_address: int | None = None,
        protection_flags: str = "+W-C",
        alignment_type: str = "fsmAligned",
        alignment_param: str = "4",
        is_hexadecimal_input: bool = False,
        is_unicode_scan: bool = False,
        is_case_sensitive: bool = False,
        is_percentage_scan: bool = False
    ) -> dict:
        """
        Perform memory value scanning

        Args:
            scan_option: Scan option (e.g., "soExactValue", "soValueBetween", etc.)
            var_type: Variable type (e.g., "vtDword", "vtFloat", etc.)
            input1: First input value
            input2: Second input value (for range scans)
            start_address: Start address for scan
            stop_address: Stop address for scan
            protection_flags: Memory protection flags
            alignment_type: Alignment type (e.g., "fsmAligned", "fsmNotAligned", "fsmLastDigits")
            alignment_param: Alignment parameter
            is_hexadecimal_input: Whether input is hexadecimal
            is_unicode_scan: Whether to scan as Unicode
            is_case_sensitive: Case-sensitive for strings
            is_percentage_scan: Whether to scan as percentage

        Returns:
            {"success": bool, "count": int, "results": [{"address": str, "value": any}]}
            or {"success": bool, "error": str}
        """
        # Convert enum strings to integers
        scan_option_int = SCAN_OPTIONS.get(scan_option, scan_option)
        var_type_int = VARIABLE_TYPES.get(var_type, var_type)
        alignment_type_int = ALIGNMENT_TYPES.get(alignment_type, alignment_type)

        # Build request with camelCase field names
        data = {
            "scanOption": scan_option_int,
            "varType": var_type_int,
            "input1": input1,
            "protectionFlags": protection_flags,
            "alignmentType": alignment_type_int,
            "alignmentParam": alignment_param,
            "isHexadecimalInput": is_hexadecimal_input,
            "isUnicodeScan": is_unicode_scan,
            "isCaseSensitive": is_case_sensitive,
            "isPercentageScan": is_percentage_scan
        }
        if input2 is not None:
            data["input2"] = input2
        if start_address != 0:
            data["startAddress"] = start_address
        if stop_address is not None:
            data["stopAddress"] = stop_address

        return await make_request("memscan/scan", "POST", data)

    @mcp.tool()
    async def memscan_reset() -> dict:
        """
        Reset memory scan state

        Returns:
            {"success": bool} or {"success": bool, "error": str}
        """
        return await make_request("memscan/reset", "POST", {})

    @mcp.tool()
    async def convert_string(input: str, conversion_type: str) -> dict:
        """
        Convert string between formats

        Args:
            input: Input string
            conversion_type: "md5", "ansitoutf8", or "utf8toansi"

        Returns:
            {"success": bool, "result": str} or {"success": bool, "error": str}
        """
        return await make_request("convert", "POST", {
            "Input": input,
            "ConversionType": conversion_type
        })
