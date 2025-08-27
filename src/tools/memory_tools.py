"""
Memory read/write tools for Cheat Engine MCP
"""

from typing import List
from mcp.server.fastmcp import FastMCP

from ..client import make_request
from ..models import BaseResponse, MemoryReadResponse


def register_memory_tools(mcp: FastMCP):
    """Register all memory-related tools with the MCP server"""
    
    # Memory Read Tools
    @mcp.tool()
    async def read_bytes(address: str, byte_count: int, return_as_table: bool = True) -> MemoryReadResponse:
        """
        Read bytes from memory at the specified address in the currently opened process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            byte_count: Number of bytes to read
            return_as_table: If True, returns bytes as array. If False, returns multiple values
            
        Returns:
            Dictionary with bytes array/values and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "bytes",
            "ByteCount": byte_count,
            "ReturnAsTable": return_as_table
        })

    @mcp.tool()
    async def read_bytes_local(address: str, byte_count: int, return_as_table: bool = True) -> MemoryReadResponse:
        """
        Read bytes from memory at the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            byte_count: Number of bytes to read
            return_as_table: If True, returns bytes as array. If False, returns multiple values
            
        Returns:
            Dictionary with bytes array/values and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "byteslocal",
            "ByteCount": byte_count,
            "ReturnAsTable": return_as_table
        })

    @mcp.tool()
    async def read_small_integer(address: str, signed: bool = False) -> MemoryReadResponse:
        """
        Read a 16-bit integer (small integer) from the specified address in the target process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            signed: If True, interpret value as signed. If False, interpret as unsigned.
            
        Returns:
            Dictionary with integer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "smallinteger",
            "Signed": signed
        })

    @mcp.tool()
    async def read_small_integer_local(address: str) -> MemoryReadResponse:
        """
        Read a 16-bit integer from the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with integer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "smallintegerlocal"
        })

    @mcp.tool()
    async def read_integer(address: str, signed: bool = False) -> MemoryReadResponse:
        """
        Read a 32-bit integer from the specified address in the target process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            signed: If True, interpret value as signed. If False, interpret as unsigned.
            
        Returns:
            Dictionary with integer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "integer",
            "Signed": signed
        })

    @mcp.tool()
    async def read_integer_local(address: str, signed: bool = False) -> MemoryReadResponse:
        """
        Read a 32-bit integer from the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            signed: If True, interpret value as signed. If False, interpret as unsigned.
            
        Returns:
            Dictionary with integer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "integerlocal",
            "Signed": signed
        })

    @mcp.tool()
    async def read_qword(address: str) -> MemoryReadResponse:
        """
        Read a 64-bit integer from the specified address in the target process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with integer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "qword"
        })

    @mcp.tool()
    async def read_qword_local(address: str) -> MemoryReadResponse:
        """
        Read a 64-bit integer from the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with integer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "qwordlocal"
        })

    @mcp.tool()
    async def read_pointer(address: str) -> MemoryReadResponse:
        """
        Read a pointer-sized integer from the specified address in the target process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with pointer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "pointer"
        })

    @mcp.tool()
    async def read_pointer_local(address: str) -> MemoryReadResponse:
        """
        Read a pointer-sized integer from the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with pointer value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "pointerlocal"
        })

    @mcp.tool()
    async def read_float(address: str) -> MemoryReadResponse:
        """
        Read a single precision (32-bit) floating point value from the specified address in the target process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with float value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "float"
        })

    @mcp.tool()
    async def read_float_local(address: str) -> MemoryReadResponse:
        """
        Read a single precision (32-bit) floating point value from the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with float value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "floatlocal"
        })

    @mcp.tool()
    async def read_double(address: str) -> MemoryReadResponse:
        """
        Read a double precision (64-bit) floating point value from the specified address in the target process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with double value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "double"
        })

    @mcp.tool()
    async def read_double_local(address: str) -> MemoryReadResponse:
        """
        Read a double precision (64-bit) floating point value from the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            
        Returns:
            Dictionary with double value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "doublelocal"
        })

    @mcp.tool()
    async def read_string(address: str, max_length: int, wide_char: bool = False) -> MemoryReadResponse:
        """
        Read a string from the specified address in the target process
        
        Args:
            address: Memory address to read from (as string, can be hex like "0x12345" or decimal)
            max_length: Maximum number of characters to read
            wide_char: If True, read as widechar (UTF-16/Unicode). If False, read as ASCII/ANSI.
            
        Returns:
            Dictionary with string value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "string",
            "MaxLength": max_length,
            "WideChar": wide_char
        })

    @mcp.tool()
    async def read_string_local(address: str, max_length: int, wide_char: bool = False) -> MemoryReadResponse:
        """
        Read a string from the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to read from in CE's memory (as string, can be hex like "0x12345" or decimal)
            max_length: Maximum number of characters to read
            wide_char: If True, read as widechar (UTF-16/Unicode). If False, read as ASCII/ANSI.
            
        Returns:
            Dictionary with string value and success status
        """
        return await make_request("read-memory", "POST", {
            "Address": address,
            "DataType": "stringlocal",
            "MaxLength": max_length,
            "WideChar": wide_char
        })

    # Memory Write Tools
    @mcp.tool()
    async def write_bytes(address: str, byte_values: List[int]) -> BaseResponse:
        """
        Write bytes to memory at the specified address in the currently opened process
        
        Args:
            address: Memory address to write to (as string, can be hex like "0x12345" or decimal)
            byte_values: List of byte values to write (integers 0-255)
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "bytes", 
            "Value": byte_values
        })

    @mcp.tool()
    async def write_bytes_local(address: str, byte_values: List[int]) -> BaseResponse:
        """
        Write bytes to memory at the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to write to in CE's memory (as string, can be hex like "0x12345" or decimal)
            byte_values: List of byte values to write (integers 0-255)
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "byteslocal", 
            "Value": byte_values
        })

    @mcp.tool()
    async def write_small_integer(address: str, value: int) -> BaseResponse:
        """
        Write a 16-bit integer to the specified address in the target process
        
        Args:
            address: Memory address to write to (as string, can be hex like "0x12345" or decimal)
            value: The 16-bit integer value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "smallinteger", 
            "Value": value
        })

    @mcp.tool()
    async def write_small_integer_local(address: str, value: int) -> BaseResponse:
        """
        Write a 16-bit integer to the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to write to in CE's memory (as string, can be hex like "0x12345" or decimal)
            value: The 16-bit integer value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "smallintegerlocal", 
            "Value": value
        })

    @mcp.tool()
    async def write_integer(address: str, value: int) -> BaseResponse:
        """
        Write a 32-bit integer to the specified address in the target process
        
        Args:
            address: Memory address to write to (as string, can be hex like "0x12345" or decimal)
            value: The 32-bit integer value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "integer", 
            "Value": value
        })

    @mcp.tool()
    async def write_integer_local(address: str, value: int) -> BaseResponse:
        """
        Write a 32-bit integer to the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to write to in CE's memory (as string, can be hex like "0x12345" or decimal)
            value: The 32-bit integer value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "integerlocal", 
            "Value": value
        })

    @mcp.tool()
    async def write_qword(address: str, value: int) -> BaseResponse:
        """
        Write a 64-bit integer to the specified address in the target process
        
        Args:
            address: Memory address to write to (as string, can be hex like "0x12345" or decimal)
            value: The 64-bit integer value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "qword", 
            "Value": value
        })

    @mcp.tool()
    async def write_qword_local(address: str, value: int) -> BaseResponse:
        """
        Write a 64-bit integer to the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to write to in CE's memory (as string, can be hex like "0x12345" or decimal)
            value: The 64-bit integer value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "qwordlocal", 
            "Value": value
        })

    @mcp.tool()
    async def write_float(address: str, value: float) -> BaseResponse:
        """
        Write a single precision (32-bit) floating point value to the specified address in the target process
        
        Args:
            address: Memory address to write to (as string, can be hex like "0x12345" or decimal)
            value: The single precision floating point value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "float", 
            "Value": value
        })

    @mcp.tool()
    async def write_float_local(address: str, value: float) -> BaseResponse:
        """
        Write a single precision (32-bit) floating point value to the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to write to in CE's memory (as string, can be hex like "0x12345" or decimal)
            value: The single precision floating point value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "floatlocal", 
            "Value": value
        })

    @mcp.tool()
    async def write_double(address: str, value: float) -> BaseResponse:
        """
        Write a double precision (64-bit) floating point value to the specified address in the target process
        
        Args:
            address: Memory address to write to (as string, can be hex like "0x12345" or decimal)
            value: The double precision floating point value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "double", 
            "Value": value
        })

    @mcp.tool()
    async def write_double_local(address: str, value: float) -> BaseResponse:
        """
        Write a double precision (64-bit) floating point value to the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to write to in CE's memory (as string, can be hex like "0x12345" or decimal)
            value: The double precision floating point value to write
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "doublelocal", 
            "Value": value
        })

    @mcp.tool()
    async def write_string(address: str, text: str, wide_char: bool = False) -> BaseResponse:
        """
        Write a string to the specified address in the target process
        
        Args:
            address: Memory address to write to (as string, can be hex like "0x12345" or decimal)
            text: The string to write
            wide_char: If True, write as widechar (UTF-16/Unicode). If False, write as ASCII/ANSI.
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "string", 
            "Value": text,
            "WideChar": wide_char
        })

    @mcp.tool()
    async def write_string_local(address: str, text: str, wide_char: bool = False) -> BaseResponse:
        """
        Write a string to the specified address in Cheat Engine's own process memory
        
        Args:
            address: Memory address to write to in CE's memory (as string, can be hex like "0x12345" or decimal)
            text: The string to write
            wide_char: If True, write as widechar (UTF-16/Unicode). If False, write as ASCII/ANSI.
            
        Returns:
            Dictionary with success status
        """
        return await make_request("write-memory", "POST", {
            "Address": address, 
            "DataType": "stringlocal", 
            "Value": text,
            "WideChar": wide_char
        })