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
from aws_resource_validator.pydantic_models.vpc_lattice_constants import *

class AccessLogSubscriptionSummaryTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    destinationArn: str
    id: str
    lastUpdatedAt: datetime
    resourceArn: str
    resourceId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class RuleUpdateFailureTypeDef(BaseModel):
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None
    ruleIdentifier: Optional[str] = None

class CreateAccessLogSubscriptionRequestRequestTypeDef(BaseModel):
    destinationArn: str
    resourceIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateServiceNetworkRequestRequestTypeDef(BaseModel):
    name: str
    authType: Optional[AuthTypeType] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateServiceNetworkServiceAssociationRequestRequestTypeDef(BaseModel):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DnsEntryTypeDef(BaseModel):
    domainName: Optional[str] = None
    hostedZoneId: Optional[str] = None

class CreateServiceNetworkVpcAssociationRequestRequestTypeDef(BaseModel):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None

class CreateServiceRequestRequestTypeDef(BaseModel):
    name: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None
    clientToken: Optional[str] = None
    customDomainName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteAccessLogSubscriptionRequestRequestTypeDef(BaseModel):
    accessLogSubscriptionIdentifier: str

class DeleteAuthPolicyRequestRequestTypeDef(BaseModel):
    resourceIdentifier: str

class DeleteListenerRequestRequestTypeDef(BaseModel):
    listenerIdentifier: str
    serviceIdentifier: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str

