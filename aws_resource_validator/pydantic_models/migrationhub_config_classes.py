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
from aws_resource_validator.pydantic_models.migrationhub_config_constants import *

class TargetTypeDef(BaseModel):
    Type: Literal["ACCOUNT"]
    Id: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteHomeRegionControlRequestRequestTypeDef(BaseModel):
    ControlId: str

class CreateHomeRegionControlRequestRequestTypeDef(BaseModel):
    HomeRegion: str
    Target: TargetTypeDef
    DryRun: Optional[bool] = None

class DescribeHomeRegionControlsRequestRequestTypeDef(BaseModel):
    ControlId: Optional[str] = None
    HomeRegion: Optional[str] = None
    Target: Optional[TargetTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class HomeRegionControlTypeDef(BaseModel):
    ControlId: Optional[str] = None
    HomeRegion: Optional[str] = None
    Target: Optional[TargetTypeDef] = None
    RequestedTime: Optional[datetime] = None

class GetHomeRegionResultTypeDef(BaseModel):
    HomeRegion: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHomeRegionControlResultTypeDef(BaseModel):
    HomeRegionControl: HomeRegionControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHomeRegionControlsResultTypeDef(BaseModel):
    HomeRegionControls: List[HomeRegionControlTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

