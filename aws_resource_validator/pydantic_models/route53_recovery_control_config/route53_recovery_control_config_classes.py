from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.route53_recovery_control_config.route53_recovery_control_config_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class RuleConfig(BaseValidatorModel):
    Inverted: bool
    Threshold: int
    Type: RuleTypeType


class AssertionRuleUpdate(BaseValidatorModel):
    Name: str
    SafetyRuleArn: str
    WaitPeriodMs: int


class ClusterEndpoint(BaseValidatorModel):
    Endpoint: Optional[str] = None
    Region: Optional[str] = None


class ControlPanel(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ControlPanelArn: Optional[str] = None
    DefaultControlPanel: Optional[bool] = None
    Name: Optional[str] = None
    RoutingControlCount: Optional[int] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None


class CreateClusterRequest(BaseValidatorModel):
    ClusterName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateControlPanelRequest(BaseValidatorModel):
    ClusterArn: str
    ControlPanelName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class CreateRoutingControlRequest(BaseValidatorModel):
    ClusterArn: str
    RoutingControlName: str
    ClientToken: Optional[str] = None
    ControlPanelArn: Optional[str] = None


class RoutingControl(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    Name: Optional[str] = None
    RoutingControlArn: Optional[str] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None


class DeleteClusterRequest(BaseValidatorModel):
    ClusterArn: str


class DeleteControlPanelRequest(BaseValidatorModel):
    ControlPanelArn: str


class DeleteRoutingControlRequest(BaseValidatorModel):
    RoutingControlArn: str


class DeleteSafetyRuleRequest(BaseValidatorModel):
    SafetyRuleArn: str


class DescribeClusterRequest(BaseValidatorModel):
    ClusterArn: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeControlPanelRequest(BaseValidatorModel):
    ControlPanelArn: str


class DescribeRoutingControlRequest(BaseValidatorModel):
    RoutingControlArn: str


class DescribeSafetyRuleRequest(BaseValidatorModel):
    SafetyRuleArn: str


class GatingRuleUpdate(BaseValidatorModel):
    Name: str
    SafetyRuleArn: str
    WaitPeriodMs: int


class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssociatedRoute53HealthChecksRequest(BaseValidatorModel):
    RoutingControlArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClustersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListControlPanelsRequest(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoutingControlsRequest(BaseValidatorModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSafetyRulesRequest(BaseValidatorModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateControlPanelRequest(BaseValidatorModel):
    ControlPanelArn: str
    ControlPanelName: str


class UpdateRoutingControlRequest(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlName: str


class AssertionRule(BaseValidatorModel):
    AssertedControls: List[str]
    ControlPanelArn: str
    Name: str
    RuleConfig: RuleConfig
    SafetyRuleArn: str
    Status: StatusType
    WaitPeriodMs: int
    Owner: Optional[str] = None


class GatingRule(BaseValidatorModel):
    ControlPanelArn: str
    GatingControls: List[str]
    Name: str
    RuleConfig: RuleConfig
    SafetyRuleArn: str
    Status: StatusType
    TargetControls: List[str]
    WaitPeriodMs: int
    Owner: Optional[str] = None


class NewAssertionRule(BaseValidatorModel):
    AssertedControls: List[str]
    ControlPanelArn: str
    Name: str
    RuleConfig: RuleConfig
    WaitPeriodMs: int


class NewGatingRule(BaseValidatorModel):
    ControlPanelArn: str
    GatingControls: List[str]
    Name: str
    RuleConfig: RuleConfig
    TargetControls: List[str]
    WaitPeriodMs: int


class Cluster(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ClusterEndpoints: Optional[List[ClusterEndpoint]] = None
    Name: Optional[str] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None


class CreateControlPanelResponse(BaseValidatorModel):
    ControlPanel: ControlPanel
    ResponseMetadata: ResponseMetadata


class DescribeControlPanelResponse(BaseValidatorModel):
    ControlPanel: ControlPanel
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadata


class ListAssociatedRoute53HealthChecksResponse(BaseValidatorModel):
    HealthCheckIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListControlPanelsResponse(BaseValidatorModel):
    ControlPanels: List[ControlPanel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateControlPanelResponse(BaseValidatorModel):
    ControlPanel: ControlPanel
    ResponseMetadata: ResponseMetadata


class CreateRoutingControlResponse(BaseValidatorModel):
    RoutingControl: RoutingControl
    ResponseMetadata: ResponseMetadata


class DescribeRoutingControlResponse(BaseValidatorModel):
    RoutingControl: RoutingControl
    ResponseMetadata: ResponseMetadata


class ListRoutingControlsResponse(BaseValidatorModel):
    RoutingControls: List[RoutingControl]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateRoutingControlResponse(BaseValidatorModel):
    RoutingControl: RoutingControl
    ResponseMetadata: ResponseMetadata


class DescribeClusterRequestWaitExtra(BaseValidatorModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeClusterRequestWait(BaseValidatorModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeControlPanelRequestWaitExtra(BaseValidatorModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeControlPanelRequestWait(BaseValidatorModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeRoutingControlRequestWaitExtra(BaseValidatorModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeRoutingControlRequestWait(BaseValidatorModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfig] = None


class UpdateSafetyRuleRequest(BaseValidatorModel):
    AssertionRuleUpdate: Optional[AssertionRuleUpdate] = None
    GatingRuleUpdate: Optional[GatingRuleUpdate] = None


class ListAssociatedRoute53HealthChecksRequestPaginate(BaseValidatorModel):
    RoutingControlArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListControlPanelsRequestPaginate(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoutingControlsRequestPaginate(BaseValidatorModel):
    ControlPanelArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSafetyRulesRequestPaginate(BaseValidatorModel):
    ControlPanelArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class CreateSafetyRuleResponse(BaseValidatorModel):
    AssertionRule: AssertionRule
    GatingRule: GatingRule
    ResponseMetadata: ResponseMetadata


class DescribeSafetyRuleResponse(BaseValidatorModel):
    AssertionRule: AssertionRule
    GatingRule: GatingRule
    ResponseMetadata: ResponseMetadata


class Rule(BaseValidatorModel):
    ASSERTION: Optional[AssertionRule] = None
    GATING: Optional[GatingRule] = None


class UpdateSafetyRuleResponse(BaseValidatorModel):
    AssertionRule: AssertionRule
    GatingRule: GatingRule
    ResponseMetadata: ResponseMetadata


class CreateSafetyRuleRequest(BaseValidatorModel):
    AssertionRule: Optional[NewAssertionRule] = None
    ClientToken: Optional[str] = None
    GatingRule: Optional[NewGatingRule] = None
    Tags: Optional[Dict[str, str]] = None


class CreateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DescribeClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class ListClustersResponse(BaseValidatorModel):
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSafetyRulesResponse(BaseValidatorModel):
    SafetyRules: List[Rule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None