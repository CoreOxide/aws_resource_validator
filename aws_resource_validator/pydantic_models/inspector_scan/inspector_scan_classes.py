from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.inspector_scan.inspector_scan_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'scan_sbom' function.
class ScanSbomRequest(BaseValidatorModel):
    sbom: Dict[str, Any]
    outputFormat: Optional[OutputFormatType] = None


# This class is the output for the 'scan_sbom' function.
class ScanSbomResponse(BaseValidatorModel):
    sbom: Dict[str, Any]
    ResponseMetadata: ResponseMetadata