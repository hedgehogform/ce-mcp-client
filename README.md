# Cheat Engine MCP Client

Python FastMCP server that provides AI tools for interacting with Cheat Engine through the REST API. This client allows AI assistants like Claude to perform memory analysis, process management, and reverse engineering tasks using Cheat Engine's powerful debugging capabilities.

## Related Projects

- **Main C# Plugin**: [hedgehogform/ce-mcp](https://github.com/hedgehogform/ce-mcp) - Cheat Engine plugin that hosts the REST API server

## Features

The MCP client provides **49 tools** organized into 5 categories:

### Process Management Tools (5 tools)

- `execute_lua` - Execute Lua code in Cheat Engine
- `get_process_list` - Get list of running processes
- `open_process` - Open a process by ID or name
- `get_thread_list` - Get threads for the current process
- `get_process_status` - Get status of the current process

### Memory Tools (30 tools)

**Reading Memory:**

- `read_bytes` / `read_bytes_local` - Read raw bytes from memory
- `read_small_integer` / `read_small_integer_local` - Read 16-bit integers
- `read_integer` / `read_integer_local` - Read 32-bit integers
- `read_qword` / `read_qword_local` - Read 64-bit integers
- `read_pointer` / `read_pointer_local` - Read pointer values
- `read_float` / `read_float_local` - Read 32-bit floating point
- `read_double` / `read_double_local` - Read 64-bit floating point
- `read_string` / `read_string_local` - Read strings (ASCII/Unicode)

**Writing Memory:**

- `write_bytes` / `write_bytes_local` - Write raw bytes to memory
- `write_small_integer` / `write_small_integer_local` - Write 16-bit integers
- `write_integer` / `write_integer_local` - Write 32-bit integers
- `write_qword` / `write_qword_local` - Write 64-bit integers
- `write_float` / `write_float_local` - Write 32-bit floating point
- `write_double` / `write_double_local` - Write 64-bit floating point
- `write_string` / `write_string_local` - Write strings to memory

### Address Tools (4 tools)

- `get_address_safe` - Safely resolve address strings to numeric addresses
- `get_name_from_address` - Get symbolic name from memory address
- `in_module` - Check if address is within a loaded module
- `in_system_module` - Check if address is within a system module

### Scan Tools (8 tools)

- `aob_scan` - Array of Bytes pattern scanning
- `disassemble` - Disassemble instruction at address
- `get_instruction_size` - Get size of instruction at address
- `memscan` - Perform memory value scanning (first/next scan)
- `memscan_reset` - Reset memory scan to start fresh
- `ansi_to_utf8` / `utf8_to_ansi` - String encoding conversion
- `string_to_md5` - Generate MD5 hash of string

### Utility Tools (2 tools)

- `get_api_info` - Get information about the REST API
- `get_health` - Check health status of the API server

## Installation & Setup

### Requirements

- Python 3.8+
- UV package manager: https://github.com/astral-sh/uv
- Running Cheat Engine with ce-mcp plugin enabled

### Installation

```bash
# Clone the repository
git clone https://github.com/hedgehogform/ce-mcp-client.git
cd ce-mcp-client

# Install dependencies using UV
uv sync

# Activate the virtual environment
uv shell
```

## Usage

### As MCP Server

The primary use case is as an MCP server for AI assistants:

```bash
# Run as MCP server (communicates via stdin/stdout)
python -m src.cheat_engine_mcp_server
```

### Configuration

The client connects to the Cheat Engine REST API at:

- **Host**: `127.0.0.1` (localhost)
- **Port**: `6300` (default)
- **Timeout**: 600 seconds for long-running operations

### AI Assistant Integration

Add this MCP server to your AI assistant configuration to enable Cheat Engine functionality. The server provides tools for:

- **Memory Analysis**: Read/write memory values in various formats
- **Process Debugging**: Attach to processes and analyze their state
- **Pattern Scanning**: Find byte patterns and assembly instructions
- **Address Resolution**: Convert between symbolic names and addresses
- **Reverse Engineering**: Disassemble code and analyze program structure

### Example Use Cases

1. **Game Hacking**: Find and modify game values (health, money, etc.)
2. **Malware Analysis**: Examine suspicious processes and their memory
3. **Software Debugging**: Analyze program behavior and memory layout
4. **Security Research**: Test application security and find vulnerabilities
5. **Educational**: Learn about program internals and memory management

## Architecture

The client is organized into modular components:

```
src/
├── cheat_engine_mcp_server.py    # Main MCP server entry point
├── client.py                     # HTTP client for REST API communication
├── models.py                     # TypedDict response models
└── tools/                        # Tool categories
    ├── process_tools.py          # Process management
    ├── memory_tools.py           # Memory read/write operations
    ├── address_tools.py          # Address resolution utilities
    ├── scan_tools.py            # Scanning and disassembly
    └── utility_tools.py         # API utilities and health checks
```
