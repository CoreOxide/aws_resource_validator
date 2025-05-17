from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ec2.ec2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AcceleratorCountRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class AcceleratorCount(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class AcceleratorTotalMemoryMiBRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class AcceleratorTotalMemoryMiB(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class AddressTransfer(BaseValidatorModel):
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    TransferAccountId: Optional[str] = None
    TransferOfferExpirationTimestamp: Optional[datetime] = None
    TransferOfferAcceptedTimestamp: Optional[datetime] = None
    AddressTransferStatus: Optional[AddressTransferStatusType] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'accept_capacity_reservation_billing_ownership' function.
class AcceptCapacityReservationBillingOwnershipRequest(BaseValidatorModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None


class TargetConfigurationRequest(BaseValidatorModel):
    OfferingId: str
    InstanceCount: Optional[int] = None


# This class is the input for the 'accept_transit_gateway_multicast_domain_associations' function.
class AcceptTransitGatewayMulticastDomainAssociationsRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'accept_transit_gateway_peering_attachment' function.
class AcceptTransitGatewayPeeringAttachmentRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'accept_transit_gateway_vpc_attachment' function.
class AcceptTransitGatewayVpcAttachmentRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'accept_vpc_endpoint_connections' function.
class AcceptVpcEndpointConnectionsRequest(BaseValidatorModel):
    ServiceId: str
    VpcEndpointIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'accept_vpc_peering_connection' function.
class AcceptVpcPeeringConnectionRequest(BaseValidatorModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None


class AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAccept(BaseValidatorModel):
    DryRun: Optional[bool] = None


class AccountAttributeValue(BaseValidatorModel):
    AttributeValue: Optional[str] = None


class ActiveInstance(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    SpotInstanceRequestId: Optional[str] = None
    InstanceHealth: Optional[InstanceHealthStatusType] = None


class AddIpamOperatingRegion(BaseValidatorModel):
    RegionName: Optional[str] = None


class AddIpamOrganizationalUnitExclusion(BaseValidatorModel):
    OrganizationsEntityPath: Optional[str] = None


class AddPrefixListEntry(BaseValidatorModel):
    Cidr: str
    Description: Optional[str] = None


class AddedPrincipal(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None
    ServicePermissionId: Optional[str] = None
    ServiceId: Optional[str] = None


class AnalysisComponent(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None


class RuleGroupTypePair(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    RuleGroupType: Optional[str] = None


class RuleOption(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None


class PtrUpdateStatus(BaseValidatorModel):
    Value: Optional[str] = None
    Status: Optional[str] = None
    Reason: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'advertise_byoip_cidr' function.
class AdvertiseByoipCidrRequest(BaseValidatorModel):
    Cidr: str
    Asn: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None


# This class is the input for the 'allocate_ipam_pool_cidr' function.
class AllocateIpamPoolCidrRequest(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None
    NetmaskLength: Optional[int] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PreviewNextCidr: Optional[bool] = None
    AllowedCidrs: Optional[List[str]] = None
    DisallowedCidrs: Optional[List[str]] = None


class IpamPoolAllocation(BaseValidatorModel):
    Cidr: Optional[str] = None
    IpamPoolAllocationId: Optional[str] = None
    Description: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamPoolAllocationResourceTypeType] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None


class AlternatePathHint(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentArn: Optional[str] = None


class PortRange(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None


class AnalysisLoadBalancerListener(BaseValidatorModel):
    LoadBalancerPort: Optional[int] = None
    InstancePort: Optional[int] = None


class AnalysisRouteTableRoute(BaseValidatorModel):
    DestinationCidr: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    NatGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    Origin: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    State: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    LocalGatewayId: Optional[str] = None


# This class is the input for the 'apply_security_groups_to_client_vpn_target_network' function.
class ApplySecurityGroupsToClientVpnTargetNetworkRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    VpcId: str
    SecurityGroupIds: List[str]
    DryRun: Optional[bool] = None


class AsnAssociation(BaseValidatorModel):
    Asn: Optional[str] = None
    Cidr: Optional[str] = None
    StatusMessage: Optional[str] = None
    State: Optional[AsnAssociationStateType] = None


class AsnAuthorizationContext(BaseValidatorModel):
    Message: str
    Signature: str


# This class is the input for the 'assign_ipv6_addresses' function.
class AssignIpv6AddressesRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[str]] = None
    Ipv6Addresses: Optional[List[str]] = None
    Ipv6AddressCount: Optional[int] = None


class AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddresses(BaseValidatorModel):
    Ipv4Prefixes: Optional[List[str]] = None
    Ipv4PrefixCount: Optional[int] = None
    PrivateIpAddresses: Optional[List[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    AllowReassignment: Optional[bool] = None


# This class is the input for the 'assign_private_ip_addresses' function.
class AssignPrivateIpAddressesRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    Ipv4Prefixes: Optional[List[str]] = None
    Ipv4PrefixCount: Optional[int] = None
    PrivateIpAddresses: Optional[List[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    AllowReassignment: Optional[bool] = None


class AssignedPrivateIpAddress(BaseValidatorModel):
    PrivateIpAddress: Optional[str] = None


class Ipv4PrefixSpecification(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None


# This class is the input for the 'assign_private_nat_gateway_address' function.
class AssignPrivateNatGatewayAddressRequest(BaseValidatorModel):
    NatGatewayId: str
    PrivateIpAddresses: Optional[List[str]] = None
    PrivateIpAddressCount: Optional[int] = None
    DryRun: Optional[bool] = None


class NatGatewayAddress(BaseValidatorModel):
    AllocationId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIp: Optional[str] = None
    PublicIp: Optional[str] = None
    AssociationId: Optional[str] = None
    IsPrimary: Optional[bool] = None
    FailureMessage: Optional[str] = None
    Status: Optional[NatGatewayAddressStatusType] = None


class AssociateAddressRequestClassicAddressAssociate(BaseValidatorModel):
    AllocationId: Optional[str] = None
    InstanceId: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    AllowReassociation: Optional[bool] = None


# This class is the input for the 'associate_address' function.
class AssociateAddressRequest(BaseValidatorModel):
    AllocationId: Optional[str] = None
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    AllowReassociation: Optional[bool] = None


class AssociateAddressRequestVpcAddressAssociate(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    AllowReassociation: Optional[bool] = None


# This class is the input for the 'associate_capacity_reservation_billing_owner' function.
class AssociateCapacityReservationBillingOwnerRequest(BaseValidatorModel):
    CapacityReservationId: str
    UnusedReservationBillingOwnerId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'associate_client_vpn_target_network' function.
class AssociateClientVpnTargetNetworkRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    SubnetId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


class AssociationStatus(BaseValidatorModel):
    Code: Optional[AssociationStatusCodeType] = None
    Message: Optional[str] = None


class AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpc(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'associate_dhcp_options' function.
class AssociateDhcpOptionsRequest(BaseValidatorModel):
    DhcpOptionsId: str
    VpcId: str
    DryRun: Optional[bool] = None


class AssociateDhcpOptionsRequestVpcAssociateDhcpOptions(BaseValidatorModel):
    DhcpOptionsId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'associate_enclave_certificate_iam_role' function.
class AssociateEnclaveCertificateIamRoleRequest(BaseValidatorModel):
    CertificateArn: str
    RoleArn: str
    DryRun: Optional[bool] = None


class IamInstanceProfileSpecification(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


# This class is the input for the 'associate_ipam_byoasn' function.
class AssociateIpamByoasnRequest(BaseValidatorModel):
    Asn: str
    Cidr: str
    DryRun: Optional[bool] = None


# This class is the input for the 'associate_nat_gateway_address' function.
class AssociateNatGatewayAddressRequest(BaseValidatorModel):
    NatGatewayId: str
    AllocationIds: List[str]
    PrivateIpAddresses: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class AssociateRouteTableRequestRouteTableAssociateWithSubnet(BaseValidatorModel):
    GatewayId: Optional[str] = None
    DryRun: Optional[bool] = None
    SubnetId: Optional[str] = None


# This class is the input for the 'associate_route_table' function.
class AssociateRouteTableRequest(BaseValidatorModel):
    RouteTableId: str
    GatewayId: Optional[str] = None
    DryRun: Optional[bool] = None
    SubnetId: Optional[str] = None


class RouteTableAssociationState(BaseValidatorModel):
    State: Optional[RouteTableAssociationStateCodeType] = None
    StatusMessage: Optional[str] = None


# This class is the input for the 'associate_security_group_vpc' function.
class AssociateSecurityGroupVpcRequest(BaseValidatorModel):
    GroupId: str
    VpcId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'associate_subnet_cidr_block' function.
class AssociateSubnetCidrBlockRequest(BaseValidatorModel):
    SubnetId: str
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    Ipv6CidrBlock: Optional[str] = None


# This class is the input for the 'associate_transit_gateway_multicast_domain' function.
class AssociateTransitGatewayMulticastDomainRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    TransitGatewayAttachmentId: str
    SubnetIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'associate_transit_gateway_policy_table' function.
class AssociateTransitGatewayPolicyTableRequest(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


class TransitGatewayPolicyTableAssociation(BaseValidatorModel):
    TransitGatewayPolicyTableId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None


# This class is the input for the 'associate_transit_gateway_route_table' function.
class AssociateTransitGatewayRouteTableRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


class TransitGatewayAssociation(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None


# This class is the input for the 'associate_trunk_interface' function.
class AssociateTrunkInterfaceRequest(BaseValidatorModel):
    BranchInterfaceId: str
    TrunkInterfaceId: str
    VlanId: Optional[int] = None
    GreKey: Optional[int] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'associate_vpc_cidr_block' function.
class AssociateVpcCidrBlockRequest(BaseValidatorModel):
    VpcId: str
    CidrBlock: Optional[str] = None
    Ipv6CidrBlockNetworkBorderGroup: Optional[str] = None
    Ipv6Pool: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    AmazonProvidedIpv6CidrBlock: Optional[bool] = None


class AssociatedRole(BaseValidatorModel):
    AssociatedRoleArn: Optional[str] = None
    CertificateS3BucketName: Optional[str] = None
    CertificateS3ObjectKey: Optional[str] = None
    EncryptionKmsKeyId: Optional[str] = None


class AssociatedTargetNetwork(BaseValidatorModel):
    NetworkId: Optional[str] = None
    NetworkType: Optional[Literal['vpc']] = None

Timestamp = Union[datetime, str]


class AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpc(BaseValidatorModel):
    VpcId: str
    Groups: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'attach_classic_link_vpc' function.
class AttachClassicLinkVpcRequest(BaseValidatorModel):
    InstanceId: str
    VpcId: str
    Groups: List[str]
    DryRun: Optional[bool] = None


class AttachClassicLinkVpcRequestVpcAttachClassicLinkInstance(BaseValidatorModel):
    InstanceId: str
    Groups: List[str]
    DryRun: Optional[bool] = None


class AttachInternetGatewayRequestInternetGatewayAttachToVpc(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'attach_internet_gateway' function.
class AttachInternetGatewayRequest(BaseValidatorModel):
    InternetGatewayId: str
    VpcId: str
    DryRun: Optional[bool] = None


class AttachInternetGatewayRequestVpcAttachInternetGateway(BaseValidatorModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'attach_verified_access_trust_provider' function.
class AttachVerifiedAccessTrustProviderRequest(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    VerifiedAccessTrustProviderId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


class AttachVolumeRequestInstanceAttachVolume(BaseValidatorModel):
    Device: str
    VolumeId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'attach_volume' function.
class AttachVolumeRequest(BaseValidatorModel):
    Device: str
    InstanceId: str
    VolumeId: str
    DryRun: Optional[bool] = None


class AttachVolumeRequestVolumeAttachToInstance(BaseValidatorModel):
    Device: str
    InstanceId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'attach_vpn_gateway' function.
class AttachVpnGatewayRequest(BaseValidatorModel):
    VpcId: str
    VpnGatewayId: str
    DryRun: Optional[bool] = None


class VpcAttachment(BaseValidatorModel):
    VpcId: Optional[str] = None
    State: Optional[AttachmentStatusType] = None


class AttachmentEnaSrdUdpSpecification(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None


class AttributeBooleanValue(BaseValidatorModel):
    Value: Optional[bool] = None


class RegionalSummary(BaseValidatorModel):
    RegionName: Optional[str] = None
    NumberOfMatchedAccounts: Optional[int] = None
    NumberOfUnmatchedAccounts: Optional[int] = None


class AttributeValue(BaseValidatorModel):
    Value: Optional[str] = None


class ClientVpnAuthorizationRuleStatus(BaseValidatorModel):
    Code: Optional[ClientVpnAuthorizationRuleStatusCodeType] = None
    Message: Optional[str] = None


# This class is the input for the 'authorize_client_vpn_ingress' function.
class AuthorizeClientVpnIngressRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    TargetNetworkCidr: str
    AccessGroupId: Optional[str] = None
    AuthorizeAllGroups: Optional[bool] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


class AvailabilityZoneMessage(BaseValidatorModel):
    Message: Optional[str] = None


class InstanceCapacity(BaseValidatorModel):
    AvailableCapacity: Optional[int] = None
    InstanceType: Optional[str] = None
    TotalCapacity: Optional[int] = None


class BaselineEbsBandwidthMbpsRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class BaselineEbsBandwidthMbps(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class EbsBlockDeviceResponse(BaseValidatorModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None


class EbsBlockDevice(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    KmsKeyId: Optional[str] = None
    Throughput: Optional[int] = None
    OutpostArn: Optional[str] = None
    Encrypted: Optional[bool] = None


class BlockPublicAccessStates(BaseValidatorModel):
    InternetGatewayBlockMode: Optional[BlockPublicAccessModeType] = None


class BundleTaskError(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class Byoasn(BaseValidatorModel):
    Asn: Optional[str] = None
    IpamId: Optional[str] = None
    StatusMessage: Optional[str] = None
    State: Optional[AsnStateType] = None


# This class is the input for the 'cancel_bundle_task' function.
class CancelBundleTaskRequest(BaseValidatorModel):
    BundleId: str
    DryRun: Optional[bool] = None


class CancelCapacityReservationFleetError(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


# This class is the input for the 'cancel_capacity_reservation_fleets' function.
class CancelCapacityReservationFleetsRequest(BaseValidatorModel):
    CapacityReservationFleetIds: List[str]
    DryRun: Optional[bool] = None


class CapacityReservationFleetCancellationState(BaseValidatorModel):
    CurrentFleetState: Optional[CapacityReservationFleetStateType] = None
    PreviousFleetState: Optional[CapacityReservationFleetStateType] = None
    CapacityReservationFleetId: Optional[str] = None


# This class is the input for the 'cancel_capacity_reservation' function.
class CancelCapacityReservationRequest(BaseValidatorModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'cancel_conversion_task' function.
class CancelConversionRequest(BaseValidatorModel):
    ConversionTaskId: str
    DryRun: Optional[bool] = None
    ReasonMessage: Optional[str] = None


# This class is the input for the 'cancel_declarative_policies_report' function.
class CancelDeclarativePoliciesReportRequest(BaseValidatorModel):
    ReportId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'cancel_export_task' function.
class CancelExportTaskRequest(BaseValidatorModel):
    ExportTaskId: str


# This class is the input for the 'cancel_image_launch_permission' function.
class CancelImageLaunchPermissionRequest(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'cancel_import_task' function.
class CancelImportTaskRequest(BaseValidatorModel):
    CancelReason: Optional[str] = None
    DryRun: Optional[bool] = None
    ImportTaskId: Optional[str] = None


# This class is the input for the 'cancel_reserved_instances_listing' function.
class CancelReservedInstancesListingRequest(BaseValidatorModel):
    ReservedInstancesListingId: str


class CancelSpotFleetRequestsError(BaseValidatorModel):
    Code: Optional[CancelBatchErrorCodeType] = None
    Message: Optional[str] = None


# This class is the input for the 'cancel_spot_fleet_requests' function.
class CancelSpotFleetRequestsRequest(BaseValidatorModel):
    SpotFleetRequestIds: List[str]
    TerminateInstances: bool
    DryRun: Optional[bool] = None


class CancelSpotFleetRequestsSuccessItem(BaseValidatorModel):
    CurrentSpotFleetRequestState: Optional[BatchStateType] = None
    PreviousSpotFleetRequestState: Optional[BatchStateType] = None
    SpotFleetRequestId: Optional[str] = None


# This class is the input for the 'cancel_spot_instance_requests' function.
class CancelSpotInstanceRequestsRequest(BaseValidatorModel):
    SpotInstanceRequestIds: List[str]
    DryRun: Optional[bool] = None


class CancelledSpotInstanceRequest(BaseValidatorModel):
    SpotInstanceRequestId: Optional[str] = None
    State: Optional[CancelSpotInstanceRequestStateType] = None


class CapacityAllocation(BaseValidatorModel):
    AllocationType: Optional[AllocationTypeType] = None
    Count: Optional[int] = None


class CapacityBlockExtensionOffering(BaseValidatorModel):
    CapacityBlockExtensionOfferingId: Optional[str] = None
    InstanceType: Optional[str] = None
    InstanceCount: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    StartDate: Optional[datetime] = None
    CapacityBlockExtensionStartDate: Optional[datetime] = None
    CapacityBlockExtensionEndDate: Optional[datetime] = None
    CapacityBlockExtensionDurationHours: Optional[int] = None
    UpfrontFee: Optional[str] = None
    CurrencyCode: Optional[str] = None
    Tenancy: Optional[CapacityReservationTenancyType] = None


class CapacityBlockExtension(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    InstanceType: Optional[str] = None
    InstanceCount: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    CapacityBlockExtensionOfferingId: Optional[str] = None
    CapacityBlockExtensionDurationHours: Optional[int] = None
    CapacityBlockExtensionStatus: Optional[CapacityBlockExtensionStatusType] = None
    CapacityBlockExtensionPurchaseDate: Optional[datetime] = None
    CapacityBlockExtensionStartDate: Optional[datetime] = None
    CapacityBlockExtensionEndDate: Optional[datetime] = None
    UpfrontFee: Optional[str] = None
    CurrencyCode: Optional[str] = None


class CapacityBlockOffering(BaseValidatorModel):
    CapacityBlockOfferingId: Optional[str] = None
    InstanceType: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    InstanceCount: Optional[int] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    CapacityBlockDurationHours: Optional[int] = None
    UpfrontFee: Optional[str] = None
    CurrencyCode: Optional[str] = None
    Tenancy: Optional[CapacityReservationTenancyType] = None
    CapacityBlockDurationMinutes: Optional[int] = None


class CapacityReservationInfo(BaseValidatorModel):
    InstanceType: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Tenancy: Optional[CapacityReservationTenancyType] = None


class CapacityReservationCommitmentInfo(BaseValidatorModel):
    CommittedInstanceCount: Optional[int] = None
    CommitmentEndDate: Optional[datetime] = None


class FleetCapacityReservation(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    InstancePlatform: Optional[CapacityReservationInstancePlatformType] = None
    AvailabilityZone: Optional[str] = None
    TotalInstanceCount: Optional[int] = None
    FulfilledCapacity: Optional[float] = None
    EbsOptimized: Optional[bool] = None
    CreateDate: Optional[datetime] = None
    Weight: Optional[float] = None
    Priority: Optional[int] = None


class CapacityReservationGroup(BaseValidatorModel):
    GroupArn: Optional[str] = None
    OwnerId: Optional[str] = None


class CapacityReservationOptionsRequest(BaseValidatorModel):
    UsageStrategy: Optional[Literal['use-capacity-reservations-first']] = None


class CapacityReservationOptions(BaseValidatorModel):
    UsageStrategy: Optional[Literal['use-capacity-reservations-first']] = None


class CapacityReservationTargetResponse(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None


class CapacityReservationTarget(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None


class CertificateAuthenticationRequest(BaseValidatorModel):
    ClientRootCertificateChainArn: Optional[str] = None


class CertificateAuthentication(BaseValidatorModel):
    ClientRootCertificateChain: Optional[str] = None


class CidrAuthorizationContext(BaseValidatorModel):
    Message: str
    Signature: str


class CidrBlock(BaseValidatorModel):
    CidrBlock: Optional[str] = None


class ClassicLinkDnsSupport(BaseValidatorModel):
    ClassicLinkDnsSupported: Optional[bool] = None
    VpcId: Optional[str] = None


class GroupIdentifier(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None


class ClassicLoadBalancer(BaseValidatorModel):
    Name: Optional[str] = None


class ClientCertificateRevocationListStatus(BaseValidatorModel):
    Code: Optional[ClientCertificateRevocationListStatusCodeType] = None
    Message: Optional[str] = None


class ClientConnectOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None


class ClientVpnEndpointAttributeStatus(BaseValidatorModel):
    Code: Optional[ClientVpnEndpointAttributeStatusCodeType] = None
    Message: Optional[str] = None


class ClientLoginBannerOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None


class ClientLoginBannerResponseOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None


class DirectoryServiceAuthenticationRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None


class FederatedAuthenticationRequest(BaseValidatorModel):
    SAMLProviderArn: Optional[str] = None
    SelfServiceSAMLProviderArn: Optional[str] = None


class DirectoryServiceAuthentication(BaseValidatorModel):
    DirectoryId: Optional[str] = None


class FederatedAuthentication(BaseValidatorModel):
    SamlProviderArn: Optional[str] = None
    SelfServiceSamlProviderArn: Optional[str] = None


class ClientVpnConnectionStatus(BaseValidatorModel):
    Code: Optional[ClientVpnConnectionStatusCodeType] = None
    Message: Optional[str] = None


class ClientVpnEndpointStatus(BaseValidatorModel):
    Code: Optional[ClientVpnEndpointStatusCodeType] = None
    Message: Optional[str] = None


class ConnectionLogResponseOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None


class ClientVpnRouteStatus(BaseValidatorModel):
    Code: Optional[ClientVpnRouteStatusCodeType] = None
    Message: Optional[str] = None


class CloudWatchLogOptionsSpecification(BaseValidatorModel):
    LogEnabled: Optional[bool] = None
    LogGroupArn: Optional[str] = None
    LogOutputFormat: Optional[str] = None


class CloudWatchLogOptions(BaseValidatorModel):
    LogEnabled: Optional[bool] = None
    LogGroupArn: Optional[str] = None
    LogOutputFormat: Optional[str] = None


class CoipAddressUsage(BaseValidatorModel):
    AllocationId: Optional[str] = None
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    CoIp: Optional[str] = None


class CoipCidr(BaseValidatorModel):
    Cidr: Optional[str] = None
    CoipPoolId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None


# This class is the input for the 'confirm_product_instance' function.
class ConfirmProductInstanceRequest(BaseValidatorModel):
    InstanceId: str
    ProductCode: str
    DryRun: Optional[bool] = None


class ConnectionLogOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None


class ConnectionNotification(BaseValidatorModel):
    ConnectionNotificationId: Optional[str] = None
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    ConnectionNotificationType: Optional[Literal['Topic']] = None
    ConnectionNotificationArn: Optional[str] = None
    ConnectionEvents: Optional[List[str]] = None
    ConnectionNotificationState: Optional[ConnectionNotificationStateType] = None
    ServiceRegion: Optional[str] = None


class ConnectionTrackingConfiguration(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None


class ConnectionTrackingSpecificationRequest(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None


class ConnectionTrackingSpecificationResponse(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None


class ConnectionTrackingSpecification(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None


# This class is the input for the 'copy_fpga_image' function.
class CopyFpgaImageRequest(BaseValidatorModel):
    SourceFpgaImageId: str
    SourceRegion: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None


class CpuOptionsRequest(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None


class CpuOptions(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None


class PerformanceFactorReference(BaseValidatorModel):
    InstanceFamily: Optional[str] = None


class PerformanceFactorReferenceRequest(BaseValidatorModel):
    InstanceFamily: Optional[str] = None


class ReservationFleetInstanceSpecification(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    InstancePlatform: Optional[CapacityReservationInstancePlatformType] = None
    Weight: Optional[float] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    Priority: Optional[int] = None


# This class is the input for the 'create_client_vpn_route' function.
class CreateClientVpnRouteRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    DestinationCidrBlock: str
    TargetVpcSubnetId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_coip_cidr' function.
class CreateCoipCidrRequest(BaseValidatorModel):
    Cidr: str
    CoipPoolId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'create_default_subnet' function.
class CreateDefaultSubnetRequest(BaseValidatorModel):
    AvailabilityZone: str
    DryRun: Optional[bool] = None
    Ipv6Native: Optional[bool] = None


# This class is the input for the 'create_default_vpc' function.
class CreateDefaultVpcRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class NewDhcpConfiguration(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[str]] = None


class TargetCapacitySpecificationRequest(BaseValidatorModel):
    TotalTargetCapacity: int
    OnDemandTargetCapacity: Optional[int] = None
    SpotTargetCapacity: Optional[int] = None
    DefaultTargetCapacityType: Optional[DefaultTargetCapacityTypeType] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None


class DestinationOptionsRequest(BaseValidatorModel):
    FileFormat: Optional[DestinationFileFormatType] = None
    HiveCompatiblePartitions: Optional[bool] = None
    PerHourPartition: Optional[bool] = None


class StorageLocation(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None


class InstanceEventWindowTimeRangeRequest(BaseValidatorModel):
    StartWeekDay: Optional[WeekDayType] = None
    StartHour: Optional[int] = None
    EndWeekDay: Optional[WeekDayType] = None
    EndHour: Optional[int] = None


class ExportToS3TaskSpecification(BaseValidatorModel):
    DiskImageFormat: Optional[DiskImageFormatType] = None
    ContainerFormat: Optional[Literal['ova']] = None
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None


class IpamPoolSourceResourceRequest(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal['vpc']] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None


class RequestIpamResourceTag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class OperatorRequest(BaseValidatorModel):
    Principal: Optional[str] = None


# This class is the input for the 'create_local_gateway_route' function.
class CreateLocalGatewayRouteRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None


class LocalGatewayRoute(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    Type: Optional[LocalGatewayRouteTypeType] = None
    State: Optional[LocalGatewayRouteStateType] = None
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    OwnerId: Optional[str] = None
    SubnetId: Optional[str] = None
    CoipPoolId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None


class IcmpTypeCode(BaseValidatorModel):
    Code: Optional[int] = None
    Type: Optional[int] = None


# This class is the input for the 'create_network_interface_permission' function.
class CreateNetworkInterfacePermissionRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    Permission: InterfacePermissionTypeType
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    DryRun: Optional[bool] = None


class InstanceIpv6Address(BaseValidatorModel):
    Ipv6Address: Optional[str] = None
    IsPrimaryIpv6: Optional[bool] = None


class Ipv4PrefixSpecificationRequest(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None


class Ipv6PrefixSpecificationRequest(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None


class PrivateIpAddressSpecification(BaseValidatorModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None


class PriceScheduleSpecification(BaseValidatorModel):
    Term: Optional[int] = None
    Price: Optional[float] = None
    CurrencyCode: Optional[Literal['USD']] = None


class CreateRouteRequestRouteTableCreateRoute(BaseValidatorModel):
    DestinationPrefixListId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationCidrBlock: Optional[str] = None
    GatewayId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    NatGatewayId: Optional[str] = None


# This class is the input for the 'create_route' function.
class CreateRouteRequest(BaseValidatorModel):
    RouteTableId: str
    DestinationPrefixListId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationCidrBlock: Optional[str] = None
    GatewayId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    NatGatewayId: Optional[str] = None


class InstanceSpecification(BaseValidatorModel):
    InstanceId: str
    ExcludeBootVolume: Optional[bool] = None
    ExcludeDataVolumeIds: Optional[List[str]] = None


# This class is the input for the 'create_spot_datafeed_subscription' function.
class CreateSpotDatafeedSubscriptionRequest(BaseValidatorModel):
    Bucket: str
    DryRun: Optional[bool] = None
    Prefix: Optional[str] = None


class S3ObjectTag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class TrafficMirrorPortRangeRequest(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class TransitGatewayConnectRequestBgpOptions(BaseValidatorModel):
    PeerAsn: Optional[int] = None


class CreateTransitGatewayConnectRequestOptions(BaseValidatorModel):
    Protocol: Literal['gre']


class CreateTransitGatewayMulticastDomainRequestOptions(BaseValidatorModel):
    Igmpv2Support: Optional[Igmpv2SupportValueType] = None
    StaticSourcesSupport: Optional[StaticSourcesSupportValueType] = None
    AutoAcceptSharedAssociations: Optional[AutoAcceptSharedAssociationsValueType] = None


class CreateTransitGatewayPeeringAttachmentRequestOptions(BaseValidatorModel):
    DynamicRouting: Optional[DynamicRoutingValueType] = None


# This class is the input for the 'create_transit_gateway_prefix_list_reference' function.
class CreateTransitGatewayPrefixListReferenceRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None


class TransitGatewayRequestOptions(BaseValidatorModel):
    AmazonSideAsn: Optional[int] = None
    AutoAcceptSharedAttachments: Optional[AutoAcceptSharedAttachmentsValueType] = None
    DefaultRouteTableAssociation: Optional[DefaultRouteTableAssociationValueType] = None
    DefaultRouteTablePropagation: Optional[DefaultRouteTablePropagationValueType] = None
    VpnEcmpSupport: Optional[VpnEcmpSupportValueType] = None
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    MulticastSupport: Optional[MulticastSupportValueType] = None
    TransitGatewayCidrBlocks: Optional[List[str]] = None


# This class is the input for the 'create_transit_gateway_route' function.
class CreateTransitGatewayRouteRequest(BaseValidatorModel):
    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None


class CreateTransitGatewayVpcAttachmentRequestOptions(BaseValidatorModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None


class CreateVerifiedAccessEndpointPortRange(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class CreateVerifiedAccessEndpointRdsOptions(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    RdsDbInstanceArn: Optional[str] = None
    RdsDbClusterArn: Optional[str] = None
    RdsDbProxyArn: Optional[str] = None
    RdsEndpoint: Optional[str] = None
    SubnetIds: Optional[List[str]] = None


class VerifiedAccessSseSpecificationRequest(BaseValidatorModel):
    CustomerManagedKeyEnabled: Optional[bool] = None
    KmsKeyArn: Optional[str] = None


class CreateVerifiedAccessNativeApplicationOidcOptions(BaseValidatorModel):
    PublicSigningKeyEndpoint: Optional[str] = None
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None


class CreateVerifiedAccessTrustProviderDeviceOptions(BaseValidatorModel):
    TenantId: Optional[str] = None
    PublicSigningKeyUrl: Optional[str] = None


class CreateVerifiedAccessTrustProviderOidcOptions(BaseValidatorModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None


class CreateVolumePermission(BaseValidatorModel):
    UserId: Optional[str] = None
    Group: Optional[Literal['all']] = None


# This class is the input for the 'create_vpc_endpoint_connection_notification' function.
class CreateVpcEndpointConnectionNotificationRequest(BaseValidatorModel):
    ConnectionNotificationArn: str
    ConnectionEvents: List[str]
    DryRun: Optional[bool] = None
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    ClientToken: Optional[str] = None


class DnsOptionsSpecification(BaseValidatorModel):
    DnsRecordIpType: Optional[DnsRecordIpTypeType] = None
    PrivateDnsOnlyForInboundResolverEndpoint: Optional[bool] = None


class SubnetConfiguration(BaseValidatorModel):
    SubnetId: Optional[str] = None
    Ipv4: Optional[str] = None
    Ipv6: Optional[str] = None


# This class is the input for the 'create_vpn_connection_route' function.
class CreateVpnConnectionRouteRequest(BaseValidatorModel):
    DestinationCidrBlock: str
    VpnConnectionId: str


class CreditSpecificationRequest(BaseValidatorModel):
    CpuCredits: str


class CreditSpecification(BaseValidatorModel):
    CpuCredits: Optional[str] = None


class DataQuery(BaseValidatorModel):
    Id: Optional[str] = None
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal['aggregate-latency']] = None
    Statistic: Optional[Literal['p50']] = None
    Period: Optional[PeriodTypeType] = None


class MetricPoint(BaseValidatorModel):
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    Value: Optional[float] = None
    Status: Optional[str] = None


# This class is the input for the 'delete_carrier_gateway' function.
class DeleteCarrierGatewayRequest(BaseValidatorModel):
    CarrierGatewayId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_client_vpn_endpoint' function.
class DeleteClientVpnEndpointRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_client_vpn_route' function.
class DeleteClientVpnRouteRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    DestinationCidrBlock: str
    TargetVpcSubnetId: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_coip_cidr' function.
class DeleteCoipCidrRequest(BaseValidatorModel):
    Cidr: str
    CoipPoolId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_coip_pool' function.
class DeleteCoipPoolRequest(BaseValidatorModel):
    CoipPoolId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_customer_gateway' function.
class DeleteCustomerGatewayRequest(BaseValidatorModel):
    CustomerGatewayId: str
    DryRun: Optional[bool] = None


class DeleteDhcpOptionsRequestDhcpOptionsDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_dhcp_options' function.
class DeleteDhcpOptionsRequest(BaseValidatorModel):
    DhcpOptionsId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_egress_only_internet_gateway' function.
class DeleteEgressOnlyInternetGatewayRequest(BaseValidatorModel):
    EgressOnlyInternetGatewayId: str
    DryRun: Optional[bool] = None


class DeleteFleetError(BaseValidatorModel):
    Code: Optional[DeleteFleetErrorCodeType] = None
    Message: Optional[str] = None


class DeleteFleetSuccessItem(BaseValidatorModel):
    CurrentFleetState: Optional[FleetStateCodeType] = None
    PreviousFleetState: Optional[FleetStateCodeType] = None
    FleetId: Optional[str] = None


# This class is the input for the 'delete_fleets' function.
class DeleteFleetsRequest(BaseValidatorModel):
    FleetIds: List[str]
    TerminateInstances: bool
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_flow_logs' function.
class DeleteFlowLogsRequest(BaseValidatorModel):
    FlowLogIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_fpga_image' function.
class DeleteFpgaImageRequest(BaseValidatorModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_instance_connect_endpoint' function.
class DeleteInstanceConnectEndpointRequest(BaseValidatorModel):
    InstanceConnectEndpointId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_instance_event_window' function.
class DeleteInstanceEventWindowRequest(BaseValidatorModel):
    InstanceEventWindowId: str
    DryRun: Optional[bool] = None
    ForceDelete: Optional[bool] = None


class InstanceEventWindowStateChange(BaseValidatorModel):
    InstanceEventWindowId: Optional[str] = None
    State: Optional[InstanceEventWindowStateType] = None


class DeleteInternetGatewayRequestInternetGatewayDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_internet_gateway' function.
class DeleteInternetGatewayRequest(BaseValidatorModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_ipam_external_resource_verification_token' function.
class DeleteIpamExternalResourceVerificationTokenRequest(BaseValidatorModel):
    IpamExternalResourceVerificationTokenId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_ipam_pool' function.
class DeleteIpamPoolRequest(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cascade: Optional[bool] = None


# This class is the input for the 'delete_ipam' function.
class DeleteIpamRequest(BaseValidatorModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Cascade: Optional[bool] = None


# This class is the input for the 'delete_ipam_resource_discovery' function.
class DeleteIpamResourceDiscoveryRequest(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_ipam_scope' function.
class DeleteIpamScopeRequest(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None


class DeleteKeyPairRequestKeyPairDelete(BaseValidatorModel):
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None


class DeleteKeyPairRequestKeyPairInfoDelete(BaseValidatorModel):
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_key_pair' function.
class DeleteKeyPairRequest(BaseValidatorModel):
    KeyName: Optional[str] = None
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_launch_template' function.
class DeleteLaunchTemplateRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None


# This class is the input for the 'delete_launch_template_versions' function.
class DeleteLaunchTemplateVersionsRequest(BaseValidatorModel):
    Versions: List[str]
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None


class ResponseError(BaseValidatorModel):
    Code: Optional[LaunchTemplateErrorCodeType] = None
    Message: Optional[str] = None


class DeleteLaunchTemplateVersionsResponseSuccessItem(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None


# This class is the input for the 'delete_local_gateway_route' function.
class DeleteLocalGatewayRouteRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationPrefixListId: Optional[str] = None


# This class is the input for the 'delete_local_gateway_route_table' function.
class DeleteLocalGatewayRouteTableRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DryRun: Optional[bool] = None


class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_local_gateway_route_table_vpc_association' function.
class DeleteLocalGatewayRouteTableVpcAssociationRequest(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_managed_prefix_list' function.
class DeleteManagedPrefixListRequest(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_nat_gateway' function.
class DeleteNatGatewayRequest(BaseValidatorModel):
    NatGatewayId: str
    DryRun: Optional[bool] = None


class DeleteNetworkAclEntryRequestNetworkAclDeleteEntry(BaseValidatorModel):
    RuleNumber: int
    Egress: bool
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_acl_entry' function.
class DeleteNetworkAclEntryRequest(BaseValidatorModel):
    NetworkAclId: str
    RuleNumber: int
    Egress: bool
    DryRun: Optional[bool] = None


class DeleteNetworkAclRequestNetworkAclDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_acl' function.
class DeleteNetworkAclRequest(BaseValidatorModel):
    NetworkAclId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_insights_access_scope_analysis' function.
class DeleteNetworkInsightsAccessScopeAnalysisRequest(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_insights_access_scope' function.
class DeleteNetworkInsightsAccessScopeRequest(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_insights_analysis' function.
class DeleteNetworkInsightsAnalysisRequest(BaseValidatorModel):
    NetworkInsightsAnalysisId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_insights_path' function.
class DeleteNetworkInsightsPathRequest(BaseValidatorModel):
    NetworkInsightsPathId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_interface_permission' function.
class DeleteNetworkInterfacePermissionRequest(BaseValidatorModel):
    NetworkInterfacePermissionId: str
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None


class DeleteNetworkInterfaceRequestNetworkInterfaceDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_network_interface' function.
class DeleteNetworkInterfaceRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None


class DeletePlacementGroupRequestPlacementGroupDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_placement_group' function.
class DeletePlacementGroupRequest(BaseValidatorModel):
    GroupName: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_public_ipv4_pool' function.
class DeletePublicIpv4PoolRequest(BaseValidatorModel):
    PoolId: str
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None


class DeleteQueuedReservedInstancesError(BaseValidatorModel):
    Code: Optional[DeleteQueuedReservedInstancesErrorCodeType] = None
    Message: Optional[str] = None


# This class is the input for the 'delete_queued_reserved_instances' function.
class DeleteQueuedReservedInstancesRequest(BaseValidatorModel):
    ReservedInstancesIds: List[str]
    DryRun: Optional[bool] = None


class SuccessfulQueuedPurchaseDeletion(BaseValidatorModel):
    ReservedInstancesId: Optional[str] = None


class DeleteRouteRequestRouteDelete(BaseValidatorModel):
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationIpv6CidrBlock: Optional[str] = None


# This class is the input for the 'delete_route' function.
class DeleteRouteRequest(BaseValidatorModel):
    RouteTableId: str
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None


class DeleteRouteTableRequestRouteTableDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_route_table' function.
class DeleteRouteTableRequest(BaseValidatorModel):
    RouteTableId: str
    DryRun: Optional[bool] = None


class DeleteSecurityGroupRequestSecurityGroupDelete(BaseValidatorModel):
    GroupName: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_security_group' function.
class DeleteSecurityGroupRequest(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    DryRun: Optional[bool] = None


class DeleteSnapshotRequestSnapshotDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_snapshot' function.
class DeleteSnapshotRequest(BaseValidatorModel):
    SnapshotId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_spot_datafeed_subscription' function.
class DeleteSpotDatafeedSubscriptionRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_subnet_cidr_reservation' function.
class DeleteSubnetCidrReservationRequest(BaseValidatorModel):
    SubnetCidrReservationId: str
    DryRun: Optional[bool] = None


class DeleteSubnetRequestSubnetDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_subnet' function.
class DeleteSubnetRequest(BaseValidatorModel):
    SubnetId: str
    DryRun: Optional[bool] = None


class DeleteTagsRequestTagDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_traffic_mirror_filter' function.
class DeleteTrafficMirrorFilterRequest(BaseValidatorModel):
    TrafficMirrorFilterId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_traffic_mirror_filter_rule' function.
class DeleteTrafficMirrorFilterRuleRequest(BaseValidatorModel):
    TrafficMirrorFilterRuleId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_traffic_mirror_session' function.
class DeleteTrafficMirrorSessionRequest(BaseValidatorModel):
    TrafficMirrorSessionId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_traffic_mirror_target' function.
class DeleteTrafficMirrorTargetRequest(BaseValidatorModel):
    TrafficMirrorTargetId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_connect_peer' function.
class DeleteTransitGatewayConnectPeerRequest(BaseValidatorModel):
    TransitGatewayConnectPeerId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_connect' function.
class DeleteTransitGatewayConnectRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_multicast_domain' function.
class DeleteTransitGatewayMulticastDomainRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_peering_attachment' function.
class DeleteTransitGatewayPeeringAttachmentRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_policy_table' function.
class DeleteTransitGatewayPolicyTableRequest(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_prefix_list_reference' function.
class DeleteTransitGatewayPrefixListReferenceRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway' function.
class DeleteTransitGatewayRequest(BaseValidatorModel):
    TransitGatewayId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_route' function.
class DeleteTransitGatewayRouteRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    DestinationCidrBlock: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_route_table_announcement' function.
class DeleteTransitGatewayRouteTableAnnouncementRequest(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncementId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_route_table' function.
class DeleteTransitGatewayRouteTableRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_transit_gateway_vpc_attachment' function.
class DeleteTransitGatewayVpcAttachmentRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_verified_access_endpoint' function.
class DeleteVerifiedAccessEndpointRequest(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_verified_access_group' function.
class DeleteVerifiedAccessGroupRequest(BaseValidatorModel):
    VerifiedAccessGroupId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_verified_access_instance' function.
class DeleteVerifiedAccessInstanceRequest(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'delete_verified_access_trust_provider' function.
class DeleteVerifiedAccessTrustProviderRequest(BaseValidatorModel):
    VerifiedAccessTrustProviderId: str
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'delete_volume' function.
class DeleteVolumeRequest(BaseValidatorModel):
    VolumeId: str
    DryRun: Optional[bool] = None


class DeleteVolumeRequestVolumeDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpc_block_public_access_exclusion' function.
class DeleteVpcBlockPublicAccessExclusionRequest(BaseValidatorModel):
    ExclusionId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpc_endpoint_connection_notifications' function.
class DeleteVpcEndpointConnectionNotificationsRequest(BaseValidatorModel):
    ConnectionNotificationIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpc_endpoint_service_configurations' function.
class DeleteVpcEndpointServiceConfigurationsRequest(BaseValidatorModel):
    ServiceIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpc_endpoints' function.
class DeleteVpcEndpointsRequest(BaseValidatorModel):
    VpcEndpointIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpc_peering_connection' function.
class DeleteVpcPeeringConnectionRequest(BaseValidatorModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None


class DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpc' function.
class DeleteVpcRequest(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None


class DeleteVpcRequestVpcDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpn_connection' function.
class DeleteVpnConnectionRequest(BaseValidatorModel):
    VpnConnectionId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_vpn_connection_route' function.
class DeleteVpnConnectionRouteRequest(BaseValidatorModel):
    DestinationCidrBlock: str
    VpnConnectionId: str


# This class is the input for the 'delete_vpn_gateway' function.
class DeleteVpnGatewayRequest(BaseValidatorModel):
    VpnGatewayId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'deprovision_byoip_cidr' function.
class DeprovisionByoipCidrRequest(BaseValidatorModel):
    Cidr: str
    DryRun: Optional[bool] = None


# This class is the input for the 'deprovision_ipam_byoasn' function.
class DeprovisionIpamByoasnRequest(BaseValidatorModel):
    IpamId: str
    Asn: str
    DryRun: Optional[bool] = None


# This class is the input for the 'deprovision_ipam_pool_cidr' function.
class DeprovisionIpamPoolCidrRequest(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None


# This class is the input for the 'deprovision_public_ipv4_pool_cidr' function.
class DeprovisionPublicIpv4PoolCidrRequest(BaseValidatorModel):
    PoolId: str
    Cidr: str
    DryRun: Optional[bool] = None


class DeregisterImageRequestImageDeregister(BaseValidatorModel):
    DryRun: Optional[bool] = None


class DeregisterImageRequest(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None


class DeregisterInstanceTagAttributeRequest(BaseValidatorModel):
    IncludeAllTagsOfInstance: Optional[bool] = None
    InstanceTagKeys: Optional[List[str]] = None


class InstanceTagNotificationAttribute(BaseValidatorModel):
    InstanceTagKeys: Optional[List[str]] = None
    IncludeAllTagsOfInstance: Optional[bool] = None


# This class is the input for the 'deregister_transit_gateway_multicast_group_members' function.
class DeregisterTransitGatewayMulticastGroupMembersRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    GroupIpAddress: Optional[str] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class TransitGatewayMulticastDeregisteredGroupMembers(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    DeregisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None


# This class is the input for the 'deregister_transit_gateway_multicast_group_sources' function.
class DeregisterTransitGatewayMulticastGroupSourcesRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    GroupIpAddress: Optional[str] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class TransitGatewayMulticastDeregisteredGroupSources(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    DeregisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None


# This class is the input for the 'describe_account_attributes' function.
class DescribeAccountAttributesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    AttributeNames: Optional[List[AccountAttributeNameType]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_address_transfers' function.
class DescribeAddressTransfersRequest(BaseValidatorModel):
    AllocationIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_addresses_attribute' function.
class DescribeAddressesAttributeRequest(BaseValidatorModel):
    AllocationIds: Optional[List[str]] = None
    Attribute: Optional[Literal['domain-name']] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


class Filter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[List[str]] = None


# This class is the input for the 'describe_aggregate_id_format' function.
class DescribeAggregateIdFormatRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class IdFormat(BaseValidatorModel):
    Deadline: Optional[datetime] = None
    Resource: Optional[str] = None
    UseLongIds: Optional[bool] = None


class Subscription(BaseValidatorModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal['aggregate-latency']] = None
    Statistic: Optional[Literal['p50']] = None
    Period: Optional[PeriodTypeType] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_byoip_cidrs' function.
class DescribeByoipCidrsRequest(BaseValidatorModel):
    MaxResults: int
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_capacity_block_extension_offerings' function.
class DescribeCapacityBlockExtensionOfferingsRequest(BaseValidatorModel):
    CapacityBlockExtensionDurationHours: int
    CapacityReservationId: str
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_conversion_tasks' function.
class DescribeConversionTasksRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConversionTaskIds: Optional[List[str]] = None


# This class is the input for the 'describe_declarative_policies_reports' function.
class DescribeDeclarativePoliciesReportsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ReportIds: Optional[List[str]] = None


class FastLaunchLaunchTemplateSpecificationResponse(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class FastLaunchSnapshotConfigurationResponse(BaseValidatorModel):
    TargetResourceCount: Optional[int] = None


class DescribeFastSnapshotRestoreSuccessItem(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    State: Optional[FastSnapshotRestoreStateCodeType] = None
    StateTransitionReason: Optional[str] = None
    OwnerId: Optional[str] = None
    OwnerAlias: Optional[str] = None
    EnablingTime: Optional[datetime] = None
    OptimizingTime: Optional[datetime] = None
    EnabledTime: Optional[datetime] = None
    DisablingTime: Optional[datetime] = None
    DisabledTime: Optional[datetime] = None


# This class is the input for the 'describe_fpga_image_attribute' function.
class DescribeFpgaImageAttributeRequest(BaseValidatorModel):
    FpgaImageId: str
    Attribute: FpgaImageAttributeNameType
    DryRun: Optional[bool] = None


class HostOffering(BaseValidatorModel):
    CurrencyCode: Optional[Literal['USD']] = None
    Duration: Optional[int] = None
    HourlyPrice: Optional[str] = None
    InstanceFamily: Optional[str] = None
    OfferingId: Optional[str] = None
    PaymentOption: Optional[PaymentOptionType] = None
    UpfrontPrice: Optional[str] = None


# This class is the input for the 'describe_id_format' function.
class DescribeIdFormatRequest(BaseValidatorModel):
    Resource: Optional[str] = None


# This class is the input for the 'describe_identity_id_format' function.
class DescribeIdentityIdFormatRequest(BaseValidatorModel):
    PrincipalArn: str
    Resource: Optional[str] = None


class DescribeImageAttributeRequestImageDescribeAttribute(BaseValidatorModel):
    Attribute: ImageAttributeNameType
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_image_attribute' function.
class DescribeImageAttributeRequest(BaseValidatorModel):
    Attribute: ImageAttributeNameType
    ImageId: str
    DryRun: Optional[bool] = None


class DescribeInstanceAttributeRequestInstanceDescribeAttribute(BaseValidatorModel):
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_instance_attribute' function.
class DescribeInstanceAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None


class InstanceCreditSpecification(BaseValidatorModel):
    InstanceId: Optional[str] = None
    CpuCredits: Optional[str] = None


# This class is the input for the 'describe_instance_event_notification_attributes' function.
class DescribeInstanceEventNotificationAttributesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class InstanceTopology(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    GroupName: Optional[str] = None
    NetworkNodes: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None
    ZoneId: Optional[str] = None


class InstanceTypeOffering(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    LocationType: Optional[LocationTypeType] = None
    Location: Optional[str] = None


# This class is the input for the 'describe_ipam_byoasn' function.
class DescribeIpamByoasnRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LockedSnapshotsInfo(BaseValidatorModel):
    OwnerId: Optional[str] = None
    SnapshotId: Optional[str] = None
    LockState: Optional[LockStateType] = None
    LockDuration: Optional[int] = None
    CoolOffPeriod: Optional[int] = None
    CoolOffPeriodExpiresOn: Optional[datetime] = None
    LockCreatedOn: Optional[datetime] = None
    LockDurationStartTime: Optional[datetime] = None
    LockExpiresOn: Optional[datetime] = None


class MacHost(BaseValidatorModel):
    HostId: Optional[str] = None
    MacOSLatestSupportedVersions: Optional[List[str]] = None


class MovingAddressStatus(BaseValidatorModel):
    MoveStatus: Optional[MoveStatusType] = None
    PublicIp: Optional[str] = None


class DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttribute(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Attribute: Optional[NetworkInterfaceAttributeType] = None


# This class is the input for the 'describe_network_interface_attribute' function.
class DescribeNetworkInterfaceAttributeRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None
    Attribute: Optional[NetworkInterfaceAttributeType] = None


class PrefixList(BaseValidatorModel):
    Cidrs: Optional[List[str]] = None
    PrefixListId: Optional[str] = None
    PrefixListName: Optional[str] = None


# This class is the input for the 'describe_principal_id_format' function.
class DescribePrincipalIdFormatRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Resources: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Region(BaseValidatorModel):
    OptInStatus: Optional[str] = None
    RegionName: Optional[str] = None
    Endpoint: Optional[str] = None


class ScheduledInstanceRecurrenceRequest(BaseValidatorModel):
    Frequency: Optional[str] = None
    Interval: Optional[int] = None
    OccurrenceDays: Optional[List[int]] = None
    OccurrenceRelativeToEnd: Optional[bool] = None
    OccurrenceUnit: Optional[str] = None


# This class is the input for the 'describe_security_group_references' function.
class DescribeSecurityGroupReferencesRequest(BaseValidatorModel):
    GroupId: List[str]
    DryRun: Optional[bool] = None


class SecurityGroupReference(BaseValidatorModel):
    GroupId: Optional[str] = None
    ReferencingVpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    TransitGatewayId: Optional[str] = None


class SecurityGroupVpcAssociation(BaseValidatorModel):
    GroupId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcOwnerId: Optional[str] = None
    State: Optional[SecurityGroupVpcAssociationStateType] = None
    StateReason: Optional[str] = None


class DescribeSnapshotAttributeRequestSnapshotDescribeAttribute(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_snapshot_attribute' function.
class DescribeSnapshotAttributeRequest(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    SnapshotId: str
    DryRun: Optional[bool] = None


class ProductCode(BaseValidatorModel):
    ProductCodeId: Optional[str] = None
    ProductCodeType: Optional[ProductCodeValuesType] = None


# This class is the input for the 'describe_spot_datafeed_subscription' function.
class DescribeSpotDatafeedSubscriptionRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_spot_fleet_instances' function.
class DescribeSpotFleetInstancesRequest(BaseValidatorModel):
    SpotFleetRequestId: str
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_spot_fleet_requests' function.
class DescribeSpotFleetRequestsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    SpotFleetRequestIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SpotPrice(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    SpotPrice: Optional[str] = None
    Timestamp: Optional[datetime] = None


# This class is the input for the 'describe_stale_security_groups' function.
class DescribeStaleSecurityGroupsRequest(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class StoreImageTaskResult(BaseValidatorModel):
    AmiId: Optional[str] = None
    TaskStartTime: Optional[datetime] = None
    Bucket: Optional[str] = None
    S3objectKey: Optional[str] = None
    ProgressPercentage: Optional[int] = None
    StoreTaskState: Optional[str] = None
    StoreTaskFailureReason: Optional[str] = None


class TagDescription(BaseValidatorModel):
    Key: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    Value: Optional[str] = None


# This class is the input for the 'describe_volume_attribute' function.
class DescribeVolumeAttributeRequest(BaseValidatorModel):
    Attribute: VolumeAttributeNameType
    VolumeId: str
    DryRun: Optional[bool] = None


class DescribeVolumeAttributeRequestVolumeDescribeAttribute(BaseValidatorModel):
    Attribute: VolumeAttributeNameType
    DryRun: Optional[bool] = None


class VolumeModification(BaseValidatorModel):
    VolumeId: Optional[str] = None
    ModificationState: Optional[VolumeModificationStateType] = None
    StatusMessage: Optional[str] = None
    TargetSize: Optional[int] = None
    TargetIops: Optional[int] = None
    TargetVolumeType: Optional[VolumeTypeType] = None
    TargetThroughput: Optional[int] = None
    TargetMultiAttachEnabled: Optional[bool] = None
    OriginalSize: Optional[int] = None
    OriginalIops: Optional[int] = None
    OriginalVolumeType: Optional[VolumeTypeType] = None
    OriginalThroughput: Optional[int] = None
    OriginalMultiAttachEnabled: Optional[bool] = None
    Progress: Optional[int] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


# This class is the input for the 'describe_vpc_attribute' function.
class DescribeVpcAttributeRequest(BaseValidatorModel):
    Attribute: VpcAttributeNameType
    VpcId: str
    DryRun: Optional[bool] = None


class DescribeVpcAttributeRequestVpcDescribeAttribute(BaseValidatorModel):
    Attribute: VpcAttributeNameType
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_vpc_block_public_access_options' function.
class DescribeVpcBlockPublicAccessOptionsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class VpcBlockPublicAccessOptions(BaseValidatorModel):
    AwsAccountId: Optional[str] = None
    AwsRegion: Optional[str] = None
    State: Optional[VpcBlockPublicAccessStateType] = None
    InternetGatewayBlockMode: Optional[InternetGatewayBlockModeType] = None
    Reason: Optional[str] = None
    LastUpdateTimestamp: Optional[datetime] = None
    ManagedBy: Optional[ManagedByType] = None
    ExclusionsAllowed: Optional[VpcBlockPublicAccessExclusionsAllowedType] = None


# This class is the input for the 'describe_vpc_classic_link_dns_support' function.
class DescribeVpcClassicLinkDnsSupportRequest(BaseValidatorModel):
    VpcIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DestinationOptionsResponse(BaseValidatorModel):
    FileFormat: Optional[DestinationFileFormatType] = None
    HiveCompatiblePartitions: Optional[bool] = None
    PerHourPartition: Optional[bool] = None


class DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpc(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'detach_classic_link_vpc' function.
class DetachClassicLinkVpcRequest(BaseValidatorModel):
    InstanceId: str
    VpcId: str
    DryRun: Optional[bool] = None


class DetachClassicLinkVpcRequestVpcDetachClassicLinkInstance(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None


class DetachInternetGatewayRequestInternetGatewayDetachFromVpc(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'detach_internet_gateway' function.
class DetachInternetGatewayRequest(BaseValidatorModel):
    InternetGatewayId: str
    VpcId: str
    DryRun: Optional[bool] = None


class DetachInternetGatewayRequestVpcDetachInternetGateway(BaseValidatorModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None


class DetachNetworkInterfaceRequestNetworkInterfaceDetach(BaseValidatorModel):
    AttachmentId: str
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None


# This class is the input for the 'detach_network_interface' function.
class DetachNetworkInterfaceRequest(BaseValidatorModel):
    AttachmentId: str
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None


# This class is the input for the 'detach_verified_access_trust_provider' function.
class DetachVerifiedAccessTrustProviderRequest(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    VerifiedAccessTrustProviderId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DetachVolumeRequestInstanceDetachVolume(BaseValidatorModel):
    VolumeId: str
    Device: Optional[str] = None
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'detach_volume' function.
class DetachVolumeRequest(BaseValidatorModel):
    VolumeId: str
    Device: Optional[str] = None
    Force: Optional[bool] = None
    InstanceId: Optional[str] = None
    DryRun: Optional[bool] = None


class DetachVolumeRequestVolumeDetachFromInstance(BaseValidatorModel):
    Device: Optional[str] = None
    Force: Optional[bool] = None
    InstanceId: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'detach_vpn_gateway' function.
class DetachVpnGatewayRequest(BaseValidatorModel):
    VpcId: str
    VpnGatewayId: str
    DryRun: Optional[bool] = None


class DeviceOptions(BaseValidatorModel):
    TenantId: Optional[str] = None
    PublicSigningKeyUrl: Optional[str] = None


# This class is the input for the 'disable_address_transfer' function.
class DisableAddressTransferRequest(BaseValidatorModel):
    AllocationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_allowed_images_settings' function.
class DisableAllowedImagesSettingsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_aws_network_performance_metric_subscription' function.
class DisableAwsNetworkPerformanceMetricSubscriptionRequest(BaseValidatorModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal['aggregate-latency']] = None
    Statistic: Optional[Literal['p50']] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_ebs_encryption_by_default' function.
class DisableEbsEncryptionByDefaultRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_fast_launch' function.
class DisableFastLaunchRequest(BaseValidatorModel):
    ImageId: str
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None


class DisableFastSnapshotRestoreStateError(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class DisableFastSnapshotRestoreSuccessItem(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    State: Optional[FastSnapshotRestoreStateCodeType] = None
    StateTransitionReason: Optional[str] = None
    OwnerId: Optional[str] = None
    OwnerAlias: Optional[str] = None
    EnablingTime: Optional[datetime] = None
    OptimizingTime: Optional[datetime] = None
    EnabledTime: Optional[datetime] = None
    DisablingTime: Optional[datetime] = None
    DisabledTime: Optional[datetime] = None


# This class is the input for the 'disable_fast_snapshot_restores' function.
class DisableFastSnapshotRestoresRequest(BaseValidatorModel):
    AvailabilityZones: List[str]
    SourceSnapshotIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_image_block_public_access' function.
class DisableImageBlockPublicAccessRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_image_deprecation' function.
class DisableImageDeprecationRequest(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_image_deregistration_protection' function.
class DisableImageDeregistrationProtectionRequest(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_image' function.
class DisableImageRequest(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_ipam_organization_admin_account' function.
class DisableIpamOrganizationAdminAccountRequest(BaseValidatorModel):
    DelegatedAdminAccountId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_serial_console_access' function.
class DisableSerialConsoleAccessRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_snapshot_block_public_access' function.
class DisableSnapshotBlockPublicAccessRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_transit_gateway_route_table_propagation' function.
class DisableTransitGatewayRouteTablePropagationRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    DryRun: Optional[bool] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None


class TransitGatewayPropagation(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayPropagationStateType] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None


# This class is the input for the 'disable_vgw_route_propagation' function.
class DisableVgwRoutePropagationRequest(BaseValidatorModel):
    GatewayId: str
    RouteTableId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disable_vpc_classic_link_dns_support' function.
class DisableVpcClassicLinkDnsSupportRequest(BaseValidatorModel):
    VpcId: Optional[str] = None


# This class is the input for the 'disable_vpc_classic_link' function.
class DisableVpcClassicLinkRequest(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None


class DisableVpcClassicLinkRequestVpcDisableClassicLink(BaseValidatorModel):
    DryRun: Optional[bool] = None


class DisassociateAddressRequestClassicAddressDisassociate(BaseValidatorModel):
    AssociationId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None


class DisassociateAddressRequestNetworkInterfaceAssociationDelete(BaseValidatorModel):
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_address' function.
class DisassociateAddressRequest(BaseValidatorModel):
    AssociationId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_capacity_reservation_billing_owner' function.
class DisassociateCapacityReservationBillingOwnerRequest(BaseValidatorModel):
    CapacityReservationId: str
    UnusedReservationBillingOwnerId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_client_vpn_target_network' function.
class DisassociateClientVpnTargetNetworkRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    AssociationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_enclave_certificate_iam_role' function.
class DisassociateEnclaveCertificateIamRoleRequest(BaseValidatorModel):
    CertificateArn: str
    RoleArn: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_iam_instance_profile' function.
class DisassociateIamInstanceProfileRequest(BaseValidatorModel):
    AssociationId: str


# This class is the input for the 'disassociate_ipam_byoasn' function.
class DisassociateIpamByoasnRequest(BaseValidatorModel):
    Asn: str
    Cidr: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_ipam_resource_discovery' function.
class DisassociateIpamResourceDiscoveryRequest(BaseValidatorModel):
    IpamResourceDiscoveryAssociationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_nat_gateway_address' function.
class DisassociateNatGatewayAddressRequest(BaseValidatorModel):
    NatGatewayId: str
    AssociationIds: List[str]
    MaxDrainDurationSeconds: Optional[int] = None
    DryRun: Optional[bool] = None


class DisassociateRouteTableRequestRouteTableAssociationDelete(BaseValidatorModel):
    DryRun: Optional[bool] = None


class DisassociateRouteTableRequestServiceResourceDisassociateRouteTable(BaseValidatorModel):
    AssociationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_route_table' function.
class DisassociateRouteTableRequest(BaseValidatorModel):
    AssociationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_security_group_vpc' function.
class DisassociateSecurityGroupVpcRequest(BaseValidatorModel):
    GroupId: str
    VpcId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_subnet_cidr_block' function.
class DisassociateSubnetCidrBlockRequest(BaseValidatorModel):
    AssociationId: str


# This class is the input for the 'disassociate_transit_gateway_multicast_domain' function.
class DisassociateTransitGatewayMulticastDomainRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    TransitGatewayAttachmentId: str
    SubnetIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_transit_gateway_policy_table' function.
class DisassociateTransitGatewayPolicyTableRequest(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_transit_gateway_route_table' function.
class DisassociateTransitGatewayRouteTableRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_trunk_interface' function.
class DisassociateTrunkInterfaceRequest(BaseValidatorModel):
    AssociationId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'disassociate_vpc_cidr_block' function.
class DisassociateVpcCidrBlockRequest(BaseValidatorModel):
    AssociationId: str


class DiskImageDescription(BaseValidatorModel):
    Checksum: Optional[str] = None
    Format: Optional[DiskImageFormatType] = None
    ImportManifestUrl: Optional[str] = None
    Size: Optional[int] = None


class DiskImageDetail(BaseValidatorModel):
    Format: DiskImageFormatType
    Bytes: int
    ImportManifestUrl: str


class VolumeDetail(BaseValidatorModel):
    Size: int


class DiskImageVolumeDescription(BaseValidatorModel):
    Id: Optional[str] = None
    Size: Optional[int] = None


class DiskInfo(BaseValidatorModel):
    SizeInGB: Optional[int] = None
    Count: Optional[int] = None
    Type: Optional[DiskTypeType] = None


class DnsEntry(BaseValidatorModel):
    DnsName: Optional[str] = None
    HostedZoneId: Optional[str] = None


class DnsOptions(BaseValidatorModel):
    DnsRecordIpType: Optional[DnsRecordIpTypeType] = None
    PrivateDnsOnlyForInboundResolverEndpoint: Optional[bool] = None


class DnsServersOptionsModifyStructure(BaseValidatorModel):
    CustomDnsServers: Optional[List[str]] = None
    Enabled: Optional[bool] = None


class EbsOptimizedInfo(BaseValidatorModel):
    BaselineBandwidthInMbps: Optional[int] = None
    BaselineThroughputInMBps: Optional[float] = None
    BaselineIops: Optional[int] = None
    MaximumBandwidthInMbps: Optional[int] = None
    MaximumThroughputInMBps: Optional[float] = None
    MaximumIops: Optional[int] = None


class EbsInstanceBlockDeviceSpecification(BaseValidatorModel):
    VolumeId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None


class OperatorResponse(BaseValidatorModel):
    Managed: Optional[bool] = None
    Principal: Optional[str] = None


class EbsStatusDetails(BaseValidatorModel):
    ImpairedSince: Optional[datetime] = None
    Name: Optional[Literal['reachability']] = None
    Status: Optional[StatusTypeType] = None


class EfaInfo(BaseValidatorModel):
    MaximumEfaInterfaces: Optional[int] = None


class InternetGatewayAttachment(BaseValidatorModel):
    State: Optional[AttachmentStatusType] = None
    VpcId: Optional[str] = None


class ElasticGpuAssociation(BaseValidatorModel):
    ElasticGpuId: Optional[str] = None
    ElasticGpuAssociationId: Optional[str] = None
    ElasticGpuAssociationState: Optional[str] = None
    ElasticGpuAssociationTime: Optional[str] = None


class ElasticGpuHealth(BaseValidatorModel):
    Status: Optional[ElasticGpuStatusType] = None


class ElasticGpuSpecificationResponse(BaseValidatorModel):
    Type: Optional[str] = None


class ElasticGpuSpecification(BaseValidatorModel):
    Type: str


class ElasticInferenceAcceleratorAssociation(BaseValidatorModel):
    ElasticInferenceAcceleratorArn: Optional[str] = None
    ElasticInferenceAcceleratorAssociationId: Optional[str] = None
    ElasticInferenceAcceleratorAssociationState: Optional[str] = None
    ElasticInferenceAcceleratorAssociationTime: Optional[datetime] = None


class ElasticInferenceAccelerator(BaseValidatorModel):
    Type: str
    Count: Optional[int] = None


class EnaSrdUdpSpecificationRequest(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None


class EnaSrdUdpSpecification(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None


# This class is the input for the 'enable_address_transfer' function.
class EnableAddressTransferRequest(BaseValidatorModel):
    AllocationId: str
    TransferAccountId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_allowed_images_settings' function.
class EnableAllowedImagesSettingsRequest(BaseValidatorModel):
    AllowedImagesSettingsState: AllowedImagesSettingsEnabledStateType
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_aws_network_performance_metric_subscription' function.
class EnableAwsNetworkPerformanceMetricSubscriptionRequest(BaseValidatorModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal['aggregate-latency']] = None
    Statistic: Optional[Literal['p50']] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_ebs_encryption_by_default' function.
class EnableEbsEncryptionByDefaultRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class FastLaunchLaunchTemplateSpecificationRequest(BaseValidatorModel):
    Version: str
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None


class FastLaunchSnapshotConfigurationRequest(BaseValidatorModel):
    TargetResourceCount: Optional[int] = None


class EnableFastSnapshotRestoreStateError(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class EnableFastSnapshotRestoreSuccessItem(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    State: Optional[FastSnapshotRestoreStateCodeType] = None
    StateTransitionReason: Optional[str] = None
    OwnerId: Optional[str] = None
    OwnerAlias: Optional[str] = None
    EnablingTime: Optional[datetime] = None
    OptimizingTime: Optional[datetime] = None
    EnabledTime: Optional[datetime] = None
    DisablingTime: Optional[datetime] = None
    DisabledTime: Optional[datetime] = None


# This class is the input for the 'enable_fast_snapshot_restores' function.
class EnableFastSnapshotRestoresRequest(BaseValidatorModel):
    AvailabilityZones: List[str]
    SourceSnapshotIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_image_block_public_access' function.
class EnableImageBlockPublicAccessRequest(BaseValidatorModel):
    ImageBlockPublicAccessState: Literal['block-new-sharing']
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_image_deregistration_protection' function.
class EnableImageDeregistrationProtectionRequest(BaseValidatorModel):
    ImageId: str
    WithCooldown: Optional[bool] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_image' function.
class EnableImageRequest(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_ipam_organization_admin_account' function.
class EnableIpamOrganizationAdminAccountRequest(BaseValidatorModel):
    DelegatedAdminAccountId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_reachability_analyzer_organization_sharing' function.
class EnableReachabilityAnalyzerOrganizationSharingRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_serial_console_access' function.
class EnableSerialConsoleAccessRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_snapshot_block_public_access' function.
class EnableSnapshotBlockPublicAccessRequest(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_transit_gateway_route_table_propagation' function.
class EnableTransitGatewayRouteTablePropagationRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    DryRun: Optional[bool] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None


# This class is the input for the 'enable_vgw_route_propagation' function.
class EnableVgwRoutePropagationRequest(BaseValidatorModel):
    GatewayId: str
    RouteTableId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_volume_io' function.
class EnableVolumeIORequest(BaseValidatorModel):
    VolumeId: str
    DryRun: Optional[bool] = None


class EnableVolumeIORequestVolumeEnableIo(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'enable_vpc_classic_link_dns_support' function.
class EnableVpcClassicLinkDnsSupportRequest(BaseValidatorModel):
    VpcId: Optional[str] = None


# This class is the input for the 'enable_vpc_classic_link' function.
class EnableVpcClassicLinkRequest(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None


class EnableVpcClassicLinkRequestVpcEnableClassicLink(BaseValidatorModel):
    DryRun: Optional[bool] = None


class EnclaveOptionsRequest(BaseValidatorModel):
    Enabled: Optional[bool] = None


class EnclaveOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None


class EventInformation(BaseValidatorModel):
    EventDescription: Optional[str] = None
    EventSubType: Optional[str] = None
    InstanceId: Optional[str] = None


class TransitGatewayRouteTableRoute(BaseValidatorModel):
    DestinationCidr: Optional[str] = None
    State: Optional[str] = None
    RouteOrigin: Optional[str] = None
    PrefixListId: Optional[str] = None
    AttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None


# This class is the input for the 'export_client_vpn_client_certificate_revocation_list' function.
class ExportClientVpnClientCertificateRevocationListRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'export_client_vpn_client_configuration' function.
class ExportClientVpnClientConfigurationRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None


class ExportTaskS3LocationRequest(BaseValidatorModel):
    S3Bucket: str
    S3Prefix: Optional[str] = None


class ExportTaskS3Location(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None


class ExportToS3Task(BaseValidatorModel):
    ContainerFormat: Optional[Literal['ova']] = None
    DiskImageFormat: Optional[DiskImageFormatType] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None


class InstanceExportDetails(BaseValidatorModel):
    InstanceId: Optional[str] = None
    TargetEnvironment: Optional[ExportEnvironmentType] = None


# This class is the input for the 'export_verified_access_instance_client_configuration' function.
class ExportVerifiedAccessInstanceClientConfigurationRequest(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    DryRun: Optional[bool] = None


class VerifiedAccessInstanceUserTrustProviderClientConfiguration(BaseValidatorModel):
    Type: Optional[UserTrustProviderTypeType] = None
    Scopes: Optional[str] = None
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    PublicSigningKeyEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    PkceEnabled: Optional[bool] = None


class FilterPortRange(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class FleetEbsBlockDeviceRequest(BaseValidatorModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None


class TargetCapacitySpecification(BaseValidatorModel):
    TotalTargetCapacity: Optional[int] = None
    OnDemandTargetCapacity: Optional[int] = None
    SpotTargetCapacity: Optional[int] = None
    DefaultTargetCapacityType: Optional[DefaultTargetCapacityTypeType] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None


class FleetLaunchTemplateSpecificationRequest(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class FleetLaunchTemplateSpecification(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class Placement(BaseValidatorModel):
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    PartitionNumber: Optional[int] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    GroupId: Optional[str] = None
    AvailabilityZone: Optional[str] = None


class PlacementResponse(BaseValidatorModel):
    GroupName: Optional[str] = None


class FleetSpotCapacityRebalanceRequest(BaseValidatorModel):
    ReplacementStrategy: Optional[FleetReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None


class FleetSpotCapacityRebalance(BaseValidatorModel):
    ReplacementStrategy: Optional[FleetReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None


class FpgaDeviceMemoryInfo(BaseValidatorModel):
    SizeInMiB: Optional[int] = None


class LoadPermission(BaseValidatorModel):
    UserId: Optional[str] = None
    Group: Optional[Literal['all']] = None


class FpgaImageState(BaseValidatorModel):
    Code: Optional[FpgaImageStateCodeType] = None
    Message: Optional[str] = None


class PciId(BaseValidatorModel):
    DeviceId: Optional[str] = None
    VendorId: Optional[str] = None
    SubsystemId: Optional[str] = None
    SubsystemVendorId: Optional[str] = None


# This class is the input for the 'get_allowed_images_settings' function.
class GetAllowedImagesSettingsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class ImageCriterion(BaseValidatorModel):
    ImageProviders: Optional[List[str]] = None


# This class is the input for the 'get_associated_enclave_certificate_iam_roles' function.
class GetAssociatedEnclaveCertificateIamRolesRequest(BaseValidatorModel):
    CertificateArn: str
    DryRun: Optional[bool] = None


# This class is the input for the 'get_associated_ipv6_pool_cidrs' function.
class GetAssociatedIpv6PoolCidrsRequest(BaseValidatorModel):
    PoolId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


class Ipv6CidrAssociation(BaseValidatorModel):
    Ipv6Cidr: Optional[str] = None
    AssociatedResource: Optional[str] = None


# This class is the input for the 'get_capacity_reservation_usage' function.
class GetCapacityReservationUsageRequest(BaseValidatorModel):
    CapacityReservationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


class InstanceUsage(BaseValidatorModel):
    AccountId: Optional[str] = None
    UsedInstanceCount: Optional[int] = None


class GetConsoleOutputRequestInstanceConsoleOutput(BaseValidatorModel):
    Latest: Optional[bool] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_console_output' function.
class GetConsoleOutputRequest(BaseValidatorModel):
    InstanceId: str
    Latest: Optional[bool] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_console_screenshot' function.
class GetConsoleScreenshotRequest(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    WakeUp: Optional[bool] = None


# This class is the input for the 'get_declarative_policies_report_summary' function.
class GetDeclarativePoliciesReportSummaryRequest(BaseValidatorModel):
    ReportId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'get_default_credit_specification' function.
class GetDefaultCreditSpecificationRequest(BaseValidatorModel):
    InstanceFamily: UnlimitedSupportedInstanceFamilyType
    DryRun: Optional[bool] = None


class InstanceFamilyCreditSpecification(BaseValidatorModel):
    InstanceFamily: Optional[UnlimitedSupportedInstanceFamilyType] = None
    CpuCredits: Optional[str] = None


# This class is the input for the 'get_ebs_default_kms_key_id' function.
class GetEbsDefaultKmsKeyIdRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'get_ebs_encryption_by_default' function.
class GetEbsEncryptionByDefaultRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'get_groups_for_capacity_reservation' function.
class GetGroupsForCapacityReservationRequest(BaseValidatorModel):
    CapacityReservationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_host_reservation_purchase_preview' function.
class GetHostReservationPurchasePreviewRequest(BaseValidatorModel):
    HostIdSet: List[str]
    OfferingId: str


class Purchase(BaseValidatorModel):
    CurrencyCode: Optional[Literal['USD']] = None
    Duration: Optional[int] = None
    HostIdSet: Optional[List[str]] = None
    HostReservationId: Optional[str] = None
    HourlyPrice: Optional[str] = None
    InstanceFamily: Optional[str] = None
    PaymentOption: Optional[PaymentOptionType] = None
    UpfrontPrice: Optional[str] = None


# This class is the input for the 'get_image_block_public_access_state' function.
class GetImageBlockPublicAccessStateRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'get_instance_metadata_defaults' function.
class GetInstanceMetadataDefaultsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class InstanceMetadataDefaultsResponse(BaseValidatorModel):
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None
    ManagedBy: Optional[ManagedByType] = None
    ManagedExceptionMessage: Optional[str] = None


# This class is the input for the 'get_instance_tpm_ek_pub' function.
class GetInstanceTpmEkPubRequest(BaseValidatorModel):
    InstanceId: str
    KeyType: EkPubKeyTypeType
    KeyFormat: EkPubKeyFormatType
    DryRun: Optional[bool] = None


class InstanceTypeInfoFromInstanceRequirements(BaseValidatorModel):
    InstanceType: Optional[str] = None


# This class is the input for the 'get_instance_uefi_data' function.
class GetInstanceUefiDataRequest(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None


class IpamAddressHistoryRecord(BaseValidatorModel):
    ResourceOwnerId: Optional[str] = None
    ResourceRegion: Optional[str] = None
    ResourceType: Optional[IpamAddressHistoryResourceTypeType] = None
    ResourceId: Optional[str] = None
    ResourceCidr: Optional[str] = None
    ResourceName: Optional[str] = None
    ResourceComplianceStatus: Optional[IpamComplianceStatusType] = None
    ResourceOverlapStatus: Optional[IpamOverlapStatusType] = None
    VpcId: Optional[str] = None
    SampledStartTime: Optional[datetime] = None
    SampledEndTime: Optional[datetime] = None


# This class is the input for the 'get_launch_template_data' function.
class GetLaunchTemplateDataRequest(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'get_managed_prefix_list_associations' function.
class GetManagedPrefixListAssociationsRequest(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PrefixListAssociation(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceOwner: Optional[str] = None


# This class is the input for the 'get_managed_prefix_list_entries' function.
class GetManagedPrefixListEntriesRequest(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    TargetVersion: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class PrefixListEntry(BaseValidatorModel):
    Cidr: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'get_network_insights_access_scope_analysis_findings' function.
class GetNetworkInsightsAccessScopeAnalysisFindingsRequest(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_network_insights_access_scope_content' function.
class GetNetworkInsightsAccessScopeContentRequest(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    DryRun: Optional[bool] = None


class GetPasswordDataRequestInstancePasswordData(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'get_password_data' function.
class GetPasswordDataRequest(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None


class ReservationValue(BaseValidatorModel):
    HourlyPrice: Optional[str] = None
    RemainingTotalValue: Optional[str] = None
    RemainingUpfrontValue: Optional[str] = None


# This class is the input for the 'get_serial_console_access_status' function.
class GetSerialConsoleAccessStatusRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'get_snapshot_block_public_access_state' function.
class GetSnapshotBlockPublicAccessStateRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


class SpotPlacementScore(BaseValidatorModel):
    Region: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Score: Optional[int] = None


class TransitGatewayAttachmentPropagation(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayPropagationStateType] = None


class TransitGatewayRouteTableAssociation(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None


class TransitGatewayRouteTablePropagation(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayPropagationStateType] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None


# This class is the input for the 'get_verified_access_endpoint_policy' function.
class GetVerifiedAccessEndpointPolicyRequest(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'get_verified_access_endpoint_targets' function.
class GetVerifiedAccessEndpointTargetsRequest(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class VerifiedAccessEndpointTarget(BaseValidatorModel):
    VerifiedAccessEndpointId: Optional[str] = None
    VerifiedAccessEndpointTargetIpAddress: Optional[str] = None
    VerifiedAccessEndpointTargetDns: Optional[str] = None


# This class is the input for the 'get_verified_access_group_policy' function.
class GetVerifiedAccessGroupPolicyRequest(BaseValidatorModel):
    VerifiedAccessGroupId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'get_vpn_connection_device_sample_configuration' function.
class GetVpnConnectionDeviceSampleConfigurationRequest(BaseValidatorModel):
    VpnConnectionId: str
    VpnConnectionDeviceTypeId: str
    InternetKeyExchangeVersion: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_vpn_connection_device_types' function.
class GetVpnConnectionDeviceTypesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class VpnConnectionDeviceType(BaseValidatorModel):
    VpnConnectionDeviceTypeId: Optional[str] = None
    Vendor: Optional[str] = None
    Platform: Optional[str] = None
    Software: Optional[str] = None


# This class is the input for the 'get_vpn_tunnel_replacement_status' function.
class GetVpnTunnelReplacementStatusRequest(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    DryRun: Optional[bool] = None


class MaintenanceDetails(BaseValidatorModel):
    PendingMaintenance: Optional[str] = None
    MaintenanceAutoAppliedAfter: Optional[datetime] = None
    LastMaintenanceApplied: Optional[datetime] = None


class GpuDeviceMemoryInfo(BaseValidatorModel):
    SizeInMiB: Optional[int] = None


class HibernationOptionsRequest(BaseValidatorModel):
    Configured: Optional[bool] = None


class HibernationOptions(BaseValidatorModel):
    Configured: Optional[bool] = None


class HostInstance(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    OwnerId: Optional[str] = None


class HostProperties(BaseValidatorModel):
    Cores: Optional[int] = None
    InstanceType: Optional[str] = None
    InstanceFamily: Optional[str] = None
    Sockets: Optional[int] = None
    TotalVCpus: Optional[int] = None


class IKEVersionsListValue(BaseValidatorModel):
    Value: Optional[str] = None


class IKEVersionsRequestListValue(BaseValidatorModel):
    Value: Optional[str] = None


class IamInstanceProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None


class LaunchPermission(BaseValidatorModel):
    OrganizationArn: Optional[str] = None
    OrganizationalUnitArn: Optional[str] = None
    UserId: Optional[str] = None
    Group: Optional[Literal['all']] = None


class ImageCriterionRequest(BaseValidatorModel):
    ImageProviders: Optional[List[str]] = None


class UserBucket(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None


class ImageMetadata(BaseValidatorModel):
    ImageId: Optional[str] = None
    Name: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[ImageStateType] = None
    ImageOwnerAlias: Optional[str] = None
    CreationDate: Optional[str] = None
    DeprecationTime: Optional[str] = None
    ImageAllowed: Optional[bool] = None
    IsPublic: Optional[bool] = None


class ImageRecycleBinInfo(BaseValidatorModel):
    ImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    RecycleBinEnterTime: Optional[datetime] = None
    RecycleBinExitTime: Optional[datetime] = None


class StateReason(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


# This class is the input for the 'import_client_vpn_client_certificate_revocation_list' function.
class ImportClientVpnClientCertificateRevocationListRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    CertificateRevocationList: str
    DryRun: Optional[bool] = None


class ImportImageLicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


class ImportImageLicenseConfigurationResponse(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


class UserData(BaseValidatorModel):
    Data: Optional[str] = None


class InferenceDeviceMemoryInfo(BaseValidatorModel):
    SizeInMiB: Optional[int] = None


class InstanceAttachmentEnaSrdUdpSpecification(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None


class InstanceCount(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    State: Optional[ListingStateType] = None


class InstanceCreditSpecificationRequest(BaseValidatorModel):
    InstanceId: str
    CpuCredits: Optional[str] = None


class InstanceEventWindowTimeRange(BaseValidatorModel):
    StartWeekDay: Optional[WeekDayType] = None
    StartHour: Optional[int] = None
    EndWeekDay: Optional[WeekDayType] = None
    EndHour: Optional[int] = None


class InstanceState(BaseValidatorModel):
    Code: Optional[int] = None
    Name: Optional[InstanceStateNameType] = None


class InstanceIpv4Prefix(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None


class InstanceIpv6AddressRequest(BaseValidatorModel):
    Ipv6Address: Optional[str] = None


class InstanceIpv6Prefix(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None


class InstanceMaintenanceOptionsRequest(BaseValidatorModel):
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None


class InstanceMaintenanceOptions(BaseValidatorModel):
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None


class InstanceMetadataOptionsRequest(BaseValidatorModel):
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None


class InstanceMetadataOptionsResponse(BaseValidatorModel):
    State: Optional[InstanceMetadataOptionsStateType] = None
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None


class Monitoring(BaseValidatorModel):
    State: Optional[MonitoringStateType] = None


class InstanceNetworkInterfaceAssociation(BaseValidatorModel):
    CarrierIp: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    IpOwnerId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None


class InstanceNetworkPerformanceOptionsRequest(BaseValidatorModel):
    BandwidthWeighting: Optional[InstanceBandwidthWeightingType] = None


class InstanceNetworkPerformanceOptions(BaseValidatorModel):
    BandwidthWeighting: Optional[InstanceBandwidthWeightingType] = None


class MemoryGiBPerVCpu(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class MemoryMiB(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class NetworkBandwidthGbps(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class NetworkInterfaceCount(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class TotalLocalStorageGB(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class VCpuCountRange(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class MemoryGiBPerVCpuRequest(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class MemoryMiBRequest(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None


class NetworkBandwidthGbpsRequest(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class NetworkInterfaceCountRequest(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None


class TotalLocalStorageGBRequest(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None


class VCpuCountRangeRequest(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None


class InstanceStatusDetails(BaseValidatorModel):
    ImpairedSince: Optional[datetime] = None
    Name: Optional[Literal['reachability']] = None
    Status: Optional[StatusTypeType] = None


class InstanceStatusEvent(BaseValidatorModel):
    InstanceEventId: Optional[str] = None
    Code: Optional[EventCodeType] = None
    Description: Optional[str] = None
    NotAfter: Optional[datetime] = None
    NotBefore: Optional[datetime] = None
    NotBeforeDeadline: Optional[datetime] = None


class LicenseConfiguration(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


class PrivateDnsNameOptionsResponse(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None


class MemoryInfo(BaseValidatorModel):
    SizeInMiB: Optional[int] = None


class NitroTpmInfo(BaseValidatorModel):
    SupportedVersions: Optional[List[str]] = None


class PlacementGroupInfo(BaseValidatorModel):
    SupportedStrategies: Optional[List[PlacementGroupStrategyType]] = None


class ProcessorInfo(BaseValidatorModel):
    SupportedArchitectures: Optional[List[ArchitectureTypeType]] = None
    SustainedClockSpeedInGhz: Optional[float] = None
    SupportedFeatures: Optional[List[Literal['amd-sev-snp']]] = None
    Manufacturer: Optional[str] = None


class VCpuInfo(BaseValidatorModel):
    DefaultVCpus: Optional[int] = None
    DefaultCores: Optional[int] = None
    DefaultThreadsPerCore: Optional[int] = None
    ValidCores: Optional[List[int]] = None
    ValidThreadsPerCore: Optional[List[int]] = None


class IpRange(BaseValidatorModel):
    Description: Optional[str] = None
    CidrIp: Optional[str] = None


class Ipv6Range(BaseValidatorModel):
    Description: Optional[str] = None
    CidrIpv6: Optional[str] = None


class PrefixListId(BaseValidatorModel):
    Description: Optional[str] = None
    PrefixListId: Optional[str] = None


class UserIdGroupPair(BaseValidatorModel):
    Description: Optional[str] = None
    UserId: Optional[str] = None
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    PeeringStatus: Optional[str] = None


class IpamCidrAuthorizationContext(BaseValidatorModel):
    Message: Optional[str] = None
    Signature: Optional[str] = None


class IpamDiscoveryFailureReason(BaseValidatorModel):
    Code: Optional[IpamDiscoveryFailureCodeType] = None
    Message: Optional[str] = None


class IpamPublicAddressSecurityGroup(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None


class IpamResourceTag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class IpamOperatingRegion(BaseValidatorModel):
    RegionName: Optional[str] = None


class IpamOrganizationalUnitExclusion(BaseValidatorModel):
    OrganizationsEntityPath: Optional[str] = None


class IpamPoolCidrFailureReason(BaseValidatorModel):
    Code: Optional[IpamPoolCidrFailureCodeType] = None
    Message: Optional[str] = None


class IpamPoolSourceResource(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal['vpc']] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None


class IpamPublicAddressTag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class Ipv4PrefixSpecificationResponse(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None


class Ipv6CidrBlock(BaseValidatorModel):
    Ipv6CidrBlock: Optional[str] = None


class PoolCidrBlock(BaseValidatorModel):
    Cidr: Optional[str] = None


class Ipv6PrefixSpecificationResponse(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None


class Ipv6PrefixSpecification(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None


class LastError(BaseValidatorModel):
    Message: Optional[str] = None
    Code: Optional[str] = None


class RunInstancesMonitoringEnabled(BaseValidatorModel):
    Enabled: bool


class SpotPlacement(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None
    Tenancy: Optional[TenancyType] = None


class LaunchTemplateEbsBlockDeviceRequest(BaseValidatorModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Throughput: Optional[int] = None


class LaunchTemplateEbsBlockDevice(BaseValidatorModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Throughput: Optional[int] = None


class LaunchTemplateCpuOptionsRequest(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None


class LaunchTemplateCpuOptions(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None


class LaunchTemplateElasticInferenceAcceleratorResponse(BaseValidatorModel):
    Type: Optional[str] = None
    Count: Optional[int] = None


class LaunchTemplateElasticInferenceAccelerator(BaseValidatorModel):
    Type: str
    Count: Optional[int] = None


class LaunchTemplateEnaSrdUdpSpecification(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None


class LaunchTemplateEnclaveOptionsRequest(BaseValidatorModel):
    Enabled: Optional[bool] = None


class LaunchTemplateEnclaveOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None


class LaunchTemplateHibernationOptionsRequest(BaseValidatorModel):
    Configured: Optional[bool] = None


class LaunchTemplateHibernationOptions(BaseValidatorModel):
    Configured: Optional[bool] = None


class LaunchTemplateIamInstanceProfileSpecificationRequest(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class LaunchTemplateIamInstanceProfileSpecification(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class LaunchTemplateInstanceMaintenanceOptionsRequest(BaseValidatorModel):
    AutoRecovery: Optional[LaunchTemplateAutoRecoveryStateType] = None


class LaunchTemplateInstanceMaintenanceOptions(BaseValidatorModel):
    AutoRecovery: Optional[LaunchTemplateAutoRecoveryStateType] = None


class LaunchTemplateSpotMarketOptions(BaseValidatorModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[datetime] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None


class LaunchTemplateInstanceMetadataOptionsRequest(BaseValidatorModel):
    HttpTokens: Optional[LaunchTemplateHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[LaunchTemplateInstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[LaunchTemplateInstanceMetadataProtocolIpv6Type] = None
    InstanceMetadataTags: Optional[LaunchTemplateInstanceMetadataTagsStateType] = None


class LaunchTemplateInstanceMetadataOptions(BaseValidatorModel):
    State: Optional[LaunchTemplateInstanceMetadataOptionsStateType] = None
    HttpTokens: Optional[LaunchTemplateHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[LaunchTemplateInstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[LaunchTemplateInstanceMetadataProtocolIpv6Type] = None
    InstanceMetadataTags: Optional[LaunchTemplateInstanceMetadataTagsStateType] = None


class LaunchTemplateLicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


class LaunchTemplateLicenseConfiguration(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


class LaunchTemplateNetworkPerformanceOptionsRequest(BaseValidatorModel):
    BandwidthWeighting: Optional[InstanceBandwidthWeightingType] = None


class LaunchTemplateNetworkPerformanceOptions(BaseValidatorModel):
    BandwidthWeighting: Optional[InstanceBandwidthWeightingType] = None


class LaunchTemplatePlacementRequest(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    GroupId: Optional[str] = None


class LaunchTemplatePlacement(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    GroupId: Optional[str] = None


class LaunchTemplatePrivateDnsNameOptionsRequest(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None


class LaunchTemplatePrivateDnsNameOptions(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None


class LaunchTemplateSpecification(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None


class LaunchTemplatesMonitoringRequest(BaseValidatorModel):
    Enabled: Optional[bool] = None


class LaunchTemplatesMonitoring(BaseValidatorModel):
    Enabled: Optional[bool] = None


class LicenseConfigurationRequest(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None


# This class is the input for the 'list_images_in_recycle_bin' function.
class ListImagesInRecycleBinRequest(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'list_snapshots_in_recycle_bin' function.
class ListSnapshotsInRecycleBinRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SnapshotIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class SnapshotRecycleBinInfo(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    RecycleBinEnterTime: Optional[datetime] = None
    RecycleBinExitTime: Optional[datetime] = None
    Description: Optional[str] = None
    VolumeId: Optional[str] = None


class LoadPermissionRequest(BaseValidatorModel):
    Group: Optional[Literal['all']] = None
    UserId: Optional[str] = None


class MediaDeviceMemoryInfo(BaseValidatorModel):
    SizeInMiB: Optional[int] = None


# This class is the input for the 'modify_address_attribute' function.
class ModifyAddressAttributeRequest(BaseValidatorModel):
    AllocationId: str
    DomainName: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_availability_zone_group' function.
class ModifyAvailabilityZoneGroupRequest(BaseValidatorModel):
    GroupName: str
    OptInStatus: ModifyAvailabilityZoneOptInStatusType
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_default_credit_specification' function.
class ModifyDefaultCreditSpecificationRequest(BaseValidatorModel):
    InstanceFamily: UnlimitedSupportedInstanceFamilyType
    CpuCredits: str
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_ebs_default_kms_key_id' function.
class ModifyEbsDefaultKmsKeyIdRequest(BaseValidatorModel):
    KmsKeyId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_hosts' function.
class ModifyHostsRequest(BaseValidatorModel):
    HostIds: List[str]
    HostRecovery: Optional[HostRecoveryType] = None
    InstanceType: Optional[str] = None
    InstanceFamily: Optional[str] = None
    HostMaintenance: Optional[HostMaintenanceType] = None
    AutoPlacement: Optional[AutoPlacementType] = None


# This class is the input for the 'modify_id_format' function.
class ModifyIdFormatRequest(BaseValidatorModel):
    Resource: str
    UseLongIds: bool


# This class is the input for the 'modify_identity_id_format' function.
class ModifyIdentityIdFormatRequest(BaseValidatorModel):
    Resource: str
    UseLongIds: bool
    PrincipalArn: str


# This class is the input for the 'modify_instance_cpu_options' function.
class ModifyInstanceCpuOptionsRequest(BaseValidatorModel):
    InstanceId: str
    CoreCount: int
    ThreadsPerCore: int
    DryRun: Optional[bool] = None


class SuccessfulInstanceCreditSpecificationItem(BaseValidatorModel):
    InstanceId: Optional[str] = None


# This class is the input for the 'modify_instance_maintenance_options' function.
class ModifyInstanceMaintenanceOptionsRequest(BaseValidatorModel):
    InstanceId: str
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_instance_metadata_defaults' function.
class ModifyInstanceMetadataDefaultsRequest(BaseValidatorModel):
    HttpTokens: Optional[MetadataDefaultHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[DefaultInstanceMetadataEndpointStateType] = None
    InstanceMetadataTags: Optional[DefaultInstanceMetadataTagsStateType] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_instance_metadata_options' function.
class ModifyInstanceMetadataOptionsRequest(BaseValidatorModel):
    InstanceId: str
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    DryRun: Optional[bool] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None


# This class is the input for the 'modify_instance_network_performance_options' function.
class ModifyInstanceNetworkPerformanceRequest(BaseValidatorModel):
    InstanceId: str
    BandwidthWeighting: InstanceBandwidthWeightingType
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_instance_placement' function.
class ModifyInstancePlacementRequest(BaseValidatorModel):
    InstanceId: str
    GroupName: Optional[str] = None
    PartitionNumber: Optional[int] = None
    HostResourceGroupArn: Optional[str] = None
    GroupId: Optional[str] = None
    Tenancy: Optional[HostTenancyType] = None
    Affinity: Optional[AffinityType] = None
    HostId: Optional[str] = None


class RemoveIpamOperatingRegion(BaseValidatorModel):
    RegionName: Optional[str] = None


# This class is the input for the 'modify_ipam_resource_cidr' function.
class ModifyIpamResourceCidrRequest(BaseValidatorModel):
    ResourceId: str
    ResourceCidr: str
    ResourceRegion: str
    CurrentIpamScopeId: str
    Monitored: bool
    DryRun: Optional[bool] = None
    DestinationIpamScopeId: Optional[str] = None


class RemoveIpamOrganizationalUnitExclusion(BaseValidatorModel):
    OrganizationsEntityPath: Optional[str] = None


# This class is the input for the 'modify_ipam_scope' function.
class ModifyIpamScopeRequest(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None


# This class is the input for the 'modify_launch_template' function.
class ModifyLaunchTemplateRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    DefaultVersion: Optional[str] = None


# This class is the input for the 'modify_local_gateway_route' function.
class ModifyLocalGatewayRouteRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationPrefixListId: Optional[str] = None


class RemovePrefixListEntry(BaseValidatorModel):
    Cidr: str


class NetworkInterfaceAttachmentChanges(BaseValidatorModel):
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None


# This class is the input for the 'modify_private_dns_name_options' function.
class ModifyPrivateDnsNameOptionsRequest(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    PrivateDnsHostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None


class ReservedInstancesConfiguration(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[str] = None
    Scope: Optional[ScopeType] = None


# This class is the input for the 'modify_snapshot_tier' function.
class ModifySnapshotTierRequest(BaseValidatorModel):
    SnapshotId: str
    StorageTier: Optional[Literal['archive']] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_traffic_mirror_filter_network_services' function.
class ModifyTrafficMirrorFilterNetworkServicesRequest(BaseValidatorModel):
    TrafficMirrorFilterId: str
    AddNetworkServices: Optional[List[Literal['amazon-dns']]] = None
    RemoveNetworkServices: Optional[List[Literal['amazon-dns']]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_traffic_mirror_session' function.
class ModifyTrafficMirrorSessionRequest(BaseValidatorModel):
    TrafficMirrorSessionId: str
    TrafficMirrorTargetId: Optional[str] = None
    TrafficMirrorFilterId: Optional[str] = None
    PacketLength: Optional[int] = None
    SessionNumber: Optional[int] = None
    VirtualNetworkId: Optional[int] = None
    Description: Optional[str] = None
    RemoveFields: Optional[List[TrafficMirrorSessionFieldType]] = None
    DryRun: Optional[bool] = None


class ModifyTransitGatewayOptions(BaseValidatorModel):
    AddTransitGatewayCidrBlocks: Optional[List[str]] = None
    RemoveTransitGatewayCidrBlocks: Optional[List[str]] = None
    VpnEcmpSupport: Optional[VpnEcmpSupportValueType] = None
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    AutoAcceptSharedAttachments: Optional[AutoAcceptSharedAttachmentsValueType] = None
    DefaultRouteTableAssociation: Optional[DefaultRouteTableAssociationValueType] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    DefaultRouteTablePropagation: Optional[DefaultRouteTablePropagationValueType] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    AmazonSideAsn: Optional[int] = None


# This class is the input for the 'modify_transit_gateway_prefix_list_reference' function.
class ModifyTransitGatewayPrefixListReferenceRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None


class ModifyTransitGatewayVpcAttachmentRequestOptions(BaseValidatorModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None


class ModifyVerifiedAccessEndpointPortRange(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class VerifiedAccessSseSpecificationResponse(BaseValidatorModel):
    CustomerManagedKeyEnabled: Optional[bool] = None
    KmsKeyArn: Optional[str] = None


class ModifyVerifiedAccessEndpointRdsOptions(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    Port: Optional[int] = None
    RdsEndpoint: Optional[str] = None


# This class is the input for the 'modify_verified_access_group' function.
class ModifyVerifiedAccessGroupRequest(BaseValidatorModel):
    VerifiedAccessGroupId: str
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_verified_access_instance' function.
class ModifyVerifiedAccessInstanceRequest(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    CidrEndpointsCustomSubDomain: Optional[str] = None


class ModifyVerifiedAccessNativeApplicationOidcOptions(BaseValidatorModel):
    PublicSigningKeyEndpoint: Optional[str] = None
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None


class ModifyVerifiedAccessTrustProviderDeviceOptions(BaseValidatorModel):
    PublicSigningKeyUrl: Optional[str] = None


class ModifyVerifiedAccessTrustProviderOidcOptions(BaseValidatorModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None


# This class is the input for the 'modify_volume' function.
class ModifyVolumeRequest(BaseValidatorModel):
    VolumeId: str
    DryRun: Optional[bool] = None
    Size: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None
    MultiAttachEnabled: Optional[bool] = None


# This class is the input for the 'modify_vpc_block_public_access_exclusion' function.
class ModifyVpcBlockPublicAccessExclusionRequest(BaseValidatorModel):
    ExclusionId: str
    InternetGatewayExclusionMode: InternetGatewayExclusionModeType
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_vpc_block_public_access_options' function.
class ModifyVpcBlockPublicAccessOptionsRequest(BaseValidatorModel):
    InternetGatewayBlockMode: InternetGatewayBlockModeType
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_vpc_endpoint_connection_notification' function.
class ModifyVpcEndpointConnectionNotificationRequest(BaseValidatorModel):
    ConnectionNotificationId: str
    DryRun: Optional[bool] = None
    ConnectionNotificationArn: Optional[str] = None
    ConnectionEvents: Optional[List[str]] = None


# This class is the input for the 'modify_vpc_endpoint_service_configuration' function.
class ModifyVpcEndpointServiceConfigurationRequest(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    RemovePrivateDnsName: Optional[bool] = None
    AcceptanceRequired: Optional[bool] = None
    AddNetworkLoadBalancerArns: Optional[List[str]] = None
    RemoveNetworkLoadBalancerArns: Optional[List[str]] = None
    AddGatewayLoadBalancerArns: Optional[List[str]] = None
    RemoveGatewayLoadBalancerArns: Optional[List[str]] = None
    AddSupportedIpAddressTypes: Optional[List[str]] = None
    RemoveSupportedIpAddressTypes: Optional[List[str]] = None
    AddSupportedRegions: Optional[List[str]] = None
    RemoveSupportedRegions: Optional[List[str]] = None


# This class is the input for the 'modify_vpc_endpoint_service_payer_responsibility' function.
class ModifyVpcEndpointServicePayerResponsibilityRequest(BaseValidatorModel):
    ServiceId: str
    PayerResponsibility: Literal['ServiceOwner']
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_vpc_endpoint_service_permissions' function.
class ModifyVpcEndpointServicePermissionsRequest(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    AddAllowedPrincipals: Optional[List[str]] = None
    RemoveAllowedPrincipals: Optional[List[str]] = None


class PeeringConnectionOptionsRequest(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None


class PeeringConnectionOptions(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None


# This class is the input for the 'modify_vpc_tenancy' function.
class ModifyVpcTenancyRequest(BaseValidatorModel):
    VpcId: str
    InstanceTenancy: Literal['default']
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_vpn_connection_options' function.
class ModifyVpnConnectionOptionsRequest(BaseValidatorModel):
    VpnConnectionId: str
    LocalIpv4NetworkCidr: Optional[str] = None
    RemoteIpv4NetworkCidr: Optional[str] = None
    LocalIpv6NetworkCidr: Optional[str] = None
    RemoteIpv6NetworkCidr: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_vpn_connection' function.
class ModifyVpnConnectionRequest(BaseValidatorModel):
    VpnConnectionId: str
    TransitGatewayId: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_vpn_tunnel_certificate' function.
class ModifyVpnTunnelCertificateRequest(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    DryRun: Optional[bool] = None


class Phase1DHGroupNumbersRequestListValue(BaseValidatorModel):
    Value: Optional[int] = None


class Phase1EncryptionAlgorithmsRequestListValue(BaseValidatorModel):
    Value: Optional[str] = None


class Phase1IntegrityAlgorithmsRequestListValue(BaseValidatorModel):
    Value: Optional[str] = None


class Phase2DHGroupNumbersRequestListValue(BaseValidatorModel):
    Value: Optional[int] = None


class Phase2EncryptionAlgorithmsRequestListValue(BaseValidatorModel):
    Value: Optional[str] = None


class Phase2IntegrityAlgorithmsRequestListValue(BaseValidatorModel):
    Value: Optional[str] = None


class MonitorInstancesRequestInstanceMonitor(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'monitor_instances' function.
class MonitorInstancesRequest(BaseValidatorModel):
    InstanceIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'move_address_to_vpc' function.
class MoveAddressToVpcRequest(BaseValidatorModel):
    PublicIp: str
    DryRun: Optional[bool] = None


# This class is the input for the 'move_byoip_cidr_to_ipam' function.
class MoveByoipCidrToIpamRequest(BaseValidatorModel):
    Cidr: str
    IpamPoolId: str
    IpamPoolOwner: str
    DryRun: Optional[bool] = None


# This class is the input for the 'move_capacity_reservation_instances' function.
class MoveCapacityReservationInstancesRequest(BaseValidatorModel):
    SourceCapacityReservationId: str
    DestinationCapacityReservationId: str
    InstanceCount: int
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


class ProvisionedBandwidth(BaseValidatorModel):
    ProvisionTime: Optional[datetime] = None
    Provisioned: Optional[str] = None
    RequestTime: Optional[datetime] = None
    Requested: Optional[str] = None
    Status: Optional[str] = None


class NativeApplicationOidcOptions(BaseValidatorModel):
    PublicSigningKeyEndpoint: Optional[str] = None
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    Scope: Optional[str] = None


class NetworkAclAssociation(BaseValidatorModel):
    NetworkAclAssociationId: Optional[str] = None
    NetworkAclId: Optional[str] = None
    SubnetId: Optional[str] = None


class NetworkCardInfo(BaseValidatorModel):
    NetworkCardIndex: Optional[int] = None
    NetworkPerformance: Optional[str] = None
    MaximumNetworkInterfaces: Optional[int] = None
    BaselineBandwidthInGbps: Optional[float] = None
    PeakBandwidthInGbps: Optional[float] = None


class NetworkInterfaceAssociation(BaseValidatorModel):
    AllocationId: Optional[str] = None
    AssociationId: Optional[str] = None
    IpOwnerId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    CarrierIp: Optional[str] = None


class NetworkInterfaceIpv6Address(BaseValidatorModel):
    Ipv6Address: Optional[str] = None
    IsPrimaryIpv6: Optional[bool] = None


class NetworkInterfacePermissionState(BaseValidatorModel):
    State: Optional[NetworkInterfacePermissionStateCodeType] = None
    StatusMessage: Optional[str] = None


class NeuronDeviceCoreInfo(BaseValidatorModel):
    Count: Optional[int] = None
    Version: Optional[int] = None


class NeuronDeviceMemoryInfo(BaseValidatorModel):
    SizeInMiB: Optional[int] = None


class OidcOptions(BaseValidatorModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None


class PacketHeaderStatementRequest(BaseValidatorModel):
    SourceAddresses: Optional[List[str]] = None
    DestinationAddresses: Optional[List[str]] = None
    SourcePorts: Optional[List[str]] = None
    DestinationPorts: Optional[List[str]] = None
    SourcePrefixLists: Optional[List[str]] = None
    DestinationPrefixLists: Optional[List[str]] = None
    Protocols: Optional[List[ProtocolType]] = None


class PacketHeaderStatement(BaseValidatorModel):
    SourceAddresses: Optional[List[str]] = None
    DestinationAddresses: Optional[List[str]] = None
    SourcePorts: Optional[List[str]] = None
    DestinationPorts: Optional[List[str]] = None
    SourcePrefixLists: Optional[List[str]] = None
    DestinationPrefixLists: Optional[List[str]] = None
    Protocols: Optional[List[ProtocolType]] = None


class RequestFilterPortRange(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class ResourceStatementRequest(BaseValidatorModel):
    Resources: Optional[List[str]] = None
    ResourceTypes: Optional[List[str]] = None


class ResourceStatement(BaseValidatorModel):
    Resources: Optional[List[str]] = None
    ResourceTypes: Optional[List[str]] = None


class PeeringAttachmentStatus(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class PeeringTgwInfo(BaseValidatorModel):
    TransitGatewayId: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    OwnerId: Optional[str] = None
    Region: Optional[str] = None


class Phase1DHGroupNumbersListValue(BaseValidatorModel):
    Value: Optional[int] = None


class Phase1EncryptionAlgorithmsListValue(BaseValidatorModel):
    Value: Optional[str] = None


class Phase1IntegrityAlgorithmsListValue(BaseValidatorModel):
    Value: Optional[str] = None


class Phase2DHGroupNumbersListValue(BaseValidatorModel):
    Value: Optional[int] = None


class Phase2EncryptionAlgorithmsListValue(BaseValidatorModel):
    Value: Optional[str] = None


class Phase2IntegrityAlgorithmsListValue(BaseValidatorModel):
    Value: Optional[str] = None


class PriceSchedule(BaseValidatorModel):
    Active: Optional[bool] = None
    CurrencyCode: Optional[Literal['USD']] = None
    Price: Optional[float] = None
    Term: Optional[int] = None


class PricingDetail(BaseValidatorModel):
    Count: Optional[int] = None
    Price: Optional[float] = None


class PrivateDnsDetails(BaseValidatorModel):
    PrivateDnsName: Optional[str] = None


class PrivateDnsNameConfiguration(BaseValidatorModel):
    State: Optional[DnsNameStateType] = None
    Type: Optional[str] = None
    Value: Optional[str] = None
    Name: Optional[str] = None


class PrivateDnsNameOptionsOnLaunch(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None


class PrivateDnsNameOptionsRequest(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None


class PropagatingVgw(BaseValidatorModel):
    GatewayId: Optional[str] = None


# This class is the input for the 'provision_public_ipv4_pool_cidr' function.
class ProvisionPublicIpv4PoolCidrRequest(BaseValidatorModel):
    IpamPoolId: str
    PoolId: str
    NetmaskLength: int
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None


class PublicIpv4PoolRange(BaseValidatorModel):
    FirstAddress: Optional[str] = None
    LastAddress: Optional[str] = None
    AddressCount: Optional[int] = None
    AvailableAddressCount: Optional[int] = None


# This class is the input for the 'purchase_capacity_block_extension' function.
class PurchaseCapacityBlockExtensionRequest(BaseValidatorModel):
    CapacityBlockExtensionOfferingId: str
    CapacityReservationId: str
    DryRun: Optional[bool] = None


class PurchaseRequest(BaseValidatorModel):
    InstanceCount: int
    PurchaseToken: str


class ReservedInstanceLimitPrice(BaseValidatorModel):
    Amount: Optional[float] = None
    CurrencyCode: Optional[Literal['USD']] = None


class RebootInstancesRequestInstanceReboot(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'reboot_instances' function.
class RebootInstancesRequest(BaseValidatorModel):
    InstanceIds: List[str]
    DryRun: Optional[bool] = None


class RecurringCharge(BaseValidatorModel):
    Amount: Optional[float] = None
    Frequency: Optional[Literal['Hourly']] = None


class ReferencedSecurityGroup(BaseValidatorModel):
    GroupId: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None


class RegisterInstanceTagAttributeRequest(BaseValidatorModel):
    IncludeAllTagsOfInstance: Optional[bool] = None
    InstanceTagKeys: Optional[List[str]] = None


# This class is the input for the 'register_transit_gateway_multicast_group_members' function.
class RegisterTransitGatewayMulticastGroupMembersRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    NetworkInterfaceIds: List[str]
    GroupIpAddress: Optional[str] = None
    DryRun: Optional[bool] = None


class TransitGatewayMulticastRegisteredGroupMembers(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    RegisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None


# This class is the input for the 'register_transit_gateway_multicast_group_sources' function.
class RegisterTransitGatewayMulticastGroupSourcesRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    NetworkInterfaceIds: List[str]
    GroupIpAddress: Optional[str] = None
    DryRun: Optional[bool] = None


class TransitGatewayMulticastRegisteredGroupSources(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    RegisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None


# This class is the input for the 'reject_capacity_reservation_billing_ownership' function.
class RejectCapacityReservationBillingOwnershipRequest(BaseValidatorModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'reject_transit_gateway_multicast_domain_associations' function.
class RejectTransitGatewayMulticastDomainAssociationsRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'reject_transit_gateway_peering_attachment' function.
class RejectTransitGatewayPeeringAttachmentRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'reject_transit_gateway_vpc_attachment' function.
class RejectTransitGatewayVpcAttachmentRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'reject_vpc_endpoint_connections' function.
class RejectVpcEndpointConnectionsRequest(BaseValidatorModel):
    ServiceId: str
    VpcEndpointIds: List[str]
    DryRun: Optional[bool] = None


# This class is the input for the 'reject_vpc_peering_connection' function.
class RejectVpcPeeringConnectionRequest(BaseValidatorModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None


class RejectVpcPeeringConnectionRequestVpcPeeringConnectionReject(BaseValidatorModel):
    DryRun: Optional[bool] = None


class ReleaseAddressRequestClassicAddressRelease(BaseValidatorModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'release_address' function.
class ReleaseAddressRequest(BaseValidatorModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None


class ReleaseAddressRequestVpcAddressRelease(BaseValidatorModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'release_hosts' function.
class ReleaseHostsRequest(BaseValidatorModel):
    HostIds: List[str]


# This class is the input for the 'release_ipam_pool_allocation' function.
class ReleaseIpamPoolAllocationRequest(BaseValidatorModel):
    IpamPoolId: str
    Cidr: str
    IpamPoolAllocationId: str
    DryRun: Optional[bool] = None


class ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociation(BaseValidatorModel):
    AssociationId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'replace_network_acl_association' function.
class ReplaceNetworkAclAssociationRequest(BaseValidatorModel):
    AssociationId: str
    NetworkAclId: str
    DryRun: Optional[bool] = None


class ReplaceRouteRequestRouteReplace(BaseValidatorModel):
    DestinationPrefixListId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    LocalTarget: Optional[bool] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    DryRun: Optional[bool] = None
    GatewayId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    NatGatewayId: Optional[str] = None


# This class is the input for the 'replace_route' function.
class ReplaceRouteRequest(BaseValidatorModel):
    RouteTableId: str
    DestinationPrefixListId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    LocalTarget: Optional[bool] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationCidrBlock: Optional[str] = None
    GatewayId: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    NatGatewayId: Optional[str] = None


class ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnet(BaseValidatorModel):
    RouteTableId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'replace_route_table_association' function.
class ReplaceRouteTableAssociationRequest(BaseValidatorModel):
    AssociationId: str
    RouteTableId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'replace_transit_gateway_route' function.
class ReplaceTransitGatewayRouteRequest(BaseValidatorModel):
    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'replace_vpn_tunnel' function.
class ReplaceVpnTunnelRequest(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    ApplyPendingMaintenance: Optional[bool] = None
    DryRun: Optional[bool] = None


class ReservedInstancesId(BaseValidatorModel):
    ReservedInstancesId: Optional[str] = None


# This class is the input for the 'reset_address_attribute' function.
class ResetAddressAttributeRequest(BaseValidatorModel):
    AllocationId: str
    Attribute: Literal['domain-name']
    DryRun: Optional[bool] = None


# This class is the input for the 'reset_ebs_default_kms_key_id' function.
class ResetEbsDefaultKmsKeyIdRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'reset_fpga_image_attribute' function.
class ResetFpgaImageAttributeRequest(BaseValidatorModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None
    Attribute: Optional[Literal['loadPermission']] = None


class ResetImageAttributeRequestImageResetAttribute(BaseValidatorModel):
    Attribute: Literal['launchPermission']
    DryRun: Optional[bool] = None


# This class is the input for the 'reset_image_attribute' function.
class ResetImageAttributeRequest(BaseValidatorModel):
    Attribute: Literal['launchPermission']
    ImageId: str
    DryRun: Optional[bool] = None


class ResetInstanceAttributeRequestInstanceResetAttribute(BaseValidatorModel):
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None


class ResetInstanceAttributeRequestInstanceResetKernel(BaseValidatorModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None


class ResetInstanceAttributeRequestInstanceResetRamdisk(BaseValidatorModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None


class ResetInstanceAttributeRequestInstanceResetSourceDestCheck(BaseValidatorModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'reset_instance_attribute' function.
class ResetInstanceAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None


class ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttribute(BaseValidatorModel):
    DryRun: Optional[bool] = None
    SourceDestCheck: Optional[str] = None


# This class is the input for the 'reset_network_interface_attribute' function.
class ResetNetworkInterfaceAttributeRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None
    SourceDestCheck: Optional[str] = None


class ResetSnapshotAttributeRequestSnapshotResetAttribute(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    DryRun: Optional[bool] = None


# This class is the input for the 'reset_snapshot_attribute' function.
class ResetSnapshotAttributeRequest(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    SnapshotId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'restore_address_to_classic' function.
class RestoreAddressToClassicRequest(BaseValidatorModel):
    PublicIp: str
    DryRun: Optional[bool] = None


# This class is the input for the 'restore_image_from_recycle_bin' function.
class RestoreImageFromRecycleBinRequest(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'restore_managed_prefix_list_version' function.
class RestoreManagedPrefixListVersionRequest(BaseValidatorModel):
    PrefixListId: str
    PreviousVersion: int
    CurrentVersion: int
    DryRun: Optional[bool] = None


# This class is the input for the 'restore_snapshot_from_recycle_bin' function.
class RestoreSnapshotFromRecycleBinRequest(BaseValidatorModel):
    SnapshotId: str
    DryRun: Optional[bool] = None


# This class is the input for the 'restore_snapshot_tier' function.
class RestoreSnapshotTierRequest(BaseValidatorModel):
    SnapshotId: str
    TemporaryRestoreDays: Optional[int] = None
    PermanentRestore: Optional[bool] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'revoke_client_vpn_ingress' function.
class RevokeClientVpnIngressRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    TargetNetworkCidr: str
    AccessGroupId: Optional[str] = None
    RevokeAllGroups: Optional[bool] = None
    DryRun: Optional[bool] = None


class RevokedSecurityGroupRule(BaseValidatorModel):
    SecurityGroupRuleId: Optional[str] = None
    GroupId: Optional[str] = None
    IsEgress: Optional[bool] = None
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIpv4: Optional[str] = None
    CidrIpv6: Optional[str] = None
    PrefixListId: Optional[str] = None
    ReferencedGroupId: Optional[str] = None
    Description: Optional[str] = None


class Route(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    NatGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    Origin: Optional[RouteOriginType] = None
    State: Optional[RouteStateType] = None
    VpcPeeringConnectionId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None


class S3StorageOutput(BaseValidatorModel):
    AWSAccessKeyId: Optional[str] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None
    UploadPolicy: Optional[bytes] = None
    UploadPolicySignature: Optional[str] = None


class ScheduledInstanceRecurrence(BaseValidatorModel):
    Frequency: Optional[str] = None
    Interval: Optional[int] = None
    OccurrenceDaySet: Optional[List[int]] = None
    OccurrenceRelativeToEnd: Optional[bool] = None
    OccurrenceUnit: Optional[str] = None


class ScheduledInstancesEbs(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None


class ScheduledInstancesIamInstanceProfile(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None


class ScheduledInstancesIpv6Address(BaseValidatorModel):
    Ipv6Address: Optional[str] = None


class ScheduledInstancesMonitoring(BaseValidatorModel):
    Enabled: Optional[bool] = None


class ScheduledInstancesPlacement(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None


class ScheduledInstancesPrivateIpAddressConfig(BaseValidatorModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None


class TransitGatewayMulticastGroup(BaseValidatorModel):
    GroupIpAddress: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SubnetId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    GroupMember: Optional[bool] = None
    GroupSource: Optional[bool] = None
    MemberType: Optional[MembershipTypeType] = None
    SourceType: Optional[MembershipTypeType] = None


class SecurityGroupIdentifier(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None


class SecurityGroupRuleDescription(BaseValidatorModel):
    SecurityGroupRuleId: Optional[str] = None
    Description: Optional[str] = None


class SecurityGroupRuleRequest(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIpv4: Optional[str] = None
    CidrIpv6: Optional[str] = None
    PrefixListId: Optional[str] = None
    ReferencedGroupId: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'send_diagnostic_interrupt' function.
class SendDiagnosticInterruptRequest(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None


class ServiceTypeDetail(BaseValidatorModel):
    ServiceType: Optional[ServiceTypeType] = None


class SupportedRegionDetail(BaseValidatorModel):
    Region: Optional[str] = None
    ServiceState: Optional[str] = None


class UserBucketDetails(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None


class SpotCapacityRebalance(BaseValidatorModel):
    ReplacementStrategy: Optional[ReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None


class SpotInstanceStateFault(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class SpotFleetMonitoring(BaseValidatorModel):
    Enabled: Optional[bool] = None


class SpotInstanceStatus(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None
    UpdateTime: Optional[datetime] = None


class StartInstancesRequestInstanceStart(BaseValidatorModel):
    AdditionalInfo: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'start_instances' function.
class StartInstancesRequest(BaseValidatorModel):
    InstanceIds: List[str]
    AdditionalInfo: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'start_vpc_endpoint_service_private_dns_verification' function.
class StartVpcEndpointServicePrivateDnsVerificationRequest(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None


class StopInstancesRequestInstanceStop(BaseValidatorModel):
    Hibernate: Optional[bool] = None
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None


# This class is the input for the 'stop_instances' function.
class StopInstancesRequest(BaseValidatorModel):
    InstanceIds: List[str]
    Hibernate: Optional[bool] = None
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None


class SubnetAssociation(BaseValidatorModel):
    SubnetId: Optional[str] = None
    State: Optional[TransitGatewayMulitcastDomainAssociationStateType] = None


class SubnetCidrBlockState(BaseValidatorModel):
    State: Optional[SubnetCidrBlockStateCodeType] = None
    StatusMessage: Optional[str] = None


class SubnetIpPrefixes(BaseValidatorModel):
    SubnetId: Optional[str] = None
    IpPrefixes: Optional[List[str]] = None


class TargetConfiguration(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    OfferingId: Optional[str] = None


class TargetGroup(BaseValidatorModel):
    Arn: Optional[str] = None


# This class is the input for the 'terminate_client_vpn_connections' function.
class TerminateClientVpnConnectionsRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    ConnectionId: Optional[str] = None
    Username: Optional[str] = None
    DryRun: Optional[bool] = None


class TerminateInstancesRequestInstanceTerminate(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'terminate_instances' function.
class TerminateInstancesRequest(BaseValidatorModel):
    InstanceIds: List[str]
    DryRun: Optional[bool] = None


class TrafficMirrorPortRange(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class TransitGatewayAttachmentAssociation(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayAssociationStateType] = None


class TransitGatewayAttachmentBgpConfiguration(BaseValidatorModel):
    TransitGatewayAsn: Optional[int] = None
    PeerAsn: Optional[int] = None
    TransitGatewayAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    BgpStatus: Optional[BgpStatusType] = None


class TransitGatewayConnectOptions(BaseValidatorModel):
    Protocol: Optional[Literal['gre']] = None


class TransitGatewayMulticastDomainOptions(BaseValidatorModel):
    Igmpv2Support: Optional[Igmpv2SupportValueType] = None
    StaticSourcesSupport: Optional[StaticSourcesSupportValueType] = None
    AutoAcceptSharedAssociations: Optional[AutoAcceptSharedAssociationsValueType] = None


class TransitGatewayOptions(BaseValidatorModel):
    AmazonSideAsn: Optional[int] = None
    TransitGatewayCidrBlocks: Optional[List[str]] = None
    AutoAcceptSharedAttachments: Optional[AutoAcceptSharedAttachmentsValueType] = None
    DefaultRouteTableAssociation: Optional[DefaultRouteTableAssociationValueType] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    DefaultRouteTablePropagation: Optional[DefaultRouteTablePropagationValueType] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    VpnEcmpSupport: Optional[VpnEcmpSupportValueType] = None
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    MulticastSupport: Optional[MulticastSupportValueType] = None


class TransitGatewayPeeringAttachmentOptions(BaseValidatorModel):
    DynamicRouting: Optional[DynamicRoutingValueType] = None


class TransitGatewayPolicyRuleMetaData(BaseValidatorModel):
    MetaDataKey: Optional[str] = None
    MetaDataValue: Optional[str] = None


class TransitGatewayPrefixListAttachment(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceId: Optional[str] = None


class TransitGatewayRouteAttachment(BaseValidatorModel):
    ResourceId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None


class TransitGatewayVpcAttachmentOptions(BaseValidatorModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None


# This class is the input for the 'unassign_ipv6_addresses' function.
class UnassignIpv6AddressesRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    Ipv6Prefixes: Optional[List[str]] = None
    Ipv6Addresses: Optional[List[str]] = None


class UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddresses(BaseValidatorModel):
    Ipv4Prefixes: Optional[List[str]] = None
    PrivateIpAddresses: Optional[List[str]] = None


# This class is the input for the 'unassign_private_ip_addresses' function.
class UnassignPrivateIpAddressesRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    Ipv4Prefixes: Optional[List[str]] = None
    PrivateIpAddresses: Optional[List[str]] = None


# This class is the input for the 'unassign_private_nat_gateway_address' function.
class UnassignPrivateNatGatewayAddressRequest(BaseValidatorModel):
    NatGatewayId: str
    PrivateIpAddresses: List[str]
    MaxDrainDurationSeconds: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'unlock_snapshot' function.
class UnlockSnapshotRequest(BaseValidatorModel):
    SnapshotId: str
    DryRun: Optional[bool] = None


class UnmonitorInstancesRequestInstanceUnmonitor(BaseValidatorModel):
    DryRun: Optional[bool] = None


# This class is the input for the 'unmonitor_instances' function.
class UnmonitorInstancesRequest(BaseValidatorModel):
    InstanceIds: List[str]
    DryRun: Optional[bool] = None


class UnsuccessfulInstanceCreditSpecificationItemError(BaseValidatorModel):
    Code: Optional[UnsuccessfulInstanceCreditSpecificationErrorCodeType] = None
    Message: Optional[str] = None


class UnsuccessfulItemError(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class ValidationError(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None


class VerifiedAccessEndpointPortRange(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None


class VerifiedAccessEndpointRdsOptions(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    RdsDbInstanceArn: Optional[str] = None
    RdsDbClusterArn: Optional[str] = None
    RdsDbProxyArn: Optional[str] = None
    RdsEndpoint: Optional[str] = None
    SubnetIds: Optional[List[str]] = None


class VerifiedAccessEndpointStatus(BaseValidatorModel):
    Code: Optional[VerifiedAccessEndpointStatusCodeType] = None
    Message: Optional[str] = None


class VerifiedAccessInstanceCustomSubDomain(BaseValidatorModel):
    SubDomain: Optional[str] = None
    Nameservers: Optional[List[str]] = None


class VerifiedAccessInstanceOpenVpnClientConfigurationRoute(BaseValidatorModel):
    Cidr: Optional[str] = None


class VerifiedAccessTrustProviderCondensed(BaseValidatorModel):
    VerifiedAccessTrustProviderId: Optional[str] = None
    Description: Optional[str] = None
    TrustProviderType: Optional[TrustProviderTypeType] = None
    UserTrustProviderType: Optional[UserTrustProviderTypeType] = None
    DeviceTrustProviderType: Optional[DeviceTrustProviderTypeType] = None


class VerifiedAccessLogCloudWatchLogsDestinationOptions(BaseValidatorModel):
    Enabled: bool
    LogGroup: Optional[str] = None


class VerifiedAccessLogDeliveryStatus(BaseValidatorModel):
    Code: Optional[VerifiedAccessLogDeliveryStatusCodeType] = None
    Message: Optional[str] = None


class VerifiedAccessLogKinesisDataFirehoseDestinationOptions(BaseValidatorModel):
    Enabled: bool
    DeliveryStream: Optional[str] = None


class VerifiedAccessLogS3DestinationOptions(BaseValidatorModel):
    Enabled: bool
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None


class VgwTelemetry(BaseValidatorModel):
    AcceptedRouteCount: Optional[int] = None
    LastStatusChange: Optional[datetime] = None
    OutsideIpAddress: Optional[str] = None
    Status: Optional[TelemetryStatusType] = None
    StatusMessage: Optional[str] = None
    CertificateArn: Optional[str] = None


class VolumeAttachment(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    AssociatedResource: Optional[str] = None
    InstanceOwningService: Optional[str] = None
    VolumeId: Optional[str] = None
    InstanceId: Optional[str] = None
    Device: Optional[str] = None
    State: Optional[VolumeAttachmentStateType] = None
    AttachTime: Optional[datetime] = None


class VolumeStatusAction(BaseValidatorModel):
    Code: Optional[str] = None
    Description: Optional[str] = None
    EventId: Optional[str] = None
    EventType: Optional[str] = None


class VolumeStatusAttachmentStatus(BaseValidatorModel):
    IoPerformance: Optional[str] = None
    InstanceId: Optional[str] = None


class VolumeStatusDetails(BaseValidatorModel):
    Name: Optional[VolumeStatusNameType] = None
    Status: Optional[str] = None


class VolumeStatusEvent(BaseValidatorModel):
    Description: Optional[str] = None
    EventId: Optional[str] = None
    EventType: Optional[str] = None
    NotAfter: Optional[datetime] = None
    NotBefore: Optional[datetime] = None
    InstanceId: Optional[str] = None


class VpcCidrBlockState(BaseValidatorModel):
    State: Optional[VpcCidrBlockStateCodeType] = None
    StatusMessage: Optional[str] = None


class VpcEncryptionControlExclusion(BaseValidatorModel):
    State: Optional[VpcEncryptionControlExclusionStateType] = None
    StateMessage: Optional[str] = None


class VpcPeeringConnectionOptionsDescription(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None


class VpcPeeringConnectionStateReason(BaseValidatorModel):
    Code: Optional[VpcPeeringConnectionStateReasonCodeType] = None
    Message: Optional[str] = None


class VpnStaticRoute(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    Source: Optional[Literal['Static']] = None
    State: Optional[VpnStateType] = None


# This class is the input for the 'withdraw_byoip_cidr' function.
class WithdrawByoipCidrRequest(BaseValidatorModel):
    Cidr: str
    DryRun: Optional[bool] = None


# This class is the output for the 'accept_address_transfer' function.
class AcceptAddressTransferResult(BaseValidatorModel):
    AddressTransfer: AddressTransfer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_capacity_reservation_billing_ownership' function.
class AcceptCapacityReservationBillingOwnershipResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_reserved_instances_exchange_quote' function.
class AcceptReservedInstancesExchangeQuoteResult(BaseValidatorModel):
    ExchangeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'allocate_address' function.
class AllocateAddressResult(BaseValidatorModel):
    AllocationId: str
    PublicIpv4Pool: str
    NetworkBorderGroup: str
    Domain: DomainTypeType
    CustomerOwnedIp: str
    CustomerOwnedIpv4Pool: str
    CarrierIp: str
    PublicIp: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'allocate_hosts' function.
class AllocateHostsResult(BaseValidatorModel):
    HostIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'apply_security_groups_to_client_vpn_target_network' function.
class ApplySecurityGroupsToClientVpnTargetNetworkResult(BaseValidatorModel):
    SecurityGroupIds: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'assign_ipv6_addresses' function.
class AssignIpv6AddressesResult(BaseValidatorModel):
    AssignedIpv6Addresses: List[str]
    AssignedIpv6Prefixes: List[str]
    NetworkInterfaceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_address' function.
class AssociateAddressResult(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_capacity_reservation_billing_owner' function.
class AssociateCapacityReservationBillingOwnerResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_enclave_certificate_iam_role' function.
class AssociateEnclaveCertificateIamRoleResult(BaseValidatorModel):
    CertificateS3BucketName: str
    CertificateS3ObjectKey: str
    EncryptionKmsKeyId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_security_group_vpc' function.
class AssociateSecurityGroupVpcResult(BaseValidatorModel):
    State: SecurityGroupVpcAssociationStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_classic_link_vpc' function.
class AttachClassicLinkVpcResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_network_interface' function.
class AttachNetworkInterfaceResult(BaseValidatorModel):
    AttachmentId: str
    NetworkCardIndex: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_capacity_reservation' function.
class CancelCapacityReservationResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_declarative_policies_report' function.
class CancelDeclarativePoliciesReportResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_image_launch_permission' function.
class CancelImageLaunchPermissionResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_import_task' function.
class CancelImportTaskResult(BaseValidatorModel):
    ImportTaskId: str
    PreviousState: str
    State: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'confirm_product_instance' function.
class ConfirmProductInstanceResult(BaseValidatorModel):
    Return: bool
    OwnerId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_fpga_image' function.
class CopyFpgaImageResult(BaseValidatorModel):
    FpgaImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_image' function.
class CopyImageResult(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_fpga_image' function.
class CreateFpgaImageResult(BaseValidatorModel):
    FpgaImageId: str
    FpgaImageGlobalId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_image' function.
class CreateImageResult(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_public_ipv4_pool' function.
class CreatePublicIpv4PoolResult(BaseValidatorModel):
    PoolId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_restore_image_task' function.
class CreateRestoreImageTaskResult(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_route' function.
class CreateRouteResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_store_image_task' function.
class CreateStoreImageTaskResult(BaseValidatorModel):
    ObjectKey: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_egress_only_internet_gateway' function.
class DeleteEgressOnlyInternetGatewayResult(BaseValidatorModel):
    ReturnCode: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_fpga_image' function.
class DeleteFpgaImageResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_key_pair' function.
class DeleteKeyPairResult(BaseValidatorModel):
    Return: bool
    KeyPairId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_nat_gateway' function.
class DeleteNatGatewayResult(BaseValidatorModel):
    NatGatewayId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_network_insights_access_scope_analysis' function.
class DeleteNetworkInsightsAccessScopeAnalysisResult(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_network_insights_access_scope' function.
class DeleteNetworkInsightsAccessScopeResult(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_network_insights_analysis' function.
class DeleteNetworkInsightsAnalysisResult(BaseValidatorModel):
    NetworkInsightsAnalysisId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_network_insights_path' function.
class DeleteNetworkInsightsPathResult(BaseValidatorModel):
    NetworkInsightsPathId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_network_interface_permission' function.
class DeleteNetworkInterfacePermissionResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_public_ipv4_pool' function.
class DeletePublicIpv4PoolResult(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_security_group' function.
class DeleteSecurityGroupResult(BaseValidatorModel):
    Return: bool
    GroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_traffic_mirror_filter' function.
class DeleteTrafficMirrorFilterResult(BaseValidatorModel):
    TrafficMirrorFilterId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_traffic_mirror_filter_rule' function.
class DeleteTrafficMirrorFilterRuleResult(BaseValidatorModel):
    TrafficMirrorFilterRuleId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_traffic_mirror_session' function.
class DeleteTrafficMirrorSessionResult(BaseValidatorModel):
    TrafficMirrorSessionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_traffic_mirror_target' function.
class DeleteTrafficMirrorTargetResult(BaseValidatorModel):
    TrafficMirrorTargetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_peering_connection' function.
class DeleteVpcPeeringConnectionResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deprovision_public_ipv4_pool_cidr' function.
class DeprovisionPublicIpv4PoolCidrResult(BaseValidatorModel):
    PoolId: str
    DeprovisionedAddresses: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_address_transfers' function.
class DescribeAddressTransfersResult(BaseValidatorModel):
    AddressTransfers: List[AddressTransfer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'detach_classic_link_vpc' function.
class DetachClassicLinkVpcResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_address_transfer' function.
class DisableAddressTransferResult(BaseValidatorModel):
    AddressTransfer: AddressTransfer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_allowed_images_settings' function.
class DisableAllowedImagesSettingsResult(BaseValidatorModel):
    AllowedImagesSettingsState: Literal['disabled']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_aws_network_performance_metric_subscription' function.
class DisableAwsNetworkPerformanceMetricSubscriptionResult(BaseValidatorModel):
    Output: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_ebs_encryption_by_default' function.
class DisableEbsEncryptionByDefaultResult(BaseValidatorModel):
    EbsEncryptionByDefault: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_image_block_public_access' function.
class DisableImageBlockPublicAccessResult(BaseValidatorModel):
    ImageBlockPublicAccessState: Literal['unblocked']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_image_deprecation' function.
class DisableImageDeprecationResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_image_deregistration_protection' function.
class DisableImageDeregistrationProtectionResult(BaseValidatorModel):
    Return: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_image' function.
class DisableImageResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_ipam_organization_admin_account' function.
class DisableIpamOrganizationAdminAccountResult(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_serial_console_access' function.
class DisableSerialConsoleAccessResult(BaseValidatorModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_snapshot_block_public_access' function.
class DisableSnapshotBlockPublicAccessResult(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_vpc_classic_link_dns_support' function.
class DisableVpcClassicLinkDnsSupportResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disable_vpc_classic_link' function.
class DisableVpcClassicLinkResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_capacity_reservation_billing_owner' function.
class DisassociateCapacityReservationBillingOwnerResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_enclave_certificate_iam_role' function.
class DisassociateEnclaveCertificateIamRoleResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_security_group_vpc' function.
class DisassociateSecurityGroupVpcResult(BaseValidatorModel):
    State: SecurityGroupVpcAssociationStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_trunk_interface' function.
class DisassociateTrunkInterfaceResult(BaseValidatorModel):
    Return: bool
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unassign_private_ip_addresses' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_address_transfer' function.
class EnableAddressTransferResult(BaseValidatorModel):
    AddressTransfer: AddressTransfer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_allowed_images_settings' function.
class EnableAllowedImagesSettingsResult(BaseValidatorModel):
    AllowedImagesSettingsState: AllowedImagesSettingsEnabledStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_aws_network_performance_metric_subscription' function.
class EnableAwsNetworkPerformanceMetricSubscriptionResult(BaseValidatorModel):
    Output: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_ebs_encryption_by_default' function.
class EnableEbsEncryptionByDefaultResult(BaseValidatorModel):
    EbsEncryptionByDefault: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_image_block_public_access' function.
class EnableImageBlockPublicAccessResult(BaseValidatorModel):
    ImageBlockPublicAccessState: Literal['block-new-sharing']
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_image_deprecation' function.
class EnableImageDeprecationResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_image_deregistration_protection' function.
class EnableImageDeregistrationProtectionResult(BaseValidatorModel):
    Return: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_image' function.
class EnableImageResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_ipam_organization_admin_account' function.
class EnableIpamOrganizationAdminAccountResult(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_reachability_analyzer_organization_sharing' function.
class EnableReachabilityAnalyzerOrganizationSharingResult(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_serial_console_access' function.
class EnableSerialConsoleAccessResult(BaseValidatorModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_snapshot_block_public_access' function.
class EnableSnapshotBlockPublicAccessResult(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_vpc_classic_link_dns_support' function.
class EnableVpcClassicLinkDnsSupportResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_vpc_classic_link' function.
class EnableVpcClassicLinkResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_client_vpn_client_configuration' function.
class ExportClientVpnClientConfigurationResult(BaseValidatorModel):
    ClientConfiguration: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_transit_gateway_routes' function.
class ExportTransitGatewayRoutesResult(BaseValidatorModel):
    S3Location: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_console_output' function.
class GetConsoleOutputResult(BaseValidatorModel):
    InstanceId: str
    Timestamp: datetime
    Output: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_console_screenshot' function.
class GetConsoleScreenshotResult(BaseValidatorModel):
    ImageData: str
    InstanceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ebs_default_kms_key_id' function.
class GetEbsDefaultKmsKeyIdResult(BaseValidatorModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ebs_encryption_by_default' function.
class GetEbsEncryptionByDefaultResult(BaseValidatorModel):
    EbsEncryptionByDefault: bool
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_flow_logs_integration_template' function.
class GetFlowLogsIntegrationTemplateResult(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_image_block_public_access_state' function.
class GetImageBlockPublicAccessStateResult(BaseValidatorModel):
    ImageBlockPublicAccessState: str
    ManagedBy: ManagedByType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_tpm_ek_pub' function.
class GetInstanceTpmEkPubResult(BaseValidatorModel):
    InstanceId: str
    KeyType: EkPubKeyTypeType
    KeyFormat: EkPubKeyFormatType
    KeyValue: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_uefi_data' function.
class GetInstanceUefiDataResult(BaseValidatorModel):
    InstanceId: str
    UefiData: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_password_data' function.
class GetPasswordDataResult(BaseValidatorModel):
    InstanceId: str
    Timestamp: datetime
    PasswordData: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_serial_console_access_status' function.
class GetSerialConsoleAccessStatusResult(BaseValidatorModel):
    SerialConsoleAccessEnabled: bool
    ManagedBy: ManagedByType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_snapshot_block_public_access_state' function.
class GetSnapshotBlockPublicAccessStateResult(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    ManagedBy: ManagedByType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_verified_access_endpoint_policy' function.
class GetVerifiedAccessEndpointPolicyResult(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_verified_access_group_policy' function.
class GetVerifiedAccessGroupPolicyResult(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_vpn_connection_device_sample_configuration' function.
class GetVpnConnectionDeviceSampleConfigurationResult(BaseValidatorModel):
    VpnConnectionDeviceSampleConfiguration: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_client_vpn_client_certificate_revocation_list' function.
class ImportClientVpnClientCertificateRevocationListResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'lock_snapshot' function.
class LockSnapshotResult(BaseValidatorModel):
    SnapshotId: str
    LockState: LockStateType
    LockDuration: int
    CoolOffPeriod: int
    CoolOffPeriodExpiresOn: datetime
    LockCreatedOn: datetime
    LockExpiresOn: datetime
    LockDurationStartTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_availability_zone_group' function.
class ModifyAvailabilityZoneGroupResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_capacity_reservation_fleet' function.
class ModifyCapacityReservationFleetResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_capacity_reservation' function.
class ModifyCapacityReservationResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_client_vpn_endpoint' function.
class ModifyClientVpnEndpointResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_ebs_default_kms_key_id' function.
class ModifyEbsDefaultKmsKeyIdResult(BaseValidatorModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_fleet' function.
class ModifyFleetResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_capacity_reservation_attributes' function.
class ModifyInstanceCapacityReservationAttributesResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_cpu_options' function.
class ModifyInstanceCpuOptionsResult(BaseValidatorModel):
    InstanceId: str
    CoreCount: int
    ThreadsPerCore: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_maintenance_options' function.
class ModifyInstanceMaintenanceOptionsResult(BaseValidatorModel):
    InstanceId: str
    AutoRecovery: InstanceAutoRecoveryStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_metadata_defaults' function.
class ModifyInstanceMetadataDefaultsResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_network_performance_options' function.
class ModifyInstanceNetworkPerformanceResult(BaseValidatorModel):
    InstanceId: str
    BandwidthWeighting: InstanceBandwidthWeightingType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_placement' function.
class ModifyInstancePlacementResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_private_dns_name_options' function.
class ModifyPrivateDnsNameOptionsResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_reserved_instances' function.
class ModifyReservedInstancesResult(BaseValidatorModel):
    ReservedInstancesModificationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_security_group_rules' function.
class ModifySecurityGroupRulesResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_snapshot_tier' function.
class ModifySnapshotTierResult(BaseValidatorModel):
    SnapshotId: str
    TieringStartTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_spot_fleet_request' function.
class ModifySpotFleetRequestResponse(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpc_endpoint_connection_notification' function.
class ModifyVpcEndpointConnectionNotificationResult(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpc_endpoint' function.
class ModifyVpcEndpointResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpc_endpoint_service_configuration' function.
class ModifyVpcEndpointServiceConfigurationResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpc_endpoint_service_payer_responsibility' function.
class ModifyVpcEndpointServicePayerResponsibilityResult(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpc_tenancy' function.
class ModifyVpcTenancyResult(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'move_address_to_vpc' function.
class MoveAddressToVpcResult(BaseValidatorModel):
    AllocationId: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'purchase_reserved_instances_offering' function.
class PurchaseReservedInstancesOfferingResult(BaseValidatorModel):
    ReservedInstancesId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_image' function.
class RegisterImageResult(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_capacity_reservation_billing_ownership' function.
class RejectCapacityReservationBillingOwnershipResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_vpc_peering_connection' function.
class RejectVpcPeeringConnectionResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'release_ipam_pool_allocation' function.
class ReleaseIpamPoolAllocationResult(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replace_image_criteria_in_allowed_images_settings' function.
class ReplaceImageCriteriaInAllowedImagesSettingsResult(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replace_network_acl_association' function.
class ReplaceNetworkAclAssociationResult(BaseValidatorModel):
    NewAssociationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replace_vpn_tunnel' function.
class ReplaceVpnTunnelResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'request_spot_fleet' function.
class RequestSpotFleetResponse(BaseValidatorModel):
    SpotFleetRequestId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_ebs_default_kms_key_id' function.
class ResetEbsDefaultKmsKeyIdResult(BaseValidatorModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_fpga_image_attribute' function.
class ResetFpgaImageAttributeResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_address_to_classic' function.
class RestoreAddressToClassicResult(BaseValidatorModel):
    PublicIp: str
    Status: StatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_image_from_recycle_bin' function.
class RestoreImageFromRecycleBinResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_snapshot_from_recycle_bin' function.
class RestoreSnapshotFromRecycleBinResult(BaseValidatorModel):
    SnapshotId: str
    OutpostArn: str
    Description: str
    Encrypted: bool
    OwnerId: str
    Progress: str
    StartTime: datetime
    State: SnapshotStateType
    VolumeId: str
    VolumeSize: int
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_snapshot_tier' function.
class RestoreSnapshotTierResult(BaseValidatorModel):
    SnapshotId: str
    RestoreStartTime: datetime
    RestoreDuration: int
    IsPermanentRestore: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'run_scheduled_instances' function.
class RunScheduledInstancesResult(BaseValidatorModel):
    InstanceIdSet: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_declarative_policies_report' function.
class StartDeclarativePoliciesReportResult(BaseValidatorModel):
    ReportId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_vpc_endpoint_service_private_dns_verification' function.
class StartVpcEndpointServicePrivateDnsVerificationResult(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unassign_ipv6_addresses' function.
class UnassignIpv6AddressesResult(BaseValidatorModel):
    NetworkInterfaceId: str
    UnassignedIpv6Addresses: List[str]
    UnassignedIpv6Prefixes: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unlock_snapshot' function.
class UnlockSnapshotResult(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_security_group_rule_descriptions_egress' function.
class UpdateSecurityGroupRuleDescriptionsEgressResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_security_group_rule_descriptions_ingress' function.
class UpdateSecurityGroupRuleDescriptionsIngressResult(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'detach_volume' function.
class VolumeAttachmentResponse(BaseValidatorModel):
    DeleteOnTermination: bool
    AssociatedResource: str
    InstanceOwningService: str
    VolumeId: str
    InstanceId: str
    Device: str
    State: VolumeAttachmentStateType
    AttachTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'accept_reserved_instances_exchange_quote' function.
class AcceptReservedInstancesExchangeQuoteRequest(BaseValidatorModel):
    ReservedInstanceIds: List[str]
    DryRun: Optional[bool] = None
    TargetConfigurations: Optional[List[TargetConfigurationRequest]] = None


# This class is the input for the 'get_reserved_instances_exchange_quote' function.
class GetReservedInstancesExchangeQuoteRequest(BaseValidatorModel):
    ReservedInstanceIds: List[str]
    DryRun: Optional[bool] = None
    TargetConfigurations: Optional[List[TargetConfigurationRequest]] = None


class AccountAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[AccountAttributeValue]] = None


# This class is the output for the 'describe_fleet_instances' function.
class DescribeFleetInstancesResult(BaseValidatorModel):
    ActiveInstances: List[ActiveInstance]
    FleetId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_spot_fleet_instances' function.
class DescribeSpotFleetInstancesResponse(BaseValidatorModel):
    ActiveInstances: List[ActiveInstance]
    SpotFleetRequestId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_vpc_endpoint_service_permissions' function.
class ModifyVpcEndpointServicePermissionsResult(BaseValidatorModel):
    AddedPrincipals: List[AddedPrincipal]
    ReturnValue: bool
    ResponseMetadata: ResponseMetadata


class AnalysisLoadBalancerTarget(BaseValidatorModel):
    Address: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Instance: Optional[AnalysisComponent] = None
    Port: Optional[int] = None


class RuleGroupRuleOptionsPair(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    RuleOptions: Optional[List[RuleOption]] = None


class AddressAttribute(BaseValidatorModel):
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    PtrRecord: Optional[str] = None
    PtrRecordUpdate: Optional[PtrUpdateStatus] = None


class Address(BaseValidatorModel):
    AllocationId: Optional[str] = None
    AssociationId: Optional[str] = None
    Domain: Optional[DomainTypeType] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfaceOwnerId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    PublicIpv4Pool: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    CarrierIp: Optional[str] = None
    ServiceManaged: Optional[ServiceManagedType] = None
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None


class AllowedPrincipal(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None
    ServicePermissionId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ServiceId: Optional[str] = None


class CarrierGateway(BaseValidatorModel):
    CarrierGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    State: Optional[CarrierGatewayStateType] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_tags' function.
class ClientCreateTagsRequest(BaseValidatorModel):
    Resources: List[str]
    Tags: List[Tag]
    DryRun: Optional[bool] = None


# This class is the input for the 'delete_tags' function.
class ClientDeleteTagsRequest(BaseValidatorModel):
    Resources: List[str]
    Tags: Optional[List[Tag]] = None
    DryRun: Optional[bool] = None


class CoipPool(BaseValidatorModel):
    PoolId: Optional[str] = None
    PoolCidrs: Optional[List[str]] = None
    LocalGatewayRouteTableId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    PoolArn: Optional[str] = None


# This class is the output for the 'copy_snapshot' function.
class CopySnapshotResult(BaseValidatorModel):
    Tags: List[Tag]
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_security_group' function.
class CreateSecurityGroupResult(BaseValidatorModel):
    GroupId: str
    Tags: List[Tag]
    SecurityGroupArn: str
    ResponseMetadata: ResponseMetadata


class CreateTagsRequestServiceResourceCreateTags(BaseValidatorModel):
    Resources: List[str]
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class CustomerGateway(BaseValidatorModel):
    CertificateArn: Optional[str] = None
    DeviceName: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    BgpAsnExtended: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    State: Optional[str] = None
    Type: Optional[str] = None
    IpAddress: Optional[str] = None
    BgpAsn: Optional[str] = None


class DeclarativePoliciesReport(BaseValidatorModel):
    ReportId: Optional[str] = None
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None
    TargetId: Optional[str] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Status: Optional[ReportStateType] = None
    Tags: Optional[List[Tag]] = None


class DhcpOptionsCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class Ec2InstanceConnectEndpoint(BaseValidatorModel):
    OwnerId: Optional[str] = None
    InstanceConnectEndpointId: Optional[str] = None
    InstanceConnectEndpointArn: Optional[str] = None
    State: Optional[Ec2InstanceConnectEndpointStateType] = None
    StateMessage: Optional[str] = None
    DnsName: Optional[str] = None
    FipsDnsName: Optional[str] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    SubnetId: Optional[str] = None
    PreserveClientIp: Optional[bool] = None
    SecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


class HostReservation(BaseValidatorModel):
    Count: Optional[int] = None
    CurrencyCode: Optional[Literal['USD']] = None
    Duration: Optional[int] = None
    End: Optional[datetime] = None
    HostIdSet: Optional[List[str]] = None
    HostReservationId: Optional[str] = None
    HourlyPrice: Optional[str] = None
    InstanceFamily: Optional[str] = None
    OfferingId: Optional[str] = None
    PaymentOption: Optional[PaymentOptionType] = None
    Start: Optional[datetime] = None
    State: Optional[ReservationStateType] = None
    UpfrontPrice: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ImageCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


# This class is the output for the 'import_key_pair' function.
class ImportKeyPairResult(BaseValidatorModel):
    KeyFingerprint: str
    KeyName: str
    KeyPairId: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class InstanceCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class InstanceDeleteTagsRequest(BaseValidatorModel):
    Tags: Optional[List[Tag]] = None
    DryRun: Optional[bool] = None


class InstanceEventWindowAssociationRequest(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    InstanceTags: Optional[List[Tag]] = None
    DedicatedHostIds: Optional[List[str]] = None


class InstanceEventWindowAssociationTarget(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    DedicatedHostIds: Optional[List[str]] = None


class InstanceEventWindowDisassociationRequest(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    InstanceTags: Optional[List[Tag]] = None
    DedicatedHostIds: Optional[List[str]] = None


class InternetGatewayCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class IpamExternalResourceVerificationToken(BaseValidatorModel):
    IpamExternalResourceVerificationTokenId: Optional[str] = None
    IpamExternalResourceVerificationTokenArn: Optional[str] = None
    IpamId: Optional[str] = None
    IpamArn: Optional[str] = None
    IpamRegion: Optional[str] = None
    TokenValue: Optional[str] = None
    TokenName: Optional[str] = None
    NotAfter: Optional[datetime] = None
    Status: Optional[TokenStateType] = None
    Tags: Optional[List[Tag]] = None
    State: Optional[IpamExternalResourceVerificationTokenStateType] = None


class IpamResourceDiscoveryAssociation(BaseValidatorModel):
    OwnerId: Optional[str] = None
    IpamResourceDiscoveryAssociationId: Optional[str] = None
    IpamResourceDiscoveryAssociationArn: Optional[str] = None
    IpamResourceDiscoveryId: Optional[str] = None
    IpamId: Optional[str] = None
    IpamArn: Optional[str] = None
    IpamRegion: Optional[str] = None
    IsDefault: Optional[bool] = None
    ResourceDiscoveryStatus: Optional[IpamAssociatedResourceDiscoveryStatusType] = None
    State: Optional[IpamResourceDiscoveryAssociationStateType] = None
    Tags: Optional[List[Tag]] = None


class IpamScope(BaseValidatorModel):
    OwnerId: Optional[str] = None
    IpamScopeId: Optional[str] = None
    IpamScopeArn: Optional[str] = None
    IpamArn: Optional[str] = None
    IpamRegion: Optional[str] = None
    IpamScopeType: Optional[IpamScopeTypeType] = None
    IsDefault: Optional[bool] = None
    Description: Optional[str] = None
    PoolCount: Optional[int] = None
    State: Optional[IpamScopeStateType] = None
    Tags: Optional[List[Tag]] = None


class KeyPairInfo(BaseValidatorModel):
    KeyPairId: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Tags: Optional[List[Tag]] = None
    PublicKey: Optional[str] = None
    CreateTime: Optional[datetime] = None
    KeyName: Optional[str] = None
    KeyFingerprint: Optional[str] = None


# This class is the output for the 'create_key_pair' function.
class KeyPair(BaseValidatorModel):
    KeyPairId: str
    Tags: List[Tag]
    KeyName: str
    KeyFingerprint: str
    KeyMaterial: str
    ResponseMetadata: ResponseMetadata


class LaunchTemplateTagSpecificationRequest(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[Tag]] = None


class LaunchTemplateTagSpecification(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[Tag]] = None


class LocalGatewayRouteTableVirtualInterfaceGroupAssociation(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class LocalGatewayRouteTableVpcAssociation(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class LocalGateway(BaseValidatorModel):
    LocalGatewayId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class LocalGatewayVirtualInterfaceGroup(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    LocalGatewayVirtualInterfaceIds: Optional[List[str]] = None
    LocalGatewayId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class LocalGatewayVirtualInterface(BaseValidatorModel):
    LocalGatewayVirtualInterfaceId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    Vlan: Optional[int] = None
    LocalAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    LocalBgpAsn: Optional[int] = None
    PeerBgpAsn: Optional[int] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ManagedPrefixList(BaseValidatorModel):
    PrefixListId: Optional[str] = None
    AddressFamily: Optional[str] = None
    State: Optional[PrefixListStateType] = None
    StateMessage: Optional[str] = None
    PrefixListArn: Optional[str] = None
    PrefixListName: Optional[str] = None
    MaxEntries: Optional[int] = None
    Version: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    OwnerId: Optional[str] = None


class NetworkAclCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class NetworkInsightsAccessScopeAnalysis(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: Optional[str] = None
    NetworkInsightsAccessScopeAnalysisArn: Optional[str] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    Status: Optional[AnalysisStatusType] = None
    StatusMessage: Optional[str] = None
    WarningMessage: Optional[str] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    FindingsFound: Optional[FindingsFoundType] = None
    AnalyzedEniCount: Optional[int] = None
    Tags: Optional[List[Tag]] = None


class NetworkInsightsAccessScope(BaseValidatorModel):
    NetworkInsightsAccessScopeId: Optional[str] = None
    NetworkInsightsAccessScopeArn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class NetworkInterfaceCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class PlacementGroup(BaseValidatorModel):
    GroupName: Optional[str] = None
    State: Optional[PlacementGroupStateType] = None
    Strategy: Optional[PlacementStrategyType] = None
    PartitionCount: Optional[int] = None
    GroupId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    GroupArn: Optional[str] = None
    SpreadLevel: Optional[SpreadLevelType] = None


class ReplaceRootVolumeTask(BaseValidatorModel):
    ReplaceRootVolumeTaskId: Optional[str] = None
    InstanceId: Optional[str] = None
    TaskState: Optional[ReplaceRootVolumeTaskStateType] = None
    StartTime: Optional[str] = None
    CompleteTime: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ImageId: Optional[str] = None
    SnapshotId: Optional[str] = None
    DeleteReplacedRootVolume: Optional[bool] = None


class RouteTableCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class SecurityGroupCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class SecurityGroupForVpc(BaseValidatorModel):
    Description: Optional[str] = None
    GroupName: Optional[str] = None
    OwnerId: Optional[str] = None
    GroupId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    PrimaryVpcId: Optional[str] = None


class SnapshotCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class SnapshotInfo(BaseValidatorModel):
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Encrypted: Optional[bool] = None
    VolumeId: Optional[str] = None
    State: Optional[SnapshotStateType] = None
    VolumeSize: Optional[int] = None
    StartTime: Optional[datetime] = None
    Progress: Optional[str] = None
    OwnerId: Optional[str] = None
    SnapshotId: Optional[str] = None
    OutpostArn: Optional[str] = None
    SseType: Optional[SSETypeType] = None
    AvailabilityZone: Optional[str] = None


# This class is the output for the 'create_snapshot' function.
class SnapshotResponse(BaseValidatorModel):
    OwnerAlias: str
    OutpostArn: str
    Tags: List[Tag]
    StorageTier: StorageTierType
    RestoreExpiryTime: datetime
    SseType: SSETypeType
    AvailabilityZone: str
    TransferType: TransferTypeType
    CompletionDurationMinutes: int
    CompletionTime: datetime
    FullSnapshotSizeInBytes: int
    SnapshotId: str
    VolumeId: str
    State: SnapshotStateType
    StateMessage: str
    StartTime: datetime
    Progress: str
    OwnerId: str
    Description: str
    VolumeSize: int
    Encrypted: bool
    KmsKeyId: str
    DataEncryptionKeyId: str
    ResponseMetadata: ResponseMetadata


class SnapshotTierStatus(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    VolumeId: Optional[str] = None
    Status: Optional[SnapshotStateType] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    StorageTier: Optional[StorageTierType] = None
    LastTieringStartTime: Optional[datetime] = None
    LastTieringProgress: Optional[int] = None
    LastTieringOperationStatus: Optional[TieringOperationStatusType] = None
    LastTieringOperationStatusDetail: Optional[str] = None
    ArchivalCompleteTime: Optional[datetime] = None
    RestoreExpiryTime: Optional[datetime] = None


class Snapshot(BaseValidatorModel):
    OwnerAlias: Optional[str] = None
    OutpostArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    StorageTier: Optional[StorageTierType] = None
    RestoreExpiryTime: Optional[datetime] = None
    SseType: Optional[SSETypeType] = None
    AvailabilityZone: Optional[str] = None
    TransferType: Optional[TransferTypeType] = None
    CompletionDurationMinutes: Optional[int] = None
    CompletionTime: Optional[datetime] = None
    FullSnapshotSizeInBytes: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeId: Optional[str] = None
    State: Optional[SnapshotStateType] = None
    StateMessage: Optional[str] = None
    StartTime: Optional[datetime] = None
    Progress: Optional[str] = None
    OwnerId: Optional[str] = None
    Description: Optional[str] = None
    VolumeSize: Optional[int] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DataEncryptionKeyId: Optional[str] = None


class SpotFleetTagSpecificationOutput(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[Tag]] = None


class SpotFleetTagSpecification(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[Tag]] = None


class SubnetCidrReservation(BaseValidatorModel):
    SubnetCidrReservationId: Optional[str] = None
    SubnetId: Optional[str] = None
    Cidr: Optional[str] = None
    ReservationType: Optional[SubnetCidrReservationTypeType] = None
    OwnerId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class SubnetCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class TagSpecificationOutput(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[Tag]] = None


class TagSpecification(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[Tag]] = None


class TrafficMirrorSession(BaseValidatorModel):
    TrafficMirrorSessionId: Optional[str] = None
    TrafficMirrorTargetId: Optional[str] = None
    TrafficMirrorFilterId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    OwnerId: Optional[str] = None
    PacketLength: Optional[int] = None
    SessionNumber: Optional[int] = None
    VirtualNetworkId: Optional[int] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TrafficMirrorTarget(BaseValidatorModel):
    TrafficMirrorTargetId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkLoadBalancerArn: Optional[str] = None
    Type: Optional[TrafficMirrorTargetTypeType] = None
    Description: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    GatewayLoadBalancerEndpointId: Optional[str] = None


class TransitGatewayPolicyTable(BaseValidatorModel):
    TransitGatewayPolicyTableId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayPolicyTableStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class TransitGatewayRouteTableAnnouncement(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    PeerTransitGatewayId: Optional[str] = None
    PeerCoreNetworkId: Optional[str] = None
    PeeringAttachmentId: Optional[str] = None
    AnnouncementDirection: Optional[TransitGatewayRouteTableAnnouncementDirectionType] = None
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayRouteTableAnnouncementStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class TransitGatewayRouteTable(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayRouteTableStateType] = None
    DefaultAssociationRouteTable: Optional[bool] = None
    DefaultPropagationRouteTable: Optional[bool] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class TrunkInterfaceAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    BranchInterfaceId: Optional[str] = None
    TrunkInterfaceId: Optional[str] = None
    InterfaceProtocol: Optional[InterfaceProtocolTypeType] = None
    VlanId: Optional[int] = None
    GreKey: Optional[int] = None
    Tags: Optional[List[Tag]] = None


class VolumeCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


class VpcBlockPublicAccessExclusion(BaseValidatorModel):
    ExclusionId: Optional[str] = None
    InternetGatewayExclusionMode: Optional[InternetGatewayExclusionModeType] = None
    ResourceArn: Optional[str] = None
    State: Optional[VpcBlockPublicAccessExclusionStateType] = None
    Reason: Optional[str] = None
    CreationTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    DeletionTimestamp: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class VpcClassicLink(BaseValidatorModel):
    ClassicLinkEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    VpcId: Optional[str] = None


class VpcCreateTagsRequest(BaseValidatorModel):
    Tags: List[Tag]
    DryRun: Optional[bool] = None


# This class is the output for the 'allocate_ipam_pool_cidr' function.
class AllocateIpamPoolCidrResult(BaseValidatorModel):
    IpamPoolAllocation: IpamPoolAllocation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ipam_pool_allocations' function.
class GetIpamPoolAllocationsResult(BaseValidatorModel):
    IpamPoolAllocations: List[IpamPoolAllocation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AnalysisAclRule(BaseValidatorModel):
    Cidr: Optional[str] = None
    Egress: Optional[bool] = None
    PortRange: Optional[PortRange] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    RuleNumber: Optional[int] = None


class AnalysisPacketHeader(BaseValidatorModel):
    DestinationAddresses: Optional[List[str]] = None
    DestinationPortRanges: Optional[List[PortRange]] = None
    Protocol: Optional[str] = None
    SourceAddresses: Optional[List[str]] = None
    SourcePortRanges: Optional[List[PortRange]] = None


class AnalysisSecurityGroupRule(BaseValidatorModel):
    Cidr: Optional[str] = None
    Direction: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    PortRange: Optional[PortRange] = None
    PrefixListId: Optional[str] = None
    Protocol: Optional[str] = None


class FirewallStatefulRule(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    Sources: Optional[List[str]] = None
    Destinations: Optional[List[str]] = None
    SourcePorts: Optional[List[PortRange]] = None
    DestinationPorts: Optional[List[PortRange]] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    Direction: Optional[str] = None


class FirewallStatelessRule(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    Sources: Optional[List[str]] = None
    Destinations: Optional[List[str]] = None
    SourcePorts: Optional[List[PortRange]] = None
    DestinationPorts: Optional[List[PortRange]] = None
    Protocols: Optional[List[int]] = None
    RuleAction: Optional[str] = None
    Priority: Optional[int] = None


# This class is the output for the 'associate_ipam_byoasn' function.
class AssociateIpamByoasnResult(BaseValidatorModel):
    AsnAssociation: AsnAssociation
    ResponseMetadata: ResponseMetadata


class ByoipCidr(BaseValidatorModel):
    Cidr: Optional[str] = None
    Description: Optional[str] = None
    AsnAssociations: Optional[List[AsnAssociation]] = None
    StatusMessage: Optional[str] = None
    State: Optional[ByoipCidrStateType] = None
    NetworkBorderGroup: Optional[str] = None


# This class is the output for the 'disassociate_ipam_byoasn' function.
class DisassociateIpamByoasnResult(BaseValidatorModel):
    AsnAssociation: AsnAssociation
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'provision_ipam_byoasn' function.
class ProvisionIpamByoasnRequest(BaseValidatorModel):
    IpamId: str
    Asn: str
    AsnAuthorizationContext: AsnAuthorizationContext
    DryRun: Optional[bool] = None


# This class is the output for the 'assign_private_ip_addresses' function.
class AssignPrivateIpAddressesResult(BaseValidatorModel):
    NetworkInterfaceId: str
    AssignedPrivateIpAddresses: List[AssignedPrivateIpAddress]
    AssignedIpv4Prefixes: List[Ipv4PrefixSpecification]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'assign_private_nat_gateway_address' function.
class AssignPrivateNatGatewayAddressResult(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddress]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_nat_gateway_address' function.
class AssociateNatGatewayAddressResult(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddress]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_nat_gateway_address' function.
class DisassociateNatGatewayAddressResult(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddress]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unassign_private_nat_gateway_address' function.
class UnassignPrivateNatGatewayAddressResult(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddress]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_client_vpn_target_network' function.
class AssociateClientVpnTargetNetworkResult(BaseValidatorModel):
    AssociationId: str
    Status: AssociationStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_client_vpn_target_network' function.
class DisassociateClientVpnTargetNetworkResult(BaseValidatorModel):
    AssociationId: str
    Status: AssociationStatus
    ResponseMetadata: ResponseMetadata


class TargetNetwork(BaseValidatorModel):
    AssociationId: Optional[str] = None
    VpcId: Optional[str] = None
    TargetNetworkId: Optional[str] = None
    ClientVpnEndpointId: Optional[str] = None
    Status: Optional[AssociationStatus] = None
    SecurityGroups: Optional[List[str]] = None


# This class is the input for the 'associate_iam_instance_profile' function.
class AssociateIamInstanceProfileRequest(BaseValidatorModel):
    IamInstanceProfile: IamInstanceProfileSpecification
    InstanceId: str


# This class is the input for the 'replace_iam_instance_profile_association' function.
class ReplaceIamInstanceProfileAssociationRequest(BaseValidatorModel):
    IamInstanceProfile: IamInstanceProfileSpecification
    AssociationId: str


# This class is the output for the 'associate_route_table' function.
class AssociateRouteTableResult(BaseValidatorModel):
    AssociationId: str
    AssociationState: RouteTableAssociationState
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replace_route_table_association' function.
class ReplaceRouteTableAssociationResult(BaseValidatorModel):
    NewAssociationId: str
    AssociationState: RouteTableAssociationState
    ResponseMetadata: ResponseMetadata


class RouteTableAssociation(BaseValidatorModel):
    Main: Optional[bool] = None
    RouteTableAssociationId: Optional[str] = None
    RouteTableId: Optional[str] = None
    SubnetId: Optional[str] = None
    GatewayId: Optional[str] = None
    AssociationState: Optional[RouteTableAssociationState] = None


# This class is the output for the 'associate_transit_gateway_policy_table' function.
class AssociateTransitGatewayPolicyTableResult(BaseValidatorModel):
    Association: TransitGatewayPolicyTableAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_transit_gateway_policy_table' function.
class DisassociateTransitGatewayPolicyTableResult(BaseValidatorModel):
    Association: TransitGatewayPolicyTableAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transit_gateway_policy_table_associations' function.
class GetTransitGatewayPolicyTableAssociationsResult(BaseValidatorModel):
    Associations: List[TransitGatewayPolicyTableAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_transit_gateway_route_table' function.
class AssociateTransitGatewayRouteTableResult(BaseValidatorModel):
    Association: TransitGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_transit_gateway_route_table' function.
class DisassociateTransitGatewayRouteTableResult(BaseValidatorModel):
    Association: TransitGatewayAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_associated_enclave_certificate_iam_roles' function.
class GetAssociatedEnclaveCertificateIamRolesResult(BaseValidatorModel):
    AssociatedRoles: List[AssociatedRole]
    ResponseMetadata: ResponseMetadata


class AthenaIntegration(BaseValidatorModel):
    IntegrationResultS3DestinationArn: str
    PartitionLoadFrequency: PartitionLoadFrequencyType
    PartitionStartDate: Optional[Timestamp] = None
    PartitionEndDate: Optional[Timestamp] = None


class ClientData(BaseValidatorModel):
    Comment: Optional[str] = None
    UploadEnd: Optional[Timestamp] = None
    UploadSize: Optional[float] = None
    UploadStart: Optional[Timestamp] = None


# This class is the input for the 'describe_capacity_block_offerings' function.
class DescribeCapacityBlockOfferingsRequest(BaseValidatorModel):
    CapacityDurationHours: int
    DryRun: Optional[bool] = None
    InstanceType: Optional[str] = None
    InstanceCount: Optional[int] = None
    StartDateRange: Optional[Timestamp] = None
    EndDateRange: Optional[Timestamp] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_fleet_history' function.
class DescribeFleetHistoryRequest(BaseValidatorModel):
    FleetId: str
    StartTime: Timestamp
    DryRun: Optional[bool] = None
    EventType: Optional[FleetEventTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_spot_fleet_request_history' function.
class DescribeSpotFleetRequestHistoryRequest(BaseValidatorModel):
    SpotFleetRequestId: str
    StartTime: Timestamp
    DryRun: Optional[bool] = None
    EventType: Optional[EventTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'enable_image_deprecation' function.
class EnableImageDeprecationRequest(BaseValidatorModel):
    ImageId: str
    DeprecateAt: Timestamp
    DryRun: Optional[bool] = None


# This class is the input for the 'get_ipam_address_history' function.
class GetIpamAddressHistoryRequest(BaseValidatorModel):
    Cidr: str
    IpamScopeId: str
    DryRun: Optional[bool] = None
    VpcId: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LaunchTemplateSpotMarketOptionsRequest(BaseValidatorModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[Timestamp] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None


# This class is the input for the 'lock_snapshot' function.
class LockSnapshotRequest(BaseValidatorModel):
    SnapshotId: str
    LockMode: LockModeType
    DryRun: Optional[bool] = None
    CoolOffPeriod: Optional[int] = None
    LockDuration: Optional[int] = None
    ExpirationDate: Optional[Timestamp] = None


# This class is the input for the 'modify_capacity_reservation_fleet' function.
class ModifyCapacityReservationFleetRequest(BaseValidatorModel):
    CapacityReservationFleetId: str
    TotalTargetCapacity: Optional[int] = None
    EndDate: Optional[Timestamp] = None
    DryRun: Optional[bool] = None
    RemoveEndDate: Optional[bool] = None


# This class is the input for the 'modify_capacity_reservation' function.
class ModifyCapacityReservationRequest(BaseValidatorModel):
    CapacityReservationId: str
    InstanceCount: Optional[int] = None
    EndDate: Optional[Timestamp] = None
    EndDateType: Optional[EndDateTypeType] = None
    Accept: Optional[bool] = None
    DryRun: Optional[bool] = None
    AdditionalInfo: Optional[str] = None
    InstanceMatchCriteria: Optional[InstanceMatchCriteriaType] = None


# This class is the input for the 'modify_instance_event_start_time' function.
class ModifyInstanceEventStartTimeRequest(BaseValidatorModel):
    InstanceId: str
    InstanceEventId: str
    NotBefore: Timestamp
    DryRun: Optional[bool] = None


class ReportInstanceStatusRequestInstanceReportStatus(BaseValidatorModel):
    Status: ReportStatusTypeType
    ReasonCodes: List[ReportInstanceReasonCodesType]
    DryRun: Optional[bool] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Description: Optional[str] = None


# This class is the input for the 'report_instance_status' function.
class ReportInstanceStatusRequest(BaseValidatorModel):
    Instances: List[str]
    Status: ReportStatusTypeType
    ReasonCodes: List[ReportInstanceReasonCodesType]
    DryRun: Optional[bool] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Description: Optional[str] = None


class SlotDateTimeRangeRequest(BaseValidatorModel):
    EarliestTime: Timestamp
    LatestTime: Timestamp


class SlotStartTimeRangeRequest(BaseValidatorModel):
    EarliestTime: Optional[Timestamp] = None
    LatestTime: Optional[Timestamp] = None


class SpotMarketOptions(BaseValidatorModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[Timestamp] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None


# This class is the output for the 'attach_vpn_gateway' function.
class AttachVpnGatewayResult(BaseValidatorModel):
    VpcAttachment: VpcAttachment
    ResponseMetadata: ResponseMetadata


class VpnGateway(BaseValidatorModel):
    AmazonSideAsn: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    VpnGatewayId: Optional[str] = None
    State: Optional[VpnStateType] = None
    Type: Optional[Literal['ipsec.1']] = None
    AvailabilityZone: Optional[str] = None
    VpcAttachments: Optional[List[VpcAttachment]] = None


class AttachmentEnaSrdSpecification(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[AttachmentEnaSrdUdpSpecification] = None


# This class is the output for the 'describe_vpc_attribute' function.
class DescribeVpcAttributeResult(BaseValidatorModel):
    EnableDnsHostnames: AttributeBooleanValue
    EnableDnsSupport: AttributeBooleanValue
    EnableNetworkAddressUsageMetrics: AttributeBooleanValue
    VpcId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'modify_subnet_attribute' function.
class ModifySubnetAttributeRequest(BaseValidatorModel):
    SubnetId: str
    AssignIpv6AddressOnCreation: Optional[AttributeBooleanValue] = None
    MapPublicIpOnLaunch: Optional[AttributeBooleanValue] = None
    MapCustomerOwnedIpOnLaunch: Optional[AttributeBooleanValue] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    EnableDns64: Optional[AttributeBooleanValue] = None
    PrivateDnsHostnameTypeOnLaunch: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecordOnLaunch: Optional[AttributeBooleanValue] = None
    EnableResourceNameDnsAAAARecordOnLaunch: Optional[AttributeBooleanValue] = None
    EnableLniAtDeviceIndex: Optional[int] = None
    DisableLniAtDeviceIndex: Optional[AttributeBooleanValue] = None


# This class is the input for the 'modify_volume_attribute' function.
class ModifyVolumeAttributeRequest(BaseValidatorModel):
    VolumeId: str
    AutoEnableIO: Optional[AttributeBooleanValue] = None
    DryRun: Optional[bool] = None


class ModifyVolumeAttributeRequestVolumeModifyAttribute(BaseValidatorModel):
    AutoEnableIO: Optional[AttributeBooleanValue] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_vpc_attribute' function.
class ModifyVpcAttributeRequest(BaseValidatorModel):
    VpcId: str
    EnableDnsHostnames: Optional[AttributeBooleanValue] = None
    EnableDnsSupport: Optional[AttributeBooleanValue] = None
    EnableNetworkAddressUsageMetrics: Optional[AttributeBooleanValue] = None


class ModifyVpcAttributeRequestVpcModifyAttribute(BaseValidatorModel):
    EnableDnsHostnames: Optional[AttributeBooleanValue] = None
    EnableDnsSupport: Optional[AttributeBooleanValue] = None
    EnableNetworkAddressUsageMetrics: Optional[AttributeBooleanValue] = None


class AttributeSummary(BaseValidatorModel):
    AttributeName: Optional[str] = None
    MostFrequentValue: Optional[str] = None
    NumberOfMatchedAccounts: Optional[int] = None
    NumberOfUnmatchedAccounts: Optional[int] = None
    RegionalSummaries: Optional[List[RegionalSummary]] = None


class DhcpConfiguration(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[AttributeValue]] = None


class AuthorizationRule(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    AccessAll: Optional[bool] = None
    DestinationCidr: Optional[str] = None
    Status: Optional[ClientVpnAuthorizationRuleStatus] = None


# This class is the output for the 'authorize_client_vpn_ingress' function.
class AuthorizeClientVpnIngressResult(BaseValidatorModel):
    Status: ClientVpnAuthorizationRuleStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_client_vpn_ingress' function.
class RevokeClientVpnIngressResult(BaseValidatorModel):
    Status: ClientVpnAuthorizationRuleStatus
    ResponseMetadata: ResponseMetadata


class AvailabilityZone(BaseValidatorModel):
    OptInStatus: Optional[AvailabilityZoneOptInStatusType] = None
    Messages: Optional[List[AvailabilityZoneMessage]] = None
    RegionName: Optional[str] = None
    ZoneName: Optional[str] = None
    ZoneId: Optional[str] = None
    GroupName: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    ZoneType: Optional[str] = None
    ParentZoneName: Optional[str] = None
    ParentZoneId: Optional[str] = None
    State: Optional[AvailabilityZoneStateType] = None


class AvailableCapacity(BaseValidatorModel):
    AvailableInstanceCapacity: Optional[List[InstanceCapacity]] = None
    AvailableVCpus: Optional[int] = None


class BlobAttributeValue(BaseValidatorModel):
    Value: Optional[Blob] = None


class S3Storage(BaseValidatorModel):
    AWSAccessKeyId: Optional[str] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None
    UploadPolicy: Optional[Blob] = None
    UploadPolicySignature: Optional[str] = None


class BlockDeviceMappingResponse(BaseValidatorModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsBlockDeviceResponse] = None
    NoDevice: Optional[str] = None


class BlockDeviceMapping(BaseValidatorModel):
    Ebs: Optional[EbsBlockDevice] = None
    NoDevice: Optional[str] = None
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None


# This class is the output for the 'deprovision_ipam_byoasn' function.
class DeprovisionIpamByoasnResult(BaseValidatorModel):
    Byoasn: Byoasn
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ipam_byoasn' function.
class DescribeIpamByoasnResult(BaseValidatorModel):
    Byoasns: List[Byoasn]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'provision_ipam_byoasn' function.
class ProvisionIpamByoasnResult(BaseValidatorModel):
    Byoasn: Byoasn
    ResponseMetadata: ResponseMetadata


class FailedCapacityReservationFleetCancellationResult(BaseValidatorModel):
    CapacityReservationFleetId: Optional[str] = None
    CancelCapacityReservationFleetError: Optional[CancelCapacityReservationFleetError] = None


class CancelSpotFleetRequestsErrorItem(BaseValidatorModel):
    Error: Optional[CancelSpotFleetRequestsError] = None
    SpotFleetRequestId: Optional[str] = None


# This class is the output for the 'cancel_spot_instance_requests' function.
class CancelSpotInstanceRequestsResult(BaseValidatorModel):
    CancelledSpotInstanceRequests: List[CancelledSpotInstanceRequest]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_capacity_block_extension_offerings' function.
class DescribeCapacityBlockExtensionOfferingsResult(BaseValidatorModel):
    CapacityBlockExtensionOfferings: List[CapacityBlockExtensionOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_capacity_block_extension_history' function.
class DescribeCapacityBlockExtensionHistoryResult(BaseValidatorModel):
    CapacityBlockExtensions: List[CapacityBlockExtension]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'purchase_capacity_block_extension' function.
class PurchaseCapacityBlockExtensionResult(BaseValidatorModel):
    CapacityBlockExtensions: List[CapacityBlockExtension]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_capacity_block_offerings' function.
class DescribeCapacityBlockOfferingsResult(BaseValidatorModel):
    CapacityBlockOfferings: List[CapacityBlockOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CapacityReservationBillingRequest(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    RequestedBy: Optional[str] = None
    UnusedReservationBillingOwnerId: Optional[str] = None
    LastUpdateTime: Optional[datetime] = None
    Status: Optional[CapacityReservationBillingRequestStatusType] = None
    StatusMessage: Optional[str] = None
    CapacityReservationInfo: Optional[CapacityReservationInfo] = None


class CapacityReservation(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    OwnerId: Optional[str] = None
    CapacityReservationArn: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    InstanceType: Optional[str] = None
    InstancePlatform: Optional[CapacityReservationInstancePlatformType] = None
    AvailabilityZone: Optional[str] = None
    Tenancy: Optional[CapacityReservationTenancyType] = None
    TotalInstanceCount: Optional[int] = None
    AvailableInstanceCount: Optional[int] = None
    EbsOptimized: Optional[bool] = None
    EphemeralStorage: Optional[bool] = None
    State: Optional[CapacityReservationStateType] = None
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    EndDateType: Optional[EndDateTypeType] = None
    InstanceMatchCriteria: Optional[InstanceMatchCriteriaType] = None
    CreateDate: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    OutpostArn: Optional[str] = None
    CapacityReservationFleetId: Optional[str] = None
    PlacementGroupArn: Optional[str] = None
    CapacityAllocations: Optional[List[CapacityAllocation]] = None
    ReservationType: Optional[CapacityReservationTypeType] = None
    UnusedReservationBillingOwnerId: Optional[str] = None
    CommitmentInfo: Optional[CapacityReservationCommitmentInfo] = None
    DeliveryPreference: Optional[CapacityReservationDeliveryPreferenceType] = None


class CapacityReservationFleet(BaseValidatorModel):
    CapacityReservationFleetId: Optional[str] = None
    CapacityReservationFleetArn: Optional[str] = None
    State: Optional[CapacityReservationFleetStateType] = None
    TotalTargetCapacity: Optional[int] = None
    TotalFulfilledCapacity: Optional[float] = None
    Tenancy: Optional[Literal['default']] = None
    EndDate: Optional[datetime] = None
    CreateTime: Optional[datetime] = None
    InstanceMatchCriteria: Optional[Literal['open']] = None
    AllocationStrategy: Optional[str] = None
    InstanceTypeSpecifications: Optional[List[FleetCapacityReservation]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_capacity_reservation_fleet' function.
class CreateCapacityReservationFleetResult(BaseValidatorModel):
    CapacityReservationFleetId: str
    State: CapacityReservationFleetStateType
    TotalTargetCapacity: int
    TotalFulfilledCapacity: float
    InstanceMatchCriteria: Literal['open']
    AllocationStrategy: str
    CreateTime: datetime
    EndDate: datetime
    Tenancy: Literal['default']
    FleetCapacityReservations: List[FleetCapacityReservation]
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_groups_for_capacity_reservation' function.
class GetGroupsForCapacityReservationResult(BaseValidatorModel):
    CapacityReservationGroups: List[CapacityReservationGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OnDemandOptionsRequest(BaseValidatorModel):
    AllocationStrategy: Optional[FleetOnDemandAllocationStrategyType] = None
    CapacityReservationOptions: Optional[CapacityReservationOptionsRequest] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None


class OnDemandOptions(BaseValidatorModel):
    AllocationStrategy: Optional[FleetOnDemandAllocationStrategyType] = None
    CapacityReservationOptions: Optional[CapacityReservationOptions] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None


class CapacityReservationSpecificationResponse(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetResponse] = None


class LaunchTemplateCapacityReservationSpecificationResponse(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetResponse] = None


class CapacityReservationSpecification(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTarget] = None


class LaunchTemplateCapacityReservationSpecificationRequest(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTarget] = None


# This class is the output for the 'describe_vpc_classic_link_dns_support' function.
class DescribeVpcClassicLinkDnsSupportResult(BaseValidatorModel):
    Vpcs: List[ClassicLinkDnsSupport]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClassicLinkInstance(BaseValidatorModel):
    Groups: Optional[List[GroupIdentifier]] = None
    InstanceId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    VpcId: Optional[str] = None


class ClassicLoadBalancersConfigOutput(BaseValidatorModel):
    ClassicLoadBalancers: Optional[List[ClassicLoadBalancer]] = None


class ClassicLoadBalancersConfig(BaseValidatorModel):
    ClassicLoadBalancers: Optional[List[ClassicLoadBalancer]] = None


# This class is the output for the 'export_client_vpn_client_certificate_revocation_list' function.
class ExportClientVpnClientCertificateRevocationListResult(BaseValidatorModel):
    CertificateRevocationList: str
    Status: ClientCertificateRevocationListStatus
    ResponseMetadata: ResponseMetadata


class ClientConnectResponseOptions(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None
    Status: Optional[ClientVpnEndpointAttributeStatus] = None


class ClientVpnAuthenticationRequest(BaseValidatorModel):
    Type: Optional[ClientVpnAuthenticationTypeType] = None
    ActiveDirectory: Optional[DirectoryServiceAuthenticationRequest] = None
    MutualAuthentication: Optional[CertificateAuthenticationRequest] = None
    FederatedAuthentication: Optional[FederatedAuthenticationRequest] = None


class ClientVpnAuthentication(BaseValidatorModel):
    Type: Optional[ClientVpnAuthenticationTypeType] = None
    ActiveDirectory: Optional[DirectoryServiceAuthentication] = None
    MutualAuthentication: Optional[CertificateAuthentication] = None
    FederatedAuthentication: Optional[FederatedAuthentication] = None


class ClientVpnConnection(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Timestamp: Optional[str] = None
    ConnectionId: Optional[str] = None
    Username: Optional[str] = None
    ConnectionEstablishedTime: Optional[str] = None
    IngressBytes: Optional[str] = None
    EgressBytes: Optional[str] = None
    IngressPackets: Optional[str] = None
    EgressPackets: Optional[str] = None
    ClientIp: Optional[str] = None
    CommonName: Optional[str] = None
    Status: Optional[ClientVpnConnectionStatus] = None
    ConnectionEndTime: Optional[str] = None
    PostureComplianceStatuses: Optional[List[str]] = None


class TerminateConnectionStatus(BaseValidatorModel):
    ConnectionId: Optional[str] = None
    PreviousStatus: Optional[ClientVpnConnectionStatus] = None
    CurrentStatus: Optional[ClientVpnConnectionStatus] = None


# This class is the output for the 'create_client_vpn_endpoint' function.
class CreateClientVpnEndpointResult(BaseValidatorModel):
    ClientVpnEndpointId: str
    Status: ClientVpnEndpointStatus
    DnsName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_client_vpn_endpoint' function.
class DeleteClientVpnEndpointResult(BaseValidatorModel):
    Status: ClientVpnEndpointStatus
    ResponseMetadata: ResponseMetadata


class ClientVpnRoute(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    DestinationCidr: Optional[str] = None
    TargetSubnet: Optional[str] = None
    Type: Optional[str] = None
    Origin: Optional[str] = None
    Status: Optional[ClientVpnRouteStatus] = None
    Description: Optional[str] = None


# This class is the output for the 'create_client_vpn_route' function.
class CreateClientVpnRouteResult(BaseValidatorModel):
    Status: ClientVpnRouteStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_client_vpn_route' function.
class DeleteClientVpnRouteResult(BaseValidatorModel):
    Status: ClientVpnRouteStatus
    ResponseMetadata: ResponseMetadata


class VpnTunnelLogOptionsSpecification(BaseValidatorModel):
    CloudWatchLogOptions: Optional[CloudWatchLogOptionsSpecification] = None


class VpnTunnelLogOptions(BaseValidatorModel):
    CloudWatchLogOptions: Optional[CloudWatchLogOptions] = None


# This class is the output for the 'get_coip_pool_usage' function.
class GetCoipPoolUsageResult(BaseValidatorModel):
    CoipPoolId: str
    CoipAddressUsages: List[CoipAddressUsage]
    LocalGatewayRouteTableId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_coip_cidr' function.
class CreateCoipCidrResult(BaseValidatorModel):
    CoipCidr: CoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_coip_cidr' function.
class DeleteCoipCidrResult(BaseValidatorModel):
    CoipCidr: CoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpc_endpoint_connection_notification' function.
class CreateVpcEndpointConnectionNotificationResult(BaseValidatorModel):
    ConnectionNotification: ConnectionNotification
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_endpoint_connection_notifications' function.
class DescribeVpcEndpointConnectionNotificationsResult(BaseValidatorModel):
    ConnectionNotificationSet: List[ConnectionNotification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CpuPerformanceFactorOutput(BaseValidatorModel):
    References: Optional[List[PerformanceFactorReference]] = None


class CpuPerformanceFactor(BaseValidatorModel):
    References: Optional[List[PerformanceFactorReference]] = None


class CpuPerformanceFactorRequest(BaseValidatorModel):
    References: Optional[List[PerformanceFactorReferenceRequest]] = None


# This class is the input for the 'modify_instance_event_window' function.
class ModifyInstanceEventWindowRequest(BaseValidatorModel):
    InstanceEventWindowId: str
    DryRun: Optional[bool] = None
    Name: Optional[str] = None
    TimeRanges: Optional[List[InstanceEventWindowTimeRangeRequest]] = None
    CronExpression: Optional[str] = None


# This class is the input for the 'modify_ipam_pool' function.
class ModifyIpamPoolRequest(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AutoImport: Optional[bool] = None
    AllocationMinNetmaskLength: Optional[int] = None
    AllocationMaxNetmaskLength: Optional[int] = None
    AllocationDefaultNetmaskLength: Optional[int] = None
    ClearAllocationDefaultNetmaskLength: Optional[bool] = None
    AddAllocationResourceTags: Optional[List[RequestIpamResourceTag]] = None
    RemoveAllocationResourceTags: Optional[List[RequestIpamResourceTag]] = None


# This class is the output for the 'create_local_gateway_route' function.
class CreateLocalGatewayRouteResult(BaseValidatorModel):
    Route: LocalGatewayRoute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_local_gateway_route' function.
class DeleteLocalGatewayRouteResult(BaseValidatorModel):
    Route: LocalGatewayRoute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_local_gateway_route' function.
class ModifyLocalGatewayRouteResult(BaseValidatorModel):
    Route: LocalGatewayRoute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_local_gateway_routes' function.
class SearchLocalGatewayRoutesResult(BaseValidatorModel):
    Routes: List[LocalGatewayRoute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateNetworkAclEntryRequestNetworkAclCreateEntry(BaseValidatorModel):
    RuleNumber: int
    Protocol: str
    RuleAction: RuleActionType
    Egress: bool
    DryRun: Optional[bool] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    IcmpTypeCode: Optional[IcmpTypeCode] = None
    PortRange: Optional[PortRange] = None


# This class is the input for the 'create_network_acl_entry' function.
class CreateNetworkAclEntryRequest(BaseValidatorModel):
    NetworkAclId: str
    RuleNumber: int
    Protocol: str
    RuleAction: RuleActionType
    Egress: bool
    DryRun: Optional[bool] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    IcmpTypeCode: Optional[IcmpTypeCode] = None
    PortRange: Optional[PortRange] = None


class NetworkAclEntry(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Egress: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCode] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRange] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[RuleActionType] = None
    RuleNumber: Optional[int] = None


class ReplaceNetworkAclEntryRequestNetworkAclReplaceEntry(BaseValidatorModel):
    RuleNumber: int
    Protocol: str
    RuleAction: RuleActionType
    Egress: bool
    DryRun: Optional[bool] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    IcmpTypeCode: Optional[IcmpTypeCode] = None
    PortRange: Optional[PortRange] = None


# This class is the input for the 'replace_network_acl_entry' function.
class ReplaceNetworkAclEntryRequest(BaseValidatorModel):
    NetworkAclId: str
    RuleNumber: int
    Protocol: str
    RuleAction: RuleActionType
    Egress: bool
    DryRun: Optional[bool] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    IcmpTypeCode: Optional[IcmpTypeCode] = None
    PortRange: Optional[PortRange] = None


# This class is the input for the 'create_reserved_instances_listing' function.
class CreateReservedInstancesListingRequest(BaseValidatorModel):
    ReservedInstancesId: str
    InstanceCount: int
    PriceSchedules: List[PriceScheduleSpecification]
    ClientToken: str


# This class is the input for the 'create_store_image_task' function.
class CreateStoreImageTaskRequest(BaseValidatorModel):
    ImageId: str
    Bucket: str
    S3ObjectTags: Optional[List[S3ObjectTag]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_traffic_mirror_filter_rule' function.
class ModifyTrafficMirrorFilterRuleRequest(BaseValidatorModel):
    TrafficMirrorFilterRuleId: str
    TrafficDirection: Optional[TrafficDirectionType] = None
    RuleNumber: Optional[int] = None
    RuleAction: Optional[TrafficMirrorRuleActionType] = None
    DestinationPortRange: Optional[TrafficMirrorPortRangeRequest] = None
    SourcePortRange: Optional[TrafficMirrorPortRangeRequest] = None
    Protocol: Optional[int] = None
    DestinationCidrBlock: Optional[str] = None
    SourceCidrBlock: Optional[str] = None
    Description: Optional[str] = None
    RemoveFields: Optional[List[TrafficMirrorFilterRuleFieldType]] = None
    DryRun: Optional[bool] = None


class CreateVerifiedAccessEndpointCidrOptions(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    SubnetIds: Optional[List[str]] = None
    Cidr: Optional[str] = None
    PortRanges: Optional[List[CreateVerifiedAccessEndpointPortRange]] = None


class CreateVerifiedAccessEndpointEniOptions(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    PortRanges: Optional[List[CreateVerifiedAccessEndpointPortRange]] = None


class CreateVerifiedAccessEndpointLoadBalancerOptions(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    LoadBalancerArn: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    PortRanges: Optional[List[CreateVerifiedAccessEndpointPortRange]] = None


# This class is the input for the 'modify_verified_access_endpoint_policy' function.
class ModifyVerifiedAccessEndpointPolicyRequest(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    PolicyEnabled: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequest] = None


# This class is the input for the 'modify_verified_access_group_policy' function.
class ModifyVerifiedAccessGroupPolicyRequest(BaseValidatorModel):
    VerifiedAccessGroupId: str
    PolicyEnabled: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequest] = None


class CreateVolumePermissionModifications(BaseValidatorModel):
    Add: Optional[List[CreateVolumePermission]] = None
    Remove: Optional[List[CreateVolumePermission]] = None


# This class is the input for the 'modify_vpc_endpoint' function.
class ModifyVpcEndpointRequest(BaseValidatorModel):
    VpcEndpointId: str
    DryRun: Optional[bool] = None
    ResetPolicy: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    AddRouteTableIds: Optional[List[str]] = None
    RemoveRouteTableIds: Optional[List[str]] = None
    AddSubnetIds: Optional[List[str]] = None
    RemoveSubnetIds: Optional[List[str]] = None
    AddSecurityGroupIds: Optional[List[str]] = None
    RemoveSecurityGroupIds: Optional[List[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DnsOptions: Optional[DnsOptionsSpecification] = None
    PrivateDnsEnabled: Optional[bool] = None
    SubnetConfigurations: Optional[List[SubnetConfiguration]] = None


# This class is the input for the 'get_aws_network_performance_data' function.
class GetAwsNetworkPerformanceDataRequest(BaseValidatorModel):
    DataQueries: Optional[List[DataQuery]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DataResponse(BaseValidatorModel):
    Id: Optional[str] = None
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal['aggregate-latency']] = None
    Statistic: Optional[Literal['p50']] = None
    Period: Optional[PeriodTypeType] = None
    MetricPoints: Optional[List[MetricPoint]] = None


class DeleteFleetErrorItem(BaseValidatorModel):
    Error: Optional[DeleteFleetError] = None
    FleetId: Optional[str] = None


# This class is the output for the 'delete_instance_event_window' function.
class DeleteInstanceEventWindowResult(BaseValidatorModel):
    InstanceEventWindowState: InstanceEventWindowStateChange
    ResponseMetadata: ResponseMetadata


class DeleteLaunchTemplateVersionsResponseErrorItem(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None
    ResponseError: Optional[ResponseError] = None


class FailedQueuedPurchaseDeletion(BaseValidatorModel):
    Error: Optional[DeleteQueuedReservedInstancesError] = None
    ReservedInstancesId: Optional[str] = None


# This class is the input for the 'deregister_instance_event_notification_attributes' function.
class DeregisterInstanceEventNotificationAttributesRequest(BaseValidatorModel):
    InstanceTagAttribute: DeregisterInstanceTagAttributeRequest
    DryRun: Optional[bool] = None


# This class is the output for the 'deregister_instance_event_notification_attributes' function.
class DeregisterInstanceEventNotificationAttributesResult(BaseValidatorModel):
    InstanceTagAttribute: InstanceTagNotificationAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_instance_event_notification_attributes' function.
class DescribeInstanceEventNotificationAttributesResult(BaseValidatorModel):
    InstanceTagAttribute: InstanceTagNotificationAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_instance_event_notification_attributes' function.
class RegisterInstanceEventNotificationAttributesResult(BaseValidatorModel):
    InstanceTagAttribute: InstanceTagNotificationAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_transit_gateway_multicast_group_members' function.
class DeregisterTransitGatewayMulticastGroupMembersResult(BaseValidatorModel):
    DeregisteredMulticastGroupMembers: TransitGatewayMulticastDeregisteredGroupMembers
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_transit_gateway_multicast_group_sources' function.
class DeregisterTransitGatewayMulticastGroupSourcesResult(BaseValidatorModel):
    DeregisteredMulticastGroupSources: TransitGatewayMulticastDeregisteredGroupSources
    ResponseMetadata: ResponseMetadata


class DescribeAddressTransfersRequestPaginate(BaseValidatorModel):
    AllocationIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAddressesAttributeRequestPaginate(BaseValidatorModel):
    AllocationIds: Optional[List[str]] = None
    Attribute: Optional[Literal['domain-name']] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeByoipCidrsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCapacityBlockExtensionOfferingsRequestPaginate(BaseValidatorModel):
    CapacityBlockExtensionDurationHours: int
    CapacityReservationId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCapacityBlockOfferingsRequestPaginate(BaseValidatorModel):
    CapacityDurationHours: int
    DryRun: Optional[bool] = None
    InstanceType: Optional[str] = None
    InstanceCount: Optional[int] = None
    StartDateRange: Optional[Timestamp] = None
    EndDateRange: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePrincipalIdFormatRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Resources: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSpotFleetInstancesRequestPaginate(BaseValidatorModel):
    SpotFleetRequestId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSpotFleetRequestsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    SpotFleetRequestIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeStaleSecurityGroupsRequestPaginate(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeVpcClassicLinkDnsSupportRequestPaginate(BaseValidatorModel):
    VpcIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAssociatedIpv6PoolCidrsRequestPaginate(BaseValidatorModel):
    PoolId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetAwsNetworkPerformanceDataRequestPaginate(BaseValidatorModel):
    DataQueries: Optional[List[DataQuery]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetGroupsForCapacityReservationRequestPaginate(BaseValidatorModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetIpamAddressHistoryRequestPaginate(BaseValidatorModel):
    Cidr: str
    IpamScopeId: str
    DryRun: Optional[bool] = None
    VpcId: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetManagedPrefixListAssociationsRequestPaginate(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetManagedPrefixListEntriesRequestPaginate(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    TargetVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetNetworkInsightsAccessScopeAnalysisFindingsRequestPaginate(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetVpnConnectionDeviceTypesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImagesInRecycleBinRequestPaginate(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSnapshotsInRecycleBinRequestPaginate(BaseValidatorModel):
    SnapshotIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_addresses' function.
class DescribeAddressesRequest(BaseValidatorModel):
    PublicIps: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    AllocationIds: Optional[List[str]] = None


# This class is the input for the 'describe_availability_zones' function.
class DescribeAvailabilityZonesRequest(BaseValidatorModel):
    ZoneNames: Optional[List[str]] = None
    ZoneIds: Optional[List[str]] = None
    AllAvailabilityZones: Optional[bool] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeAwsNetworkPerformanceMetricSubscriptionsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_aws_network_performance_metric_subscriptions' function.
class DescribeAwsNetworkPerformanceMetricSubscriptionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_bundle_tasks' function.
class DescribeBundleTasksRequest(BaseValidatorModel):
    BundleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeCapacityBlockExtensionHistoryRequestPaginate(BaseValidatorModel):
    CapacityReservationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_capacity_block_extension_history' function.
class DescribeCapacityBlockExtensionHistoryRequest(BaseValidatorModel):
    CapacityReservationIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeCapacityReservationBillingRequestsRequestPaginate(BaseValidatorModel):
    Role: CallerRoleType
    CapacityReservationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_capacity_reservation_billing_requests' function.
class DescribeCapacityReservationBillingRequestsRequest(BaseValidatorModel):
    Role: CallerRoleType
    CapacityReservationIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeCapacityReservationFleetsRequestPaginate(BaseValidatorModel):
    CapacityReservationFleetIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_capacity_reservation_fleets' function.
class DescribeCapacityReservationFleetsRequest(BaseValidatorModel):
    CapacityReservationFleetIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeCapacityReservationsRequestPaginate(BaseValidatorModel):
    CapacityReservationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_capacity_reservations' function.
class DescribeCapacityReservationsRequest(BaseValidatorModel):
    CapacityReservationIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeCarrierGatewaysRequestPaginate(BaseValidatorModel):
    CarrierGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_carrier_gateways' function.
class DescribeCarrierGatewaysRequest(BaseValidatorModel):
    CarrierGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeClassicLinkInstancesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_classic_link_instances' function.
class DescribeClassicLinkInstancesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeClientVpnAuthorizationRulesRequestPaginate(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_client_vpn_authorization_rules' function.
class DescribeClientVpnAuthorizationRulesRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None


class DescribeClientVpnConnectionsRequestPaginate(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_client_vpn_connections' function.
class DescribeClientVpnConnectionsRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


class DescribeClientVpnEndpointsRequestPaginate(BaseValidatorModel):
    ClientVpnEndpointIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_client_vpn_endpoints' function.
class DescribeClientVpnEndpointsRequest(BaseValidatorModel):
    ClientVpnEndpointIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeClientVpnRoutesRequestPaginate(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_client_vpn_routes' function.
class DescribeClientVpnRoutesRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeClientVpnTargetNetworksRequestPaginate(BaseValidatorModel):
    ClientVpnEndpointId: str
    AssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_client_vpn_target_networks' function.
class DescribeClientVpnTargetNetworksRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    AssociationIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeCoipPoolsRequestPaginate(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_coip_pools' function.
class DescribeCoipPoolsRequest(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_customer_gateways' function.
class DescribeCustomerGatewaysRequest(BaseValidatorModel):
    CustomerGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeDhcpOptionsRequestPaginate(BaseValidatorModel):
    DhcpOptionsIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_dhcp_options' function.
class DescribeDhcpOptionsRequest(BaseValidatorModel):
    DhcpOptionsIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeEgressOnlyInternetGatewaysRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    EgressOnlyInternetGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_egress_only_internet_gateways' function.
class DescribeEgressOnlyInternetGatewaysRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    EgressOnlyInternetGatewayIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_elastic_gpus' function.
class DescribeElasticGpusRequest(BaseValidatorModel):
    ElasticGpuIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeExportImageTasksRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ExportImageTaskIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_export_image_tasks' function.
class DescribeExportImageTasksRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ExportImageTaskIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_export_tasks' function.
class DescribeExportTasksRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    ExportTaskIds: Optional[List[str]] = None


class DescribeFastLaunchImagesRequestPaginate(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_fast_launch_images' function.
class DescribeFastLaunchImagesRequest(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeFastSnapshotRestoresRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_fast_snapshot_restores' function.
class DescribeFastSnapshotRestoresRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_fleet_instances' function.
class DescribeFleetInstancesRequest(BaseValidatorModel):
    FleetId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class DescribeFleetsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    FleetIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_fleets' function.
class DescribeFleetsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FleetIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


class DescribeFlowLogsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    FlowLogIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_flow_logs' function.
class DescribeFlowLogsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    FlowLogIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeFpgaImagesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    FpgaImageIds: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_fpga_images' function.
class DescribeFpgaImagesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    FpgaImageIds: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeHostReservationOfferingsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxDuration: Optional[int] = None
    MinDuration: Optional[int] = None
    OfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_host_reservation_offerings' function.
class DescribeHostReservationOfferingsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxDuration: Optional[int] = None
    MaxResults: Optional[int] = None
    MinDuration: Optional[int] = None
    NextToken: Optional[str] = None
    OfferingId: Optional[str] = None


class DescribeHostReservationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    HostReservationIdSet: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_host_reservations' function.
class DescribeHostReservationsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    HostReservationIdSet: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeHostsRequestPaginate(BaseValidatorModel):
    HostIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_hosts' function.
class DescribeHostsRequest(BaseValidatorModel):
    HostIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None


class DescribeIamInstanceProfileAssociationsRequestPaginate(BaseValidatorModel):
    AssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_iam_instance_profile_associations' function.
class DescribeIamInstanceProfileAssociationsRequest(BaseValidatorModel):
    AssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeImagesRequestPaginate(BaseValidatorModel):
    ExecutableUsers: Optional[List[str]] = None
    ImageIds: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_images' function.
class DescribeImagesRequest(BaseValidatorModel):
    ExecutableUsers: Optional[List[str]] = None
    ImageIds: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeImportImageTasksRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ImportTaskIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_import_image_tasks' function.
class DescribeImportImageTasksRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ImportTaskIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeImportSnapshotTasksRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ImportTaskIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_import_snapshot_tasks' function.
class DescribeImportSnapshotTasksRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ImportTaskIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceConnectEndpointsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    InstanceConnectEndpointIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_connect_endpoints' function.
class DescribeInstanceConnectEndpointsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    InstanceConnectEndpointIds: Optional[List[str]] = None


class DescribeInstanceCreditSpecificationsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    InstanceIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_credit_specifications' function.
class DescribeInstanceCreditSpecificationsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    InstanceIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceEventWindowsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceEventWindowIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_event_windows' function.
class DescribeInstanceEventWindowsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceEventWindowIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceImageMetadataRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_image_metadata' function.
class DescribeInstanceImageMetadataRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    InstanceIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeInstanceStatusRequestPaginate(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IncludeAllInstances: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_status' function.
class DescribeInstanceStatusRequest(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IncludeAllInstances: Optional[bool] = None


class DescribeInstanceTopologyRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceIds: Optional[List[str]] = None
    GroupNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_topology' function.
class DescribeInstanceTopologyRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InstanceIds: Optional[List[str]] = None
    GroupNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


class DescribeInstanceTypeOfferingsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LocationType: Optional[LocationTypeType] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_type_offerings' function.
class DescribeInstanceTypeOfferingsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LocationType: Optional[LocationTypeType] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstanceTypesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceTypes: Optional[List[InstanceTypeType]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instance_types' function.
class DescribeInstanceTypesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceTypes: Optional[List[InstanceTypeType]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeInstancesRequestPaginate(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_instances' function.
class DescribeInstancesRequest(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeInternetGatewaysRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_internet_gateways' function.
class DescribeInternetGatewaysRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_ipam_external_resource_verification_tokens' function.
class DescribeIpamExternalResourceVerificationTokensRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IpamExternalResourceVerificationTokenIds: Optional[List[str]] = None


class DescribeIpamPoolsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IpamPoolIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_ipam_pools' function.
class DescribeIpamPoolsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamPoolIds: Optional[List[str]] = None


class DescribeIpamResourceDiscoveriesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_ipam_resource_discoveries' function.
class DescribeIpamResourceDiscoveriesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None


class DescribeIpamResourceDiscoveryAssociationsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryAssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_ipam_resource_discovery_associations' function.
class DescribeIpamResourceDiscoveryAssociationsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryAssociationIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None


class DescribeIpamScopesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IpamScopeIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_ipam_scopes' function.
class DescribeIpamScopesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamScopeIds: Optional[List[str]] = None


class DescribeIpamsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IpamIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_ipams' function.
class DescribeIpamsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamIds: Optional[List[str]] = None


class DescribeIpv6PoolsRequestPaginate(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_ipv6_pools' function.
class DescribeIpv6PoolsRequest(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_key_pairs' function.
class DescribeKeyPairsRequest(BaseValidatorModel):
    KeyNames: Optional[List[str]] = None
    KeyPairIds: Optional[List[str]] = None
    IncludePublicKey: Optional[bool] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeLaunchTemplateVersionsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Versions: Optional[List[str]] = None
    MinVersion: Optional[str] = None
    MaxVersion: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    ResolveAlias: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_launch_template_versions' function.
class DescribeLaunchTemplateVersionsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Versions: Optional[List[str]] = None
    MinVersion: Optional[str] = None
    MaxVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    ResolveAlias: Optional[bool] = None


class DescribeLaunchTemplatesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateIds: Optional[List[str]] = None
    LaunchTemplateNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_launch_templates' function.
class DescribeLaunchTemplatesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateIds: Optional[List[str]] = None
    LaunchTemplateNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestPaginate(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequest(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeLocalGatewayRouteTableVpcAssociationsRequestPaginate(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_local_gateway_route_table_vpc_associations' function.
class DescribeLocalGatewayRouteTableVpcAssociationsRequest(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeLocalGatewayRouteTablesRequestPaginate(BaseValidatorModel):
    LocalGatewayRouteTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_local_gateway_route_tables' function.
class DescribeLocalGatewayRouteTablesRequest(BaseValidatorModel):
    LocalGatewayRouteTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeLocalGatewayVirtualInterfaceGroupsRequestPaginate(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroupIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_local_gateway_virtual_interface_groups' function.
class DescribeLocalGatewayVirtualInterfaceGroupsRequest(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroupIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeLocalGatewayVirtualInterfacesRequestPaginate(BaseValidatorModel):
    LocalGatewayVirtualInterfaceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_local_gateway_virtual_interfaces' function.
class DescribeLocalGatewayVirtualInterfacesRequest(BaseValidatorModel):
    LocalGatewayVirtualInterfaceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeLocalGatewaysRequestPaginate(BaseValidatorModel):
    LocalGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_local_gateways' function.
class DescribeLocalGatewaysRequest(BaseValidatorModel):
    LocalGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_locked_snapshots' function.
class DescribeLockedSnapshotsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SnapshotIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


class DescribeMacHostsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    HostIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_mac_hosts' function.
class DescribeMacHostsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    HostIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeManagedPrefixListsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PrefixListIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_managed_prefix_lists' function.
class DescribeManagedPrefixListsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PrefixListIds: Optional[List[str]] = None


class DescribeMovingAddressesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    PublicIps: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_moving_addresses' function.
class DescribeMovingAddressesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    PublicIps: Optional[List[str]] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None


class DescribeNatGatewaysRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NatGatewayIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_nat_gateways' function.
class DescribeNatGatewaysRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[List[str]] = None
    NextToken: Optional[str] = None


class DescribeNetworkAclsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    NetworkAclIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_network_acls' function.
class DescribeNetworkAclsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NetworkAclIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


class DescribeNetworkInsightsAccessScopeAnalysesRequestPaginate(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisIds: Optional[List[str]] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    AnalysisStartTimeBegin: Optional[Timestamp] = None
    AnalysisStartTimeEnd: Optional[Timestamp] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_network_insights_access_scope_analyses' function.
class DescribeNetworkInsightsAccessScopeAnalysesRequest(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisIds: Optional[List[str]] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    AnalysisStartTimeBegin: Optional[Timestamp] = None
    AnalysisStartTimeEnd: Optional[Timestamp] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None


class DescribeNetworkInsightsAccessScopesRequestPaginate(BaseValidatorModel):
    NetworkInsightsAccessScopeIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_network_insights_access_scopes' function.
class DescribeNetworkInsightsAccessScopesRequest(BaseValidatorModel):
    NetworkInsightsAccessScopeIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None


class DescribeNetworkInsightsAnalysesRequestPaginate(BaseValidatorModel):
    NetworkInsightsAnalysisIds: Optional[List[str]] = None
    NetworkInsightsPathId: Optional[str] = None
    AnalysisStartTime: Optional[Timestamp] = None
    AnalysisEndTime: Optional[Timestamp] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_network_insights_analyses' function.
class DescribeNetworkInsightsAnalysesRequest(BaseValidatorModel):
    NetworkInsightsAnalysisIds: Optional[List[str]] = None
    NetworkInsightsPathId: Optional[str] = None
    AnalysisStartTime: Optional[Timestamp] = None
    AnalysisEndTime: Optional[Timestamp] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None


class DescribeNetworkInsightsPathsRequestPaginate(BaseValidatorModel):
    NetworkInsightsPathIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_network_insights_paths' function.
class DescribeNetworkInsightsPathsRequest(BaseValidatorModel):
    NetworkInsightsPathIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None


class DescribeNetworkInterfacePermissionsRequestPaginate(BaseValidatorModel):
    NetworkInterfacePermissionIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_network_interface_permissions' function.
class DescribeNetworkInterfacePermissionsRequest(BaseValidatorModel):
    NetworkInterfacePermissionIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeNetworkInterfacesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_network_interfaces' function.
class DescribeNetworkInterfacesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_placement_groups' function.
class DescribePlacementGroupsRequest(BaseValidatorModel):
    GroupIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    GroupNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


class DescribePrefixListsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PrefixListIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_prefix_lists' function.
class DescribePrefixListsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PrefixListIds: Optional[List[str]] = None


class DescribePublicIpv4PoolsRequestPaginate(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_public_ipv4_pools' function.
class DescribePublicIpv4PoolsRequest(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_regions' function.
class DescribeRegionsRequest(BaseValidatorModel):
    RegionNames: Optional[List[str]] = None
    AllRegions: Optional[bool] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeReplaceRootVolumeTasksRequestPaginate(BaseValidatorModel):
    ReplaceRootVolumeTaskIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_replace_root_volume_tasks' function.
class DescribeReplaceRootVolumeTasksRequest(BaseValidatorModel):
    ReplaceRootVolumeTaskIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_reserved_instances_listings' function.
class DescribeReservedInstancesListingsRequest(BaseValidatorModel):
    ReservedInstancesId: Optional[str] = None
    ReservedInstancesListingId: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class DescribeReservedInstancesModificationsRequestPaginate(BaseValidatorModel):
    ReservedInstancesModificationIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_reserved_instances_modifications' function.
class DescribeReservedInstancesModificationsRequest(BaseValidatorModel):
    ReservedInstancesModificationIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None


class DescribeReservedInstancesOfferingsRequestPaginate(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    IncludeMarketplace: Optional[bool] = None
    InstanceType: Optional[InstanceTypeType] = None
    MaxDuration: Optional[int] = None
    MaxInstanceCount: Optional[int] = None
    MinDuration: Optional[int] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    ReservedInstancesOfferingIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    InstanceTenancy: Optional[TenancyType] = None
    OfferingType: Optional[OfferingTypeValuesType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_reserved_instances_offerings' function.
class DescribeReservedInstancesOfferingsRequest(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    IncludeMarketplace: Optional[bool] = None
    InstanceType: Optional[InstanceTypeType] = None
    MaxDuration: Optional[int] = None
    MaxInstanceCount: Optional[int] = None
    MinDuration: Optional[int] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    ReservedInstancesOfferingIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    InstanceTenancy: Optional[TenancyType] = None
    OfferingType: Optional[OfferingTypeValuesType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_reserved_instances' function.
class DescribeReservedInstancesRequest(BaseValidatorModel):
    OfferingClass: Optional[OfferingClassTypeType] = None
    ReservedInstancesIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    OfferingType: Optional[OfferingTypeValuesType] = None


class DescribeRouteTablesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    RouteTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_route_tables' function.
class DescribeRouteTablesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    RouteTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


class DescribeSecurityGroupRulesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    SecurityGroupRuleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_security_group_rules' function.
class DescribeSecurityGroupRulesRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    SecurityGroupRuleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeSecurityGroupVpcAssociationsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_security_group_vpc_associations' function.
class DescribeSecurityGroupVpcAssociationsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


class DescribeSecurityGroupsRequestPaginate(BaseValidatorModel):
    GroupIds: Optional[List[str]] = None
    GroupNames: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_security_groups' function.
class DescribeSecurityGroupsRequest(BaseValidatorModel):
    GroupIds: Optional[List[str]] = None
    GroupNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeSnapshotTierStatusRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_snapshot_tier_status' function.
class DescribeSnapshotTierStatusRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeSnapshotsRequestPaginate(BaseValidatorModel):
    OwnerIds: Optional[List[str]] = None
    RestorableByUserIds: Optional[List[str]] = None
    SnapshotIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_snapshots' function.
class DescribeSnapshotsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerIds: Optional[List[str]] = None
    RestorableByUserIds: Optional[List[str]] = None
    SnapshotIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeSpotInstanceRequestsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_spot_instance_requests' function.
class DescribeSpotInstanceRequestsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


class DescribeSpotPriceHistoryRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    InstanceTypes: Optional[List[InstanceTypeType]] = None
    ProductDescriptions: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    AvailabilityZone: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_spot_price_history' function.
class DescribeSpotPriceHistoryRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    InstanceTypes: Optional[List[InstanceTypeType]] = None
    ProductDescriptions: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    AvailabilityZone: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeStoreImageTasksRequestPaginate(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_store_image_tasks' function.
class DescribeStoreImageTasksRequest(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeSubnetsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    SubnetIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_subnets' function.
class DescribeSubnetsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    SubnetIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


class DescribeTagsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_traffic_mirror_filter_rules' function.
class DescribeTrafficMirrorFilterRulesRequest(BaseValidatorModel):
    TrafficMirrorFilterRuleIds: Optional[List[str]] = None
    TrafficMirrorFilterId: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeTrafficMirrorFiltersRequestPaginate(BaseValidatorModel):
    TrafficMirrorFilterIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_traffic_mirror_filters' function.
class DescribeTrafficMirrorFiltersRequest(BaseValidatorModel):
    TrafficMirrorFilterIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeTrafficMirrorSessionsRequestPaginate(BaseValidatorModel):
    TrafficMirrorSessionIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_traffic_mirror_sessions' function.
class DescribeTrafficMirrorSessionsRequest(BaseValidatorModel):
    TrafficMirrorSessionIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeTrafficMirrorTargetsRequestPaginate(BaseValidatorModel):
    TrafficMirrorTargetIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_traffic_mirror_targets' function.
class DescribeTrafficMirrorTargetsRequest(BaseValidatorModel):
    TrafficMirrorTargetIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeTransitGatewayAttachmentsRequestPaginate(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_attachments' function.
class DescribeTransitGatewayAttachmentsRequest(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayConnectPeersRequestPaginate(BaseValidatorModel):
    TransitGatewayConnectPeerIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_connect_peers' function.
class DescribeTransitGatewayConnectPeersRequest(BaseValidatorModel):
    TransitGatewayConnectPeerIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayConnectsRequestPaginate(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_connects' function.
class DescribeTransitGatewayConnectsRequest(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayMulticastDomainsRequestPaginate(BaseValidatorModel):
    TransitGatewayMulticastDomainIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_multicast_domains' function.
class DescribeTransitGatewayMulticastDomainsRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayPeeringAttachmentsRequestPaginate(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_peering_attachments' function.
class DescribeTransitGatewayPeeringAttachmentsRequest(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayPolicyTablesRequestPaginate(BaseValidatorModel):
    TransitGatewayPolicyTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_policy_tables' function.
class DescribeTransitGatewayPolicyTablesRequest(BaseValidatorModel):
    TransitGatewayPolicyTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayRouteTableAnnouncementsRequestPaginate(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncementIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_route_table_announcements' function.
class DescribeTransitGatewayRouteTableAnnouncementsRequest(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncementIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayRouteTablesRequestPaginate(BaseValidatorModel):
    TransitGatewayRouteTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_route_tables' function.
class DescribeTransitGatewayRouteTablesRequest(BaseValidatorModel):
    TransitGatewayRouteTableIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewayVpcAttachmentsRequestPaginate(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateway_vpc_attachments' function.
class DescribeTransitGatewayVpcAttachmentsRequest(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTransitGatewaysRequestPaginate(BaseValidatorModel):
    TransitGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_transit_gateways' function.
class DescribeTransitGatewaysRequest(BaseValidatorModel):
    TransitGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class DescribeTrunkInterfaceAssociationsRequestPaginate(BaseValidatorModel):
    AssociationIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_trunk_interface_associations' function.
class DescribeTrunkInterfaceAssociationsRequest(BaseValidatorModel):
    AssociationIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeVerifiedAccessEndpointsRequestPaginate(BaseValidatorModel):
    VerifiedAccessEndpointIds: Optional[List[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_verified_access_endpoints' function.
class DescribeVerifiedAccessEndpointsRequest(BaseValidatorModel):
    VerifiedAccessEndpointIds: Optional[List[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeVerifiedAccessGroupsRequestPaginate(BaseValidatorModel):
    VerifiedAccessGroupIds: Optional[List[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_verified_access_groups' function.
class DescribeVerifiedAccessGroupsRequest(BaseValidatorModel):
    VerifiedAccessGroupIds: Optional[List[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeVerifiedAccessInstanceLoggingConfigurationsRequestPaginate(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_verified_access_instance_logging_configurations' function.
class DescribeVerifiedAccessInstanceLoggingConfigurationsRequest(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeVerifiedAccessInstancesRequestPaginate(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_verified_access_instances' function.
class DescribeVerifiedAccessInstancesRequest(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeVerifiedAccessTrustProvidersRequestPaginate(BaseValidatorModel):
    VerifiedAccessTrustProviderIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_verified_access_trust_providers' function.
class DescribeVerifiedAccessTrustProvidersRequest(BaseValidatorModel):
    VerifiedAccessTrustProviderIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


class DescribeVolumeStatusRequestPaginate(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_volume_status' function.
class DescribeVolumeStatusRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VolumeIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeVolumeStatusRequestVolumeDescribeStatus(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None


class DescribeVolumesModificationsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VolumeIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_volumes_modifications' function.
class DescribeVolumesModificationsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VolumeIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeVolumesRequestPaginate(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_volumes' function.
class DescribeVolumesRequest(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_vpc_block_public_access_exclusions' function.
class DescribeVpcBlockPublicAccessExclusionsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ExclusionIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_vpc_classic_link' function.
class DescribeVpcClassicLinkRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VpcIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_vpc_endpoint_associations' function.
class DescribeVpcEndpointAssociationsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VpcEndpointIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointConnectionNotificationsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConnectionNotificationId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpc_endpoint_connection_notifications' function.
class DescribeVpcEndpointConnectionNotificationsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConnectionNotificationId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointConnectionsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpc_endpoint_connections' function.
class DescribeVpcEndpointConnectionsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointServiceConfigurationsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpc_endpoint_service_configurations' function.
class DescribeVpcEndpointServiceConfigurationsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointServicePermissionsRequestPaginate(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpc_endpoint_service_permissions' function.
class DescribeVpcEndpointServicePermissionsRequest(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcEndpointServicesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    ServiceRegions: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpc_endpoint_services' function.
class DescribeVpcEndpointServicesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceNames: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ServiceRegions: Optional[List[str]] = None


class DescribeVpcEndpointsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VpcEndpointIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpc_endpoints' function.
class DescribeVpcEndpointsRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VpcEndpointIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeVpcPeeringConnectionsRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpc_peering_connections' function.
class DescribeVpcPeeringConnectionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None


class DescribeVpcsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpcIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_vpcs' function.
class DescribeVpcsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpcIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_vpn_connections' function.
class DescribeVpnConnectionsRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpnConnectionIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'describe_vpn_gateways' function.
class DescribeVpnGatewaysRequest(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpnGatewayIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'export_transit_gateway_routes' function.
class ExportTransitGatewayRoutesRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    S3Bucket: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_coip_pool_usage' function.
class GetCoipPoolUsageRequest(BaseValidatorModel):
    PoolId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class GetIpamDiscoveredAccountsRequestPaginate(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DiscoveryRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_ipam_discovered_accounts' function.
class GetIpamDiscoveredAccountsRequest(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DiscoveryRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'get_ipam_discovered_public_addresses' function.
class GetIpamDiscoveredPublicAddressesRequest(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    AddressRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetIpamDiscoveredResourceCidrsRequestPaginate(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    ResourceRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_ipam_discovered_resource_cidrs' function.
class GetIpamDiscoveredResourceCidrsRequest(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    ResourceRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetIpamPoolAllocationsRequestPaginate(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    IpamPoolAllocationId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_ipam_pool_allocations' function.
class GetIpamPoolAllocationsRequest(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    IpamPoolAllocationId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetIpamPoolCidrsRequestPaginate(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_ipam_pool_cidrs' function.
class GetIpamPoolCidrsRequest(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetIpamResourceCidrsRequestPaginate(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IpamPoolId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTag: Optional[RequestIpamResourceTag] = None
    ResourceOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_ipam_resource_cidrs' function.
class GetIpamResourceCidrsRequest(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamPoolId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTag: Optional[RequestIpamResourceTag] = None
    ResourceOwner: Optional[str] = None


class GetSecurityGroupsForVpcRequestPaginate(BaseValidatorModel):
    VpcId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_security_groups_for_vpc' function.
class GetSecurityGroupsForVpcRequest(BaseValidatorModel):
    VpcId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_subnet_cidr_reservations' function.
class GetSubnetCidrReservationsRequest(BaseValidatorModel):
    SubnetId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetTransitGatewayAttachmentPropagationsRequestPaginate(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_transit_gateway_attachment_propagations' function.
class GetTransitGatewayAttachmentPropagationsRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class GetTransitGatewayMulticastDomainAssociationsRequestPaginate(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_transit_gateway_multicast_domain_associations' function.
class GetTransitGatewayMulticastDomainAssociationsRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class GetTransitGatewayPolicyTableAssociationsRequestPaginate(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_transit_gateway_policy_table_associations' function.
class GetTransitGatewayPolicyTableAssociationsRequest(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'get_transit_gateway_policy_table_entries' function.
class GetTransitGatewayPolicyTableEntriesRequest(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class GetTransitGatewayPrefixListReferencesRequestPaginate(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_transit_gateway_prefix_list_references' function.
class GetTransitGatewayPrefixListReferencesRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class GetTransitGatewayRouteTableAssociationsRequestPaginate(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_transit_gateway_route_table_associations' function.
class GetTransitGatewayRouteTableAssociationsRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class GetTransitGatewayRouteTablePropagationsRequestPaginate(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_transit_gateway_route_table_propagations' function.
class GetTransitGatewayRouteTablePropagationsRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class SearchLocalGatewayRoutesRequestPaginate(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_local_gateway_routes' function.
class SearchLocalGatewayRoutesRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


class SearchTransitGatewayMulticastGroupsRequestPaginate(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_transit_gateway_multicast_groups' function.
class SearchTransitGatewayMulticastGroupsRequest(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'search_transit_gateway_routes' function.
class SearchTransitGatewayRoutesRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: List[Filter]
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the output for the 'describe_aggregate_id_format' function.
class DescribeAggregateIdFormatResult(BaseValidatorModel):
    UseLongIdsAggregated: bool
    Statuses: List[IdFormat]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_id_format' function.
class DescribeIdFormatResult(BaseValidatorModel):
    Statuses: List[IdFormat]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_identity_id_format' function.
class DescribeIdentityIdFormatResult(BaseValidatorModel):
    Statuses: List[IdFormat]
    ResponseMetadata: ResponseMetadata


class PrincipalIdFormat(BaseValidatorModel):
    Arn: Optional[str] = None
    Statuses: Optional[List[IdFormat]] = None


# This class is the output for the 'describe_aws_network_performance_metric_subscriptions' function.
class DescribeAwsNetworkPerformanceMetricSubscriptionsResult(BaseValidatorModel):
    Subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeBundleTasksRequestWait(BaseValidatorModel):
    BundleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeConversionTasksRequestWaitExtraExtra(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConversionTaskIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeConversionTasksRequestWaitExtra(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConversionTaskIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeConversionTasksRequestWait(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConversionTaskIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeCustomerGatewaysRequestWait(BaseValidatorModel):
    CustomerGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeExportTasksRequestWaitExtra(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    ExportTaskIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeExportTasksRequestWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    ExportTaskIds: Optional[List[str]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImagesRequestWaitExtra(BaseValidatorModel):
    ExecutableUsers: Optional[List[str]] = None
    ImageIds: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImagesRequestWait(BaseValidatorModel):
    ExecutableUsers: Optional[List[str]] = None
    ImageIds: Optional[List[str]] = None
    Owners: Optional[List[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeImportSnapshotTasksRequestWait(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ImportTaskIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstanceStatusRequestWaitExtra(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IncludeAllInstances: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstanceStatusRequestWait(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    IncludeAllInstances: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWaitExtraExtraExtra(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWaitExtraExtra(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWaitExtra(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInstancesRequestWait(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeInternetGatewaysRequestWait(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeKeyPairsRequestWait(BaseValidatorModel):
    KeyNames: Optional[List[str]] = None
    KeyPairIds: Optional[List[str]] = None
    IncludePublicKey: Optional[bool] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNatGatewaysRequestWaitExtra(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNatGatewaysRequestWait(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeNetworkInterfacesRequestWait(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeSecurityGroupsRequestWait(BaseValidatorModel):
    GroupIds: Optional[List[str]] = None
    GroupNames: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeSnapshotsRequestWait(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerIds: Optional[List[str]] = None
    RestorableByUserIds: Optional[List[str]] = None
    SnapshotIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeSpotInstanceRequestsRequestWait(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeStoreImageTasksRequestWait(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeSubnetsRequestWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    SubnetIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVolumesRequestWaitExtraExtra(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVolumesRequestWaitExtra(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVolumesRequestWait(BaseValidatorModel):
    VolumeIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVpcPeeringConnectionsRequestWaitExtra(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVpcPeeringConnectionsRequestWait(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVpcsRequestWaitExtra(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpcIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVpcsRequestWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpcIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVpnConnectionsRequestWaitExtra(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpnConnectionIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeVpnConnectionsRequestWait(BaseValidatorModel):
    Filters: Optional[List[Filter]] = None
    VpnConnectionIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class GetPasswordDataRequestWait(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeFastLaunchImagesSuccessItem(BaseValidatorModel):
    ImageId: Optional[str] = None
    ResourceType: Optional[Literal['snapshot']] = None
    SnapshotConfiguration: Optional[FastLaunchSnapshotConfigurationResponse] = None
    LaunchTemplate: Optional[FastLaunchLaunchTemplateSpecificationResponse] = None
    MaxParallelLaunches: Optional[int] = None
    OwnerId: Optional[str] = None
    State: Optional[FastLaunchStateCodeType] = None
    StateTransitionReason: Optional[str] = None
    StateTransitionTime: Optional[datetime] = None


# This class is the output for the 'disable_fast_launch' function.
class DisableFastLaunchResult(BaseValidatorModel):
    ImageId: str
    ResourceType: Literal['snapshot']
    SnapshotConfiguration: FastLaunchSnapshotConfigurationResponse
    LaunchTemplate: FastLaunchLaunchTemplateSpecificationResponse
    MaxParallelLaunches: int
    OwnerId: str
    State: FastLaunchStateCodeType
    StateTransitionReason: str
    StateTransitionTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_fast_launch' function.
class EnableFastLaunchResult(BaseValidatorModel):
    ImageId: str
    ResourceType: Literal['snapshot']
    SnapshotConfiguration: FastLaunchSnapshotConfigurationResponse
    LaunchTemplate: FastLaunchLaunchTemplateSpecificationResponse
    MaxParallelLaunches: int
    OwnerId: str
    State: FastLaunchStateCodeType
    StateTransitionReason: str
    StateTransitionTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fast_snapshot_restores' function.
class DescribeFastSnapshotRestoresResult(BaseValidatorModel):
    FastSnapshotRestores: List[DescribeFastSnapshotRestoreSuccessItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_host_reservation_offerings' function.
class DescribeHostReservationOfferingsResult(BaseValidatorModel):
    OfferingSet: List[HostOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_instance_credit_specifications' function.
class DescribeInstanceCreditSpecificationsResult(BaseValidatorModel):
    InstanceCreditSpecifications: List[InstanceCreditSpecification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_instance_topology' function.
class DescribeInstanceTopologyResult(BaseValidatorModel):
    Instances: List[InstanceTopology]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_instance_type_offerings' function.
class DescribeInstanceTypeOfferingsResult(BaseValidatorModel):
    InstanceTypeOfferings: List[InstanceTypeOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_locked_snapshots' function.
class DescribeLockedSnapshotsResult(BaseValidatorModel):
    Snapshots: List[LockedSnapshotsInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_mac_hosts' function.
class DescribeMacHostsResult(BaseValidatorModel):
    MacHosts: List[MacHost]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_moving_addresses' function.
class DescribeMovingAddressesResult(BaseValidatorModel):
    MovingAddressStatuses: List[MovingAddressStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_prefix_lists' function.
class DescribePrefixListsResult(BaseValidatorModel):
    PrefixLists: List[PrefixList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_regions' function.
class DescribeRegionsResult(BaseValidatorModel):
    Regions: List[Region]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_security_group_references' function.
class DescribeSecurityGroupReferencesResult(BaseValidatorModel):
    SecurityGroupReferenceSet: List[SecurityGroupReference]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_security_group_vpc_associations' function.
class DescribeSecurityGroupVpcAssociationsResult(BaseValidatorModel):
    SecurityGroupVpcAssociations: List[SecurityGroupVpcAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_snapshot_attribute' function.
class DescribeSnapshotAttributeResult(BaseValidatorModel):
    ProductCodes: List[ProductCode]
    SnapshotId: str
    CreateVolumePermissions: List[CreateVolumePermission]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_volume_attribute' function.
class DescribeVolumeAttributeResult(BaseValidatorModel):
    AutoEnableIO: AttributeBooleanValue
    ProductCodes: List[ProductCode]
    VolumeId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_spot_price_history' function.
class DescribeSpotPriceHistoryResult(BaseValidatorModel):
    SpotPriceHistory: List[SpotPrice]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_store_image_tasks' function.
class DescribeStoreImageTasksResult(BaseValidatorModel):
    StoreImageTaskResults: List[StoreImageTaskResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_tags' function.
class DescribeTagsResult(BaseValidatorModel):
    Tags: List[TagDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_volumes_modifications' function.
class DescribeVolumesModificationsResult(BaseValidatorModel):
    VolumesModifications: List[VolumeModification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_volume' function.
class ModifyVolumeResult(BaseValidatorModel):
    VolumeModification: VolumeModification
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_block_public_access_options' function.
class DescribeVpcBlockPublicAccessOptionsResult(BaseValidatorModel):
    VpcBlockPublicAccessOptions: VpcBlockPublicAccessOptions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpc_block_public_access_options' function.
class ModifyVpcBlockPublicAccessOptionsResult(BaseValidatorModel):
    VpcBlockPublicAccessOptions: VpcBlockPublicAccessOptions
    ResponseMetadata: ResponseMetadata


class FlowLog(BaseValidatorModel):
    CreationTime: Optional[datetime] = None
    DeliverLogsErrorMessage: Optional[str] = None
    DeliverLogsPermissionArn: Optional[str] = None
    DeliverCrossAccountRole: Optional[str] = None
    DeliverLogsStatus: Optional[str] = None
    FlowLogId: Optional[str] = None
    FlowLogStatus: Optional[str] = None
    LogGroupName: Optional[str] = None
    ResourceId: Optional[str] = None
    TrafficType: Optional[TrafficTypeType] = None
    LogDestinationType: Optional[LogDestinationTypeType] = None
    LogDestination: Optional[str] = None
    LogFormat: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    MaxAggregationInterval: Optional[int] = None
    DestinationOptions: Optional[DestinationOptionsResponse] = None


class DisableFastSnapshotRestoreStateErrorItem(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Error: Optional[DisableFastSnapshotRestoreStateError] = None


# This class is the output for the 'disable_transit_gateway_route_table_propagation' function.
class DisableTransitGatewayRouteTablePropagationResult(BaseValidatorModel):
    Propagation: TransitGatewayPropagation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_transit_gateway_route_table_propagation' function.
class EnableTransitGatewayRouteTablePropagationResult(BaseValidatorModel):
    Propagation: TransitGatewayPropagation
    ResponseMetadata: ResponseMetadata


class DiskImage(BaseValidatorModel):
    Description: Optional[str] = None
    Image: Optional[DiskImageDetail] = None
    Volume: Optional[VolumeDetail] = None


# This class is the input for the 'import_volume' function.
class ImportVolumeRequest(BaseValidatorModel):
    AvailabilityZone: str
    Image: DiskImageDetail
    Volume: VolumeDetail
    DryRun: Optional[bool] = None
    Description: Optional[str] = None


class ImportInstanceVolumeDetailItem(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    BytesConverted: Optional[int] = None
    Description: Optional[str] = None
    Image: Optional[DiskImageDescription] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Volume: Optional[DiskImageVolumeDescription] = None


class ImportVolumeTaskDetails(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    BytesConverted: Optional[int] = None
    Description: Optional[str] = None
    Image: Optional[DiskImageDescription] = None
    Volume: Optional[DiskImageVolumeDescription] = None


class InstanceStorageInfo(BaseValidatorModel):
    TotalSizeInGB: Optional[int] = None
    Disks: Optional[List[DiskInfo]] = None
    NvmeSupport: Optional[EphemeralNvmeSupportType] = None
    EncryptionSupport: Optional[InstanceStorageEncryptionSupportType] = None


class VpcEndpointAssociation(BaseValidatorModel):
    Id: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    ServiceNetworkArn: Optional[str] = None
    ServiceNetworkName: Optional[str] = None
    AssociatedResourceAccessibility: Optional[str] = None
    FailureReason: Optional[str] = None
    FailureCode: Optional[str] = None
    DnsEntry: Optional[DnsEntry] = None
    PrivateDnsEntry: Optional[DnsEntry] = None
    AssociatedResourceArn: Optional[str] = None
    ResourceConfigurationGroupArn: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class VpcEndpointConnection(BaseValidatorModel):
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    VpcEndpointState: Optional[StateType] = None
    CreationTimestamp: Optional[datetime] = None
    DnsEntries: Optional[List[DnsEntry]] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    VpcEndpointConnectionId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    VpcEndpointRegion: Optional[str] = None


# This class is the input for the 'modify_client_vpn_endpoint' function.
class ModifyClientVpnEndpointRequest(BaseValidatorModel):
    ClientVpnEndpointId: str
    ServerCertificateArn: Optional[str] = None
    ConnectionLogOptions: Optional[ConnectionLogOptions] = None
    DnsServers: Optional[DnsServersOptionsModifyStructure] = None
    VpnPort: Optional[int] = None
    Description: Optional[str] = None
    SplitTunnel: Optional[bool] = None
    DryRun: Optional[bool] = None
    SecurityGroupIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortal: Optional[SelfServicePortalType] = None
    ClientConnectOptions: Optional[ClientConnectOptions] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ClientLoginBannerOptions] = None
    DisconnectOnSessionTimeout: Optional[bool] = None


class EbsInfo(BaseValidatorModel):
    EbsOptimizedSupport: Optional[EbsOptimizedSupportType] = None
    EncryptionSupport: Optional[EbsEncryptionSupportType] = None
    EbsOptimizedInfo: Optional[EbsOptimizedInfo] = None
    NvmeSupport: Optional[EbsNvmeSupportType] = None


class InstanceBlockDeviceMappingSpecification(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[EbsInstanceBlockDeviceSpecification] = None
    VirtualName: Optional[str] = None
    NoDevice: Optional[str] = None


class EbsInstanceBlockDevice(BaseValidatorModel):
    AttachTime: Optional[datetime] = None
    DeleteOnTermination: Optional[bool] = None
    Status: Optional[AttachmentStatusType] = None
    VolumeId: Optional[str] = None
    AssociatedResource: Optional[str] = None
    VolumeOwnerId: Optional[str] = None
    Operator: Optional[OperatorResponse] = None


class LaunchTemplate(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    CreateTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    Operator: Optional[OperatorResponse] = None


class EbsStatusSummary(BaseValidatorModel):
    Details: Optional[List[EbsStatusDetails]] = None
    Status: Optional[SummaryStatusType] = None


class EgressOnlyInternetGateway(BaseValidatorModel):
    Attachments: Optional[List[InternetGatewayAttachment]] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class InternetGateway(BaseValidatorModel):
    Attachments: Optional[List[InternetGatewayAttachment]] = None
    InternetGatewayId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ElasticGpus(BaseValidatorModel):
    ElasticGpuId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    ElasticGpuType: Optional[str] = None
    ElasticGpuHealth: Optional[ElasticGpuHealth] = None
    ElasticGpuState: Optional[Literal['ATTACHED']] = None
    InstanceId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class EnaSrdSpecificationRequest(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[EnaSrdUdpSpecificationRequest] = None


class EnaSrdSpecification(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[EnaSrdUdpSpecification] = None


# This class is the input for the 'enable_fast_launch' function.
class EnableFastLaunchRequest(BaseValidatorModel):
    ImageId: str
    ResourceType: Optional[str] = None
    SnapshotConfiguration: Optional[FastLaunchSnapshotConfigurationRequest] = None
    LaunchTemplate: Optional[FastLaunchLaunchTemplateSpecificationRequest] = None
    MaxParallelLaunches: Optional[int] = None
    DryRun: Optional[bool] = None


class EnableFastSnapshotRestoreStateErrorItem(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Error: Optional[EnableFastSnapshotRestoreStateError] = None


class HistoryRecordEntry(BaseValidatorModel):
    EventInformation: Optional[EventInformation] = None
    EventType: Optional[FleetEventTypeType] = None
    Timestamp: Optional[datetime] = None


class HistoryRecord(BaseValidatorModel):
    EventInformation: Optional[EventInformation] = None
    EventType: Optional[EventTypeType] = None
    Timestamp: Optional[datetime] = None


# This class is the output for the 'export_image' function.
class ExportImageResult(BaseValidatorModel):
    Description: str
    DiskImageFormat: DiskImageFormatType
    ExportImageTaskId: str
    ImageId: str
    RoleName: str
    Progress: str
    S3ExportLocation: ExportTaskS3Location
    Status: str
    StatusMessage: str
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ExportImageTask(BaseValidatorModel):
    Description: Optional[str] = None
    ExportImageTaskId: Optional[str] = None
    ImageId: Optional[str] = None
    Progress: Optional[str] = None
    S3ExportLocation: Optional[ExportTaskS3Location] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class ExportTask(BaseValidatorModel):
    Description: Optional[str] = None
    ExportTaskId: Optional[str] = None
    ExportToS3Task: Optional[ExportToS3Task] = None
    InstanceExportDetails: Optional[InstanceExportDetails] = None
    State: Optional[ExportTaskStateType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class PathFilter(BaseValidatorModel):
    SourceAddress: Optional[str] = None
    SourcePortRange: Optional[FilterPortRange] = None
    DestinationAddress: Optional[str] = None
    DestinationPortRange: Optional[FilterPortRange] = None


class FleetBlockDeviceMappingRequest(BaseValidatorModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[FleetEbsBlockDeviceRequest] = None
    NoDevice: Optional[str] = None


class FleetSpotMaintenanceStrategiesRequest(BaseValidatorModel):
    CapacityRebalance: Optional[FleetSpotCapacityRebalanceRequest] = None


class FleetSpotMaintenanceStrategies(BaseValidatorModel):
    CapacityRebalance: Optional[FleetSpotCapacityRebalance] = None


class FpgaDeviceInfo(BaseValidatorModel):
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    Count: Optional[int] = None
    MemoryInfo: Optional[FpgaDeviceMemoryInfo] = None


class FpgaImageAttribute(BaseValidatorModel):
    FpgaImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoadPermissions: Optional[List[LoadPermission]] = None
    ProductCodes: Optional[List[ProductCode]] = None


class FpgaImage(BaseValidatorModel):
    FpgaImageId: Optional[str] = None
    FpgaImageGlobalId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ShellVersion: Optional[str] = None
    PciId: Optional[PciId] = None
    State: Optional[FpgaImageState] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    OwnerId: Optional[str] = None
    OwnerAlias: Optional[str] = None
    ProductCodes: Optional[List[ProductCode]] = None
    Tags: Optional[List[Tag]] = None
    Public: Optional[bool] = None
    DataRetentionSupport: Optional[bool] = None
    InstanceTypes: Optional[List[str]] = None


# This class is the output for the 'get_allowed_images_settings' function.
class GetAllowedImagesSettingsResult(BaseValidatorModel):
    State: str
    ImageCriteria: List[ImageCriterion]
    ManagedBy: ManagedByType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_associated_ipv6_pool_cidrs' function.
class GetAssociatedIpv6PoolCidrsResult(BaseValidatorModel):
    Ipv6CidrAssociations: List[Ipv6CidrAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_capacity_reservation_usage' function.
class GetCapacityReservationUsageResult(BaseValidatorModel):
    CapacityReservationId: str
    InstanceType: str
    TotalInstanceCount: int
    AvailableInstanceCount: int
    State: CapacityReservationStateType
    InstanceUsages: List[InstanceUsage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_default_credit_specification' function.
class GetDefaultCreditSpecificationResult(BaseValidatorModel):
    InstanceFamilyCreditSpecification: InstanceFamilyCreditSpecification
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_default_credit_specification' function.
class ModifyDefaultCreditSpecificationResult(BaseValidatorModel):
    InstanceFamilyCreditSpecification: InstanceFamilyCreditSpecification
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_host_reservation_purchase_preview' function.
class GetHostReservationPurchasePreviewResult(BaseValidatorModel):
    CurrencyCode: Literal['USD']
    Purchase: List[Purchase]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'purchase_host_reservation' function.
class PurchaseHostReservationResult(BaseValidatorModel):
    ClientToken: str
    CurrencyCode: Literal['USD']
    Purchase: List[Purchase]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_metadata_defaults' function.
class GetInstanceMetadataDefaultsResult(BaseValidatorModel):
    AccountLevel: InstanceMetadataDefaultsResponse
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_instance_types_from_instance_requirements' function.
class GetInstanceTypesFromInstanceRequirementsResult(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeInfoFromInstanceRequirements]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_ipam_address_history' function.
class GetIpamAddressHistoryResult(BaseValidatorModel):
    HistoryRecords: List[IpamAddressHistoryRecord]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_managed_prefix_list_associations' function.
class GetManagedPrefixListAssociationsResult(BaseValidatorModel):
    PrefixListAssociations: List[PrefixListAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_managed_prefix_list_entries' function.
class GetManagedPrefixListEntriesResult(BaseValidatorModel):
    Entries: List[PrefixListEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ReservedInstanceReservationValue(BaseValidatorModel):
    ReservationValue: Optional[ReservationValue] = None
    ReservedInstanceId: Optional[str] = None


# This class is the output for the 'get_spot_placement_scores' function.
class GetSpotPlacementScoresResult(BaseValidatorModel):
    SpotPlacementScores: List[SpotPlacementScore]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_transit_gateway_attachment_propagations' function.
class GetTransitGatewayAttachmentPropagationsResult(BaseValidatorModel):
    TransitGatewayAttachmentPropagations: List[TransitGatewayAttachmentPropagation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_transit_gateway_route_table_associations' function.
class GetTransitGatewayRouteTableAssociationsResult(BaseValidatorModel):
    Associations: List[TransitGatewayRouteTableAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_transit_gateway_route_table_propagations' function.
class GetTransitGatewayRouteTablePropagationsResult(BaseValidatorModel):
    TransitGatewayRouteTablePropagations: List[TransitGatewayRouteTablePropagation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_verified_access_endpoint_targets' function.
class GetVerifiedAccessEndpointTargetsResult(BaseValidatorModel):
    VerifiedAccessEndpointTargets: List[VerifiedAccessEndpointTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_vpn_connection_device_types' function.
class GetVpnConnectionDeviceTypesResult(BaseValidatorModel):
    VpnConnectionDeviceTypes: List[VpnConnectionDeviceType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_vpn_tunnel_replacement_status' function.
class GetVpnTunnelReplacementStatusResult(BaseValidatorModel):
    VpnConnectionId: str
    TransitGatewayId: str
    CustomerGatewayId: str
    VpnGatewayId: str
    VpnTunnelOutsideIpAddress: str
    MaintenanceDetails: MaintenanceDetails
    ResponseMetadata: ResponseMetadata


class GpuDeviceInfo(BaseValidatorModel):
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    Count: Optional[int] = None
    MemoryInfo: Optional[GpuDeviceMemoryInfo] = None


class IamInstanceProfileAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    InstanceId: Optional[str] = None
    IamInstanceProfile: Optional[IamInstanceProfile] = None
    State: Optional[IamInstanceProfileAssociationStateType] = None
    Timestamp: Optional[datetime] = None


class LaunchPermissionModifications(BaseValidatorModel):
    Add: Optional[List[LaunchPermission]] = None
    Remove: Optional[List[LaunchPermission]] = None


# This class is the input for the 'replace_image_criteria_in_allowed_images_settings' function.
class ReplaceImageCriteriaInAllowedImagesSettingsRequest(BaseValidatorModel):
    ImageCriteria: Optional[List[ImageCriterionRequest]] = None
    DryRun: Optional[bool] = None


class ImageDiskContainer(BaseValidatorModel):
    Description: Optional[str] = None
    DeviceName: Optional[str] = None
    Format: Optional[str] = None
    SnapshotId: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucket] = None


class SnapshotDiskContainer(BaseValidatorModel):
    Description: Optional[str] = None
    Format: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucket] = None


# This class is the output for the 'list_images_in_recycle_bin' function.
class ListImagesInRecycleBinResult(BaseValidatorModel):
    Images: List[ImageRecycleBinInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LocalGatewayRouteTable(BaseValidatorModel):
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    Mode: Optional[LocalGatewayRouteTableModeType] = None
    StateReason: Optional[StateReason] = None


class ImportInstanceLaunchSpecification(BaseValidatorModel):
    Architecture: Optional[ArchitectureValuesType] = None
    GroupNames: Optional[List[str]] = None
    GroupIds: Optional[List[str]] = None
    AdditionalInfo: Optional[str] = None
    UserData: Optional[UserData] = None
    InstanceType: Optional[InstanceTypeType] = None
    Placement: Optional[Placement] = None
    Monitoring: Optional[bool] = None
    SubnetId: Optional[str] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    PrivateIpAddress: Optional[str] = None


class InferenceDeviceInfo(BaseValidatorModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    MemoryInfo: Optional[InferenceDeviceMemoryInfo] = None


class InstanceAttachmentEnaSrdSpecification(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[InstanceAttachmentEnaSrdUdpSpecification] = None


# This class is the input for the 'modify_instance_credit_specification' function.
class ModifyInstanceCreditSpecificationRequest(BaseValidatorModel):
    InstanceCreditSpecifications: List[InstanceCreditSpecificationRequest]
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


class InstanceImageMetadata(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    LaunchTime: Optional[datetime] = None
    AvailabilityZone: Optional[str] = None
    ZoneId: Optional[str] = None
    State: Optional[InstanceState] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ImageMetadata: Optional[ImageMetadata] = None
    Operator: Optional[OperatorResponse] = None


class InstanceStateChange(BaseValidatorModel):
    InstanceId: Optional[str] = None
    CurrentState: Optional[InstanceState] = None
    PreviousState: Optional[InstanceState] = None


# This class is the output for the 'modify_instance_metadata_options' function.
class ModifyInstanceMetadataOptionsResult(BaseValidatorModel):
    InstanceId: str
    InstanceMetadataOptions: InstanceMetadataOptionsResponse
    ResponseMetadata: ResponseMetadata


class InstanceMonitoring(BaseValidatorModel):
    InstanceId: Optional[str] = None
    Monitoring: Optional[Monitoring] = None


class InstancePrivateIpAddress(BaseValidatorModel):
    Association: Optional[InstanceNetworkInterfaceAssociation] = None
    Primary: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None


class InstanceStatusSummary(BaseValidatorModel):
    Details: Optional[List[InstanceStatusDetails]] = None
    Status: Optional[SummaryStatusType] = None


# This class is the output for the 'modify_instance_event_start_time' function.
class ModifyInstanceEventStartTimeResult(BaseValidatorModel):
    Event: InstanceStatusEvent
    ResponseMetadata: ResponseMetadata


class IpPermissionOutput(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPair]] = None
    IpRanges: Optional[List[IpRange]] = None
    Ipv6Ranges: Optional[List[Ipv6Range]] = None
    PrefixListIds: Optional[List[PrefixListId]] = None


class IpPermission(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPair]] = None
    IpRanges: Optional[List[IpRange]] = None
    Ipv6Ranges: Optional[List[Ipv6Range]] = None
    PrefixListIds: Optional[List[PrefixListId]] = None


class StaleIpPermission(BaseValidatorModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[List[str]] = None
    PrefixListIds: Optional[List[str]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPair]] = None


# This class is the input for the 'provision_ipam_pool_cidr' function.
class ProvisionIpamPoolCidrRequest(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None
    CidrAuthorizationContext: Optional[IpamCidrAuthorizationContext] = None
    NetmaskLength: Optional[int] = None
    ClientToken: Optional[str] = None
    VerificationMethod: Optional[VerificationMethodType] = None
    IpamExternalResourceVerificationTokenId: Optional[str] = None


class IpamDiscoveredAccount(BaseValidatorModel):
    AccountId: Optional[str] = None
    DiscoveryRegion: Optional[str] = None
    FailureReason: Optional[IpamDiscoveryFailureReason] = None
    LastAttemptedDiscoveryTime: Optional[datetime] = None
    LastSuccessfulDiscoveryTime: Optional[datetime] = None
    OrganizationalUnitId: Optional[str] = None


class IpamDiscoveredResourceCidr(BaseValidatorModel):
    IpamResourceDiscoveryId: Optional[str] = None
    ResourceRegion: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    ResourceCidr: Optional[str] = None
    IpSource: Optional[IpamResourceCidrIpSourceType] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTags: Optional[List[IpamResourceTag]] = None
    IpUsage: Optional[float] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    NetworkInterfaceAttachmentStatus: Optional[IpamNetworkInterfaceAttachmentStatusType] = None
    SampleTime: Optional[datetime] = None
    AvailabilityZoneId: Optional[str] = None


class IpamResourceCidr(BaseValidatorModel):
    IpamId: Optional[str] = None
    IpamScopeId: Optional[str] = None
    IpamPoolId: Optional[str] = None
    ResourceRegion: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceName: Optional[str] = None
    ResourceCidr: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTags: Optional[List[IpamResourceTag]] = None
    IpUsage: Optional[float] = None
    ComplianceStatus: Optional[IpamComplianceStatusType] = None
    ManagementState: Optional[IpamManagementStateType] = None
    OverlapStatus: Optional[IpamOverlapStatusType] = None
    VpcId: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None


class Ipam(BaseValidatorModel):
    OwnerId: Optional[str] = None
    IpamId: Optional[str] = None
    IpamArn: Optional[str] = None
    IpamRegion: Optional[str] = None
    PublicDefaultScopeId: Optional[str] = None
    PrivateDefaultScopeId: Optional[str] = None
    ScopeCount: Optional[int] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[List[IpamOperatingRegion]] = None
    State: Optional[IpamStateType] = None
    Tags: Optional[List[Tag]] = None
    DefaultResourceDiscoveryId: Optional[str] = None
    DefaultResourceDiscoveryAssociationId: Optional[str] = None
    ResourceDiscoveryAssociationCount: Optional[int] = None
    StateMessage: Optional[str] = None
    Tier: Optional[IpamTierType] = None
    EnablePrivateGua: Optional[bool] = None


class IpamResourceDiscovery(BaseValidatorModel):
    OwnerId: Optional[str] = None
    IpamResourceDiscoveryId: Optional[str] = None
    IpamResourceDiscoveryArn: Optional[str] = None
    IpamResourceDiscoveryRegion: Optional[str] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[List[IpamOperatingRegion]] = None
    IsDefault: Optional[bool] = None
    State: Optional[IpamResourceDiscoveryStateType] = None
    Tags: Optional[List[Tag]] = None
    OrganizationalUnitExclusions: Optional[List[IpamOrganizationalUnitExclusion]] = None


class IpamPoolCidr(BaseValidatorModel):
    Cidr: Optional[str] = None
    State: Optional[IpamPoolCidrStateType] = None
    FailureReason: Optional[IpamPoolCidrFailureReason] = None
    IpamPoolCidrId: Optional[str] = None
    NetmaskLength: Optional[int] = None


class IpamPool(BaseValidatorModel):
    OwnerId: Optional[str] = None
    IpamPoolId: Optional[str] = None
    SourceIpamPoolId: Optional[str] = None
    IpamPoolArn: Optional[str] = None
    IpamScopeArn: Optional[str] = None
    IpamScopeType: Optional[IpamScopeTypeType] = None
    IpamArn: Optional[str] = None
    IpamRegion: Optional[str] = None
    Locale: Optional[str] = None
    PoolDepth: Optional[int] = None
    State: Optional[IpamPoolStateType] = None
    StateMessage: Optional[str] = None
    Description: Optional[str] = None
    AutoImport: Optional[bool] = None
    PubliclyAdvertisable: Optional[bool] = None
    AddressFamily: Optional[AddressFamilyType] = None
    AllocationMinNetmaskLength: Optional[int] = None
    AllocationMaxNetmaskLength: Optional[int] = None
    AllocationDefaultNetmaskLength: Optional[int] = None
    AllocationResourceTags: Optional[List[IpamResourceTag]] = None
    Tags: Optional[List[Tag]] = None
    AwsService: Optional[Literal['ec2']] = None
    PublicIpSource: Optional[IpamPoolPublicIpSourceType] = None
    SourceResource: Optional[IpamPoolSourceResource] = None


class IpamPublicAddressTags(BaseValidatorModel):
    EipTags: Optional[List[IpamPublicAddressTag]] = None


class Ipv6Pool(BaseValidatorModel):
    PoolId: Optional[str] = None
    Description: Optional[str] = None
    PoolCidrBlocks: Optional[List[PoolCidrBlock]] = None
    Tags: Optional[List[Tag]] = None


class LaunchTemplateBlockDeviceMappingRequest(BaseValidatorModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[LaunchTemplateEbsBlockDeviceRequest] = None
    NoDevice: Optional[str] = None


class LaunchTemplateBlockDeviceMapping(BaseValidatorModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[LaunchTemplateEbsBlockDevice] = None
    NoDevice: Optional[str] = None


class LaunchTemplateEnaSrdSpecification(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[LaunchTemplateEnaSrdUdpSpecification] = None


class LaunchTemplateInstanceMarketOptions(BaseValidatorModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[LaunchTemplateSpotMarketOptions] = None


# This class is the output for the 'list_snapshots_in_recycle_bin' function.
class ListSnapshotsInRecycleBinResult(BaseValidatorModel):
    Snapshots: List[SnapshotRecycleBinInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LoadPermissionModifications(BaseValidatorModel):
    Add: Optional[List[LoadPermissionRequest]] = None
    Remove: Optional[List[LoadPermissionRequest]] = None


class MediaDeviceInfo(BaseValidatorModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    MemoryInfo: Optional[MediaDeviceMemoryInfo] = None


# This class is the input for the 'modify_ipam' function.
class ModifyIpamRequest(BaseValidatorModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AddOperatingRegions: Optional[List[AddIpamOperatingRegion]] = None
    RemoveOperatingRegions: Optional[List[RemoveIpamOperatingRegion]] = None
    Tier: Optional[IpamTierType] = None
    EnablePrivateGua: Optional[bool] = None


# This class is the input for the 'modify_ipam_resource_discovery' function.
class ModifyIpamResourceDiscoveryRequest(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AddOperatingRegions: Optional[List[AddIpamOperatingRegion]] = None
    RemoveOperatingRegions: Optional[List[RemoveIpamOperatingRegion]] = None
    AddOrganizationalUnitExclusions: Optional[List[AddIpamOrganizationalUnitExclusion]] = None
    RemoveOrganizationalUnitExclusions: Optional[List[RemoveIpamOrganizationalUnitExclusion]] = None


# This class is the input for the 'modify_managed_prefix_list' function.
class ModifyManagedPrefixListRequest(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    CurrentVersion: Optional[int] = None
    PrefixListName: Optional[str] = None
    AddEntries: Optional[List[AddPrefixListEntry]] = None
    RemoveEntries: Optional[List[RemovePrefixListEntry]] = None
    MaxEntries: Optional[int] = None


# This class is the input for the 'modify_reserved_instances' function.
class ModifyReservedInstancesRequest(BaseValidatorModel):
    ReservedInstancesIds: List[str]
    TargetConfigurations: List[ReservedInstancesConfiguration]
    ClientToken: Optional[str] = None


class ReservedInstancesModificationResult(BaseValidatorModel):
    ReservedInstancesId: Optional[str] = None
    TargetConfiguration: Optional[ReservedInstancesConfiguration] = None


# This class is the input for the 'modify_transit_gateway' function.
class ModifyTransitGatewayRequest(BaseValidatorModel):
    TransitGatewayId: str
    Description: Optional[str] = None
    Options: Optional[ModifyTransitGatewayOptions] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_transit_gateway_vpc_attachment' function.
class ModifyTransitGatewayVpcAttachmentRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    AddSubnetIds: Optional[List[str]] = None
    RemoveSubnetIds: Optional[List[str]] = None
    Options: Optional[ModifyTransitGatewayVpcAttachmentRequestOptions] = None
    DryRun: Optional[bool] = None


class ModifyVerifiedAccessEndpointCidrOptions(BaseValidatorModel):
    PortRanges: Optional[List[ModifyVerifiedAccessEndpointPortRange]] = None


class ModifyVerifiedAccessEndpointEniOptions(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    PortRanges: Optional[List[ModifyVerifiedAccessEndpointPortRange]] = None


class ModifyVerifiedAccessEndpointLoadBalancerOptions(BaseValidatorModel):
    SubnetIds: Optional[List[str]] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    PortRanges: Optional[List[ModifyVerifiedAccessEndpointPortRange]] = None


# This class is the output for the 'modify_verified_access_endpoint_policy' function.
class ModifyVerifiedAccessEndpointPolicyResult(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    SseSpecification: VerifiedAccessSseSpecificationResponse
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_verified_access_group_policy' function.
class ModifyVerifiedAccessGroupPolicyResult(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    SseSpecification: VerifiedAccessSseSpecificationResponse
    ResponseMetadata: ResponseMetadata


class VerifiedAccessGroup(BaseValidatorModel):
    VerifiedAccessGroupId: Optional[str] = None
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    VerifiedAccessGroupArn: Optional[str] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    DeletionTime: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationResponse] = None


# This class is the input for the 'modify_verified_access_trust_provider' function.
class ModifyVerifiedAccessTrustProviderRequest(BaseValidatorModel):
    VerifiedAccessTrustProviderId: str
    OidcOptions: Optional[ModifyVerifiedAccessTrustProviderOidcOptions] = None
    DeviceOptions: Optional[ModifyVerifiedAccessTrustProviderDeviceOptions] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequest] = None
    NativeApplicationOidcOptions: Optional[ModifyVerifiedAccessNativeApplicationOidcOptions] = None


# This class is the input for the 'modify_vpc_peering_connection_options' function.
class ModifyVpcPeeringConnectionOptionsRequest(BaseValidatorModel):
    VpcPeeringConnectionId: str
    AccepterPeeringConnectionOptions: Optional[PeeringConnectionOptionsRequest] = None
    DryRun: Optional[bool] = None
    RequesterPeeringConnectionOptions: Optional[PeeringConnectionOptionsRequest] = None


# This class is the output for the 'modify_vpc_peering_connection_options' function.
class ModifyVpcPeeringConnectionOptionsResult(BaseValidatorModel):
    AccepterPeeringConnectionOptions: PeeringConnectionOptions
    RequesterPeeringConnectionOptions: PeeringConnectionOptions
    ResponseMetadata: ResponseMetadata


class NatGateway(BaseValidatorModel):
    CreateTime: Optional[datetime] = None
    DeleteTime: Optional[datetime] = None
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None
    NatGatewayAddresses: Optional[List[NatGatewayAddress]] = None
    NatGatewayId: Optional[str] = None
    ProvisionedBandwidth: Optional[ProvisionedBandwidth] = None
    State: Optional[NatGatewayStateType] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ConnectivityType: Optional[ConnectivityTypeType] = None


class NetworkInfo(BaseValidatorModel):
    NetworkPerformance: Optional[str] = None
    MaximumNetworkInterfaces: Optional[int] = None
    MaximumNetworkCards: Optional[int] = None
    DefaultNetworkCardIndex: Optional[int] = None
    NetworkCards: Optional[List[NetworkCardInfo]] = None
    Ipv4AddressesPerInterface: Optional[int] = None
    Ipv6AddressesPerInterface: Optional[int] = None
    Ipv6Supported: Optional[bool] = None
    EnaSupport: Optional[EnaSupportType] = None
    EfaSupported: Optional[bool] = None
    EfaInfo: Optional[EfaInfo] = None
    EncryptionInTransitSupported: Optional[bool] = None
    EnaSrdSupported: Optional[bool] = None
    BandwidthWeightings: Optional[List[BandwidthWeightingTypeType]] = None


class NetworkInterfacePrivateIpAddress(BaseValidatorModel):
    Association: Optional[NetworkInterfaceAssociation] = None
    Primary: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None


class NetworkInterfacePermission(BaseValidatorModel):
    NetworkInterfacePermissionId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    Permission: Optional[InterfacePermissionTypeType] = None
    PermissionState: Optional[NetworkInterfacePermissionState] = None


class NeuronDeviceInfo(BaseValidatorModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    CoreInfo: Optional[NeuronDeviceCoreInfo] = None
    MemoryInfo: Optional[NeuronDeviceMemoryInfo] = None


class VerifiedAccessTrustProvider(BaseValidatorModel):
    VerifiedAccessTrustProviderId: Optional[str] = None
    Description: Optional[str] = None
    TrustProviderType: Optional[TrustProviderTypeType] = None
    UserTrustProviderType: Optional[UserTrustProviderTypeType] = None
    DeviceTrustProviderType: Optional[DeviceTrustProviderTypeType] = None
    OidcOptions: Optional[OidcOptions] = None
    DeviceOptions: Optional[DeviceOptions] = None
    PolicyReferenceName: Optional[str] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationResponse] = None
    NativeApplicationOidcOptions: Optional[NativeApplicationOidcOptions] = None


class PathRequestFilter(BaseValidatorModel):
    SourceAddress: Optional[str] = None
    SourcePortRange: Optional[RequestFilterPortRange] = None
    DestinationAddress: Optional[str] = None
    DestinationPortRange: Optional[RequestFilterPortRange] = None


class PathStatementRequest(BaseValidatorModel):
    PacketHeaderStatement: Optional[PacketHeaderStatementRequest] = None
    ResourceStatement: Optional[ResourceStatementRequest] = None


class ThroughResourcesStatementRequest(BaseValidatorModel):
    ResourceStatement: Optional[ResourceStatementRequest] = None


class PathStatement(BaseValidatorModel):
    PacketHeaderStatement: Optional[PacketHeaderStatement] = None
    ResourceStatement: Optional[ResourceStatement] = None


class ThroughResourcesStatement(BaseValidatorModel):
    ResourceStatement: Optional[ResourceStatement] = None


class ReservedInstancesListing(BaseValidatorModel):
    ClientToken: Optional[str] = None
    CreateDate: Optional[datetime] = None
    InstanceCounts: Optional[List[InstanceCount]] = None
    PriceSchedules: Optional[List[PriceSchedule]] = None
    ReservedInstancesId: Optional[str] = None
    ReservedInstancesListingId: Optional[str] = None
    Status: Optional[ListingStatusType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    UpdateDate: Optional[datetime] = None


# This class is the output for the 'provision_public_ipv4_pool_cidr' function.
class ProvisionPublicIpv4PoolCidrResult(BaseValidatorModel):
    PoolId: str
    PoolAddressRange: PublicIpv4PoolRange
    ResponseMetadata: ResponseMetadata


class PublicIpv4Pool(BaseValidatorModel):
    PoolId: Optional[str] = None
    Description: Optional[str] = None
    PoolAddressRanges: Optional[List[PublicIpv4PoolRange]] = None
    TotalAddressCount: Optional[int] = None
    TotalAvailableAddressCount: Optional[int] = None
    NetworkBorderGroup: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'purchase_scheduled_instances' function.
class PurchaseScheduledInstancesRequest(BaseValidatorModel):
    PurchaseRequests: List[PurchaseRequest]
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'purchase_reserved_instances_offering' function.
class PurchaseReservedInstancesOfferingRequest(BaseValidatorModel):
    InstanceCount: int
    ReservedInstancesOfferingId: str
    PurchaseTime: Optional[Timestamp] = None
    DryRun: Optional[bool] = None
    LimitPrice: Optional[ReservedInstanceLimitPrice] = None


class ReservedInstancesOffering(BaseValidatorModel):
    CurrencyCode: Optional[Literal['USD']] = None
    InstanceTenancy: Optional[TenancyType] = None
    Marketplace: Optional[bool] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    OfferingType: Optional[OfferingTypeValuesType] = None
    PricingDetails: Optional[List[PricingDetail]] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    Scope: Optional[ScopeType] = None
    ReservedInstancesOfferingId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    AvailabilityZone: Optional[str] = None
    Duration: Optional[int] = None
    UsagePrice: Optional[float] = None
    FixedPrice: Optional[float] = None
    ProductDescription: Optional[RIProductDescriptionType] = None


class ReservedInstances(BaseValidatorModel):
    CurrencyCode: Optional[Literal['USD']] = None
    InstanceTenancy: Optional[TenancyType] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    OfferingType: Optional[OfferingTypeValuesType] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    Scope: Optional[ScopeType] = None
    Tags: Optional[List[Tag]] = None
    ReservedInstancesId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    AvailabilityZone: Optional[str] = None
    Start: Optional[datetime] = None
    End: Optional[datetime] = None
    Duration: Optional[int] = None
    UsagePrice: Optional[float] = None
    FixedPrice: Optional[float] = None
    InstanceCount: Optional[int] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    State: Optional[ReservedInstanceStateType] = None


class SecurityGroupRule(BaseValidatorModel):
    SecurityGroupRuleId: Optional[str] = None
    GroupId: Optional[str] = None
    GroupOwnerId: Optional[str] = None
    IsEgress: Optional[bool] = None
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIpv4: Optional[str] = None
    CidrIpv6: Optional[str] = None
    PrefixListId: Optional[str] = None
    ReferencedGroupInfo: Optional[ReferencedSecurityGroup] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SecurityGroupRuleArn: Optional[str] = None


# This class is the input for the 'register_instance_event_notification_attributes' function.
class RegisterInstanceEventNotificationAttributesRequest(BaseValidatorModel):
    InstanceTagAttribute: RegisterInstanceTagAttributeRequest
    DryRun: Optional[bool] = None


# This class is the output for the 'register_transit_gateway_multicast_group_members' function.
class RegisterTransitGatewayMulticastGroupMembersResult(BaseValidatorModel):
    RegisteredMulticastGroupMembers: TransitGatewayMulticastRegisteredGroupMembers
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_transit_gateway_multicast_group_sources' function.
class RegisterTransitGatewayMulticastGroupSourcesResult(BaseValidatorModel):
    RegisteredMulticastGroupSources: TransitGatewayMulticastRegisteredGroupSources
    ResponseMetadata: ResponseMetadata


class StorageOutput(BaseValidatorModel):
    S3: Optional[S3StorageOutput] = None


class ScheduledInstanceAvailability(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailableInstanceCount: Optional[int] = None
    FirstSlotStartTime: Optional[datetime] = None
    HourlyPrice: Optional[str] = None
    InstanceType: Optional[str] = None
    MaxTermDurationInDays: Optional[int] = None
    MinTermDurationInDays: Optional[int] = None
    NetworkPlatform: Optional[str] = None
    Platform: Optional[str] = None
    PurchaseToken: Optional[str] = None
    Recurrence: Optional[ScheduledInstanceRecurrence] = None
    SlotDurationInHours: Optional[int] = None
    TotalScheduledInstanceHours: Optional[int] = None


class ScheduledInstance(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    CreateDate: Optional[datetime] = None
    HourlyPrice: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[str] = None
    NetworkPlatform: Optional[str] = None
    NextSlotStartTime: Optional[datetime] = None
    Platform: Optional[str] = None
    PreviousSlotEndTime: Optional[datetime] = None
    Recurrence: Optional[ScheduledInstanceRecurrence] = None
    ScheduledInstanceId: Optional[str] = None
    SlotDurationInHours: Optional[int] = None
    TermEndDate: Optional[datetime] = None
    TermStartDate: Optional[datetime] = None
    TotalScheduledInstanceHours: Optional[int] = None


class ScheduledInstancesBlockDeviceMapping(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[ScheduledInstancesEbs] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None


class ScheduledInstancesNetworkInterface(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[ScheduledInstancesIpv6Address]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddressConfigs: Optional[List[ScheduledInstancesPrivateIpAddressConfig]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None


# This class is the output for the 'search_transit_gateway_multicast_groups' function.
class SearchTransitGatewayMulticastGroupsResult(BaseValidatorModel):
    MulticastGroups: List[TransitGatewayMulticastGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SecurityGroupRuleUpdate(BaseValidatorModel):
    SecurityGroupRuleId: str
    SecurityGroupRule: Optional[SecurityGroupRuleRequest] = None


class ServiceDetail(BaseValidatorModel):
    ServiceName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceType: Optional[List[ServiceTypeDetail]] = None
    ServiceRegion: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    Owner: Optional[str] = None
    BaseEndpointDnsNames: Optional[List[str]] = None
    PrivateDnsName: Optional[str] = None
    PrivateDnsNames: Optional[List[PrivateDnsDetails]] = None
    VpcEndpointPolicySupported: Optional[bool] = None
    AcceptanceRequired: Optional[bool] = None
    ManagesVpcEndpoints: Optional[bool] = None
    PayerResponsibility: Optional[Literal['ServiceOwner']] = None
    Tags: Optional[List[Tag]] = None
    PrivateDnsNameVerificationState: Optional[DnsNameStateType] = None
    SupportedIpAddressTypes: Optional[List[ServiceConnectivityTypeType]] = None


class ServiceConfiguration(BaseValidatorModel):
    ServiceType: Optional[List[ServiceTypeDetail]] = None
    ServiceId: Optional[str] = None
    ServiceName: Optional[str] = None
    ServiceState: Optional[ServiceStateType] = None
    AvailabilityZones: Optional[List[str]] = None
    AcceptanceRequired: Optional[bool] = None
    ManagesVpcEndpoints: Optional[bool] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    SupportedIpAddressTypes: Optional[List[ServiceConnectivityTypeType]] = None
    BaseEndpointDnsNames: Optional[List[str]] = None
    PrivateDnsName: Optional[str] = None
    PrivateDnsNameConfiguration: Optional[PrivateDnsNameConfiguration] = None
    PayerResponsibility: Optional[Literal['ServiceOwner']] = None
    Tags: Optional[List[Tag]] = None
    SupportedRegions: Optional[List[SupportedRegionDetail]] = None
    RemoteAccessEnabled: Optional[bool] = None


class SnapshotDetail(BaseValidatorModel):
    Description: Optional[str] = None
    DeviceName: Optional[str] = None
    DiskImageSize: Optional[float] = None
    Format: Optional[str] = None
    Progress: Optional[str] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucketDetails] = None


class SnapshotTaskDetail(BaseValidatorModel):
    Description: Optional[str] = None
    DiskImageSize: Optional[float] = None
    Encrypted: Optional[bool] = None
    Format: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Progress: Optional[str] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucketDetails] = None


class SpotMaintenanceStrategies(BaseValidatorModel):
    CapacityRebalance: Optional[SpotCapacityRebalance] = None


class SpotDatafeedSubscription(BaseValidatorModel):
    Bucket: Optional[str] = None
    Fault: Optional[SpotInstanceStateFault] = None
    OwnerId: Optional[str] = None
    Prefix: Optional[str] = None
    State: Optional[DatafeedSubscriptionStateType] = None


class TransitGatewayMulticastDomainAssociation(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    Subnet: Optional[SubnetAssociation] = None


class TransitGatewayMulticastDomainAssociations(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    Subnets: Optional[List[SubnetAssociation]] = None


class SubnetIpv6CidrBlockAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv6CidrBlockState: Optional[SubnetCidrBlockState] = None
    Ipv6AddressAttribute: Optional[Ipv6AddressAttributeType] = None
    IpSource: Optional[IpSourceType] = None


class VpcEndpoint(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointType: Optional[VpcEndpointTypeType] = None
    VpcId: Optional[str] = None
    ServiceName: Optional[str] = None
    State: Optional[StateType] = None
    PolicyDocument: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    Groups: Optional[List[SecurityGroupIdentifier]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DnsOptions: Optional[DnsOptions] = None
    PrivateDnsEnabled: Optional[bool] = None
    RequesterManaged: Optional[bool] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DnsEntries: Optional[List[DnsEntry]] = None
    CreationTimestamp: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    OwnerId: Optional[str] = None
    LastError: Optional[LastError] = None
    Ipv4Prefixes: Optional[List[SubnetIpPrefixes]] = None
    Ipv6Prefixes: Optional[List[SubnetIpPrefixes]] = None
    FailureReason: Optional[str] = None
    ServiceNetworkArn: Optional[str] = None
    ResourceConfigurationArn: Optional[str] = None
    ServiceRegion: Optional[str] = None


class TargetReservationValue(BaseValidatorModel):
    ReservationValue: Optional[ReservationValue] = None
    TargetConfiguration: Optional[TargetConfiguration] = None


class TargetGroupsConfigOutput(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroup]] = None


class TargetGroupsConfig(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroup]] = None


class TrafficMirrorFilterRule(BaseValidatorModel):
    TrafficMirrorFilterRuleId: Optional[str] = None
    TrafficMirrorFilterId: Optional[str] = None
    TrafficDirection: Optional[TrafficDirectionType] = None
    RuleNumber: Optional[int] = None
    RuleAction: Optional[TrafficMirrorRuleActionType] = None
    Protocol: Optional[int] = None
    DestinationPortRange: Optional[TrafficMirrorPortRange] = None
    SourcePortRange: Optional[TrafficMirrorPortRange] = None
    DestinationCidrBlock: Optional[str] = None
    SourceCidrBlock: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class TransitGatewayAttachment(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    TransitGatewayOwnerId: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    Association: Optional[TransitGatewayAttachmentAssociation] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class TransitGatewayConnectPeerConfiguration(BaseValidatorModel):
    TransitGatewayAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    Protocol: Optional[Literal['gre']] = None
    BgpConfigurations: Optional[List[TransitGatewayAttachmentBgpConfiguration]] = None


class TransitGatewayConnect(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransportTransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayConnectOptions] = None
    Tags: Optional[List[Tag]] = None


class TransitGatewayMulticastDomain(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    TransitGatewayMulticastDomainArn: Optional[str] = None
    OwnerId: Optional[str] = None
    Options: Optional[TransitGatewayMulticastDomainOptions] = None
    State: Optional[TransitGatewayMulticastDomainStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class TransitGateway(BaseValidatorModel):
    TransitGatewayId: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    State: Optional[TransitGatewayStateType] = None
    OwnerId: Optional[str] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayOptions] = None
    Tags: Optional[List[Tag]] = None


class TransitGatewayPeeringAttachment(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    AccepterTransitGatewayAttachmentId: Optional[str] = None
    RequesterTgwInfo: Optional[PeeringTgwInfo] = None
    AccepterTgwInfo: Optional[PeeringTgwInfo] = None
    Options: Optional[TransitGatewayPeeringAttachmentOptions] = None
    Status: Optional[PeeringAttachmentStatus] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None


class TransitGatewayPolicyRule(BaseValidatorModel):
    SourceCidrBlock: Optional[str] = None
    SourcePortRange: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPortRange: Optional[str] = None
    Protocol: Optional[str] = None
    MetaData: Optional[TransitGatewayPolicyRuleMetaData] = None


class TransitGatewayPrefixListReference(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    PrefixListId: Optional[str] = None
    PrefixListOwnerId: Optional[str] = None
    State: Optional[TransitGatewayPrefixListReferenceStateType] = None
    Blackhole: Optional[bool] = None
    TransitGatewayAttachment: Optional[TransitGatewayPrefixListAttachment] = None


class TransitGatewayRoute(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    PrefixListId: Optional[str] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None
    TransitGatewayAttachments: Optional[List[TransitGatewayRouteAttachment]] = None
    Type: Optional[TransitGatewayRouteTypeType] = None
    State: Optional[TransitGatewayRouteStateType] = None


class TransitGatewayVpcAttachment(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcOwnerId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    SubnetIds: Optional[List[str]] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayVpcAttachmentOptions] = None
    Tags: Optional[List[Tag]] = None


class UnsuccessfulInstanceCreditSpecificationItem(BaseValidatorModel):
    InstanceId: Optional[str] = None
    Error: Optional[UnsuccessfulInstanceCreditSpecificationItemError] = None


class UnsuccessfulItem(BaseValidatorModel):
    Error: Optional[UnsuccessfulItemError] = None
    ResourceId: Optional[str] = None


class ValidationWarning(BaseValidatorModel):
    Errors: Optional[List[ValidationError]] = None


class VerifiedAccessEndpointCidrOptions(BaseValidatorModel):
    Cidr: Optional[str] = None
    PortRanges: Optional[List[VerifiedAccessEndpointPortRange]] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    SubnetIds: Optional[List[str]] = None


class VerifiedAccessEndpointEniOptions(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    PortRanges: Optional[List[VerifiedAccessEndpointPortRange]] = None


class VerifiedAccessEndpointLoadBalancerOptions(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    LoadBalancerArn: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    PortRanges: Optional[List[VerifiedAccessEndpointPortRange]] = None


class VerifiedAccessInstanceOpenVpnClientConfiguration(BaseValidatorModel):
    Config: Optional[str] = None
    Routes: Optional[List[VerifiedAccessInstanceOpenVpnClientConfigurationRoute]] = None


class VerifiedAccessInstance(BaseValidatorModel):
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    VerifiedAccessTrustProviders: Optional[List[VerifiedAccessTrustProviderCondensed]] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    FipsEnabled: Optional[bool] = None
    CidrEndpointsCustomSubDomain: Optional[VerifiedAccessInstanceCustomSubDomain] = None


class VerifiedAccessLogCloudWatchLogsDestination(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatus] = None
    LogGroup: Optional[str] = None


class VerifiedAccessLogKinesisDataFirehoseDestination(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatus] = None
    DeliveryStream: Optional[str] = None


class VerifiedAccessLogS3Destination(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatus] = None
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None


class VerifiedAccessLogOptions(BaseValidatorModel):
    S3: Optional[VerifiedAccessLogS3DestinationOptions] = None
    CloudWatchLogs: Optional[VerifiedAccessLogCloudWatchLogsDestinationOptions] = None
    KinesisDataFirehose: Optional[VerifiedAccessLogKinesisDataFirehoseDestinationOptions] = None
    LogVersion: Optional[str] = None
    IncludeTrustContext: Optional[bool] = None


# This class is the output for the 'create_volume' function.
class VolumeResponse(BaseValidatorModel):
    OutpostArn: str
    Iops: int
    Tags: List[Tag]
    VolumeType: VolumeTypeType
    FastRestored: bool
    MultiAttachEnabled: bool
    Throughput: int
    SseType: SSETypeType
    Operator: OperatorResponse
    VolumeId: str
    Size: int
    SnapshotId: str
    AvailabilityZone: str
    State: VolumeStateType
    CreateTime: datetime
    Attachments: List[VolumeAttachment]
    Encrypted: bool
    KmsKeyId: str
    ResponseMetadata: ResponseMetadata


class Volume(BaseValidatorModel):
    OutpostArn: Optional[str] = None
    Iops: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    VolumeType: Optional[VolumeTypeType] = None
    FastRestored: Optional[bool] = None
    MultiAttachEnabled: Optional[bool] = None
    Throughput: Optional[int] = None
    SseType: Optional[SSETypeType] = None
    Operator: Optional[OperatorResponse] = None
    VolumeId: Optional[str] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    State: Optional[VolumeStateType] = None
    CreateTime: Optional[datetime] = None
    Attachments: Optional[List[VolumeAttachment]] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None


class VolumeStatusInfo(BaseValidatorModel):
    Details: Optional[List[VolumeStatusDetails]] = None
    Status: Optional[VolumeStatusInfoStatusType] = None


class VpcCidrBlockAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    CidrBlock: Optional[str] = None
    CidrBlockState: Optional[VpcCidrBlockState] = None


class VpcIpv6CidrBlockAssociation(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv6CidrBlockState: Optional[VpcCidrBlockState] = None
    NetworkBorderGroup: Optional[str] = None
    Ipv6Pool: Optional[str] = None
    Ipv6AddressAttribute: Optional[Ipv6AddressAttributeType] = None
    IpSource: Optional[IpSourceType] = None


class VpcEncryptionControlExclusions(BaseValidatorModel):
    InternetGateway: Optional[VpcEncryptionControlExclusion] = None
    EgressOnlyInternetGateway: Optional[VpcEncryptionControlExclusion] = None
    NatGateway: Optional[VpcEncryptionControlExclusion] = None
    VirtualPrivateGateway: Optional[VpcEncryptionControlExclusion] = None
    VpcPeering: Optional[VpcEncryptionControlExclusion] = None


class VpcPeeringConnectionVpcInfo(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Ipv6CidrBlockSet: Optional[List[Ipv6CidrBlock]] = None
    CidrBlockSet: Optional[List[CidrBlock]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcPeeringConnectionOptionsDescription] = None
    VpcId: Optional[str] = None
    Region: Optional[str] = None


# This class is the output for the 'describe_account_attributes' function.
class DescribeAccountAttributesResult(BaseValidatorModel):
    AccountAttributes: List[AccountAttribute]
    ResponseMetadata: ResponseMetadata


class AdditionalDetail(BaseValidatorModel):
    AdditionalDetailType: Optional[str] = None
    Component: Optional[AnalysisComponent] = None
    VpcEndpointService: Optional[AnalysisComponent] = None
    RuleOptions: Optional[List[RuleOption]] = None
    RuleGroupTypePairs: Optional[List[RuleGroupTypePair]] = None
    RuleGroupRuleOptionsPairs: Optional[List[RuleGroupRuleOptionsPair]] = None
    ServiceName: Optional[str] = None
    LoadBalancers: Optional[List[AnalysisComponent]] = None


# This class is the output for the 'describe_addresses_attribute' function.
class DescribeAddressesAttributeResult(BaseValidatorModel):
    Addresses: List[AddressAttribute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_address_attribute' function.
class ModifyAddressAttributeResult(BaseValidatorModel):
    Address: AddressAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_address_attribute' function.
class ResetAddressAttributeResult(BaseValidatorModel):
    Address: AddressAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_addresses' function.
class DescribeAddressesResult(BaseValidatorModel):
    Addresses: List[Address]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_endpoint_service_permissions' function.
class DescribeVpcEndpointServicePermissionsResult(BaseValidatorModel):
    AllowedPrincipals: List[AllowedPrincipal]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_carrier_gateway' function.
class CreateCarrierGatewayResult(BaseValidatorModel):
    CarrierGateway: CarrierGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_carrier_gateway' function.
class DeleteCarrierGatewayResult(BaseValidatorModel):
    CarrierGateway: CarrierGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_carrier_gateways' function.
class DescribeCarrierGatewaysResult(BaseValidatorModel):
    CarrierGateways: List[CarrierGateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_coip_pool' function.
class CreateCoipPoolResult(BaseValidatorModel):
    CoipPool: CoipPool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_coip_pool' function.
class DeleteCoipPoolResult(BaseValidatorModel):
    CoipPool: CoipPool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_coip_pools' function.
class DescribeCoipPoolsResult(BaseValidatorModel):
    CoipPools: List[CoipPool]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_customer_gateway' function.
class CreateCustomerGatewayResult(BaseValidatorModel):
    CustomerGateway: CustomerGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_customer_gateways' function.
class DescribeCustomerGatewaysResult(BaseValidatorModel):
    CustomerGateways: List[CustomerGateway]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_declarative_policies_reports' function.
class DescribeDeclarativePoliciesReportsResult(BaseValidatorModel):
    Reports: List[DeclarativePoliciesReport]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_instance_connect_endpoint' function.
class CreateInstanceConnectEndpointResult(BaseValidatorModel):
    InstanceConnectEndpoint: Ec2InstanceConnectEndpoint
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_instance_connect_endpoint' function.
class DeleteInstanceConnectEndpointResult(BaseValidatorModel):
    InstanceConnectEndpoint: Ec2InstanceConnectEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_instance_connect_endpoints' function.
class DescribeInstanceConnectEndpointsResult(BaseValidatorModel):
    InstanceConnectEndpoints: List[Ec2InstanceConnectEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_host_reservations' function.
class DescribeHostReservationsResult(BaseValidatorModel):
    HostReservationSet: List[HostReservation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'associate_instance_event_window' function.
class AssociateInstanceEventWindowRequest(BaseValidatorModel):
    InstanceEventWindowId: str
    AssociationTarget: InstanceEventWindowAssociationRequest
    DryRun: Optional[bool] = None


class InstanceEventWindow(BaseValidatorModel):
    InstanceEventWindowId: Optional[str] = None
    TimeRanges: Optional[List[InstanceEventWindowTimeRange]] = None
    Name: Optional[str] = None
    CronExpression: Optional[str] = None
    AssociationTarget: Optional[InstanceEventWindowAssociationTarget] = None
    State: Optional[InstanceEventWindowStateType] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'disassociate_instance_event_window' function.
class DisassociateInstanceEventWindowRequest(BaseValidatorModel):
    InstanceEventWindowId: str
    AssociationTarget: InstanceEventWindowDisassociationRequest
    DryRun: Optional[bool] = None


# This class is the output for the 'create_ipam_external_resource_verification_token' function.
class CreateIpamExternalResourceVerificationTokenResult(BaseValidatorModel):
    IpamExternalResourceVerificationToken: IpamExternalResourceVerificationToken
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ipam_external_resource_verification_token' function.
class DeleteIpamExternalResourceVerificationTokenResult(BaseValidatorModel):
    IpamExternalResourceVerificationToken: IpamExternalResourceVerificationToken
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ipam_external_resource_verification_tokens' function.
class DescribeIpamExternalResourceVerificationTokensResult(BaseValidatorModel):
    IpamExternalResourceVerificationTokens: List[IpamExternalResourceVerificationToken]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_ipam_resource_discovery' function.
class AssociateIpamResourceDiscoveryResult(BaseValidatorModel):
    IpamResourceDiscoveryAssociation: IpamResourceDiscoveryAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ipam_resource_discovery_associations' function.
class DescribeIpamResourceDiscoveryAssociationsResult(BaseValidatorModel):
    IpamResourceDiscoveryAssociations: List[IpamResourceDiscoveryAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'disassociate_ipam_resource_discovery' function.
class DisassociateIpamResourceDiscoveryResult(BaseValidatorModel):
    IpamResourceDiscoveryAssociation: IpamResourceDiscoveryAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ipam_scope' function.
class CreateIpamScopeResult(BaseValidatorModel):
    IpamScope: IpamScope
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ipam_scope' function.
class DeleteIpamScopeResult(BaseValidatorModel):
    IpamScope: IpamScope
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ipam_scopes' function.
class DescribeIpamScopesResult(BaseValidatorModel):
    IpamScopes: List[IpamScope]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_ipam_scope' function.
class ModifyIpamScopeResult(BaseValidatorModel):
    IpamScope: IpamScope
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_key_pairs' function.
class DescribeKeyPairsResult(BaseValidatorModel):
    KeyPairs: List[KeyPairInfo]
    ResponseMetadata: ResponseMetadata


class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociation: LocalGatewayRouteTableVirtualInterfaceGroupAssociation
    ResponseMetadata: ResponseMetadata


class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociation: LocalGatewayRouteTableVirtualInterfaceGroupAssociation
    ResponseMetadata: ResponseMetadata


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociations: List[LocalGatewayRouteTableVirtualInterfaceGroupAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_local_gateway_route_table_vpc_association' function.
class CreateLocalGatewayRouteTableVpcAssociationResult(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociation: LocalGatewayRouteTableVpcAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_local_gateway_route_table_vpc_association' function.
class DeleteLocalGatewayRouteTableVpcAssociationResult(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociation: LocalGatewayRouteTableVpcAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_local_gateway_route_table_vpc_associations' function.
class DescribeLocalGatewayRouteTableVpcAssociationsResult(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociations: List[LocalGatewayRouteTableVpcAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_local_gateways' function.
class DescribeLocalGatewaysResult(BaseValidatorModel):
    LocalGateways: List[LocalGateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_local_gateway_virtual_interface_groups' function.
class DescribeLocalGatewayVirtualInterfaceGroupsResult(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroups: List[LocalGatewayVirtualInterfaceGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_local_gateway_virtual_interfaces' function.
class DescribeLocalGatewayVirtualInterfacesResult(BaseValidatorModel):
    LocalGatewayVirtualInterfaces: List[LocalGatewayVirtualInterface]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_managed_prefix_list' function.
class CreateManagedPrefixListResult(BaseValidatorModel):
    PrefixList: ManagedPrefixList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_managed_prefix_list' function.
class DeleteManagedPrefixListResult(BaseValidatorModel):
    PrefixList: ManagedPrefixList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_managed_prefix_lists' function.
class DescribeManagedPrefixListsResult(BaseValidatorModel):
    PrefixLists: List[ManagedPrefixList]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_managed_prefix_list' function.
class ModifyManagedPrefixListResult(BaseValidatorModel):
    PrefixList: ManagedPrefixList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_managed_prefix_list_version' function.
class RestoreManagedPrefixListVersionResult(BaseValidatorModel):
    PrefixList: ManagedPrefixList
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_network_insights_access_scope_analyses' function.
class DescribeNetworkInsightsAccessScopeAnalysesResult(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalyses: List[NetworkInsightsAccessScopeAnalysis]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_network_insights_access_scope_analysis' function.
class StartNetworkInsightsAccessScopeAnalysisResult(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysis: NetworkInsightsAccessScopeAnalysis
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_network_insights_access_scopes' function.
class DescribeNetworkInsightsAccessScopesResult(BaseValidatorModel):
    NetworkInsightsAccessScopes: List[NetworkInsightsAccessScope]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_placement_group' function.
class CreatePlacementGroupResult(BaseValidatorModel):
    PlacementGroup: PlacementGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_placement_groups' function.
class DescribePlacementGroupsResult(BaseValidatorModel):
    PlacementGroups: List[PlacementGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_replace_root_volume_task' function.
class CreateReplaceRootVolumeTaskResult(BaseValidatorModel):
    ReplaceRootVolumeTask: ReplaceRootVolumeTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_replace_root_volume_tasks' function.
class DescribeReplaceRootVolumeTasksResult(BaseValidatorModel):
    ReplaceRootVolumeTasks: List[ReplaceRootVolumeTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_security_groups_for_vpc' function.
class GetSecurityGroupsForVpcResult(BaseValidatorModel):
    SecurityGroupForVpcs: List[SecurityGroupForVpc]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_snapshots' function.
class CreateSnapshotsResult(BaseValidatorModel):
    Snapshots: List[SnapshotInfo]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snapshot_tier_status' function.
class DescribeSnapshotTierStatusResult(BaseValidatorModel):
    SnapshotTierStatuses: List[SnapshotTierStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_snapshots' function.
class DescribeSnapshotsResult(BaseValidatorModel):
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_subnet_cidr_reservation' function.
class CreateSubnetCidrReservationResult(BaseValidatorModel):
    SubnetCidrReservation: SubnetCidrReservation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_subnet_cidr_reservation' function.
class DeleteSubnetCidrReservationResult(BaseValidatorModel):
    DeletedSubnetCidrReservation: SubnetCidrReservation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_subnet_cidr_reservations' function.
class GetSubnetCidrReservationsResult(BaseValidatorModel):
    SubnetIpv4CidrReservations: List[SubnetCidrReservation]
    SubnetIpv6CidrReservations: List[SubnetCidrReservation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

TagSpecificationUnion = Union[TagSpecification, TagSpecificationOutput]


# This class is the output for the 'create_traffic_mirror_session' function.
class CreateTrafficMirrorSessionResult(BaseValidatorModel):
    TrafficMirrorSession: TrafficMirrorSession
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_traffic_mirror_sessions' function.
class DescribeTrafficMirrorSessionsResult(BaseValidatorModel):
    TrafficMirrorSessions: List[TrafficMirrorSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_traffic_mirror_session' function.
class ModifyTrafficMirrorSessionResult(BaseValidatorModel):
    TrafficMirrorSession: TrafficMirrorSession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_traffic_mirror_target' function.
class CreateTrafficMirrorTargetResult(BaseValidatorModel):
    TrafficMirrorTarget: TrafficMirrorTarget
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_traffic_mirror_targets' function.
class DescribeTrafficMirrorTargetsResult(BaseValidatorModel):
    TrafficMirrorTargets: List[TrafficMirrorTarget]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_transit_gateway_policy_table' function.
class CreateTransitGatewayPolicyTableResult(BaseValidatorModel):
    TransitGatewayPolicyTable: TransitGatewayPolicyTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_policy_table' function.
class DeleteTransitGatewayPolicyTableResult(BaseValidatorModel):
    TransitGatewayPolicyTable: TransitGatewayPolicyTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_policy_tables' function.
class DescribeTransitGatewayPolicyTablesResult(BaseValidatorModel):
    TransitGatewayPolicyTables: List[TransitGatewayPolicyTable]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_transit_gateway_route_table_announcement' function.
class CreateTransitGatewayRouteTableAnnouncementResult(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncement: TransitGatewayRouteTableAnnouncement
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_route_table_announcement' function.
class DeleteTransitGatewayRouteTableAnnouncementResult(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncement: TransitGatewayRouteTableAnnouncement
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_route_table_announcements' function.
class DescribeTransitGatewayRouteTableAnnouncementsResult(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncements: List[TransitGatewayRouteTableAnnouncement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_transit_gateway_route_table' function.
class CreateTransitGatewayRouteTableResult(BaseValidatorModel):
    TransitGatewayRouteTable: TransitGatewayRouteTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_route_table' function.
class DeleteTransitGatewayRouteTableResult(BaseValidatorModel):
    TransitGatewayRouteTable: TransitGatewayRouteTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_route_tables' function.
class DescribeTransitGatewayRouteTablesResult(BaseValidatorModel):
    TransitGatewayRouteTables: List[TransitGatewayRouteTable]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'associate_trunk_interface' function.
class AssociateTrunkInterfaceResult(BaseValidatorModel):
    InterfaceAssociation: TrunkInterfaceAssociation
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_trunk_interface_associations' function.
class DescribeTrunkInterfaceAssociationsResult(BaseValidatorModel):
    InterfaceAssociations: List[TrunkInterfaceAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_vpc_block_public_access_exclusion' function.
class CreateVpcBlockPublicAccessExclusionResult(BaseValidatorModel):
    VpcBlockPublicAccessExclusion: VpcBlockPublicAccessExclusion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_block_public_access_exclusion' function.
class DeleteVpcBlockPublicAccessExclusionResult(BaseValidatorModel):
    VpcBlockPublicAccessExclusion: VpcBlockPublicAccessExclusion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_block_public_access_exclusions' function.
class DescribeVpcBlockPublicAccessExclusionsResult(BaseValidatorModel):
    VpcBlockPublicAccessExclusions: List[VpcBlockPublicAccessExclusion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_vpc_block_public_access_exclusion' function.
class ModifyVpcBlockPublicAccessExclusionResult(BaseValidatorModel):
    VpcBlockPublicAccessExclusion: VpcBlockPublicAccessExclusion
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_classic_link' function.
class DescribeVpcClassicLinkResult(BaseValidatorModel):
    Vpcs: List[VpcClassicLink]
    ResponseMetadata: ResponseMetadata


class Explanation(BaseValidatorModel):
    Acl: Optional[AnalysisComponent] = None
    AclRule: Optional[AnalysisAclRule] = None
    Address: Optional[str] = None
    Addresses: Optional[List[str]] = None
    AttachedTo: Optional[AnalysisComponent] = None
    AvailabilityZones: Optional[List[str]] = None
    Cidrs: Optional[List[str]] = None
    Component: Optional[AnalysisComponent] = None
    CustomerGateway: Optional[AnalysisComponent] = None
    Destination: Optional[AnalysisComponent] = None
    DestinationVpc: Optional[AnalysisComponent] = None
    Direction: Optional[str] = None
    ExplanationCode: Optional[str] = None
    IngressRouteTable: Optional[AnalysisComponent] = None
    InternetGateway: Optional[AnalysisComponent] = None
    LoadBalancerArn: Optional[str] = None
    ClassicLoadBalancerListener: Optional[AnalysisLoadBalancerListener] = None
    LoadBalancerListenerPort: Optional[int] = None
    LoadBalancerTarget: Optional[AnalysisLoadBalancerTarget] = None
    LoadBalancerTargetGroup: Optional[AnalysisComponent] = None
    LoadBalancerTargetGroups: Optional[List[AnalysisComponent]] = None
    LoadBalancerTargetPort: Optional[int] = None
    ElasticLoadBalancerListener: Optional[AnalysisComponent] = None
    MissingComponent: Optional[str] = None
    NatGateway: Optional[AnalysisComponent] = None
    NetworkInterface: Optional[AnalysisComponent] = None
    PacketField: Optional[str] = None
    VpcPeeringConnection: Optional[AnalysisComponent] = None
    Port: Optional[int] = None
    PortRanges: Optional[List[PortRange]] = None
    PrefixList: Optional[AnalysisComponent] = None
    Protocols: Optional[List[str]] = None
    RouteTableRoute: Optional[AnalysisRouteTableRoute] = None
    RouteTable: Optional[AnalysisComponent] = None
    SecurityGroup: Optional[AnalysisComponent] = None
    SecurityGroupRule: Optional[AnalysisSecurityGroupRule] = None
    SecurityGroups: Optional[List[AnalysisComponent]] = None
    SourceVpc: Optional[AnalysisComponent] = None
    State: Optional[str] = None
    Subnet: Optional[AnalysisComponent] = None
    SubnetRouteTable: Optional[AnalysisComponent] = None
    Vpc: Optional[AnalysisComponent] = None
    VpcEndpoint: Optional[AnalysisComponent] = None
    VpnConnection: Optional[AnalysisComponent] = None
    VpnGateway: Optional[AnalysisComponent] = None
    TransitGateway: Optional[AnalysisComponent] = None
    TransitGatewayRouteTable: Optional[AnalysisComponent] = None
    TransitGatewayRouteTableRoute: Optional[TransitGatewayRouteTableRoute] = None
    TransitGatewayAttachment: Optional[AnalysisComponent] = None
    ComponentAccount: Optional[str] = None
    ComponentRegion: Optional[str] = None
    FirewallStatelessRule: Optional[FirewallStatelessRule] = None
    FirewallStatefulRule: Optional[FirewallStatefulRule] = None


# This class is the output for the 'advertise_byoip_cidr' function.
class AdvertiseByoipCidrResult(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deprovision_byoip_cidr' function.
class DeprovisionByoipCidrResult(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_byoip_cidrs' function.
class DescribeByoipCidrsResult(BaseValidatorModel):
    ByoipCidrs: List[ByoipCidr]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'move_byoip_cidr_to_ipam' function.
class MoveByoipCidrToIpamResult(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'provision_byoip_cidr' function.
class ProvisionByoipCidrResult(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'withdraw_byoip_cidr' function.
class WithdrawByoipCidrResult(BaseValidatorModel):
    ByoipCidr: ByoipCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_client_vpn_target_networks' function.
class DescribeClientVpnTargetNetworksResult(BaseValidatorModel):
    ClientVpnTargetNetworks: List[TargetNetwork]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RouteTable(BaseValidatorModel):
    Associations: Optional[List[RouteTableAssociation]] = None
    PropagatingVgws: Optional[List[PropagatingVgw]] = None
    RouteTableId: Optional[str] = None
    Routes: Optional[List[Route]] = None
    Tags: Optional[List[Tag]] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None


class IntegrateServices(BaseValidatorModel):
    AthenaIntegrations: Optional[List[AthenaIntegration]] = None


class LaunchTemplateInstanceMarketOptionsRequest(BaseValidatorModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[LaunchTemplateSpotMarketOptionsRequest] = None


class DescribeScheduledInstanceAvailabilityRequestPaginate(BaseValidatorModel):
    FirstSlotStartTimeRange: SlotDateTimeRangeRequest
    Recurrence: ScheduledInstanceRecurrenceRequest
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxSlotDurationInHours: Optional[int] = None
    MinSlotDurationInHours: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_scheduled_instance_availability' function.
class DescribeScheduledInstanceAvailabilityRequest(BaseValidatorModel):
    FirstSlotStartTimeRange: SlotDateTimeRangeRequest
    Recurrence: ScheduledInstanceRecurrenceRequest
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    MaxSlotDurationInHours: Optional[int] = None
    MinSlotDurationInHours: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeScheduledInstancesRequestPaginate(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    ScheduledInstanceIds: Optional[List[str]] = None
    SlotStartTimeRange: Optional[SlotStartTimeRangeRequest] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_scheduled_instances' function.
class DescribeScheduledInstancesRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ScheduledInstanceIds: Optional[List[str]] = None
    SlotStartTimeRange: Optional[SlotStartTimeRangeRequest] = None


class InstanceMarketOptionsRequest(BaseValidatorModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[SpotMarketOptions] = None


# This class is the output for the 'create_vpn_gateway' function.
class CreateVpnGatewayResult(BaseValidatorModel):
    VpnGateway: VpnGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpn_gateways' function.
class DescribeVpnGatewaysResult(BaseValidatorModel):
    VpnGateways: List[VpnGateway]
    ResponseMetadata: ResponseMetadata


class NetworkInterfaceAttachment(BaseValidatorModel):
    AttachTime: Optional[datetime] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    NetworkCardIndex: Optional[int] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    Status: Optional[AttachmentStatusType] = None
    EnaSrdSpecification: Optional[AttachmentEnaSrdSpecification] = None


# This class is the output for the 'get_declarative_policies_report_summary' function.
class GetDeclarativePoliciesReportSummaryResult(BaseValidatorModel):
    ReportId: str
    S3Bucket: str
    S3Prefix: str
    TargetId: str
    StartTime: datetime
    EndTime: datetime
    NumberOfAccounts: int
    NumberOfFailedAccounts: int
    AttributeSummaries: List[AttributeSummary]
    ResponseMetadata: ResponseMetadata


class DhcpOptions(BaseValidatorModel):
    OwnerId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DhcpOptionsId: Optional[str] = None
    DhcpConfigurations: Optional[List[DhcpConfiguration]] = None


# This class is the output for the 'describe_client_vpn_authorization_rules' function.
class DescribeClientVpnAuthorizationRulesResult(BaseValidatorModel):
    AuthorizationRules: List[AuthorizationRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_availability_zones' function.
class DescribeAvailabilityZonesResult(BaseValidatorModel):
    AvailabilityZones: List[AvailabilityZone]
    ResponseMetadata: ResponseMetadata


class Host(BaseValidatorModel):
    AutoPlacement: Optional[AutoPlacementType] = None
    AvailabilityZone: Optional[str] = None
    AvailableCapacity: Optional[AvailableCapacity] = None
    ClientToken: Optional[str] = None
    HostId: Optional[str] = None
    HostProperties: Optional[HostProperties] = None
    HostReservationId: Optional[str] = None
    Instances: Optional[List[HostInstance]] = None
    State: Optional[AllocationStateType] = None
    AllocationTime: Optional[datetime] = None
    ReleaseTime: Optional[datetime] = None
    Tags: Optional[List[Tag]] = None
    HostRecovery: Optional[HostRecoveryType] = None
    AllowsMultipleInstanceTypes: Optional[AllowsMultipleInstanceTypesType] = None
    OwnerId: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    MemberOfServiceLinkedResourceGroup: Optional[bool] = None
    OutpostArn: Optional[str] = None
    HostMaintenance: Optional[HostMaintenanceType] = None
    AssetId: Optional[str] = None


class Storage(BaseValidatorModel):
    S3: Optional[S3Storage] = None


# This class is the output for the 'describe_image_attribute' function.
class ImageAttribute(BaseValidatorModel):
    Description: AttributeValue
    KernelId: AttributeValue
    RamdiskId: AttributeValue
    SriovNetSupport: AttributeValue
    BootMode: AttributeValue
    TpmSupport: AttributeValue
    UefiData: AttributeValue
    LastLaunchedTime: AttributeValue
    ImdsSupport: AttributeValue
    DeregistrationProtection: AttributeValue
    ImageId: str
    LaunchPermissions: List[LaunchPermission]
    ProductCodes: List[ProductCode]
    BlockDeviceMappings: List[BlockDeviceMapping]
    ResponseMetadata: ResponseMetadata


class Image(BaseValidatorModel):
    PlatformDetails: Optional[str] = None
    UsageOperation: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    Description: Optional[str] = None
    EnaSupport: Optional[bool] = None
    Hypervisor: Optional[HypervisorTypeType] = None
    ImageOwnerAlias: Optional[str] = None
    Name: Optional[str] = None
    RootDeviceName: Optional[str] = None
    RootDeviceType: Optional[DeviceTypeType] = None
    SriovNetSupport: Optional[str] = None
    StateReason: Optional[StateReason] = None
    Tags: Optional[List[Tag]] = None
    VirtualizationType: Optional[VirtualizationTypeType] = None
    BootMode: Optional[BootModeValuesType] = None
    TpmSupport: Optional[Literal['v2.0']] = None
    DeprecationTime: Optional[str] = None
    ImdsSupport: Optional[Literal['v2.0']] = None
    SourceInstanceId: Optional[str] = None
    DeregistrationProtection: Optional[str] = None
    LastLaunchedTime: Optional[str] = None
    ImageAllowed: Optional[bool] = None
    SourceImageId: Optional[str] = None
    SourceImageRegion: Optional[str] = None
    ImageId: Optional[str] = None
    ImageLocation: Optional[str] = None
    State: Optional[ImageStateType] = None
    OwnerId: Optional[str] = None
    CreationDate: Optional[str] = None
    Public: Optional[bool] = None
    ProductCodes: Optional[List[ProductCode]] = None
    Architecture: Optional[ArchitectureValuesType] = None
    ImageType: Optional[ImageTypeValuesType] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    Platform: Optional[Literal['windows']] = None


# This class is the output for the 'cancel_capacity_reservation_fleets' function.
class CancelCapacityReservationFleetsResult(BaseValidatorModel):
    SuccessfulFleetCancellations: List[CapacityReservationFleetCancellationState]
    FailedFleetCancellations: List[FailedCapacityReservationFleetCancellationResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_spot_fleet_requests' function.
class CancelSpotFleetRequestsResponse(BaseValidatorModel):
    SuccessfulFleetRequests: List[CancelSpotFleetRequestsSuccessItem]
    UnsuccessfulFleetRequests: List[CancelSpotFleetRequestsErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_capacity_reservation_billing_requests' function.
class DescribeCapacityReservationBillingRequestsResult(BaseValidatorModel):
    CapacityReservationBillingRequests: List[CapacityReservationBillingRequest]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_capacity_reservation_by_splitting' function.
class CreateCapacityReservationBySplittingResult(BaseValidatorModel):
    SourceCapacityReservation: CapacityReservation
    DestinationCapacityReservation: CapacityReservation
    InstanceCount: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_capacity_reservation' function.
class CreateCapacityReservationResult(BaseValidatorModel):
    CapacityReservation: CapacityReservation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_capacity_reservations' function.
class DescribeCapacityReservationsResult(BaseValidatorModel):
    CapacityReservations: List[CapacityReservation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'move_capacity_reservation_instances' function.
class MoveCapacityReservationInstancesResult(BaseValidatorModel):
    SourceCapacityReservation: CapacityReservation
    DestinationCapacityReservation: CapacityReservation
    InstanceCount: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'purchase_capacity_block' function.
class PurchaseCapacityBlockResult(BaseValidatorModel):
    CapacityReservation: CapacityReservation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_capacity_reservation_fleets' function.
class DescribeCapacityReservationFleetsResult(BaseValidatorModel):
    CapacityReservationFleets: List[CapacityReservationFleet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'modify_instance_capacity_reservation_attributes' function.
class ModifyInstanceCapacityReservationAttributesRequest(BaseValidatorModel):
    InstanceId: str
    CapacityReservationSpecification: CapacityReservationSpecification
    DryRun: Optional[bool] = None


# This class is the output for the 'describe_classic_link_instances' function.
class DescribeClassicLinkInstancesResult(BaseValidatorModel):
    Instances: List[ClassicLinkInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClientVpnEndpoint(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ClientVpnEndpointStatus] = None
    CreationTime: Optional[str] = None
    DeletionTime: Optional[str] = None
    DnsName: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServers: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    VpnProtocol: Optional[Literal['openvpn']] = None
    TransportProtocol: Optional[TransportProtocolType] = None
    VpnPort: Optional[int] = None
    AssociatedTargetNetworks: Optional[List[AssociatedTargetNetwork]] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[List[ClientVpnAuthentication]] = None
    ConnectionLogOptions: Optional[ConnectionLogResponseOptions] = None
    Tags: Optional[List[Tag]] = None
    SecurityGroupIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[ClientConnectResponseOptions] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ClientLoginBannerResponseOptions] = None
    DisconnectOnSessionTimeout: Optional[bool] = None


# This class is the output for the 'describe_client_vpn_connections' function.
class DescribeClientVpnConnectionsResult(BaseValidatorModel):
    Connections: List[ClientVpnConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'terminate_client_vpn_connections' function.
class TerminateClientVpnConnectionsResult(BaseValidatorModel):
    ClientVpnEndpointId: str
    Username: str
    ConnectionStatuses: List[TerminateConnectionStatus]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_client_vpn_routes' function.
class DescribeClientVpnRoutesResult(BaseValidatorModel):
    Routes: List[ClientVpnRoute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyVpnTunnelOptionsSpecification(BaseValidatorModel):
    TunnelInsideCidr: Optional[str] = None
    TunnelInsideIpv6Cidr: Optional[str] = None
    PreSharedKey: Optional[str] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2LifetimeSeconds: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    RekeyFuzzPercentage: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    DPDTimeoutSeconds: Optional[int] = None
    DPDTimeoutAction: Optional[str] = None
    Phase1EncryptionAlgorithms: Optional[List[Phase1EncryptionAlgorithmsRequestListValue]] = None
    Phase2EncryptionAlgorithms: Optional[List[Phase2EncryptionAlgorithmsRequestListValue]] = None
    Phase1IntegrityAlgorithms: Optional[List[Phase1IntegrityAlgorithmsRequestListValue]] = None
    Phase2IntegrityAlgorithms: Optional[List[Phase2IntegrityAlgorithmsRequestListValue]] = None
    Phase1DHGroupNumbers: Optional[List[Phase1DHGroupNumbersRequestListValue]] = None
    Phase2DHGroupNumbers: Optional[List[Phase2DHGroupNumbersRequestListValue]] = None
    IKEVersions: Optional[List[IKEVersionsRequestListValue]] = None
    StartupAction: Optional[str] = None
    LogOptions: Optional[VpnTunnelLogOptionsSpecification] = None
    EnableTunnelLifecycleControl: Optional[bool] = None


class VpnTunnelOptionsSpecification(BaseValidatorModel):
    TunnelInsideCidr: Optional[str] = None
    TunnelInsideIpv6Cidr: Optional[str] = None
    PreSharedKey: Optional[str] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2LifetimeSeconds: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    RekeyFuzzPercentage: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    DPDTimeoutSeconds: Optional[int] = None
    DPDTimeoutAction: Optional[str] = None
    Phase1EncryptionAlgorithms: Optional[List[Phase1EncryptionAlgorithmsRequestListValue]] = None
    Phase2EncryptionAlgorithms: Optional[List[Phase2EncryptionAlgorithmsRequestListValue]] = None
    Phase1IntegrityAlgorithms: Optional[List[Phase1IntegrityAlgorithmsRequestListValue]] = None
    Phase2IntegrityAlgorithms: Optional[List[Phase2IntegrityAlgorithmsRequestListValue]] = None
    Phase1DHGroupNumbers: Optional[List[Phase1DHGroupNumbersRequestListValue]] = None
    Phase2DHGroupNumbers: Optional[List[Phase2DHGroupNumbersRequestListValue]] = None
    IKEVersions: Optional[List[IKEVersionsRequestListValue]] = None
    StartupAction: Optional[str] = None
    LogOptions: Optional[VpnTunnelLogOptionsSpecification] = None
    EnableTunnelLifecycleControl: Optional[bool] = None


class TunnelOption(BaseValidatorModel):
    OutsideIpAddress: Optional[str] = None
    TunnelInsideCidr: Optional[str] = None
    TunnelInsideIpv6Cidr: Optional[str] = None
    PreSharedKey: Optional[str] = None
    Phase1LifetimeSeconds: Optional[int] = None
    Phase2LifetimeSeconds: Optional[int] = None
    RekeyMarginTimeSeconds: Optional[int] = None
    RekeyFuzzPercentage: Optional[int] = None
    ReplayWindowSize: Optional[int] = None
    DpdTimeoutSeconds: Optional[int] = None
    DpdTimeoutAction: Optional[str] = None
    Phase1EncryptionAlgorithms: Optional[List[Phase1EncryptionAlgorithmsListValue]] = None
    Phase2EncryptionAlgorithms: Optional[List[Phase2EncryptionAlgorithmsListValue]] = None
    Phase1IntegrityAlgorithms: Optional[List[Phase1IntegrityAlgorithmsListValue]] = None
    Phase2IntegrityAlgorithms: Optional[List[Phase2IntegrityAlgorithmsListValue]] = None
    Phase1DHGroupNumbers: Optional[List[Phase1DHGroupNumbersListValue]] = None
    Phase2DHGroupNumbers: Optional[List[Phase2DHGroupNumbersListValue]] = None
    IkeVersions: Optional[List[IKEVersionsListValue]] = None
    StartupAction: Optional[str] = None
    LogOptions: Optional[VpnTunnelLogOptions] = None
    EnableTunnelLifecycleControl: Optional[bool] = None


class BaselinePerformanceFactorsOutput(BaseValidatorModel):
    Cpu: Optional[CpuPerformanceFactorOutput] = None

CpuPerformanceFactorUnion = Union[CpuPerformanceFactor, CpuPerformanceFactorOutput]


class BaselinePerformanceFactorsRequest(BaseValidatorModel):
    Cpu: Optional[CpuPerformanceFactorRequest] = None


class NetworkAcl(BaseValidatorModel):
    Associations: Optional[List[NetworkAclAssociation]] = None
    Entries: Optional[List[NetworkAclEntry]] = None
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None


class ModifySnapshotAttributeRequestSnapshotModifyAttribute(BaseValidatorModel):
    Attribute: Optional[SnapshotAttributeNameType] = None
    CreateVolumePermission: Optional[CreateVolumePermissionModifications] = None
    GroupNames: Optional[List[str]] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_snapshot_attribute' function.
class ModifySnapshotAttributeRequest(BaseValidatorModel):
    SnapshotId: str
    Attribute: Optional[SnapshotAttributeNameType] = None
    CreateVolumePermission: Optional[CreateVolumePermissionModifications] = None
    GroupNames: Optional[List[str]] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the output for the 'get_aws_network_performance_data' function.
class GetAwsNetworkPerformanceDataResult(BaseValidatorModel):
    DataResponses: List[DataResponse]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'delete_fleets' function.
class DeleteFleetsResult(BaseValidatorModel):
    SuccessfulFleetDeletions: List[DeleteFleetSuccessItem]
    UnsuccessfulFleetDeletions: List[DeleteFleetErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_launch_template_versions' function.
class DeleteLaunchTemplateVersionsResult(BaseValidatorModel):
    SuccessfullyDeletedLaunchTemplateVersions: List[DeleteLaunchTemplateVersionsResponseSuccessItem]
    UnsuccessfullyDeletedLaunchTemplateVersions: List[DeleteLaunchTemplateVersionsResponseErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_queued_reserved_instances' function.
class DeleteQueuedReservedInstancesResult(BaseValidatorModel):
    SuccessfulQueuedPurchaseDeletions: List[SuccessfulQueuedPurchaseDeletion]
    FailedQueuedPurchaseDeletions: List[FailedQueuedPurchaseDeletion]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_principal_id_format' function.
class DescribePrincipalIdFormatResult(BaseValidatorModel):
    Principals: List[PrincipalIdFormat]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_fast_launch_images' function.
class DescribeFastLaunchImagesResult(BaseValidatorModel):
    FastLaunchImages: List[DescribeFastLaunchImagesSuccessItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_flow_logs' function.
class DescribeFlowLogsResult(BaseValidatorModel):
    FlowLogs: List[FlowLog]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DisableFastSnapshotRestoreErrorItem(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    FastSnapshotRestoreStateErrors: Optional[List[DisableFastSnapshotRestoreStateErrorItem]] = None


class ImportInstanceTaskDetails(BaseValidatorModel):
    Description: Optional[str] = None
    InstanceId: Optional[str] = None
    Platform: Optional[Literal['windows']] = None
    Volumes: Optional[List[ImportInstanceVolumeDetailItem]] = None


# This class is the output for the 'describe_vpc_endpoint_associations' function.
class DescribeVpcEndpointAssociationsResult(BaseValidatorModel):
    VpcEndpointAssociations: List[VpcEndpointAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_vpc_endpoint_connections' function.
class DescribeVpcEndpointConnectionsResult(BaseValidatorModel):
    VpcEndpointConnections: List[VpcEndpointConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyInstanceAttributeRequestInstanceModifyAttribute(BaseValidatorModel):
    SourceDestCheck: Optional[AttributeBooleanValue] = None
    DisableApiStop: Optional[AttributeBooleanValue] = None
    DryRun: Optional[bool] = None
    Attribute: Optional[InstanceAttributeNameType] = None
    Value: Optional[str] = None
    BlockDeviceMappings: Optional[List[InstanceBlockDeviceMappingSpecification]] = None
    DisableApiTermination: Optional[AttributeBooleanValue] = None
    InstanceType: Optional[AttributeValue] = None
    Kernel: Optional[AttributeValue] = None
    Ramdisk: Optional[AttributeValue] = None
    UserData: Optional[BlobAttributeValue] = None
    InstanceInitiatedShutdownBehavior: Optional[AttributeValue] = None
    Groups: Optional[List[str]] = None
    EbsOptimized: Optional[AttributeBooleanValue] = None
    SriovNetSupport: Optional[AttributeValue] = None
    EnaSupport: Optional[AttributeBooleanValue] = None


# This class is the input for the 'modify_instance_attribute' function.
class ModifyInstanceAttributeRequest(BaseValidatorModel):
    InstanceId: str
    SourceDestCheck: Optional[AttributeBooleanValue] = None
    DisableApiStop: Optional[AttributeBooleanValue] = None
    DryRun: Optional[bool] = None
    Attribute: Optional[InstanceAttributeNameType] = None
    Value: Optional[str] = None
    BlockDeviceMappings: Optional[List[InstanceBlockDeviceMappingSpecification]] = None
    DisableApiTermination: Optional[AttributeBooleanValue] = None
    InstanceType: Optional[AttributeValue] = None
    Kernel: Optional[AttributeValue] = None
    Ramdisk: Optional[AttributeValue] = None
    UserData: Optional[BlobAttributeValue] = None
    InstanceInitiatedShutdownBehavior: Optional[AttributeValue] = None
    Groups: Optional[List[str]] = None
    EbsOptimized: Optional[AttributeBooleanValue] = None
    SriovNetSupport: Optional[AttributeValue] = None
    EnaSupport: Optional[AttributeBooleanValue] = None


class InstanceBlockDeviceMapping(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[EbsInstanceBlockDevice] = None


# This class is the output for the 'delete_launch_template' function.
class DeleteLaunchTemplateResult(BaseValidatorModel):
    LaunchTemplate: LaunchTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_launch_templates' function.
class DescribeLaunchTemplatesResult(BaseValidatorModel):
    LaunchTemplates: List[LaunchTemplate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_launch_template' function.
class ModifyLaunchTemplateResult(BaseValidatorModel):
    LaunchTemplate: LaunchTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_egress_only_internet_gateway' function.
class CreateEgressOnlyInternetGatewayResult(BaseValidatorModel):
    ClientToken: str
    EgressOnlyInternetGateway: EgressOnlyInternetGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_egress_only_internet_gateways' function.
class DescribeEgressOnlyInternetGatewaysResult(BaseValidatorModel):
    EgressOnlyInternetGateways: List[EgressOnlyInternetGateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_internet_gateway' function.
class CreateInternetGatewayResult(BaseValidatorModel):
    InternetGateway: InternetGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_internet_gateways' function.
class DescribeInternetGatewaysResult(BaseValidatorModel):
    InternetGateways: List[InternetGateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_elastic_gpus' function.
class DescribeElasticGpusResult(BaseValidatorModel):
    ElasticGpuSet: List[ElasticGpus]
    MaxResults: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InstanceNetworkInterfaceSpecificationOutput(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecification]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    AssociateCarrierIpAddress: Optional[bool] = None
    InterfaceType: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequest]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequest]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationRequest] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None


class InstanceNetworkInterfaceSpecification(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecification]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    AssociateCarrierIpAddress: Optional[bool] = None
    InterfaceType: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequest]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequest]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationRequest] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None


class LaunchTemplateInstanceNetworkInterfaceSpecificationRequest(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6AddressRequest]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecification]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequest]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequest]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationRequest] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None


class AttachNetworkInterfaceRequestNetworkInterfaceAttach(BaseValidatorModel):
    InstanceId: str
    DeviceIndex: int
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[EnaSrdSpecification] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'attach_network_interface' function.
class AttachNetworkInterfaceRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    InstanceId: str
    DeviceIndex: int
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[EnaSrdSpecification] = None
    DryRun: Optional[bool] = None


class ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttribute(BaseValidatorModel):
    EnaSrdSpecification: Optional[EnaSrdSpecification] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DryRun: Optional[bool] = None
    Description: Optional[AttributeValue] = None
    SourceDestCheck: Optional[AttributeBooleanValue] = None
    Groups: Optional[List[str]] = None
    Attachment: Optional[NetworkInterfaceAttachmentChanges] = None


# This class is the input for the 'modify_network_interface_attribute' function.
class ModifyNetworkInterfaceAttributeRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    EnaSrdSpecification: Optional[EnaSrdSpecification] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DryRun: Optional[bool] = None
    Description: Optional[AttributeValue] = None
    SourceDestCheck: Optional[AttributeBooleanValue] = None
    Groups: Optional[List[str]] = None
    Attachment: Optional[NetworkInterfaceAttachmentChanges] = None


class EnableFastSnapshotRestoreErrorItem(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    FastSnapshotRestoreStateErrors: Optional[List[EnableFastSnapshotRestoreStateErrorItem]] = None


# This class is the output for the 'describe_fleet_history' function.
class DescribeFleetHistoryResult(BaseValidatorModel):
    HistoryRecords: List[HistoryRecordEntry]
    LastEvaluatedTime: datetime
    FleetId: str
    StartTime: datetime
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_spot_fleet_request_history' function.
class DescribeSpotFleetRequestHistoryResponse(BaseValidatorModel):
    HistoryRecords: List[HistoryRecord]
    LastEvaluatedTime: datetime
    SpotFleetRequestId: str
    StartTime: datetime
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_export_image_tasks' function.
class DescribeExportImageTasksResult(BaseValidatorModel):
    ExportImageTasks: List[ExportImageTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_instance_export_task' function.
class CreateInstanceExportTaskResult(BaseValidatorModel):
    ExportTask: ExportTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_export_tasks' function.
class DescribeExportTasksResult(BaseValidatorModel):
    ExportTasks: List[ExportTask]
    ResponseMetadata: ResponseMetadata


class NetworkInsightsPath(BaseValidatorModel):
    NetworkInsightsPathId: Optional[str] = None
    NetworkInsightsPathArn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    Source: Optional[str] = None
    Destination: Optional[str] = None
    SourceArn: Optional[str] = None
    DestinationArn: Optional[str] = None
    SourceIp: Optional[str] = None
    DestinationIp: Optional[str] = None
    Protocol: Optional[ProtocolType] = None
    DestinationPort: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    FilterAtSource: Optional[PathFilter] = None
    FilterAtDestination: Optional[PathFilter] = None


class SpotOptionsRequest(BaseValidatorModel):
    AllocationStrategy: Optional[SpotAllocationStrategyType] = None
    MaintenanceStrategies: Optional[FleetSpotMaintenanceStrategiesRequest] = None
    InstanceInterruptionBehavior: Optional[SpotInstanceInterruptionBehaviorType] = None
    InstancePoolsToUseCount: Optional[int] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None


class SpotOptions(BaseValidatorModel):
    AllocationStrategy: Optional[SpotAllocationStrategyType] = None
    MaintenanceStrategies: Optional[FleetSpotMaintenanceStrategies] = None
    InstanceInterruptionBehavior: Optional[SpotInstanceInterruptionBehaviorType] = None
    InstancePoolsToUseCount: Optional[int] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None


class FpgaInfo(BaseValidatorModel):
    Fpgas: Optional[List[FpgaDeviceInfo]] = None
    TotalFpgaMemoryInMiB: Optional[int] = None


# This class is the output for the 'describe_fpga_image_attribute' function.
class DescribeFpgaImageAttributeResult(BaseValidatorModel):
    FpgaImageAttribute: FpgaImageAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_fpga_image_attribute' function.
class ModifyFpgaImageAttributeResult(BaseValidatorModel):
    FpgaImageAttribute: FpgaImageAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_fpga_images' function.
class DescribeFpgaImagesResult(BaseValidatorModel):
    FpgaImages: List[FpgaImage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GpuInfo(BaseValidatorModel):
    Gpus: Optional[List[GpuDeviceInfo]] = None
    TotalGpuMemoryInMiB: Optional[int] = None


# This class is the output for the 'associate_iam_instance_profile' function.
class AssociateIamInstanceProfileResult(BaseValidatorModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_iam_instance_profile_associations' function.
class DescribeIamInstanceProfileAssociationsResult(BaseValidatorModel):
    IamInstanceProfileAssociations: List[IamInstanceProfileAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'disassociate_iam_instance_profile' function.
class DisassociateIamInstanceProfileResult(BaseValidatorModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replace_iam_instance_profile_association' function.
class ReplaceIamInstanceProfileAssociationResult(BaseValidatorModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociation
    ResponseMetadata: ResponseMetadata


class ModifyImageAttributeRequestImageModifyAttribute(BaseValidatorModel):
    Attribute: Optional[str] = None
    Description: Optional[AttributeValue] = None
    LaunchPermission: Optional[LaunchPermissionModifications] = None
    OperationType: Optional[OperationTypeType] = None
    ProductCodes: Optional[List[str]] = None
    UserGroups: Optional[List[str]] = None
    UserIds: Optional[List[str]] = None
    Value: Optional[str] = None
    OrganizationArns: Optional[List[str]] = None
    OrganizationalUnitArns: Optional[List[str]] = None
    ImdsSupport: Optional[AttributeValue] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'modify_image_attribute' function.
class ModifyImageAttributeRequest(BaseValidatorModel):
    ImageId: str
    Attribute: Optional[str] = None
    Description: Optional[AttributeValue] = None
    LaunchPermission: Optional[LaunchPermissionModifications] = None
    OperationType: Optional[OperationTypeType] = None
    ProductCodes: Optional[List[str]] = None
    UserGroups: Optional[List[str]] = None
    UserIds: Optional[List[str]] = None
    Value: Optional[str] = None
    OrganizationArns: Optional[List[str]] = None
    OrganizationalUnitArns: Optional[List[str]] = None
    ImdsSupport: Optional[AttributeValue] = None
    DryRun: Optional[bool] = None


# This class is the output for the 'create_local_gateway_route_table' function.
class CreateLocalGatewayRouteTableResult(BaseValidatorModel):
    LocalGatewayRouteTable: LocalGatewayRouteTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_local_gateway_route_table' function.
class DeleteLocalGatewayRouteTableResult(BaseValidatorModel):
    LocalGatewayRouteTable: LocalGatewayRouteTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_local_gateway_route_tables' function.
class DescribeLocalGatewayRouteTablesResult(BaseValidatorModel):
    LocalGatewayRouteTables: List[LocalGatewayRouteTable]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'import_instance' function.
class ImportInstanceRequest(BaseValidatorModel):
    Platform: Literal['windows']
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    LaunchSpecification: Optional[ImportInstanceLaunchSpecification] = None
    DiskImages: Optional[List[DiskImage]] = None


class InferenceAcceleratorInfo(BaseValidatorModel):
    Accelerators: Optional[List[InferenceDeviceInfo]] = None
    TotalInferenceMemoryInMiB: Optional[int] = None


class InstanceNetworkInterfaceAttachment(BaseValidatorModel):
    AttachTime: Optional[datetime] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    Status: Optional[AttachmentStatusType] = None
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[InstanceAttachmentEnaSrdSpecification] = None


# This class is the output for the 'describe_instance_image_metadata' function.
class DescribeInstanceImageMetadataResult(BaseValidatorModel):
    InstanceImageMetadata: List[InstanceImageMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_instances' function.
class StartInstancesResult(BaseValidatorModel):
    StartingInstances: List[InstanceStateChange]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_instances' function.
class StopInstancesResult(BaseValidatorModel):
    StoppingInstances: List[InstanceStateChange]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'terminate_instances' function.
class TerminateInstancesResult(BaseValidatorModel):
    TerminatingInstances: List[InstanceStateChange]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'monitor_instances' function.
class MonitorInstancesResult(BaseValidatorModel):
    InstanceMonitorings: List[InstanceMonitoring]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unmonitor_instances' function.
class UnmonitorInstancesResult(BaseValidatorModel):
    InstanceMonitorings: List[InstanceMonitoring]
    ResponseMetadata: ResponseMetadata


class InstanceStatus(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    OutpostArn: Optional[str] = None
    Operator: Optional[OperatorResponse] = None
    Events: Optional[List[InstanceStatusEvent]] = None
    InstanceId: Optional[str] = None
    InstanceState: Optional[InstanceState] = None
    InstanceStatus: Optional[InstanceStatusSummary] = None
    SystemStatus: Optional[InstanceStatusSummary] = None
    AttachedEbsStatus: Optional[EbsStatusSummary] = None


# This class is the output for the 'revoke_security_group_egress' function.
class RevokeSecurityGroupEgressResult(BaseValidatorModel):
    Return: bool
    UnknownIpPermissions: List[IpPermissionOutput]
    RevokedSecurityGroupRules: List[RevokedSecurityGroupRule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_security_group_ingress' function.
class RevokeSecurityGroupIngressResult(BaseValidatorModel):
    Return: bool
    UnknownIpPermissions: List[IpPermissionOutput]
    RevokedSecurityGroupRules: List[RevokedSecurityGroupRule]
    ResponseMetadata: ResponseMetadata


class SecurityGroup(BaseValidatorModel):
    GroupId: Optional[str] = None
    IpPermissionsEgress: Optional[List[IpPermissionOutput]] = None
    Tags: Optional[List[Tag]] = None
    VpcId: Optional[str] = None
    SecurityGroupArn: Optional[str] = None
    OwnerId: Optional[str] = None
    GroupName: Optional[str] = None
    Description: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionOutput]] = None

IpPermissionUnion = Union[IpPermission, IpPermissionOutput]


class StaleSecurityGroup(BaseValidatorModel):
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    StaleIpPermissions: Optional[List[StaleIpPermission]] = None
    StaleIpPermissionsEgress: Optional[List[StaleIpPermission]] = None
    VpcId: Optional[str] = None


# This class is the output for the 'get_ipam_discovered_accounts' function.
class GetIpamDiscoveredAccountsResult(BaseValidatorModel):
    IpamDiscoveredAccounts: List[IpamDiscoveredAccount]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_ipam_discovered_resource_cidrs' function.
class GetIpamDiscoveredResourceCidrsResult(BaseValidatorModel):
    IpamDiscoveredResourceCidrs: List[IpamDiscoveredResourceCidr]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_ipam_resource_cidrs' function.
class GetIpamResourceCidrsResult(BaseValidatorModel):
    IpamResourceCidrs: List[IpamResourceCidr]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_ipam_resource_cidr' function.
class ModifyIpamResourceCidrResult(BaseValidatorModel):
    IpamResourceCidr: IpamResourceCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ipam' function.
class CreateIpamResult(BaseValidatorModel):
    Ipam: Ipam
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ipam' function.
class DeleteIpamResult(BaseValidatorModel):
    Ipam: Ipam
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ipams' function.
class DescribeIpamsResult(BaseValidatorModel):
    Ipams: List[Ipam]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_ipam' function.
class ModifyIpamResult(BaseValidatorModel):
    Ipam: Ipam
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ipam_resource_discovery' function.
class CreateIpamResourceDiscoveryResult(BaseValidatorModel):
    IpamResourceDiscovery: IpamResourceDiscovery
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ipam_resource_discovery' function.
class DeleteIpamResourceDiscoveryResult(BaseValidatorModel):
    IpamResourceDiscovery: IpamResourceDiscovery
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ipam_resource_discoveries' function.
class DescribeIpamResourceDiscoveriesResult(BaseValidatorModel):
    IpamResourceDiscoveries: List[IpamResourceDiscovery]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_ipam_resource_discovery' function.
class ModifyIpamResourceDiscoveryResult(BaseValidatorModel):
    IpamResourceDiscovery: IpamResourceDiscovery
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deprovision_ipam_pool_cidr' function.
class DeprovisionIpamPoolCidrResult(BaseValidatorModel):
    IpamPoolCidr: IpamPoolCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ipam_pool_cidrs' function.
class GetIpamPoolCidrsResult(BaseValidatorModel):
    IpamPoolCidrs: List[IpamPoolCidr]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'provision_ipam_pool_cidr' function.
class ProvisionIpamPoolCidrResult(BaseValidatorModel):
    IpamPoolCidr: IpamPoolCidr
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ipam_pool' function.
class CreateIpamPoolResult(BaseValidatorModel):
    IpamPool: IpamPool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_ipam_pool' function.
class DeleteIpamPoolResult(BaseValidatorModel):
    IpamPool: IpamPool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ipam_pools' function.
class DescribeIpamPoolsResult(BaseValidatorModel):
    IpamPools: List[IpamPool]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_ipam_pool' function.
class ModifyIpamPoolResult(BaseValidatorModel):
    IpamPool: IpamPool
    ResponseMetadata: ResponseMetadata


class IpamDiscoveredPublicAddress(BaseValidatorModel):
    IpamResourceDiscoveryId: Optional[str] = None
    AddressRegion: Optional[str] = None
    Address: Optional[str] = None
    AddressOwnerId: Optional[str] = None
    AddressAllocationId: Optional[str] = None
    AssociationStatus: Optional[IpamPublicAddressAssociationStatusType] = None
    AddressType: Optional[IpamPublicAddressTypeType] = None
    Service: Optional[IpamPublicAddressAwsServiceType] = None
    ServiceResource: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    PublicIpv4PoolId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfaceDescription: Optional[str] = None
    InstanceId: Optional[str] = None
    Tags: Optional[IpamPublicAddressTags] = None
    NetworkBorderGroup: Optional[str] = None
    SecurityGroups: Optional[List[IpamPublicAddressSecurityGroup]] = None
    SampleTime: Optional[datetime] = None


# This class is the output for the 'describe_ipv6_pools' function.
class DescribeIpv6PoolsResult(BaseValidatorModel):
    Ipv6Pools: List[Ipv6Pool]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LaunchTemplateInstanceNetworkInterfaceSpecification(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecification]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationResponse]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationResponse]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[LaunchTemplateEnaSrdSpecification] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecification] = None


# This class is the input for the 'modify_fpga_image_attribute' function.
class ModifyFpgaImageAttributeRequest(BaseValidatorModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None
    Attribute: Optional[FpgaImageAttributeNameType] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[List[str]] = None
    UserGroups: Optional[List[str]] = None
    ProductCodes: Optional[List[str]] = None
    LoadPermission: Optional[LoadPermissionModifications] = None
    Description: Optional[str] = None
    Name: Optional[str] = None


class MediaAcceleratorInfo(BaseValidatorModel):
    Accelerators: Optional[List[MediaDeviceInfo]] = None
    TotalMediaMemoryInMiB: Optional[int] = None


class ReservedInstancesModification(BaseValidatorModel):
    ClientToken: Optional[str] = None
    CreateDate: Optional[datetime] = None
    EffectiveDate: Optional[datetime] = None
    ModificationResults: Optional[List[ReservedInstancesModificationResult]] = None
    ReservedInstancesIds: Optional[List[ReservedInstancesId]] = None
    ReservedInstancesModificationId: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdateDate: Optional[datetime] = None


# This class is the input for the 'modify_verified_access_endpoint' function.
class ModifyVerifiedAccessEndpointRequest(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    VerifiedAccessGroupId: Optional[str] = None
    LoadBalancerOptions: Optional[ModifyVerifiedAccessEndpointLoadBalancerOptions] = None
    NetworkInterfaceOptions: Optional[ModifyVerifiedAccessEndpointEniOptions] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    RdsOptions: Optional[ModifyVerifiedAccessEndpointRdsOptions] = None
    CidrOptions: Optional[ModifyVerifiedAccessEndpointCidrOptions] = None


# This class is the output for the 'create_verified_access_group' function.
class CreateVerifiedAccessGroupResult(BaseValidatorModel):
    VerifiedAccessGroup: VerifiedAccessGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_verified_access_group' function.
class DeleteVerifiedAccessGroupResult(BaseValidatorModel):
    VerifiedAccessGroup: VerifiedAccessGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_verified_access_groups' function.
class DescribeVerifiedAccessGroupsResult(BaseValidatorModel):
    VerifiedAccessGroups: List[VerifiedAccessGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_verified_access_group' function.
class ModifyVerifiedAccessGroupResult(BaseValidatorModel):
    VerifiedAccessGroup: VerifiedAccessGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_nat_gateway' function.
class CreateNatGatewayResult(BaseValidatorModel):
    ClientToken: str
    NatGateway: NatGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_nat_gateways' function.
class DescribeNatGatewaysResult(BaseValidatorModel):
    NatGateways: List[NatGateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_network_interface_permission' function.
class CreateNetworkInterfacePermissionResult(BaseValidatorModel):
    InterfacePermission: NetworkInterfacePermission
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_network_interface_permissions' function.
class DescribeNetworkInterfacePermissionsResult(BaseValidatorModel):
    NetworkInterfacePermissions: List[NetworkInterfacePermission]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class NeuronInfo(BaseValidatorModel):
    NeuronDevices: Optional[List[NeuronDeviceInfo]] = None
    TotalNeuronDeviceMemoryInMiB: Optional[int] = None


# This class is the output for the 'create_verified_access_trust_provider' function.
class CreateVerifiedAccessTrustProviderResult(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProvider
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_verified_access_trust_provider' function.
class DeleteVerifiedAccessTrustProviderResult(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProvider
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_verified_access_trust_providers' function.
class DescribeVerifiedAccessTrustProvidersResult(BaseValidatorModel):
    VerifiedAccessTrustProviders: List[VerifiedAccessTrustProvider]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_verified_access_trust_provider' function.
class ModifyVerifiedAccessTrustProviderResult(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProvider
    ResponseMetadata: ResponseMetadata


class AccessScopePathRequest(BaseValidatorModel):
    Source: Optional[PathStatementRequest] = None
    Destination: Optional[PathStatementRequest] = None
    ThroughResources: Optional[List[ThroughResourcesStatementRequest]] = None


class AccessScopePath(BaseValidatorModel):
    Source: Optional[PathStatement] = None
    Destination: Optional[PathStatement] = None
    ThroughResources: Optional[List[ThroughResourcesStatement]] = None


# This class is the output for the 'cancel_reserved_instances_listing' function.
class CancelReservedInstancesListingResult(BaseValidatorModel):
    ReservedInstancesListings: List[ReservedInstancesListing]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_reserved_instances_listing' function.
class CreateReservedInstancesListingResult(BaseValidatorModel):
    ReservedInstancesListings: List[ReservedInstancesListing]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_instances_listings' function.
class DescribeReservedInstancesListingsResult(BaseValidatorModel):
    ReservedInstancesListings: List[ReservedInstancesListing]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_public_ipv4_pools' function.
class DescribePublicIpv4PoolsResult(BaseValidatorModel):
    PublicIpv4Pools: List[PublicIpv4Pool]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_reserved_instances_offerings' function.
class DescribeReservedInstancesOfferingsResult(BaseValidatorModel):
    ReservedInstancesOfferings: List[ReservedInstancesOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_reserved_instances' function.
class DescribeReservedInstancesResult(BaseValidatorModel):
    ReservedInstances: List[ReservedInstances]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'authorize_security_group_egress' function.
class AuthorizeSecurityGroupEgressResult(BaseValidatorModel):
    Return: bool
    SecurityGroupRules: List[SecurityGroupRule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'authorize_security_group_ingress' function.
class AuthorizeSecurityGroupIngressResult(BaseValidatorModel):
    Return: bool
    SecurityGroupRules: List[SecurityGroupRule]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_security_group_rules' function.
class DescribeSecurityGroupRulesResult(BaseValidatorModel):
    SecurityGroupRules: List[SecurityGroupRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BundleTask(BaseValidatorModel):
    InstanceId: Optional[str] = None
    BundleId: Optional[str] = None
    State: Optional[BundleTaskStateType] = None
    StartTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    Storage: Optional[StorageOutput] = None
    Progress: Optional[str] = None
    BundleTaskError: Optional[BundleTaskError] = None


# This class is the output for the 'describe_scheduled_instance_availability' function.
class DescribeScheduledInstanceAvailabilityResult(BaseValidatorModel):
    ScheduledInstanceAvailabilitySet: List[ScheduledInstanceAvailability]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_scheduled_instances' function.
class DescribeScheduledInstancesResult(BaseValidatorModel):
    ScheduledInstanceSet: List[ScheduledInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'purchase_scheduled_instances' function.
class PurchaseScheduledInstancesResult(BaseValidatorModel):
    ScheduledInstanceSet: List[ScheduledInstance]
    ResponseMetadata: ResponseMetadata


class ScheduledInstancesLaunchSpecification(BaseValidatorModel):
    ImageId: str
    BlockDeviceMappings: Optional[List[ScheduledInstancesBlockDeviceMapping]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[ScheduledInstancesIamInstanceProfile] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[ScheduledInstancesMonitoring] = None
    NetworkInterfaces: Optional[List[ScheduledInstancesNetworkInterface]] = None
    Placement: Optional[ScheduledInstancesPlacement] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None


# This class is the input for the 'modify_security_group_rules' function.
class ModifySecurityGroupRulesRequest(BaseValidatorModel):
    GroupId: str
    SecurityGroupRules: List[SecurityGroupRuleUpdate]
    DryRun: Optional[bool] = None


# This class is the output for the 'describe_vpc_endpoint_services' function.
class DescribeVpcEndpointServicesResult(BaseValidatorModel):
    ServiceNames: List[str]
    ServiceDetails: List[ServiceDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_vpc_endpoint_service_configuration' function.
class CreateVpcEndpointServiceConfigurationResult(BaseValidatorModel):
    ServiceConfiguration: ServiceConfiguration
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_endpoint_service_configurations' function.
class DescribeVpcEndpointServiceConfigurationsResult(BaseValidatorModel):
    ServiceConfigurations: List[ServiceConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'import_image' function.
class ImportImageResult(BaseValidatorModel):
    Architecture: str
    Description: str
    Encrypted: bool
    Hypervisor: str
    ImageId: str
    ImportTaskId: str
    KmsKeyId: str
    LicenseType: str
    Platform: str
    Progress: str
    SnapshotDetails: List[SnapshotDetail]
    Status: str
    StatusMessage: str
    LicenseSpecifications: List[ImportImageLicenseConfigurationResponse]
    Tags: List[Tag]
    UsageOperation: str
    ResponseMetadata: ResponseMetadata


class ImportImageTask(BaseValidatorModel):
    Architecture: Optional[str] = None
    Description: Optional[str] = None
    Encrypted: Optional[bool] = None
    Hypervisor: Optional[str] = None
    ImageId: Optional[str] = None
    ImportTaskId: Optional[str] = None
    KmsKeyId: Optional[str] = None
    LicenseType: Optional[str] = None
    Platform: Optional[str] = None
    Progress: Optional[str] = None
    SnapshotDetails: Optional[List[SnapshotDetail]] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    LicenseSpecifications: Optional[List[ImportImageLicenseConfigurationResponse]] = None
    UsageOperation: Optional[str] = None
    BootMode: Optional[BootModeValuesType] = None


# This class is the output for the 'import_snapshot' function.
class ImportSnapshotResult(BaseValidatorModel):
    Description: str
    ImportTaskId: str
    SnapshotTaskDetail: SnapshotTaskDetail
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ImportSnapshotTask(BaseValidatorModel):
    Description: Optional[str] = None
    ImportTaskId: Optional[str] = None
    SnapshotTaskDetail: Optional[SnapshotTaskDetail] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_spot_datafeed_subscription' function.
class CreateSpotDatafeedSubscriptionResult(BaseValidatorModel):
    SpotDatafeedSubscription: SpotDatafeedSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_spot_datafeed_subscription' function.
class DescribeSpotDatafeedSubscriptionResult(BaseValidatorModel):
    SpotDatafeedSubscription: SpotDatafeedSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transit_gateway_multicast_domain_associations' function.
class GetTransitGatewayMulticastDomainAssociationsResult(BaseValidatorModel):
    MulticastDomainAssociations: List[TransitGatewayMulticastDomainAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'accept_transit_gateway_multicast_domain_associations' function.
class AcceptTransitGatewayMulticastDomainAssociationsResult(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociations
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_transit_gateway_multicast_domain' function.
class AssociateTransitGatewayMulticastDomainResult(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociations
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_transit_gateway_multicast_domain' function.
class DisassociateTransitGatewayMulticastDomainResult(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociations
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_transit_gateway_multicast_domain_associations' function.
class RejectTransitGatewayMulticastDomainAssociationsResult(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociations
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_subnet_cidr_block' function.
class AssociateSubnetCidrBlockResult(BaseValidatorModel):
    Ipv6CidrBlockAssociation: SubnetIpv6CidrBlockAssociation
    SubnetId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_subnet_cidr_block' function.
class DisassociateSubnetCidrBlockResult(BaseValidatorModel):
    Ipv6CidrBlockAssociation: SubnetIpv6CidrBlockAssociation
    SubnetId: str
    ResponseMetadata: ResponseMetadata


class Subnet(BaseValidatorModel):
    AvailabilityZoneId: Optional[str] = None
    EnableLniAtDeviceIndex: Optional[int] = None
    MapCustomerOwnedIpOnLaunch: Optional[bool] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    OwnerId: Optional[str] = None
    AssignIpv6AddressOnCreation: Optional[bool] = None
    Ipv6CidrBlockAssociationSet: Optional[List[SubnetIpv6CidrBlockAssociation]] = None
    Tags: Optional[List[Tag]] = None
    SubnetArn: Optional[str] = None
    OutpostArn: Optional[str] = None
    EnableDns64: Optional[bool] = None
    Ipv6Native: Optional[bool] = None
    PrivateDnsNameOptionsOnLaunch: Optional[PrivateDnsNameOptionsOnLaunch] = None
    BlockPublicAccessStates: Optional[BlockPublicAccessStates] = None
    SubnetId: Optional[str] = None
    State: Optional[SubnetStateType] = None
    VpcId: Optional[str] = None
    CidrBlock: Optional[str] = None
    AvailableIpAddressCount: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    DefaultForAz: Optional[bool] = None
    MapPublicIpOnLaunch: Optional[bool] = None


# This class is the output for the 'create_vpc_endpoint' function.
class CreateVpcEndpointResult(BaseValidatorModel):
    VpcEndpoint: VpcEndpoint
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_endpoints' function.
class DescribeVpcEndpointsResult(BaseValidatorModel):
    VpcEndpoints: List[VpcEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_reserved_instances_exchange_quote' function.
class GetReservedInstancesExchangeQuoteResult(BaseValidatorModel):
    CurrencyCode: str
    IsValidExchange: bool
    OutputReservedInstancesWillExpireAt: datetime
    PaymentDue: str
    ReservedInstanceValueRollup: ReservationValue
    ReservedInstanceValueSet: List[ReservedInstanceReservationValue]
    TargetConfigurationValueRollup: ReservationValue
    TargetConfigurationValueSet: List[TargetReservationValue]
    ValidationFailureReason: str
    ResponseMetadata: ResponseMetadata


class LoadBalancersConfigOutput(BaseValidatorModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfigOutput] = None
    TargetGroupsConfig: Optional[TargetGroupsConfigOutput] = None


class LoadBalancersConfig(BaseValidatorModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfig] = None
    TargetGroupsConfig: Optional[TargetGroupsConfig] = None


# This class is the output for the 'create_traffic_mirror_filter_rule' function.
class CreateTrafficMirrorFilterRuleResult(BaseValidatorModel):
    TrafficMirrorFilterRule: TrafficMirrorFilterRule
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_traffic_mirror_filter_rules' function.
class DescribeTrafficMirrorFilterRulesResult(BaseValidatorModel):
    TrafficMirrorFilterRules: List[TrafficMirrorFilterRule]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_traffic_mirror_filter_rule' function.
class ModifyTrafficMirrorFilterRuleResult(BaseValidatorModel):
    TrafficMirrorFilterRule: TrafficMirrorFilterRule
    ResponseMetadata: ResponseMetadata


class TrafficMirrorFilter(BaseValidatorModel):
    TrafficMirrorFilterId: Optional[str] = None
    IngressFilterRules: Optional[List[TrafficMirrorFilterRule]] = None
    EgressFilterRules: Optional[List[TrafficMirrorFilterRule]] = None
    NetworkServices: Optional[List[Literal['amazon-dns']]] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_transit_gateway_attachments' function.
class DescribeTransitGatewayAttachmentsResult(BaseValidatorModel):
    TransitGatewayAttachments: List[TransitGatewayAttachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TransitGatewayConnectPeer(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayConnectPeerId: Optional[str] = None
    State: Optional[TransitGatewayConnectPeerStateType] = None
    CreationTime: Optional[datetime] = None
    ConnectPeerConfiguration: Optional[TransitGatewayConnectPeerConfiguration] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_transit_gateway_connect' function.
class CreateTransitGatewayConnectResult(BaseValidatorModel):
    TransitGatewayConnect: TransitGatewayConnect
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_connect' function.
class DeleteTransitGatewayConnectResult(BaseValidatorModel):
    TransitGatewayConnect: TransitGatewayConnect
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_connects' function.
class DescribeTransitGatewayConnectsResult(BaseValidatorModel):
    TransitGatewayConnects: List[TransitGatewayConnect]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_transit_gateway_multicast_domain' function.
class CreateTransitGatewayMulticastDomainResult(BaseValidatorModel):
    TransitGatewayMulticastDomain: TransitGatewayMulticastDomain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_multicast_domain' function.
class DeleteTransitGatewayMulticastDomainResult(BaseValidatorModel):
    TransitGatewayMulticastDomain: TransitGatewayMulticastDomain
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_multicast_domains' function.
class DescribeTransitGatewayMulticastDomainsResult(BaseValidatorModel):
    TransitGatewayMulticastDomains: List[TransitGatewayMulticastDomain]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_transit_gateway' function.
class CreateTransitGatewayResult(BaseValidatorModel):
    TransitGateway: TransitGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway' function.
class DeleteTransitGatewayResult(BaseValidatorModel):
    TransitGateway: TransitGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateways' function.
class DescribeTransitGatewaysResult(BaseValidatorModel):
    TransitGateways: List[TransitGateway]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_transit_gateway' function.
class ModifyTransitGatewayResult(BaseValidatorModel):
    TransitGateway: TransitGateway
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_transit_gateway_peering_attachment' function.
class AcceptTransitGatewayPeeringAttachmentResult(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transit_gateway_peering_attachment' function.
class CreateTransitGatewayPeeringAttachmentResult(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_peering_attachment' function.
class DeleteTransitGatewayPeeringAttachmentResult(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_peering_attachments' function.
class DescribeTransitGatewayPeeringAttachmentsResult(BaseValidatorModel):
    TransitGatewayPeeringAttachments: List[TransitGatewayPeeringAttachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'reject_transit_gateway_peering_attachment' function.
class RejectTransitGatewayPeeringAttachmentResult(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachment
    ResponseMetadata: ResponseMetadata


class TransitGatewayPolicyTableEntry(BaseValidatorModel):
    PolicyRuleNumber: Optional[str] = None
    PolicyRule: Optional[TransitGatewayPolicyRule] = None
    TargetRouteTableId: Optional[str] = None


# This class is the output for the 'create_transit_gateway_prefix_list_reference' function.
class CreateTransitGatewayPrefixListReferenceResult(BaseValidatorModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReference
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_prefix_list_reference' function.
class DeleteTransitGatewayPrefixListReferenceResult(BaseValidatorModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReference
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_transit_gateway_prefix_list_references' function.
class GetTransitGatewayPrefixListReferencesResult(BaseValidatorModel):
    TransitGatewayPrefixListReferences: List[TransitGatewayPrefixListReference]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_transit_gateway_prefix_list_reference' function.
class ModifyTransitGatewayPrefixListReferenceResult(BaseValidatorModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReference
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transit_gateway_route' function.
class CreateTransitGatewayRouteResult(BaseValidatorModel):
    Route: TransitGatewayRoute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_route' function.
class DeleteTransitGatewayRouteResult(BaseValidatorModel):
    Route: TransitGatewayRoute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replace_transit_gateway_route' function.
class ReplaceTransitGatewayRouteResult(BaseValidatorModel):
    Route: TransitGatewayRoute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_transit_gateway_routes' function.
class SearchTransitGatewayRoutesResult(BaseValidatorModel):
    Routes: List[TransitGatewayRoute]
    AdditionalRoutesAvailable: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_transit_gateway_vpc_attachment' function.
class AcceptTransitGatewayVpcAttachmentResult(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transit_gateway_vpc_attachment' function.
class CreateTransitGatewayVpcAttachmentResult(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_vpc_attachment' function.
class DeleteTransitGatewayVpcAttachmentResult(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_vpc_attachments' function.
class DescribeTransitGatewayVpcAttachmentsResult(BaseValidatorModel):
    TransitGatewayVpcAttachments: List[TransitGatewayVpcAttachment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_transit_gateway_vpc_attachment' function.
class ModifyTransitGatewayVpcAttachmentResult(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_transit_gateway_vpc_attachment' function.
class RejectTransitGatewayVpcAttachmentResult(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_credit_specification' function.
class ModifyInstanceCreditSpecificationResult(BaseValidatorModel):
    SuccessfulInstanceCreditSpecifications: List[SuccessfulInstanceCreditSpecificationItem]
    UnsuccessfulInstanceCreditSpecifications: List[UnsuccessfulInstanceCreditSpecificationItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_vpc_endpoint_connections' function.
class AcceptVpcEndpointConnectionsResult(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_flow_logs' function.
class CreateFlowLogsResult(BaseValidatorModel):
    ClientToken: str
    FlowLogIds: List[str]
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_flow_logs' function.
class DeleteFlowLogsResult(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_endpoint_connection_notifications' function.
class DeleteVpcEndpointConnectionNotificationsResult(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_endpoint_service_configurations' function.
class DeleteVpcEndpointServiceConfigurationsResult(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vpc_endpoints' function.
class DeleteVpcEndpointsResult(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_hosts' function.
class ModifyHostsResult(BaseValidatorModel):
    Successful: List[str]
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_vpc_endpoint_connections' function.
class RejectVpcEndpointConnectionsResult(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'release_hosts' function.
class ReleaseHostsResult(BaseValidatorModel):
    Successful: List[str]
    Unsuccessful: List[UnsuccessfulItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_launch_template' function.
class CreateLaunchTemplateResult(BaseValidatorModel):
    LaunchTemplate: LaunchTemplate
    Warning: ValidationWarning
    ResponseMetadata: ResponseMetadata


class VerifiedAccessEndpoint(BaseValidatorModel):
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    VerifiedAccessEndpointId: Optional[str] = None
    ApplicationDomain: Optional[str] = None
    EndpointType: Optional[VerifiedAccessEndpointTypeType] = None
    AttachmentType: Optional[Literal['vpc']] = None
    DomainCertificateArn: Optional[str] = None
    EndpointDomain: Optional[str] = None
    DeviceValidationDomain: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    LoadBalancerOptions: Optional[VerifiedAccessEndpointLoadBalancerOptions] = None
    NetworkInterfaceOptions: Optional[VerifiedAccessEndpointEniOptions] = None
    Status: Optional[VerifiedAccessEndpointStatus] = None
    Description: Optional[str] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    DeletionTime: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationResponse] = None
    RdsOptions: Optional[VerifiedAccessEndpointRdsOptions] = None
    CidrOptions: Optional[VerifiedAccessEndpointCidrOptions] = None


# This class is the output for the 'export_verified_access_instance_client_configuration' function.
class ExportVerifiedAccessInstanceClientConfigurationResult(BaseValidatorModel):
    Version: str
    VerifiedAccessInstanceId: str
    Region: str
    DeviceTrustProviders: List[DeviceTrustProviderTypeType]
    UserTrustProvider: VerifiedAccessInstanceUserTrustProviderClientConfiguration
    OpenVpnConfigurations: List[VerifiedAccessInstanceOpenVpnClientConfiguration]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'attach_verified_access_trust_provider' function.
class AttachVerifiedAccessTrustProviderResult(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProvider
    VerifiedAccessInstance: VerifiedAccessInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_verified_access_instance' function.
class CreateVerifiedAccessInstanceResult(BaseValidatorModel):
    VerifiedAccessInstance: VerifiedAccessInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_verified_access_instance' function.
class DeleteVerifiedAccessInstanceResult(BaseValidatorModel):
    VerifiedAccessInstance: VerifiedAccessInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_verified_access_instances' function.
class DescribeVerifiedAccessInstancesResult(BaseValidatorModel):
    VerifiedAccessInstances: List[VerifiedAccessInstance]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'detach_verified_access_trust_provider' function.
class DetachVerifiedAccessTrustProviderResult(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProvider
    VerifiedAccessInstance: VerifiedAccessInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_verified_access_instance' function.
class ModifyVerifiedAccessInstanceResult(BaseValidatorModel):
    VerifiedAccessInstance: VerifiedAccessInstance
    ResponseMetadata: ResponseMetadata


class VerifiedAccessLogs(BaseValidatorModel):
    S3: Optional[VerifiedAccessLogS3Destination] = None
    CloudWatchLogs: Optional[VerifiedAccessLogCloudWatchLogsDestination] = None
    KinesisDataFirehose: Optional[VerifiedAccessLogKinesisDataFirehoseDestination] = None
    LogVersion: Optional[str] = None
    IncludeTrustContext: Optional[bool] = None


# This class is the input for the 'modify_verified_access_instance_logging_configuration' function.
class ModifyVerifiedAccessInstanceLoggingConfigurationRequest(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    AccessLogs: VerifiedAccessLogOptions
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


# This class is the output for the 'describe_volumes' function.
class DescribeVolumesResult(BaseValidatorModel):
    Volumes: List[Volume]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class VolumeStatusItem(BaseValidatorModel):
    Actions: Optional[List[VolumeStatusAction]] = None
    AvailabilityZone: Optional[str] = None
    OutpostArn: Optional[str] = None
    Events: Optional[List[VolumeStatusEvent]] = None
    VolumeId: Optional[str] = None
    VolumeStatus: Optional[VolumeStatusInfo] = None
    AttachmentStatuses: Optional[List[VolumeStatusAttachmentStatus]] = None


# This class is the output for the 'associate_vpc_cidr_block' function.
class AssociateVpcCidrBlockResult(BaseValidatorModel):
    Ipv6CidrBlockAssociation: VpcIpv6CidrBlockAssociation
    CidrBlockAssociation: VpcCidrBlockAssociation
    VpcId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_vpc_cidr_block' function.
class DisassociateVpcCidrBlockResult(BaseValidatorModel):
    Ipv6CidrBlockAssociation: VpcIpv6CidrBlockAssociation
    CidrBlockAssociation: VpcCidrBlockAssociation
    VpcId: str
    ResponseMetadata: ResponseMetadata


class VpcEncryptionControl(BaseValidatorModel):
    VpcId: Optional[str] = None
    VpcEncryptionControlId: Optional[str] = None
    Mode: Optional[VpcEncryptionControlModeType] = None
    State: Optional[VpcEncryptionControlStateType] = None
    StateMessage: Optional[str] = None
    ResourceExclusions: Optional[VpcEncryptionControlExclusions] = None
    Tags: Optional[List[Tag]] = None


class VpcPeeringConnection(BaseValidatorModel):
    AccepterVpcInfo: Optional[VpcPeeringConnectionVpcInfo] = None
    ExpirationTime: Optional[datetime] = None
    RequesterVpcInfo: Optional[VpcPeeringConnectionVpcInfo] = None
    Status: Optional[VpcPeeringConnectionStateReason] = None
    Tags: Optional[List[Tag]] = None
    VpcPeeringConnectionId: Optional[str] = None


# This class is the output for the 'associate_instance_event_window' function.
class AssociateInstanceEventWindowResult(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindow
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_instance_event_window' function.
class CreateInstanceEventWindowResult(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindow
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_instance_event_windows' function.
class DescribeInstanceEventWindowsResult(BaseValidatorModel):
    InstanceEventWindows: List[InstanceEventWindow]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'disassociate_instance_event_window' function.
class DisassociateInstanceEventWindowResult(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindow
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_instance_event_window' function.
class ModifyInstanceEventWindowResult(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindow
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'accept_address_transfer' function.
class AcceptAddressTransferRequest(BaseValidatorModel):
    Address: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'allocate_address' function.
class AllocateAddressRequest(BaseValidatorModel):
    Domain: Optional[DomainTypeType] = None
    Address: Optional[str] = None
    PublicIpv4Pool: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    IpamPoolId: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'allocate_hosts' function.
class AllocateHostsRequest(BaseValidatorModel):
    AvailabilityZone: str
    InstanceFamily: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    HostRecovery: Optional[HostRecoveryType] = None
    OutpostArn: Optional[str] = None
    HostMaintenance: Optional[HostMaintenanceType] = None
    AssetIds: Optional[List[str]] = None
    AutoPlacement: Optional[AutoPlacementType] = None
    ClientToken: Optional[str] = None
    InstanceType: Optional[str] = None
    Quantity: Optional[int] = None


# This class is the input for the 'associate_ipam_resource_discovery' function.
class AssociateIpamResourceDiscoveryRequest(BaseValidatorModel):
    IpamId: str
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'copy_image' function.
class CopyImageRequest(BaseValidatorModel):
    Name: str
    SourceImageId: str
    SourceRegion: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DestinationOutpostArn: Optional[str] = None
    CopyImageTags: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    SnapshotCopyCompletionDurationMinutes: Optional[int] = None
    DryRun: Optional[bool] = None


class CopySnapshotRequestSnapshotCopy(BaseValidatorModel):
    SourceRegion: str
    Description: Optional[str] = None
    DestinationOutpostArn: Optional[str] = None
    DestinationRegion: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PresignedUrl: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    CompletionDurationMinutes: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'copy_snapshot' function.
class CopySnapshotRequest(BaseValidatorModel):
    SourceRegion: str
    SourceSnapshotId: str
    Description: Optional[str] = None
    DestinationOutpostArn: Optional[str] = None
    DestinationRegion: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PresignedUrl: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    CompletionDurationMinutes: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_capacity_reservation_by_splitting' function.
class CreateCapacityReservationBySplittingRequest(BaseValidatorModel):
    SourceCapacityReservationId: str
    InstanceCount: int
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'create_capacity_reservation_fleet' function.
class CreateCapacityReservationFleetRequest(BaseValidatorModel):
    InstanceTypeSpecifications: List[ReservationFleetInstanceSpecification]
    TotalTargetCapacity: int
    AllocationStrategy: Optional[str] = None
    ClientToken: Optional[str] = None
    Tenancy: Optional[Literal['default']] = None
    EndDate: Optional[Timestamp] = None
    InstanceMatchCriteria: Optional[Literal['open']] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_capacity_reservation' function.
class CreateCapacityReservationRequest(BaseValidatorModel):
    InstanceType: str
    InstancePlatform: CapacityReservationInstancePlatformType
    InstanceCount: int
    ClientToken: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Tenancy: Optional[CapacityReservationTenancyType] = None
    EbsOptimized: Optional[bool] = None
    EphemeralStorage: Optional[bool] = None
    EndDate: Optional[Timestamp] = None
    EndDateType: Optional[EndDateTypeType] = None
    InstanceMatchCriteria: Optional[InstanceMatchCriteriaType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    OutpostArn: Optional[str] = None
    PlacementGroupArn: Optional[str] = None
    StartDate: Optional[Timestamp] = None
    CommitmentDuration: Optional[int] = None
    DeliveryPreference: Optional[CapacityReservationDeliveryPreferenceType] = None


# This class is the input for the 'create_carrier_gateway' function.
class CreateCarrierGatewayRequest(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_client_vpn_endpoint' function.
class CreateClientVpnEndpointRequest(BaseValidatorModel):
    ClientCidrBlock: str
    ServerCertificateArn: str
    AuthenticationOptions: List[ClientVpnAuthenticationRequest]
    ConnectionLogOptions: ConnectionLogOptions
    DnsServers: Optional[List[str]] = None
    TransportProtocol: Optional[TransportProtocolType] = None
    VpnPort: Optional[int] = None
    Description: Optional[str] = None
    SplitTunnel: Optional[bool] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    SecurityGroupIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortal: Optional[SelfServicePortalType] = None
    ClientConnectOptions: Optional[ClientConnectOptions] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ClientLoginBannerOptions] = None
    DisconnectOnSessionTimeout: Optional[bool] = None


# This class is the input for the 'create_coip_pool' function.
class CreateCoipPoolRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_customer_gateway' function.
class CreateCustomerGatewayRequest(BaseValidatorModel):
    Type: Literal['ipsec.1']
    BgpAsn: Optional[int] = None
    PublicIp: Optional[str] = None
    CertificateArn: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DeviceName: Optional[str] = None
    IpAddress: Optional[str] = None
    BgpAsnExtended: Optional[int] = None
    DryRun: Optional[bool] = None


class CreateDhcpOptionsRequestServiceResourceCreateDhcpOptions(BaseValidatorModel):
    DhcpConfigurations: List[NewDhcpConfiguration]
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_dhcp_options' function.
class CreateDhcpOptionsRequest(BaseValidatorModel):
    DhcpConfigurations: List[NewDhcpConfiguration]
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_egress_only_internet_gateway' function.
class CreateEgressOnlyInternetGatewayRequest(BaseValidatorModel):
    VpcId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'create_flow_logs' function.
class CreateFlowLogsRequest(BaseValidatorModel):
    ResourceIds: List[str]
    ResourceType: FlowLogsResourceTypeType
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    DeliverLogsPermissionArn: Optional[str] = None
    DeliverCrossAccountRole: Optional[str] = None
    LogGroupName: Optional[str] = None
    TrafficType: Optional[TrafficTypeType] = None
    LogDestinationType: Optional[LogDestinationTypeType] = None
    LogDestination: Optional[str] = None
    LogFormat: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    MaxAggregationInterval: Optional[int] = None
    DestinationOptions: Optional[DestinationOptionsRequest] = None


# This class is the input for the 'create_fpga_image' function.
class CreateFpgaImageRequest(BaseValidatorModel):
    InputStorageLocation: StorageLocation
    DryRun: Optional[bool] = None
    LogsStorageLocation: Optional[StorageLocation] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


class CreateImageRequestInstanceCreateImage(BaseValidatorModel):
    Name: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    NoReboot: Optional[bool] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None


# This class is the input for the 'create_image' function.
class CreateImageRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    NoReboot: Optional[bool] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None


# This class is the input for the 'create_instance_connect_endpoint' function.
class CreateInstanceConnectEndpointRequest(BaseValidatorModel):
    SubnetId: str
    DryRun: Optional[bool] = None
    SecurityGroupIds: Optional[List[str]] = None
    PreserveClientIp: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'create_instance_event_window' function.
class CreateInstanceEventWindowRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Name: Optional[str] = None
    TimeRanges: Optional[List[InstanceEventWindowTimeRangeRequest]] = None
    CronExpression: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'create_instance_export_task' function.
class CreateInstanceExportTaskRequest(BaseValidatorModel):
    InstanceId: str
    TargetEnvironment: ExportEnvironmentType
    ExportToS3Task: ExportToS3TaskSpecification
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    Description: Optional[str] = None


class CreateInternetGatewayRequestServiceResourceCreateInternetGateway(BaseValidatorModel):
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_internet_gateway' function.
class CreateInternetGatewayRequest(BaseValidatorModel):
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_ipam_external_resource_verification_token' function.
class CreateIpamExternalResourceVerificationTokenRequest(BaseValidatorModel):
    IpamId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_ipam_pool' function.
class CreateIpamPoolRequest(BaseValidatorModel):
    IpamScopeId: str
    AddressFamily: AddressFamilyType
    DryRun: Optional[bool] = None
    Locale: Optional[str] = None
    SourceIpamPoolId: Optional[str] = None
    Description: Optional[str] = None
    AutoImport: Optional[bool] = None
    PubliclyAdvertisable: Optional[bool] = None
    AllocationMinNetmaskLength: Optional[int] = None
    AllocationMaxNetmaskLength: Optional[int] = None
    AllocationDefaultNetmaskLength: Optional[int] = None
    AllocationResourceTags: Optional[List[RequestIpamResourceTag]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    AwsService: Optional[Literal['ec2']] = None
    PublicIpSource: Optional[IpamPoolPublicIpSourceType] = None
    SourceResource: Optional[IpamPoolSourceResourceRequest] = None


# This class is the input for the 'create_ipam' function.
class CreateIpamRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[List[AddIpamOperatingRegion]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    Tier: Optional[IpamTierType] = None
    EnablePrivateGua: Optional[bool] = None


# This class is the input for the 'create_ipam_resource_discovery' function.
class CreateIpamResourceDiscoveryRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[List[AddIpamOperatingRegion]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_ipam_scope' function.
class CreateIpamScopeRequest(BaseValidatorModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None


class CreateKeyPairRequestServiceResourceCreateKeyPair(BaseValidatorModel):
    KeyName: str
    KeyType: Optional[KeyTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    KeyFormat: Optional[KeyFormatType] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_key_pair' function.
class CreateKeyPairRequest(BaseValidatorModel):
    KeyName: str
    KeyType: Optional[KeyTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    KeyFormat: Optional[KeyFormatType] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_local_gateway_route_table' function.
class CreateLocalGatewayRouteTableRequest(BaseValidatorModel):
    LocalGatewayId: str
    Mode: Optional[LocalGatewayRouteTableModeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    LocalGatewayVirtualInterfaceGroupId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_local_gateway_route_table_vpc_association' function.
class CreateLocalGatewayRouteTableVpcAssociationRequest(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_managed_prefix_list' function.
class CreateManagedPrefixListRequest(BaseValidatorModel):
    PrefixListName: str
    MaxEntries: int
    AddressFamily: str
    DryRun: Optional[bool] = None
    Entries: Optional[List[AddPrefixListEntry]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_nat_gateway' function.
class CreateNatGatewayRequest(BaseValidatorModel):
    SubnetId: str
    AllocationId: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ConnectivityType: Optional[ConnectivityTypeType] = None
    PrivateIpAddress: Optional[str] = None
    SecondaryAllocationIds: Optional[List[str]] = None
    SecondaryPrivateIpAddresses: Optional[List[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None


class CreateNetworkAclRequestServiceResourceCreateNetworkAcl(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_network_acl' function.
class CreateNetworkAclRequest(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


class CreateNetworkAclRequestVpcCreateNetworkAcl(BaseValidatorModel):
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_network_insights_path' function.
class CreateNetworkInsightsPathRequest(BaseValidatorModel):
    Source: str
    Protocol: ProtocolType
    ClientToken: str
    SourceIp: Optional[str] = None
    DestinationIp: Optional[str] = None
    Destination: Optional[str] = None
    DestinationPort: Optional[int] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    FilterAtSource: Optional[PathRequestFilter] = None
    FilterAtDestination: Optional[PathRequestFilter] = None


class CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterface(BaseValidatorModel):
    SubnetId: str
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequest]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequest]] = None
    Ipv6PrefixCount: Optional[int] = None
    InterfaceType: Optional[NetworkInterfaceCreationTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None
    Operator: Optional[OperatorRequest] = None
    Description: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    Groups: Optional[List[str]] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecification]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    Ipv6AddressCount: Optional[int] = None
    DryRun: Optional[bool] = None


class CreateNetworkInterfaceRequestSubnetCreateNetworkInterface(BaseValidatorModel):
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequest]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequest]] = None
    Ipv6PrefixCount: Optional[int] = None
    InterfaceType: Optional[NetworkInterfaceCreationTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None
    Operator: Optional[OperatorRequest] = None
    Description: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    Groups: Optional[List[str]] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecification]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    Ipv6AddressCount: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_network_interface' function.
class CreateNetworkInterfaceRequest(BaseValidatorModel):
    SubnetId: str
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequest]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequest]] = None
    Ipv6PrefixCount: Optional[int] = None
    InterfaceType: Optional[NetworkInterfaceCreationTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationRequest] = None
    Operator: Optional[OperatorRequest] = None
    Description: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    Groups: Optional[List[str]] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecification]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    Ipv6AddressCount: Optional[int] = None
    DryRun: Optional[bool] = None


class CreatePlacementGroupRequestServiceResourceCreatePlacementGroup(BaseValidatorModel):
    PartitionCount: Optional[int] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    SpreadLevel: Optional[SpreadLevelType] = None
    DryRun: Optional[bool] = None
    GroupName: Optional[str] = None
    Strategy: Optional[PlacementStrategyType] = None


# This class is the input for the 'create_placement_group' function.
class CreatePlacementGroupRequest(BaseValidatorModel):
    PartitionCount: Optional[int] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    SpreadLevel: Optional[SpreadLevelType] = None
    DryRun: Optional[bool] = None
    GroupName: Optional[str] = None
    Strategy: Optional[PlacementStrategyType] = None


# This class is the input for the 'create_public_ipv4_pool' function.
class CreatePublicIpv4PoolRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    NetworkBorderGroup: Optional[str] = None


# This class is the input for the 'create_replace_root_volume_task' function.
class CreateReplaceRootVolumeTaskRequest(BaseValidatorModel):
    InstanceId: str
    SnapshotId: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ImageId: Optional[str] = None
    DeleteReplacedRootVolume: Optional[bool] = None


# This class is the input for the 'create_restore_image_task' function.
class CreateRestoreImageTaskRequest(BaseValidatorModel):
    Bucket: str
    ObjectKey: str
    Name: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


class CreateRouteTableRequestServiceResourceCreateRouteTable(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_route_table' function.
class CreateRouteTableRequest(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


class CreateRouteTableRequestVpcCreateRouteTable(BaseValidatorModel):
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None


class CreateSecurityGroupRequestServiceResourceCreateSecurityGroup(BaseValidatorModel):
    Description: str
    GroupName: str
    VpcId: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_security_group' function.
class CreateSecurityGroupRequest(BaseValidatorModel):
    Description: str
    GroupName: str
    VpcId: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


class CreateSecurityGroupRequestVpcCreateSecurityGroup(BaseValidatorModel):
    Description: str
    GroupName: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


class CreateSnapshotRequestServiceResourceCreateSnapshot(BaseValidatorModel):
    VolumeId: str
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    Location: Optional[SnapshotLocationEnumType] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_snapshot' function.
class CreateSnapshotRequest(BaseValidatorModel):
    VolumeId: str
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    Location: Optional[SnapshotLocationEnumType] = None
    DryRun: Optional[bool] = None


class CreateSnapshotRequestVolumeCreateSnapshot(BaseValidatorModel):
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    Location: Optional[SnapshotLocationEnumType] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_snapshots' function.
class CreateSnapshotsRequest(BaseValidatorModel):
    InstanceSpecification: InstanceSpecification
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    CopyTagsFromSource: Optional[Literal['volume']] = None
    Location: Optional[SnapshotLocationEnumType] = None


# This class is the input for the 'create_subnet_cidr_reservation' function.
class CreateSubnetCidrReservationRequest(BaseValidatorModel):
    SubnetId: str
    Cidr: str
    ReservationType: SubnetCidrReservationTypeType
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


class CreateSubnetRequestServiceResourceCreateSubnet(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    OutpostArn: Optional[str] = None
    Ipv6Native: Optional[bool] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_subnet' function.
class CreateSubnetRequest(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    OutpostArn: Optional[str] = None
    Ipv6Native: Optional[bool] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    DryRun: Optional[bool] = None


class CreateSubnetRequestVpcCreateSubnet(BaseValidatorModel):
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    OutpostArn: Optional[str] = None
    Ipv6Native: Optional[bool] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_traffic_mirror_filter' function.
class CreateTrafficMirrorFilterRequest(BaseValidatorModel):
    Description: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_traffic_mirror_filter_rule' function.
class CreateTrafficMirrorFilterRuleRequest(BaseValidatorModel):
    TrafficMirrorFilterId: str
    TrafficDirection: TrafficDirectionType
    RuleNumber: int
    RuleAction: TrafficMirrorRuleActionType
    DestinationCidrBlock: str
    SourceCidrBlock: str
    DestinationPortRange: Optional[TrafficMirrorPortRangeRequest] = None
    SourcePortRange: Optional[TrafficMirrorPortRangeRequest] = None
    Protocol: Optional[int] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'create_traffic_mirror_session' function.
class CreateTrafficMirrorSessionRequest(BaseValidatorModel):
    NetworkInterfaceId: str
    TrafficMirrorTargetId: str
    TrafficMirrorFilterId: str
    SessionNumber: int
    PacketLength: Optional[int] = None
    VirtualNetworkId: Optional[int] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_traffic_mirror_target' function.
class CreateTrafficMirrorTargetRequest(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    NetworkLoadBalancerArn: Optional[str] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    GatewayLoadBalancerEndpointId: Optional[str] = None


# This class is the input for the 'create_transit_gateway_connect_peer' function.
class CreateTransitGatewayConnectPeerRequest(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    PeerAddress: str
    InsideCidrBlocks: List[str]
    TransitGatewayAddress: Optional[str] = None
    BgpOptions: Optional[TransitGatewayConnectRequestBgpOptions] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway_connect' function.
class CreateTransitGatewayConnectRequest(BaseValidatorModel):
    TransportTransitGatewayAttachmentId: str
    Options: CreateTransitGatewayConnectRequestOptions
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway_multicast_domain' function.
class CreateTransitGatewayMulticastDomainRequest(BaseValidatorModel):
    TransitGatewayId: str
    Options: Optional[CreateTransitGatewayMulticastDomainRequestOptions] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway_peering_attachment' function.
class CreateTransitGatewayPeeringAttachmentRequest(BaseValidatorModel):
    TransitGatewayId: str
    PeerTransitGatewayId: str
    PeerAccountId: str
    PeerRegion: str
    Options: Optional[CreateTransitGatewayPeeringAttachmentRequestOptions] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway_policy_table' function.
class CreateTransitGatewayPolicyTableRequest(BaseValidatorModel):
    TransitGatewayId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway' function.
class CreateTransitGatewayRequest(BaseValidatorModel):
    Description: Optional[str] = None
    Options: Optional[TransitGatewayRequestOptions] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway_route_table_announcement' function.
class CreateTransitGatewayRouteTableAnnouncementRequest(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PeeringAttachmentId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway_route_table' function.
class CreateTransitGatewayRouteTableRequest(BaseValidatorModel):
    TransitGatewayId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_transit_gateway_vpc_attachment' function.
class CreateTransitGatewayVpcAttachmentRequest(BaseValidatorModel):
    TransitGatewayId: str
    VpcId: str
    SubnetIds: List[str]
    Options: Optional[CreateTransitGatewayVpcAttachmentRequestOptions] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_verified_access_endpoint' function.
class CreateVerifiedAccessEndpointRequest(BaseValidatorModel):
    VerifiedAccessGroupId: str
    EndpointType: VerifiedAccessEndpointTypeType
    AttachmentType: Literal['vpc']
    DomainCertificateArn: Optional[str] = None
    ApplicationDomain: Optional[str] = None
    EndpointDomainPrefix: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    LoadBalancerOptions: Optional[CreateVerifiedAccessEndpointLoadBalancerOptions] = None
    NetworkInterfaceOptions: Optional[CreateVerifiedAccessEndpointEniOptions] = None
    Description: Optional[str] = None
    PolicyDocument: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequest] = None
    RdsOptions: Optional[CreateVerifiedAccessEndpointRdsOptions] = None
    CidrOptions: Optional[CreateVerifiedAccessEndpointCidrOptions] = None


# This class is the input for the 'create_verified_access_group' function.
class CreateVerifiedAccessGroupRequest(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    Description: Optional[str] = None
    PolicyDocument: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequest] = None


# This class is the input for the 'create_verified_access_instance' function.
class CreateVerifiedAccessInstanceRequest(BaseValidatorModel):
    Description: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    FIPSEnabled: Optional[bool] = None
    CidrEndpointsCustomSubDomain: Optional[str] = None


# This class is the input for the 'create_verified_access_trust_provider' function.
class CreateVerifiedAccessTrustProviderRequest(BaseValidatorModel):
    TrustProviderType: TrustProviderTypeType
    PolicyReferenceName: str
    UserTrustProviderType: Optional[UserTrustProviderTypeType] = None
    DeviceTrustProviderType: Optional[DeviceTrustProviderTypeType] = None
    OidcOptions: Optional[CreateVerifiedAccessTrustProviderOidcOptions] = None
    DeviceOptions: Optional[CreateVerifiedAccessTrustProviderDeviceOptions] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequest] = None
    NativeApplicationOidcOptions: Optional[CreateVerifiedAccessNativeApplicationOidcOptions] = None


class CreateVolumeRequestServiceResourceCreateVolume(BaseValidatorModel):
    AvailabilityZone: str
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    OutpostArn: Optional[str] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    MultiAttachEnabled: Optional[bool] = None
    Throughput: Optional[int] = None
    ClientToken: Optional[str] = None
    Operator: Optional[OperatorRequest] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_volume' function.
class CreateVolumeRequest(BaseValidatorModel):
    AvailabilityZone: str
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    OutpostArn: Optional[str] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    MultiAttachEnabled: Optional[bool] = None
    Throughput: Optional[int] = None
    ClientToken: Optional[str] = None
    Operator: Optional[OperatorRequest] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'create_vpc_block_public_access_exclusion' function.
class CreateVpcBlockPublicAccessExclusionRequest(BaseValidatorModel):
    InternetGatewayExclusionMode: InternetGatewayExclusionModeType
    DryRun: Optional[bool] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'create_vpc_endpoint' function.
class CreateVpcEndpointRequest(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    VpcEndpointType: Optional[VpcEndpointTypeType] = None
    ServiceName: Optional[str] = None
    PolicyDocument: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DnsOptions: Optional[DnsOptionsSpecification] = None
    ClientToken: Optional[str] = None
    PrivateDnsEnabled: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    SubnetConfigurations: Optional[List[SubnetConfiguration]] = None
    ServiceNetworkArn: Optional[str] = None
    ResourceConfigurationArn: Optional[str] = None
    ServiceRegion: Optional[str] = None


# This class is the input for the 'create_vpc_endpoint_service_configuration' function.
class CreateVpcEndpointServiceConfigurationRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    AcceptanceRequired: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    SupportedIpAddressTypes: Optional[List[str]] = None
    SupportedRegions: Optional[List[str]] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


class CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnection(BaseValidatorModel):
    VpcId: str
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    PeerVpcId: Optional[str] = None
    PeerOwnerId: Optional[str] = None


# This class is the input for the 'create_vpc_peering_connection' function.
class CreateVpcPeeringConnectionRequest(BaseValidatorModel):
    VpcId: str
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    PeerVpcId: Optional[str] = None
    PeerOwnerId: Optional[str] = None


class CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnection(BaseValidatorModel):
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    PeerVpcId: Optional[str] = None
    PeerOwnerId: Optional[str] = None


class CreateVpcRequestServiceResourceCreateVpc(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Ipv6Pool: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    Ipv6CidrBlockNetworkBorderGroup: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    InstanceTenancy: Optional[TenancyType] = None
    AmazonProvidedIpv6CidrBlock: Optional[bool] = None


# This class is the input for the 'create_vpc' function.
class CreateVpcRequest(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Ipv6Pool: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    Ipv6CidrBlockNetworkBorderGroup: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    InstanceTenancy: Optional[TenancyType] = None
    AmazonProvidedIpv6CidrBlock: Optional[bool] = None


# This class is the input for the 'create_vpn_gateway' function.
class CreateVpnGatewayRequest(BaseValidatorModel):
    Type: Literal['ipsec.1']
    AvailabilityZone: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    AmazonSideAsn: Optional[int] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'export_image' function.
class ExportImageRequest(BaseValidatorModel):
    DiskImageFormat: DiskImageFormatType
    ImageId: str
    S3ExportLocation: ExportTaskS3LocationRequest
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    RoleName: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'import_image' function.
class ImportImageRequest(BaseValidatorModel):
    Architecture: Optional[str] = None
    ClientData: Optional[ClientData] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DiskContainers: Optional[List[ImageDiskContainer]] = None
    DryRun: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Hypervisor: Optional[str] = None
    KmsKeyId: Optional[str] = None
    LicenseType: Optional[str] = None
    Platform: Optional[str] = None
    RoleName: Optional[str] = None
    LicenseSpecifications: Optional[List[ImportImageLicenseConfigurationRequest]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    UsageOperation: Optional[str] = None
    BootMode: Optional[BootModeValuesType] = None


class ImportKeyPairRequestServiceResourceImportKeyPair(BaseValidatorModel):
    KeyName: str
    PublicKeyMaterial: Blob
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'import_key_pair' function.
class ImportKeyPairRequest(BaseValidatorModel):
    KeyName: str
    PublicKeyMaterial: Blob
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'import_snapshot' function.
class ImportSnapshotRequest(BaseValidatorModel):
    ClientData: Optional[ClientData] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DiskContainer: Optional[SnapshotDiskContainer] = None
    DryRun: Optional[bool] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    RoleName: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'provision_byoip_cidr' function.
class ProvisionByoipCidrRequest(BaseValidatorModel):
    Cidr: str
    CidrAuthorizationContext: Optional[CidrAuthorizationContext] = None
    PubliclyAdvertisable: Optional[bool] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    PoolTagSpecifications: Optional[List[TagSpecificationUnion]] = None
    MultiRegion: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None


# This class is the input for the 'purchase_capacity_block' function.
class PurchaseCapacityBlockRequest(BaseValidatorModel):
    CapacityBlockOfferingId: str
    InstancePlatform: CapacityReservationInstancePlatformType
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'purchase_host_reservation' function.
class PurchaseHostReservationRequest(BaseValidatorModel):
    HostIdSet: List[str]
    OfferingId: str
    ClientToken: Optional[str] = None
    CurrencyCode: Optional[Literal['USD']] = None
    LimitPrice: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


class RegisterImageRequestServiceResourceRegisterImage(BaseValidatorModel):
    Name: str
    ImageLocation: Optional[str] = None
    BillingProducts: Optional[List[str]] = None
    BootMode: Optional[BootModeValuesType] = None
    TpmSupport: Optional[Literal['v2.0']] = None
    UefiData: Optional[str] = None
    ImdsSupport: Optional[Literal['v2.0']] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    Architecture: Optional[ArchitectureValuesType] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    RootDeviceName: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    VirtualizationType: Optional[str] = None
    SriovNetSupport: Optional[str] = None
    EnaSupport: Optional[bool] = None


# This class is the input for the 'register_image' function.
class RegisterImageRequest(BaseValidatorModel):
    Name: str
    ImageLocation: Optional[str] = None
    BillingProducts: Optional[List[str]] = None
    BootMode: Optional[BootModeValuesType] = None
    TpmSupport: Optional[Literal['v2.0']] = None
    UefiData: Optional[str] = None
    ImdsSupport: Optional[Literal['v2.0']] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    Architecture: Optional[ArchitectureValuesType] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    RootDeviceName: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    VirtualizationType: Optional[str] = None
    SriovNetSupport: Optional[str] = None
    EnaSupport: Optional[bool] = None


# This class is the input for the 'start_declarative_policies_report' function.
class StartDeclarativePoliciesReportRequest(BaseValidatorModel):
    S3Bucket: str
    TargetId: str
    DryRun: Optional[bool] = None
    S3Prefix: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'start_network_insights_access_scope_analysis' function.
class StartNetworkInsightsAccessScopeAnalysisRequest(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    ClientToken: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'start_network_insights_analysis' function.
class StartNetworkInsightsAnalysisRequest(BaseValidatorModel):
    NetworkInsightsPathId: str
    ClientToken: str
    AdditionalAccounts: Optional[List[str]] = None
    FilterInArns: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


class PathComponent(BaseValidatorModel):
    SequenceNumber: Optional[int] = None
    AclRule: Optional[AnalysisAclRule] = None
    AttachedTo: Optional[AnalysisComponent] = None
    Component: Optional[AnalysisComponent] = None
    DestinationVpc: Optional[AnalysisComponent] = None
    OutboundHeader: Optional[AnalysisPacketHeader] = None
    InboundHeader: Optional[AnalysisPacketHeader] = None
    RouteTableRoute: Optional[AnalysisRouteTableRoute] = None
    SecurityGroupRule: Optional[AnalysisSecurityGroupRule] = None
    SourceVpc: Optional[AnalysisComponent] = None
    Subnet: Optional[AnalysisComponent] = None
    Vpc: Optional[AnalysisComponent] = None
    AdditionalDetails: Optional[List[AdditionalDetail]] = None
    TransitGateway: Optional[AnalysisComponent] = None
    TransitGatewayRouteTableRoute: Optional[TransitGatewayRouteTableRoute] = None
    Explanations: Optional[List[Explanation]] = None
    ElasticLoadBalancerListener: Optional[AnalysisComponent] = None
    FirewallStatelessRule: Optional[FirewallStatelessRule] = None
    FirewallStatefulRule: Optional[FirewallStatefulRule] = None
    ServiceName: Optional[str] = None


# This class is the output for the 'create_route_table' function.
class CreateRouteTableResult(BaseValidatorModel):
    RouteTable: RouteTable
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_route_tables' function.
class DescribeRouteTablesResult(BaseValidatorModel):
    RouteTables: List[RouteTable]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'get_flow_logs_integration_template' function.
class GetFlowLogsIntegrationTemplateRequest(BaseValidatorModel):
    FlowLogId: str
    ConfigDeliveryS3DestinationArn: str
    IntegrateServices: IntegrateServices
    DryRun: Optional[bool] = None


# This class is the output for the 'describe_network_interface_attribute' function.
class DescribeNetworkInterfaceAttributeResult(BaseValidatorModel):
    Attachment: NetworkInterfaceAttachment
    Description: AttributeValue
    Groups: List[GroupIdentifier]
    NetworkInterfaceId: str
    SourceDestCheck: AttributeBooleanValue
    AssociatePublicIpAddress: bool
    ResponseMetadata: ResponseMetadata


class NetworkInterface(BaseValidatorModel):
    Association: Optional[NetworkInterfaceAssociation] = None
    Attachment: Optional[NetworkInterfaceAttachment] = None
    AvailabilityZone: Optional[str] = None
    ConnectionTrackingConfiguration: Optional[ConnectionTrackingConfiguration] = None
    Description: Optional[str] = None
    Groups: Optional[List[GroupIdentifier]] = None
    InterfaceType: Optional[NetworkInterfaceTypeType] = None
    Ipv6Addresses: Optional[List[NetworkInterfaceIpv6Address]] = None
    MacAddress: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[NetworkInterfacePrivateIpAddress]] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecification]] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecification]] = None
    RequesterId: Optional[str] = None
    RequesterManaged: Optional[bool] = None
    SourceDestCheck: Optional[bool] = None
    Status: Optional[NetworkInterfaceStatusType] = None
    SubnetId: Optional[str] = None
    TagSet: Optional[List[Tag]] = None
    VpcId: Optional[str] = None
    DenyAllIgwTraffic: Optional[bool] = None
    Ipv6Native: Optional[bool] = None
    Ipv6Address: Optional[str] = None
    Operator: Optional[OperatorResponse] = None


# This class is the output for the 'create_dhcp_options' function.
class CreateDhcpOptionsResult(BaseValidatorModel):
    DhcpOptions: DhcpOptions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_dhcp_options' function.
class DescribeDhcpOptionsResult(BaseValidatorModel):
    DhcpOptions: List[DhcpOptions]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_hosts' function.
class DescribeHostsResult(BaseValidatorModel):
    Hosts: List[Host]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

StorageUnion = Union[Storage, StorageOutput]


# This class is the output for the 'describe_images' function.
class DescribeImagesResult(BaseValidatorModel):
    Images: List[Image]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_client_vpn_endpoints' function.
class DescribeClientVpnEndpointsResult(BaseValidatorModel):
    ClientVpnEndpoints: List[ClientVpnEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'modify_vpn_tunnel_options' function.
class ModifyVpnTunnelOptionsRequest(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    TunnelOptions: ModifyVpnTunnelOptionsSpecification
    DryRun: Optional[bool] = None
    SkipTunnelReplacement: Optional[bool] = None


class VpnConnectionOptionsSpecification(BaseValidatorModel):
    EnableAcceleration: Optional[bool] = None
    TunnelInsideIpVersion: Optional[TunnelInsideIpVersionType] = None
    TunnelOptions: Optional[List[VpnTunnelOptionsSpecification]] = None
    LocalIpv4NetworkCidr: Optional[str] = None
    RemoteIpv4NetworkCidr: Optional[str] = None
    LocalIpv6NetworkCidr: Optional[str] = None
    RemoteIpv6NetworkCidr: Optional[str] = None
    OutsideIpAddressType: Optional[str] = None
    TransportTransitGatewayAttachmentId: Optional[str] = None
    StaticRoutesOnly: Optional[bool] = None


class VpnConnectionOptions(BaseValidatorModel):
    EnableAcceleration: Optional[bool] = None
    StaticRoutesOnly: Optional[bool] = None
    LocalIpv4NetworkCidr: Optional[str] = None
    RemoteIpv4NetworkCidr: Optional[str] = None
    LocalIpv6NetworkCidr: Optional[str] = None
    RemoteIpv6NetworkCidr: Optional[str] = None
    OutsideIpAddressType: Optional[str] = None
    TransportTransitGatewayAttachmentId: Optional[str] = None
    TunnelInsideIpVersion: Optional[TunnelInsideIpVersionType] = None
    TunnelOptions: Optional[List[TunnelOption]] = None


class InstanceRequirementsOutput(BaseValidatorModel):
    VCpuCount: Optional[VCpuCountRange] = None
    MemoryMiB: Optional[MemoryMiB] = None
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpu] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCount] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGB] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbps] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCount] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiB] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbps] = None
    AllowedInstanceTypes: Optional[List[str]] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsOutput] = None


class BaselinePerformanceFactors(BaseValidatorModel):
    Cpu: Optional[CpuPerformanceFactorUnion] = None


class InstanceRequirementsRequest(BaseValidatorModel):
    VCpuCount: VCpuCountRangeRequest
    MemoryMiB: MemoryMiBRequest
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequest] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequest] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequest] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequest] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountRequest] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequest] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequest] = None
    AllowedInstanceTypes: Optional[List[str]] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsRequest] = None


# This class is the output for the 'create_network_acl' function.
class CreateNetworkAclResult(BaseValidatorModel):
    NetworkAcl: NetworkAcl
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_network_acls' function.
class DescribeNetworkAclsResult(BaseValidatorModel):
    NetworkAcls: List[NetworkAcl]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'disable_fast_snapshot_restores' function.
class DisableFastSnapshotRestoresResult(BaseValidatorModel):
    Successful: List[DisableFastSnapshotRestoreSuccessItem]
    Unsuccessful: List[DisableFastSnapshotRestoreErrorItem]
    ResponseMetadata: ResponseMetadata


class ConversionTask(BaseValidatorModel):
    ConversionTaskId: Optional[str] = None
    ExpirationTime: Optional[str] = None
    ImportInstance: Optional[ImportInstanceTaskDetails] = None
    ImportVolume: Optional[ImportVolumeTaskDetails] = None
    State: Optional[ConversionTaskStateType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_instance_attribute' function.
class InstanceAttribute(BaseValidatorModel):
    BlockDeviceMappings: List[InstanceBlockDeviceMapping]
    DisableApiTermination: AttributeBooleanValue
    EnaSupport: AttributeBooleanValue
    EnclaveOptions: EnclaveOptions
    EbsOptimized: AttributeBooleanValue
    InstanceId: str
    InstanceInitiatedShutdownBehavior: AttributeValue
    InstanceType: AttributeValue
    KernelId: AttributeValue
    ProductCodes: List[ProductCode]
    RamdiskId: AttributeValue
    RootDeviceName: AttributeValue
    SourceDestCheck: AttributeBooleanValue
    SriovNetSupport: AttributeValue
    UserData: AttributeValue
    DisableApiStop: AttributeBooleanValue
    Groups: List[GroupIdentifier]
    ResponseMetadata: ResponseMetadata


class LaunchSpecification(BaseValidatorModel):
    UserData: Optional[str] = None
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecification] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationOutput]] = None
    Placement: Optional[SpotPlacement] = None
    RamdiskId: Optional[str] = None
    SubnetId: Optional[str] = None
    SecurityGroups: Optional[List[GroupIdentifier]] = None
    Monitoring: Optional[RunInstancesMonitoringEnabled] = None

InstanceNetworkInterfaceSpecificationUnion = Union[InstanceNetworkInterfaceSpecification, InstanceNetworkInterfaceSpecificationOutput]


# This class is the output for the 'enable_fast_snapshot_restores' function.
class EnableFastSnapshotRestoresResult(BaseValidatorModel):
    Successful: List[EnableFastSnapshotRestoreSuccessItem]
    Unsuccessful: List[EnableFastSnapshotRestoreErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_network_insights_path' function.
class CreateNetworkInsightsPathResult(BaseValidatorModel):
    NetworkInsightsPath: NetworkInsightsPath
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_network_insights_paths' function.
class DescribeNetworkInsightsPathsResult(BaseValidatorModel):
    NetworkInsightsPaths: List[NetworkInsightsPath]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InstanceNetworkInterface(BaseValidatorModel):
    Association: Optional[InstanceNetworkInterfaceAssociation] = None
    Attachment: Optional[InstanceNetworkInterfaceAttachment] = None
    Description: Optional[str] = None
    Groups: Optional[List[GroupIdentifier]] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    MacAddress: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    OwnerId: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[InstancePrivateIpAddress]] = None
    SourceDestCheck: Optional[bool] = None
    Status: Optional[NetworkInterfaceStatusType] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    InterfaceType: Optional[str] = None
    Ipv4Prefixes: Optional[List[InstanceIpv4Prefix]] = None
    Ipv6Prefixes: Optional[List[InstanceIpv6Prefix]] = None
    ConnectionTrackingConfiguration: Optional[ConnectionTrackingSpecificationResponse] = None
    Operator: Optional[OperatorResponse] = None


# This class is the output for the 'describe_instance_status' function.
class DescribeInstanceStatusResult(BaseValidatorModel):
    InstanceStatuses: List[InstanceStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_security_groups' function.
class DescribeSecurityGroupsResult(BaseValidatorModel):
    SecurityGroups: List[SecurityGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgress(BaseValidatorModel):
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIp: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None


# This class is the input for the 'authorize_security_group_egress' function.
class AuthorizeSecurityGroupEgressRequest(BaseValidatorModel):
    GroupId: str
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIp: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None


class AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngress(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'authorize_security_group_ingress' function.
class AuthorizeSecurityGroupIngressRequest(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


class RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgress(BaseValidatorModel):
    SecurityGroupRuleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIp: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None


# This class is the input for the 'revoke_security_group_egress' function.
class RevokeSecurityGroupEgressRequest(BaseValidatorModel):
    GroupId: str
    SecurityGroupRuleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIp: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None


class RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngress(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    SecurityGroupRuleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'revoke_security_group_ingress' function.
class RevokeSecurityGroupIngressRequest(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    SecurityGroupRuleIds: Optional[List[str]] = None
    DryRun: Optional[bool] = None


# This class is the input for the 'update_security_group_rule_descriptions_egress' function.
class UpdateSecurityGroupRuleDescriptionsEgressRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None
    SecurityGroupRuleDescriptions: Optional[List[SecurityGroupRuleDescription]] = None


# This class is the input for the 'update_security_group_rule_descriptions_ingress' function.
class UpdateSecurityGroupRuleDescriptionsIngressRequest(BaseValidatorModel):
    DryRun: Optional[bool] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionUnion]] = None
    SecurityGroupRuleDescriptions: Optional[List[SecurityGroupRuleDescription]] = None


# This class is the output for the 'describe_stale_security_groups' function.
class DescribeStaleSecurityGroupsResult(BaseValidatorModel):
    StaleSecurityGroupSet: List[StaleSecurityGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_ipam_discovered_public_addresses' function.
class GetIpamDiscoveredPublicAddressesResult(BaseValidatorModel):
    IpamDiscoveredPublicAddresses: List[IpamDiscoveredPublicAddress]
    OldestSampleTime: datetime
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_reserved_instances_modifications' function.
class DescribeReservedInstancesModificationsResult(BaseValidatorModel):
    ReservedInstancesModifications: List[ReservedInstancesModification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InstanceTypeInfo(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    CurrentGeneration: Optional[bool] = None
    FreeTierEligible: Optional[bool] = None
    SupportedUsageClasses: Optional[List[UsageClassTypeType]] = None
    SupportedRootDeviceTypes: Optional[List[RootDeviceTypeType]] = None
    SupportedVirtualizationTypes: Optional[List[VirtualizationTypeType]] = None
    BareMetal: Optional[bool] = None
    Hypervisor: Optional[InstanceTypeHypervisorType] = None
    ProcessorInfo: Optional[ProcessorInfo] = None
    VCpuInfo: Optional[VCpuInfo] = None
    MemoryInfo: Optional[MemoryInfo] = None
    InstanceStorageSupported: Optional[bool] = None
    InstanceStorageInfo: Optional[InstanceStorageInfo] = None
    EbsInfo: Optional[EbsInfo] = None
    NetworkInfo: Optional[NetworkInfo] = None
    GpuInfo: Optional[GpuInfo] = None
    FpgaInfo: Optional[FpgaInfo] = None
    PlacementGroupInfo: Optional[PlacementGroupInfo] = None
    InferenceAcceleratorInfo: Optional[InferenceAcceleratorInfo] = None
    HibernationSupported: Optional[bool] = None
    BurstablePerformanceSupported: Optional[bool] = None
    DedicatedHostsSupported: Optional[bool] = None
    AutoRecoverySupported: Optional[bool] = None
    SupportedBootModes: Optional[List[BootModeTypeType]] = None
    NitroEnclavesSupport: Optional[NitroEnclavesSupportType] = None
    NitroTpmSupport: Optional[NitroTpmSupportType] = None
    NitroTpmInfo: Optional[NitroTpmInfo] = None
    MediaAcceleratorInfo: Optional[MediaAcceleratorInfo] = None
    NeuronInfo: Optional[NeuronInfo] = None
    PhcSupport: Optional[PhcSupportType] = None


# This class is the input for the 'create_network_insights_access_scope' function.
class CreateNetworkInsightsAccessScopeRequest(BaseValidatorModel):
    ClientToken: str
    MatchPaths: Optional[List[AccessScopePathRequest]] = None
    ExcludePaths: Optional[List[AccessScopePathRequest]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None


class NetworkInsightsAccessScopeContent(BaseValidatorModel):
    NetworkInsightsAccessScopeId: Optional[str] = None
    MatchPaths: Optional[List[AccessScopePath]] = None
    ExcludePaths: Optional[List[AccessScopePath]] = None


# This class is the output for the 'bundle_instance' function.
class BundleInstanceResult(BaseValidatorModel):
    BundleTask: BundleTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_bundle_task' function.
class CancelBundleTaskResult(BaseValidatorModel):
    BundleTask: BundleTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_bundle_tasks' function.
class DescribeBundleTasksResult(BaseValidatorModel):
    BundleTasks: List[BundleTask]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'run_scheduled_instances' function.
class RunScheduledInstancesRequest(BaseValidatorModel):
    LaunchSpecification: ScheduledInstancesLaunchSpecification
    ScheduledInstanceId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    InstanceCount: Optional[int] = None


# This class is the output for the 'describe_import_image_tasks' function.
class DescribeImportImageTasksResult(BaseValidatorModel):
    ImportImageTasks: List[ImportImageTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_import_snapshot_tasks' function.
class DescribeImportSnapshotTasksResult(BaseValidatorModel):
    ImportSnapshotTasks: List[ImportSnapshotTask]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_default_subnet' function.
class CreateDefaultSubnetResult(BaseValidatorModel):
    Subnet: Subnet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_subnet' function.
class CreateSubnetResult(BaseValidatorModel):
    Subnet: Subnet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_subnets' function.
class DescribeSubnetsResult(BaseValidatorModel):
    Subnets: List[Subnet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_traffic_mirror_filter' function.
class CreateTrafficMirrorFilterResult(BaseValidatorModel):
    TrafficMirrorFilter: TrafficMirrorFilter
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_traffic_mirror_filters' function.
class DescribeTrafficMirrorFiltersResult(BaseValidatorModel):
    TrafficMirrorFilters: List[TrafficMirrorFilter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_traffic_mirror_filter_network_services' function.
class ModifyTrafficMirrorFilterNetworkServicesResult(BaseValidatorModel):
    TrafficMirrorFilter: TrafficMirrorFilter
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_transit_gateway_connect_peer' function.
class CreateTransitGatewayConnectPeerResult(BaseValidatorModel):
    TransitGatewayConnectPeer: TransitGatewayConnectPeer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_transit_gateway_connect_peer' function.
class DeleteTransitGatewayConnectPeerResult(BaseValidatorModel):
    TransitGatewayConnectPeer: TransitGatewayConnectPeer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_transit_gateway_connect_peers' function.
class DescribeTransitGatewayConnectPeersResult(BaseValidatorModel):
    TransitGatewayConnectPeers: List[TransitGatewayConnectPeer]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_transit_gateway_policy_table_entries' function.
class GetTransitGatewayPolicyTableEntriesResult(BaseValidatorModel):
    TransitGatewayPolicyTableEntries: List[TransitGatewayPolicyTableEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_verified_access_endpoint' function.
class CreateVerifiedAccessEndpointResult(BaseValidatorModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_verified_access_endpoint' function.
class DeleteVerifiedAccessEndpointResult(BaseValidatorModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpoint
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_verified_access_endpoints' function.
class DescribeVerifiedAccessEndpointsResult(BaseValidatorModel):
    VerifiedAccessEndpoints: List[VerifiedAccessEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_verified_access_endpoint' function.
class ModifyVerifiedAccessEndpointResult(BaseValidatorModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpoint
    ResponseMetadata: ResponseMetadata


class VerifiedAccessInstanceLoggingConfiguration(BaseValidatorModel):
    VerifiedAccessInstanceId: Optional[str] = None
    AccessLogs: Optional[VerifiedAccessLogs] = None


# This class is the output for the 'describe_volume_status' function.
class DescribeVolumeStatusResult(BaseValidatorModel):
    VolumeStatuses: List[VolumeStatusItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Vpc(BaseValidatorModel):
    OwnerId: Optional[str] = None
    InstanceTenancy: Optional[TenancyType] = None
    Ipv6CidrBlockAssociationSet: Optional[List[VpcIpv6CidrBlockAssociation]] = None
    CidrBlockAssociationSet: Optional[List[VpcCidrBlockAssociation]] = None
    IsDefault: Optional[bool] = None
    EncryptionControl: Optional[VpcEncryptionControl] = None
    Tags: Optional[List[Tag]] = None
    BlockPublicAccessStates: Optional[BlockPublicAccessStates] = None
    VpcId: Optional[str] = None
    State: Optional[VpcStateType] = None
    CidrBlock: Optional[str] = None
    DhcpOptionsId: Optional[str] = None


# This class is the output for the 'accept_vpc_peering_connection' function.
class AcceptVpcPeeringConnectionResult(BaseValidatorModel):
    VpcPeeringConnection: VpcPeeringConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpc_peering_connection' function.
class CreateVpcPeeringConnectionResult(BaseValidatorModel):
    VpcPeeringConnection: VpcPeeringConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpc_peering_connections' function.
class DescribeVpcPeeringConnectionsResult(BaseValidatorModel):
    VpcPeeringConnections: List[VpcPeeringConnection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AccessScopeAnalysisFinding(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: Optional[str] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    FindingId: Optional[str] = None
    FindingComponents: Optional[List[PathComponent]] = None


class NetworkInsightsAnalysis(BaseValidatorModel):
    NetworkInsightsAnalysisId: Optional[str] = None
    NetworkInsightsAnalysisArn: Optional[str] = None
    NetworkInsightsPathId: Optional[str] = None
    AdditionalAccounts: Optional[List[str]] = None
    FilterInArns: Optional[List[str]] = None
    StartDate: Optional[datetime] = None
    Status: Optional[AnalysisStatusType] = None
    StatusMessage: Optional[str] = None
    WarningMessage: Optional[str] = None
    NetworkPathFound: Optional[bool] = None
    ForwardPathComponents: Optional[List[PathComponent]] = None
    ReturnPathComponents: Optional[List[PathComponent]] = None
    Explanations: Optional[List[Explanation]] = None
    AlternatePathHints: Optional[List[AlternatePathHint]] = None
    SuggestedAccounts: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_network_interface' function.
class CreateNetworkInterfaceResult(BaseValidatorModel):
    NetworkInterface: NetworkInterface
    ClientToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_network_interfaces' function.
class DescribeNetworkInterfacesResult(BaseValidatorModel):
    NetworkInterfaces: List[NetworkInterface]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'bundle_instance' function.
class BundleInstanceRequest(BaseValidatorModel):
    InstanceId: str
    Storage: StorageUnion
    DryRun: Optional[bool] = None


# This class is the input for the 'create_vpn_connection' function.
class CreateVpnConnectionRequest(BaseValidatorModel):
    CustomerGatewayId: str
    Type: str
    VpnGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    DryRun: Optional[bool] = None
    Options: Optional[VpnConnectionOptionsSpecification] = None


class VpnConnection(BaseValidatorModel):
    Category: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    CoreNetworkAttachmentArn: Optional[str] = None
    GatewayAssociationState: Optional[GatewayAssociationStateType] = None
    Options: Optional[VpnConnectionOptions] = None
    Routes: Optional[List[VpnStaticRoute]] = None
    Tags: Optional[List[Tag]] = None
    VgwTelemetry: Optional[List[VgwTelemetry]] = None
    VpnConnectionId: Optional[str] = None
    State: Optional[VpnStateType] = None
    CustomerGatewayConfiguration: Optional[str] = None
    Type: Optional[Literal['ipsec.1']] = None
    CustomerGatewayId: Optional[str] = None
    VpnGatewayId: Optional[str] = None


class FleetLaunchTemplateOverrides(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    MaxPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    Placement: Optional[PlacementResponse] = None
    InstanceRequirements: Optional[InstanceRequirementsOutput] = None
    ImageId: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMappingResponse]] = None


class LaunchTemplateOverridesOutput(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsOutput] = None


class ResponseLaunchTemplateData(BaseValidatorModel):
    KernelId: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[LaunchTemplateIamInstanceProfileSpecification] = None
    BlockDeviceMappings: Optional[List[LaunchTemplateBlockDeviceMapping]] = None
    NetworkInterfaces: Optional[List[LaunchTemplateInstanceNetworkInterfaceSpecification]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[LaunchTemplatesMonitoring] = None
    Placement: Optional[LaunchTemplatePlacement] = None
    RamDiskId: Optional[str] = None
    DisableApiTermination: Optional[bool] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    UserData: Optional[str] = None
    TagSpecifications: Optional[List[LaunchTemplateTagSpecification]] = None
    ElasticGpuSpecifications: Optional[List[ElasticGpuSpecificationResponse]] = None
    ElasticInferenceAccelerators: Optional[List[LaunchTemplateElasticInferenceAcceleratorResponse]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    InstanceMarketOptions: Optional[LaunchTemplateInstanceMarketOptions] = None
    CreditSpecification: Optional[CreditSpecification] = None
    CpuOptions: Optional[LaunchTemplateCpuOptions] = None
    CapacityReservationSpecification: Optional[LaunchTemplateCapacityReservationSpecificationResponse] = None
    LicenseSpecifications: Optional[List[LaunchTemplateLicenseConfiguration]] = None
    HibernationOptions: Optional[LaunchTemplateHibernationOptions] = None
    MetadataOptions: Optional[LaunchTemplateInstanceMetadataOptions] = None
    EnclaveOptions: Optional[LaunchTemplateEnclaveOptions] = None
    InstanceRequirements: Optional[InstanceRequirementsOutput] = None
    PrivateDnsNameOptions: Optional[LaunchTemplatePrivateDnsNameOptions] = None
    MaintenanceOptions: Optional[LaunchTemplateInstanceMaintenanceOptions] = None
    DisableApiStop: Optional[bool] = None
    Operator: Optional[OperatorResponse] = None
    NetworkPerformanceOptions: Optional[LaunchTemplateNetworkPerformanceOptions] = None


class SpotFleetLaunchSpecificationOutput(BaseValidatorModel):
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecification] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[SpotFleetMonitoring] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationOutput]] = None
    Placement: Optional[SpotPlacement] = None
    RamdiskId: Optional[str] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    TagSpecifications: Optional[List[SpotFleetTagSpecificationOutput]] = None
    InstanceRequirements: Optional[InstanceRequirementsOutput] = None
    SecurityGroups: Optional[List[GroupIdentifier]] = None

BaselinePerformanceFactorsUnion = Union[BaselinePerformanceFactors, BaselinePerformanceFactorsOutput]


class FleetLaunchTemplateOverridesRequest(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    MaxPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    Placement: Optional[Placement] = None
    BlockDeviceMappings: Optional[List[FleetBlockDeviceMappingRequest]] = None
    InstanceRequirements: Optional[InstanceRequirementsRequest] = None
    ImageId: Optional[str] = None


class GetInstanceTypesFromInstanceRequirementsRequestPaginate(BaseValidatorModel):
    ArchitectureTypes: List[ArchitectureTypeType]
    VirtualizationTypes: List[VirtualizationTypeType]
    InstanceRequirements: InstanceRequirementsRequest
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_instance_types_from_instance_requirements' function.
class GetInstanceTypesFromInstanceRequirementsRequest(BaseValidatorModel):
    ArchitectureTypes: List[ArchitectureTypeType]
    VirtualizationTypes: List[VirtualizationTypeType]
    InstanceRequirements: InstanceRequirementsRequest
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class InstanceRequirementsWithMetadataRequest(BaseValidatorModel):
    ArchitectureTypes: Optional[List[ArchitectureTypeType]] = None
    VirtualizationTypes: Optional[List[VirtualizationTypeType]] = None
    InstanceRequirements: Optional[InstanceRequirementsRequest] = None


class RequestLaunchTemplateData(BaseValidatorModel):
    KernelId: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[LaunchTemplateIamInstanceProfileSpecificationRequest] = None
    BlockDeviceMappings: Optional[List[LaunchTemplateBlockDeviceMappingRequest]] = None
    NetworkInterfaces: Optional[List[LaunchTemplateInstanceNetworkInterfaceSpecificationRequest]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[LaunchTemplatesMonitoringRequest] = None
    Placement: Optional[LaunchTemplatePlacementRequest] = None
    RamDiskId: Optional[str] = None
    DisableApiTermination: Optional[bool] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    UserData: Optional[str] = None
    TagSpecifications: Optional[List[LaunchTemplateTagSpecificationRequest]] = None
    ElasticGpuSpecifications: Optional[List[ElasticGpuSpecification]] = None
    ElasticInferenceAccelerators: Optional[List[LaunchTemplateElasticInferenceAccelerator]] = None
    SecurityGroupIds: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    InstanceMarketOptions: Optional[LaunchTemplateInstanceMarketOptionsRequest] = None
    CreditSpecification: Optional[CreditSpecificationRequest] = None
    CpuOptions: Optional[LaunchTemplateCpuOptionsRequest] = None
    CapacityReservationSpecification: Optional[LaunchTemplateCapacityReservationSpecificationRequest] = None
    LicenseSpecifications: Optional[List[LaunchTemplateLicenseConfigurationRequest]] = None
    HibernationOptions: Optional[LaunchTemplateHibernationOptionsRequest] = None
    MetadataOptions: Optional[LaunchTemplateInstanceMetadataOptionsRequest] = None
    EnclaveOptions: Optional[LaunchTemplateEnclaveOptionsRequest] = None
    InstanceRequirements: Optional[InstanceRequirementsRequest] = None
    PrivateDnsNameOptions: Optional[LaunchTemplatePrivateDnsNameOptionsRequest] = None
    MaintenanceOptions: Optional[LaunchTemplateInstanceMaintenanceOptionsRequest] = None
    DisableApiStop: Optional[bool] = None
    Operator: Optional[OperatorRequest] = None
    NetworkPerformanceOptions: Optional[LaunchTemplateNetworkPerformanceOptionsRequest] = None


# This class is the output for the 'describe_conversion_tasks' function.
class DescribeConversionTasksResult(BaseValidatorModel):
    ConversionTasks: List[ConversionTask]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_instance' function.
class ImportInstanceResult(BaseValidatorModel):
    ConversionTask: ConversionTask
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_volume' function.
class ImportVolumeResult(BaseValidatorModel):
    ConversionTask: ConversionTask
    ResponseMetadata: ResponseMetadata


class SpotInstanceRequest(BaseValidatorModel):
    ActualBlockHourlyPrice: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    BlockDurationMinutes: Optional[int] = None
    CreateTime: Optional[datetime] = None
    Fault: Optional[SpotInstanceStateFault] = None
    InstanceId: Optional[str] = None
    LaunchGroup: Optional[str] = None
    LaunchSpecification: Optional[LaunchSpecification] = None
    LaunchedAvailabilityZone: Optional[str] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    SpotInstanceRequestId: Optional[str] = None
    SpotPrice: Optional[str] = None
    State: Optional[SpotInstanceStateType] = None
    Status: Optional[SpotInstanceStatus] = None
    Tags: Optional[List[Tag]] = None
    Type: Optional[SpotInstanceTypeType] = None
    ValidFrom: Optional[datetime] = None
    ValidUntil: Optional[datetime] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None


class RequestSpotLaunchSpecification(BaseValidatorModel):
    SecurityGroupIds: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecification] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabled] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationUnion]] = None
    Placement: Optional[SpotPlacement] = None
    RamdiskId: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None


class RunInstancesRequestServiceResourceCreateInstances(BaseValidatorModel):
    MaxCount: int
    MinCount: int
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabled] = None
    Placement: Optional[Placement] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    ElasticGpuSpecification: Optional[List[ElasticGpuSpecification]] = None
    ElasticInferenceAccelerators: Optional[List[ElasticInferenceAccelerator]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    InstanceMarketOptions: Optional[InstanceMarketOptionsRequest] = None
    CreditSpecification: Optional[CreditSpecificationRequest] = None
    CpuOptions: Optional[CpuOptionsRequest] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecification] = None
    HibernationOptions: Optional[HibernationOptionsRequest] = None
    LicenseSpecifications: Optional[List[LicenseConfigurationRequest]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsRequest] = None
    EnclaveOptions: Optional[EnclaveOptionsRequest] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsRequest] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptionsRequest] = None
    DisableApiStop: Optional[bool] = None
    EnablePrimaryIpv6: Optional[bool] = None
    NetworkPerformanceOptions: Optional[InstanceNetworkPerformanceOptionsRequest] = None
    Operator: Optional[OperatorRequest] = None
    DryRun: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    PrivateIpAddress: Optional[str] = None
    ClientToken: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationUnion]] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecification] = None
    EbsOptimized: Optional[bool] = None


class RunInstancesRequestSubnetCreateInstances(BaseValidatorModel):
    MaxCount: int
    MinCount: int
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabled] = None
    Placement: Optional[Placement] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    UserData: Optional[str] = None
    ElasticGpuSpecification: Optional[List[ElasticGpuSpecification]] = None
    ElasticInferenceAccelerators: Optional[List[ElasticInferenceAccelerator]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    InstanceMarketOptions: Optional[InstanceMarketOptionsRequest] = None
    CreditSpecification: Optional[CreditSpecificationRequest] = None
    CpuOptions: Optional[CpuOptionsRequest] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecification] = None
    HibernationOptions: Optional[HibernationOptionsRequest] = None
    LicenseSpecifications: Optional[List[LicenseConfigurationRequest]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsRequest] = None
    EnclaveOptions: Optional[EnclaveOptionsRequest] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsRequest] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptionsRequest] = None
    DisableApiStop: Optional[bool] = None
    EnablePrimaryIpv6: Optional[bool] = None
    NetworkPerformanceOptions: Optional[InstanceNetworkPerformanceOptionsRequest] = None
    Operator: Optional[OperatorRequest] = None
    DryRun: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    PrivateIpAddress: Optional[str] = None
    ClientToken: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationUnion]] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecification] = None
    EbsOptimized: Optional[bool] = None


# This class is the input for the 'run_instances' function.
class RunInstancesRequest(BaseValidatorModel):
    MaxCount: int
    MinCount: int
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6Address]] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabled] = None
    Placement: Optional[Placement] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    ElasticGpuSpecification: Optional[List[ElasticGpuSpecification]] = None
    ElasticInferenceAccelerators: Optional[List[ElasticInferenceAccelerator]] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    LaunchTemplate: Optional[LaunchTemplateSpecification] = None
    InstanceMarketOptions: Optional[InstanceMarketOptionsRequest] = None
    CreditSpecification: Optional[CreditSpecificationRequest] = None
    CpuOptions: Optional[CpuOptionsRequest] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecification] = None
    HibernationOptions: Optional[HibernationOptionsRequest] = None
    LicenseSpecifications: Optional[List[LicenseConfigurationRequest]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsRequest] = None
    EnclaveOptions: Optional[EnclaveOptionsRequest] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsRequest] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptionsRequest] = None
    DisableApiStop: Optional[bool] = None
    EnablePrimaryIpv6: Optional[bool] = None
    NetworkPerformanceOptions: Optional[InstanceNetworkPerformanceOptionsRequest] = None
    Operator: Optional[OperatorRequest] = None
    DryRun: Optional[bool] = None
    DisableApiTermination: Optional[bool] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    PrivateIpAddress: Optional[str] = None
    ClientToken: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationUnion]] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecification] = None
    EbsOptimized: Optional[bool] = None


class Instance(BaseValidatorModel):
    Architecture: Optional[ArchitectureValuesType] = None
    BlockDeviceMappings: Optional[List[InstanceBlockDeviceMapping]] = None
    ClientToken: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    EnaSupport: Optional[bool] = None
    Hypervisor: Optional[HypervisorTypeType] = None
    IamInstanceProfile: Optional[IamInstanceProfile] = None
    InstanceLifecycle: Optional[InstanceLifecycleTypeType] = None
    ElasticGpuAssociations: Optional[List[ElasticGpuAssociation]] = None
    ElasticInferenceAcceleratorAssociations: Optional[List[ElasticInferenceAcceleratorAssociation]] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterface]] = None
    OutpostArn: Optional[str] = None
    RootDeviceName: Optional[str] = None
    RootDeviceType: Optional[DeviceTypeType] = None
    SecurityGroups: Optional[List[GroupIdentifier]] = None
    SourceDestCheck: Optional[bool] = None
    SpotInstanceRequestId: Optional[str] = None
    SriovNetSupport: Optional[str] = None
    StateReason: Optional[StateReason] = None
    Tags: Optional[List[Tag]] = None
    VirtualizationType: Optional[VirtualizationTypeType] = None
    CpuOptions: Optional[CpuOptions] = None
    CapacityReservationId: Optional[str] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationResponse] = None
    HibernationOptions: Optional[HibernationOptions] = None
    Licenses: Optional[List[LicenseConfiguration]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsResponse] = None
    EnclaveOptions: Optional[EnclaveOptions] = None
    BootMode: Optional[BootModeValuesType] = None
    PlatformDetails: Optional[str] = None
    UsageOperation: Optional[str] = None
    UsageOperationUpdateTime: Optional[datetime] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsResponse] = None
    Ipv6Address: Optional[str] = None
    TpmSupport: Optional[str] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptions] = None
    CurrentInstanceBootMode: Optional[InstanceBootModeValuesType] = None
    NetworkPerformanceOptions: Optional[InstanceNetworkPerformanceOptions] = None
    Operator: Optional[OperatorResponse] = None
    InstanceId: Optional[str] = None
    ImageId: Optional[str] = None
    State: Optional[InstanceState] = None
    PrivateDnsName: Optional[str] = None
    PublicDnsName: Optional[str] = None
    StateTransitionReason: Optional[str] = None
    KeyName: Optional[str] = None
    AmiLaunchIndex: Optional[int] = None
    ProductCodes: Optional[List[ProductCode]] = None
    InstanceType: Optional[InstanceTypeType] = None
    LaunchTime: Optional[datetime] = None
    Placement: Optional[Placement] = None
    KernelId: Optional[str] = None
    RamdiskId: Optional[str] = None
    Platform: Optional[Literal['windows']] = None
    Monitoring: Optional[Monitoring] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PublicIpAddress: Optional[str] = None


# This class is the output for the 'describe_instance_types' function.
class DescribeInstanceTypesResult(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_network_insights_access_scope' function.
class CreateNetworkInsightsAccessScopeResult(BaseValidatorModel):
    NetworkInsightsAccessScope: NetworkInsightsAccessScope
    NetworkInsightsAccessScopeContent: NetworkInsightsAccessScopeContent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_network_insights_access_scope_content' function.
class GetNetworkInsightsAccessScopeContentResult(BaseValidatorModel):
    NetworkInsightsAccessScopeContent: NetworkInsightsAccessScopeContent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_verified_access_instance_logging_configurations' function.
class DescribeVerifiedAccessInstanceLoggingConfigurationsResult(BaseValidatorModel):
    LoggingConfigurations: List[VerifiedAccessInstanceLoggingConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_verified_access_instance_logging_configuration' function.
class ModifyVerifiedAccessInstanceLoggingConfigurationResult(BaseValidatorModel):
    LoggingConfiguration: VerifiedAccessInstanceLoggingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_default_vpc' function.
class CreateDefaultVpcResult(BaseValidatorModel):
    Vpc: Vpc
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpc' function.
class CreateVpcResult(BaseValidatorModel):
    Vpc: Vpc
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpcs' function.
class DescribeVpcsResult(BaseValidatorModel):
    Vpcs: List[Vpc]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_network_insights_access_scope_analysis_findings' function.
class GetNetworkInsightsAccessScopeAnalysisFindingsResult(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    AnalysisStatus: AnalysisStatusType
    AnalysisFindings: List[AccessScopeAnalysisFinding]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_network_insights_analyses' function.
class DescribeNetworkInsightsAnalysesResult(BaseValidatorModel):
    NetworkInsightsAnalyses: List[NetworkInsightsAnalysis]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'start_network_insights_analysis' function.
class StartNetworkInsightsAnalysisResult(BaseValidatorModel):
    NetworkInsightsAnalysis: NetworkInsightsAnalysis
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vpn_connection' function.
class CreateVpnConnectionResult(BaseValidatorModel):
    VpnConnection: VpnConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vpn_connections' function.
class DescribeVpnConnectionsResult(BaseValidatorModel):
    VpnConnections: List[VpnConnection]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpn_connection_options' function.
class ModifyVpnConnectionOptionsResult(BaseValidatorModel):
    VpnConnection: VpnConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpn_connection' function.
class ModifyVpnConnectionResult(BaseValidatorModel):
    VpnConnection: VpnConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpn_tunnel_certificate' function.
class ModifyVpnTunnelCertificateResult(BaseValidatorModel):
    VpnConnection: VpnConnection
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_vpn_tunnel_options' function.
class ModifyVpnTunnelOptionsResult(BaseValidatorModel):
    VpnConnection: VpnConnection
    ResponseMetadata: ResponseMetadata


class FleetLaunchTemplateConfig(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecification] = None
    Overrides: Optional[List[FleetLaunchTemplateOverrides]] = None


class LaunchTemplateAndOverridesResponse(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecification] = None
    Overrides: Optional[FleetLaunchTemplateOverrides] = None


class LaunchTemplateConfigOutput(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecification] = None
    Overrides: Optional[List[LaunchTemplateOverridesOutput]] = None


# This class is the output for the 'get_launch_template_data' function.
class GetLaunchTemplateDataResult(BaseValidatorModel):
    LaunchTemplateData: ResponseLaunchTemplateData
    ResponseMetadata: ResponseMetadata


class LaunchTemplateVersion(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None
    VersionDescription: Optional[str] = None
    CreateTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DefaultVersion: Optional[bool] = None
    LaunchTemplateData: Optional[ResponseLaunchTemplateData] = None
    Operator: Optional[OperatorResponse] = None


class InstanceRequirements(BaseValidatorModel):
    VCpuCount: Optional[VCpuCountRange] = None
    MemoryMiB: Optional[MemoryMiB] = None
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpu] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCount] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGB] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbps] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCount] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiB] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbps] = None
    AllowedInstanceTypes: Optional[List[str]] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None
    BaselinePerformanceFactors: Optional[BaselinePerformanceFactorsUnion] = None


class FleetLaunchTemplateConfigRequest(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationRequest] = None
    Overrides: Optional[List[FleetLaunchTemplateOverridesRequest]] = None


class GetSpotPlacementScoresRequestPaginate(BaseValidatorModel):
    TargetCapacity: int
    InstanceTypes: Optional[List[str]] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    SingleAvailabilityZone: Optional[bool] = None
    RegionNames: Optional[List[str]] = None
    InstanceRequirementsWithMetadata: Optional[InstanceRequirementsWithMetadataRequest] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_spot_placement_scores' function.
class GetSpotPlacementScoresRequest(BaseValidatorModel):
    TargetCapacity: int
    InstanceTypes: Optional[List[str]] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    SingleAvailabilityZone: Optional[bool] = None
    RegionNames: Optional[List[str]] = None
    InstanceRequirementsWithMetadata: Optional[InstanceRequirementsWithMetadataRequest] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'create_launch_template' function.
class CreateLaunchTemplateRequest(BaseValidatorModel):
    LaunchTemplateName: str
    LaunchTemplateData: RequestLaunchTemplateData
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    VersionDescription: Optional[str] = None
    Operator: Optional[OperatorRequest] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None


# This class is the input for the 'create_launch_template_version' function.
class CreateLaunchTemplateVersionRequest(BaseValidatorModel):
    LaunchTemplateData: RequestLaunchTemplateData
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    SourceVersion: Optional[str] = None
    VersionDescription: Optional[str] = None
    ResolveAlias: Optional[bool] = None


# This class is the output for the 'describe_spot_instance_requests' function.
class DescribeSpotInstanceRequestsResult(BaseValidatorModel):
    SpotInstanceRequests: List[SpotInstanceRequest]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'request_spot_instances' function.
class RequestSpotInstancesResult(BaseValidatorModel):
    SpotInstanceRequests: List[SpotInstanceRequest]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'request_spot_instances' function.
class RequestSpotInstancesRequest(BaseValidatorModel):
    LaunchSpecification: Optional[RequestSpotLaunchSpecification] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None
    DryRun: Optional[bool] = None
    SpotPrice: Optional[str] = None
    ClientToken: Optional[str] = None
    InstanceCount: Optional[int] = None
    Type: Optional[SpotInstanceTypeType] = None
    ValidFrom: Optional[Timestamp] = None
    ValidUntil: Optional[Timestamp] = None
    LaunchGroup: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    BlockDurationMinutes: Optional[int] = None


# This class is the output for the 'run_instances' function.
class ReservationResponse(BaseValidatorModel):
    ReservationId: str
    OwnerId: str
    RequesterId: str
    Groups: List[GroupIdentifier]
    Instances: List[Instance]
    ResponseMetadata: ResponseMetadata


class Reservation(BaseValidatorModel):
    ReservationId: Optional[str] = None
    OwnerId: Optional[str] = None
    RequesterId: Optional[str] = None
    Groups: Optional[List[GroupIdentifier]] = None
    Instances: Optional[List[Instance]] = None


class CreateFleetError(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponse] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class CreateFleetInstance(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponse] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    InstanceIds: Optional[List[str]] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[Literal['windows']] = None


class DescribeFleetError(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponse] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class DescribeFleetsInstances(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponse] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    InstanceIds: Optional[List[str]] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[Literal['windows']] = None


class SpotFleetRequestConfigDataOutput(BaseValidatorModel):
    IamFleetRole: str
    TargetCapacity: int
    AllocationStrategy: Optional[AllocationStrategyType] = None
    OnDemandAllocationStrategy: Optional[OnDemandAllocationStrategyType] = None
    SpotMaintenanceStrategies: Optional[SpotMaintenanceStrategies] = None
    ClientToken: Optional[str] = None
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None
    FulfilledCapacity: Optional[float] = None
    OnDemandFulfilledCapacity: Optional[float] = None
    LaunchSpecifications: Optional[List[SpotFleetLaunchSpecificationOutput]] = None
    LaunchTemplateConfigs: Optional[List[LaunchTemplateConfigOutput]] = None
    SpotPrice: Optional[str] = None
    OnDemandTargetCapacity: Optional[int] = None
    OnDemandMaxTotalPrice: Optional[str] = None
    SpotMaxTotalPrice: Optional[str] = None
    TerminateInstancesWithExpiration: Optional[bool] = None
    Type: Optional[FleetTypeType] = None
    ValidFrom: Optional[datetime] = None
    ValidUntil: Optional[datetime] = None
    ReplaceUnhealthyInstances: Optional[bool] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None
    LoadBalancersConfig: Optional[LoadBalancersConfigOutput] = None
    InstancePoolsToUseCount: Optional[int] = None
    Context: Optional[str] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationOutput]] = None


# This class is the output for the 'create_launch_template_version' function.
class CreateLaunchTemplateVersionResult(BaseValidatorModel):
    LaunchTemplateVersion: LaunchTemplateVersion
    Warning: ValidationWarning
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_launch_template_versions' function.
class DescribeLaunchTemplateVersionsResult(BaseValidatorModel):
    LaunchTemplateVersions: List[LaunchTemplateVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

InstanceRequirementsUnion = Union[InstanceRequirements, InstanceRequirementsOutput]


class SpotFleetLaunchSpecification(BaseValidatorModel):
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMapping]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecification] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[SpotFleetMonitoring] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecification]] = None
    Placement: Optional[SpotPlacement] = None
    RamdiskId: Optional[str] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    TagSpecifications: Optional[List[SpotFleetTagSpecification]] = None
    InstanceRequirements: Optional[InstanceRequirements] = None
    SecurityGroups: Optional[List[GroupIdentifier]] = None


# This class is the input for the 'create_fleet' function.
class CreateFleetRequest(BaseValidatorModel):
    LaunchTemplateConfigs: List[FleetLaunchTemplateConfigRequest]
    TargetCapacitySpecification: TargetCapacitySpecificationRequest
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    SpotOptions: Optional[SpotOptionsRequest] = None
    OnDemandOptions: Optional[OnDemandOptionsRequest] = None
    ExcessCapacityTerminationPolicy: Optional[FleetExcessCapacityTerminationPolicyType] = None
    TerminateInstancesWithExpiration: Optional[bool] = None
    Type: Optional[FleetTypeType] = None
    ValidFrom: Optional[Timestamp] = None
    ValidUntil: Optional[Timestamp] = None
    ReplaceUnhealthyInstances: Optional[bool] = None
    TagSpecifications: Optional[List[TagSpecificationUnion]] = None
    Context: Optional[str] = None


# This class is the input for the 'modify_fleet' function.
class ModifyFleetRequest(BaseValidatorModel):
    FleetId: str
    DryRun: Optional[bool] = None
    ExcessCapacityTerminationPolicy: Optional[FleetExcessCapacityTerminationPolicyType] = None
    LaunchTemplateConfigs: Optional[List[FleetLaunchTemplateConfigRequest]] = None
    TargetCapacitySpecification: Optional[TargetCapacitySpecificationRequest] = None
    Context: Optional[str] = None


# This class is the output for the 'describe_instances' function.
class DescribeInstancesResult(BaseValidatorModel):
    Reservations: List[Reservation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_fleet' function.
class CreateFleetResult(BaseValidatorModel):
    FleetId: str
    Errors: List[CreateFleetError]
    Instances: List[CreateFleetInstance]
    ResponseMetadata: ResponseMetadata


class FleetData(BaseValidatorModel):
    ActivityStatus: Optional[FleetActivityStatusType] = None
    CreateTime: Optional[datetime] = None
    FleetId: Optional[str] = None
    FleetState: Optional[FleetStateCodeType] = None
    ClientToken: Optional[str] = None
    ExcessCapacityTerminationPolicy: Optional[FleetExcessCapacityTerminationPolicyType] = None
    FulfilledCapacity: Optional[float] = None
    FulfilledOnDemandCapacity: Optional[float] = None
    LaunchTemplateConfigs: Optional[List[FleetLaunchTemplateConfig]] = None
    TargetCapacitySpecification: Optional[TargetCapacitySpecification] = None
    TerminateInstancesWithExpiration: Optional[bool] = None
    Type: Optional[FleetTypeType] = None
    ValidFrom: Optional[datetime] = None
    ValidUntil: Optional[datetime] = None
    ReplaceUnhealthyInstances: Optional[bool] = None
    SpotOptions: Optional[SpotOptions] = None
    OnDemandOptions: Optional[OnDemandOptions] = None
    Tags: Optional[List[Tag]] = None
    Errors: Optional[List[DescribeFleetError]] = None
    Instances: Optional[List[DescribeFleetsInstances]] = None
    Context: Optional[str] = None


class SpotFleetRequestConfig(BaseValidatorModel):
    ActivityStatus: Optional[ActivityStatusType] = None
    CreateTime: Optional[datetime] = None
    SpotFleetRequestConfig: Optional[SpotFleetRequestConfigDataOutput] = None
    SpotFleetRequestId: Optional[str] = None
    SpotFleetRequestState: Optional[BatchStateType] = None
    Tags: Optional[List[Tag]] = None


class LaunchTemplateOverrides(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsUnion] = None


# This class is the output for the 'describe_fleets' function.
class DescribeFleetsResult(BaseValidatorModel):
    Fleets: List[FleetData]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_spot_fleet_requests' function.
class DescribeSpotFleetRequestsResponse(BaseValidatorModel):
    SpotFleetRequestConfigs: List[SpotFleetRequestConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

LaunchTemplateOverridesUnion = Union[LaunchTemplateOverrides, LaunchTemplateOverridesOutput]


class LaunchTemplateConfig(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecification] = None
    Overrides: Optional[List[LaunchTemplateOverridesUnion]] = None

LaunchTemplateConfigUnion = Union[LaunchTemplateConfig, LaunchTemplateConfigOutput]


class SpotFleetRequestConfigData(BaseValidatorModel):
    IamFleetRole: str
    TargetCapacity: int
    AllocationStrategy: Optional[AllocationStrategyType] = None
    OnDemandAllocationStrategy: Optional[OnDemandAllocationStrategyType] = None
    SpotMaintenanceStrategies: Optional[SpotMaintenanceStrategies] = None
    ClientToken: Optional[str] = None
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None
    FulfilledCapacity: Optional[float] = None
    OnDemandFulfilledCapacity: Optional[float] = None
    LaunchSpecifications: Optional[List[SpotFleetLaunchSpecification]] = None
    LaunchTemplateConfigs: Optional[List[LaunchTemplateConfig]] = None
    SpotPrice: Optional[str] = None
    OnDemandTargetCapacity: Optional[int] = None
    OnDemandMaxTotalPrice: Optional[str] = None
    SpotMaxTotalPrice: Optional[str] = None
    TerminateInstancesWithExpiration: Optional[bool] = None
    Type: Optional[FleetTypeType] = None
    ValidFrom: Optional[Timestamp] = None
    ValidUntil: Optional[Timestamp] = None
    ReplaceUnhealthyInstances: Optional[bool] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None
    LoadBalancersConfig: Optional[LoadBalancersConfig] = None
    InstancePoolsToUseCount: Optional[int] = None
    Context: Optional[str] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    TagSpecifications: Optional[List[TagSpecification]] = None


# This class is the input for the 'modify_spot_fleet_request' function.
class ModifySpotFleetRequestRequest(BaseValidatorModel):
    SpotFleetRequestId: str
    LaunchTemplateConfigs: Optional[List[LaunchTemplateConfigUnion]] = None
    OnDemandTargetCapacity: Optional[int] = None
    Context: Optional[str] = None
    TargetCapacity: Optional[int] = None
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None

SpotFleetRequestConfigDataUnion = Union[SpotFleetRequestConfigData, SpotFleetRequestConfigDataOutput]


# This class is the input for the 'request_spot_fleet' function.
class RequestSpotFleetRequest(BaseValidatorModel):
    SpotFleetRequestConfig: SpotFleetRequestConfigDataUnion
    DryRun: Optional[bool] = None