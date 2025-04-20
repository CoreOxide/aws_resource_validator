from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53_recovery_cluster.route53_recovery_cluster_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    SafetyRulesToOverride: Optional[List[str]] = None


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
    UpdateRoutingControlStateEntries: List[UpdateRoutingControlStateEntry]
    SafetyRulesToOverride: Optional[List[str]] = None