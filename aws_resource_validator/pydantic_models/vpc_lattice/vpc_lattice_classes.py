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


# This class is the input for the 'create_access_log_subscription' function.
class CreateAccessLogSubscriptionRequest(BaseValidatorModel):
    destinationArn: str
    resourceIdentifier: str
    clientToken: Optional[str] = None
    serviceNetworkLogType: Optional[ServiceNetworkLogTypeType] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_resource_gateway' function.
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


# This class is the input for the 'create_service_network_resource_association' function.
class CreateServiceNetworkResourceAssociationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_service_network_service_association' function.
class CreateServiceNetworkServiceAssociationRequest(BaseValidatorModel):
    serviceIdentifier: str
    serviceNetworkIdentifier: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DnsEntry(BaseValidatorModel):
    domainName: Optional[str] = None
    hostedZoneId: Optional[str] = None


# This class is the input for the 'create_service_network_vpc_association' function.
class CreateServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str
    vpcIdentifier: str
    clientToken: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_service' function.
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


# This class is the input for the 'delete_resource_endpoint_association' function.
class DeleteResourceEndpointAssociationRequest(BaseValidatorModel):
    resourceEndpointAssociationIdentifier: str


# This class is the input for the 'delete_resource_gateway' function.
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


# This class is the input for the 'delete_service_network_resource_association' function.
class DeleteServiceNetworkResourceAssociationRequest(BaseValidatorModel):
    serviceNetworkResourceAssociationIdentifier: str


