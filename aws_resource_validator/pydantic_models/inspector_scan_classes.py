from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ScanSbomRequestRequestTypeDef(BaseValidatorModel):
    sbom: Mapping[str, Any]
    outputFormat: Optional[OutputFormatType] = None

class ScanSbomResponseTypeDef(BaseValidatorModel):
    sbom: Dict[str, Any]
    ResponseMetadata: ResponseMetadataTypeDef

