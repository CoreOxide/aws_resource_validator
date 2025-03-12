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
from aws_resource_validator.pydantic_models.globalaccelerator_constants import *

class AcceleratorAttributesTypeDef(BaseValidatorModel):
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class AcceleratorEventTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Timestamp: Optional[datetime] = None


class IpSetTypeDef(BaseValidatorModel):
    IpFamily: Optional[str] = None
    IpAddresses: Optional[List[str]] = None
    IpAddressFamily: Optional[IpAddressFamilyType] = None


class CustomRoutingEndpointConfigurationTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    AttachmentArn: Optional[str] = None


class CustomRoutingEndpointDescriptionTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EndpointConfigurationTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Weight: Optional[int] = None
    ClientIPPreservationEnabled: Optional[bool] = None
    AttachmentArn: Optional[str] = None


class EndpointDescriptionTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Weight: Optional[int] = None
    HealthState: Optional[HealthStateType] = None
    HealthReason: Optional[str] = None
    ClientIPPreservationEnabled: Optional[bool] = None


class AdvertiseByoipCidrRequestTypeDef(BaseValidatorModel):
    Cidr: str


class AllowCustomRoutingTrafficRequestTypeDef(BaseValidatorModel):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: Optional[Sequence[str]] = None
    DestinationPorts: Optional[Sequence[int]] = None
    AllowAllTrafficToEndpoint: Optional[bool] = None


class ResourceTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Cidr: Optional[str] = None
    Region: Optional[str] = None


class ByoipCidrEventTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Timestamp: Optional[datetime] = None


class CidrAuthorizationContextTypeDef(BaseValidatorModel):
    Message: str
    Signature: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class CustomRoutingDestinationConfigurationTypeDef(BaseValidatorModel):
    FromPort: int
    ToPort: int
    Protocols: Sequence[CustomRoutingProtocolType]


class PortRangeTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class PortOverrideTypeDef(BaseValidatorModel):
    ListenerPort: Optional[int] = None
    EndpointPort: Optional[int] = None


class CrossAccountResourceTypeDef(BaseValidatorModel):
    EndpointId: Optional[str] = None
    Cidr: Optional[str] = None
    AttachmentArn: Optional[str] = None


class CustomRoutingAcceleratorAttributesTypeDef(BaseValidatorModel):
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class CustomRoutingDestinationDescriptionTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    Protocols: Optional[List[ProtocolType]] = None


class DeleteAcceleratorRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str


class DeleteCrossAccountAttachmentRequestTypeDef(BaseValidatorModel):
    AttachmentArn: str


class DeleteCustomRoutingAcceleratorRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str


class DeleteCustomRoutingEndpointGroupRequestTypeDef(BaseValidatorModel):
    EndpointGroupArn: str


class DeleteCustomRoutingListenerRequestTypeDef(BaseValidatorModel):
    ListenerArn: str


class DeleteEndpointGroupRequestTypeDef(BaseValidatorModel):
    EndpointGroupArn: str


class DeleteListenerRequestTypeDef(BaseValidatorModel):
    ListenerArn: str


class DenyCustomRoutingTrafficRequestTypeDef(BaseValidatorModel):
    EndpointGroupArn: str
    EndpointId: str
    DestinationAddresses: Optional[Sequence[str]] = None
    DestinationPorts: Optional[Sequence[int]] = None
    DenyAllTrafficToEndpoint: Optional[bool] = None


class DeprovisionByoipCidrRequestTypeDef(BaseValidatorModel):
    Cidr: str


class DescribeAcceleratorAttributesRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str


class DescribeAcceleratorRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str


class DescribeCrossAccountAttachmentRequestTypeDef(BaseValidatorModel):
    AttachmentArn: str


class DescribeCustomRoutingAcceleratorAttributesRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str


class DescribeCustomRoutingAcceleratorRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str


class DescribeCustomRoutingEndpointGroupRequestTypeDef(BaseValidatorModel):
    EndpointGroupArn: str


