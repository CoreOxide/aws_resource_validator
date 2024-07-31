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
from aws_resource_validator.pydantic_models.directconnect_constants import *

class RouteFilterPrefixTypeDef(BaseModel):
    cidr: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AllocateConnectionOnInterconnectRequestRequestTypeDef(BaseModel):
    bandwidth: str
    connectionName: str
    ownerAccount: str
    interconnectId: str
    vlan: int

class TagTypeDef(BaseModel):
    key: str
    value: Optional[str] = None

class AssociateConnectionWithLagRequestRequestTypeDef(BaseModel):
    connectionId: str
    lagId: str

class AssociateHostedConnectionRequestRequestTypeDef(BaseModel):
    connectionId: str
    parentConnectionId: str

class AssociateMacSecKeyRequestRequestTypeDef(BaseModel):
    connectionId: str
    secretARN: Optional[str] = None
    ckn: Optional[str] = None
    cak: Optional[str] = None

class MacSecKeyTypeDef(BaseModel):
    secretARN: Optional[str] = None
    ckn: Optional[str] = None
    state: Optional[str] = None
    startOn: Optional[str] = None

class AssociateVirtualInterfaceRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str
    connectionId: str

class AssociatedGatewayTypeDef(BaseModel):
    id: Optional[str] = None
    type: Optional[GatewayTypeType] = None
    ownerAccount: Optional[str] = None
    region: Optional[str] = None

class BGPPeerTypeDef(BaseModel):
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

class ConfirmConnectionRequestRequestTypeDef(BaseModel):
    connectionId: str

class ConfirmCustomerAgreementRequestRequestTypeDef(BaseModel):
    agreementName: Optional[str] = None

class ConfirmPrivateVirtualInterfaceRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str
    virtualGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None

class ConfirmPublicVirtualInterfaceRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str

class ConfirmTransitVirtualInterfaceRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str
    directConnectGatewayId: str

class NewBGPPeerTypeDef(BaseModel):
    asn: Optional[int] = None
    authKey: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None

class CreateDirectConnectGatewayRequestRequestTypeDef(BaseModel):
    directConnectGatewayName: str
    amazonSideAsn: Optional[int] = None

class DirectConnectGatewayTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayName: Optional[str] = None
    amazonSideAsn: Optional[int] = None
    ownerAccount: Optional[str] = None
    directConnectGatewayState: Optional[DirectConnectGatewayStateType] = None
    stateChangeError: Optional[str] = None

class CustomerAgreementTypeDef(BaseModel):
    agreementName: Optional[str] = None
    status: Optional[str] = None

class DeleteBGPPeerRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: Optional[str] = None
    asn: Optional[int] = None
    customerAddress: Optional[str] = None
    bgpPeerId: Optional[str] = None

class DeleteConnectionRequestRequestTypeDef(BaseModel):
    connectionId: str

class DeleteDirectConnectGatewayAssociationProposalRequestRequestTypeDef(BaseModel):
    proposalId: str

class DeleteDirectConnectGatewayAssociationRequestRequestTypeDef(BaseModel):
    associationId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    virtualGatewayId: Optional[str] = None

class DeleteDirectConnectGatewayRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: str

class DeleteInterconnectRequestRequestTypeDef(BaseModel):
    interconnectId: str

class DeleteLagRequestRequestTypeDef(BaseModel):
    lagId: str

class DeleteVirtualInterfaceRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str

class DescribeConnectionLoaRequestRequestTypeDef(BaseModel):
    connectionId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal["application/pdf"]] = None

class LoaTypeDef(BaseModel):
    loaContent: Optional[bytes] = None
    loaContentType: Optional[Literal["application/pdf"]] = None

class DescribeConnectionsOnInterconnectRequestRequestTypeDef(BaseModel):
    interconnectId: str

class DescribeConnectionsRequestRequestTypeDef(BaseModel):
    connectionId: Optional[str] = None