# This class is the input for the 'delete_service_network_service_association' function.
class DeleteServiceNetworkServiceAssociationRequest(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str


# This class is the input for the 'delete_service_network_vpc_association' function.
class DeleteServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str


# This class is the input for the 'delete_service' function.
class DeleteServiceRequest(BaseValidatorModel):
    serviceIdentifier: str


# This class is the input for the 'delete_target_group' function.
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


# This class is the input for the 'get_access_log_subscription' function.
class GetAccessLogSubscriptionRequest(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str


# This class is the input for the 'get_auth_policy' function.
class GetAuthPolicyRequest(BaseValidatorModel):
    resourceIdentifier: str


# This class is the input for the 'get_listener' function.
class GetListenerRequest(BaseValidatorModel):
    listenerIdentifier: str
    serviceIdentifier: str


# This class is the input for the 'get_resource_configuration' function.
class GetResourceConfigurationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str


# This class is the input for the 'get_resource_gateway' function.
class GetResourceGatewayRequest(BaseValidatorModel):
    resourceGatewayIdentifier: str


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'get_rule' function.
class GetRuleRequest(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str


# This class is the input for the 'get_service_network' function.
class GetServiceNetworkRequest(BaseValidatorModel):
    serviceNetworkIdentifier: str


# This class is the input for the 'get_service_network_resource_association' function.
class GetServiceNetworkResourceAssociationRequest(BaseValidatorModel):
    serviceNetworkResourceAssociationIdentifier: str


# This class is the input for the 'get_service_network_service_association' function.
class GetServiceNetworkServiceAssociationRequest(BaseValidatorModel):
    serviceNetworkServiceAssociationIdentifier: str


# This class is the input for the 'get_service_network_vpc_association' function.
class GetServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    serviceNetworkVpcAssociationIdentifier: str


# This class is the input for the 'get_service' function.
class GetServiceRequest(BaseValidatorModel):
    serviceIdentifier: str


# This class is the input for the 'get_target_group' function.
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


# This class is the input for the 'list_access_log_subscriptions' function.
class ListAccessLogSubscriptionsRequest(BaseValidatorModel):
    resourceIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_listeners' function.
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


# This class is the input for the 'list_resource_configurations' function.
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


# This class is the input for the 'list_resource_endpoint_associations' function.
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


# This class is the input for the 'list_resource_gateways' function.
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


# This class is the input for the 'list_rules' function.
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


# This class is the input for the 'list_service_network_resource_associations' function.
class ListServiceNetworkResourceAssociationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    resourceConfigurationIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None


# This class is the input for the 'list_service_network_service_associations' function.
class ListServiceNetworkServiceAssociationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    serviceIdentifier: Optional[str] = None
    serviceNetworkIdentifier: Optional[str] = None


# This class is the input for the 'list_service_network_vpc_associations' function.
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


# This class is the input for the 'list_service_network_vpc_endpoint_associations' function.
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


# This class is the input for the 'list_service_networks' function.
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


# This class is the input for the 'list_services' function.
class ListServicesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_target_groups' function.
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


# This class is the input for the 'put_auth_policy' function.
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


# This class is the input for the 'update_access_log_subscription' function.
class UpdateAccessLogSubscriptionRequest(BaseValidatorModel):
    accessLogSubscriptionIdentifier: str
    destinationArn: str


# This class is the input for the 'update_resource_gateway' function.
class UpdateResourceGatewayRequest(BaseValidatorModel):
    resourceGatewayIdentifier: str
    securityGroupIds: Optional[List[str]] = None


# This class is the input for the 'update_service_network' function.
class UpdateServiceNetworkRequest(BaseValidatorModel):
    authType: AuthTypeType
    serviceNetworkIdentifier: str


# This class is the input for the 'update_service_network_vpc_association' function.
class UpdateServiceNetworkVpcAssociationRequest(BaseValidatorModel):
    securityGroupIds: List[str]
    serviceNetworkVpcAssociationIdentifier: str


# This class is the input for the 'update_service' function.
class UpdateServiceRequest(BaseValidatorModel):
    serviceIdentifier: str
    authType: Optional[AuthTypeType] = None
    certificateArn: Optional[str] = None


# This class is the output for the 'create_access_log_subscription' function.
class CreateAccessLogSubscriptionResponse(BaseValidatorModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    serviceNetworkLogType: ServiceNetworkLogTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_resource_gateway' function.
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


# This class is the output for the 'create_service_network_resource_association' function.
class CreateServiceNetworkResourceAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    status: ServiceNetworkResourceAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service_network_vpc_association' function.
class CreateServiceNetworkVpcAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_endpoint_association' function.
class DeleteResourceEndpointAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    resourceConfigurationArn: str
    resourceConfigurationId: str
    vpcEndpointId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_gateway' function.
class DeleteResourceGatewayResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    status: ResourceGatewayStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service_network_resource_association' function.
class DeleteServiceNetworkResourceAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkResourceAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service_network_service_association' function.
class DeleteServiceNetworkServiceAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service_network_vpc_association' function.
class DeleteServiceNetworkVpcAssociationResponse(BaseValidatorModel):
    arn: str
    id: str
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service' function.
class DeleteServiceResponse(BaseValidatorModel):
    arn: str
    id: str
    name: str
    status: ServiceStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_target_group' function.
class DeleteTargetGroupResponse(BaseValidatorModel):
    arn: str
    id: str
    status: TargetGroupStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_access_log_subscription' function.
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


# This class is the output for the 'get_auth_policy' function.
class GetAuthPolicyResponse(BaseValidatorModel):
    createdAt: datetime
    lastUpdatedAt: datetime
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_gateway' function.
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


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_network_vpc_association' function.
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


# This class is the output for the 'list_access_log_subscriptions' function.
class ListAccessLogSubscriptionsResponse(BaseValidatorModel):
    items: List[AccessLogSubscriptionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_auth_policy' function.
class PutAuthPolicyResponse(BaseValidatorModel):
    policy: str
    state: AuthPolicyStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_access_log_subscription' function.
class UpdateAccessLogSubscriptionResponse(BaseValidatorModel):
    arn: str
    destinationArn: str
    id: str
    resourceArn: str
    resourceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_resource_gateway' function.
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


# This class is the output for the 'update_service_network' function.
class UpdateServiceNetworkResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_network_vpc_association' function.
class UpdateServiceNetworkVpcAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    id: str
    securityGroupIds: List[str]
    status: ServiceNetworkVpcAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service' function.
class UpdateServiceResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    certificateArn: str
    customDomainName: str
    id: str
    name: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_service_network' function.
class CreateServiceNetworkRequest(BaseValidatorModel):
    name: str
    authType: Optional[AuthTypeType] = None
    clientToken: Optional[str] = None
    sharingConfig: Optional[SharingConfig] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_service_network' function.
class CreateServiceNetworkResponse(BaseValidatorModel):
    arn: str
    authType: AuthTypeType
    id: str
    name: str
    sharingConfig: SharingConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_service_network' function.
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


# This class is the output for the 'create_service_network_service_association' function.
class CreateServiceNetworkServiceAssociationResponse(BaseValidatorModel):
    arn: str
    createdBy: str
    customDomainName: str
    dnsEntry: DnsEntry
    id: str
    status: ServiceNetworkServiceAssociationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_service' function.
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


# This class is the output for the 'get_service_network_resource_association' function.
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


# This class is the output for the 'get_service_network_service_association' function.
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


# This class is the output for the 'get_service' function.
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


# This class is the input for the 'deregister_targets' function.
class DeregisterTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: List[Target]


# This class is the input for the 'list_targets' function.
class ListTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targets: Optional[List[Target]] = None


# This class is the input for the 'register_targets' function.
class RegisterTargetsRequest(BaseValidatorModel):
    targetGroupIdentifier: str
    targets: List[Target]


# This class is the output for the 'deregister_targets' function.
class DeregisterTargetsResponse(BaseValidatorModel):
    successful: List[Target]
    unsuccessful: List[TargetFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_targets' function.
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


# This class is the output for the 'list_listeners' function.
class ListListenersResponse(BaseValidatorModel):
    items: List[ListenerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_resource_configurations' function.
class ListResourceConfigurationsResponse(BaseValidatorModel):
    items: List[ResourceConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_resource_endpoint_associations' function.
class ListResourceEndpointAssociationsResponse(BaseValidatorModel):
    items: List[ResourceEndpointAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_resource_gateways' function.
class ListResourceGatewaysResponse(BaseValidatorModel):
    items: List[ResourceGatewaySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_rules' function.
class ListRulesResponse(BaseValidatorModel):
    items: List[RuleSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_network_vpc_associations' function.
class ListServiceNetworkVpcAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkVpcAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_network_vpc_endpoint_associations' function.
class ListServiceNetworkVpcEndpointAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkEndpointAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_networks' function.
class ListServiceNetworksResponse(BaseValidatorModel):
    items: List[ServiceNetworkSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_target_groups' function.
class ListTargetGroupsResponse(BaseValidatorModel):
    items: List[TargetGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_targets' function.
class ListTargetsResponse(BaseValidatorModel):
    items: List[TargetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PathMatch(BaseValidatorModel):
    match: PathMatchType
    caseSensitive: Optional[bool] = None


# This class is the output for the 'list_service_network_resource_associations' function.
class ListServiceNetworkResourceAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkResourceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_service_network_service_associations' function.
class ListServiceNetworkServiceAssociationsResponse(BaseValidatorModel):
    items: List[ServiceNetworkServiceAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_services' function.
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


# This class is the input for the 'update_target_group' function.
class UpdateTargetGroupRequest(BaseValidatorModel):
    healthCheck: HealthCheckConfig
    targetGroupIdentifier: str


# This class is the input for the 'create_resource_configuration' function.
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


# This class is the output for the 'create_resource_configuration' function.
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


# This class is the output for the 'get_resource_configuration' function.
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


# This class is the input for the 'update_resource_configuration' function.
class UpdateResourceConfigurationRequest(BaseValidatorModel):
    resourceConfigurationIdentifier: str
    allowAssociationToShareableServiceNetwork: Optional[bool] = None
    portRanges: Optional[List[str]] = None
    resourceConfigurationDefinition: Optional[ResourceConfigurationDefinition] = None


# This class is the output for the 'update_resource_configuration' function.
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


# This class is the output for the 'create_listener' function.
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


# This class is the output for the 'get_listener' function.
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


# This class is the output for the 'update_listener' function.
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


# This class is the input for the 'create_target_group' function.
class CreateTargetGroupRequest(BaseValidatorModel):
    name: str
    type: TargetGroupTypeType
    clientToken: Optional[str] = None
    config: Optional[TargetGroupConfig] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'create_target_group' function.
class CreateTargetGroupResponse(BaseValidatorModel):
    arn: str
    config: TargetGroupConfig
    id: str
    name: str
    status: TargetGroupStatusType
    type: TargetGroupTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_target_group' function.
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


# This class is the output for the 'update_target_group' function.
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


# This class is the output for the 'create_rule' function.
class CreateRuleResponse(BaseValidatorModel):
    action: RuleActionOutput
    arn: str
    id: str
    match: RuleMatchOutput
    name: str
    priority: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_rule' function.
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


# This class is the output for the 'update_rule' function.
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


# This class is the input for the 'create_listener' function.
class CreateListenerRequest(BaseValidatorModel):
    defaultAction: RuleActionUnion
    name: str
    protocol: ListenerProtocolType
    serviceIdentifier: str
    clientToken: Optional[str] = None
    port: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_listener' function.
class UpdateListenerRequest(BaseValidatorModel):
    defaultAction: RuleActionUnion
    listenerIdentifier: str
    serviceIdentifier: str


# This class is the output for the 'batch_update_rule' function.
class BatchUpdateRuleResponse(BaseValidatorModel):
    successful: List[RuleUpdateSuccess]
    unsuccessful: List[RuleUpdateFailure]
    ResponseMetadata: ResponseMetadata

RuleMatchUnion = Union[RuleMatch, RuleMatchOutput]


# This class is the input for the 'create_rule' function.
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


# This class is the input for the 'update_rule' function.
class UpdateRuleRequest(BaseValidatorModel):
    listenerIdentifier: str
    ruleIdentifier: str
    serviceIdentifier: str
    action: Optional[RuleActionUnion] = None
    match: Optional[RuleMatchUnion] = None
    priority: Optional[int] = None


# This class is the input for the 'batch_update_rule' function.
class BatchUpdateRuleRequest(BaseValidatorModel):
    listenerIdentifier: str
    rules: List[RuleUpdate]
    serviceIdentifier: str