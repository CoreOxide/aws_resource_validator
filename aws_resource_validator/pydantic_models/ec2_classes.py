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
from aws_resource_validator.pydantic_models.ec2_constants import *

class AcceleratorCountRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AcceleratorCountTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AcceleratorTotalMemoryMiBRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AcceleratorTotalMemoryMiBTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AddressTransferTypeDef(BaseValidatorModel):
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    TransferAccountId: Optional[str] = None
    TransferOfferExpirationTimestamp: Optional[datetime] = None
    TransferOfferAcceptedTimestamp: Optional[datetime] = None
    AddressTransferStatus: Optional[AddressTransferStatusType] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TargetConfigurationRequestTypeDef(BaseValidatorModel):
    OfferingId: str
    InstanceCount: Optional[int] = None

class AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class AcceptVpcEndpointConnectionsRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    VpcEndpointIds: Sequence[str]
    DryRun: Optional[bool] = None

class AcceptVpcPeeringConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None

class AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class AccountAttributeValueTypeDef(BaseValidatorModel):
    AttributeValue: Optional[str] = None

class ActiveInstanceTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    SpotInstanceRequestId: Optional[str] = None
    InstanceHealth: Optional[InstanceHealthStatusType] = None

class AddIpamOperatingRegionTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None

class AddPrefixListEntryTypeDef(BaseValidatorModel):
    Cidr: str
    Description: Optional[str] = None

class AddedPrincipalTypeDef(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None
    ServicePermissionId: Optional[str] = None
    ServiceId: Optional[str] = None

class AnalysisComponentTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None

class RuleGroupTypePairTypeDef(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    RuleGroupType: Optional[str] = None

class RuleOptionTypeDef(BaseValidatorModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None

class PtrUpdateStatusTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Status: Optional[str] = None
    Reason: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AdvertiseByoipCidrRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    Asn: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class AllocateIpamPoolCidrRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None
    NetmaskLength: Optional[int] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PreviewNextCidr: Optional[bool] = None
    AllowedCidrs: Optional[Sequence[str]] = None
    DisallowedCidrs: Optional[Sequence[str]] = None

class IpamPoolAllocationTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    IpamPoolAllocationId: Optional[str] = None
    Description: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamPoolAllocationResourceTypeType] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None

class AlternatePathHintTypeDef(BaseValidatorModel):
    ComponentId: Optional[str] = None
    ComponentArn: Optional[str] = None

class PortRangeTypeDef(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None

class AnalysisLoadBalancerListenerTypeDef(BaseValidatorModel):
    LoadBalancerPort: Optional[int] = None
    InstancePort: Optional[int] = None

class AnalysisRouteTableRouteTypeDef(BaseValidatorModel):
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

class ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    VpcId: str
    SecurityGroupIds: Sequence[str]
    DryRun: Optional[bool] = None

class AsnAssociationTypeDef(BaseValidatorModel):
    Asn: Optional[str] = None
    Cidr: Optional[str] = None
    StatusMessage: Optional[str] = None
    State: Optional[AsnAssociationStateType] = None

class AsnAuthorizationContextTypeDef(BaseValidatorModel):
    Message: str
    Signature: str

class AssignIpv6AddressesRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[str]] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[Sequence[str]] = None

class AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef(BaseValidatorModel):
    AllowReassignment: Optional[bool] = None
    PrivateIpAddresses: Optional[Sequence[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None
    Ipv4PrefixCount: Optional[int] = None

class AssignPrivateIpAddressesRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    AllowReassignment: Optional[bool] = None
    PrivateIpAddresses: Optional[Sequence[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None
    Ipv4PrefixCount: Optional[int] = None

class AssignedPrivateIpAddressTypeDef(BaseValidatorModel):
    PrivateIpAddress: Optional[str] = None

class Ipv4PrefixSpecificationTypeDef(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None

class AssignPrivateNatGatewayAddressRequestRequestTypeDef(BaseValidatorModel):
    NatGatewayId: str
    PrivateIpAddresses: Optional[Sequence[str]] = None
    PrivateIpAddressCount: Optional[int] = None
    DryRun: Optional[bool] = None

class NatGatewayAddressTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIp: Optional[str] = None
    PublicIp: Optional[str] = None
    AssociationId: Optional[str] = None
    IsPrimary: Optional[bool] = None
    FailureMessage: Optional[str] = None
    Status: Optional[NatGatewayAddressStatusType] = None

class AssociateAddressRequestClassicAddressAssociateTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    InstanceId: Optional[str] = None
    AllowReassociation: Optional[bool] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class AssociateAddressRequestRequestTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    AllowReassociation: Optional[bool] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class AssociateAddressRequestVpcAddressAssociateTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    AllowReassociation: Optional[bool] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class AssociateClientVpnTargetNetworkRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    SubnetId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AssociationStatusTypeDef(BaseValidatorModel):
    Code: Optional[AssociationStatusCodeType] = None
    Message: Optional[str] = None

class AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None

class AssociateDhcpOptionsRequestRequestTypeDef(BaseValidatorModel):
    DhcpOptionsId: str
    VpcId: str
    DryRun: Optional[bool] = None

class AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef(BaseValidatorModel):
    DhcpOptionsId: str
    DryRun: Optional[bool] = None

class AssociateEnclaveCertificateIamRoleRequestRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    RoleArn: str
    DryRun: Optional[bool] = None

class IamInstanceProfileSpecificationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class AssociateIpamByoasnRequestRequestTypeDef(BaseValidatorModel):
    Asn: str
    Cidr: str
    DryRun: Optional[bool] = None

class AssociateNatGatewayAddressRequestRequestTypeDef(BaseValidatorModel):
    NatGatewayId: str
    AllocationIds: Sequence[str]
    PrivateIpAddresses: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class AssociateRouteTableRequestRequestTypeDef(BaseValidatorModel):
    RouteTableId: str
    DryRun: Optional[bool] = None
    SubnetId: Optional[str] = None
    GatewayId: Optional[str] = None

class AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    SubnetId: Optional[str] = None
    GatewayId: Optional[str] = None

class RouteTableAssociationStateTypeDef(BaseValidatorModel):
    State: Optional[RouteTableAssociationStateCodeType] = None
    StatusMessage: Optional[str] = None

class AssociateSubnetCidrBlockRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    Ipv6CidrBlock: Optional[str] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None

class AssociateTransitGatewayMulticastDomainRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    TransitGatewayAttachmentId: str
    SubnetIds: Sequence[str]
    DryRun: Optional[bool] = None

class AssociateTransitGatewayPolicyTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class TransitGatewayPolicyTableAssociationTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class AssociateTransitGatewayRouteTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class TransitGatewayAssociationTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class AssociateTrunkInterfaceRequestRequestTypeDef(BaseValidatorModel):
    BranchInterfaceId: str
    TrunkInterfaceId: str
    VlanId: Optional[int] = None
    GreKey: Optional[int] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AssociateVpcCidrBlockRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    AmazonProvidedIpv6CidrBlock: Optional[bool] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlockNetworkBorderGroup: Optional[str] = None
    Ipv6Pool: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None

class AssociatedRoleTypeDef(BaseValidatorModel):
    AssociatedRoleArn: Optional[str] = None
    CertificateS3BucketName: Optional[str] = None
    CertificateS3ObjectKey: Optional[str] = None
    EncryptionKmsKeyId: Optional[str] = None

class AssociatedTargetNetworkTypeDef(BaseValidatorModel):
    NetworkId: Optional[str] = None
    NetworkType: Optional[Literal["vpc"]] = None

class AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef(BaseValidatorModel):
    Groups: Sequence[str]
    VpcId: str
    DryRun: Optional[bool] = None

class AttachClassicLinkVpcRequestRequestTypeDef(BaseValidatorModel):
    Groups: Sequence[str]
    InstanceId: str
    VpcId: str
    DryRun: Optional[bool] = None

class AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef(BaseValidatorModel):
    Groups: Sequence[str]
    InstanceId: str
    DryRun: Optional[bool] = None

class AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None

class AttachInternetGatewayRequestRequestTypeDef(BaseValidatorModel):
    InternetGatewayId: str
    VpcId: str
    DryRun: Optional[bool] = None

class AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef(BaseValidatorModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None

class AttachVerifiedAccessTrustProviderRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    VerifiedAccessTrustProviderId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AttachVolumeRequestInstanceAttachVolumeTypeDef(BaseValidatorModel):
    Device: str
    VolumeId: str
    DryRun: Optional[bool] = None

class AttachVolumeRequestRequestTypeDef(BaseValidatorModel):
    Device: str
    InstanceId: str
    VolumeId: str
    DryRun: Optional[bool] = None

class AttachVolumeRequestVolumeAttachToInstanceTypeDef(BaseValidatorModel):
    Device: str
    InstanceId: str
    DryRun: Optional[bool] = None

class AttachVpnGatewayRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    VpnGatewayId: str
    DryRun: Optional[bool] = None

class VpcAttachmentTypeDef(BaseValidatorModel):
    State: Optional[AttachmentStatusType] = None
    VpcId: Optional[str] = None

class AttachmentEnaSrdUdpSpecificationTypeDef(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class AttributeBooleanValueTypeDef(BaseValidatorModel):
    Value: Optional[bool] = None

class AttributeValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class ClientVpnAuthorizationRuleStatusTypeDef(BaseValidatorModel):
    Code: Optional[ClientVpnAuthorizationRuleStatusCodeType] = None
    Message: Optional[str] = None

class AuthorizeClientVpnIngressRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    TargetNetworkCidr: str
    AccessGroupId: Optional[str] = None
    AuthorizeAllGroups: Optional[bool] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AvailabilityZoneMessageTypeDef(BaseValidatorModel):
    Message: Optional[str] = None

class InstanceCapacityTypeDef(BaseValidatorModel):
    AvailableCapacity: Optional[int] = None
    InstanceType: Optional[str] = None
    TotalCapacity: Optional[int] = None

class BaselineEbsBandwidthMbpsRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class BaselineEbsBandwidthMbpsTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class EbsBlockDeviceTypeDef(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    KmsKeyId: Optional[str] = None
    Throughput: Optional[int] = None
    OutpostArn: Optional[str] = None
    Encrypted: Optional[bool] = None

class BundleTaskErrorTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ByoasnTypeDef(BaseValidatorModel):
    Asn: Optional[str] = None
    IpamId: Optional[str] = None
    StatusMessage: Optional[str] = None
    State: Optional[AsnStateType] = None

class CancelBundleTaskRequestRequestTypeDef(BaseValidatorModel):
    BundleId: str
    DryRun: Optional[bool] = None

class CancelCapacityReservationFleetErrorTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class CancelCapacityReservationFleetsRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationFleetIds: Sequence[str]
    DryRun: Optional[bool] = None

class CapacityReservationFleetCancellationStateTypeDef(BaseValidatorModel):
    CurrentFleetState: Optional[CapacityReservationFleetStateType] = None
    PreviousFleetState: Optional[CapacityReservationFleetStateType] = None
    CapacityReservationFleetId: Optional[str] = None

class CancelCapacityReservationRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None

class CancelConversionRequestRequestTypeDef(BaseValidatorModel):
    ConversionTaskId: str
    DryRun: Optional[bool] = None
    ReasonMessage: Optional[str] = None

class CancelExportTaskRequestRequestTypeDef(BaseValidatorModel):
    ExportTaskId: str

class CancelImageLaunchPermissionRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None

class CancelImportTaskRequestRequestTypeDef(BaseValidatorModel):
    CancelReason: Optional[str] = None
    DryRun: Optional[bool] = None
    ImportTaskId: Optional[str] = None

class CancelReservedInstancesListingRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstancesListingId: str

class CancelSpotFleetRequestsErrorTypeDef(BaseValidatorModel):
    Code: Optional[CancelBatchErrorCodeType] = None
    Message: Optional[str] = None

class CancelSpotFleetRequestsRequestRequestTypeDef(BaseValidatorModel):
    SpotFleetRequestIds: Sequence[str]
    TerminateInstances: bool
    DryRun: Optional[bool] = None

class CancelSpotFleetRequestsSuccessItemTypeDef(BaseValidatorModel):
    CurrentSpotFleetRequestState: Optional[BatchStateType] = None
    PreviousSpotFleetRequestState: Optional[BatchStateType] = None
    SpotFleetRequestId: Optional[str] = None

class CancelSpotInstanceRequestsRequestRequestTypeDef(BaseValidatorModel):
    SpotInstanceRequestIds: Sequence[str]
    DryRun: Optional[bool] = None

class CancelledSpotInstanceRequestTypeDef(BaseValidatorModel):
    SpotInstanceRequestId: Optional[str] = None
    State: Optional[CancelSpotInstanceRequestStateType] = None

class CapacityAllocationTypeDef(BaseValidatorModel):
    AllocationType: Optional[Literal["used"]] = None
    Count: Optional[int] = None

class CapacityBlockOfferingTypeDef(BaseValidatorModel):
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

class FleetCapacityReservationTypeDef(BaseValidatorModel):
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

class CapacityReservationGroupTypeDef(BaseValidatorModel):
    GroupArn: Optional[str] = None
    OwnerId: Optional[str] = None

class CapacityReservationOptionsRequestTypeDef(BaseValidatorModel):
    UsageStrategy: Optional[Literal["use-capacity-reservations-first"]] = None

class CapacityReservationOptionsTypeDef(BaseValidatorModel):
    UsageStrategy: Optional[Literal["use-capacity-reservations-first"]] = None

class CapacityReservationTargetResponseTypeDef(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class CapacityReservationTargetTypeDef(BaseValidatorModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class CertificateAuthenticationRequestTypeDef(BaseValidatorModel):
    ClientRootCertificateChainArn: Optional[str] = None

class CertificateAuthenticationTypeDef(BaseValidatorModel):
    ClientRootCertificateChain: Optional[str] = None

class CidrAuthorizationContextTypeDef(BaseValidatorModel):
    Message: str
    Signature: str

class CidrBlockTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None

class ClassicLinkDnsSupportTypeDef(BaseValidatorModel):
    ClassicLinkDnsSupported: Optional[bool] = None
    VpcId: Optional[str] = None

class GroupIdentifierTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class ClassicLoadBalancerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class ClientCertificateRevocationListStatusTypeDef(BaseValidatorModel):
    Code: Optional[ClientCertificateRevocationListStatusCodeType] = None
    Message: Optional[str] = None

class ClientConnectOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None

class ClientVpnEndpointAttributeStatusTypeDef(BaseValidatorModel):
    Code: Optional[ClientVpnEndpointAttributeStatusCodeType] = None
    Message: Optional[str] = None

class ClientLoginBannerOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None

class ClientLoginBannerResponseOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None

class DirectoryServiceAuthenticationRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None

class FederatedAuthenticationRequestTypeDef(BaseValidatorModel):
    SAMLProviderArn: Optional[str] = None
    SelfServiceSAMLProviderArn: Optional[str] = None

class DirectoryServiceAuthenticationTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None

class FederatedAuthenticationTypeDef(BaseValidatorModel):
    SamlProviderArn: Optional[str] = None
    SelfServiceSamlProviderArn: Optional[str] = None

class ClientVpnConnectionStatusTypeDef(BaseValidatorModel):
    Code: Optional[ClientVpnConnectionStatusCodeType] = None
    Message: Optional[str] = None

class ClientVpnEndpointStatusTypeDef(BaseValidatorModel):
    Code: Optional[ClientVpnEndpointStatusCodeType] = None
    Message: Optional[str] = None

class ConnectionLogResponseOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None

class ClientVpnRouteStatusTypeDef(BaseValidatorModel):
    Code: Optional[ClientVpnRouteStatusCodeType] = None
    Message: Optional[str] = None

class CloudWatchLogOptionsSpecificationTypeDef(BaseValidatorModel):
    LogEnabled: Optional[bool] = None
    LogGroupArn: Optional[str] = None
    LogOutputFormat: Optional[str] = None

class CloudWatchLogOptionsTypeDef(BaseValidatorModel):
    LogEnabled: Optional[bool] = None
    LogGroupArn: Optional[str] = None
    LogOutputFormat: Optional[str] = None

class CoipAddressUsageTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    CoIp: Optional[str] = None

class CoipCidrTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    CoipPoolId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None

class ConfirmProductInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ProductCode: str
    DryRun: Optional[bool] = None

class ConnectionLogOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None

class ConnectionNotificationTypeDef(BaseValidatorModel):
    ConnectionNotificationId: Optional[str] = None
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    ConnectionNotificationType: Optional[Literal["Topic"]] = None
    ConnectionNotificationArn: Optional[str] = None
    ConnectionEvents: Optional[List[str]] = None
    ConnectionNotificationState: Optional[ConnectionNotificationStateType] = None

class ConnectionTrackingConfigurationTypeDef(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None

class ConnectionTrackingSpecificationRequestTypeDef(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None

class ConnectionTrackingSpecificationResponseTypeDef(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None

class ConnectionTrackingSpecificationTypeDef(BaseValidatorModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None

class CopyFpgaImageRequestRequestTypeDef(BaseValidatorModel):
    SourceFpgaImageId: str
    SourceRegion: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None

class CpuOptionsRequestTypeDef(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class CpuOptionsTypeDef(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class ReservationFleetInstanceSpecificationTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    InstancePlatform: Optional[CapacityReservationInstancePlatformType] = None
    Weight: Optional[float] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    Priority: Optional[int] = None

class CreateClientVpnRouteRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    DestinationCidrBlock: str
    TargetVpcSubnetId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class CreateCoipCidrRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    CoipPoolId: str
    DryRun: Optional[bool] = None

class CreateDefaultSubnetRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZone: str
    DryRun: Optional[bool] = None
    Ipv6Native: Optional[bool] = None

class CreateDefaultVpcRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class NewDhcpConfigurationTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class TargetCapacitySpecificationRequestTypeDef(BaseValidatorModel):
    TotalTargetCapacity: int
    OnDemandTargetCapacity: Optional[int] = None
    SpotTargetCapacity: Optional[int] = None
    DefaultTargetCapacityType: Optional[DefaultTargetCapacityTypeType] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None

class DestinationOptionsRequestTypeDef(BaseValidatorModel):
    FileFormat: Optional[DestinationFileFormatType] = None
    HiveCompatiblePartitions: Optional[bool] = None
    PerHourPartition: Optional[bool] = None

class StorageLocationTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class InstanceEventWindowTimeRangeRequestTypeDef(BaseValidatorModel):
    StartWeekDay: Optional[WeekDayType] = None
    StartHour: Optional[int] = None
    EndWeekDay: Optional[WeekDayType] = None
    EndHour: Optional[int] = None

class ExportToS3TaskSpecificationTypeDef(BaseValidatorModel):
    ContainerFormat: Optional[Literal["ova"]] = None
    DiskImageFormat: Optional[DiskImageFormatType] = None
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None

class IpamPoolSourceResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal["vpc"]] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None

class RequestIpamResourceTagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class CreateLocalGatewayRouteRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None

class LocalGatewayRouteTypeDef(BaseValidatorModel):
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

class IcmpTypeCodeTypeDef(BaseValidatorModel):
    Code: Optional[int] = None
    Type: Optional[int] = None

class CreateNetworkInterfacePermissionRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    Permission: InterfacePermissionTypeType
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    DryRun: Optional[bool] = None

class InstanceIpv6AddressTypeDef(BaseValidatorModel):
    Ipv6Address: Optional[str] = None
    IsPrimaryIpv6: Optional[bool] = None

class Ipv4PrefixSpecificationRequestTypeDef(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None

class Ipv6PrefixSpecificationRequestTypeDef(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None

class PrivateIpAddressSpecificationTypeDef(BaseValidatorModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None

class PriceScheduleSpecificationTypeDef(BaseValidatorModel):
    CurrencyCode: Optional[Literal["USD"]] = None
    Price: Optional[float] = None
    Term: Optional[int] = None

class CreateRouteRequestRequestTypeDef(BaseValidatorModel):
    RouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None
    VpcEndpointId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    NatGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None

class CreateRouteRequestRouteTableCreateRouteTypeDef(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None
    VpcEndpointId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    NatGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None

class InstanceSpecificationTypeDef(BaseValidatorModel):
    InstanceId: str
    ExcludeBootVolume: Optional[bool] = None
    ExcludeDataVolumeIds: Optional[Sequence[str]] = None

class CreateSpotDatafeedSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    DryRun: Optional[bool] = None
    Prefix: Optional[str] = None

class S3ObjectTagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class TrafficMirrorPortRangeRequestTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class TransitGatewayConnectRequestBgpOptionsTypeDef(BaseValidatorModel):
    PeerAsn: Optional[int] = None

class CreateTransitGatewayConnectRequestOptionsTypeDef(BaseValidatorModel):
    Protocol: Literal["gre"]

class CreateTransitGatewayMulticastDomainRequestOptionsTypeDef(BaseValidatorModel):
    Igmpv2Support: Optional[Igmpv2SupportValueType] = None
    StaticSourcesSupport: Optional[StaticSourcesSupportValueType] = None
    AutoAcceptSharedAssociations: Optional[AutoAcceptSharedAssociationsValueType] = None

class CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef(BaseValidatorModel):
    DynamicRouting: Optional[DynamicRoutingValueType] = None

class CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class TransitGatewayRequestOptionsTypeDef(BaseValidatorModel):
    AmazonSideAsn: Optional[int] = None
    AutoAcceptSharedAttachments: Optional[AutoAcceptSharedAttachmentsValueType] = None
    DefaultRouteTableAssociation: Optional[DefaultRouteTableAssociationValueType] = None
    DefaultRouteTablePropagation: Optional[DefaultRouteTablePropagationValueType] = None
    VpnEcmpSupport: Optional[VpnEcmpSupportValueType] = None
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    MulticastSupport: Optional[MulticastSupportValueType] = None
    TransitGatewayCidrBlocks: Optional[Sequence[str]] = None

class CreateTransitGatewayRouteRequestRequestTypeDef(BaseValidatorModel):
    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef(BaseValidatorModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None

class CreateVerifiedAccessEndpointEniOptionsTypeDef(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    LoadBalancerArn: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None

class VerifiedAccessSseSpecificationRequestTypeDef(BaseValidatorModel):
    CustomerManagedKeyEnabled: Optional[bool] = None
    KmsKeyArn: Optional[str] = None

class CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef(BaseValidatorModel):
    TenantId: Optional[str] = None
    PublicSigningKeyUrl: Optional[str] = None

class CreateVerifiedAccessTrustProviderOidcOptionsTypeDef(BaseValidatorModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None

class CreateVolumePermissionTypeDef(BaseValidatorModel):
    Group: Optional[Literal["all"]] = None
    UserId: Optional[str] = None

class CreateVpcEndpointConnectionNotificationRequestRequestTypeDef(BaseValidatorModel):
    ConnectionNotificationArn: str
    ConnectionEvents: Sequence[str]
    DryRun: Optional[bool] = None
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    ClientToken: Optional[str] = None

class DnsOptionsSpecificationTypeDef(BaseValidatorModel):
    DnsRecordIpType: Optional[DnsRecordIpTypeType] = None
    PrivateDnsOnlyForInboundResolverEndpoint: Optional[bool] = None

class SubnetConfigurationTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    Ipv4: Optional[str] = None
    Ipv6: Optional[str] = None

class CreateVpnConnectionRouteRequestRequestTypeDef(BaseValidatorModel):
    DestinationCidrBlock: str
    VpnConnectionId: str

class CreditSpecificationRequestTypeDef(BaseValidatorModel):
    CpuCredits: str

class CreditSpecificationTypeDef(BaseValidatorModel):
    CpuCredits: Optional[str] = None

class DataQueryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    Period: Optional[PeriodTypeType] = None

class MetricPointTypeDef(BaseValidatorModel):
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    Value: Optional[float] = None
    Status: Optional[str] = None

class DeleteCarrierGatewayRequestRequestTypeDef(BaseValidatorModel):
    CarrierGatewayId: str
    DryRun: Optional[bool] = None

class DeleteClientVpnEndpointRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None

class DeleteClientVpnRouteRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    DestinationCidrBlock: str
    TargetVpcSubnetId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteCoipCidrRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    CoipPoolId: str
    DryRun: Optional[bool] = None

class DeleteCoipPoolRequestRequestTypeDef(BaseValidatorModel):
    CoipPoolId: str
    DryRun: Optional[bool] = None

class DeleteCustomerGatewayRequestRequestTypeDef(BaseValidatorModel):
    CustomerGatewayId: str
    DryRun: Optional[bool] = None

class DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteDhcpOptionsRequestRequestTypeDef(BaseValidatorModel):
    DhcpOptionsId: str
    DryRun: Optional[bool] = None

class DeleteEgressOnlyInternetGatewayRequestRequestTypeDef(BaseValidatorModel):
    EgressOnlyInternetGatewayId: str
    DryRun: Optional[bool] = None

class DeleteFleetErrorTypeDef(BaseValidatorModel):
    Code: Optional[DeleteFleetErrorCodeType] = None
    Message: Optional[str] = None

class DeleteFleetSuccessItemTypeDef(BaseValidatorModel):
    CurrentFleetState: Optional[FleetStateCodeType] = None
    PreviousFleetState: Optional[FleetStateCodeType] = None
    FleetId: Optional[str] = None

class DeleteFleetsRequestRequestTypeDef(BaseValidatorModel):
    FleetIds: Sequence[str]
    TerminateInstances: bool
    DryRun: Optional[bool] = None

class DeleteFlowLogsRequestRequestTypeDef(BaseValidatorModel):
    FlowLogIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteFpgaImageRequestRequestTypeDef(BaseValidatorModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None

class DeleteInstanceConnectEndpointRequestRequestTypeDef(BaseValidatorModel):
    InstanceConnectEndpointId: str
    DryRun: Optional[bool] = None

class DeleteInstanceEventWindowRequestRequestTypeDef(BaseValidatorModel):
    InstanceEventWindowId: str
    DryRun: Optional[bool] = None
    ForceDelete: Optional[bool] = None

class InstanceEventWindowStateChangeTypeDef(BaseValidatorModel):
    InstanceEventWindowId: Optional[str] = None
    State: Optional[InstanceEventWindowStateType] = None

class DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteInternetGatewayRequestRequestTypeDef(BaseValidatorModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None

class DeleteIpamPoolRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cascade: Optional[bool] = None

class DeleteIpamRequestRequestTypeDef(BaseValidatorModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Cascade: Optional[bool] = None

class DeleteIpamResourceDiscoveryRequestRequestTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None

class DeleteIpamScopeRequestRequestTypeDef(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None

class DeleteKeyPairRequestKeyPairDeleteTypeDef(BaseValidatorModel):
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteKeyPairRequestKeyPairInfoDeleteTypeDef(BaseValidatorModel):
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteKeyPairRequestRequestTypeDef(BaseValidatorModel):
    KeyName: Optional[str] = None
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteLaunchTemplateRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None

class DeleteLaunchTemplateVersionsRequestRequestTypeDef(BaseValidatorModel):
    Versions: Sequence[str]
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None

class ResponseErrorTypeDef(BaseValidatorModel):
    Code: Optional[LaunchTemplateErrorCodeType] = None
    Message: Optional[str] = None

class DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None

class DeleteLocalGatewayRouteRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationPrefixListId: Optional[str] = None

class DeleteLocalGatewayRouteTableRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DryRun: Optional[bool] = None

class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str
    DryRun: Optional[bool] = None

class DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationId: str
    DryRun: Optional[bool] = None

class DeleteManagedPrefixListRequestRequestTypeDef(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None

class DeleteNatGatewayRequestRequestTypeDef(BaseValidatorModel):
    NatGatewayId: str
    DryRun: Optional[bool] = None

class DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef(BaseValidatorModel):
    Egress: bool
    RuleNumber: int
    DryRun: Optional[bool] = None

class DeleteNetworkAclEntryRequestRequestTypeDef(BaseValidatorModel):
    Egress: bool
    NetworkAclId: str
    RuleNumber: int
    DryRun: Optional[bool] = None

class DeleteNetworkAclRequestNetworkAclDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteNetworkAclRequestRequestTypeDef(BaseValidatorModel):
    NetworkAclId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsAccessScopeRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsAnalysisRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAnalysisId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsPathRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsPathId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInterfacePermissionRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfacePermissionId: str
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None

class DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteNetworkInterfaceRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None

class DeletePlacementGroupRequestPlacementGroupDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeletePlacementGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    DryRun: Optional[bool] = None

class DeletePublicIpv4PoolRequestRequestTypeDef(BaseValidatorModel):
    PoolId: str
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class DeleteQueuedReservedInstancesErrorTypeDef(BaseValidatorModel):
    Code: Optional[DeleteQueuedReservedInstancesErrorCodeType] = None
    Message: Optional[str] = None

class DeleteQueuedReservedInstancesRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstancesIds: Sequence[str]
    DryRun: Optional[bool] = None

class SuccessfulQueuedPurchaseDeletionTypeDef(BaseValidatorModel):
    ReservedInstancesId: Optional[str] = None

class DeleteRouteRequestRequestTypeDef(BaseValidatorModel):
    RouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteRouteRequestRouteDeleteTypeDef(BaseValidatorModel):
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteRouteTableRequestRequestTypeDef(BaseValidatorModel):
    RouteTableId: str
    DryRun: Optional[bool] = None

class DeleteRouteTableRequestRouteTableDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteSecurityGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteSnapshotRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    DryRun: Optional[bool] = None

class DeleteSnapshotRequestSnapshotDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteSpotDatafeedSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteSubnetCidrReservationRequestRequestTypeDef(BaseValidatorModel):
    SubnetCidrReservationId: str
    DryRun: Optional[bool] = None

class DeleteSubnetRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    DryRun: Optional[bool] = None

class DeleteSubnetRequestSubnetDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteTagsRequestTagDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorFilterRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorFilterId: str
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorFilterRuleRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRuleId: str
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorSessionRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorSessionId: str
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorTargetRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorTargetId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeerId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayConnectRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayMulticastDomainRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayPolicyTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRouteRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    DestinationCidrBlock: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncementId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRouteTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DeleteVerifiedAccessEndpointRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteVerifiedAccessGroupRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessGroupId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteVerifiedAccessInstanceRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class DeleteVerifiedAccessTrustProviderRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProviderId: str
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class DeleteVolumeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    DryRun: Optional[bool] = None

class DeleteVolumeRequestVolumeDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef(BaseValidatorModel):
    ConnectionNotificationIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    ServiceIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteVpcEndpointsRequestRequestTypeDef(BaseValidatorModel):
    VpcEndpointIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteVpcPeeringConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None

class DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteVpcRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DeleteVpcRequestVpcDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeleteVpnConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    DryRun: Optional[bool] = None

class DeleteVpnConnectionRouteRequestRequestTypeDef(BaseValidatorModel):
    DestinationCidrBlock: str
    VpnConnectionId: str

class DeleteVpnGatewayRequestRequestTypeDef(BaseValidatorModel):
    VpnGatewayId: str
    DryRun: Optional[bool] = None

class DeprovisionByoipCidrRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    DryRun: Optional[bool] = None

class DeprovisionIpamByoasnRequestRequestTypeDef(BaseValidatorModel):
    IpamId: str
    Asn: str
    DryRun: Optional[bool] = None

class DeprovisionIpamPoolCidrRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None

class DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef(BaseValidatorModel):
    PoolId: str
    Cidr: str
    DryRun: Optional[bool] = None

class DeregisterImageRequestImageDeregisterTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DeregisterImageRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DeregisterInstanceTagAttributeRequestTypeDef(BaseValidatorModel):
    IncludeAllTagsOfInstance: Optional[bool] = None
    InstanceTagKeys: Optional[Sequence[str]] = None

class InstanceTagNotificationAttributeTypeDef(BaseValidatorModel):
    InstanceTagKeys: Optional[List[str]] = None
    IncludeAllTagsOfInstance: Optional[bool] = None

class DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    GroupIpAddress: Optional[str] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastDeregisteredGroupMembersTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    DeregisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    GroupIpAddress: Optional[str] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastDeregisteredGroupSourcesTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    DeregisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class DescribeAccountAttributesRequestRequestTypeDef(BaseValidatorModel):
    AttributeNames: Optional[Sequence[AccountAttributeNameType]] = None
    DryRun: Optional[bool] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAddressTransfersRequestRequestTypeDef(BaseValidatorModel):
    AllocationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class DescribeAddressesAttributeRequestRequestTypeDef(BaseValidatorModel):
    AllocationIds: Optional[Sequence[str]] = None
    Attribute: Optional[Literal["domain-name"]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class FilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DescribeAggregateIdFormatRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class IdFormatTypeDef(BaseValidatorModel):
    Deadline: Optional[datetime] = None
    Resource: Optional[str] = None
    UseLongIds: Optional[bool] = None

class SubscriptionTypeDef(BaseValidatorModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    Period: Optional[PeriodTypeType] = None

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeByoipCidrsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: int
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeConversionTasksRequestRequestTypeDef(BaseValidatorModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class FastLaunchLaunchTemplateSpecificationResponseTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class FastLaunchSnapshotConfigurationResponseTypeDef(BaseValidatorModel):
    TargetResourceCount: Optional[int] = None

class DescribeFastSnapshotRestoreSuccessItemTypeDef(BaseValidatorModel):
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

class DescribeFpgaImageAttributeRequestRequestTypeDef(BaseValidatorModel):
    FpgaImageId: str
    Attribute: FpgaImageAttributeNameType
    DryRun: Optional[bool] = None

class HostOfferingTypeDef(BaseValidatorModel):
    CurrencyCode: Optional[Literal["USD"]] = None
    Duration: Optional[int] = None
    HourlyPrice: Optional[str] = None
    InstanceFamily: Optional[str] = None
    OfferingId: Optional[str] = None
    PaymentOption: Optional[PaymentOptionType] = None
    UpfrontPrice: Optional[str] = None

class DescribeIdFormatRequestRequestTypeDef(BaseValidatorModel):
    Resource: Optional[str] = None

class DescribeIdentityIdFormatRequestRequestTypeDef(BaseValidatorModel):
    PrincipalArn: str
    Resource: Optional[str] = None

class DescribeImageAttributeRequestImageDescribeAttributeTypeDef(BaseValidatorModel):
    Attribute: ImageAttributeNameType
    DryRun: Optional[bool] = None

class DescribeImageAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: ImageAttributeNameType
    ImageId: str
    DryRun: Optional[bool] = None

class DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef(BaseValidatorModel):
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None

class DescribeInstanceAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: InstanceAttributeNameType
    InstanceId: str
    DryRun: Optional[bool] = None

class InstanceCreditSpecificationTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    CpuCredits: Optional[str] = None

class DescribeInstanceEventNotificationAttributesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class InstanceTopologyTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    GroupName: Optional[str] = None
    NetworkNodes: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None
    ZoneId: Optional[str] = None

class InstanceTypeOfferingTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    LocationType: Optional[LocationTypeType] = None
    Location: Optional[str] = None

class DescribeIpamByoasnRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LockedSnapshotsInfoTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    SnapshotId: Optional[str] = None
    LockState: Optional[LockStateType] = None
    LockDuration: Optional[int] = None
    CoolOffPeriod: Optional[int] = None
    CoolOffPeriodExpiresOn: Optional[datetime] = None
    LockCreatedOn: Optional[datetime] = None
    LockDurationStartTime: Optional[datetime] = None
    LockExpiresOn: Optional[datetime] = None

class MacHostTypeDef(BaseValidatorModel):
    HostId: Optional[str] = None
    MacOSLatestSupportedVersions: Optional[List[str]] = None

class MovingAddressStatusTypeDef(BaseValidatorModel):
    MoveStatus: Optional[MoveStatusType] = None
    PublicIp: Optional[str] = None

class DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef(BaseValidatorModel):
    Attribute: Optional[NetworkInterfaceAttributeType] = None
    DryRun: Optional[bool] = None

class DescribeNetworkInterfaceAttributeRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    Attribute: Optional[NetworkInterfaceAttributeType] = None
    DryRun: Optional[bool] = None

class PrefixListTypeDef(BaseValidatorModel):
    Cidrs: Optional[List[str]] = None
    PrefixListId: Optional[str] = None
    PrefixListName: Optional[str] = None

class DescribePrincipalIdFormatRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Resources: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RegionTypeDef(BaseValidatorModel):
    Endpoint: Optional[str] = None
    RegionName: Optional[str] = None
    OptInStatus: Optional[str] = None

class ScheduledInstanceRecurrenceRequestTypeDef(BaseValidatorModel):
    Frequency: Optional[str] = None
    Interval: Optional[int] = None
    OccurrenceDays: Optional[Sequence[int]] = None
    OccurrenceRelativeToEnd: Optional[bool] = None
    OccurrenceUnit: Optional[str] = None

class DescribeSecurityGroupReferencesRequestRequestTypeDef(BaseValidatorModel):
    GroupId: Sequence[str]
    DryRun: Optional[bool] = None

class SecurityGroupReferenceTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    ReferencingVpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    TransitGatewayId: Optional[str] = None

class DescribeSnapshotAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    SnapshotId: str
    DryRun: Optional[bool] = None

class DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    DryRun: Optional[bool] = None

class ProductCodeTypeDef(BaseValidatorModel):
    ProductCodeId: Optional[str] = None
    ProductCodeType: Optional[ProductCodeValuesType] = None

class DescribeSpotDatafeedSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DescribeSpotFleetInstancesRequestRequestTypeDef(BaseValidatorModel):
    SpotFleetRequestId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SpotFleetRequestIds: Optional[Sequence[str]] = None

class SpotPriceTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    SpotPrice: Optional[str] = None
    Timestamp: Optional[datetime] = None

class DescribeStaleSecurityGroupsRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class StoreImageTaskResultTypeDef(BaseValidatorModel):
    AmiId: Optional[str] = None
    TaskStartTime: Optional[datetime] = None
    Bucket: Optional[str] = None
    S3objectKey: Optional[str] = None
    ProgressPercentage: Optional[int] = None
    StoreTaskState: Optional[str] = None
    StoreTaskFailureReason: Optional[str] = None

class TagDescriptionTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    Value: Optional[str] = None

class DescribeVolumeAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: VolumeAttributeNameType
    VolumeId: str
    DryRun: Optional[bool] = None

class DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef(BaseValidatorModel):
    Attribute: VolumeAttributeNameType
    DryRun: Optional[bool] = None

class VolumeModificationTypeDef(BaseValidatorModel):
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

class DescribeVpcAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: VpcAttributeNameType
    VpcId: str
    DryRun: Optional[bool] = None

class DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef(BaseValidatorModel):
    Attribute: VpcAttributeNameType
    DryRun: Optional[bool] = None

class DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None

class DestinationOptionsResponseTypeDef(BaseValidatorModel):
    FileFormat: Optional[DestinationFileFormatType] = None
    HiveCompatiblePartitions: Optional[bool] = None
    PerHourPartition: Optional[bool] = None

class DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DetachClassicLinkVpcRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    VpcId: str
    DryRun: Optional[bool] = None

class DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DetachInternetGatewayRequestRequestTypeDef(BaseValidatorModel):
    InternetGatewayId: str
    VpcId: str
    DryRun: Optional[bool] = None

class DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef(BaseValidatorModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None

class DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef(BaseValidatorModel):
    AttachmentId: str
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class DetachNetworkInterfaceRequestRequestTypeDef(BaseValidatorModel):
    AttachmentId: str
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class DetachVerifiedAccessTrustProviderRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    VerifiedAccessTrustProviderId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DetachVolumeRequestInstanceDetachVolumeTypeDef(BaseValidatorModel):
    VolumeId: str
    Device: Optional[str] = None
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None

class DetachVolumeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    Device: Optional[str] = None
    Force: Optional[bool] = None
    InstanceId: Optional[str] = None
    DryRun: Optional[bool] = None

class DetachVolumeRequestVolumeDetachFromInstanceTypeDef(BaseValidatorModel):
    Device: Optional[str] = None
    Force: Optional[bool] = None
    InstanceId: Optional[str] = None
    DryRun: Optional[bool] = None

class DetachVpnGatewayRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    VpnGatewayId: str
    DryRun: Optional[bool] = None

class DeviceOptionsTypeDef(BaseValidatorModel):
    TenantId: Optional[str] = None
    PublicSigningKeyUrl: Optional[str] = None

class DisableAddressTransferRequestRequestTypeDef(BaseValidatorModel):
    AllocationId: str
    DryRun: Optional[bool] = None

class DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    DryRun: Optional[bool] = None

class DisableEbsEncryptionByDefaultRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DisableFastLaunchRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None

class DisableFastSnapshotRestoreStateErrorTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class DisableFastSnapshotRestoreSuccessItemTypeDef(BaseValidatorModel):
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

class DisableFastSnapshotRestoresRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZones: Sequence[str]
    SourceSnapshotIds: Sequence[str]
    DryRun: Optional[bool] = None

class DisableImageBlockPublicAccessRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DisableImageDeprecationRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DisableImageDeregistrationProtectionRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DisableImageRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DisableIpamOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    DelegatedAdminAccountId: str
    DryRun: Optional[bool] = None

class DisableSerialConsoleAccessRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DisableSnapshotBlockPublicAccessRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    DryRun: Optional[bool] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class TransitGatewayPropagationTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayPropagationStateType] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class DisableVgwRoutePropagationRequestRequestTypeDef(BaseValidatorModel):
    GatewayId: str
    RouteTableId: str
    DryRun: Optional[bool] = None

class DisableVpcClassicLinkDnsSupportRequestRequestTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None

class DisableVpcClassicLinkRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DisassociateAddressRequestClassicAddressDisassociateTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef(BaseValidatorModel):
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateAddressRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateClientVpnTargetNetworkRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    AssociationId: str
    DryRun: Optional[bool] = None

class DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    RoleArn: str
    DryRun: Optional[bool] = None

class DisassociateIamInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: str

class DisassociateIpamByoasnRequestRequestTypeDef(BaseValidatorModel):
    Asn: str
    Cidr: str
    DryRun: Optional[bool] = None

class DisassociateIpamResourceDiscoveryRequestRequestTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryAssociationId: str
    DryRun: Optional[bool] = None

class DisassociateNatGatewayAddressRequestRequestTypeDef(BaseValidatorModel):
    NatGatewayId: str
    AssociationIds: Sequence[str]
    MaxDrainDurationSeconds: Optional[int] = None
    DryRun: Optional[bool] = None

class DisassociateRouteTableRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    DryRun: Optional[bool] = None

class DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef(BaseValidatorModel):
    AssociationId: str
    DryRun: Optional[bool] = None

class DisassociateSubnetCidrBlockRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: str

class DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    TransitGatewayAttachmentId: str
    SubnetIds: Sequence[str]
    DryRun: Optional[bool] = None

class DisassociateTransitGatewayPolicyTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DisassociateTransitGatewayRouteTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DisassociateTrunkInterfaceRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateVpcCidrBlockRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: str

class DiskImageDescriptionTypeDef(BaseValidatorModel):
    Checksum: Optional[str] = None
    Format: Optional[DiskImageFormatType] = None
    ImportManifestUrl: Optional[str] = None
    Size: Optional[int] = None

class DiskImageDetailTypeDef(BaseValidatorModel):
    Bytes: int
    Format: DiskImageFormatType
    ImportManifestUrl: str

class VolumeDetailTypeDef(BaseValidatorModel):
    Size: int

class DiskImageVolumeDescriptionTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Size: Optional[int] = None

class DiskInfoTypeDef(BaseValidatorModel):
    SizeInGB: Optional[int] = None
    Count: Optional[int] = None
    Type: Optional[DiskTypeType] = None

class DnsEntryTypeDef(BaseValidatorModel):
    DnsName: Optional[str] = None
    HostedZoneId: Optional[str] = None

class DnsOptionsTypeDef(BaseValidatorModel):
    DnsRecordIpType: Optional[DnsRecordIpTypeType] = None
    PrivateDnsOnlyForInboundResolverEndpoint: Optional[bool] = None

class DnsServersOptionsModifyStructureTypeDef(BaseValidatorModel):
    CustomDnsServers: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class EbsOptimizedInfoTypeDef(BaseValidatorModel):
    BaselineBandwidthInMbps: Optional[int] = None
    BaselineThroughputInMBps: Optional[float] = None
    BaselineIops: Optional[int] = None
    MaximumBandwidthInMbps: Optional[int] = None
    MaximumThroughputInMBps: Optional[float] = None
    MaximumIops: Optional[int] = None

class EbsInstanceBlockDeviceSpecificationTypeDef(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    VolumeId: Optional[str] = None

class EbsInstanceBlockDeviceTypeDef(BaseValidatorModel):
    AttachTime: Optional[datetime] = None
    DeleteOnTermination: Optional[bool] = None
    Status: Optional[AttachmentStatusType] = None
    VolumeId: Optional[str] = None
    AssociatedResource: Optional[str] = None
    VolumeOwnerId: Optional[str] = None

class EfaInfoTypeDef(BaseValidatorModel):
    MaximumEfaInterfaces: Optional[int] = None

class InternetGatewayAttachmentTypeDef(BaseValidatorModel):
    State: Optional[AttachmentStatusType] = None
    VpcId: Optional[str] = None

class ElasticGpuAssociationTypeDef(BaseValidatorModel):
    ElasticGpuId: Optional[str] = None
    ElasticGpuAssociationId: Optional[str] = None
    ElasticGpuAssociationState: Optional[str] = None
    ElasticGpuAssociationTime: Optional[str] = None

class ElasticGpuHealthTypeDef(BaseValidatorModel):
    Status: Optional[ElasticGpuStatusType] = None

class ElasticGpuSpecificationResponseTypeDef(BaseValidatorModel):
    Type: Optional[str] = None

class ElasticGpuSpecificationTypeDef(BaseValidatorModel):
    Type: str

class ElasticInferenceAcceleratorAssociationTypeDef(BaseValidatorModel):
    ElasticInferenceAcceleratorArn: Optional[str] = None
    ElasticInferenceAcceleratorAssociationId: Optional[str] = None
    ElasticInferenceAcceleratorAssociationState: Optional[str] = None
    ElasticInferenceAcceleratorAssociationTime: Optional[datetime] = None

class ElasticInferenceAcceleratorTypeDef(BaseValidatorModel):
    Type: str
    Count: Optional[int] = None

class EnaSrdUdpSpecificationRequestTypeDef(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class EnaSrdUdpSpecificationTypeDef(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class EnableAddressTransferRequestRequestTypeDef(BaseValidatorModel):
    AllocationId: str
    TransferAccountId: str
    DryRun: Optional[bool] = None

class EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    DryRun: Optional[bool] = None

class EnableEbsEncryptionByDefaultRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class FastLaunchLaunchTemplateSpecificationRequestTypeDef(BaseValidatorModel):
    Version: str
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None

class FastLaunchSnapshotConfigurationRequestTypeDef(BaseValidatorModel):
    TargetResourceCount: Optional[int] = None

class EnableFastSnapshotRestoreStateErrorTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class EnableFastSnapshotRestoreSuccessItemTypeDef(BaseValidatorModel):
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

class EnableFastSnapshotRestoresRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZones: Sequence[str]
    SourceSnapshotIds: Sequence[str]
    DryRun: Optional[bool] = None

class EnableImageBlockPublicAccessRequestRequestTypeDef(BaseValidatorModel):
    ImageBlockPublicAccessState: Literal["block-new-sharing"]
    DryRun: Optional[bool] = None

class EnableImageDeregistrationProtectionRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    WithCooldown: Optional[bool] = None
    DryRun: Optional[bool] = None

class EnableImageRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None

class EnableIpamOrganizationAdminAccountRequestRequestTypeDef(BaseValidatorModel):
    DelegatedAdminAccountId: str
    DryRun: Optional[bool] = None

class EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class EnableSerialConsoleAccessRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class EnableSnapshotBlockPublicAccessRequestRequestTypeDef(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    DryRun: Optional[bool] = None

class EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    DryRun: Optional[bool] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class EnableVgwRoutePropagationRequestRequestTypeDef(BaseValidatorModel):
    GatewayId: str
    RouteTableId: str
    DryRun: Optional[bool] = None

class EnableVolumeIORequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    DryRun: Optional[bool] = None

class EnableVolumeIORequestVolumeEnableIoTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class EnableVpcClassicLinkDnsSupportRequestRequestTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None

class EnableVpcClassicLinkRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None

class EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class EnclaveOptionsRequestTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class EnclaveOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class EventInformationTypeDef(BaseValidatorModel):
    EventDescription: Optional[str] = None
    EventSubType: Optional[str] = None
    InstanceId: Optional[str] = None

class TransitGatewayRouteTableRouteTypeDef(BaseValidatorModel):
    DestinationCidr: Optional[str] = None
    State: Optional[str] = None
    RouteOrigin: Optional[str] = None
    PrefixListId: Optional[str] = None
    AttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None

class ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None

class ExportClientVpnClientConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None

class ExportTaskS3LocationRequestTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3Prefix: Optional[str] = None

class ExportTaskS3LocationTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None

class ExportToS3TaskTypeDef(BaseValidatorModel):
    ContainerFormat: Optional[Literal["ova"]] = None
    DiskImageFormat: Optional[DiskImageFormatType] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None

class InstanceExportDetailsTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    TargetEnvironment: Optional[ExportEnvironmentType] = None

class FilterPortRangeTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class TargetCapacitySpecificationTypeDef(BaseValidatorModel):
    TotalTargetCapacity: Optional[int] = None
    OnDemandTargetCapacity: Optional[int] = None
    SpotTargetCapacity: Optional[int] = None
    DefaultTargetCapacityType: Optional[DefaultTargetCapacityTypeType] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None

class FleetLaunchTemplateSpecificationRequestTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class FleetLaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class PlacementTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    PartitionNumber: Optional[int] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    GroupId: Optional[str] = None

class PlacementResponseTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None

class FleetSpotCapacityRebalanceRequestTypeDef(BaseValidatorModel):
    ReplacementStrategy: Optional[FleetReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None

class FleetSpotCapacityRebalanceTypeDef(BaseValidatorModel):
    ReplacementStrategy: Optional[FleetReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None

class FpgaDeviceMemoryInfoTypeDef(BaseValidatorModel):
    SizeInMiB: Optional[int] = None

class LoadPermissionTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None
    Group: Optional[Literal["all"]] = None

class FpgaImageStateTypeDef(BaseValidatorModel):
    Code: Optional[FpgaImageStateCodeType] = None
    Message: Optional[str] = None

class PciIdTypeDef(BaseValidatorModel):
    DeviceId: Optional[str] = None
    VendorId: Optional[str] = None
    SubsystemId: Optional[str] = None
    SubsystemVendorId: Optional[str] = None

class GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef(BaseValidatorModel):
    CertificateArn: str
    DryRun: Optional[bool] = None

class GetAssociatedIpv6PoolCidrsRequestRequestTypeDef(BaseValidatorModel):
    PoolId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class Ipv6CidrAssociationTypeDef(BaseValidatorModel):
    Ipv6Cidr: Optional[str] = None
    AssociatedResource: Optional[str] = None

class GetCapacityReservationUsageRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class InstanceUsageTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    UsedInstanceCount: Optional[int] = None

class GetConsoleOutputRequestInstanceConsoleOutputTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Latest: Optional[bool] = None

class GetConsoleOutputRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    Latest: Optional[bool] = None

class GetConsoleScreenshotRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    WakeUp: Optional[bool] = None

class GetDefaultCreditSpecificationRequestRequestTypeDef(BaseValidatorModel):
    InstanceFamily: UnlimitedSupportedInstanceFamilyType
    DryRun: Optional[bool] = None

class InstanceFamilyCreditSpecificationTypeDef(BaseValidatorModel):
    InstanceFamily: Optional[UnlimitedSupportedInstanceFamilyType] = None
    CpuCredits: Optional[str] = None

class GetEbsDefaultKmsKeyIdRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class GetEbsEncryptionByDefaultRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class GetGroupsForCapacityReservationRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class GetHostReservationPurchasePreviewRequestRequestTypeDef(BaseValidatorModel):
    HostIdSet: Sequence[str]
    OfferingId: str

class PurchaseTypeDef(BaseValidatorModel):
    CurrencyCode: Optional[Literal["USD"]] = None
    Duration: Optional[int] = None
    HostIdSet: Optional[List[str]] = None
    HostReservationId: Optional[str] = None
    HourlyPrice: Optional[str] = None
    InstanceFamily: Optional[str] = None
    PaymentOption: Optional[PaymentOptionType] = None
    UpfrontPrice: Optional[str] = None

class GetImageBlockPublicAccessStateRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class GetInstanceMetadataDefaultsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class InstanceMetadataDefaultsResponseTypeDef(BaseValidatorModel):
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class GetInstanceTpmEkPubRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    KeyType: EkPubKeyTypeType
    KeyFormat: EkPubKeyFormatType
    DryRun: Optional[bool] = None

class InstanceTypeInfoFromInstanceRequirementsTypeDef(BaseValidatorModel):
    InstanceType: Optional[str] = None

class GetInstanceUefiDataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class IpamAddressHistoryRecordTypeDef(BaseValidatorModel):
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

class GetLaunchTemplateDataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class GetManagedPrefixListAssociationsRequestRequestTypeDef(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrefixListAssociationTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceOwner: Optional[str] = None

class GetManagedPrefixListEntriesRequestRequestTypeDef(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    TargetVersion: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrefixListEntryTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    Description: Optional[str] = None

class GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetNetworkInsightsAccessScopeContentRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    DryRun: Optional[bool] = None

class GetPasswordDataRequestInstancePasswordDataTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class GetPasswordDataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class ReservationValueTypeDef(BaseValidatorModel):
    HourlyPrice: Optional[str] = None
    RemainingTotalValue: Optional[str] = None
    RemainingUpfrontValue: Optional[str] = None

class GetSerialConsoleAccessStatusRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class GetSnapshotBlockPublicAccessStateRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class SpotPlacementScoreTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Score: Optional[int] = None

class TransitGatewayAttachmentPropagationTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayPropagationStateType] = None

class TransitGatewayRouteTableAssociationTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class TransitGatewayRouteTablePropagationTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayPropagationStateType] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class GetVerifiedAccessEndpointPolicyRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    DryRun: Optional[bool] = None

class GetVerifiedAccessGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessGroupId: str
    DryRun: Optional[bool] = None

class GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    VpnConnectionDeviceTypeId: str
    InternetKeyExchangeVersion: Optional[str] = None
    DryRun: Optional[bool] = None

class GetVpnConnectionDeviceTypesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class VpnConnectionDeviceTypeTypeDef(BaseValidatorModel):
    VpnConnectionDeviceTypeId: Optional[str] = None
    Vendor: Optional[str] = None
    Platform: Optional[str] = None
    Software: Optional[str] = None

class GetVpnTunnelReplacementStatusRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    DryRun: Optional[bool] = None

class MaintenanceDetailsTypeDef(BaseValidatorModel):
    PendingMaintenance: Optional[str] = None
    MaintenanceAutoAppliedAfter: Optional[datetime] = None
    LastMaintenanceApplied: Optional[datetime] = None

class GpuDeviceMemoryInfoTypeDef(BaseValidatorModel):
    SizeInMiB: Optional[int] = None

class HibernationOptionsRequestTypeDef(BaseValidatorModel):
    Configured: Optional[bool] = None

class HibernationOptionsTypeDef(BaseValidatorModel):
    Configured: Optional[bool] = None

class HostInstanceTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    OwnerId: Optional[str] = None

class HostPropertiesTypeDef(BaseValidatorModel):
    Cores: Optional[int] = None
    InstanceType: Optional[str] = None
    InstanceFamily: Optional[str] = None
    Sockets: Optional[int] = None
    TotalVCpus: Optional[int] = None

class IKEVersionsListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class IKEVersionsRequestListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class IamInstanceProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None

class LaunchPermissionTypeDef(BaseValidatorModel):
    Group: Optional[Literal["all"]] = None
    UserId: Optional[str] = None
    OrganizationArn: Optional[str] = None
    OrganizationalUnitArn: Optional[str] = None

class UserBucketTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None

class ImageRecycleBinInfoTypeDef(BaseValidatorModel):
    ImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    RecycleBinEnterTime: Optional[datetime] = None
    RecycleBinExitTime: Optional[datetime] = None

class StateReasonTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    CertificateRevocationList: str
    DryRun: Optional[bool] = None

class ImportImageLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None

class ImportImageLicenseConfigurationResponseTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None

class UserDataTypeDef(BaseValidatorModel):
    Data: Optional[str] = None

class InferenceDeviceMemoryInfoTypeDef(BaseValidatorModel):
    SizeInMiB: Optional[int] = None

class InstanceAttachmentEnaSrdUdpSpecificationTypeDef(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class InstanceCountTypeDef(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    State: Optional[ListingStateType] = None

class InstanceCreditSpecificationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    CpuCredits: Optional[str] = None

class InstanceEventWindowTimeRangeTypeDef(BaseValidatorModel):
    StartWeekDay: Optional[WeekDayType] = None
    StartHour: Optional[int] = None
    EndWeekDay: Optional[WeekDayType] = None
    EndHour: Optional[int] = None

class InstanceIpv4PrefixTypeDef(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None

class InstanceIpv6AddressRequestTypeDef(BaseValidatorModel):
    Ipv6Address: Optional[str] = None

class InstanceIpv6PrefixTypeDef(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None

class InstanceMaintenanceOptionsRequestTypeDef(BaseValidatorModel):
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None

class InstanceMaintenanceOptionsTypeDef(BaseValidatorModel):
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None

class InstanceMetadataOptionsRequestTypeDef(BaseValidatorModel):
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class InstanceMetadataOptionsResponseTypeDef(BaseValidatorModel):
    State: Optional[InstanceMetadataOptionsStateType] = None
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class MonitoringTypeDef(BaseValidatorModel):
    State: Optional[MonitoringStateType] = None

class InstanceNetworkInterfaceAssociationTypeDef(BaseValidatorModel):
    CarrierIp: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    IpOwnerId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class MemoryGiBPerVCpuTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class MemoryMiBTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class NetworkBandwidthGbpsTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class NetworkInterfaceCountTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class TotalLocalStorageGBTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class VCpuCountRangeTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class MemoryGiBPerVCpuRequestTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class MemoryMiBRequestTypeDef(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None

class NetworkBandwidthGbpsRequestTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class NetworkInterfaceCountRequestTypeDef(BaseValidatorModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class TotalLocalStorageGBRequestTypeDef(BaseValidatorModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class VCpuCountRangeRequestTypeDef(BaseValidatorModel):
    Min: int
    Max: Optional[int] = None

class InstanceStateTypeDef(BaseValidatorModel):
    Code: Optional[int] = None
    Name: Optional[InstanceStateNameType] = None

class InstanceStatusDetailsTypeDef(BaseValidatorModel):
    ImpairedSince: Optional[datetime] = None
    Name: Optional[Literal["reachability"]] = None
    Status: Optional[StatusTypeType] = None

class InstanceStatusEventTypeDef(BaseValidatorModel):
    InstanceEventId: Optional[str] = None
    Code: Optional[EventCodeType] = None
    Description: Optional[str] = None
    NotAfter: Optional[datetime] = None
    NotBefore: Optional[datetime] = None
    NotBeforeDeadline: Optional[datetime] = None

class LicenseConfigurationTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None

class PrivateDnsNameOptionsResponseTypeDef(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class MemoryInfoTypeDef(BaseValidatorModel):
    SizeInMiB: Optional[int] = None

class NitroTpmInfoTypeDef(BaseValidatorModel):
    SupportedVersions: Optional[List[str]] = None

class PlacementGroupInfoTypeDef(BaseValidatorModel):
    SupportedStrategies: Optional[List[PlacementGroupStrategyType]] = None

class ProcessorInfoTypeDef(BaseValidatorModel):
    SupportedArchitectures: Optional[List[ArchitectureTypeType]] = None
    SustainedClockSpeedInGhz: Optional[float] = None
    SupportedFeatures: Optional[List[Literal["amd-sev-snp"]]] = None
    Manufacturer: Optional[str] = None

class VCpuInfoTypeDef(BaseValidatorModel):
    DefaultVCpus: Optional[int] = None
    DefaultCores: Optional[int] = None
    DefaultThreadsPerCore: Optional[int] = None
    ValidCores: Optional[List[int]] = None
    ValidThreadsPerCore: Optional[List[int]] = None

class IpRangeTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None
    Description: Optional[str] = None

class Ipv6RangeTypeDef(BaseValidatorModel):
    CidrIpv6: Optional[str] = None
    Description: Optional[str] = None

class PrefixListIdTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    PrefixListId: Optional[str] = None

class UserIdGroupPairTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None

class IpamCidrAuthorizationContextTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Signature: Optional[str] = None

class IpamDiscoveryFailureReasonTypeDef(BaseValidatorModel):
    Code: Optional[IpamDiscoveryFailureCodeType] = None
    Message: Optional[str] = None

class IpamPublicAddressSecurityGroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class IpamResourceTagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class IpamOperatingRegionTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None

class IpamPoolCidrFailureReasonTypeDef(BaseValidatorModel):
    Code: Optional[IpamPoolCidrFailureCodeType] = None
    Message: Optional[str] = None

class IpamPoolSourceResourceTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal["vpc"]] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None

class IpamPublicAddressTagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class Ipv4PrefixSpecificationResponseTypeDef(BaseValidatorModel):
    Ipv4Prefix: Optional[str] = None

class Ipv6CidrBlockTypeDef(BaseValidatorModel):
    Ipv6CidrBlock: Optional[str] = None

class PoolCidrBlockTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None

class Ipv6PrefixSpecificationResponseTypeDef(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None

class Ipv6PrefixSpecificationTypeDef(BaseValidatorModel):
    Ipv6Prefix: Optional[str] = None

class LastErrorTypeDef(BaseValidatorModel):
    Message: Optional[str] = None
    Code: Optional[str] = None

class RunInstancesMonitoringEnabledTypeDef(BaseValidatorModel):
    Enabled: bool

class SpotPlacementTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None
    Tenancy: Optional[TenancyType] = None

class LaunchTemplateEbsBlockDeviceRequestTypeDef(BaseValidatorModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Throughput: Optional[int] = None

class LaunchTemplateEbsBlockDeviceTypeDef(BaseValidatorModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Throughput: Optional[int] = None

class LaunchTemplateCpuOptionsRequestTypeDef(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class LaunchTemplateCpuOptionsTypeDef(BaseValidatorModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class LaunchTemplateElasticInferenceAcceleratorResponseTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Count: Optional[int] = None

class LaunchTemplateElasticInferenceAcceleratorTypeDef(BaseValidatorModel):
    Type: str
    Count: Optional[int] = None

class LaunchTemplateEnaSrdUdpSpecificationTypeDef(BaseValidatorModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class LaunchTemplateEnclaveOptionsRequestTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class LaunchTemplateEnclaveOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class LaunchTemplateHibernationOptionsRequestTypeDef(BaseValidatorModel):
    Configured: Optional[bool] = None

class LaunchTemplateHibernationOptionsTypeDef(BaseValidatorModel):
    Configured: Optional[bool] = None

class LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class LaunchTemplateIamInstanceProfileSpecificationTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef(BaseValidatorModel):
    AutoRecovery: Optional[LaunchTemplateAutoRecoveryStateType] = None

class LaunchTemplateInstanceMaintenanceOptionsTypeDef(BaseValidatorModel):
    AutoRecovery: Optional[LaunchTemplateAutoRecoveryStateType] = None

class LaunchTemplateSpotMarketOptionsTypeDef(BaseValidatorModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[datetime] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class LaunchTemplateInstanceMetadataOptionsRequestTypeDef(BaseValidatorModel):
    HttpTokens: Optional[LaunchTemplateHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[LaunchTemplateInstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[LaunchTemplateInstanceMetadataProtocolIpv6Type] = None
    InstanceMetadataTags: Optional[LaunchTemplateInstanceMetadataTagsStateType] = None

class LaunchTemplateInstanceMetadataOptionsTypeDef(BaseValidatorModel):
    State: Optional[LaunchTemplateInstanceMetadataOptionsStateType] = None
    HttpTokens: Optional[LaunchTemplateHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[LaunchTemplateInstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[LaunchTemplateInstanceMetadataProtocolIpv6Type] = None
    InstanceMetadataTags: Optional[LaunchTemplateInstanceMetadataTagsStateType] = None

class LaunchTemplateLicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None

class LaunchTemplateLicenseConfigurationTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None

class LaunchTemplatePlacementRequestTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    GroupId: Optional[str] = None

class LaunchTemplatePlacementTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    GroupId: Optional[str] = None

class LaunchTemplatePrivateDnsNameOptionsRequestTypeDef(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class LaunchTemplatePrivateDnsNameOptionsTypeDef(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class LaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class LaunchTemplatesMonitoringRequestTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class LaunchTemplatesMonitoringTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class LicenseConfigurationRequestTypeDef(BaseValidatorModel):
    LicenseConfigurationArn: Optional[str] = None

class ListImagesInRecycleBinRequestRequestTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class ListSnapshotsInRecycleBinRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class SnapshotRecycleBinInfoTypeDef(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    RecycleBinEnterTime: Optional[datetime] = None
    RecycleBinExitTime: Optional[datetime] = None
    Description: Optional[str] = None
    VolumeId: Optional[str] = None

class LoadPermissionRequestTypeDef(BaseValidatorModel):
    Group: Optional[Literal["all"]] = None
    UserId: Optional[str] = None

class MediaDeviceMemoryInfoTypeDef(BaseValidatorModel):
    SizeInMiB: Optional[int] = None

class ModifyAddressAttributeRequestRequestTypeDef(BaseValidatorModel):
    AllocationId: str
    DomainName: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyAvailabilityZoneGroupRequestRequestTypeDef(BaseValidatorModel):
    GroupName: str
    OptInStatus: ModifyAvailabilityZoneOptInStatusType
    DryRun: Optional[bool] = None

class ModifyDefaultCreditSpecificationRequestRequestTypeDef(BaseValidatorModel):
    InstanceFamily: UnlimitedSupportedInstanceFamilyType
    CpuCredits: str
    DryRun: Optional[bool] = None

class ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef(BaseValidatorModel):
    KmsKeyId: str
    DryRun: Optional[bool] = None

class ModifyHostsRequestRequestTypeDef(BaseValidatorModel):
    HostIds: Sequence[str]
    AutoPlacement: Optional[AutoPlacementType] = None
    HostRecovery: Optional[HostRecoveryType] = None
    InstanceType: Optional[str] = None
    InstanceFamily: Optional[str] = None
    HostMaintenance: Optional[HostMaintenanceType] = None

class ModifyIdFormatRequestRequestTypeDef(BaseValidatorModel):
    Resource: str
    UseLongIds: bool

class ModifyIdentityIdFormatRequestRequestTypeDef(BaseValidatorModel):
    PrincipalArn: str
    Resource: str
    UseLongIds: bool

class SuccessfulInstanceCreditSpecificationItemTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None

class ModifyInstanceMaintenanceOptionsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None
    DryRun: Optional[bool] = None

class ModifyInstanceMetadataDefaultsRequestRequestTypeDef(BaseValidatorModel):
    HttpTokens: Optional[MetadataDefaultHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[DefaultInstanceMetadataEndpointStateType] = None
    InstanceMetadataTags: Optional[DefaultInstanceMetadataTagsStateType] = None
    DryRun: Optional[bool] = None

class ModifyInstanceMetadataOptionsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    DryRun: Optional[bool] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class ModifyInstancePlacementRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Affinity: Optional[AffinityType] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[HostTenancyType] = None
    PartitionNumber: Optional[int] = None
    HostResourceGroupArn: Optional[str] = None
    GroupId: Optional[str] = None

class RemoveIpamOperatingRegionTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None

class ModifyIpamResourceCidrRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    ResourceCidr: str
    ResourceRegion: str
    CurrentIpamScopeId: str
    Monitored: bool
    DryRun: Optional[bool] = None
    DestinationIpamScopeId: Optional[str] = None

class ModifyIpamScopeRequestRequestTypeDef(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None

class ModifyLaunchTemplateRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    DefaultVersion: Optional[str] = None

class ModifyLocalGatewayRouteRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationPrefixListId: Optional[str] = None

class RemovePrefixListEntryTypeDef(BaseValidatorModel):
    Cidr: str

class NetworkInterfaceAttachmentChangesTypeDef(BaseValidatorModel):
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None

class ModifyPrivateDnsNameOptionsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    PrivateDnsHostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class ReservedInstancesConfigurationTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[str] = None
    Scope: Optional[ScopeType] = None

class ModifySnapshotTierRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    StorageTier: Optional[Literal["archive"]] = None
    DryRun: Optional[bool] = None

class ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorFilterId: str
    AddNetworkServices: Optional[Sequence[Literal["amazon-dns"]]] = None
    RemoveNetworkServices: Optional[Sequence[Literal["amazon-dns"]]] = None
    DryRun: Optional[bool] = None

class ModifyTrafficMirrorSessionRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorSessionId: str
    TrafficMirrorTargetId: Optional[str] = None
    TrafficMirrorFilterId: Optional[str] = None
    PacketLength: Optional[int] = None
    SessionNumber: Optional[int] = None
    VirtualNetworkId: Optional[int] = None
    Description: Optional[str] = None
    RemoveFields: Optional[Sequence[TrafficMirrorSessionFieldType]] = None
    DryRun: Optional[bool] = None

class ModifyTransitGatewayOptionsTypeDef(BaseValidatorModel):
    AddTransitGatewayCidrBlocks: Optional[Sequence[str]] = None
    RemoveTransitGatewayCidrBlocks: Optional[Sequence[str]] = None
    VpnEcmpSupport: Optional[VpnEcmpSupportValueType] = None
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    AutoAcceptSharedAttachments: Optional[AutoAcceptSharedAttachmentsValueType] = None
    DefaultRouteTableAssociation: Optional[DefaultRouteTableAssociationValueType] = None
    AssociationDefaultRouteTableId: Optional[str] = None
    DefaultRouteTablePropagation: Optional[DefaultRouteTablePropagationValueType] = None
    PropagationDefaultRouteTableId: Optional[str] = None
    AmazonSideAsn: Optional[int] = None

class ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef(BaseValidatorModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None

class ModifyVerifiedAccessEndpointEniOptionsTypeDef(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef(BaseValidatorModel):
    SubnetIds: Optional[Sequence[str]] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class VerifiedAccessSseSpecificationResponseTypeDef(BaseValidatorModel):
    CustomerManagedKeyEnabled: Optional[bool] = None
    KmsKeyArn: Optional[str] = None

class ModifyVerifiedAccessGroupRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessGroupId: str
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVerifiedAccessInstanceRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef(BaseValidatorModel):
    PublicSigningKeyUrl: Optional[str] = None

class ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef(BaseValidatorModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None

class ModifyVolumeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    DryRun: Optional[bool] = None
    Size: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None
    MultiAttachEnabled: Optional[bool] = None

class ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef(BaseValidatorModel):
    ConnectionNotificationId: str
    DryRun: Optional[bool] = None
    ConnectionNotificationArn: Optional[str] = None
    ConnectionEvents: Optional[Sequence[str]] = None

class ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    RemovePrivateDnsName: Optional[bool] = None
    AcceptanceRequired: Optional[bool] = None
    AddNetworkLoadBalancerArns: Optional[Sequence[str]] = None
    RemoveNetworkLoadBalancerArns: Optional[Sequence[str]] = None
    AddGatewayLoadBalancerArns: Optional[Sequence[str]] = None
    RemoveGatewayLoadBalancerArns: Optional[Sequence[str]] = None
    AddSupportedIpAddressTypes: Optional[Sequence[str]] = None
    RemoveSupportedIpAddressTypes: Optional[Sequence[str]] = None

class ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    PayerResponsibility: Literal["ServiceOwner"]
    DryRun: Optional[bool] = None

class ModifyVpcEndpointServicePermissionsRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    AddAllowedPrincipals: Optional[Sequence[str]] = None
    RemoveAllowedPrincipals: Optional[Sequence[str]] = None

class PeeringConnectionOptionsRequestTypeDef(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class PeeringConnectionOptionsTypeDef(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class ModifyVpcTenancyRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    InstanceTenancy: Literal["default"]
    DryRun: Optional[bool] = None

class ModifyVpnConnectionOptionsRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    LocalIpv4NetworkCidr: Optional[str] = None
    RemoteIpv4NetworkCidr: Optional[str] = None
    LocalIpv6NetworkCidr: Optional[str] = None
    RemoteIpv6NetworkCidr: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVpnConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    TransitGatewayId: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVpnTunnelCertificateRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    DryRun: Optional[bool] = None

class Phase1DHGroupNumbersRequestListValueTypeDef(BaseValidatorModel):
    Value: Optional[int] = None

class Phase1EncryptionAlgorithmsRequestListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class Phase1IntegrityAlgorithmsRequestListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class Phase2DHGroupNumbersRequestListValueTypeDef(BaseValidatorModel):
    Value: Optional[int] = None

class Phase2EncryptionAlgorithmsRequestListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class Phase2IntegrityAlgorithmsRequestListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class MonitorInstancesRequestInstanceMonitorTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class MonitorInstancesRequestRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class MoveAddressToVpcRequestRequestTypeDef(BaseValidatorModel):
    PublicIp: str
    DryRun: Optional[bool] = None

class MoveByoipCidrToIpamRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    IpamPoolId: str
    IpamPoolOwner: str
    DryRun: Optional[bool] = None

class ProvisionedBandwidthTypeDef(BaseValidatorModel):
    ProvisionTime: Optional[datetime] = None
    Provisioned: Optional[str] = None
    RequestTime: Optional[datetime] = None
    Requested: Optional[str] = None
    Status: Optional[str] = None

class NetworkAclAssociationTypeDef(BaseValidatorModel):
    NetworkAclAssociationId: Optional[str] = None
    NetworkAclId: Optional[str] = None
    SubnetId: Optional[str] = None

class NetworkCardInfoTypeDef(BaseValidatorModel):
    NetworkCardIndex: Optional[int] = None
    NetworkPerformance: Optional[str] = None
    MaximumNetworkInterfaces: Optional[int] = None
    BaselineBandwidthInGbps: Optional[float] = None
    PeakBandwidthInGbps: Optional[float] = None

class NetworkInterfaceAssociationTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    AssociationId: Optional[str] = None
    IpOwnerId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    CarrierIp: Optional[str] = None

class NetworkInterfaceIpv6AddressTypeDef(BaseValidatorModel):
    Ipv6Address: Optional[str] = None
    IsPrimaryIpv6: Optional[bool] = None

class NetworkInterfacePermissionStateTypeDef(BaseValidatorModel):
    State: Optional[NetworkInterfacePermissionStateCodeType] = None
    StatusMessage: Optional[str] = None

class NeuronDeviceCoreInfoTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Version: Optional[int] = None

class NeuronDeviceMemoryInfoTypeDef(BaseValidatorModel):
    SizeInMiB: Optional[int] = None

class OidcOptionsTypeDef(BaseValidatorModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None

class PacketHeaderStatementRequestTypeDef(BaseValidatorModel):
    SourceAddresses: Optional[Sequence[str]] = None
    DestinationAddresses: Optional[Sequence[str]] = None
    SourcePorts: Optional[Sequence[str]] = None
    DestinationPorts: Optional[Sequence[str]] = None
    SourcePrefixLists: Optional[Sequence[str]] = None
    DestinationPrefixLists: Optional[Sequence[str]] = None
    Protocols: Optional[Sequence[ProtocolType]] = None

class PacketHeaderStatementTypeDef(BaseValidatorModel):
    SourceAddresses: Optional[List[str]] = None
    DestinationAddresses: Optional[List[str]] = None
    SourcePorts: Optional[List[str]] = None
    DestinationPorts: Optional[List[str]] = None
    SourcePrefixLists: Optional[List[str]] = None
    DestinationPrefixLists: Optional[List[str]] = None
    Protocols: Optional[List[ProtocolType]] = None

class RequestFilterPortRangeTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class ResourceStatementRequestTypeDef(BaseValidatorModel):
    Resources: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None

class ResourceStatementTypeDef(BaseValidatorModel):
    Resources: Optional[List[str]] = None
    ResourceTypes: Optional[List[str]] = None

class PeeringAttachmentStatusTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class PeeringTgwInfoTypeDef(BaseValidatorModel):
    TransitGatewayId: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    OwnerId: Optional[str] = None
    Region: Optional[str] = None

class Phase1DHGroupNumbersListValueTypeDef(BaseValidatorModel):
    Value: Optional[int] = None

class Phase1EncryptionAlgorithmsListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class Phase1IntegrityAlgorithmsListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class Phase2DHGroupNumbersListValueTypeDef(BaseValidatorModel):
    Value: Optional[int] = None

class Phase2EncryptionAlgorithmsListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class Phase2IntegrityAlgorithmsListValueTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class PriceScheduleTypeDef(BaseValidatorModel):
    Active: Optional[bool] = None
    CurrencyCode: Optional[Literal["USD"]] = None
    Price: Optional[float] = None
    Term: Optional[int] = None

class PricingDetailTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Price: Optional[float] = None

class PrivateDnsDetailsTypeDef(BaseValidatorModel):
    PrivateDnsName: Optional[str] = None

class PrivateDnsNameConfigurationTypeDef(BaseValidatorModel):
    State: Optional[DnsNameStateType] = None
    Type: Optional[str] = None
    Value: Optional[str] = None
    Name: Optional[str] = None

class PrivateDnsNameOptionsOnLaunchTypeDef(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class PrivateDnsNameOptionsRequestTypeDef(BaseValidatorModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class PropagatingVgwTypeDef(BaseValidatorModel):
    GatewayId: Optional[str] = None

class ProvisionPublicIpv4PoolCidrRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    PoolId: str
    NetmaskLength: int
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class PublicIpv4PoolRangeTypeDef(BaseValidatorModel):
    FirstAddress: Optional[str] = None
    LastAddress: Optional[str] = None
    AddressCount: Optional[int] = None
    AvailableAddressCount: Optional[int] = None

class PurchaseRequestTypeDef(BaseValidatorModel):
    InstanceCount: int
    PurchaseToken: str

class ReservedInstanceLimitPriceTypeDef(BaseValidatorModel):
    Amount: Optional[float] = None
    CurrencyCode: Optional[Literal["USD"]] = None

class RebootInstancesRequestInstanceRebootTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class RebootInstancesRequestRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class RecurringChargeTypeDef(BaseValidatorModel):
    Amount: Optional[float] = None
    Frequency: Optional[Literal["Hourly"]] = None

class ReferencedSecurityGroupTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None

class RegisterInstanceTagAttributeRequestTypeDef(BaseValidatorModel):
    IncludeAllTagsOfInstance: Optional[bool] = None
    InstanceTagKeys: Optional[Sequence[str]] = None

class RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    NetworkInterfaceIds: Sequence[str]
    GroupIpAddress: Optional[str] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastRegisteredGroupMembersTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    RegisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    NetworkInterfaceIds: Sequence[str]
    GroupIpAddress: Optional[str] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastRegisteredGroupSourcesTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    RegisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class RejectTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class RejectVpcEndpointConnectionsRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    VpcEndpointIds: Sequence[str]
    DryRun: Optional[bool] = None

class RejectVpcPeeringConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None

class RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class ReleaseAddressRequestClassicAddressReleaseTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None

class ReleaseAddressRequestRequestTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None

class ReleaseAddressRequestVpcAddressReleaseTypeDef(BaseValidatorModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None

class ReleaseHostsRequestRequestTypeDef(BaseValidatorModel):
    HostIds: Sequence[str]

class ReleaseIpamPoolAllocationRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    Cidr: str
    IpamPoolAllocationId: str
    DryRun: Optional[bool] = None

class ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef(BaseValidatorModel):
    AssociationId: str
    DryRun: Optional[bool] = None

class ReplaceNetworkAclAssociationRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    NetworkAclId: str
    DryRun: Optional[bool] = None

class ReplaceRouteRequestRequestTypeDef(BaseValidatorModel):
    RouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None
    VpcEndpointId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    LocalTarget: Optional[bool] = None
    NatGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None

class ReplaceRouteRequestRouteReplaceTypeDef(BaseValidatorModel):
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None
    VpcEndpointId: Optional[str] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    GatewayId: Optional[str] = None
    InstanceId: Optional[str] = None
    LocalTarget: Optional[bool] = None
    NatGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    CarrierGatewayId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None

class ReplaceRouteTableAssociationRequestRequestTypeDef(BaseValidatorModel):
    AssociationId: str
    RouteTableId: str
    DryRun: Optional[bool] = None

class ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef(BaseValidatorModel):
    RouteTableId: str
    DryRun: Optional[bool] = None

class ReplaceTransitGatewayRouteRequestRequestTypeDef(BaseValidatorModel):
    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class ReplaceVpnTunnelRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    ApplyPendingMaintenance: Optional[bool] = None
    DryRun: Optional[bool] = None

class ReservedInstancesIdTypeDef(BaseValidatorModel):
    ReservedInstancesId: Optional[str] = None

class ResetAddressAttributeRequestRequestTypeDef(BaseValidatorModel):
    AllocationId: str
    Attribute: Literal["domain-name"]
    DryRun: Optional[bool] = None

class ResetEbsDefaultKmsKeyIdRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class ResetFpgaImageAttributeRequestRequestTypeDef(BaseValidatorModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None
    Attribute: Optional[Literal["loadPermission"]] = None

class ResetImageAttributeRequestImageResetAttributeTypeDef(BaseValidatorModel):
    Attribute: Literal["launchPermission"]
    DryRun: Optional[bool] = None

class ResetImageAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: Literal["launchPermission"]
    ImageId: str
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetAttributeTypeDef(BaseValidatorModel):
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetKernelTypeDef(BaseValidatorModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef(BaseValidatorModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef(BaseValidatorModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: InstanceAttributeNameType
    InstanceId: str
    DryRun: Optional[bool] = None

class ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    SourceDestCheck: Optional[str] = None

class ResetNetworkInterfaceAttributeRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None
    SourceDestCheck: Optional[str] = None

class ResetSnapshotAttributeRequestRequestTypeDef(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    SnapshotId: str
    DryRun: Optional[bool] = None

class ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef(BaseValidatorModel):
    Attribute: SnapshotAttributeNameType
    DryRun: Optional[bool] = None

class RestoreAddressToClassicRequestRequestTypeDef(BaseValidatorModel):
    PublicIp: str
    DryRun: Optional[bool] = None

class RestoreImageFromRecycleBinRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DryRun: Optional[bool] = None

class RestoreManagedPrefixListVersionRequestRequestTypeDef(BaseValidatorModel):
    PrefixListId: str
    PreviousVersion: int
    CurrentVersion: int
    DryRun: Optional[bool] = None

class RestoreSnapshotFromRecycleBinRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    DryRun: Optional[bool] = None

class RestoreSnapshotTierRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    TemporaryRestoreDays: Optional[int] = None
    PermanentRestore: Optional[bool] = None
    DryRun: Optional[bool] = None

class RevokeClientVpnIngressRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    TargetNetworkCidr: str
    AccessGroupId: Optional[str] = None
    RevokeAllGroups: Optional[bool] = None
    DryRun: Optional[bool] = None

class RouteTypeDef(BaseValidatorModel):
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

class S3StorageOutputTypeDef(BaseValidatorModel):
    AWSAccessKeyId: Optional[str] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None
    UploadPolicy: Optional[bytes] = None
    UploadPolicySignature: Optional[str] = None

class ScheduledInstanceRecurrenceTypeDef(BaseValidatorModel):
    Frequency: Optional[str] = None
    Interval: Optional[int] = None
    OccurrenceDaySet: Optional[List[int]] = None
    OccurrenceRelativeToEnd: Optional[bool] = None
    OccurrenceUnit: Optional[str] = None

class ScheduledInstancesEbsTypeDef(BaseValidatorModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None

class ScheduledInstancesIamInstanceProfileTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ScheduledInstancesIpv6AddressTypeDef(BaseValidatorModel):
    Ipv6Address: Optional[str] = None

class ScheduledInstancesMonitoringTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class ScheduledInstancesPlacementTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None

class ScheduledInstancesPrivateIpAddressConfigTypeDef(BaseValidatorModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None

class TransitGatewayMulticastGroupTypeDef(BaseValidatorModel):
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

class SecurityGroupIdentifierTypeDef(BaseValidatorModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None

class SecurityGroupRuleDescriptionTypeDef(BaseValidatorModel):
    SecurityGroupRuleId: Optional[str] = None
    Description: Optional[str] = None

class SecurityGroupRuleRequestTypeDef(BaseValidatorModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIpv4: Optional[str] = None
    CidrIpv6: Optional[str] = None
    PrefixListId: Optional[str] = None
    ReferencedGroupId: Optional[str] = None
    Description: Optional[str] = None

class SendDiagnosticInterruptRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class ServiceTypeDetailTypeDef(BaseValidatorModel):
    ServiceType: Optional[ServiceTypeType] = None

class UserBucketDetailsTypeDef(BaseValidatorModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None

class SpotCapacityRebalanceTypeDef(BaseValidatorModel):
    ReplacementStrategy: Optional[ReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None

class SpotInstanceStateFaultTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class SpotFleetMonitoringTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None

class SpotInstanceStatusTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None
    UpdateTime: Optional[datetime] = None

class StartInstancesRequestInstanceStartTypeDef(BaseValidatorModel):
    AdditionalInfo: Optional[str] = None
    DryRun: Optional[bool] = None

class StartInstancesRequestRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    AdditionalInfo: Optional[str] = None
    DryRun: Optional[bool] = None

class StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None

class StopInstancesRequestInstanceStopTypeDef(BaseValidatorModel):
    Hibernate: Optional[bool] = None
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class StopInstancesRequestRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    Hibernate: Optional[bool] = None
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class SubnetAssociationTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    State: Optional[TransitGatewayMulitcastDomainAssociationStateType] = None

class SubnetCidrBlockStateTypeDef(BaseValidatorModel):
    State: Optional[SubnetCidrBlockStateCodeType] = None
    StatusMessage: Optional[str] = None

class TargetConfigurationTypeDef(BaseValidatorModel):
    InstanceCount: Optional[int] = None
    OfferingId: Optional[str] = None

class TargetGroupTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class TerminateClientVpnConnectionsRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    ConnectionId: Optional[str] = None
    Username: Optional[str] = None
    DryRun: Optional[bool] = None

class TerminateInstancesRequestInstanceTerminateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class TerminateInstancesRequestRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class TrafficMirrorPortRangeTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class TransitGatewayAttachmentAssociationTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class TransitGatewayAttachmentBgpConfigurationTypeDef(BaseValidatorModel):
    TransitGatewayAsn: Optional[int] = None
    PeerAsn: Optional[int] = None
    TransitGatewayAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    BgpStatus: Optional[BgpStatusType] = None

class TransitGatewayConnectOptionsTypeDef(BaseValidatorModel):
    Protocol: Optional[Literal["gre"]] = None

class TransitGatewayMulticastDomainOptionsTypeDef(BaseValidatorModel):
    Igmpv2Support: Optional[Igmpv2SupportValueType] = None
    StaticSourcesSupport: Optional[StaticSourcesSupportValueType] = None
    AutoAcceptSharedAssociations: Optional[AutoAcceptSharedAssociationsValueType] = None

class TransitGatewayOptionsTypeDef(BaseValidatorModel):
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

class TransitGatewayPeeringAttachmentOptionsTypeDef(BaseValidatorModel):
    DynamicRouting: Optional[DynamicRoutingValueType] = None

class TransitGatewayPolicyRuleMetaDataTypeDef(BaseValidatorModel):
    MetaDataKey: Optional[str] = None
    MetaDataValue: Optional[str] = None

class TransitGatewayPrefixListAttachmentTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceId: Optional[str] = None

class TransitGatewayRouteAttachmentTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None

class TransitGatewayVpcAttachmentOptionsTypeDef(BaseValidatorModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None

class UnassignIpv6AddressesRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    Ipv6Addresses: Optional[Sequence[str]] = None
    Ipv6Prefixes: Optional[Sequence[str]] = None

class UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef(BaseValidatorModel):
    PrivateIpAddresses: Optional[Sequence[str]] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None

class UnassignPrivateIpAddressesRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    PrivateIpAddresses: Optional[Sequence[str]] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None

class UnassignPrivateNatGatewayAddressRequestRequestTypeDef(BaseValidatorModel):
    NatGatewayId: str
    PrivateIpAddresses: Sequence[str]
    MaxDrainDurationSeconds: Optional[int] = None
    DryRun: Optional[bool] = None

class UnlockSnapshotRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    DryRun: Optional[bool] = None

class UnmonitorInstancesRequestInstanceUnmonitorTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None

class UnmonitorInstancesRequestRequestTypeDef(BaseValidatorModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef(BaseValidatorModel):
    Code: Optional[UnsuccessfulInstanceCreditSpecificationErrorCodeType] = None
    Message: Optional[str] = None

class UnsuccessfulItemErrorTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ValidationErrorTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class VerifiedAccessEndpointEniOptionsTypeDef(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class VerifiedAccessEndpointLoadBalancerOptionsTypeDef(BaseValidatorModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    LoadBalancerArn: Optional[str] = None
    SubnetIds: Optional[List[str]] = None

class VerifiedAccessEndpointStatusTypeDef(BaseValidatorModel):
    Code: Optional[VerifiedAccessEndpointStatusCodeType] = None
    Message: Optional[str] = None

class VerifiedAccessTrustProviderCondensedTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProviderId: Optional[str] = None
    Description: Optional[str] = None
    TrustProviderType: Optional[TrustProviderTypeType] = None
    UserTrustProviderType: Optional[UserTrustProviderTypeType] = None
    DeviceTrustProviderType: Optional[DeviceTrustProviderTypeType] = None

class VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef(BaseValidatorModel):
    Enabled: bool
    LogGroup: Optional[str] = None

class VerifiedAccessLogDeliveryStatusTypeDef(BaseValidatorModel):
    Code: Optional[VerifiedAccessLogDeliveryStatusCodeType] = None
    Message: Optional[str] = None

class VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef(BaseValidatorModel):
    Enabled: bool
    DeliveryStream: Optional[str] = None

class VerifiedAccessLogS3DestinationOptionsTypeDef(BaseValidatorModel):
    Enabled: bool
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None

class VgwTelemetryTypeDef(BaseValidatorModel):
    AcceptedRouteCount: Optional[int] = None
    LastStatusChange: Optional[datetime] = None
    OutsideIpAddress: Optional[str] = None
    Status: Optional[TelemetryStatusType] = None
    StatusMessage: Optional[str] = None
    CertificateArn: Optional[str] = None

class VolumeAttachmentTypeDef(BaseValidatorModel):
    AttachTime: Optional[datetime] = None
    Device: Optional[str] = None
    InstanceId: Optional[str] = None
    State: Optional[VolumeAttachmentStateType] = None
    VolumeId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    AssociatedResource: Optional[str] = None
    InstanceOwningService: Optional[str] = None

class VolumeStatusActionTypeDef(BaseValidatorModel):
    Code: Optional[str] = None
    Description: Optional[str] = None
    EventId: Optional[str] = None
    EventType: Optional[str] = None

class VolumeStatusAttachmentStatusTypeDef(BaseValidatorModel):
    IoPerformance: Optional[str] = None
    InstanceId: Optional[str] = None

class VolumeStatusDetailsTypeDef(BaseValidatorModel):
    Name: Optional[VolumeStatusNameType] = None
    Status: Optional[str] = None

class VolumeStatusEventTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    EventId: Optional[str] = None
    EventType: Optional[str] = None
    NotAfter: Optional[datetime] = None
    NotBefore: Optional[datetime] = None
    InstanceId: Optional[str] = None

class VpcCidrBlockStateTypeDef(BaseValidatorModel):
    State: Optional[VpcCidrBlockStateCodeType] = None
    StatusMessage: Optional[str] = None

class VpcPeeringConnectionOptionsDescriptionTypeDef(BaseValidatorModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class VpcPeeringConnectionStateReasonTypeDef(BaseValidatorModel):
    Code: Optional[VpcPeeringConnectionStateReasonCodeType] = None
    Message: Optional[str] = None

class VpnStaticRouteTypeDef(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    Source: Optional[Literal["Static"]] = None
    State: Optional[VpnStateType] = None

class WithdrawByoipCidrRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    DryRun: Optional[bool] = None

class AcceptAddressTransferResultTypeDef(BaseValidatorModel):
    AddressTransfer: AddressTransferTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptReservedInstancesExchangeQuoteResultTypeDef(BaseValidatorModel):
    ExchangeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateAddressResultTypeDef(BaseValidatorModel):
    PublicIp: str
    AllocationId: str
    PublicIpv4Pool: str
    NetworkBorderGroup: str
    Domain: DomainTypeType
    CustomerOwnedIp: str
    CustomerOwnedIpv4Pool: str
    CarrierIp: str
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateHostsResultTypeDef(BaseValidatorModel):
    HostIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef(BaseValidatorModel):
    SecurityGroupIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class AssignIpv6AddressesResultTypeDef(BaseValidatorModel):
    AssignedIpv6Addresses: List[str]
    AssignedIpv6Prefixes: List[str]
    NetworkInterfaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateAddressResultTypeDef(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateEnclaveCertificateIamRoleResultTypeDef(BaseValidatorModel):
    CertificateS3BucketName: str
    CertificateS3ObjectKey: str
    EncryptionKmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachClassicLinkVpcResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AttachNetworkInterfaceResultTypeDef(BaseValidatorModel):
    AttachmentId: str
    NetworkCardIndex: int
    ResponseMetadata: ResponseMetadataTypeDef

class CancelCapacityReservationResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CancelImageLaunchPermissionResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CancelImportTaskResultTypeDef(BaseValidatorModel):
    ImportTaskId: str
    PreviousState: str
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmProductInstanceResultTypeDef(BaseValidatorModel):
    OwnerId: str
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CopyFpgaImageResultTypeDef(BaseValidatorModel):
    FpgaImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CopyImageResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFpgaImageResultTypeDef(BaseValidatorModel):
    FpgaImageId: str
    FpgaImageGlobalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublicIpv4PoolResultTypeDef(BaseValidatorModel):
    PoolId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreImageTaskResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStoreImageTaskResultTypeDef(BaseValidatorModel):
    ObjectKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEgressOnlyInternetGatewayResultTypeDef(BaseValidatorModel):
    ReturnCode: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFpgaImageResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeyPairResultTypeDef(BaseValidatorModel):
    Return: bool
    KeyPairId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNatGatewayResultTypeDef(BaseValidatorModel):
    NatGatewayId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsAccessScopeResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsAnalysisResultTypeDef(BaseValidatorModel):
    NetworkInsightsAnalysisId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsPathResultTypeDef(BaseValidatorModel):
    NetworkInsightsPathId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInterfacePermissionResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePublicIpv4PoolResultTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorFilterResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorFilterRuleResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorSessionResultTypeDef(BaseValidatorModel):
    TrafficMirrorSessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorTargetResultTypeDef(BaseValidatorModel):
    TrafficMirrorTargetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcPeeringConnectionResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionPublicIpv4PoolCidrResultTypeDef(BaseValidatorModel):
    PoolId: str
    DeprovisionedAddresses: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressTransfersResultTypeDef(BaseValidatorModel):
    AddressTransfers: List[AddressTransferTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetachClassicLinkVpcResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableAddressTransferResultTypeDef(BaseValidatorModel):
    AddressTransfer: AddressTransferTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef(BaseValidatorModel):
    Output: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableEbsEncryptionByDefaultResultTypeDef(BaseValidatorModel):
    EbsEncryptionByDefault: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageBlockPublicAccessResultTypeDef(BaseValidatorModel):
    ImageBlockPublicAccessState: Literal["unblocked"]
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageDeprecationResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageDeregistrationProtectionResultTypeDef(BaseValidatorModel):
    Return: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableIpamOrganizationAdminAccountResultTypeDef(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableSerialConsoleAccessResultTypeDef(BaseValidatorModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableSnapshotBlockPublicAccessResultTypeDef(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DisableVpcClassicLinkDnsSupportResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableVpcClassicLinkResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateEnclaveCertificateIamRoleResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTrunkInterfaceResultTypeDef(BaseValidatorModel):
    Return: bool
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableAddressTransferResultTypeDef(BaseValidatorModel):
    AddressTransfer: AddressTransferTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef(BaseValidatorModel):
    Output: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableEbsEncryptionByDefaultResultTypeDef(BaseValidatorModel):
    EbsEncryptionByDefault: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageBlockPublicAccessResultTypeDef(BaseValidatorModel):
    ImageBlockPublicAccessState: Literal["block-new-sharing"]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageDeprecationResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageDeregistrationProtectionResultTypeDef(BaseValidatorModel):
    Return: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableIpamOrganizationAdminAccountResultTypeDef(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableReachabilityAnalyzerOrganizationSharingResultTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSerialConsoleAccessResultTypeDef(BaseValidatorModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSnapshotBlockPublicAccessResultTypeDef(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableVpcClassicLinkDnsSupportResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableVpcClassicLinkResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ExportClientVpnClientConfigurationResultTypeDef(BaseValidatorModel):
    ClientConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTransitGatewayRoutesResultTypeDef(BaseValidatorModel):
    S3Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConsoleOutputResultTypeDef(BaseValidatorModel):
    InstanceId: str
    Output: str
    Timestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetConsoleScreenshotResultTypeDef(BaseValidatorModel):
    ImageData: str
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEbsDefaultKmsKeyIdResultTypeDef(BaseValidatorModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEbsEncryptionByDefaultResultTypeDef(BaseValidatorModel):
    EbsEncryptionByDefault: bool
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowLogsIntegrationTemplateResultTypeDef(BaseValidatorModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageBlockPublicAccessStateResultTypeDef(BaseValidatorModel):
    ImageBlockPublicAccessState: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceTpmEkPubResultTypeDef(BaseValidatorModel):
    InstanceId: str
    KeyType: EkPubKeyTypeType
    KeyFormat: EkPubKeyFormatType
    KeyValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceUefiDataResultTypeDef(BaseValidatorModel):
    InstanceId: str
    UefiData: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPasswordDataResultTypeDef(BaseValidatorModel):
    InstanceId: str
    PasswordData: str
    Timestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSerialConsoleAccessStatusResultTypeDef(BaseValidatorModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnapshotBlockPublicAccessStateResultTypeDef(BaseValidatorModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetVerifiedAccessEndpointPolicyResultTypeDef(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVerifiedAccessGroupPolicyResultTypeDef(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpnConnectionDeviceSampleConfigurationResultTypeDef(BaseValidatorModel):
    VpnConnectionDeviceSampleConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportClientVpnClientCertificateRevocationListResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class LockSnapshotResultTypeDef(BaseValidatorModel):
    SnapshotId: str
    LockState: LockStateType
    LockDuration: int
    CoolOffPeriod: int
    CoolOffPeriodExpiresOn: datetime
    LockCreatedOn: datetime
    LockExpiresOn: datetime
    LockDurationStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyAvailabilityZoneGroupResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCapacityReservationFleetResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCapacityReservationResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClientVpnEndpointResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEbsDefaultKmsKeyIdResultTypeDef(BaseValidatorModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyFleetResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceCapacityReservationAttributesResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceMaintenanceOptionsResultTypeDef(BaseValidatorModel):
    InstanceId: str
    AutoRecovery: InstanceAutoRecoveryStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceMetadataDefaultsResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstancePlacementResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyPrivateDnsNameOptionsResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReservedInstancesResultTypeDef(BaseValidatorModel):
    ReservedInstancesModificationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySecurityGroupRulesResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySnapshotTierResultTypeDef(BaseValidatorModel):
    SnapshotId: str
    TieringStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySpotFleetRequestResponseTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointConnectionNotificationResultTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointServiceConfigurationResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointServicePayerResponsibilityResultTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcTenancyResultTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class MoveAddressToVpcResultTypeDef(BaseValidatorModel):
    AllocationId: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedInstancesOfferingResultTypeDef(BaseValidatorModel):
    ReservedInstancesId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterImageResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectVpcPeeringConnectionResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReleaseIpamPoolAllocationResultTypeDef(BaseValidatorModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceNetworkAclAssociationResultTypeDef(BaseValidatorModel):
    NewAssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceVpnTunnelResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RequestSpotFleetResponseTypeDef(BaseValidatorModel):
    SpotFleetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetEbsDefaultKmsKeyIdResultTypeDef(BaseValidatorModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetFpgaImageAttributeResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreAddressToClassicResultTypeDef(BaseValidatorModel):
    PublicIp: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreImageFromRecycleBinResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreSnapshotFromRecycleBinResultTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreSnapshotTierResultTypeDef(BaseValidatorModel):
    SnapshotId: str
    RestoreStartTime: datetime
    RestoreDuration: int
    IsPermanentRestore: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RunScheduledInstancesResultTypeDef(BaseValidatorModel):
    InstanceIdSet: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartVpcEndpointServicePrivateDnsVerificationResultTypeDef(BaseValidatorModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UnassignIpv6AddressesResultTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    UnassignedIpv6Addresses: List[str]
    UnassignedIpv6Prefixes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UnlockSnapshotResultTypeDef(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef(BaseValidatorModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class VolumeAttachmentResponseTypeDef(BaseValidatorModel):
    AttachTime: datetime
    Device: str
    InstanceId: str
    State: VolumeAttachmentStateType
    VolumeId: str
    DeleteOnTermination: bool
    AssociatedResource: str
    InstanceOwningService: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstanceIds: Sequence[str]
    DryRun: Optional[bool] = None
    TargetConfigurations: Optional[Sequence[TargetConfigurationRequestTypeDef]] = None

class GetReservedInstancesExchangeQuoteRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstanceIds: Sequence[str]
    DryRun: Optional[bool] = None
    TargetConfigurations: Optional[Sequence[TargetConfigurationRequestTypeDef]] = None

class AccountAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[AccountAttributeValueTypeDef]] = None

class DescribeFleetInstancesResultTypeDef(BaseValidatorModel):
    ActiveInstances: List[ActiveInstanceTypeDef]
    FleetId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSpotFleetInstancesResponseTypeDef(BaseValidatorModel):
    ActiveInstances: List[ActiveInstanceTypeDef]
    SpotFleetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVpcEndpointServicePermissionsResultTypeDef(BaseValidatorModel):
    AddedPrincipals: List[AddedPrincipalTypeDef]
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisLoadBalancerTargetTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Instance: Optional[AnalysisComponentTypeDef] = None
    Port: Optional[int] = None

class RuleGroupRuleOptionsPairTypeDef(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    RuleOptions: Optional[List[RuleOptionTypeDef]] = None

class AddressAttributeTypeDef(BaseValidatorModel):
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    PtrRecord: Optional[str] = None
    PtrRecordUpdate: Optional[PtrUpdateStatusTypeDef] = None

class AddressTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    AssociationId: Optional[str] = None
    Domain: Optional[DomainTypeType] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkInterfaceOwnerId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    PublicIpv4Pool: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    CarrierIp: Optional[str] = None

class AllowedPrincipalTypeDef(BaseValidatorModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None
    ServicePermissionId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ServiceId: Optional[str] = None

class CarrierGatewayTypeDef(BaseValidatorModel):
    CarrierGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    State: Optional[CarrierGatewayStateType] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ClientCreateTagsRequestTypeDef(BaseValidatorModel):
    Resources: Sequence[str]
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class ClientDeleteTagsRequestTypeDef(BaseValidatorModel):
    Resources: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None

class CoipPoolTypeDef(BaseValidatorModel):
    PoolId: Optional[str] = None
    PoolCidrs: Optional[List[str]] = None
    LocalGatewayRouteTableId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    PoolArn: Optional[str] = None

class CopySnapshotResultTypeDef(BaseValidatorModel):
    SnapshotId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityGroupResultTypeDef(BaseValidatorModel):
    GroupId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTagsRequestServiceResourceCreateTagsTypeDef(BaseValidatorModel):
    Resources: Sequence[str]
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class CustomerGatewayTypeDef(BaseValidatorModel):
    BgpAsn: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    IpAddress: Optional[str] = None
    CertificateArn: Optional[str] = None
    State: Optional[str] = None
    Type: Optional[str] = None
    DeviceName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    BgpAsnExtended: Optional[str] = None

class Ec2InstanceConnectEndpointTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class HostReservationTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    CurrencyCode: Optional[Literal["USD"]] = None
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
    Tags: Optional[List[TagTypeDef]] = None

class ImportKeyPairResultTypeDef(BaseValidatorModel):
    KeyFingerprint: str
    KeyName: str
    KeyPairId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceCreateTagsRequestTypeDef(BaseValidatorModel):
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class InstanceDeleteTagsRequestTypeDef(BaseValidatorModel):
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None

class InstanceEventWindowAssociationRequestTypeDef(BaseValidatorModel):
    InstanceIds: Optional[Sequence[str]] = None
    InstanceTags: Optional[Sequence[TagTypeDef]] = None
    DedicatedHostIds: Optional[Sequence[str]] = None

class InstanceEventWindowAssociationTargetTypeDef(BaseValidatorModel):
    InstanceIds: Optional[List[str]] = None
    Tags: Optional[List[TagTypeDef]] = None
    DedicatedHostIds: Optional[List[str]] = None

class InstanceEventWindowDisassociationRequestTypeDef(BaseValidatorModel):
    InstanceIds: Optional[Sequence[str]] = None
    InstanceTags: Optional[Sequence[TagTypeDef]] = None
    DedicatedHostIds: Optional[Sequence[str]] = None

class IpamResourceDiscoveryAssociationTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class IpamScopeTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class KeyPairInfoTypeDef(BaseValidatorModel):
    KeyPairId: Optional[str] = None
    KeyFingerprint: Optional[str] = None
    KeyName: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None
    PublicKey: Optional[str] = None
    CreateTime: Optional[datetime] = None

class KeyPairTypeDef(BaseValidatorModel):
    KeyFingerprint: str
    KeyMaterial: str
    KeyName: str
    KeyPairId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchTemplateTagSpecificationRequestTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class LaunchTemplateTagSpecificationTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class LaunchTemplateTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    CreateTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayRouteTableVpcAssociationTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayTypeDef(BaseValidatorModel):
    LocalGatewayId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayVirtualInterfaceGroupTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    LocalGatewayVirtualInterfaceIds: Optional[List[str]] = None
    LocalGatewayId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayVirtualInterfaceTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaceId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    Vlan: Optional[int] = None
    LocalAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    LocalBgpAsn: Optional[int] = None
    PeerBgpAsn: Optional[int] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ManagedPrefixListTypeDef(BaseValidatorModel):
    PrefixListId: Optional[str] = None
    AddressFamily: Optional[str] = None
    State: Optional[PrefixListStateType] = None
    StateMessage: Optional[str] = None
    PrefixListArn: Optional[str] = None
    PrefixListName: Optional[str] = None
    MaxEntries: Optional[int] = None
    Version: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None
    OwnerId: Optional[str] = None

class NetworkInsightsAccessScopeAnalysisTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class NetworkInsightsAccessScopeTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeId: Optional[str] = None
    NetworkInsightsAccessScopeArn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class PlacementGroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    State: Optional[PlacementGroupStateType] = None
    Strategy: Optional[PlacementStrategyType] = None
    PartitionCount: Optional[int] = None
    GroupId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    GroupArn: Optional[str] = None
    SpreadLevel: Optional[SpreadLevelType] = None

class ReplaceRootVolumeTaskTypeDef(BaseValidatorModel):
    ReplaceRootVolumeTaskId: Optional[str] = None
    InstanceId: Optional[str] = None
    TaskState: Optional[ReplaceRootVolumeTaskStateType] = None
    StartTime: Optional[str] = None
    CompleteTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ImageId: Optional[str] = None
    SnapshotId: Optional[str] = None
    DeleteReplacedRootVolume: Optional[bool] = None

class SecurityGroupForVpcTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    GroupName: Optional[str] = None
    OwnerId: Optional[str] = None
    GroupId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    PrimaryVpcId: Optional[str] = None

class SnapshotInfoTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
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

class SnapshotResponseTypeDef(BaseValidatorModel):
    DataEncryptionKeyId: str
    Description: str
    Encrypted: bool
    KmsKeyId: str
    OwnerId: str
    Progress: str
    SnapshotId: str
    StartTime: datetime
    State: SnapshotStateType
    StateMessage: str
    VolumeId: str
    VolumeSize: int
    OwnerAlias: str
    OutpostArn: str
    Tags: List[TagTypeDef]
    StorageTier: StorageTierType
    RestoreExpiryTime: datetime
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadataTypeDef

class SnapshotTierStatusTypeDef(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    VolumeId: Optional[str] = None
    Status: Optional[SnapshotStateType] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    StorageTier: Optional[StorageTierType] = None
    LastTieringStartTime: Optional[datetime] = None
    LastTieringProgress: Optional[int] = None
    LastTieringOperationStatus: Optional[TieringOperationStatusType] = None
    LastTieringOperationStatusDetail: Optional[str] = None
    ArchivalCompleteTime: Optional[datetime] = None
    RestoreExpiryTime: Optional[datetime] = None

class SnapshotTypeDef(BaseValidatorModel):
    DataEncryptionKeyId: Optional[str] = None
    Description: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    OwnerId: Optional[str] = None
    Progress: Optional[str] = None
    SnapshotId: Optional[str] = None
    StartTime: Optional[datetime] = None
    State: Optional[SnapshotStateType] = None
    StateMessage: Optional[str] = None
    VolumeId: Optional[str] = None
    VolumeSize: Optional[int] = None
    OwnerAlias: Optional[str] = None
    OutpostArn: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    StorageTier: Optional[StorageTierType] = None
    RestoreExpiryTime: Optional[datetime] = None
    SseType: Optional[SSETypeType] = None

class SpotFleetTagSpecificationExtraOutputTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class SpotFleetTagSpecificationOutputTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class SpotFleetTagSpecificationTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class SubnetCidrReservationTypeDef(BaseValidatorModel):
    SubnetCidrReservationId: Optional[str] = None
    SubnetId: Optional[str] = None
    Cidr: Optional[str] = None
    ReservationType: Optional[SubnetCidrReservationTypeType] = None
    OwnerId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagSpecificationExtraOutputTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagSpecificationOutputTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagSpecificationTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TrafficMirrorSessionTypeDef(BaseValidatorModel):
    TrafficMirrorSessionId: Optional[str] = None
    TrafficMirrorTargetId: Optional[str] = None
    TrafficMirrorFilterId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    OwnerId: Optional[str] = None
    PacketLength: Optional[int] = None
    SessionNumber: Optional[int] = None
    VirtualNetworkId: Optional[int] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class TrafficMirrorTargetTypeDef(BaseValidatorModel):
    TrafficMirrorTargetId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkLoadBalancerArn: Optional[str] = None
    Type: Optional[TrafficMirrorTargetTypeType] = None
    Description: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    GatewayLoadBalancerEndpointId: Optional[str] = None

class TransitGatewayPolicyTableTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayPolicyTableStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayRouteTableAnnouncementTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayRouteTableTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayRouteTableStateType] = None
    DefaultAssociationRouteTable: Optional[bool] = None
    DefaultPropagationRouteTable: Optional[bool] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TrunkInterfaceAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    BranchInterfaceId: Optional[str] = None
    TrunkInterfaceId: Optional[str] = None
    InterfaceProtocol: Optional[InterfaceProtocolTypeType] = None
    VlanId: Optional[int] = None
    GreKey: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None

class VpcClassicLinkTypeDef(BaseValidatorModel):
    ClassicLinkEnabled: Optional[bool] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None

class VpcCreateTagsRequestTypeDef(BaseValidatorModel):
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class AllocateIpamPoolCidrResultTypeDef(BaseValidatorModel):
    IpamPoolAllocation: IpamPoolAllocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIpamPoolAllocationsResultTypeDef(BaseValidatorModel):
    IpamPoolAllocations: List[IpamPoolAllocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AnalysisAclRuleTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    Egress: Optional[bool] = None
    PortRange: Optional[PortRangeTypeDef] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    RuleNumber: Optional[int] = None

class AnalysisPacketHeaderTypeDef(BaseValidatorModel):
    DestinationAddresses: Optional[List[str]] = None
    DestinationPortRanges: Optional[List[PortRangeTypeDef]] = None
    Protocol: Optional[str] = None
    SourceAddresses: Optional[List[str]] = None
    SourcePortRanges: Optional[List[PortRangeTypeDef]] = None

class AnalysisSecurityGroupRuleTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    Direction: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None
    PrefixListId: Optional[str] = None
    Protocol: Optional[str] = None

class FirewallStatefulRuleTypeDef(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    Sources: Optional[List[str]] = None
    Destinations: Optional[List[str]] = None
    SourcePorts: Optional[List[PortRangeTypeDef]] = None
    DestinationPorts: Optional[List[PortRangeTypeDef]] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    Direction: Optional[str] = None

class FirewallStatelessRuleTypeDef(BaseValidatorModel):
    RuleGroupArn: Optional[str] = None
    Sources: Optional[List[str]] = None
    Destinations: Optional[List[str]] = None
    SourcePorts: Optional[List[PortRangeTypeDef]] = None
    DestinationPorts: Optional[List[PortRangeTypeDef]] = None
    Protocols: Optional[List[int]] = None
    RuleAction: Optional[str] = None
    Priority: Optional[int] = None

class AssociateIpamByoasnResultTypeDef(BaseValidatorModel):
    AsnAssociation: AsnAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ByoipCidrTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    Description: Optional[str] = None
    AsnAssociations: Optional[List[AsnAssociationTypeDef]] = None
    StatusMessage: Optional[str] = None
    State: Optional[ByoipCidrStateType] = None
    NetworkBorderGroup: Optional[str] = None

class DisassociateIpamByoasnResultTypeDef(BaseValidatorModel):
    AsnAssociation: AsnAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionIpamByoasnRequestRequestTypeDef(BaseValidatorModel):
    IpamId: str
    Asn: str
    AsnAuthorizationContext: AsnAuthorizationContextTypeDef
    DryRun: Optional[bool] = None

class AssignPrivateIpAddressesResultTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    AssignedPrivateIpAddresses: List[AssignedPrivateIpAddressTypeDef]
    AssignedIpv4Prefixes: List[Ipv4PrefixSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssignPrivateNatGatewayAddressResultTypeDef(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateNatGatewayAddressResultTypeDef(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateNatGatewayAddressResultTypeDef(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UnassignPrivateNatGatewayAddressResultTypeDef(BaseValidatorModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateClientVpnTargetNetworkResultTypeDef(BaseValidatorModel):
    AssociationId: str
    Status: AssociationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateClientVpnTargetNetworkResultTypeDef(BaseValidatorModel):
    AssociationId: str
    Status: AssociationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TargetNetworkTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    VpcId: Optional[str] = None
    TargetNetworkId: Optional[str] = None
    ClientVpnEndpointId: Optional[str] = None
    Status: Optional[AssociationStatusTypeDef] = None
    SecurityGroups: Optional[List[str]] = None

class AssociateIamInstanceProfileRequestRequestTypeDef(BaseValidatorModel):
    IamInstanceProfile: IamInstanceProfileSpecificationTypeDef
    InstanceId: str

class ReplaceIamInstanceProfileAssociationRequestRequestTypeDef(BaseValidatorModel):
    IamInstanceProfile: IamInstanceProfileSpecificationTypeDef
    AssociationId: str

class AssociateRouteTableResultTypeDef(BaseValidatorModel):
    AssociationId: str
    AssociationState: RouteTableAssociationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceRouteTableAssociationResultTypeDef(BaseValidatorModel):
    NewAssociationId: str
    AssociationState: RouteTableAssociationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RouteTableAssociationTypeDef(BaseValidatorModel):
    Main: Optional[bool] = None
    RouteTableAssociationId: Optional[str] = None
    RouteTableId: Optional[str] = None
    SubnetId: Optional[str] = None
    GatewayId: Optional[str] = None
    AssociationState: Optional[RouteTableAssociationStateTypeDef] = None

class AssociateTransitGatewayPolicyTableResultTypeDef(BaseValidatorModel):
    Association: TransitGatewayPolicyTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayPolicyTableResultTypeDef(BaseValidatorModel):
    Association: TransitGatewayPolicyTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayPolicyTableAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[TransitGatewayPolicyTableAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateTransitGatewayRouteTableResultTypeDef(BaseValidatorModel):
    Association: TransitGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayRouteTableResultTypeDef(BaseValidatorModel):
    Association: TransitGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedEnclaveCertificateIamRolesResultTypeDef(BaseValidatorModel):
    AssociatedRoles: List[AssociatedRoleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AthenaIntegrationTypeDef(BaseValidatorModel):
    IntegrationResultS3DestinationArn: str
    PartitionLoadFrequency: PartitionLoadFrequencyType
    PartitionStartDate: Optional[TimestampTypeDef] = None
    PartitionEndDate: Optional[TimestampTypeDef] = None

class ClientDataTypeDef(BaseValidatorModel):
    Comment: Optional[str] = None
    UploadEnd: Optional[TimestampTypeDef] = None
    UploadSize: Optional[float] = None
    UploadStart: Optional[TimestampTypeDef] = None

class DescribeCapacityBlockOfferingsRequestRequestTypeDef(BaseValidatorModel):
    InstanceType: str
    InstanceCount: int
    CapacityDurationHours: int
    DryRun: Optional[bool] = None
    StartDateRange: Optional[TimestampTypeDef] = None
    EndDateRange: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeFleetHistoryRequestRequestTypeDef(BaseValidatorModel):
    FleetId: str
    StartTime: TimestampTypeDef
    DryRun: Optional[bool] = None
    EventType: Optional[FleetEventTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestHistoryRequestRequestTypeDef(BaseValidatorModel):
    SpotFleetRequestId: str
    StartTime: TimestampTypeDef
    DryRun: Optional[bool] = None
    EventType: Optional[EventTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class EnableImageDeprecationRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    DeprecateAt: TimestampTypeDef
    DryRun: Optional[bool] = None

class GetIpamAddressHistoryRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    IpamScopeId: str
    DryRun: Optional[bool] = None
    VpcId: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LaunchTemplateSpotMarketOptionsRequestTypeDef(BaseValidatorModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[TimestampTypeDef] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class LockSnapshotRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    LockMode: LockModeType
    DryRun: Optional[bool] = None
    CoolOffPeriod: Optional[int] = None
    LockDuration: Optional[int] = None
    ExpirationDate: Optional[TimestampTypeDef] = None

class ModifyCapacityReservationFleetRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationFleetId: str
    TotalTargetCapacity: Optional[int] = None
    EndDate: Optional[TimestampTypeDef] = None
    DryRun: Optional[bool] = None
    RemoveEndDate: Optional[bool] = None

class ModifyCapacityReservationRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationId: str
    InstanceCount: Optional[int] = None
    EndDate: Optional[TimestampTypeDef] = None
    EndDateType: Optional[EndDateTypeType] = None
    Accept: Optional[bool] = None
    DryRun: Optional[bool] = None
    AdditionalInfo: Optional[str] = None

class ModifyInstanceEventStartTimeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    InstanceEventId: str
    NotBefore: TimestampTypeDef
    DryRun: Optional[bool] = None

class ReportInstanceStatusRequestInstanceReportStatusTypeDef(BaseValidatorModel):
    ReasonCodes: Sequence[ReportInstanceReasonCodesType]
    Status: ReportStatusTypeType
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None

class ReportInstanceStatusRequestRequestTypeDef(BaseValidatorModel):
    Instances: Sequence[str]
    ReasonCodes: Sequence[ReportInstanceReasonCodesType]
    Status: ReportStatusTypeType
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None

class SlotDateTimeRangeRequestTypeDef(BaseValidatorModel):
    EarliestTime: TimestampTypeDef
    LatestTime: TimestampTypeDef

class SlotStartTimeRangeRequestTypeDef(BaseValidatorModel):
    EarliestTime: Optional[TimestampTypeDef] = None
    LatestTime: Optional[TimestampTypeDef] = None

class SpotMarketOptionsTypeDef(BaseValidatorModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[TimestampTypeDef] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class AttachVpnGatewayResultTypeDef(BaseValidatorModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VpnGatewayTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    State: Optional[VpnStateType] = None
    Type: Optional[Literal["ipsec.1"]] = None
    VpcAttachments: Optional[List[VpcAttachmentTypeDef]] = None
    VpnGatewayId: Optional[str] = None
    AmazonSideAsn: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None

class AttachmentEnaSrdSpecificationTypeDef(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[AttachmentEnaSrdUdpSpecificationTypeDef] = None

class DescribeVpcAttributeResultTypeDef(BaseValidatorModel):
    VpcId: str
    EnableDnsHostnames: AttributeBooleanValueTypeDef
    EnableDnsSupport: AttributeBooleanValueTypeDef
    EnableNetworkAddressUsageMetrics: AttributeBooleanValueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySubnetAttributeRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    AssignIpv6AddressOnCreation: Optional[AttributeBooleanValueTypeDef] = None
    MapPublicIpOnLaunch: Optional[AttributeBooleanValueTypeDef] = None
    MapCustomerOwnedIpOnLaunch: Optional[AttributeBooleanValueTypeDef] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    EnableDns64: Optional[AttributeBooleanValueTypeDef] = None
    PrivateDnsHostnameTypeOnLaunch: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecordOnLaunch: Optional[AttributeBooleanValueTypeDef] = None
    EnableResourceNameDnsAAAARecordOnLaunch: Optional[AttributeBooleanValueTypeDef] = None
    EnableLniAtDeviceIndex: Optional[int] = None
    DisableLniAtDeviceIndex: Optional[AttributeBooleanValueTypeDef] = None

class ModifyVolumeAttributeRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    AutoEnableIO: Optional[AttributeBooleanValueTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef(BaseValidatorModel):
    AutoEnableIO: Optional[AttributeBooleanValueTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyVpcAttributeRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    EnableDnsHostnames: Optional[AttributeBooleanValueTypeDef] = None
    EnableDnsSupport: Optional[AttributeBooleanValueTypeDef] = None
    EnableNetworkAddressUsageMetrics: Optional[AttributeBooleanValueTypeDef] = None

class ModifyVpcAttributeRequestVpcModifyAttributeTypeDef(BaseValidatorModel):
    EnableDnsHostnames: Optional[AttributeBooleanValueTypeDef] = None
    EnableDnsSupport: Optional[AttributeBooleanValueTypeDef] = None
    EnableNetworkAddressUsageMetrics: Optional[AttributeBooleanValueTypeDef] = None

class DhcpConfigurationTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[List[AttributeValueTypeDef]] = None

class AuthorizationRuleTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    AccessAll: Optional[bool] = None
    DestinationCidr: Optional[str] = None
    Status: Optional[ClientVpnAuthorizationRuleStatusTypeDef] = None

class AuthorizeClientVpnIngressResultTypeDef(BaseValidatorModel):
    Status: ClientVpnAuthorizationRuleStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeClientVpnIngressResultTypeDef(BaseValidatorModel):
    Status: ClientVpnAuthorizationRuleStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AvailabilityZoneTypeDef(BaseValidatorModel):
    State: Optional[AvailabilityZoneStateType] = None
    OptInStatus: Optional[AvailabilityZoneOptInStatusType] = None
    Messages: Optional[List[AvailabilityZoneMessageTypeDef]] = None
    RegionName: Optional[str] = None
    ZoneName: Optional[str] = None
    ZoneId: Optional[str] = None
    GroupName: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    ZoneType: Optional[str] = None
    ParentZoneName: Optional[str] = None
    ParentZoneId: Optional[str] = None

class AvailableCapacityTypeDef(BaseValidatorModel):
    AvailableInstanceCapacity: Optional[List[InstanceCapacityTypeDef]] = None
    AvailableVCpus: Optional[int] = None

class BlobAttributeValueTypeDef(BaseValidatorModel):
    Value: Optional[BlobTypeDef] = None

class S3StorageTypeDef(BaseValidatorModel):
    AWSAccessKeyId: Optional[str] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None
    UploadPolicy: Optional[BlobTypeDef] = None
    UploadPolicySignature: Optional[str] = None

class BlockDeviceMappingTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsBlockDeviceTypeDef] = None
    NoDevice: Optional[str] = None

class DeprovisionIpamByoasnResultTypeDef(BaseValidatorModel):
    Byoasn: ByoasnTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamByoasnResultTypeDef(BaseValidatorModel):
    Byoasns: List[ByoasnTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ProvisionIpamByoasnResultTypeDef(BaseValidatorModel):
    Byoasn: ByoasnTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailedCapacityReservationFleetCancellationResultTypeDef(BaseValidatorModel):
    CapacityReservationFleetId: Optional[str] = None
    CancelCapacityReservationFleetError: Optional[       CancelCapacityReservationFleetErrorTypeDef     ] = None

class CancelSpotFleetRequestsErrorItemTypeDef(BaseValidatorModel):
    Error: Optional[CancelSpotFleetRequestsErrorTypeDef] = None
    SpotFleetRequestId: Optional[str] = None

class CancelSpotInstanceRequestsResultTypeDef(BaseValidatorModel):
    CancelledSpotInstanceRequests: List[CancelledSpotInstanceRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CapacityReservationTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None
    OutpostArn: Optional[str] = None
    CapacityReservationFleetId: Optional[str] = None
    PlacementGroupArn: Optional[str] = None
    CapacityAllocations: Optional[List[CapacityAllocationTypeDef]] = None
    ReservationType: Optional[CapacityReservationTypeType] = None

class DescribeCapacityBlockOfferingsResultTypeDef(BaseValidatorModel):
    CapacityBlockOfferings: List[CapacityBlockOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CapacityReservationFleetTypeDef(BaseValidatorModel):
    CapacityReservationFleetId: Optional[str] = None
    CapacityReservationFleetArn: Optional[str] = None
    State: Optional[CapacityReservationFleetStateType] = None
    TotalTargetCapacity: Optional[int] = None
    TotalFulfilledCapacity: Optional[float] = None
    Tenancy: Optional[Literal["default"]] = None
    EndDate: Optional[datetime] = None
    CreateTime: Optional[datetime] = None
    InstanceMatchCriteria: Optional[Literal["open"]] = None
    AllocationStrategy: Optional[str] = None
    InstanceTypeSpecifications: Optional[List[FleetCapacityReservationTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateCapacityReservationFleetResultTypeDef(BaseValidatorModel):
    CapacityReservationFleetId: str
    State: CapacityReservationFleetStateType
    TotalTargetCapacity: int
    TotalFulfilledCapacity: float
    InstanceMatchCriteria: Literal["open"]
    AllocationStrategy: str
    CreateTime: datetime
    EndDate: datetime
    Tenancy: Literal["default"]
    FleetCapacityReservations: List[FleetCapacityReservationTypeDef]
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupsForCapacityReservationResultTypeDef(BaseValidatorModel):
    CapacityReservationGroups: List[CapacityReservationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OnDemandOptionsRequestTypeDef(BaseValidatorModel):
    AllocationStrategy: Optional[FleetOnDemandAllocationStrategyType] = None
    CapacityReservationOptions: Optional[CapacityReservationOptionsRequestTypeDef] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class OnDemandOptionsTypeDef(BaseValidatorModel):
    AllocationStrategy: Optional[FleetOnDemandAllocationStrategyType] = None
    CapacityReservationOptions: Optional[CapacityReservationOptionsTypeDef] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class CapacityReservationSpecificationResponseTypeDef(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetResponseTypeDef] = None

class LaunchTemplateCapacityReservationSpecificationResponseTypeDef(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetResponseTypeDef] = None

class CapacityReservationSpecificationTypeDef(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetTypeDef] = None

class LaunchTemplateCapacityReservationSpecificationRequestTypeDef(BaseValidatorModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetTypeDef] = None

class DescribeVpcClassicLinkDnsSupportResultTypeDef(BaseValidatorModel):
    Vpcs: List[ClassicLinkDnsSupportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClassicLinkInstanceTypeDef(BaseValidatorModel):
    Groups: Optional[List[GroupIdentifierTypeDef]] = None
    InstanceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None

class ClassicLoadBalancersConfigExtraOutputTypeDef(BaseValidatorModel):
    ClassicLoadBalancers: Optional[List[ClassicLoadBalancerTypeDef]] = None

class ClassicLoadBalancersConfigOutputTypeDef(BaseValidatorModel):
    ClassicLoadBalancers: Optional[List[ClassicLoadBalancerTypeDef]] = None

class ClassicLoadBalancersConfigTypeDef(BaseValidatorModel):
    ClassicLoadBalancers: Optional[Sequence[ClassicLoadBalancerTypeDef]] = None

class ExportClientVpnClientCertificateRevocationListResultTypeDef(BaseValidatorModel):
    CertificateRevocationList: str
    Status: ClientCertificateRevocationListStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClientConnectResponseOptionsTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None
    Status: Optional[ClientVpnEndpointAttributeStatusTypeDef] = None

class ClientVpnAuthenticationRequestTypeDef(BaseValidatorModel):
    Type: Optional[ClientVpnAuthenticationTypeType] = None
    ActiveDirectory: Optional[DirectoryServiceAuthenticationRequestTypeDef] = None
    MutualAuthentication: Optional[CertificateAuthenticationRequestTypeDef] = None
    FederatedAuthentication: Optional[FederatedAuthenticationRequestTypeDef] = None

class ClientVpnAuthenticationTypeDef(BaseValidatorModel):
    Type: Optional[ClientVpnAuthenticationTypeType] = None
    ActiveDirectory: Optional[DirectoryServiceAuthenticationTypeDef] = None
    MutualAuthentication: Optional[CertificateAuthenticationTypeDef] = None
    FederatedAuthentication: Optional[FederatedAuthenticationTypeDef] = None

class ClientVpnConnectionTypeDef(BaseValidatorModel):
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
    Status: Optional[ClientVpnConnectionStatusTypeDef] = None
    ConnectionEndTime: Optional[str] = None
    PostureComplianceStatuses: Optional[List[str]] = None

class TerminateConnectionStatusTypeDef(BaseValidatorModel):
    ConnectionId: Optional[str] = None
    PreviousStatus: Optional[ClientVpnConnectionStatusTypeDef] = None
    CurrentStatus: Optional[ClientVpnConnectionStatusTypeDef] = None

class CreateClientVpnEndpointResultTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    Status: ClientVpnEndpointStatusTypeDef
    DnsName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClientVpnEndpointResultTypeDef(BaseValidatorModel):
    Status: ClientVpnEndpointStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClientVpnRouteTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    DestinationCidr: Optional[str] = None
    TargetSubnet: Optional[str] = None
    Type: Optional[str] = None
    Origin: Optional[str] = None
    Status: Optional[ClientVpnRouteStatusTypeDef] = None
    Description: Optional[str] = None

class CreateClientVpnRouteResultTypeDef(BaseValidatorModel):
    Status: ClientVpnRouteStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClientVpnRouteResultTypeDef(BaseValidatorModel):
    Status: ClientVpnRouteStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VpnTunnelLogOptionsSpecificationTypeDef(BaseValidatorModel):
    CloudWatchLogOptions: Optional[CloudWatchLogOptionsSpecificationTypeDef] = None

class VpnTunnelLogOptionsTypeDef(BaseValidatorModel):
    CloudWatchLogOptions: Optional[CloudWatchLogOptionsTypeDef] = None

class GetCoipPoolUsageResultTypeDef(BaseValidatorModel):
    CoipPoolId: str
    CoipAddressUsages: List[CoipAddressUsageTypeDef]
    LocalGatewayRouteTableId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCoipCidrResultTypeDef(BaseValidatorModel):
    CoipCidr: CoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCoipCidrResultTypeDef(BaseValidatorModel):
    CoipCidr: CoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcEndpointConnectionNotificationResultTypeDef(BaseValidatorModel):
    ConnectionNotification: ConnectionNotificationTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointConnectionNotificationsResultTypeDef(BaseValidatorModel):
    ConnectionNotificationSet: List[ConnectionNotificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyInstanceEventWindowRequestRequestTypeDef(BaseValidatorModel):
    InstanceEventWindowId: str
    DryRun: Optional[bool] = None
    Name: Optional[str] = None
    TimeRanges: Optional[Sequence[InstanceEventWindowTimeRangeRequestTypeDef]] = None
    CronExpression: Optional[str] = None

class ModifyIpamPoolRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AutoImport: Optional[bool] = None
    AllocationMinNetmaskLength: Optional[int] = None
    AllocationMaxNetmaskLength: Optional[int] = None
    AllocationDefaultNetmaskLength: Optional[int] = None
    ClearAllocationDefaultNetmaskLength: Optional[bool] = None
    AddAllocationResourceTags: Optional[Sequence[RequestIpamResourceTagTypeDef]] = None
    RemoveAllocationResourceTags: Optional[Sequence[RequestIpamResourceTagTypeDef]] = None

class CreateLocalGatewayRouteResultTypeDef(BaseValidatorModel):
    Route: LocalGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteResultTypeDef(BaseValidatorModel):
    Route: LocalGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLocalGatewayRouteResultTypeDef(BaseValidatorModel):
    Route: LocalGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchLocalGatewayRoutesResultTypeDef(BaseValidatorModel):
    Routes: List[LocalGatewayRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef(BaseValidatorModel):
    Egress: bool
    Protocol: str
    RuleAction: RuleActionType
    RuleNumber: int
    CidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None

class CreateNetworkAclEntryRequestRequestTypeDef(BaseValidatorModel):
    Egress: bool
    NetworkAclId: str
    Protocol: str
    RuleAction: RuleActionType
    RuleNumber: int
    CidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None

class NetworkAclEntryTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Egress: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[RuleActionType] = None
    RuleNumber: Optional[int] = None

class ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef(BaseValidatorModel):
    Egress: bool
    Protocol: str
    RuleAction: RuleActionType
    RuleNumber: int
    CidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None

class ReplaceNetworkAclEntryRequestRequestTypeDef(BaseValidatorModel):
    Egress: bool
    NetworkAclId: str
    Protocol: str
    RuleAction: RuleActionType
    RuleNumber: int
    CidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None

class CreateReservedInstancesListingRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    InstanceCount: int
    PriceSchedules: Sequence[PriceScheduleSpecificationTypeDef]
    ReservedInstancesId: str

class CreateStoreImageTaskRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    Bucket: str
    S3ObjectTags: Optional[Sequence[S3ObjectTagTypeDef]] = None
    DryRun: Optional[bool] = None

class ModifyTrafficMirrorFilterRuleRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRuleId: str
    TrafficDirection: Optional[TrafficDirectionType] = None
    RuleNumber: Optional[int] = None
    RuleAction: Optional[TrafficMirrorRuleActionType] = None
    DestinationPortRange: Optional[TrafficMirrorPortRangeRequestTypeDef] = None
    SourcePortRange: Optional[TrafficMirrorPortRangeRequestTypeDef] = None
    Protocol: Optional[int] = None
    DestinationCidrBlock: Optional[str] = None
    SourceCidrBlock: Optional[str] = None
    Description: Optional[str] = None
    RemoveFields: Optional[Sequence[TrafficMirrorFilterRuleFieldType]] = None
    DryRun: Optional[bool] = None

class ModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    PolicyEnabled: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class ModifyVerifiedAccessGroupPolicyRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessGroupId: str
    PolicyEnabled: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class CreateVolumePermissionModificationsTypeDef(BaseValidatorModel):
    Add: Optional[Sequence[CreateVolumePermissionTypeDef]] = None
    Remove: Optional[Sequence[CreateVolumePermissionTypeDef]] = None

class ModifyVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    VpcEndpointId: str
    DryRun: Optional[bool] = None
    ResetPolicy: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    AddRouteTableIds: Optional[Sequence[str]] = None
    RemoveRouteTableIds: Optional[Sequence[str]] = None
    AddSubnetIds: Optional[Sequence[str]] = None
    RemoveSubnetIds: Optional[Sequence[str]] = None
    AddSecurityGroupIds: Optional[Sequence[str]] = None
    RemoveSecurityGroupIds: Optional[Sequence[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DnsOptions: Optional[DnsOptionsSpecificationTypeDef] = None
    PrivateDnsEnabled: Optional[bool] = None
    SubnetConfigurations: Optional[Sequence[SubnetConfigurationTypeDef]] = None

class GetAwsNetworkPerformanceDataRequestRequestTypeDef(BaseValidatorModel):
    DataQueries: Optional[Sequence[DataQueryTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DataResponseTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    Period: Optional[PeriodTypeType] = None
    MetricPoints: Optional[List[MetricPointTypeDef]] = None

class DeleteFleetErrorItemTypeDef(BaseValidatorModel):
    Error: Optional[DeleteFleetErrorTypeDef] = None
    FleetId: Optional[str] = None

class DeleteInstanceEventWindowResultTypeDef(BaseValidatorModel):
    InstanceEventWindowState: InstanceEventWindowStateChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchTemplateVersionsResponseErrorItemTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None
    ResponseError: Optional[ResponseErrorTypeDef] = None

class FailedQueuedPurchaseDeletionTypeDef(BaseValidatorModel):
    Error: Optional[DeleteQueuedReservedInstancesErrorTypeDef] = None
    ReservedInstancesId: Optional[str] = None

class DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef(BaseValidatorModel):
    InstanceTagAttribute: DeregisterInstanceTagAttributeRequestTypeDef
    DryRun: Optional[bool] = None

class DeregisterInstanceEventNotificationAttributesResultTypeDef(BaseValidatorModel):
    InstanceTagAttribute: InstanceTagNotificationAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceEventNotificationAttributesResultTypeDef(BaseValidatorModel):
    InstanceTagAttribute: InstanceTagNotificationAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceEventNotificationAttributesResultTypeDef(BaseValidatorModel):
    InstanceTagAttribute: InstanceTagNotificationAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTransitGatewayMulticastGroupMembersResultTypeDef(BaseValidatorModel):
    DeregisteredMulticastGroupMembers: TransitGatewayMulticastDeregisteredGroupMembersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef(BaseValidatorModel):
    DeregisteredMulticastGroupSources: TransitGatewayMulticastDeregisteredGroupSourcesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressTransfersRequestDescribeAddressTransfersPaginateTypeDef(BaseValidatorModel):
    AllocationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAddressesAttributeRequestDescribeAddressesAttributePaginateTypeDef(BaseValidatorModel):
    AllocationIds: Optional[Sequence[str]] = None
    Attribute: Optional[Literal["domain-name"]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeByoipCidrsRequestDescribeByoipCidrsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCapacityBlockOfferingsRequestDescribeCapacityBlockOfferingsPaginateTypeDef(BaseValidatorModel):
    InstanceType: str
    InstanceCount: int
    CapacityDurationHours: int
    DryRun: Optional[bool] = None
    StartDateRange: Optional[TimestampTypeDef] = None
    EndDateRange: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePrincipalIdFormatRequestDescribePrincipalIdFormatPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Resources: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotFleetInstancesRequestDescribeSpotFleetInstancesPaginateTypeDef(BaseValidatorModel):
    SpotFleetRequestId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotFleetRequestsRequestDescribeSpotFleetRequestsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    SpotFleetRequestIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStaleSecurityGroupsRequestDescribeStaleSecurityGroupsPaginateTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcClassicLinkDnsSupportRequestDescribeVpcClassicLinkDnsSupportPaginateTypeDef(BaseValidatorModel):
    VpcIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAssociatedIpv6PoolCidrsRequestGetAssociatedIpv6PoolCidrsPaginateTypeDef(BaseValidatorModel):
    PoolId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAwsNetworkPerformanceDataRequestGetAwsNetworkPerformanceDataPaginateTypeDef(BaseValidatorModel):
    DataQueries: Optional[Sequence[DataQueryTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGroupsForCapacityReservationRequestGetGroupsForCapacityReservationPaginateTypeDef(BaseValidatorModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamAddressHistoryRequestGetIpamAddressHistoryPaginateTypeDef(BaseValidatorModel):
    Cidr: str
    IpamScopeId: str
    DryRun: Optional[bool] = None
    VpcId: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetManagedPrefixListAssociationsRequestGetManagedPrefixListAssociationsPaginateTypeDef(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetManagedPrefixListEntriesRequestGetManagedPrefixListEntriesPaginateTypeDef(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    TargetVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkInsightsAccessScopeAnalysisFindingsRequestGetNetworkInsightsAccessScopeAnalysisFindingsPaginateTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetVpnConnectionDeviceTypesRequestGetVpnConnectionDeviceTypesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImagesInRecycleBinRequestListImagesInRecycleBinPaginateTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSnapshotsInRecycleBinRequestListSnapshotsInRecycleBinPaginateTypeDef(BaseValidatorModel):
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAddressesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PublicIps: Optional[Sequence[str]] = None
    AllocationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeAvailabilityZonesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ZoneNames: Optional[Sequence[str]] = None
    ZoneIds: Optional[Sequence[str]] = None
    AllAvailabilityZones: Optional[bool] = None
    DryRun: Optional[bool] = None

class DescribeAwsNetworkPerformanceMetricSubscriptionsRequestDescribeAwsNetworkPerformanceMetricSubscriptionsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeBundleTasksRequestRequestTypeDef(BaseValidatorModel):
    BundleIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCapacityReservationFleetsRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationFleetIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCapacityReservationsRequestDescribeCapacityReservationsPaginateTypeDef(BaseValidatorModel):
    CapacityReservationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCapacityReservationsRequestRequestTypeDef(BaseValidatorModel):
    CapacityReservationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCarrierGatewaysRequestDescribeCarrierGatewaysPaginateTypeDef(BaseValidatorModel):
    CarrierGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCarrierGatewaysRequestRequestTypeDef(BaseValidatorModel):
    CarrierGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeClassicLinkInstancesRequestDescribeClassicLinkInstancesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClassicLinkInstancesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeClientVpnAuthorizationRulesRequestDescribeClientVpnAuthorizationRulesPaginateTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnAuthorizationRulesRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None

class DescribeClientVpnConnectionsRequestDescribeClientVpnConnectionsPaginateTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnConnectionsRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class DescribeClientVpnEndpointsRequestDescribeClientVpnEndpointsPaginateTypeDef(BaseValidatorModel):
    ClientVpnEndpointIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnEndpointsRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeClientVpnRoutesRequestDescribeClientVpnRoutesPaginateTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnRoutesRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeClientVpnTargetNetworksRequestDescribeClientVpnTargetNetworksPaginateTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnTargetNetworksRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    AssociationIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCoipPoolsRequestDescribeCoipPoolsPaginateTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCoipPoolsRequestRequestTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeCustomerGatewaysRequestRequestTypeDef(BaseValidatorModel):
    CustomerGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeDhcpOptionsRequestDescribeDhcpOptionsPaginateTypeDef(BaseValidatorModel):
    DhcpOptionsIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDhcpOptionsRequestRequestTypeDef(BaseValidatorModel):
    DhcpOptionsIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEgressOnlyInternetGatewaysRequestDescribeEgressOnlyInternetGatewaysPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    EgressOnlyInternetGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    EgressOnlyInternetGatewayIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeElasticGpusRequestRequestTypeDef(BaseValidatorModel):
    ElasticGpuIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeExportImageTasksRequestDescribeExportImageTasksPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ExportImageTaskIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportImageTasksRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ExportImageTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeExportTasksRequestRequestTypeDef(BaseValidatorModel):
    ExportTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeFastLaunchImagesRequestDescribeFastLaunchImagesPaginateTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFastLaunchImagesRequestRequestTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeFastSnapshotRestoresRequestDescribeFastSnapshotRestoresPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFastSnapshotRestoresRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeFleetInstancesRequestRequestTypeDef(BaseValidatorModel):
    FleetId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeFleetsRequestDescribeFleetsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    FleetIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FleetIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeFlowLogsRequestDescribeFlowLogsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FlowLogIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFlowLogsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FlowLogIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFpgaImagesRequestDescribeFpgaImagesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    FpgaImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFpgaImagesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    FpgaImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeHostReservationOfferingsRequestDescribeHostReservationOfferingsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxDuration: Optional[int] = None
    MinDuration: Optional[int] = None
    OfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHostReservationOfferingsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxDuration: Optional[int] = None
    MaxResults: Optional[int] = None
    MinDuration: Optional[int] = None
    NextToken: Optional[str] = None
    OfferingId: Optional[str] = None

class DescribeHostReservationsRequestDescribeHostReservationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostReservationIdSet: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHostReservationsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostReservationIdSet: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeHostsRequestDescribeHostsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHostsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeIamInstanceProfileAssociationsRequestDescribeIamInstanceProfileAssociationsPaginateTypeDef(BaseValidatorModel):
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIamInstanceProfileAssociationsRequestRequestTypeDef(BaseValidatorModel):
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImagesRequestDescribeImagesPaginateTypeDef(BaseValidatorModel):
    ExecutableUsers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesRequestRequestTypeDef(BaseValidatorModel):
    ExecutableUsers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImportImageTasksRequestDescribeImportImageTasksPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImportImageTasksRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImportSnapshotTasksRequestDescribeImportSnapshotTasksPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImportSnapshotTasksRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceConnectEndpointsRequestDescribeInstanceConnectEndpointsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceConnectEndpointIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceConnectEndpointsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceConnectEndpointIds: Optional[Sequence[str]] = None

class DescribeInstanceCreditSpecificationsRequestDescribeInstanceCreditSpecificationsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceCreditSpecificationsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceEventWindowsRequestDescribeInstanceEventWindowsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceEventWindowIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceEventWindowsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceEventWindowIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceStatusRequestDescribeInstanceStatusPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceStatusRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None

class DescribeInstanceTopologyRequestDescribeInstanceTopologyPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceTopologyRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InstanceIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeInstanceTypeOfferingsRequestDescribeInstanceTypeOfferingsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LocationType: Optional[LocationTypeType] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceTypeOfferingsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LocationType: Optional[LocationTypeType] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceTypesRequestDescribeInstanceTypesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceTypesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstancesRequestDescribeInstancesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInternetGatewaysRequestDescribeInternetGatewaysPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInternetGatewaysRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeIpamPoolsRequestDescribeIpamPoolsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamPoolIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamPoolsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamPoolIds: Optional[Sequence[str]] = None

class DescribeIpamResourceDiscoveriesRequestDescribeIpamResourceDiscoveriesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamResourceDiscoveriesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeIpamResourceDiscoveryAssociationsRequestDescribeIpamResourceDiscoveryAssociationsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryAssociationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeIpamScopesRequestDescribeIpamScopesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamScopeIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamScopesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamScopeIds: Optional[Sequence[str]] = None

class DescribeIpamsRequestDescribeIpamsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamIds: Optional[Sequence[str]] = None

class DescribeIpv6PoolsRequestDescribeIpv6PoolsPaginateTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpv6PoolsRequestRequestTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeKeyPairsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    KeyNames: Optional[Sequence[str]] = None
    KeyPairIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    IncludePublicKey: Optional[bool] = None

class DescribeLaunchTemplateVersionsRequestDescribeLaunchTemplateVersionsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Versions: Optional[Sequence[str]] = None
    MinVersion: Optional[str] = None
    MaxVersion: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ResolveAlias: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchTemplateVersionsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Versions: Optional[Sequence[str]] = None
    MinVersion: Optional[str] = None
    MaxVersion: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ResolveAlias: Optional[bool] = None

class DescribeLaunchTemplatesRequestDescribeLaunchTemplatesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateIds: Optional[Sequence[str]] = None
    LaunchTemplateNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchTemplatesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    LaunchTemplateIds: Optional[Sequence[str]] = None
    LaunchTemplateNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginateTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayRouteTableVpcAssociationsRequestDescribeLocalGatewayRouteTableVpcAssociationsPaginateTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayRouteTablesRequestDescribeLocalGatewayRouteTablesPaginateTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayRouteTablesRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayVirtualInterfaceGroupsRequestDescribeLocalGatewayVirtualInterfaceGroupsPaginateTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayVirtualInterfacesRequestDescribeLocalGatewayVirtualInterfacesPaginateTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewaysRequestDescribeLocalGatewaysPaginateTypeDef(BaseValidatorModel):
    LocalGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewaysRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLockedSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeMacHostsRequestDescribeMacHostsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMacHostsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeManagedPrefixListsRequestDescribeManagedPrefixListsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PrefixListIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeManagedPrefixListsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PrefixListIds: Optional[Sequence[str]] = None

class DescribeMovingAddressesRequestDescribeMovingAddressesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PublicIps: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMovingAddressesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PublicIps: Optional[Sequence[str]] = None

class DescribeNatGatewaysRequestDescribeNatGatewaysPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNatGatewaysRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeNetworkAclsRequestDescribeNetworkAclsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkAclIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkAclsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkAclIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeNetworkInsightsAccessScopeAnalysesRequestDescribeNetworkInsightsAccessScopeAnalysesPaginateTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    AnalysisStartTimeBegin: Optional[TimestampTypeDef] = None
    AnalysisStartTimeEnd: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    AnalysisStartTimeBegin: Optional[TimestampTypeDef] = None
    AnalysisStartTimeEnd: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInsightsAccessScopesRequestDescribeNetworkInsightsAccessScopesPaginateTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsAccessScopesRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInsightsAnalysesRequestDescribeNetworkInsightsAnalysesPaginateTypeDef(BaseValidatorModel):
    NetworkInsightsAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsPathId: Optional[str] = None
    AnalysisStartTime: Optional[TimestampTypeDef] = None
    AnalysisEndTime: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsAnalysesRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsPathId: Optional[str] = None
    AnalysisStartTime: Optional[TimestampTypeDef] = None
    AnalysisEndTime: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInsightsPathsRequestDescribeNetworkInsightsPathsPaginateTypeDef(BaseValidatorModel):
    NetworkInsightsPathIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsPathsRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsPathIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInterfacePermissionsRequestDescribeNetworkInterfacePermissionsPaginateTypeDef(BaseValidatorModel):
    NetworkInterfacePermissionIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInterfacePermissionsRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfacePermissionIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeNetworkInterfacesRequestDescribeNetworkInterfacesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInterfacesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribePlacementGroupsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    GroupNames: Optional[Sequence[str]] = None
    GroupIds: Optional[Sequence[str]] = None

class DescribePrefixListsRequestDescribePrefixListsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PrefixListIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePrefixListsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PrefixListIds: Optional[Sequence[str]] = None

class DescribePublicIpv4PoolsRequestDescribePublicIpv4PoolsPaginateTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePublicIpv4PoolsRequestRequestTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeRegionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    RegionNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    AllRegions: Optional[bool] = None

class DescribeReplaceRootVolumeTasksRequestDescribeReplaceRootVolumeTasksPaginateTypeDef(BaseValidatorModel):
    ReplaceRootVolumeTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplaceRootVolumeTasksRequestRequestTypeDef(BaseValidatorModel):
    ReplaceRootVolumeTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeReservedInstancesListingsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ReservedInstancesId: Optional[str] = None
    ReservedInstancesListingId: Optional[str] = None

class DescribeReservedInstancesModificationsRequestDescribeReservedInstancesModificationsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ReservedInstancesModificationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedInstancesModificationsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ReservedInstancesModificationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeReservedInstancesOfferingsRequestDescribeReservedInstancesOfferingsPaginateTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeMarketplace: Optional[bool] = None
    InstanceType: Optional[InstanceTypeType] = None
    MaxDuration: Optional[int] = None
    MaxInstanceCount: Optional[int] = None
    MinDuration: Optional[int] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    ReservedInstancesOfferingIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    InstanceTenancy: Optional[TenancyType] = None
    OfferingType: Optional[OfferingTypeValuesType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedInstancesOfferingsRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeMarketplace: Optional[bool] = None
    InstanceType: Optional[InstanceTypeType] = None
    MaxDuration: Optional[int] = None
    MaxInstanceCount: Optional[int] = None
    MinDuration: Optional[int] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    ReservedInstancesOfferingIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    InstanceTenancy: Optional[TenancyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OfferingType: Optional[OfferingTypeValuesType] = None

class DescribeReservedInstancesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    ReservedInstancesIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    OfferingType: Optional[OfferingTypeValuesType] = None

class DescribeRouteTablesRequestDescribeRouteTablesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    RouteTableIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRouteTablesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    RouteTableIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSecurityGroupRulesRequestDescribeSecurityGroupRulesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSecurityGroupRulesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSecurityGroupsRequestDescribeSecurityGroupsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    GroupIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSecurityGroupsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    GroupIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSnapshotTierStatusRequestDescribeSnapshotTierStatusPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotTierStatusRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    OwnerIds: Optional[Sequence[str]] = None
    RestorableByUserIds: Optional[Sequence[str]] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerIds: Optional[Sequence[str]] = None
    RestorableByUserIds: Optional[Sequence[str]] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeSpotInstanceRequestsRequestDescribeSpotInstanceRequestsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotInstanceRequestsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSpotPriceHistoryRequestDescribeSpotPriceHistoryPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    ProductDescriptions: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotPriceHistoryRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProductDescriptions: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None

class DescribeStoreImageTasksRequestDescribeStoreImageTasksPaginateTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStoreImageTasksRequestRequestTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSubnetsRequestDescribeSubnetsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubnetsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeTagsRequestDescribeTagsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorFilterRulesRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRuleIds: Optional[Sequence[str]] = None
    TrafficMirrorFilterId: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorFiltersRequestDescribeTrafficMirrorFiltersPaginateTypeDef(BaseValidatorModel):
    TrafficMirrorFilterIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrafficMirrorFiltersRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorFilterIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorSessionsRequestDescribeTrafficMirrorSessionsPaginateTypeDef(BaseValidatorModel):
    TrafficMirrorSessionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrafficMirrorSessionsRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorSessionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorTargetsRequestDescribeTrafficMirrorTargetsPaginateTypeDef(BaseValidatorModel):
    TrafficMirrorTargetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrafficMirrorTargetsRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorTargetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTransitGatewayAttachmentsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayConnectPeersRequestDescribeTransitGatewayConnectPeersPaginateTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeerIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayConnectPeersRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeerIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayConnectsRequestDescribeTransitGatewayConnectsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayConnectsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayMulticastDomainsRequestDescribeTransitGatewayMulticastDomainsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayPeeringAttachmentsRequestDescribeTransitGatewayPeeringAttachmentsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayPolicyTablesRequestDescribeTransitGatewayPolicyTablesPaginateTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayPolicyTablesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayRouteTableAnnouncementsRequestDescribeTransitGatewayRouteTableAnnouncementsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncementIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncementIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayRouteTablesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayVpcAttachmentsRequestDescribeTransitGatewayVpcAttachmentsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewaysRequestDescribeTransitGatewaysPaginateTypeDef(BaseValidatorModel):
    TransitGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewaysRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTrunkInterfaceAssociationsRequestDescribeTrunkInterfaceAssociationsPaginateTypeDef(BaseValidatorModel):
    AssociationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrunkInterfaceAssociationsRequestRequestTypeDef(BaseValidatorModel):
    AssociationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVerifiedAccessEndpointsRequestDescribeVerifiedAccessEndpointsPaginateTypeDef(BaseValidatorModel):
    VerifiedAccessEndpointIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessEndpointsRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessEndpointIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessGroupsRequestDescribeVerifiedAccessGroupsPaginateTypeDef(BaseValidatorModel):
    VerifiedAccessGroupIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessGroupsRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessGroupIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessInstanceLoggingConfigurationsRequestDescribeVerifiedAccessInstanceLoggingConfigurationsPaginateTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessInstancesRequestDescribeVerifiedAccessInstancesPaginateTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessInstancesRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessTrustProvidersRequestDescribeVerifiedAccessTrustProvidersPaginateTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProviderIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProviderIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVolumeStatusRequestDescribeVolumeStatusPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVolumeStatusRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeVolumesModificationsRequestDescribeVolumesModificationsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVolumesModificationsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVolumesRequestDescribeVolumesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVolumesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcClassicLinkRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcIds: Optional[Sequence[str]] = None

class DescribeVpcEndpointConnectionNotificationsRequestDescribeVpcEndpointConnectionNotificationsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConnectionNotificationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ConnectionNotificationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointConnectionsRequestDescribeVpcEndpointConnectionsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointConnectionsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointServiceConfigurationsRequestDescribeVpcEndpointServiceConfigurationsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointServicePermissionsRequestDescribeVpcEndpointServicePermissionsPaginateTypeDef(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointServicePermissionsRequestRequestTypeDef(BaseValidatorModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointServicesRequestDescribeVpcEndpointServicesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointServicesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    ServiceNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointsRequestDescribeVpcEndpointsPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VpcEndpointIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointsRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    VpcEndpointIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcPeeringConnectionsRequestDescribeVpcPeeringConnectionsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcPeeringConnectionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVpcsRequestDescribeVpcsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVpnConnectionsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnConnectionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeVpnGatewaysRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnGatewayIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class ExportTransitGatewayRoutesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    S3Bucket: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class GetCoipPoolUsageRequestRequestTypeDef(BaseValidatorModel):
    PoolId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetIpamDiscoveredAccountsRequestGetIpamDiscoveredAccountsPaginateTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DiscoveryRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamDiscoveredAccountsRequestRequestTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DiscoveryRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetIpamDiscoveredPublicAddressesRequestRequestTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    AddressRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetIpamDiscoveredResourceCidrsRequestGetIpamDiscoveredResourceCidrsPaginateTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    ResourceRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamDiscoveredResourceCidrsRequestRequestTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    ResourceRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetIpamPoolAllocationsRequestGetIpamPoolAllocationsPaginateTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    IpamPoolAllocationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamPoolAllocationsRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    IpamPoolAllocationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetIpamPoolCidrsRequestGetIpamPoolCidrsPaginateTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamPoolCidrsRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetIpamResourceCidrsRequestGetIpamResourceCidrsPaginateTypeDef(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamPoolId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTag: Optional[RequestIpamResourceTagTypeDef] = None
    ResourceOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamResourceCidrsRequestRequestTypeDef(BaseValidatorModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamPoolId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTag: Optional[RequestIpamResourceTagTypeDef] = None
    ResourceOwner: Optional[str] = None

class GetSecurityGroupsForVpcRequestGetSecurityGroupsForVpcPaginateTypeDef(BaseValidatorModel):
    VpcId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSecurityGroupsForVpcRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class GetSubnetCidrReservationsRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetTransitGatewayAttachmentPropagationsRequestGetTransitGatewayAttachmentPropagationsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayMulticastDomainAssociationsRequestGetTransitGatewayMulticastDomainAssociationsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayPolicyTableAssociationsRequestGetTransitGatewayPolicyTableAssociationsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayPolicyTableEntriesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayPrefixListReferencesRequestGetTransitGatewayPrefixListReferencesPaginateTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayPrefixListReferencesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayRouteTableAssociationsRequestGetTransitGatewayRouteTableAssociationsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayRouteTablePropagationsRequestGetTransitGatewayRouteTablePropagationsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class SearchLocalGatewayRoutesRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class SearchLocalGatewayRoutesRequestSearchLocalGatewayRoutesPaginateTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTransitGatewayMulticastGroupsRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class SearchTransitGatewayMulticastGroupsRequestSearchTransitGatewayMulticastGroupsPaginateTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTransitGatewayRoutesRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    Filters: Sequence[FilterTypeDef]
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class DescribeAggregateIdFormatResultTypeDef(BaseValidatorModel):
    UseLongIdsAggregated: bool
    Statuses: List[IdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdFormatResultTypeDef(BaseValidatorModel):
    Statuses: List[IdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityIdFormatResultTypeDef(BaseValidatorModel):
    Statuses: List[IdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PrincipalIdFormatTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Statuses: Optional[List[IdFormatTypeDef]] = None

class DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef(BaseValidatorModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeBundleTasksRequestBundleTaskCompleteWaitTypeDef(BaseValidatorModel):
    BundleIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeConversionTasksRequestConversionTaskCancelledWaitTypeDef(BaseValidatorModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeConversionTasksRequestConversionTaskCompletedWaitTypeDef(BaseValidatorModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeConversionTasksRequestConversionTaskDeletedWaitTypeDef(BaseValidatorModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeCustomerGatewaysRequestCustomerGatewayAvailableWaitTypeDef(BaseValidatorModel):
    CustomerGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeExportTasksRequestExportTaskCancelledWaitTypeDef(BaseValidatorModel):
    ExportTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeExportTasksRequestExportTaskCompletedWaitTypeDef(BaseValidatorModel):
    ExportTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImagesRequestImageAvailableWaitTypeDef(BaseValidatorModel):
    ExecutableUsers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImagesRequestImageExistsWaitTypeDef(BaseValidatorModel):
    ExecutableUsers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImportSnapshotTasksRequestSnapshotImportedWaitTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstanceStatusRequestInstanceStatusOkWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstanceStatusRequestSystemStatusOkWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceExistsWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceRunningWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceStoppedWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceTerminatedWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInternetGatewaysRequestInternetGatewayExistsWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeKeyPairsRequestKeyPairExistsWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    KeyNames: Optional[Sequence[str]] = None
    KeyPairIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    IncludePublicKey: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNatGatewaysRequestNatGatewayAvailableWaitTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNatGatewaysRequestNatGatewayDeletedWaitTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNetworkInterfacesRequestNetworkInterfaceAvailableWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSecurityGroupsRequestSecurityGroupExistsWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    GroupIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSnapshotsRequestSnapshotCompletedWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerIds: Optional[Sequence[str]] = None
    RestorableByUserIds: Optional[Sequence[str]] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSpotInstanceRequestsRequestSpotInstanceRequestFulfilledWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStoreImageTasksRequestStoreImageTaskCompleteWaitTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSubnetsRequestSubnetAvailableWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVolumesRequestVolumeAvailableWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVolumesRequestVolumeDeletedWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVolumesRequestVolumeInUseWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionDeletedWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionExistsWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcsRequestVpcAvailableWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcsRequestVpcExistsWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpnConnectionsRequestVpnConnectionAvailableWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnConnectionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpnConnectionsRequestVpnConnectionDeletedWaitTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnConnectionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPasswordDataRequestPasswordDataAvailableWaitTypeDef(BaseValidatorModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFastLaunchImagesSuccessItemTypeDef(BaseValidatorModel):
    ImageId: Optional[str] = None
    ResourceType: Optional[Literal["snapshot"]] = None
    SnapshotConfiguration: Optional[FastLaunchSnapshotConfigurationResponseTypeDef] = None
    LaunchTemplate: Optional[FastLaunchLaunchTemplateSpecificationResponseTypeDef] = None
    MaxParallelLaunches: Optional[int] = None
    OwnerId: Optional[str] = None
    State: Optional[FastLaunchStateCodeType] = None
    StateTransitionReason: Optional[str] = None
    StateTransitionTime: Optional[datetime] = None

class DisableFastLaunchResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResourceType: Literal["snapshot"]
    SnapshotConfiguration: FastLaunchSnapshotConfigurationResponseTypeDef
    LaunchTemplate: FastLaunchLaunchTemplateSpecificationResponseTypeDef
    MaxParallelLaunches: int
    OwnerId: str
    State: FastLaunchStateCodeType
    StateTransitionReason: str
    StateTransitionTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class EnableFastLaunchResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResourceType: Literal["snapshot"]
    SnapshotConfiguration: FastLaunchSnapshotConfigurationResponseTypeDef
    LaunchTemplate: FastLaunchLaunchTemplateSpecificationResponseTypeDef
    MaxParallelLaunches: int
    OwnerId: str
    State: FastLaunchStateCodeType
    StateTransitionReason: str
    StateTransitionTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFastSnapshotRestoresResultTypeDef(BaseValidatorModel):
    FastSnapshotRestores: List[DescribeFastSnapshotRestoreSuccessItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHostReservationOfferingsResultTypeDef(BaseValidatorModel):
    OfferingSet: List[HostOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstanceCreditSpecificationsResultTypeDef(BaseValidatorModel):
    InstanceCreditSpecifications: List[InstanceCreditSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstanceTopologyResultTypeDef(BaseValidatorModel):
    Instances: List[InstanceTopologyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstanceTypeOfferingsResultTypeDef(BaseValidatorModel):
    InstanceTypeOfferings: List[InstanceTypeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLockedSnapshotsResultTypeDef(BaseValidatorModel):
    Snapshots: List[LockedSnapshotsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMacHostsResultTypeDef(BaseValidatorModel):
    MacHosts: List[MacHostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMovingAddressesResultTypeDef(BaseValidatorModel):
    MovingAddressStatuses: List[MovingAddressStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePrefixListsResultTypeDef(BaseValidatorModel):
    PrefixLists: List[PrefixListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRegionsResultTypeDef(BaseValidatorModel):
    Regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityGroupReferencesResultTypeDef(BaseValidatorModel):
    SecurityGroupReferenceSet: List[SecurityGroupReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotAttributeResultTypeDef(BaseValidatorModel):
    CreateVolumePermissions: List[CreateVolumePermissionTypeDef]
    ProductCodes: List[ProductCodeTypeDef]
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVolumeAttributeResultTypeDef(BaseValidatorModel):
    AutoEnableIO: AttributeBooleanValueTypeDef
    ProductCodes: List[ProductCodeTypeDef]
    VolumeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpotPriceHistoryResultTypeDef(BaseValidatorModel):
    SpotPriceHistory: List[SpotPriceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStoreImageTasksResultTypeDef(BaseValidatorModel):
    StoreImageTaskResults: List[StoreImageTaskResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeTagsResultTypeDef(BaseValidatorModel):
    Tags: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVolumesModificationsResultTypeDef(BaseValidatorModel):
    VolumesModifications: List[VolumeModificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVolumeResultTypeDef(BaseValidatorModel):
    VolumeModification: VolumeModificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FlowLogTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None
    MaxAggregationInterval: Optional[int] = None
    DestinationOptions: Optional[DestinationOptionsResponseTypeDef] = None

class DisableFastSnapshotRestoreStateErrorItemTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Error: Optional[DisableFastSnapshotRestoreStateErrorTypeDef] = None

class DisableTransitGatewayRouteTablePropagationResultTypeDef(BaseValidatorModel):
    Propagation: TransitGatewayPropagationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableTransitGatewayRouteTablePropagationResultTypeDef(BaseValidatorModel):
    Propagation: TransitGatewayPropagationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DiskImageTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Image: Optional[DiskImageDetailTypeDef] = None
    Volume: Optional[VolumeDetailTypeDef] = None

class ImportVolumeRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZone: str
    Image: DiskImageDetailTypeDef
    Volume: VolumeDetailTypeDef
    Description: Optional[str] = None
    DryRun: Optional[bool] = None

class ImportInstanceVolumeDetailItemTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    BytesConverted: Optional[int] = None
    Description: Optional[str] = None
    Image: Optional[DiskImageDescriptionTypeDef] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Volume: Optional[DiskImageVolumeDescriptionTypeDef] = None

class ImportVolumeTaskDetailsTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    BytesConverted: Optional[int] = None
    Description: Optional[str] = None
    Image: Optional[DiskImageDescriptionTypeDef] = None
    Volume: Optional[DiskImageVolumeDescriptionTypeDef] = None

class InstanceStorageInfoTypeDef(BaseValidatorModel):
    TotalSizeInGB: Optional[int] = None
    Disks: Optional[List[DiskInfoTypeDef]] = None
    NvmeSupport: Optional[EphemeralNvmeSupportType] = None
    EncryptionSupport: Optional[InstanceStorageEncryptionSupportType] = None

class VpcEndpointConnectionTypeDef(BaseValidatorModel):
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    VpcEndpointOwner: Optional[str] = None
    VpcEndpointState: Optional[StateType] = None
    CreationTimestamp: Optional[datetime] = None
    DnsEntries: Optional[List[DnsEntryTypeDef]] = None
    NetworkLoadBalancerArns: Optional[List[str]] = None
    GatewayLoadBalancerArns: Optional[List[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    VpcEndpointConnectionId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ModifyClientVpnEndpointRequestRequestTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    ServerCertificateArn: Optional[str] = None
    ConnectionLogOptions: Optional[ConnectionLogOptionsTypeDef] = None
    DnsServers: Optional[DnsServersOptionsModifyStructureTypeDef] = None
    VpnPort: Optional[int] = None
    Description: Optional[str] = None
    SplitTunnel: Optional[bool] = None
    DryRun: Optional[bool] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortal: Optional[SelfServicePortalType] = None
    ClientConnectOptions: Optional[ClientConnectOptionsTypeDef] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ClientLoginBannerOptionsTypeDef] = None

class EbsInfoTypeDef(BaseValidatorModel):
    EbsOptimizedSupport: Optional[EbsOptimizedSupportType] = None
    EncryptionSupport: Optional[EbsEncryptionSupportType] = None
    EbsOptimizedInfo: Optional[EbsOptimizedInfoTypeDef] = None
    NvmeSupport: Optional[EbsNvmeSupportType] = None

class InstanceBlockDeviceMappingSpecificationTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[EbsInstanceBlockDeviceSpecificationTypeDef] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None

class InstanceBlockDeviceMappingTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[EbsInstanceBlockDeviceTypeDef] = None

class EgressOnlyInternetGatewayTypeDef(BaseValidatorModel):
    Attachments: Optional[List[InternetGatewayAttachmentTypeDef]] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class InternetGatewayTypeDef(BaseValidatorModel):
    Attachments: Optional[List[InternetGatewayAttachmentTypeDef]] = None
    InternetGatewayId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ElasticGpusTypeDef(BaseValidatorModel):
    ElasticGpuId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    ElasticGpuType: Optional[str] = None
    ElasticGpuHealth: Optional[ElasticGpuHealthTypeDef] = None
    ElasticGpuState: Optional[Literal["ATTACHED"]] = None
    InstanceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class EnaSrdSpecificationRequestTypeDef(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[EnaSrdUdpSpecificationRequestTypeDef] = None

class EnaSrdSpecificationTypeDef(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[EnaSrdUdpSpecificationTypeDef] = None

class EnableFastLaunchRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    ResourceType: Optional[str] = None
    SnapshotConfiguration: Optional[FastLaunchSnapshotConfigurationRequestTypeDef] = None
    LaunchTemplate: Optional[FastLaunchLaunchTemplateSpecificationRequestTypeDef] = None
    MaxParallelLaunches: Optional[int] = None
    DryRun: Optional[bool] = None

class EnableFastSnapshotRestoreStateErrorItemTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Error: Optional[EnableFastSnapshotRestoreStateErrorTypeDef] = None

class HistoryRecordEntryTypeDef(BaseValidatorModel):
    EventInformation: Optional[EventInformationTypeDef] = None
    EventType: Optional[FleetEventTypeType] = None
    Timestamp: Optional[datetime] = None

class HistoryRecordTypeDef(BaseValidatorModel):
    EventInformation: Optional[EventInformationTypeDef] = None
    EventType: Optional[EventTypeType] = None
    Timestamp: Optional[datetime] = None

class ExportImageResultTypeDef(BaseValidatorModel):
    Description: str
    DiskImageFormat: DiskImageFormatType
    ExportImageTaskId: str
    ImageId: str
    RoleName: str
    Progress: str
    S3ExportLocation: ExportTaskS3LocationTypeDef
    Status: str
    StatusMessage: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportImageTaskTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    ExportImageTaskId: Optional[str] = None
    ImageId: Optional[str] = None
    Progress: Optional[str] = None
    S3ExportLocation: Optional[ExportTaskS3LocationTypeDef] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ExportTaskTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    ExportTaskId: Optional[str] = None
    ExportToS3Task: Optional[ExportToS3TaskTypeDef] = None
    InstanceExportDetails: Optional[InstanceExportDetailsTypeDef] = None
    State: Optional[ExportTaskStateType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class PathFilterTypeDef(BaseValidatorModel):
    SourceAddress: Optional[str] = None
    SourcePortRange: Optional[FilterPortRangeTypeDef] = None
    DestinationAddress: Optional[str] = None
    DestinationPortRange: Optional[FilterPortRangeTypeDef] = None

class FleetSpotMaintenanceStrategiesRequestTypeDef(BaseValidatorModel):
    CapacityRebalance: Optional[FleetSpotCapacityRebalanceRequestTypeDef] = None

class FleetSpotMaintenanceStrategiesTypeDef(BaseValidatorModel):
    CapacityRebalance: Optional[FleetSpotCapacityRebalanceTypeDef] = None

class FpgaDeviceInfoTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    Count: Optional[int] = None
    MemoryInfo: Optional[FpgaDeviceMemoryInfoTypeDef] = None

class FpgaImageAttributeTypeDef(BaseValidatorModel):
    FpgaImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoadPermissions: Optional[List[LoadPermissionTypeDef]] = None
    ProductCodes: Optional[List[ProductCodeTypeDef]] = None

class FpgaImageTypeDef(BaseValidatorModel):
    FpgaImageId: Optional[str] = None
    FpgaImageGlobalId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    ShellVersion: Optional[str] = None
    PciId: Optional[PciIdTypeDef] = None
    State: Optional[FpgaImageStateTypeDef] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    OwnerId: Optional[str] = None
    OwnerAlias: Optional[str] = None
    ProductCodes: Optional[List[ProductCodeTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    Public: Optional[bool] = None
    DataRetentionSupport: Optional[bool] = None
    InstanceTypes: Optional[List[str]] = None

class GetAssociatedIpv6PoolCidrsResultTypeDef(BaseValidatorModel):
    Ipv6CidrAssociations: List[Ipv6CidrAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCapacityReservationUsageResultTypeDef(BaseValidatorModel):
    CapacityReservationId: str
    InstanceType: str
    TotalInstanceCount: int
    AvailableInstanceCount: int
    State: CapacityReservationStateType
    InstanceUsages: List[InstanceUsageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDefaultCreditSpecificationResultTypeDef(BaseValidatorModel):
    InstanceFamilyCreditSpecification: InstanceFamilyCreditSpecificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDefaultCreditSpecificationResultTypeDef(BaseValidatorModel):
    InstanceFamilyCreditSpecification: InstanceFamilyCreditSpecificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostReservationPurchasePreviewResultTypeDef(BaseValidatorModel):
    CurrencyCode: Literal["USD"]
    Purchase: List[PurchaseTypeDef]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseHostReservationResultTypeDef(BaseValidatorModel):
    ClientToken: str
    CurrencyCode: Literal["USD"]
    Purchase: List[PurchaseTypeDef]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceMetadataDefaultsResultTypeDef(BaseValidatorModel):
    AccountLevel: InstanceMetadataDefaultsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceTypesFromInstanceRequirementsResultTypeDef(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeInfoFromInstanceRequirementsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamAddressHistoryResultTypeDef(BaseValidatorModel):
    HistoryRecords: List[IpamAddressHistoryRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetManagedPrefixListAssociationsResultTypeDef(BaseValidatorModel):
    PrefixListAssociations: List[PrefixListAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetManagedPrefixListEntriesResultTypeDef(BaseValidatorModel):
    Entries: List[PrefixListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ReservedInstanceReservationValueTypeDef(BaseValidatorModel):
    ReservationValue: Optional[ReservationValueTypeDef] = None
    ReservedInstanceId: Optional[str] = None

class GetSpotPlacementScoresResultTypeDef(BaseValidatorModel):
    SpotPlacementScores: List[SpotPlacementScoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayAttachmentPropagationsResultTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentPropagations: List[TransitGatewayAttachmentPropagationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayRouteTableAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[TransitGatewayRouteTableAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayRouteTablePropagationsResultTypeDef(BaseValidatorModel):
    TransitGatewayRouteTablePropagations: List[TransitGatewayRouteTablePropagationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetVpnConnectionDeviceTypesResultTypeDef(BaseValidatorModel):
    VpnConnectionDeviceTypes: List[VpnConnectionDeviceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetVpnTunnelReplacementStatusResultTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    TransitGatewayId: str
    CustomerGatewayId: str
    VpnGatewayId: str
    VpnTunnelOutsideIpAddress: str
    MaintenanceDetails: MaintenanceDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GpuDeviceInfoTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    Count: Optional[int] = None
    MemoryInfo: Optional[GpuDeviceMemoryInfoTypeDef] = None

class IamInstanceProfileAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    InstanceId: Optional[str] = None
    IamInstanceProfile: Optional[IamInstanceProfileTypeDef] = None
    State: Optional[IamInstanceProfileAssociationStateType] = None
    Timestamp: Optional[datetime] = None

class LaunchPermissionModificationsTypeDef(BaseValidatorModel):
    Add: Optional[Sequence[LaunchPermissionTypeDef]] = None
    Remove: Optional[Sequence[LaunchPermissionTypeDef]] = None

class ImageDiskContainerTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    DeviceName: Optional[str] = None
    Format: Optional[str] = None
    SnapshotId: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucketTypeDef] = None

class SnapshotDiskContainerTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Format: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucketTypeDef] = None

class ListImagesInRecycleBinResultTypeDef(BaseValidatorModel):
    Images: List[ImageRecycleBinInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LocalGatewayRouteTableTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    Mode: Optional[LocalGatewayRouteTableModeType] = None
    StateReason: Optional[StateReasonTypeDef] = None

class ImportInstanceLaunchSpecificationTypeDef(BaseValidatorModel):
    AdditionalInfo: Optional[str] = None
    Architecture: Optional[ArchitectureValuesType] = None
    GroupIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    InstanceType: Optional[InstanceTypeType] = None
    Monitoring: Optional[bool] = None
    Placement: Optional[PlacementTypeDef] = None
    PrivateIpAddress: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[UserDataTypeDef] = None

class InferenceDeviceInfoTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    MemoryInfo: Optional[InferenceDeviceMemoryInfoTypeDef] = None

class InstanceAttachmentEnaSrdSpecificationTypeDef(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[InstanceAttachmentEnaSrdUdpSpecificationTypeDef] = None

class ModifyInstanceCreditSpecificationRequestRequestTypeDef(BaseValidatorModel):
    InstanceCreditSpecifications: Sequence[InstanceCreditSpecificationRequestTypeDef]
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class ModifyInstanceMetadataOptionsResultTypeDef(BaseValidatorModel):
    InstanceId: str
    InstanceMetadataOptions: InstanceMetadataOptionsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceMonitoringTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    Monitoring: Optional[MonitoringTypeDef] = None

class InstancePrivateIpAddressTypeDef(BaseValidatorModel):
    Association: Optional[InstanceNetworkInterfaceAssociationTypeDef] = None
    Primary: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class InstanceRequirementsExtraOutputTypeDef(BaseValidatorModel):
    VCpuCount: Optional[VCpuCountRangeTypeDef] = None
    MemoryMiB: Optional[MemoryMiBTypeDef] = None
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuTypeDef] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountTypeDef] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBTypeDef] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsTypeDef] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountTypeDef] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBTypeDef] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsTypeDef] = None
    AllowedInstanceTypes: Optional[List[str]] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None

class InstanceRequirementsOutputTypeDef(BaseValidatorModel):
    VCpuCount: Optional[VCpuCountRangeTypeDef] = None
    MemoryMiB: Optional[MemoryMiBTypeDef] = None
    CpuManufacturers: Optional[List[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuTypeDef] = None
    ExcludedInstanceTypes: Optional[List[str]] = None
    InstanceGenerations: Optional[List[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountTypeDef] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[List[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBTypeDef] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsTypeDef] = None
    AcceleratorTypes: Optional[List[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountTypeDef] = None
    AcceleratorManufacturers: Optional[List[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[List[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBTypeDef] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsTypeDef] = None
    AllowedInstanceTypes: Optional[List[str]] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None

class InstanceRequirementsTypeDef(BaseValidatorModel):
    VCpuCount: Optional[VCpuCountRangeTypeDef] = None
    MemoryMiB: Optional[MemoryMiBTypeDef] = None
    CpuManufacturers: Optional[Sequence[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuTypeDef] = None
    ExcludedInstanceTypes: Optional[Sequence[str]] = None
    InstanceGenerations: Optional[Sequence[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountTypeDef] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[Sequence[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBTypeDef] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsTypeDef] = None
    AcceleratorTypes: Optional[Sequence[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountTypeDef] = None
    AcceleratorManufacturers: Optional[Sequence[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[Sequence[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBTypeDef] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsTypeDef] = None
    AllowedInstanceTypes: Optional[Sequence[str]] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None

class InstanceRequirementsRequestTypeDef(BaseValidatorModel):
    VCpuCount: VCpuCountRangeRequestTypeDef
    MemoryMiB: MemoryMiBRequestTypeDef
    CpuManufacturers: Optional[Sequence[CpuManufacturerType]] = None
    MemoryGiBPerVCpu: Optional[MemoryGiBPerVCpuRequestTypeDef] = None
    ExcludedInstanceTypes: Optional[Sequence[str]] = None
    InstanceGenerations: Optional[Sequence[InstanceGenerationType]] = None
    SpotMaxPricePercentageOverLowestPrice: Optional[int] = None
    OnDemandMaxPricePercentageOverLowestPrice: Optional[int] = None
    BareMetal: Optional[BareMetalType] = None
    BurstablePerformance: Optional[BurstablePerformanceType] = None
    RequireHibernateSupport: Optional[bool] = None
    NetworkInterfaceCount: Optional[NetworkInterfaceCountRequestTypeDef] = None
    LocalStorage: Optional[LocalStorageType] = None
    LocalStorageTypes: Optional[Sequence[LocalStorageTypeType]] = None
    TotalLocalStorageGB: Optional[TotalLocalStorageGBRequestTypeDef] = None
    BaselineEbsBandwidthMbps: Optional[BaselineEbsBandwidthMbpsRequestTypeDef] = None
    AcceleratorTypes: Optional[Sequence[AcceleratorTypeType]] = None
    AcceleratorCount: Optional[AcceleratorCountRequestTypeDef] = None
    AcceleratorManufacturers: Optional[Sequence[AcceleratorManufacturerType]] = None
    AcceleratorNames: Optional[Sequence[AcceleratorNameType]] = None
    AcceleratorTotalMemoryMiB: Optional[AcceleratorTotalMemoryMiBRequestTypeDef] = None
    NetworkBandwidthGbps: Optional[NetworkBandwidthGbpsRequestTypeDef] = None
    AllowedInstanceTypes: Optional[Sequence[str]] = None
    MaxSpotPriceAsPercentageOfOptimalOnDemandPrice: Optional[int] = None

class InstanceStateChangeTypeDef(BaseValidatorModel):
    CurrentState: Optional[InstanceStateTypeDef] = None
    InstanceId: Optional[str] = None
    PreviousState: Optional[InstanceStateTypeDef] = None

class InstanceStatusSummaryTypeDef(BaseValidatorModel):
    Details: Optional[List[InstanceStatusDetailsTypeDef]] = None
    Status: Optional[SummaryStatusType] = None

class ModifyInstanceEventStartTimeResultTypeDef(BaseValidatorModel):
    Event: InstanceStatusEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IpPermissionExtraExtraOutputTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[List[IpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[Ipv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[PrefixListIdTypeDef]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPairTypeDef]] = None

class IpPermissionOutputTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[List[IpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[Ipv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[PrefixListIdTypeDef]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPairTypeDef]] = None

class IpPermissionTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[Sequence[IpRangeTypeDef]] = None
    Ipv6Ranges: Optional[Sequence[Ipv6RangeTypeDef]] = None
    PrefixListIds: Optional[Sequence[PrefixListIdTypeDef]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[Sequence[UserIdGroupPairTypeDef]] = None

class StaleIpPermissionTypeDef(BaseValidatorModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[List[str]] = None
    PrefixListIds: Optional[List[str]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPairTypeDef]] = None

class ProvisionIpamPoolCidrRequestRequestTypeDef(BaseValidatorModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None
    CidrAuthorizationContext: Optional[IpamCidrAuthorizationContextTypeDef] = None
    NetmaskLength: Optional[int] = None
    ClientToken: Optional[str] = None

class IpamDiscoveredAccountTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    DiscoveryRegion: Optional[str] = None
    FailureReason: Optional[IpamDiscoveryFailureReasonTypeDef] = None
    LastAttemptedDiscoveryTime: Optional[datetime] = None
    LastSuccessfulDiscoveryTime: Optional[datetime] = None

class IpamDiscoveredResourceCidrTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: Optional[str] = None
    ResourceRegion: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    ResourceCidr: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTags: Optional[List[IpamResourceTagTypeDef]] = None
    IpUsage: Optional[float] = None
    VpcId: Optional[str] = None
    NetworkInterfaceAttachmentStatus: Optional[IpamNetworkInterfaceAttachmentStatusType] = None
    SampleTime: Optional[datetime] = None
    AvailabilityZoneId: Optional[str] = None

class IpamResourceCidrTypeDef(BaseValidatorModel):
    IpamId: Optional[str] = None
    IpamScopeId: Optional[str] = None
    IpamPoolId: Optional[str] = None
    ResourceRegion: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceName: Optional[str] = None
    ResourceCidr: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTags: Optional[List[IpamResourceTagTypeDef]] = None
    IpUsage: Optional[float] = None
    ComplianceStatus: Optional[IpamComplianceStatusType] = None
    ManagementState: Optional[IpamManagementStateType] = None
    OverlapStatus: Optional[IpamOverlapStatusType] = None
    VpcId: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None

class IpamResourceDiscoveryTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    IpamResourceDiscoveryId: Optional[str] = None
    IpamResourceDiscoveryArn: Optional[str] = None
    IpamResourceDiscoveryRegion: Optional[str] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[List[IpamOperatingRegionTypeDef]] = None
    IsDefault: Optional[bool] = None
    State: Optional[IpamResourceDiscoveryStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class IpamTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    IpamId: Optional[str] = None
    IpamArn: Optional[str] = None
    IpamRegion: Optional[str] = None
    PublicDefaultScopeId: Optional[str] = None
    PrivateDefaultScopeId: Optional[str] = None
    ScopeCount: Optional[int] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[List[IpamOperatingRegionTypeDef]] = None
    State: Optional[IpamStateType] = None
    Tags: Optional[List[TagTypeDef]] = None
    DefaultResourceDiscoveryId: Optional[str] = None
    DefaultResourceDiscoveryAssociationId: Optional[str] = None
    ResourceDiscoveryAssociationCount: Optional[int] = None
    StateMessage: Optional[str] = None
    Tier: Optional[IpamTierType] = None

class IpamPoolCidrTypeDef(BaseValidatorModel):
    Cidr: Optional[str] = None
    State: Optional[IpamPoolCidrStateType] = None
    FailureReason: Optional[IpamPoolCidrFailureReasonTypeDef] = None
    IpamPoolCidrId: Optional[str] = None
    NetmaskLength: Optional[int] = None

class IpamPoolTypeDef(BaseValidatorModel):
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
    AllocationResourceTags: Optional[List[IpamResourceTagTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    AwsService: Optional[Literal["ec2"]] = None
    PublicIpSource: Optional[IpamPoolPublicIpSourceType] = None
    SourceResource: Optional[IpamPoolSourceResourceTypeDef] = None

class IpamPublicAddressTagsTypeDef(BaseValidatorModel):
    EipTags: Optional[List[IpamPublicAddressTagTypeDef]] = None

class Ipv6PoolTypeDef(BaseValidatorModel):
    PoolId: Optional[str] = None
    Description: Optional[str] = None
    PoolCidrBlocks: Optional[List[PoolCidrBlockTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None

class LaunchTemplateBlockDeviceMappingRequestTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[LaunchTemplateEbsBlockDeviceRequestTypeDef] = None
    NoDevice: Optional[str] = None

class LaunchTemplateBlockDeviceMappingTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[LaunchTemplateEbsBlockDeviceTypeDef] = None
    NoDevice: Optional[str] = None

class LaunchTemplateEnaSrdSpecificationTypeDef(BaseValidatorModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[LaunchTemplateEnaSrdUdpSpecificationTypeDef] = None

class LaunchTemplateInstanceMarketOptionsTypeDef(BaseValidatorModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[LaunchTemplateSpotMarketOptionsTypeDef] = None

class ListSnapshotsInRecycleBinResultTypeDef(BaseValidatorModel):
    Snapshots: List[SnapshotRecycleBinInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LoadPermissionModificationsTypeDef(BaseValidatorModel):
    Add: Optional[Sequence[LoadPermissionRequestTypeDef]] = None
    Remove: Optional[Sequence[LoadPermissionRequestTypeDef]] = None

class MediaDeviceInfoTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    MemoryInfo: Optional[MediaDeviceMemoryInfoTypeDef] = None

class ModifyIpamRequestRequestTypeDef(BaseValidatorModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AddOperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    RemoveOperatingRegions: Optional[Sequence[RemoveIpamOperatingRegionTypeDef]] = None
    Tier: Optional[IpamTierType] = None

class ModifyIpamResourceDiscoveryRequestRequestTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AddOperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    RemoveOperatingRegions: Optional[Sequence[RemoveIpamOperatingRegionTypeDef]] = None

class ModifyManagedPrefixListRequestRequestTypeDef(BaseValidatorModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    CurrentVersion: Optional[int] = None
    PrefixListName: Optional[str] = None
    AddEntries: Optional[Sequence[AddPrefixListEntryTypeDef]] = None
    RemoveEntries: Optional[Sequence[RemovePrefixListEntryTypeDef]] = None
    MaxEntries: Optional[int] = None

class ModifyReservedInstancesRequestRequestTypeDef(BaseValidatorModel):
    ReservedInstancesIds: Sequence[str]
    TargetConfigurations: Sequence[ReservedInstancesConfigurationTypeDef]
    ClientToken: Optional[str] = None

class ReservedInstancesModificationResultTypeDef(BaseValidatorModel):
    ReservedInstancesId: Optional[str] = None
    TargetConfiguration: Optional[ReservedInstancesConfigurationTypeDef] = None

class ModifyTransitGatewayRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayId: str
    Description: Optional[str] = None
    Options: Optional[ModifyTransitGatewayOptionsTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    AddSubnetIds: Optional[Sequence[str]] = None
    RemoveSubnetIds: Optional[Sequence[str]] = None
    Options: Optional[ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyVerifiedAccessEndpointRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessEndpointId: str
    VerifiedAccessGroupId: Optional[str] = None
    LoadBalancerOptions: Optional[ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef] = None
    NetworkInterfaceOptions: Optional[ModifyVerifiedAccessEndpointEniOptionsTypeDef] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVerifiedAccessEndpointPolicyResultTypeDef(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    SseSpecification: VerifiedAccessSseSpecificationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVerifiedAccessGroupPolicyResultTypeDef(BaseValidatorModel):
    PolicyEnabled: bool
    PolicyDocument: str
    SseSpecification: VerifiedAccessSseSpecificationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VerifiedAccessGroupTypeDef(BaseValidatorModel):
    VerifiedAccessGroupId: Optional[str] = None
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    VerifiedAccessGroupArn: Optional[str] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    DeletionTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationResponseTypeDef] = None

class ModifyVerifiedAccessTrustProviderRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProviderId: str
    OidcOptions: Optional[ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef] = None
    DeviceOptions: Optional[ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef(BaseValidatorModel):
    VpcPeeringConnectionId: str
    AccepterPeeringConnectionOptions: Optional[PeeringConnectionOptionsRequestTypeDef] = None
    DryRun: Optional[bool] = None
    RequesterPeeringConnectionOptions: Optional[PeeringConnectionOptionsRequestTypeDef] = None

class ModifyVpcPeeringConnectionOptionsResultTypeDef(BaseValidatorModel):
    AccepterPeeringConnectionOptions: PeeringConnectionOptionsTypeDef
    RequesterPeeringConnectionOptions: PeeringConnectionOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NatGatewayTypeDef(BaseValidatorModel):
    CreateTime: Optional[datetime] = None
    DeleteTime: Optional[datetime] = None
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None
    NatGatewayAddresses: Optional[List[NatGatewayAddressTypeDef]] = None
    NatGatewayId: Optional[str] = None
    ProvisionedBandwidth: Optional[ProvisionedBandwidthTypeDef] = None
    State: Optional[NatGatewayStateType] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ConnectivityType: Optional[ConnectivityTypeType] = None

class NetworkInfoTypeDef(BaseValidatorModel):
    NetworkPerformance: Optional[str] = None
    MaximumNetworkInterfaces: Optional[int] = None
    MaximumNetworkCards: Optional[int] = None
    DefaultNetworkCardIndex: Optional[int] = None
    NetworkCards: Optional[List[NetworkCardInfoTypeDef]] = None
    Ipv4AddressesPerInterface: Optional[int] = None
    Ipv6AddressesPerInterface: Optional[int] = None
    Ipv6Supported: Optional[bool] = None
    EnaSupport: Optional[EnaSupportType] = None
    EfaSupported: Optional[bool] = None
    EfaInfo: Optional[EfaInfoTypeDef] = None
    EncryptionInTransitSupported: Optional[bool] = None
    EnaSrdSupported: Optional[bool] = None

class NetworkInterfacePrivateIpAddressTypeDef(BaseValidatorModel):
    Association: Optional[NetworkInterfaceAssociationTypeDef] = None
    Primary: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class NetworkInterfacePermissionTypeDef(BaseValidatorModel):
    NetworkInterfacePermissionId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    Permission: Optional[InterfacePermissionTypeType] = None
    PermissionState: Optional[NetworkInterfacePermissionStateTypeDef] = None

class NeuronDeviceInfoTypeDef(BaseValidatorModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    CoreInfo: Optional[NeuronDeviceCoreInfoTypeDef] = None
    MemoryInfo: Optional[NeuronDeviceMemoryInfoTypeDef] = None

class VerifiedAccessTrustProviderTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProviderId: Optional[str] = None
    Description: Optional[str] = None
    TrustProviderType: Optional[TrustProviderTypeType] = None
    UserTrustProviderType: Optional[UserTrustProviderTypeType] = None
    DeviceTrustProviderType: Optional[DeviceTrustProviderTypeType] = None
    OidcOptions: Optional[OidcOptionsTypeDef] = None
    DeviceOptions: Optional[DeviceOptionsTypeDef] = None
    PolicyReferenceName: Optional[str] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationResponseTypeDef] = None

class PathRequestFilterTypeDef(BaseValidatorModel):
    SourceAddress: Optional[str] = None
    SourcePortRange: Optional[RequestFilterPortRangeTypeDef] = None
    DestinationAddress: Optional[str] = None
    DestinationPortRange: Optional[RequestFilterPortRangeTypeDef] = None

class PathStatementRequestTypeDef(BaseValidatorModel):
    PacketHeaderStatement: Optional[PacketHeaderStatementRequestTypeDef] = None
    ResourceStatement: Optional[ResourceStatementRequestTypeDef] = None

class ThroughResourcesStatementRequestTypeDef(BaseValidatorModel):
    ResourceStatement: Optional[ResourceStatementRequestTypeDef] = None

class PathStatementTypeDef(BaseValidatorModel):
    PacketHeaderStatement: Optional[PacketHeaderStatementTypeDef] = None
    ResourceStatement: Optional[ResourceStatementTypeDef] = None

class ThroughResourcesStatementTypeDef(BaseValidatorModel):
    ResourceStatement: Optional[ResourceStatementTypeDef] = None

class ReservedInstancesListingTypeDef(BaseValidatorModel):
    ClientToken: Optional[str] = None
    CreateDate: Optional[datetime] = None
    InstanceCounts: Optional[List[InstanceCountTypeDef]] = None
    PriceSchedules: Optional[List[PriceScheduleTypeDef]] = None
    ReservedInstancesId: Optional[str] = None
    ReservedInstancesListingId: Optional[str] = None
    Status: Optional[ListingStatusType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    UpdateDate: Optional[datetime] = None

class ProvisionPublicIpv4PoolCidrResultTypeDef(BaseValidatorModel):
    PoolId: str
    PoolAddressRange: PublicIpv4PoolRangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PublicIpv4PoolTypeDef(BaseValidatorModel):
    PoolId: Optional[str] = None
    Description: Optional[str] = None
    PoolAddressRanges: Optional[List[PublicIpv4PoolRangeTypeDef]] = None
    TotalAddressCount: Optional[int] = None
    TotalAvailableAddressCount: Optional[int] = None
    NetworkBorderGroup: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class PurchaseScheduledInstancesRequestRequestTypeDef(BaseValidatorModel):
    PurchaseRequests: Sequence[PurchaseRequestTypeDef]
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class PurchaseReservedInstancesOfferingRequestRequestTypeDef(BaseValidatorModel):
    InstanceCount: int
    ReservedInstancesOfferingId: str
    DryRun: Optional[bool] = None
    LimitPrice: Optional[ReservedInstanceLimitPriceTypeDef] = None
    PurchaseTime: Optional[TimestampTypeDef] = None

class ReservedInstancesOfferingTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    InstanceType: Optional[InstanceTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    ReservedInstancesOfferingId: Optional[str] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[Literal["USD"]] = None
    InstanceTenancy: Optional[TenancyType] = None
    Marketplace: Optional[bool] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    OfferingType: Optional[OfferingTypeValuesType] = None
    PricingDetails: Optional[List[PricingDetailTypeDef]] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    Scope: Optional[ScopeType] = None

class ReservedInstancesTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    Duration: Optional[int] = None
    End: Optional[datetime] = None
    FixedPrice: Optional[float] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[InstanceTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    ReservedInstancesId: Optional[str] = None
    Start: Optional[datetime] = None
    State: Optional[ReservedInstanceStateType] = None
    UsagePrice: Optional[float] = None
    CurrencyCode: Optional[Literal["USD"]] = None
    InstanceTenancy: Optional[TenancyType] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    OfferingType: Optional[OfferingTypeValuesType] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    Scope: Optional[ScopeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class SecurityGroupRuleTypeDef(BaseValidatorModel):
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
    ReferencedGroupInfo: Optional[ReferencedSecurityGroupTypeDef] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class RegisterInstanceEventNotificationAttributesRequestRequestTypeDef(BaseValidatorModel):
    InstanceTagAttribute: RegisterInstanceTagAttributeRequestTypeDef
    DryRun: Optional[bool] = None

class RegisterTransitGatewayMulticastGroupMembersResultTypeDef(BaseValidatorModel):
    RegisteredMulticastGroupMembers: TransitGatewayMulticastRegisteredGroupMembersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTransitGatewayMulticastGroupSourcesResultTypeDef(BaseValidatorModel):
    RegisteredMulticastGroupSources: TransitGatewayMulticastRegisteredGroupSourcesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StorageOutputTypeDef(BaseValidatorModel):
    S3: Optional[S3StorageOutputTypeDef] = None

class ScheduledInstanceAvailabilityTypeDef(BaseValidatorModel):
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
    Recurrence: Optional[ScheduledInstanceRecurrenceTypeDef] = None
    SlotDurationInHours: Optional[int] = None
    TotalScheduledInstanceHours: Optional[int] = None

class ScheduledInstanceTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    CreateDate: Optional[datetime] = None
    HourlyPrice: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[str] = None
    NetworkPlatform: Optional[str] = None
    NextSlotStartTime: Optional[datetime] = None
    Platform: Optional[str] = None
    PreviousSlotEndTime: Optional[datetime] = None
    Recurrence: Optional[ScheduledInstanceRecurrenceTypeDef] = None
    ScheduledInstanceId: Optional[str] = None
    SlotDurationInHours: Optional[int] = None
    TermEndDate: Optional[datetime] = None
    TermStartDate: Optional[datetime] = None
    TotalScheduledInstanceHours: Optional[int] = None

class ScheduledInstancesBlockDeviceMappingTypeDef(BaseValidatorModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[ScheduledInstancesEbsTypeDef] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None

class ScheduledInstancesNetworkInterfaceTypeDef(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[Sequence[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[ScheduledInstancesIpv6AddressTypeDef]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddressConfigs: Optional[       Sequence[ScheduledInstancesPrivateIpAddressConfigTypeDef]     ] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None

class SearchTransitGatewayMulticastGroupsResultTypeDef(BaseValidatorModel):
    MulticastGroups: List[TransitGatewayMulticastGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class VpcEndpointTypeDef(BaseValidatorModel):
    VpcEndpointId: Optional[str] = None
    VpcEndpointType: Optional[VpcEndpointTypeType] = None
    VpcId: Optional[str] = None
    ServiceName: Optional[str] = None
    State: Optional[StateType] = None
    PolicyDocument: Optional[str] = None
    RouteTableIds: Optional[List[str]] = None
    SubnetIds: Optional[List[str]] = None
    Groups: Optional[List[SecurityGroupIdentifierTypeDef]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DnsOptions: Optional[DnsOptionsTypeDef] = None
    PrivateDnsEnabled: Optional[bool] = None
    RequesterManaged: Optional[bool] = None
    NetworkInterfaceIds: Optional[List[str]] = None
    DnsEntries: Optional[List[DnsEntryTypeDef]] = None
    CreationTimestamp: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    OwnerId: Optional[str] = None
    LastError: Optional[LastErrorTypeDef] = None

class SecurityGroupRuleUpdateTypeDef(BaseValidatorModel):
    SecurityGroupRuleId: str
    SecurityGroupRule: Optional[SecurityGroupRuleRequestTypeDef] = None

class ServiceConfigurationTypeDef(BaseValidatorModel):
    ServiceType: Optional[List[ServiceTypeDetailTypeDef]] = None
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
    PrivateDnsNameConfiguration: Optional[PrivateDnsNameConfigurationTypeDef] = None
    PayerResponsibility: Optional[Literal["ServiceOwner"]] = None
    Tags: Optional[List[TagTypeDef]] = None

class ServiceDetailTypeDef(BaseValidatorModel):
    ServiceName: Optional[str] = None
    ServiceId: Optional[str] = None
    ServiceType: Optional[List[ServiceTypeDetailTypeDef]] = None
    AvailabilityZones: Optional[List[str]] = None
    Owner: Optional[str] = None
    BaseEndpointDnsNames: Optional[List[str]] = None
    PrivateDnsName: Optional[str] = None
    PrivateDnsNames: Optional[List[PrivateDnsDetailsTypeDef]] = None
    VpcEndpointPolicySupported: Optional[bool] = None
    AcceptanceRequired: Optional[bool] = None
    ManagesVpcEndpoints: Optional[bool] = None
    PayerResponsibility: Optional[Literal["ServiceOwner"]] = None
    Tags: Optional[List[TagTypeDef]] = None
    PrivateDnsNameVerificationState: Optional[DnsNameStateType] = None
    SupportedIpAddressTypes: Optional[List[ServiceConnectivityTypeType]] = None

class SnapshotDetailTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    DeviceName: Optional[str] = None
    DiskImageSize: Optional[float] = None
    Format: Optional[str] = None
    Progress: Optional[str] = None
    SnapshotId: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucketDetailsTypeDef] = None

class SnapshotTaskDetailTypeDef(BaseValidatorModel):
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
    UserBucket: Optional[UserBucketDetailsTypeDef] = None

class SpotMaintenanceStrategiesTypeDef(BaseValidatorModel):
    CapacityRebalance: Optional[SpotCapacityRebalanceTypeDef] = None

class SpotDatafeedSubscriptionTypeDef(BaseValidatorModel):
    Bucket: Optional[str] = None
    Fault: Optional[SpotInstanceStateFaultTypeDef] = None
    OwnerId: Optional[str] = None
    Prefix: Optional[str] = None
    State: Optional[DatafeedSubscriptionStateType] = None

class TransitGatewayMulticastDomainAssociationTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    Subnet: Optional[SubnetAssociationTypeDef] = None

class TransitGatewayMulticastDomainAssociationsTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    Subnets: Optional[List[SubnetAssociationTypeDef]] = None

class SubnetIpv6CidrBlockAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv6CidrBlockState: Optional[SubnetCidrBlockStateTypeDef] = None

class TargetReservationValueTypeDef(BaseValidatorModel):
    ReservationValue: Optional[ReservationValueTypeDef] = None
    TargetConfiguration: Optional[TargetConfigurationTypeDef] = None

class TargetGroupsConfigExtraOutputTypeDef(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroupTypeDef]] = None

class TargetGroupsConfigOutputTypeDef(BaseValidatorModel):
    TargetGroups: Optional[List[TargetGroupTypeDef]] = None

class TargetGroupsConfigTypeDef(BaseValidatorModel):
    TargetGroups: Optional[Sequence[TargetGroupTypeDef]] = None

class TrafficMirrorFilterRuleTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRuleId: Optional[str] = None
    TrafficMirrorFilterId: Optional[str] = None
    TrafficDirection: Optional[TrafficDirectionType] = None
    RuleNumber: Optional[int] = None
    RuleAction: Optional[TrafficMirrorRuleActionType] = None
    Protocol: Optional[int] = None
    DestinationPortRange: Optional[TrafficMirrorPortRangeTypeDef] = None
    SourcePortRange: Optional[TrafficMirrorPortRangeTypeDef] = None
    DestinationCidrBlock: Optional[str] = None
    SourceCidrBlock: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayAttachmentTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    TransitGatewayOwnerId: Optional[str] = None
    ResourceOwnerId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    Association: Optional[TransitGatewayAttachmentAssociationTypeDef] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayConnectPeerConfigurationTypeDef(BaseValidatorModel):
    TransitGatewayAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    Protocol: Optional[Literal["gre"]] = None
    BgpConfigurations: Optional[List[TransitGatewayAttachmentBgpConfigurationTypeDef]] = None

class TransitGatewayConnectTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransportTransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayConnectOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayMulticastDomainTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    TransitGatewayMulticastDomainArn: Optional[str] = None
    OwnerId: Optional[str] = None
    Options: Optional[TransitGatewayMulticastDomainOptionsTypeDef] = None
    State: Optional[TransitGatewayMulticastDomainStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayTypeDef(BaseValidatorModel):
    TransitGatewayId: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    State: Optional[TransitGatewayStateType] = None
    OwnerId: Optional[str] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayPeeringAttachmentTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    AccepterTransitGatewayAttachmentId: Optional[str] = None
    RequesterTgwInfo: Optional[PeeringTgwInfoTypeDef] = None
    AccepterTgwInfo: Optional[PeeringTgwInfoTypeDef] = None
    Options: Optional[TransitGatewayPeeringAttachmentOptionsTypeDef] = None
    Status: Optional[PeeringAttachmentStatusTypeDef] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayPolicyRuleTypeDef(BaseValidatorModel):
    SourceCidrBlock: Optional[str] = None
    SourcePortRange: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPortRange: Optional[str] = None
    Protocol: Optional[str] = None
    MetaData: Optional[TransitGatewayPolicyRuleMetaDataTypeDef] = None

class TransitGatewayPrefixListReferenceTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: Optional[str] = None
    PrefixListId: Optional[str] = None
    PrefixListOwnerId: Optional[str] = None
    State: Optional[TransitGatewayPrefixListReferenceStateType] = None
    Blackhole: Optional[bool] = None
    TransitGatewayAttachment: Optional[TransitGatewayPrefixListAttachmentTypeDef] = None

class TransitGatewayRouteTypeDef(BaseValidatorModel):
    DestinationCidrBlock: Optional[str] = None
    PrefixListId: Optional[str] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None
    TransitGatewayAttachments: Optional[List[TransitGatewayRouteAttachmentTypeDef]] = None
    Type: Optional[TransitGatewayRouteTypeType] = None
    State: Optional[TransitGatewayRouteStateType] = None

class TransitGatewayVpcAttachmentTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcOwnerId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    SubnetIds: Optional[List[str]] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayVpcAttachmentOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class UnsuccessfulInstanceCreditSpecificationItemTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    Error: Optional[UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef] = None

class UnsuccessfulItemTypeDef(BaseValidatorModel):
    Error: Optional[UnsuccessfulItemErrorTypeDef] = None
    ResourceId: Optional[str] = None

class ValidationWarningTypeDef(BaseValidatorModel):
    Errors: Optional[List[ValidationErrorTypeDef]] = None

class VerifiedAccessEndpointTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    VerifiedAccessEndpointId: Optional[str] = None
    ApplicationDomain: Optional[str] = None
    EndpointType: Optional[VerifiedAccessEndpointTypeType] = None
    AttachmentType: Optional[Literal["vpc"]] = None
    DomainCertificateArn: Optional[str] = None
    EndpointDomain: Optional[str] = None
    DeviceValidationDomain: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    LoadBalancerOptions: Optional[VerifiedAccessEndpointLoadBalancerOptionsTypeDef] = None
    NetworkInterfaceOptions: Optional[VerifiedAccessEndpointEniOptionsTypeDef] = None
    Status: Optional[VerifiedAccessEndpointStatusTypeDef] = None
    Description: Optional[str] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    DeletionTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationResponseTypeDef] = None

class VerifiedAccessInstanceTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    VerifiedAccessTrustProviders: Optional[       List[VerifiedAccessTrustProviderCondensedTypeDef]     ] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    FipsEnabled: Optional[bool] = None

class VerifiedAccessLogCloudWatchLogsDestinationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatusTypeDef] = None
    LogGroup: Optional[str] = None

class VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatusTypeDef] = None
    DeliveryStream: Optional[str] = None

class VerifiedAccessLogS3DestinationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatusTypeDef] = None
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None

class VerifiedAccessLogOptionsTypeDef(BaseValidatorModel):
    S3: Optional[VerifiedAccessLogS3DestinationOptionsTypeDef] = None
    CloudWatchLogs: Optional[VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef] = None
    KinesisDataFirehose: Optional[       VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef     ] = None
    LogVersion: Optional[str] = None
    IncludeTrustContext: Optional[bool] = None

class VolumeResponseTypeDef(BaseValidatorModel):
    Attachments: List[VolumeAttachmentTypeDef]
    AvailabilityZone: str
    CreateTime: datetime
    Encrypted: bool
    KmsKeyId: str
    OutpostArn: str
    Size: int
    SnapshotId: str
    State: VolumeStateType
    VolumeId: str
    Iops: int
    Tags: List[TagTypeDef]
    VolumeType: VolumeTypeType
    FastRestored: bool
    MultiAttachEnabled: bool
    Throughput: int
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadataTypeDef

class VolumeTypeDef(BaseValidatorModel):
    Attachments: Optional[List[VolumeAttachmentTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    CreateTime: Optional[datetime] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    OutpostArn: Optional[str] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    State: Optional[VolumeStateType] = None
    VolumeId: Optional[str] = None
    Iops: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None
    VolumeType: Optional[VolumeTypeType] = None
    FastRestored: Optional[bool] = None
    MultiAttachEnabled: Optional[bool] = None
    Throughput: Optional[int] = None
    SseType: Optional[SSETypeType] = None

class VolumeStatusInfoTypeDef(BaseValidatorModel):
    Details: Optional[List[VolumeStatusDetailsTypeDef]] = None
    Status: Optional[VolumeStatusInfoStatusType] = None

class VpcCidrBlockAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    CidrBlock: Optional[str] = None
    CidrBlockState: Optional[VpcCidrBlockStateTypeDef] = None

class VpcIpv6CidrBlockAssociationTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv6CidrBlockState: Optional[VpcCidrBlockStateTypeDef] = None
    NetworkBorderGroup: Optional[str] = None
    Ipv6Pool: Optional[str] = None

class VpcPeeringConnectionVpcInfoTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    Ipv6CidrBlockSet: Optional[List[Ipv6CidrBlockTypeDef]] = None
    CidrBlockSet: Optional[List[CidrBlockTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcPeeringConnectionOptionsDescriptionTypeDef] = None
    VpcId: Optional[str] = None
    Region: Optional[str] = None

class DescribeAccountAttributesResultTypeDef(BaseValidatorModel):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AdditionalDetailTypeDef(BaseValidatorModel):
    AdditionalDetailType: Optional[str] = None
    Component: Optional[AnalysisComponentTypeDef] = None
    VpcEndpointService: Optional[AnalysisComponentTypeDef] = None
    RuleOptions: Optional[List[RuleOptionTypeDef]] = None
    RuleGroupTypePairs: Optional[List[RuleGroupTypePairTypeDef]] = None
    RuleGroupRuleOptionsPairs: Optional[List[RuleGroupRuleOptionsPairTypeDef]] = None
    ServiceName: Optional[str] = None
    LoadBalancers: Optional[List[AnalysisComponentTypeDef]] = None

class DescribeAddressesAttributeResultTypeDef(BaseValidatorModel):
    Addresses: List[AddressAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyAddressAttributeResultTypeDef(BaseValidatorModel):
    Address: AddressAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetAddressAttributeResultTypeDef(BaseValidatorModel):
    Address: AddressAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressesResultTypeDef(BaseValidatorModel):
    Addresses: List[AddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointServicePermissionsResultTypeDef(BaseValidatorModel):
    AllowedPrincipals: List[AllowedPrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCarrierGatewayResultTypeDef(BaseValidatorModel):
    CarrierGateway: CarrierGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCarrierGatewayResultTypeDef(BaseValidatorModel):
    CarrierGateway: CarrierGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCarrierGatewaysResultTypeDef(BaseValidatorModel):
    CarrierGateways: List[CarrierGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCoipPoolResultTypeDef(BaseValidatorModel):
    CoipPool: CoipPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCoipPoolResultTypeDef(BaseValidatorModel):
    CoipPool: CoipPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCoipPoolsResultTypeDef(BaseValidatorModel):
    CoipPools: List[CoipPoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCustomerGatewayResultTypeDef(BaseValidatorModel):
    CustomerGateway: CustomerGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomerGatewaysResultTypeDef(BaseValidatorModel):
    CustomerGateways: List[CustomerGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceConnectEndpointResultTypeDef(BaseValidatorModel):
    InstanceConnectEndpoint: Ec2InstanceConnectEndpointTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInstanceConnectEndpointResultTypeDef(BaseValidatorModel):
    InstanceConnectEndpoint: Ec2InstanceConnectEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceConnectEndpointsResultTypeDef(BaseValidatorModel):
    InstanceConnectEndpoints: List[Ec2InstanceConnectEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHostReservationsResultTypeDef(BaseValidatorModel):
    HostReservationSet: List[HostReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateInstanceEventWindowRequestRequestTypeDef(BaseValidatorModel):
    InstanceEventWindowId: str
    AssociationTarget: InstanceEventWindowAssociationRequestTypeDef
    DryRun: Optional[bool] = None

class InstanceEventWindowTypeDef(BaseValidatorModel):
    InstanceEventWindowId: Optional[str] = None
    TimeRanges: Optional[List[InstanceEventWindowTimeRangeTypeDef]] = None
    Name: Optional[str] = None
    CronExpression: Optional[str] = None
    AssociationTarget: Optional[InstanceEventWindowAssociationTargetTypeDef] = None
    State: Optional[InstanceEventWindowStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class DisassociateInstanceEventWindowRequestRequestTypeDef(BaseValidatorModel):
    InstanceEventWindowId: str
    AssociationTarget: InstanceEventWindowDisassociationRequestTypeDef
    DryRun: Optional[bool] = None

class AssociateIpamResourceDiscoveryResultTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryAssociation: IpamResourceDiscoveryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamResourceDiscoveryAssociationsResultTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryAssociations: List[IpamResourceDiscoveryAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisassociateIpamResourceDiscoveryResultTypeDef(BaseValidatorModel):
    IpamResourceDiscoveryAssociation: IpamResourceDiscoveryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamScopeResultTypeDef(BaseValidatorModel):
    IpamScope: IpamScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamScopeResultTypeDef(BaseValidatorModel):
    IpamScope: IpamScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamScopesResultTypeDef(BaseValidatorModel):
    IpamScopes: List[IpamScopeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamScopeResultTypeDef(BaseValidatorModel):
    IpamScope: IpamScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyPairsResultTypeDef(BaseValidatorModel):
    KeyPairs: List[KeyPairInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchTemplateResultTypeDef(BaseValidatorModel):
    LaunchTemplate: LaunchTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLaunchTemplatesResultTypeDef(BaseValidatorModel):
    LaunchTemplates: List[LaunchTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyLaunchTemplateResultTypeDef(BaseValidatorModel):
    LaunchTemplate: LaunchTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociation: LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociation: LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociations: List[       LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateLocalGatewayRouteTableVpcAssociationResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociation: LocalGatewayRouteTableVpcAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociation: LocalGatewayRouteTableVpcAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableVpcAssociations: List[LocalGatewayRouteTableVpcAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLocalGatewaysResultTypeDef(BaseValidatorModel):
    LocalGateways: List[LocalGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaceGroups: List[LocalGatewayVirtualInterfaceGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLocalGatewayVirtualInterfacesResultTypeDef(BaseValidatorModel):
    LocalGatewayVirtualInterfaces: List[LocalGatewayVirtualInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateManagedPrefixListResultTypeDef(BaseValidatorModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteManagedPrefixListResultTypeDef(BaseValidatorModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeManagedPrefixListsResultTypeDef(BaseValidatorModel):
    PrefixLists: List[ManagedPrefixListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyManagedPrefixListResultTypeDef(BaseValidatorModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreManagedPrefixListVersionResultTypeDef(BaseValidatorModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalyses: List[NetworkInsightsAccessScopeAnalysisTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartNetworkInsightsAccessScopeAnalysisResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysis: NetworkInsightsAccessScopeAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInsightsAccessScopesResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopes: List[NetworkInsightsAccessScopeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreatePlacementGroupResultTypeDef(BaseValidatorModel):
    PlacementGroup: PlacementGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePlacementGroupsResultTypeDef(BaseValidatorModel):
    PlacementGroups: List[PlacementGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplaceRootVolumeTaskResultTypeDef(BaseValidatorModel):
    ReplaceRootVolumeTask: ReplaceRootVolumeTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplaceRootVolumeTasksResultTypeDef(BaseValidatorModel):
    ReplaceRootVolumeTasks: List[ReplaceRootVolumeTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetSecurityGroupsForVpcResultTypeDef(BaseValidatorModel):
    SecurityGroupForVpcs: List[SecurityGroupForVpcTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateSnapshotsResultTypeDef(BaseValidatorModel):
    Snapshots: List[SnapshotInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotTierStatusResultTypeDef(BaseValidatorModel):
    SnapshotTierStatuses: List[SnapshotTierStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSnapshotsResultTypeDef(BaseValidatorModel):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateSubnetCidrReservationResultTypeDef(BaseValidatorModel):
    SubnetCidrReservation: SubnetCidrReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSubnetCidrReservationResultTypeDef(BaseValidatorModel):
    DeletedSubnetCidrReservation: SubnetCidrReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubnetCidrReservationsResultTypeDef(BaseValidatorModel):
    SubnetIpv4CidrReservations: List[SubnetCidrReservationTypeDef]
    SubnetIpv6CidrReservations: List[SubnetCidrReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CopySnapshotRequestSnapshotCopyTypeDef(BaseValidatorModel):
    SourceRegion: str
    Description: Optional[str] = None
    DestinationOutpostArn: Optional[str] = None
    DestinationRegion: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PresignedUrl: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateNetworkAclRequestVpcCreateNetworkAclTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressTypeDef]] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[Sequence[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[Ipv4PrefixSpecificationRequestTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[Sequence[Ipv6PrefixSpecificationRequestTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    InterfaceType: Optional[NetworkInterfaceCreationTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    ClientToken: Optional[str] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None

class CreateRouteTableRequestVpcCreateRouteTableTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef(BaseValidatorModel):
    Description: str
    GroupName: str
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotRequestVolumeCreateSnapshotTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSubnetRequestVpcCreateSubnetTypeDef(BaseValidatorModel):
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    OutpostArn: Optional[str] = None
    DryRun: Optional[bool] = None
    Ipv6Native: Optional[bool] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None

class CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    PeerOwnerId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None

class CreateTrafficMirrorSessionResultTypeDef(BaseValidatorModel):
    TrafficMirrorSession: TrafficMirrorSessionTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorSessionsResultTypeDef(BaseValidatorModel):
    TrafficMirrorSessions: List[TrafficMirrorSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTrafficMirrorSessionResultTypeDef(BaseValidatorModel):
    TrafficMirrorSession: TrafficMirrorSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficMirrorTargetResultTypeDef(BaseValidatorModel):
    TrafficMirrorTarget: TrafficMirrorTargetTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorTargetsResultTypeDef(BaseValidatorModel):
    TrafficMirrorTargets: List[TrafficMirrorTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayPolicyTableResultTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTable: TransitGatewayPolicyTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayPolicyTableResultTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTable: TransitGatewayPolicyTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayPolicyTablesResultTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTables: List[TransitGatewayPolicyTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayRouteTableAnnouncementResultTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncement: TransitGatewayRouteTableAnnouncementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayRouteTableAnnouncementResultTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncement: TransitGatewayRouteTableAnnouncementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableAnnouncements: List[TransitGatewayRouteTableAnnouncementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayRouteTableResultTypeDef(BaseValidatorModel):
    TransitGatewayRouteTable: TransitGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayRouteTableResultTypeDef(BaseValidatorModel):
    TransitGatewayRouteTable: TransitGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayRouteTablesResultTypeDef(BaseValidatorModel):
    TransitGatewayRouteTables: List[TransitGatewayRouteTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateTrunkInterfaceResultTypeDef(BaseValidatorModel):
    InterfaceAssociation: TrunkInterfaceAssociationTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrunkInterfaceAssociationsResultTypeDef(BaseValidatorModel):
    InterfaceAssociations: List[TrunkInterfaceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVpcClassicLinkResultTypeDef(BaseValidatorModel):
    Vpcs: List[VpcClassicLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExplanationTypeDef(BaseValidatorModel):
    Acl: Optional[AnalysisComponentTypeDef] = None
    AclRule: Optional[AnalysisAclRuleTypeDef] = None
    Address: Optional[str] = None
    Addresses: Optional[List[str]] = None
    AttachedTo: Optional[AnalysisComponentTypeDef] = None
    AvailabilityZones: Optional[List[str]] = None
    Cidrs: Optional[List[str]] = None
    Component: Optional[AnalysisComponentTypeDef] = None
    CustomerGateway: Optional[AnalysisComponentTypeDef] = None
    Destination: Optional[AnalysisComponentTypeDef] = None
    DestinationVpc: Optional[AnalysisComponentTypeDef] = None
    Direction: Optional[str] = None
    ExplanationCode: Optional[str] = None
    IngressRouteTable: Optional[AnalysisComponentTypeDef] = None
    InternetGateway: Optional[AnalysisComponentTypeDef] = None
    LoadBalancerArn: Optional[str] = None
    ClassicLoadBalancerListener: Optional[AnalysisLoadBalancerListenerTypeDef] = None
    LoadBalancerListenerPort: Optional[int] = None
    LoadBalancerTarget: Optional[AnalysisLoadBalancerTargetTypeDef] = None
    LoadBalancerTargetGroup: Optional[AnalysisComponentTypeDef] = None
    LoadBalancerTargetGroups: Optional[List[AnalysisComponentTypeDef]] = None
    LoadBalancerTargetPort: Optional[int] = None
    ElasticLoadBalancerListener: Optional[AnalysisComponentTypeDef] = None
    MissingComponent: Optional[str] = None
    NatGateway: Optional[AnalysisComponentTypeDef] = None
    NetworkInterface: Optional[AnalysisComponentTypeDef] = None
    PacketField: Optional[str] = None
    VpcPeeringConnection: Optional[AnalysisComponentTypeDef] = None
    Port: Optional[int] = None
    PortRanges: Optional[List[PortRangeTypeDef]] = None
    PrefixList: Optional[AnalysisComponentTypeDef] = None
    Protocols: Optional[List[str]] = None
    RouteTableRoute: Optional[AnalysisRouteTableRouteTypeDef] = None
    RouteTable: Optional[AnalysisComponentTypeDef] = None
    SecurityGroup: Optional[AnalysisComponentTypeDef] = None
    SecurityGroupRule: Optional[AnalysisSecurityGroupRuleTypeDef] = None
    SecurityGroups: Optional[List[AnalysisComponentTypeDef]] = None
    SourceVpc: Optional[AnalysisComponentTypeDef] = None
    State: Optional[str] = None
    Subnet: Optional[AnalysisComponentTypeDef] = None
    SubnetRouteTable: Optional[AnalysisComponentTypeDef] = None
    Vpc: Optional[AnalysisComponentTypeDef] = None
    VpcEndpoint: Optional[AnalysisComponentTypeDef] = None
    VpnConnection: Optional[AnalysisComponentTypeDef] = None
    VpnGateway: Optional[AnalysisComponentTypeDef] = None
    TransitGateway: Optional[AnalysisComponentTypeDef] = None
    TransitGatewayRouteTable: Optional[AnalysisComponentTypeDef] = None
    TransitGatewayRouteTableRoute: Optional[TransitGatewayRouteTableRouteTypeDef] = None
    TransitGatewayAttachment: Optional[AnalysisComponentTypeDef] = None
    ComponentAccount: Optional[str] = None
    ComponentRegion: Optional[str] = None
    FirewallStatelessRule: Optional[FirewallStatelessRuleTypeDef] = None
    FirewallStatefulRule: Optional[FirewallStatefulRuleTypeDef] = None

class AdvertiseByoipCidrResultTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionByoipCidrResultTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeByoipCidrsResultTypeDef(BaseValidatorModel):
    ByoipCidrs: List[ByoipCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MoveByoipCidrToIpamResultTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionByoipCidrResultTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WithdrawByoipCidrResultTypeDef(BaseValidatorModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClientVpnTargetNetworksResultTypeDef(BaseValidatorModel):
    ClientVpnTargetNetworks: List[TargetNetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RouteTableTypeDef(BaseValidatorModel):
    Associations: Optional[List[RouteTableAssociationTypeDef]] = None
    PropagatingVgws: Optional[List[PropagatingVgwTypeDef]] = None
    RouteTableId: Optional[str] = None
    Routes: Optional[List[RouteTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None

class IntegrateServicesTypeDef(BaseValidatorModel):
    AthenaIntegrations: Optional[Sequence[AthenaIntegrationTypeDef]] = None

class LaunchTemplateInstanceMarketOptionsRequestTypeDef(BaseValidatorModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[LaunchTemplateSpotMarketOptionsRequestTypeDef] = None

class DescribeScheduledInstanceAvailabilityRequestDescribeScheduledInstanceAvailabilityPaginateTypeDef(BaseValidatorModel):
    FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef
    Recurrence: ScheduledInstanceRecurrenceRequestTypeDef
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxSlotDurationInHours: Optional[int] = None
    MinSlotDurationInHours: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledInstanceAvailabilityRequestRequestTypeDef(BaseValidatorModel):
    FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef
    Recurrence: ScheduledInstanceRecurrenceRequestTypeDef
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    MaxSlotDurationInHours: Optional[int] = None
    MinSlotDurationInHours: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeScheduledInstancesRequestDescribeScheduledInstancesPaginateTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ScheduledInstanceIds: Optional[Sequence[str]] = None
    SlotStartTimeRange: Optional[SlotStartTimeRangeRequestTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledInstancesRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ScheduledInstanceIds: Optional[Sequence[str]] = None
    SlotStartTimeRange: Optional[SlotStartTimeRangeRequestTypeDef] = None

class InstanceMarketOptionsRequestTypeDef(BaseValidatorModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[SpotMarketOptionsTypeDef] = None

class CreateVpnGatewayResultTypeDef(BaseValidatorModel):
    VpnGateway: VpnGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpnGatewaysResultTypeDef(BaseValidatorModel):
    VpnGateways: List[VpnGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInterfaceAttachmentTypeDef(BaseValidatorModel):
    AttachTime: Optional[datetime] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    NetworkCardIndex: Optional[int] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    Status: Optional[AttachmentStatusType] = None
    EnaSrdSpecification: Optional[AttachmentEnaSrdSpecificationTypeDef] = None

class DhcpOptionsTypeDef(BaseValidatorModel):
    DhcpConfigurations: Optional[List[DhcpConfigurationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeClientVpnAuthorizationRulesResultTypeDef(BaseValidatorModel):
    AuthorizationRules: List[AuthorizationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAvailabilityZonesResultTypeDef(BaseValidatorModel):
    AvailabilityZones: List[AvailabilityZoneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class HostTypeDef(BaseValidatorModel):
    AutoPlacement: Optional[AutoPlacementType] = None
    AvailabilityZone: Optional[str] = None
    AvailableCapacity: Optional[AvailableCapacityTypeDef] = None
    ClientToken: Optional[str] = None
    HostId: Optional[str] = None
    HostProperties: Optional[HostPropertiesTypeDef] = None
    HostReservationId: Optional[str] = None
    Instances: Optional[List[HostInstanceTypeDef]] = None
    State: Optional[AllocationStateType] = None
    AllocationTime: Optional[datetime] = None
    ReleaseTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None
    HostRecovery: Optional[HostRecoveryType] = None
    AllowsMultipleInstanceTypes: Optional[AllowsMultipleInstanceTypesType] = None
    OwnerId: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    MemberOfServiceLinkedResourceGroup: Optional[bool] = None
    OutpostArn: Optional[str] = None
    HostMaintenance: Optional[HostMaintenanceType] = None
    AssetId: Optional[str] = None

class StorageTypeDef(BaseValidatorModel):
    S3: Optional[S3StorageTypeDef] = None

class CreateImageRequestInstanceCreateImageTypeDef(BaseValidatorModel):
    Name: str
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    NoReboot: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None

class ImageAttributeTypeDef(BaseValidatorModel):
    BlockDeviceMappings: List[BlockDeviceMappingTypeDef]
    ImageId: str
    LaunchPermissions: List[LaunchPermissionTypeDef]
    ProductCodes: List[ProductCodeTypeDef]
    Description: AttributeValueTypeDef
    KernelId: AttributeValueTypeDef
    RamdiskId: AttributeValueTypeDef
    SriovNetSupport: AttributeValueTypeDef
    BootMode: AttributeValueTypeDef
    TpmSupport: AttributeValueTypeDef
    UefiData: AttributeValueTypeDef
    LastLaunchedTime: AttributeValueTypeDef
    ImdsSupport: AttributeValueTypeDef
    DeregistrationProtection: AttributeValueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImageTypeDef(BaseValidatorModel):
    Architecture: Optional[ArchitectureValuesType] = None
    CreationDate: Optional[str] = None
    ImageId: Optional[str] = None
    ImageLocation: Optional[str] = None
    ImageType: Optional[ImageTypeValuesType] = None
    Public: Optional[bool] = None
    KernelId: Optional[str] = None
    OwnerId: Optional[str] = None
    Platform: Optional[Literal["windows"]] = None
    PlatformDetails: Optional[str] = None
    UsageOperation: Optional[str] = None
    ProductCodes: Optional[List[ProductCodeTypeDef]] = None
    RamdiskId: Optional[str] = None
    State: Optional[ImageStateType] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMappingTypeDef]] = None
    Description: Optional[str] = None
    EnaSupport: Optional[bool] = None
    Hypervisor: Optional[HypervisorTypeType] = None
    ImageOwnerAlias: Optional[str] = None
    Name: Optional[str] = None
    RootDeviceName: Optional[str] = None
    RootDeviceType: Optional[DeviceTypeType] = None
    SriovNetSupport: Optional[str] = None
    StateReason: Optional[StateReasonTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    VirtualizationType: Optional[VirtualizationTypeType] = None
    BootMode: Optional[BootModeValuesType] = None
    TpmSupport: Optional[Literal["v2.0"]] = None
    DeprecationTime: Optional[str] = None
    ImdsSupport: Optional[Literal["v2.0"]] = None
    SourceInstanceId: Optional[str] = None
    DeregistrationProtection: Optional[str] = None
    LastLaunchedTime: Optional[str] = None

class CancelCapacityReservationFleetsResultTypeDef(BaseValidatorModel):
    SuccessfulFleetCancellations: List[CapacityReservationFleetCancellationStateTypeDef]
    FailedFleetCancellations: List[FailedCapacityReservationFleetCancellationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelSpotFleetRequestsResponseTypeDef(BaseValidatorModel):
    SuccessfulFleetRequests: List[CancelSpotFleetRequestsSuccessItemTypeDef]
    UnsuccessfulFleetRequests: List[CancelSpotFleetRequestsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCapacityReservationResultTypeDef(BaseValidatorModel):
    CapacityReservation: CapacityReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapacityReservationsResultTypeDef(BaseValidatorModel):
    CapacityReservations: List[CapacityReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseCapacityBlockResultTypeDef(BaseValidatorModel):
    CapacityReservation: CapacityReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapacityReservationFleetsResultTypeDef(BaseValidatorModel):
    CapacityReservationFleets: List[CapacityReservationFleetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    CapacityReservationSpecification: CapacityReservationSpecificationTypeDef
    DryRun: Optional[bool] = None

class DescribeClassicLinkInstancesResultTypeDef(BaseValidatorModel):
    Instances: List[ClassicLinkInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClientVpnEndpointTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[ClientVpnEndpointStatusTypeDef] = None
    CreationTime: Optional[str] = None
    DeletionTime: Optional[str] = None
    DnsName: Optional[str] = None
    ClientCidrBlock: Optional[str] = None
    DnsServers: Optional[List[str]] = None
    SplitTunnel: Optional[bool] = None
    VpnProtocol: Optional[Literal["openvpn"]] = None
    TransportProtocol: Optional[TransportProtocolType] = None
    VpnPort: Optional[int] = None
    AssociatedTargetNetworks: Optional[List[AssociatedTargetNetworkTypeDef]] = None
    ServerCertificateArn: Optional[str] = None
    AuthenticationOptions: Optional[List[ClientVpnAuthenticationTypeDef]] = None
    ConnectionLogOptions: Optional[ConnectionLogResponseOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    SecurityGroupIds: Optional[List[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortalUrl: Optional[str] = None
    ClientConnectOptions: Optional[ClientConnectResponseOptionsTypeDef] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ClientLoginBannerResponseOptionsTypeDef] = None

class DescribeClientVpnConnectionsResultTypeDef(BaseValidatorModel):
    Connections: List[ClientVpnConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TerminateClientVpnConnectionsResultTypeDef(BaseValidatorModel):
    ClientVpnEndpointId: str
    Username: str
    ConnectionStatuses: List[TerminateConnectionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClientVpnRoutesResultTypeDef(BaseValidatorModel):
    Routes: List[ClientVpnRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVpnTunnelOptionsSpecificationTypeDef(BaseValidatorModel):
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
    Phase1EncryptionAlgorithms: Optional[       Sequence[Phase1EncryptionAlgorithmsRequestListValueTypeDef]     ] = None
    Phase2EncryptionAlgorithms: Optional[       Sequence[Phase2EncryptionAlgorithmsRequestListValueTypeDef]     ] = None
    Phase1IntegrityAlgorithms: Optional[       Sequence[Phase1IntegrityAlgorithmsRequestListValueTypeDef]     ] = None
    Phase2IntegrityAlgorithms: Optional[       Sequence[Phase2IntegrityAlgorithmsRequestListValueTypeDef]     ] = None
    Phase1DHGroupNumbers: Optional[Sequence[Phase1DHGroupNumbersRequestListValueTypeDef]] = None
    Phase2DHGroupNumbers: Optional[Sequence[Phase2DHGroupNumbersRequestListValueTypeDef]] = None
    IKEVersions: Optional[Sequence[IKEVersionsRequestListValueTypeDef]] = None
    StartupAction: Optional[str] = None
    LogOptions: Optional[VpnTunnelLogOptionsSpecificationTypeDef] = None
    EnableTunnelLifecycleControl: Optional[bool] = None

class VpnTunnelOptionsSpecificationTypeDef(BaseValidatorModel):
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
    Phase1EncryptionAlgorithms: Optional[       Sequence[Phase1EncryptionAlgorithmsRequestListValueTypeDef]     ] = None
    Phase2EncryptionAlgorithms: Optional[       Sequence[Phase2EncryptionAlgorithmsRequestListValueTypeDef]     ] = None
    Phase1IntegrityAlgorithms: Optional[       Sequence[Phase1IntegrityAlgorithmsRequestListValueTypeDef]     ] = None
    Phase2IntegrityAlgorithms: Optional[       Sequence[Phase2IntegrityAlgorithmsRequestListValueTypeDef]     ] = None
    Phase1DHGroupNumbers: Optional[Sequence[Phase1DHGroupNumbersRequestListValueTypeDef]] = None
    Phase2DHGroupNumbers: Optional[Sequence[Phase2DHGroupNumbersRequestListValueTypeDef]] = None
    IKEVersions: Optional[Sequence[IKEVersionsRequestListValueTypeDef]] = None
    StartupAction: Optional[str] = None
    LogOptions: Optional[VpnTunnelLogOptionsSpecificationTypeDef] = None
    EnableTunnelLifecycleControl: Optional[bool] = None

class TunnelOptionTypeDef(BaseValidatorModel):
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
    Phase1EncryptionAlgorithms: Optional[List[Phase1EncryptionAlgorithmsListValueTypeDef]] = None
    Phase2EncryptionAlgorithms: Optional[List[Phase2EncryptionAlgorithmsListValueTypeDef]] = None
    Phase1IntegrityAlgorithms: Optional[List[Phase1IntegrityAlgorithmsListValueTypeDef]] = None
    Phase2IntegrityAlgorithms: Optional[List[Phase2IntegrityAlgorithmsListValueTypeDef]] = None
    Phase1DHGroupNumbers: Optional[List[Phase1DHGroupNumbersListValueTypeDef]] = None
    Phase2DHGroupNumbers: Optional[List[Phase2DHGroupNumbersListValueTypeDef]] = None
    IkeVersions: Optional[List[IKEVersionsListValueTypeDef]] = None
    StartupAction: Optional[str] = None
    LogOptions: Optional[VpnTunnelLogOptionsTypeDef] = None
    EnableTunnelLifecycleControl: Optional[bool] = None

class NetworkAclTypeDef(BaseValidatorModel):
    Associations: Optional[List[NetworkAclAssociationTypeDef]] = None
    Entries: Optional[List[NetworkAclEntryTypeDef]] = None
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None

class ModifySnapshotAttributeRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str
    Attribute: Optional[SnapshotAttributeNameType] = None
    CreateVolumePermission: Optional[CreateVolumePermissionModificationsTypeDef] = None
    GroupNames: Optional[Sequence[str]] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef(BaseValidatorModel):
    Attribute: Optional[SnapshotAttributeNameType] = None
    CreateVolumePermission: Optional[CreateVolumePermissionModificationsTypeDef] = None
    GroupNames: Optional[Sequence[str]] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class GetAwsNetworkPerformanceDataResultTypeDef(BaseValidatorModel):
    DataResponses: List[DataResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeleteFleetsResultTypeDef(BaseValidatorModel):
    SuccessfulFleetDeletions: List[DeleteFleetSuccessItemTypeDef]
    UnsuccessfulFleetDeletions: List[DeleteFleetErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchTemplateVersionsResultTypeDef(BaseValidatorModel):
    SuccessfullyDeletedLaunchTemplateVersions: List[       DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef     ]
    UnsuccessfullyDeletedLaunchTemplateVersions: List[       DeleteLaunchTemplateVersionsResponseErrorItemTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteQueuedReservedInstancesResultTypeDef(BaseValidatorModel):
    SuccessfulQueuedPurchaseDeletions: List[SuccessfulQueuedPurchaseDeletionTypeDef]
    FailedQueuedPurchaseDeletions: List[FailedQueuedPurchaseDeletionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePrincipalIdFormatResultTypeDef(BaseValidatorModel):
    Principals: List[PrincipalIdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFastLaunchImagesResultTypeDef(BaseValidatorModel):
    FastLaunchImages: List[DescribeFastLaunchImagesSuccessItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFlowLogsResultTypeDef(BaseValidatorModel):
    FlowLogs: List[FlowLogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisableFastSnapshotRestoreErrorItemTypeDef(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    FastSnapshotRestoreStateErrors: Optional[       List[DisableFastSnapshotRestoreStateErrorItemTypeDef]     ] = None

class ImportInstanceTaskDetailsTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    InstanceId: Optional[str] = None
    Platform: Optional[Literal["windows"]] = None
    Volumes: Optional[List[ImportInstanceVolumeDetailItemTypeDef]] = None

class DescribeVpcEndpointConnectionsResultTypeDef(BaseValidatorModel):
    VpcEndpointConnections: List[VpcEndpointConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef(BaseValidatorModel):
    SourceDestCheck: Optional[AttributeBooleanValueTypeDef] = None
    Attribute: Optional[InstanceAttributeNameType] = None
    BlockDeviceMappings: Optional[       Sequence[InstanceBlockDeviceMappingSpecificationTypeDef]     ] = None
    DisableApiTermination: Optional[AttributeBooleanValueTypeDef] = None
    DryRun: Optional[bool] = None
    EbsOptimized: Optional[AttributeBooleanValueTypeDef] = None
    EnaSupport: Optional[AttributeBooleanValueTypeDef] = None
    Groups: Optional[Sequence[str]] = None
    InstanceInitiatedShutdownBehavior: Optional[AttributeValueTypeDef] = None
    InstanceType: Optional[AttributeValueTypeDef] = None
    Kernel: Optional[AttributeValueTypeDef] = None
    Ramdisk: Optional[AttributeValueTypeDef] = None
    SriovNetSupport: Optional[AttributeValueTypeDef] = None
    UserData: Optional[BlobAttributeValueTypeDef] = None
    Value: Optional[str] = None
    DisableApiStop: Optional[AttributeBooleanValueTypeDef] = None

class ModifyInstanceAttributeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SourceDestCheck: Optional[AttributeBooleanValueTypeDef] = None
    Attribute: Optional[InstanceAttributeNameType] = None
    BlockDeviceMappings: Optional[       Sequence[InstanceBlockDeviceMappingSpecificationTypeDef]     ] = None
    DisableApiTermination: Optional[AttributeBooleanValueTypeDef] = None
    DryRun: Optional[bool] = None
    EbsOptimized: Optional[AttributeBooleanValueTypeDef] = None
    EnaSupport: Optional[AttributeBooleanValueTypeDef] = None
    Groups: Optional[Sequence[str]] = None
    InstanceInitiatedShutdownBehavior: Optional[AttributeValueTypeDef] = None
    InstanceType: Optional[AttributeValueTypeDef] = None
    Kernel: Optional[AttributeValueTypeDef] = None
    Ramdisk: Optional[AttributeValueTypeDef] = None
    SriovNetSupport: Optional[AttributeValueTypeDef] = None
    UserData: Optional[BlobAttributeValueTypeDef] = None
    Value: Optional[str] = None
    DisableApiStop: Optional[AttributeBooleanValueTypeDef] = None

class InstanceAttributeTypeDef(BaseValidatorModel):
    Groups: List[GroupIdentifierTypeDef]
    BlockDeviceMappings: List[InstanceBlockDeviceMappingTypeDef]
    DisableApiTermination: AttributeBooleanValueTypeDef
    EnaSupport: AttributeBooleanValueTypeDef
    EnclaveOptions: EnclaveOptionsTypeDef
    EbsOptimized: AttributeBooleanValueTypeDef
    InstanceId: str
    InstanceInitiatedShutdownBehavior: AttributeValueTypeDef
    InstanceType: AttributeValueTypeDef
    KernelId: AttributeValueTypeDef
    ProductCodes: List[ProductCodeTypeDef]
    RamdiskId: AttributeValueTypeDef
    RootDeviceName: AttributeValueTypeDef
    SourceDestCheck: AttributeBooleanValueTypeDef
    SriovNetSupport: AttributeValueTypeDef
    UserData: AttributeValueTypeDef
    DisableApiStop: AttributeBooleanValueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEgressOnlyInternetGatewayResultTypeDef(BaseValidatorModel):
    ClientToken: str
    EgressOnlyInternetGateway: EgressOnlyInternetGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEgressOnlyInternetGatewaysResultTypeDef(BaseValidatorModel):
    EgressOnlyInternetGateways: List[EgressOnlyInternetGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateInternetGatewayResultTypeDef(BaseValidatorModel):
    InternetGateway: InternetGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInternetGatewaysResultTypeDef(BaseValidatorModel):
    InternetGateways: List[InternetGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeElasticGpusResultTypeDef(BaseValidatorModel):
    ElasticGpuSet: List[ElasticGpusTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceNetworkInterfaceSpecificationExtraOutputTypeDef(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6AddressTypeDef]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    AssociateCarrierIpAddress: Optional[bool] = None
    InterfaceType: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequestTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequestTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationRequestTypeDef] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None

class InstanceNetworkInterfaceSpecificationOutputTypeDef(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6AddressTypeDef]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    AssociateCarrierIpAddress: Optional[bool] = None
    InterfaceType: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationRequestTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationRequestTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationRequestTypeDef] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None

class InstanceNetworkInterfaceSpecificationTypeDef(BaseValidatorModel):
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[Sequence[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressTypeDef]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[Sequence[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    AssociateCarrierIpAddress: Optional[bool] = None
    InterfaceType: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[Ipv4PrefixSpecificationRequestTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[Sequence[Ipv6PrefixSpecificationRequestTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationRequestTypeDef] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None

class LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[Sequence[str]] = None
    InterfaceType: Optional[str] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressRequestTypeDef]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[Sequence[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[Ipv4PrefixSpecificationRequestTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[Sequence[Ipv6PrefixSpecificationRequestTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationRequestTypeDef] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None

class AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef(BaseValidatorModel):
    DeviceIndex: int
    InstanceId: str
    DryRun: Optional[bool] = None
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationTypeDef] = None

class AttachNetworkInterfaceRequestRequestTypeDef(BaseValidatorModel):
    DeviceIndex: int
    InstanceId: str
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationTypeDef] = None

class ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef(BaseValidatorModel):
    Attachment: Optional[NetworkInterfaceAttachmentChangesTypeDef] = None
    Description: Optional[AttributeValueTypeDef] = None
    DryRun: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    SourceDestCheck: Optional[AttributeBooleanValueTypeDef] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationTypeDef] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None
    AssociatePublicIpAddress: Optional[bool] = None

class ModifyNetworkInterfaceAttributeRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    Attachment: Optional[NetworkInterfaceAttachmentChangesTypeDef] = None
    Description: Optional[AttributeValueTypeDef] = None
    DryRun: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    SourceDestCheck: Optional[AttributeBooleanValueTypeDef] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationTypeDef] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None
    AssociatePublicIpAddress: Optional[bool] = None

class EnableFastSnapshotRestoreErrorItemTypeDef(BaseValidatorModel):
    SnapshotId: Optional[str] = None
    FastSnapshotRestoreStateErrors: Optional[       List[EnableFastSnapshotRestoreStateErrorItemTypeDef]     ] = None

class DescribeFleetHistoryResultTypeDef(BaseValidatorModel):
    HistoryRecords: List[HistoryRecordEntryTypeDef]
    LastEvaluatedTime: datetime
    FleetId: str
    StartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestHistoryResponseTypeDef(BaseValidatorModel):
    HistoryRecords: List[HistoryRecordTypeDef]
    LastEvaluatedTime: datetime
    SpotFleetRequestId: str
    StartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeExportImageTasksResultTypeDef(BaseValidatorModel):
    ExportImageTasks: List[ExportImageTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateInstanceExportTaskResultTypeDef(BaseValidatorModel):
    ExportTask: ExportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportTasksResultTypeDef(BaseValidatorModel):
    ExportTasks: List[ExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInsightsPathTypeDef(BaseValidatorModel):
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
    Tags: Optional[List[TagTypeDef]] = None
    FilterAtSource: Optional[PathFilterTypeDef] = None
    FilterAtDestination: Optional[PathFilterTypeDef] = None

class SpotOptionsRequestTypeDef(BaseValidatorModel):
    AllocationStrategy: Optional[SpotAllocationStrategyType] = None
    MaintenanceStrategies: Optional[FleetSpotMaintenanceStrategiesRequestTypeDef] = None
    InstanceInterruptionBehavior: Optional[SpotInstanceInterruptionBehaviorType] = None
    InstancePoolsToUseCount: Optional[int] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class SpotOptionsTypeDef(BaseValidatorModel):
    AllocationStrategy: Optional[SpotAllocationStrategyType] = None
    MaintenanceStrategies: Optional[FleetSpotMaintenanceStrategiesTypeDef] = None
    InstanceInterruptionBehavior: Optional[SpotInstanceInterruptionBehaviorType] = None
    InstancePoolsToUseCount: Optional[int] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class FpgaInfoTypeDef(BaseValidatorModel):
    Fpgas: Optional[List[FpgaDeviceInfoTypeDef]] = None
    TotalFpgaMemoryInMiB: Optional[int] = None

class DescribeFpgaImageAttributeResultTypeDef(BaseValidatorModel):
    FpgaImageAttribute: FpgaImageAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyFpgaImageAttributeResultTypeDef(BaseValidatorModel):
    FpgaImageAttribute: FpgaImageAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFpgaImagesResultTypeDef(BaseValidatorModel):
    FpgaImages: List[FpgaImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GpuInfoTypeDef(BaseValidatorModel):
    Gpus: Optional[List[GpuDeviceInfoTypeDef]] = None
    TotalGpuMemoryInMiB: Optional[int] = None

class AssociateIamInstanceProfileResultTypeDef(BaseValidatorModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIamInstanceProfileAssociationsResultTypeDef(BaseValidatorModel):
    IamInstanceProfileAssociations: List[IamInstanceProfileAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisassociateIamInstanceProfileResultTypeDef(BaseValidatorModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceIamInstanceProfileAssociationResultTypeDef(BaseValidatorModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyImageAttributeRequestImageModifyAttributeTypeDef(BaseValidatorModel):
    Attribute: Optional[str] = None
    Description: Optional[AttributeValueTypeDef] = None
    LaunchPermission: Optional[LaunchPermissionModificationsTypeDef] = None
    OperationType: Optional[OperationTypeType] = None
    ProductCodes: Optional[Sequence[str]] = None
    UserGroups: Optional[Sequence[str]] = None
    UserIds: Optional[Sequence[str]] = None
    Value: Optional[str] = None
    DryRun: Optional[bool] = None
    OrganizationArns: Optional[Sequence[str]] = None
    OrganizationalUnitArns: Optional[Sequence[str]] = None
    ImdsSupport: Optional[AttributeValueTypeDef] = None

class ModifyImageAttributeRequestRequestTypeDef(BaseValidatorModel):
    ImageId: str
    Attribute: Optional[str] = None
    Description: Optional[AttributeValueTypeDef] = None
    LaunchPermission: Optional[LaunchPermissionModificationsTypeDef] = None
    OperationType: Optional[OperationTypeType] = None
    ProductCodes: Optional[Sequence[str]] = None
    UserGroups: Optional[Sequence[str]] = None
    UserIds: Optional[Sequence[str]] = None
    Value: Optional[str] = None
    DryRun: Optional[bool] = None
    OrganizationArns: Optional[Sequence[str]] = None
    OrganizationalUnitArns: Optional[Sequence[str]] = None
    ImdsSupport: Optional[AttributeValueTypeDef] = None

class CreateLocalGatewayRouteTableResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTable: LocalGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteTableResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTable: LocalGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocalGatewayRouteTablesResultTypeDef(BaseValidatorModel):
    LocalGatewayRouteTables: List[LocalGatewayRouteTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportInstanceRequestRequestTypeDef(BaseValidatorModel):
    Platform: Literal["windows"]
    Description: Optional[str] = None
    DiskImages: Optional[Sequence[DiskImageTypeDef]] = None
    DryRun: Optional[bool] = None
    LaunchSpecification: Optional[ImportInstanceLaunchSpecificationTypeDef] = None

class InferenceAcceleratorInfoTypeDef(BaseValidatorModel):
    Accelerators: Optional[List[InferenceDeviceInfoTypeDef]] = None
    TotalInferenceMemoryInMiB: Optional[int] = None

class InstanceNetworkInterfaceAttachmentTypeDef(BaseValidatorModel):
    AttachTime: Optional[datetime] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    Status: Optional[AttachmentStatusType] = None
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[InstanceAttachmentEnaSrdSpecificationTypeDef] = None

class MonitorInstancesResultTypeDef(BaseValidatorModel):
    InstanceMonitorings: List[InstanceMonitoringTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UnmonitorInstancesResultTypeDef(BaseValidatorModel):
    InstanceMonitorings: List[InstanceMonitoringTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchTemplateOverridesExtraOutputTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsExtraOutputTypeDef] = None

class FleetLaunchTemplateOverridesTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    MaxPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    Placement: Optional[PlacementResponseTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None
    ImageId: Optional[str] = None

class LaunchTemplateOverridesOutputTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None

class LaunchTemplateOverridesTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsTypeDef] = None

class FleetLaunchTemplateOverridesRequestTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    MaxPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    Placement: Optional[PlacementTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsRequestTypeDef] = None
    ImageId: Optional[str] = None

class GetInstanceTypesFromInstanceRequirementsRequestGetInstanceTypesFromInstanceRequirementsPaginateTypeDef(BaseValidatorModel):
    ArchitectureTypes: Sequence[ArchitectureTypeType]
    VirtualizationTypes: Sequence[VirtualizationTypeType]
    InstanceRequirements: InstanceRequirementsRequestTypeDef
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef(BaseValidatorModel):
    ArchitectureTypes: Sequence[ArchitectureTypeType]
    VirtualizationTypes: Sequence[VirtualizationTypeType]
    InstanceRequirements: InstanceRequirementsRequestTypeDef
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class InstanceRequirementsWithMetadataRequestTypeDef(BaseValidatorModel):
    ArchitectureTypes: Optional[Sequence[ArchitectureTypeType]] = None
    VirtualizationTypes: Optional[Sequence[VirtualizationTypeType]] = None
    InstanceRequirements: Optional[InstanceRequirementsRequestTypeDef] = None

class StartInstancesResultTypeDef(BaseValidatorModel):
    StartingInstances: List[InstanceStateChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopInstancesResultTypeDef(BaseValidatorModel):
    StoppingInstances: List[InstanceStateChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateInstancesResultTypeDef(BaseValidatorModel):
    TerminatingInstances: List[InstanceStateChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceStatusTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    OutpostArn: Optional[str] = None
    Events: Optional[List[InstanceStatusEventTypeDef]] = None
    InstanceId: Optional[str] = None
    InstanceState: Optional[InstanceStateTypeDef] = None
    InstanceStatus: Optional[InstanceStatusSummaryTypeDef] = None
    SystemStatus: Optional[InstanceStatusSummaryTypeDef] = None

class RevokeSecurityGroupEgressResultTypeDef(BaseValidatorModel):
    Return: bool
    UnknownIpPermissions: List[IpPermissionExtraExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    Return: bool
    UnknownIpPermissions: List[IpPermissionExtraExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SecurityGroupTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionOutputTypeDef]] = None
    OwnerId: Optional[str] = None
    GroupId: Optional[str] = None
    IpPermissionsEgress: Optional[List[IpPermissionOutputTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None

class AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    ToPort: Optional[int] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None

class AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None

class RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    IpPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    ToPort: Optional[int] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None

class RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    DryRun: Optional[bool] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None

class StaleSecurityGroupTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    StaleIpPermissions: Optional[List[StaleIpPermissionTypeDef]] = None
    StaleIpPermissionsEgress: Optional[List[StaleIpPermissionTypeDef]] = None
    VpcId: Optional[str] = None

class GetIpamDiscoveredAccountsResultTypeDef(BaseValidatorModel):
    IpamDiscoveredAccounts: List[IpamDiscoveredAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamDiscoveredResourceCidrsResultTypeDef(BaseValidatorModel):
    IpamDiscoveredResourceCidrs: List[IpamDiscoveredResourceCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamResourceCidrsResultTypeDef(BaseValidatorModel):
    IpamResourceCidrs: List[IpamResourceCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamResourceCidrResultTypeDef(BaseValidatorModel):
    IpamResourceCidr: IpamResourceCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamResourceDiscoveryResultTypeDef(BaseValidatorModel):
    IpamResourceDiscovery: IpamResourceDiscoveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamResourceDiscoveryResultTypeDef(BaseValidatorModel):
    IpamResourceDiscovery: IpamResourceDiscoveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamResourceDiscoveriesResultTypeDef(BaseValidatorModel):
    IpamResourceDiscoveries: List[IpamResourceDiscoveryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamResourceDiscoveryResultTypeDef(BaseValidatorModel):
    IpamResourceDiscovery: IpamResourceDiscoveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamResultTypeDef(BaseValidatorModel):
    Ipam: IpamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamResultTypeDef(BaseValidatorModel):
    Ipam: IpamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamsResultTypeDef(BaseValidatorModel):
    Ipams: List[IpamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamResultTypeDef(BaseValidatorModel):
    Ipam: IpamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionIpamPoolCidrResultTypeDef(BaseValidatorModel):
    IpamPoolCidr: IpamPoolCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIpamPoolCidrsResultTypeDef(BaseValidatorModel):
    IpamPoolCidrs: List[IpamPoolCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ProvisionIpamPoolCidrResultTypeDef(BaseValidatorModel):
    IpamPoolCidr: IpamPoolCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamPoolResultTypeDef(BaseValidatorModel):
    IpamPool: IpamPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamPoolResultTypeDef(BaseValidatorModel):
    IpamPool: IpamPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamPoolsResultTypeDef(BaseValidatorModel):
    IpamPools: List[IpamPoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamPoolResultTypeDef(BaseValidatorModel):
    IpamPool: IpamPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IpamDiscoveredPublicAddressTypeDef(BaseValidatorModel):
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
    Tags: Optional[IpamPublicAddressTagsTypeDef] = None
    NetworkBorderGroup: Optional[str] = None
    SecurityGroups: Optional[List[IpamPublicAddressSecurityGroupTypeDef]] = None
    SampleTime: Optional[datetime] = None

class DescribeIpv6PoolsResultTypeDef(BaseValidatorModel):
    Ipv6Pools: List[Ipv6PoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef(BaseValidatorModel):
    AssociateCarrierIpAddress: Optional[bool] = None
    AssociatePublicIpAddress: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Description: Optional[str] = None
    DeviceIndex: Optional[int] = None
    Groups: Optional[List[str]] = None
    InterfaceType: Optional[str] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[List[InstanceIpv6AddressTypeDef]] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    SubnetId: Optional[str] = None
    NetworkCardIndex: Optional[int] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationResponseTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationResponseTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    PrimaryIpv6: Optional[bool] = None
    EnaSrdSpecification: Optional[LaunchTemplateEnaSrdSpecificationTypeDef] = None
    ConnectionTrackingSpecification: Optional[ConnectionTrackingSpecificationTypeDef] = None

class ModifyFpgaImageAttributeRequestRequestTypeDef(BaseValidatorModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None
    Attribute: Optional[FpgaImageAttributeNameType] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[Sequence[str]] = None
    UserGroups: Optional[Sequence[str]] = None
    ProductCodes: Optional[Sequence[str]] = None
    LoadPermission: Optional[LoadPermissionModificationsTypeDef] = None
    Description: Optional[str] = None
    Name: Optional[str] = None

class MediaAcceleratorInfoTypeDef(BaseValidatorModel):
    Accelerators: Optional[List[MediaDeviceInfoTypeDef]] = None
    TotalMediaMemoryInMiB: Optional[int] = None

class ReservedInstancesModificationTypeDef(BaseValidatorModel):
    ClientToken: Optional[str] = None
    CreateDate: Optional[datetime] = None
    EffectiveDate: Optional[datetime] = None
    ModificationResults: Optional[List[ReservedInstancesModificationResultTypeDef]] = None
    ReservedInstancesIds: Optional[List[ReservedInstancesIdTypeDef]] = None
    ReservedInstancesModificationId: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdateDate: Optional[datetime] = None

class CreateVerifiedAccessGroupResultTypeDef(BaseValidatorModel):
    VerifiedAccessGroup: VerifiedAccessGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessGroupResultTypeDef(BaseValidatorModel):
    VerifiedAccessGroup: VerifiedAccessGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessGroupsResultTypeDef(BaseValidatorModel):
    VerifiedAccessGroups: List[VerifiedAccessGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessGroupResultTypeDef(BaseValidatorModel):
    VerifiedAccessGroup: VerifiedAccessGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNatGatewayResultTypeDef(BaseValidatorModel):
    ClientToken: str
    NatGateway: NatGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNatGatewaysResultTypeDef(BaseValidatorModel):
    NatGateways: List[NatGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateNetworkInterfacePermissionResultTypeDef(BaseValidatorModel):
    InterfacePermission: NetworkInterfacePermissionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInterfacePermissionsResultTypeDef(BaseValidatorModel):
    NetworkInterfacePermissions: List[NetworkInterfacePermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NeuronInfoTypeDef(BaseValidatorModel):
    NeuronDevices: Optional[List[NeuronDeviceInfoTypeDef]] = None
    TotalNeuronDeviceMemoryInMiB: Optional[int] = None

class CreateVerifiedAccessTrustProviderResultTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessTrustProviderResultTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessTrustProvidersResultTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProviders: List[VerifiedAccessTrustProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessTrustProviderResultTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccessScopePathRequestTypeDef(BaseValidatorModel):
    Source: Optional[PathStatementRequestTypeDef] = None
    Destination: Optional[PathStatementRequestTypeDef] = None
    ThroughResources: Optional[Sequence[ThroughResourcesStatementRequestTypeDef]] = None

class AccessScopePathTypeDef(BaseValidatorModel):
    Source: Optional[PathStatementTypeDef] = None
    Destination: Optional[PathStatementTypeDef] = None
    ThroughResources: Optional[List[ThroughResourcesStatementTypeDef]] = None

class CancelReservedInstancesListingResultTypeDef(BaseValidatorModel):
    ReservedInstancesListings: List[ReservedInstancesListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReservedInstancesListingResultTypeDef(BaseValidatorModel):
    ReservedInstancesListings: List[ReservedInstancesListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReservedInstancesListingsResultTypeDef(BaseValidatorModel):
    ReservedInstancesListings: List[ReservedInstancesListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePublicIpv4PoolsResultTypeDef(BaseValidatorModel):
    PublicIpv4Pools: List[PublicIpv4PoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstancesOfferingsResultTypeDef(BaseValidatorModel):
    ReservedInstancesOfferings: List[ReservedInstancesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstancesResultTypeDef(BaseValidatorModel):
    ReservedInstances: List[ReservedInstancesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeSecurityGroupEgressResultTypeDef(BaseValidatorModel):
    Return: bool
    SecurityGroupRules: List[SecurityGroupRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    Return: bool
    SecurityGroupRules: List[SecurityGroupRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityGroupRulesResultTypeDef(BaseValidatorModel):
    SecurityGroupRules: List[SecurityGroupRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BundleTaskTypeDef(BaseValidatorModel):
    BundleId: Optional[str] = None
    BundleTaskError: Optional[BundleTaskErrorTypeDef] = None
    InstanceId: Optional[str] = None
    Progress: Optional[str] = None
    StartTime: Optional[datetime] = None
    State: Optional[BundleTaskStateType] = None
    Storage: Optional[StorageOutputTypeDef] = None
    UpdateTime: Optional[datetime] = None

class DescribeScheduledInstanceAvailabilityResultTypeDef(BaseValidatorModel):
    ScheduledInstanceAvailabilitySet: List[ScheduledInstanceAvailabilityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeScheduledInstancesResultTypeDef(BaseValidatorModel):
    ScheduledInstanceSet: List[ScheduledInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseScheduledInstancesResultTypeDef(BaseValidatorModel):
    ScheduledInstanceSet: List[ScheduledInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledInstancesLaunchSpecificationTypeDef(BaseValidatorModel):
    ImageId: str
    BlockDeviceMappings: Optional[Sequence[ScheduledInstancesBlockDeviceMappingTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[ScheduledInstancesIamInstanceProfileTypeDef] = None
    InstanceType: Optional[str] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[ScheduledInstancesMonitoringTypeDef] = None
    NetworkInterfaces: Optional[Sequence[ScheduledInstancesNetworkInterfaceTypeDef]] = None
    Placement: Optional[ScheduledInstancesPlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None

class CreateVpcEndpointResultTypeDef(BaseValidatorModel):
    VpcEndpoint: VpcEndpointTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointsResultTypeDef(BaseValidatorModel):
    VpcEndpoints: List[VpcEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifySecurityGroupRulesRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    SecurityGroupRules: Sequence[SecurityGroupRuleUpdateTypeDef]
    DryRun: Optional[bool] = None

class CreateVpcEndpointServiceConfigurationResultTypeDef(BaseValidatorModel):
    ServiceConfiguration: ServiceConfigurationTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointServiceConfigurationsResultTypeDef(BaseValidatorModel):
    ServiceConfigurations: List[ServiceConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVpcEndpointServicesResultTypeDef(BaseValidatorModel):
    ServiceNames: List[str]
    ServiceDetails: List[ServiceDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportImageResultTypeDef(BaseValidatorModel):
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
    SnapshotDetails: List[SnapshotDetailTypeDef]
    Status: str
    StatusMessage: str
    LicenseSpecifications: List[ImportImageLicenseConfigurationResponseTypeDef]
    Tags: List[TagTypeDef]
    UsageOperation: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportImageTaskTypeDef(BaseValidatorModel):
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
    SnapshotDetails: Optional[List[SnapshotDetailTypeDef]] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    LicenseSpecifications: Optional[List[ImportImageLicenseConfigurationResponseTypeDef]] = None
    UsageOperation: Optional[str] = None
    BootMode: Optional[BootModeValuesType] = None

class ImportSnapshotResultTypeDef(BaseValidatorModel):
    Description: str
    ImportTaskId: str
    SnapshotTaskDetail: SnapshotTaskDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSnapshotTaskTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    ImportTaskId: Optional[str] = None
    SnapshotTaskDetail: Optional[SnapshotTaskDetailTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateSpotDatafeedSubscriptionResultTypeDef(BaseValidatorModel):
    SpotDatafeedSubscription: SpotDatafeedSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpotDatafeedSubscriptionResultTypeDef(BaseValidatorModel):
    SpotDatafeedSubscription: SpotDatafeedSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayMulticastDomainAssociationsResultTypeDef(BaseValidatorModel):
    MulticastDomainAssociations: List[TransitGatewayMulticastDomainAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateTransitGatewayMulticastDomainResultTypeDef(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayMulticastDomainResultTypeDef(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RejectTransitGatewayMulticastDomainAssociationsResultTypeDef(BaseValidatorModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSubnetCidrBlockResultTypeDef(BaseValidatorModel):
    Ipv6CidrBlockAssociation: SubnetIpv6CidrBlockAssociationTypeDef
    SubnetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateSubnetCidrBlockResultTypeDef(BaseValidatorModel):
    Ipv6CidrBlockAssociation: SubnetIpv6CidrBlockAssociationTypeDef
    SubnetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetTypeDef(BaseValidatorModel):
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    AvailableIpAddressCount: Optional[int] = None
    CidrBlock: Optional[str] = None
    DefaultForAz: Optional[bool] = None
    EnableLniAtDeviceIndex: Optional[int] = None
    MapPublicIpOnLaunch: Optional[bool] = None
    MapCustomerOwnedIpOnLaunch: Optional[bool] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    State: Optional[SubnetStateType] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None
    AssignIpv6AddressOnCreation: Optional[bool] = None
    Ipv6CidrBlockAssociationSet: Optional[List[SubnetIpv6CidrBlockAssociationTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    SubnetArn: Optional[str] = None
    OutpostArn: Optional[str] = None
    EnableDns64: Optional[bool] = None
    Ipv6Native: Optional[bool] = None
    PrivateDnsNameOptionsOnLaunch: Optional[PrivateDnsNameOptionsOnLaunchTypeDef] = None

class GetReservedInstancesExchangeQuoteResultTypeDef(BaseValidatorModel):
    CurrencyCode: str
    IsValidExchange: bool
    OutputReservedInstancesWillExpireAt: datetime
    PaymentDue: str
    ReservedInstanceValueRollup: ReservationValueTypeDef
    ReservedInstanceValueSet: List[ReservedInstanceReservationValueTypeDef]
    TargetConfigurationValueRollup: ReservationValueTypeDef
    TargetConfigurationValueSet: List[TargetReservationValueTypeDef]
    ValidationFailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class LoadBalancersConfigExtraOutputTypeDef(BaseValidatorModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfigExtraOutputTypeDef] = None
    TargetGroupsConfig: Optional[TargetGroupsConfigExtraOutputTypeDef] = None

class LoadBalancersConfigOutputTypeDef(BaseValidatorModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfigOutputTypeDef] = None
    TargetGroupsConfig: Optional[TargetGroupsConfigOutputTypeDef] = None

class LoadBalancersConfigTypeDef(BaseValidatorModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfigTypeDef] = None
    TargetGroupsConfig: Optional[TargetGroupsConfigTypeDef] = None

class CreateTrafficMirrorFilterRuleResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRule: TrafficMirrorFilterRuleTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorFilterRulesResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRules: List[TrafficMirrorFilterRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTrafficMirrorFilterRuleResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilterRule: TrafficMirrorFilterRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TrafficMirrorFilterTypeDef(BaseValidatorModel):
    TrafficMirrorFilterId: Optional[str] = None
    IngressFilterRules: Optional[List[TrafficMirrorFilterRuleTypeDef]] = None
    EgressFilterRules: Optional[List[TrafficMirrorFilterRuleTypeDef]] = None
    NetworkServices: Optional[List[Literal["amazon-dns"]]] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeTransitGatewayAttachmentsResultTypeDef(BaseValidatorModel):
    TransitGatewayAttachments: List[TransitGatewayAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TransitGatewayConnectPeerTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayConnectPeerId: Optional[str] = None
    State: Optional[TransitGatewayConnectPeerStateType] = None
    CreationTime: Optional[datetime] = None
    ConnectPeerConfiguration: Optional[TransitGatewayConnectPeerConfigurationTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateTransitGatewayConnectResultTypeDef(BaseValidatorModel):
    TransitGatewayConnect: TransitGatewayConnectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayConnectResultTypeDef(BaseValidatorModel):
    TransitGatewayConnect: TransitGatewayConnectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayConnectsResultTypeDef(BaseValidatorModel):
    TransitGatewayConnects: List[TransitGatewayConnectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayMulticastDomainResultTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomain: TransitGatewayMulticastDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayMulticastDomainResultTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomain: TransitGatewayMulticastDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayMulticastDomainsResultTypeDef(BaseValidatorModel):
    TransitGatewayMulticastDomains: List[TransitGatewayMulticastDomainTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayResultTypeDef(BaseValidatorModel):
    TransitGateway: TransitGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayResultTypeDef(BaseValidatorModel):
    TransitGateway: TransitGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewaysResultTypeDef(BaseValidatorModel):
    TransitGateways: List[TransitGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTransitGatewayResultTypeDef(BaseValidatorModel):
    TransitGateway: TransitGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptTransitGatewayPeeringAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayPeeringAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayPeeringAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayPeeringAttachmentsResultTypeDef(BaseValidatorModel):
    TransitGatewayPeeringAttachments: List[TransitGatewayPeeringAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectTransitGatewayPeeringAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransitGatewayPolicyTableEntryTypeDef(BaseValidatorModel):
    PolicyRuleNumber: Optional[str] = None
    PolicyRule: Optional[TransitGatewayPolicyRuleTypeDef] = None
    TargetRouteTableId: Optional[str] = None

class CreateTransitGatewayPrefixListReferenceResultTypeDef(BaseValidatorModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayPrefixListReferenceResultTypeDef(BaseValidatorModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayPrefixListReferencesResultTypeDef(BaseValidatorModel):
    TransitGatewayPrefixListReferences: List[TransitGatewayPrefixListReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTransitGatewayPrefixListReferenceResultTypeDef(BaseValidatorModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayRouteResultTypeDef(BaseValidatorModel):
    Route: TransitGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayRouteResultTypeDef(BaseValidatorModel):
    Route: TransitGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceTransitGatewayRouteResultTypeDef(BaseValidatorModel):
    Route: TransitGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchTransitGatewayRoutesResultTypeDef(BaseValidatorModel):
    Routes: List[TransitGatewayRouteTypeDef]
    AdditionalRoutesAvailable: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptTransitGatewayVpcAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayVpcAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayVpcAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayVpcAttachmentsResultTypeDef(BaseValidatorModel):
    TransitGatewayVpcAttachments: List[TransitGatewayVpcAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTransitGatewayVpcAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RejectTransitGatewayVpcAttachmentResultTypeDef(BaseValidatorModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceCreditSpecificationResultTypeDef(BaseValidatorModel):
    SuccessfulInstanceCreditSpecifications: List[       SuccessfulInstanceCreditSpecificationItemTypeDef     ]
    UnsuccessfulInstanceCreditSpecifications: List[       UnsuccessfulInstanceCreditSpecificationItemTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptVpcEndpointConnectionsResultTypeDef(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowLogsResultTypeDef(BaseValidatorModel):
    ClientToken: str
    FlowLogIds: List[str]
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowLogsResultTypeDef(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointConnectionNotificationsResultTypeDef(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointServiceConfigurationsResultTypeDef(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointsResultTypeDef(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyHostsResultTypeDef(BaseValidatorModel):
    Successful: List[str]
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RejectVpcEndpointConnectionsResultTypeDef(BaseValidatorModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReleaseHostsResultTypeDef(BaseValidatorModel):
    Successful: List[str]
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLaunchTemplateResultTypeDef(BaseValidatorModel):
    LaunchTemplate: LaunchTemplateTypeDef
    Warning: ValidationWarningTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVerifiedAccessEndpointResultTypeDef(BaseValidatorModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessEndpointResultTypeDef(BaseValidatorModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessEndpointsResultTypeDef(BaseValidatorModel):
    VerifiedAccessEndpoints: List[VerifiedAccessEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessEndpointResultTypeDef(BaseValidatorModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttachVerifiedAccessTrustProviderResultTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVerifiedAccessInstanceResultTypeDef(BaseValidatorModel):
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessInstanceResultTypeDef(BaseValidatorModel):
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessInstancesResultTypeDef(BaseValidatorModel):
    VerifiedAccessInstances: List[VerifiedAccessInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetachVerifiedAccessTrustProviderResultTypeDef(BaseValidatorModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVerifiedAccessInstanceResultTypeDef(BaseValidatorModel):
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VerifiedAccessLogsTypeDef(BaseValidatorModel):
    S3: Optional[VerifiedAccessLogS3DestinationTypeDef] = None
    CloudWatchLogs: Optional[VerifiedAccessLogCloudWatchLogsDestinationTypeDef] = None
    KinesisDataFirehose: Optional[VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef] = None
    LogVersion: Optional[str] = None
    IncludeTrustContext: Optional[bool] = None

class ModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    AccessLogs: VerifiedAccessLogOptionsTypeDef
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class DescribeVolumesResultTypeDef(BaseValidatorModel):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class VolumeStatusItemTypeDef(BaseValidatorModel):
    Actions: Optional[List[VolumeStatusActionTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    OutpostArn: Optional[str] = None
    Events: Optional[List[VolumeStatusEventTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeStatus: Optional[VolumeStatusInfoTypeDef] = None
    AttachmentStatuses: Optional[List[VolumeStatusAttachmentStatusTypeDef]] = None

class AssociateVpcCidrBlockResultTypeDef(BaseValidatorModel):
    Ipv6CidrBlockAssociation: VpcIpv6CidrBlockAssociationTypeDef
    CidrBlockAssociation: VpcCidrBlockAssociationTypeDef
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateVpcCidrBlockResultTypeDef(BaseValidatorModel):
    Ipv6CidrBlockAssociation: VpcIpv6CidrBlockAssociationTypeDef
    CidrBlockAssociation: VpcCidrBlockAssociationTypeDef
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VpcTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    DhcpOptionsId: Optional[str] = None
    State: Optional[VpcStateType] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None
    InstanceTenancy: Optional[TenancyType] = None
    Ipv6CidrBlockAssociationSet: Optional[List[VpcIpv6CidrBlockAssociationTypeDef]] = None
    CidrBlockAssociationSet: Optional[List[VpcCidrBlockAssociationTypeDef]] = None
    IsDefault: Optional[bool] = None
    Tags: Optional[List[TagTypeDef]] = None

class VpcPeeringConnectionTypeDef(BaseValidatorModel):
    AccepterVpcInfo: Optional[VpcPeeringConnectionVpcInfoTypeDef] = None
    ExpirationTime: Optional[datetime] = None
    RequesterVpcInfo: Optional[VpcPeeringConnectionVpcInfoTypeDef] = None
    Status: Optional[VpcPeeringConnectionStateReasonTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcPeeringConnectionId: Optional[str] = None

class AssociateInstanceEventWindowResultTypeDef(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceEventWindowResultTypeDef(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceEventWindowsResultTypeDef(BaseValidatorModel):
    InstanceEventWindows: List[InstanceEventWindowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisassociateInstanceEventWindowResultTypeDef(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceEventWindowResultTypeDef(BaseValidatorModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptAddressTransferRequestRequestTypeDef(BaseValidatorModel):
    Address: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class AllocateAddressRequestRequestTypeDef(BaseValidatorModel):
    Domain: Optional[DomainTypeType] = None
    Address: Optional[str] = None
    PublicIpv4Pool: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class AllocateHostsRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZone: str
    AutoPlacement: Optional[AutoPlacementType] = None
    ClientToken: Optional[str] = None
    InstanceType: Optional[str] = None
    InstanceFamily: Optional[str] = None
    Quantity: Optional[int] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    HostRecovery: Optional[HostRecoveryType] = None
    OutpostArn: Optional[str] = None
    HostMaintenance: Optional[HostMaintenanceType] = None
    AssetIds: Optional[Sequence[str]] = None

class AssociateIpamResourceDiscoveryRequestRequestTypeDef(BaseValidatorModel):
    IpamId: str
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CopyImageRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    SourceImageId: str
    SourceRegion: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DestinationOutpostArn: Optional[str] = None
    DryRun: Optional[bool] = None
    CopyImageTags: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CopySnapshotRequestRequestTypeDef(BaseValidatorModel):
    SourceRegion: str
    SourceSnapshotId: str
    Description: Optional[str] = None
    DestinationOutpostArn: Optional[str] = None
    DestinationRegion: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PresignedUrl: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateCapacityReservationFleetRequestRequestTypeDef(BaseValidatorModel):
    InstanceTypeSpecifications: Sequence[ReservationFleetInstanceSpecificationTypeDef]
    TotalTargetCapacity: int
    AllocationStrategy: Optional[str] = None
    ClientToken: Optional[str] = None
    Tenancy: Optional[Literal["default"]] = None
    EndDate: Optional[TimestampTypeDef] = None
    InstanceMatchCriteria: Optional[Literal["open"]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateCapacityReservationRequestRequestTypeDef(BaseValidatorModel):
    InstanceType: str
    InstancePlatform: CapacityReservationInstancePlatformType
    InstanceCount: int
    ClientToken: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Tenancy: Optional[CapacityReservationTenancyType] = None
    EbsOptimized: Optional[bool] = None
    EphemeralStorage: Optional[bool] = None
    EndDate: Optional[TimestampTypeDef] = None
    EndDateType: Optional[EndDateTypeType] = None
    InstanceMatchCriteria: Optional[InstanceMatchCriteriaType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    OutpostArn: Optional[str] = None
    PlacementGroupArn: Optional[str] = None

class CreateCarrierGatewayRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class CreateClientVpnEndpointRequestRequestTypeDef(BaseValidatorModel):
    ClientCidrBlock: str
    ServerCertificateArn: str
    AuthenticationOptions: Sequence[ClientVpnAuthenticationRequestTypeDef]
    ConnectionLogOptions: ConnectionLogOptionsTypeDef
    DnsServers: Optional[Sequence[str]] = None
    TransportProtocol: Optional[TransportProtocolType] = None
    VpnPort: Optional[int] = None
    Description: Optional[str] = None
    SplitTunnel: Optional[bool] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    VpcId: Optional[str] = None
    SelfServicePortal: Optional[SelfServicePortalType] = None
    ClientConnectOptions: Optional[ClientConnectOptionsTypeDef] = None
    SessionTimeoutHours: Optional[int] = None
    ClientLoginBannerOptions: Optional[ClientLoginBannerOptionsTypeDef] = None

class CreateCoipPoolRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateCustomerGatewayRequestRequestTypeDef(BaseValidatorModel):
    Type: Literal["ipsec.1"]
    BgpAsn: Optional[int] = None
    PublicIp: Optional[str] = None
    CertificateArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DeviceName: Optional[str] = None
    IpAddress: Optional[str] = None
    DryRun: Optional[bool] = None
    BgpAsnExtended: Optional[int] = None

class CreateDhcpOptionsRequestRequestTypeDef(BaseValidatorModel):
    DhcpConfigurations: Sequence[NewDhcpConfigurationTypeDef]
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef(BaseValidatorModel):
    DhcpConfigurations: Sequence[NewDhcpConfigurationTypeDef]
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateEgressOnlyInternetGatewayRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateFlowLogsRequestRequestTypeDef(BaseValidatorModel):
    ResourceIds: Sequence[str]
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
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    MaxAggregationInterval: Optional[int] = None
    DestinationOptions: Optional[DestinationOptionsRequestTypeDef] = None

class CreateFpgaImageRequestRequestTypeDef(BaseValidatorModel):
    InputStorageLocation: StorageLocationTypeDef
    DryRun: Optional[bool] = None
    LogsStorageLocation: Optional[StorageLocationTypeDef] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateImageRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    NoReboot: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInstanceConnectEndpointRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    DryRun: Optional[bool] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    PreserveClientIp: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInstanceEventWindowRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Name: Optional[str] = None
    TimeRanges: Optional[Sequence[InstanceEventWindowTimeRangeRequestTypeDef]] = None
    CronExpression: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInstanceExportTaskRequestRequestTypeDef(BaseValidatorModel):
    ExportToS3Task: ExportToS3TaskSpecificationTypeDef
    InstanceId: str
    TargetEnvironment: ExportEnvironmentType
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInternetGatewayRequestRequestTypeDef(BaseValidatorModel):
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef(BaseValidatorModel):
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateIpamPoolRequestRequestTypeDef(BaseValidatorModel):
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
    AllocationResourceTags: Optional[Sequence[RequestIpamResourceTagTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    AwsService: Optional[Literal["ec2"]] = None
    PublicIpSource: Optional[IpamPoolPublicIpSourceType] = None
    SourceResource: Optional[IpamPoolSourceResourceRequestTypeDef] = None

class CreateIpamRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    Tier: Optional[IpamTierType] = None

class CreateIpamResourceDiscoveryRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateIpamScopeRequestRequestTypeDef(BaseValidatorModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateKeyPairRequestRequestTypeDef(BaseValidatorModel):
    KeyName: str
    DryRun: Optional[bool] = None
    KeyType: Optional[KeyTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    KeyFormat: Optional[KeyFormatType] = None

class CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef(BaseValidatorModel):
    KeyName: str
    DryRun: Optional[bool] = None
    KeyType: Optional[KeyTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    KeyFormat: Optional[KeyFormatType] = None

class CreateLocalGatewayRouteTableRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayId: str
    Mode: Optional[LocalGatewayRouteTableModeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    LocalGatewayVirtualInterfaceGroupId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef(BaseValidatorModel):
    LocalGatewayRouteTableId: str
    VpcId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateManagedPrefixListRequestRequestTypeDef(BaseValidatorModel):
    PrefixListName: str
    MaxEntries: int
    AddressFamily: str
    DryRun: Optional[bool] = None
    Entries: Optional[Sequence[AddPrefixListEntryTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNatGatewayRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    AllocationId: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ConnectivityType: Optional[ConnectivityTypeType] = None
    PrivateIpAddress: Optional[str] = None
    SecondaryAllocationIds: Optional[Sequence[str]] = None
    SecondaryPrivateIpAddresses: Optional[Sequence[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None

class CreateNetworkAclRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNetworkInsightsPathRequestRequestTypeDef(BaseValidatorModel):
    Source: str
    Protocol: ProtocolType
    ClientToken: str
    SourceIp: Optional[str] = None
    DestinationIp: Optional[str] = None
    Destination: Optional[str] = None
    DestinationPort: Optional[int] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    FilterAtSource: Optional[PathRequestFilterTypeDef] = None
    FilterAtDestination: Optional[PathRequestFilterTypeDef] = None

class CreateNetworkInterfaceRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressTypeDef]] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[Sequence[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[Ipv4PrefixSpecificationRequestTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[Sequence[Ipv6PrefixSpecificationRequestTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    InterfaceType: Optional[NetworkInterfaceCreationTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None

class CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef(BaseValidatorModel):
    SubnetId: str
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressTypeDef]] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[Sequence[PrivateIpAddressSpecificationTypeDef]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[Ipv4PrefixSpecificationRequestTypeDef]] = None
    Ipv4PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[Sequence[Ipv6PrefixSpecificationRequestTypeDef]] = None
    Ipv6PrefixCount: Optional[int] = None
    InterfaceType: Optional[NetworkInterfaceCreationTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None

class CreatePlacementGroupRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    GroupName: Optional[str] = None
    Strategy: Optional[PlacementStrategyType] = None
    PartitionCount: Optional[int] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    SpreadLevel: Optional[SpreadLevelType] = None

class CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    GroupName: Optional[str] = None
    Strategy: Optional[PlacementStrategyType] = None
    PartitionCount: Optional[int] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    SpreadLevel: Optional[SpreadLevelType] = None

class CreatePublicIpv4PoolRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    NetworkBorderGroup: Optional[str] = None

class CreateReplaceRootVolumeTaskRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SnapshotId: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ImageId: Optional[str] = None
    DeleteReplacedRootVolume: Optional[bool] = None

class CreateRestoreImageTaskRequestRequestTypeDef(BaseValidatorModel):
    Bucket: str
    ObjectKey: str
    Name: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateRouteTableRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateSecurityGroupRequestRequestTypeDef(BaseValidatorModel):
    Description: str
    GroupName: str
    VpcId: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef(BaseValidatorModel):
    Description: str
    GroupName: str
    VpcId: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotRequestRequestTypeDef(BaseValidatorModel):
    VolumeId: str
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef(BaseValidatorModel):
    VolumeId: str
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    InstanceSpecification: InstanceSpecificationTypeDef
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    CopyTagsFromSource: Optional[Literal["volume"]] = None

class CreateSubnetCidrReservationRequestRequestTypeDef(BaseValidatorModel):
    SubnetId: str
    Cidr: str
    ReservationType: SubnetCidrReservationTypeType
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateSubnetRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    OutpostArn: Optional[str] = None
    DryRun: Optional[bool] = None
    Ipv6Native: Optional[bool] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None

class CreateSubnetRequestServiceResourceCreateSubnetTypeDef(BaseValidatorModel):
    VpcId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    CidrBlock: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    OutpostArn: Optional[str] = None
    DryRun: Optional[bool] = None
    Ipv6Native: Optional[bool] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None

class CreateTrafficMirrorFilterRequestRequestTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class CreateTrafficMirrorFilterRuleRequestRequestTypeDef(BaseValidatorModel):
    TrafficMirrorFilterId: str
    TrafficDirection: TrafficDirectionType
    RuleNumber: int
    RuleAction: TrafficMirrorRuleActionType
    DestinationCidrBlock: str
    SourceCidrBlock: str
    DestinationPortRange: Optional[TrafficMirrorPortRangeRequestTypeDef] = None
    SourcePortRange: Optional[TrafficMirrorPortRangeRequestTypeDef] = None
    Protocol: Optional[int] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateTrafficMirrorSessionRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: str
    TrafficMirrorTargetId: str
    TrafficMirrorFilterId: str
    SessionNumber: int
    PacketLength: Optional[int] = None
    VirtualNetworkId: Optional[int] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class CreateTrafficMirrorTargetRequestRequestTypeDef(BaseValidatorModel):
    NetworkInterfaceId: Optional[str] = None
    NetworkLoadBalancerArn: Optional[str] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    GatewayLoadBalancerEndpointId: Optional[str] = None

class CreateTransitGatewayConnectPeerRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayAttachmentId: str
    PeerAddress: str
    InsideCidrBlocks: Sequence[str]
    TransitGatewayAddress: Optional[str] = None
    BgpOptions: Optional[TransitGatewayConnectRequestBgpOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayConnectRequestRequestTypeDef(BaseValidatorModel):
    TransportTransitGatewayAttachmentId: str
    Options: CreateTransitGatewayConnectRequestOptionsTypeDef
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayMulticastDomainRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayId: str
    Options: Optional[CreateTransitGatewayMulticastDomainRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayId: str
    PeerTransitGatewayId: str
    PeerAccountId: str
    PeerRegion: str
    Options: Optional[CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayPolicyTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayRequestRequestTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Options: Optional[TransitGatewayRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayRouteTableId: str
    PeeringAttachmentId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayRouteTableRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseValidatorModel):
    TransitGatewayId: str
    VpcId: str
    SubnetIds: Sequence[str]
    Options: Optional[CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateVerifiedAccessEndpointRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessGroupId: str
    EndpointType: VerifiedAccessEndpointTypeType
    AttachmentType: Literal["vpc"]
    DomainCertificateArn: str
    ApplicationDomain: str
    EndpointDomainPrefix: str
    SecurityGroupIds: Optional[Sequence[str]] = None
    LoadBalancerOptions: Optional[CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef] = None
    NetworkInterfaceOptions: Optional[CreateVerifiedAccessEndpointEniOptionsTypeDef] = None
    Description: Optional[str] = None
    PolicyDocument: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class CreateVerifiedAccessGroupRequestRequestTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: str
    Description: Optional[str] = None
    PolicyDocument: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class CreateVerifiedAccessInstanceRequestRequestTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    FIPSEnabled: Optional[bool] = None

class CreateVerifiedAccessTrustProviderRequestRequestTypeDef(BaseValidatorModel):
    TrustProviderType: TrustProviderTypeType
    PolicyReferenceName: str
    UserTrustProviderType: Optional[UserTrustProviderTypeType] = None
    DeviceTrustProviderType: Optional[DeviceTrustProviderTypeType] = None
    OidcOptions: Optional[CreateVerifiedAccessTrustProviderOidcOptionsTypeDef] = None
    DeviceOptions: Optional[CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class CreateVolumeRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZone: str
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    OutpostArn: Optional[str] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    MultiAttachEnabled: Optional[bool] = None
    Throughput: Optional[int] = None
    ClientToken: Optional[str] = None

class CreateVolumeRequestServiceResourceCreateVolumeTypeDef(BaseValidatorModel):
    AvailabilityZone: str
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    OutpostArn: Optional[str] = None
    Size: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeType: Optional[VolumeTypeType] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    MultiAttachEnabled: Optional[bool] = None
    Throughput: Optional[int] = None
    ClientToken: Optional[str] = None

class CreateVpcEndpointRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    ServiceName: str
    DryRun: Optional[bool] = None
    VpcEndpointType: Optional[VpcEndpointTypeType] = None
    PolicyDocument: Optional[str] = None
    RouteTableIds: Optional[Sequence[str]] = None
    SubnetIds: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    IpAddressType: Optional[IpAddressTypeType] = None
    DnsOptions: Optional[DnsOptionsSpecificationTypeDef] = None
    ClientToken: Optional[str] = None
    PrivateDnsEnabled: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    SubnetConfigurations: Optional[Sequence[SubnetConfigurationTypeDef]] = None

class CreateVpcEndpointServiceConfigurationRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    AcceptanceRequired: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    NetworkLoadBalancerArns: Optional[Sequence[str]] = None
    GatewayLoadBalancerArns: Optional[Sequence[str]] = None
    SupportedIpAddressTypes: Optional[Sequence[str]] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpcPeeringConnectionRequestRequestTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    PeerOwnerId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef(BaseValidatorModel):
    VpcId: str
    DryRun: Optional[bool] = None
    PeerOwnerId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpcRequestRequestTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    AmazonProvidedIpv6CidrBlock: Optional[bool] = None
    Ipv6Pool: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    DryRun: Optional[bool] = None
    InstanceTenancy: Optional[TenancyType] = None
    Ipv6CidrBlockNetworkBorderGroup: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpcRequestServiceResourceCreateVpcTypeDef(BaseValidatorModel):
    CidrBlock: Optional[str] = None
    AmazonProvidedIpv6CidrBlock: Optional[bool] = None
    Ipv6Pool: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv4IpamPoolId: Optional[str] = None
    Ipv4NetmaskLength: Optional[int] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None
    DryRun: Optional[bool] = None
    InstanceTenancy: Optional[TenancyType] = None
    Ipv6CidrBlockNetworkBorderGroup: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpnGatewayRequestRequestTypeDef(BaseValidatorModel):
    Type: Literal["ipsec.1"]
    AvailabilityZone: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    AmazonSideAsn: Optional[int] = None
    DryRun: Optional[bool] = None

class ExportImageRequestRequestTypeDef(BaseValidatorModel):
    DiskImageFormat: DiskImageFormatType
    ImageId: str
    S3ExportLocation: ExportTaskS3LocationRequestTypeDef
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    RoleName: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ImportImageRequestRequestTypeDef(BaseValidatorModel):
    Architecture: Optional[str] = None
    ClientData: Optional[ClientDataTypeDef] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DiskContainers: Optional[Sequence[ImageDiskContainerTypeDef]] = None
    DryRun: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Hypervisor: Optional[str] = None
    KmsKeyId: Optional[str] = None
    LicenseType: Optional[str] = None
    Platform: Optional[str] = None
    RoleName: Optional[str] = None
    LicenseSpecifications: Optional[       Sequence[ImportImageLicenseConfigurationRequestTypeDef]     ] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    UsageOperation: Optional[str] = None
    BootMode: Optional[BootModeValuesType] = None

class ImportKeyPairRequestRequestTypeDef(BaseValidatorModel):
    KeyName: str
    PublicKeyMaterial: BlobTypeDef
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ImportKeyPairRequestServiceResourceImportKeyPairTypeDef(BaseValidatorModel):
    KeyName: str
    PublicKeyMaterial: BlobTypeDef
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ImportSnapshotRequestRequestTypeDef(BaseValidatorModel):
    ClientData: Optional[ClientDataTypeDef] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DiskContainer: Optional[SnapshotDiskContainerTypeDef] = None
    DryRun: Optional[bool] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    RoleName: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ProvisionByoipCidrRequestRequestTypeDef(BaseValidatorModel):
    Cidr: str
    CidrAuthorizationContext: Optional[CidrAuthorizationContextTypeDef] = None
    PubliclyAdvertisable: Optional[bool] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    PoolTagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    MultiRegion: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class PurchaseCapacityBlockRequestRequestTypeDef(BaseValidatorModel):
    CapacityBlockOfferingId: str
    InstancePlatform: CapacityReservationInstancePlatformType
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class PurchaseHostReservationRequestRequestTypeDef(BaseValidatorModel):
    HostIdSet: Sequence[str]
    OfferingId: str
    ClientToken: Optional[str] = None
    CurrencyCode: Optional[Literal["USD"]] = None
    LimitPrice: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class RegisterImageRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ImageLocation: Optional[str] = None
    Architecture: Optional[ArchitectureValuesType] = None
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EnaSupport: Optional[bool] = None
    KernelId: Optional[str] = None
    BillingProducts: Optional[Sequence[str]] = None
    RamdiskId: Optional[str] = None
    RootDeviceName: Optional[str] = None
    SriovNetSupport: Optional[str] = None
    VirtualizationType: Optional[str] = None
    BootMode: Optional[BootModeValuesType] = None
    TpmSupport: Optional[Literal["v2.0"]] = None
    UefiData: Optional[str] = None
    ImdsSupport: Optional[Literal["v2.0"]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class RegisterImageRequestServiceResourceRegisterImageTypeDef(BaseValidatorModel):
    Name: str
    ImageLocation: Optional[str] = None
    Architecture: Optional[ArchitectureValuesType] = None
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EnaSupport: Optional[bool] = None
    KernelId: Optional[str] = None
    BillingProducts: Optional[Sequence[str]] = None
    RamdiskId: Optional[str] = None
    RootDeviceName: Optional[str] = None
    SriovNetSupport: Optional[str] = None
    VirtualizationType: Optional[str] = None
    BootMode: Optional[BootModeValuesType] = None
    TpmSupport: Optional[Literal["v2.0"]] = None
    UefiData: Optional[str] = None
    ImdsSupport: Optional[Literal["v2.0"]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeId: str
    ClientToken: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class StartNetworkInsightsAnalysisRequestRequestTypeDef(BaseValidatorModel):
    NetworkInsightsPathId: str
    ClientToken: str
    AdditionalAccounts: Optional[Sequence[str]] = None
    FilterInArns: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class PathComponentTypeDef(BaseValidatorModel):
    SequenceNumber: Optional[int] = None
    AclRule: Optional[AnalysisAclRuleTypeDef] = None
    AttachedTo: Optional[AnalysisComponentTypeDef] = None
    Component: Optional[AnalysisComponentTypeDef] = None
    DestinationVpc: Optional[AnalysisComponentTypeDef] = None
    OutboundHeader: Optional[AnalysisPacketHeaderTypeDef] = None
    InboundHeader: Optional[AnalysisPacketHeaderTypeDef] = None
    RouteTableRoute: Optional[AnalysisRouteTableRouteTypeDef] = None
    SecurityGroupRule: Optional[AnalysisSecurityGroupRuleTypeDef] = None
    SourceVpc: Optional[AnalysisComponentTypeDef] = None
    Subnet: Optional[AnalysisComponentTypeDef] = None
    Vpc: Optional[AnalysisComponentTypeDef] = None
    AdditionalDetails: Optional[List[AdditionalDetailTypeDef]] = None
    TransitGateway: Optional[AnalysisComponentTypeDef] = None
    TransitGatewayRouteTableRoute: Optional[TransitGatewayRouteTableRouteTypeDef] = None
    Explanations: Optional[List[ExplanationTypeDef]] = None
    ElasticLoadBalancerListener: Optional[AnalysisComponentTypeDef] = None
    FirewallStatelessRule: Optional[FirewallStatelessRuleTypeDef] = None
    FirewallStatefulRule: Optional[FirewallStatefulRuleTypeDef] = None
    ServiceName: Optional[str] = None

class CreateRouteTableResultTypeDef(BaseValidatorModel):
    RouteTable: RouteTableTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRouteTablesResultTypeDef(BaseValidatorModel):
    RouteTables: List[RouteTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetFlowLogsIntegrationTemplateRequestRequestTypeDef(BaseValidatorModel):
    FlowLogId: str
    ConfigDeliveryS3DestinationArn: str
    IntegrateServices: IntegrateServicesTypeDef
    DryRun: Optional[bool] = None

class DescribeNetworkInterfaceAttributeResultTypeDef(BaseValidatorModel):
    Attachment: NetworkInterfaceAttachmentTypeDef
    Description: AttributeValueTypeDef
    Groups: List[GroupIdentifierTypeDef]
    NetworkInterfaceId: str
    SourceDestCheck: AttributeBooleanValueTypeDef
    AssociatePublicIpAddress: bool
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInterfaceTypeDef(BaseValidatorModel):
    Association: Optional[NetworkInterfaceAssociationTypeDef] = None
    Attachment: Optional[NetworkInterfaceAttachmentTypeDef] = None
    AvailabilityZone: Optional[str] = None
    ConnectionTrackingConfiguration: Optional[ConnectionTrackingConfigurationTypeDef] = None
    Description: Optional[str] = None
    Groups: Optional[List[GroupIdentifierTypeDef]] = None
    InterfaceType: Optional[NetworkInterfaceTypeType] = None
    Ipv6Addresses: Optional[List[NetworkInterfaceIpv6AddressTypeDef]] = None
    MacAddress: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[NetworkInterfacePrivateIpAddressTypeDef]] = None
    Ipv4Prefixes: Optional[List[Ipv4PrefixSpecificationTypeDef]] = None
    Ipv6Prefixes: Optional[List[Ipv6PrefixSpecificationTypeDef]] = None
    RequesterId: Optional[str] = None
    RequesterManaged: Optional[bool] = None
    SourceDestCheck: Optional[bool] = None
    Status: Optional[NetworkInterfaceStatusType] = None
    SubnetId: Optional[str] = None
    TagSet: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None
    DenyAllIgwTraffic: Optional[bool] = None
    Ipv6Native: Optional[bool] = None
    Ipv6Address: Optional[str] = None

class CreateDhcpOptionsResultTypeDef(BaseValidatorModel):
    DhcpOptions: DhcpOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDhcpOptionsResultTypeDef(BaseValidatorModel):
    DhcpOptions: List[DhcpOptionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHostsResultTypeDef(BaseValidatorModel):
    Hosts: List[HostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BundleInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Storage: StorageTypeDef
    DryRun: Optional[bool] = None

class DescribeImagesResultTypeDef(BaseValidatorModel):
    Images: List[ImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeClientVpnEndpointsResultTypeDef(BaseValidatorModel):
    ClientVpnEndpoints: List[ClientVpnEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVpnTunnelOptionsRequestRequestTypeDef(BaseValidatorModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    TunnelOptions: ModifyVpnTunnelOptionsSpecificationTypeDef
    DryRun: Optional[bool] = None
    SkipTunnelReplacement: Optional[bool] = None

class VpnConnectionOptionsSpecificationTypeDef(BaseValidatorModel):
    EnableAcceleration: Optional[bool] = None
    StaticRoutesOnly: Optional[bool] = None
    TunnelInsideIpVersion: Optional[TunnelInsideIpVersionType] = None
    TunnelOptions: Optional[Sequence[VpnTunnelOptionsSpecificationTypeDef]] = None
    LocalIpv4NetworkCidr: Optional[str] = None
    RemoteIpv4NetworkCidr: Optional[str] = None
    LocalIpv6NetworkCidr: Optional[str] = None
    RemoteIpv6NetworkCidr: Optional[str] = None
    OutsideIpAddressType: Optional[str] = None
    TransportTransitGatewayAttachmentId: Optional[str] = None

class VpnConnectionOptionsTypeDef(BaseValidatorModel):
    EnableAcceleration: Optional[bool] = None
    StaticRoutesOnly: Optional[bool] = None
    LocalIpv4NetworkCidr: Optional[str] = None
    RemoteIpv4NetworkCidr: Optional[str] = None
    LocalIpv6NetworkCidr: Optional[str] = None
    RemoteIpv6NetworkCidr: Optional[str] = None
    OutsideIpAddressType: Optional[str] = None
    TransportTransitGatewayAttachmentId: Optional[str] = None
    TunnelInsideIpVersion: Optional[TunnelInsideIpVersionType] = None
    TunnelOptions: Optional[List[TunnelOptionTypeDef]] = None

class CreateNetworkAclResultTypeDef(BaseValidatorModel):
    NetworkAcl: NetworkAclTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkAclsResultTypeDef(BaseValidatorModel):
    NetworkAcls: List[NetworkAclTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisableFastSnapshotRestoresResultTypeDef(BaseValidatorModel):
    Successful: List[DisableFastSnapshotRestoreSuccessItemTypeDef]
    Unsuccessful: List[DisableFastSnapshotRestoreErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConversionTaskTypeDef(BaseValidatorModel):
    ConversionTaskId: Optional[str] = None
    ExpirationTime: Optional[str] = None
    ImportInstance: Optional[ImportInstanceTaskDetailsTypeDef] = None
    ImportVolume: Optional[ImportVolumeTaskDetailsTypeDef] = None
    State: Optional[ConversionTaskStateType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class SpotFleetLaunchSpecificationExtraOutputTypeDef(BaseValidatorModel):
    SecurityGroups: Optional[List[GroupIdentifierTypeDef]] = None
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMappingTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[SpotFleetMonitoringTypeDef] = None
    NetworkInterfaces: Optional[       List[InstanceNetworkInterfaceSpecificationExtraOutputTypeDef]     ] = None
    Placement: Optional[SpotPlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    TagSpecifications: Optional[List[SpotFleetTagSpecificationExtraOutputTypeDef]] = None
    InstanceRequirements: Optional[InstanceRequirementsExtraOutputTypeDef] = None

class LaunchSpecificationTypeDef(BaseValidatorModel):
    UserData: Optional[str] = None
    SecurityGroups: Optional[List[GroupIdentifierTypeDef]] = None
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMappingTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationOutputTypeDef]] = None
    Placement: Optional[SpotPlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SubnetId: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabledTypeDef] = None

class SpotFleetLaunchSpecificationOutputTypeDef(BaseValidatorModel):
    SecurityGroups: Optional[List[GroupIdentifierTypeDef]] = None
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[List[BlockDeviceMappingTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[SpotFleetMonitoringTypeDef] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceSpecificationOutputTypeDef]] = None
    Placement: Optional[SpotPlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    TagSpecifications: Optional[List[SpotFleetTagSpecificationOutputTypeDef]] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None

class RequestSpotLaunchSpecificationTypeDef(BaseValidatorModel):
    SecurityGroupIds: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabledTypeDef] = None
    NetworkInterfaces: Optional[Sequence[InstanceNetworkInterfaceSpecificationTypeDef]] = None
    Placement: Optional[SpotPlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None

class RunInstancesRequestSubnetCreateInstancesTypeDef(BaseValidatorModel):
    MaxCount: int
    MinCount: int
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressTypeDef]] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabledTypeDef] = None
    Placement: Optional[PlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    UserData: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    ClientToken: Optional[str] = None
    DisableApiTermination: Optional[bool] = None
    DryRun: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    NetworkInterfaces: Optional[Sequence[InstanceNetworkInterfaceSpecificationTypeDef]] = None
    PrivateIpAddress: Optional[str] = None
    ElasticGpuSpecification: Optional[Sequence[ElasticGpuSpecificationTypeDef]] = None
    ElasticInferenceAccelerators: Optional[Sequence[ElasticInferenceAcceleratorTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceMarketOptions: Optional[InstanceMarketOptionsRequestTypeDef] = None
    CreditSpecification: Optional[CreditSpecificationRequestTypeDef] = None
    CpuOptions: Optional[CpuOptionsRequestTypeDef] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationTypeDef] = None
    HibernationOptions: Optional[HibernationOptionsRequestTypeDef] = None
    LicenseSpecifications: Optional[Sequence[LicenseConfigurationRequestTypeDef]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsRequestTypeDef] = None
    EnclaveOptions: Optional[EnclaveOptionsRequestTypeDef] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsRequestTypeDef] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptionsRequestTypeDef] = None
    DisableApiStop: Optional[bool] = None
    EnablePrimaryIpv6: Optional[bool] = None

class SpotFleetLaunchSpecificationTypeDef(BaseValidatorModel):
    SecurityGroups: Optional[Sequence[GroupIdentifierTypeDef]] = None
    AddressingType: Optional[str] = None
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[SpotFleetMonitoringTypeDef] = None
    NetworkInterfaces: Optional[Sequence[InstanceNetworkInterfaceSpecificationTypeDef]] = None
    Placement: Optional[SpotPlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    TagSpecifications: Optional[Sequence[SpotFleetTagSpecificationTypeDef]] = None
    InstanceRequirements: Optional[InstanceRequirementsTypeDef] = None

class RequestLaunchTemplateDataTypeDef(BaseValidatorModel):
    KernelId: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[       LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef     ] = None
    BlockDeviceMappings: Optional[       Sequence[LaunchTemplateBlockDeviceMappingRequestTypeDef]     ] = None
    NetworkInterfaces: Optional[       Sequence[LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef]     ] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[LaunchTemplatesMonitoringRequestTypeDef] = None
    Placement: Optional[LaunchTemplatePlacementRequestTypeDef] = None
    RamDiskId: Optional[str] = None
    DisableApiTermination: Optional[bool] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    UserData: Optional[str] = None
    TagSpecifications: Optional[Sequence[LaunchTemplateTagSpecificationRequestTypeDef]] = None
    ElasticGpuSpecifications: Optional[Sequence[ElasticGpuSpecificationTypeDef]] = None
    ElasticInferenceAccelerators: Optional[       Sequence[LaunchTemplateElasticInferenceAcceleratorTypeDef]     ] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    InstanceMarketOptions: Optional[LaunchTemplateInstanceMarketOptionsRequestTypeDef] = None
    CreditSpecification: Optional[CreditSpecificationRequestTypeDef] = None
    CpuOptions: Optional[LaunchTemplateCpuOptionsRequestTypeDef] = None
    CapacityReservationSpecification: Optional[       LaunchTemplateCapacityReservationSpecificationRequestTypeDef     ] = None
    LicenseSpecifications: Optional[       Sequence[LaunchTemplateLicenseConfigurationRequestTypeDef]     ] = None
    HibernationOptions: Optional[LaunchTemplateHibernationOptionsRequestTypeDef] = None
    MetadataOptions: Optional[LaunchTemplateInstanceMetadataOptionsRequestTypeDef] = None
    EnclaveOptions: Optional[LaunchTemplateEnclaveOptionsRequestTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsRequestTypeDef] = None
    PrivateDnsNameOptions: Optional[LaunchTemplatePrivateDnsNameOptionsRequestTypeDef] = None
    MaintenanceOptions: Optional[LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef] = None
    DisableApiStop: Optional[bool] = None

class EnableFastSnapshotRestoresResultTypeDef(BaseValidatorModel):
    Successful: List[EnableFastSnapshotRestoreSuccessItemTypeDef]
    Unsuccessful: List[EnableFastSnapshotRestoreErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkInsightsPathResultTypeDef(BaseValidatorModel):
    NetworkInsightsPath: NetworkInsightsPathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInsightsPathsResultTypeDef(BaseValidatorModel):
    NetworkInsightsPaths: List[NetworkInsightsPathTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceNetworkInterfaceTypeDef(BaseValidatorModel):
    Association: Optional[InstanceNetworkInterfaceAssociationTypeDef] = None
    Attachment: Optional[InstanceNetworkInterfaceAttachmentTypeDef] = None
    Description: Optional[str] = None
    Groups: Optional[List[GroupIdentifierTypeDef]] = None
    Ipv6Addresses: Optional[List[InstanceIpv6AddressTypeDef]] = None
    MacAddress: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    OwnerId: Optional[str] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    PrivateIpAddresses: Optional[List[InstancePrivateIpAddressTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    Status: Optional[NetworkInterfaceStatusType] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    InterfaceType: Optional[str] = None
    Ipv4Prefixes: Optional[List[InstanceIpv4PrefixTypeDef]] = None
    Ipv6Prefixes: Optional[List[InstanceIpv6PrefixTypeDef]] = None
    ConnectionTrackingConfiguration: Optional[       ConnectionTrackingSpecificationResponseTypeDef     ] = None

class LaunchTemplateConfigExtraOutputTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[LaunchTemplateOverridesExtraOutputTypeDef]] = None

class FleetLaunchTemplateConfigTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[FleetLaunchTemplateOverridesTypeDef]] = None

class LaunchTemplateAndOverridesResponseTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[FleetLaunchTemplateOverridesTypeDef] = None

class LaunchTemplateConfigOutputTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[LaunchTemplateOverridesOutputTypeDef]] = None

class LaunchTemplateConfigTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[Sequence[LaunchTemplateOverridesTypeDef]] = None

class FleetLaunchTemplateConfigRequestTypeDef(BaseValidatorModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationRequestTypeDef] = None
    Overrides: Optional[Sequence[FleetLaunchTemplateOverridesRequestTypeDef]] = None

class GetSpotPlacementScoresRequestGetSpotPlacementScoresPaginateTypeDef(BaseValidatorModel):
    TargetCapacity: int
    InstanceTypes: Optional[Sequence[str]] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    SingleAvailabilityZone: Optional[bool] = None
    RegionNames: Optional[Sequence[str]] = None
    InstanceRequirementsWithMetadata: Optional[       InstanceRequirementsWithMetadataRequestTypeDef     ] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSpotPlacementScoresRequestRequestTypeDef(BaseValidatorModel):
    TargetCapacity: int
    InstanceTypes: Optional[Sequence[str]] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    SingleAvailabilityZone: Optional[bool] = None
    RegionNames: Optional[Sequence[str]] = None
    InstanceRequirementsWithMetadata: Optional[       InstanceRequirementsWithMetadataRequestTypeDef     ] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceStatusResultTypeDef(BaseValidatorModel):
    InstanceStatuses: List[InstanceStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSecurityGroupsResultTypeDef(BaseValidatorModel):
    SecurityGroups: List[SecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AuthorizeSecurityGroupEgressRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    DryRun: Optional[bool] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    ToPort: Optional[int] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None

class AuthorizeSecurityGroupIngressRequestRequestTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class RevokeSecurityGroupEgressRequestRequestTypeDef(BaseValidatorModel):
    GroupId: str
    DryRun: Optional[bool] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    ToPort: Optional[int] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None

class RevokeSecurityGroupIngressRequestRequestTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    IpProtocol: Optional[str] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None
    ToPort: Optional[int] = None
    DryRun: Optional[bool] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None

class UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    SecurityGroupRuleDescriptions: Optional[Sequence[SecurityGroupRuleDescriptionTypeDef]] = None

class UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef(BaseValidatorModel):
    DryRun: Optional[bool] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    SecurityGroupRuleDescriptions: Optional[Sequence[SecurityGroupRuleDescriptionTypeDef]] = None

class DescribeStaleSecurityGroupsResultTypeDef(BaseValidatorModel):
    StaleSecurityGroupSet: List[StaleSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamDiscoveredPublicAddressesResultTypeDef(BaseValidatorModel):
    IpamDiscoveredPublicAddresses: List[IpamDiscoveredPublicAddressTypeDef]
    OldestSampleTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResponseLaunchTemplateDataTypeDef(BaseValidatorModel):
    KernelId: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[LaunchTemplateIamInstanceProfileSpecificationTypeDef] = None
    BlockDeviceMappings: Optional[List[LaunchTemplateBlockDeviceMappingTypeDef]] = None
    NetworkInterfaces: Optional[       List[LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef]     ] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[LaunchTemplatesMonitoringTypeDef] = None
    Placement: Optional[LaunchTemplatePlacementTypeDef] = None
    RamDiskId: Optional[str] = None
    DisableApiTermination: Optional[bool] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    UserData: Optional[str] = None
    TagSpecifications: Optional[List[LaunchTemplateTagSpecificationTypeDef]] = None
    ElasticGpuSpecifications: Optional[List[ElasticGpuSpecificationResponseTypeDef]] = None
    ElasticInferenceAccelerators: Optional[       List[LaunchTemplateElasticInferenceAcceleratorResponseTypeDef]     ] = None
    SecurityGroupIds: Optional[List[str]] = None
    SecurityGroups: Optional[List[str]] = None
    InstanceMarketOptions: Optional[LaunchTemplateInstanceMarketOptionsTypeDef] = None
    CreditSpecification: Optional[CreditSpecificationTypeDef] = None
    CpuOptions: Optional[LaunchTemplateCpuOptionsTypeDef] = None
    CapacityReservationSpecification: Optional[       LaunchTemplateCapacityReservationSpecificationResponseTypeDef     ] = None
    LicenseSpecifications: Optional[List[LaunchTemplateLicenseConfigurationTypeDef]] = None
    HibernationOptions: Optional[LaunchTemplateHibernationOptionsTypeDef] = None
    MetadataOptions: Optional[LaunchTemplateInstanceMetadataOptionsTypeDef] = None
    EnclaveOptions: Optional[LaunchTemplateEnclaveOptionsTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None
    PrivateDnsNameOptions: Optional[LaunchTemplatePrivateDnsNameOptionsTypeDef] = None
    MaintenanceOptions: Optional[LaunchTemplateInstanceMaintenanceOptionsTypeDef] = None
    DisableApiStop: Optional[bool] = None

class DescribeReservedInstancesModificationsResultTypeDef(BaseValidatorModel):
    ReservedInstancesModifications: List[ReservedInstancesModificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceTypeInfoTypeDef(BaseValidatorModel):
    InstanceType: Optional[InstanceTypeType] = None
    CurrentGeneration: Optional[bool] = None
    FreeTierEligible: Optional[bool] = None
    SupportedUsageClasses: Optional[List[UsageClassTypeType]] = None
    SupportedRootDeviceTypes: Optional[List[RootDeviceTypeType]] = None
    SupportedVirtualizationTypes: Optional[List[VirtualizationTypeType]] = None
    BareMetal: Optional[bool] = None
    Hypervisor: Optional[InstanceTypeHypervisorType] = None
    ProcessorInfo: Optional[ProcessorInfoTypeDef] = None
    VCpuInfo: Optional[VCpuInfoTypeDef] = None
    MemoryInfo: Optional[MemoryInfoTypeDef] = None
    InstanceStorageSupported: Optional[bool] = None
    InstanceStorageInfo: Optional[InstanceStorageInfoTypeDef] = None
    EbsInfo: Optional[EbsInfoTypeDef] = None
    NetworkInfo: Optional[NetworkInfoTypeDef] = None
    GpuInfo: Optional[GpuInfoTypeDef] = None
    FpgaInfo: Optional[FpgaInfoTypeDef] = None
    PlacementGroupInfo: Optional[PlacementGroupInfoTypeDef] = None
    InferenceAcceleratorInfo: Optional[InferenceAcceleratorInfoTypeDef] = None
    HibernationSupported: Optional[bool] = None
    BurstablePerformanceSupported: Optional[bool] = None
    DedicatedHostsSupported: Optional[bool] = None
    AutoRecoverySupported: Optional[bool] = None
    SupportedBootModes: Optional[List[BootModeTypeType]] = None
    NitroEnclavesSupport: Optional[NitroEnclavesSupportType] = None
    NitroTpmSupport: Optional[NitroTpmSupportType] = None
    NitroTpmInfo: Optional[NitroTpmInfoTypeDef] = None
    MediaAcceleratorInfo: Optional[MediaAcceleratorInfoTypeDef] = None
    NeuronInfo: Optional[NeuronInfoTypeDef] = None
    PhcSupport: Optional[PhcSupportType] = None

class CreateNetworkInsightsAccessScopeRequestRequestTypeDef(BaseValidatorModel):
    ClientToken: str
    MatchPaths: Optional[Sequence[AccessScopePathRequestTypeDef]] = None
    ExcludePaths: Optional[Sequence[AccessScopePathRequestTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class NetworkInsightsAccessScopeContentTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeId: Optional[str] = None
    MatchPaths: Optional[List[AccessScopePathTypeDef]] = None
    ExcludePaths: Optional[List[AccessScopePathTypeDef]] = None

class BundleInstanceResultTypeDef(BaseValidatorModel):
    BundleTask: BundleTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelBundleTaskResultTypeDef(BaseValidatorModel):
    BundleTask: BundleTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBundleTasksResultTypeDef(BaseValidatorModel):
    BundleTasks: List[BundleTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RunScheduledInstancesRequestRequestTypeDef(BaseValidatorModel):
    LaunchSpecification: ScheduledInstancesLaunchSpecificationTypeDef
    ScheduledInstanceId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    InstanceCount: Optional[int] = None

class DescribeImportImageTasksResultTypeDef(BaseValidatorModel):
    ImportImageTasks: List[ImportImageTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeImportSnapshotTasksResultTypeDef(BaseValidatorModel):
    ImportSnapshotTasks: List[ImportSnapshotTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDefaultSubnetResultTypeDef(BaseValidatorModel):
    Subnet: SubnetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubnetResultTypeDef(BaseValidatorModel):
    Subnet: SubnetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubnetsResultTypeDef(BaseValidatorModel):
    Subnets: List[SubnetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTrafficMirrorFilterResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilter: TrafficMirrorFilterTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorFiltersResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilters: List[TrafficMirrorFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTrafficMirrorFilterNetworkServicesResultTypeDef(BaseValidatorModel):
    TrafficMirrorFilter: TrafficMirrorFilterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayConnectPeerResultTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeer: TransitGatewayConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayConnectPeerResultTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeer: TransitGatewayConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayConnectPeersResultTypeDef(BaseValidatorModel):
    TransitGatewayConnectPeers: List[TransitGatewayConnectPeerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayPolicyTableEntriesResultTypeDef(BaseValidatorModel):
    TransitGatewayPolicyTableEntries: List[TransitGatewayPolicyTableEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VerifiedAccessInstanceLoggingConfigurationTypeDef(BaseValidatorModel):
    VerifiedAccessInstanceId: Optional[str] = None
    AccessLogs: Optional[VerifiedAccessLogsTypeDef] = None

class DescribeVolumeStatusResultTypeDef(BaseValidatorModel):
    VolumeStatuses: List[VolumeStatusItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDefaultVpcResultTypeDef(BaseValidatorModel):
    Vpc: VpcTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcResultTypeDef(BaseValidatorModel):
    Vpc: VpcTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcsResultTypeDef(BaseValidatorModel):
    Vpcs: List[VpcTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AcceptVpcPeeringConnectionResultTypeDef(BaseValidatorModel):
    VpcPeeringConnection: VpcPeeringConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcPeeringConnectionResultTypeDef(BaseValidatorModel):
    VpcPeeringConnection: VpcPeeringConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcPeeringConnectionsResultTypeDef(BaseValidatorModel):
    VpcPeeringConnections: List[VpcPeeringConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AccessScopeAnalysisFindingTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: Optional[str] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    FindingId: Optional[str] = None
    FindingComponents: Optional[List[PathComponentTypeDef]] = None

class NetworkInsightsAnalysisTypeDef(BaseValidatorModel):
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
    ForwardPathComponents: Optional[List[PathComponentTypeDef]] = None
    ReturnPathComponents: Optional[List[PathComponentTypeDef]] = None
    Explanations: Optional[List[ExplanationTypeDef]] = None
    AlternatePathHints: Optional[List[AlternatePathHintTypeDef]] = None
    SuggestedAccounts: Optional[List[str]] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateNetworkInterfaceResultTypeDef(BaseValidatorModel):
    NetworkInterface: NetworkInterfaceTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInterfacesResultTypeDef(BaseValidatorModel):
    NetworkInterfaces: List[NetworkInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateVpnConnectionRequestRequestTypeDef(BaseValidatorModel):
    CustomerGatewayId: str
    Type: str
    VpnGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    DryRun: Optional[bool] = None
    Options: Optional[VpnConnectionOptionsSpecificationTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class VpnConnectionTypeDef(BaseValidatorModel):
    CustomerGatewayConfiguration: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    Category: Optional[str] = None
    State: Optional[VpnStateType] = None
    Type: Optional[Literal["ipsec.1"]] = None
    VpnConnectionId: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    CoreNetworkArn: Optional[str] = None
    CoreNetworkAttachmentArn: Optional[str] = None
    GatewayAssociationState: Optional[GatewayAssociationStateType] = None
    Options: Optional[VpnConnectionOptionsTypeDef] = None
    Routes: Optional[List[VpnStaticRouteTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    VgwTelemetry: Optional[List[VgwTelemetryTypeDef]] = None

class DescribeConversionTasksResultTypeDef(BaseValidatorModel):
    ConversionTasks: List[ConversionTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportInstanceResultTypeDef(BaseValidatorModel):
    ConversionTask: ConversionTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportVolumeResultTypeDef(BaseValidatorModel):
    ConversionTask: ConversionTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SpotInstanceRequestTypeDef(BaseValidatorModel):
    ActualBlockHourlyPrice: Optional[str] = None
    AvailabilityZoneGroup: Optional[str] = None
    BlockDurationMinutes: Optional[int] = None
    CreateTime: Optional[datetime] = None
    Fault: Optional[SpotInstanceStateFaultTypeDef] = None
    InstanceId: Optional[str] = None
    LaunchGroup: Optional[str] = None
    LaunchSpecification: Optional[LaunchSpecificationTypeDef] = None
    LaunchedAvailabilityZone: Optional[str] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    SpotInstanceRequestId: Optional[str] = None
    SpotPrice: Optional[str] = None
    State: Optional[SpotInstanceStateType] = None
    Status: Optional[SpotInstanceStatusTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    Type: Optional[SpotInstanceTypeType] = None
    ValidFrom: Optional[datetime] = None
    ValidUntil: Optional[datetime] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class RunInstancesRequestRequestTypeDef(BaseValidatorModel):
    MaxCount: int
    MinCount: int
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressTypeDef]] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabledTypeDef] = None
    Placement: Optional[PlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    ClientToken: Optional[str] = None
    DisableApiTermination: Optional[bool] = None
    DryRun: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    NetworkInterfaces: Optional[       Sequence[InstanceNetworkInterfaceSpecificationUnionTypeDef]     ] = None
    PrivateIpAddress: Optional[str] = None
    ElasticGpuSpecification: Optional[Sequence[ElasticGpuSpecificationTypeDef]] = None
    ElasticInferenceAccelerators: Optional[Sequence[ElasticInferenceAcceleratorTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceMarketOptions: Optional[InstanceMarketOptionsRequestTypeDef] = None
    CreditSpecification: Optional[CreditSpecificationRequestTypeDef] = None
    CpuOptions: Optional[CpuOptionsRequestTypeDef] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationTypeDef] = None
    HibernationOptions: Optional[HibernationOptionsRequestTypeDef] = None
    LicenseSpecifications: Optional[Sequence[LicenseConfigurationRequestTypeDef]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsRequestTypeDef] = None
    EnclaveOptions: Optional[EnclaveOptionsRequestTypeDef] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsRequestTypeDef] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptionsRequestTypeDef] = None
    DisableApiStop: Optional[bool] = None
    EnablePrimaryIpv6: Optional[bool] = None

class RunInstancesRequestServiceResourceCreateInstancesTypeDef(BaseValidatorModel):
    MaxCount: int
    MinCount: int
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    ImageId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[InstanceIpv6AddressTypeDef]] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    Monitoring: Optional[RunInstancesMonitoringEnabledTypeDef] = None
    Placement: Optional[PlacementTypeDef] = None
    RamdiskId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SecurityGroups: Optional[Sequence[str]] = None
    SubnetId: Optional[str] = None
    UserData: Optional[str] = None
    AdditionalInfo: Optional[str] = None
    ClientToken: Optional[str] = None
    DisableApiTermination: Optional[bool] = None
    DryRun: Optional[bool] = None
    EbsOptimized: Optional[bool] = None
    IamInstanceProfile: Optional[IamInstanceProfileSpecificationTypeDef] = None
    InstanceInitiatedShutdownBehavior: Optional[ShutdownBehaviorType] = None
    NetworkInterfaces: Optional[       Sequence[InstanceNetworkInterfaceSpecificationUnionTypeDef]     ] = None
    PrivateIpAddress: Optional[str] = None
    ElasticGpuSpecification: Optional[Sequence[ElasticGpuSpecificationTypeDef]] = None
    ElasticInferenceAccelerators: Optional[Sequence[ElasticInferenceAcceleratorTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    LaunchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    InstanceMarketOptions: Optional[InstanceMarketOptionsRequestTypeDef] = None
    CreditSpecification: Optional[CreditSpecificationRequestTypeDef] = None
    CpuOptions: Optional[CpuOptionsRequestTypeDef] = None
    CapacityReservationSpecification: Optional[CapacityReservationSpecificationTypeDef] = None
    HibernationOptions: Optional[HibernationOptionsRequestTypeDef] = None
    LicenseSpecifications: Optional[Sequence[LicenseConfigurationRequestTypeDef]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsRequestTypeDef] = None
    EnclaveOptions: Optional[EnclaveOptionsRequestTypeDef] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsRequestTypeDef] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptionsRequestTypeDef] = None
    DisableApiStop: Optional[bool] = None
    EnablePrimaryIpv6: Optional[bool] = None

class RequestSpotInstancesRequestRequestTypeDef(BaseValidatorModel):
    AvailabilityZoneGroup: Optional[str] = None
    BlockDurationMinutes: Optional[int] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    InstanceCount: Optional[int] = None
    LaunchGroup: Optional[str] = None
    LaunchSpecification: Optional[RequestSpotLaunchSpecificationTypeDef] = None
    SpotPrice: Optional[str] = None
    Type: Optional[SpotInstanceTypeType] = None
    ValidFrom: Optional[TimestampTypeDef] = None
    ValidUntil: Optional[TimestampTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class CreateLaunchTemplateRequestRequestTypeDef(BaseValidatorModel):
    LaunchTemplateName: str
    LaunchTemplateData: RequestLaunchTemplateDataTypeDef
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    VersionDescription: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateLaunchTemplateVersionRequestRequestTypeDef(BaseValidatorModel):
    LaunchTemplateData: RequestLaunchTemplateDataTypeDef
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    SourceVersion: Optional[str] = None
    VersionDescription: Optional[str] = None
    ResolveAlias: Optional[bool] = None

class InstanceTypeDef(BaseValidatorModel):
    AmiLaunchIndex: Optional[int] = None
    ImageId: Optional[str] = None
    InstanceId: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    KernelId: Optional[str] = None
    KeyName: Optional[str] = None
    LaunchTime: Optional[datetime] = None
    Monitoring: Optional[MonitoringTypeDef] = None
    Placement: Optional[PlacementTypeDef] = None
    Platform: Optional[Literal["windows"]] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None
    ProductCodes: Optional[List[ProductCodeTypeDef]] = None
    PublicDnsName: Optional[str] = None
    PublicIpAddress: Optional[str] = None
    RamdiskId: Optional[str] = None
    State: Optional[InstanceStateTypeDef] = None
    StateTransitionReason: Optional[str] = None
    SubnetId: Optional[str] = None
    VpcId: Optional[str] = None
    Architecture: Optional[ArchitectureValuesType] = None
    BlockDeviceMappings: Optional[List[InstanceBlockDeviceMappingTypeDef]] = None
    ClientToken: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    EnaSupport: Optional[bool] = None
    Hypervisor: Optional[HypervisorTypeType] = None
    IamInstanceProfile: Optional[IamInstanceProfileTypeDef] = None
    InstanceLifecycle: Optional[InstanceLifecycleTypeType] = None
    ElasticGpuAssociations: Optional[List[ElasticGpuAssociationTypeDef]] = None
    ElasticInferenceAcceleratorAssociations: Optional[       List[ElasticInferenceAcceleratorAssociationTypeDef]     ] = None
    NetworkInterfaces: Optional[List[InstanceNetworkInterfaceTypeDef]] = None
    OutpostArn: Optional[str] = None
    RootDeviceName: Optional[str] = None
    RootDeviceType: Optional[DeviceTypeType] = None
    SecurityGroups: Optional[List[GroupIdentifierTypeDef]] = None
    SourceDestCheck: Optional[bool] = None
    SpotInstanceRequestId: Optional[str] = None
    SriovNetSupport: Optional[str] = None
    StateReason: Optional[StateReasonTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    VirtualizationType: Optional[VirtualizationTypeType] = None
    CpuOptions: Optional[CpuOptionsTypeDef] = None
    CapacityReservationId: Optional[str] = None
    CapacityReservationSpecification: Optional[       CapacityReservationSpecificationResponseTypeDef     ] = None
    HibernationOptions: Optional[HibernationOptionsTypeDef] = None
    Licenses: Optional[List[LicenseConfigurationTypeDef]] = None
    MetadataOptions: Optional[InstanceMetadataOptionsResponseTypeDef] = None
    EnclaveOptions: Optional[EnclaveOptionsTypeDef] = None
    BootMode: Optional[BootModeValuesType] = None
    PlatformDetails: Optional[str] = None
    UsageOperation: Optional[str] = None
    UsageOperationUpdateTime: Optional[datetime] = None
    PrivateDnsNameOptions: Optional[PrivateDnsNameOptionsResponseTypeDef] = None
    Ipv6Address: Optional[str] = None
    TpmSupport: Optional[str] = None
    MaintenanceOptions: Optional[InstanceMaintenanceOptionsTypeDef] = None
    CurrentInstanceBootMode: Optional[InstanceBootModeValuesType] = None

class SpotFleetRequestConfigDataExtraOutputTypeDef(BaseValidatorModel):
    IamFleetRole: str
    TargetCapacity: int
    AllocationStrategy: Optional[AllocationStrategyType] = None
    OnDemandAllocationStrategy: Optional[OnDemandAllocationStrategyType] = None
    SpotMaintenanceStrategies: Optional[SpotMaintenanceStrategiesTypeDef] = None
    ClientToken: Optional[str] = None
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None
    FulfilledCapacity: Optional[float] = None
    OnDemandFulfilledCapacity: Optional[float] = None
    LaunchSpecifications: Optional[List[SpotFleetLaunchSpecificationExtraOutputTypeDef]] = None
    LaunchTemplateConfigs: Optional[List[LaunchTemplateConfigExtraOutputTypeDef]] = None
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
    LoadBalancersConfig: Optional[LoadBalancersConfigExtraOutputTypeDef] = None
    InstancePoolsToUseCount: Optional[int] = None
    Context: Optional[str] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationExtraOutputTypeDef]] = None

class CreateFleetErrorTypeDef(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class CreateFleetInstanceTypeDef(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    InstanceIds: Optional[List[str]] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[Literal["windows"]] = None

class DescribeFleetErrorTypeDef(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class DescribeFleetsInstancesTypeDef(BaseValidatorModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    InstanceIds: Optional[List[str]] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[Literal["windows"]] = None

class SpotFleetRequestConfigDataOutputTypeDef(BaseValidatorModel):
    IamFleetRole: str
    TargetCapacity: int
    AllocationStrategy: Optional[AllocationStrategyType] = None
    OnDemandAllocationStrategy: Optional[OnDemandAllocationStrategyType] = None
    SpotMaintenanceStrategies: Optional[SpotMaintenanceStrategiesTypeDef] = None
    ClientToken: Optional[str] = None
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None
    FulfilledCapacity: Optional[float] = None
    OnDemandFulfilledCapacity: Optional[float] = None
    LaunchSpecifications: Optional[List[SpotFleetLaunchSpecificationOutputTypeDef]] = None
    LaunchTemplateConfigs: Optional[List[LaunchTemplateConfigOutputTypeDef]] = None
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
    LoadBalancersConfig: Optional[LoadBalancersConfigOutputTypeDef] = None
    InstancePoolsToUseCount: Optional[int] = None
    Context: Optional[str] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    TagSpecifications: Optional[List[TagSpecificationOutputTypeDef]] = None

class SpotFleetRequestConfigDataTypeDef(BaseValidatorModel):
    IamFleetRole: str
    TargetCapacity: int
    AllocationStrategy: Optional[AllocationStrategyType] = None
    OnDemandAllocationStrategy: Optional[OnDemandAllocationStrategyType] = None
    SpotMaintenanceStrategies: Optional[SpotMaintenanceStrategiesTypeDef] = None
    ClientToken: Optional[str] = None
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None
    FulfilledCapacity: Optional[float] = None
    OnDemandFulfilledCapacity: Optional[float] = None
    LaunchSpecifications: Optional[Sequence[SpotFleetLaunchSpecificationTypeDef]] = None
    LaunchTemplateConfigs: Optional[Sequence[LaunchTemplateConfigTypeDef]] = None
    SpotPrice: Optional[str] = None
    OnDemandTargetCapacity: Optional[int] = None
    OnDemandMaxTotalPrice: Optional[str] = None
    SpotMaxTotalPrice: Optional[str] = None
    TerminateInstancesWithExpiration: Optional[bool] = None
    Type: Optional[FleetTypeType] = None
    ValidFrom: Optional[TimestampTypeDef] = None
    ValidUntil: Optional[TimestampTypeDef] = None
    ReplaceUnhealthyInstances: Optional[bool] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None
    LoadBalancersConfig: Optional[LoadBalancersConfigTypeDef] = None
    InstancePoolsToUseCount: Optional[int] = None
    Context: Optional[str] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None

class CreateFleetRequestRequestTypeDef(BaseValidatorModel):
    LaunchTemplateConfigs: Sequence[FleetLaunchTemplateConfigRequestTypeDef]
    TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    SpotOptions: Optional[SpotOptionsRequestTypeDef] = None
    OnDemandOptions: Optional[OnDemandOptionsRequestTypeDef] = None
    ExcessCapacityTerminationPolicy: Optional[FleetExcessCapacityTerminationPolicyType] = None
    TerminateInstancesWithExpiration: Optional[bool] = None
    Type: Optional[FleetTypeType] = None
    ValidFrom: Optional[TimestampTypeDef] = None
    ValidUntil: Optional[TimestampTypeDef] = None
    ReplaceUnhealthyInstances: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    Context: Optional[str] = None

class ModifyFleetRequestRequestTypeDef(BaseValidatorModel):
    FleetId: str
    DryRun: Optional[bool] = None
    ExcessCapacityTerminationPolicy: Optional[FleetExcessCapacityTerminationPolicyType] = None
    LaunchTemplateConfigs: Optional[Sequence[FleetLaunchTemplateConfigRequestTypeDef]] = None
    TargetCapacitySpecification: Optional[TargetCapacitySpecificationRequestTypeDef] = None
    Context: Optional[str] = None

class GetLaunchTemplateDataResultTypeDef(BaseValidatorModel):
    LaunchTemplateData: ResponseLaunchTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchTemplateVersionTypeDef(BaseValidatorModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None
    VersionDescription: Optional[str] = None
    CreateTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DefaultVersion: Optional[bool] = None
    LaunchTemplateData: Optional[ResponseLaunchTemplateDataTypeDef] = None

class DescribeInstanceTypesResultTypeDef(BaseValidatorModel):
    InstanceTypes: List[InstanceTypeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateNetworkInsightsAccessScopeResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScope: NetworkInsightsAccessScopeTypeDef
    NetworkInsightsAccessScopeContent: NetworkInsightsAccessScopeContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkInsightsAccessScopeContentResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeContent: NetworkInsightsAccessScopeContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef(BaseValidatorModel):
    LoggingConfigurations: List[VerifiedAccessInstanceLoggingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef(BaseValidatorModel):
    LoggingConfiguration: VerifiedAccessInstanceLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef(BaseValidatorModel):
    NetworkInsightsAccessScopeAnalysisId: str
    AnalysisStatus: AnalysisStatusType
    AnalysisFindings: List[AccessScopeAnalysisFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeNetworkInsightsAnalysesResultTypeDef(BaseValidatorModel):
    NetworkInsightsAnalyses: List[NetworkInsightsAnalysisTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartNetworkInsightsAnalysisResultTypeDef(BaseValidatorModel):
    NetworkInsightsAnalysis: NetworkInsightsAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpnConnectionResultTypeDef(BaseValidatorModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpnConnectionsResultTypeDef(BaseValidatorModel):
    VpnConnections: List[VpnConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnConnectionOptionsResultTypeDef(BaseValidatorModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnConnectionResultTypeDef(BaseValidatorModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnTunnelCertificateResultTypeDef(BaseValidatorModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnTunnelOptionsResultTypeDef(BaseValidatorModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpotInstanceRequestsResultTypeDef(BaseValidatorModel):
    SpotInstanceRequests: List[SpotInstanceRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RequestSpotInstancesResultTypeDef(BaseValidatorModel):
    SpotInstanceRequests: List[SpotInstanceRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationResponseTypeDef(BaseValidatorModel):
    Groups: List[GroupIdentifierTypeDef]
    Instances: List[InstanceTypeDef]
    OwnerId: str
    RequesterId: str
    ReservationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationTypeDef(BaseValidatorModel):
    Groups: Optional[List[GroupIdentifierTypeDef]] = None
    Instances: Optional[List[InstanceTypeDef]] = None
    OwnerId: Optional[str] = None
    RequesterId: Optional[str] = None
    ReservationId: Optional[str] = None

class CreateFleetResultTypeDef(BaseValidatorModel):
    FleetId: str
    Errors: List[CreateFleetErrorTypeDef]
    Instances: List[CreateFleetInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FleetDataTypeDef(BaseValidatorModel):
    ActivityStatus: Optional[FleetActivityStatusType] = None
    CreateTime: Optional[datetime] = None
    FleetId: Optional[str] = None
    FleetState: Optional[FleetStateCodeType] = None
    ClientToken: Optional[str] = None
    ExcessCapacityTerminationPolicy: Optional[FleetExcessCapacityTerminationPolicyType] = None
    FulfilledCapacity: Optional[float] = None
    FulfilledOnDemandCapacity: Optional[float] = None
    LaunchTemplateConfigs: Optional[List[FleetLaunchTemplateConfigTypeDef]] = None
    TargetCapacitySpecification: Optional[TargetCapacitySpecificationTypeDef] = None
    TerminateInstancesWithExpiration: Optional[bool] = None
    Type: Optional[FleetTypeType] = None
    ValidFrom: Optional[datetime] = None
    ValidUntil: Optional[datetime] = None
    ReplaceUnhealthyInstances: Optional[bool] = None
    SpotOptions: Optional[SpotOptionsTypeDef] = None
    OnDemandOptions: Optional[OnDemandOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    Errors: Optional[List[DescribeFleetErrorTypeDef]] = None
    Instances: Optional[List[DescribeFleetsInstancesTypeDef]] = None
    Context: Optional[str] = None

class SpotFleetRequestConfigTypeDef(BaseValidatorModel):
    ActivityStatus: Optional[ActivityStatusType] = None
    CreateTime: Optional[datetime] = None
    SpotFleetRequestConfig: Optional[SpotFleetRequestConfigDataOutputTypeDef] = None
    SpotFleetRequestId: Optional[str] = None
    SpotFleetRequestState: Optional[BatchStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class ModifySpotFleetRequestRequestRequestTypeDef(BaseValidatorModel):
    SpotFleetRequestId: str
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None
    LaunchTemplateConfigs: Optional[Sequence[LaunchTemplateConfigUnionTypeDef]] = None
    TargetCapacity: Optional[int] = None
    OnDemandTargetCapacity: Optional[int] = None
    Context: Optional[str] = None

class RequestSpotFleetRequestRequestTypeDef(BaseValidatorModel):
    SpotFleetRequestConfig: SpotFleetRequestConfigDataTypeDef
    DryRun: Optional[bool] = None

class CreateLaunchTemplateVersionResultTypeDef(BaseValidatorModel):
    LaunchTemplateVersion: LaunchTemplateVersionTypeDef
    Warning: ValidationWarningTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLaunchTemplateVersionsResultTypeDef(BaseValidatorModel):
    LaunchTemplateVersions: List[LaunchTemplateVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancesResultTypeDef(BaseValidatorModel):
    Reservations: List[ReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFleetsResultTypeDef(BaseValidatorModel):
    Fleets: List[FleetDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestsResponseTypeDef(BaseValidatorModel):
    SpotFleetRequestConfigs: List[SpotFleetRequestConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

