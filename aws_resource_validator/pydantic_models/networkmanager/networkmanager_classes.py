from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.networkmanager.networkmanager_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AWSLocation(BaseValidatorModel):
    Zone: Optional[str] = None
    SubnetArn: Optional[str] = None


# This class is the input for the 'accept_attachment' function.
class AcceptAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AccountStatus(BaseValidatorModel):
    AccountId: Optional[str] = None
    SLRDeploymentStatus: Optional[str] = None


# This class is the input for the 'associate_connect_peer' function.
class AssociateConnectPeerRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerId: str
    DeviceId: str
    LinkId: Optional[str] = None


class ConnectPeerAssociation(BaseValidatorModel):
    ConnectPeerId: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[ConnectPeerAssociationStateType] = None


# This class is the input for the 'associate_customer_gateway' function.
class AssociateCustomerGatewayRequest(BaseValidatorModel):
    CustomerGatewayArn: str
    GlobalNetworkId: str
    DeviceId: str
    LinkId: Optional[str] = None


class CustomerGatewayAssociation(BaseValidatorModel):
    CustomerGatewayArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[CustomerGatewayAssociationStateType] = None


# This class is the input for the 'associate_link' function.
class AssociateLinkRequest(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str


class LinkAssociation(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    LinkAssociationState: Optional[LinkAssociationStateType] = None


# This class is the input for the 'associate_transit_gateway_connect_peer' function.
class AssociateTransitGatewayConnectPeerRequest(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str
    DeviceId: str
    LinkId: Optional[str] = None


class TransitGatewayConnectPeerAssociation(BaseValidatorModel):
    TransitGatewayConnectPeerArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    State: Optional[TransitGatewayConnectPeerAssociationStateType] = None


class AttachmentError(BaseValidatorModel):
    Code: Optional[AttachmentErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class Bandwidth(BaseValidatorModel):
    UploadSpeed: Optional[int] = None
    DownloadSpeed: Optional[int] = None


class BgpOptions(BaseValidatorModel):
    PeerAsn: Optional[int] = None


class ConnectAttachmentOptions(BaseValidatorModel):
    Protocol: Optional[TunnelProtocolType] = None


class ConnectPeerBgpConfiguration(BaseValidatorModel):
    CoreNetworkAsn: Optional[int] = None
    PeerAsn: Optional[int] = None
    CoreNetworkAddress: Optional[str] = None
    PeerAddress: Optional[str] = None


class ConnectPeerError(BaseValidatorModel):
    Code: Optional[ConnectPeerErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None


class ConnectionHealth(BaseValidatorModel):
    Type: Optional[ConnectionTypeType] = None
    Status: Optional[ConnectionStatusType] = None
    Timestamp: Optional[datetime] = None


class CoreNetworkChangeEventValues(BaseValidatorModel):
    EdgeLocation: Optional[str] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    AttachmentId: Optional[str] = None
    Cidr: Optional[str] = None


class CoreNetworkEdge(BaseValidatorModel):
    EdgeLocation: Optional[str] = None
    Asn: Optional[int] = None
    InsideCidrBlocks: Optional[List[str]] = None


class CoreNetworkNetworkFunctionGroupIdentifier(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocation: Optional[str] = None


class ServiceInsertionSegments(BaseValidatorModel):
    SendVia: Optional[List[str]] = None
    SendTo: Optional[List[str]] = None


class CoreNetworkPolicyError(BaseValidatorModel):
    ErrorCode: str
    Message: str
    Path: Optional[str] = None


class CoreNetworkPolicyVersion(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ChangeSetState: Optional[ChangeSetStateType] = None


class CoreNetworkSegmentEdgeIdentifier(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    SegmentName: Optional[str] = None
    EdgeLocation: Optional[str] = None


class CoreNetworkSegment(BaseValidatorModel):
    Name: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    SharedSegments: Optional[List[str]] = None


class Location(BaseValidatorModel):
    Address: Optional[str] = None
    Latitude: Optional[str] = None
    Longitude: Optional[str] = None


class VpcOptions(BaseValidatorModel):
    Ipv6Support: Optional[bool] = None
    ApplianceModeSupport: Optional[bool] = None


# This class is the input for the 'delete_attachment' function.
class DeleteAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


# This class is the input for the 'delete_connect_peer' function.
class DeleteConnectPeerRequest(BaseValidatorModel):
    ConnectPeerId: str


# This class is the input for the 'delete_connection' function.
class DeleteConnectionRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionId: str


# This class is the input for the 'delete_core_network_policy_version' function.
class DeleteCoreNetworkPolicyVersionRequest(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int


# This class is the input for the 'delete_core_network' function.
class DeleteCoreNetworkRequest(BaseValidatorModel):
    CoreNetworkId: str


# This class is the input for the 'delete_device' function.
class DeleteDeviceRequest(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str


# This class is the input for the 'delete_global_network' function.
class DeleteGlobalNetworkRequest(BaseValidatorModel):
    GlobalNetworkId: str


# This class is the input for the 'delete_link' function.
class DeleteLinkRequest(BaseValidatorModel):
    GlobalNetworkId: str
    LinkId: str


# This class is the input for the 'delete_peering' function.
class DeletePeeringRequest(BaseValidatorModel):
    PeeringId: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'delete_site' function.
class DeleteSiteRequest(BaseValidatorModel):
    GlobalNetworkId: str
    SiteId: str


# This class is the input for the 'deregister_transit_gateway' function.
class DeregisterTransitGatewayRequest(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArn: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_global_networks' function.
class DescribeGlobalNetworksRequest(BaseValidatorModel):
    GlobalNetworkIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'disassociate_connect_peer' function.
class DisassociateConnectPeerRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerId: str


# This class is the input for the 'disassociate_customer_gateway' function.
class DisassociateCustomerGatewayRequest(BaseValidatorModel):
    GlobalNetworkId: str
    CustomerGatewayArn: str


# This class is the input for the 'disassociate_link' function.
class DisassociateLinkRequest(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str


# This class is the input for the 'disassociate_transit_gateway_connect_peer' function.
class DisassociateTransitGatewayConnectPeerRequest(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArn: str


class EdgeOverride(BaseValidatorModel):
    EdgeSets: Optional[List[List[str]]] = None
    UseEdge: Optional[str] = None


class ExecuteCoreNetworkChangeSetRequest(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int


# This class is the input for the 'get_connect_attachment' function.
class GetConnectAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


# This class is the input for the 'get_connect_peer_associations' function.
class GetConnectPeerAssociationsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_connect_peer' function.
class GetConnectPeerRequest(BaseValidatorModel):
    ConnectPeerId: str


# This class is the input for the 'get_connections' function.
class GetConnectionsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionIds: Optional[List[str]] = None
    DeviceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_core_network_change_events' function.
class GetCoreNetworkChangeEventsRequest(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_core_network_change_set' function.
class GetCoreNetworkChangeSetRequest(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_core_network_policy' function.
class GetCoreNetworkPolicyRequest(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None


# This class is the input for the 'get_core_network' function.
class GetCoreNetworkRequest(BaseValidatorModel):
    CoreNetworkId: str


# This class is the input for the 'get_customer_gateway_associations' function.
class GetCustomerGatewayAssociationsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    CustomerGatewayArns: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_devices' function.
class GetDevicesRequest(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceIds: Optional[List[str]] = None
    SiteId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_direct_connect_gateway_attachment' function.
class GetDirectConnectGatewayAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


# This class is the input for the 'get_link_associations' function.
class GetLinkAssociationsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_links' function.
class GetLinksRequest(BaseValidatorModel):
    GlobalNetworkId: str
    LinkIds: Optional[List[str]] = None
    SiteId: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_network_resource_counts' function.
class GetNetworkResourceCountsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ResourceType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class NetworkResourceCount(BaseValidatorModel):
    ResourceType: Optional[str] = None
    Count: Optional[int] = None


# This class is the input for the 'get_network_resource_relationships' function.
class GetNetworkResourceRelationshipsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Relationship(BaseValidatorModel):
    From: Optional[str] = None
    To: Optional[str] = None


# This class is the input for the 'get_network_resources' function.
class GetNetworkResourcesRequest(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_network_telemetry' function.
class GetNetworkTelemetryRequest(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_route_analysis' function.
class GetRouteAnalysisRequest(BaseValidatorModel):
    GlobalNetworkId: str
    RouteAnalysisId: str


# This class is the input for the 'get_site_to_site_vpn_attachment' function.
class GetSiteToSiteVpnAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


# This class is the input for the 'get_sites' function.
class GetSitesRequest(BaseValidatorModel):
    GlobalNetworkId: str
    SiteIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_transit_gateway_connect_peer_associations' function.
class GetTransitGatewayConnectPeerAssociationsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_transit_gateway_peering' function.
class GetTransitGatewayPeeringRequest(BaseValidatorModel):
    PeeringId: str


# This class is the input for the 'get_transit_gateway_registrations' function.
class GetTransitGatewayRegistrationsRequest(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArns: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'get_transit_gateway_route_table_attachment' function.
class GetTransitGatewayRouteTableAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


# This class is the input for the 'get_vpc_attachment' function.
class GetVpcAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


# This class is the input for the 'list_attachments' function.
class ListAttachmentsRequest(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    EdgeLocation: Optional[str] = None
    State: Optional[AttachmentStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_connect_peers' function.
class ListConnectPeersRequest(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_core_network_policy_versions' function.
class ListCoreNetworkPolicyVersionsRequest(BaseValidatorModel):
    CoreNetworkId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_core_networks' function.
class ListCoreNetworksRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_organization_service_access_status' function.
class ListOrganizationServiceAccessStatusRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_peerings' function.
class ListPeeringsRequest(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PeeringType: Optional[Literal['TRANSIT_GATEWAY']] = None
    EdgeLocation: Optional[str] = None
    State: Optional[PeeringStateType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str


class NetworkFunctionGroup(BaseValidatorModel):
    Name: Optional[str] = None


class NetworkResourceSummary(BaseValidatorModel):
    RegisteredGatewayArn: Optional[str] = None
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None
    Definition: Optional[str] = None
    NameTag: Optional[str] = None
    IsMiddlebox: Optional[bool] = None


class NetworkRouteDestination(BaseValidatorModel):
    CoreNetworkAttachmentId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocation: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None


class PermissionsErrorContext(BaseValidatorModel):
    MissingPermission: Optional[str] = None


# This class is the input for the 'put_core_network_policy' function.
class PutCoreNetworkPolicyRequest(BaseValidatorModel):
    CoreNetworkId: str
    PolicyDocument: str
    Description: Optional[str] = None
    LatestVersionId: Optional[int] = None
    ClientToken: Optional[str] = None


class PutResourcePolicyRequest(BaseValidatorModel):
    PolicyDocument: str
    ResourceArn: str


# This class is the input for the 'register_transit_gateway' function.
class RegisterTransitGatewayRequest(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArn: str


# This class is the input for the 'reject_attachment' function.
class RejectAttachmentRequest(BaseValidatorModel):
    AttachmentId: str


# This class is the input for the 'restore_core_network_policy_version' function.
class RestoreCoreNetworkPolicyVersionRequest(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int


class RouteAnalysisCompletion(BaseValidatorModel):
    ResultCode: Optional[RouteAnalysisCompletionResultCodeType] = None
    ReasonCode: Optional[RouteAnalysisCompletionReasonCodeType] = None
    ReasonContext: Optional[Dict[str, str]] = None


class RouteAnalysisEndpointOptionsSpecification(BaseValidatorModel):
    TransitGatewayAttachmentArn: Optional[str] = None
    IpAddress: Optional[str] = None


class RouteAnalysisEndpointOptions(BaseValidatorModel):
    TransitGatewayAttachmentArn: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    IpAddress: Optional[str] = None


class WhenSentTo(BaseValidatorModel):
    WhenSentToSegmentsList: Optional[List[str]] = None


# This class is the input for the 'start_organization_service_access_update' function.
class StartOrganizationServiceAccessUpdateRequest(BaseValidatorModel):
    Action: str


class TransitGatewayRegistrationStateReason(BaseValidatorModel):
    Code: Optional[TransitGatewayRegistrationStateType] = None
    Message: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_connection' function.
class UpdateConnectionRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionId: str
    LinkId: Optional[str] = None
    ConnectedLinkId: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_core_network' function.
class UpdateCoreNetworkRequest(BaseValidatorModel):
    CoreNetworkId: str
    Description: Optional[str] = None


# This class is the input for the 'update_direct_connect_gateway_attachment' function.
class UpdateDirectConnectGatewayAttachmentRequest(BaseValidatorModel):
    AttachmentId: str
    EdgeLocations: Optional[List[str]] = None


# This class is the input for the 'update_global_network' function.
class UpdateGlobalNetworkRequest(BaseValidatorModel):
    GlobalNetworkId: str
    Description: Optional[str] = None


# This class is the input for the 'update_network_resource_metadata' function.
class UpdateNetworkResourceMetadataRequest(BaseValidatorModel):
    GlobalNetworkId: str
    ResourceArn: str
    Metadata: Dict[str, str]


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    PolicyDocument: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_network_resource_metadata' function.
class UpdateNetworkResourceMetadataResponse(BaseValidatorModel):
    ResourceArn: str
    Metadata: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class OrganizationStatus(BaseValidatorModel):
    OrganizationId: Optional[str] = None
    OrganizationAwsServiceAccessStatus: Optional[str] = None
    SLRDeploymentStatus: Optional[str] = None
    AccountStatusList: Optional[List[AccountStatus]] = None


# This class is the output for the 'associate_connect_peer' function.
class AssociateConnectPeerResponse(BaseValidatorModel):
    ConnectPeerAssociation: ConnectPeerAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_connect_peer' function.
class DisassociateConnectPeerResponse(BaseValidatorModel):
    ConnectPeerAssociation: ConnectPeerAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_connect_peer_associations' function.
class GetConnectPeerAssociationsResponse(BaseValidatorModel):
    ConnectPeerAssociations: List[ConnectPeerAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_customer_gateway' function.
class AssociateCustomerGatewayResponse(BaseValidatorModel):
    CustomerGatewayAssociation: CustomerGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_customer_gateway' function.
class DisassociateCustomerGatewayResponse(BaseValidatorModel):
    CustomerGatewayAssociation: CustomerGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_customer_gateway_associations' function.
class GetCustomerGatewayAssociationsResponse(BaseValidatorModel):
    CustomerGatewayAssociations: List[CustomerGatewayAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_link' function.
class AssociateLinkResponse(BaseValidatorModel):
    LinkAssociation: LinkAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_link' function.
class DisassociateLinkResponse(BaseValidatorModel):
    LinkAssociation: LinkAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_link_associations' function.
class GetLinkAssociationsResponse(BaseValidatorModel):
    LinkAssociations: List[LinkAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_transit_gateway_connect_peer' function.
class AssociateTransitGatewayConnectPeerResponse(BaseValidatorModel):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_transit_gateway_connect_peer' function.
class DisassociateTransitGatewayConnectPeerResponse(BaseValidatorModel):
    TransitGatewayConnectPeerAssociation: TransitGatewayConnectPeerAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transit_gateway_connect_peer_associations' function.
class GetTransitGatewayConnectPeerAssociationsResponse(BaseValidatorModel):
    TransitGatewayConnectPeerAssociations: List[TransitGatewayConnectPeerAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConnectPeerSummary(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    ConnectPeerId: Optional[str] = None
    EdgeLocation: Optional[str] = None
    ConnectPeerState: Optional[ConnectPeerStateType] = None
    CreatedAt: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    SubnetArn: Optional[str] = None


class Connection(BaseValidatorModel):
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
    Tags: Optional[List[Tag]] = None


class CoreNetworkSummary(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    State: Optional[CoreNetworkStateType] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_connection' function.
class CreateConnectionRequest(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str
    ConnectedDeviceId: str
    LinkId: Optional[str] = None
    ConnectedLinkId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_core_network' function.
class CreateCoreNetworkRequest(BaseValidatorModel):
    GlobalNetworkId: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_direct_connect_gateway_attachment' function.
class CreateDirectConnectGatewayAttachmentRequest(BaseValidatorModel):
    CoreNetworkId: str
    DirectConnectGatewayArn: str
    EdgeLocations: List[str]
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_global_network' function.
class CreateGlobalNetworkRequest(BaseValidatorModel):
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_site_to_site_vpn_attachment' function.
class CreateSiteToSiteVpnAttachmentRequest(BaseValidatorModel):
    CoreNetworkId: str
    VpnConnectionArn: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_transit_gateway_peering' function.
class CreateTransitGatewayPeeringRequest(BaseValidatorModel):
    CoreNetworkId: str
    TransitGatewayArn: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_transit_gateway_route_table_attachment' function.
class CreateTransitGatewayRouteTableAttachmentRequest(BaseValidatorModel):
    PeeringId: str
    TransitGatewayRouteTableArn: str
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class GlobalNetwork(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    GlobalNetworkArn: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[GlobalNetworkStateType] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class NetworkResource(BaseValidatorModel):
    RegisteredGatewayArn: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceArn: Optional[str] = None
    Definition: Optional[str] = None
    DefinitionTimestamp: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    Metadata: Optional[Dict[str, str]] = None


class ProposedNetworkFunctionGroupChange(BaseValidatorModel):
    Tags: Optional[List[Tag]] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    NetworkFunctionGroupName: Optional[str] = None


class ProposedSegmentChange(BaseValidatorModel):
    Tags: Optional[List[Tag]] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    SegmentName: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the input for the 'create_link' function.
class CreateLinkRequest(BaseValidatorModel):
    GlobalNetworkId: str
    Bandwidth: Bandwidth
    SiteId: str
    Description: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class Link(BaseValidatorModel):
    LinkId: Optional[str] = None
    LinkArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    SiteId: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Bandwidth: Optional[Bandwidth] = None
    Provider: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[LinkStateType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_link' function.
class UpdateLinkRequest(BaseValidatorModel):
    GlobalNetworkId: str
    LinkId: str
    Description: Optional[str] = None
    Type: Optional[str] = None
    Bandwidth: Optional[Bandwidth] = None
    Provider: Optional[str] = None


# This class is the input for the 'create_connect_peer' function.
class CreateConnectPeerRequest(BaseValidatorModel):
    ConnectAttachmentId: str
    PeerAddress: str
    CoreNetworkAddress: Optional[str] = None
    BgpOptions: Optional[BgpOptions] = None
    InsideCidrBlocks: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None
    SubnetArn: Optional[str] = None


# This class is the input for the 'create_connect_attachment' function.
class CreateConnectAttachmentRequest(BaseValidatorModel):
    CoreNetworkId: str
    EdgeLocation: str
    TransportAttachmentId: str
    Options: ConnectAttachmentOptions
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


class ConnectPeerConfiguration(BaseValidatorModel):
    CoreNetworkAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    Protocol: Optional[TunnelProtocolType] = None
    BgpConfigurations: Optional[List[ConnectPeerBgpConfiguration]] = None


class NetworkTelemetry(BaseValidatorModel):
    RegisteredGatewayArn: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceArn: Optional[str] = None
    Address: Optional[str] = None
    Health: Optional[ConnectionHealth] = None


class CoreNetworkChangeEvent(BaseValidatorModel):
    Type: Optional[ChangeTypeType] = None
    Action: Optional[ChangeActionType] = None
    IdentifierPath: Optional[str] = None
    EventTime: Optional[datetime] = None
    Status: Optional[ChangeStatusType] = None
    Values: Optional[CoreNetworkChangeEventValues] = None


class CoreNetworkNetworkFunctionGroup(BaseValidatorModel):
    Name: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    Segments: Optional[ServiceInsertionSegments] = None


class CoreNetworkPolicy(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PolicyVersionId: Optional[int] = None
    Alias: Optional[CoreNetworkPolicyAliasType] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    ChangeSetState: Optional[ChangeSetStateType] = None
    PolicyErrors: Optional[List[CoreNetworkPolicyError]] = None
    PolicyDocument: Optional[str] = None


# This class is the output for the 'list_core_network_policy_versions' function.
class ListCoreNetworkPolicyVersionsResponse(BaseValidatorModel):
    CoreNetworkPolicyVersions: List[CoreNetworkPolicyVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RouteTableIdentifier(BaseValidatorModel):
    TransitGatewayRouteTableArn: Optional[str] = None
    CoreNetworkSegmentEdge: Optional[CoreNetworkSegmentEdgeIdentifier] = None
    CoreNetworkNetworkFunctionGroup: Optional[CoreNetworkNetworkFunctionGroupIdentifier] = None


# This class is the input for the 'create_device' function.
class CreateDeviceRequest(BaseValidatorModel):
    GlobalNetworkId: str
    AWSLocation: Optional[AWSLocation] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Vendor: Optional[str] = None
    Model: Optional[str] = None
    SerialNumber: Optional[str] = None
    Location: Optional[Location] = None
    SiteId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_site' function.
class CreateSiteRequest(BaseValidatorModel):
    GlobalNetworkId: str
    Description: Optional[str] = None
    Location: Optional[Location] = None
    Tags: Optional[List[Tag]] = None


class Device(BaseValidatorModel):
    DeviceId: Optional[str] = None
    DeviceArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    AWSLocation: Optional[AWSLocation] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Vendor: Optional[str] = None
    Model: Optional[str] = None
    SerialNumber: Optional[str] = None
    Location: Optional[Location] = None
    SiteId: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[DeviceStateType] = None
    Tags: Optional[List[Tag]] = None


class Site(BaseValidatorModel):
    SiteId: Optional[str] = None
    SiteArn: Optional[str] = None
    GlobalNetworkId: Optional[str] = None
    Description: Optional[str] = None
    Location: Optional[Location] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[SiteStateType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'update_device' function.
class UpdateDeviceRequest(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: str
    AWSLocation: Optional[AWSLocation] = None
    Description: Optional[str] = None
    Type: Optional[str] = None
    Vendor: Optional[str] = None
    Model: Optional[str] = None
    SerialNumber: Optional[str] = None
    Location: Optional[Location] = None
    SiteId: Optional[str] = None


# This class is the input for the 'update_site' function.
class UpdateSiteRequest(BaseValidatorModel):
    GlobalNetworkId: str
    SiteId: str
    Description: Optional[str] = None
    Location: Optional[Location] = None


# This class is the input for the 'create_vpc_attachment' function.
class CreateVpcAttachmentRequest(BaseValidatorModel):
    CoreNetworkId: str
    VpcArn: str
    SubnetArns: List[str]
    Options: Optional[VpcOptions] = None
    Tags: Optional[List[Tag]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_vpc_attachment' function.
class UpdateVpcAttachmentRequest(BaseValidatorModel):
    AttachmentId: str
    AddSubnetArns: Optional[List[str]] = None
    RemoveSubnetArns: Optional[List[str]] = None
    Options: Optional[VpcOptions] = None


class DescribeGlobalNetworksRequestPaginate(BaseValidatorModel):
    GlobalNetworkIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetConnectPeerAssociationsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectPeerIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetConnectionsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    ConnectionIds: Optional[List[str]] = None
    DeviceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCoreNetworkChangeEventsRequestPaginate(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCoreNetworkChangeSetRequestPaginate(BaseValidatorModel):
    CoreNetworkId: str
    PolicyVersionId: int
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCustomerGatewayAssociationsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    CustomerGatewayArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDevicesRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceIds: Optional[List[str]] = None
    SiteId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetLinkAssociationsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    DeviceId: Optional[str] = None
    LinkId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetLinksRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    LinkIds: Optional[List[str]] = None
    SiteId: Optional[str] = None
    Type: Optional[str] = None
    Provider: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetNetworkResourceCountsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    ResourceType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetNetworkResourceRelationshipsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetNetworkResourcesRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetNetworkTelemetryRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    CoreNetworkId: Optional[str] = None
    RegisteredGatewayArn: Optional[str] = None
    AwsRegion: Optional[str] = None
    AccountId: Optional[str] = None
    ResourceType: Optional[str] = None
    ResourceArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSitesRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    SiteIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTransitGatewayConnectPeerAssociationsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayConnectPeerArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTransitGatewayRegistrationsRequestPaginate(BaseValidatorModel):
    GlobalNetworkId: str
    TransitGatewayArns: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttachmentsRequestPaginate(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    EdgeLocation: Optional[str] = None
    State: Optional[AttachmentStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectPeersRequestPaginate(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoreNetworkPolicyVersionsRequestPaginate(BaseValidatorModel):
    CoreNetworkId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoreNetworksRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPeeringsRequestPaginate(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    PeeringType: Optional[Literal['TRANSIT_GATEWAY']] = None
    EdgeLocation: Optional[str] = None
    State: Optional[PeeringStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_network_resource_counts' function.
class GetNetworkResourceCountsResponse(BaseValidatorModel):
    NetworkResourceCounts: List[NetworkResourceCount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_network_resource_relationships' function.
class GetNetworkResourceRelationshipsResponse(BaseValidatorModel):
    Relationships: List[Relationship]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Via(BaseValidatorModel):
    NetworkFunctionGroups: Optional[List[NetworkFunctionGroup]] = None
    WithEdgeOverrides: Optional[List[EdgeOverride]] = None


class PathComponent(BaseValidatorModel):
    Sequence: Optional[int] = None
    Resource: Optional[NetworkResourceSummary] = None
    DestinationCidrBlock: Optional[str] = None


class NetworkRoute(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    Destinations: Optional[List[NetworkRouteDestination]] = None
    PrefixListId: Optional[str] = None
    State: Optional[RouteStateType] = None
    Type: Optional[RouteTypeType] = None


class PeeringError(BaseValidatorModel):
    Code: Optional[PeeringErrorCodeType] = None
    Message: Optional[str] = None
    ResourceArn: Optional[str] = None
    RequestId: Optional[str] = None
    MissingPermissionsContext: Optional[PermissionsErrorContext] = None


# This class is the input for the 'start_route_analysis' function.
class StartRouteAnalysisRequest(BaseValidatorModel):
    GlobalNetworkId: str
    Source: RouteAnalysisEndpointOptionsSpecification
    Destination: RouteAnalysisEndpointOptionsSpecification
    IncludeReturnPath: Optional[bool] = None
    UseMiddleboxes: Optional[bool] = None


class TransitGatewayRegistration(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    State: Optional[TransitGatewayRegistrationStateReason] = None


# This class is the output for the 'list_organization_service_access_status' function.
class ListOrganizationServiceAccessStatusResponse(BaseValidatorModel):
    OrganizationStatus: OrganizationStatus
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_organization_service_access_update' function.
class StartOrganizationServiceAccessUpdateResponse(BaseValidatorModel):
    OrganizationStatus: OrganizationStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_connect_peers' function.
class ListConnectPeersResponse(BaseValidatorModel):
    ConnectPeers: List[ConnectPeerSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_connection' function.
class CreateConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_connection' function.
class DeleteConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_connections' function.
class GetConnectionsResponse(BaseValidatorModel):
    Connections: List[Connection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_connection' function.
class UpdateConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_core_networks' function.
class ListCoreNetworksResponse(BaseValidatorModel):
    CoreNetworks: List[CoreNetworkSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_global_network' function.
class CreateGlobalNetworkResponse(BaseValidatorModel):
    GlobalNetwork: GlobalNetwork
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_global_network' function.
class DeleteGlobalNetworkResponse(BaseValidatorModel):
    GlobalNetwork: GlobalNetwork
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_global_networks' function.
class DescribeGlobalNetworksResponse(BaseValidatorModel):
    GlobalNetworks: List[GlobalNetwork]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_global_network' function.
class UpdateGlobalNetworkResponse(BaseValidatorModel):
    GlobalNetwork: GlobalNetwork
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_network_resources' function.
class GetNetworkResourcesResponse(BaseValidatorModel):
    NetworkResources: List[NetworkResource]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Attachment(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    AttachmentId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    AttachmentType: Optional[AttachmentTypeType] = None
    State: Optional[AttachmentStateType] = None
    EdgeLocation: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    ResourceArn: Optional[str] = None
    AttachmentPolicyRuleNumber: Optional[int] = None
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ProposedSegmentChange: Optional[ProposedSegmentChange] = None
    ProposedNetworkFunctionGroupChange: Optional[ProposedNetworkFunctionGroupChange] = None
    CreatedAt: Optional[datetime] = None
    UpdatedAt: Optional[datetime] = None
    LastModificationErrors: Optional[List[AttachmentError]] = None


# This class is the output for the 'create_link' function.
class CreateLinkResponse(BaseValidatorModel):
    Link: Link
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_link' function.
class DeleteLinkResponse(BaseValidatorModel):
    Link: Link
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_links' function.
class GetLinksResponse(BaseValidatorModel):
    Links: List[Link]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_link' function.
class UpdateLinkResponse(BaseValidatorModel):
    Link: Link
    ResponseMetadata: ResponseMetadata


class ConnectPeer(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    ConnectAttachmentId: Optional[str] = None
    ConnectPeerId: Optional[str] = None
    EdgeLocation: Optional[str] = None
    State: Optional[ConnectPeerStateType] = None
    CreatedAt: Optional[datetime] = None
    Configuration: Optional[ConnectPeerConfiguration] = None
    Tags: Optional[List[Tag]] = None
    SubnetArn: Optional[str] = None
    LastModificationErrors: Optional[List[ConnectPeerError]] = None


# This class is the output for the 'get_network_telemetry' function.
class GetNetworkTelemetryResponse(BaseValidatorModel):
    NetworkTelemetry: List[NetworkTelemetry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_core_network_change_events' function.
class GetCoreNetworkChangeEventsResponse(BaseValidatorModel):
    CoreNetworkChangeEvents: List[CoreNetworkChangeEvent]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CoreNetwork(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    Description: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    State: Optional[CoreNetworkStateType] = None
    Segments: Optional[List[CoreNetworkSegment]] = None
    NetworkFunctionGroups: Optional[List[CoreNetworkNetworkFunctionGroup]] = None
    Edges: Optional[List[CoreNetworkEdge]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'delete_core_network_policy_version' function.
class DeleteCoreNetworkPolicyVersionResponse(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_core_network_policy' function.
class GetCoreNetworkPolicyResponse(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_core_network_policy' function.
class PutCoreNetworkPolicyResponse(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_core_network_policy_version' function.
class RestoreCoreNetworkPolicyVersionResponse(BaseValidatorModel):
    CoreNetworkPolicy: CoreNetworkPolicy
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'get_network_routes' function.
class GetNetworkRoutesRequest(BaseValidatorModel):
    GlobalNetworkId: str
    RouteTableIdentifier: RouteTableIdentifier
    ExactCidrMatches: Optional[List[str]] = None
    LongestPrefixMatches: Optional[List[str]] = None
    SubnetOfMatches: Optional[List[str]] = None
    SupernetOfMatches: Optional[List[str]] = None
    PrefixListIds: Optional[List[str]] = None
    States: Optional[List[RouteStateType]] = None
    Types: Optional[List[RouteTypeType]] = None
    DestinationFilters: Optional[Dict[str, List[str]]] = None


# This class is the output for the 'create_device' function.
class CreateDeviceResponse(BaseValidatorModel):
    Device: Device
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_device' function.
class DeleteDeviceResponse(BaseValidatorModel):
    Device: Device
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_devices' function.
class GetDevicesResponse(BaseValidatorModel):
    Devices: List[Device]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_device' function.
class UpdateDeviceResponse(BaseValidatorModel):
    Device: Device
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_site' function.
class CreateSiteResponse(BaseValidatorModel):
    Site: Site
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_site' function.
class DeleteSiteResponse(BaseValidatorModel):
    Site: Site
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_sites' function.
class GetSitesResponse(BaseValidatorModel):
    Sites: List[Site]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_site' function.
class UpdateSiteResponse(BaseValidatorModel):
    Site: Site
    ResponseMetadata: ResponseMetadata


class ServiceInsertionAction(BaseValidatorModel):
    Action: Optional[SegmentActionServiceInsertionType] = None
    Mode: Optional[SendViaModeType] = None
    WhenSentTo: Optional[WhenSentTo] = None
    Via: Optional[Via] = None


class RouteAnalysisPath(BaseValidatorModel):
    CompletionStatus: Optional[RouteAnalysisCompletion] = None
    Path: Optional[List[PathComponent]] = None


# This class is the output for the 'get_network_routes' function.
class GetNetworkRoutesResponse(BaseValidatorModel):
    RouteTableArn: str
    CoreNetworkSegmentEdge: CoreNetworkSegmentEdgeIdentifier
    RouteTableType: RouteTableTypeType
    RouteTableTimestamp: datetime
    NetworkRoutes: List[NetworkRoute]
    ResponseMetadata: ResponseMetadata


class Peering(BaseValidatorModel):
    CoreNetworkId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    PeeringId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    PeeringType: Optional[Literal['TRANSIT_GATEWAY']] = None
    State: Optional[PeeringStateType] = None
    EdgeLocation: Optional[str] = None
    ResourceArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    CreatedAt: Optional[datetime] = None
    LastModificationErrors: Optional[List[PeeringError]] = None


# This class is the output for the 'deregister_transit_gateway' function.
class DeregisterTransitGatewayResponse(BaseValidatorModel):
    TransitGatewayRegistration: TransitGatewayRegistration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transit_gateway_registrations' function.
class GetTransitGatewayRegistrationsResponse(BaseValidatorModel):
    TransitGatewayRegistrations: List[TransitGatewayRegistration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'register_transit_gateway' function.
class RegisterTransitGatewayResponse(BaseValidatorModel):
    TransitGatewayRegistration: TransitGatewayRegistration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_attachment' function.
class AcceptAttachmentResponse(BaseValidatorModel):
    Attachment: Attachment
    ResponseMetadata: ResponseMetadata


class ConnectAttachment(BaseValidatorModel):
    Attachment: Optional[Attachment] = None
    TransportAttachmentId: Optional[str] = None
    Options: Optional[ConnectAttachmentOptions] = None


# This class is the output for the 'delete_attachment' function.
class DeleteAttachmentResponse(BaseValidatorModel):
    Attachment: Attachment
    ResponseMetadata: ResponseMetadata


class DirectConnectGatewayAttachment(BaseValidatorModel):
    Attachment: Optional[Attachment] = None
    DirectConnectGatewayArn: Optional[str] = None


# This class is the output for the 'list_attachments' function.
class ListAttachmentsResponse(BaseValidatorModel):
    Attachments: List[Attachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'reject_attachment' function.
class RejectAttachmentResponse(BaseValidatorModel):
    Attachment: Attachment
    ResponseMetadata: ResponseMetadata


class SiteToSiteVpnAttachment(BaseValidatorModel):
    Attachment: Optional[Attachment] = None
    VpnConnectionArn: Optional[str] = None


class TransitGatewayRouteTableAttachment(BaseValidatorModel):
    Attachment: Optional[Attachment] = None
    PeeringId: Optional[str] = None
    TransitGatewayRouteTableArn: Optional[str] = None


class VpcAttachment(BaseValidatorModel):
    Attachment: Optional[Attachment] = None
    SubnetArns: Optional[List[str]] = None
    Options: Optional[VpcOptions] = None


# This class is the output for the 'create_connect_peer' function.
class CreateConnectPeerResponse(BaseValidatorModel):
    ConnectPeer: ConnectPeer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_connect_peer' function.
class DeleteConnectPeerResponse(BaseValidatorModel):
    ConnectPeer: ConnectPeer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_connect_peer' function.
class GetConnectPeerResponse(BaseValidatorModel):
    ConnectPeer: ConnectPeer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_core_network' function.
class CreateCoreNetworkResponse(BaseValidatorModel):
    CoreNetwork: CoreNetwork
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_core_network' function.
class DeleteCoreNetworkResponse(BaseValidatorModel):
    CoreNetwork: CoreNetwork
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_core_network' function.
class GetCoreNetworkResponse(BaseValidatorModel):
    CoreNetwork: CoreNetwork
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_core_network' function.
class UpdateCoreNetworkResponse(BaseValidatorModel):
    CoreNetwork: CoreNetwork
    ResponseMetadata: ResponseMetadata


class CoreNetworkChangeValues(BaseValidatorModel):
    SegmentName: Optional[str] = None
    NetworkFunctionGroupName: Optional[str] = None
    EdgeLocations: Optional[List[str]] = None
    Asn: Optional[int] = None
    Cidr: Optional[str] = None
    DestinationIdentifier: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    SharedSegments: Optional[List[str]] = None
    ServiceInsertionActions: Optional[List[ServiceInsertionAction]] = None


class RouteAnalysis(BaseValidatorModel):
    GlobalNetworkId: Optional[str] = None
    OwnerAccountId: Optional[str] = None
    RouteAnalysisId: Optional[str] = None
    StartTimestamp: Optional[datetime] = None
    Status: Optional[RouteAnalysisStatusType] = None
    Source: Optional[RouteAnalysisEndpointOptions] = None
    Destination: Optional[RouteAnalysisEndpointOptions] = None
    IncludeReturnPath: Optional[bool] = None
    UseMiddleboxes: Optional[bool] = None
    ForwardPath: Optional[RouteAnalysisPath] = None
    ReturnPath: Optional[RouteAnalysisPath] = None


# This class is the output for the 'delete_peering' function.
class DeletePeeringResponse(BaseValidatorModel):
    Peering: Peering
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_peerings' function.
class ListPeeringsResponse(BaseValidatorModel):
    Peerings: List[Peering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TransitGatewayPeering(BaseValidatorModel):
    Peering: Optional[Peering] = None
    TransitGatewayArn: Optional[str] = None
    TransitGatewayPeeringAttachmentId: Optional[str] = None


# This class is the output for the 'create_connect_attachment' function.
class CreateConnectAttachmentResponse(BaseValidatorModel):
    ConnectAttachment: ConnectAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_connect_attachment' function.
class GetConnectAttachmentResponse(BaseValidatorModel):
    ConnectAttachment: ConnectAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_direct_connect_gateway_attachment' function.
class CreateDirectConnectGatewayAttachmentResponse(BaseValidatorModel):
    DirectConnectGatewayAttachment: DirectConnectGatewayAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_direct_connect_gateway_attachment' function.
class GetDirectConnectGatewayAttachmentResponse(BaseValidatorModel):
    DirectConnectGatewayAttachment: DirectConnectGatewayAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_direct_connect_gateway_attachment' function.
class UpdateDirectConnectGatewayAttachmentResponse(BaseValidatorModel):
    DirectConnectGatewayAttachment: DirectConnectGatewayAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_site_to_site_vpn_attachment' function.
class CreateSiteToSiteVpnAttachmentResponse(BaseValidatorModel):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_site_to_site_vpn_attachment' function.
class GetSiteToSiteVpnAttachmentResponse(BaseValidatorModel):
    SiteToSiteVpnAttachment: SiteToSiteVpnAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transit_gateway_route_table_attachment' function.
class CreateTransitGatewayRouteTableAttachmentResponse(BaseValidatorModel):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transit_gateway_route_table_attachment' function.
class GetTransitGatewayRouteTableAttachmentResponse(BaseValidatorModel):
    TransitGatewayRouteTableAttachment: TransitGatewayRouteTableAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpc_attachment' function.
class CreateVpcAttachmentResponse(BaseValidatorModel):
    VpcAttachment: VpcAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_vpc_attachment' function.
class GetVpcAttachmentResponse(BaseValidatorModel):
    VpcAttachment: VpcAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_vpc_attachment' function.
class UpdateVpcAttachmentResponse(BaseValidatorModel):
    VpcAttachment: VpcAttachment
    ResponseMetadata: ResponseMetadata


class CoreNetworkChange(BaseValidatorModel):
    Type: Optional[ChangeTypeType] = None
    Action: Optional[ChangeActionType] = None
    Identifier: Optional[str] = None
    PreviousValues: Optional[CoreNetworkChangeValues] = None
    NewValues: Optional[CoreNetworkChangeValues] = None
    IdentifierPath: Optional[str] = None


# This class is the output for the 'get_route_analysis' function.
class GetRouteAnalysisResponse(BaseValidatorModel):
    RouteAnalysis: RouteAnalysis
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_route_analysis' function.
class StartRouteAnalysisResponse(BaseValidatorModel):
    RouteAnalysis: RouteAnalysis
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transit_gateway_peering' function.
class CreateTransitGatewayPeeringResponse(BaseValidatorModel):
    TransitGatewayPeering: TransitGatewayPeering
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transit_gateway_peering' function.
class GetTransitGatewayPeeringResponse(BaseValidatorModel):
    TransitGatewayPeering: TransitGatewayPeering
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_core_network_change_set' function.
class GetCoreNetworkChangeSetResponse(BaseValidatorModel):
    CoreNetworkChanges: List[CoreNetworkChange]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None