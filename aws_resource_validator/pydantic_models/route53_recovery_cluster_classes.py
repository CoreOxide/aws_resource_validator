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

class GetRoutingControlStateRequest(BaseValidatorModel):
    RoutingControlArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListRoutingControlsRequest(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RoutingControl(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    ControlPanelName: Optional[str] = None
    RoutingControlArn: Optional[str] = None
    RoutingControlName: Optional[str] = None
    RoutingControlState: Optional[RoutingControlStateType] = None
    Owner: Optional[str] = None


class UpdateRoutingControlStateEntry(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType


class UpdateRoutingControlStateRequest(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    SafetyRulesToOverride: Optional[Sequence[str]] = None


class GetRoutingControlStateResponse(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlState: RoutingControlStateType
    RoutingControlName: str
    ResponseMetadata: ResponseMetadata


class ListRoutingControlsRequestPaginate(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoutingControlsResponse(BaseValidatorModel):
    RoutingControls: List[RoutingControl]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateRoutingControlStatesRequest(BaseValidatorModel):
    UpdateRoutingControlStateEntries: Sequence[UpdateRoutingControlStateEntry]
    SafetyRulesToOverride: Optional[Sequence[str]] = None


