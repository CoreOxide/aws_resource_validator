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
from aws_resource_validator.pydantic_models.networkmanager_constants import *

class AWSLocationTypeDef(BaseModel):
    Zone: Optional[str] = None
    SubnetArn: Optional[str] = None

class AcceptAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AccountStatusTypeDef(BaseModel):
    AccountId: Optional[str] = None
    SLRDeploymentStatus: Optional[str] = None

class AssociateConnectPeerRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectPeerId: str
    DeviceId: str
    LinkId: Optional[str] = None

class ConnectPeerAssociationTypeDef(BaseModel):
    ConnectPeerId: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[ConnectPeerAssociationStateType] = None

class AssociateCustomerGatewayRequestRequestTypeDef(BaseModel):
    CustomerGatewayArn: str
    GlobalNetworkId: str
    DeviceId: str
    LinkId: Optional[str] = None

class CustomerGatewayAssociationTypeDef(BaseModel):
    CustomerGatewayArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[CustomerGatewayAssociationStateType] = None

class AssociateLinkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str

class LinkAssociationTypeDef(BaseModel):
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    LinkAssociationState: Optional[LinkAssociationStateType] = None

class AssociateTransitGatewayConnectPeerRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str
    DeviceId: str
    LinkId: Optional[str] = None

class TransitGatewayConnectPeerAssociationTypeDef(BaseModel):
    TransitGatewayConnectPeerArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[TransitGatewayConnectPeerAssociationStateType] = None

