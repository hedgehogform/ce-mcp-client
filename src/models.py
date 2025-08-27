"""
Type definitions for Cheat Engine MCP Server responses
"""

from typing import List, Optional, TypedDict, Union


class BaseResponse(TypedDict):
    success: bool
    error: Optional[str]


class LuaResponse(BaseResponse):
    result: Optional[str]
    returnCount: Optional[int]
    executionTime: Optional[str]


class ProcessInfo(TypedDict):
    processId: int
    processName: str


class ProcessListResponse(BaseResponse):
    processList: Optional[List[ProcessInfo]]


class ProcessStatusResponse(BaseResponse):
    processId: Optional[int]
    isOpen: Optional[bool]
    processName: Optional[str]


class ThreadListResponse(BaseResponse):
    threadList: Optional[List[str]]


class MemoryReadResponse(BaseResponse):
    value: Optional[Union[str, int, float, List[int]]]


class ConversionResponse(BaseResponse):
    output: Optional[str]


class AobScanResponse(BaseResponse):
    addresses: Optional[List[str]]


class DisassemblerResponse(BaseResponse):
    output: Optional[str]


class ResultItem(TypedDict):
    address: str
    value: str


class ResultList(TypedDict):
    totalCount: int
    storedCount: int
    items: List[ResultItem]


class MemScanResponse(BaseResponse):
    results: Optional[ResultList]


class GetAddressSafeResponse(BaseResponse):
    address: Optional[str]


class GetNameFromAddressResponse(BaseResponse):
    name: Optional[str]


class InModuleResponse(BaseResponse):
    inModule: Optional[bool]


class InSystemModuleResponse(BaseResponse):
    inSystemModule: Optional[bool]


class ApiInfoResponse(TypedDict):
    base_url: str
    swagger_ui: str
    description: str


class HealthResponse(BaseResponse):
    status: Optional[str]
    server: Optional[str]
    version: Optional[str]
    timestamp: Optional[str]