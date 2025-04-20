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


class AdvertiseByoipCidrRequest(BaseValidatorModel):
    Cidr: str


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


class DeleteAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


class DeleteCrossAccountAttachmentRequest(BaseValidatorModel):
    AttachmentArn: str


class DeleteCustomRoutingAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


class DeleteCustomRoutingEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


class DeleteCustomRoutingListenerRequest(BaseValidatorModel):
    ListenerArn: str


class DeleteEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


class DeleteListenerRequest(BaseValidatorModel):
    ListenerArn: str


class DenyCustomRoutingTrafficRequest(BaseValidatorModel):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: Optional[List[str]] = None
    DestinationPorts: Optional[List[int]] = None
    DenyAllTrafficToEndpoint: Optional[bool] = None


class DeprovisionByoipCidrRequest(BaseValidatorModel):
    Cidr: str


class DescribeAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str


class DescribeAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


class DescribeCrossAccountAttachmentRequest(BaseValidatorModel):
    AttachmentArn: str


class DescribeCustomRoutingAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str


class DescribeCustomRoutingAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str


class DescribeCustomRoutingEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


class DescribeCustomRoutingListenerRequest(BaseValidatorModel):
    ListenerArn: str


class DescribeEndpointGroupRequest(BaseValidatorModel):
    EndpointGroupArn: str


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


class ListAcceleratorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListByoipCidrsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrossAccountAttachmentsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrossAccountResourcesRequest(BaseValidatorModel):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingAcceleratorsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingEndpointGroupsRequest(BaseValidatorModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingListenersRequest(BaseValidatorModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsByDestinationRequest(BaseValidatorModel):
    EndpointId: str
    DestinationAddress: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsRequest(BaseValidatorModel):
    AcceleratorArn: str
    EndpointGroupArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEndpointGroupsRequest(BaseValidatorModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListListenersRequest(BaseValidatorModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class RemoveCustomRoutingEndpointsRequest(BaseValidatorModel):
    EndpointIds: List[str]
    EndpointGroupArn: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


class UpdateAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class UpdateAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class UpdateCustomRoutingAcceleratorAttributesRequest(BaseValidatorModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class UpdateCustomRoutingAcceleratorRequest(BaseValidatorModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None


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


class AddCustomRoutingEndpointsRequest(BaseValidatorModel):
    EndpointConfigurations: List[CustomRoutingEndpointConfiguration]
    EndpointGroupArn: str


class AddCustomRoutingEndpointsResponse(BaseValidatorModel):
    EndpointDescriptions: List[CustomRoutingEndpointDescription]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadata


class DescribeAcceleratorAttributesResponse(BaseValidatorModel):
    AcceleratorAttributes: AcceleratorAttributes
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListCrossAccountResourceAccountsResponse(BaseValidatorModel):
    ResourceOwnerAwsAccountIds: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateAcceleratorAttributesResponse(BaseValidatorModel):
    AcceleratorAttributes: AcceleratorAttributes
    ResponseMetadata: ResponseMetadata


class AddEndpointsRequest(BaseValidatorModel):
    EndpointConfigurations: List[EndpointConfiguration]
    EndpointGroupArn: str


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


class ProvisionByoipCidrRequest(BaseValidatorModel):
    Cidr: str
    CidrAuthorizationContext: CidrAuthorizationContext


class CreateAcceleratorRequest(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class CreateCrossAccountAttachmentRequest(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    Principals: Optional[List[str]] = None
    Resources: Optional[List[Resource]] = None
    Tags: Optional[List[Tag]] = None


class CreateCustomRoutingAcceleratorRequest(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class CreateCustomRoutingEndpointGroupRequest(BaseValidatorModel):
    ListenerArn: str
    EndpointGroupRegion: str
    DestinationConfigurations: List[CustomRoutingDestinationConfiguration]
    IdempotencyToken: str


class CreateCustomRoutingListenerRequest(BaseValidatorModel):
    AcceleratorArn: str
    PortRanges: List[PortRange]
    IdempotencyToken: str


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


class UpdateCustomRoutingListenerRequest(BaseValidatorModel):
    ListenerArn: str
    PortRanges: List[PortRange]


class UpdateListenerRequest(BaseValidatorModel):
    ListenerArn: str
    PortRanges: Optional[List[PortRange]] = None
    Protocol: Optional[ProtocolType] = None
    ClientAffinity: Optional[ClientAffinityType] = None


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


class ListCrossAccountResourcesResponse(BaseValidatorModel):
    CrossAccountResources: List[CrossAccountResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeCustomRoutingAcceleratorAttributesResponse(BaseValidatorModel):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributes
    ResponseMetadata: ResponseMetadata


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


class CreateAcceleratorResponse(BaseValidatorModel):
    Accelerator: Accelerator
    ResponseMetadata: ResponseMetadata


class DescribeAcceleratorResponse(BaseValidatorModel):
    Accelerator: Accelerator
    ResponseMetadata: ResponseMetadata


class ListAcceleratorsResponse(BaseValidatorModel):
    Accelerators: List[Accelerator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateAcceleratorResponse(BaseValidatorModel):
    Accelerator: Accelerator
    ResponseMetadata: ResponseMetadata


class CreateCustomRoutingAcceleratorResponse(BaseValidatorModel):
    Accelerator: CustomRoutingAccelerator
    ResponseMetadata: ResponseMetadata


class DescribeCustomRoutingAcceleratorResponse(BaseValidatorModel):
    Accelerator: CustomRoutingAccelerator
    ResponseMetadata: ResponseMetadata


class ListCustomRoutingAcceleratorsResponse(BaseValidatorModel):
    Accelerators: List[CustomRoutingAccelerator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateCustomRoutingAcceleratorResponse(BaseValidatorModel):
    Accelerator: CustomRoutingAccelerator
    ResponseMetadata: ResponseMetadata


class CreateCrossAccountAttachmentResponse(BaseValidatorModel):
    CrossAccountAttachment: Attachment
    ResponseMetadata: ResponseMetadata


class DescribeCrossAccountAttachmentResponse(BaseValidatorModel):
    CrossAccountAttachment: Attachment
    ResponseMetadata: ResponseMetadata


class ListCrossAccountAttachmentsResponse(BaseValidatorModel):
    CrossAccountAttachments: List[Attachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateCrossAccountAttachmentResponse(BaseValidatorModel):
    CrossAccountAttachment: Attachment
    ResponseMetadata: ResponseMetadata


class AdvertiseByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


class DeprovisionByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


class ListByoipCidrsResponse(BaseValidatorModel):
    ByoipCidrs: List[ByoipCidr]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ProvisionByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


class WithdrawByoipCidrResponse(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


class CreateCustomRoutingListenerResponse(BaseValidatorModel):
    Listener: CustomRoutingListener
    ResponseMetadata: ResponseMetadata


class DescribeCustomRoutingListenerResponse(BaseValidatorModel):
    Listener: CustomRoutingListener
    ResponseMetadata: ResponseMetadata


class ListCustomRoutingListenersResponse(BaseValidatorModel):
    Listeners: List[CustomRoutingListener]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateCustomRoutingListenerResponse(BaseValidatorModel):
    Listener: CustomRoutingListener
    ResponseMetadata: ResponseMetadata


class CreateListenerResponse(BaseValidatorModel):
    Listener: Listener
    ResponseMetadata: ResponseMetadata


class DescribeListenerResponse(BaseValidatorModel):
    Listener: Listener
    ResponseMetadata: ResponseMetadata


class ListListenersResponse(BaseValidatorModel):
    Listeners: List[Listener]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateListenerResponse(BaseValidatorModel):
    Listener: Listener
    ResponseMetadata: ResponseMetadata


class CreateEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: EndpointGroup
    ResponseMetadata: ResponseMetadata


class DescribeEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: EndpointGroup
    ResponseMetadata: ResponseMetadata


class ListEndpointGroupsResponse(BaseValidatorModel):
    EndpointGroups: List[EndpointGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: EndpointGroup
    ResponseMetadata: ResponseMetadata


class CreateCustomRoutingEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: CustomRoutingEndpointGroup
    ResponseMetadata: ResponseMetadata


class DescribeCustomRoutingEndpointGroupResponse(BaseValidatorModel):
    EndpointGroup: CustomRoutingEndpointGroup
    ResponseMetadata: ResponseMetadata


class ListCustomRoutingEndpointGroupsResponse(BaseValidatorModel):
    EndpointGroups: List[CustomRoutingEndpointGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsByDestinationResponse(BaseValidatorModel):
    DestinationPortMappings: List[DestinationPortMapping]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsResponse(BaseValidatorModel):
    PortMappings: List[PortMapping]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None