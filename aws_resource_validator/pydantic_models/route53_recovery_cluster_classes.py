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
from aws_resource_validator.pydantic_models.route53_recovery_cluster_constants import *

class GetRoutingControlStateRequestRequestTypeDef(BaseModel):
    RoutingControlArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRoutingControlsRequestRequestTypeDef(BaseModel):
    ControlPanelArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RoutingControlTypeDef(BaseModel):
    ControlPanelArn: Optional[str] = None
    ControlPanelName: Optional[str] = None
    RoutingControlArn: Optional[str] = None
    RoutingControlName: Optional[str] = None
    RoutingControlState: Optional[RoutingControlStateType] = None
    Owner: Optional[str] = None

class UpdateRoutingControlStateEntryTypeDef(BaseModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType

class UpdateRoutingControlStateRequestRequestTypeDef(BaseModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    SafetyRulesToOverride: Optional[Sequence[str]] = None

class GetRoutingControlStateResponseTypeDef(BaseModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    RoutingControlName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoutingControlsRequestListRoutingControlsPaginateTypeDef(BaseModel):
    ControlPanelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingControlsResponseTypeDef(BaseModel):
    RoutingControls: List[RoutingControlTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoutingControlStatesRequestRequestTypeDef(BaseModel):
    UpdateRoutingControlStateEntries: Sequence[UpdateRoutingControlStateEntryTypeDef]
    SafetyRulesToOverride: Optional[Sequence[str]] = None

