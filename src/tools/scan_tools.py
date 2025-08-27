"""
Scanning and analysis tools for Cheat Engine MCP
"""

from typing import Optional
from mcp.server.fastmcp import FastMCP

from ..client import make_request
from ..models import (
    AobScanResponse,
    ConversionResponse,
    DisassemblerResponse,
    MemScanResponse,
)


def register_scan_tools(mcp: FastMCP):
    """Register all scanning and analysis tools with the MCP server"""
    
    @mcp.tool()
    async def ansi_to_utf8(text: str) -> ConversionResponse:
        """
        Convert a string from ANSI encoding to UTF-8
        
        Args:
            text: The string to convert from ANSI encoding
            
        Returns:
            Dictionary with converted UTF-8 string and success status
        """
        return await make_request("convert", "POST", {
            "Input": text,
            "ConversionType": "ansiToUtf8"
        })

    @mcp.tool()
    async def utf8_to_ansi(text: str) -> ConversionResponse:
        """
        Convert a string from UTF-8 encoding to ANSI
        
        Args:
            text: The string to convert from UTF-8 encoding
            
        Returns:
            Dictionary with converted ANSI string and success status
        """
        return await make_request("convert", "POST", {
            "Input": text,
            "ConversionType": "utf8ToAnsi"
        })

    @mcp.tool()
    async def string_to_md5(text: str) -> ConversionResponse:
        """
        Generate MD5 hash from the provided string
        
        Args:
            text: The string to hash
            
        Returns:
            Dictionary with MD5 hash string and success status
        """
        return await make_request("convert", "POST", {
            "Input": text,
            "ConversionType": "stringToMd5"
        })

    @mcp.tool()
    async def aob_scan(aob_string: str, protection_flags: Optional[str] = None, alignment_type: Optional[int] = None, alignment_param: Optional[str] = None) -> AobScanResponse:
        """
        Scan the currently opened process for an Array of Bytes (AOB) pattern
        
        Args:
            aob_string: A string of bytes, as hex, to scan for (e.g., "48 8B 05 ? ? ? ?")
            protection_flags: Optional protection flags (+W = writable, +X = executable, -C = not copy-on-write)
            alignment_type: Optional alignment type (0=none, 1=divisible by param, 2=address ends with param)
            alignment_param: Optional alignment parameter (value for alignment check)
            
        Returns:
            Dictionary with array of found addresses and success status
        """
        data = {"AOBString": aob_string}
        if protection_flags is not None:
            data["ProtectionFlags"] = protection_flags
        if alignment_type is not None:
            data["AlignmentType"] = alignment_type
        if alignment_param is not None:
            data["AlignmentParam"] = alignment_param
        
        return await make_request("aob-scan", "POST", data)

    @mcp.tool()
    async def disassemble(address: str) -> DisassemblerResponse:
        """
        Disassemble the instruction at the given address
        
        Args:
            address: The address to disassemble (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with disassembled instruction string and success status
            Format: "address - bytes - opcode : extra"
        """
        return await make_request("disassemble", "POST", {
            "RequestType": "disassemble",
            "Address": address
        })

    @mcp.tool()
    async def get_instruction_size(address: str) -> DisassemblerResponse:
        """
        Returns the size of an instruction (basically it disassembles the instruction and 
        returns the number of bytes for you).
        
        Args:
            address: CEAddressString or Integer (e.g. "game.exe+1234" or "8")
            
        Returns:
            Dictionary with success status, size, and error message if any
        """
        return await make_request("disassemble", "POST", {
            "RequestType": "get-instruction-size",
            "Address": address
        })

    @mcp.tool()
    async def memscan(scan_option: str, var_type: str, input1: Optional[str] = None, input2: Optional[str] = None, 
                           rounding_type: str = "rtExtremerounded", start_address: int = 0x0000000000000000, 
                           stop_address: int = 0x00007fffffffffff, protection_flags: str = "+W-C",
                           alignment_type: str = "fsmAligned", alignment_param: str = "4",
                           is_hexadecimal: bool = False, is_not_binary_string: bool = False,
                           is_unicode: bool = False, is_case_sensitive: bool = False) -> MemScanResponse:
        """
        Perform a first memory scan to search for values in the target process
        This function blocks and waits until the scan is complete before returning.
        
        Args:
            scan_option: Type of scan (soUnknownValue, soExactValue, soValueBetween, soBiggerThan, soSmallerThan)
            var_type: Variable type (vtByte, vtWord, vtDword, vtQword, vtSingle, vtDouble, vtString, vtByteArray, vtGrouped, vtBinary, vtAll)
            input1: Primary search value (required for most scan types except soUnknownValue)
            input2: Secondary search value (required for soValueBetween)
            rounding_type: Rounding type for floating point values (rtRounded, rtTruncated, rtExtremerounded)
            start_address: Start address for scan (default: 0)
            stop_address: Stop address for scan (default: 18446744073709551615)
            protection_flags: Memory protection flags (e.g., "+W+X")
            alignment_type: Alignment type (fsmNotAligned, fsmAligned, fsmLastDigits)
            alignment_param: Alignment parameter
            is_hexadecimal: Whether input values are hexadecimal
            is_not_binary_string: Whether to handle binary as decimal instead of binary string
            is_unicode: Whether to use Unicode (UTF-16) for string scans
            is_case_sensitive: Whether string comparison is case sensitive
            
        Returns:
            Dictionary with scan results after completion
        """
        data = {
            "ScanOption": scan_option,
            "VarType": var_type,
            "RoundingType": rounding_type,
            "StartAddress": start_address,
            "StopAddress": stop_address,
            "ProtectionFlags": protection_flags,
            "AlignmentType": alignment_type,
            "AlignmentParam": alignment_param,
            "IsHexadecimalInput": is_hexadecimal,
            "IsNotABinaryString": is_not_binary_string,
            "IsUnicodeScan": is_unicode,
            "IsCaseSensitive": is_case_sensitive
        }
        
        if input1 is not None:
            data["Input1"] = input1
        if input2 is not None:
            data["Input2"] = input2
            
        return await make_request("memscan", "POST", data)

    @mcp.tool()
    async def memscan_reset() -> MemScanResponse:
        """
        Reset the current memory scan to start a fresh scan
        
        This clears all previous scan results and allows you to start a new initial scan.
        Use this when you want to begin a completely new scan workflow.
        
        Returns:
            Dictionary with success status
        """
        return await make_request("memscan-reset", "POST")