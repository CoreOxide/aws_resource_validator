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
from aws_resource_validator.pydantic_models.vpc_lattice_constants import *

class AccessLogSubscriptionSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destinationArn: str
    id: str
    lastUpdatedAt: datetime
    resourceArn: str
    resourceId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class RuleUpdateFailureTypeDef(BaseValidatorModel):
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None
    ruleIdentifier: Optional[str] = None

class CreateAccessLogSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    destinationArn: str
    resourceIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateServiceNetworkRequestRequestTypeDef(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CreateServiceNetworkServiceAssociationRequestRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DnsEntryTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    hostedZoneId: Optional[str] = None

class CreateServiceNetworkVpcAssociationRequestRequestTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None

class CreateServiceRequestRequestTypeDef(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None
    clientToken: Optional[str] = None
    customDomainName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteAccessLogSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str

class DeleteAuthPolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str

class DeleteListenerRequestRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class DeleteRuleRequestRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str

class DeleteServiceNetworkRequestRequestTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str

class DeleteServiceNetworkServiceAssociationRequestRequestTypeDef(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str

class DeleteServiceNetworkVpcAssociationRequestRequestTypeDef(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str

class DeleteServiceRequestRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str

class DeleteTargetGroupRequestRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str

class TargetTypeDef(BaseValidatorModel):
    id: str
    port: Optional[int] = None

class TargetFailureTypeDef(BaseValidatorModel):
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None
    id: Optional[str] = None
    port: Optional[int] = None

class FixedResponseActionTypeDef(BaseValidatorModel):
    statusCode: int

class WeightedTargetGroupTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    weight: Optional[int] = None

class GetAccessLogSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str

class GetAuthPolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str

class GetListenerRequestRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class GetRuleRequestRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str

class GetServiceNetworkRequestRequestTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str

class GetServiceNetworkServiceAssociationRequestRequestTypeDef(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str

class GetServiceNetworkVpcAssociationRequestRequestTypeDef(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str

class GetServiceRequestRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str

class GetTargetGroupRequestRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str

class HeaderMatchTypeTypeDef(BaseValidatorModel):
    contains: Optional[str] = None
    exact: Optional[str] = None
    prefix: Optional[str] = None

class MatcherTypeDef(BaseValidatorModel):
    httpCode: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccessLogSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListListenersRequestRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListenerSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[ListenerProtocolType] = None

class ListRulesRequestRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RuleSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    isDefault: Optional[bool] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    priority: Optional[int] = None

class ListServiceNetworkServiceAssociationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None

class ListServiceNetworkVpcAssociationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    vpcIdentifier: Optional[str] = None

class ServiceNetworkVpcAssociationSummaryTypeDef(BaseValidatorModel):
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

class ListServiceNetworksRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ServiceNetworkSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    numberOfAssociatedServices: Optional[int] = None
    numberOfAssociatedVPCs: Optional[int] = None

class ListServicesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTargetGroupsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None

class TargetGroupSummaryTypeDef(BaseValidatorModel):
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

class TargetSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    port: Optional[int] = None
    reasonCode: Optional[str] = None
    status: Optional[TargetStatusType] = None

class PathMatchTypeTypeDef(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None

class PutAuthPolicyRequestRequestTypeDef(BaseValidatorModel):
    policy: str
    resourceIdentifier: str

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    policy: str
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAccessLogSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str
    destinationArn: str

class UpdateServiceNetworkRequestRequestTypeDef(BaseValidatorModel):
    authType: AuthTypeType
    serviceNetworkIdentifier: str

class UpdateServiceNetworkVpcAssociationRequestRequestTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    serviceNetworkVpcAssociationIdentifier: str

class UpdateServiceRequestRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None

class CreateAccessLogSubscriptionResponseTypeDef(BaseValidatorModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceNetworkResponseTypeDef(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceNetworkVpcAssociationResponseTypeDef(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceNetworkServiceAssociationResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceNetworkVpcAssociationResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTargetGroupResponseTypeDef(BaseValidatorModel):
    arn: str
    id: str
    status: TargetGroupStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccessLogSubscriptionResponseTypeDef(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destinationArn: str
    id: str
    lastUpdatedAt: datetime
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthPolicyResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceNetworkResponseTypeDef(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    createdAt: datetime
    id: str
    lastUpdatedAt: datetime
    name: str
    numberOfAssociatedServices: int
    numberOfAssociatedVPCs: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceNetworkVpcAssociationResponseTypeDef(BaseValidatorModel):
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

class ListAccessLogSubscriptionsResponseTypeDef(BaseValidatorModel):
    items: List[AccessLogSubscriptionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAuthPolicyResponseTypeDef(BaseValidatorModel):
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccessLogSubscriptionResponseTypeDef(BaseValidatorModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceNetworkResponseTypeDef(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceNetworkVpcAssociationResponseTypeDef(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    customDomainName: str
    id: str
    name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceNetworkServiceAssociationResponseTypeDef(BaseValidatorModel):
    arn: str
    createdBy: str
    customDomainName: str
    dnsEntry: DnsEntryTypeDef
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServiceResponseTypeDef(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    customDomainName: str
    dnsEntry: DnsEntryTypeDef
    id: str
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceNetworkServiceAssociationResponseTypeDef(BaseValidatorModel):
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

class GetServiceResponseTypeDef(BaseValidatorModel):
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

class ServiceNetworkServiceAssociationSummaryTypeDef(BaseValidatorModel):
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

class ServiceSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    customDomainName: Optional[str] = None
    dnsEntry: Optional[DnsEntryTypeDef] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[ServiceStatusType] = None

class DeregisterTargetsRequestRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]

class ListTargetsRequestRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targets: Optional[Sequence[TargetTypeDef]] = None

class RegisterTargetsRequestRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]

class DeregisterTargetsResponseTypeDef(BaseValidatorModel):
    successful: List[TargetTypeDef]
    unsuccessful: List[TargetFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTargetsResponseTypeDef(BaseValidatorModel):
    successful: List[TargetTypeDef]
    unsuccessful: List[TargetFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ForwardActionOutputTypeDef(BaseValidatorModel):
    targetGroups: List[WeightedTargetGroupTypeDef]

class ForwardActionTypeDef(BaseValidatorModel):
    targetGroups: Sequence[WeightedTargetGroupTypeDef]

class HeaderMatchTypeDef(BaseValidatorModel):
    match: HeaderMatchTypeTypeDef
    name: str
    caseSensitive: Optional[bool] = None

class HealthCheckConfigTypeDef(BaseValidatorModel):
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

class ListAccessLogSubscriptionsRequestListAccessLogSubscriptionsPaginateTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListListenersRequestListListenersPaginateTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceNetworkServiceAssociationsRequestListServiceNetworkServiceAssociationsPaginateTypeDef(BaseValidatorModel):
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServiceNetworksRequestListServiceNetworksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesRequestListServicesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetGroupsRequestListTargetGroupsPaginateTypeDef(BaseValidatorModel):
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsRequestListTargetsPaginateTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Optional[Sequence[TargetTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListListenersResponseTypeDef(BaseValidatorModel):
    items: List[ListenerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRulesResponseTypeDef(BaseValidatorModel):
    items: List[RuleSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceNetworkVpcAssociationsResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkVpcAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServiceNetworksResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetGroupsResponseTypeDef(BaseValidatorModel):
    items: List[TargetGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsResponseTypeDef(BaseValidatorModel):
    items: List[TargetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PathMatchTypeDef(BaseValidatorModel):
    match: PathMatchTypeTypeDef
    caseSensitive: Optional[bool] = None

class ListServiceNetworkServiceAssociationsResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkServiceAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesResponseTypeDef(BaseValidatorModel):
    items: List[ServiceSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RuleActionOutputTypeDef(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseActionTypeDef] = None
    forward: Optional[ForwardActionOutputTypeDef] = None

class RuleActionTypeDef(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseActionTypeDef] = None
    forward: Optional[ForwardActionTypeDef] = None

class TargetGroupConfigTypeDef(BaseValidatorModel):
    healthCheck: Optional[HealthCheckConfigTypeDef] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    lambdaEventStructureVersion: Optional[LambdaEventStructureVersionType] = None
    port: Optional[int] = None
    protocol: Optional[TargetGroupProtocolType] = None
    protocolVersion: Optional[TargetGroupProtocolVersionType] = None
    vpcIdentifier: Optional[str] = None

class UpdateTargetGroupRequestRequestTypeDef(BaseValidatorModel):
    healthCheck: HealthCheckConfigTypeDef
    targetGroupIdentifier: str

class HttpMatchOutputTypeDef(BaseValidatorModel):
    headerMatches: Optional[List[HeaderMatchTypeDef]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatchTypeDef] = None

class HttpMatchTypeDef(BaseValidatorModel):
    headerMatches: Optional[Sequence[HeaderMatchTypeDef]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatchTypeDef] = None

class CreateListenerResponseTypeDef(BaseValidatorModel):
    arn: str
    defaultAction: RuleActionOutputTypeDef
    id: str
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetListenerResponseTypeDef(BaseValidatorModel):
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

class UpdateListenerResponseTypeDef(BaseValidatorModel):
    arn: str
    defaultAction: RuleActionOutputTypeDef
    id: str
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateListenerRequestRequestTypeDef(BaseValidatorModel):
    defaultAction: RuleActionTypeDef
    name: str
    protocol: ListenerProtocolType
    serviceIdentifier: str
    clientToken: Optional[str] = None
    port: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateListenerRequestRequestTypeDef(BaseValidatorModel):
    defaultAction: RuleActionTypeDef
    listenerIdentifier: str
    serviceIdentifier: str

class CreateTargetGroupRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: TargetGroupTypeType
    clientToken: Optional[str] = None
    config: Optional[TargetGroupConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class CreateTargetGroupResponseTypeDef(BaseValidatorModel):
    arn: str
    config: TargetGroupConfigTypeDef
    id: str
    name: str
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetTargetGroupResponseTypeDef(BaseValidatorModel):
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

class UpdateTargetGroupResponseTypeDef(BaseValidatorModel):
    arn: str
    config: TargetGroupConfigTypeDef
    id: str
    name: str
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class RuleMatchOutputTypeDef(BaseValidatorModel):
    httpMatch: Optional[HttpMatchOutputTypeDef] = None

class RuleMatchTypeDef(BaseValidatorModel):
    httpMatch: Optional[HttpMatchTypeDef] = None

class CreateRuleResponseTypeDef(BaseValidatorModel):
    action: RuleActionOutputTypeDef
    arn: str
    id: str
    match: RuleMatchOutputTypeDef
    name: str
    priority: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetRuleResponseTypeDef(BaseValidatorModel):
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

class RuleUpdateSuccessTypeDef(BaseValidatorModel):
    action: Optional[RuleActionOutputTypeDef] = None
    arn: Optional[str] = None
    id: Optional[str] = None
    isDefault: Optional[bool] = None
    match: Optional[RuleMatchOutputTypeDef] = None
    name: Optional[str] = None
    priority: Optional[int] = None

class UpdateRuleResponseTypeDef(BaseValidatorModel):
    action: RuleActionOutputTypeDef
    arn: str
    id: str
    isDefault: bool
    match: RuleMatchOutputTypeDef
    name: str
    priority: int
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleRequestRequestTypeDef(BaseValidatorModel):
    action: RuleActionTypeDef
    listenerIdentifier: str
    match: RuleMatchTypeDef
    name: str
    priority: int
    serviceIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class RuleUpdateTypeDef(BaseValidatorModel):
    ruleIdentifier: str
    action: Optional[RuleActionTypeDef] = None
    match: Optional[RuleMatchTypeDef] = None
    priority: Optional[int] = None

class UpdateRuleRequestRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str
    action: Optional[RuleActionTypeDef] = None
    match: Optional[RuleMatchTypeDef] = None
    priority: Optional[int] = None

class BatchUpdateRuleResponseTypeDef(BaseValidatorModel):
    successful: List[RuleUpdateSuccessTypeDef]
    unsuccessful: List[RuleUpdateFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateRuleRequestRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    rules: Sequence[RuleUpdateTypeDef]
    serviceIdentifier: str

