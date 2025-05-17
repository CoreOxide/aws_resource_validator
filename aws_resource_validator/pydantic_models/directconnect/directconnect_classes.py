from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.directconnect.directconnect_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class RouteFilterPrefix(BaseValidatorModel):
    cidr: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'allocate_connection_on_interconnect' function.
class AllocateConnectionOnInterconnectRequest(BaseValidatorModel):
    bandwidth: str
    connectionName: str
    ownerAccount: str
    interconnectId: str
    vlan: int


class Tag(BaseValidatorModel):
    key: str
    value: Optional[str] = None


# This class is the input for the 'associate_connection_with_lag' function.
class AssociateConnectionWithLagRequest(BaseValidatorModel):
    connectionId: str
    lagId: str


# This class is the input for the 'associate_hosted_connection' function.
class AssociateHostedConnectionRequest(BaseValidatorModel):
    connectionId: str
    parentConnectionId: str


# This class is the input for the 'associate_mac_sec_key' function.
class AssociateMacSecKeyRequest(BaseValidatorModel):
    connectionId: str
    secretARN: Optional[str] = None
    ckn: Optional[str] = None
    cak: Optional[str] = None


class MacSecKey(BaseValidatorModel):
    secretARN: Optional[str] = None
    ckn: Optional[str] = None
    state: Optional[str] = None
    startOn: Optional[str] = None


# This class is the input for the 'associate_virtual_interface' function.
class AssociateVirtualInterfaceRequest(BaseValidatorModel):
    virtualInterfaceId: str
    connectionId: str


class AssociatedCoreNetwork(BaseValidatorModel):
    id: Optional[str] = None
    ownerAccount: Optional[str] = None
    attachmentId: Optional[str] = None


