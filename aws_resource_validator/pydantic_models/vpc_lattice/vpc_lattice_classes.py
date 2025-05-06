from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.vpc_lattice.vpc_lattice_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccessLogSubscriptionSummary(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destinationArn: str
    id: str
    lastUpdatedAt: datetime
    resourceArn: str
    resourceId: str
    serviceNetworkLogType: Optional[ServiceNetworkLogTypeType] = None


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
    tags: Optional[Dict[str, str]] = None


class CreateResourceGatewayRequest(BaseValidatorModel):
    name: str
    subnetIds: List[str]
    vpcIdentifier: str
    clientToken: Optional[str] = None
    ipAddressType: Optional[ResourceGatewayIpAddressTypeType] = None
    securityGroupIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None


class SharingConfig(BaseValidatorModel):
    enabled: Optional[bool] = None


class CreateServiceNetworkResourceAssociationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateServiceNetworkServiceAssociationRequest(BaseValidatorModel):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DnsEntry(BaseValidatorModel):
    domainName: Optional[str] = None
    hostedZoneId: Optional[str] = None


class CreateServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None


class CreateServiceRequest(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None
    clientToken: Optional[str] = None
    customDomainName: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


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


class Target(BaseValidatorModel):
    id: str
    port: Optional[int] = None


class TargetFailure(BaseValidatorModel):
    failureCode: Optional[str] = None
    failureMessage: Optional[str] = None
    id: Optional[str] = None
    port: Optional[int] = None


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


class ListenerSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    port: Optional[int] = None
    protocol: Optional[ListenerProtocolType] = None


class ListResourceConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceConfigurationGroupIdentifier: Optional[str] = None
    resourceGatewayIdentifier: Optional[str] = None


class ResourceConfigurationSummary(BaseValidatorModel):
    amazonManaged: Optional[bool] = None
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    resourceConfigurationGroupId: Optional[str] = None
    resourceGatewayId: Optional[str] = None
    status: Optional[ResourceConfigurationStatusType] = None
    type: Optional[ResourceConfigurationTypeType] = None


class ListResourceEndpointAssociationsRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceEndpointAssociationIdentifier: Optional[str] = None
    vpcEndpointId: Optional[str] = None
    vpcEndpointOwner: Optional[str] = None


class ResourceEndpointAssociationSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    id: Optional[str] = None
    resourceConfigurationArn: Optional[str] = None
    resourceConfigurationId: Optional[str] = None
    resourceConfigurationName: Optional[str] = None
    vpcEndpointId: Optional[str] = None
    vpcEndpointOwner: Optional[str] = None


class ListResourceGatewaysRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ResourceGatewaySummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    ipAddressType: Optional[ResourceGatewayIpAddressTypeType] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    status: Optional[ResourceGatewayStatusType] = None
    subnetIds: Optional[List[str]] = None
    vpcIdentifier: Optional[str] = None


class ListRulesRequest(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RuleSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    isDefault: Optional[bool] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    priority: Optional[int] = None


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


class ServiceNetworkVpcAssociationSummary(BaseValidatorModel):
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


class ListServiceNetworkVpcEndpointAssociationsRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ServiceNetworkEndpointAssociation(BaseValidatorModel):
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    serviceNetworkArn: Optional[str] = None
    state: Optional[str] = None
    vpcEndpointId: Optional[str] = None
    vpcEndpointOwnerId: Optional[str] = None
    vpcId: Optional[str] = None


class ListServiceNetworksRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ServiceNetworkSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    numberOfAssociatedResourceConfigurations: Optional[int] = None
    numberOfAssociatedServices: Optional[int] = None
    numberOfAssociatedVPCs: Optional[int] = None


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


class TargetGroupSummary(BaseValidatorModel):
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


class TargetSummary(BaseValidatorModel):
    id: Optional[str] = None
    port: Optional[int] = None
    reasonCode: Optional[str] = None
    status: Optional[TargetStatusType] = None


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
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateAccessLogSubscriptionRequest(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str
    destinationArn: str


class UpdateResourceGatewayRequest(BaseValidatorModel):
    resourceGatewayIdentifier: str
    securityGroupIds: Optional[List[str]] = None


class UpdateServiceNetworkRequest(BaseValidatorModel):
    authType: AuthTypeType
    serviceNetworkIdentifier: str


class UpdateServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    securityGroupIds: List[str]
    serviceNetworkVpcAssociationIdentifier: str


class UpdateServiceRequest(BaseValidatorModel):
    serviceIdentifier: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None


class CreateAccessLogSubscriptionResponse(BaseValidatorModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    serviceNetworkLogType: ServiceNetworkLogTypeType
    ResponseMetadata: ResponseMetadata


class CreateResourceGatewayResponse(BaseValidatorModel):
    arn: str
    id: str
    ipAddressType: ResourceGatewayIpAddressTypeType
    name: str
    securityGroupIds: List[str]
    status: ResourceGatewayStatusType
    subnetIds: List[str]
    vpcIdentifier: str
    ResponseMetadata: ResponseMetadata


class CreateServiceNetworkResourceAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    status: ServiceNetworkResourceAssociationStatusType
    ResponseMetadata: ResponseMetadata


class CreateServiceNetworkVpcAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadata


class DeleteResourceEndpointAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    resourceConfigurationArn: str
    resourceConfigurationId: str
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadata


class DeleteResourceGatewayResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    status: ResourceGatewayStatusType
    ResponseMetadata: ResponseMetadata


class DeleteServiceNetworkResourceAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkResourceAssociationStatusType
    ResponseMetadata: ResponseMetadata


class DeleteServiceNetworkServiceAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadata


class DeleteServiceNetworkVpcAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadata


class DeleteServiceResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadata


class DeleteTargetGroupResponse(BaseValidatorModel):
    arn: str
    id: str
    status: TargetGroupStatusType
    ResponseMetadata: ResponseMetadata


class GetAccessLogSubscriptionResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    destinationArn: str
    id: str
    lastUpdatedAt: datetime
    resourceArn: str
    resourceId: str
    serviceNetworkLogType: ServiceNetworkLogTypeType
    ResponseMetadata: ResponseMetadata


class GetAuthPolicyResponse(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadata


class GetResourceGatewayResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    id: str
    ipAddressType: ResourceGatewayIpAddressTypeType
    lastUpdatedAt: datetime
    name: str
    securityGroupIds: List[str]
    status: ResourceGatewayStatusType
    subnetIds: List[str]
    vpcId: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadata


class GetServiceNetworkVpcAssociationResponse(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


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


class UpdateAccessLogSubscriptionResponse(BaseValidatorModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadata


class UpdateResourceGatewayResponse(BaseValidatorModel):
    arn: str
    id: str
    ipAddressType: IpAddressTypeType
    name: str
    securityGroupIds: List[str]
    status: ResourceGatewayStatusType
    subnetIds: List[str]
    vpcId: str
    ResponseMetadata: ResponseMetadata


class UpdateServiceNetworkResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    ResponseMetadata: ResponseMetadata


class UpdateServiceNetworkVpcAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadata


class UpdateServiceResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    customDomainName: str
    id: str
    name: str
    ResponseMetadata: ResponseMetadata


class CreateServiceNetworkRequest(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    clientToken: Optional[str] = None
    sharingConfig: Optional[SharingConfig] = None
    tags: Optional[Dict[str, str]] = None


class CreateServiceNetworkResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    sharingConfig: SharingConfig
    ResponseMetadata: ResponseMetadata


class GetServiceNetworkResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    createdAt: datetime
    id: str
    lastUpdatedAt: datetime
    name: str
    numberOfAssociatedServices: int
    numberOfAssociatedVPCs: int
    sharingConfig: SharingConfig
    ResponseMetadata: ResponseMetadata


class CreateServiceNetworkServiceAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    customDomainName: str
    dnsEntry: DnsEntry
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadata


class CreateServiceResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    customDomainName: str
    dnsEntry: DnsEntry
    id: str
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadata


class GetServiceNetworkResourceAssociationResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    createdBy: str
    dnsEntry: DnsEntry
    failureCode: str
    failureReason: str
    id: str
    isManagedAssociation: bool
    lastUpdatedAt: datetime
    privateDnsEntry: DnsEntry
    resourceConfigurationArn: str
    resourceConfigurationId: str
    resourceConfigurationName: str
    serviceNetworkArn: str
    serviceNetworkId: str
    serviceNetworkName: str
    status: ServiceNetworkResourceAssociationStatusType
    ResponseMetadata: ResponseMetadata


class GetServiceNetworkServiceAssociationResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    createdBy: str
    customDomainName: str
    dnsEntry: DnsEntry
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
    ResponseMetadata: ResponseMetadata


class GetServiceResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    createdAt: datetime
    customDomainName: str
    dnsEntry: DnsEntry
    failureCode: str
    failureMessage: str
    id: str
    lastUpdatedAt: datetime
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadata


class ServiceNetworkResourceAssociationSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    dnsEntry: Optional[DnsEntry] = None
    failureCode: Optional[str] = None
    id: Optional[str] = None
    isManagedAssociation: Optional[bool] = None
    privateDnsEntry: Optional[DnsEntry] = None
    resourceConfigurationArn: Optional[str] = None
    resourceConfigurationId: Optional[str] = None
    resourceConfigurationName: Optional[str] = None
    serviceNetworkArn: Optional[str] = None
    serviceNetworkId: Optional[str] = None
    serviceNetworkName: Optional[str] = None
    status: Optional[ServiceNetworkResourceAssociationStatusType] = None


class ServiceNetworkServiceAssociationSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    createdBy: Optional[str] = None
    customDomainName: Optional[str] = None
    dnsEntry: Optional[DnsEntry] = None
    id: Optional[str] = None
    serviceArn: Optional[str] = None
    serviceId: Optional[str] = None
    serviceName: Optional[str] = None
    serviceNetworkArn: Optional[str] = None
    serviceNetworkId: Optional[str] = None
    serviceNetworkName: Optional[str] = None
    status: Optional[ServiceNetworkServiceAssociationStatusType] = None


class ServiceSummary(BaseValidatorModel):
    arn: Optional[str] = None
    createdAt: Optional[datetime] = None
    customDomainName: Optional[str] = None
    dnsEntry: Optional[DnsEntry] = None
    id: Optional[str] = None
    lastUpdatedAt: Optional[datetime] = None
    name: Optional[str] = None
    status: Optional[ServiceStatusType] = None


class DeregisterTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: List[Target]


class ListTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targets: Optional[List[Target]] = None


class RegisterTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: List[Target]


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
    targetGroups: List[WeightedTargetGroup]


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
    targets: Optional[List[Target]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListListenersResponse(BaseValidatorModel):
    items: List[ListenerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListResourceConfigurationsResponse(BaseValidatorModel):
    items: List[ResourceConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListResourceEndpointAssociationsResponse(BaseValidatorModel):
    items: List[ResourceEndpointAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListResourceGatewaysResponse(BaseValidatorModel):
    items: List[ResourceGatewaySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRulesResponse(BaseValidatorModel):
    items: List[RuleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceNetworkVpcAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkVpcAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceNetworkVpcEndpointAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkEndpointAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceNetworksResponse(BaseValidatorModel):
    items: List[ServiceNetworkSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTargetGroupsResponse(BaseValidatorModel):
    items: List[TargetGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTargetsResponse(BaseValidatorModel):
    items: List[TargetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PathMatch(BaseValidatorModel):
    match: PathMatchType
    caseSensitive: Optional[bool] = None


class ListServiceNetworkResourceAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkResourceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServiceNetworkServiceAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkServiceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListServicesResponse(BaseValidatorModel):
    items: List[ServiceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RuleActionOutput(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseAction] = None
    forward: Optional[ForwardActionOutput] = None

ForwardActionUnion = Union[ForwardAction, ForwardActionOutput]


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


class CreateResourceConfigurationRequest(BaseValidatorModel):
    name: str
    type: ResourceConfigurationTypeType
    allowAssociationToShareableServiceNetwork: Optional[bool] = None
    clientToken: Optional[str] = None
    portRanges: Optional[List[str]] = None
    protocol: Optional[Literal['TCP']] = None
    resourceConfigurationDefinition: Optional[ResourceConfigurationDefinition] = None
    resourceConfigurationGroupIdentifier: Optional[str] = None
    resourceGatewayIdentifier: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateResourceConfigurationResponse(BaseValidatorModel):
    allowAssociationToShareableServiceNetwork: bool
    arn: str
    createdAt: datetime
    failureReason: str
    id: str
    name: str
    portRanges: List[str]
    protocol: Literal['TCP']
    resourceConfigurationDefinition: ResourceConfigurationDefinition
    resourceConfigurationGroupId: str
    resourceGatewayId: str
    status: ResourceConfigurationStatusType
    type: ResourceConfigurationTypeType
    ResponseMetadata: ResponseMetadata


class GetResourceConfigurationResponse(BaseValidatorModel):
    allowAssociationToShareableServiceNetwork: bool
    amazonManaged: bool
    arn: str
    createdAt: datetime
    customDomainName: str
    failureReason: str
    id: str
    lastUpdatedAt: datetime
    name: str
    portRanges: List[str]
    protocol: Literal['TCP']
    resourceConfigurationDefinition: ResourceConfigurationDefinition
    resourceConfigurationGroupId: str
    resourceGatewayId: str
    status: ResourceConfigurationStatusType
    type: ResourceConfigurationTypeType
    ResponseMetadata: ResponseMetadata


class UpdateResourceConfigurationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    allowAssociationToShareableServiceNetwork: Optional[bool] = None
    portRanges: Optional[List[str]] = None
    resourceConfigurationDefinition: Optional[ResourceConfigurationDefinition] = None


class UpdateResourceConfigurationResponse(BaseValidatorModel):
    allowAssociationToShareableServiceNetwork: bool
    arn: str
    id: str
    name: str
    portRanges: List[str]
    protocol: Literal['TCP']
    resourceConfigurationDefinition: ResourceConfigurationDefinition
    resourceConfigurationGroupId: str
    resourceGatewayId: str
    status: ResourceConfigurationStatusType
    type: ResourceConfigurationTypeType
    ResponseMetadata: ResponseMetadata


class HttpMatchOutput(BaseValidatorModel):
    headerMatches: Optional[List[HeaderMatch]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatch] = None


class HttpMatch(BaseValidatorModel):
    headerMatches: Optional[List[HeaderMatch]] = None
    method: Optional[str] = None
    pathMatch: Optional[PathMatch] = None


class CreateListenerResponse(BaseValidatorModel):
    arn: str
    defaultAction: RuleActionOutput
    id: str
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadata


class GetListenerResponse(BaseValidatorModel):
    arn: str
    createdAt: datetime
    defaultAction: RuleActionOutput
    id: str
    lastUpdatedAt: datetime
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadata


class UpdateListenerResponse(BaseValidatorModel):
    arn: str
    defaultAction: RuleActionOutput
    id: str
    name: str
    port: int
    protocol: ListenerProtocolType
    serviceArn: str
    serviceId: str
    ResponseMetadata: ResponseMetadata


class RuleAction(BaseValidatorModel):
    fixedResponse: Optional[FixedResponseAction] = None
    forward: Optional[ForwardActionUnion] = None


class CreateTargetGroupRequest(BaseValidatorModel):
    name: str
    type: TargetGroupTypeType
    clientToken: Optional[str] = None
    config: Optional[TargetGroupConfig] = None
    tags: Optional[Dict[str, str]] = None


class CreateTargetGroupResponse(BaseValidatorModel):
    arn: str
    config: TargetGroupConfig
    id: str
    name: str
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadata


class GetTargetGroupResponse(BaseValidatorModel):
    arn: str
    config: TargetGroupConfig
    createdAt: datetime
    failureCode: str
    failureMessage: str
    id: str
    lastUpdatedAt: datetime
    name: str
    serviceArns: List[str]
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadata


class UpdateTargetGroupResponse(BaseValidatorModel):
    arn: str
    config: TargetGroupConfig
    id: str
    name: str
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadata


class RuleMatchOutput(BaseValidatorModel):
    httpMatch: Optional[HttpMatchOutput] = None

HttpMatchUnion = Union[HttpMatch, HttpMatchOutput]

RuleActionUnion = Union[RuleAction, RuleActionOutput]


class CreateRuleResponse(BaseValidatorModel):
    action: RuleActionOutput
    arn: str
    id: str
    match: RuleMatchOutput
    name: str
    priority: int
    ResponseMetadata: ResponseMetadata


class GetRuleResponse(BaseValidatorModel):
    action: RuleActionOutput
    arn: str
    createdAt: datetime
    id: str
    isDefault: bool
    lastUpdatedAt: datetime
    match: RuleMatchOutput
    name: str
    priority: int
    ResponseMetadata: ResponseMetadata


class RuleUpdateSuccess(BaseValidatorModel):
    action: Optional[RuleActionOutput] = None
    arn: Optional[str] = None
    id: Optional[str] = None
    isDefault: Optional[bool] = None
    match: Optional[RuleMatchOutput] = None
    name: Optional[str] = None
    priority: Optional[int] = None


class UpdateRuleResponse(BaseValidatorModel):
    action: RuleActionOutput
    arn: str
    id: str
    isDefault: bool
    match: RuleMatchOutput
    name: str
    priority: int
    ResponseMetadata: ResponseMetadata


class RuleMatch(BaseValidatorModel):
    httpMatch: Optional[HttpMatchUnion] = None


class CreateListenerRequest(BaseValidatorModel):
    defaultAction: RuleActionUnion
    name: str
    protocol: ListenerProtocolType
    serviceIdentifier: str
    clientToken: Optional[str] = None
    port: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class UpdateListenerRequest(BaseValidatorModel):
    defaultAction: RuleActionUnion
    listenerIdentifier: str
    serviceIdentifier: str


class BatchUpdateRuleResponse(BaseValidatorModel):
    successful: List[RuleUpdateSuccess]
    unsuccessful: List[RuleUpdateFailure]
    ResponseMetadata: ResponseMetadata

RuleMatchUnion = Union[RuleMatch, RuleMatchOutput]


class CreateRuleRequest(BaseValidatorModel):
    action: RuleActionUnion
    listenerIdentifier: str
    match: RuleMatchUnion
    name: str
    priority: int
    serviceIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


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
    rules: List[RuleUpdate]
    serviceIdentifier: str