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
from aws_resource_validator.pydantic_models.route53_recovery_control_config_constants import *

class AssertionRuleUpdateTypeDef(BaseValidatorModel):
    Name: str
    SafetyRuleArn: str
    WaitPeriodMs: int


class ClusterEndpointTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None
    Region: Optional[str] = None


class ControlPanelTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ControlPanelArn: Optional[str] = None
    DefaultControlPanel: Optional[bool] = None
    Name: Optional[str] = None
    RoutingControlCount: Optional[int] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None


class CreateClusterRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateControlPanelRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    ControlPanelName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateRoutingControlRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    RoutingControlName: str
    ClientToken: Optional[str] = None
    ControlPanelArn: Optional[str] = None


class RoutingControlTypeDef(BaseValidatorModel):
    ControlPanelArn: Optional[str] = None
    Name: Optional[str] = None
    RoutingControlArn: Optional[str] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None


class DeleteClusterRequestTypeDef(BaseValidatorModel):
    ClusterArn: str


class DeleteControlPanelRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str


class DeleteRoutingControlRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str


class DeleteSafetyRuleRequestTypeDef(BaseValidatorModel):
    SafetyRuleArn: str


class DescribeClusterRequestTypeDef(BaseValidatorModel):
    ClusterArn: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeControlPanelRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str


class DescribeRoutingControlRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str


class DescribeSafetyRuleRequestTypeDef(BaseValidatorModel):
    SafetyRuleArn: str


class GatingRuleUpdateTypeDef(BaseValidatorModel):
    Name: str
    SafetyRuleArn: str
    WaitPeriodMs: int


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssociatedRoute53HealthChecksRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListClustersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListControlPanelsRequestTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoutingControlsRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSafetyRulesRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateControlPanelRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    ControlPanelName: str


class UpdateRoutingControlRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlName: str


class RuleConfigTypeDef(BaseValidatorModel):
    pass


class AssertionRuleTypeDef(BaseValidatorModel):
    AssertedControls: List[str]
    ControlPanelArn: str
    Name: str
    RuleConfig: RuleConfigTypeDef
    SafetyRuleArn: str
    Status: StatusType
    WaitPeriodMs: int
    Owner: Optional[str] = None


class GatingRuleTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    GatingControls: List[str]
    Name: str
    RuleConfig: RuleConfigTypeDef
    SafetyRuleArn: str
    Status: StatusType
    TargetControls: List[str]
    WaitPeriodMs: int
    Owner: Optional[str] = None


class NewAssertionRuleTypeDef(BaseValidatorModel):
    AssertedControls: Sequence[str]
    ControlPanelArn: str
    Name: str
    RuleConfig: RuleConfigTypeDef
    WaitPeriodMs: int


class NewGatingRuleTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    GatingControls: Sequence[str]
    Name: str
    RuleConfig: RuleConfigTypeDef
    TargetControls: Sequence[str]
    WaitPeriodMs: int


class ClusterTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    ClusterEndpoints: Optional[List[ClusterEndpointTypeDef]] = None
    Name: Optional[str] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None


class CreateControlPanelResponseTypeDef(BaseValidatorModel):
    ControlPanel: ControlPanelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeControlPanelResponseTypeDef(BaseValidatorModel):
    ControlPanel: ControlPanelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssociatedRoute53HealthChecksResponseTypeDef(BaseValidatorModel):
    HealthCheckIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListControlPanelsResponseTypeDef(BaseValidatorModel):
    ControlPanels: List[ControlPanelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateControlPanelResponseTypeDef(BaseValidatorModel):
    ControlPanel: ControlPanelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRoutingControlResponseTypeDef(BaseValidatorModel):
    RoutingControl: RoutingControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRoutingControlResponseTypeDef(BaseValidatorModel):
    RoutingControl: RoutingControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRoutingControlsResponseTypeDef(BaseValidatorModel):
    RoutingControls: List[RoutingControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateRoutingControlResponseTypeDef(BaseValidatorModel):
    RoutingControl: RoutingControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeClusterRequestWaitExtraTypeDef(BaseValidatorModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeClusterRequestWaitTypeDef(BaseValidatorModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeControlPanelRequestWaitExtraTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeControlPanelRequestWaitTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeRoutingControlRequestWaitExtraTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeRoutingControlRequestWaitTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class UpdateSafetyRuleRequestTypeDef(BaseValidatorModel):
    AssertionRuleUpdate: Optional[AssertionRuleUpdateTypeDef] = None
    GatingRuleUpdate: Optional[GatingRuleUpdateTypeDef] = None


class ListAssociatedRoute53HealthChecksRequestPaginateTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClustersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListControlPanelsRequestPaginateTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoutingControlsRequestPaginateTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSafetyRulesRequestPaginateTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class CreateSafetyRuleResponseTypeDef(BaseValidatorModel):
    AssertionRule: AssertionRuleTypeDef
    GatingRule: GatingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSafetyRuleResponseTypeDef(BaseValidatorModel):
    AssertionRule: AssertionRuleTypeDef
    GatingRule: GatingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RuleTypeDef(BaseValidatorModel):
    ASSERTION: Optional[AssertionRuleTypeDef] = None
    GATING: Optional[GatingRuleTypeDef] = None


class UpdateSafetyRuleResponseTypeDef(BaseValidatorModel):
    AssertionRule: AssertionRuleTypeDef
    GatingRule: GatingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSafetyRuleRequestTypeDef(BaseValidatorModel):
    AssertionRule: Optional[NewAssertionRuleTypeDef] = None
    ClientToken: Optional[str] = None
    GatingRule: Optional[NewGatingRuleTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListClustersResponseTypeDef(BaseValidatorModel):
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSafetyRulesResponseTypeDef(BaseValidatorModel):
    SafetyRules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


