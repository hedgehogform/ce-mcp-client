"""
Type definitions for Cheat Engine MCP Server responses
"""

from typing import List, Optional, TypedDict, Union


class BaseResponse(TypedDict):
    Success: bool
    Error: Optional[str]


class LuaResponse(BaseResponse):
    Result: Optional[str]


class ProcessInfo(TypedDict):
    ProcessId: int
    ProcessName: str


class ProcessListResponse(BaseResponse):
    ProcessList: Optional[List[ProcessInfo]]


class ProcessStatusResponse(BaseResponse):
    ProcessId: Optional[int]
    IsOpen: Optional[bool]
    ProcessName: Optional[str]


class ThreadListResponse(BaseResponse):
    ThreadList: Optional[List[str]]


class MemoryReadResponse(BaseResponse):
    Value: Optional[Union[str, int, float, List[int]]]


class ConversionResponse(BaseResponse):
    Output: Optional[str]


class AobScanResponse(BaseResponse):
    Addresses: Optional[List[str]]


class DisassemblerResponse(BaseResponse):
    Output: Optional[str]


class ResultItem(TypedDict):
    Address: str
    Value: str


class ResultList(TypedDict):
    TotalCount: int
    StoredCount: int
    Items: List[ResultItem]


class MemScanResponse(BaseResponse):
    Results: Optional[ResultList]


class GetAddressSafeResponse(BaseResponse):
    Address: Optional[str]


class GetNameFromAddressResponse(BaseResponse):
    Name: Optional[str]


class InModuleResponse(BaseResponse):
    InModule: Optional[bool]


class InSystemModuleResponse(BaseResponse):
    InSystemModule: Optional[bool]


class ApiInfoResponse(TypedDict):
    base_url: str
    swagger_ui: str
    description: str


class HealthResponse(BaseResponse):
    status: Optional[str]
    server: Optional[str]
    version: Optional[str]
    timestamp: Optional[str]