class DescribeDirectConnectGatewayAssociationProposalsRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    proposalId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDirectConnectGatewayAssociationsRequestRequestTypeDef(BaseModel):
    associationId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    virtualGatewayId: Optional[str] = None

class DescribeDirectConnectGatewayAttachmentsRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DirectConnectGatewayAttachmentTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    virtualInterfaceRegion: Optional[str] = None
    virtualInterfaceOwnerAccount: Optional[str] = None
    attachmentState: Optional[DirectConnectGatewayAttachmentStateType] = None
    attachmentType: Optional[DirectConnectGatewayAttachmentTypeType] = None
    stateChangeError: Optional[str] = None

class DescribeDirectConnectGatewaysRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeHostedConnectionsRequestRequestTypeDef(BaseModel):
    connectionId: str

class DescribeInterconnectLoaRequestRequestTypeDef(BaseModel):
    interconnectId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal["application/pdf"]] = None

class DescribeInterconnectsRequestRequestTypeDef(BaseModel):
    interconnectId: Optional[str] = None

class DescribeLagsRequestRequestTypeDef(BaseModel):
    lagId: Optional[str] = None

class DescribeLoaRequestRequestTypeDef(BaseModel):
    connectionId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal["application/pdf"]] = None

class DescribeRouterConfigurationRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str
    routerTypeIdentifier: Optional[str] = None

class RouterTypeTypeDef(BaseModel):
    vendor: Optional[str] = None
    platform: Optional[str] = None
    software: Optional[str] = None
    xsltTemplateName: Optional[str] = None
    xsltTemplateNameForMacSec: Optional[str] = None
    routerTypeIdentifier: Optional[str] = None

class DescribeTagsRequestRequestTypeDef(BaseModel):
    resourceArns: Sequence[str]

class DescribeVirtualInterfacesRequestRequestTypeDef(BaseModel):
    connectionId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None

class DisassociateConnectionFromLagRequestRequestTypeDef(BaseModel):
    connectionId: str
    lagId: str

class DisassociateMacSecKeyRequestRequestTypeDef(BaseModel):
    connectionId: str
    secretARN: str

class ListVirtualInterfaceTestHistoryRequestRequestTypeDef(BaseModel):
    testId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    bgpPeers: Optional[Sequence[str]] = None
    status: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class VirtualInterfaceTestHistoryTypeDef(BaseModel):
    testId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    bgpPeers: Optional[List[str]] = None
    status: Optional[str] = None
    ownerAccount: Optional[str] = None
    testDurationInMinutes: Optional[int] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class LocationTypeDef(BaseModel):
    locationCode: Optional[str] = None
    locationName: Optional[str] = None
    region: Optional[str] = None
    availablePortSpeeds: Optional[List[str]] = None
    availableProviders: Optional[List[str]] = None
    availableMacSecPortSpeeds: Optional[List[str]] = None

class StartBgpFailoverTestRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str
    bgpPeers: Optional[Sequence[str]] = None
    testDurationInMinutes: Optional[int] = None

class StopBgpFailoverTestRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateConnectionRequestRequestTypeDef(BaseModel):
    connectionId: str
    connectionName: Optional[str] = None
    encryptionMode: Optional[str] = None

class UpdateDirectConnectGatewayRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: str
    newDirectConnectGatewayName: str

class UpdateLagRequestRequestTypeDef(BaseModel):
    lagId: str
    lagName: Optional[str] = None
    minimumLinks: Optional[int] = None
    encryptionMode: Optional[str] = None

class UpdateVirtualInterfaceAttributesRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: str
    mtu: Optional[int] = None
    enableSiteLink: Optional[bool] = None
    virtualInterfaceName: Optional[str] = None

class VirtualGatewayTypeDef(BaseModel):
    virtualGatewayId: Optional[str] = None
    virtualGatewayState: Optional[str] = None

class AcceptDirectConnectGatewayAssociationProposalRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: str
    proposalId: str
    associatedGatewayOwnerAccount: str
    overrideAllowedPrefixesToDirectConnectGateway: Optional[       Sequence[RouteFilterPrefixTypeDef]     ] = None