class AssociatedGateway(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[GatewayTypeType] = None
    ownerAccount: Optional[str] = None
    region: Optional[str] = None


class BGPPeer(BaseValidatorModel):
    bgpPeerId: Optional[str] = None
    asn: Optional[int] = None
    authKey: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    bgpPeerState: Optional[BGPPeerStateType] = None
    bgpStatus: Optional[BGPStatusType] = None
    awsDeviceV2: Optional[str] = None
    awsLogicalDeviceId: Optional[str] = None


# This class is the input for the 'confirm_connection' function.
class ConfirmConnectionRequest(BaseValidatorModel):
    connectionId: str


# This class is the input for the 'confirm_customer_agreement' function.
class ConfirmCustomerAgreementRequest(BaseValidatorModel):
    agreementName: Optional[str] = None


# This class is the input for the 'confirm_private_virtual_interface' function.
class ConfirmPrivateVirtualInterfaceRequest(BaseValidatorModel):
    virtualInterfaceId: str
    virtualGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None


# This class is the input for the 'confirm_public_virtual_interface' function.
class ConfirmPublicVirtualInterfaceRequest(BaseValidatorModel):
    virtualInterfaceId: str


# This class is the input for the 'confirm_transit_virtual_interface' function.
class ConfirmTransitVirtualInterfaceRequest(BaseValidatorModel):
    virtualInterfaceId: str
    directConnectGatewayId: str


class NewBGPPeer(BaseValidatorModel):
    asn: Optional[int] = None
    authKey: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None


# This class is the input for the 'create_direct_connect_gateway' function.
class CreateDirectConnectGatewayRequest(BaseValidatorModel):
    directConnectGatewayName: str
    amazonSideAsn: Optional[int] = None


class DirectConnectGateway(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayName: Optional[str] = None
    amazonSideAsn: Optional[int] = None
    ownerAccount: Optional[str] = None
    directConnectGatewayState: Optional[DirectConnectGatewayStateType] = None
    stateChangeError: Optional[str] = None


class CustomerAgreement(BaseValidatorModel):
    agreementName: Optional[str] = None
    status: Optional[str] = None


# This class is the input for the 'delete_bgp_peer' function.
class DeleteBGPPeerRequest(BaseValidatorModel):
    virtualInterfaceId: Optional[str] = None
    asn: Optional[int] = None
    customerAddress: Optional[str] = None
    bgpPeerId: Optional[str] = None


# This class is the input for the 'delete_connection' function.
class DeleteConnectionRequest(BaseValidatorModel):
    connectionId: str


# This class is the input for the 'delete_direct_connect_gateway_association_proposal' function.
class DeleteDirectConnectGatewayAssociationProposalRequest(BaseValidatorModel):
    proposalId: str


# This class is the input for the 'delete_direct_connect_gateway_association' function.
class DeleteDirectConnectGatewayAssociationRequest(BaseValidatorModel):
    associationId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    virtualGatewayId: Optional[str] = None


# This class is the input for the 'delete_direct_connect_gateway' function.
class DeleteDirectConnectGatewayRequest(BaseValidatorModel):
    directConnectGatewayId: str


# This class is the input for the 'delete_interconnect' function.
class DeleteInterconnectRequest(BaseValidatorModel):
    interconnectId: str


# This class is the input for the 'delete_lag' function.
class DeleteLagRequest(BaseValidatorModel):
    lagId: str


# This class is the input for the 'delete_virtual_interface' function.
class DeleteVirtualInterfaceRequest(BaseValidatorModel):
    virtualInterfaceId: str


# This class is the input for the 'describe_connection_loa' function.
class DescribeConnectionLoaRequest(BaseValidatorModel):
    connectionId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal['application/pdf']] = None


class Loa(BaseValidatorModel):
    loaContent: Optional[bytes] = None
    loaContentType: Optional[Literal['application/pdf']] = None


# This class is the input for the 'describe_connections_on_interconnect' function.
class DescribeConnectionsOnInterconnectRequest(BaseValidatorModel):
    interconnectId: str


# This class is the input for the 'describe_connections' function.
class DescribeConnectionsRequest(BaseValidatorModel):
    connectionId: Optional[str] = None


# This class is the input for the 'describe_direct_connect_gateway_association_proposals' function.
class DescribeDirectConnectGatewayAssociationProposalsRequest(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    proposalId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_direct_connect_gateway_associations' function.
class DescribeDirectConnectGatewayAssociationsRequest(BaseValidatorModel):
    associationId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    virtualGatewayId: Optional[str] = None


# This class is the input for the 'describe_direct_connect_gateway_attachments' function.
class DescribeDirectConnectGatewayAttachmentsRequest(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DirectConnectGatewayAttachment(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    virtualInterfaceRegion: Optional[str] = None
    virtualInterfaceOwnerAccount: Optional[str] = None
    attachmentState: Optional[DirectConnectGatewayAttachmentStateType] = None
    attachmentType: Optional[DirectConnectGatewayAttachmentTypeType] = None
    stateChangeError: Optional[str] = None


# This class is the input for the 'describe_direct_connect_gateways' function.
class DescribeDirectConnectGatewaysRequest(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'describe_hosted_connections' function.
class DescribeHostedConnectionsRequest(BaseValidatorModel):
    connectionId: str


# This class is the input for the 'describe_interconnect_loa' function.
class DescribeInterconnectLoaRequest(BaseValidatorModel):
    interconnectId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal['application/pdf']] = None


# This class is the input for the 'describe_interconnects' function.
class DescribeInterconnectsRequest(BaseValidatorModel):
    interconnectId: Optional[str] = None


# This class is the input for the 'describe_lags' function.
class DescribeLagsRequest(BaseValidatorModel):
    lagId: Optional[str] = None


# This class is the input for the 'describe_loa' function.
class DescribeLoaRequest(BaseValidatorModel):
    connectionId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal['application/pdf']] = None


# This class is the input for the 'describe_router_configuration' function.
class DescribeRouterConfigurationRequest(BaseValidatorModel):
    virtualInterfaceId: str
    routerTypeIdentifier: Optional[str] = None


class RouterType(BaseValidatorModel):
    vendor: Optional[str] = None
    platform: Optional[str] = None
    software: Optional[str] = None
    xsltTemplateName: Optional[str] = None
    xsltTemplateNameForMacSec: Optional[str] = None
    routerTypeIdentifier: Optional[str] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsRequest(BaseValidatorModel):
    resourceArns: List[str]


# This class is the input for the 'describe_virtual_interfaces' function.
class DescribeVirtualInterfacesRequest(BaseValidatorModel):
    connectionId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None


# This class is the input for the 'disassociate_connection_from_lag' function.
class DisassociateConnectionFromLagRequest(BaseValidatorModel):
    connectionId: str
    lagId: str


# This class is the input for the 'disassociate_mac_sec_key' function.
class DisassociateMacSecKeyRequest(BaseValidatorModel):
    connectionId: str
    secretARN: str


# This class is the input for the 'list_virtual_interface_test_history' function.
class ListVirtualInterfaceTestHistoryRequest(BaseValidatorModel):
    testId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    bgpPeers: Optional[List[str]] = None
    status: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class VirtualInterfaceTestHistory(BaseValidatorModel):
    testId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    bgpPeers: Optional[List[str]] = None
    status: Optional[str] = None
    ownerAccount: Optional[str] = None
    testDurationInMinutes: Optional[int] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class Location(BaseValidatorModel):
    locationCode: Optional[str] = None
    locationName: Optional[str] = None
    region: Optional[str] = None
    availablePortSpeeds: Optional[List[str]] = None
    availableProviders: Optional[List[str]] = None
    availableMacSecPortSpeeds: Optional[List[str]] = None


# This class is the input for the 'start_bgp_failover_test' function.
class StartBgpFailoverTestRequest(BaseValidatorModel):
    virtualInterfaceId: str
    bgpPeers: Optional[List[str]] = None
    testDurationInMinutes: Optional[int] = None


# This class is the input for the 'stop_bgp_failover_test' function.
class StopBgpFailoverTestRequest(BaseValidatorModel):
    virtualInterfaceId: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_connection' function.
class UpdateConnectionRequest(BaseValidatorModel):
    connectionId: str
    connectionName: Optional[str] = None
    encryptionMode: Optional[str] = None


# This class is the input for the 'update_direct_connect_gateway' function.
class UpdateDirectConnectGatewayRequest(BaseValidatorModel):
    directConnectGatewayId: str
    newDirectConnectGatewayName: str


# This class is the input for the 'update_lag' function.
class UpdateLagRequest(BaseValidatorModel):
    lagId: str
    lagName: Optional[str] = None
    minimumLinks: Optional[int] = None
    encryptionMode: Optional[str] = None


# This class is the input for the 'update_virtual_interface_attributes' function.
class UpdateVirtualInterfaceAttributesRequest(BaseValidatorModel):
    virtualInterfaceId: str
    mtu: Optional[int] = None
    enableSiteLink: Optional[bool] = None
    virtualInterfaceName: Optional[str] = None


class VirtualGateway(BaseValidatorModel):
    virtualGatewayId: Optional[str] = None
    virtualGatewayState: Optional[str] = None


# This class is the input for the 'accept_direct_connect_gateway_association_proposal' function.
class AcceptDirectConnectGatewayAssociationProposalRequest(BaseValidatorModel):
    directConnectGatewayId: str
    proposalId: str
    associatedGatewayOwnerAccount: str
    overrideAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None


# This class is the input for the 'create_direct_connect_gateway_association_proposal' function.
class CreateDirectConnectGatewayAssociationProposalRequest(BaseValidatorModel):
    directConnectGatewayId: str
    directConnectGatewayOwnerAccount: str
    gatewayId: str
    addAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None
    removeAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None


# This class is the input for the 'create_direct_connect_gateway_association' function.
class CreateDirectConnectGatewayAssociationRequest(BaseValidatorModel):
    directConnectGatewayId: str
    gatewayId: Optional[str] = None
    addAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None
    virtualGatewayId: Optional[str] = None


# This class is the input for the 'update_direct_connect_gateway_association' function.
class UpdateDirectConnectGatewayAssociationRequest(BaseValidatorModel):
    associationId: Optional[str] = None
    addAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None
    removeAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None


# This class is the output for the 'confirm_connection' function.
class ConfirmConnectionResponse(BaseValidatorModel):
    connectionState: ConnectionStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'confirm_customer_agreement' function.
class ConfirmCustomerAgreementResponse(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'confirm_private_virtual_interface' function.
class ConfirmPrivateVirtualInterfaceResponse(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'confirm_public_virtual_interface' function.
class ConfirmPublicVirtualInterfaceResponse(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'confirm_transit_virtual_interface' function.
class ConfirmTransitVirtualInterfaceResponse(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_interconnect' function.
class DeleteInterconnectResponse(BaseValidatorModel):
    interconnectState: InterconnectStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_virtual_interface' function.
class DeleteVirtualInterfaceResponse(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_loa' function.
class LoaResponse(BaseValidatorModel):
    loaContent: bytes
    loaContentType: Literal['application/pdf']
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'allocate_hosted_connection' function.
class AllocateHostedConnectionRequest(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    bandwidth: str
    connectionName: str
    vlan: int
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_connection' function.
class CreateConnectionRequest(BaseValidatorModel):
    location: str
    bandwidth: str
    connectionName: str
    lagId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    providerName: Optional[str] = None
    requestMACSec: Optional[bool] = None


# This class is the input for the 'create_interconnect' function.
class CreateInterconnectRequest(BaseValidatorModel):
    interconnectName: str
    bandwidth: str
    location: str
    lagId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    providerName: Optional[str] = None


# This class is the input for the 'create_lag' function.
class CreateLagRequest(BaseValidatorModel):
    numberOfConnections: int
    location: str
    connectionsBandwidth: str
    lagName: str
    connectionId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    childConnectionTags: Optional[List[Tag]] = None
    providerName: Optional[str] = None
    requestMACSec: Optional[bool] = None


# This class is the output for the 'create_interconnect' function.
class InterconnectResponse(BaseValidatorModel):
    interconnectId: str
    interconnectName: str
    interconnectState: InterconnectStateType
    region: str
    location: str
    bandwidth: str
    loaIssueTime: datetime
    lagId: str
    awsDevice: str
    jumboFrameCapable: bool
    awsDeviceV2: str
    awsLogicalDeviceId: str
    hasLogicalRedundancy: HasLogicalRedundancyType
    tags: List[Tag]
    providerName: str
    ResponseMetadata: ResponseMetadata


class Interconnect(BaseValidatorModel):
    interconnectId: Optional[str] = None
    interconnectName: Optional[str] = None
    interconnectState: Optional[InterconnectStateType] = None
    region: Optional[str] = None
    location: Optional[str] = None
    bandwidth: Optional[str] = None
    loaIssueTime: Optional[datetime] = None
    lagId: Optional[str] = None
    awsDevice: Optional[str] = None
    jumboFrameCapable: Optional[bool] = None
    awsDeviceV2: Optional[str] = None
    awsLogicalDeviceId: Optional[str] = None
    hasLogicalRedundancy: Optional[HasLogicalRedundancyType] = None
    tags: Optional[List[Tag]] = None
    providerName: Optional[str] = None


class NewPrivateVirtualInterfaceAllocation(BaseValidatorModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    customerAddress: Optional[str] = None
    tags: Optional[List[Tag]] = None


class NewPrivateVirtualInterface(BaseValidatorModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    virtualGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    enableSiteLink: Optional[bool] = None


class NewPublicVirtualInterfaceAllocation(BaseValidatorModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    routeFilterPrefixes: Optional[List[RouteFilterPrefix]] = None
    tags: Optional[List[Tag]] = None


class NewPublicVirtualInterface(BaseValidatorModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    routeFilterPrefixes: Optional[List[RouteFilterPrefix]] = None
    tags: Optional[List[Tag]] = None


class NewTransitVirtualInterfaceAllocation(BaseValidatorModel):
    virtualInterfaceName: Optional[str] = None
    vlan: Optional[int] = None
    asn: Optional[int] = None
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    tags: Optional[List[Tag]] = None


class NewTransitVirtualInterface(BaseValidatorModel):
    virtualInterfaceName: Optional[str] = None
    vlan: Optional[int] = None
    asn: Optional[int] = None
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    directConnectGatewayId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    enableSiteLink: Optional[bool] = None


class ResourceTag(BaseValidatorModel):
    resourceArn: Optional[str] = None
    tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the output for the 'associate_mac_sec_key' function.
class AssociateMacSecKeyResponse(BaseValidatorModel):
    connectionId: str
    macSecKeys: List[MacSecKey]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_connection' function.
class ConnectionResponse(BaseValidatorModel):
    ownerAccount: str
    connectionId: str
    connectionName: str
    connectionState: ConnectionStateType
    region: str
    location: str
    bandwidth: str
    vlan: int
    partnerName: str
    loaIssueTime: datetime
    lagId: str
    awsDevice: str
    jumboFrameCapable: bool
    awsDeviceV2: str
    awsLogicalDeviceId: str
    hasLogicalRedundancy: HasLogicalRedundancyType
    tags: List[Tag]
    providerName: str
    macSecCapable: bool
    portEncryptionStatus: str
    encryptionMode: str
    macSecKeys: List[MacSecKey]
    ResponseMetadata: ResponseMetadata


class Connection(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    connectionId: Optional[str] = None
    connectionName: Optional[str] = None
    connectionState: Optional[ConnectionStateType] = None
    region: Optional[str] = None
    location: Optional[str] = None
    bandwidth: Optional[str] = None
    vlan: Optional[int] = None
    partnerName: Optional[str] = None
    loaIssueTime: Optional[datetime] = None
    lagId: Optional[str] = None
    awsDevice: Optional[str] = None
    jumboFrameCapable: Optional[bool] = None
    awsDeviceV2: Optional[str] = None
    awsLogicalDeviceId: Optional[str] = None
    hasLogicalRedundancy: Optional[HasLogicalRedundancyType] = None
    tags: Optional[List[Tag]] = None
    providerName: Optional[str] = None
    macSecCapable: Optional[bool] = None
    portEncryptionStatus: Optional[str] = None
    encryptionMode: Optional[str] = None
    macSecKeys: Optional[List[MacSecKey]] = None


# This class is the output for the 'disassociate_mac_sec_key' function.
class DisassociateMacSecKeyResponse(BaseValidatorModel):
    connectionId: str
    macSecKeys: List[MacSecKey]
    ResponseMetadata: ResponseMetadata


class DirectConnectGatewayAssociationProposal(BaseValidatorModel):
    proposalId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayOwnerAccount: Optional[str] = None
    proposalState: Optional[DirectConnectGatewayAssociationProposalStateType] = None
    associatedGateway: Optional[AssociatedGateway] = None
    existingAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None
    requestedAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None


class DirectConnectGatewayAssociation(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayOwnerAccount: Optional[str] = None
    associationState: Optional[DirectConnectGatewayAssociationStateType] = None
    stateChangeError: Optional[str] = None
    associatedGateway: Optional[AssociatedGateway] = None
    associationId: Optional[str] = None
    allowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefix]] = None
    associatedCoreNetwork: Optional[AssociatedCoreNetwork] = None
    virtualGatewayId: Optional[str] = None
    virtualGatewayRegion: Optional[str] = None
    virtualGatewayOwnerAccount: Optional[str] = None


# This class is the output for the 'update_virtual_interface_attributes' function.
class VirtualInterfaceResponse(BaseValidatorModel):
    ownerAccount: str
    virtualInterfaceId: str
    location: str
    connectionId: str
    virtualInterfaceType: str
    virtualInterfaceName: str
    vlan: int
    asn: int
    amazonSideAsn: int
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamilyType
    virtualInterfaceState: VirtualInterfaceStateType
    customerRouterConfig: str
    mtu: int
    jumboFrameCapable: bool
    virtualGatewayId: str
    directConnectGatewayId: str
    routeFilterPrefixes: List[RouteFilterPrefix]
    bgpPeers: List[BGPPeer]
    region: str
    awsDeviceV2: str
    awsLogicalDeviceId: str
    tags: List[Tag]
    siteLinkEnabled: bool
    ResponseMetadata: ResponseMetadata


class VirtualInterface(BaseValidatorModel):
    ownerAccount: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    location: Optional[str] = None
    connectionId: Optional[str] = None
    virtualInterfaceType: Optional[str] = None
    virtualInterfaceName: Optional[str] = None
    vlan: Optional[int] = None
    asn: Optional[int] = None
    amazonSideAsn: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    virtualInterfaceState: Optional[VirtualInterfaceStateType] = None
    customerRouterConfig: Optional[str] = None
    mtu: Optional[int] = None
    jumboFrameCapable: Optional[bool] = None
    virtualGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    routeFilterPrefixes: Optional[List[RouteFilterPrefix]] = None
    bgpPeers: Optional[List[BGPPeer]] = None
    region: Optional[str] = None
    awsDeviceV2: Optional[str] = None
    awsLogicalDeviceId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    siteLinkEnabled: Optional[bool] = None


# This class is the input for the 'create_bgp_peer' function.
class CreateBGPPeerRequest(BaseValidatorModel):
    virtualInterfaceId: Optional[str] = None
    newBGPPeer: Optional[NewBGPPeer] = None


# This class is the output for the 'create_direct_connect_gateway' function.
class CreateDirectConnectGatewayResult(BaseValidatorModel):
    directConnectGateway: DirectConnectGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_direct_connect_gateway' function.
class DeleteDirectConnectGatewayResult(BaseValidatorModel):
    directConnectGateway: DirectConnectGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_direct_connect_gateways' function.
class DescribeDirectConnectGatewaysResult(BaseValidatorModel):
    directConnectGateways: List[DirectConnectGateway]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_direct_connect_gateway' function.
class UpdateDirectConnectGatewayResponse(BaseValidatorModel):
    directConnectGateway: DirectConnectGateway
    ResponseMetadata: ResponseMetadata


class DescribeCustomerMetadataResponse(BaseValidatorModel):
    agreements: List[CustomerAgreement]
    nniPartnerType: NniPartnerTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_connection_loa' function.
class DescribeConnectionLoaResponse(BaseValidatorModel):
    loa: Loa
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_interconnect_loa' function.
class DescribeInterconnectLoaResponse(BaseValidatorModel):
    loa: Loa
    ResponseMetadata: ResponseMetadata


class DescribeDirectConnectGatewayAssociationsRequestPaginate(BaseValidatorModel):
    associationId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    virtualGatewayId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDirectConnectGatewayAttachmentsRequestPaginate(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDirectConnectGatewaysRequestPaginate(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_direct_connect_gateway_attachments' function.
class DescribeDirectConnectGatewayAttachmentsResult(BaseValidatorModel):
    directConnectGatewayAttachments: List[DirectConnectGatewayAttachment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_router_configuration' function.
class DescribeRouterConfigurationResponse(BaseValidatorModel):
    customerRouterConfig: str
    router: RouterType
    virtualInterfaceId: str
    virtualInterfaceName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_virtual_interface_test_history' function.
class ListVirtualInterfaceTestHistoryResponse(BaseValidatorModel):
    virtualInterfaceTestHistory: List[VirtualInterfaceTestHistory]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_bgp_failover_test' function.
class StartBgpFailoverTestResponse(BaseValidatorModel):
    virtualInterfaceTest: VirtualInterfaceTestHistory
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_bgp_failover_test' function.
class StopBgpFailoverTestResponse(BaseValidatorModel):
    virtualInterfaceTest: VirtualInterfaceTestHistory
    ResponseMetadata: ResponseMetadata


class Locations(BaseValidatorModel):
    locations: List[Location]
    ResponseMetadata: ResponseMetadata


class VirtualGateways(BaseValidatorModel):
    virtualGateways: List[VirtualGateway]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_interconnects' function.
class Interconnects(BaseValidatorModel):
    interconnects: List[Interconnect]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'allocate_private_virtual_interface' function.
class AllocatePrivateVirtualInterfaceRequest(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocation


# This class is the input for the 'create_private_virtual_interface' function.
class CreatePrivateVirtualInterfaceRequest(BaseValidatorModel):
    connectionId: str
    newPrivateVirtualInterface: NewPrivateVirtualInterface


# This class is the input for the 'allocate_public_virtual_interface' function.
class AllocatePublicVirtualInterfaceRequest(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocation


# This class is the input for the 'create_public_virtual_interface' function.
class CreatePublicVirtualInterfaceRequest(BaseValidatorModel):
    connectionId: str
    newPublicVirtualInterface: NewPublicVirtualInterface


# This class is the input for the 'allocate_transit_virtual_interface' function.
class AllocateTransitVirtualInterfaceRequest(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocation


# This class is the input for the 'create_transit_virtual_interface' function.
class CreateTransitVirtualInterfaceRequest(BaseValidatorModel):
    connectionId: str
    newTransitVirtualInterface: NewTransitVirtualInterface


# This class is the output for the 'describe_tags' function.
class DescribeTagsResponse(BaseValidatorModel):
    resourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_hosted_connections' function.
class Connections(BaseValidatorModel):
    connections: List[Connection]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_lag' function.
class LagResponse(BaseValidatorModel):
    connectionsBandwidth: str
    numberOfConnections: int
    lagId: str
    ownerAccount: str
    lagName: str
    lagState: LagStateType
    location: str
    region: str
    minimumLinks: int
    awsDevice: str
    awsDeviceV2: str
    awsLogicalDeviceId: str
    connections: List[Connection]
    allowsHostedConnections: bool
    jumboFrameCapable: bool
    hasLogicalRedundancy: HasLogicalRedundancyType
    tags: List[Tag]
    providerName: str
    macSecCapable: bool
    encryptionMode: str
    macSecKeys: List[MacSecKey]
    ResponseMetadata: ResponseMetadata


class Lag(BaseValidatorModel):
    connectionsBandwidth: Optional[str] = None
    numberOfConnections: Optional[int] = None
    lagId: Optional[str] = None
    ownerAccount: Optional[str] = None
    lagName: Optional[str] = None
    lagState: Optional[LagStateType] = None
    location: Optional[str] = None
    region: Optional[str] = None
    minimumLinks: Optional[int] = None
    awsDevice: Optional[str] = None
    awsDeviceV2: Optional[str] = None
    awsLogicalDeviceId: Optional[str] = None
    connections: Optional[List[Connection]] = None
    allowsHostedConnections: Optional[bool] = None
    jumboFrameCapable: Optional[bool] = None
    hasLogicalRedundancy: Optional[HasLogicalRedundancyType] = None
    tags: Optional[List[Tag]] = None
    providerName: Optional[str] = None
    macSecCapable: Optional[bool] = None
    encryptionMode: Optional[str] = None
    macSecKeys: Optional[List[MacSecKey]] = None


# This class is the output for the 'create_direct_connect_gateway_association_proposal' function.
class CreateDirectConnectGatewayAssociationProposalResult(BaseValidatorModel):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposal
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_direct_connect_gateway_association_proposal' function.
class DeleteDirectConnectGatewayAssociationProposalResult(BaseValidatorModel):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposal
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_direct_connect_gateway_association_proposals' function.
class DescribeDirectConnectGatewayAssociationProposalsResult(BaseValidatorModel):
    directConnectGatewayAssociationProposals: List[DirectConnectGatewayAssociationProposal]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'accept_direct_connect_gateway_association_proposal' function.
class AcceptDirectConnectGatewayAssociationProposalResult(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_direct_connect_gateway_association' function.
class CreateDirectConnectGatewayAssociationResult(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_direct_connect_gateway_association' function.
class DeleteDirectConnectGatewayAssociationResult(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_direct_connect_gateway_associations' function.
class DescribeDirectConnectGatewayAssociationsResult(BaseValidatorModel):
    directConnectGatewayAssociations: List[DirectConnectGatewayAssociation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_direct_connect_gateway_association' function.
class UpdateDirectConnectGatewayAssociationResult(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'allocate_transit_virtual_interface' function.
class AllocateTransitVirtualInterfaceResult(BaseValidatorModel):
    virtualInterface: VirtualInterface
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_bgp_peer' function.
class CreateBGPPeerResponse(BaseValidatorModel):
    virtualInterface: VirtualInterface
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transit_virtual_interface' function.
class CreateTransitVirtualInterfaceResult(BaseValidatorModel):
    virtualInterface: VirtualInterface
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_bgp_peer' function.
class DeleteBGPPeerResponse(BaseValidatorModel):
    virtualInterface: VirtualInterface
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_virtual_interfaces' function.
class VirtualInterfaces(BaseValidatorModel):
    virtualInterfaces: List[VirtualInterface]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_lags' function.
class Lags(BaseValidatorModel):
    lags: List[Lag]
    ResponseMetadata: ResponseMetadata