class DescribeCustomRoutingListenerRequestTypeDef(BaseValidatorModel):
    ListenerArn: str


class DescribeEndpointGroupRequestTypeDef(BaseValidatorModel):
    EndpointGroupArn: str


class DescribeListenerRequestTypeDef(BaseValidatorModel):
    ListenerArn: str


class SocketAddressTypeDef(BaseValidatorModel):
    IpAddress: Optional[str] = None
    Port: Optional[int] = None


class EndpointIdentifierTypeDef(BaseValidatorModel):
    EndpointId: str
    ClientIPPreservationEnabled: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAcceleratorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListByoipCidrsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrossAccountAttachmentsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrossAccountResourcesRequestTypeDef(BaseValidatorModel):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingAcceleratorsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingEndpointGroupsRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingListenersRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsByDestinationRequestTypeDef(BaseValidatorModel):
    EndpointId: str
    DestinationAddress: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    EndpointGroupArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEndpointGroupsRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListListenersRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class RemoveCustomRoutingEndpointsRequestTypeDef(BaseValidatorModel):
    EndpointIds: Sequence[str]
    EndpointGroupArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateAcceleratorAttributesRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class UpdateAcceleratorRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None


class UpdateCustomRoutingAcceleratorAttributesRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    FlowLogsEnabled: Optional[bool] = None
    FlowLogsS3Bucket: Optional[str] = None
    FlowLogsS3Prefix: Optional[str] = None


class UpdateCustomRoutingAcceleratorRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None


class WithdrawByoipCidrRequestTypeDef(BaseValidatorModel):
    Cidr: str


class AcceleratorTypeDef(BaseValidatorModel):
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


class CustomRoutingAcceleratorTypeDef(BaseValidatorModel):
    AcceleratorArn: Optional[str] = None
    Name: Optional[str] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    Enabled: Optional[bool] = None
    IpSets: Optional[List[IpSetTypeDef]] = None
    DnsName: Optional[str] = None
    Status: Optional[CustomRoutingAcceleratorStatusType] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None


class AddCustomRoutingEndpointsRequestTypeDef(BaseValidatorModel):
    EndpointConfigurations: Sequence[CustomRoutingEndpointConfigurationTypeDef]
    EndpointGroupArn: str


class AddCustomRoutingEndpointsResponseTypeDef(BaseValidatorModel):
    EndpointDescriptions: List[CustomRoutingEndpointDescriptionTypeDef]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAcceleratorAttributesResponseTypeDef(BaseValidatorModel):
    AcceleratorAttributes: AcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ListCrossAccountResourceAccountsResponseTypeDef(BaseValidatorModel):
    ResourceOwnerAwsAccountIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAcceleratorAttributesResponseTypeDef(BaseValidatorModel):
    AcceleratorAttributes: AcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AddEndpointsRequestTypeDef(BaseValidatorModel):
    EndpointConfigurations: Sequence[EndpointConfigurationTypeDef]
    EndpointGroupArn: str


class AddEndpointsResponseTypeDef(BaseValidatorModel):
    EndpointDescriptions: List[EndpointDescriptionTypeDef]
    EndpointGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AttachmentTypeDef(BaseValidatorModel):
    AttachmentArn: Optional[str] = None
    Name: Optional[str] = None
    Principals: Optional[List[str]] = None
    Resources: Optional[List[ResourceTypeDef]] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None


class UpdateCrossAccountAttachmentRequestTypeDef(BaseValidatorModel):
    AttachmentArn: str
    Name: Optional[str] = None
    AddPrincipals: Optional[Sequence[str]] = None
    RemovePrincipals: Optional[Sequence[str]] = None
    AddResources: Optional[Sequence[ResourceTypeDef]] = None
    RemoveResources: Optional[Sequence[ResourceTypeDef]] = None


class ByoipCidrTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    State: Optional[ByoipCidrStateType] = None
    Events: Optional[List[ByoipCidrEventTypeDef]] = None


