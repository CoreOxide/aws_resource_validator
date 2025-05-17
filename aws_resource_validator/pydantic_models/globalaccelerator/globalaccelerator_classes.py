from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.globalaccelerator.globalaccelerator_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceleratorAttributes(BaseValidatorModel):
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class AcceleratorEvent(BaseValidatorModel):
    Message: Optional[str] = None
    Timestamp: Optional[datetime] = None


class IpSet(BaseValidatorModel):
    IpFamily: Optional[str] = None
    IpAddresses: Optional[List[str]] = None
    IpAddressFamily: Optional[IpAddressFamilyType] = None


class CustomRoutingEndpointConfiguration(BaseValidatorModel):
    EndpointId: Optional[str] = None
    AttachmentArn: Optional[str] = None


class CustomRoutingEndpointDescription(BaseValidatorModel):
    EndpointId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EndpointConfiguration(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Weight: Optional[int] = None
    ClientIPPreservationEnabled: Optional[bool] = None
    AttachmentArn: Optional[str] = None


class EndpointDescription(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Weight: Optional[int] = None
    HealthState: Optional[HealthStateType] = None
    HealthReason: Optional[str] = None
    ClientIPPreservationEnabled: Optional[bool] = None


# This class is the input for the 'advertise_byoip_cidr' function.
class AdvertiseByoipCidrRequest(BaseValidatorModel):
    Cidr: str


# This class is the input for the 'allow_custom_routing_traffic' function.
class AllowCustomRoutingTrafficRequest(BaseValidatorModel):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: Optional[List[str]] = None
    DestinationPorts: Optional[List[int]] = None
    AllowAllTrafficToEndpoint: Optional[bool] = None


class Resource(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Cidr: Optional[str] = None
    Region: Optional[str] = None


class ByoipCidrEvent(BaseValidatorModel):
    Message: Optional[str] = None
    Timestamp: Optional[datetime] = None


class CidrAuthorizationContext(BaseValidatorModel):
    Message: str
    Signature: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CustomRoutingDestinationConfiguration(BaseValidatorModel):
    FromPort: int
    ToPort: int
    Protocols: List[CustomRoutingProtocolType]


class PortRange(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class PortOverride(BaseValidatorModel):
    ListenerPort: Optional[int] = None
    EndpointPort: Optional[int] = None


class CrossAccountResource(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Cidr: Optional[str] = None
    AttachmentArn: Optional[str] = None


class CustomRoutingAcceleratorAttributes(BaseValidatorModel):
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class CustomRoutingDestinationDescription(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    Protocols: Optional[List[ProtocolType]] = None


# This class is the input for the 'delete_accelerator' function.
class DeleteAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


# This class is the input for the 'delete_cross_account_attachment' function.
class DeleteCrossAccountAttachmentRequest(BaseValidatorModel):
    AttachmentArn: str


# This class is the input for the 'delete_custom_routing_accelerator' function.
class DeleteCustomRoutingAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


# This class is the input for the 'delete_custom_routing_endpoint_group' function.
class DeleteCustomRoutingEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


# This class is the input for the 'delete_custom_routing_listener' function.
class DeleteCustomRoutingListenerRequest(BaseValidatorModel):
    ListenerArn: str


# This class is the input for the 'delete_endpoint_group' function.
class DeleteEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


# This class is the input for the 'delete_listener' function.
class DeleteListenerRequest(BaseValidatorModel):
    ListenerArn: str


# This class is the input for the 'deny_custom_routing_traffic' function.
class DenyCustomRoutingTrafficRequest(BaseValidatorModel):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: Optional[List[str]] = None
    DestinationPorts: Optional[List[int]] = None
    DenyAllTrafficToEndpoint: Optional[bool] = None


# This class is the input for the 'deprovision_byoip_cidr' function.
class DeprovisionByoipCidrRequest(BaseValidatorModel):
    Cidr: str


# This class is the input for the 'describe_accelerator_attributes' function.
class DescribeAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str


# This class is the input for the 'describe_accelerator' function.
class DescribeAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


# This class is the input for the 'describe_cross_account_attachment' function.
class DescribeCrossAccountAttachmentRequest(BaseValidatorModel):
    AttachmentArn: str


# This class is the input for the 'describe_custom_routing_accelerator_attributes' function.
class DescribeCustomRoutingAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str


# This class is the input for the 'describe_custom_routing_accelerator' function.
class DescribeCustomRoutingAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


# This class is the input for the 'describe_custom_routing_endpoint_group' function.
class DescribeCustomRoutingEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


# This class is the input for the 'describe_custom_routing_listener' function.
class DescribeCustomRoutingListenerRequest(BaseValidatorModel):
    ListenerArn: str


# This class is the input for the 'describe_endpoint_group' function.
class DescribeEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


# This class is the input for the 'describe_listener' function.
class DescribeListenerRequest(BaseValidatorModel):
    ListenerArn: str


class SocketAddress(BaseValidatorModel):
    IpAddress: Optional[str] = None
    Port: Optional[int] = None


class EndpointIdentifier(BaseValidatorModel):
    EndpointId: str
    ClientIPPreservationEnabled: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_accelerators' function.
class ListAcceleratorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_byoip_cidrs' function.
class ListByoipCidrsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_cross_account_attachments' function.
class ListCrossAccountAttachmentsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_cross_account_resources' function.
class ListCrossAccountResourcesRequest(BaseValidatorModel):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_custom_routing_accelerators' function.
class ListCustomRoutingAcceleratorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_custom_routing_endpoint_groups' function.
class ListCustomRoutingEndpointGroupsRequest(BaseValidatorModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_custom_routing_listeners' function.
class ListCustomRoutingListenersRequest(BaseValidatorModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_custom_routing_port_mappings_by_destination' function.
class ListCustomRoutingPortMappingsByDestinationRequest(BaseValidatorModel):
    EndpointId: str
    DestinationAddress: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_custom_routing_port_mappings' function.
class ListCustomRoutingPortMappingsRequest(BaseValidatorModel):
    AcceleratorArn: str
    EndpointGroupArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_endpoint_groups' function.
class ListEndpointGroupsRequest(BaseValidatorModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_listeners' function.
class ListListenersRequest(BaseValidatorModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'remove_custom_routing_endpoints' function.
class RemoveCustomRoutingEndpointsRequest(BaseValidatorModel):
    EndpointIds: List[str]
    EndpointGroupArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_accelerator_attributes' function.
class UpdateAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


# This class is the input for the 'update_accelerator' function.
class UpdateAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None


# This class is the input for the 'update_custom_routing_accelerator_attributes' function.
class UpdateCustomRoutingAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


# This class is the input for the 'update_custom_routing_accelerator' function.
class UpdateCustomRoutingAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None


# This class is the input for the 'withdraw_byoip_cidr' function.
class WithdrawByoipCidrRequest(BaseValidatorModel):
    Cidr: str


class Accelerator(BaseValidatorModel):
    AcceleratorArn: Optional[str] = None
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    Enabled: Optional[bool] = None
    IpSets: Optional[List[IpSet]] = None
    DnsName: Optional[str] = None
    Status: Optional[AcceleratorStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    DualStackDnsName: Optional[str] = None
    Events: Optional[List[AcceleratorEvent]] = None


class CustomRoutingAccelerator(BaseValidatorModel):
    AcceleratorArn: Optional[str] = None
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    Enabled: Optional[bool] = None
    IpSets: Optional[List[IpSet]] = None
    DnsName: Optional[str] = None
    Status: Optional[CustomRoutingAcceleratorStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


# This class is the input for the 'add_custom_routing_endpoints' function.
class AddCustomRoutingEndpointsRequest(BaseValidatorModel):
    EndpointConfigurations: List[CustomRoutingEndpointConfiguration]
    EndpointGroupArn: str


# This class is the output for the 'add_custom_routing_endpoints' function.
class AddCustomRoutingEndpointsResponse(BaseValidatorModel):
    EndpointDescriptions: List[CustomRoutingEndpointDescription]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_accelerator_attributes' function.
class DescribeAcceleratorAttributesResponse(BaseValidatorModel):
    AcceleratorAttributes: AcceleratorAttributes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_endpoints' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListCrossAccountResourceAccountsResponse(BaseValidatorModel):
    ResourceOwnerAwsAccountIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_accelerator_attributes' function.
class UpdateAcceleratorAttributesResponse(BaseValidatorModel):
    AcceleratorAttributes: AcceleratorAttributes
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_endpoints' function.
class AddEndpointsRequest(BaseValidatorModel):
    EndpointConfigurations: List[EndpointConfiguration]
    EndpointGroupArn: str


# This class is the output for the 'add_endpoints' function.
class AddEndpointsResponse(BaseValidatorModel):
    EndpointDescriptions: List[EndpointDescription]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadata


class Attachment(BaseValidatorModel):
    AttachmentArn: Optional[str] = None
    Name: Optional[str] = None
    Principals: Optional[List[str]] = None
    Resources: Optional[List[Resource]] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None


# This class is the input for the 'update_cross_account_attachment' function.
class UpdateCrossAccountAttachmentRequest(BaseValidatorModel):
    AttachmentArn: str
    Name: Optional[str] = None
    AddPrincipals: Optional[List[str]] = None
    RemovePrincipals: Optional[List[str]] = None
    AddResources: Optional[List[Resource]] = None
    RemoveResources: Optional[List[Resource]] = None


class ByoipCidr(BaseValidatorModel):
    Cidr: Optional[str] = None
    State: Optional[ByoipCidrStateType] = None
    Events: Optional[List[ByoipCidrEvent]] = None


# This class is the input for the 'provision_byoip_cidr' function.
class ProvisionByoipCidrRequest(BaseValidatorModel):
    Cidr: str
    CidrAuthorizationContext: CidrAuthorizationContext


# This class is the input for the 'create_accelerator' function.
class CreateAcceleratorRequest(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cross_account_attachment' function.
class CreateCrossAccountAttachmentRequest(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    Principals: Optional[List[str]] = None
    Resources: Optional[List[Resource]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_custom_routing_accelerator' function.
class CreateCustomRoutingAcceleratorRequest(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the input for the 'create_custom_routing_endpoint_group' function.
class CreateCustomRoutingEndpointGroupRequest(BaseValidatorModel):
    ListenerArn: str
    EndpointGroupRegion: str
    DestinationConfigurations: List[CustomRoutingDestinationConfiguration]
    IdempotencyToken: str


# This class is the input for the 'create_custom_routing_listener' function.
class CreateCustomRoutingListenerRequest(BaseValidatorModel):
    AcceleratorArn: str
    PortRanges: List[PortRange]
    IdempotencyToken: str


# This class is the input for the 'create_listener' function.
class CreateListenerRequest(BaseValidatorModel):
    AcceleratorArn: str
    PortRanges: List[PortRange]
    Protocol: ProtocolType
    IdempotencyToken: str
    ClientAffinity: Optional[ClientAffinityType] = None


class CustomRoutingListener(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    PortRanges: Optional[List[PortRange]] = None


class Listener(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    PortRanges: Optional[List[PortRange]] = None
    Protocol: Optional[ProtocolType] = None
    ClientAffinity: Optional[ClientAffinityType] = None


# This class is the input for the 'update_custom_routing_listener' function.
class UpdateCustomRoutingListenerRequest(BaseValidatorModel):
    ListenerArn: str
    PortRanges: List[PortRange]


# This class is the input for the 'update_listener' function.
class UpdateListenerRequest(BaseValidatorModel):
    ListenerArn: str
    PortRanges: Optional[List[PortRange]] = None
    Protocol: Optional[ProtocolType] = None
    ClientAffinity: Optional[ClientAffinityType] = None


# This class is the input for the 'create_endpoint_group' function.
class CreateEndpointGroupRequest(BaseValidatorModel):
    ListenerArn: str
    EndpointGroupRegion: str
    IdempotencyToken: str
    EndpointConfigurations: Optional[List[EndpointConfiguration]] = None
    TrafficDialPercentage: Optional[float] = None
    HealthCheckPort: Optional[int] = None
    HealthCheckProtocol: Optional[HealthCheckProtocolType] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    ThresholdCount: Optional[int] = None
    PortOverrides: Optional[List[PortOverride]] = None


class EndpointGroup(BaseValidatorModel):
    EndpointGroupArn: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    EndpointDescriptions: Optional[List[EndpointDescription]] = None
    TrafficDialPercentage: Optional[float] = None
    HealthCheckPort: Optional[int] = None
    HealthCheckProtocol: Optional[HealthCheckProtocolType] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    ThresholdCount: Optional[int] = None
    PortOverrides: Optional[List[PortOverride]] = None


# This class is the input for the 'update_endpoint_group' function.
class UpdateEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str
    EndpointConfigurations: Optional[List[EndpointConfiguration]] = None
    TrafficDialPercentage: Optional[float] = None
    HealthCheckPort: Optional[int] = None
    HealthCheckProtocol: Optional[HealthCheckProtocolType] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    ThresholdCount: Optional[int] = None
    PortOverrides: Optional[List[PortOverride]] = None


# This class is the output for the 'list_cross_account_resources' function.
class ListCrossAccountResourcesResponse(BaseValidatorModel):
    CrossAccountResources: List[CrossAccountResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_custom_routing_accelerator_attributes' function.
class DescribeCustomRoutingAcceleratorAttributesResponse(BaseValidatorModel):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_custom_routing_accelerator_attributes' function.
class UpdateCustomRoutingAcceleratorAttributesResponse(BaseValidatorModel):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributes
    ResponseMetadata: ResponseMetadata


class CustomRoutingEndpointGroup(BaseValidatorModel):
    EndpointGroupArn: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    DestinationDescriptions: Optional[List[CustomRoutingDestinationDescription]] = None
    EndpointDescriptions: Optional[List[CustomRoutingEndpointDescription]] = None


class DestinationPortMapping(BaseValidatorModel):
    AcceleratorArn: Optional[str] = None
    AcceleratorSocketAddresses: Optional[List[SocketAddress]] = None
    EndpointGroupArn: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    DestinationSocketAddress: Optional[SocketAddress] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DestinationTrafficState: Optional[CustomRoutingDestinationTrafficStateType] = None


class PortMapping(BaseValidatorModel):
    AcceleratorPort: Optional[int] = None
    EndpointGroupArn: Optional[str] = None
    EndpointId: Optional[str] = None
    DestinationSocketAddress: Optional[SocketAddress] = None
    Protocols: Optional[List[CustomRoutingProtocolType]] = None
    DestinationTrafficState: Optional[CustomRoutingDestinationTrafficStateType] = None


# This class is the input for the 'remove_endpoints' function.
class RemoveEndpointsRequest(BaseValidatorModel):
    EndpointIdentifiers: List[EndpointIdentifier]
    EndpointGroupArn: str


class ListAcceleratorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListByoipCidrsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCrossAccountAttachmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCrossAccountResourcesRequestPaginate(BaseValidatorModel):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomRoutingAcceleratorsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomRoutingEndpointGroupsRequestPaginate(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomRoutingListenersRequestPaginate(BaseValidatorModel):
    AcceleratorArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomRoutingPortMappingsByDestinationRequestPaginate(BaseValidatorModel):
    EndpointId: str
    DestinationAddress: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomRoutingPortMappingsRequestPaginate(BaseValidatorModel):
    AcceleratorArn: str
    EndpointGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEndpointGroupsRequestPaginate(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListListenersRequestPaginate(BaseValidatorModel):
    AcceleratorArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'create_accelerator' function.
class CreateAcceleratorResponse(BaseValidatorModel):
    Accelerator: Accelerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_accelerator' function.
class DescribeAcceleratorResponse(BaseValidatorModel):
    Accelerator: Accelerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_accelerators' function.
class ListAcceleratorsResponse(BaseValidatorModel):
    Accelerators: List[Accelerator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_accelerator' function.
class UpdateAcceleratorResponse(BaseValidatorModel):
    Accelerator: Accelerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_custom_routing_accelerator' function.
class CreateCustomRoutingAcceleratorResponse(BaseValidatorModel):
    Accelerator: CustomRoutingAccelerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_custom_routing_accelerator' function.
class DescribeCustomRoutingAcceleratorResponse(BaseValidatorModel):
    Accelerator: CustomRoutingAccelerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_custom_routing_accelerators' function.
class ListCustomRoutingAcceleratorsResponse(BaseValidatorModel):
    Accelerators: List[CustomRoutingAccelerator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_custom_routing_accelerator' function.
class UpdateCustomRoutingAcceleratorResponse(BaseValidatorModel):
    Accelerator: CustomRoutingAccelerator
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cross_account_attachment' function.
class CreateCrossAccountAttachmentResponse(BaseValidatorModel):
    CrossAccountAttachment: Attachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cross_account_attachment' function.
class DescribeCrossAccountAttachmentResponse(BaseValidatorModel):
    CrossAccountAttachment: Attachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_cross_account_attachments' function.
class ListCrossAccountAttachmentsResponse(BaseValidatorModel):
    CrossAccountAttachments: List[Attachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_cross_account_attachment' function.
class UpdateCrossAccountAttachmentResponse(BaseValidatorModel):
    CrossAccountAttachment: Attachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'advertise_byoip_cidr' function.
class AdvertiseByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deprovision_byoip_cidr' function.
class DeprovisionByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_byoip_cidrs' function.
class ListByoipCidrsResponse(BaseValidatorModel):
    ByoipCidrs: List[ByoipCidr]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'provision_byoip_cidr' function.
class ProvisionByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'withdraw_byoip_cidr' function.
class WithdrawByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_custom_routing_listener' function.
class CreateCustomRoutingListenerResponse(BaseValidatorModel):
    Listener: CustomRoutingListener
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_custom_routing_listener' function.
class DescribeCustomRoutingListenerResponse(BaseValidatorModel):
    Listener: CustomRoutingListener
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_custom_routing_listeners' function.
class ListCustomRoutingListenersResponse(BaseValidatorModel):
    Listeners: List[CustomRoutingListener]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_custom_routing_listener' function.
class UpdateCustomRoutingListenerResponse(BaseValidatorModel):
    Listener: CustomRoutingListener
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_listener' function.
class CreateListenerResponse(BaseValidatorModel):
    Listener: Listener
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_listener' function.
class DescribeListenerResponse(BaseValidatorModel):
    Listener: Listener
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_listeners' function.
class ListListenersResponse(BaseValidatorModel):
    Listeners: List[Listener]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_listener' function.
class UpdateListenerResponse(BaseValidatorModel):
    Listener: Listener
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_endpoint_group' function.
class CreateEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: EndpointGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_endpoint_group' function.
class DescribeEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: EndpointGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_endpoint_groups' function.
class ListEndpointGroupsResponse(BaseValidatorModel):
    EndpointGroups: List[EndpointGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_endpoint_group' function.
class UpdateEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: EndpointGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_custom_routing_endpoint_group' function.
class CreateCustomRoutingEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: CustomRoutingEndpointGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_custom_routing_endpoint_group' function.
class DescribeCustomRoutingEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: CustomRoutingEndpointGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_custom_routing_endpoint_groups' function.
class ListCustomRoutingEndpointGroupsResponse(BaseValidatorModel):
    EndpointGroups: List[CustomRoutingEndpointGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_custom_routing_port_mappings_by_destination' function.
class ListCustomRoutingPortMappingsByDestinationResponse(BaseValidatorModel):
    DestinationPortMappings: List[DestinationPortMapping]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_custom_routing_port_mappings' function.
class ListCustomRoutingPortMappingsResponse(BaseValidatorModel):
    PortMappings: List[PortMapping]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None