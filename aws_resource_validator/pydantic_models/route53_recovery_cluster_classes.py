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
from aws_resource_validator.pydantic_models.route53_recovery_cluster_constants import *

class GetRoutingControlStateRequestRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListRoutingControlsRequestRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RoutingControlTypeDef(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    ControlPanelName: Optional[str] = None
    RoutingControlArn: Optional[str] = None
    RoutingControlName: Optional[str] = None
    RoutingControlState: Optional[RoutingControlStateType] = None
    Owner: Optional[str] = None

class UpdateRoutingControlStateEntryTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType

class UpdateRoutingControlStateRequestRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    SafetyRulesToOverride: Optional[Sequence[str]] = None

class GetRoutingControlStateResponseTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    RoutingControlName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoutingControlsRequestListRoutingControlsPaginateTypeDef(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingControlsResponseTypeDef(BaseValidatorModel):
    RoutingControls: List[RoutingControlTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoutingControlStatesRequestRequestTypeDef(BaseValidatorModel):
    UpdateRoutingControlStateEntries: Sequence[UpdateRoutingControlStateEntryTypeDef]
    SafetyRulesToOverride: Optional[Sequence[str]] = None