class AttachmentErrorTypeDef(BaseModel):
    Code: Optional[AttachmentErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class BandwidthTypeDef(BaseModel):
    UploadSpeed: Optional[int] = None
    DownloadSpeed: Optional[int] = None

class BgpOptionsTypeDef(BaseModel):
    PeerAsn: Optional[int] = None

class ConnectAttachmentOptionsTypeDef(BaseModel):
    Protocol: Optional[TunnelProtocolType] = None

class ConnectPeerBgpConfigurationTypeDef(BaseModel):
    CoreNetworkAsn: Optional[int] = None
    PeerAsn: Optional[int] = None
    CoreNetworkAddress: Optional[str] = None
    PeerAddress: Optional[str] = None

class ConnectPeerErrorTypeDef(BaseModel):
    Code: Optional[ConnectPeerErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None

class ConnectionHealthTypeDef(BaseModel):
    Type: Optional[ConnectionTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    Timestamp: Optional[datetime] = None

class CoreNetworkChangeEventValuesTypeDef(BaseModel):
    EdgeLocation: Optional[str] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    AttachmentId: Optional[str] = None
    Cidr: Optional[str] = None

class CoreNetworkEdgeTypeDef(BaseModel):
    EdgeLocation: Optional[str] = None
    Asn: Optional[int] = None
    InsideCidrBlocks: Optional[List[str]] = None

class CoreNetworkNetworkFunctionGroupIdentifierTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocation: Optional[str] = None

class ServiceInsertionSegmentsTypeDef(BaseModel):
    SendVia: Optional[List[str]] = None
    SendTo: Optional[List[str]] = None

class CoreNetworkPolicyErrorTypeDef(BaseModel):
    ErrorCode: str
    Message: str
    Path: Optional[str] = None

class CoreNetworkPolicyVersionTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ChangeSetState: Optional[ChangeSetStateType] = None

class CoreNetworkSegmentEdgeIdentifierTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    SegmentName: Optional[str] = None
    EdgeLocation: Optional[str] = None

class CoreNetworkSegmentTypeDef(BaseModel):
    Name: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    SharedSegments: Optional[List[str]] = None

class LocationTypeDef(BaseModel):
    Address: Optional[str] = None
    Latitude: Optional[str] = None
    Longitude: Optional[str] = None

class VpcOptionsTypeDef(BaseModel):
    Ipv6Support: Optional[bool] = None
    ApplianceModeSupport: Optional[bool] = None

class DeleteAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str

class DeleteConnectPeerRequestRequestTypeDef(BaseModel):
    ConnectPeerId: str

class DeleteConnectionRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectionId: str

class DeleteCoreNetworkPolicyVersionRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: int

class DeleteCoreNetworkRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str

class DeleteDeviceRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceId: str

class DeleteGlobalNetworkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str

class DeleteLinkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    LinkId: str

class DeletePeeringRequestRequestTypeDef(BaseModel):
    PeeringId: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteSiteRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    SiteId: str

class DeregisterTransitGatewayRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeGlobalNetworksRequestRequestTypeDef(BaseModel):
    GlobalNetworkIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DisassociateConnectPeerRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectPeerId: str

class DisassociateCustomerGatewayRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    CustomerGatewayArn: str

class DisassociateLinkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str

class DisassociateTransitGatewayConnectPeerRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str

class EdgeOverrideTypeDef(BaseModel):
    EdgeSets: Optional[List[List[str]]] = None
    UseEdge: Optional[str] = None

class ExecuteCoreNetworkChangeSetRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: int

class GetConnectAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str

class GetConnectPeerAssociationsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectPeerIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetConnectPeerRequestRequestTypeDef(BaseModel):
    ConnectPeerId: str

class GetConnectionsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectionIds: Optional[Sequence[str]] = None
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCoreNetworkChangeEventsRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCoreNetworkChangeSetRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCoreNetworkPolicyRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None

class GetCoreNetworkRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str

class GetCustomerGatewayAssociationsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    CustomerGatewayArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetDevicesRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetLinkAssociationsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetLinksRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    LinkIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetNetworkResourceCountsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ResourceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NetworkResourceCountTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    Count: Optional[int] = None

class GetNetworkResourceRelationshipsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RelationshipTypeDef(BaseModel):
    From: Optional[str] = None
    To: Optional[str] = None

class GetNetworkResourcesRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetNetworkTelemetryRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetRouteAnalysisRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    RouteAnalysisId: str

class GetSiteToSiteVpnAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str

class GetSitesRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    SiteIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetTransitGatewayPeeringRequestRequestTypeDef(BaseModel):
    PeeringId: str

class GetTransitGatewayRegistrationsRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetTransitGatewayRouteTableAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str

class GetVpcAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str

class ListAttachmentsRequestRequestTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    EdgeLocation: Optional[str] = None
    State: Optional[AttachmentStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConnectPeersRequestRequestTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCoreNetworkPolicyVersionsRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCoreNetworksRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOrganizationServiceAccessStatusRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPeeringsRequestRequestTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    PeeringType: Optional[Literal["TRANSIT_GATEWAY"]] = None
    EdgeLocation: Optional[str] = None
    State: Optional[PeeringStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class NetworkFunctionGroupTypeDef(BaseModel):
    Name: Optional[str] = None

class NetworkResourceSummaryTypeDef(BaseModel):
    RegisteredGatewayArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    Definition: Optional[str] = None
    NameTag: Optional[str] = None
    IsMiddlebox: Optional[bool] = None

class NetworkRouteDestinationTypeDef(BaseModel):
    CoreNetworkAttachmentId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocation: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None

class PermissionsErrorContextTypeDef(BaseModel):
    MissingPermission: Optional[str] = None

class PutCoreNetworkPolicyRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyDocument: str
    Description: Optional[str] = None
    LatestVersionId: Optional[int] = None
    ClientToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    PolicyDocument: str
    ResourceArn: str

class RegisterTransitGatewayRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayArn: str

class RejectAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str

class RestoreCoreNetworkPolicyVersionRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: int

class RouteAnalysisCompletionTypeDef(BaseModel):
    ResultCode: Optional[RouteAnalysisCompletionResultCodeType] = None
    ReasonCode: Optional[RouteAnalysisCompletionReasonCodeType] = None
    ReasonContext: Optional[Dict[str, str]] = None

class RouteAnalysisEndpointOptionsSpecificationTypeDef(BaseModel):
    TransitGatewayAttachmentArn: Optional[str] = None
    IpAddress: Optional[str] = None

class RouteAnalysisEndpointOptionsTypeDef(BaseModel):
    TransitGatewayAttachmentArn: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    IpAddress: Optional[str] = None

class WhenSentToTypeDef(BaseModel):
    WhenSentToSegmentsList: Optional[List[str]] = None

class StartOrganizationServiceAccessUpdateRequestRequestTypeDef(BaseModel):
    Action: str

class TransitGatewayRegistrationStateReasonTypeDef(BaseModel):
    Code: Optional[TransitGatewayRegistrationStateType] = None
    Message: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConnectionRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectionId: str
    LinkId: Optional[str] = None
    ConnectedLinkId: Optional[str] = None
    Description: Optional[str] = None

class UpdateCoreNetworkRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    Description: Optional[str] = None

class UpdateGlobalNetworkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    Description: Optional[str] = None

class UpdateNetworkResourceMetadataRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    ResourceArn: str
    Metadata: Mapping[str, str]

class GetResourcePolicyResponseTypeDef(BaseModel):
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkResourceMetadataResponseTypeDef(BaseModel):
    ResourceArn: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class OrganizationStatusTypeDef(BaseModel):
    OrganizationId: Optional[str] = None
    OrganizationAwsServiceAccessStatus: Optional[str] = None
    SLRDeploymentStatus: Optional[str] = None
    AccountStatusList: Optional[List[AccountStatusTypeDef]] = None

class AssociateConnectPeerResponseTypeDef(BaseModel):
    ConnectPeerAssociation: ConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateConnectPeerResponseTypeDef(BaseModel):
    ConnectPeerAssociation: ConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectPeerAssociationsResponseTypeDef(BaseModel):
    ConnectPeerAssociations: List[ConnectPeerAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateCustomerGatewayResponseTypeDef(BaseModel):
    CustomerGatewayAssociation: CustomerGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateCustomerGatewayResponseTypeDef(BaseModel):
    CustomerGatewayAssociation: CustomerGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomerGatewayAssociationsResponseTypeDef(BaseModel):
    CustomerGatewayAssociations: List[CustomerGatewayAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateLinkResponseTypeDef(BaseModel):
    LinkAssociation: LinkAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateLinkResponseTypeDef(BaseModel):
    LinkAssociation: LinkAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinkAssociationsResponseTypeDef(BaseModel):
    LinkAssociations: List[LinkAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateTransitGatewayConnectPeerResponseTypeDef(BaseModel):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayConnectPeerResponseTypeDef(BaseModel):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayConnectPeerAssociationsResponseTypeDef(BaseModel):
    TransitGatewayConnectPeerAssociations: List[TransitGatewayConnectPeerAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ConnectPeerSummaryTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    ConnectPeerId: Optional[str] = None
    EdgeLocation: Optional[str] = None
    ConnectPeerState: Optional[ConnectPeerStateType] = None
    CreatedAt: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    SubnetArn: Optional[str] = None

class ConnectionTypeDef(BaseModel):
    ConnectionId: Optional[str] = None
    ConnectionArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    ConnectedDeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    ConnectedLinkId: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[ConnectionStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class CoreNetworkSummaryTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    State: Optional[CoreNetworkStateType] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateConnectionRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceId: str
    ConnectedDeviceId: str
    LinkId: Optional[str] = None
    ConnectedLinkId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateCoreNetworkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None

class CreateGlobalNetworkRequestRequestTypeDef(BaseModel):
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSiteToSiteVpnAttachmentRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    VpnConnectionArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateTransitGatewayPeeringRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    TransitGatewayArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateTransitGatewayRouteTableAttachmentRequestRequestTypeDef(BaseModel):
    PeeringId: str
    TransitGatewayRouteTableArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class GlobalNetworkTypeDef(BaseModel):
    GlobalNetworkId: Optional[str] = None
    GlobalNetworkArn: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[GlobalNetworkStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkResourceTypeDef(BaseModel):
    RegisteredGatewayArn: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceArn: Optional[str] = None
    Definition: Optional[str] = None
    DefinitionTimestamp: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    Metadata: Optional[Dict[str, str]] = None

class ProposedNetworkFunctionGroupChangeTypeDef(BaseModel):
    Tags: Optional[List[TagTypeDef]] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    NetworkFunctionGroupName: Optional[str] = None

class ProposedSegmentChangeTypeDef(BaseModel):
    Tags: Optional[List[TagTypeDef]] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    SegmentName: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateLinkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    Bandwidth: BandwidthTypeDef
    SiteId: str
    Description: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class LinkTypeDef(BaseModel):
    LinkId: Optional[str] = None
    LinkArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    SiteId: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Bandwidth: Optional[BandwidthTypeDef] = None
    Provider: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[LinkStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class UpdateLinkRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    LinkId: str
    Description: Optional[str] = None
    Type: Optional[str] = None
    Bandwidth: Optional[BandwidthTypeDef] = None
    Provider: Optional[str] = None

class CreateConnectPeerRequestRequestTypeDef(BaseModel):
    ConnectAttachmentId: str
    PeerAddress: str
    CoreNetworkAddress: Optional[str] = None
    BgpOptions: Optional[BgpOptionsTypeDef] = None
    InsideCidrBlocks: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None
    SubnetArn: Optional[str] = None

class CreateConnectAttachmentRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    EdgeLocation: str
    TransportAttachmentId: str
    Options: ConnectAttachmentOptionsTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class ConnectPeerConfigurationTypeDef(BaseModel):
    CoreNetworkAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    Protocol: Optional[TunnelProtocolType] = None
    BgpConfigurations: Optional[List[ConnectPeerBgpConfigurationTypeDef]] = None

class NetworkTelemetryTypeDef(BaseModel):
    RegisteredGatewayArn: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceArn: Optional[str] = None
    Address: Optional[str] = None
    Health: Optional[ConnectionHealthTypeDef] = None

class CoreNetworkChangeEventTypeDef(BaseModel):
    Type: Optional[ChangeTypeType] = None
    Action: Optional[ChangeActionType] = None
    IdentifierPath: Optional[str] = None
    EventTime: Optional[datetime] = None
    Status: Optional[ChangeStatusType] = None
    Values: Optional[CoreNetworkChangeEventValuesTypeDef] = None

class CoreNetworkNetworkFunctionGroupTypeDef(BaseModel):
    Name: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    Segments: Optional[ServiceInsertionSegmentsTypeDef] = None

class CoreNetworkPolicyTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ChangeSetState: Optional[ChangeSetStateType] = None
    PolicyErrors: Optional[List[CoreNetworkPolicyErrorTypeDef]] = None
    PolicyDocument: Optional[str] = None

class ListCoreNetworkPolicyVersionsResponseTypeDef(BaseModel):
    CoreNetworkPolicyVersions: List[CoreNetworkPolicyVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RouteTableIdentifierTypeDef(BaseModel):
    TransitGatewayRouteTableArn: Optional[str] = None
    CoreNetworkSegmentEdge: Optional[CoreNetworkSegmentEdgeIdentifierTypeDef] = None
    CoreNetworkNetworkFunctionGroup: Optional[       CoreNetworkNetworkFunctionGroupIdentifierTypeDef     ] = None

class CreateDeviceRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    AWSLocation: Optional[AWSLocationTypeDef] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Vendor: Optional[str] = None
    Model: Optional[str] = None
    SerialNumber: Optional[str] = None
    Location: Optional[LocationTypeDef] = None
    SiteId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSiteRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    Description: Optional[str] = None
    Location: Optional[LocationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DeviceTypeDef(BaseModel):
    DeviceId: Optional[str] = None
    DeviceArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    AWSLocation: Optional[AWSLocationTypeDef] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Vendor: Optional[str] = None
    Model: Optional[str] = None
    SerialNumber: Optional[str] = None
    Location: Optional[LocationTypeDef] = None
    SiteId: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[DeviceStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class SiteTypeDef(BaseModel):
    SiteId: Optional[str] = None
    SiteArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    Description: Optional[str] = None
    Location: Optional[LocationTypeDef] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[SiteStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class UpdateDeviceRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceId: str
    AWSLocation: Optional[AWSLocationTypeDef] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Vendor: Optional[str] = None
    Model: Optional[str] = None
    SerialNumber: Optional[str] = None
    Location: Optional[LocationTypeDef] = None
    SiteId: Optional[str] = None

class UpdateSiteRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    SiteId: str
    Description: Optional[str] = None
    Location: Optional[LocationTypeDef] = None

class CreateVpcAttachmentRequestRequestTypeDef(BaseModel):
    CoreNetworkId: str
    VpcArn: str
    SubnetArns: Sequence[str]
    Options: Optional[VpcOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class UpdateVpcAttachmentRequestRequestTypeDef(BaseModel):
    AttachmentId: str
    AddSubnetArns: Optional[Sequence[str]] = None
    RemoveSubnetArns: Optional[Sequence[str]] = None
    Options: Optional[VpcOptionsTypeDef] = None

class DescribeGlobalNetworksRequestDescribeGlobalNetworksPaginateTypeDef(BaseModel):
    GlobalNetworkIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectPeerAssociationsRequestGetConnectPeerAssociationsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectPeerIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectionsRequestGetConnectionsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    ConnectionIds: Optional[Sequence[str]] = None
    DeviceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCoreNetworkChangeEventsRequestGetCoreNetworkChangeEventsPaginateTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCoreNetworkChangeSetRequestGetCoreNetworkChangeSetPaginateTypeDef(BaseModel):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCustomerGatewayAssociationsRequestGetCustomerGatewayAssociationsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    CustomerGatewayArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDevicesRequestGetDevicesPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLinkAssociationsRequestGetLinkAssociationsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLinksRequestGetLinksPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    LinkIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourceCountsRequestGetNetworkResourceCountsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourceRelationshipsRequestGetNetworkResourceRelationshipsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourcesRequestGetNetworkResourcesPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkTelemetryRequestGetNetworkTelemetryPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSitesRequestGetSitesPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    SiteIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayConnectPeerAssociationsRequestGetTransitGatewayConnectPeerAssociationsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayRegistrationsRequestGetTransitGatewayRegistrationsPaginateTypeDef(BaseModel):
    GlobalNetworkId: str
    TransitGatewayArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachmentsRequestListAttachmentsPaginateTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    EdgeLocation: Optional[str] = None
    State: Optional[AttachmentStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectPeersRequestListConnectPeersPaginateTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreNetworkPolicyVersionsRequestListCoreNetworkPolicyVersionsPaginateTypeDef(BaseModel):
    CoreNetworkId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreNetworksRequestListCoreNetworksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPeeringsRequestListPeeringsPaginateTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    PeeringType: Optional[Literal["TRANSIT_GATEWAY"]] = None
    EdgeLocation: Optional[str] = None
    State: Optional[PeeringStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourceCountsResponseTypeDef(BaseModel):
    NetworkResourceCounts: List[NetworkResourceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetNetworkResourceRelationshipsResponseTypeDef(BaseModel):
    Relationships: List[RelationshipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ViaTypeDef(BaseModel):
    NetworkFunctionGroups: Optional[List[NetworkFunctionGroupTypeDef]] = None
    WithEdgeOverrides: Optional[List[EdgeOverrideTypeDef]] = None

class PathComponentTypeDef(BaseModel):
    Sequence: Optional[int] = None
    Resource: Optional[NetworkResourceSummaryTypeDef] = None
    DestinationCidrBlock: Optional[str] = None

class NetworkRouteTypeDef(BaseModel):
    DestinationCidrBlock: Optional[str] = None
    Destinations: Optional[List[NetworkRouteDestinationTypeDef]] = None
    PrefixListId: Optional[str] = None
    State: Optional[RouteStateType] = None
    Type: Optional[RouteTypeType] = None

class PeeringErrorTypeDef(BaseModel):
    Code: Optional[PeeringErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None
    MissingPermissionsContext: Optional[PermissionsErrorContextTypeDef] = None

class StartRouteAnalysisRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    Source: RouteAnalysisEndpointOptionsSpecificationTypeDef
    Destination: RouteAnalysisEndpointOptionsSpecificationTypeDef
    IncludeReturnPath: Optional[bool] = None
    UseMiddleboxes: Optional[bool] = None

class TransitGatewayRegistrationTypeDef(BaseModel):
    GlobalNetworkId: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    State: Optional[TransitGatewayRegistrationStateReasonTypeDef] = None

class ListOrganizationServiceAccessStatusResponseTypeDef(BaseModel):
    OrganizationStatus: OrganizationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartOrganizationServiceAccessUpdateResponseTypeDef(BaseModel):
    OrganizationStatus: OrganizationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectPeersResponseTypeDef(BaseModel):
    ConnectPeers: List[ConnectPeerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionsResponseTypeDef(BaseModel):
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCoreNetworksResponseTypeDef(BaseModel):
    CoreNetworks: List[CoreNetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateGlobalNetworkResponseTypeDef(BaseModel):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalNetworkResponseTypeDef(BaseModel):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalNetworksResponseTypeDef(BaseModel):
    GlobalNetworks: List[GlobalNetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGlobalNetworkResponseTypeDef(BaseModel):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResourcesResponseTypeDef(BaseModel):
    NetworkResources: List[NetworkResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AttachmentTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    AttachmentId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    State: Optional[AttachmentStateType] = None
    EdgeLocation: Optional[str] = None
    ResourceArn: Optional[str] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ProposedSegmentChange: Optional[ProposedSegmentChangeTypeDef] = None
    ProposedNetworkFunctionGroupChange: Optional[       ProposedNetworkFunctionGroupChangeTypeDef     ] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    LastModificationErrors: Optional[List[AttachmentErrorTypeDef]] = None

class CreateLinkResponseTypeDef(BaseModel):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLinkResponseTypeDef(BaseModel):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinksResponseTypeDef(BaseModel):
    Links: List[LinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateLinkResponseTypeDef(BaseModel):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectPeerTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    ConnectPeerId: Optional[str] = None
    EdgeLocation: Optional[str] = None
    State: Optional[ConnectPeerStateType] = None
    CreatedAt: Optional[datetime] = None
    Configuration: Optional[ConnectPeerConfigurationTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    SubnetArn: Optional[str] = None
    LastModificationErrors: Optional[List[ConnectPeerErrorTypeDef]] = None

class GetNetworkTelemetryResponseTypeDef(BaseModel):
    NetworkTelemetry: List[NetworkTelemetryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCoreNetworkChangeEventsResponseTypeDef(BaseModel):
    CoreNetworkChangeEvents: List[CoreNetworkChangeEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CoreNetworkTypeDef(BaseModel):
    GlobalNetworkId: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[CoreNetworkStateType] = None
    Segments: Optional[List[CoreNetworkSegmentTypeDef]] = None
    NetworkFunctionGroups: Optional[List[CoreNetworkNetworkFunctionGroupTypeDef]] = None
    Edges: Optional[List[CoreNetworkEdgeTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None

class DeleteCoreNetworkPolicyVersionResponseTypeDef(BaseModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkPolicyResponseTypeDef(BaseModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCoreNetworkPolicyResponseTypeDef(BaseModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreCoreNetworkPolicyVersionResponseTypeDef(BaseModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkRoutesRequestRequestTypeDef(BaseModel):
    GlobalNetworkId: str
    RouteTableIdentifier: RouteTableIdentifierTypeDef
    ExactCidrMatches: Optional[Sequence[str]] = None
    LongestPrefixMatches: Optional[Sequence[str]] = None
    SubnetOfMatches: Optional[Sequence[str]] = None
    SupernetOfMatches: Optional[Sequence[str]] = None
    PrefixListIds: Optional[Sequence[str]] = None
    States: Optional[Sequence[RouteStateType]] = None
    Types: Optional[Sequence[RouteTypeType]] = None
    DestinationFilters: Optional[Mapping[str, Sequence[str]]] = None

class CreateDeviceResponseTypeDef(BaseModel):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeviceResponseTypeDef(BaseModel):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicesResponseTypeDef(BaseModel):
    Devices: List[DeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateDeviceResponseTypeDef(BaseModel):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteResponseTypeDef(BaseModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSiteResponseTypeDef(BaseModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSitesResponseTypeDef(BaseModel):
    Sites: List[SiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSiteResponseTypeDef(BaseModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceInsertionActionTypeDef(BaseModel):
    Action: Optional[SegmentActionServiceInsertionType] = None
    Mode: Optional[SendViaModeType] = None
    WhenSentTo: Optional[WhenSentToTypeDef] = None
    Via: Optional[ViaTypeDef] = None

class RouteAnalysisPathTypeDef(BaseModel):
    CompletionStatus: Optional[RouteAnalysisCompletionTypeDef] = None
    Path: Optional[List[PathComponentTypeDef]] = None

class GetNetworkRoutesResponseTypeDef(BaseModel):
    RouteTableArn: str
    CoreNetworkSegmentEdge: CoreNetworkSegmentEdgeIdentifierTypeDef
    RouteTableType: RouteTableTypeType
    RouteTableTimestamp: datetime
    NetworkRoutes: List[NetworkRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PeeringTypeDef(BaseModel):
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    PeeringId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    PeeringType: Optional[Literal["TRANSIT_GATEWAY"]] = None
    State: Optional[PeeringStateType] = None
    EdgeLocation: Optional[str] = None
    ResourceArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    CreatedAt: Optional[datetime] = None
    LastModificationErrors: Optional[List[PeeringErrorTypeDef]] = None

class DeregisterTransitGatewayResponseTypeDef(BaseModel):
    TransitGatewayRegistration: TransitGatewayRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayRegistrationsResponseTypeDef(BaseModel):
    TransitGatewayRegistrations: List[TransitGatewayRegistrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegisterTransitGatewayResponseTypeDef(BaseModel):
    TransitGatewayRegistration: TransitGatewayRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptAttachmentResponseTypeDef(BaseModel):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectAttachmentTypeDef(BaseModel):
    Attachment: Optional[AttachmentTypeDef] = None
    TransportAttachmentId: Optional[str] = None
    Options: Optional[ConnectAttachmentOptionsTypeDef] = None

class DeleteAttachmentResponseTypeDef(BaseModel):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachmentsResponseTypeDef(BaseModel):
    Attachments: List[AttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectAttachmentResponseTypeDef(BaseModel):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SiteToSiteVpnAttachmentTypeDef(BaseModel):
    Attachment: Optional[AttachmentTypeDef] = None
    VpnConnectionArn: Optional[str] = None

class TransitGatewayRouteTableAttachmentTypeDef(BaseModel):
    Attachment: Optional[AttachmentTypeDef] = None
    PeeringId: Optional[str] = None
    TransitGatewayRouteTableArn: Optional[str] = None

class VpcAttachmentTypeDef(BaseModel):
    Attachment: Optional[AttachmentTypeDef] = None
    SubnetArns: Optional[List[str]] = None
    Options: Optional[VpcOptionsTypeDef] = None

class CreateConnectPeerResponseTypeDef(BaseModel):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectPeerResponseTypeDef(BaseModel):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectPeerResponseTypeDef(BaseModel):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreNetworkResponseTypeDef(BaseModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCoreNetworkResponseTypeDef(BaseModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkResponseTypeDef(BaseModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCoreNetworkResponseTypeDef(BaseModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CoreNetworkChangeValuesTypeDef(BaseModel):
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    Asn: Optional[int] = None
    Cidr: Optional[str] = None
    DestinationIdentifier: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    SharedSegments: Optional[List[str]] = None
    ServiceInsertionActions: Optional[List[ServiceInsertionActionTypeDef]] = None

class RouteAnalysisTypeDef(BaseModel):
    GlobalNetworkId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    RouteAnalysisId: Optional[str] = None
    StartTimestamp: Optional[datetime] = None
    Status: Optional[RouteAnalysisStatusType] = None
    Source: Optional[RouteAnalysisEndpointOptionsTypeDef] = None
    Destination: Optional[RouteAnalysisEndpointOptionsTypeDef] = None
    IncludeReturnPath: Optional[bool] = None
    UseMiddleboxes: Optional[bool] = None
    ForwardPath: Optional[RouteAnalysisPathTypeDef] = None
    ReturnPath: Optional[RouteAnalysisPathTypeDef] = None

class DeletePeeringResponseTypeDef(BaseModel):
    Peering: PeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPeeringsResponseTypeDef(BaseModel):
    Peerings: List[PeeringTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TransitGatewayPeeringTypeDef(BaseModel):
    Peering: Optional[PeeringTypeDef] = None
    TransitGatewayArn: Optional[str] = None
    TransitGatewayPeeringAttachmentId: Optional[str] = None

class CreateConnectAttachmentResponseTypeDef(BaseModel):
    ConnectAttachment: ConnectAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectAttachmentResponseTypeDef(BaseModel):
    ConnectAttachment: ConnectAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteToSiteVpnAttachmentResponseTypeDef(BaseModel):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteToSiteVpnAttachmentResponseTypeDef(BaseModel):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayRouteTableAttachmentResponseTypeDef(BaseModel):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayRouteTableAttachmentResponseTypeDef(BaseModel):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcAttachmentResponseTypeDef(BaseModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcAttachmentResponseTypeDef(BaseModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcAttachmentResponseTypeDef(BaseModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CoreNetworkChangeTypeDef(BaseModel):
    Type: Optional[ChangeTypeType] = None
    Action: Optional[ChangeActionType] = None
    Identifier: Optional[str] = None
    PreviousValues: Optional[CoreNetworkChangeValuesTypeDef] = None
    NewValues: Optional[CoreNetworkChangeValuesTypeDef] = None
    IdentifierPath: Optional[str] = None

class GetRouteAnalysisResponseTypeDef(BaseModel):
    RouteAnalysis: RouteAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartRouteAnalysisResponseTypeDef(BaseModel):
    RouteAnalysis: RouteAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayPeeringResponseTypeDef(BaseModel):
    TransitGatewayPeering: TransitGatewayPeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayPeeringResponseTypeDef(BaseModel):
    TransitGatewayPeering: TransitGatewayPeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkChangeSetResponseTypeDef(BaseModel):
    CoreNetworkChanges: List[CoreNetworkChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

