from datetime import datetime
from pydantic import BaseModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.inspector_scan_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ScanSbomRequestRequestTypeDef(BaseModel):
    sbom: Mapping[str, Any]
    outputFormat: Optional[OutputFormatType] = None

class ScanSbomResponseTypeDef(BaseModel):
    sbom: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

