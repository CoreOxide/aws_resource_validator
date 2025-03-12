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

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteHomeRegionControlRequestTypeDef(BaseValidatorModel):
    ControlId: str


class TargetTypeDef(BaseValidatorModel):
    pass


class CreateHomeRegionControlRequestTypeDef(BaseValidatorModel):
    HomeRegion: str
    Target: TargetTypeDef
    DryRun: Optional[bool] = None


class DescribeHomeRegionControlsRequestTypeDef(BaseValidatorModel):
    ControlId: Optional[str] = None
    HomeRegion: Optional[str] = None
    Target: Optional[TargetTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class HomeRegionControlTypeDef(BaseValidatorModel):
    ControlId: Optional[str] = None
    HomeRegion: Optional[str] = None
    Target: Optional[TargetTypeDef] = None
    RequestedTime: Optional[datetime] = None


class GetHomeRegionResultTypeDef(BaseValidatorModel):
    HomeRegion: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateHomeRegionControlResultTypeDef(BaseValidatorModel):
    HomeRegionControl: HomeRegionControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeHomeRegionControlsResultTypeDef(BaseValidatorModel):
    HomeRegionControls: List[HomeRegionControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


