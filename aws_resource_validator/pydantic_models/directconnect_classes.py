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
from aws_resource_validator.pydantic_models.directconnect_constants import *

class RouteFilterPrefixTypeDef(BaseValidatorModel):
    cidr: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AllocateConnectionOnInterconnectRequestTypeDef(BaseValidatorModel):
    bandwidth: str
    connectionName: str
    ownerAccount: str
    interconnectId: str
    vlan: int


class TagTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class AssociateConnectionWithLagRequestTypeDef(BaseValidatorModel):
    connectionId: str
    lagId: str


class AssociateHostedConnectionRequestTypeDef(BaseValidatorModel):
    connectionId: str
    parentConnectionId: str


class AssociateMacSecKeyRequestTypeDef(BaseValidatorModel):
    connectionId: str
    secretARN: Optional[str] = None
    ckn: Optional[str] = None
    cak: Optional[str] = None


class MacSecKeyTypeDef(BaseValidatorModel):
    secretARN: Optional[str] = None
    ckn: Optional[str] = None
    state: Optional[str] = None
    startOn: Optional[str] = None


class AssociateVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str
    connectionId: str


class BGPPeerTypeDef(BaseValidatorModel):
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


class ConfirmConnectionRequestTypeDef(BaseValidatorModel):
    connectionId: str


class ConfirmCustomerAgreementRequestTypeDef(BaseValidatorModel):
    agreementName: Optional[str] = None


class ConfirmPrivateVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str
    virtualGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None


class ConfirmPublicVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str


class ConfirmTransitVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str
    directConnectGatewayId: str


class NewBGPPeerTypeDef(BaseValidatorModel):
    asn: Optional[int] = None
    authKey: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None


class CreateDirectConnectGatewayRequestTypeDef(BaseValidatorModel):
    directConnectGatewayName: str
    amazonSideAsn: Optional[int] = None


class DirectConnectGatewayTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayName: Optional[str] = None
    amazonSideAsn: Optional[int] = None
    ownerAccount: Optional[str] = None
    directConnectGatewayState: Optional[DirectConnectGatewayStateType] = None
    stateChangeError: Optional[str] = None


class CustomerAgreementTypeDef(BaseValidatorModel):
    agreementName: Optional[str] = None
    status: Optional[str] = None


class DeleteBGPPeerRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: Optional[str] = None
    asn: Optional[int] = None
    customerAddress: Optional[str] = None
    bgpPeerId: Optional[str] = None


class DeleteConnectionRequestTypeDef(BaseValidatorModel):
    connectionId: str


class DeleteDirectConnectGatewayAssociationProposalRequestTypeDef(BaseValidatorModel):
    proposalId: str


class DeleteDirectConnectGatewayAssociationRequestTypeDef(BaseValidatorModel):
    associationId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    virtualGatewayId: Optional[str] = None


class DeleteDirectConnectGatewayRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: str


class DeleteInterconnectRequestTypeDef(BaseValidatorModel):
    interconnectId: str


class DeleteLagRequestTypeDef(BaseValidatorModel):
    lagId: str


class DeleteVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str


class DescribeConnectionLoaRequestTypeDef(BaseValidatorModel):
    connectionId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal["application/pdf"]] = None


class LoaTypeDef(BaseValidatorModel):
    loaContent: Optional[bytes] = None
    loaContentType: Optional[Literal["application/pdf"]] = None


class DescribeConnectionsOnInterconnectRequestTypeDef(BaseValidatorModel):
    interconnectId: str


class DescribeConnectionsRequestTypeDef(BaseValidatorModel):
    connectionId: Optional[str] = None


class DescribeDirectConnectGatewayAssociationProposalsRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    proposalId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeDirectConnectGatewayAssociationsRequestTypeDef(BaseValidatorModel):
    associationId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    virtualGatewayId: Optional[str] = None


class DescribeDirectConnectGatewayAttachmentsRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DirectConnectGatewayAttachmentTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    virtualInterfaceRegion: Optional[str] = None
    virtualInterfaceOwnerAccount: Optional[str] = None
    attachmentState: Optional[DirectConnectGatewayAttachmentStateType] = None
    attachmentType: Optional[DirectConnectGatewayAttachmentTypeType] = None
    stateChangeError: Optional[str] = None


class DescribeDirectConnectGatewaysRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeHostedConnectionsRequestTypeDef(BaseValidatorModel):
    connectionId: str


class DescribeInterconnectLoaRequestTypeDef(BaseValidatorModel):
    interconnectId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal["application/pdf"]] = None