class DeleteRuleRequestRequestTypeDef(BaseModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str

class DeleteServiceNetworkRequestRequestTypeDef(BaseModel):
    serviceNetworkIdentifier: str

class DeleteServiceNetworkServiceAssociationRequestRequestTypeDef(BaseModel):
    serviceNetworkServiceAssociationIdentifier: str

class DeleteServiceNetworkVpcAssociationRequestRequestTypeDef(BaseModel):
    serviceNetworkVpcAssociationIdentifier: str

class DeleteServiceRequestRequestTypeDef(BaseModel):
    serviceIdentifier: str

class DeleteTargetGroupRequestRequestTypeDef(BaseModel):
    targetGroupIdentifier: str

class TargetTypeDef(BaseModel):
    id: str
    port: Optional[int] = None

class TargetFailureTypeDef(BaseModel):
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None
    id: Optional[str] = None
    port: Optional[int] = None

class FixedResponseActionTypeDef(BaseModel):
    statusCode: int

class WeightedTargetGroupTypeDef(BaseModel):
    targetGroupIdentifier: str
    weight: Optional[int] = None

class GetAccessLogSubscriptionRequestRequestTypeDef(BaseModel):
    accessLogSubscriptionIdentifier: str

class GetAuthPolicyRequestRequestTypeDef(BaseModel):
    resourceIdentifier: str

class GetListenerRequestRequestTypeDef(BaseModel):
    listenerIdentifier: str
    serviceIdentifier: str

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    resourceArn: str

class GetRuleRequestRequestTypeDef(BaseModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str

class GetServiceNetworkRequestRequestTypeDef(BaseModel):
    serviceNetworkIdentifier: str

class GetServiceNetworkServiceAssociationRequestRequestTypeDef(BaseModel):
    serviceNetworkServiceAssociationIdentifier: str

class GetServiceNetworkVpcAssociationRequestRequestTypeDef(BaseModel):
    serviceNetworkVpcAssociationIdentifier: str

class GetServiceRequestRequestTypeDef(BaseModel):
    serviceIdentifier: str

class GetTargetGroupRequestRequestTypeDef(BaseModel):
    targetGroupIdentifier: str

class HeaderMatchTypeTypeDef(BaseModel):
    contains: Optional[str] = None
    exact: Optional[str] = None
    prefix: Optional[str] = None

class MatcherTypeDef(BaseModel):
    httpCode: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessLogSubscriptionsRequestRequestTypeDef(BaseModel):
    resourceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListListenersRequestRequestTypeDef(BaseModel):
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListenerSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[ListenerProtocolType] = None

class ListRulesRequestRequestTypeDef(BaseModel):
    listenerIdentifier: str
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RuleSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    isDefault: Optional[bool] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    priority: Optional[int] = None

class ListServiceNetworkServiceAssociationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None

class ListServiceNetworkVpcAssociationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    vpcIdentifier: Optional[str] = None

class ServiceNetworkVpcAssociationSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    serviceNetworkArn: Optional[str] = None
    serviceNetworkId: Optional[str] = None
    serviceNetworkName: Optional[str] = None
    status: Optional[ServiceNetworkVpcAssociationStatusType] = None
    vpcId: Optional[str] = None

class ListServiceNetworksRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceNetworkSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    numberOfAssociatedServices: Optional[int] = None
    numberOfAssociatedVPCs: Optional[int] = None

class ListServicesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTargetGroupsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None

class TargetGroupSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    lambdaEventStructureVersion: Optional[LambdaEventStructureVersionType] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[TargetGroupProtocolType] = None
    serviceArns: Optional[List[str]] = None
    status: Optional[TargetGroupStatusType] = None
    type: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None

class TargetSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    port: Optional[int] = None
    reasonCode: Optional[str] = None
    status: Optional[TargetStatusType] = None

class PathMatchTypeTypeDef(BaseModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None

class PutAuthPolicyRequestRequestTypeDef(BaseModel):
    policy: str
    resourceIdentifier: str

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    policy: str
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessLogSubscriptionRequestRequestTypeDef(BaseModel):
    accessLogSubscriptionIdentifier: str
    destinationArn: str

class UpdateServiceNetworkRequestRequestTypeDef(BaseModel):
    authType: AuthTypeType
    serviceNetworkIdentifier: str

class UpdateServiceNetworkVpcAssociationRequestRequestTypeDef(BaseModel):
    securityGroupIds: Sequence[str]
    serviceNetworkVpcAssociationIdentifier: str

class UpdateServiceRequestRequestTypeDef(BaseModel):
    serviceIdentifier: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None

class CreateAccessLogSubscriptionResponseTypeDef(BaseModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceNetworkResponseTypeDef(BaseModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceNetworkVpcAssociationResponseTypeDef(BaseModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceNetworkServiceAssociationResponseTypeDef(BaseModel):
    arn: str
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceNetworkVpcAssociationResponseTypeDef(BaseModel):
    arn: str
    id: str
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceResponseTypeDef(BaseModel):
    arn: str
    id: str
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTargetGroupResponseTypeDef(BaseModel):
    arn: str
    id: str
    status: TargetGroupStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessLogSubscriptionResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    destinationArn: str
    id: str
    lastUpdatedAt: datetime
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthPolicyResponseTypeDef(BaseModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceNetworkResponseTypeDef(BaseModel):
    arn: str
    authType: AuthTypeType
    createdAt: datetime
    id: str
    lastUpdatedAt: datetime
    name: str
    numberOfAssociatedServices: int
    numberOfAssociatedVPCs: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceNetworkVpcAssociationResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    createdBy: str
    failureCode: str
    failureMessage: str
    id: str
    lastUpdatedAt: datetime
    securityGroupIds: List[str]
    serviceNetworkArn: str
    serviceNetworkId: str
    serviceNetworkName: str
    status: ServiceNetworkVpcAssociationStatusType
    vpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccessLogSubscriptionsResponseTypeDef(BaseModel):
    items: List[AccessLogSubscriptionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAuthPolicyResponseTypeDef(BaseModel):
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessLogSubscriptionResponseTypeDef(BaseModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceNetworkResponseTypeDef(BaseModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceNetworkVpcAssociationResponseTypeDef(BaseModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(BaseModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    customDomainName: str
    id: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceNetworkServiceAssociationResponseTypeDef(BaseModel):
    arn: str
    createdBy: str
    customDomainName: str
    dnsEntry: DnsEntryTypeDef
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceResponseTypeDef(BaseModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    customDomainName: str
    dnsEntry: DnsEntryTypeDef
    id: str
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceNetworkServiceAssociationResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    createdBy: str
    customDomainName: str
    dnsEntry: DnsEntryTypeDef
    failureCode: str
    failureMessage: str
    id: str
    serviceArn: str
    serviceId: str
    serviceName: str
    serviceNetworkArn: str
    serviceNetworkId: str
    serviceNetworkName: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceResponseTypeDef(BaseModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    createdAt: datetime
    customDomainName: str
    dnsEntry: DnsEntryTypeDef
    failureCode: str
    failureMessage: str
    id: str
    lastUpdatedAt: datetime
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceNetworkServiceAssociationSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    customDomainName: Optional[str] = None
    dnsEntry: Optional[DnsEntryTypeDef] = None
    id: Optional[str] = None
    serviceArn: Optional[str] = None
    serviceId: Optional[str] = None
    serviceName: Optional[str] = None
    serviceNetworkArn: Optional[str] = None
    serviceNetworkId: Optional[str] = None
    serviceNetworkName: Optional[str] = None
    status: Optional[ServiceNetworkServiceAssociationStatusType] = None

class ServiceSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    customDomainName: Optional[str] = None
    dnsEntry: Optional[DnsEntryTypeDef] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[ServiceStatusType] = None

class DeregisterTargetsRequestRequestTypeDef(BaseModel):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]

class ListTargetsRequestRequestTypeDef(BaseModel):
    targetGroupIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targets: Optional[Sequence[TargetTypeDef]] = None

class RegisterTargetsRequestRequestTypeDef(BaseModel):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]

class DeregisterTargetsResponseTypeDef(BaseModel):
    successful: List[TargetTypeDef]
    unsuccessful: List[TargetFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTargetsResponseTypeDef(BaseModel):
    successful: List[TargetTypeDef]
    unsuccessful: List[TargetFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ForwardActionOutputTypeDef(BaseModel):
    targetGroups: List[WeightedTargetGroupTypeDef]

class ForwardActionTypeDef(BaseModel):
    targetGroups: Sequence[WeightedTargetGroupTypeDef]

class HeaderMatchTypeDef(BaseModel):
    match: HeaderMatchTypeTypeDef
    name: str
    caseSensitive: Optional[bool] = None

class HealthCheckConfigTypeDef(BaseModel):
    enabled: Optional[bool] = None
    healthCheckIntervalSeconds: Optional[int] = None
    healthCheckTimeoutSeconds: Optional[int] = None
    healthyThresholdCount: Optional[int] = None
    matcher: Optional[MatcherTypeDef] = None
    path: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[TargetGroupProtocolType] = None
    protocolVersion: Optional[HealthCheckProtocolVersionType] = None
    unhealthyThresholdCount: Optional[int] = None

class ListAccessLogSubscriptionsRequestListAccessLogSubscriptionsPaginateTypeDef(BaseModel):
    resourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListListenersRequestListListenersPaginateTypeDef(BaseModel):
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseModel):
    listenerIdentifier: str
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceNetworkServiceAssociationsRequestListServiceNetworkServiceAssociationsPaginateTypeDef(BaseModel):
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceNetworksRequestListServiceNetworksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesRequestListServicesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetGroupsRequestListTargetGroupsPaginateTypeDef(BaseModel):
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsRequestListTargetsPaginateTypeDef(BaseModel):
    targetGroupIdentifier: str
    targets: Optional[Sequence[TargetTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListListenersResponseTypeDef(BaseModel):
    items: List[ListenerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesResponseTypeDef(BaseModel):
    items: List[RuleSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceNetworkVpcAssociationsResponseTypeDef(BaseModel):
    items: List[ServiceNetworkVpcAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceNetworksResponseTypeDef(BaseModel):
    items: List[ServiceNetworkSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetGroupsResponseTypeDef(BaseModel):
    items: List[TargetGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsResponseTypeDef(BaseModel):
    items: List[TargetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PathMatchTypeDef(BaseModel):
    match: PathMatchTypeTypeDef
    caseSensitive: Optional[bool] = None

class ListServiceNetworkServiceAssociationsResponseTypeDef(BaseModel):
    items: List[ServiceNetworkServiceAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesResponseTypeDef(BaseModel):
    items: List[ServiceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RuleActionOutputTypeDef(BaseModel):
    fixedResponse: Optional[FixedResponseActionTypeDef] = None
    forward: Optional[ForwardActionOutputTypeDef] = None

class RuleActionTypeDef(BaseModel):
    fixedResponse: Optional[FixedResponseActionTypeDef] = None
    forward: Optional[ForwardActionTypeDef] = None

class TargetGroupConfigTypeDef(BaseModel):
    healthCheck: Optional[HealthCheckConfigTypeDef] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    lambdaEventStructureVersion: Optional[LambdaEventStructureVersionType] = None
    port: Optional[int] = None
    protocol: Optional[TargetGroupProtocolType] = None
    protocolVersion: Optional[TargetGroupProtocolVersionType] = None
    vpcIdentifier: Optional[str] = None

class UpdateTargetGroupRequestRequestTypeDef(BaseModel):
    healthCheck: HealthCheckConfigTypeDef
    targetGroupIdentifier: str

class HttpMatchOutputTypeDef(BaseModel):
    headerMatches: Optional[List[HeaderMatchTypeDef]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatchTypeDef] = None

class HttpMatchTypeDef(BaseModel):
    headerMatches: Optional[Sequence[HeaderMatchTypeDef]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatchTypeDef] = None

class CreateListenerResponseTypeDef(BaseModel):
    arn: str
    defaultAction: RuleActionOutputTypeDef
    id: str
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetListenerResponseTypeDef(BaseModel):
    arn: str
    createdAt: datetime
    defaultAction: RuleActionOutputTypeDef
    id: str
    lastUpdatedAt: datetime
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateListenerResponseTypeDef(BaseModel):
    arn: str
    defaultAction: RuleActionOutputTypeDef
    id: str
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateListenerRequestRequestTypeDef(BaseModel):
    defaultAction: RuleActionTypeDef
    name: str
    protocol: ListenerProtocolType
    serviceIdentifier: str
    clientToken: Optional[str] = None
    port: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateListenerRequestRequestTypeDef(BaseModel):
    defaultAction: RuleActionTypeDef
    listenerIdentifier: str
    serviceIdentifier: str

class CreateTargetGroupRequestRequestTypeDef(BaseModel):
    name: str
    type: TargetGroupTypeType
    clientToken: Optional[str] = None
    config: Optional[TargetGroupConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateTargetGroupResponseTypeDef(BaseModel):
    arn: str
    config: TargetGroupConfigTypeDef
    id: str
    name: str
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetTargetGroupResponseTypeDef(BaseModel):
    arn: str
    config: TargetGroupConfigTypeDef
    createdAt: datetime
    failureCode: str
    failureMessage: str
    id: str
    lastUpdatedAt: datetime
    name: str
    serviceArns: List[str]
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTargetGroupResponseTypeDef(BaseModel):
    arn: str
    config: TargetGroupConfigTypeDef
    id: str
    name: str
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class RuleMatchOutputTypeDef(BaseModel):
    httpMatch: Optional[HttpMatchOutputTypeDef] = None

class RuleMatchTypeDef(BaseModel):
    httpMatch: Optional[HttpMatchTypeDef] = None

class CreateRuleResponseTypeDef(BaseModel):
    action: RuleActionOutputTypeDef
    arn: str
    id: str
    match: RuleMatchOutputTypeDef
    name: str
    priority: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleResponseTypeDef(BaseModel):
    action: RuleActionOutputTypeDef
    arn: str
    createdAt: datetime
    id: str
    isDefault: bool
    lastUpdatedAt: datetime
    match: RuleMatchOutputTypeDef
    name: str
    priority: int
    ResponseMetadata: ResponseMetadataTypeDef

class RuleUpdateSuccessTypeDef(BaseModel):
    action: Optional[RuleActionOutputTypeDef] = None
    arn: Optional[str] = None
    id: Optional[str] = None
    isDefault: Optional[bool] = None
    match: Optional[RuleMatchOutputTypeDef] = None
    name: Optional[str] = None
    priority: Optional[int] = None

class UpdateRuleResponseTypeDef(BaseModel):
    action: RuleActionOutputTypeDef
    arn: str
    id: str
    isDefault: bool
    match: RuleMatchOutputTypeDef
    name: str
    priority: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleRequestRequestTypeDef(BaseModel):
    action: RuleActionTypeDef
    listenerIdentifier: str
    match: RuleMatchTypeDef
    name: str
    priority: int
    serviceIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class RuleUpdateTypeDef(BaseModel):
    ruleIdentifier: str
    action: Optional[RuleActionTypeDef] = None
    match: Optional[RuleMatchTypeDef] = None
    priority: Optional[int] = None

class UpdateRuleRequestRequestTypeDef(BaseModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str
    action: Optional[RuleActionTypeDef] = None
    match: Optional[RuleMatchTypeDef] = None
    priority: Optional[int] = None

class BatchUpdateRuleResponseTypeDef(BaseModel):
    successful: List[RuleUpdateSuccessTypeDef]
    unsuccessful: List[RuleUpdateFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRuleRequestRequestTypeDef(BaseModel):
    listenerIdentifier: str
    rules: Sequence[RuleUpdateTypeDef]
    serviceIdentifier: str

