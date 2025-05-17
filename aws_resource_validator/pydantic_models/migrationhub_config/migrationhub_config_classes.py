from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.migrationhub_config.migrationhub_config_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Target(BaseValidatorModel):
    Type: Literal['ACCOUNT']
    Id: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteHomeRegionControlRequest(BaseValidatorModel):
    ControlId: str


# This class is the input for the 'create_home_region_control' function.
class CreateHomeRegionControlRequest(BaseValidatorModel):
    HomeRegion: str
    Target: Target
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_home_region_controls' function.
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


# This class is the output for the 'create_home_region_control' function.
class CreateHomeRegionControlResult(BaseValidatorModel):
    HomeRegionControl: HomeRegionControl
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_home_region_controls' function.
class DescribeHomeRegionControlsResult(BaseValidatorModel):
    HomeRegionControls: List[HomeRegionControl]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None