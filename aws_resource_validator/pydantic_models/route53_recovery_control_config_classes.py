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
from aws_resource_validator.pydantic_models.route53_recovery_control_config_constants import *

class RuleConfigTypeDef(BaseModel):
    Inverted: bool
    Threshold: int
    Type: RuleTypeType

class AssertionRuleUpdateTypeDef(BaseModel):
    Name: str
    SafetyRuleArn: str
    WaitPeriodMs: int

class ClusterEndpointTypeDef(BaseModel):
    Endpoint: Optional[str] = None
    Region: Optional[str] = None

class ControlPanelTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    ControlPanelArn: Optional[str] = None
    DefaultControlPanel: Optional[bool] = None
    Name: Optional[str] = None
    RoutingControlCount: Optional[int] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None

class CreateClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateControlPanelRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    ControlPanelName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateRoutingControlRequestRequestTypeDef(BaseModel):
    ClusterArn: str
    RoutingControlName: str
    ClientToken: Optional[str] = None
    ControlPanelArn: Optional[str] = None

class RoutingControlTypeDef(BaseModel):
    ControlPanelArn: Optional[str] = None
    Name: Optional[str] = None
    RoutingControlArn: Optional[str] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None

class DeleteClusterRequestRequestTypeDef(BaseModel):
    ClusterArn: str

class DeleteControlPanelRequestRequestTypeDef(BaseModel):
    ControlPanelArn: str

class DeleteRoutingControlRequestRequestTypeDef(BaseModel):
    RoutingControlArn: str

class DeleteSafetyRuleRequestRequestTypeDef(BaseModel):
    SafetyRuleArn: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeClusterRequestRequestTypeDef(BaseModel):
    ClusterArn: str

class DescribeControlPanelRequestRequestTypeDef(BaseModel):
    ControlPanelArn: str

class DescribeRoutingControlRequestRequestTypeDef(BaseModel):
    RoutingControlArn: str

class DescribeSafetyRuleRequestRequestTypeDef(BaseModel):
    SafetyRuleArn: str

class GatingRuleUpdateTypeDef(BaseModel):
    Name: str
    SafetyRuleArn: str
    WaitPeriodMs: int

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssociatedRoute53HealthChecksRequestRequestTypeDef(BaseModel):
    RoutingControlArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClustersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListControlPanelsRequestRequestTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRoutingControlsRequestRequestTypeDef(BaseModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSafetyRulesRequestRequestTypeDef(BaseModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateControlPanelRequestRequestTypeDef(BaseModel):
    ControlPanelArn: str
    ControlPanelName: str

class UpdateRoutingControlRequestRequestTypeDef(BaseModel):
    RoutingControlArn: str
    RoutingControlName: str

class AssertionRuleTypeDef(BaseModel):
    AssertedControls: List[str]
    ControlPanelArn: str
    Name: str
    RuleConfig: RuleConfigTypeDef
    SafetyRuleArn: str
    Status: StatusType
    WaitPeriodMs: int
    Owner: Optional[str] = None

class GatingRuleTypeDef(BaseModel):
    ControlPanelArn: str
    GatingControls: List[str]
    Name: str
    RuleConfig: RuleConfigTypeDef
    SafetyRuleArn: str
    Status: StatusType
    TargetControls: List[str]
    WaitPeriodMs: int
    Owner: Optional[str] = None

class NewAssertionRuleTypeDef(BaseModel):
    AssertedControls: Sequence[str]
    ControlPanelArn: str
    Name: str
    RuleConfig: RuleConfigTypeDef
    WaitPeriodMs: int

class NewGatingRuleTypeDef(BaseModel):
    ControlPanelArn: str
    GatingControls: Sequence[str]
    Name: str
    RuleConfig: RuleConfigTypeDef
    TargetControls: Sequence[str]
    WaitPeriodMs: int

class ClusterTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    ClusterEndpoints: Optional[List[ClusterEndpointTypeDef]] = None
    Name: Optional[str] = None
    Status: Optional[StatusType] = None
    Owner: Optional[str] = None

class CreateControlPanelResponseTypeDef(BaseModel):
    ControlPanel: ControlPanelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeControlPanelResponseTypeDef(BaseModel):
    ControlPanel: ControlPanelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedRoute53HealthChecksResponseTypeDef(BaseModel):
    HealthCheckIds: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlPanelsResponseTypeDef(BaseModel):
    ControlPanels: List[ControlPanelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateControlPanelResponseTypeDef(BaseModel):
    ControlPanel: ControlPanelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoutingControlResponseTypeDef(BaseModel):
    RoutingControl: RoutingControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRoutingControlResponseTypeDef(BaseModel):
    RoutingControl: RoutingControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoutingControlsResponseTypeDef(BaseModel):
    NextToken: str
    RoutingControls: List[RoutingControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoutingControlResponseTypeDef(BaseModel):
    RoutingControl: RoutingControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClusterRequestClusterCreatedWaitTypeDef(BaseModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterRequestClusterDeletedWaitTypeDef(BaseModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeControlPanelRequestControlPanelCreatedWaitTypeDef(BaseModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeControlPanelRequestControlPanelDeletedWaitTypeDef(BaseModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeRoutingControlRequestRoutingControlCreatedWaitTypeDef(BaseModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeRoutingControlRequestRoutingControlDeletedWaitTypeDef(BaseModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class UpdateSafetyRuleRequestRequestTypeDef(BaseModel):
    AssertionRuleUpdate: Optional[AssertionRuleUpdateTypeDef] = None
    GatingRuleUpdate: Optional[GatingRuleUpdateTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListControlPanelsRequestListControlPanelsPaginateTypeDef(BaseModel):
    ClusterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingControlsRequestListRoutingControlsPaginateTypeDef(BaseModel):
    ControlPanelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSafetyRulesRequestListSafetyRulesPaginateTypeDef(BaseModel):
    ControlPanelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateSafetyRuleResponseTypeDef(BaseModel):
    AssertionRule: AssertionRuleTypeDef
    GatingRule: GatingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSafetyRuleResponseTypeDef(BaseModel):
    AssertionRule: AssertionRuleTypeDef
    GatingRule: GatingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RuleTypeDef(BaseModel):
    ASSERTION: Optional[AssertionRuleTypeDef] = None
    GATING: Optional[GatingRuleTypeDef] = None

class UpdateSafetyRuleResponseTypeDef(BaseModel):
    AssertionRule: AssertionRuleTypeDef
    GatingRule: GatingRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSafetyRuleRequestRequestTypeDef(BaseModel):
    AssertionRule: Optional[NewAssertionRuleTypeDef] = None
    ClientToken: Optional[str] = None
    GatingRule: Optional[NewGatingRuleTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersResponseTypeDef(BaseModel):
    Clusters: List[ClusterTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSafetyRulesResponseTypeDef(BaseModel):
    NextToken: str
    SafetyRules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

