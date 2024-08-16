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
from aws_resource_validator.pydantic_models.route53_recovery_control_config_constants import *

class RuleConfigTypeDef(BaseValidatorModel):
    Inverted: bool
    Threshold: int
    Type: RuleTypeType

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

class CreateClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateControlPanelRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str
    ControlPanelName: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateRoutingControlRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str

class DeleteControlPanelRequestRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str

class DeleteRoutingControlRequestRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str

class DeleteSafetyRuleRequestRequestTypeDef(BaseValidatorModel):
    SafetyRuleArn: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: str

class DescribeControlPanelRequestRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str

class DescribeRoutingControlRequestRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str

class DescribeSafetyRuleRequestRequestTypeDef(BaseValidatorModel):
    SafetyRuleArn: str

class GatingRuleUpdateTypeDef(BaseValidatorModel):
    Name: str
    SafetyRuleArn: str
    WaitPeriodMs: int

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssociatedRoute53HealthChecksRequestRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListClustersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListControlPanelsRequestRequestTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRoutingControlsRequestRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSafetyRulesRequestRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateControlPanelRequestRequestTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    ControlPanelName: str

class UpdateRoutingControlRequestRequestTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    RoutingControlName: str

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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListControlPanelsResponseTypeDef(BaseValidatorModel):
    ControlPanels: List[ControlPanelTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    RoutingControls: List[RoutingControlTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoutingControlResponseTypeDef(BaseValidatorModel):
    RoutingControl: RoutingControlTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClusterRequestClusterCreatedWaitTypeDef(BaseValidatorModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeClusterRequestClusterDeletedWaitTypeDef(BaseValidatorModel):
    ClusterArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeControlPanelRequestControlPanelCreatedWaitTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeControlPanelRequestControlPanelDeletedWaitTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeRoutingControlRequestRoutingControlCreatedWaitTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeRoutingControlRequestRoutingControlDeletedWaitTypeDef(BaseValidatorModel):
    RoutingControlArn: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class UpdateSafetyRuleRequestRequestTypeDef(BaseValidatorModel):
    AssertionRuleUpdate: Optional[AssertionRuleUpdateTypeDef] = None
    GatingRuleUpdate: Optional[GatingRuleUpdateTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListControlPanelsRequestListControlPanelsPaginateTypeDef(BaseValidatorModel):
    ClusterArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingControlsRequestListRoutingControlsPaginateTypeDef(BaseValidatorModel):
    ControlPanelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSafetyRulesRequestListSafetyRulesPaginateTypeDef(BaseValidatorModel):
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

class CreateSafetyRuleRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSafetyRulesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    SafetyRules: List[RuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

