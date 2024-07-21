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
from aws_resource_validator.pydantic_models.globalaccelerator_constants import *

class AcceleratorAttributesTypeDef(BaseModel):
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None

class AcceleratorEventTypeDef(BaseModel):
    Message: Optional[str] = None
    Timestamp: Optional[datetime] = None

class IpSetTypeDef(BaseModel):
    IpFamily: Optional[str] = None
    IpAddresses: Optional[List[str]] = None
    IpAddressFamily: Optional[IpAddressFamilyType] = None

class CustomRoutingEndpointConfigurationTypeDef(BaseModel):
    EndpointId: Optional[str] = None
    AttachmentArn: Optional[str] = None

class CustomRoutingEndpointDescriptionTypeDef(BaseModel):
    EndpointId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class EndpointConfigurationTypeDef(BaseModel):
    EndpointId: Optional[str] = None
    Weight: Optional[int] = None
    ClientIPPreservationEnabled: Optional[bool] = None
    AttachmentArn: Optional[str] = None

class EndpointDescriptionTypeDef(BaseModel):
    EndpointId: Optional[str] = None
    Weight: Optional[int] = None
    HealthState: Optional[HealthStateType] = None
    HealthReason: Optional[str] = None
    ClientIPPreservationEnabled: Optional[bool] = None

class AdvertiseByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str

class AllowCustomRoutingTrafficRequestRequestTypeDef(BaseModel):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: Optional[Sequence[str]] = None
    DestinationPorts: Optional[Sequence[int]] = None
    AllowAllTrafficToEndpoint: Optional[bool] = None

class ResourceTypeDef(BaseModel):
    EndpointId: Optional[str] = None
    Cidr: Optional[str] = None
    Region: Optional[str] = None

class ByoipCidrEventTypeDef(BaseModel):
    Message: Optional[str] = None
    Timestamp: Optional[datetime] = None

class CidrAuthorizationContextTypeDef(BaseModel):
    Message: str
    Signature: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CustomRoutingDestinationConfigurationTypeDef(BaseModel):
    FromPort: int
    ToPort: int
    Protocols: Sequence[CustomRoutingProtocolType]

class PortRangeTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class PortOverrideTypeDef(BaseModel):
    ListenerPort: Optional[int] = None
    EndpointPort: Optional[int] = None

class CrossAccountResourceTypeDef(BaseModel):
    EndpointId: Optional[str] = None
    Cidr: Optional[str] = None
    AttachmentArn: Optional[str] = None

class CustomRoutingAcceleratorAttributesTypeDef(BaseModel):
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None

class CustomRoutingDestinationDescriptionTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    Protocols: Optional[List[ProtocolType]] = None

class DeleteAcceleratorRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str

class DeleteCrossAccountAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentArn: str

class DeleteCustomRoutingAcceleratorRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str

class DeleteCustomRoutingEndpointGroupRequestRequestTypeDef(BaseModel):
    EndpointGroupArn: str

class DeleteCustomRoutingListenerRequestRequestTypeDef(BaseModel):
    ListenerArn: str

class DeleteEndpointGroupRequestRequestTypeDef(BaseModel):
    EndpointGroupArn: str

class DeleteListenerRequestRequestTypeDef(BaseModel):
    ListenerArn: str

class DenyCustomRoutingTrafficRequestRequestTypeDef(BaseModel):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: Optional[Sequence[str]] = None
    DestinationPorts: Optional[Sequence[int]] = None
    DenyAllTrafficToEndpoint: Optional[bool] = None

class DeprovisionByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str

class DescribeAcceleratorAttributesRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str

class DescribeAcceleratorRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str

class DescribeCrossAccountAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentArn: str

class DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str

class DescribeCustomRoutingAcceleratorRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str

class DescribeCustomRoutingEndpointGroupRequestRequestTypeDef(BaseModel):
    EndpointGroupArn: str

class DescribeCustomRoutingListenerRequestRequestTypeDef(BaseModel):
    ListenerArn: str

class DescribeEndpointGroupRequestRequestTypeDef(BaseModel):
    EndpointGroupArn: str

class DescribeListenerRequestRequestTypeDef(BaseModel):
    ListenerArn: str

