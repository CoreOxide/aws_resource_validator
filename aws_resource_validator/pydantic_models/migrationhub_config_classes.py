from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.migrationhub_config_constants import *

class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteHomeRegionControlRequest(BaseValidatorModel):
    ControlId: str


class Target(BaseValidatorModel):
    pass


class CreateHomeRegionControlRequest(BaseValidatorModel):
    HomeRegion: str
    Target: Target
    DryRun: Optional[bool] = None


class DescribeHomeRegionControlsRequest(BaseValidatorModel):
    ControlId: Optional[str] = None
    HomeRegion: Optional[str] = None
    Target: Optional[Target] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class HomeRegionControl(BaseValidatorModel):
    ControlId: Optional[str] = None
    HomeRegion: Optional[str] = None
    Target: Optional[Target] = None
    RequestedTime: Optional[datetime] = None


class GetHomeRegionResult(BaseValidatorModel):
    HomeRegion: str
    ResponseMetadata: ResponseMetadata


class CreateHomeRegionControlResult(BaseValidatorModel):
    HomeRegionControl: HomeRegionControl
    ResponseMetadata: ResponseMetadata


class DescribeHomeRegionControlsResult(BaseValidatorModel):
    HomeRegionControls: List[HomeRegionControl]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


