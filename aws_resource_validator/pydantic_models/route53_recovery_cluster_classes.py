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
from aws_resource_validator.pydantic_models.route53_recovery_cluster_constants import *

class GetRoutingControlStateRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRoutingControlsRequestTypeDef(BaseValidatorModel):
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


class UpdateRoutingControlStateRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    SafetyRulesToOverride: Optional[Sequence[str]] = None


class GetRoutingControlStateResponseTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    RoutingControlName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListRoutingControlsRequestPaginateTypeDef(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoutingControlsResponseTypeDef(BaseValidatorModel):
    RoutingControls: List[RoutingControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateRoutingControlStatesRequestTypeDef(BaseValidatorModel):
    UpdateRoutingControlStateEntries: Sequence[UpdateRoutingControlStateEntryTypeDef]
    SafetyRulesToOverride: Optional[Sequence[str]] = None


