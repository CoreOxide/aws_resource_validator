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

class ArnResource(BaseValidatorModel):
    arn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RuleUpdateFailure(BaseValidatorModel):
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None
    ruleIdentifier: Optional[str] = None


class CreateAccessLogSubscriptionRequest(BaseValidatorModel):
    destinationArn: str
    resourceIdentifier: str
    clientToken: Optional[str] = None
    serviceNetworkLogType: Optional[ServiceNetworkLogTypeType] = None
    tags: Optional[Mapping[str, str]] = None


class CreateResourceGatewayRequest(BaseValidatorModel):
    name: str
    subnetIds: Sequence[str]
    vpcIdentifier: str
    clientToken: Optional[str] = None
    ipAddressType: Optional[ResourceGatewayIpAddressTypeType] = None
    securityGroupIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class SharingConfig(BaseValidatorModel):
    enabled: Optional[bool] = None


class CreateServiceNetworkResourceAssociationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CreateServiceNetworkServiceAssociationRequest(BaseValidatorModel):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DnsEntry(BaseValidatorModel):
    domainName: Optional[str] = None
    hostedZoneId: Optional[str] = None


class CreateServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    tags: Optional[Mapping[str, str]] = None


class CreateServiceRequest(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None
    clientToken: Optional[str] = None
    customDomainName: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteAccessLogSubscriptionRequest(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str


class DeleteAuthPolicyRequest(BaseValidatorModel):
    resourceIdentifier: str


class DeleteListenerRequest(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str


class DeleteResourceConfigurationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str


class DeleteResourceEndpointAssociationRequest(BaseValidatorModel):
    resourceEndpointAssociationIdentifier: str


class DeleteResourceGatewayRequest(BaseValidatorModel):
    resourceGatewayIdentifier: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


class DeleteRuleRequest(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str


class DeleteServiceNetworkRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str


class DeleteServiceNetworkResourceAssociationRequest(BaseValidatorModel):
    serviceNetworkResourceAssociationIdentifier: str


class DeleteServiceNetworkServiceAssociationRequest(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str


class DeleteServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str


class DeleteServiceRequest(BaseValidatorModel):
    serviceIdentifier: str


class DeleteTargetGroupRequest(BaseValidatorModel):
    targetGroupIdentifier: str


class DnsResource(BaseValidatorModel):
    domainName: Optional[str] = None
    ipAddressType: Optional[ResourceConfigurationIpAddressTypeType] = None


class FixedResponseAction(BaseValidatorModel):
    statusCode: int


class WeightedTargetGroup(BaseValidatorModel):
    targetGroupIdentifier: str
    weight: Optional[int] = None


class GetAccessLogSubscriptionRequest(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str


class GetAuthPolicyRequest(BaseValidatorModel):
    resourceIdentifier: str


class GetListenerRequest(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str


class GetResourceConfigurationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str


class GetResourceGatewayRequest(BaseValidatorModel):
    resourceGatewayIdentifier: str


class GetResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


class GetRuleRequest(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str


class GetServiceNetworkRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str


class GetServiceNetworkResourceAssociationRequest(BaseValidatorModel):
    serviceNetworkResourceAssociationIdentifier: str


class GetServiceNetworkServiceAssociationRequest(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str


class GetServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str


class GetServiceRequest(BaseValidatorModel):
    serviceIdentifier: str


class GetTargetGroupRequest(BaseValidatorModel):
    targetGroupIdentifier: str


class HeaderMatchType(BaseValidatorModel):
    contains: Optional[str] = None
    exact: Optional[str] = None
    prefix: Optional[str] = None


class Matcher(BaseValidatorModel):
    httpCode: Optional[str] = None


class IpResource(BaseValidatorModel):
    ipAddress: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccessLogSubscriptionsRequest(BaseValidatorModel):
    resourceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListListenersRequest(BaseValidatorModel):
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListResourceConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceConfigurationGroupIdentifier: Optional[str] = None
    resourceGatewayIdentifier: Optional[str] = None


class ListResourceEndpointAssociationsRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceEndpointAssociationIdentifier: Optional[str] = None
    vpcEndpointId: Optional[str] = None
    vpcEndpointOwner: Optional[str] = None


class ListResourceGatewaysRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRulesRequest(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListServiceNetworkResourceAssociationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceConfigurationIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None


class ListServiceNetworkServiceAssociationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None


class ListServiceNetworkVpcAssociationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    vpcIdentifier: Optional[str] = None


class ListServiceNetworkVpcEndpointAssociationsRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListServiceNetworksRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListServicesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTargetGroupsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None


class PathMatchType(BaseValidatorModel):
    exact: Optional[str] = None
    prefix: Optional[str] = None


class PutAuthPolicyRequest(BaseValidatorModel):
    policy: str
    resourceIdentifier: str


class PutResourcePolicyRequest(BaseValidatorModel):
    policy: str
    resourceArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAccessLogSubscriptionRequest(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str
    destinationArn: str


class UpdateResourceGatewayRequest(BaseValidatorModel):
    resourceGatewayIdentifier: str
    securityGroupIds: Optional[Sequence[str]] = None


class UpdateServiceNetworkRequest(BaseValidatorModel):
    authType: AuthTypeType
    serviceNetworkIdentifier: str


class UpdateServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    securityGroupIds: Sequence[str]
    serviceNetworkVpcAssociationIdentifier: str


class UpdateServiceRequest(BaseValidatorModel):
    serviceIdentifier: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None


class GetAuthPolicyResponse(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadata


class AccessLogSubscriptionSummary(BaseValidatorModel):
    pass


class ListAccessLogSubscriptionsResponse(BaseValidatorModel):
    items: List[AccessLogSubscriptionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutAuthPolicyResponse(BaseValidatorModel):
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadata


class CreateServiceNetworkRequest(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    clientToken: Optional[str] = None
    sharingConfig: Optional[SharingConfig] = None
    tags: Optional[Mapping[str, str]] = None


class Target(BaseValidatorModel):
    pass


class DeregisterTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Sequence[Target]


class ListTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targets: Optional[Sequence[Target]] = None


class RegisterTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Sequence[Target]


class TargetFailure(BaseValidatorModel):
    pass


class DeregisterTargetsResponse(BaseValidatorModel):
    successful: List[Target]
    unsuccessful: List[TargetFailure]
    ResponseMetadata: ResponseMetadata


class RegisterTargetsResponse(BaseValidatorModel):
    successful: List[Target]
    unsuccessful: List[TargetFailure]
    ResponseMetadata: ResponseMetadata


class ForwardActionOutput(BaseValidatorModel):
    targetGroups: List[WeightedTargetGroup]


class ForwardAction(BaseValidatorModel):
    targetGroups: Sequence[WeightedTargetGroup]


class HeaderMatch(BaseValidatorModel):
    match: HeaderMatchType
    name: str
    caseSensitive: Optional[bool] = None


class HealthCheckConfig(BaseValidatorModel):
    enabled: Optional[bool] = None
    healthCheckIntervalSeconds: Optional[int] = None
    healthCheckTimeoutSeconds: Optional[int] = None
    healthyThresholdCount: Optional[int] = None
    matcher: Optional[Matcher] = None
    path: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[TargetGroupProtocolType] = None
    protocolVersion: Optional[HealthCheckProtocolVersionType] = None
    unhealthyThresholdCount: Optional[int] = None


class ResourceConfigurationDefinition(BaseValidatorModel):
    arnResource: Optional[ArnResource] = None
    dnsResource: Optional[DnsResource] = None
    ipResource: Optional[IpResource] = None


class ListAccessLogSubscriptionsRequestPaginate(BaseValidatorModel):
    resourceIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListListenersRequestPaginate(BaseValidatorModel):
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceConfigurationsRequestPaginate(BaseValidatorModel):
    resourceConfigurationGroupIdentifier: Optional[str] = None
    resourceGatewayIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceEndpointAssociationsRequestPaginate(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    resourceEndpointAssociationIdentifier: Optional[str] = None
    vpcEndpointId: Optional[str] = None
    vpcEndpointOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourceGatewaysRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesRequestPaginate(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceNetworkResourceAssociationsRequestPaginate(BaseValidatorModel):
    resourceConfigurationIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceNetworkServiceAssociationsRequestPaginate(BaseValidatorModel):
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceNetworkVpcAssociationsRequestPaginate(BaseValidatorModel):
    serviceNetworkIdentifier: Optional[str] = None
    vpcIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceNetworkVpcEndpointAssociationsRequestPaginate(BaseValidatorModel):
    serviceNetworkIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServiceNetworksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetGroupsRequestPaginate(BaseValidatorModel):
    targetGroupType: Optional[TargetGroupTypeType] = None
    vpcIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetsRequestPaginate(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: Optional[Sequence[Target]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListenerSummary(BaseValidatorModel):
    pass


class ListListenersResponse(BaseValidatorModel):
    items: List[ListenerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ResourceConfigurationSummary(BaseValidatorModel):
    pass


class ListResourceConfigurationsResponse(BaseValidatorModel):
    items: List[ResourceConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ResourceEndpointAssociationSummary(BaseValidatorModel):
    pass


class ListResourceEndpointAssociationsResponse(BaseValidatorModel):
    items: List[ResourceEndpointAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ResourceGatewaySummary(BaseValidatorModel):
    pass


class ListResourceGatewaysResponse(BaseValidatorModel):
    items: List[ResourceGatewaySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RuleSummary(BaseValidatorModel):
    pass


class ListRulesResponse(BaseValidatorModel):
    items: List[RuleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ServiceNetworkVpcAssociationSummary(BaseValidatorModel):
    pass


class ListServiceNetworkVpcAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkVpcAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ServiceNetworkEndpointAssociation(BaseValidatorModel):
    pass


class ListServiceNetworkVpcEndpointAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkEndpointAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ServiceNetworkSummary(BaseValidatorModel):
    pass


class ListServiceNetworksResponse(BaseValidatorModel):
    items: List[ServiceNetworkSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TargetGroupSummary(BaseValidatorModel):
    pass


class ListTargetGroupsResponse(BaseValidatorModel):
    items: List[TargetGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TargetSummary(BaseValidatorModel):
    pass


class ListTargetsResponse(BaseValidatorModel):
    items: List[TargetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PathMatch(BaseValidatorModel):
    match: PathMatchType
    caseSensitive: Optional[bool] = None


class ServiceNetworkResourceAssociationSummary(BaseValidatorModel):
    pass


class ListServiceNetworkResourceAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkResourceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ServiceNetworkServiceAssociationSummary(BaseValidatorModel):
    pass


class ListServiceNetworkServiceAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkServiceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ServiceSummary(BaseValidatorModel):
    pass


class ListServicesResponse(BaseValidatorModel):
    items: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RuleActionOutput(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseAction] = None
    forward: Optional[ForwardActionOutput] = None


class TargetGroupConfig(BaseValidatorModel):
    healthCheck: Optional[HealthCheckConfig] = None
    ipAddressType: Optional[IpAddressTypeType] = None
    lambdaEventStructureVersion: Optional[LambdaEventStructureVersionType] = None
    port: Optional[int] = None
    protocol: Optional[TargetGroupProtocolType] = None
    protocolVersion: Optional[TargetGroupProtocolVersionType] = None
    vpcIdentifier: Optional[str] = None


class UpdateTargetGroupRequest(BaseValidatorModel):
    healthCheck: HealthCheckConfig
    targetGroupIdentifier: str


class UpdateResourceConfigurationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    allowAssociationToShareableServiceNetwork: Optional[bool] = None
    portRanges: Optional[Sequence[str]] = None
    resourceConfigurationDefinition: Optional[ResourceConfigurationDefinition] = None


class HttpMatchOutput(BaseValidatorModel):
    headerMatches: Optional[List[HeaderMatch]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatch] = None


class HttpMatch(BaseValidatorModel):
    headerMatches: Optional[Sequence[HeaderMatch]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatch] = None


class ForwardActionUnion(BaseValidatorModel):
    pass


class RuleAction(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseAction] = None
    forward: Optional[ForwardActionUnion] = None


class RuleMatchOutput(BaseValidatorModel):
    httpMatch: Optional[HttpMatchOutput] = None


class HttpMatchUnion(BaseValidatorModel):
    pass


class RuleMatch(BaseValidatorModel):
    httpMatch: Optional[HttpMatchUnion] = None


class RuleActionUnion(BaseValidatorModel):
    pass


class CreateListenerRequest(BaseValidatorModel):
    defaultAction: RuleActionUnion
    name: str
    protocol: ListenerProtocolType
    serviceIdentifier: str
    clientToken: Optional[str] = None
    port: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateListenerRequest(BaseValidatorModel):
    defaultAction: RuleActionUnion
    listenerIdentifier: str
    serviceIdentifier: str


class RuleUpdateSuccess(BaseValidatorModel):
    pass


class BatchUpdateRuleResponse(BaseValidatorModel):
    successful: List[RuleUpdateSuccess]
    unsuccessful: List[RuleUpdateFailure]
    ResponseMetadata: ResponseMetadata


class RuleMatchUnion(BaseValidatorModel):
    pass


class CreateRuleRequest(BaseValidatorModel):
    action: RuleActionUnion
    listenerIdentifier: str
    match: RuleMatchUnion
    name: str
    priority: int
    serviceIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class RuleUpdate(BaseValidatorModel):
    ruleIdentifier: str
    action: Optional[RuleActionUnion] = None
    match: Optional[RuleMatchUnion] = None
    priority: Optional[int] = None


class UpdateRuleRequest(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str
    action: Optional[RuleActionUnion] = None
    match: Optional[RuleMatchUnion] = None
    priority: Optional[int] = None


class BatchUpdateRuleRequest(BaseValidatorModel):
    listenerIdentifier: str
    rules: Sequence[RuleUpdate]
    serviceIdentifier: str