class SocketAddressTypeDef(BaseModel):
    IpAddress: Optional[str] = None
    Port: Optional[int] = None

class EndpointIdentifierTypeDef(BaseModel):
    EndpointId: str
    ClientIPPreservationEnabled: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAcceleratorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListByoipCidrsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCrossAccountAttachmentsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCrossAccountResourcesRequestRequestTypeDef(BaseModel):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCustomRoutingAcceleratorsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCustomRoutingEndpointGroupsRequestRequestTypeDef(BaseModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCustomRoutingListenersRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef(BaseModel):
    EndpointId: str
    DestinationAddress: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCustomRoutingPortMappingsRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    EndpointGroupArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEndpointGroupsRequestRequestTypeDef(BaseModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListListenersRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class RemoveCustomRoutingEndpointsRequestRequestTypeDef(BaseModel):
    EndpointIds: Sequence[str]
    EndpointGroupArn: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateAcceleratorAttributesRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None

class UpdateAcceleratorRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class UpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None

class UpdateCustomRoutingAcceleratorRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class WithdrawByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str

class AcceleratorTypeDef(BaseModel):
    AcceleratorArn: Optional[str] = None
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    Enabled: Optional[bool] = None
    IpSets: Optional[List[IpSetTypeDef]] = None
    DnsName: Optional[str] = None
    Status: Optional[AcceleratorStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    DualStackDnsName: Optional[str] = None
    Events: Optional[List[AcceleratorEventTypeDef]] = None

class CustomRoutingAcceleratorTypeDef(BaseModel):
    AcceleratorArn: Optional[str] = None
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    Enabled: Optional[bool] = None
    IpSets: Optional[List[IpSetTypeDef]] = None
    DnsName: Optional[str] = None
    Status: Optional[CustomRoutingAcceleratorStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None

class AddCustomRoutingEndpointsRequestRequestTypeDef(BaseModel):
    EndpointConfigurations: Sequence[CustomRoutingEndpointConfigurationTypeDef]
    EndpointGroupArn: str

class AddCustomRoutingEndpointsResponseTypeDef(BaseModel):
    EndpointDescriptions: List[CustomRoutingEndpointDescriptionTypeDef]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorAttributesResponseTypeDef(BaseModel):
    AcceleratorAttributes: AcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrossAccountResourceAccountsResponseTypeDef(BaseModel):
    ResourceOwnerAwsAccountIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAcceleratorAttributesResponseTypeDef(BaseModel):
    AcceleratorAttributes: AcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddEndpointsRequestRequestTypeDef(BaseModel):
    EndpointConfigurations: Sequence[EndpointConfigurationTypeDef]
    EndpointGroupArn: str

class AddEndpointsResponseTypeDef(BaseModel):
    EndpointDescriptions: List[EndpointDescriptionTypeDef]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachmentTypeDef(BaseModel):
    AttachmentArn: Optional[str] = None
    Name: Optional[str] = None
    Principals: Optional[List[str]] = None
    Resources: Optional[List[ResourceTypeDef]] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None

class UpdateCrossAccountAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentArn: str
    Name: Optional[str] = None
    AddPrincipals: Optional[Sequence[str]] = None
    RemovePrincipals: Optional[Sequence[str]] = None
    AddResources: Optional[Sequence[ResourceTypeDef]] = None
    RemoveResources: Optional[Sequence[ResourceTypeDef]] = None

class ByoipCidrTypeDef(BaseModel):
    Cidr: Optional[str] = None
    State: Optional[ByoipCidrStateType] = None
    Events: Optional[List[ByoipCidrEventTypeDef]] = None

class ProvisionByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str
    CidrAuthorizationContext: CidrAuthorizationContextTypeDef

class CreateAcceleratorRequestRequestTypeDef(BaseModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateCrossAccountAttachmentRequestRequestTypeDef(BaseModel):
    Name: str
    IdempotencyToken: str
    Principals: Optional[Sequence[str]] = None
    Resources: Optional[Sequence[ResourceTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateCustomRoutingAcceleratorRequestRequestTypeDef(BaseModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateCustomRoutingEndpointGroupRequestRequestTypeDef(BaseModel):
    ListenerArn: str
    EndpointGroupRegion: str
    DestinationConfigurations: Sequence[CustomRoutingDestinationConfigurationTypeDef]
    IdempotencyToken: str

class CreateCustomRoutingListenerRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    PortRanges: Sequence[PortRangeTypeDef]
    IdempotencyToken: str

class CreateListenerRequestRequestTypeDef(BaseModel):
    AcceleratorArn: str
    PortRanges: Sequence[PortRangeTypeDef]
    Protocol: ProtocolType
    IdempotencyToken: str
    ClientAffinity: Optional[ClientAffinityType] = None

class CustomRoutingListenerTypeDef(BaseModel):
    ListenerArn: Optional[str] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None

class ListenerTypeDef(BaseModel):
    ListenerArn: Optional[str] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None
    Protocol: Optional[ProtocolType] = None
    ClientAffinity: Optional[ClientAffinityType] = None

class UpdateCustomRoutingListenerRequestRequestTypeDef(BaseModel):
    ListenerArn: str
    PortRanges: Sequence[PortRangeTypeDef]

class UpdateListenerRequestRequestTypeDef(BaseModel):
    ListenerArn: str
    PortRanges: Optional[Sequence[PortRangeTypeDef]] = None
    Protocol: Optional[ProtocolType] = None
    ClientAffinity: Optional[ClientAffinityType] = None

class CreateEndpointGroupRequestRequestTypeDef(BaseModel):
    ListenerArn: str
    EndpointGroupRegion: str
    IdempotencyToken: str
    EndpointConfigurations: Optional[Sequence[EndpointConfigurationTypeDef]] = None
    TrafficDialPercentage: Optional[float] = None
    HealthCheckPort: Optional[int] = None
    HealthCheckProtocol: Optional[HealthCheckProtocolType] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    ThresholdCount: Optional[int] = None
    PortOverrides: Optional[Sequence[PortOverrideTypeDef]] = None

class EndpointGroupTypeDef(BaseModel):
    EndpointGroupArn: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    EndpointDescriptions: Optional[List[EndpointDescriptionTypeDef]] = None
    TrafficDialPercentage: Optional[float] = None
    HealthCheckPort: Optional[int] = None
    HealthCheckProtocol: Optional[HealthCheckProtocolType] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    ThresholdCount: Optional[int] = None
    PortOverrides: Optional[List[PortOverrideTypeDef]] = None

class UpdateEndpointGroupRequestRequestTypeDef(BaseModel):
    EndpointGroupArn: str
    EndpointConfigurations: Optional[Sequence[EndpointConfigurationTypeDef]] = None
    TrafficDialPercentage: Optional[float] = None
    HealthCheckPort: Optional[int] = None
    HealthCheckProtocol: Optional[HealthCheckProtocolType] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    ThresholdCount: Optional[int] = None
    PortOverrides: Optional[Sequence[PortOverrideTypeDef]] = None

class ListCrossAccountResourcesResponseTypeDef(BaseModel):
    CrossAccountResources: List[CrossAccountResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeCustomRoutingAcceleratorAttributesResponseTypeDef(BaseModel):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCustomRoutingAcceleratorAttributesResponseTypeDef(BaseModel):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CustomRoutingEndpointGroupTypeDef(BaseModel):
    EndpointGroupArn: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    DestinationDescriptions: Optional[List[CustomRoutingDestinationDescriptionTypeDef]] = None
    EndpointDescriptions: Optional[List[CustomRoutingEndpointDescriptionTypeDef]] = None

class DestinationPortMappingTypeDef(BaseModel):
    AcceleratorArn: Optional[str] = None
    AcceleratorSocketAddresses: Optional[List[SocketAddressTypeDef]] = None
    EndpointGroupArn: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    DestinationSocketAddress: Optional[SocketAddressTypeDef] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DestinationTrafficState: Optional[CustomRoutingDestinationTrafficStateType] = None

class PortMappingTypeDef(BaseModel):
    AcceleratorPort: Optional[int] = None
    EndpointGroupArn: Optional[str] = None
    EndpointId: Optional[str] = None
    DestinationSocketAddress: Optional[SocketAddressTypeDef] = None
    Protocols: Optional[List[CustomRoutingProtocolType]] = None
    DestinationTrafficState: Optional[CustomRoutingDestinationTrafficStateType] = None

class RemoveEndpointsRequestRequestTypeDef(BaseModel):
    EndpointIdentifiers: Sequence[EndpointIdentifierTypeDef]
    EndpointGroupArn: str

class ListAcceleratorsRequestListAcceleratorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListByoipCidrsRequestListByoipCidrsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCrossAccountAttachmentsRequestListCrossAccountAttachmentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCrossAccountResourcesRequestListCrossAccountResourcesPaginateTypeDef(BaseModel):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomRoutingAcceleratorsRequestListCustomRoutingAcceleratorsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomRoutingEndpointGroupsRequestListCustomRoutingEndpointGroupsPaginateTypeDef(BaseModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomRoutingListenersRequestListCustomRoutingListenersPaginateTypeDef(BaseModel):
    AcceleratorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomRoutingPortMappingsByDestinationRequestListCustomRoutingPortMappingsByDestinationPaginateTypeDef(BaseModel):
    EndpointId: str
    DestinationAddress: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomRoutingPortMappingsRequestListCustomRoutingPortMappingsPaginateTypeDef(BaseModel):
    AcceleratorArn: str
    EndpointGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEndpointGroupsRequestListEndpointGroupsPaginateTypeDef(BaseModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListListenersRequestListListenersPaginateTypeDef(BaseModel):
    AcceleratorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateAcceleratorResponseTypeDef(BaseModel):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAcceleratorResponseTypeDef(BaseModel):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAcceleratorsResponseTypeDef(BaseModel):
    Accelerators: List[AcceleratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateAcceleratorResponseTypeDef(BaseModel):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomRoutingAcceleratorResponseTypeDef(BaseModel):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomRoutingAcceleratorResponseTypeDef(BaseModel):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomRoutingAcceleratorsResponseTypeDef(BaseModel):
    Accelerators: List[CustomRoutingAcceleratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateCustomRoutingAcceleratorResponseTypeDef(BaseModel):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCrossAccountAttachmentResponseTypeDef(BaseModel):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCrossAccountAttachmentResponseTypeDef(BaseModel):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCrossAccountAttachmentsResponseTypeDef(BaseModel):
    CrossAccountAttachments: List[AttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateCrossAccountAttachmentResponseTypeDef(BaseModel):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AdvertiseByoipCidrResponseTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionByoipCidrResponseTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListByoipCidrsResponseTypeDef(BaseModel):
    ByoipCidrs: List[ByoipCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ProvisionByoipCidrResponseTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WithdrawByoipCidrResponseTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomRoutingListenerResponseTypeDef(BaseModel):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomRoutingListenerResponseTypeDef(BaseModel):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomRoutingListenersResponseTypeDef(BaseModel):
    Listeners: List[CustomRoutingListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateCustomRoutingListenerResponseTypeDef(BaseModel):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateListenerResponseTypeDef(BaseModel):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeListenerResponseTypeDef(BaseModel):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListListenersResponseTypeDef(BaseModel):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateListenerResponseTypeDef(BaseModel):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEndpointGroupResponseTypeDef(BaseModel):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointGroupResponseTypeDef(BaseModel):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEndpointGroupsResponseTypeDef(BaseModel):
    EndpointGroups: List[EndpointGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateEndpointGroupResponseTypeDef(BaseModel):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomRoutingEndpointGroupResponseTypeDef(BaseModel):
    EndpointGroup: CustomRoutingEndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomRoutingEndpointGroupResponseTypeDef(BaseModel):
    EndpointGroup: CustomRoutingEndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomRoutingEndpointGroupsResponseTypeDef(BaseModel):
    EndpointGroups: List[CustomRoutingEndpointGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCustomRoutingPortMappingsByDestinationResponseTypeDef(BaseModel):
    DestinationPortMappings: List[DestinationPortMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCustomRoutingPortMappingsResponseTypeDef(BaseModel):
    PortMappings: List[PortMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