class DescribeInterconnectsRequestTypeDef(BaseValidatorModel):
    interconnectId: Optional[str] = None


class DescribeLagsRequestTypeDef(BaseValidatorModel):
    lagId: Optional[str] = None


class DescribeLoaRequestTypeDef(BaseValidatorModel):
    connectionId: str
    providerName: Optional[str] = None
    loaContentType: Optional[Literal["application/pdf"]] = None


class DescribeRouterConfigurationRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str
    routerTypeIdentifier: Optional[str] = None


class RouterTypeTypeDef(BaseValidatorModel):
    vendor: Optional[str] = None
    platform: Optional[str] = None
    software: Optional[str] = None
    xsltTemplateName: Optional[str] = None
    xsltTemplateNameForMacSec: Optional[str] = None
    routerTypeIdentifier: Optional[str] = None


class DescribeTagsRequestTypeDef(BaseValidatorModel):
    resourceArns: Sequence[str]


class DescribeVirtualInterfacesRequestTypeDef(BaseValidatorModel):
    connectionId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None


class DisassociateConnectionFromLagRequestTypeDef(BaseValidatorModel):
    connectionId: str
    lagId: str


class DisassociateMacSecKeyRequestTypeDef(BaseValidatorModel):
    connectionId: str
    secretARN: str


class ListVirtualInterfaceTestHistoryRequestTypeDef(BaseValidatorModel):
    testId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    bgpPeers: Optional[Sequence[str]] = None
    status: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class VirtualInterfaceTestHistoryTypeDef(BaseValidatorModel):
    testId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    bgpPeers: Optional[List[str]] = None
    status: Optional[str] = None
    ownerAccount: Optional[str] = None
    testDurationInMinutes: Optional[int] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class LocationTypeDef(BaseValidatorModel):
    locationCode: Optional[str] = None
    locationName: Optional[str] = None
    region: Optional[str] = None
    availablePortSpeeds: Optional[List[str]] = None
    availableProviders: Optional[List[str]] = None
    availableMacSecPortSpeeds: Optional[List[str]] = None


class StartBgpFailoverTestRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str
    bgpPeers: Optional[Sequence[str]] = None
    testDurationInMinutes: Optional[int] = None


class StopBgpFailoverTestRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateConnectionRequestTypeDef(BaseValidatorModel):
    connectionId: str
    connectionName: Optional[str] = None
    encryptionMode: Optional[str] = None


class UpdateDirectConnectGatewayRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: str
    newDirectConnectGatewayName: str


class UpdateLagRequestTypeDef(BaseValidatorModel):
    lagId: str
    lagName: Optional[str] = None
    minimumLinks: Optional[int] = None
    encryptionMode: Optional[str] = None


class UpdateVirtualInterfaceAttributesRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: str
    mtu: Optional[int] = None
    enableSiteLink: Optional[bool] = None
    virtualInterfaceName: Optional[str] = None


class VirtualGatewayTypeDef(BaseValidatorModel):
    virtualGatewayId: Optional[str] = None
    virtualGatewayState: Optional[str] = None


class AcceptDirectConnectGatewayAssociationProposalRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: str
    proposalId: str
    associatedGatewayOwnerAccount: str
    overrideAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None


class CreateDirectConnectGatewayAssociationProposalRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: str
    directConnectGatewayOwnerAccount: str
    gatewayId: str
    addAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    removeAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None


class CreateDirectConnectGatewayAssociationRequestTypeDef(BaseValidatorModel):
    directConnectGatewayId: str
    gatewayId: Optional[str] = None
    addAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    virtualGatewayId: Optional[str] = None


class UpdateDirectConnectGatewayAssociationRequestTypeDef(BaseValidatorModel):
    associationId: Optional[str] = None
    addAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    removeAllowedPrefixesToDirectConnectGateway: Optional[Sequence[RouteFilterPrefixTypeDef]] = None


class ConfirmConnectionResponseTypeDef(BaseValidatorModel):
    connectionState: ConnectionStateType
    ResponseMetadata: ResponseMetadataTypeDef


class ConfirmCustomerAgreementResponseTypeDef(BaseValidatorModel):
    status: str
    ResponseMetadata: ResponseMetadataTypeDef