class CreateDirectConnectGatewayAssociationProposalRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: str
    directConnectGatewayOwnerAccount: str
    gatewayId: str
    addAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    removeAllowedPrefixesToDirectConnectGateway: Optional[       Sequence[RouteFilterPrefixTypeDef]     ] = None

class CreateDirectConnectGatewayAssociationRequestRequestTypeDef(BaseModel):
    directConnectGatewayId: str
    gatewayId: Optional[str] = None
    addAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    virtualGatewayId: Optional[str] = None

class UpdateDirectConnectGatewayAssociationRequestRequestTypeDef(BaseModel):
    associationId: Optional[str] = None
    addAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    removeAllowedPrefixesToDirectConnectGateway: Optional[       Sequence[RouteFilterPrefixTypeDef]     ] = None

class ConfirmConnectionResponseTypeDef(BaseModel):
    connectionState: ConnectionStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmCustomerAgreementResponseTypeDef(BaseModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmPrivateVirtualInterfaceResponseTypeDef(BaseModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmPublicVirtualInterfaceResponseTypeDef(BaseModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmTransitVirtualInterfaceResponseTypeDef(BaseModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInterconnectResponseTypeDef(BaseModel):
    interconnectState: InterconnectStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVirtualInterfaceResponseTypeDef(BaseModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef

class LoaResponseTypeDef(BaseModel):
    loaContent: bytes
    loaContentType: Literal["application/pdf"]
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateHostedConnectionRequestRequestTypeDef(BaseModel):
    connectionId: str
    ownerAccount: str
    bandwidth: str
    connectionName: str
    vlan: int
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateConnectionRequestRequestTypeDef(BaseModel):
    location: str
    bandwidth: str
    connectionName: str
    lagId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    providerName: Optional[str] = None
    requestMACSec: Optional[bool] = None

class CreateInterconnectRequestRequestTypeDef(BaseModel):
    interconnectName: str
    bandwidth: str
    location: str
    lagId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    providerName: Optional[str] = None

class CreateLagRequestRequestTypeDef(BaseModel):
    numberOfConnections: int
    location: str
    connectionsBandwidth: str
    lagName: str
    connectionId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    childConnectionTags: Optional[Sequence[TagTypeDef]] = None
    providerName: Optional[str] = None
    requestMACSec: Optional[bool] = None

class InterconnectResponseTypeDef(BaseModel):
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
    tags: List[TagTypeDef]
    providerName: str
    ResponseMetadata: ResponseMetadataTypeDef

class InterconnectTypeDef(BaseModel):
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
    tags: Optional[List[TagTypeDef]] = None
    providerName: Optional[str] = None

class NewPrivateVirtualInterfaceAllocationTypeDef(BaseModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    customerAddress: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class NewPrivateVirtualInterfaceTypeDef(BaseModel):
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
    tags: Optional[Sequence[TagTypeDef]] = None
    enableSiteLink: Optional[bool] = None

class NewPublicVirtualInterfaceAllocationTypeDef(BaseModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    routeFilterPrefixes: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class NewPublicVirtualInterfaceTypeDef(BaseModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    routeFilterPrefixes: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class NewTransitVirtualInterfaceAllocationTypeDef(BaseModel):
    virtualInterfaceName: Optional[str] = None
    vlan: Optional[int] = None
    asn: Optional[int] = None
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class NewTransitVirtualInterfaceTypeDef(BaseModel):
    virtualInterfaceName: Optional[str] = None
    vlan: Optional[int] = None
    asn: Optional[int] = None
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    directConnectGatewayId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    enableSiteLink: Optional[bool] = None

class ResourceTagTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class AssociateMacSecKeyResponseTypeDef(BaseModel):
    connectionId: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionResponseTypeDef(BaseModel):
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
    tags: List[TagTypeDef]
    providerName: str
    macSecCapable: bool
    portEncryptionStatus: str
    encryptionMode: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionTypeDef(BaseModel):
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
    tags: Optional[List[TagTypeDef]] = None
    providerName: Optional[str] = None
    macSecCapable: Optional[bool] = None
    portEncryptionStatus: Optional[str] = None
    encryptionMode: Optional[str] = None
    macSecKeys: Optional[List[MacSecKeyTypeDef]] = None

class DisassociateMacSecKeyResponseTypeDef(BaseModel):
    connectionId: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DirectConnectGatewayAssociationProposalTypeDef(BaseModel):
    proposalId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayOwnerAccount: Optional[str] = None
    proposalState: Optional[DirectConnectGatewayAssociationProposalStateType] = None
    associatedGateway: Optional[AssociatedGatewayTypeDef] = None
    existingAllowedPrefixesToDirectConnectGateway: Optional[       List[RouteFilterPrefixTypeDef]     ] = None
    requestedAllowedPrefixesToDirectConnectGateway: Optional[       List[RouteFilterPrefixTypeDef]     ] = None

class DirectConnectGatewayAssociationTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayOwnerAccount: Optional[str] = None
    associationState: Optional[DirectConnectGatewayAssociationStateType] = None
    stateChangeError: Optional[str] = None
    associatedGateway: Optional[AssociatedGatewayTypeDef] = None
    associationId: Optional[str] = None
    allowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefixTypeDef]] = None
    virtualGatewayId: Optional[str] = None
    virtualGatewayRegion: Optional[str] = None
    virtualGatewayOwnerAccount: Optional[str] = None

class VirtualInterfaceResponseTypeDef(BaseModel):
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
    routeFilterPrefixes: List[RouteFilterPrefixTypeDef]
    bgpPeers: List[BGPPeerTypeDef]
    region: str
    awsDeviceV2: str
    awsLogicalDeviceId: str
    tags: List[TagTypeDef]
    siteLinkEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualInterfaceTypeDef(BaseModel):
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
    routeFilterPrefixes: Optional[List[RouteFilterPrefixTypeDef]] = None
    bgpPeers: Optional[List[BGPPeerTypeDef]] = None
    region: Optional[str] = None
    awsDeviceV2: Optional[str] = None
    awsLogicalDeviceId: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None
    siteLinkEnabled: Optional[bool] = None

class CreateBGPPeerRequestRequestTypeDef(BaseModel):
    virtualInterfaceId: Optional[str] = None
    newBGPPeer: Optional[NewBGPPeerTypeDef] = None

class CreateDirectConnectGatewayResultTypeDef(BaseModel):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectConnectGatewayResultTypeDef(BaseModel):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewaysResultTypeDef(BaseModel):
    directConnectGateways: List[DirectConnectGatewayTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDirectConnectGatewayResponseTypeDef(BaseModel):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomerMetadataResponseTypeDef(BaseModel):
    agreements: List[CustomerAgreementTypeDef]
    nniPartnerType: NniPartnerTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectionLoaResponseTypeDef(BaseModel):
    loa: LoaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInterconnectLoaResponseTypeDef(BaseModel):
    loa: LoaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewayAssociationsRequestDescribeDirectConnectGatewayAssociationsPaginateTypeDef(BaseModel):
    associationId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    virtualGatewayId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDirectConnectGatewayAttachmentsRequestDescribeDirectConnectGatewayAttachmentsPaginateTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDirectConnectGatewaysRequestDescribeDirectConnectGatewaysPaginateTypeDef(BaseModel):
    directConnectGatewayId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDirectConnectGatewayAttachmentsResultTypeDef(BaseModel):
    directConnectGatewayAttachments: List[DirectConnectGatewayAttachmentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRouterConfigurationResponseTypeDef(BaseModel):
    customerRouterConfig: str
    router: RouterTypeTypeDef
    virtualInterfaceId: str
    virtualInterfaceName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVirtualInterfaceTestHistoryResponseTypeDef(BaseModel):
    virtualInterfaceTestHistory: List[VirtualInterfaceTestHistoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartBgpFailoverTestResponseTypeDef(BaseModel):
    virtualInterfaceTest: VirtualInterfaceTestHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopBgpFailoverTestResponseTypeDef(BaseModel):
    virtualInterfaceTest: VirtualInterfaceTestHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LocationsTypeDef(BaseModel):
    locations: List[LocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualGatewaysTypeDef(BaseModel):
    virtualGateways: List[VirtualGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InterconnectsTypeDef(BaseModel):
    interconnects: List[InterconnectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AllocatePrivateVirtualInterfaceRequestRequestTypeDef(BaseModel):
    connectionId: str
    ownerAccount: str
    newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocationTypeDef

class CreatePrivateVirtualInterfaceRequestRequestTypeDef(BaseModel):
    connectionId: str
    newPrivateVirtualInterface: NewPrivateVirtualInterfaceTypeDef

class AllocatePublicVirtualInterfaceRequestRequestTypeDef(BaseModel):
    connectionId: str
    ownerAccount: str
    newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocationTypeDef

class CreatePublicVirtualInterfaceRequestRequestTypeDef(BaseModel):
    connectionId: str
    newPublicVirtualInterface: NewPublicVirtualInterfaceTypeDef

class AllocateTransitVirtualInterfaceRequestRequestTypeDef(BaseModel):
    connectionId: str
    ownerAccount: str
    newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocationTypeDef

class CreateTransitVirtualInterfaceRequestRequestTypeDef(BaseModel):
    connectionId: str
    newTransitVirtualInterface: NewTransitVirtualInterfaceTypeDef

class DescribeTagsResponseTypeDef(BaseModel):
    resourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectionsTypeDef(BaseModel):
    connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LagResponseTypeDef(BaseModel):
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
    connections: List[ConnectionTypeDef]
    allowsHostedConnections: bool
    jumboFrameCapable: bool
    hasLogicalRedundancy: HasLogicalRedundancyType
    tags: List[TagTypeDef]
    providerName: str
    macSecCapable: bool
    encryptionMode: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LagTypeDef(BaseModel):
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
    connections: Optional[List[ConnectionTypeDef]] = None
    allowsHostedConnections: Optional[bool] = None
    jumboFrameCapable: Optional[bool] = None
    hasLogicalRedundancy: Optional[HasLogicalRedundancyType] = None
    tags: Optional[List[TagTypeDef]] = None
    providerName: Optional[str] = None
    macSecCapable: Optional[bool] = None
    encryptionMode: Optional[str] = None
    macSecKeys: Optional[List[MacSecKeyTypeDef]] = None

class CreateDirectConnectGatewayAssociationProposalResultTypeDef(BaseModel):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectConnectGatewayAssociationProposalResultTypeDef(BaseModel):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewayAssociationProposalsResultTypeDef(BaseModel):
    directConnectGatewayAssociationProposals: List[       DirectConnectGatewayAssociationProposalTypeDef     ]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptDirectConnectGatewayAssociationProposalResultTypeDef(BaseModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectConnectGatewayAssociationResultTypeDef(BaseModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectConnectGatewayAssociationResultTypeDef(BaseModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDirectConnectGatewayAssociationsResultTypeDef(BaseModel):
    directConnectGatewayAssociations: List[DirectConnectGatewayAssociationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDirectConnectGatewayAssociationResultTypeDef(BaseModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateTransitVirtualInterfaceResultTypeDef(BaseModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBGPPeerResponseTypeDef(BaseModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitVirtualInterfaceResultTypeDef(BaseModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBGPPeerResponseTypeDef(BaseModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VirtualInterfacesTypeDef(BaseModel):
    virtualInterfaces: List[VirtualInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LagsTypeDef(BaseModel):
    lags: List[LagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