class ProvisionByoipCidrRequestTypeDef(BaseValidatorModel):
    Cidr: str
    CidrAuthorizationContext: CidrAuthorizationContextTypeDef


class CreateAcceleratorRequestTypeDef(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateCrossAccountAttachmentRequestTypeDef(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    Principals: Optional[Sequence[str]] = None
    Resources: Optional[Sequence[ResourceTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateCustomRoutingAcceleratorRequestTypeDef(BaseValidatorModel):
    Name: str
    IdempotencyToken: str
    IpAddressType: Optional[IpAddressTypeType] = None
    IpAddresses: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]


class CreateCustomRoutingEndpointGroupRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    EndpointGroupRegion: str
    DestinationConfigurations: Sequence[CustomRoutingDestinationConfigurationTypeDef]
    IdempotencyToken: str


class CreateCustomRoutingListenerRequestTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    PortRanges: Sequence[PortRangeTypeDef]
    IdempotencyToken: str


class CustomRoutingListenerTypeDef(BaseValidatorModel):
    ListenerArn: Optional[str] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None


class UpdateCustomRoutingListenerRequestTypeDef(BaseValidatorModel):
    ListenerArn: str
    PortRanges: Sequence[PortRangeTypeDef]


class CreateEndpointGroupRequestTypeDef(BaseValidatorModel):
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


class EndpointGroupTypeDef(BaseValidatorModel):
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


class UpdateEndpointGroupRequestTypeDef(BaseValidatorModel):
    EndpointGroupArn: str
    EndpointConfigurations: Optional[Sequence[EndpointConfigurationTypeDef]] = None
    TrafficDialPercentage: Optional[float] = None
    HealthCheckPort: Optional[int] = None
    HealthCheckProtocol: Optional[HealthCheckProtocolType] = None
    HealthCheckPath: Optional[str] = None
    HealthCheckIntervalSeconds: Optional[int] = None
    ThresholdCount: Optional[int] = None
    PortOverrides: Optional[Sequence[PortOverrideTypeDef]] = None


class ListCrossAccountResourcesResponseTypeDef(BaseValidatorModel):
    CrossAccountResources: List[CrossAccountResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeCustomRoutingAcceleratorAttributesResponseTypeDef(BaseValidatorModel):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCustomRoutingAcceleratorAttributesResponseTypeDef(BaseValidatorModel):
    AcceleratorAttributes: CustomRoutingAcceleratorAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CustomRoutingEndpointGroupTypeDef(BaseValidatorModel):
    EndpointGroupArn: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    DestinationDescriptions: Optional[List[CustomRoutingDestinationDescriptionTypeDef]] = None
    EndpointDescriptions: Optional[List[CustomRoutingEndpointDescriptionTypeDef]] = None


class DestinationPortMappingTypeDef(BaseValidatorModel):
    AcceleratorArn: Optional[str] = None
    AcceleratorSocketAddresses: Optional[List[SocketAddressTypeDef]] = None
    EndpointGroupArn: Optional[str] = None
    EndpointId: Optional[str] = None
    EndpointGroupRegion: Optional[str] = None
    DestinationSocketAddress: Optional[SocketAddressTypeDef] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DestinationTrafficState: Optional[CustomRoutingDestinationTrafficStateType] = None


class PortMappingTypeDef(BaseValidatorModel):
    AcceleratorPort: Optional[int] = None
    EndpointGroupArn: Optional[str] = None
    EndpointId: Optional[str] = None
    DestinationSocketAddress: Optional[SocketAddressTypeDef] = None
    Protocols: Optional[List[CustomRoutingProtocolType]] = None
    DestinationTrafficState: Optional[CustomRoutingDestinationTrafficStateType] = None


class RemoveEndpointsRequestTypeDef(BaseValidatorModel):
    EndpointIdentifiers: Sequence[EndpointIdentifierTypeDef]
    EndpointGroupArn: str


class ListAcceleratorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListByoipCidrsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCrossAccountAttachmentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCrossAccountResourcesRequestPaginateTypeDef(BaseValidatorModel):
    ResourceOwnerAwsAccountId: str
    AcceleratorArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomRoutingAcceleratorsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomRoutingEndpointGroupsRequestPaginateTypeDef(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomRoutingListenersRequestPaginateTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomRoutingPortMappingsByDestinationRequestPaginateTypeDef(BaseValidatorModel):
    EndpointId: str
    DestinationAddress: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomRoutingPortMappingsRequestPaginateTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    EndpointGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEndpointGroupsRequestPaginateTypeDef(BaseValidatorModel):
    ListenerArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListListenersRequestPaginateTypeDef(BaseValidatorModel):
    AcceleratorArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class CreateAcceleratorResponseTypeDef(BaseValidatorModel):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAcceleratorResponseTypeDef(BaseValidatorModel):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAcceleratorsResponseTypeDef(BaseValidatorModel):
    Accelerators: List[AcceleratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateAcceleratorResponseTypeDef(BaseValidatorModel):
    Accelerator: AcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomRoutingAcceleratorResponseTypeDef(BaseValidatorModel):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCustomRoutingAcceleratorResponseTypeDef(BaseValidatorModel):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomRoutingAcceleratorsResponseTypeDef(BaseValidatorModel):
    Accelerators: List[CustomRoutingAcceleratorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateCustomRoutingAcceleratorResponseTypeDef(BaseValidatorModel):
    Accelerator: CustomRoutingAcceleratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCrossAccountAttachmentResponseTypeDef(BaseValidatorModel):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCrossAccountAttachmentResponseTypeDef(BaseValidatorModel):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCrossAccountAttachmentsResponseTypeDef(BaseValidatorModel):
    CrossAccountAttachments: List[AttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateCrossAccountAttachmentResponseTypeDef(BaseValidatorModel):
    CrossAccountAttachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AdvertiseByoipCidrResponseTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeprovisionByoipCidrResponseTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListByoipCidrsResponseTypeDef(BaseValidatorModel):
    ByoipCidrs: List[ByoipCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ProvisionByoipCidrResponseTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WithdrawByoipCidrResponseTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomRoutingListenerResponseTypeDef(BaseValidatorModel):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCustomRoutingListenerResponseTypeDef(BaseValidatorModel):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomRoutingListenersResponseTypeDef(BaseValidatorModel):
    Listeners: List[CustomRoutingListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateCustomRoutingListenerResponseTypeDef(BaseValidatorModel):
    Listener: CustomRoutingListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListenerTypeDef(BaseValidatorModel):
    pass


class CreateListenerResponseTypeDef(BaseValidatorModel):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeListenerResponseTypeDef(BaseValidatorModel):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListListenersResponseTypeDef(BaseValidatorModel):
    Listeners: List[ListenerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateListenerResponseTypeDef(BaseValidatorModel):
    Listener: ListenerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEndpointGroupResponseTypeDef(BaseValidatorModel):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEndpointGroupResponseTypeDef(BaseValidatorModel):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEndpointGroupsResponseTypeDef(BaseValidatorModel):
    EndpointGroups: List[EndpointGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateEndpointGroupResponseTypeDef(BaseValidatorModel):
    EndpointGroup: EndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomRoutingEndpointGroupResponseTypeDef(BaseValidatorModel):
    EndpointGroup: CustomRoutingEndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCustomRoutingEndpointGroupResponseTypeDef(BaseValidatorModel):
    EndpointGroup: CustomRoutingEndpointGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomRoutingEndpointGroupsResponseTypeDef(BaseValidatorModel):
    EndpointGroups: List[CustomRoutingEndpointGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsByDestinationResponseTypeDef(BaseValidatorModel):
    DestinationPortMappings: List[DestinationPortMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCustomRoutingPortMappingsResponseTypeDef(BaseValidatorModel):
    PortMappings: List[PortMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