class ConfirmPrivateVirtualInterfaceResponseTypeDef(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef


class ConfirmPublicVirtualInterfaceResponseTypeDef(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef


class ConfirmTransitVirtualInterfaceResponseTypeDef(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInterconnectResponseTypeDef(BaseValidatorModel):
    interconnectState: InterconnectStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteVirtualInterfaceResponseTypeDef(BaseValidatorModel):
    virtualInterfaceState: VirtualInterfaceStateType
    ResponseMetadata: ResponseMetadataTypeDef


class LoaResponseTypeDef(BaseValidatorModel):
    loaContent: bytes
    loaContentType: Literal["application/pdf"]
    ResponseMetadata: ResponseMetadataTypeDef


class AllocateHostedConnectionRequestTypeDef(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    bandwidth: str
    connectionName: str
    vlan: int
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateConnectionRequestTypeDef(BaseValidatorModel):
    location: str
    bandwidth: str
    connectionName: str
    lagId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    providerName: Optional[str] = None
    requestMACSec: Optional[bool] = None


class CreateInterconnectRequestTypeDef(BaseValidatorModel):
    interconnectName: str
    bandwidth: str
    location: str
    lagId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    providerName: Optional[str] = None


class CreateLagRequestTypeDef(BaseValidatorModel):
    numberOfConnections: int
    location: str
    connectionsBandwidth: str
    lagName: str
    connectionId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    childConnectionTags: Optional[Sequence[TagTypeDef]] = None
    providerName: Optional[str] = None
    requestMACSec: Optional[bool] = None


class InterconnectResponseTypeDef(BaseValidatorModel):
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


class InterconnectTypeDef(BaseValidatorModel):
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


class NewPrivateVirtualInterfaceAllocationTypeDef(BaseValidatorModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    customerAddress: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class NewPrivateVirtualInterfaceTypeDef(BaseValidatorModel):
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


class NewPublicVirtualInterfaceAllocationTypeDef(BaseValidatorModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    routeFilterPrefixes: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class NewPublicVirtualInterfaceTypeDef(BaseValidatorModel):
    virtualInterfaceName: str
    vlan: int
    asn: int
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    routeFilterPrefixes: Optional[Sequence[RouteFilterPrefixTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class NewTransitVirtualInterfaceAllocationTypeDef(BaseValidatorModel):
    virtualInterfaceName: Optional[str] = None
    vlan: Optional[int] = None
    asn: Optional[int] = None
    mtu: Optional[int] = None
    authKey: Optional[str] = None
    amazonAddress: Optional[str] = None
    customerAddress: Optional[str] = None
    addressFamily: Optional[AddressFamilyType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class NewTransitVirtualInterfaceTypeDef(BaseValidatorModel):
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


class ResourceTagTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class AssociateMacSecKeyResponseTypeDef(BaseValidatorModel):
    connectionId: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ConnectionResponseTypeDef(BaseValidatorModel):
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


class ConnectionTypeDef(BaseValidatorModel):
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


class DisassociateMacSecKeyResponseTypeDef(BaseValidatorModel):
    connectionId: str
    macSecKeys: List[MacSecKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AssociatedGatewayTypeDef(BaseValidatorModel):
    pass


class DirectConnectGatewayAssociationProposalTypeDef(BaseValidatorModel):
    proposalId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayOwnerAccount: Optional[str] = None
    proposalState: Optional[DirectConnectGatewayAssociationProposalStateType] = None
    associatedGateway: Optional[AssociatedGatewayTypeDef] = None
    existingAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefixTypeDef]] = None
    requestedAllowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefixTypeDef]] = None


class AssociatedCoreNetworkTypeDef(BaseValidatorModel):
    pass


class DirectConnectGatewayAssociationTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    directConnectGatewayOwnerAccount: Optional[str] = None
    associationState: Optional[DirectConnectGatewayAssociationStateType] = None
    stateChangeError: Optional[str] = None
    associatedGateway: Optional[AssociatedGatewayTypeDef] = None
    associationId: Optional[str] = None
    allowedPrefixesToDirectConnectGateway: Optional[List[RouteFilterPrefixTypeDef]] = None
    associatedCoreNetwork: Optional[AssociatedCoreNetworkTypeDef] = None
    virtualGatewayId: Optional[str] = None
    virtualGatewayRegion: Optional[str] = None
    virtualGatewayOwnerAccount: Optional[str] = None


class VirtualInterfaceResponseTypeDef(BaseValidatorModel):
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


class VirtualInterfaceTypeDef(BaseValidatorModel):
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


class CreateBGPPeerRequestTypeDef(BaseValidatorModel):
    virtualInterfaceId: Optional[str] = None
    newBGPPeer: Optional[NewBGPPeerTypeDef] = None


class CreateDirectConnectGatewayResultTypeDef(BaseValidatorModel):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDirectConnectGatewayResultTypeDef(BaseValidatorModel):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDirectConnectGatewaysResultTypeDef(BaseValidatorModel):
    directConnectGateways: List[DirectConnectGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDirectConnectGatewayResponseTypeDef(BaseValidatorModel):
    directConnectGateway: DirectConnectGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCustomerMetadataResponseTypeDef(BaseValidatorModel):
    agreements: List[CustomerAgreementTypeDef]
    nniPartnerType: NniPartnerTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConnectionLoaResponseTypeDef(BaseValidatorModel):
    loa: LoaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeInterconnectLoaResponseTypeDef(BaseValidatorModel):
    loa: LoaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDirectConnectGatewayAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    associationId: Optional[str] = None
    associatedGatewayId: Optional[str] = None
    directConnectGatewayId: Optional[str] = None
    virtualGatewayId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDirectConnectGatewayAttachmentsRequestPaginateTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    virtualInterfaceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDirectConnectGatewaysRequestPaginateTypeDef(BaseValidatorModel):
    directConnectGatewayId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDirectConnectGatewayAttachmentsResultTypeDef(BaseValidatorModel):
    directConnectGatewayAttachments: List[DirectConnectGatewayAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeRouterConfigurationResponseTypeDef(BaseValidatorModel):
    customerRouterConfig: str
    router: RouterTypeTypeDef
    virtualInterfaceId: str
    virtualInterfaceName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListVirtualInterfaceTestHistoryResponseTypeDef(BaseValidatorModel):
    virtualInterfaceTestHistory: List[VirtualInterfaceTestHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartBgpFailoverTestResponseTypeDef(BaseValidatorModel):
    virtualInterfaceTest: VirtualInterfaceTestHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopBgpFailoverTestResponseTypeDef(BaseValidatorModel):
    virtualInterfaceTest: VirtualInterfaceTestHistoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class LocationsTypeDef(BaseValidatorModel):
    locations: List[LocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class VirtualGatewaysTypeDef(BaseValidatorModel):
    virtualGateways: List[VirtualGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class InterconnectsTypeDef(BaseValidatorModel):
    interconnects: List[InterconnectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AllocatePrivateVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    newPrivateVirtualInterfaceAllocation: NewPrivateVirtualInterfaceAllocationTypeDef


class CreatePrivateVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    connectionId: str
    newPrivateVirtualInterface: NewPrivateVirtualInterfaceTypeDef


class AllocatePublicVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    newPublicVirtualInterfaceAllocation: NewPublicVirtualInterfaceAllocationTypeDef


class CreatePublicVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    connectionId: str
    newPublicVirtualInterface: NewPublicVirtualInterfaceTypeDef


class AllocateTransitVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    connectionId: str
    ownerAccount: str
    newTransitVirtualInterfaceAllocation: NewTransitVirtualInterfaceAllocationTypeDef


class CreateTransitVirtualInterfaceRequestTypeDef(BaseValidatorModel):
    connectionId: str
    newTransitVirtualInterface: NewTransitVirtualInterfaceTypeDef


class DescribeTagsResponseTypeDef(BaseValidatorModel):
    resourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ConnectionsTypeDef(BaseValidatorModel):
    connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LagResponseTypeDef(BaseValidatorModel):
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


class LagTypeDef(BaseValidatorModel):
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


class CreateDirectConnectGatewayAssociationProposalResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDirectConnectGatewayAssociationProposalResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociationProposal: DirectConnectGatewayAssociationProposalTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDirectConnectGatewayAssociationProposalsResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociationProposals: List[DirectConnectGatewayAssociationProposalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AcceptDirectConnectGatewayAssociationProposalResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDirectConnectGatewayAssociationResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDirectConnectGatewayAssociationResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDirectConnectGatewayAssociationsResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociations: List[DirectConnectGatewayAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateDirectConnectGatewayAssociationResultTypeDef(BaseValidatorModel):
    directConnectGatewayAssociation: DirectConnectGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AllocateTransitVirtualInterfaceResultTypeDef(BaseValidatorModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBGPPeerResponseTypeDef(BaseValidatorModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTransitVirtualInterfaceResultTypeDef(BaseValidatorModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBGPPeerResponseTypeDef(BaseValidatorModel):
    virtualInterface: VirtualInterfaceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class VirtualInterfacesTypeDef(BaseValidatorModel):
    virtualInterfaces: List[VirtualInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LagsTypeDef(BaseValidatorModel):
    lags: List[LagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


