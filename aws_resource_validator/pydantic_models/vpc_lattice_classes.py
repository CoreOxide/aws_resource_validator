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
from aws_resource_validator.pydantic_models.vpc_lattice_constants import *

class ArnResourceTypeDef(BaseValidatorModel):
    arn: Optional[str] = None


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


class CreateAccessLogSubscriptionRequestTypeDef(BaseValidatorModel):
    destinationArn: str
    resourceIdentifier: str
    clientToken: Optional[str] = None
    serviceNetworkLogType: Optional[ServiceNetworkLogTypeType] = None
    tags: Optional[Mapping[str, str]] = None


class CreateResourceGatewayRequestTypeDef(BaseValidatorModel):
    name: str
    subnetIds: Sequence[str]
    vpcIdentifier: str
    clientToken: Optional[str] = None
    ipAddressType: Optional[ResourceGatewayIpAddressTypeType] = None
    securityGroupIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class SharingConfigTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None


class CreateServiceNetworkResourceAssociationRequestTypeDef(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateServiceNetworkServiceAssociationRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DnsEntryTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    hostedZoneId: Optional[str] = None


class CreateServiceNetworkVpcAssociationRequestTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class CreateServiceRequestTypeDef(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None
    clientToken: Optional[str] = None
    customDomainName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteAccessLogSubscriptionRequestTypeDef(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str


class DeleteAuthPolicyRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str


class DeleteListenerRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str


class DeleteResourceConfigurationRequestTypeDef(BaseValidatorModel):
    resourceConfigurationIdentifier: str


class DeleteResourceEndpointAssociationRequestTypeDef(BaseValidatorModel):
    resourceEndpointAssociationIdentifier: str


class DeleteResourceGatewayRequestTypeDef(BaseValidatorModel):
    resourceGatewayIdentifier: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class DeleteRuleRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str


class DeleteServiceNetworkRequestTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str


class DeleteServiceNetworkResourceAssociationRequestTypeDef(BaseValidatorModel):
    serviceNetworkResourceAssociationIdentifier: str


class DeleteServiceNetworkServiceAssociationRequestTypeDef(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str


class DeleteServiceNetworkVpcAssociationRequestTypeDef(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str


class DeleteServiceRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str


class DeleteTargetGroupRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str


class DnsResourceTypeDef(BaseValidatorModel):
    domainName: Optional[str] = None
    ipAddressType: Optional[ResourceConfigurationIpAddressTypeType] = None


class FixedResponseActionTypeDef(BaseValidatorModel):
    statusCode: int


class WeightedTargetGroupTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    weight: Optional[int] = None


class GetAccessLogSubscriptionRequestTypeDef(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str


class GetAuthPolicyRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str


class GetListenerRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str


class GetResourceConfigurationRequestTypeDef(BaseValidatorModel):
    resourceConfigurationIdentifier: str


class GetResourceGatewayRequestTypeDef(BaseValidatorModel):
    resourceGatewayIdentifier: str


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class GetRuleRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str


class GetServiceNetworkRequestTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str


class GetServiceNetworkResourceAssociationRequestTypeDef(BaseValidatorModel):
    serviceNetworkResourceAssociationIdentifier: str


class GetServiceNetworkServiceAssociationRequestTypeDef(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str


class GetServiceNetworkVpcAssociationRequestTypeDef(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str


class GetServiceRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str


class GetTargetGroupRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str


class HeaderMatchTypeTypeDef(BaseValidatorModel):
    contains: Optional[str] = None
    exact: Optional[str] = None
    prefix: Optional[str] = None


class MatcherTypeDef(BaseValidatorModel):
    httpCode: Optional[str] = None


class IpResourceTypeDef(BaseValidatorModel):
    ipAddress: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccessLogSubscriptionsRequestTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListListenersRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListResourceConfigurationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceConfigurationGroupIdentifier: Optional[str] = None
    resourceGatewayIdentifier: Optional[str] = None


class ListResourceEndpointAssociationsRequestTypeDef(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceEndpointAssociationIdentifier: Optional[str] = None
    vpcEndpointId: Optional[str] = None
    vpcEndpointOwner: Optional[str] = None


class ListResourceGatewaysRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRulesRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListServiceNetworkResourceAssociationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceConfigurationIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None


class ListServiceNetworkServiceAssociationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None


class ListServiceNetworkVpcAssociationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    vpcIdentifier: Optional[str] = None


class ListServiceNetworkVpcEndpointAssociationsRequestTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListServiceNetworksRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListServicesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTargetGroupsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None


class PathMatchTypeTypeDef(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None


class PutAuthPolicyRequestTypeDef(BaseValidatorModel):
    policy: str
    resourceIdentifier: str


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    policy: str
    resourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAccessLogSubscriptionRequestTypeDef(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str
    destinationArn: str


class UpdateResourceGatewayRequestTypeDef(BaseValidatorModel):
    resourceGatewayIdentifier: str
    securityGroupIds: Optional[Sequence[str]] = None


class UpdateServiceNetworkRequestTypeDef(BaseValidatorModel):
    authType: AuthTypeType
    serviceNetworkIdentifier: str


class UpdateServiceNetworkVpcAssociationRequestTypeDef(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    serviceNetworkVpcAssociationIdentifier: str


class UpdateServiceRequestTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None


class GetAuthPolicyResponseTypeDef(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class AccessLogSubscriptionSummaryTypeDef(BaseValidatorModel):
    pass


class ListAccessLogSubscriptionsResponseTypeDef(BaseValidatorModel):
    items: List[AccessLogSubscriptionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutAuthPolicyResponseTypeDef(BaseValidatorModel):
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServiceNetworkRequestTypeDef(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    clientToken: Optional[str] = None
    sharingConfig: Optional[SharingConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class TargetTypeDef(BaseValidatorModel):
    pass


class DeregisterTargetsRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]


class ListTargetsRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targets: Optional[Sequence[TargetTypeDef]] = None


class RegisterTargetsRequestTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Sequence[TargetTypeDef]


class TargetFailureTypeDef(BaseValidatorModel):
    pass


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


class ResourceConfigurationDefinitionTypeDef(BaseValidatorModel):
    arnResource: Optional[ArnResourceTypeDef] = None
    dnsResource: Optional[DnsResourceTypeDef] = None
    ipResource: Optional[IpResourceTypeDef] = None


class ListAccessLogSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    resourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListListenersRequestPaginateTypeDef(BaseValidatorModel):
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    resourceConfigurationGroupIdentifier: Optional[str] = None
    resourceGatewayIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceEndpointAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    resourceEndpointAssociationIdentifier: Optional[str] = None
    vpcEndpointId: Optional[str] = None
    vpcEndpointOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourceGatewaysRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesRequestPaginateTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceNetworkResourceAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    resourceConfigurationIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceNetworkServiceAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceNetworkVpcAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: Optional[str] = None
    vpcIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceNetworkVpcEndpointAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    serviceNetworkIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceNetworksRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTargetGroupsRequestPaginateTypeDef(BaseValidatorModel):
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTargetsRequestPaginateTypeDef(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Optional[Sequence[TargetTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListenerSummaryTypeDef(BaseValidatorModel):
    pass


class ListListenersResponseTypeDef(BaseValidatorModel):
    items: List[ListenerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResourceConfigurationSummaryTypeDef(BaseValidatorModel):
    pass


class ListResourceConfigurationsResponseTypeDef(BaseValidatorModel):
    items: List[ResourceConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResourceEndpointAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListResourceEndpointAssociationsResponseTypeDef(BaseValidatorModel):
    items: List[ResourceEndpointAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ResourceGatewaySummaryTypeDef(BaseValidatorModel):
    pass


class ListResourceGatewaysResponseTypeDef(BaseValidatorModel):
    items: List[ResourceGatewaySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RuleSummaryTypeDef(BaseValidatorModel):
    pass


class ListRulesResponseTypeDef(BaseValidatorModel):
    items: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceNetworkVpcAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListServiceNetworkVpcAssociationsResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkVpcAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceNetworkEndpointAssociationTypeDef(BaseValidatorModel):
    pass


class ListServiceNetworkVpcEndpointAssociationsResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkEndpointAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceNetworkSummaryTypeDef(BaseValidatorModel):
    pass


class ListServiceNetworksResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TargetGroupSummaryTypeDef(BaseValidatorModel):
    pass


class ListTargetGroupsResponseTypeDef(BaseValidatorModel):
    items: List[TargetGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TargetSummaryTypeDef(BaseValidatorModel):
    pass


class ListTargetsResponseTypeDef(BaseValidatorModel):
    items: List[TargetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PathMatchTypeDef(BaseValidatorModel):
    match: PathMatchTypeTypeDef
    caseSensitive: Optional[bool] = None


class ServiceNetworkResourceAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListServiceNetworkResourceAssociationsResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkResourceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceNetworkServiceAssociationSummaryTypeDef(BaseValidatorModel):
    pass


class ListServiceNetworkServiceAssociationsResponseTypeDef(BaseValidatorModel):
    items: List[ServiceNetworkServiceAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceSummaryTypeDef(BaseValidatorModel):
    pass


class ListServicesResponseTypeDef(BaseValidatorModel):
    items: List[ServiceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RuleActionOutputTypeDef(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseActionTypeDef] = None
    forward: Optional[ForwardActionOutputTypeDef] = None


class TargetGroupConfigTypeDef(BaseValidatorModel):
    healthCheck: Optional[HealthCheckConfigTypeDef] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    lambdaEventStructureVersion: Optional[LambdaEventStructureVersionType] = None
    port: Optional[int] = None
    protocol: Optional[TargetGroupProtocolType] = None
    protocolVersion: Optional[TargetGroupProtocolVersionType] = None
    vpcIdentifier: Optional[str] = None


class UpdateTargetGroupRequestTypeDef(BaseValidatorModel):
    healthCheck: HealthCheckConfigTypeDef
    targetGroupIdentifier: str


class UpdateResourceConfigurationRequestTypeDef(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    allowAssociationToShareableServiceNetwork: Optional[bool] = None
    portRanges: Optional[Sequence[str]] = None
    resourceConfigurationDefinition: Optional[ResourceConfigurationDefinitionTypeDef] = None


class HttpMatchOutputTypeDef(BaseValidatorModel):
    headerMatches: Optional[List[HeaderMatchTypeDef]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatchTypeDef] = None


class HttpMatchTypeDef(BaseValidatorModel):
    headerMatches: Optional[Sequence[HeaderMatchTypeDef]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatchTypeDef] = None


class ForwardActionUnionTypeDef(BaseValidatorModel):
    pass


class RuleActionTypeDef(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseActionTypeDef] = None
    forward: Optional[ForwardActionUnionTypeDef] = None


class RuleMatchOutputTypeDef(BaseValidatorModel):
    httpMatch: Optional[HttpMatchOutputTypeDef] = None


class HttpMatchUnionTypeDef(BaseValidatorModel):
    pass


class RuleMatchTypeDef(BaseValidatorModel):
    httpMatch: Optional[HttpMatchUnionTypeDef] = None


class RuleActionUnionTypeDef(BaseValidatorModel):
    pass


class CreateListenerRequestTypeDef(BaseValidatorModel):
    defaultAction: RuleActionUnionTypeDef
    name: str
    protocol: ListenerProtocolType
    serviceIdentifier: str
    clientToken: Optional[str] = None
    port: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateListenerRequestTypeDef(BaseValidatorModel):
    defaultAction: RuleActionUnionTypeDef
    listenerIdentifier: str
    serviceIdentifier: str


class RuleUpdateSuccessTypeDef(BaseValidatorModel):
    pass


class BatchUpdateRuleResponseTypeDef(BaseValidatorModel):
    successful: List[RuleUpdateSuccessTypeDef]
    unsuccessful: List[RuleUpdateFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RuleMatchUnionTypeDef(BaseValidatorModel):
    pass


class CreateRuleRequestTypeDef(BaseValidatorModel):
    action: RuleActionUnionTypeDef
    listenerIdentifier: str
    match: RuleMatchUnionTypeDef
    name: str
    priority: int
    serviceIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class RuleUpdateTypeDef(BaseValidatorModel):
    ruleIdentifier: str
    action: Optional[RuleActionUnionTypeDef] = None
    match: Optional[RuleMatchUnionTypeDef] = None
    priority: Optional[int] = None


class UpdateRuleRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str
    action: Optional[RuleActionUnionTypeDef] = None
    match: Optional[RuleMatchUnionTypeDef] = None
    priority: Optional[int] = None


class BatchUpdateRuleRequestTypeDef(BaseValidatorModel):
    listenerIdentifier: str
    rules: Sequence[RuleUpdateTypeDef]
    serviceIdentifier: str


