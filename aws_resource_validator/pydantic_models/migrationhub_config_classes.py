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
from aws_resource_validator.pydantic_models.migrationhub_config_constants import *

class TargetTypeDef(BaseValidatorModel):
    Type: Literal["ACCOUNT"]
    Id: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteHomeRegionControlRequestRequestTypeDef(BaseValidatorModel):
    ControlId: str

class CreateHomeRegionControlRequestRequestTypeDef(BaseValidatorModel):
    HomeRegion: str
    Target: TargetTypeDef
    DryRun: Optional[bool] = None

class DescribeHomeRegionControlsRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

