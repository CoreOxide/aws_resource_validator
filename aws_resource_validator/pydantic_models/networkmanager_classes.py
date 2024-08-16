from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AWSLocationTypeDef(BaseValidatorModel):
    Zone: Optional[str] = None
    SubnetArn: Optional[str] = None

class AcceptAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AccountStatusTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    SLRDeploymentStatus: Optional[str] = None

class AssociateConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerId: str
    DeviceId: str
    LinkId: Optional[str] = None

class ConnectPeerAssociationTypeDef(BaseValidatorModel):
    ConnectPeerId: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[ConnectPeerAssociationStateType] = None

class AssociateCustomerGatewayRequestRequestTypeDef(BaseValidatorModel):
    CustomerGatewayArn: str
    GlobalNetworkId: str
    DeviceId: str
    LinkId: Optional[str] = None

class CustomerGatewayAssociationTypeDef(BaseValidatorModel):
    CustomerGatewayArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[CustomerGatewayAssociationStateType] = None

class AssociateLinkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str

class LinkAssociationTypeDef(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    LinkAssociationState: Optional[LinkAssociationStateType] = None

class AssociateTransitGatewayConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str
    DeviceId: str
    LinkId: Optional[str] = None

class TransitGatewayConnectPeerAssociationTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeerArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[TransitGatewayConnectPeerAssociationStateType] = None

class AttachmentErrorTypeDef(BaseValidatorModel):
    Code: Optional[AttachmentErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class BandwidthTypeDef(BaseValidatorModel):
    UploadSpeed: Optional[int] = None
    DownloadSpeed: Optional[int] = None

class BgpOptionsTypeDef(BaseValidatorModel):
    PeerAsn: Optional[int] = None

class ConnectAttachmentOptionsTypeDef(BaseValidatorModel):
    Protocol: Optional[TunnelProtocolType] = None

class ConnectPeerBgpConfigurationTypeDef(BaseValidatorModel):
    CoreNetworkAsn: Optional[int] = None
    PeerAsn: Optional[int] = None
    CoreNetworkAddress: Optional[str] = None
    PeerAddress: Optional[str] = None

class ConnectPeerErrorTypeDef(BaseValidatorModel):
    Code: Optional[ConnectPeerErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None

class ConnectionHealthTypeDef(BaseValidatorModel):
    Type: Optional[ConnectionTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    Timestamp: Optional[datetime] = None

class CoreNetworkChangeEventValuesTypeDef(BaseValidatorModel):
    EdgeLocation: Optional[str] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    AttachmentId: Optional[str] = None
    Cidr: Optional[str] = None

class CoreNetworkEdgeTypeDef(BaseValidatorModel):
    EdgeLocation: Optional[str] = None
    Asn: Optional[int] = None
    InsideCidrBlocks: Optional[List[str]] = None

class CoreNetworkNetworkFunctionGroupIdentifierTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocation: Optional[str] = None

class ServiceInsertionSegmentsTypeDef(BaseValidatorModel):
    SendVia: Optional[List[str]] = None
    SendTo: Optional[List[str]] = None

class CoreNetworkPolicyErrorTypeDef(BaseValidatorModel):
    ErrorCode: str
    Message: str
    Path: Optional[str] = None

class CoreNetworkPolicyVersionTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ChangeSetState: Optional[ChangeSetStateType] = None

class CoreNetworkSegmentEdgeIdentifierTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    SegmentName: Optional[str] = None
    EdgeLocation: Optional[str] = None

class CoreNetworkSegmentTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    SharedSegments: Optional[List[str]] = None

class LocationTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Latitude: Optional[str] = None
    Longitude: Optional[str] = None

class VpcOptionsTypeDef(BaseValidatorModel):
    Ipv6Support: Optional[bool] = None
    ApplianceModeSupport: Optional[bool] = None

class DeleteAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str

class DeleteConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    ConnectPeerId: str

class DeleteConnectionRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionId: str

class DeleteCoreNetworkPolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int

class DeleteCoreNetworkRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str

class DeleteDeviceRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str

class DeleteGlobalNetworkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str

class DeleteLinkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    LinkId: str

class DeletePeeringRequestRequestTypeDef(BaseValidatorModel):
    PeeringId: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DeleteSiteRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    SiteId: str

class DeregisterTransitGatewayRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeGlobalNetworksRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DisassociateConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerId: str

class DisassociateCustomerGatewayRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CustomerGatewayArn: str

class DisassociateLinkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str

class DisassociateTransitGatewayConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str

class EdgeOverrideTypeDef(BaseValidatorModel):
    EdgeSets: Optional[List[List[str]]] = None
    UseEdge: Optional[str] = None

class ExecuteCoreNetworkChangeSetRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int

class GetConnectAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str

class GetConnectPeerAssociationsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    ConnectPeerId: str

class GetConnectionsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionIds: Optional[Sequence[str]] = None
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCoreNetworkChangeEventsRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCoreNetworkChangeSetRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCoreNetworkPolicyRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None

class GetCoreNetworkRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str

class GetCustomerGatewayAssociationsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CustomerGatewayArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetDevicesRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetLinkAssociationsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetLinksRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    LinkIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetNetworkResourceCountsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ResourceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class NetworkResourceCountTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    Count: Optional[int] = None

class GetNetworkResourceRelationshipsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RelationshipTypeDef(BaseValidatorModel):
    From: Optional[str] = None
    To: Optional[str] = None

class GetNetworkResourcesRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetNetworkTelemetryRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GetRouteAnalysisRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    RouteAnalysisId: str

class GetSiteToSiteVpnAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str

class GetSitesRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    SiteIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetTransitGatewayPeeringRequestRequestTypeDef(BaseValidatorModel):
    PeeringId: str

class GetTransitGatewayRegistrationsRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArns: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetTransitGatewayRouteTableAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str

class GetVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str

class ListAttachmentsRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    EdgeLocation: Optional[str] = None
    State: Optional[AttachmentStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListConnectPeersRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCoreNetworkPolicyVersionsRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCoreNetworksRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListOrganizationServiceAccessStatusRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPeeringsRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PeeringType: Optional[Literal["TRANSIT_GATEWAY"]] = None
    EdgeLocation: Optional[str] = None
    State: Optional[PeeringStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class NetworkFunctionGroupTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class NetworkResourceSummaryTypeDef(BaseValidatorModel):
    RegisteredGatewayArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    Definition: Optional[str] = None
    NameTag: Optional[str] = None
    IsMiddlebox: Optional[bool] = None

class NetworkRouteDestinationTypeDef(BaseValidatorModel):
    CoreNetworkAttachmentId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocation: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None

class PermissionsErrorContextTypeDef(BaseValidatorModel):
    MissingPermission: Optional[str] = None

class PutCoreNetworkPolicyRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyDocument: str
    Description: Optional[str] = None
    LatestVersionId: Optional[int] = None
    ClientToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyDocument: str
    ResourceArn: str

class RegisterTransitGatewayRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArn: str

class RejectAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str

class RestoreCoreNetworkPolicyVersionRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int

class RouteAnalysisCompletionTypeDef(BaseValidatorModel):
    ResultCode: Optional[RouteAnalysisCompletionResultCodeType] = None
    ReasonCode: Optional[RouteAnalysisCompletionReasonCodeType] = None
    ReasonContext: Optional[Dict[str, str]] = None

class RouteAnalysisEndpointOptionsSpecificationTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentArn: Optional[str] = None
    IpAddress: Optional[str] = None

class RouteAnalysisEndpointOptionsTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentArn: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    IpAddress: Optional[str] = None

class WhenSentToTypeDef(BaseValidatorModel):
    WhenSentToSegmentsList: Optional[List[str]] = None

class StartOrganizationServiceAccessUpdateRequestRequestTypeDef(BaseValidatorModel):
    Action: str

class TransitGatewayRegistrationStateReasonTypeDef(BaseValidatorModel):
    Code: Optional[TransitGatewayRegistrationStateType] = None
    Message: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateConnectionRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionId: str
    LinkId: Optional[str] = None
    ConnectedLinkId: Optional[str] = None
    Description: Optional[str] = None

class UpdateCoreNetworkRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    Description: Optional[str] = None

class UpdateGlobalNetworkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    Description: Optional[str] = None

class UpdateNetworkResourceMetadataRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ResourceArn: str
    Metadata: Mapping[str, str]

class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNetworkResourceMetadataResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class OrganizationStatusTypeDef(BaseValidatorModel):
    OrganizationId: Optional[str] = None
    OrganizationAwsServiceAccessStatus: Optional[str] = None
    SLRDeploymentStatus: Optional[str] = None
    AccountStatusList: Optional[List[AccountStatusTypeDef]] = None

class AssociateConnectPeerResponseTypeDef(BaseValidatorModel):
    ConnectPeerAssociation: ConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateConnectPeerResponseTypeDef(BaseValidatorModel):
    ConnectPeerAssociation: ConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectPeerAssociationsResponseTypeDef(BaseValidatorModel):
    ConnectPeerAssociations: List[ConnectPeerAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateCustomerGatewayResponseTypeDef(BaseValidatorModel):
    CustomerGatewayAssociation: CustomerGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateCustomerGatewayResponseTypeDef(BaseValidatorModel):
    CustomerGatewayAssociation: CustomerGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomerGatewayAssociationsResponseTypeDef(BaseValidatorModel):
    CustomerGatewayAssociations: List[CustomerGatewayAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateLinkResponseTypeDef(BaseValidatorModel):
    LinkAssociation: LinkAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateLinkResponseTypeDef(BaseValidatorModel):
    LinkAssociation: LinkAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinkAssociationsResponseTypeDef(BaseValidatorModel):
    LinkAssociations: List[LinkAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateTransitGatewayConnectPeerResponseTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayConnectPeerResponseTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayConnectPeerAssociationsResponseTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeerAssociations: List[TransitGatewayConnectPeerAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ConnectPeerSummaryTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    ConnectPeerId: Optional[str] = None
    EdgeLocation: Optional[str] = None
    ConnectPeerState: Optional[ConnectPeerStateType] = None
    CreatedAt: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    SubnetArn: Optional[str] = None

class ConnectionTypeDef(BaseValidatorModel):
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

class CoreNetworkSummaryTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    State: Optional[CoreNetworkStateType] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateConnectionRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str
    ConnectedDeviceId: str
    LinkId: Optional[str] = None
    ConnectedLinkId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateCoreNetworkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None

class CreateGlobalNetworkRequestRequestTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSiteToSiteVpnAttachmentRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    VpnConnectionArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateTransitGatewayPeeringRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    TransitGatewayArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateTransitGatewayRouteTableAttachmentRequestRequestTypeDef(BaseValidatorModel):
    PeeringId: str
    TransitGatewayRouteTableArn: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class GlobalNetworkTypeDef(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    GlobalNetworkArn: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[GlobalNetworkStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkResourceTypeDef(BaseValidatorModel):
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

class ProposedNetworkFunctionGroupChangeTypeDef(BaseValidatorModel):
    Tags: Optional[List[TagTypeDef]] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    NetworkFunctionGroupName: Optional[str] = None

class ProposedSegmentChangeTypeDef(BaseValidatorModel):
    Tags: Optional[List[TagTypeDef]] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    SegmentName: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class CreateLinkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    Bandwidth: BandwidthTypeDef
    SiteId: str
    Description: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class LinkTypeDef(BaseValidatorModel):
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

class UpdateLinkRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    LinkId: str
    Description: Optional[str] = None
    Type: Optional[str] = None
    Bandwidth: Optional[BandwidthTypeDef] = None
    Provider: Optional[str] = None

class CreateConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    ConnectAttachmentId: str
    PeerAddress: str
    CoreNetworkAddress: Optional[str] = None
    BgpOptions: Optional[BgpOptionsTypeDef] = None
    InsideCidrBlocks: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None
    SubnetArn: Optional[str] = None

class CreateConnectAttachmentRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    EdgeLocation: str
    TransportAttachmentId: str
    Options: ConnectAttachmentOptionsTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class ConnectPeerConfigurationTypeDef(BaseValidatorModel):
    CoreNetworkAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    Protocol: Optional[TunnelProtocolType] = None
    BgpConfigurations: Optional[List[ConnectPeerBgpConfigurationTypeDef]] = None

class NetworkTelemetryTypeDef(BaseValidatorModel):
    RegisteredGatewayArn: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceArn: Optional[str] = None
    Address: Optional[str] = None
    Health: Optional[ConnectionHealthTypeDef] = None

class CoreNetworkChangeEventTypeDef(BaseValidatorModel):
    Type: Optional[ChangeTypeType] = None
    Action: Optional[ChangeActionType] = None
    IdentifierPath: Optional[str] = None
    EventTime: Optional[datetime] = None
    Status: Optional[ChangeStatusType] = None
    Values: Optional[CoreNetworkChangeEventValuesTypeDef] = None

class CoreNetworkNetworkFunctionGroupTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    Segments: Optional[ServiceInsertionSegmentsTypeDef] = None

class CoreNetworkPolicyTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ChangeSetState: Optional[ChangeSetStateType] = None
    PolicyErrors: Optional[List[CoreNetworkPolicyErrorTypeDef]] = None
    PolicyDocument: Optional[str] = None

class ListCoreNetworkPolicyVersionsResponseTypeDef(BaseValidatorModel):
    CoreNetworkPolicyVersions: List[CoreNetworkPolicyVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RouteTableIdentifierTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableArn: Optional[str] = None
    CoreNetworkSegmentEdge: Optional[CoreNetworkSegmentEdgeIdentifierTypeDef] = None
    CoreNetworkNetworkFunctionGroup: Optional[       CoreNetworkNetworkFunctionGroupIdentifierTypeDef     ] = None

class CreateDeviceRequestRequestTypeDef(BaseValidatorModel):
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

class CreateSiteRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    Description: Optional[str] = None
    Location: Optional[LocationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DeviceTypeDef(BaseValidatorModel):
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

class SiteTypeDef(BaseValidatorModel):
    SiteId: Optional[str] = None
    SiteArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    Description: Optional[str] = None
    Location: Optional[LocationTypeDef] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[SiteStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class UpdateDeviceRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateSiteRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    SiteId: str
    Description: Optional[str] = None
    Location: Optional[LocationTypeDef] = None

class CreateVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    VpcArn: str
    SubnetArns: Sequence[str]
    Options: Optional[VpcOptionsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientToken: Optional[str] = None

class UpdateVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str
    AddSubnetArns: Optional[Sequence[str]] = None
    RemoveSubnetArns: Optional[Sequence[str]] = None
    Options: Optional[VpcOptionsTypeDef] = None

class DescribeGlobalNetworksRequestDescribeGlobalNetworksPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectPeerAssociationsRequestGetConnectPeerAssociationsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectionsRequestGetConnectionsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionIds: Optional[Sequence[str]] = None
    DeviceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCoreNetworkChangeEventsRequestGetCoreNetworkChangeEventsPaginateTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCoreNetworkChangeSetRequestGetCoreNetworkChangeSetPaginateTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCustomerGatewayAssociationsRequestGetCustomerGatewayAssociationsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CustomerGatewayArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDevicesRequestGetDevicesPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLinkAssociationsRequestGetLinkAssociationsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLinksRequestGetLinksPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    LinkIds: Optional[Sequence[str]] = None
    SiteId: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourceCountsRequestGetNetworkResourceCountsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourceRelationshipsRequestGetNetworkResourceRelationshipsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourcesRequestGetNetworkResourcesPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkTelemetryRequestGetNetworkTelemetryPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSitesRequestGetSitesPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    SiteIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayConnectPeerAssociationsRequestGetTransitGatewayConnectPeerAssociationsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayRegistrationsRequestGetTransitGatewayRegistrationsPaginateTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArns: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttachmentsRequestListAttachmentsPaginateTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    EdgeLocation: Optional[str] = None
    State: Optional[AttachmentStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConnectPeersRequestListConnectPeersPaginateTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreNetworkPolicyVersionsRequestListCoreNetworkPolicyVersionsPaginateTypeDef(BaseValidatorModel):
    CoreNetworkId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreNetworksRequestListCoreNetworksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPeeringsRequestListPeeringsPaginateTypeDef(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PeeringType: Optional[Literal["TRANSIT_GATEWAY"]] = None
    EdgeLocation: Optional[str] = None
    State: Optional[PeeringStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkResourceCountsResponseTypeDef(BaseValidatorModel):
    NetworkResourceCounts: List[NetworkResourceCountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetNetworkResourceRelationshipsResponseTypeDef(BaseValidatorModel):
    Relationships: List[RelationshipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ViaTypeDef(BaseValidatorModel):
    NetworkFunctionGroups: Optional[List[NetworkFunctionGroupTypeDef]] = None
    WithEdgeOverrides: Optional[List[EdgeOverrideTypeDef]] = None

class PathComponentTypeDef(BaseValidatorModel):
    Sequence: Optional[int] = None
    Resource: Optional[NetworkResourceSummaryTypeDef] = None
    DestinationCidrBlock: Optional[str] = None

class NetworkRouteTypeDef(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    Destinations: Optional[List[NetworkRouteDestinationTypeDef]] = None
    PrefixListId: Optional[str] = None
    State: Optional[RouteStateType] = None
    Type: Optional[RouteTypeType] = None

class PeeringErrorTypeDef(BaseValidatorModel):
    Code: Optional[PeeringErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None
    MissingPermissionsContext: Optional[PermissionsErrorContextTypeDef] = None

class StartRouteAnalysisRequestRequestTypeDef(BaseValidatorModel):
    GlobalNetworkId: str
    Source: RouteAnalysisEndpointOptionsSpecificationTypeDef
    Destination: RouteAnalysisEndpointOptionsSpecificationTypeDef
    IncludeReturnPath: Optional[bool] = None
    UseMiddleboxes: Optional[bool] = None

class TransitGatewayRegistrationTypeDef(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    State: Optional[TransitGatewayRegistrationStateReasonTypeDef] = None

class ListOrganizationServiceAccessStatusResponseTypeDef(BaseValidatorModel):
    OrganizationStatus: OrganizationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartOrganizationServiceAccessUpdateResponseTypeDef(BaseValidatorModel):
    OrganizationStatus: OrganizationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListConnectPeersResponseTypeDef(BaseValidatorModel):
    ConnectPeers: List[ConnectPeerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionsResponseTypeDef(BaseValidatorModel):
    Connections: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCoreNetworksResponseTypeDef(BaseValidatorModel):
    CoreNetworks: List[CoreNetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateGlobalNetworkResponseTypeDef(BaseValidatorModel):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalNetworkResponseTypeDef(BaseValidatorModel):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalNetworksResponseTypeDef(BaseValidatorModel):
    GlobalNetworks: List[GlobalNetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateGlobalNetworkResponseTypeDef(BaseValidatorModel):
    GlobalNetwork: GlobalNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkResourcesResponseTypeDef(BaseValidatorModel):
    NetworkResources: List[NetworkResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AttachmentTypeDef(BaseValidatorModel):
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

class CreateLinkResponseTypeDef(BaseValidatorModel):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLinkResponseTypeDef(BaseValidatorModel):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLinksResponseTypeDef(BaseValidatorModel):
    Links: List[LinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateLinkResponseTypeDef(BaseValidatorModel):
    Link: LinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectPeerTypeDef(BaseValidatorModel):
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

class GetNetworkTelemetryResponseTypeDef(BaseValidatorModel):
    NetworkTelemetry: List[NetworkTelemetryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCoreNetworkChangeEventsResponseTypeDef(BaseValidatorModel):
    CoreNetworkChangeEvents: List[CoreNetworkChangeEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CoreNetworkTypeDef(BaseValidatorModel):
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

class DeleteCoreNetworkPolicyVersionResponseTypeDef(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkPolicyResponseTypeDef(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutCoreNetworkPolicyResponseTypeDef(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreCoreNetworkPolicyVersionResponseTypeDef(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkRoutesRequestRequestTypeDef(BaseValidatorModel):
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

class CreateDeviceResponseTypeDef(BaseValidatorModel):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDeviceResponseTypeDef(BaseValidatorModel):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevicesResponseTypeDef(BaseValidatorModel):
    Devices: List[DeviceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateDeviceResponseTypeDef(BaseValidatorModel):
    Device: DeviceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteResponseTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSiteResponseTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSitesResponseTypeDef(BaseValidatorModel):
    Sites: List[SiteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateSiteResponseTypeDef(BaseValidatorModel):
    Site: SiteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceInsertionActionTypeDef(BaseValidatorModel):
    Action: Optional[SegmentActionServiceInsertionType] = None
    Mode: Optional[SendViaModeType] = None
    WhenSentTo: Optional[WhenSentToTypeDef] = None
    Via: Optional[ViaTypeDef] = None

class RouteAnalysisPathTypeDef(BaseValidatorModel):
    CompletionStatus: Optional[RouteAnalysisCompletionTypeDef] = None
    Path: Optional[List[PathComponentTypeDef]] = None

class GetNetworkRoutesResponseTypeDef(BaseValidatorModel):
    RouteTableArn: str
    CoreNetworkSegmentEdge: CoreNetworkSegmentEdgeIdentifierTypeDef
    RouteTableType: RouteTableTypeType
    RouteTableTimestamp: datetime
    NetworkRoutes: List[NetworkRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PeeringTypeDef(BaseValidatorModel):
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

class DeregisterTransitGatewayResponseTypeDef(BaseValidatorModel):
    TransitGatewayRegistration: TransitGatewayRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayRegistrationsResponseTypeDef(BaseValidatorModel):
    TransitGatewayRegistrations: List[TransitGatewayRegistrationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RegisterTransitGatewayResponseTypeDef(BaseValidatorModel):
    TransitGatewayRegistration: TransitGatewayRegistrationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptAttachmentResponseTypeDef(BaseValidatorModel):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectAttachmentTypeDef(BaseValidatorModel):
    Attachment: Optional[AttachmentTypeDef] = None
    TransportAttachmentId: Optional[str] = None
    Options: Optional[ConnectAttachmentOptionsTypeDef] = None

class DeleteAttachmentResponseTypeDef(BaseValidatorModel):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttachmentsResponseTypeDef(BaseValidatorModel):
    Attachments: List[AttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectAttachmentResponseTypeDef(BaseValidatorModel):
    Attachment: AttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SiteToSiteVpnAttachmentTypeDef(BaseValidatorModel):
    Attachment: Optional[AttachmentTypeDef] = None
    VpnConnectionArn: Optional[str] = None

class TransitGatewayRouteTableAttachmentTypeDef(BaseValidatorModel):
    Attachment: Optional[AttachmentTypeDef] = None
    PeeringId: Optional[str] = None
    TransitGatewayRouteTableArn: Optional[str] = None

class VpcAttachmentTypeDef(BaseValidatorModel):
    Attachment: Optional[AttachmentTypeDef] = None
    SubnetArns: Optional[List[str]] = None
    Options: Optional[VpcOptionsTypeDef] = None

class CreateConnectPeerResponseTypeDef(BaseValidatorModel):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteConnectPeerResponseTypeDef(BaseValidatorModel):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectPeerResponseTypeDef(BaseValidatorModel):
    ConnectPeer: ConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCoreNetworkResponseTypeDef(BaseValidatorModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCoreNetworkResponseTypeDef(BaseValidatorModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkResponseTypeDef(BaseValidatorModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCoreNetworkResponseTypeDef(BaseValidatorModel):
    CoreNetwork: CoreNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CoreNetworkChangeValuesTypeDef(BaseValidatorModel):
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    Asn: Optional[int] = None
    Cidr: Optional[str] = None
    DestinationIdentifier: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    SharedSegments: Optional[List[str]] = None
    ServiceInsertionActions: Optional[List[ServiceInsertionActionTypeDef]] = None

class RouteAnalysisTypeDef(BaseValidatorModel):
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

class DeletePeeringResponseTypeDef(BaseValidatorModel):
    Peering: PeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPeeringsResponseTypeDef(BaseValidatorModel):
    Peerings: List[PeeringTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TransitGatewayPeeringTypeDef(BaseValidatorModel):
    Peering: Optional[PeeringTypeDef] = None
    TransitGatewayArn: Optional[str] = None
    TransitGatewayPeeringAttachmentId: Optional[str] = None

class CreateConnectAttachmentResponseTypeDef(BaseValidatorModel):
    ConnectAttachment: ConnectAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectAttachmentResponseTypeDef(BaseValidatorModel):
    ConnectAttachment: ConnectAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSiteToSiteVpnAttachmentResponseTypeDef(BaseValidatorModel):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSiteToSiteVpnAttachmentResponseTypeDef(BaseValidatorModel):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayRouteTableAttachmentResponseTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayRouteTableAttachmentResponseTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcAttachmentResponseTypeDef(BaseValidatorModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpcAttachmentResponseTypeDef(BaseValidatorModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVpcAttachmentResponseTypeDef(BaseValidatorModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CoreNetworkChangeTypeDef(BaseValidatorModel):
    Type: Optional[ChangeTypeType] = None
    Action: Optional[ChangeActionType] = None
    Identifier: Optional[str] = None
    PreviousValues: Optional[CoreNetworkChangeValuesTypeDef] = None
    NewValues: Optional[CoreNetworkChangeValuesTypeDef] = None
    IdentifierPath: Optional[str] = None

class GetRouteAnalysisResponseTypeDef(BaseValidatorModel):
    RouteAnalysis: RouteAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartRouteAnalysisResponseTypeDef(BaseValidatorModel):
    RouteAnalysis: RouteAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayPeeringResponseTypeDef(BaseValidatorModel):
    TransitGatewayPeering: TransitGatewayPeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayPeeringResponseTypeDef(BaseValidatorModel):
    TransitGatewayPeering: TransitGatewayPeeringTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreNetworkChangeSetResponseTypeDef(BaseValidatorModel):
    CoreNetworkChanges: List[CoreNetworkChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

