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
from aws_resource_validator.pydantic_models.ec2_constants import *

class AcceleratorCountRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AcceleratorCountTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AcceleratorTotalMemoryMiBRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AcceleratorTotalMemoryMiBTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class AddressTransferTypeDef(BaseModel):
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    TransferAccountId: Optional[str] = None
    TransferOfferExpirationTimestamp: Optional[datetime] = None
    TransferOfferAcceptedTimestamp: Optional[datetime] = None
    AddressTransferStatus: Optional[AddressTransferStatusType] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class TargetConfigurationRequestTypeDef(BaseModel):
    OfferingId: str
    InstanceCount: Optional[int] = None

class AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class AcceptVpcEndpointConnectionsRequestRequestTypeDef(BaseModel):
    ServiceId: str
    VpcEndpointIds: Sequence[str]
    DryRun: Optional[bool] = None

class AcceptVpcPeeringConnectionRequestRequestTypeDef(BaseModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None

class AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class AccountAttributeValueTypeDef(BaseModel):
    AttributeValue: Optional[str] = None

class ActiveInstanceTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    SpotInstanceRequestId: Optional[str] = None
    InstanceHealth: Optional[InstanceHealthStatusType] = None

class AddIpamOperatingRegionTypeDef(BaseModel):
    RegionName: Optional[str] = None

class AddPrefixListEntryTypeDef(BaseModel):
    Cidr: str
    Description: Optional[str] = None

class AddedPrincipalTypeDef(BaseModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None
    ServicePermissionId: Optional[str] = None
    ServiceId: Optional[str] = None

class AnalysisComponentTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None

class RuleGroupTypePairTypeDef(BaseModel):
    RuleGroupArn: Optional[str] = None
    RuleGroupType: Optional[str] = None

class RuleOptionTypeDef(BaseModel):
    Keyword: Optional[str] = None
    Settings: Optional[List[str]] = None

class PtrUpdateStatusTypeDef(BaseModel):
    Value: Optional[str] = None
    Status: Optional[str] = None
    Reason: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class AdvertiseByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str
    Asn: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class AllocateIpamPoolCidrRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None
    NetmaskLength: Optional[int] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    PreviewNextCidr: Optional[bool] = None
    AllowedCidrs: Optional[Sequence[str]] = None
    DisallowedCidrs: Optional[Sequence[str]] = None

class IpamPoolAllocationTypeDef(BaseModel):
    Cidr: Optional[str] = None
    IpamPoolAllocationId: Optional[str] = None
    Description: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamPoolAllocationResourceTypeType] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None

class AlternatePathHintTypeDef(BaseModel):
    ComponentId: Optional[str] = None
    ComponentArn: Optional[str] = None

class PortRangeTypeDef(BaseModel):
    From: Optional[int] = None
    To: Optional[int] = None

class AnalysisLoadBalancerListenerTypeDef(BaseModel):
    LoadBalancerPort: Optional[int] = None
    InstancePort: Optional[int] = None

class AnalysisRouteTableRouteTypeDef(BaseModel):
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

class ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    VpcId: str
    SecurityGroupIds: Sequence[str]
    DryRun: Optional[bool] = None

class AsnAssociationTypeDef(BaseModel):
    Asn: Optional[str] = None
    Cidr: Optional[str] = None
    StatusMessage: Optional[str] = None
    State: Optional[AsnAssociationStateType] = None

class AsnAuthorizationContextTypeDef(BaseModel):
    Message: str
    Signature: str

class AssignIpv6AddressesRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    Ipv6AddressCount: Optional[int] = None
    Ipv6Addresses: Optional[Sequence[str]] = None
    Ipv6PrefixCount: Optional[int] = None
    Ipv6Prefixes: Optional[Sequence[str]] = None

class AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef(BaseModel):
    AllowReassignment: Optional[bool] = None
    PrivateIpAddresses: Optional[Sequence[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None
    Ipv4PrefixCount: Optional[int] = None

class AssignPrivateIpAddressesRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    AllowReassignment: Optional[bool] = None
    PrivateIpAddresses: Optional[Sequence[str]] = None
    SecondaryPrivateIpAddressCount: Optional[int] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None
    Ipv4PrefixCount: Optional[int] = None

class AssignedPrivateIpAddressTypeDef(BaseModel):
    PrivateIpAddress: Optional[str] = None

class Ipv4PrefixSpecificationTypeDef(BaseModel):
    Ipv4Prefix: Optional[str] = None

class AssignPrivateNatGatewayAddressRequestRequestTypeDef(BaseModel):
    NatGatewayId: str
    PrivateIpAddresses: Optional[Sequence[str]] = None
    PrivateIpAddressCount: Optional[int] = None
    DryRun: Optional[bool] = None

class NatGatewayAddressTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIp: Optional[str] = None
    PublicIp: Optional[str] = None
    AssociationId: Optional[str] = None
    IsPrimary: Optional[bool] = None
    FailureMessage: Optional[str] = None
    Status: Optional[NatGatewayAddressStatusType] = None

class AssociateAddressRequestClassicAddressAssociateTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    InstanceId: Optional[str] = None
    AllowReassociation: Optional[bool] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class AssociateAddressRequestRequestTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    AllowReassociation: Optional[bool] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class AssociateAddressRequestVpcAddressAssociateTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    PublicIp: Optional[str] = None
    AllowReassociation: Optional[bool] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class AssociateClientVpnTargetNetworkRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    SubnetId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AssociationStatusTypeDef(BaseModel):
    Code: Optional[AssociationStatusCodeType] = None
    Message: Optional[str] = None

class AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None

class AssociateDhcpOptionsRequestRequestTypeDef(BaseModel):
    DhcpOptionsId: str
    VpcId: str
    DryRun: Optional[bool] = None

class AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef(BaseModel):
    DhcpOptionsId: str
    DryRun: Optional[bool] = None

class AssociateEnclaveCertificateIamRoleRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    RoleArn: str
    DryRun: Optional[bool] = None

class IamInstanceProfileSpecificationTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class AssociateIpamByoasnRequestRequestTypeDef(BaseModel):
    Asn: str
    Cidr: str
    DryRun: Optional[bool] = None

class AssociateNatGatewayAddressRequestRequestTypeDef(BaseModel):
    NatGatewayId: str
    AllocationIds: Sequence[str]
    PrivateIpAddresses: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class AssociateRouteTableRequestRequestTypeDef(BaseModel):
    RouteTableId: str
    DryRun: Optional[bool] = None
    SubnetId: Optional[str] = None
    GatewayId: Optional[str] = None

class AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    SubnetId: Optional[str] = None
    GatewayId: Optional[str] = None

class RouteTableAssociationStateTypeDef(BaseModel):
    State: Optional[RouteTableAssociationStateCodeType] = None
    StatusMessage: Optional[str] = None

class AssociateSubnetCidrBlockRequestRequestTypeDef(BaseModel):
    SubnetId: str
    Ipv6CidrBlock: Optional[str] = None
    Ipv6IpamPoolId: Optional[str] = None
    Ipv6NetmaskLength: Optional[int] = None

class AssociateTransitGatewayMulticastDomainRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    TransitGatewayAttachmentId: str
    SubnetIds: Sequence[str]
    DryRun: Optional[bool] = None

class AssociateTransitGatewayPolicyTableRequestRequestTypeDef(BaseModel):
    TransitGatewayPolicyTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class TransitGatewayPolicyTableAssociationTypeDef(BaseModel):
    TransitGatewayPolicyTableId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class AssociateTransitGatewayRouteTableRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class TransitGatewayAssociationTypeDef(BaseModel):
    TransitGatewayRouteTableId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class AssociateTrunkInterfaceRequestRequestTypeDef(BaseModel):
    BranchInterfaceId: str
    TrunkInterfaceId: str
    VlanId: Optional[int] = None
    GreKey: Optional[int] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AssociateVpcCidrBlockRequestRequestTypeDef(BaseModel):
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

class AssociatedRoleTypeDef(BaseModel):
    AssociatedRoleArn: Optional[str] = None
    CertificateS3BucketName: Optional[str] = None
    CertificateS3ObjectKey: Optional[str] = None
    EncryptionKmsKeyId: Optional[str] = None

class AssociatedTargetNetworkTypeDef(BaseModel):
    NetworkId: Optional[str] = None
    NetworkType: Optional[Literal["vpc"]] = None

class AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef(BaseModel):
    Groups: Sequence[str]
    VpcId: str
    DryRun: Optional[bool] = None

class AttachClassicLinkVpcRequestRequestTypeDef(BaseModel):
    Groups: Sequence[str]
    InstanceId: str
    VpcId: str
    DryRun: Optional[bool] = None

class AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef(BaseModel):
    Groups: Sequence[str]
    InstanceId: str
    DryRun: Optional[bool] = None

class AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None

class AttachInternetGatewayRequestRequestTypeDef(BaseModel):
    InternetGatewayId: str
    VpcId: str
    DryRun: Optional[bool] = None

class AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef(BaseModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None

class AttachVerifiedAccessTrustProviderRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceId: str
    VerifiedAccessTrustProviderId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AttachVolumeRequestInstanceAttachVolumeTypeDef(BaseModel):
    Device: str
    VolumeId: str
    DryRun: Optional[bool] = None

class AttachVolumeRequestRequestTypeDef(BaseModel):
    Device: str
    InstanceId: str
    VolumeId: str
    DryRun: Optional[bool] = None

class AttachVolumeRequestVolumeAttachToInstanceTypeDef(BaseModel):
    Device: str
    InstanceId: str
    DryRun: Optional[bool] = None

class AttachVpnGatewayRequestRequestTypeDef(BaseModel):
    VpcId: str
    VpnGatewayId: str
    DryRun: Optional[bool] = None

class VpcAttachmentTypeDef(BaseModel):
    State: Optional[AttachmentStatusType] = None
    VpcId: Optional[str] = None

class AttachmentEnaSrdUdpSpecificationTypeDef(BaseModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class AttributeBooleanValueTypeDef(BaseModel):
    Value: Optional[bool] = None

class AttributeValueTypeDef(BaseModel):
    Value: Optional[str] = None

class ClientVpnAuthorizationRuleStatusTypeDef(BaseModel):
    Code: Optional[ClientVpnAuthorizationRuleStatusCodeType] = None
    Message: Optional[str] = None

class AuthorizeClientVpnIngressRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    TargetNetworkCidr: str
    AccessGroupId: Optional[str] = None
    AuthorizeAllGroups: Optional[bool] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class AvailabilityZoneMessageTypeDef(BaseModel):
    Message: Optional[str] = None

class InstanceCapacityTypeDef(BaseModel):
    AvailableCapacity: Optional[int] = None
    InstanceType: Optional[str] = None
    TotalCapacity: Optional[int] = None

class BaselineEbsBandwidthMbpsRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class BaselineEbsBandwidthMbpsTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class EbsBlockDeviceTypeDef(BaseModel):
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    KmsKeyId: Optional[str] = None
    Throughput: Optional[int] = None
    OutpostArn: Optional[str] = None
    Encrypted: Optional[bool] = None

class BundleTaskErrorTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ByoasnTypeDef(BaseModel):
    Asn: Optional[str] = None
    IpamId: Optional[str] = None
    StatusMessage: Optional[str] = None
    State: Optional[AsnStateType] = None

class CancelBundleTaskRequestRequestTypeDef(BaseModel):
    BundleId: str
    DryRun: Optional[bool] = None

class CancelCapacityReservationFleetErrorTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class CancelCapacityReservationFleetsRequestRequestTypeDef(BaseModel):
    CapacityReservationFleetIds: Sequence[str]
    DryRun: Optional[bool] = None

class CapacityReservationFleetCancellationStateTypeDef(BaseModel):
    CurrentFleetState: Optional[CapacityReservationFleetStateType] = None
    PreviousFleetState: Optional[CapacityReservationFleetStateType] = None
    CapacityReservationFleetId: Optional[str] = None

class CancelCapacityReservationRequestRequestTypeDef(BaseModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None

class CancelConversionRequestRequestTypeDef(BaseModel):
    ConversionTaskId: str
    DryRun: Optional[bool] = None
    ReasonMessage: Optional[str] = None

class CancelExportTaskRequestRequestTypeDef(BaseModel):
    ExportTaskId: str

class CancelImageLaunchPermissionRequestRequestTypeDef(BaseModel):
    ImageId: str
    DryRun: Optional[bool] = None

class CancelImportTaskRequestRequestTypeDef(BaseModel):
    CancelReason: Optional[str] = None
    DryRun: Optional[bool] = None
    ImportTaskId: Optional[str] = None

class CancelReservedInstancesListingRequestRequestTypeDef(BaseModel):
    ReservedInstancesListingId: str

class CancelSpotFleetRequestsErrorTypeDef(BaseModel):
    Code: Optional[CancelBatchErrorCodeType] = None
    Message: Optional[str] = None

class CancelSpotFleetRequestsRequestRequestTypeDef(BaseModel):
    SpotFleetRequestIds: Sequence[str]
    TerminateInstances: bool
    DryRun: Optional[bool] = None

class CancelSpotFleetRequestsSuccessItemTypeDef(BaseModel):
    CurrentSpotFleetRequestState: Optional[BatchStateType] = None
    PreviousSpotFleetRequestState: Optional[BatchStateType] = None
    SpotFleetRequestId: Optional[str] = None

class CancelSpotInstanceRequestsRequestRequestTypeDef(BaseModel):
    SpotInstanceRequestIds: Sequence[str]
    DryRun: Optional[bool] = None

class CancelledSpotInstanceRequestTypeDef(BaseModel):
    SpotInstanceRequestId: Optional[str] = None
    State: Optional[CancelSpotInstanceRequestStateType] = None

class CapacityAllocationTypeDef(BaseModel):
    AllocationType: Optional[Literal["used"]] = None
    Count: Optional[int] = None

class CapacityBlockOfferingTypeDef(BaseModel):
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

class FleetCapacityReservationTypeDef(BaseModel):
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

class CapacityReservationGroupTypeDef(BaseModel):
    GroupArn: Optional[str] = None
    OwnerId: Optional[str] = None

class CapacityReservationOptionsRequestTypeDef(BaseModel):
    UsageStrategy: Optional[Literal["use-capacity-reservations-first"]] = None

class CapacityReservationOptionsTypeDef(BaseModel):
    UsageStrategy: Optional[Literal["use-capacity-reservations-first"]] = None

class CapacityReservationTargetResponseTypeDef(BaseModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class CapacityReservationTargetTypeDef(BaseModel):
    CapacityReservationId: Optional[str] = None
    CapacityReservationResourceGroupArn: Optional[str] = None

class CertificateAuthenticationRequestTypeDef(BaseModel):
    ClientRootCertificateChainArn: Optional[str] = None

class CertificateAuthenticationTypeDef(BaseModel):
    ClientRootCertificateChain: Optional[str] = None

class CidrAuthorizationContextTypeDef(BaseModel):
    Message: str
    Signature: str

class CidrBlockTypeDef(BaseModel):
    CidrBlock: Optional[str] = None

class ClassicLinkDnsSupportTypeDef(BaseModel):
    ClassicLinkDnsSupported: Optional[bool] = None
    VpcId: Optional[str] = None

class GroupIdentifierTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class ClassicLoadBalancerTypeDef(BaseModel):
    Name: Optional[str] = None

class ClientCertificateRevocationListStatusTypeDef(BaseModel):
    Code: Optional[ClientCertificateRevocationListStatusCodeType] = None
    Message: Optional[str] = None

class ClientConnectOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None

class ClientVpnEndpointAttributeStatusTypeDef(BaseModel):
    Code: Optional[ClientVpnEndpointAttributeStatusCodeType] = None
    Message: Optional[str] = None

class ClientLoginBannerOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None

class ClientLoginBannerResponseOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    BannerText: Optional[str] = None

class DirectoryServiceAuthenticationRequestTypeDef(BaseModel):
    DirectoryId: Optional[str] = None

class FederatedAuthenticationRequestTypeDef(BaseModel):
    SAMLProviderArn: Optional[str] = None
    SelfServiceSAMLProviderArn: Optional[str] = None

class DirectoryServiceAuthenticationTypeDef(BaseModel):
    DirectoryId: Optional[str] = None

class FederatedAuthenticationTypeDef(BaseModel):
    SamlProviderArn: Optional[str] = None
    SelfServiceSamlProviderArn: Optional[str] = None

class ClientVpnConnectionStatusTypeDef(BaseModel):
    Code: Optional[ClientVpnConnectionStatusCodeType] = None
    Message: Optional[str] = None

class ClientVpnEndpointStatusTypeDef(BaseModel):
    Code: Optional[ClientVpnEndpointStatusCodeType] = None
    Message: Optional[str] = None

class ConnectionLogResponseOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None

class ClientVpnRouteStatusTypeDef(BaseModel):
    Code: Optional[ClientVpnRouteStatusCodeType] = None
    Message: Optional[str] = None

class CloudWatchLogOptionsSpecificationTypeDef(BaseModel):
    LogEnabled: Optional[bool] = None
    LogGroupArn: Optional[str] = None
    LogOutputFormat: Optional[str] = None

class CloudWatchLogOptionsTypeDef(BaseModel):
    LogEnabled: Optional[bool] = None
    LogGroupArn: Optional[str] = None
    LogOutputFormat: Optional[str] = None

class CoipAddressUsageTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    CoIp: Optional[str] = None

class CoipCidrTypeDef(BaseModel):
    Cidr: Optional[str] = None
    CoipPoolId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None

class ConfirmProductInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ProductCode: str
    DryRun: Optional[bool] = None

class ConnectionLogOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    CloudwatchLogGroup: Optional[str] = None
    CloudwatchLogStream: Optional[str] = None

class ConnectionNotificationTypeDef(BaseModel):
    ConnectionNotificationId: Optional[str] = None
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    ConnectionNotificationType: Optional[Literal["Topic"]] = None
    ConnectionNotificationArn: Optional[str] = None
    ConnectionEvents: Optional[List[str]] = None
    ConnectionNotificationState: Optional[ConnectionNotificationStateType] = None

class ConnectionTrackingConfigurationTypeDef(BaseModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None

class ConnectionTrackingSpecificationRequestTypeDef(BaseModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None

class ConnectionTrackingSpecificationResponseTypeDef(BaseModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None

class ConnectionTrackingSpecificationTypeDef(BaseModel):
    TcpEstablishedTimeout: Optional[int] = None
    UdpTimeout: Optional[int] = None
    UdpStreamTimeout: Optional[int] = None

class CopyFpgaImageRequestRequestTypeDef(BaseModel):
    SourceFpgaImageId: str
    SourceRegion: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None

class CpuOptionsRequestTypeDef(BaseModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class CpuOptionsTypeDef(BaseModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class ReservationFleetInstanceSpecificationTypeDef(BaseModel):
    InstanceType: Optional[InstanceTypeType] = None
    InstancePlatform: Optional[CapacityReservationInstancePlatformType] = None
    Weight: Optional[float] = None
    AvailabilityZone: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    EbsOptimized: Optional[bool] = None
    Priority: Optional[int] = None

class CreateClientVpnRouteRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    DestinationCidrBlock: str
    TargetVpcSubnetId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class CreateCoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str
    CoipPoolId: str
    DryRun: Optional[bool] = None

class CreateDefaultSubnetRequestRequestTypeDef(BaseModel):
    AvailabilityZone: str
    DryRun: Optional[bool] = None
    Ipv6Native: Optional[bool] = None

class CreateDefaultVpcRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class NewDhcpConfigurationTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class TargetCapacitySpecificationRequestTypeDef(BaseModel):
    TotalTargetCapacity: int
    OnDemandTargetCapacity: Optional[int] = None
    SpotTargetCapacity: Optional[int] = None
    DefaultTargetCapacityType: Optional[DefaultTargetCapacityTypeType] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None

class DestinationOptionsRequestTypeDef(BaseModel):
    FileFormat: Optional[DestinationFileFormatType] = None
    HiveCompatiblePartitions: Optional[bool] = None
    PerHourPartition: Optional[bool] = None

class StorageLocationTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Key: Optional[str] = None

class InstanceEventWindowTimeRangeRequestTypeDef(BaseModel):
    StartWeekDay: Optional[WeekDayType] = None
    StartHour: Optional[int] = None
    EndWeekDay: Optional[WeekDayType] = None
    EndHour: Optional[int] = None

class ExportToS3TaskSpecificationTypeDef(BaseModel):
    ContainerFormat: Optional[Literal["ova"]] = None
    DiskImageFormat: Optional[DiskImageFormatType] = None
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None

class IpamPoolSourceResourceRequestTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal["vpc"]] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None

class RequestIpamResourceTagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class CreateLocalGatewayRouteRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceId: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None

class LocalGatewayRouteTypeDef(BaseModel):
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

class IcmpTypeCodeTypeDef(BaseModel):
    Code: Optional[int] = None
    Type: Optional[int] = None

class CreateNetworkInterfacePermissionRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    Permission: InterfacePermissionTypeType
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    DryRun: Optional[bool] = None

class InstanceIpv6AddressTypeDef(BaseModel):
    Ipv6Address: Optional[str] = None
    IsPrimaryIpv6: Optional[bool] = None

class Ipv4PrefixSpecificationRequestTypeDef(BaseModel):
    Ipv4Prefix: Optional[str] = None

class Ipv6PrefixSpecificationRequestTypeDef(BaseModel):
    Ipv6Prefix: Optional[str] = None

class PrivateIpAddressSpecificationTypeDef(BaseModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None

class PriceScheduleSpecificationTypeDef(BaseModel):
    CurrencyCode: Optional[Literal["USD"]] = None
    Price: Optional[float] = None
    Term: Optional[int] = None

class CreateRouteRequestRequestTypeDef(BaseModel):
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

class CreateRouteRequestRouteTableCreateRouteTypeDef(BaseModel):
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

class InstanceSpecificationTypeDef(BaseModel):
    InstanceId: str
    ExcludeBootVolume: Optional[bool] = None
    ExcludeDataVolumeIds: Optional[Sequence[str]] = None

class CreateSpotDatafeedSubscriptionRequestRequestTypeDef(BaseModel):
    Bucket: str
    DryRun: Optional[bool] = None
    Prefix: Optional[str] = None

class S3ObjectTagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class TrafficMirrorPortRangeRequestTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class TransitGatewayConnectRequestBgpOptionsTypeDef(BaseModel):
    PeerAsn: Optional[int] = None

class CreateTransitGatewayConnectRequestOptionsTypeDef(BaseModel):
    Protocol: Literal["gre"]

class CreateTransitGatewayMulticastDomainRequestOptionsTypeDef(BaseModel):
    Igmpv2Support: Optional[Igmpv2SupportValueType] = None
    StaticSourcesSupport: Optional[StaticSourcesSupportValueType] = None
    AutoAcceptSharedAssociations: Optional[AutoAcceptSharedAssociationsValueType] = None

class CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef(BaseModel):
    DynamicRouting: Optional[DynamicRoutingValueType] = None

class CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class TransitGatewayRequestOptionsTypeDef(BaseModel):
    AmazonSideAsn: Optional[int] = None
    AutoAcceptSharedAttachments: Optional[AutoAcceptSharedAttachmentsValueType] = None
    DefaultRouteTableAssociation: Optional[DefaultRouteTableAssociationValueType] = None
    DefaultRouteTablePropagation: Optional[DefaultRouteTablePropagationValueType] = None
    VpnEcmpSupport: Optional[VpnEcmpSupportValueType] = None
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    MulticastSupport: Optional[MulticastSupportValueType] = None
    TransitGatewayCidrBlocks: Optional[Sequence[str]] = None

class CreateTransitGatewayRouteRequestRequestTypeDef(BaseModel):
    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef(BaseModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None

class CreateVerifiedAccessEndpointEniOptionsTypeDef(BaseModel):
    NetworkInterfaceId: Optional[str] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef(BaseModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    LoadBalancerArn: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None

class VerifiedAccessSseSpecificationRequestTypeDef(BaseModel):
    CustomerManagedKeyEnabled: Optional[bool] = None
    KmsKeyArn: Optional[str] = None

class CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef(BaseModel):
    TenantId: Optional[str] = None
    PublicSigningKeyUrl: Optional[str] = None

class CreateVerifiedAccessTrustProviderOidcOptionsTypeDef(BaseModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None

class CreateVolumePermissionTypeDef(BaseModel):
    Group: Optional[Literal["all"]] = None
    UserId: Optional[str] = None

class CreateVpcEndpointConnectionNotificationRequestRequestTypeDef(BaseModel):
    ConnectionNotificationArn: str
    ConnectionEvents: Sequence[str]
    DryRun: Optional[bool] = None
    ServiceId: Optional[str] = None
    VpcEndpointId: Optional[str] = None
    ClientToken: Optional[str] = None

class DnsOptionsSpecificationTypeDef(BaseModel):
    DnsRecordIpType: Optional[DnsRecordIpTypeType] = None
    PrivateDnsOnlyForInboundResolverEndpoint: Optional[bool] = None

class SubnetConfigurationTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    Ipv4: Optional[str] = None
    Ipv6: Optional[str] = None

class CreateVpnConnectionRouteRequestRequestTypeDef(BaseModel):
    DestinationCidrBlock: str
    VpnConnectionId: str

class CreditSpecificationRequestTypeDef(BaseModel):
    CpuCredits: str

class CreditSpecificationTypeDef(BaseModel):
    CpuCredits: Optional[str] = None

class DataQueryTypeDef(BaseModel):
    Id: Optional[str] = None
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    Period: Optional[PeriodTypeType] = None

class MetricPointTypeDef(BaseModel):
    StartDate: Optional[datetime] = None
    EndDate: Optional[datetime] = None
    Value: Optional[float] = None
    Status: Optional[str] = None

class DeleteCarrierGatewayRequestRequestTypeDef(BaseModel):
    CarrierGatewayId: str
    DryRun: Optional[bool] = None

class DeleteClientVpnEndpointRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None

class DeleteClientVpnRouteRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    DestinationCidrBlock: str
    TargetVpcSubnetId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteCoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str
    CoipPoolId: str
    DryRun: Optional[bool] = None

class DeleteCoipPoolRequestRequestTypeDef(BaseModel):
    CoipPoolId: str
    DryRun: Optional[bool] = None

class DeleteCustomerGatewayRequestRequestTypeDef(BaseModel):
    CustomerGatewayId: str
    DryRun: Optional[bool] = None

class DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteDhcpOptionsRequestRequestTypeDef(BaseModel):
    DhcpOptionsId: str
    DryRun: Optional[bool] = None

class DeleteEgressOnlyInternetGatewayRequestRequestTypeDef(BaseModel):
    EgressOnlyInternetGatewayId: str
    DryRun: Optional[bool] = None

class DeleteFleetErrorTypeDef(BaseModel):
    Code: Optional[DeleteFleetErrorCodeType] = None
    Message: Optional[str] = None

class DeleteFleetSuccessItemTypeDef(BaseModel):
    CurrentFleetState: Optional[FleetStateCodeType] = None
    PreviousFleetState: Optional[FleetStateCodeType] = None
    FleetId: Optional[str] = None

class DeleteFleetsRequestRequestTypeDef(BaseModel):
    FleetIds: Sequence[str]
    TerminateInstances: bool
    DryRun: Optional[bool] = None

class DeleteFlowLogsRequestRequestTypeDef(BaseModel):
    FlowLogIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteFpgaImageRequestRequestTypeDef(BaseModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None

class DeleteInstanceConnectEndpointRequestRequestTypeDef(BaseModel):
    InstanceConnectEndpointId: str
    DryRun: Optional[bool] = None

class DeleteInstanceEventWindowRequestRequestTypeDef(BaseModel):
    InstanceEventWindowId: str
    DryRun: Optional[bool] = None
    ForceDelete: Optional[bool] = None

class InstanceEventWindowStateChangeTypeDef(BaseModel):
    InstanceEventWindowId: Optional[str] = None
    State: Optional[InstanceEventWindowStateType] = None

class DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteInternetGatewayRequestRequestTypeDef(BaseModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None

class DeleteIpamPoolRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cascade: Optional[bool] = None

class DeleteIpamRequestRequestTypeDef(BaseModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Cascade: Optional[bool] = None

class DeleteIpamResourceDiscoveryRequestRequestTypeDef(BaseModel):
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None

class DeleteIpamScopeRequestRequestTypeDef(BaseModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None

class DeleteKeyPairRequestKeyPairDeleteTypeDef(BaseModel):
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteKeyPairRequestKeyPairInfoDeleteTypeDef(BaseModel):
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteKeyPairRequestRequestTypeDef(BaseModel):
    KeyName: Optional[str] = None
    KeyPairId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteLaunchTemplateRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None

class DeleteLaunchTemplateVersionsRequestRequestTypeDef(BaseModel):
    Versions: Sequence[str]
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None

class ResponseErrorTypeDef(BaseModel):
    Code: Optional[LaunchTemplateErrorCodeType] = None
    Message: Optional[str] = None

class DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None

class DeleteLocalGatewayRouteRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationPrefixListId: Optional[str] = None

class DeleteLocalGatewayRouteTableRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    DryRun: Optional[bool] = None

class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str
    DryRun: Optional[bool] = None

class DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableVpcAssociationId: str
    DryRun: Optional[bool] = None

class DeleteManagedPrefixListRequestRequestTypeDef(BaseModel):
    PrefixListId: str
    DryRun: Optional[bool] = None

class DeleteNatGatewayRequestRequestTypeDef(BaseModel):
    NatGatewayId: str
    DryRun: Optional[bool] = None

class DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef(BaseModel):
    Egress: bool
    RuleNumber: int
    DryRun: Optional[bool] = None

class DeleteNetworkAclEntryRequestRequestTypeDef(BaseModel):
    Egress: bool
    NetworkAclId: str
    RuleNumber: int
    DryRun: Optional[bool] = None

class DeleteNetworkAclRequestNetworkAclDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteNetworkAclRequestRequestTypeDef(BaseModel):
    NetworkAclId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsAccessScopeRequestRequestTypeDef(BaseModel):
    NetworkInsightsAccessScopeId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsAnalysisRequestRequestTypeDef(BaseModel):
    NetworkInsightsAnalysisId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInsightsPathRequestRequestTypeDef(BaseModel):
    NetworkInsightsPathId: str
    DryRun: Optional[bool] = None

class DeleteNetworkInterfacePermissionRequestRequestTypeDef(BaseModel):
    NetworkInterfacePermissionId: str
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None

class DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteNetworkInterfaceRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None

class DeletePlacementGroupRequestPlacementGroupDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeletePlacementGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    DryRun: Optional[bool] = None

class DeletePublicIpv4PoolRequestRequestTypeDef(BaseModel):
    PoolId: str
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class DeleteQueuedReservedInstancesErrorTypeDef(BaseModel):
    Code: Optional[DeleteQueuedReservedInstancesErrorCodeType] = None
    Message: Optional[str] = None

class DeleteQueuedReservedInstancesRequestRequestTypeDef(BaseModel):
    ReservedInstancesIds: Sequence[str]
    DryRun: Optional[bool] = None

class SuccessfulQueuedPurchaseDeletionTypeDef(BaseModel):
    ReservedInstancesId: Optional[str] = None

class DeleteRouteRequestRequestTypeDef(BaseModel):
    RouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteRouteRequestRouteDeleteTypeDef(BaseModel):
    DestinationIpv6CidrBlock: Optional[str] = None
    DestinationPrefixListId: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteRouteTableRequestRequestTypeDef(BaseModel):
    RouteTableId: str
    DryRun: Optional[bool] = None

class DeleteRouteTableRequestRouteTableDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteSecurityGroupRequestRequestTypeDef(BaseModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef(BaseModel):
    GroupName: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteSnapshotRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    DryRun: Optional[bool] = None

class DeleteSnapshotRequestSnapshotDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteSpotDatafeedSubscriptionRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteSubnetCidrReservationRequestRequestTypeDef(BaseModel):
    SubnetCidrReservationId: str
    DryRun: Optional[bool] = None

class DeleteSubnetRequestRequestTypeDef(BaseModel):
    SubnetId: str
    DryRun: Optional[bool] = None

class DeleteSubnetRequestSubnetDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteTagsRequestTagDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorFilterRequestRequestTypeDef(BaseModel):
    TrafficMirrorFilterId: str
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorFilterRuleRequestRequestTypeDef(BaseModel):
    TrafficMirrorFilterRuleId: str
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorSessionRequestRequestTypeDef(BaseModel):
    TrafficMirrorSessionId: str
    DryRun: Optional[bool] = None

class DeleteTrafficMirrorTargetRequestRequestTypeDef(BaseModel):
    TrafficMirrorTargetId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayConnectPeerRequestRequestTypeDef(BaseModel):
    TransitGatewayConnectPeerId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayConnectRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayMulticastDomainRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayPolicyTableRequestRequestTypeDef(BaseModel):
    TransitGatewayPolicyTableId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRequestRequestTypeDef(BaseModel):
    TransitGatewayId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRouteRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    DestinationCidrBlock: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableAnnouncementId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayRouteTableRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    DryRun: Optional[bool] = None

class DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DeleteVerifiedAccessEndpointRequestRequestTypeDef(BaseModel):
    VerifiedAccessEndpointId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteVerifiedAccessGroupRequestRequestTypeDef(BaseModel):
    VerifiedAccessGroupId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DeleteVerifiedAccessInstanceRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceId: str
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class DeleteVerifiedAccessTrustProviderRequestRequestTypeDef(BaseModel):
    VerifiedAccessTrustProviderId: str
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class DeleteVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    DryRun: Optional[bool] = None

class DeleteVolumeRequestVolumeDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef(BaseModel):
    ConnectionNotificationIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef(BaseModel):
    ServiceIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteVpcEndpointsRequestRequestTypeDef(BaseModel):
    VpcEndpointIds: Sequence[str]
    DryRun: Optional[bool] = None

class DeleteVpcPeeringConnectionRequestRequestTypeDef(BaseModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None

class DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteVpcRequestRequestTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DeleteVpcRequestVpcDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeleteVpnConnectionRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    DryRun: Optional[bool] = None

class DeleteVpnConnectionRouteRequestRequestTypeDef(BaseModel):
    DestinationCidrBlock: str
    VpnConnectionId: str

class DeleteVpnGatewayRequestRequestTypeDef(BaseModel):
    VpnGatewayId: str
    DryRun: Optional[bool] = None

class DeprovisionByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str
    DryRun: Optional[bool] = None

class DeprovisionIpamByoasnRequestRequestTypeDef(BaseModel):
    IpamId: str
    Asn: str
    DryRun: Optional[bool] = None

class DeprovisionIpamPoolCidrRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None

class DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef(BaseModel):
    PoolId: str
    Cidr: str
    DryRun: Optional[bool] = None

class DeregisterImageRequestImageDeregisterTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DeregisterImageRequestRequestTypeDef(BaseModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DeregisterInstanceTagAttributeRequestTypeDef(BaseModel):
    IncludeAllTagsOfInstance: Optional[bool] = None
    InstanceTagKeys: Optional[Sequence[str]] = None

class InstanceTagNotificationAttributeTypeDef(BaseModel):
    InstanceTagKeys: Optional[List[str]] = None
    IncludeAllTagsOfInstance: Optional[bool] = None

class DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    GroupIpAddress: Optional[str] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastDeregisteredGroupMembersTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    DeregisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    GroupIpAddress: Optional[str] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastDeregisteredGroupSourcesTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    DeregisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class DescribeAccountAttributesRequestRequestTypeDef(BaseModel):
    AttributeNames: Optional[Sequence[AccountAttributeNameType]] = None
    DryRun: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAddressTransfersRequestRequestTypeDef(BaseModel):
    AllocationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class DescribeAddressesAttributeRequestRequestTypeDef(BaseModel):
    AllocationIds: Optional[Sequence[str]] = None
    Attribute: Optional[Literal["domain-name"]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class FilterTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DescribeAggregateIdFormatRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class IdFormatTypeDef(BaseModel):
    Deadline: Optional[datetime] = None
    Resource: Optional[str] = None
    UseLongIds: Optional[bool] = None

class SubscriptionTypeDef(BaseModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    Period: Optional[PeriodTypeType] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeByoipCidrsRequestRequestTypeDef(BaseModel):
    MaxResults: int
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeConversionTasksRequestRequestTypeDef(BaseModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class FastLaunchLaunchTemplateSpecificationResponseTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class FastLaunchSnapshotConfigurationResponseTypeDef(BaseModel):
    TargetResourceCount: Optional[int] = None

class DescribeFastSnapshotRestoreSuccessItemTypeDef(BaseModel):
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

class DescribeFpgaImageAttributeRequestRequestTypeDef(BaseModel):
    FpgaImageId: str
    Attribute: FpgaImageAttributeNameType
    DryRun: Optional[bool] = None

class HostOfferingTypeDef(BaseModel):
    CurrencyCode: Optional[Literal["USD"]] = None
    Duration: Optional[int] = None
    HourlyPrice: Optional[str] = None
    InstanceFamily: Optional[str] = None
    OfferingId: Optional[str] = None
    PaymentOption: Optional[PaymentOptionType] = None
    UpfrontPrice: Optional[str] = None

class DescribeIdFormatRequestRequestTypeDef(BaseModel):
    Resource: Optional[str] = None

class DescribeIdentityIdFormatRequestRequestTypeDef(BaseModel):
    PrincipalArn: str
    Resource: Optional[str] = None

class DescribeImageAttributeRequestImageDescribeAttributeTypeDef(BaseModel):
    Attribute: ImageAttributeNameType
    DryRun: Optional[bool] = None

class DescribeImageAttributeRequestRequestTypeDef(BaseModel):
    Attribute: ImageAttributeNameType
    ImageId: str
    DryRun: Optional[bool] = None

class DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef(BaseModel):
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None

class DescribeInstanceAttributeRequestRequestTypeDef(BaseModel):
    Attribute: InstanceAttributeNameType
    InstanceId: str
    DryRun: Optional[bool] = None

class InstanceCreditSpecificationTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    CpuCredits: Optional[str] = None

class DescribeInstanceEventNotificationAttributesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class InstanceTopologyTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    GroupName: Optional[str] = None
    NetworkNodes: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None
    ZoneId: Optional[str] = None

class InstanceTypeOfferingTypeDef(BaseModel):
    InstanceType: Optional[InstanceTypeType] = None
    LocationType: Optional[LocationTypeType] = None
    Location: Optional[str] = None

class DescribeIpamByoasnRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LockedSnapshotsInfoTypeDef(BaseModel):
    OwnerId: Optional[str] = None
    SnapshotId: Optional[str] = None
    LockState: Optional[LockStateType] = None
    LockDuration: Optional[int] = None
    CoolOffPeriod: Optional[int] = None
    CoolOffPeriodExpiresOn: Optional[datetime] = None
    LockCreatedOn: Optional[datetime] = None
    LockDurationStartTime: Optional[datetime] = None
    LockExpiresOn: Optional[datetime] = None

class MacHostTypeDef(BaseModel):
    HostId: Optional[str] = None
    MacOSLatestSupportedVersions: Optional[List[str]] = None

class MovingAddressStatusTypeDef(BaseModel):
    MoveStatus: Optional[MoveStatusType] = None
    PublicIp: Optional[str] = None

class DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef(BaseModel):
    Attribute: Optional[NetworkInterfaceAttributeType] = None
    DryRun: Optional[bool] = None

class DescribeNetworkInterfaceAttributeRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    Attribute: Optional[NetworkInterfaceAttributeType] = None
    DryRun: Optional[bool] = None

class PrefixListTypeDef(BaseModel):
    Cidrs: Optional[List[str]] = None
    PrefixListId: Optional[str] = None
    PrefixListName: Optional[str] = None

class DescribePrincipalIdFormatRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Resources: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RegionTypeDef(BaseModel):
    Endpoint: Optional[str] = None
    RegionName: Optional[str] = None
    OptInStatus: Optional[str] = None

class ScheduledInstanceRecurrenceRequestTypeDef(BaseModel):
    Frequency: Optional[str] = None
    Interval: Optional[int] = None
    OccurrenceDays: Optional[Sequence[int]] = None
    OccurrenceRelativeToEnd: Optional[bool] = None
    OccurrenceUnit: Optional[str] = None

class DescribeSecurityGroupReferencesRequestRequestTypeDef(BaseModel):
    GroupId: Sequence[str]
    DryRun: Optional[bool] = None

class SecurityGroupReferenceTypeDef(BaseModel):
    GroupId: Optional[str] = None
    ReferencingVpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None
    TransitGatewayId: Optional[str] = None

class DescribeSnapshotAttributeRequestRequestTypeDef(BaseModel):
    Attribute: SnapshotAttributeNameType
    SnapshotId: str
    DryRun: Optional[bool] = None

class DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef(BaseModel):
    Attribute: SnapshotAttributeNameType
    DryRun: Optional[bool] = None

class ProductCodeTypeDef(BaseModel):
    ProductCodeId: Optional[str] = None
    ProductCodeType: Optional[ProductCodeValuesType] = None

class DescribeSpotDatafeedSubscriptionRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DescribeSpotFleetInstancesRequestRequestTypeDef(BaseModel):
    SpotFleetRequestId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SpotFleetRequestIds: Optional[Sequence[str]] = None

class SpotPriceTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    InstanceType: Optional[InstanceTypeType] = None
    ProductDescription: Optional[RIProductDescriptionType] = None
    SpotPrice: Optional[str] = None
    Timestamp: Optional[datetime] = None

class DescribeStaleSecurityGroupsRequestRequestTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class StoreImageTaskResultTypeDef(BaseModel):
    AmiId: Optional[str] = None
    TaskStartTime: Optional[datetime] = None
    Bucket: Optional[str] = None
    S3objectKey: Optional[str] = None
    ProgressPercentage: Optional[int] = None
    StoreTaskState: Optional[str] = None
    StoreTaskFailureReason: Optional[str] = None

class TagDescriptionTypeDef(BaseModel):
    Key: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[ResourceTypeType] = None
    Value: Optional[str] = None

class DescribeVolumeAttributeRequestRequestTypeDef(BaseModel):
    Attribute: VolumeAttributeNameType
    VolumeId: str
    DryRun: Optional[bool] = None

class DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef(BaseModel):
    Attribute: VolumeAttributeNameType
    DryRun: Optional[bool] = None

class VolumeModificationTypeDef(BaseModel):
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

class DescribeVpcAttributeRequestRequestTypeDef(BaseModel):
    Attribute: VpcAttributeNameType
    VpcId: str
    DryRun: Optional[bool] = None

class DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef(BaseModel):
    Attribute: VpcAttributeNameType
    DryRun: Optional[bool] = None

class DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VpcIds: Optional[Sequence[str]] = None

class DestinationOptionsResponseTypeDef(BaseModel):
    FileFormat: Optional[DestinationFileFormatType] = None
    HiveCompatiblePartitions: Optional[bool] = None
    PerHourPartition: Optional[bool] = None

class DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DetachClassicLinkVpcRequestRequestTypeDef(BaseModel):
    InstanceId: str
    VpcId: str
    DryRun: Optional[bool] = None

class DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DetachInternetGatewayRequestRequestTypeDef(BaseModel):
    InternetGatewayId: str
    VpcId: str
    DryRun: Optional[bool] = None

class DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef(BaseModel):
    InternetGatewayId: str
    DryRun: Optional[bool] = None

class DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef(BaseModel):
    AttachmentId: str
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class DetachNetworkInterfaceRequestRequestTypeDef(BaseModel):
    AttachmentId: str
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class DetachVerifiedAccessTrustProviderRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceId: str
    VerifiedAccessTrustProviderId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DetachVolumeRequestInstanceDetachVolumeTypeDef(BaseModel):
    VolumeId: str
    Device: Optional[str] = None
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None

class DetachVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    Device: Optional[str] = None
    Force: Optional[bool] = None
    InstanceId: Optional[str] = None
    DryRun: Optional[bool] = None

class DetachVolumeRequestVolumeDetachFromInstanceTypeDef(BaseModel):
    Device: Optional[str] = None
    Force: Optional[bool] = None
    InstanceId: Optional[str] = None
    DryRun: Optional[bool] = None

class DetachVpnGatewayRequestRequestTypeDef(BaseModel):
    VpcId: str
    VpnGatewayId: str
    DryRun: Optional[bool] = None

class DeviceOptionsTypeDef(BaseModel):
    TenantId: Optional[str] = None
    PublicSigningKeyUrl: Optional[str] = None

class DisableAddressTransferRequestRequestTypeDef(BaseModel):
    AllocationId: str
    DryRun: Optional[bool] = None

class DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef(BaseModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    DryRun: Optional[bool] = None

class DisableEbsEncryptionByDefaultRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DisableFastLaunchRequestRequestTypeDef(BaseModel):
    ImageId: str
    Force: Optional[bool] = None
    DryRun: Optional[bool] = None

class DisableFastSnapshotRestoreStateErrorTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class DisableFastSnapshotRestoreSuccessItemTypeDef(BaseModel):
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

class DisableFastSnapshotRestoresRequestRequestTypeDef(BaseModel):
    AvailabilityZones: Sequence[str]
    SourceSnapshotIds: Sequence[str]
    DryRun: Optional[bool] = None

class DisableImageBlockPublicAccessRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DisableImageDeprecationRequestRequestTypeDef(BaseModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DisableImageDeregistrationProtectionRequestRequestTypeDef(BaseModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DisableImageRequestRequestTypeDef(BaseModel):
    ImageId: str
    DryRun: Optional[bool] = None

class DisableIpamOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    DelegatedAdminAccountId: str
    DryRun: Optional[bool] = None

class DisableSerialConsoleAccessRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DisableSnapshotBlockPublicAccessRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    DryRun: Optional[bool] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class TransitGatewayPropagationTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayPropagationStateType] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class DisableVgwRoutePropagationRequestRequestTypeDef(BaseModel):
    GatewayId: str
    RouteTableId: str
    DryRun: Optional[bool] = None

class DisableVpcClassicLinkDnsSupportRequestRequestTypeDef(BaseModel):
    VpcId: Optional[str] = None

class DisableVpcClassicLinkRequestRequestTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None

class DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DisassociateAddressRequestClassicAddressDisassociateTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef(BaseModel):
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateAddressRequestRequestTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    PublicIp: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateClientVpnTargetNetworkRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    AssociationId: str
    DryRun: Optional[bool] = None

class DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    RoleArn: str
    DryRun: Optional[bool] = None

class DisassociateIamInstanceProfileRequestRequestTypeDef(BaseModel):
    AssociationId: str

class DisassociateIpamByoasnRequestRequestTypeDef(BaseModel):
    Asn: str
    Cidr: str
    DryRun: Optional[bool] = None

class DisassociateIpamResourceDiscoveryRequestRequestTypeDef(BaseModel):
    IpamResourceDiscoveryAssociationId: str
    DryRun: Optional[bool] = None

class DisassociateNatGatewayAddressRequestRequestTypeDef(BaseModel):
    NatGatewayId: str
    AssociationIds: Sequence[str]
    MaxDrainDurationSeconds: Optional[int] = None
    DryRun: Optional[bool] = None

class DisassociateRouteTableRequestRequestTypeDef(BaseModel):
    AssociationId: str
    DryRun: Optional[bool] = None

class DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef(BaseModel):
    AssociationId: str
    DryRun: Optional[bool] = None

class DisassociateSubnetCidrBlockRequestRequestTypeDef(BaseModel):
    AssociationId: str

class DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    TransitGatewayAttachmentId: str
    SubnetIds: Sequence[str]
    DryRun: Optional[bool] = None

class DisassociateTransitGatewayPolicyTableRequestRequestTypeDef(BaseModel):
    TransitGatewayPolicyTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DisassociateTransitGatewayRouteTableRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class DisassociateTrunkInterfaceRequestRequestTypeDef(BaseModel):
    AssociationId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DisassociateVpcCidrBlockRequestRequestTypeDef(BaseModel):
    AssociationId: str

class DiskImageDescriptionTypeDef(BaseModel):
    Checksum: Optional[str] = None
    Format: Optional[DiskImageFormatType] = None
    ImportManifestUrl: Optional[str] = None
    Size: Optional[int] = None

class DiskImageDetailTypeDef(BaseModel):
    Bytes: int
    Format: DiskImageFormatType
    ImportManifestUrl: str

class VolumeDetailTypeDef(BaseModel):
    Size: int

class DiskImageVolumeDescriptionTypeDef(BaseModel):
    Id: Optional[str] = None
    Size: Optional[int] = None

class DiskInfoTypeDef(BaseModel):
    SizeInGB: Optional[int] = None
    Count: Optional[int] = None
    Type: Optional[DiskTypeType] = None

class DnsEntryTypeDef(BaseModel):
    DnsName: Optional[str] = None
    HostedZoneId: Optional[str] = None

class DnsOptionsTypeDef(BaseModel):
    DnsRecordIpType: Optional[DnsRecordIpTypeType] = None
    PrivateDnsOnlyForInboundResolverEndpoint: Optional[bool] = None

class DnsServersOptionsModifyStructureTypeDef(BaseModel):
    CustomDnsServers: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class EbsOptimizedInfoTypeDef(BaseModel):
    BaselineBandwidthInMbps: Optional[int] = None
    BaselineThroughputInMBps: Optional[float] = None
    BaselineIops: Optional[int] = None
    MaximumBandwidthInMbps: Optional[int] = None
    MaximumThroughputInMBps: Optional[float] = None
    MaximumIops: Optional[int] = None

class EbsInstanceBlockDeviceSpecificationTypeDef(BaseModel):
    DeleteOnTermination: Optional[bool] = None
    VolumeId: Optional[str] = None

class EbsInstanceBlockDeviceTypeDef(BaseModel):
    AttachTime: Optional[datetime] = None
    DeleteOnTermination: Optional[bool] = None
    Status: Optional[AttachmentStatusType] = None
    VolumeId: Optional[str] = None
    AssociatedResource: Optional[str] = None
    VolumeOwnerId: Optional[str] = None

class EfaInfoTypeDef(BaseModel):
    MaximumEfaInterfaces: Optional[int] = None

class InternetGatewayAttachmentTypeDef(BaseModel):
    State: Optional[AttachmentStatusType] = None
    VpcId: Optional[str] = None

class ElasticGpuAssociationTypeDef(BaseModel):
    ElasticGpuId: Optional[str] = None
    ElasticGpuAssociationId: Optional[str] = None
    ElasticGpuAssociationState: Optional[str] = None
    ElasticGpuAssociationTime: Optional[str] = None

class ElasticGpuHealthTypeDef(BaseModel):
    Status: Optional[ElasticGpuStatusType] = None

class ElasticGpuSpecificationResponseTypeDef(BaseModel):
    Type: Optional[str] = None

class ElasticGpuSpecificationTypeDef(BaseModel):
    Type: str

class ElasticInferenceAcceleratorAssociationTypeDef(BaseModel):
    ElasticInferenceAcceleratorArn: Optional[str] = None
    ElasticInferenceAcceleratorAssociationId: Optional[str] = None
    ElasticInferenceAcceleratorAssociationState: Optional[str] = None
    ElasticInferenceAcceleratorAssociationTime: Optional[datetime] = None

class ElasticInferenceAcceleratorTypeDef(BaseModel):
    Type: str
    Count: Optional[int] = None

class EnaSrdUdpSpecificationRequestTypeDef(BaseModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class EnaSrdUdpSpecificationTypeDef(BaseModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class EnableAddressTransferRequestRequestTypeDef(BaseModel):
    AllocationId: str
    TransferAccountId: str
    DryRun: Optional[bool] = None

class EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef(BaseModel):
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    DryRun: Optional[bool] = None

class EnableEbsEncryptionByDefaultRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class FastLaunchLaunchTemplateSpecificationRequestTypeDef(BaseModel):
    Version: str
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None

class FastLaunchSnapshotConfigurationRequestTypeDef(BaseModel):
    TargetResourceCount: Optional[int] = None

class EnableFastSnapshotRestoreStateErrorTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class EnableFastSnapshotRestoreSuccessItemTypeDef(BaseModel):
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

class EnableFastSnapshotRestoresRequestRequestTypeDef(BaseModel):
    AvailabilityZones: Sequence[str]
    SourceSnapshotIds: Sequence[str]
    DryRun: Optional[bool] = None

class EnableImageBlockPublicAccessRequestRequestTypeDef(BaseModel):
    ImageBlockPublicAccessState: Literal["block-new-sharing"]
    DryRun: Optional[bool] = None

class EnableImageDeregistrationProtectionRequestRequestTypeDef(BaseModel):
    ImageId: str
    WithCooldown: Optional[bool] = None
    DryRun: Optional[bool] = None

class EnableImageRequestRequestTypeDef(BaseModel):
    ImageId: str
    DryRun: Optional[bool] = None

class EnableIpamOrganizationAdminAccountRequestRequestTypeDef(BaseModel):
    DelegatedAdminAccountId: str
    DryRun: Optional[bool] = None

class EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class EnableSerialConsoleAccessRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class EnableSnapshotBlockPublicAccessRequestRequestTypeDef(BaseModel):
    State: SnapshotBlockPublicAccessStateType
    DryRun: Optional[bool] = None

class EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    DryRun: Optional[bool] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class EnableVgwRoutePropagationRequestRequestTypeDef(BaseModel):
    GatewayId: str
    RouteTableId: str
    DryRun: Optional[bool] = None

class EnableVolumeIORequestRequestTypeDef(BaseModel):
    VolumeId: str
    DryRun: Optional[bool] = None

class EnableVolumeIORequestVolumeEnableIoTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class EnableVpcClassicLinkDnsSupportRequestRequestTypeDef(BaseModel):
    VpcId: Optional[str] = None

class EnableVpcClassicLinkRequestRequestTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None

class EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class EnclaveOptionsRequestTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class EnclaveOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class EventInformationTypeDef(BaseModel):
    EventDescription: Optional[str] = None
    EventSubType: Optional[str] = None
    InstanceId: Optional[str] = None

class TransitGatewayRouteTableRouteTypeDef(BaseModel):
    DestinationCidr: Optional[str] = None
    State: Optional[str] = None
    RouteOrigin: Optional[str] = None
    PrefixListId: Optional[str] = None
    AttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[str] = None

class ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None

class ExportClientVpnClientConfigurationRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None

class ExportTaskS3LocationRequestTypeDef(BaseModel):
    S3Bucket: str
    S3Prefix: Optional[str] = None

class ExportTaskS3LocationTypeDef(BaseModel):
    S3Bucket: Optional[str] = None
    S3Prefix: Optional[str] = None

class ExportToS3TaskTypeDef(BaseModel):
    ContainerFormat: Optional[Literal["ova"]] = None
    DiskImageFormat: Optional[DiskImageFormatType] = None
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None

class InstanceExportDetailsTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    TargetEnvironment: Optional[ExportEnvironmentType] = None

class FilterPortRangeTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class TargetCapacitySpecificationTypeDef(BaseModel):
    TotalTargetCapacity: Optional[int] = None
    OnDemandTargetCapacity: Optional[int] = None
    SpotTargetCapacity: Optional[int] = None
    DefaultTargetCapacityType: Optional[DefaultTargetCapacityTypeType] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None

class FleetLaunchTemplateSpecificationRequestTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class FleetLaunchTemplateSpecificationTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class PlacementTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    PartitionNumber: Optional[int] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    GroupId: Optional[str] = None

class PlacementResponseTypeDef(BaseModel):
    GroupName: Optional[str] = None

class FleetSpotCapacityRebalanceRequestTypeDef(BaseModel):
    ReplacementStrategy: Optional[FleetReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None

class FleetSpotCapacityRebalanceTypeDef(BaseModel):
    ReplacementStrategy: Optional[FleetReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None

class FpgaDeviceMemoryInfoTypeDef(BaseModel):
    SizeInMiB: Optional[int] = None

class LoadPermissionTypeDef(BaseModel):
    UserId: Optional[str] = None
    Group: Optional[Literal["all"]] = None

class FpgaImageStateTypeDef(BaseModel):
    Code: Optional[FpgaImageStateCodeType] = None
    Message: Optional[str] = None

class PciIdTypeDef(BaseModel):
    DeviceId: Optional[str] = None
    VendorId: Optional[str] = None
    SubsystemId: Optional[str] = None
    SubsystemVendorId: Optional[str] = None

class GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef(BaseModel):
    CertificateArn: str
    DryRun: Optional[bool] = None

class GetAssociatedIpv6PoolCidrsRequestRequestTypeDef(BaseModel):
    PoolId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class Ipv6CidrAssociationTypeDef(BaseModel):
    Ipv6Cidr: Optional[str] = None
    AssociatedResource: Optional[str] = None

class GetCapacityReservationUsageRequestRequestTypeDef(BaseModel):
    CapacityReservationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class InstanceUsageTypeDef(BaseModel):
    AccountId: Optional[str] = None
    UsedInstanceCount: Optional[int] = None

class GetConsoleOutputRequestInstanceConsoleOutputTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Latest: Optional[bool] = None

class GetConsoleOutputRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    Latest: Optional[bool] = None

class GetConsoleScreenshotRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    WakeUp: Optional[bool] = None

class GetDefaultCreditSpecificationRequestRequestTypeDef(BaseModel):
    InstanceFamily: UnlimitedSupportedInstanceFamilyType
    DryRun: Optional[bool] = None

class InstanceFamilyCreditSpecificationTypeDef(BaseModel):
    InstanceFamily: Optional[UnlimitedSupportedInstanceFamilyType] = None
    CpuCredits: Optional[str] = None

class GetEbsDefaultKmsKeyIdRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class GetEbsEncryptionByDefaultRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class GetGroupsForCapacityReservationRequestRequestTypeDef(BaseModel):
    CapacityReservationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class GetHostReservationPurchasePreviewRequestRequestTypeDef(BaseModel):
    HostIdSet: Sequence[str]
    OfferingId: str

class PurchaseTypeDef(BaseModel):
    CurrencyCode: Optional[Literal["USD"]] = None
    Duration: Optional[int] = None
    HostIdSet: Optional[List[str]] = None
    HostReservationId: Optional[str] = None
    HourlyPrice: Optional[str] = None
    InstanceFamily: Optional[str] = None
    PaymentOption: Optional[PaymentOptionType] = None
    UpfrontPrice: Optional[str] = None

class GetImageBlockPublicAccessStateRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class GetInstanceMetadataDefaultsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class InstanceMetadataDefaultsResponseTypeDef(BaseModel):
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class GetInstanceTpmEkPubRequestRequestTypeDef(BaseModel):
    InstanceId: str
    KeyType: EkPubKeyTypeType
    KeyFormat: EkPubKeyFormatType
    DryRun: Optional[bool] = None

class InstanceTypeInfoFromInstanceRequirementsTypeDef(BaseModel):
    InstanceType: Optional[str] = None

class GetInstanceUefiDataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class IpamAddressHistoryRecordTypeDef(BaseModel):
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

class GetLaunchTemplateDataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class GetManagedPrefixListAssociationsRequestRequestTypeDef(BaseModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrefixListAssociationTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    ResourceOwner: Optional[str] = None

class GetManagedPrefixListEntriesRequestRequestTypeDef(BaseModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    TargetVersion: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class PrefixListEntryTypeDef(BaseModel):
    Cidr: Optional[str] = None
    Description: Optional[str] = None

class GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetNetworkInsightsAccessScopeContentRequestRequestTypeDef(BaseModel):
    NetworkInsightsAccessScopeId: str
    DryRun: Optional[bool] = None

class GetPasswordDataRequestInstancePasswordDataTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class GetPasswordDataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class ReservationValueTypeDef(BaseModel):
    HourlyPrice: Optional[str] = None
    RemainingTotalValue: Optional[str] = None
    RemainingUpfrontValue: Optional[str] = None

class GetSerialConsoleAccessStatusRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class GetSnapshotBlockPublicAccessStateRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class SpotPlacementScoreTypeDef(BaseModel):
    Region: Optional[str] = None
    AvailabilityZoneId: Optional[str] = None
    Score: Optional[int] = None

class TransitGatewayAttachmentPropagationTypeDef(BaseModel):
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayPropagationStateType] = None

class TransitGatewayRouteTableAssociationTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class TransitGatewayRouteTablePropagationTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    State: Optional[TransitGatewayPropagationStateType] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None

class GetVerifiedAccessEndpointPolicyRequestRequestTypeDef(BaseModel):
    VerifiedAccessEndpointId: str
    DryRun: Optional[bool] = None

class GetVerifiedAccessGroupPolicyRequestRequestTypeDef(BaseModel):
    VerifiedAccessGroupId: str
    DryRun: Optional[bool] = None

class GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    VpnConnectionDeviceTypeId: str
    InternetKeyExchangeVersion: Optional[str] = None
    DryRun: Optional[bool] = None

class GetVpnConnectionDeviceTypesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class VpnConnectionDeviceTypeTypeDef(BaseModel):
    VpnConnectionDeviceTypeId: Optional[str] = None
    Vendor: Optional[str] = None
    Platform: Optional[str] = None
    Software: Optional[str] = None

class GetVpnTunnelReplacementStatusRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    DryRun: Optional[bool] = None

class MaintenanceDetailsTypeDef(BaseModel):
    PendingMaintenance: Optional[str] = None
    MaintenanceAutoAppliedAfter: Optional[datetime] = None
    LastMaintenanceApplied: Optional[datetime] = None

class GpuDeviceMemoryInfoTypeDef(BaseModel):
    SizeInMiB: Optional[int] = None

class HibernationOptionsRequestTypeDef(BaseModel):
    Configured: Optional[bool] = None

class HibernationOptionsTypeDef(BaseModel):
    Configured: Optional[bool] = None

class HostInstanceTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    InstanceType: Optional[str] = None
    OwnerId: Optional[str] = None

class HostPropertiesTypeDef(BaseModel):
    Cores: Optional[int] = None
    InstanceType: Optional[str] = None
    InstanceFamily: Optional[str] = None
    Sockets: Optional[int] = None
    TotalVCpus: Optional[int] = None

class IKEVersionsListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class IKEVersionsRequestListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class IamInstanceProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None

class LaunchPermissionTypeDef(BaseModel):
    Group: Optional[Literal["all"]] = None
    UserId: Optional[str] = None
    OrganizationArn: Optional[str] = None
    OrganizationalUnitArn: Optional[str] = None

class UserBucketTypeDef(BaseModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None

class ImageRecycleBinInfoTypeDef(BaseModel):
    ImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    RecycleBinEnterTime: Optional[datetime] = None
    RecycleBinExitTime: Optional[datetime] = None

class StateReasonTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    CertificateRevocationList: str
    DryRun: Optional[bool] = None

class ImportImageLicenseConfigurationRequestTypeDef(BaseModel):
    LicenseConfigurationArn: Optional[str] = None

class ImportImageLicenseConfigurationResponseTypeDef(BaseModel):
    LicenseConfigurationArn: Optional[str] = None

class UserDataTypeDef(BaseModel):
    Data: Optional[str] = None

class InferenceDeviceMemoryInfoTypeDef(BaseModel):
    SizeInMiB: Optional[int] = None

class InstanceAttachmentEnaSrdUdpSpecificationTypeDef(BaseModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class InstanceCountTypeDef(BaseModel):
    InstanceCount: Optional[int] = None
    State: Optional[ListingStateType] = None

class InstanceCreditSpecificationRequestTypeDef(BaseModel):
    InstanceId: str
    CpuCredits: Optional[str] = None

class InstanceEventWindowTimeRangeTypeDef(BaseModel):
    StartWeekDay: Optional[WeekDayType] = None
    StartHour: Optional[int] = None
    EndWeekDay: Optional[WeekDayType] = None
    EndHour: Optional[int] = None

class InstanceIpv4PrefixTypeDef(BaseModel):
    Ipv4Prefix: Optional[str] = None

class InstanceIpv6AddressRequestTypeDef(BaseModel):
    Ipv6Address: Optional[str] = None

class InstanceIpv6PrefixTypeDef(BaseModel):
    Ipv6Prefix: Optional[str] = None

class InstanceMaintenanceOptionsRequestTypeDef(BaseModel):
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None

class InstanceMaintenanceOptionsTypeDef(BaseModel):
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None

class InstanceMetadataOptionsRequestTypeDef(BaseModel):
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class InstanceMetadataOptionsResponseTypeDef(BaseModel):
    State: Optional[InstanceMetadataOptionsStateType] = None
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class MonitoringTypeDef(BaseModel):
    State: Optional[MonitoringStateType] = None

class InstanceNetworkInterfaceAssociationTypeDef(BaseModel):
    CarrierIp: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    IpOwnerId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None

class MemoryGiBPerVCpuTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class MemoryMiBTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class NetworkBandwidthGbpsTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class NetworkInterfaceCountTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class TotalLocalStorageGBTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class VCpuCountRangeTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class MemoryGiBPerVCpuRequestTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class MemoryMiBRequestTypeDef(BaseModel):
    Min: int
    Max: Optional[int] = None

class NetworkBandwidthGbpsRequestTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class NetworkInterfaceCountRequestTypeDef(BaseModel):
    Min: Optional[int] = None
    Max: Optional[int] = None

class TotalLocalStorageGBRequestTypeDef(BaseModel):
    Min: Optional[float] = None
    Max: Optional[float] = None

class VCpuCountRangeRequestTypeDef(BaseModel):
    Min: int
    Max: Optional[int] = None

class InstanceStateTypeDef(BaseModel):
    Code: Optional[int] = None
    Name: Optional[InstanceStateNameType] = None

class InstanceStatusDetailsTypeDef(BaseModel):
    ImpairedSince: Optional[datetime] = None
    Name: Optional[Literal["reachability"]] = None
    Status: Optional[StatusTypeType] = None

class InstanceStatusEventTypeDef(BaseModel):
    InstanceEventId: Optional[str] = None
    Code: Optional[EventCodeType] = None
    Description: Optional[str] = None
    NotAfter: Optional[datetime] = None
    NotBefore: Optional[datetime] = None
    NotBeforeDeadline: Optional[datetime] = None

class LicenseConfigurationTypeDef(BaseModel):
    LicenseConfigurationArn: Optional[str] = None

class PrivateDnsNameOptionsResponseTypeDef(BaseModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class MemoryInfoTypeDef(BaseModel):
    SizeInMiB: Optional[int] = None

class NitroTpmInfoTypeDef(BaseModel):
    SupportedVersions: Optional[List[str]] = None

class PlacementGroupInfoTypeDef(BaseModel):
    SupportedStrategies: Optional[List[PlacementGroupStrategyType]] = None

class ProcessorInfoTypeDef(BaseModel):
    SupportedArchitectures: Optional[List[ArchitectureTypeType]] = None
    SustainedClockSpeedInGhz: Optional[float] = None
    SupportedFeatures: Optional[List[Literal["amd-sev-snp"]]] = None
    Manufacturer: Optional[str] = None

class VCpuInfoTypeDef(BaseModel):
    DefaultVCpus: Optional[int] = None
    DefaultCores: Optional[int] = None
    DefaultThreadsPerCore: Optional[int] = None
    ValidCores: Optional[List[int]] = None
    ValidThreadsPerCore: Optional[List[int]] = None

class IpRangeTypeDef(BaseModel):
    CidrIp: Optional[str] = None
    Description: Optional[str] = None

class Ipv6RangeTypeDef(BaseModel):
    CidrIpv6: Optional[str] = None
    Description: Optional[str] = None

class PrefixListIdTypeDef(BaseModel):
    Description: Optional[str] = None
    PrefixListId: Optional[str] = None

class UserIdGroupPairTypeDef(BaseModel):
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None

class IpamCidrAuthorizationContextTypeDef(BaseModel):
    Message: Optional[str] = None
    Signature: Optional[str] = None

class IpamDiscoveryFailureReasonTypeDef(BaseModel):
    Code: Optional[IpamDiscoveryFailureCodeType] = None
    Message: Optional[str] = None

class IpamPublicAddressSecurityGroupTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupId: Optional[str] = None

class IpamResourceTagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class IpamOperatingRegionTypeDef(BaseModel):
    RegionName: Optional[str] = None

class IpamPoolCidrFailureReasonTypeDef(BaseModel):
    Code: Optional[IpamPoolCidrFailureCodeType] = None
    Message: Optional[str] = None

class IpamPoolSourceResourceTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    ResourceType: Optional[Literal["vpc"]] = None
    ResourceRegion: Optional[str] = None
    ResourceOwner: Optional[str] = None

class IpamPublicAddressTagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class Ipv4PrefixSpecificationResponseTypeDef(BaseModel):
    Ipv4Prefix: Optional[str] = None

class Ipv6CidrBlockTypeDef(BaseModel):
    Ipv6CidrBlock: Optional[str] = None

class PoolCidrBlockTypeDef(BaseModel):
    Cidr: Optional[str] = None

class Ipv6PrefixSpecificationResponseTypeDef(BaseModel):
    Ipv6Prefix: Optional[str] = None

class Ipv6PrefixSpecificationTypeDef(BaseModel):
    Ipv6Prefix: Optional[str] = None

class LastErrorTypeDef(BaseModel):
    Message: Optional[str] = None
    Code: Optional[str] = None

class RunInstancesMonitoringEnabledTypeDef(BaseModel):
    Enabled: bool

class SpotPlacementTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None
    Tenancy: Optional[TenancyType] = None

class LaunchTemplateEbsBlockDeviceRequestTypeDef(BaseModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Throughput: Optional[int] = None

class LaunchTemplateEbsBlockDeviceTypeDef(BaseModel):
    Encrypted: Optional[bool] = None
    DeleteOnTermination: Optional[bool] = None
    Iops: Optional[int] = None
    KmsKeyId: Optional[str] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Throughput: Optional[int] = None

class LaunchTemplateCpuOptionsRequestTypeDef(BaseModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class LaunchTemplateCpuOptionsTypeDef(BaseModel):
    CoreCount: Optional[int] = None
    ThreadsPerCore: Optional[int] = None
    AmdSevSnp: Optional[AmdSevSnpSpecificationType] = None

class LaunchTemplateElasticInferenceAcceleratorResponseTypeDef(BaseModel):
    Type: Optional[str] = None
    Count: Optional[int] = None

class LaunchTemplateElasticInferenceAcceleratorTypeDef(BaseModel):
    Type: str
    Count: Optional[int] = None

class LaunchTemplateEnaSrdUdpSpecificationTypeDef(BaseModel):
    EnaSrdUdpEnabled: Optional[bool] = None

class LaunchTemplateEnclaveOptionsRequestTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class LaunchTemplateEnclaveOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class LaunchTemplateHibernationOptionsRequestTypeDef(BaseModel):
    Configured: Optional[bool] = None

class LaunchTemplateHibernationOptionsTypeDef(BaseModel):
    Configured: Optional[bool] = None

class LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class LaunchTemplateIamInstanceProfileSpecificationTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef(BaseModel):
    AutoRecovery: Optional[LaunchTemplateAutoRecoveryStateType] = None

class LaunchTemplateInstanceMaintenanceOptionsTypeDef(BaseModel):
    AutoRecovery: Optional[LaunchTemplateAutoRecoveryStateType] = None

class LaunchTemplateSpotMarketOptionsTypeDef(BaseModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[datetime] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class LaunchTemplateInstanceMetadataOptionsRequestTypeDef(BaseModel):
    HttpTokens: Optional[LaunchTemplateHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[LaunchTemplateInstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[LaunchTemplateInstanceMetadataProtocolIpv6Type] = None
    InstanceMetadataTags: Optional[LaunchTemplateInstanceMetadataTagsStateType] = None

class LaunchTemplateInstanceMetadataOptionsTypeDef(BaseModel):
    State: Optional[LaunchTemplateInstanceMetadataOptionsStateType] = None
    HttpTokens: Optional[LaunchTemplateHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[LaunchTemplateInstanceMetadataEndpointStateType] = None
    HttpProtocolIpv6: Optional[LaunchTemplateInstanceMetadataProtocolIpv6Type] = None
    InstanceMetadataTags: Optional[LaunchTemplateInstanceMetadataTagsStateType] = None

class LaunchTemplateLicenseConfigurationRequestTypeDef(BaseModel):
    LicenseConfigurationArn: Optional[str] = None

class LaunchTemplateLicenseConfigurationTypeDef(BaseModel):
    LicenseConfigurationArn: Optional[str] = None

class LaunchTemplatePlacementRequestTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    GroupId: Optional[str] = None

class LaunchTemplatePlacementTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    Affinity: Optional[str] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[TenancyType] = None
    SpreadDomain: Optional[str] = None
    HostResourceGroupArn: Optional[str] = None
    PartitionNumber: Optional[int] = None
    GroupId: Optional[str] = None

class LaunchTemplatePrivateDnsNameOptionsRequestTypeDef(BaseModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class LaunchTemplatePrivateDnsNameOptionsTypeDef(BaseModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class LaunchTemplateSpecificationTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Version: Optional[str] = None

class LaunchTemplatesMonitoringRequestTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class LaunchTemplatesMonitoringTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class LicenseConfigurationRequestTypeDef(BaseModel):
    LicenseConfigurationArn: Optional[str] = None

class ListImagesInRecycleBinRequestRequestTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class ListSnapshotsInRecycleBinRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class SnapshotRecycleBinInfoTypeDef(BaseModel):
    SnapshotId: Optional[str] = None
    RecycleBinEnterTime: Optional[datetime] = None
    RecycleBinExitTime: Optional[datetime] = None
    Description: Optional[str] = None
    VolumeId: Optional[str] = None

class LoadPermissionRequestTypeDef(BaseModel):
    Group: Optional[Literal["all"]] = None
    UserId: Optional[str] = None

class MediaDeviceMemoryInfoTypeDef(BaseModel):
    SizeInMiB: Optional[int] = None

class ModifyAddressAttributeRequestRequestTypeDef(BaseModel):
    AllocationId: str
    DomainName: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyAvailabilityZoneGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    OptInStatus: ModifyAvailabilityZoneOptInStatusType
    DryRun: Optional[bool] = None

class ModifyDefaultCreditSpecificationRequestRequestTypeDef(BaseModel):
    InstanceFamily: UnlimitedSupportedInstanceFamilyType
    CpuCredits: str
    DryRun: Optional[bool] = None

class ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef(BaseModel):
    KmsKeyId: str
    DryRun: Optional[bool] = None

class ModifyHostsRequestRequestTypeDef(BaseModel):
    HostIds: Sequence[str]
    AutoPlacement: Optional[AutoPlacementType] = None
    HostRecovery: Optional[HostRecoveryType] = None
    InstanceType: Optional[str] = None
    InstanceFamily: Optional[str] = None
    HostMaintenance: Optional[HostMaintenanceType] = None

class ModifyIdFormatRequestRequestTypeDef(BaseModel):
    Resource: str
    UseLongIds: bool

class ModifyIdentityIdFormatRequestRequestTypeDef(BaseModel):
    PrincipalArn: str
    Resource: str
    UseLongIds: bool

class SuccessfulInstanceCreditSpecificationItemTypeDef(BaseModel):
    InstanceId: Optional[str] = None

class ModifyInstanceMaintenanceOptionsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AutoRecovery: Optional[InstanceAutoRecoveryStateType] = None
    DryRun: Optional[bool] = None

class ModifyInstanceMetadataDefaultsRequestRequestTypeDef(BaseModel):
    HttpTokens: Optional[MetadataDefaultHttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[DefaultInstanceMetadataEndpointStateType] = None
    InstanceMetadataTags: Optional[DefaultInstanceMetadataTagsStateType] = None
    DryRun: Optional[bool] = None

class ModifyInstanceMetadataOptionsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    HttpTokens: Optional[HttpTokensStateType] = None
    HttpPutResponseHopLimit: Optional[int] = None
    HttpEndpoint: Optional[InstanceMetadataEndpointStateType] = None
    DryRun: Optional[bool] = None
    HttpProtocolIpv6: Optional[InstanceMetadataProtocolStateType] = None
    InstanceMetadataTags: Optional[InstanceMetadataTagsStateType] = None

class ModifyInstancePlacementRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Affinity: Optional[AffinityType] = None
    GroupName: Optional[str] = None
    HostId: Optional[str] = None
    Tenancy: Optional[HostTenancyType] = None
    PartitionNumber: Optional[int] = None
    HostResourceGroupArn: Optional[str] = None
    GroupId: Optional[str] = None

class RemoveIpamOperatingRegionTypeDef(BaseModel):
    RegionName: Optional[str] = None

class ModifyIpamResourceCidrRequestRequestTypeDef(BaseModel):
    ResourceId: str
    ResourceCidr: str
    ResourceRegion: str
    CurrentIpamScopeId: str
    Monitored: bool
    DryRun: Optional[bool] = None
    DestinationIpamScopeId: Optional[str] = None

class ModifyIpamScopeRequestRequestTypeDef(BaseModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None

class ModifyLaunchTemplateRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    DefaultVersion: Optional[str] = None

class ModifyLocalGatewayRouteRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    DestinationCidrBlock: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    DryRun: Optional[bool] = None
    DestinationPrefixListId: Optional[str] = None

class RemovePrefixListEntryTypeDef(BaseModel):
    Cidr: str

class NetworkInterfaceAttachmentChangesTypeDef(BaseModel):
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None

class ModifyPrivateDnsNameOptionsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    PrivateDnsHostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class ReservedInstancesConfigurationTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    InstanceCount: Optional[int] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[str] = None
    Scope: Optional[ScopeType] = None

class ModifySnapshotTierRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    StorageTier: Optional[Literal["archive"]] = None
    DryRun: Optional[bool] = None

class ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef(BaseModel):
    TrafficMirrorFilterId: str
    AddNetworkServices: Optional[Sequence[Literal["amazon-dns"]]] = None
    RemoveNetworkServices: Optional[Sequence[Literal["amazon-dns"]]] = None
    DryRun: Optional[bool] = None

class ModifyTrafficMirrorSessionRequestRequestTypeDef(BaseModel):
    TrafficMirrorSessionId: str
    TrafficMirrorTargetId: Optional[str] = None
    TrafficMirrorFilterId: Optional[str] = None
    PacketLength: Optional[int] = None
    SessionNumber: Optional[int] = None
    VirtualNetworkId: Optional[int] = None
    Description: Optional[str] = None
    RemoveFields: Optional[Sequence[TrafficMirrorSessionFieldType]] = None
    DryRun: Optional[bool] = None

class ModifyTransitGatewayOptionsTypeDef(BaseModel):
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

class ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef(BaseModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None

class ModifyVerifiedAccessEndpointEniOptionsTypeDef(BaseModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef(BaseModel):
    SubnetIds: Optional[Sequence[str]] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class VerifiedAccessSseSpecificationResponseTypeDef(BaseModel):
    CustomerManagedKeyEnabled: Optional[bool] = None
    KmsKeyArn: Optional[str] = None

class ModifyVerifiedAccessGroupRequestRequestTypeDef(BaseModel):
    VerifiedAccessGroupId: str
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVerifiedAccessInstanceRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceId: str
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef(BaseModel):
    PublicSigningKeyUrl: Optional[str] = None

class ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef(BaseModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None

class ModifyVolumeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    DryRun: Optional[bool] = None
    Size: Optional[int] = None
    VolumeType: Optional[VolumeTypeType] = None
    Iops: Optional[int] = None
    Throughput: Optional[int] = None
    MultiAttachEnabled: Optional[bool] = None

class ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef(BaseModel):
    ConnectionNotificationId: str
    DryRun: Optional[bool] = None
    ConnectionNotificationArn: Optional[str] = None
    ConnectionEvents: Optional[Sequence[str]] = None

class ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef(BaseModel):
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

class ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef(BaseModel):
    ServiceId: str
    PayerResponsibility: Literal["ServiceOwner"]
    DryRun: Optional[bool] = None

class ModifyVpcEndpointServicePermissionsRequestRequestTypeDef(BaseModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    AddAllowedPrincipals: Optional[Sequence[str]] = None
    RemoveAllowedPrincipals: Optional[Sequence[str]] = None

class PeeringConnectionOptionsRequestTypeDef(BaseModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class PeeringConnectionOptionsTypeDef(BaseModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class ModifyVpcTenancyRequestRequestTypeDef(BaseModel):
    VpcId: str
    InstanceTenancy: Literal["default"]
    DryRun: Optional[bool] = None

class ModifyVpnConnectionOptionsRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    LocalIpv4NetworkCidr: Optional[str] = None
    RemoteIpv4NetworkCidr: Optional[str] = None
    LocalIpv6NetworkCidr: Optional[str] = None
    RemoteIpv6NetworkCidr: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVpnConnectionRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    TransitGatewayId: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    VpnGatewayId: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVpnTunnelCertificateRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    DryRun: Optional[bool] = None

class Phase1DHGroupNumbersRequestListValueTypeDef(BaseModel):
    Value: Optional[int] = None

class Phase1EncryptionAlgorithmsRequestListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class Phase1IntegrityAlgorithmsRequestListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class Phase2DHGroupNumbersRequestListValueTypeDef(BaseModel):
    Value: Optional[int] = None

class Phase2EncryptionAlgorithmsRequestListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class Phase2IntegrityAlgorithmsRequestListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class MonitorInstancesRequestInstanceMonitorTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class MonitorInstancesRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class MoveAddressToVpcRequestRequestTypeDef(BaseModel):
    PublicIp: str
    DryRun: Optional[bool] = None

class MoveByoipCidrToIpamRequestRequestTypeDef(BaseModel):
    Cidr: str
    IpamPoolId: str
    IpamPoolOwner: str
    DryRun: Optional[bool] = None

class ProvisionedBandwidthTypeDef(BaseModel):
    ProvisionTime: Optional[datetime] = None
    Provisioned: Optional[str] = None
    RequestTime: Optional[datetime] = None
    Requested: Optional[str] = None
    Status: Optional[str] = None

class NetworkAclAssociationTypeDef(BaseModel):
    NetworkAclAssociationId: Optional[str] = None
    NetworkAclId: Optional[str] = None
    SubnetId: Optional[str] = None

class NetworkCardInfoTypeDef(BaseModel):
    NetworkCardIndex: Optional[int] = None
    NetworkPerformance: Optional[str] = None
    MaximumNetworkInterfaces: Optional[int] = None
    BaselineBandwidthInGbps: Optional[float] = None
    PeakBandwidthInGbps: Optional[float] = None

class NetworkInterfaceAssociationTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    AssociationId: Optional[str] = None
    IpOwnerId: Optional[str] = None
    PublicDnsName: Optional[str] = None
    PublicIp: Optional[str] = None
    CustomerOwnedIp: Optional[str] = None
    CarrierIp: Optional[str] = None

class NetworkInterfaceIpv6AddressTypeDef(BaseModel):
    Ipv6Address: Optional[str] = None
    IsPrimaryIpv6: Optional[bool] = None

class NetworkInterfacePermissionStateTypeDef(BaseModel):
    State: Optional[NetworkInterfacePermissionStateCodeType] = None
    StatusMessage: Optional[str] = None

class NeuronDeviceCoreInfoTypeDef(BaseModel):
    Count: Optional[int] = None
    Version: Optional[int] = None

class NeuronDeviceMemoryInfoTypeDef(BaseModel):
    SizeInMiB: Optional[int] = None

class OidcOptionsTypeDef(BaseModel):
    Issuer: Optional[str] = None
    AuthorizationEndpoint: Optional[str] = None
    TokenEndpoint: Optional[str] = None
    UserInfoEndpoint: Optional[str] = None
    ClientId: Optional[str] = None
    ClientSecret: Optional[str] = None
    Scope: Optional[str] = None

class PacketHeaderStatementRequestTypeDef(BaseModel):
    SourceAddresses: Optional[Sequence[str]] = None
    DestinationAddresses: Optional[Sequence[str]] = None
    SourcePorts: Optional[Sequence[str]] = None
    DestinationPorts: Optional[Sequence[str]] = None
    SourcePrefixLists: Optional[Sequence[str]] = None
    DestinationPrefixLists: Optional[Sequence[str]] = None
    Protocols: Optional[Sequence[ProtocolType]] = None

class PacketHeaderStatementTypeDef(BaseModel):
    SourceAddresses: Optional[List[str]] = None
    DestinationAddresses: Optional[List[str]] = None
    SourcePorts: Optional[List[str]] = None
    DestinationPorts: Optional[List[str]] = None
    SourcePrefixLists: Optional[List[str]] = None
    DestinationPrefixLists: Optional[List[str]] = None
    Protocols: Optional[List[ProtocolType]] = None

class RequestFilterPortRangeTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class ResourceStatementRequestTypeDef(BaseModel):
    Resources: Optional[Sequence[str]] = None
    ResourceTypes: Optional[Sequence[str]] = None

class ResourceStatementTypeDef(BaseModel):
    Resources: Optional[List[str]] = None
    ResourceTypes: Optional[List[str]] = None

class PeeringAttachmentStatusTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class PeeringTgwInfoTypeDef(BaseModel):
    TransitGatewayId: Optional[str] = None
    CoreNetworkId: Optional[str] = None
    OwnerId: Optional[str] = None
    Region: Optional[str] = None

class Phase1DHGroupNumbersListValueTypeDef(BaseModel):
    Value: Optional[int] = None

class Phase1EncryptionAlgorithmsListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class Phase1IntegrityAlgorithmsListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class Phase2DHGroupNumbersListValueTypeDef(BaseModel):
    Value: Optional[int] = None

class Phase2EncryptionAlgorithmsListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class Phase2IntegrityAlgorithmsListValueTypeDef(BaseModel):
    Value: Optional[str] = None

class PriceScheduleTypeDef(BaseModel):
    Active: Optional[bool] = None
    CurrencyCode: Optional[Literal["USD"]] = None
    Price: Optional[float] = None
    Term: Optional[int] = None

class PricingDetailTypeDef(BaseModel):
    Count: Optional[int] = None
    Price: Optional[float] = None

class PrivateDnsDetailsTypeDef(BaseModel):
    PrivateDnsName: Optional[str] = None

class PrivateDnsNameConfigurationTypeDef(BaseModel):
    State: Optional[DnsNameStateType] = None
    Type: Optional[str] = None
    Value: Optional[str] = None
    Name: Optional[str] = None

class PrivateDnsNameOptionsOnLaunchTypeDef(BaseModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class PrivateDnsNameOptionsRequestTypeDef(BaseModel):
    HostnameType: Optional[HostnameTypeType] = None
    EnableResourceNameDnsARecord: Optional[bool] = None
    EnableResourceNameDnsAAAARecord: Optional[bool] = None

class PropagatingVgwTypeDef(BaseModel):
    GatewayId: Optional[str] = None

class ProvisionPublicIpv4PoolCidrRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    PoolId: str
    NetmaskLength: int
    DryRun: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class PublicIpv4PoolRangeTypeDef(BaseModel):
    FirstAddress: Optional[str] = None
    LastAddress: Optional[str] = None
    AddressCount: Optional[int] = None
    AvailableAddressCount: Optional[int] = None

class PurchaseRequestTypeDef(BaseModel):
    InstanceCount: int
    PurchaseToken: str

class ReservedInstanceLimitPriceTypeDef(BaseModel):
    Amount: Optional[float] = None
    CurrencyCode: Optional[Literal["USD"]] = None

class RebootInstancesRequestInstanceRebootTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class RebootInstancesRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class RecurringChargeTypeDef(BaseModel):
    Amount: Optional[float] = None
    Frequency: Optional[Literal["Hourly"]] = None

class ReferencedSecurityGroupTypeDef(BaseModel):
    GroupId: Optional[str] = None
    PeeringStatus: Optional[str] = None
    UserId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcPeeringConnectionId: Optional[str] = None

class RegisterInstanceTagAttributeRequestTypeDef(BaseModel):
    IncludeAllTagsOfInstance: Optional[bool] = None
    InstanceTagKeys: Optional[Sequence[str]] = None

class RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    NetworkInterfaceIds: Sequence[str]
    GroupIpAddress: Optional[str] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastRegisteredGroupMembersTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    RegisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    NetworkInterfaceIds: Sequence[str]
    GroupIpAddress: Optional[str] = None
    DryRun: Optional[bool] = None

class TransitGatewayMulticastRegisteredGroupSourcesTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    RegisteredNetworkInterfaceIds: Optional[List[str]] = None
    GroupIpAddress: Optional[str] = None

class RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class RejectTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    DryRun: Optional[bool] = None

class RejectVpcEndpointConnectionsRequestRequestTypeDef(BaseModel):
    ServiceId: str
    VpcEndpointIds: Sequence[str]
    DryRun: Optional[bool] = None

class RejectVpcPeeringConnectionRequestRequestTypeDef(BaseModel):
    VpcPeeringConnectionId: str
    DryRun: Optional[bool] = None

class RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class ReleaseAddressRequestClassicAddressReleaseTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None

class ReleaseAddressRequestRequestTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None

class ReleaseAddressRequestVpcAddressReleaseTypeDef(BaseModel):
    AllocationId: Optional[str] = None
    PublicIp: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    DryRun: Optional[bool] = None

class ReleaseHostsRequestRequestTypeDef(BaseModel):
    HostIds: Sequence[str]

class ReleaseIpamPoolAllocationRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    Cidr: str
    IpamPoolAllocationId: str
    DryRun: Optional[bool] = None

class ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef(BaseModel):
    AssociationId: str
    DryRun: Optional[bool] = None

class ReplaceNetworkAclAssociationRequestRequestTypeDef(BaseModel):
    AssociationId: str
    NetworkAclId: str
    DryRun: Optional[bool] = None

class ReplaceRouteRequestRequestTypeDef(BaseModel):
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

class ReplaceRouteRequestRouteReplaceTypeDef(BaseModel):
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

class ReplaceRouteTableAssociationRequestRequestTypeDef(BaseModel):
    AssociationId: str
    RouteTableId: str
    DryRun: Optional[bool] = None

class ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef(BaseModel):
    RouteTableId: str
    DryRun: Optional[bool] = None

class ReplaceTransitGatewayRouteRequestRequestTypeDef(BaseModel):
    DestinationCidrBlock: str
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: Optional[str] = None
    Blackhole: Optional[bool] = None
    DryRun: Optional[bool] = None

class ReplaceVpnTunnelRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    ApplyPendingMaintenance: Optional[bool] = None
    DryRun: Optional[bool] = None

class ReservedInstancesIdTypeDef(BaseModel):
    ReservedInstancesId: Optional[str] = None

class ResetAddressAttributeRequestRequestTypeDef(BaseModel):
    AllocationId: str
    Attribute: Literal["domain-name"]
    DryRun: Optional[bool] = None

class ResetEbsDefaultKmsKeyIdRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class ResetFpgaImageAttributeRequestRequestTypeDef(BaseModel):
    FpgaImageId: str
    DryRun: Optional[bool] = None
    Attribute: Optional[Literal["loadPermission"]] = None

class ResetImageAttributeRequestImageResetAttributeTypeDef(BaseModel):
    Attribute: Literal["launchPermission"]
    DryRun: Optional[bool] = None

class ResetImageAttributeRequestRequestTypeDef(BaseModel):
    Attribute: Literal["launchPermission"]
    ImageId: str
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetAttributeTypeDef(BaseModel):
    Attribute: InstanceAttributeNameType
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetKernelTypeDef(BaseModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef(BaseModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef(BaseModel):
    Attribute: Optional[InstanceAttributeNameType] = None
    DryRun: Optional[bool] = None

class ResetInstanceAttributeRequestRequestTypeDef(BaseModel):
    Attribute: InstanceAttributeNameType
    InstanceId: str
    DryRun: Optional[bool] = None

class ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    SourceDestCheck: Optional[str] = None

class ResetNetworkInterfaceAttributeRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None
    SourceDestCheck: Optional[str] = None

class ResetSnapshotAttributeRequestRequestTypeDef(BaseModel):
    Attribute: SnapshotAttributeNameType
    SnapshotId: str
    DryRun: Optional[bool] = None

class ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef(BaseModel):
    Attribute: SnapshotAttributeNameType
    DryRun: Optional[bool] = None

class RestoreAddressToClassicRequestRequestTypeDef(BaseModel):
    PublicIp: str
    DryRun: Optional[bool] = None

class RestoreImageFromRecycleBinRequestRequestTypeDef(BaseModel):
    ImageId: str
    DryRun: Optional[bool] = None

class RestoreManagedPrefixListVersionRequestRequestTypeDef(BaseModel):
    PrefixListId: str
    PreviousVersion: int
    CurrentVersion: int
    DryRun: Optional[bool] = None

class RestoreSnapshotFromRecycleBinRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    DryRun: Optional[bool] = None

class RestoreSnapshotTierRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    TemporaryRestoreDays: Optional[int] = None
    PermanentRestore: Optional[bool] = None
    DryRun: Optional[bool] = None

class RevokeClientVpnIngressRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    TargetNetworkCidr: str
    AccessGroupId: Optional[str] = None
    RevokeAllGroups: Optional[bool] = None
    DryRun: Optional[bool] = None

class RouteTypeDef(BaseModel):
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

class S3StorageOutputTypeDef(BaseModel):
    AWSAccessKeyId: Optional[str] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None
    UploadPolicy: Optional[bytes] = None
    UploadPolicySignature: Optional[str] = None

class ScheduledInstanceRecurrenceTypeDef(BaseModel):
    Frequency: Optional[str] = None
    Interval: Optional[int] = None
    OccurrenceDaySet: Optional[List[int]] = None
    OccurrenceRelativeToEnd: Optional[bool] = None
    OccurrenceUnit: Optional[str] = None

class ScheduledInstancesEbsTypeDef(BaseModel):
    DeleteOnTermination: Optional[bool] = None
    Encrypted: Optional[bool] = None
    Iops: Optional[int] = None
    SnapshotId: Optional[str] = None
    VolumeSize: Optional[int] = None
    VolumeType: Optional[str] = None

class ScheduledInstancesIamInstanceProfileTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ScheduledInstancesIpv6AddressTypeDef(BaseModel):
    Ipv6Address: Optional[str] = None

class ScheduledInstancesMonitoringTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class ScheduledInstancesPlacementTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    GroupName: Optional[str] = None

class ScheduledInstancesPrivateIpAddressConfigTypeDef(BaseModel):
    Primary: Optional[bool] = None
    PrivateIpAddress: Optional[str] = None

class TransitGatewayMulticastGroupTypeDef(BaseModel):
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

class SecurityGroupIdentifierTypeDef(BaseModel):
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None

class SecurityGroupRuleDescriptionTypeDef(BaseModel):
    SecurityGroupRuleId: Optional[str] = None
    Description: Optional[str] = None

class SecurityGroupRuleRequestTypeDef(BaseModel):
    IpProtocol: Optional[str] = None
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None
    CidrIpv4: Optional[str] = None
    CidrIpv6: Optional[str] = None
    PrefixListId: Optional[str] = None
    ReferencedGroupId: Optional[str] = None
    Description: Optional[str] = None

class SendDiagnosticInterruptRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None

class ServiceTypeDetailTypeDef(BaseModel):
    ServiceType: Optional[ServiceTypeType] = None

class UserBucketDetailsTypeDef(BaseModel):
    S3Bucket: Optional[str] = None
    S3Key: Optional[str] = None

class SpotCapacityRebalanceTypeDef(BaseModel):
    ReplacementStrategy: Optional[ReplacementStrategyType] = None
    TerminationDelay: Optional[int] = None

class SpotInstanceStateFaultTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class SpotFleetMonitoringTypeDef(BaseModel):
    Enabled: Optional[bool] = None

class SpotInstanceStatusTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None
    UpdateTime: Optional[datetime] = None

class StartInstancesRequestInstanceStartTypeDef(BaseModel):
    AdditionalInfo: Optional[str] = None
    DryRun: Optional[bool] = None

class StartInstancesRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    AdditionalInfo: Optional[str] = None
    DryRun: Optional[bool] = None

class StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef(BaseModel):
    ServiceId: str
    DryRun: Optional[bool] = None

class StopInstancesRequestInstanceStopTypeDef(BaseModel):
    Hibernate: Optional[bool] = None
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class StopInstancesRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    Hibernate: Optional[bool] = None
    DryRun: Optional[bool] = None
    Force: Optional[bool] = None

class SubnetAssociationTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    State: Optional[TransitGatewayMulitcastDomainAssociationStateType] = None

class SubnetCidrBlockStateTypeDef(BaseModel):
    State: Optional[SubnetCidrBlockStateCodeType] = None
    StatusMessage: Optional[str] = None

class TargetConfigurationTypeDef(BaseModel):
    InstanceCount: Optional[int] = None
    OfferingId: Optional[str] = None

class TargetGroupTypeDef(BaseModel):
    Arn: Optional[str] = None

class TerminateClientVpnConnectionsRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    ConnectionId: Optional[str] = None
    Username: Optional[str] = None
    DryRun: Optional[bool] = None

class TerminateInstancesRequestInstanceTerminateTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class TerminateInstancesRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class TrafficMirrorPortRangeTypeDef(BaseModel):
    FromPort: Optional[int] = None
    ToPort: Optional[int] = None

class TransitGatewayAttachmentAssociationTypeDef(BaseModel):
    TransitGatewayRouteTableId: Optional[str] = None
    State: Optional[TransitGatewayAssociationStateType] = None

class TransitGatewayAttachmentBgpConfigurationTypeDef(BaseModel):
    TransitGatewayAsn: Optional[int] = None
    PeerAsn: Optional[int] = None
    TransitGatewayAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    BgpStatus: Optional[BgpStatusType] = None

class TransitGatewayConnectOptionsTypeDef(BaseModel):
    Protocol: Optional[Literal["gre"]] = None

class TransitGatewayMulticastDomainOptionsTypeDef(BaseModel):
    Igmpv2Support: Optional[Igmpv2SupportValueType] = None
    StaticSourcesSupport: Optional[StaticSourcesSupportValueType] = None
    AutoAcceptSharedAssociations: Optional[AutoAcceptSharedAssociationsValueType] = None

class TransitGatewayOptionsTypeDef(BaseModel):
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

class TransitGatewayPeeringAttachmentOptionsTypeDef(BaseModel):
    DynamicRouting: Optional[DynamicRoutingValueType] = None

class TransitGatewayPolicyRuleMetaDataTypeDef(BaseModel):
    MetaDataKey: Optional[str] = None
    MetaDataValue: Optional[str] = None

class TransitGatewayPrefixListAttachmentTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceId: Optional[str] = None

class TransitGatewayRouteAttachmentTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None

class TransitGatewayVpcAttachmentOptionsTypeDef(BaseModel):
    DnsSupport: Optional[DnsSupportValueType] = None
    SecurityGroupReferencingSupport: Optional[SecurityGroupReferencingSupportValueType] = None
    Ipv6Support: Optional[Ipv6SupportValueType] = None
    ApplianceModeSupport: Optional[ApplianceModeSupportValueType] = None

class UnassignIpv6AddressesRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    Ipv6Addresses: Optional[Sequence[str]] = None
    Ipv6Prefixes: Optional[Sequence[str]] = None

class UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef(BaseModel):
    PrivateIpAddresses: Optional[Sequence[str]] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None

class UnassignPrivateIpAddressesRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: str
    PrivateIpAddresses: Optional[Sequence[str]] = None
    Ipv4Prefixes: Optional[Sequence[str]] = None

class UnassignPrivateNatGatewayAddressRequestRequestTypeDef(BaseModel):
    NatGatewayId: str
    PrivateIpAddresses: Sequence[str]
    MaxDrainDurationSeconds: Optional[int] = None
    DryRun: Optional[bool] = None

class UnlockSnapshotRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    DryRun: Optional[bool] = None

class UnmonitorInstancesRequestInstanceUnmonitorTypeDef(BaseModel):
    DryRun: Optional[bool] = None

class UnmonitorInstancesRequestRequestTypeDef(BaseModel):
    InstanceIds: Sequence[str]
    DryRun: Optional[bool] = None

class UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef(BaseModel):
    Code: Optional[UnsuccessfulInstanceCreditSpecificationErrorCodeType] = None
    Message: Optional[str] = None

class UnsuccessfulItemErrorTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class ValidationErrorTypeDef(BaseModel):
    Code: Optional[str] = None
    Message: Optional[str] = None

class VerifiedAccessEndpointEniOptionsTypeDef(BaseModel):
    NetworkInterfaceId: Optional[str] = None
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None

class VerifiedAccessEndpointLoadBalancerOptionsTypeDef(BaseModel):
    Protocol: Optional[VerifiedAccessEndpointProtocolType] = None
    Port: Optional[int] = None
    LoadBalancerArn: Optional[str] = None
    SubnetIds: Optional[List[str]] = None

class VerifiedAccessEndpointStatusTypeDef(BaseModel):
    Code: Optional[VerifiedAccessEndpointStatusCodeType] = None
    Message: Optional[str] = None

class VerifiedAccessTrustProviderCondensedTypeDef(BaseModel):
    VerifiedAccessTrustProviderId: Optional[str] = None
    Description: Optional[str] = None
    TrustProviderType: Optional[TrustProviderTypeType] = None
    UserTrustProviderType: Optional[UserTrustProviderTypeType] = None
    DeviceTrustProviderType: Optional[DeviceTrustProviderTypeType] = None

class VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef(BaseModel):
    Enabled: bool
    LogGroup: Optional[str] = None

class VerifiedAccessLogDeliveryStatusTypeDef(BaseModel):
    Code: Optional[VerifiedAccessLogDeliveryStatusCodeType] = None
    Message: Optional[str] = None

class VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef(BaseModel):
    Enabled: bool
    DeliveryStream: Optional[str] = None

class VerifiedAccessLogS3DestinationOptionsTypeDef(BaseModel):
    Enabled: bool
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None

class VgwTelemetryTypeDef(BaseModel):
    AcceptedRouteCount: Optional[int] = None
    LastStatusChange: Optional[datetime] = None
    OutsideIpAddress: Optional[str] = None
    Status: Optional[TelemetryStatusType] = None
    StatusMessage: Optional[str] = None
    CertificateArn: Optional[str] = None

class VolumeAttachmentTypeDef(BaseModel):
    AttachTime: Optional[datetime] = None
    Device: Optional[str] = None
    InstanceId: Optional[str] = None
    State: Optional[VolumeAttachmentStateType] = None
    VolumeId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    AssociatedResource: Optional[str] = None
    InstanceOwningService: Optional[str] = None

class VolumeStatusActionTypeDef(BaseModel):
    Code: Optional[str] = None
    Description: Optional[str] = None
    EventId: Optional[str] = None
    EventType: Optional[str] = None

class VolumeStatusAttachmentStatusTypeDef(BaseModel):
    IoPerformance: Optional[str] = None
    InstanceId: Optional[str] = None

class VolumeStatusDetailsTypeDef(BaseModel):
    Name: Optional[VolumeStatusNameType] = None
    Status: Optional[str] = None

class VolumeStatusEventTypeDef(BaseModel):
    Description: Optional[str] = None
    EventId: Optional[str] = None
    EventType: Optional[str] = None
    NotAfter: Optional[datetime] = None
    NotBefore: Optional[datetime] = None
    InstanceId: Optional[str] = None

class VpcCidrBlockStateTypeDef(BaseModel):
    State: Optional[VpcCidrBlockStateCodeType] = None
    StatusMessage: Optional[str] = None

class VpcPeeringConnectionOptionsDescriptionTypeDef(BaseModel):
    AllowDnsResolutionFromRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalClassicLinkToRemoteVpc: Optional[bool] = None
    AllowEgressFromLocalVpcToRemoteClassicLink: Optional[bool] = None

class VpcPeeringConnectionStateReasonTypeDef(BaseModel):
    Code: Optional[VpcPeeringConnectionStateReasonCodeType] = None
    Message: Optional[str] = None

class VpnStaticRouteTypeDef(BaseModel):
    DestinationCidrBlock: Optional[str] = None
    Source: Optional[Literal["Static"]] = None
    State: Optional[VpnStateType] = None

class WithdrawByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str
    DryRun: Optional[bool] = None

class AcceptAddressTransferResultTypeDef(BaseModel):
    AddressTransfer: AddressTransferTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptReservedInstancesExchangeQuoteResultTypeDef(BaseModel):
    ExchangeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateAddressResultTypeDef(BaseModel):
    PublicIp: str
    AllocationId: str
    PublicIpv4Pool: str
    NetworkBorderGroup: str
    Domain: DomainTypeType
    CustomerOwnedIp: str
    CustomerOwnedIpv4Pool: str
    CarrierIp: str
    ResponseMetadata: ResponseMetadataTypeDef

class AllocateHostsResultTypeDef(BaseModel):
    HostIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef(BaseModel):
    SecurityGroupIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class AssignIpv6AddressesResultTypeDef(BaseModel):
    AssignedIpv6Addresses: List[str]
    AssignedIpv6Prefixes: List[str]
    NetworkInterfaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateAddressResultTypeDef(BaseModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateEnclaveCertificateIamRoleResultTypeDef(BaseModel):
    CertificateS3BucketName: str
    CertificateS3ObjectKey: str
    EncryptionKmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachClassicLinkVpcResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AttachNetworkInterfaceResultTypeDef(BaseModel):
    AttachmentId: str
    NetworkCardIndex: int
    ResponseMetadata: ResponseMetadataTypeDef

class CancelCapacityReservationResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CancelImageLaunchPermissionResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CancelImportTaskResultTypeDef(BaseModel):
    ImportTaskId: str
    PreviousState: str
    State: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConfirmProductInstanceResultTypeDef(BaseModel):
    OwnerId: str
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CopyFpgaImageResultTypeDef(BaseModel):
    FpgaImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CopyImageResultTypeDef(BaseModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFpgaImageResultTypeDef(BaseModel):
    FpgaImageId: str
    FpgaImageGlobalId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageResultTypeDef(BaseModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePublicIpv4PoolResultTypeDef(BaseModel):
    PoolId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRestoreImageTaskResultTypeDef(BaseModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRouteResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStoreImageTaskResultTypeDef(BaseModel):
    ObjectKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEgressOnlyInternetGatewayResultTypeDef(BaseModel):
    ReturnCode: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFpgaImageResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteKeyPairResultTypeDef(BaseModel):
    Return: bool
    KeyPairId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNatGatewayResultTypeDef(BaseModel):
    NatGatewayId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsAccessScopeResultTypeDef(BaseModel):
    NetworkInsightsAccessScopeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsAnalysisResultTypeDef(BaseModel):
    NetworkInsightsAnalysisId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInsightsPathResultTypeDef(BaseModel):
    NetworkInsightsPathId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNetworkInterfacePermissionResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePublicIpv4PoolResultTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorFilterResultTypeDef(BaseModel):
    TrafficMirrorFilterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorFilterRuleResultTypeDef(BaseModel):
    TrafficMirrorFilterRuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorSessionResultTypeDef(BaseModel):
    TrafficMirrorSessionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrafficMirrorTargetResultTypeDef(BaseModel):
    TrafficMirrorTargetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcPeeringConnectionResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionPublicIpv4PoolCidrResultTypeDef(BaseModel):
    PoolId: str
    DeprovisionedAddresses: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressTransfersResultTypeDef(BaseModel):
    AddressTransfers: List[AddressTransferTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetachClassicLinkVpcResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableAddressTransferResultTypeDef(BaseModel):
    AddressTransfer: AddressTransferTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef(BaseModel):
    Output: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableEbsEncryptionByDefaultResultTypeDef(BaseModel):
    EbsEncryptionByDefault: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageBlockPublicAccessResultTypeDef(BaseModel):
    ImageBlockPublicAccessState: Literal["unblocked"]
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageDeprecationResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageDeregistrationProtectionResultTypeDef(BaseModel):
    Return: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableImageResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableIpamOrganizationAdminAccountResultTypeDef(BaseModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableSerialConsoleAccessResultTypeDef(BaseModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableSnapshotBlockPublicAccessResultTypeDef(BaseModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DisableVpcClassicLinkDnsSupportResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisableVpcClassicLinkResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateEnclaveCertificateIamRoleResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTrunkInterfaceResultTypeDef(BaseModel):
    Return: bool
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EnableAddressTransferResultTypeDef(BaseModel):
    AddressTransfer: AddressTransferTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef(BaseModel):
    Output: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableEbsEncryptionByDefaultResultTypeDef(BaseModel):
    EbsEncryptionByDefault: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageBlockPublicAccessResultTypeDef(BaseModel):
    ImageBlockPublicAccessState: Literal["block-new-sharing"]
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageDeprecationResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageDeregistrationProtectionResultTypeDef(BaseModel):
    Return: str
    ResponseMetadata: ResponseMetadataTypeDef

class EnableImageResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableIpamOrganizationAdminAccountResultTypeDef(BaseModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableReachabilityAnalyzerOrganizationSharingResultTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSerialConsoleAccessResultTypeDef(BaseModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableSnapshotBlockPublicAccessResultTypeDef(BaseModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableVpcClassicLinkDnsSupportResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EnableVpcClassicLinkResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ExportClientVpnClientConfigurationResultTypeDef(BaseModel):
    ClientConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTransitGatewayRoutesResultTypeDef(BaseModel):
    S3Location: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConsoleOutputResultTypeDef(BaseModel):
    InstanceId: str
    Output: str
    Timestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetConsoleScreenshotResultTypeDef(BaseModel):
    ImageData: str
    InstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEbsDefaultKmsKeyIdResultTypeDef(BaseModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEbsEncryptionByDefaultResultTypeDef(BaseModel):
    EbsEncryptionByDefault: bool
    SseType: SSETypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowLogsIntegrationTemplateResultTypeDef(BaseModel):
    Result: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageBlockPublicAccessStateResultTypeDef(BaseModel):
    ImageBlockPublicAccessState: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceTpmEkPubResultTypeDef(BaseModel):
    InstanceId: str
    KeyType: EkPubKeyTypeType
    KeyFormat: EkPubKeyFormatType
    KeyValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceUefiDataResultTypeDef(BaseModel):
    InstanceId: str
    UefiData: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPasswordDataResultTypeDef(BaseModel):
    InstanceId: str
    PasswordData: str
    Timestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSerialConsoleAccessStatusResultTypeDef(BaseModel):
    SerialConsoleAccessEnabled: bool
    ResponseMetadata: ResponseMetadataTypeDef

class GetSnapshotBlockPublicAccessStateResultTypeDef(BaseModel):
    State: SnapshotBlockPublicAccessStateType
    ResponseMetadata: ResponseMetadataTypeDef

class GetVerifiedAccessEndpointPolicyResultTypeDef(BaseModel):
    PolicyEnabled: bool
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVerifiedAccessGroupPolicyResultTypeDef(BaseModel):
    PolicyEnabled: bool
    PolicyDocument: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVpnConnectionDeviceSampleConfigurationResultTypeDef(BaseModel):
    VpnConnectionDeviceSampleConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportClientVpnClientCertificateRevocationListResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class LockSnapshotResultTypeDef(BaseModel):
    SnapshotId: str
    LockState: LockStateType
    LockDuration: int
    CoolOffPeriod: int
    CoolOffPeriodExpiresOn: datetime
    LockCreatedOn: datetime
    LockExpiresOn: datetime
    LockDurationStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyAvailabilityZoneGroupResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCapacityReservationFleetResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCapacityReservationResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyClientVpnEndpointResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEbsDefaultKmsKeyIdResultTypeDef(BaseModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyFleetResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceCapacityReservationAttributesResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceMaintenanceOptionsResultTypeDef(BaseModel):
    InstanceId: str
    AutoRecovery: InstanceAutoRecoveryStateType
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceMetadataDefaultsResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstancePlacementResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyPrivateDnsNameOptionsResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReservedInstancesResultTypeDef(BaseModel):
    ReservedInstancesModificationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySecurityGroupRulesResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySnapshotTierResultTypeDef(BaseModel):
    SnapshotId: str
    TieringStartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySpotFleetRequestResponseTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointConnectionNotificationResultTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointServiceConfigurationResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcEndpointServicePayerResponsibilityResultTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpcTenancyResultTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class MoveAddressToVpcResultTypeDef(BaseModel):
    AllocationId: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedInstancesOfferingResultTypeDef(BaseModel):
    ReservedInstancesId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterImageResultTypeDef(BaseModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectVpcPeeringConnectionResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReleaseIpamPoolAllocationResultTypeDef(BaseModel):
    Success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceNetworkAclAssociationResultTypeDef(BaseModel):
    NewAssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceVpnTunnelResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RequestSpotFleetResponseTypeDef(BaseModel):
    SpotFleetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetEbsDefaultKmsKeyIdResultTypeDef(BaseModel):
    KmsKeyId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetFpgaImageAttributeResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreAddressToClassicResultTypeDef(BaseModel):
    PublicIp: str
    Status: StatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreImageFromRecycleBinResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreSnapshotFromRecycleBinResultTypeDef(BaseModel):
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

class RestoreSnapshotTierResultTypeDef(BaseModel):
    SnapshotId: str
    RestoreStartTime: datetime
    RestoreDuration: int
    IsPermanentRestore: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RunScheduledInstancesResultTypeDef(BaseModel):
    InstanceIdSet: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartVpcEndpointServicePrivateDnsVerificationResultTypeDef(BaseModel):
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UnassignIpv6AddressesResultTypeDef(BaseModel):
    NetworkInterfaceId: str
    UnassignedIpv6Addresses: List[str]
    UnassignedIpv6Prefixes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UnlockSnapshotResultTypeDef(BaseModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef(BaseModel):
    Return: bool
    ResponseMetadata: ResponseMetadataTypeDef

class VolumeAttachmentResponseTypeDef(BaseModel):
    AttachTime: datetime
    Device: str
    InstanceId: str
    State: VolumeAttachmentStateType
    VolumeId: str
    DeleteOnTermination: bool
    AssociatedResource: str
    InstanceOwningService: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef(BaseModel):
    ReservedInstanceIds: Sequence[str]
    DryRun: Optional[bool] = None
    TargetConfigurations: Optional[Sequence[TargetConfigurationRequestTypeDef]] = None

class GetReservedInstancesExchangeQuoteRequestRequestTypeDef(BaseModel):
    ReservedInstanceIds: Sequence[str]
    DryRun: Optional[bool] = None
    TargetConfigurations: Optional[Sequence[TargetConfigurationRequestTypeDef]] = None

class AccountAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[AccountAttributeValueTypeDef]] = None

class DescribeFleetInstancesResultTypeDef(BaseModel):
    ActiveInstances: List[ActiveInstanceTypeDef]
    FleetId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSpotFleetInstancesResponseTypeDef(BaseModel):
    ActiveInstances: List[ActiveInstanceTypeDef]
    SpotFleetRequestId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVpcEndpointServicePermissionsResultTypeDef(BaseModel):
    AddedPrincipals: List[AddedPrincipalTypeDef]
    ReturnValue: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AnalysisLoadBalancerTargetTypeDef(BaseModel):
    Address: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Instance: Optional[AnalysisComponentTypeDef] = None
    Port: Optional[int] = None

class RuleGroupRuleOptionsPairTypeDef(BaseModel):
    RuleGroupArn: Optional[str] = None
    RuleOptions: Optional[List[RuleOptionTypeDef]] = None

class AddressAttributeTypeDef(BaseModel):
    PublicIp: Optional[str] = None
    AllocationId: Optional[str] = None
    PtrRecord: Optional[str] = None
    PtrRecordUpdate: Optional[PtrUpdateStatusTypeDef] = None

class AddressTypeDef(BaseModel):
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

class AllowedPrincipalTypeDef(BaseModel):
    PrincipalType: Optional[PrincipalTypeType] = None
    Principal: Optional[str] = None
    ServicePermissionId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ServiceId: Optional[str] = None

class CarrierGatewayTypeDef(BaseModel):
    CarrierGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    State: Optional[CarrierGatewayStateType] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ClientCreateTagsRequestTypeDef(BaseModel):
    Resources: Sequence[str]
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class ClientDeleteTagsRequestTypeDef(BaseModel):
    Resources: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None

class CoipPoolTypeDef(BaseModel):
    PoolId: Optional[str] = None
    PoolCidrs: Optional[List[str]] = None
    LocalGatewayRouteTableId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    PoolArn: Optional[str] = None

class CopySnapshotResultTypeDef(BaseModel):
    SnapshotId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityGroupResultTypeDef(BaseModel):
    GroupId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTagsRequestServiceResourceCreateTagsTypeDef(BaseModel):
    Resources: Sequence[str]
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class CustomerGatewayTypeDef(BaseModel):
    BgpAsn: Optional[str] = None
    CustomerGatewayId: Optional[str] = None
    IpAddress: Optional[str] = None
    CertificateArn: Optional[str] = None
    State: Optional[str] = None
    Type: Optional[str] = None
    DeviceName: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    BgpAsnExtended: Optional[str] = None

class Ec2InstanceConnectEndpointTypeDef(BaseModel):
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

class HostReservationTypeDef(BaseModel):
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

class ImportKeyPairResultTypeDef(BaseModel):
    KeyFingerprint: str
    KeyName: str
    KeyPairId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceCreateTagsRequestTypeDef(BaseModel):
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class InstanceDeleteTagsRequestTypeDef(BaseModel):
    Tags: Optional[Sequence[TagTypeDef]] = None
    DryRun: Optional[bool] = None

class InstanceEventWindowAssociationRequestTypeDef(BaseModel):
    InstanceIds: Optional[Sequence[str]] = None
    InstanceTags: Optional[Sequence[TagTypeDef]] = None
    DedicatedHostIds: Optional[Sequence[str]] = None

class InstanceEventWindowAssociationTargetTypeDef(BaseModel):
    InstanceIds: Optional[List[str]] = None
    Tags: Optional[List[TagTypeDef]] = None
    DedicatedHostIds: Optional[List[str]] = None

class InstanceEventWindowDisassociationRequestTypeDef(BaseModel):
    InstanceIds: Optional[Sequence[str]] = None
    InstanceTags: Optional[Sequence[TagTypeDef]] = None
    DedicatedHostIds: Optional[Sequence[str]] = None

class IpamResourceDiscoveryAssociationTypeDef(BaseModel):
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

class IpamScopeTypeDef(BaseModel):
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

class KeyPairInfoTypeDef(BaseModel):
    KeyPairId: Optional[str] = None
    KeyFingerprint: Optional[str] = None
    KeyName: Optional[str] = None
    KeyType: Optional[KeyTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None
    PublicKey: Optional[str] = None
    CreateTime: Optional[datetime] = None

class KeyPairTypeDef(BaseModel):
    KeyFingerprint: str
    KeyMaterial: str
    KeyName: str
    KeyPairId: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchTemplateTagSpecificationRequestTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class LaunchTemplateTagSpecificationTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class LaunchTemplateTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    CreateTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DefaultVersionNumber: Optional[int] = None
    LatestVersionNumber: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: Optional[str] = None
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayRouteTableVpcAssociationTypeDef(BaseModel):
    LocalGatewayRouteTableVpcAssociationId: Optional[str] = None
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayTypeDef(BaseModel):
    LocalGatewayId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayVirtualInterfaceGroupTypeDef(BaseModel):
    LocalGatewayVirtualInterfaceGroupId: Optional[str] = None
    LocalGatewayVirtualInterfaceIds: Optional[List[str]] = None
    LocalGatewayId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class LocalGatewayVirtualInterfaceTypeDef(BaseModel):
    LocalGatewayVirtualInterfaceId: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    Vlan: Optional[int] = None
    LocalAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    LocalBgpAsn: Optional[int] = None
    PeerBgpAsn: Optional[int] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ManagedPrefixListTypeDef(BaseModel):
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

class NetworkInsightsAccessScopeAnalysisTypeDef(BaseModel):
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

class NetworkInsightsAccessScopeTypeDef(BaseModel):
    NetworkInsightsAccessScopeId: Optional[str] = None
    NetworkInsightsAccessScopeArn: Optional[str] = None
    CreatedDate: Optional[datetime] = None
    UpdatedDate: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class PlacementGroupTypeDef(BaseModel):
    GroupName: Optional[str] = None
    State: Optional[PlacementGroupStateType] = None
    Strategy: Optional[PlacementStrategyType] = None
    PartitionCount: Optional[int] = None
    GroupId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    GroupArn: Optional[str] = None
    SpreadLevel: Optional[SpreadLevelType] = None

class ReplaceRootVolumeTaskTypeDef(BaseModel):
    ReplaceRootVolumeTaskId: Optional[str] = None
    InstanceId: Optional[str] = None
    TaskState: Optional[ReplaceRootVolumeTaskStateType] = None
    StartTime: Optional[str] = None
    CompleteTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ImageId: Optional[str] = None
    SnapshotId: Optional[str] = None
    DeleteReplacedRootVolume: Optional[bool] = None

class SecurityGroupForVpcTypeDef(BaseModel):
    Description: Optional[str] = None
    GroupName: Optional[str] = None
    OwnerId: Optional[str] = None
    GroupId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    PrimaryVpcId: Optional[str] = None

class SnapshotInfoTypeDef(BaseModel):
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

class SnapshotResponseTypeDef(BaseModel):
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

class SnapshotTierStatusTypeDef(BaseModel):
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

class SnapshotTypeDef(BaseModel):
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

class SpotFleetTagSpecificationExtraOutputTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class SpotFleetTagSpecificationOutputTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class SpotFleetTagSpecificationTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class SubnetCidrReservationTypeDef(BaseModel):
    SubnetCidrReservationId: Optional[str] = None
    SubnetId: Optional[str] = None
    Cidr: Optional[str] = None
    ReservationType: Optional[SubnetCidrReservationTypeType] = None
    OwnerId: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagSpecificationExtraOutputTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagSpecificationOutputTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[List[TagTypeDef]] = None

class TagSpecificationTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TrafficMirrorSessionTypeDef(BaseModel):
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

class TrafficMirrorTargetTypeDef(BaseModel):
    TrafficMirrorTargetId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    NetworkLoadBalancerArn: Optional[str] = None
    Type: Optional[TrafficMirrorTargetTypeType] = None
    Description: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    GatewayLoadBalancerEndpointId: Optional[str] = None

class TransitGatewayPolicyTableTypeDef(BaseModel):
    TransitGatewayPolicyTableId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayPolicyTableStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayRouteTableAnnouncementTypeDef(BaseModel):
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

class TransitGatewayRouteTableTypeDef(BaseModel):
    TransitGatewayRouteTableId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayRouteTableStateType] = None
    DefaultAssociationRouteTable: Optional[bool] = None
    DefaultPropagationRouteTable: Optional[bool] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TrunkInterfaceAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    BranchInterfaceId: Optional[str] = None
    TrunkInterfaceId: Optional[str] = None
    InterfaceProtocol: Optional[InterfaceProtocolTypeType] = None
    VlanId: Optional[int] = None
    GreKey: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None

class VpcClassicLinkTypeDef(BaseModel):
    ClassicLinkEnabled: Optional[bool] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None

class VpcCreateTagsRequestTypeDef(BaseModel):
    Tags: Sequence[TagTypeDef]
    DryRun: Optional[bool] = None

class AllocateIpamPoolCidrResultTypeDef(BaseModel):
    IpamPoolAllocation: IpamPoolAllocationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIpamPoolAllocationsResultTypeDef(BaseModel):
    IpamPoolAllocations: List[IpamPoolAllocationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AnalysisAclRuleTypeDef(BaseModel):
    Cidr: Optional[str] = None
    Egress: Optional[bool] = None
    PortRange: Optional[PortRangeTypeDef] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    RuleNumber: Optional[int] = None

class AnalysisPacketHeaderTypeDef(BaseModel):
    DestinationAddresses: Optional[List[str]] = None
    DestinationPortRanges: Optional[List[PortRangeTypeDef]] = None
    Protocol: Optional[str] = None
    SourceAddresses: Optional[List[str]] = None
    SourcePortRanges: Optional[List[PortRangeTypeDef]] = None

class AnalysisSecurityGroupRuleTypeDef(BaseModel):
    Cidr: Optional[str] = None
    Direction: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None
    PrefixListId: Optional[str] = None
    Protocol: Optional[str] = None

class FirewallStatefulRuleTypeDef(BaseModel):
    RuleGroupArn: Optional[str] = None
    Sources: Optional[List[str]] = None
    Destinations: Optional[List[str]] = None
    SourcePorts: Optional[List[PortRangeTypeDef]] = None
    DestinationPorts: Optional[List[PortRangeTypeDef]] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[str] = None
    Direction: Optional[str] = None

class FirewallStatelessRuleTypeDef(BaseModel):
    RuleGroupArn: Optional[str] = None
    Sources: Optional[List[str]] = None
    Destinations: Optional[List[str]] = None
    SourcePorts: Optional[List[PortRangeTypeDef]] = None
    DestinationPorts: Optional[List[PortRangeTypeDef]] = None
    Protocols: Optional[List[int]] = None
    RuleAction: Optional[str] = None
    Priority: Optional[int] = None

class AssociateIpamByoasnResultTypeDef(BaseModel):
    AsnAssociation: AsnAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ByoipCidrTypeDef(BaseModel):
    Cidr: Optional[str] = None
    Description: Optional[str] = None
    AsnAssociations: Optional[List[AsnAssociationTypeDef]] = None
    StatusMessage: Optional[str] = None
    State: Optional[ByoipCidrStateType] = None
    NetworkBorderGroup: Optional[str] = None

class DisassociateIpamByoasnResultTypeDef(BaseModel):
    AsnAssociation: AsnAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionIpamByoasnRequestRequestTypeDef(BaseModel):
    IpamId: str
    Asn: str
    AsnAuthorizationContext: AsnAuthorizationContextTypeDef
    DryRun: Optional[bool] = None

class AssignPrivateIpAddressesResultTypeDef(BaseModel):
    NetworkInterfaceId: str
    AssignedPrivateIpAddresses: List[AssignedPrivateIpAddressTypeDef]
    AssignedIpv4Prefixes: List[Ipv4PrefixSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssignPrivateNatGatewayAddressResultTypeDef(BaseModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateNatGatewayAddressResultTypeDef(BaseModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateNatGatewayAddressResultTypeDef(BaseModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UnassignPrivateNatGatewayAddressResultTypeDef(BaseModel):
    NatGatewayId: str
    NatGatewayAddresses: List[NatGatewayAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateClientVpnTargetNetworkResultTypeDef(BaseModel):
    AssociationId: str
    Status: AssociationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateClientVpnTargetNetworkResultTypeDef(BaseModel):
    AssociationId: str
    Status: AssociationStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TargetNetworkTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    VpcId: Optional[str] = None
    TargetNetworkId: Optional[str] = None
    ClientVpnEndpointId: Optional[str] = None
    Status: Optional[AssociationStatusTypeDef] = None
    SecurityGroups: Optional[List[str]] = None

class AssociateIamInstanceProfileRequestRequestTypeDef(BaseModel):
    IamInstanceProfile: IamInstanceProfileSpecificationTypeDef
    InstanceId: str

class ReplaceIamInstanceProfileAssociationRequestRequestTypeDef(BaseModel):
    IamInstanceProfile: IamInstanceProfileSpecificationTypeDef
    AssociationId: str

class AssociateRouteTableResultTypeDef(BaseModel):
    AssociationId: str
    AssociationState: RouteTableAssociationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceRouteTableAssociationResultTypeDef(BaseModel):
    NewAssociationId: str
    AssociationState: RouteTableAssociationStateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RouteTableAssociationTypeDef(BaseModel):
    Main: Optional[bool] = None
    RouteTableAssociationId: Optional[str] = None
    RouteTableId: Optional[str] = None
    SubnetId: Optional[str] = None
    GatewayId: Optional[str] = None
    AssociationState: Optional[RouteTableAssociationStateTypeDef] = None

class AssociateTransitGatewayPolicyTableResultTypeDef(BaseModel):
    Association: TransitGatewayPolicyTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayPolicyTableResultTypeDef(BaseModel):
    Association: TransitGatewayPolicyTableAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayPolicyTableAssociationsResultTypeDef(BaseModel):
    Associations: List[TransitGatewayPolicyTableAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateTransitGatewayRouteTableResultTypeDef(BaseModel):
    Association: TransitGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayRouteTableResultTypeDef(BaseModel):
    Association: TransitGatewayAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedEnclaveCertificateIamRolesResultTypeDef(BaseModel):
    AssociatedRoles: List[AssociatedRoleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AthenaIntegrationTypeDef(BaseModel):
    IntegrationResultS3DestinationArn: str
    PartitionLoadFrequency: PartitionLoadFrequencyType
    PartitionStartDate: Optional[TimestampTypeDef] = None
    PartitionEndDate: Optional[TimestampTypeDef] = None

class ClientDataTypeDef(BaseModel):
    Comment: Optional[str] = None
    UploadEnd: Optional[TimestampTypeDef] = None
    UploadSize: Optional[float] = None
    UploadStart: Optional[TimestampTypeDef] = None

class DescribeCapacityBlockOfferingsRequestRequestTypeDef(BaseModel):
    InstanceType: str
    InstanceCount: int
    CapacityDurationHours: int
    DryRun: Optional[bool] = None
    StartDateRange: Optional[TimestampTypeDef] = None
    EndDateRange: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeFleetHistoryRequestRequestTypeDef(BaseModel):
    FleetId: str
    StartTime: TimestampTypeDef
    DryRun: Optional[bool] = None
    EventType: Optional[FleetEventTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestHistoryRequestRequestTypeDef(BaseModel):
    SpotFleetRequestId: str
    StartTime: TimestampTypeDef
    DryRun: Optional[bool] = None
    EventType: Optional[EventTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class EnableImageDeprecationRequestRequestTypeDef(BaseModel):
    ImageId: str
    DeprecateAt: TimestampTypeDef
    DryRun: Optional[bool] = None

class GetIpamAddressHistoryRequestRequestTypeDef(BaseModel):
    Cidr: str
    IpamScopeId: str
    DryRun: Optional[bool] = None
    VpcId: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class LaunchTemplateSpotMarketOptionsRequestTypeDef(BaseModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[TimestampTypeDef] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class LockSnapshotRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    LockMode: LockModeType
    DryRun: Optional[bool] = None
    CoolOffPeriod: Optional[int] = None
    LockDuration: Optional[int] = None
    ExpirationDate: Optional[TimestampTypeDef] = None

class ModifyCapacityReservationFleetRequestRequestTypeDef(BaseModel):
    CapacityReservationFleetId: str
    TotalTargetCapacity: Optional[int] = None
    EndDate: Optional[TimestampTypeDef] = None
    DryRun: Optional[bool] = None
    RemoveEndDate: Optional[bool] = None

class ModifyCapacityReservationRequestRequestTypeDef(BaseModel):
    CapacityReservationId: str
    InstanceCount: Optional[int] = None
    EndDate: Optional[TimestampTypeDef] = None
    EndDateType: Optional[EndDateTypeType] = None
    Accept: Optional[bool] = None
    DryRun: Optional[bool] = None
    AdditionalInfo: Optional[str] = None

class ModifyInstanceEventStartTimeRequestRequestTypeDef(BaseModel):
    InstanceId: str
    InstanceEventId: str
    NotBefore: TimestampTypeDef
    DryRun: Optional[bool] = None

class ReportInstanceStatusRequestInstanceReportStatusTypeDef(BaseModel):
    ReasonCodes: Sequence[ReportInstanceReasonCodesType]
    Status: ReportStatusTypeType
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None

class ReportInstanceStatusRequestRequestTypeDef(BaseModel):
    Instances: Sequence[str]
    ReasonCodes: Sequence[ReportInstanceReasonCodesType]
    Status: ReportStatusTypeType
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    StartTime: Optional[TimestampTypeDef] = None

class SlotDateTimeRangeRequestTypeDef(BaseModel):
    EarliestTime: TimestampTypeDef
    LatestTime: TimestampTypeDef

class SlotStartTimeRangeRequestTypeDef(BaseModel):
    EarliestTime: Optional[TimestampTypeDef] = None
    LatestTime: Optional[TimestampTypeDef] = None

class SpotMarketOptionsTypeDef(BaseModel):
    MaxPrice: Optional[str] = None
    SpotInstanceType: Optional[SpotInstanceTypeType] = None
    BlockDurationMinutes: Optional[int] = None
    ValidUntil: Optional[TimestampTypeDef] = None
    InstanceInterruptionBehavior: Optional[InstanceInterruptionBehaviorType] = None

class AttachVpnGatewayResultTypeDef(BaseModel):
    VpcAttachment: VpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VpnGatewayTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    State: Optional[VpnStateType] = None
    Type: Optional[Literal["ipsec.1"]] = None
    VpcAttachments: Optional[List[VpcAttachmentTypeDef]] = None
    VpnGatewayId: Optional[str] = None
    AmazonSideAsn: Optional[int] = None
    Tags: Optional[List[TagTypeDef]] = None

class AttachmentEnaSrdSpecificationTypeDef(BaseModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[AttachmentEnaSrdUdpSpecificationTypeDef] = None

class DescribeVpcAttributeResultTypeDef(BaseModel):
    VpcId: str
    EnableDnsHostnames: AttributeBooleanValueTypeDef
    EnableDnsSupport: AttributeBooleanValueTypeDef
    EnableNetworkAddressUsageMetrics: AttributeBooleanValueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySubnetAttributeRequestRequestTypeDef(BaseModel):
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

class ModifyVolumeAttributeRequestRequestTypeDef(BaseModel):
    VolumeId: str
    AutoEnableIO: Optional[AttributeBooleanValueTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef(BaseModel):
    AutoEnableIO: Optional[AttributeBooleanValueTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyVpcAttributeRequestRequestTypeDef(BaseModel):
    VpcId: str
    EnableDnsHostnames: Optional[AttributeBooleanValueTypeDef] = None
    EnableDnsSupport: Optional[AttributeBooleanValueTypeDef] = None
    EnableNetworkAddressUsageMetrics: Optional[AttributeBooleanValueTypeDef] = None

class ModifyVpcAttributeRequestVpcModifyAttributeTypeDef(BaseModel):
    EnableDnsHostnames: Optional[AttributeBooleanValueTypeDef] = None
    EnableDnsSupport: Optional[AttributeBooleanValueTypeDef] = None
    EnableNetworkAddressUsageMetrics: Optional[AttributeBooleanValueTypeDef] = None

class DhcpConfigurationTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[List[AttributeValueTypeDef]] = None

class AuthorizationRuleTypeDef(BaseModel):
    ClientVpnEndpointId: Optional[str] = None
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    AccessAll: Optional[bool] = None
    DestinationCidr: Optional[str] = None
    Status: Optional[ClientVpnAuthorizationRuleStatusTypeDef] = None

class AuthorizeClientVpnIngressResultTypeDef(BaseModel):
    Status: ClientVpnAuthorizationRuleStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeClientVpnIngressResultTypeDef(BaseModel):
    Status: ClientVpnAuthorizationRuleStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AvailabilityZoneTypeDef(BaseModel):
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

class AvailableCapacityTypeDef(BaseModel):
    AvailableInstanceCapacity: Optional[List[InstanceCapacityTypeDef]] = None
    AvailableVCpus: Optional[int] = None

class BlobAttributeValueTypeDef(BaseModel):
    Value: Optional[BlobTypeDef] = None

class S3StorageTypeDef(BaseModel):
    AWSAccessKeyId: Optional[str] = None
    Bucket: Optional[str] = None
    Prefix: Optional[str] = None
    UploadPolicy: Optional[BlobTypeDef] = None
    UploadPolicySignature: Optional[str] = None

class BlockDeviceMappingTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[EbsBlockDeviceTypeDef] = None
    NoDevice: Optional[str] = None

class DeprovisionIpamByoasnResultTypeDef(BaseModel):
    Byoasn: ByoasnTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamByoasnResultTypeDef(BaseModel):
    Byoasns: List[ByoasnTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ProvisionIpamByoasnResultTypeDef(BaseModel):
    Byoasn: ByoasnTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailedCapacityReservationFleetCancellationResultTypeDef(BaseModel):
    CapacityReservationFleetId: Optional[str] = None
    CancelCapacityReservationFleetError: Optional[       CancelCapacityReservationFleetErrorTypeDef     ] = None

class CancelSpotFleetRequestsErrorItemTypeDef(BaseModel):
    Error: Optional[CancelSpotFleetRequestsErrorTypeDef] = None
    SpotFleetRequestId: Optional[str] = None

class CancelSpotInstanceRequestsResultTypeDef(BaseModel):
    CancelledSpotInstanceRequests: List[CancelledSpotInstanceRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CapacityReservationTypeDef(BaseModel):
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

class DescribeCapacityBlockOfferingsResultTypeDef(BaseModel):
    CapacityBlockOfferings: List[CapacityBlockOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CapacityReservationFleetTypeDef(BaseModel):
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

class CreateCapacityReservationFleetResultTypeDef(BaseModel):
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

class GetGroupsForCapacityReservationResultTypeDef(BaseModel):
    CapacityReservationGroups: List[CapacityReservationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OnDemandOptionsRequestTypeDef(BaseModel):
    AllocationStrategy: Optional[FleetOnDemandAllocationStrategyType] = None
    CapacityReservationOptions: Optional[CapacityReservationOptionsRequestTypeDef] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class OnDemandOptionsTypeDef(BaseModel):
    AllocationStrategy: Optional[FleetOnDemandAllocationStrategyType] = None
    CapacityReservationOptions: Optional[CapacityReservationOptionsTypeDef] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class CapacityReservationSpecificationResponseTypeDef(BaseModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetResponseTypeDef] = None

class LaunchTemplateCapacityReservationSpecificationResponseTypeDef(BaseModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetResponseTypeDef] = None

class CapacityReservationSpecificationTypeDef(BaseModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetTypeDef] = None

class LaunchTemplateCapacityReservationSpecificationRequestTypeDef(BaseModel):
    CapacityReservationPreference: Optional[CapacityReservationPreferenceType] = None
    CapacityReservationTarget: Optional[CapacityReservationTargetTypeDef] = None

class DescribeVpcClassicLinkDnsSupportResultTypeDef(BaseModel):
    Vpcs: List[ClassicLinkDnsSupportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClassicLinkInstanceTypeDef(BaseModel):
    Groups: Optional[List[GroupIdentifierTypeDef]] = None
    InstanceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None

class ClassicLoadBalancersConfigExtraOutputTypeDef(BaseModel):
    ClassicLoadBalancers: Optional[List[ClassicLoadBalancerTypeDef]] = None

class ClassicLoadBalancersConfigOutputTypeDef(BaseModel):
    ClassicLoadBalancers: Optional[List[ClassicLoadBalancerTypeDef]] = None

class ClassicLoadBalancersConfigTypeDef(BaseModel):
    ClassicLoadBalancers: Optional[Sequence[ClassicLoadBalancerTypeDef]] = None

class ExportClientVpnClientCertificateRevocationListResultTypeDef(BaseModel):
    CertificateRevocationList: str
    Status: ClientCertificateRevocationListStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClientConnectResponseOptionsTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    LambdaFunctionArn: Optional[str] = None
    Status: Optional[ClientVpnEndpointAttributeStatusTypeDef] = None

class ClientVpnAuthenticationRequestTypeDef(BaseModel):
    Type: Optional[ClientVpnAuthenticationTypeType] = None
    ActiveDirectory: Optional[DirectoryServiceAuthenticationRequestTypeDef] = None
    MutualAuthentication: Optional[CertificateAuthenticationRequestTypeDef] = None
    FederatedAuthentication: Optional[FederatedAuthenticationRequestTypeDef] = None

class ClientVpnAuthenticationTypeDef(BaseModel):
    Type: Optional[ClientVpnAuthenticationTypeType] = None
    ActiveDirectory: Optional[DirectoryServiceAuthenticationTypeDef] = None
    MutualAuthentication: Optional[CertificateAuthenticationTypeDef] = None
    FederatedAuthentication: Optional[FederatedAuthenticationTypeDef] = None

class ClientVpnConnectionTypeDef(BaseModel):
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

class TerminateConnectionStatusTypeDef(BaseModel):
    ConnectionId: Optional[str] = None
    PreviousStatus: Optional[ClientVpnConnectionStatusTypeDef] = None
    CurrentStatus: Optional[ClientVpnConnectionStatusTypeDef] = None

class CreateClientVpnEndpointResultTypeDef(BaseModel):
    ClientVpnEndpointId: str
    Status: ClientVpnEndpointStatusTypeDef
    DnsName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClientVpnEndpointResultTypeDef(BaseModel):
    Status: ClientVpnEndpointStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClientVpnRouteTypeDef(BaseModel):
    ClientVpnEndpointId: Optional[str] = None
    DestinationCidr: Optional[str] = None
    TargetSubnet: Optional[str] = None
    Type: Optional[str] = None
    Origin: Optional[str] = None
    Status: Optional[ClientVpnRouteStatusTypeDef] = None
    Description: Optional[str] = None

class CreateClientVpnRouteResultTypeDef(BaseModel):
    Status: ClientVpnRouteStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClientVpnRouteResultTypeDef(BaseModel):
    Status: ClientVpnRouteStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VpnTunnelLogOptionsSpecificationTypeDef(BaseModel):
    CloudWatchLogOptions: Optional[CloudWatchLogOptionsSpecificationTypeDef] = None

class VpnTunnelLogOptionsTypeDef(BaseModel):
    CloudWatchLogOptions: Optional[CloudWatchLogOptionsTypeDef] = None

class GetCoipPoolUsageResultTypeDef(BaseModel):
    CoipPoolId: str
    CoipAddressUsages: List[CoipAddressUsageTypeDef]
    LocalGatewayRouteTableId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCoipCidrResultTypeDef(BaseModel):
    CoipCidr: CoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCoipCidrResultTypeDef(BaseModel):
    CoipCidr: CoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcEndpointConnectionNotificationResultTypeDef(BaseModel):
    ConnectionNotification: ConnectionNotificationTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointConnectionNotificationsResultTypeDef(BaseModel):
    ConnectionNotificationSet: List[ConnectionNotificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyInstanceEventWindowRequestRequestTypeDef(BaseModel):
    InstanceEventWindowId: str
    DryRun: Optional[bool] = None
    Name: Optional[str] = None
    TimeRanges: Optional[Sequence[InstanceEventWindowTimeRangeRequestTypeDef]] = None
    CronExpression: Optional[str] = None

class ModifyIpamPoolRequestRequestTypeDef(BaseModel):
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

class CreateLocalGatewayRouteResultTypeDef(BaseModel):
    Route: LocalGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteResultTypeDef(BaseModel):
    Route: LocalGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyLocalGatewayRouteResultTypeDef(BaseModel):
    Route: LocalGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchLocalGatewayRoutesResultTypeDef(BaseModel):
    Routes: List[LocalGatewayRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef(BaseModel):
    Egress: bool
    Protocol: str
    RuleAction: RuleActionType
    RuleNumber: int
    CidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None

class CreateNetworkAclEntryRequestRequestTypeDef(BaseModel):
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

class NetworkAclEntryTypeDef(BaseModel):
    CidrBlock: Optional[str] = None
    Egress: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None
    Protocol: Optional[str] = None
    RuleAction: Optional[RuleActionType] = None
    RuleNumber: Optional[int] = None

class ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef(BaseModel):
    Egress: bool
    Protocol: str
    RuleAction: RuleActionType
    RuleNumber: int
    CidrBlock: Optional[str] = None
    DryRun: Optional[bool] = None
    IcmpTypeCode: Optional[IcmpTypeCodeTypeDef] = None
    Ipv6CidrBlock: Optional[str] = None
    PortRange: Optional[PortRangeTypeDef] = None

class ReplaceNetworkAclEntryRequestRequestTypeDef(BaseModel):
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

class CreateReservedInstancesListingRequestRequestTypeDef(BaseModel):
    ClientToken: str
    InstanceCount: int
    PriceSchedules: Sequence[PriceScheduleSpecificationTypeDef]
    ReservedInstancesId: str

class CreateStoreImageTaskRequestRequestTypeDef(BaseModel):
    ImageId: str
    Bucket: str
    S3ObjectTags: Optional[Sequence[S3ObjectTagTypeDef]] = None
    DryRun: Optional[bool] = None

class ModifyTrafficMirrorFilterRuleRequestRequestTypeDef(BaseModel):
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

class ModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef(BaseModel):
    VerifiedAccessEndpointId: str
    PolicyEnabled: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class ModifyVerifiedAccessGroupPolicyRequestRequestTypeDef(BaseModel):
    VerifiedAccessGroupId: str
    PolicyEnabled: Optional[bool] = None
    PolicyDocument: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class CreateVolumePermissionModificationsTypeDef(BaseModel):
    Add: Optional[Sequence[CreateVolumePermissionTypeDef]] = None
    Remove: Optional[Sequence[CreateVolumePermissionTypeDef]] = None

class ModifyVpcEndpointRequestRequestTypeDef(BaseModel):
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

class GetAwsNetworkPerformanceDataRequestRequestTypeDef(BaseModel):
    DataQueries: Optional[Sequence[DataQueryTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DataResponseTypeDef(BaseModel):
    Id: Optional[str] = None
    Source: Optional[str] = None
    Destination: Optional[str] = None
    Metric: Optional[Literal["aggregate-latency"]] = None
    Statistic: Optional[Literal["p50"]] = None
    Period: Optional[PeriodTypeType] = None
    MetricPoints: Optional[List[MetricPointTypeDef]] = None

class DeleteFleetErrorItemTypeDef(BaseModel):
    Error: Optional[DeleteFleetErrorTypeDef] = None
    FleetId: Optional[str] = None

class DeleteInstanceEventWindowResultTypeDef(BaseModel):
    InstanceEventWindowState: InstanceEventWindowStateChangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchTemplateVersionsResponseErrorItemTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None
    ResponseError: Optional[ResponseErrorTypeDef] = None

class FailedQueuedPurchaseDeletionTypeDef(BaseModel):
    Error: Optional[DeleteQueuedReservedInstancesErrorTypeDef] = None
    ReservedInstancesId: Optional[str] = None

class DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef(BaseModel):
    InstanceTagAttribute: DeregisterInstanceTagAttributeRequestTypeDef
    DryRun: Optional[bool] = None

class DeregisterInstanceEventNotificationAttributesResultTypeDef(BaseModel):
    InstanceTagAttribute: InstanceTagNotificationAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceEventNotificationAttributesResultTypeDef(BaseModel):
    InstanceTagAttribute: InstanceTagNotificationAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterInstanceEventNotificationAttributesResultTypeDef(BaseModel):
    InstanceTagAttribute: InstanceTagNotificationAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTransitGatewayMulticastGroupMembersResultTypeDef(BaseModel):
    DeregisteredMulticastGroupMembers: TransitGatewayMulticastDeregisteredGroupMembersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef(BaseModel):
    DeregisteredMulticastGroupSources: TransitGatewayMulticastDeregisteredGroupSourcesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressTransfersRequestDescribeAddressTransfersPaginateTypeDef(BaseModel):
    AllocationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAddressesAttributeRequestDescribeAddressesAttributePaginateTypeDef(BaseModel):
    AllocationIds: Optional[Sequence[str]] = None
    Attribute: Optional[Literal["domain-name"]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeByoipCidrsRequestDescribeByoipCidrsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCapacityBlockOfferingsRequestDescribeCapacityBlockOfferingsPaginateTypeDef(BaseModel):
    InstanceType: str
    InstanceCount: int
    CapacityDurationHours: int
    DryRun: Optional[bool] = None
    StartDateRange: Optional[TimestampTypeDef] = None
    EndDateRange: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePrincipalIdFormatRequestDescribePrincipalIdFormatPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Resources: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotFleetInstancesRequestDescribeSpotFleetInstancesPaginateTypeDef(BaseModel):
    SpotFleetRequestId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotFleetRequestsRequestDescribeSpotFleetRequestsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    SpotFleetRequestIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStaleSecurityGroupsRequestDescribeStaleSecurityGroupsPaginateTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcClassicLinkDnsSupportRequestDescribeVpcClassicLinkDnsSupportPaginateTypeDef(BaseModel):
    VpcIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAssociatedIpv6PoolCidrsRequestGetAssociatedIpv6PoolCidrsPaginateTypeDef(BaseModel):
    PoolId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetAwsNetworkPerformanceDataRequestGetAwsNetworkPerformanceDataPaginateTypeDef(BaseModel):
    DataQueries: Optional[Sequence[DataQueryTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetGroupsForCapacityReservationRequestGetGroupsForCapacityReservationPaginateTypeDef(BaseModel):
    CapacityReservationId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamAddressHistoryRequestGetIpamAddressHistoryPaginateTypeDef(BaseModel):
    Cidr: str
    IpamScopeId: str
    DryRun: Optional[bool] = None
    VpcId: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetManagedPrefixListAssociationsRequestGetManagedPrefixListAssociationsPaginateTypeDef(BaseModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetManagedPrefixListEntriesRequestGetManagedPrefixListEntriesPaginateTypeDef(BaseModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    TargetVersion: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetNetworkInsightsAccessScopeAnalysisFindingsRequestGetNetworkInsightsAccessScopeAnalysisFindingsPaginateTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: str
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetVpnConnectionDeviceTypesRequestGetVpnConnectionDeviceTypesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImagesInRecycleBinRequestListImagesInRecycleBinPaginateTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSnapshotsInRecycleBinRequestListSnapshotsInRecycleBinPaginateTypeDef(BaseModel):
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAddressesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PublicIps: Optional[Sequence[str]] = None
    AllocationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeAvailabilityZonesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ZoneNames: Optional[Sequence[str]] = None
    ZoneIds: Optional[Sequence[str]] = None
    AllAvailabilityZones: Optional[bool] = None
    DryRun: Optional[bool] = None

class DescribeAwsNetworkPerformanceMetricSubscriptionsRequestDescribeAwsNetworkPerformanceMetricSubscriptionsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeBundleTasksRequestRequestTypeDef(BaseModel):
    BundleIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCapacityReservationFleetsRequestRequestTypeDef(BaseModel):
    CapacityReservationFleetIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCapacityReservationsRequestDescribeCapacityReservationsPaginateTypeDef(BaseModel):
    CapacityReservationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCapacityReservationsRequestRequestTypeDef(BaseModel):
    CapacityReservationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCarrierGatewaysRequestDescribeCarrierGatewaysPaginateTypeDef(BaseModel):
    CarrierGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCarrierGatewaysRequestRequestTypeDef(BaseModel):
    CarrierGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeClassicLinkInstancesRequestDescribeClassicLinkInstancesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClassicLinkInstancesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeClientVpnAuthorizationRulesRequestDescribeClientVpnAuthorizationRulesPaginateTypeDef(BaseModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnAuthorizationRulesRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None

class DescribeClientVpnConnectionsRequestDescribeClientVpnConnectionsPaginateTypeDef(BaseModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnConnectionsRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class DescribeClientVpnEndpointsRequestDescribeClientVpnEndpointsPaginateTypeDef(BaseModel):
    ClientVpnEndpointIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnEndpointsRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeClientVpnRoutesRequestDescribeClientVpnRoutesPaginateTypeDef(BaseModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnRoutesRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeClientVpnTargetNetworksRequestDescribeClientVpnTargetNetworksPaginateTypeDef(BaseModel):
    ClientVpnEndpointId: str
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClientVpnTargetNetworksRequestRequestTypeDef(BaseModel):
    ClientVpnEndpointId: str
    AssociationIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeCoipPoolsRequestDescribeCoipPoolsPaginateTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCoipPoolsRequestRequestTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeCustomerGatewaysRequestRequestTypeDef(BaseModel):
    CustomerGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeDhcpOptionsRequestDescribeDhcpOptionsPaginateTypeDef(BaseModel):
    DhcpOptionsIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDhcpOptionsRequestRequestTypeDef(BaseModel):
    DhcpOptionsIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeEgressOnlyInternetGatewaysRequestDescribeEgressOnlyInternetGatewaysPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    EgressOnlyInternetGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    EgressOnlyInternetGatewayIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeElasticGpusRequestRequestTypeDef(BaseModel):
    ElasticGpuIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeExportImageTasksRequestDescribeExportImageTasksPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ExportImageTaskIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportImageTasksRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ExportImageTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeExportTasksRequestRequestTypeDef(BaseModel):
    ExportTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeFastLaunchImagesRequestDescribeFastLaunchImagesPaginateTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFastLaunchImagesRequestRequestTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeFastSnapshotRestoresRequestDescribeFastSnapshotRestoresPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFastSnapshotRestoresRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeFleetInstancesRequestRequestTypeDef(BaseModel):
    FleetId: str
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeFleetsRequestDescribeFleetsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    FleetIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFleetsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    FleetIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeFlowLogsRequestDescribeFlowLogsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FlowLogIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFlowLogsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    FlowLogIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeFpgaImagesRequestDescribeFpgaImagesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    FpgaImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeFpgaImagesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    FpgaImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeHostReservationOfferingsRequestDescribeHostReservationOfferingsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxDuration: Optional[int] = None
    MinDuration: Optional[int] = None
    OfferingId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHostReservationOfferingsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxDuration: Optional[int] = None
    MaxResults: Optional[int] = None
    MinDuration: Optional[int] = None
    NextToken: Optional[str] = None
    OfferingId: Optional[str] = None

class DescribeHostReservationsRequestDescribeHostReservationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostReservationIdSet: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHostReservationsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostReservationIdSet: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeHostsRequestDescribeHostsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeHostsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeIamInstanceProfileAssociationsRequestDescribeIamInstanceProfileAssociationsPaginateTypeDef(BaseModel):
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIamInstanceProfileAssociationsRequestRequestTypeDef(BaseModel):
    AssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImagesRequestDescribeImagesPaginateTypeDef(BaseModel):
    ExecutableUsers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesRequestRequestTypeDef(BaseModel):
    ExecutableUsers: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImageIds: Optional[Sequence[str]] = None
    Owners: Optional[Sequence[str]] = None
    IncludeDeprecated: Optional[bool] = None
    IncludeDisabled: Optional[bool] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImportImageTasksRequestDescribeImportImageTasksPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImportImageTasksRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImportSnapshotTasksRequestDescribeImportSnapshotTasksPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImportSnapshotTasksRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceConnectEndpointsRequestDescribeInstanceConnectEndpointsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceConnectEndpointIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceConnectEndpointsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceConnectEndpointIds: Optional[Sequence[str]] = None

class DescribeInstanceCreditSpecificationsRequestDescribeInstanceCreditSpecificationsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceCreditSpecificationsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceEventWindowsRequestDescribeInstanceEventWindowsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    InstanceEventWindowIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceEventWindowsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    InstanceEventWindowIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceStatusRequestDescribeInstanceStatusPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceStatusRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None

class DescribeInstanceTopologyRequestDescribeInstanceTopologyPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    InstanceIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceTopologyRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    InstanceIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeInstanceTypeOfferingsRequestDescribeInstanceTypeOfferingsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    LocationType: Optional[LocationTypeType] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceTypeOfferingsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    LocationType: Optional[LocationTypeType] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceTypesRequestDescribeInstanceTypesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstanceTypesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstancesRequestDescribeInstancesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInstancesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInternetGatewaysRequestDescribeInternetGatewaysPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeInternetGatewaysRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeIpamPoolsRequestDescribeIpamPoolsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamPoolIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamPoolsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamPoolIds: Optional[Sequence[str]] = None

class DescribeIpamResourceDiscoveriesRequestDescribeIpamResourceDiscoveriesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamResourceDiscoveriesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeIpamResourceDiscoveryAssociationsRequestDescribeIpamResourceDiscoveryAssociationsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    IpamResourceDiscoveryAssociationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeIpamScopesRequestDescribeIpamScopesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamScopeIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamScopesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamScopeIds: Optional[Sequence[str]] = None

class DescribeIpamsRequestDescribeIpamsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpamsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    IpamIds: Optional[Sequence[str]] = None

class DescribeIpv6PoolsRequestDescribeIpv6PoolsPaginateTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpv6PoolsRequestRequestTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeKeyPairsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    KeyNames: Optional[Sequence[str]] = None
    KeyPairIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    IncludePublicKey: Optional[bool] = None

class DescribeLaunchTemplateVersionsRequestDescribeLaunchTemplateVersionsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    Versions: Optional[Sequence[str]] = None
    MinVersion: Optional[str] = None
    MaxVersion: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ResolveAlias: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchTemplateVersionsRequestRequestTypeDef(BaseModel):
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

class DescribeLaunchTemplatesRequestDescribeLaunchTemplatesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    LaunchTemplateIds: Optional[Sequence[str]] = None
    LaunchTemplateNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLaunchTemplatesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    LaunchTemplateIds: Optional[Sequence[str]] = None
    LaunchTemplateNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestDescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginateTypeDef(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayRouteTableVpcAssociationsRequestDescribeLocalGatewayRouteTableVpcAssociationsPaginateTypeDef(BaseModel):
    LocalGatewayRouteTableVpcAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableVpcAssociationIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayRouteTablesRequestDescribeLocalGatewayRouteTablesPaginateTypeDef(BaseModel):
    LocalGatewayRouteTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayRouteTablesRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayVirtualInterfaceGroupsRequestDescribeLocalGatewayVirtualInterfaceGroupsPaginateTypeDef(BaseModel):
    LocalGatewayVirtualInterfaceGroupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef(BaseModel):
    LocalGatewayVirtualInterfaceGroupIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewayVirtualInterfacesRequestDescribeLocalGatewayVirtualInterfacesPaginateTypeDef(BaseModel):
    LocalGatewayVirtualInterfaceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef(BaseModel):
    LocalGatewayVirtualInterfaceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLocalGatewaysRequestDescribeLocalGatewaysPaginateTypeDef(BaseModel):
    LocalGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLocalGatewaysRequestRequestTypeDef(BaseModel):
    LocalGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeLockedSnapshotsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeMacHostsRequestDescribeMacHostsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMacHostsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    HostIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeManagedPrefixListsRequestDescribeManagedPrefixListsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PrefixListIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeManagedPrefixListsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PrefixListIds: Optional[Sequence[str]] = None

class DescribeMovingAddressesRequestDescribeMovingAddressesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PublicIps: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMovingAddressesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PublicIps: Optional[Sequence[str]] = None

class DescribeNatGatewaysRequestDescribeNatGatewaysPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNatGatewaysRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeNetworkAclsRequestDescribeNetworkAclsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkAclIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkAclsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkAclIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeNetworkInsightsAccessScopeAnalysesRequestDescribeNetworkInsightsAccessScopeAnalysesPaginateTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    AnalysisStartTimeBegin: Optional[TimestampTypeDef] = None
    AnalysisStartTimeEnd: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    AnalysisStartTimeBegin: Optional[TimestampTypeDef] = None
    AnalysisStartTimeEnd: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInsightsAccessScopesRequestDescribeNetworkInsightsAccessScopesPaginateTypeDef(BaseModel):
    NetworkInsightsAccessScopeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsAccessScopesRequestRequestTypeDef(BaseModel):
    NetworkInsightsAccessScopeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInsightsAnalysesRequestDescribeNetworkInsightsAnalysesPaginateTypeDef(BaseModel):
    NetworkInsightsAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsPathId: Optional[str] = None
    AnalysisStartTime: Optional[TimestampTypeDef] = None
    AnalysisEndTime: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsAnalysesRequestRequestTypeDef(BaseModel):
    NetworkInsightsAnalysisIds: Optional[Sequence[str]] = None
    NetworkInsightsPathId: Optional[str] = None
    AnalysisStartTime: Optional[TimestampTypeDef] = None
    AnalysisEndTime: Optional[TimestampTypeDef] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInsightsPathsRequestDescribeNetworkInsightsPathsPaginateTypeDef(BaseModel):
    NetworkInsightsPathIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInsightsPathsRequestRequestTypeDef(BaseModel):
    NetworkInsightsPathIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None

class DescribeNetworkInterfacePermissionsRequestDescribeNetworkInterfacePermissionsPaginateTypeDef(BaseModel):
    NetworkInterfacePermissionIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInterfacePermissionsRequestRequestTypeDef(BaseModel):
    NetworkInterfacePermissionIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeNetworkInterfacesRequestDescribeNetworkInterfacesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeNetworkInterfacesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribePlacementGroupsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    GroupNames: Optional[Sequence[str]] = None
    GroupIds: Optional[Sequence[str]] = None

class DescribePrefixListsRequestDescribePrefixListsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PrefixListIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePrefixListsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PrefixListIds: Optional[Sequence[str]] = None

class DescribePublicIpv4PoolsRequestDescribePublicIpv4PoolsPaginateTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePublicIpv4PoolsRequestRequestTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeRegionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    RegionNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    AllRegions: Optional[bool] = None

class DescribeReplaceRootVolumeTasksRequestDescribeReplaceRootVolumeTasksPaginateTypeDef(BaseModel):
    ReplaceRootVolumeTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplaceRootVolumeTasksRequestRequestTypeDef(BaseModel):
    ReplaceRootVolumeTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeReservedInstancesListingsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ReservedInstancesId: Optional[str] = None
    ReservedInstancesListingId: Optional[str] = None

class DescribeReservedInstancesModificationsRequestDescribeReservedInstancesModificationsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ReservedInstancesModificationIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedInstancesModificationsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ReservedInstancesModificationIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class DescribeReservedInstancesOfferingsRequestDescribeReservedInstancesOfferingsPaginateTypeDef(BaseModel):
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

class DescribeReservedInstancesOfferingsRequestRequestTypeDef(BaseModel):
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

class DescribeReservedInstancesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    OfferingClass: Optional[OfferingClassTypeType] = None
    ReservedInstancesIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    OfferingType: Optional[OfferingTypeValuesType] = None

class DescribeRouteTablesRequestDescribeRouteTablesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    RouteTableIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRouteTablesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    RouteTableIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSecurityGroupRulesRequestDescribeSecurityGroupRulesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSecurityGroupRulesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSecurityGroupsRequestDescribeSecurityGroupsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    GroupIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSecurityGroupsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    GroupIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSnapshotTierStatusRequestDescribeSnapshotTierStatusPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotTierStatusRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    OwnerIds: Optional[Sequence[str]] = None
    RestorableByUserIds: Optional[Sequence[str]] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerIds: Optional[Sequence[str]] = None
    RestorableByUserIds: Optional[Sequence[str]] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeSpotInstanceRequestsRequestDescribeSpotInstanceRequestsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotInstanceRequestsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSpotPriceHistoryRequestDescribeSpotPriceHistoryPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    ProductDescriptions: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSpotPriceHistoryRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DryRun: Optional[bool] = None
    EndTime: Optional[TimestampTypeDef] = None
    InstanceTypes: Optional[Sequence[InstanceTypeType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ProductDescriptions: Optional[Sequence[str]] = None
    StartTime: Optional[TimestampTypeDef] = None

class DescribeStoreImageTasksRequestDescribeStoreImageTasksPaginateTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeStoreImageTasksRequestRequestTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeSubnetsRequestDescribeSubnetsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubnetsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeTagsRequestDescribeTagsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTagsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorFilterRulesRequestRequestTypeDef(BaseModel):
    TrafficMirrorFilterRuleIds: Optional[Sequence[str]] = None
    TrafficMirrorFilterId: Optional[str] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorFiltersRequestDescribeTrafficMirrorFiltersPaginateTypeDef(BaseModel):
    TrafficMirrorFilterIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrafficMirrorFiltersRequestRequestTypeDef(BaseModel):
    TrafficMirrorFilterIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorSessionsRequestDescribeTrafficMirrorSessionsPaginateTypeDef(BaseModel):
    TrafficMirrorSessionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrafficMirrorSessionsRequestRequestTypeDef(BaseModel):
    TrafficMirrorSessionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTrafficMirrorTargetsRequestDescribeTrafficMirrorTargetsPaginateTypeDef(BaseModel):
    TrafficMirrorTargetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrafficMirrorTargetsRequestRequestTypeDef(BaseModel):
    TrafficMirrorTargetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeTransitGatewayAttachmentsRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayConnectPeersRequestDescribeTransitGatewayConnectPeersPaginateTypeDef(BaseModel):
    TransitGatewayConnectPeerIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayConnectPeersRequestRequestTypeDef(BaseModel):
    TransitGatewayConnectPeerIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayConnectsRequestDescribeTransitGatewayConnectsPaginateTypeDef(BaseModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayConnectsRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayMulticastDomainsRequestDescribeTransitGatewayMulticastDomainsPaginateTypeDef(BaseModel):
    TransitGatewayMulticastDomainIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayPeeringAttachmentsRequestDescribeTransitGatewayPeeringAttachmentsPaginateTypeDef(BaseModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayPolicyTablesRequestDescribeTransitGatewayPolicyTablesPaginateTypeDef(BaseModel):
    TransitGatewayPolicyTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayPolicyTablesRequestRequestTypeDef(BaseModel):
    TransitGatewayPolicyTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayRouteTableAnnouncementsRequestDescribeTransitGatewayRouteTableAnnouncementsPaginateTypeDef(BaseModel):
    TransitGatewayRouteTableAnnouncementIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableAnnouncementIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayRouteTablesRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewayVpcAttachmentsRequestDescribeTransitGatewayVpcAttachmentsPaginateTypeDef(BaseModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTransitGatewaysRequestDescribeTransitGatewaysPaginateTypeDef(BaseModel):
    TransitGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTransitGatewaysRequestRequestTypeDef(BaseModel):
    TransitGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeTrunkInterfaceAssociationsRequestDescribeTrunkInterfaceAssociationsPaginateTypeDef(BaseModel):
    AssociationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrunkInterfaceAssociationsRequestRequestTypeDef(BaseModel):
    AssociationIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVerifiedAccessEndpointsRequestDescribeVerifiedAccessEndpointsPaginateTypeDef(BaseModel):
    VerifiedAccessEndpointIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessEndpointsRequestRequestTypeDef(BaseModel):
    VerifiedAccessEndpointIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    VerifiedAccessGroupId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessGroupsRequestDescribeVerifiedAccessGroupsPaginateTypeDef(BaseModel):
    VerifiedAccessGroupIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessGroupsRequestRequestTypeDef(BaseModel):
    VerifiedAccessGroupIds: Optional[Sequence[str]] = None
    VerifiedAccessInstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessInstanceLoggingConfigurationsRequestDescribeVerifiedAccessInstanceLoggingConfigurationsPaginateTypeDef(BaseModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessInstancesRequestDescribeVerifiedAccessInstancesPaginateTypeDef(BaseModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessInstancesRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVerifiedAccessTrustProvidersRequestDescribeVerifiedAccessTrustProvidersPaginateTypeDef(BaseModel):
    VerifiedAccessTrustProviderIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef(BaseModel):
    VerifiedAccessTrustProviderIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class DescribeVolumeStatusRequestDescribeVolumeStatusPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVolumeStatusRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class DescribeVolumesModificationsRequestDescribeVolumesModificationsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVolumesModificationsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    VolumeIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVolumesRequestDescribeVolumesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVolumesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcClassicLinkRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcIds: Optional[Sequence[str]] = None

class DescribeVpcEndpointConnectionNotificationsRequestDescribeVpcEndpointConnectionNotificationsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    ConnectionNotificationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    ConnectionNotificationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointConnectionsRequestDescribeVpcEndpointConnectionsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointConnectionsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointServiceConfigurationsRequestDescribeVpcEndpointServiceConfigurationsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    ServiceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    ServiceIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointServicePermissionsRequestDescribeVpcEndpointServicePermissionsPaginateTypeDef(BaseModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointServicePermissionsRequestRequestTypeDef(BaseModel):
    ServiceId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointServicesRequestDescribeVpcEndpointServicesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    ServiceNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointServicesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    ServiceNames: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcEndpointsRequestDescribeVpcEndpointsPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    VpcEndpointIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcEndpointsRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    VpcEndpointIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeVpcPeeringConnectionsRequestDescribeVpcPeeringConnectionsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcPeeringConnectionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVpcsRequestDescribeVpcsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeVpcsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeVpnConnectionsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnConnectionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class DescribeVpnGatewaysRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnGatewayIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class ExportTransitGatewayRoutesRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    S3Bucket: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class GetCoipPoolUsageRequestRequestTypeDef(BaseModel):
    PoolId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetIpamDiscoveredAccountsRequestGetIpamDiscoveredAccountsPaginateTypeDef(BaseModel):
    IpamResourceDiscoveryId: str
    DiscoveryRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamDiscoveredAccountsRequestRequestTypeDef(BaseModel):
    IpamResourceDiscoveryId: str
    DiscoveryRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetIpamDiscoveredPublicAddressesRequestRequestTypeDef(BaseModel):
    IpamResourceDiscoveryId: str
    AddressRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetIpamDiscoveredResourceCidrsRequestGetIpamDiscoveredResourceCidrsPaginateTypeDef(BaseModel):
    IpamResourceDiscoveryId: str
    ResourceRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamDiscoveredResourceCidrsRequestRequestTypeDef(BaseModel):
    IpamResourceDiscoveryId: str
    ResourceRegion: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetIpamPoolAllocationsRequestGetIpamPoolAllocationsPaginateTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    IpamPoolAllocationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamPoolAllocationsRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    IpamPoolAllocationId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetIpamPoolCidrsRequestGetIpamPoolCidrsPaginateTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamPoolCidrsRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetIpamResourceCidrsRequestGetIpamResourceCidrsPaginateTypeDef(BaseModel):
    IpamScopeId: str
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IpamPoolId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[IpamResourceTypeType] = None
    ResourceTag: Optional[RequestIpamResourceTagTypeDef] = None
    ResourceOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetIpamResourceCidrsRequestRequestTypeDef(BaseModel):
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

class GetSecurityGroupsForVpcRequestGetSecurityGroupsForVpcPaginateTypeDef(BaseModel):
    VpcId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSecurityGroupsForVpcRequestRequestTypeDef(BaseModel):
    VpcId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None

class GetSubnetCidrReservationsRequestRequestTypeDef(BaseModel):
    SubnetId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetTransitGatewayAttachmentPropagationsRequestGetTransitGatewayAttachmentPropagationsPaginateTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayMulticastDomainAssociationsRequestGetTransitGatewayMulticastDomainAssociationsPaginateTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayPolicyTableAssociationsRequestGetTransitGatewayPolicyTableAssociationsPaginateTypeDef(BaseModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef(BaseModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayPolicyTableEntriesRequestRequestTypeDef(BaseModel):
    TransitGatewayPolicyTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayPrefixListReferencesRequestGetTransitGatewayPrefixListReferencesPaginateTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayPrefixListReferencesRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayRouteTableAssociationsRequestGetTransitGatewayRouteTableAssociationsPaginateTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class GetTransitGatewayRouteTablePropagationsRequestGetTransitGatewayRouteTablePropagationsPaginateTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class SearchLocalGatewayRoutesRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class SearchLocalGatewayRoutesRequestSearchLocalGatewayRoutesPaginateTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTransitGatewayMulticastGroupsRequestRequestTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None

class SearchTransitGatewayMulticastGroupsRequestSearchTransitGatewayMulticastGroupsPaginateTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchTransitGatewayRoutesRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    Filters: Sequence[FilterTypeDef]
    MaxResults: Optional[int] = None
    DryRun: Optional[bool] = None

class DescribeAggregateIdFormatResultTypeDef(BaseModel):
    UseLongIdsAggregated: bool
    Statuses: List[IdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdFormatResultTypeDef(BaseModel):
    Statuses: List[IdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIdentityIdFormatResultTypeDef(BaseModel):
    Statuses: List[IdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PrincipalIdFormatTypeDef(BaseModel):
    Arn: Optional[str] = None
    Statuses: Optional[List[IdFormatTypeDef]] = None

class DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef(BaseModel):
    Subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeBundleTasksRequestBundleTaskCompleteWaitTypeDef(BaseModel):
    BundleIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeConversionTasksRequestConversionTaskCancelledWaitTypeDef(BaseModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeConversionTasksRequestConversionTaskCompletedWaitTypeDef(BaseModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeConversionTasksRequestConversionTaskDeletedWaitTypeDef(BaseModel):
    ConversionTaskIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeCustomerGatewaysRequestCustomerGatewayAvailableWaitTypeDef(BaseModel):
    CustomerGatewayIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeExportTasksRequestExportTaskCancelledWaitTypeDef(BaseModel):
    ExportTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeExportTasksRequestExportTaskCompletedWaitTypeDef(BaseModel):
    ExportTaskIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeImagesRequestImageAvailableWaitTypeDef(BaseModel):
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

class DescribeImagesRequestImageExistsWaitTypeDef(BaseModel):
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

class DescribeImportSnapshotTasksRequestSnapshotImportedWaitTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ImportTaskIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstanceStatusRequestInstanceStatusOkWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstanceStatusRequestSystemStatusOkWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DryRun: Optional[bool] = None
    IncludeAllInstances: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceExistsWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceRunningWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceStoppedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInstancesRequestInstanceTerminatedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    InstanceIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeInternetGatewaysRequestInternetGatewayExistsWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    InternetGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeKeyPairsRequestKeyPairExistsWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    KeyNames: Optional[Sequence[str]] = None
    KeyPairIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    IncludePublicKey: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNatGatewaysRequestNatGatewayAvailableWaitTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNatGatewaysRequestNatGatewayDeletedWaitTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NatGatewayIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeNetworkInterfacesRequestNetworkInterfaceAvailableWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    NetworkInterfaceIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSecurityGroupsRequestSecurityGroupExistsWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    GroupIds: Optional[Sequence[str]] = None
    GroupNames: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSnapshotsRequestSnapshotCompletedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    OwnerIds: Optional[Sequence[str]] = None
    RestorableByUserIds: Optional[Sequence[str]] = None
    SnapshotIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSpotInstanceRequestsRequestSpotInstanceRequestFulfilledWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    SpotInstanceRequestIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeStoreImageTasksRequestStoreImageTaskCompleteWaitTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeSubnetsRequestSubnetAvailableWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    SubnetIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVolumesRequestVolumeAvailableWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVolumesRequestVolumeDeletedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVolumesRequestVolumeInUseWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VolumeIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionDeletedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcPeeringConnectionsRequestVpcPeeringConnectionExistsWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DryRun: Optional[bool] = None
    VpcPeeringConnectionIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcsRequestVpcAvailableWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpcsRequestVpcExistsWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpcIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpnConnectionsRequestVpnConnectionAvailableWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnConnectionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeVpnConnectionsRequestVpnConnectionDeletedWaitTypeDef(BaseModel):
    Filters: Optional[Sequence[FilterTypeDef]] = None
    VpnConnectionIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetPasswordDataRequestPasswordDataAvailableWaitTypeDef(BaseModel):
    InstanceId: str
    DryRun: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeFastLaunchImagesSuccessItemTypeDef(BaseModel):
    ImageId: Optional[str] = None
    ResourceType: Optional[Literal["snapshot"]] = None
    SnapshotConfiguration: Optional[FastLaunchSnapshotConfigurationResponseTypeDef] = None
    LaunchTemplate: Optional[FastLaunchLaunchTemplateSpecificationResponseTypeDef] = None
    MaxParallelLaunches: Optional[int] = None
    OwnerId: Optional[str] = None
    State: Optional[FastLaunchStateCodeType] = None
    StateTransitionReason: Optional[str] = None
    StateTransitionTime: Optional[datetime] = None

class DisableFastLaunchResultTypeDef(BaseModel):
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

class EnableFastLaunchResultTypeDef(BaseModel):
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

class DescribeFastSnapshotRestoresResultTypeDef(BaseModel):
    FastSnapshotRestores: List[DescribeFastSnapshotRestoreSuccessItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHostReservationOfferingsResultTypeDef(BaseModel):
    OfferingSet: List[HostOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstanceCreditSpecificationsResultTypeDef(BaseModel):
    InstanceCreditSpecifications: List[InstanceCreditSpecificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstanceTopologyResultTypeDef(BaseModel):
    Instances: List[InstanceTopologyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstanceTypeOfferingsResultTypeDef(BaseModel):
    InstanceTypeOfferings: List[InstanceTypeOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLockedSnapshotsResultTypeDef(BaseModel):
    Snapshots: List[LockedSnapshotsInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMacHostsResultTypeDef(BaseModel):
    MacHosts: List[MacHostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeMovingAddressesResultTypeDef(BaseModel):
    MovingAddressStatuses: List[MovingAddressStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePrefixListsResultTypeDef(BaseModel):
    PrefixLists: List[PrefixListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeRegionsResultTypeDef(BaseModel):
    Regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityGroupReferencesResultTypeDef(BaseModel):
    SecurityGroupReferenceSet: List[SecurityGroupReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotAttributeResultTypeDef(BaseModel):
    CreateVolumePermissions: List[CreateVolumePermissionTypeDef]
    ProductCodes: List[ProductCodeTypeDef]
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVolumeAttributeResultTypeDef(BaseModel):
    AutoEnableIO: AttributeBooleanValueTypeDef
    ProductCodes: List[ProductCodeTypeDef]
    VolumeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpotPriceHistoryResultTypeDef(BaseModel):
    SpotPriceHistory: List[SpotPriceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeStoreImageTasksResultTypeDef(BaseModel):
    StoreImageTaskResults: List[StoreImageTaskResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeTagsResultTypeDef(BaseModel):
    Tags: List[TagDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVolumesModificationsResultTypeDef(BaseModel):
    VolumesModifications: List[VolumeModificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVolumeResultTypeDef(BaseModel):
    VolumeModification: VolumeModificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FlowLogTypeDef(BaseModel):
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

class DisableFastSnapshotRestoreStateErrorItemTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    Error: Optional[DisableFastSnapshotRestoreStateErrorTypeDef] = None

class DisableTransitGatewayRouteTablePropagationResultTypeDef(BaseModel):
    Propagation: TransitGatewayPropagationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EnableTransitGatewayRouteTablePropagationResultTypeDef(BaseModel):
    Propagation: TransitGatewayPropagationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DiskImageTypeDef(BaseModel):
    Description: Optional[str] = None
    Image: Optional[DiskImageDetailTypeDef] = None
    Volume: Optional[VolumeDetailTypeDef] = None

class ImportVolumeRequestRequestTypeDef(BaseModel):
    AvailabilityZone: str
    Image: DiskImageDetailTypeDef
    Volume: VolumeDetailTypeDef
    Description: Optional[str] = None
    DryRun: Optional[bool] = None

class ImportInstanceVolumeDetailItemTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    BytesConverted: Optional[int] = None
    Description: Optional[str] = None
    Image: Optional[DiskImageDescriptionTypeDef] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Volume: Optional[DiskImageVolumeDescriptionTypeDef] = None

class ImportVolumeTaskDetailsTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    BytesConverted: Optional[int] = None
    Description: Optional[str] = None
    Image: Optional[DiskImageDescriptionTypeDef] = None
    Volume: Optional[DiskImageVolumeDescriptionTypeDef] = None

class InstanceStorageInfoTypeDef(BaseModel):
    TotalSizeInGB: Optional[int] = None
    Disks: Optional[List[DiskInfoTypeDef]] = None
    NvmeSupport: Optional[EphemeralNvmeSupportType] = None
    EncryptionSupport: Optional[InstanceStorageEncryptionSupportType] = None

class VpcEndpointConnectionTypeDef(BaseModel):
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

class ModifyClientVpnEndpointRequestRequestTypeDef(BaseModel):
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

class EbsInfoTypeDef(BaseModel):
    EbsOptimizedSupport: Optional[EbsOptimizedSupportType] = None
    EncryptionSupport: Optional[EbsEncryptionSupportType] = None
    EbsOptimizedInfo: Optional[EbsOptimizedInfoTypeDef] = None
    NvmeSupport: Optional[EbsNvmeSupportType] = None

class InstanceBlockDeviceMappingSpecificationTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[EbsInstanceBlockDeviceSpecificationTypeDef] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None

class InstanceBlockDeviceMappingTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[EbsInstanceBlockDeviceTypeDef] = None

class EgressOnlyInternetGatewayTypeDef(BaseModel):
    Attachments: Optional[List[InternetGatewayAttachmentTypeDef]] = None
    EgressOnlyInternetGatewayId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class InternetGatewayTypeDef(BaseModel):
    Attachments: Optional[List[InternetGatewayAttachmentTypeDef]] = None
    InternetGatewayId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ElasticGpusTypeDef(BaseModel):
    ElasticGpuId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    ElasticGpuType: Optional[str] = None
    ElasticGpuHealth: Optional[ElasticGpuHealthTypeDef] = None
    ElasticGpuState: Optional[Literal["ATTACHED"]] = None
    InstanceId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class EnaSrdSpecificationRequestTypeDef(BaseModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[EnaSrdUdpSpecificationRequestTypeDef] = None

class EnaSrdSpecificationTypeDef(BaseModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[EnaSrdUdpSpecificationTypeDef] = None

class EnableFastLaunchRequestRequestTypeDef(BaseModel):
    ImageId: str
    ResourceType: Optional[str] = None
    SnapshotConfiguration: Optional[FastLaunchSnapshotConfigurationRequestTypeDef] = None
    LaunchTemplate: Optional[FastLaunchLaunchTemplateSpecificationRequestTypeDef] = None
    MaxParallelLaunches: Optional[int] = None
    DryRun: Optional[bool] = None

class EnableFastSnapshotRestoreStateErrorItemTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    Error: Optional[EnableFastSnapshotRestoreStateErrorTypeDef] = None

class HistoryRecordEntryTypeDef(BaseModel):
    EventInformation: Optional[EventInformationTypeDef] = None
    EventType: Optional[FleetEventTypeType] = None
    Timestamp: Optional[datetime] = None

class HistoryRecordTypeDef(BaseModel):
    EventInformation: Optional[EventInformationTypeDef] = None
    EventType: Optional[EventTypeType] = None
    Timestamp: Optional[datetime] = None

class ExportImageResultTypeDef(BaseModel):
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

class ExportImageTaskTypeDef(BaseModel):
    Description: Optional[str] = None
    ExportImageTaskId: Optional[str] = None
    ImageId: Optional[str] = None
    Progress: Optional[str] = None
    S3ExportLocation: Optional[ExportTaskS3LocationTypeDef] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class ExportTaskTypeDef(BaseModel):
    Description: Optional[str] = None
    ExportTaskId: Optional[str] = None
    ExportToS3Task: Optional[ExportToS3TaskTypeDef] = None
    InstanceExportDetails: Optional[InstanceExportDetailsTypeDef] = None
    State: Optional[ExportTaskStateType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class PathFilterTypeDef(BaseModel):
    SourceAddress: Optional[str] = None
    SourcePortRange: Optional[FilterPortRangeTypeDef] = None
    DestinationAddress: Optional[str] = None
    DestinationPortRange: Optional[FilterPortRangeTypeDef] = None

class FleetSpotMaintenanceStrategiesRequestTypeDef(BaseModel):
    CapacityRebalance: Optional[FleetSpotCapacityRebalanceRequestTypeDef] = None

class FleetSpotMaintenanceStrategiesTypeDef(BaseModel):
    CapacityRebalance: Optional[FleetSpotCapacityRebalanceTypeDef] = None

class FpgaDeviceInfoTypeDef(BaseModel):
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    Count: Optional[int] = None
    MemoryInfo: Optional[FpgaDeviceMemoryInfoTypeDef] = None

class FpgaImageAttributeTypeDef(BaseModel):
    FpgaImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    LoadPermissions: Optional[List[LoadPermissionTypeDef]] = None
    ProductCodes: Optional[List[ProductCodeTypeDef]] = None

class FpgaImageTypeDef(BaseModel):
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

class GetAssociatedIpv6PoolCidrsResultTypeDef(BaseModel):
    Ipv6CidrAssociations: List[Ipv6CidrAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCapacityReservationUsageResultTypeDef(BaseModel):
    CapacityReservationId: str
    InstanceType: str
    TotalInstanceCount: int
    AvailableInstanceCount: int
    State: CapacityReservationStateType
    InstanceUsages: List[InstanceUsageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDefaultCreditSpecificationResultTypeDef(BaseModel):
    InstanceFamilyCreditSpecification: InstanceFamilyCreditSpecificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDefaultCreditSpecificationResultTypeDef(BaseModel):
    InstanceFamilyCreditSpecification: InstanceFamilyCreditSpecificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetHostReservationPurchasePreviewResultTypeDef(BaseModel):
    CurrencyCode: Literal["USD"]
    Purchase: List[PurchaseTypeDef]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseHostReservationResultTypeDef(BaseModel):
    ClientToken: str
    CurrencyCode: Literal["USD"]
    Purchase: List[PurchaseTypeDef]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceMetadataDefaultsResultTypeDef(BaseModel):
    AccountLevel: InstanceMetadataDefaultsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetInstanceTypesFromInstanceRequirementsResultTypeDef(BaseModel):
    InstanceTypes: List[InstanceTypeInfoFromInstanceRequirementsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamAddressHistoryResultTypeDef(BaseModel):
    HistoryRecords: List[IpamAddressHistoryRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetManagedPrefixListAssociationsResultTypeDef(BaseModel):
    PrefixListAssociations: List[PrefixListAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetManagedPrefixListEntriesResultTypeDef(BaseModel):
    Entries: List[PrefixListEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ReservedInstanceReservationValueTypeDef(BaseModel):
    ReservationValue: Optional[ReservationValueTypeDef] = None
    ReservedInstanceId: Optional[str] = None

class GetSpotPlacementScoresResultTypeDef(BaseModel):
    SpotPlacementScores: List[SpotPlacementScoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayAttachmentPropagationsResultTypeDef(BaseModel):
    TransitGatewayAttachmentPropagations: List[TransitGatewayAttachmentPropagationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayRouteTableAssociationsResultTypeDef(BaseModel):
    Associations: List[TransitGatewayRouteTableAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayRouteTablePropagationsResultTypeDef(BaseModel):
    TransitGatewayRouteTablePropagations: List[TransitGatewayRouteTablePropagationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetVpnConnectionDeviceTypesResultTypeDef(BaseModel):
    VpnConnectionDeviceTypes: List[VpnConnectionDeviceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetVpnTunnelReplacementStatusResultTypeDef(BaseModel):
    VpnConnectionId: str
    TransitGatewayId: str
    CustomerGatewayId: str
    VpnGatewayId: str
    VpnTunnelOutsideIpAddress: str
    MaintenanceDetails: MaintenanceDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GpuDeviceInfoTypeDef(BaseModel):
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    Count: Optional[int] = None
    MemoryInfo: Optional[GpuDeviceMemoryInfoTypeDef] = None

class IamInstanceProfileAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    InstanceId: Optional[str] = None
    IamInstanceProfile: Optional[IamInstanceProfileTypeDef] = None
    State: Optional[IamInstanceProfileAssociationStateType] = None
    Timestamp: Optional[datetime] = None

class LaunchPermissionModificationsTypeDef(BaseModel):
    Add: Optional[Sequence[LaunchPermissionTypeDef]] = None
    Remove: Optional[Sequence[LaunchPermissionTypeDef]] = None

class ImageDiskContainerTypeDef(BaseModel):
    Description: Optional[str] = None
    DeviceName: Optional[str] = None
    Format: Optional[str] = None
    SnapshotId: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucketTypeDef] = None

class SnapshotDiskContainerTypeDef(BaseModel):
    Description: Optional[str] = None
    Format: Optional[str] = None
    Url: Optional[str] = None
    UserBucket: Optional[UserBucketTypeDef] = None

class ListImagesInRecycleBinResultTypeDef(BaseModel):
    Images: List[ImageRecycleBinInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LocalGatewayRouteTableTypeDef(BaseModel):
    LocalGatewayRouteTableId: Optional[str] = None
    LocalGatewayRouteTableArn: Optional[str] = None
    LocalGatewayId: Optional[str] = None
    OutpostArn: Optional[str] = None
    OwnerId: Optional[str] = None
    State: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    Mode: Optional[LocalGatewayRouteTableModeType] = None
    StateReason: Optional[StateReasonTypeDef] = None

class ImportInstanceLaunchSpecificationTypeDef(BaseModel):
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

class InferenceDeviceInfoTypeDef(BaseModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    MemoryInfo: Optional[InferenceDeviceMemoryInfoTypeDef] = None

class InstanceAttachmentEnaSrdSpecificationTypeDef(BaseModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[InstanceAttachmentEnaSrdUdpSpecificationTypeDef] = None

class ModifyInstanceCreditSpecificationRequestRequestTypeDef(BaseModel):
    InstanceCreditSpecifications: Sequence[InstanceCreditSpecificationRequestTypeDef]
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class ModifyInstanceMetadataOptionsResultTypeDef(BaseModel):
    InstanceId: str
    InstanceMetadataOptions: InstanceMetadataOptionsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceMonitoringTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    Monitoring: Optional[MonitoringTypeDef] = None

class InstancePrivateIpAddressTypeDef(BaseModel):
    Association: Optional[InstanceNetworkInterfaceAssociationTypeDef] = None
    Primary: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class InstanceRequirementsExtraOutputTypeDef(BaseModel):
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

class InstanceRequirementsOutputTypeDef(BaseModel):
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

class InstanceRequirementsTypeDef(BaseModel):
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

class InstanceRequirementsRequestTypeDef(BaseModel):
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

class InstanceStateChangeTypeDef(BaseModel):
    CurrentState: Optional[InstanceStateTypeDef] = None
    InstanceId: Optional[str] = None
    PreviousState: Optional[InstanceStateTypeDef] = None

class InstanceStatusSummaryTypeDef(BaseModel):
    Details: Optional[List[InstanceStatusDetailsTypeDef]] = None
    Status: Optional[SummaryStatusType] = None

class ModifyInstanceEventStartTimeResultTypeDef(BaseModel):
    Event: InstanceStatusEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IpPermissionExtraExtraOutputTypeDef(BaseModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[List[IpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[Ipv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[PrefixListIdTypeDef]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPairTypeDef]] = None

class IpPermissionOutputTypeDef(BaseModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[List[IpRangeTypeDef]] = None
    Ipv6Ranges: Optional[List[Ipv6RangeTypeDef]] = None
    PrefixListIds: Optional[List[PrefixListIdTypeDef]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPairTypeDef]] = None

class IpPermissionTypeDef(BaseModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[Sequence[IpRangeTypeDef]] = None
    Ipv6Ranges: Optional[Sequence[Ipv6RangeTypeDef]] = None
    PrefixListIds: Optional[Sequence[PrefixListIdTypeDef]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[Sequence[UserIdGroupPairTypeDef]] = None

class StaleIpPermissionTypeDef(BaseModel):
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    IpRanges: Optional[List[str]] = None
    PrefixListIds: Optional[List[str]] = None
    ToPort: Optional[int] = None
    UserIdGroupPairs: Optional[List[UserIdGroupPairTypeDef]] = None

class ProvisionIpamPoolCidrRequestRequestTypeDef(BaseModel):
    IpamPoolId: str
    DryRun: Optional[bool] = None
    Cidr: Optional[str] = None
    CidrAuthorizationContext: Optional[IpamCidrAuthorizationContextTypeDef] = None
    NetmaskLength: Optional[int] = None
    ClientToken: Optional[str] = None

class IpamDiscoveredAccountTypeDef(BaseModel):
    AccountId: Optional[str] = None
    DiscoveryRegion: Optional[str] = None
    FailureReason: Optional[IpamDiscoveryFailureReasonTypeDef] = None
    LastAttemptedDiscoveryTime: Optional[datetime] = None
    LastSuccessfulDiscoveryTime: Optional[datetime] = None

class IpamDiscoveredResourceCidrTypeDef(BaseModel):
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

class IpamResourceCidrTypeDef(BaseModel):
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

class IpamResourceDiscoveryTypeDef(BaseModel):
    OwnerId: Optional[str] = None
    IpamResourceDiscoveryId: Optional[str] = None
    IpamResourceDiscoveryArn: Optional[str] = None
    IpamResourceDiscoveryRegion: Optional[str] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[List[IpamOperatingRegionTypeDef]] = None
    IsDefault: Optional[bool] = None
    State: Optional[IpamResourceDiscoveryStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class IpamTypeDef(BaseModel):
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

class IpamPoolCidrTypeDef(BaseModel):
    Cidr: Optional[str] = None
    State: Optional[IpamPoolCidrStateType] = None
    FailureReason: Optional[IpamPoolCidrFailureReasonTypeDef] = None
    IpamPoolCidrId: Optional[str] = None
    NetmaskLength: Optional[int] = None

class IpamPoolTypeDef(BaseModel):
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

class IpamPublicAddressTagsTypeDef(BaseModel):
    EipTags: Optional[List[IpamPublicAddressTagTypeDef]] = None

class Ipv6PoolTypeDef(BaseModel):
    PoolId: Optional[str] = None
    Description: Optional[str] = None
    PoolCidrBlocks: Optional[List[PoolCidrBlockTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None

class LaunchTemplateBlockDeviceMappingRequestTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[LaunchTemplateEbsBlockDeviceRequestTypeDef] = None
    NoDevice: Optional[str] = None

class LaunchTemplateBlockDeviceMappingTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    VirtualName: Optional[str] = None
    Ebs: Optional[LaunchTemplateEbsBlockDeviceTypeDef] = None
    NoDevice: Optional[str] = None

class LaunchTemplateEnaSrdSpecificationTypeDef(BaseModel):
    EnaSrdEnabled: Optional[bool] = None
    EnaSrdUdpSpecification: Optional[LaunchTemplateEnaSrdUdpSpecificationTypeDef] = None

class LaunchTemplateInstanceMarketOptionsTypeDef(BaseModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[LaunchTemplateSpotMarketOptionsTypeDef] = None

class ListSnapshotsInRecycleBinResultTypeDef(BaseModel):
    Snapshots: List[SnapshotRecycleBinInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LoadPermissionModificationsTypeDef(BaseModel):
    Add: Optional[Sequence[LoadPermissionRequestTypeDef]] = None
    Remove: Optional[Sequence[LoadPermissionRequestTypeDef]] = None

class MediaDeviceInfoTypeDef(BaseModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    Manufacturer: Optional[str] = None
    MemoryInfo: Optional[MediaDeviceMemoryInfoTypeDef] = None

class ModifyIpamRequestRequestTypeDef(BaseModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AddOperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    RemoveOperatingRegions: Optional[Sequence[RemoveIpamOperatingRegionTypeDef]] = None
    Tier: Optional[IpamTierType] = None

class ModifyIpamResourceDiscoveryRequestRequestTypeDef(BaseModel):
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    AddOperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    RemoveOperatingRegions: Optional[Sequence[RemoveIpamOperatingRegionTypeDef]] = None

class ModifyManagedPrefixListRequestRequestTypeDef(BaseModel):
    PrefixListId: str
    DryRun: Optional[bool] = None
    CurrentVersion: Optional[int] = None
    PrefixListName: Optional[str] = None
    AddEntries: Optional[Sequence[AddPrefixListEntryTypeDef]] = None
    RemoveEntries: Optional[Sequence[RemovePrefixListEntryTypeDef]] = None
    MaxEntries: Optional[int] = None

class ModifyReservedInstancesRequestRequestTypeDef(BaseModel):
    ReservedInstancesIds: Sequence[str]
    TargetConfigurations: Sequence[ReservedInstancesConfigurationTypeDef]
    ClientToken: Optional[str] = None

class ReservedInstancesModificationResultTypeDef(BaseModel):
    ReservedInstancesId: Optional[str] = None
    TargetConfiguration: Optional[ReservedInstancesConfigurationTypeDef] = None

class ModifyTransitGatewayRequestRequestTypeDef(BaseModel):
    TransitGatewayId: str
    Description: Optional[str] = None
    Options: Optional[ModifyTransitGatewayOptionsTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    AddSubnetIds: Optional[Sequence[str]] = None
    RemoveSubnetIds: Optional[Sequence[str]] = None
    Options: Optional[ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef] = None
    DryRun: Optional[bool] = None

class ModifyVerifiedAccessEndpointRequestRequestTypeDef(BaseModel):
    VerifiedAccessEndpointId: str
    VerifiedAccessGroupId: Optional[str] = None
    LoadBalancerOptions: Optional[ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef] = None
    NetworkInterfaceOptions: Optional[ModifyVerifiedAccessEndpointEniOptionsTypeDef] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class ModifyVerifiedAccessEndpointPolicyResultTypeDef(BaseModel):
    PolicyEnabled: bool
    PolicyDocument: str
    SseSpecification: VerifiedAccessSseSpecificationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVerifiedAccessGroupPolicyResultTypeDef(BaseModel):
    PolicyEnabled: bool
    PolicyDocument: str
    SseSpecification: VerifiedAccessSseSpecificationResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VerifiedAccessGroupTypeDef(BaseModel):
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

class ModifyVerifiedAccessTrustProviderRequestRequestTypeDef(BaseModel):
    VerifiedAccessTrustProviderId: str
    OidcOptions: Optional[ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef] = None
    DeviceOptions: Optional[ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef(BaseModel):
    VpcPeeringConnectionId: str
    AccepterPeeringConnectionOptions: Optional[PeeringConnectionOptionsRequestTypeDef] = None
    DryRun: Optional[bool] = None
    RequesterPeeringConnectionOptions: Optional[PeeringConnectionOptionsRequestTypeDef] = None

class ModifyVpcPeeringConnectionOptionsResultTypeDef(BaseModel):
    AccepterPeeringConnectionOptions: PeeringConnectionOptionsTypeDef
    RequesterPeeringConnectionOptions: PeeringConnectionOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class NatGatewayTypeDef(BaseModel):
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

class NetworkInfoTypeDef(BaseModel):
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

class NetworkInterfacePrivateIpAddressTypeDef(BaseModel):
    Association: Optional[NetworkInterfaceAssociationTypeDef] = None
    Primary: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    PrivateIpAddress: Optional[str] = None

class NetworkInterfacePermissionTypeDef(BaseModel):
    NetworkInterfacePermissionId: Optional[str] = None
    NetworkInterfaceId: Optional[str] = None
    AwsAccountId: Optional[str] = None
    AwsService: Optional[str] = None
    Permission: Optional[InterfacePermissionTypeType] = None
    PermissionState: Optional[NetworkInterfacePermissionStateTypeDef] = None

class NeuronDeviceInfoTypeDef(BaseModel):
    Count: Optional[int] = None
    Name: Optional[str] = None
    CoreInfo: Optional[NeuronDeviceCoreInfoTypeDef] = None
    MemoryInfo: Optional[NeuronDeviceMemoryInfoTypeDef] = None

class VerifiedAccessTrustProviderTypeDef(BaseModel):
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

class PathRequestFilterTypeDef(BaseModel):
    SourceAddress: Optional[str] = None
    SourcePortRange: Optional[RequestFilterPortRangeTypeDef] = None
    DestinationAddress: Optional[str] = None
    DestinationPortRange: Optional[RequestFilterPortRangeTypeDef] = None

class PathStatementRequestTypeDef(BaseModel):
    PacketHeaderStatement: Optional[PacketHeaderStatementRequestTypeDef] = None
    ResourceStatement: Optional[ResourceStatementRequestTypeDef] = None

class ThroughResourcesStatementRequestTypeDef(BaseModel):
    ResourceStatement: Optional[ResourceStatementRequestTypeDef] = None

class PathStatementTypeDef(BaseModel):
    PacketHeaderStatement: Optional[PacketHeaderStatementTypeDef] = None
    ResourceStatement: Optional[ResourceStatementTypeDef] = None

class ThroughResourcesStatementTypeDef(BaseModel):
    ResourceStatement: Optional[ResourceStatementTypeDef] = None

class ReservedInstancesListingTypeDef(BaseModel):
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

class ProvisionPublicIpv4PoolCidrResultTypeDef(BaseModel):
    PoolId: str
    PoolAddressRange: PublicIpv4PoolRangeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PublicIpv4PoolTypeDef(BaseModel):
    PoolId: Optional[str] = None
    Description: Optional[str] = None
    PoolAddressRanges: Optional[List[PublicIpv4PoolRangeTypeDef]] = None
    TotalAddressCount: Optional[int] = None
    TotalAvailableAddressCount: Optional[int] = None
    NetworkBorderGroup: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class PurchaseScheduledInstancesRequestRequestTypeDef(BaseModel):
    PurchaseRequests: Sequence[PurchaseRequestTypeDef]
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None

class PurchaseReservedInstancesOfferingRequestRequestTypeDef(BaseModel):
    InstanceCount: int
    ReservedInstancesOfferingId: str
    DryRun: Optional[bool] = None
    LimitPrice: Optional[ReservedInstanceLimitPriceTypeDef] = None
    PurchaseTime: Optional[TimestampTypeDef] = None

class ReservedInstancesOfferingTypeDef(BaseModel):
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

class ReservedInstancesTypeDef(BaseModel):
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

class SecurityGroupRuleTypeDef(BaseModel):
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

class RegisterInstanceEventNotificationAttributesRequestRequestTypeDef(BaseModel):
    InstanceTagAttribute: RegisterInstanceTagAttributeRequestTypeDef
    DryRun: Optional[bool] = None

class RegisterTransitGatewayMulticastGroupMembersResultTypeDef(BaseModel):
    RegisteredMulticastGroupMembers: TransitGatewayMulticastRegisteredGroupMembersTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTransitGatewayMulticastGroupSourcesResultTypeDef(BaseModel):
    RegisteredMulticastGroupSources: TransitGatewayMulticastRegisteredGroupSourcesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StorageOutputTypeDef(BaseModel):
    S3: Optional[S3StorageOutputTypeDef] = None

class ScheduledInstanceAvailabilityTypeDef(BaseModel):
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

class ScheduledInstanceTypeDef(BaseModel):
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

class ScheduledInstancesBlockDeviceMappingTypeDef(BaseModel):
    DeviceName: Optional[str] = None
    Ebs: Optional[ScheduledInstancesEbsTypeDef] = None
    NoDevice: Optional[str] = None
    VirtualName: Optional[str] = None

class ScheduledInstancesNetworkInterfaceTypeDef(BaseModel):
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

class SearchTransitGatewayMulticastGroupsResultTypeDef(BaseModel):
    MulticastGroups: List[TransitGatewayMulticastGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class VpcEndpointTypeDef(BaseModel):
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

class SecurityGroupRuleUpdateTypeDef(BaseModel):
    SecurityGroupRuleId: str
    SecurityGroupRule: Optional[SecurityGroupRuleRequestTypeDef] = None

class ServiceConfigurationTypeDef(BaseModel):
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

class ServiceDetailTypeDef(BaseModel):
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

class SnapshotDetailTypeDef(BaseModel):
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

class SnapshotTaskDetailTypeDef(BaseModel):
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

class SpotMaintenanceStrategiesTypeDef(BaseModel):
    CapacityRebalance: Optional[SpotCapacityRebalanceTypeDef] = None

class SpotDatafeedSubscriptionTypeDef(BaseModel):
    Bucket: Optional[str] = None
    Fault: Optional[SpotInstanceStateFaultTypeDef] = None
    OwnerId: Optional[str] = None
    Prefix: Optional[str] = None
    State: Optional[DatafeedSubscriptionStateType] = None

class TransitGatewayMulticastDomainAssociationTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    Subnet: Optional[SubnetAssociationTypeDef] = None

class TransitGatewayMulticastDomainAssociationsTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayAttachmentId: Optional[str] = None
    ResourceId: Optional[str] = None
    ResourceType: Optional[TransitGatewayAttachmentResourceTypeType] = None
    ResourceOwnerId: Optional[str] = None
    Subnets: Optional[List[SubnetAssociationTypeDef]] = None

class SubnetIpv6CidrBlockAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv6CidrBlockState: Optional[SubnetCidrBlockStateTypeDef] = None

class TargetReservationValueTypeDef(BaseModel):
    ReservationValue: Optional[ReservationValueTypeDef] = None
    TargetConfiguration: Optional[TargetConfigurationTypeDef] = None

class TargetGroupsConfigExtraOutputTypeDef(BaseModel):
    TargetGroups: Optional[List[TargetGroupTypeDef]] = None

class TargetGroupsConfigOutputTypeDef(BaseModel):
    TargetGroups: Optional[List[TargetGroupTypeDef]] = None

class TargetGroupsConfigTypeDef(BaseModel):
    TargetGroups: Optional[Sequence[TargetGroupTypeDef]] = None

class TrafficMirrorFilterRuleTypeDef(BaseModel):
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

class TransitGatewayAttachmentTypeDef(BaseModel):
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

class TransitGatewayConnectPeerConfigurationTypeDef(BaseModel):
    TransitGatewayAddress: Optional[str] = None
    PeerAddress: Optional[str] = None
    InsideCidrBlocks: Optional[List[str]] = None
    Protocol: Optional[Literal["gre"]] = None
    BgpConfigurations: Optional[List[TransitGatewayAttachmentBgpConfigurationTypeDef]] = None

class TransitGatewayConnectTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransportTransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayConnectOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayMulticastDomainTypeDef(BaseModel):
    TransitGatewayMulticastDomainId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    TransitGatewayMulticastDomainArn: Optional[str] = None
    OwnerId: Optional[str] = None
    Options: Optional[TransitGatewayMulticastDomainOptionsTypeDef] = None
    State: Optional[TransitGatewayMulticastDomainStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayTypeDef(BaseModel):
    TransitGatewayId: Optional[str] = None
    TransitGatewayArn: Optional[str] = None
    State: Optional[TransitGatewayStateType] = None
    OwnerId: Optional[str] = None
    Description: Optional[str] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayPeeringAttachmentTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    AccepterTransitGatewayAttachmentId: Optional[str] = None
    RequesterTgwInfo: Optional[PeeringTgwInfoTypeDef] = None
    AccepterTgwInfo: Optional[PeeringTgwInfoTypeDef] = None
    Options: Optional[TransitGatewayPeeringAttachmentOptionsTypeDef] = None
    Status: Optional[PeeringAttachmentStatusTypeDef] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    CreationTime: Optional[datetime] = None
    Tags: Optional[List[TagTypeDef]] = None

class TransitGatewayPolicyRuleTypeDef(BaseModel):
    SourceCidrBlock: Optional[str] = None
    SourcePortRange: Optional[str] = None
    DestinationCidrBlock: Optional[str] = None
    DestinationPortRange: Optional[str] = None
    Protocol: Optional[str] = None
    MetaData: Optional[TransitGatewayPolicyRuleMetaDataTypeDef] = None

class TransitGatewayPrefixListReferenceTypeDef(BaseModel):
    TransitGatewayRouteTableId: Optional[str] = None
    PrefixListId: Optional[str] = None
    PrefixListOwnerId: Optional[str] = None
    State: Optional[TransitGatewayPrefixListReferenceStateType] = None
    Blackhole: Optional[bool] = None
    TransitGatewayAttachment: Optional[TransitGatewayPrefixListAttachmentTypeDef] = None

class TransitGatewayRouteTypeDef(BaseModel):
    DestinationCidrBlock: Optional[str] = None
    PrefixListId: Optional[str] = None
    TransitGatewayRouteTableAnnouncementId: Optional[str] = None
    TransitGatewayAttachments: Optional[List[TransitGatewayRouteAttachmentTypeDef]] = None
    Type: Optional[TransitGatewayRouteTypeType] = None
    State: Optional[TransitGatewayRouteStateType] = None

class TransitGatewayVpcAttachmentTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    VpcId: Optional[str] = None
    VpcOwnerId: Optional[str] = None
    State: Optional[TransitGatewayAttachmentStateType] = None
    SubnetIds: Optional[List[str]] = None
    CreationTime: Optional[datetime] = None
    Options: Optional[TransitGatewayVpcAttachmentOptionsTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class UnsuccessfulInstanceCreditSpecificationItemTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    Error: Optional[UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef] = None

class UnsuccessfulItemTypeDef(BaseModel):
    Error: Optional[UnsuccessfulItemErrorTypeDef] = None
    ResourceId: Optional[str] = None

class ValidationWarningTypeDef(BaseModel):
    Errors: Optional[List[ValidationErrorTypeDef]] = None

class VerifiedAccessEndpointTypeDef(BaseModel):
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

class VerifiedAccessInstanceTypeDef(BaseModel):
    VerifiedAccessInstanceId: Optional[str] = None
    Description: Optional[str] = None
    VerifiedAccessTrustProviders: Optional[       List[VerifiedAccessTrustProviderCondensedTypeDef]     ] = None
    CreationTime: Optional[str] = None
    LastUpdatedTime: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    FipsEnabled: Optional[bool] = None

class VerifiedAccessLogCloudWatchLogsDestinationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatusTypeDef] = None
    LogGroup: Optional[str] = None

class VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatusTypeDef] = None
    DeliveryStream: Optional[str] = None

class VerifiedAccessLogS3DestinationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    DeliveryStatus: Optional[VerifiedAccessLogDeliveryStatusTypeDef] = None
    BucketName: Optional[str] = None
    Prefix: Optional[str] = None
    BucketOwner: Optional[str] = None

class VerifiedAccessLogOptionsTypeDef(BaseModel):
    S3: Optional[VerifiedAccessLogS3DestinationOptionsTypeDef] = None
    CloudWatchLogs: Optional[VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef] = None
    KinesisDataFirehose: Optional[       VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef     ] = None
    LogVersion: Optional[str] = None
    IncludeTrustContext: Optional[bool] = None

class VolumeResponseTypeDef(BaseModel):
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

class VolumeTypeDef(BaseModel):
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

class VolumeStatusInfoTypeDef(BaseModel):
    Details: Optional[List[VolumeStatusDetailsTypeDef]] = None
    Status: Optional[VolumeStatusInfoStatusType] = None

class VpcCidrBlockAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    CidrBlock: Optional[str] = None
    CidrBlockState: Optional[VpcCidrBlockStateTypeDef] = None

class VpcIpv6CidrBlockAssociationTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    Ipv6CidrBlock: Optional[str] = None
    Ipv6CidrBlockState: Optional[VpcCidrBlockStateTypeDef] = None
    NetworkBorderGroup: Optional[str] = None
    Ipv6Pool: Optional[str] = None

class VpcPeeringConnectionVpcInfoTypeDef(BaseModel):
    CidrBlock: Optional[str] = None
    Ipv6CidrBlockSet: Optional[List[Ipv6CidrBlockTypeDef]] = None
    CidrBlockSet: Optional[List[CidrBlockTypeDef]] = None
    OwnerId: Optional[str] = None
    PeeringOptions: Optional[VpcPeeringConnectionOptionsDescriptionTypeDef] = None
    VpcId: Optional[str] = None
    Region: Optional[str] = None

class DescribeAccountAttributesResultTypeDef(BaseModel):
    AccountAttributes: List[AccountAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AdditionalDetailTypeDef(BaseModel):
    AdditionalDetailType: Optional[str] = None
    Component: Optional[AnalysisComponentTypeDef] = None
    VpcEndpointService: Optional[AnalysisComponentTypeDef] = None
    RuleOptions: Optional[List[RuleOptionTypeDef]] = None
    RuleGroupTypePairs: Optional[List[RuleGroupTypePairTypeDef]] = None
    RuleGroupRuleOptionsPairs: Optional[List[RuleGroupRuleOptionsPairTypeDef]] = None
    ServiceName: Optional[str] = None
    LoadBalancers: Optional[List[AnalysisComponentTypeDef]] = None

class DescribeAddressesAttributeResultTypeDef(BaseModel):
    Addresses: List[AddressAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyAddressAttributeResultTypeDef(BaseModel):
    Address: AddressAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetAddressAttributeResultTypeDef(BaseModel):
    Address: AddressAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAddressesResultTypeDef(BaseModel):
    Addresses: List[AddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointServicePermissionsResultTypeDef(BaseModel):
    AllowedPrincipals: List[AllowedPrincipalTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCarrierGatewayResultTypeDef(BaseModel):
    CarrierGateway: CarrierGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCarrierGatewayResultTypeDef(BaseModel):
    CarrierGateway: CarrierGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCarrierGatewaysResultTypeDef(BaseModel):
    CarrierGateways: List[CarrierGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCoipPoolResultTypeDef(BaseModel):
    CoipPool: CoipPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCoipPoolResultTypeDef(BaseModel):
    CoipPool: CoipPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCoipPoolsResultTypeDef(BaseModel):
    CoipPools: List[CoipPoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateCustomerGatewayResultTypeDef(BaseModel):
    CustomerGateway: CustomerGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCustomerGatewaysResultTypeDef(BaseModel):
    CustomerGateways: List[CustomerGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceConnectEndpointResultTypeDef(BaseModel):
    InstanceConnectEndpoint: Ec2InstanceConnectEndpointTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInstanceConnectEndpointResultTypeDef(BaseModel):
    InstanceConnectEndpoint: Ec2InstanceConnectEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceConnectEndpointsResultTypeDef(BaseModel):
    InstanceConnectEndpoints: List[Ec2InstanceConnectEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHostReservationsResultTypeDef(BaseModel):
    HostReservationSet: List[HostReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateInstanceEventWindowRequestRequestTypeDef(BaseModel):
    InstanceEventWindowId: str
    AssociationTarget: InstanceEventWindowAssociationRequestTypeDef
    DryRun: Optional[bool] = None

class InstanceEventWindowTypeDef(BaseModel):
    InstanceEventWindowId: Optional[str] = None
    TimeRanges: Optional[List[InstanceEventWindowTimeRangeTypeDef]] = None
    Name: Optional[str] = None
    CronExpression: Optional[str] = None
    AssociationTarget: Optional[InstanceEventWindowAssociationTargetTypeDef] = None
    State: Optional[InstanceEventWindowStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class DisassociateInstanceEventWindowRequestRequestTypeDef(BaseModel):
    InstanceEventWindowId: str
    AssociationTarget: InstanceEventWindowDisassociationRequestTypeDef
    DryRun: Optional[bool] = None

class AssociateIpamResourceDiscoveryResultTypeDef(BaseModel):
    IpamResourceDiscoveryAssociation: IpamResourceDiscoveryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamResourceDiscoveryAssociationsResultTypeDef(BaseModel):
    IpamResourceDiscoveryAssociations: List[IpamResourceDiscoveryAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisassociateIpamResourceDiscoveryResultTypeDef(BaseModel):
    IpamResourceDiscoveryAssociation: IpamResourceDiscoveryAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamScopeResultTypeDef(BaseModel):
    IpamScope: IpamScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamScopeResultTypeDef(BaseModel):
    IpamScope: IpamScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamScopesResultTypeDef(BaseModel):
    IpamScopes: List[IpamScopeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamScopeResultTypeDef(BaseModel):
    IpamScope: IpamScopeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKeyPairsResultTypeDef(BaseModel):
    KeyPairs: List[KeyPairInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchTemplateResultTypeDef(BaseModel):
    LaunchTemplate: LaunchTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLaunchTemplatesResultTypeDef(BaseModel):
    LaunchTemplates: List[LaunchTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyLaunchTemplateResultTypeDef(BaseModel):
    LaunchTemplate: LaunchTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociation: LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociation: LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef(BaseModel):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociations: List[       LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateLocalGatewayRouteTableVpcAssociationResultTypeDef(BaseModel):
    LocalGatewayRouteTableVpcAssociation: LocalGatewayRouteTableVpcAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef(BaseModel):
    LocalGatewayRouteTableVpcAssociation: LocalGatewayRouteTableVpcAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef(BaseModel):
    LocalGatewayRouteTableVpcAssociations: List[LocalGatewayRouteTableVpcAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLocalGatewaysResultTypeDef(BaseModel):
    LocalGateways: List[LocalGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef(BaseModel):
    LocalGatewayVirtualInterfaceGroups: List[LocalGatewayVirtualInterfaceGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeLocalGatewayVirtualInterfacesResultTypeDef(BaseModel):
    LocalGatewayVirtualInterfaces: List[LocalGatewayVirtualInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateManagedPrefixListResultTypeDef(BaseModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteManagedPrefixListResultTypeDef(BaseModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeManagedPrefixListsResultTypeDef(BaseModel):
    PrefixLists: List[ManagedPrefixListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyManagedPrefixListResultTypeDef(BaseModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreManagedPrefixListVersionResultTypeDef(BaseModel):
    PrefixList: ManagedPrefixListTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalyses: List[NetworkInsightsAccessScopeAnalysisTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartNetworkInsightsAccessScopeAnalysisResultTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysis: NetworkInsightsAccessScopeAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInsightsAccessScopesResultTypeDef(BaseModel):
    NetworkInsightsAccessScopes: List[NetworkInsightsAccessScopeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreatePlacementGroupResultTypeDef(BaseModel):
    PlacementGroup: PlacementGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePlacementGroupsResultTypeDef(BaseModel):
    PlacementGroups: List[PlacementGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplaceRootVolumeTaskResultTypeDef(BaseModel):
    ReplaceRootVolumeTask: ReplaceRootVolumeTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReplaceRootVolumeTasksResultTypeDef(BaseModel):
    ReplaceRootVolumeTasks: List[ReplaceRootVolumeTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetSecurityGroupsForVpcResultTypeDef(BaseModel):
    SecurityGroupForVpcs: List[SecurityGroupForVpcTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateSnapshotsResultTypeDef(BaseModel):
    Snapshots: List[SnapshotInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotTierStatusResultTypeDef(BaseModel):
    SnapshotTierStatuses: List[SnapshotTierStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSnapshotsResultTypeDef(BaseModel):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateSubnetCidrReservationResultTypeDef(BaseModel):
    SubnetCidrReservation: SubnetCidrReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSubnetCidrReservationResultTypeDef(BaseModel):
    DeletedSubnetCidrReservation: SubnetCidrReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSubnetCidrReservationsResultTypeDef(BaseModel):
    SubnetIpv4CidrReservations: List[SubnetCidrReservationTypeDef]
    SubnetIpv6CidrReservations: List[SubnetCidrReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CopySnapshotRequestSnapshotCopyTypeDef(BaseModel):
    SourceRegion: str
    Description: Optional[str] = None
    DestinationOutpostArn: Optional[str] = None
    DestinationRegion: Optional[str] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PresignedUrl: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateNetworkAclRequestVpcCreateNetworkAclTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef(BaseModel):
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

class CreateRouteTableRequestVpcCreateRouteTableTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef(BaseModel):
    Description: str
    GroupName: str
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotRequestVolumeCreateSnapshotTypeDef(BaseModel):
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSubnetRequestVpcCreateSubnetTypeDef(BaseModel):
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

class CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    PeerOwnerId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None

class CreateTrafficMirrorSessionResultTypeDef(BaseModel):
    TrafficMirrorSession: TrafficMirrorSessionTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorSessionsResultTypeDef(BaseModel):
    TrafficMirrorSessions: List[TrafficMirrorSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTrafficMirrorSessionResultTypeDef(BaseModel):
    TrafficMirrorSession: TrafficMirrorSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficMirrorTargetResultTypeDef(BaseModel):
    TrafficMirrorTarget: TrafficMirrorTargetTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorTargetsResultTypeDef(BaseModel):
    TrafficMirrorTargets: List[TrafficMirrorTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayPolicyTableResultTypeDef(BaseModel):
    TransitGatewayPolicyTable: TransitGatewayPolicyTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayPolicyTableResultTypeDef(BaseModel):
    TransitGatewayPolicyTable: TransitGatewayPolicyTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayPolicyTablesResultTypeDef(BaseModel):
    TransitGatewayPolicyTables: List[TransitGatewayPolicyTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayRouteTableAnnouncementResultTypeDef(BaseModel):
    TransitGatewayRouteTableAnnouncement: TransitGatewayRouteTableAnnouncementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayRouteTableAnnouncementResultTypeDef(BaseModel):
    TransitGatewayRouteTableAnnouncement: TransitGatewayRouteTableAnnouncementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef(BaseModel):
    TransitGatewayRouteTableAnnouncements: List[TransitGatewayRouteTableAnnouncementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayRouteTableResultTypeDef(BaseModel):
    TransitGatewayRouteTable: TransitGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayRouteTableResultTypeDef(BaseModel):
    TransitGatewayRouteTable: TransitGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayRouteTablesResultTypeDef(BaseModel):
    TransitGatewayRouteTables: List[TransitGatewayRouteTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateTrunkInterfaceResultTypeDef(BaseModel):
    InterfaceAssociation: TrunkInterfaceAssociationTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrunkInterfaceAssociationsResultTypeDef(BaseModel):
    InterfaceAssociations: List[TrunkInterfaceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVpcClassicLinkResultTypeDef(BaseModel):
    Vpcs: List[VpcClassicLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExplanationTypeDef(BaseModel):
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

class AdvertiseByoipCidrResultTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionByoipCidrResultTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeByoipCidrsResultTypeDef(BaseModel):
    ByoipCidrs: List[ByoipCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MoveByoipCidrToIpamResultTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionByoipCidrResultTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WithdrawByoipCidrResultTypeDef(BaseModel):
    ByoipCidr: ByoipCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClientVpnTargetNetworksResultTypeDef(BaseModel):
    ClientVpnTargetNetworks: List[TargetNetworkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RouteTableTypeDef(BaseModel):
    Associations: Optional[List[RouteTableAssociationTypeDef]] = None
    PropagatingVgws: Optional[List[PropagatingVgwTypeDef]] = None
    RouteTableId: Optional[str] = None
    Routes: Optional[List[RouteTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None

class IntegrateServicesTypeDef(BaseModel):
    AthenaIntegrations: Optional[Sequence[AthenaIntegrationTypeDef]] = None

class LaunchTemplateInstanceMarketOptionsRequestTypeDef(BaseModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[LaunchTemplateSpotMarketOptionsRequestTypeDef] = None

class DescribeScheduledInstanceAvailabilityRequestDescribeScheduledInstanceAvailabilityPaginateTypeDef(BaseModel):
    FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef
    Recurrence: ScheduledInstanceRecurrenceRequestTypeDef
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxSlotDurationInHours: Optional[int] = None
    MinSlotDurationInHours: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledInstanceAvailabilityRequestRequestTypeDef(BaseModel):
    FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef
    Recurrence: ScheduledInstanceRecurrenceRequestTypeDef
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    MaxSlotDurationInHours: Optional[int] = None
    MinSlotDurationInHours: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeScheduledInstancesRequestDescribeScheduledInstancesPaginateTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    ScheduledInstanceIds: Optional[Sequence[str]] = None
    SlotStartTimeRange: Optional[SlotStartTimeRangeRequestTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeScheduledInstancesRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ScheduledInstanceIds: Optional[Sequence[str]] = None
    SlotStartTimeRange: Optional[SlotStartTimeRangeRequestTypeDef] = None

class InstanceMarketOptionsRequestTypeDef(BaseModel):
    MarketType: Optional[MarketTypeType] = None
    SpotOptions: Optional[SpotMarketOptionsTypeDef] = None

class CreateVpnGatewayResultTypeDef(BaseModel):
    VpnGateway: VpnGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpnGatewaysResultTypeDef(BaseModel):
    VpnGateways: List[VpnGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInterfaceAttachmentTypeDef(BaseModel):
    AttachTime: Optional[datetime] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    NetworkCardIndex: Optional[int] = None
    InstanceId: Optional[str] = None
    InstanceOwnerId: Optional[str] = None
    Status: Optional[AttachmentStatusType] = None
    EnaSrdSpecification: Optional[AttachmentEnaSrdSpecificationTypeDef] = None

class DhcpOptionsTypeDef(BaseModel):
    DhcpConfigurations: Optional[List[DhcpConfigurationTypeDef]] = None
    DhcpOptionsId: Optional[str] = None
    OwnerId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeClientVpnAuthorizationRulesResultTypeDef(BaseModel):
    AuthorizationRules: List[AuthorizationRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAvailabilityZonesResultTypeDef(BaseModel):
    AvailabilityZones: List[AvailabilityZoneTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class HostTypeDef(BaseModel):
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

class StorageTypeDef(BaseModel):
    S3: Optional[S3StorageTypeDef] = None

class CreateImageRequestInstanceCreateImageTypeDef(BaseModel):
    Name: str
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    NoReboot: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None

class ImageAttributeTypeDef(BaseModel):
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

class ImageTypeDef(BaseModel):
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

class CancelCapacityReservationFleetsResultTypeDef(BaseModel):
    SuccessfulFleetCancellations: List[CapacityReservationFleetCancellationStateTypeDef]
    FailedFleetCancellations: List[FailedCapacityReservationFleetCancellationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelSpotFleetRequestsResponseTypeDef(BaseModel):
    SuccessfulFleetRequests: List[CancelSpotFleetRequestsSuccessItemTypeDef]
    UnsuccessfulFleetRequests: List[CancelSpotFleetRequestsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCapacityReservationResultTypeDef(BaseModel):
    CapacityReservation: CapacityReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapacityReservationsResultTypeDef(BaseModel):
    CapacityReservations: List[CapacityReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseCapacityBlockResultTypeDef(BaseModel):
    CapacityReservation: CapacityReservationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapacityReservationFleetsResultTypeDef(BaseModel):
    CapacityReservationFleets: List[CapacityReservationFleetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    CapacityReservationSpecification: CapacityReservationSpecificationTypeDef
    DryRun: Optional[bool] = None

class DescribeClassicLinkInstancesResultTypeDef(BaseModel):
    Instances: List[ClassicLinkInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ClientVpnEndpointTypeDef(BaseModel):
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

class DescribeClientVpnConnectionsResultTypeDef(BaseModel):
    Connections: List[ClientVpnConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TerminateClientVpnConnectionsResultTypeDef(BaseModel):
    ClientVpnEndpointId: str
    Username: str
    ConnectionStatuses: List[TerminateConnectionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClientVpnRoutesResultTypeDef(BaseModel):
    Routes: List[ClientVpnRouteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVpnTunnelOptionsSpecificationTypeDef(BaseModel):
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

class VpnTunnelOptionsSpecificationTypeDef(BaseModel):
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

class TunnelOptionTypeDef(BaseModel):
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

class NetworkAclTypeDef(BaseModel):
    Associations: Optional[List[NetworkAclAssociationTypeDef]] = None
    Entries: Optional[List[NetworkAclEntryTypeDef]] = None
    IsDefault: Optional[bool] = None
    NetworkAclId: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None
    OwnerId: Optional[str] = None

class ModifySnapshotAttributeRequestRequestTypeDef(BaseModel):
    SnapshotId: str
    Attribute: Optional[SnapshotAttributeNameType] = None
    CreateVolumePermission: Optional[CreateVolumePermissionModificationsTypeDef] = None
    GroupNames: Optional[Sequence[str]] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef(BaseModel):
    Attribute: Optional[SnapshotAttributeNameType] = None
    CreateVolumePermission: Optional[CreateVolumePermissionModificationsTypeDef] = None
    GroupNames: Optional[Sequence[str]] = None
    OperationType: Optional[OperationTypeType] = None
    UserIds: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None

class GetAwsNetworkPerformanceDataResultTypeDef(BaseModel):
    DataResponses: List[DataResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DeleteFleetsResultTypeDef(BaseModel):
    SuccessfulFleetDeletions: List[DeleteFleetSuccessItemTypeDef]
    UnsuccessfulFleetDeletions: List[DeleteFleetErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLaunchTemplateVersionsResultTypeDef(BaseModel):
    SuccessfullyDeletedLaunchTemplateVersions: List[       DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef     ]
    UnsuccessfullyDeletedLaunchTemplateVersions: List[       DeleteLaunchTemplateVersionsResponseErrorItemTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteQueuedReservedInstancesResultTypeDef(BaseModel):
    SuccessfulQueuedPurchaseDeletions: List[SuccessfulQueuedPurchaseDeletionTypeDef]
    FailedQueuedPurchaseDeletions: List[FailedQueuedPurchaseDeletionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePrincipalIdFormatResultTypeDef(BaseModel):
    Principals: List[PrincipalIdFormatTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFastLaunchImagesResultTypeDef(BaseModel):
    FastLaunchImages: List[DescribeFastLaunchImagesSuccessItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFlowLogsResultTypeDef(BaseModel):
    FlowLogs: List[FlowLogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisableFastSnapshotRestoreErrorItemTypeDef(BaseModel):
    SnapshotId: Optional[str] = None
    FastSnapshotRestoreStateErrors: Optional[       List[DisableFastSnapshotRestoreStateErrorItemTypeDef]     ] = None

class ImportInstanceTaskDetailsTypeDef(BaseModel):
    Description: Optional[str] = None
    InstanceId: Optional[str] = None
    Platform: Optional[Literal["windows"]] = None
    Volumes: Optional[List[ImportInstanceVolumeDetailItemTypeDef]] = None

class DescribeVpcEndpointConnectionsResultTypeDef(BaseModel):
    VpcEndpointConnections: List[VpcEndpointConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef(BaseModel):
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

class ModifyInstanceAttributeRequestRequestTypeDef(BaseModel):
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

class InstanceAttributeTypeDef(BaseModel):
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

class CreateEgressOnlyInternetGatewayResultTypeDef(BaseModel):
    ClientToken: str
    EgressOnlyInternetGateway: EgressOnlyInternetGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEgressOnlyInternetGatewaysResultTypeDef(BaseModel):
    EgressOnlyInternetGateways: List[EgressOnlyInternetGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateInternetGatewayResultTypeDef(BaseModel):
    InternetGateway: InternetGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInternetGatewaysResultTypeDef(BaseModel):
    InternetGateways: List[InternetGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeElasticGpusResultTypeDef(BaseModel):
    ElasticGpuSet: List[ElasticGpusTypeDef]
    MaxResults: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceNetworkInterfaceSpecificationExtraOutputTypeDef(BaseModel):
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

class InstanceNetworkInterfaceSpecificationOutputTypeDef(BaseModel):
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

class InstanceNetworkInterfaceSpecificationTypeDef(BaseModel):
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

class LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef(BaseModel):
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

class AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef(BaseModel):
    DeviceIndex: int
    InstanceId: str
    DryRun: Optional[bool] = None
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationTypeDef] = None

class AttachNetworkInterfaceRequestRequestTypeDef(BaseModel):
    DeviceIndex: int
    InstanceId: str
    NetworkInterfaceId: str
    DryRun: Optional[bool] = None
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationTypeDef] = None

class ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef(BaseModel):
    Attachment: Optional[NetworkInterfaceAttachmentChangesTypeDef] = None
    Description: Optional[AttributeValueTypeDef] = None
    DryRun: Optional[bool] = None
    Groups: Optional[Sequence[str]] = None
    SourceDestCheck: Optional[AttributeBooleanValueTypeDef] = None
    EnaSrdSpecification: Optional[EnaSrdSpecificationTypeDef] = None
    EnablePrimaryIpv6: Optional[bool] = None
    ConnectionTrackingSpecification: Optional[       ConnectionTrackingSpecificationRequestTypeDef     ] = None
    AssociatePublicIpAddress: Optional[bool] = None

class ModifyNetworkInterfaceAttributeRequestRequestTypeDef(BaseModel):
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

class EnableFastSnapshotRestoreErrorItemTypeDef(BaseModel):
    SnapshotId: Optional[str] = None
    FastSnapshotRestoreStateErrors: Optional[       List[EnableFastSnapshotRestoreStateErrorItemTypeDef]     ] = None

class DescribeFleetHistoryResultTypeDef(BaseModel):
    HistoryRecords: List[HistoryRecordEntryTypeDef]
    LastEvaluatedTime: datetime
    FleetId: str
    StartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestHistoryResponseTypeDef(BaseModel):
    HistoryRecords: List[HistoryRecordTypeDef]
    LastEvaluatedTime: datetime
    SpotFleetRequestId: str
    StartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeExportImageTasksResultTypeDef(BaseModel):
    ExportImageTasks: List[ExportImageTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateInstanceExportTaskResultTypeDef(BaseModel):
    ExportTask: ExportTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportTasksResultTypeDef(BaseModel):
    ExportTasks: List[ExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInsightsPathTypeDef(BaseModel):
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

class SpotOptionsRequestTypeDef(BaseModel):
    AllocationStrategy: Optional[SpotAllocationStrategyType] = None
    MaintenanceStrategies: Optional[FleetSpotMaintenanceStrategiesRequestTypeDef] = None
    InstanceInterruptionBehavior: Optional[SpotInstanceInterruptionBehaviorType] = None
    InstancePoolsToUseCount: Optional[int] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class SpotOptionsTypeDef(BaseModel):
    AllocationStrategy: Optional[SpotAllocationStrategyType] = None
    MaintenanceStrategies: Optional[FleetSpotMaintenanceStrategiesTypeDef] = None
    InstanceInterruptionBehavior: Optional[SpotInstanceInterruptionBehaviorType] = None
    InstancePoolsToUseCount: Optional[int] = None
    SingleInstanceType: Optional[bool] = None
    SingleAvailabilityZone: Optional[bool] = None
    MinTargetCapacity: Optional[int] = None
    MaxTotalPrice: Optional[str] = None

class FpgaInfoTypeDef(BaseModel):
    Fpgas: Optional[List[FpgaDeviceInfoTypeDef]] = None
    TotalFpgaMemoryInMiB: Optional[int] = None

class DescribeFpgaImageAttributeResultTypeDef(BaseModel):
    FpgaImageAttribute: FpgaImageAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyFpgaImageAttributeResultTypeDef(BaseModel):
    FpgaImageAttribute: FpgaImageAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFpgaImagesResultTypeDef(BaseModel):
    FpgaImages: List[FpgaImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GpuInfoTypeDef(BaseModel):
    Gpus: Optional[List[GpuDeviceInfoTypeDef]] = None
    TotalGpuMemoryInMiB: Optional[int] = None

class AssociateIamInstanceProfileResultTypeDef(BaseModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIamInstanceProfileAssociationsResultTypeDef(BaseModel):
    IamInstanceProfileAssociations: List[IamInstanceProfileAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisassociateIamInstanceProfileResultTypeDef(BaseModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceIamInstanceProfileAssociationResultTypeDef(BaseModel):
    IamInstanceProfileAssociation: IamInstanceProfileAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyImageAttributeRequestImageModifyAttributeTypeDef(BaseModel):
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

class ModifyImageAttributeRequestRequestTypeDef(BaseModel):
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

class CreateLocalGatewayRouteTableResultTypeDef(BaseModel):
    LocalGatewayRouteTable: LocalGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLocalGatewayRouteTableResultTypeDef(BaseModel):
    LocalGatewayRouteTable: LocalGatewayRouteTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLocalGatewayRouteTablesResultTypeDef(BaseModel):
    LocalGatewayRouteTables: List[LocalGatewayRouteTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportInstanceRequestRequestTypeDef(BaseModel):
    Platform: Literal["windows"]
    Description: Optional[str] = None
    DiskImages: Optional[Sequence[DiskImageTypeDef]] = None
    DryRun: Optional[bool] = None
    LaunchSpecification: Optional[ImportInstanceLaunchSpecificationTypeDef] = None

class InferenceAcceleratorInfoTypeDef(BaseModel):
    Accelerators: Optional[List[InferenceDeviceInfoTypeDef]] = None
    TotalInferenceMemoryInMiB: Optional[int] = None

class InstanceNetworkInterfaceAttachmentTypeDef(BaseModel):
    AttachTime: Optional[datetime] = None
    AttachmentId: Optional[str] = None
    DeleteOnTermination: Optional[bool] = None
    DeviceIndex: Optional[int] = None
    Status: Optional[AttachmentStatusType] = None
    NetworkCardIndex: Optional[int] = None
    EnaSrdSpecification: Optional[InstanceAttachmentEnaSrdSpecificationTypeDef] = None

class MonitorInstancesResultTypeDef(BaseModel):
    InstanceMonitorings: List[InstanceMonitoringTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UnmonitorInstancesResultTypeDef(BaseModel):
    InstanceMonitorings: List[InstanceMonitoringTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchTemplateOverridesExtraOutputTypeDef(BaseModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsExtraOutputTypeDef] = None

class FleetLaunchTemplateOverridesTypeDef(BaseModel):
    InstanceType: Optional[InstanceTypeType] = None
    MaxPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    Placement: Optional[PlacementResponseTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None
    ImageId: Optional[str] = None

class LaunchTemplateOverridesOutputTypeDef(BaseModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsOutputTypeDef] = None

class LaunchTemplateOverridesTypeDef(BaseModel):
    InstanceType: Optional[InstanceTypeType] = None
    SpotPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    InstanceRequirements: Optional[InstanceRequirementsTypeDef] = None

class FleetLaunchTemplateOverridesRequestTypeDef(BaseModel):
    InstanceType: Optional[InstanceTypeType] = None
    MaxPrice: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    WeightedCapacity: Optional[float] = None
    Priority: Optional[float] = None
    Placement: Optional[PlacementTypeDef] = None
    InstanceRequirements: Optional[InstanceRequirementsRequestTypeDef] = None
    ImageId: Optional[str] = None

class GetInstanceTypesFromInstanceRequirementsRequestGetInstanceTypesFromInstanceRequirementsPaginateTypeDef(BaseModel):
    ArchitectureTypes: Sequence[ArchitectureTypeType]
    VirtualizationTypes: Sequence[VirtualizationTypeType]
    InstanceRequirements: InstanceRequirementsRequestTypeDef
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef(BaseModel):
    ArchitectureTypes: Sequence[ArchitectureTypeType]
    VirtualizationTypes: Sequence[VirtualizationTypeType]
    InstanceRequirements: InstanceRequirementsRequestTypeDef
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class InstanceRequirementsWithMetadataRequestTypeDef(BaseModel):
    ArchitectureTypes: Optional[Sequence[ArchitectureTypeType]] = None
    VirtualizationTypes: Optional[Sequence[VirtualizationTypeType]] = None
    InstanceRequirements: Optional[InstanceRequirementsRequestTypeDef] = None

class StartInstancesResultTypeDef(BaseModel):
    StartingInstances: List[InstanceStateChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopInstancesResultTypeDef(BaseModel):
    StoppingInstances: List[InstanceStateChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateInstancesResultTypeDef(BaseModel):
    TerminatingInstances: List[InstanceStateChangeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceStatusTypeDef(BaseModel):
    AvailabilityZone: Optional[str] = None
    OutpostArn: Optional[str] = None
    Events: Optional[List[InstanceStatusEventTypeDef]] = None
    InstanceId: Optional[str] = None
    InstanceState: Optional[InstanceStateTypeDef] = None
    InstanceStatus: Optional[InstanceStatusSummaryTypeDef] = None
    SystemStatus: Optional[InstanceStatusSummaryTypeDef] = None

class RevokeSecurityGroupEgressResultTypeDef(BaseModel):
    Return: bool
    UnknownIpPermissions: List[IpPermissionExtraExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeSecurityGroupIngressResultTypeDef(BaseModel):
    Return: bool
    UnknownIpPermissions: List[IpPermissionExtraExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SecurityGroupTypeDef(BaseModel):
    Description: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[List[IpPermissionOutputTypeDef]] = None
    OwnerId: Optional[str] = None
    GroupId: Optional[str] = None
    IpPermissionsEgress: Optional[List[IpPermissionOutputTypeDef]] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcId: Optional[str] = None

class AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    IpPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationTypeDef]] = None
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    ToPort: Optional[int] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None

class AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef(BaseModel):
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

class RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    IpPermissions: Optional[Sequence[IpPermissionTypeDef]] = None
    SecurityGroupRuleIds: Optional[Sequence[str]] = None
    CidrIp: Optional[str] = None
    FromPort: Optional[int] = None
    IpProtocol: Optional[str] = None
    ToPort: Optional[int] = None
    SourceSecurityGroupName: Optional[str] = None
    SourceSecurityGroupOwnerId: Optional[str] = None

class RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef(BaseModel):
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

class StaleSecurityGroupTypeDef(BaseModel):
    Description: Optional[str] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    StaleIpPermissions: Optional[List[StaleIpPermissionTypeDef]] = None
    StaleIpPermissionsEgress: Optional[List[StaleIpPermissionTypeDef]] = None
    VpcId: Optional[str] = None

class GetIpamDiscoveredAccountsResultTypeDef(BaseModel):
    IpamDiscoveredAccounts: List[IpamDiscoveredAccountTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamDiscoveredResourceCidrsResultTypeDef(BaseModel):
    IpamDiscoveredResourceCidrs: List[IpamDiscoveredResourceCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamResourceCidrsResultTypeDef(BaseModel):
    IpamResourceCidrs: List[IpamResourceCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamResourceCidrResultTypeDef(BaseModel):
    IpamResourceCidr: IpamResourceCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamResourceDiscoveryResultTypeDef(BaseModel):
    IpamResourceDiscovery: IpamResourceDiscoveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamResourceDiscoveryResultTypeDef(BaseModel):
    IpamResourceDiscovery: IpamResourceDiscoveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamResourceDiscoveriesResultTypeDef(BaseModel):
    IpamResourceDiscoveries: List[IpamResourceDiscoveryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamResourceDiscoveryResultTypeDef(BaseModel):
    IpamResourceDiscovery: IpamResourceDiscoveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamResultTypeDef(BaseModel):
    Ipam: IpamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamResultTypeDef(BaseModel):
    Ipam: IpamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamsResultTypeDef(BaseModel):
    Ipams: List[IpamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamResultTypeDef(BaseModel):
    Ipam: IpamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeprovisionIpamPoolCidrResultTypeDef(BaseModel):
    IpamPoolCidr: IpamPoolCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetIpamPoolCidrsResultTypeDef(BaseModel):
    IpamPoolCidrs: List[IpamPoolCidrTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ProvisionIpamPoolCidrResultTypeDef(BaseModel):
    IpamPoolCidr: IpamPoolCidrTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpamPoolResultTypeDef(BaseModel):
    IpamPool: IpamPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIpamPoolResultTypeDef(BaseModel):
    IpamPool: IpamPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeIpamPoolsResultTypeDef(BaseModel):
    IpamPools: List[IpamPoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyIpamPoolResultTypeDef(BaseModel):
    IpamPool: IpamPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IpamDiscoveredPublicAddressTypeDef(BaseModel):
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

class DescribeIpv6PoolsResultTypeDef(BaseModel):
    Ipv6Pools: List[Ipv6PoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef(BaseModel):
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

class ModifyFpgaImageAttributeRequestRequestTypeDef(BaseModel):
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

class MediaAcceleratorInfoTypeDef(BaseModel):
    Accelerators: Optional[List[MediaDeviceInfoTypeDef]] = None
    TotalMediaMemoryInMiB: Optional[int] = None

class ReservedInstancesModificationTypeDef(BaseModel):
    ClientToken: Optional[str] = None
    CreateDate: Optional[datetime] = None
    EffectiveDate: Optional[datetime] = None
    ModificationResults: Optional[List[ReservedInstancesModificationResultTypeDef]] = None
    ReservedInstancesIds: Optional[List[ReservedInstancesIdTypeDef]] = None
    ReservedInstancesModificationId: Optional[str] = None
    Status: Optional[str] = None
    StatusMessage: Optional[str] = None
    UpdateDate: Optional[datetime] = None

class CreateVerifiedAccessGroupResultTypeDef(BaseModel):
    VerifiedAccessGroup: VerifiedAccessGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessGroupResultTypeDef(BaseModel):
    VerifiedAccessGroup: VerifiedAccessGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessGroupsResultTypeDef(BaseModel):
    VerifiedAccessGroups: List[VerifiedAccessGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessGroupResultTypeDef(BaseModel):
    VerifiedAccessGroup: VerifiedAccessGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNatGatewayResultTypeDef(BaseModel):
    ClientToken: str
    NatGateway: NatGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNatGatewaysResultTypeDef(BaseModel):
    NatGateways: List[NatGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateNetworkInterfacePermissionResultTypeDef(BaseModel):
    InterfacePermission: NetworkInterfacePermissionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInterfacePermissionsResultTypeDef(BaseModel):
    NetworkInterfacePermissions: List[NetworkInterfacePermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class NeuronInfoTypeDef(BaseModel):
    NeuronDevices: Optional[List[NeuronDeviceInfoTypeDef]] = None
    TotalNeuronDeviceMemoryInMiB: Optional[int] = None

class CreateVerifiedAccessTrustProviderResultTypeDef(BaseModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessTrustProviderResultTypeDef(BaseModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessTrustProvidersResultTypeDef(BaseModel):
    VerifiedAccessTrustProviders: List[VerifiedAccessTrustProviderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessTrustProviderResultTypeDef(BaseModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AccessScopePathRequestTypeDef(BaseModel):
    Source: Optional[PathStatementRequestTypeDef] = None
    Destination: Optional[PathStatementRequestTypeDef] = None
    ThroughResources: Optional[Sequence[ThroughResourcesStatementRequestTypeDef]] = None

class AccessScopePathTypeDef(BaseModel):
    Source: Optional[PathStatementTypeDef] = None
    Destination: Optional[PathStatementTypeDef] = None
    ThroughResources: Optional[List[ThroughResourcesStatementTypeDef]] = None

class CancelReservedInstancesListingResultTypeDef(BaseModel):
    ReservedInstancesListings: List[ReservedInstancesListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReservedInstancesListingResultTypeDef(BaseModel):
    ReservedInstancesListings: List[ReservedInstancesListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReservedInstancesListingsResultTypeDef(BaseModel):
    ReservedInstancesListings: List[ReservedInstancesListingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePublicIpv4PoolsResultTypeDef(BaseModel):
    PublicIpv4Pools: List[PublicIpv4PoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstancesOfferingsResultTypeDef(BaseModel):
    ReservedInstancesOfferings: List[ReservedInstancesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeReservedInstancesResultTypeDef(BaseModel):
    ReservedInstances: List[ReservedInstancesTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeSecurityGroupEgressResultTypeDef(BaseModel):
    Return: bool
    SecurityGroupRules: List[SecurityGroupRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AuthorizeSecurityGroupIngressResultTypeDef(BaseModel):
    Return: bool
    SecurityGroupRules: List[SecurityGroupRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSecurityGroupRulesResultTypeDef(BaseModel):
    SecurityGroupRules: List[SecurityGroupRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BundleTaskTypeDef(BaseModel):
    BundleId: Optional[str] = None
    BundleTaskError: Optional[BundleTaskErrorTypeDef] = None
    InstanceId: Optional[str] = None
    Progress: Optional[str] = None
    StartTime: Optional[datetime] = None
    State: Optional[BundleTaskStateType] = None
    Storage: Optional[StorageOutputTypeDef] = None
    UpdateTime: Optional[datetime] = None

class DescribeScheduledInstanceAvailabilityResultTypeDef(BaseModel):
    ScheduledInstanceAvailabilitySet: List[ScheduledInstanceAvailabilityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeScheduledInstancesResultTypeDef(BaseModel):
    ScheduledInstanceSet: List[ScheduledInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PurchaseScheduledInstancesResultTypeDef(BaseModel):
    ScheduledInstanceSet: List[ScheduledInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledInstancesLaunchSpecificationTypeDef(BaseModel):
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

class CreateVpcEndpointResultTypeDef(BaseModel):
    VpcEndpoint: VpcEndpointTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointsResultTypeDef(BaseModel):
    VpcEndpoints: List[VpcEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifySecurityGroupRulesRequestRequestTypeDef(BaseModel):
    GroupId: str
    SecurityGroupRules: Sequence[SecurityGroupRuleUpdateTypeDef]
    DryRun: Optional[bool] = None

class CreateVpcEndpointServiceConfigurationResultTypeDef(BaseModel):
    ServiceConfiguration: ServiceConfigurationTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcEndpointServiceConfigurationsResultTypeDef(BaseModel):
    ServiceConfigurations: List[ServiceConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeVpcEndpointServicesResultTypeDef(BaseModel):
    ServiceNames: List[str]
    ServiceDetails: List[ServiceDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportImageResultTypeDef(BaseModel):
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

class ImportImageTaskTypeDef(BaseModel):
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

class ImportSnapshotResultTypeDef(BaseModel):
    Description: str
    ImportTaskId: str
    SnapshotTaskDetail: SnapshotTaskDetailTypeDef
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportSnapshotTaskTypeDef(BaseModel):
    Description: Optional[str] = None
    ImportTaskId: Optional[str] = None
    SnapshotTaskDetail: Optional[SnapshotTaskDetailTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateSpotDatafeedSubscriptionResultTypeDef(BaseModel):
    SpotDatafeedSubscription: SpotDatafeedSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpotDatafeedSubscriptionResultTypeDef(BaseModel):
    SpotDatafeedSubscription: SpotDatafeedSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayMulticastDomainAssociationsResultTypeDef(BaseModel):
    MulticastDomainAssociations: List[TransitGatewayMulticastDomainAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef(BaseModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateTransitGatewayMulticastDomainResultTypeDef(BaseModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateTransitGatewayMulticastDomainResultTypeDef(BaseModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RejectTransitGatewayMulticastDomainAssociationsResultTypeDef(BaseModel):
    Associations: TransitGatewayMulticastDomainAssociationsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSubnetCidrBlockResultTypeDef(BaseModel):
    Ipv6CidrBlockAssociation: SubnetIpv6CidrBlockAssociationTypeDef
    SubnetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateSubnetCidrBlockResultTypeDef(BaseModel):
    Ipv6CidrBlockAssociation: SubnetIpv6CidrBlockAssociationTypeDef
    SubnetId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetTypeDef(BaseModel):
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

class GetReservedInstancesExchangeQuoteResultTypeDef(BaseModel):
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

class LoadBalancersConfigExtraOutputTypeDef(BaseModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfigExtraOutputTypeDef] = None
    TargetGroupsConfig: Optional[TargetGroupsConfigExtraOutputTypeDef] = None

class LoadBalancersConfigOutputTypeDef(BaseModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfigOutputTypeDef] = None
    TargetGroupsConfig: Optional[TargetGroupsConfigOutputTypeDef] = None

class LoadBalancersConfigTypeDef(BaseModel):
    ClassicLoadBalancersConfig: Optional[ClassicLoadBalancersConfigTypeDef] = None
    TargetGroupsConfig: Optional[TargetGroupsConfigTypeDef] = None

class CreateTrafficMirrorFilterRuleResultTypeDef(BaseModel):
    TrafficMirrorFilterRule: TrafficMirrorFilterRuleTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorFilterRulesResultTypeDef(BaseModel):
    TrafficMirrorFilterRules: List[TrafficMirrorFilterRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTrafficMirrorFilterRuleResultTypeDef(BaseModel):
    TrafficMirrorFilterRule: TrafficMirrorFilterRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TrafficMirrorFilterTypeDef(BaseModel):
    TrafficMirrorFilterId: Optional[str] = None
    IngressFilterRules: Optional[List[TrafficMirrorFilterRuleTypeDef]] = None
    EgressFilterRules: Optional[List[TrafficMirrorFilterRuleTypeDef]] = None
    NetworkServices: Optional[List[Literal["amazon-dns"]]] = None
    Description: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class DescribeTransitGatewayAttachmentsResultTypeDef(BaseModel):
    TransitGatewayAttachments: List[TransitGatewayAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TransitGatewayConnectPeerTypeDef(BaseModel):
    TransitGatewayAttachmentId: Optional[str] = None
    TransitGatewayConnectPeerId: Optional[str] = None
    State: Optional[TransitGatewayConnectPeerStateType] = None
    CreationTime: Optional[datetime] = None
    ConnectPeerConfiguration: Optional[TransitGatewayConnectPeerConfigurationTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None

class CreateTransitGatewayConnectResultTypeDef(BaseModel):
    TransitGatewayConnect: TransitGatewayConnectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayConnectResultTypeDef(BaseModel):
    TransitGatewayConnect: TransitGatewayConnectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayConnectsResultTypeDef(BaseModel):
    TransitGatewayConnects: List[TransitGatewayConnectTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayMulticastDomainResultTypeDef(BaseModel):
    TransitGatewayMulticastDomain: TransitGatewayMulticastDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayMulticastDomainResultTypeDef(BaseModel):
    TransitGatewayMulticastDomain: TransitGatewayMulticastDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayMulticastDomainsResultTypeDef(BaseModel):
    TransitGatewayMulticastDomains: List[TransitGatewayMulticastDomainTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTransitGatewayResultTypeDef(BaseModel):
    TransitGateway: TransitGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayResultTypeDef(BaseModel):
    TransitGateway: TransitGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewaysResultTypeDef(BaseModel):
    TransitGateways: List[TransitGatewayTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTransitGatewayResultTypeDef(BaseModel):
    TransitGateway: TransitGatewayTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptTransitGatewayPeeringAttachmentResultTypeDef(BaseModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayPeeringAttachmentResultTypeDef(BaseModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayPeeringAttachmentResultTypeDef(BaseModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayPeeringAttachmentsResultTypeDef(BaseModel):
    TransitGatewayPeeringAttachments: List[TransitGatewayPeeringAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RejectTransitGatewayPeeringAttachmentResultTypeDef(BaseModel):
    TransitGatewayPeeringAttachment: TransitGatewayPeeringAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransitGatewayPolicyTableEntryTypeDef(BaseModel):
    PolicyRuleNumber: Optional[str] = None
    PolicyRule: Optional[TransitGatewayPolicyRuleTypeDef] = None
    TargetRouteTableId: Optional[str] = None

class CreateTransitGatewayPrefixListReferenceResultTypeDef(BaseModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayPrefixListReferenceResultTypeDef(BaseModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTransitGatewayPrefixListReferencesResultTypeDef(BaseModel):
    TransitGatewayPrefixListReferences: List[TransitGatewayPrefixListReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTransitGatewayPrefixListReferenceResultTypeDef(BaseModel):
    TransitGatewayPrefixListReference: TransitGatewayPrefixListReferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayRouteResultTypeDef(BaseModel):
    Route: TransitGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayRouteResultTypeDef(BaseModel):
    Route: TransitGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplaceTransitGatewayRouteResultTypeDef(BaseModel):
    Route: TransitGatewayRouteTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchTransitGatewayRoutesResultTypeDef(BaseModel):
    Routes: List[TransitGatewayRouteTypeDef]
    AdditionalRoutesAvailable: bool
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptTransitGatewayVpcAttachmentResultTypeDef(BaseModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayVpcAttachmentResultTypeDef(BaseModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayVpcAttachmentResultTypeDef(BaseModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayVpcAttachmentsResultTypeDef(BaseModel):
    TransitGatewayVpcAttachments: List[TransitGatewayVpcAttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTransitGatewayVpcAttachmentResultTypeDef(BaseModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RejectTransitGatewayVpcAttachmentResultTypeDef(BaseModel):
    TransitGatewayVpcAttachment: TransitGatewayVpcAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceCreditSpecificationResultTypeDef(BaseModel):
    SuccessfulInstanceCreditSpecifications: List[       SuccessfulInstanceCreditSpecificationItemTypeDef     ]
    UnsuccessfulInstanceCreditSpecifications: List[       UnsuccessfulInstanceCreditSpecificationItemTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptVpcEndpointConnectionsResultTypeDef(BaseModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFlowLogsResultTypeDef(BaseModel):
    ClientToken: str
    FlowLogIds: List[str]
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFlowLogsResultTypeDef(BaseModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointConnectionNotificationsResultTypeDef(BaseModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointServiceConfigurationsResultTypeDef(BaseModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVpcEndpointsResultTypeDef(BaseModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyHostsResultTypeDef(BaseModel):
    Successful: List[str]
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RejectVpcEndpointConnectionsResultTypeDef(BaseModel):
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReleaseHostsResultTypeDef(BaseModel):
    Successful: List[str]
    Unsuccessful: List[UnsuccessfulItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLaunchTemplateResultTypeDef(BaseModel):
    LaunchTemplate: LaunchTemplateTypeDef
    Warning: ValidationWarningTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVerifiedAccessEndpointResultTypeDef(BaseModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessEndpointResultTypeDef(BaseModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessEndpointsResultTypeDef(BaseModel):
    VerifiedAccessEndpoints: List[VerifiedAccessEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessEndpointResultTypeDef(BaseModel):
    VerifiedAccessEndpoint: VerifiedAccessEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AttachVerifiedAccessTrustProviderResultTypeDef(BaseModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVerifiedAccessInstanceResultTypeDef(BaseModel):
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVerifiedAccessInstanceResultTypeDef(BaseModel):
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessInstancesResultTypeDef(BaseModel):
    VerifiedAccessInstances: List[VerifiedAccessInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DetachVerifiedAccessTrustProviderResultTypeDef(BaseModel):
    VerifiedAccessTrustProvider: VerifiedAccessTrustProviderTypeDef
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVerifiedAccessInstanceResultTypeDef(BaseModel):
    VerifiedAccessInstance: VerifiedAccessInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class VerifiedAccessLogsTypeDef(BaseModel):
    S3: Optional[VerifiedAccessLogS3DestinationTypeDef] = None
    CloudWatchLogs: Optional[VerifiedAccessLogCloudWatchLogsDestinationTypeDef] = None
    KinesisDataFirehose: Optional[VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef] = None
    LogVersion: Optional[str] = None
    IncludeTrustContext: Optional[bool] = None

class ModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceId: str
    AccessLogs: VerifiedAccessLogOptionsTypeDef
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class DescribeVolumesResultTypeDef(BaseModel):
    Volumes: List[VolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class VolumeStatusItemTypeDef(BaseModel):
    Actions: Optional[List[VolumeStatusActionTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    OutpostArn: Optional[str] = None
    Events: Optional[List[VolumeStatusEventTypeDef]] = None
    VolumeId: Optional[str] = None
    VolumeStatus: Optional[VolumeStatusInfoTypeDef] = None
    AttachmentStatuses: Optional[List[VolumeStatusAttachmentStatusTypeDef]] = None

class AssociateVpcCidrBlockResultTypeDef(BaseModel):
    Ipv6CidrBlockAssociation: VpcIpv6CidrBlockAssociationTypeDef
    CidrBlockAssociation: VpcCidrBlockAssociationTypeDef
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateVpcCidrBlockResultTypeDef(BaseModel):
    Ipv6CidrBlockAssociation: VpcIpv6CidrBlockAssociationTypeDef
    CidrBlockAssociation: VpcCidrBlockAssociationTypeDef
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VpcTypeDef(BaseModel):
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

class VpcPeeringConnectionTypeDef(BaseModel):
    AccepterVpcInfo: Optional[VpcPeeringConnectionVpcInfoTypeDef] = None
    ExpirationTime: Optional[datetime] = None
    RequesterVpcInfo: Optional[VpcPeeringConnectionVpcInfoTypeDef] = None
    Status: Optional[VpcPeeringConnectionStateReasonTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    VpcPeeringConnectionId: Optional[str] = None

class AssociateInstanceEventWindowResultTypeDef(BaseModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceEventWindowResultTypeDef(BaseModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeInstanceEventWindowsResultTypeDef(BaseModel):
    InstanceEventWindows: List[InstanceEventWindowTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisassociateInstanceEventWindowResultTypeDef(BaseModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyInstanceEventWindowResultTypeDef(BaseModel):
    InstanceEventWindow: InstanceEventWindowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptAddressTransferRequestRequestTypeDef(BaseModel):
    Address: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class AllocateAddressRequestRequestTypeDef(BaseModel):
    Domain: Optional[DomainTypeType] = None
    Address: Optional[str] = None
    PublicIpv4Pool: Optional[str] = None
    NetworkBorderGroup: Optional[str] = None
    CustomerOwnedIpv4Pool: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class AllocateHostsRequestRequestTypeDef(BaseModel):
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

class AssociateIpamResourceDiscoveryRequestRequestTypeDef(BaseModel):
    IpamId: str
    IpamResourceDiscoveryId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CopyImageRequestRequestTypeDef(BaseModel):
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

class CopySnapshotRequestRequestTypeDef(BaseModel):
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

class CreateCapacityReservationFleetRequestRequestTypeDef(BaseModel):
    InstanceTypeSpecifications: Sequence[ReservationFleetInstanceSpecificationTypeDef]
    TotalTargetCapacity: int
    AllocationStrategy: Optional[str] = None
    ClientToken: Optional[str] = None
    Tenancy: Optional[Literal["default"]] = None
    EndDate: Optional[TimestampTypeDef] = None
    InstanceMatchCriteria: Optional[Literal["open"]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateCapacityReservationRequestRequestTypeDef(BaseModel):
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

class CreateCarrierGatewayRequestRequestTypeDef(BaseModel):
    VpcId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class CreateClientVpnEndpointRequestRequestTypeDef(BaseModel):
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

class CreateCoipPoolRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateCustomerGatewayRequestRequestTypeDef(BaseModel):
    Type: Literal["ipsec.1"]
    BgpAsn: Optional[int] = None
    PublicIp: Optional[str] = None
    CertificateArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DeviceName: Optional[str] = None
    IpAddress: Optional[str] = None
    DryRun: Optional[bool] = None
    BgpAsnExtended: Optional[int] = None

class CreateDhcpOptionsRequestRequestTypeDef(BaseModel):
    DhcpConfigurations: Sequence[NewDhcpConfigurationTypeDef]
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef(BaseModel):
    DhcpConfigurations: Sequence[NewDhcpConfigurationTypeDef]
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateEgressOnlyInternetGatewayRequestRequestTypeDef(BaseModel):
    VpcId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateFlowLogsRequestRequestTypeDef(BaseModel):
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

class CreateFpgaImageRequestRequestTypeDef(BaseModel):
    InputStorageLocation: StorageLocationTypeDef
    DryRun: Optional[bool] = None
    LogsStorageLocation: Optional[StorageLocationTypeDef] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateImageRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    BlockDeviceMappings: Optional[Sequence[BlockDeviceMappingTypeDef]] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    NoReboot: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInstanceConnectEndpointRequestRequestTypeDef(BaseModel):
    SubnetId: str
    DryRun: Optional[bool] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    PreserveClientIp: Optional[bool] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInstanceEventWindowRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Name: Optional[str] = None
    TimeRanges: Optional[Sequence[InstanceEventWindowTimeRangeRequestTypeDef]] = None
    CronExpression: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInstanceExportTaskRequestRequestTypeDef(BaseModel):
    ExportToS3Task: ExportToS3TaskSpecificationTypeDef
    InstanceId: str
    TargetEnvironment: ExportEnvironmentType
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateInternetGatewayRequestRequestTypeDef(BaseModel):
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef(BaseModel):
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateIpamPoolRequestRequestTypeDef(BaseModel):
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

class CreateIpamRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    Tier: Optional[IpamTierType] = None

class CreateIpamResourceDiscoveryRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    OperatingRegions: Optional[Sequence[AddIpamOperatingRegionTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateIpamScopeRequestRequestTypeDef(BaseModel):
    IpamId: str
    DryRun: Optional[bool] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateKeyPairRequestRequestTypeDef(BaseModel):
    KeyName: str
    DryRun: Optional[bool] = None
    KeyType: Optional[KeyTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    KeyFormat: Optional[KeyFormatType] = None

class CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef(BaseModel):
    KeyName: str
    DryRun: Optional[bool] = None
    KeyType: Optional[KeyTypeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    KeyFormat: Optional[KeyFormatType] = None

class CreateLocalGatewayRouteTableRequestRequestTypeDef(BaseModel):
    LocalGatewayId: str
    Mode: Optional[LocalGatewayRouteTableModeType] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    LocalGatewayVirtualInterfaceGroupId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef(BaseModel):
    LocalGatewayRouteTableId: str
    VpcId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateManagedPrefixListRequestRequestTypeDef(BaseModel):
    PrefixListName: str
    MaxEntries: int
    AddressFamily: str
    DryRun: Optional[bool] = None
    Entries: Optional[Sequence[AddPrefixListEntryTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNatGatewayRequestRequestTypeDef(BaseModel):
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

class CreateNetworkAclRequestRequestTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateNetworkInsightsPathRequestRequestTypeDef(BaseModel):
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

class CreateNetworkInterfaceRequestRequestTypeDef(BaseModel):
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

class CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef(BaseModel):
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

class CreatePlacementGroupRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    GroupName: Optional[str] = None
    Strategy: Optional[PlacementStrategyType] = None
    PartitionCount: Optional[int] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    SpreadLevel: Optional[SpreadLevelType] = None

class CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    GroupName: Optional[str] = None
    Strategy: Optional[PlacementStrategyType] = None
    PartitionCount: Optional[int] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    SpreadLevel: Optional[SpreadLevelType] = None

class CreatePublicIpv4PoolRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    NetworkBorderGroup: Optional[str] = None

class CreateReplaceRootVolumeTaskRequestRequestTypeDef(BaseModel):
    InstanceId: str
    SnapshotId: Optional[str] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ImageId: Optional[str] = None
    DeleteReplacedRootVolume: Optional[bool] = None

class CreateRestoreImageTaskRequestRequestTypeDef(BaseModel):
    Bucket: str
    ObjectKey: str
    Name: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateRouteTableRequestRequestTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None

class CreateSecurityGroupRequestRequestTypeDef(BaseModel):
    Description: str
    GroupName: str
    VpcId: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef(BaseModel):
    Description: str
    GroupName: str
    VpcId: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotRequestRequestTypeDef(BaseModel):
    VolumeId: str
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef(BaseModel):
    VolumeId: str
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateSnapshotsRequestRequestTypeDef(BaseModel):
    InstanceSpecification: InstanceSpecificationTypeDef
    Description: Optional[str] = None
    OutpostArn: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    CopyTagsFromSource: Optional[Literal["volume"]] = None

class CreateSubnetCidrReservationRequestRequestTypeDef(BaseModel):
    SubnetId: str
    Cidr: str
    ReservationType: SubnetCidrReservationTypeType
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateSubnetRequestRequestTypeDef(BaseModel):
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

class CreateSubnetRequestServiceResourceCreateSubnetTypeDef(BaseModel):
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

class CreateTrafficMirrorFilterRequestRequestTypeDef(BaseModel):
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None

class CreateTrafficMirrorFilterRuleRequestRequestTypeDef(BaseModel):
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

class CreateTrafficMirrorSessionRequestRequestTypeDef(BaseModel):
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

class CreateTrafficMirrorTargetRequestRequestTypeDef(BaseModel):
    NetworkInterfaceId: Optional[str] = None
    NetworkLoadBalancerArn: Optional[str] = None
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    GatewayLoadBalancerEndpointId: Optional[str] = None

class CreateTransitGatewayConnectPeerRequestRequestTypeDef(BaseModel):
    TransitGatewayAttachmentId: str
    PeerAddress: str
    InsideCidrBlocks: Sequence[str]
    TransitGatewayAddress: Optional[str] = None
    BgpOptions: Optional[TransitGatewayConnectRequestBgpOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayConnectRequestRequestTypeDef(BaseModel):
    TransportTransitGatewayAttachmentId: str
    Options: CreateTransitGatewayConnectRequestOptionsTypeDef
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayMulticastDomainRequestRequestTypeDef(BaseModel):
    TransitGatewayId: str
    Options: Optional[CreateTransitGatewayMulticastDomainRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayId: str
    PeerTransitGatewayId: str
    PeerAccountId: str
    PeerRegion: str
    Options: Optional[CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayPolicyTableRequestRequestTypeDef(BaseModel):
    TransitGatewayId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayRequestRequestTypeDef(BaseModel):
    Description: Optional[str] = None
    Options: Optional[TransitGatewayRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef(BaseModel):
    TransitGatewayRouteTableId: str
    PeeringAttachmentId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayRouteTableRequestRequestTypeDef(BaseModel):
    TransitGatewayId: str
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateTransitGatewayVpcAttachmentRequestRequestTypeDef(BaseModel):
    TransitGatewayId: str
    VpcId: str
    SubnetIds: Sequence[str]
    Options: Optional[CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class CreateVerifiedAccessEndpointRequestRequestTypeDef(BaseModel):
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

class CreateVerifiedAccessGroupRequestRequestTypeDef(BaseModel):
    VerifiedAccessInstanceId: str
    Description: Optional[str] = None
    PolicyDocument: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    SseSpecification: Optional[VerifiedAccessSseSpecificationRequestTypeDef] = None

class CreateVerifiedAccessInstanceRequestRequestTypeDef(BaseModel):
    Description: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    FIPSEnabled: Optional[bool] = None

class CreateVerifiedAccessTrustProviderRequestRequestTypeDef(BaseModel):
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

class CreateVolumeRequestRequestTypeDef(BaseModel):
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

class CreateVolumeRequestServiceResourceCreateVolumeTypeDef(BaseModel):
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

class CreateVpcEndpointRequestRequestTypeDef(BaseModel):
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

class CreateVpcEndpointServiceConfigurationRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    AcceptanceRequired: Optional[bool] = None
    PrivateDnsName: Optional[str] = None
    NetworkLoadBalancerArns: Optional[Sequence[str]] = None
    GatewayLoadBalancerArns: Optional[Sequence[str]] = None
    SupportedIpAddressTypes: Optional[Sequence[str]] = None
    ClientToken: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpcPeeringConnectionRequestRequestTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    PeerOwnerId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef(BaseModel):
    VpcId: str
    DryRun: Optional[bool] = None
    PeerOwnerId: Optional[str] = None
    PeerVpcId: Optional[str] = None
    PeerRegion: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateVpcRequestRequestTypeDef(BaseModel):
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

class CreateVpcRequestServiceResourceCreateVpcTypeDef(BaseModel):
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

class CreateVpnGatewayRequestRequestTypeDef(BaseModel):
    Type: Literal["ipsec.1"]
    AvailabilityZone: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    AmazonSideAsn: Optional[int] = None
    DryRun: Optional[bool] = None

class ExportImageRequestRequestTypeDef(BaseModel):
    DiskImageFormat: DiskImageFormatType
    ImageId: str
    S3ExportLocation: ExportTaskS3LocationRequestTypeDef
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    RoleName: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ImportImageRequestRequestTypeDef(BaseModel):
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

class ImportKeyPairRequestRequestTypeDef(BaseModel):
    KeyName: str
    PublicKeyMaterial: BlobTypeDef
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ImportKeyPairRequestServiceResourceImportKeyPairTypeDef(BaseModel):
    KeyName: str
    PublicKeyMaterial: BlobTypeDef
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ImportSnapshotRequestRequestTypeDef(BaseModel):
    ClientData: Optional[ClientDataTypeDef] = None
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    DiskContainer: Optional[SnapshotDiskContainerTypeDef] = None
    DryRun: Optional[bool] = None
    Encrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    RoleName: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class ProvisionByoipCidrRequestRequestTypeDef(BaseModel):
    Cidr: str
    CidrAuthorizationContext: Optional[CidrAuthorizationContextTypeDef] = None
    PubliclyAdvertisable: Optional[bool] = None
    Description: Optional[str] = None
    DryRun: Optional[bool] = None
    PoolTagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    MultiRegion: Optional[bool] = None
    NetworkBorderGroup: Optional[str] = None

class PurchaseCapacityBlockRequestRequestTypeDef(BaseModel):
    CapacityBlockOfferingId: str
    InstancePlatform: CapacityReservationInstancePlatformType
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class PurchaseHostReservationRequestRequestTypeDef(BaseModel):
    HostIdSet: Sequence[str]
    OfferingId: str
    ClientToken: Optional[str] = None
    CurrencyCode: Optional[Literal["USD"]] = None
    LimitPrice: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class RegisterImageRequestRequestTypeDef(BaseModel):
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

class RegisterImageRequestServiceResourceRegisterImageTypeDef(BaseModel):
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

class StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef(BaseModel):
    NetworkInsightsAccessScopeId: str
    ClientToken: str
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class StartNetworkInsightsAnalysisRequestRequestTypeDef(BaseModel):
    NetworkInsightsPathId: str
    ClientToken: str
    AdditionalAccounts: Optional[Sequence[str]] = None
    FilterInArns: Optional[Sequence[str]] = None
    DryRun: Optional[bool] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class PathComponentTypeDef(BaseModel):
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

class CreateRouteTableResultTypeDef(BaseModel):
    RouteTable: RouteTableTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRouteTablesResultTypeDef(BaseModel):
    RouteTables: List[RouteTableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetFlowLogsIntegrationTemplateRequestRequestTypeDef(BaseModel):
    FlowLogId: str
    ConfigDeliveryS3DestinationArn: str
    IntegrateServices: IntegrateServicesTypeDef
    DryRun: Optional[bool] = None

class DescribeNetworkInterfaceAttributeResultTypeDef(BaseModel):
    Attachment: NetworkInterfaceAttachmentTypeDef
    Description: AttributeValueTypeDef
    Groups: List[GroupIdentifierTypeDef]
    NetworkInterfaceId: str
    SourceDestCheck: AttributeBooleanValueTypeDef
    AssociatePublicIpAddress: bool
    ResponseMetadata: ResponseMetadataTypeDef

class NetworkInterfaceTypeDef(BaseModel):
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

class CreateDhcpOptionsResultTypeDef(BaseModel):
    DhcpOptions: DhcpOptionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDhcpOptionsResultTypeDef(BaseModel):
    DhcpOptions: List[DhcpOptionsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeHostsResultTypeDef(BaseModel):
    Hosts: List[HostTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BundleInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Storage: StorageTypeDef
    DryRun: Optional[bool] = None

class DescribeImagesResultTypeDef(BaseModel):
    Images: List[ImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeClientVpnEndpointsResultTypeDef(BaseModel):
    ClientVpnEndpoints: List[ClientVpnEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVpnTunnelOptionsRequestRequestTypeDef(BaseModel):
    VpnConnectionId: str
    VpnTunnelOutsideIpAddress: str
    TunnelOptions: ModifyVpnTunnelOptionsSpecificationTypeDef
    DryRun: Optional[bool] = None
    SkipTunnelReplacement: Optional[bool] = None

class VpnConnectionOptionsSpecificationTypeDef(BaseModel):
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

class VpnConnectionOptionsTypeDef(BaseModel):
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

class CreateNetworkAclResultTypeDef(BaseModel):
    NetworkAcl: NetworkAclTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkAclsResultTypeDef(BaseModel):
    NetworkAcls: List[NetworkAclTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DisableFastSnapshotRestoresResultTypeDef(BaseModel):
    Successful: List[DisableFastSnapshotRestoreSuccessItemTypeDef]
    Unsuccessful: List[DisableFastSnapshotRestoreErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConversionTaskTypeDef(BaseModel):
    ConversionTaskId: Optional[str] = None
    ExpirationTime: Optional[str] = None
    ImportInstance: Optional[ImportInstanceTaskDetailsTypeDef] = None
    ImportVolume: Optional[ImportVolumeTaskDetailsTypeDef] = None
    State: Optional[ConversionTaskStateType] = None
    StatusMessage: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None

class SpotFleetLaunchSpecificationExtraOutputTypeDef(BaseModel):
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

class LaunchSpecificationTypeDef(BaseModel):
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

class SpotFleetLaunchSpecificationOutputTypeDef(BaseModel):
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

class RequestSpotLaunchSpecificationTypeDef(BaseModel):
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

class RunInstancesRequestSubnetCreateInstancesTypeDef(BaseModel):
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

class SpotFleetLaunchSpecificationTypeDef(BaseModel):
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

class RequestLaunchTemplateDataTypeDef(BaseModel):
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

class EnableFastSnapshotRestoresResultTypeDef(BaseModel):
    Successful: List[EnableFastSnapshotRestoreSuccessItemTypeDef]
    Unsuccessful: List[EnableFastSnapshotRestoreErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNetworkInsightsPathResultTypeDef(BaseModel):
    NetworkInsightsPath: NetworkInsightsPathTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInsightsPathsResultTypeDef(BaseModel):
    NetworkInsightsPaths: List[NetworkInsightsPathTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceNetworkInterfaceTypeDef(BaseModel):
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

class LaunchTemplateConfigExtraOutputTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[LaunchTemplateOverridesExtraOutputTypeDef]] = None

class FleetLaunchTemplateConfigTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[FleetLaunchTemplateOverridesTypeDef]] = None

class LaunchTemplateAndOverridesResponseTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[FleetLaunchTemplateOverridesTypeDef] = None

class LaunchTemplateConfigOutputTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[List[LaunchTemplateOverridesOutputTypeDef]] = None

class LaunchTemplateConfigTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationTypeDef] = None
    Overrides: Optional[Sequence[LaunchTemplateOverridesTypeDef]] = None

class FleetLaunchTemplateConfigRequestTypeDef(BaseModel):
    LaunchTemplateSpecification: Optional[FleetLaunchTemplateSpecificationRequestTypeDef] = None
    Overrides: Optional[Sequence[FleetLaunchTemplateOverridesRequestTypeDef]] = None

class GetSpotPlacementScoresRequestGetSpotPlacementScoresPaginateTypeDef(BaseModel):
    TargetCapacity: int
    InstanceTypes: Optional[Sequence[str]] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    SingleAvailabilityZone: Optional[bool] = None
    RegionNames: Optional[Sequence[str]] = None
    InstanceRequirementsWithMetadata: Optional[       InstanceRequirementsWithMetadataRequestTypeDef     ] = None
    DryRun: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSpotPlacementScoresRequestRequestTypeDef(BaseModel):
    TargetCapacity: int
    InstanceTypes: Optional[Sequence[str]] = None
    TargetCapacityUnitType: Optional[TargetCapacityUnitTypeType] = None
    SingleAvailabilityZone: Optional[bool] = None
    RegionNames: Optional[Sequence[str]] = None
    InstanceRequirementsWithMetadata: Optional[       InstanceRequirementsWithMetadataRequestTypeDef     ] = None
    DryRun: Optional[bool] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeInstanceStatusResultTypeDef(BaseModel):
    InstanceStatuses: List[InstanceStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSecurityGroupsResultTypeDef(BaseModel):
    SecurityGroups: List[SecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AuthorizeSecurityGroupEgressRequestRequestTypeDef(BaseModel):
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

class AuthorizeSecurityGroupIngressRequestRequestTypeDef(BaseModel):
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

class RevokeSecurityGroupEgressRequestRequestTypeDef(BaseModel):
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

class RevokeSecurityGroupIngressRequestRequestTypeDef(BaseModel):
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

class UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    SecurityGroupRuleDescriptions: Optional[Sequence[SecurityGroupRuleDescriptionTypeDef]] = None

class UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef(BaseModel):
    DryRun: Optional[bool] = None
    GroupId: Optional[str] = None
    GroupName: Optional[str] = None
    IpPermissions: Optional[Sequence[IpPermissionUnionTypeDef]] = None
    SecurityGroupRuleDescriptions: Optional[Sequence[SecurityGroupRuleDescriptionTypeDef]] = None

class DescribeStaleSecurityGroupsResultTypeDef(BaseModel):
    StaleSecurityGroupSet: List[StaleSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetIpamDiscoveredPublicAddressesResultTypeDef(BaseModel):
    IpamDiscoveredPublicAddresses: List[IpamDiscoveredPublicAddressTypeDef]
    OldestSampleTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ResponseLaunchTemplateDataTypeDef(BaseModel):
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

class DescribeReservedInstancesModificationsResultTypeDef(BaseModel):
    ReservedInstancesModifications: List[ReservedInstancesModificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceTypeInfoTypeDef(BaseModel):
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

class CreateNetworkInsightsAccessScopeRequestRequestTypeDef(BaseModel):
    ClientToken: str
    MatchPaths: Optional[Sequence[AccessScopePathRequestTypeDef]] = None
    ExcludePaths: Optional[Sequence[AccessScopePathRequestTypeDef]] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None
    DryRun: Optional[bool] = None

class NetworkInsightsAccessScopeContentTypeDef(BaseModel):
    NetworkInsightsAccessScopeId: Optional[str] = None
    MatchPaths: Optional[List[AccessScopePathTypeDef]] = None
    ExcludePaths: Optional[List[AccessScopePathTypeDef]] = None

class BundleInstanceResultTypeDef(BaseModel):
    BundleTask: BundleTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CancelBundleTaskResultTypeDef(BaseModel):
    BundleTask: BundleTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBundleTasksResultTypeDef(BaseModel):
    BundleTasks: List[BundleTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RunScheduledInstancesRequestRequestTypeDef(BaseModel):
    LaunchSpecification: ScheduledInstancesLaunchSpecificationTypeDef
    ScheduledInstanceId: str
    ClientToken: Optional[str] = None
    DryRun: Optional[bool] = None
    InstanceCount: Optional[int] = None

class DescribeImportImageTasksResultTypeDef(BaseModel):
    ImportImageTasks: List[ImportImageTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeImportSnapshotTasksResultTypeDef(BaseModel):
    ImportSnapshotTasks: List[ImportSnapshotTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDefaultSubnetResultTypeDef(BaseModel):
    Subnet: SubnetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubnetResultTypeDef(BaseModel):
    Subnet: SubnetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubnetsResultTypeDef(BaseModel):
    Subnets: List[SubnetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateTrafficMirrorFilterResultTypeDef(BaseModel):
    TrafficMirrorFilter: TrafficMirrorFilterTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficMirrorFiltersResultTypeDef(BaseModel):
    TrafficMirrorFilters: List[TrafficMirrorFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyTrafficMirrorFilterNetworkServicesResultTypeDef(BaseModel):
    TrafficMirrorFilter: TrafficMirrorFilterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTransitGatewayConnectPeerResultTypeDef(BaseModel):
    TransitGatewayConnectPeer: TransitGatewayConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTransitGatewayConnectPeerResultTypeDef(BaseModel):
    TransitGatewayConnectPeer: TransitGatewayConnectPeerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTransitGatewayConnectPeersResultTypeDef(BaseModel):
    TransitGatewayConnectPeers: List[TransitGatewayConnectPeerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTransitGatewayPolicyTableEntriesResultTypeDef(BaseModel):
    TransitGatewayPolicyTableEntries: List[TransitGatewayPolicyTableEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class VerifiedAccessInstanceLoggingConfigurationTypeDef(BaseModel):
    VerifiedAccessInstanceId: Optional[str] = None
    AccessLogs: Optional[VerifiedAccessLogsTypeDef] = None

class DescribeVolumeStatusResultTypeDef(BaseModel):
    VolumeStatuses: List[VolumeStatusItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDefaultVpcResultTypeDef(BaseModel):
    Vpc: VpcTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcResultTypeDef(BaseModel):
    Vpc: VpcTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcsResultTypeDef(BaseModel):
    Vpcs: List[VpcTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AcceptVpcPeeringConnectionResultTypeDef(BaseModel):
    VpcPeeringConnection: VpcPeeringConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpcPeeringConnectionResultTypeDef(BaseModel):
    VpcPeeringConnection: VpcPeeringConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpcPeeringConnectionsResultTypeDef(BaseModel):
    VpcPeeringConnections: List[VpcPeeringConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AccessScopeAnalysisFindingTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: Optional[str] = None
    NetworkInsightsAccessScopeId: Optional[str] = None
    FindingId: Optional[str] = None
    FindingComponents: Optional[List[PathComponentTypeDef]] = None

class NetworkInsightsAnalysisTypeDef(BaseModel):
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

class CreateNetworkInterfaceResultTypeDef(BaseModel):
    NetworkInterface: NetworkInterfaceTypeDef
    ClientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNetworkInterfacesResultTypeDef(BaseModel):
    NetworkInterfaces: List[NetworkInterfaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateVpnConnectionRequestRequestTypeDef(BaseModel):
    CustomerGatewayId: str
    Type: str
    VpnGatewayId: Optional[str] = None
    TransitGatewayId: Optional[str] = None
    DryRun: Optional[bool] = None
    Options: Optional[VpnConnectionOptionsSpecificationTypeDef] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class VpnConnectionTypeDef(BaseModel):
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

class DescribeConversionTasksResultTypeDef(BaseModel):
    ConversionTasks: List[ConversionTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportInstanceResultTypeDef(BaseModel):
    ConversionTask: ConversionTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportVolumeResultTypeDef(BaseModel):
    ConversionTask: ConversionTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SpotInstanceRequestTypeDef(BaseModel):
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

class RunInstancesRequestRequestTypeDef(BaseModel):
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

class RunInstancesRequestServiceResourceCreateInstancesTypeDef(BaseModel):
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

class RequestSpotInstancesRequestRequestTypeDef(BaseModel):
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

class CreateLaunchTemplateRequestRequestTypeDef(BaseModel):
    LaunchTemplateName: str
    LaunchTemplateData: RequestLaunchTemplateDataTypeDef
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    VersionDescription: Optional[str] = None
    TagSpecifications: Optional[Sequence[TagSpecificationUnionTypeDef]] = None

class CreateLaunchTemplateVersionRequestRequestTypeDef(BaseModel):
    LaunchTemplateData: RequestLaunchTemplateDataTypeDef
    DryRun: Optional[bool] = None
    ClientToken: Optional[str] = None
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    SourceVersion: Optional[str] = None
    VersionDescription: Optional[str] = None
    ResolveAlias: Optional[bool] = None

class InstanceTypeDef(BaseModel):
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

class SpotFleetRequestConfigDataExtraOutputTypeDef(BaseModel):
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

class CreateFleetErrorTypeDef(BaseModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class CreateFleetInstanceTypeDef(BaseModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    InstanceIds: Optional[List[str]] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[Literal["windows"]] = None

class DescribeFleetErrorTypeDef(BaseModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class DescribeFleetsInstancesTypeDef(BaseModel):
    LaunchTemplateAndOverrides: Optional[LaunchTemplateAndOverridesResponseTypeDef] = None
    Lifecycle: Optional[InstanceLifecycleType] = None
    InstanceIds: Optional[List[str]] = None
    InstanceType: Optional[InstanceTypeType] = None
    Platform: Optional[Literal["windows"]] = None

class SpotFleetRequestConfigDataOutputTypeDef(BaseModel):
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

class SpotFleetRequestConfigDataTypeDef(BaseModel):
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

class CreateFleetRequestRequestTypeDef(BaseModel):
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

class ModifyFleetRequestRequestTypeDef(BaseModel):
    FleetId: str
    DryRun: Optional[bool] = None
    ExcessCapacityTerminationPolicy: Optional[FleetExcessCapacityTerminationPolicyType] = None
    LaunchTemplateConfigs: Optional[Sequence[FleetLaunchTemplateConfigRequestTypeDef]] = None
    TargetCapacitySpecification: Optional[TargetCapacitySpecificationRequestTypeDef] = None
    Context: Optional[str] = None

class GetLaunchTemplateDataResultTypeDef(BaseModel):
    LaunchTemplateData: ResponseLaunchTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class LaunchTemplateVersionTypeDef(BaseModel):
    LaunchTemplateId: Optional[str] = None
    LaunchTemplateName: Optional[str] = None
    VersionNumber: Optional[int] = None
    VersionDescription: Optional[str] = None
    CreateTime: Optional[datetime] = None
    CreatedBy: Optional[str] = None
    DefaultVersion: Optional[bool] = None
    LaunchTemplateData: Optional[ResponseLaunchTemplateDataTypeDef] = None

class DescribeInstanceTypesResultTypeDef(BaseModel):
    InstanceTypes: List[InstanceTypeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateNetworkInsightsAccessScopeResultTypeDef(BaseModel):
    NetworkInsightsAccessScope: NetworkInsightsAccessScopeTypeDef
    NetworkInsightsAccessScopeContent: NetworkInsightsAccessScopeContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkInsightsAccessScopeContentResultTypeDef(BaseModel):
    NetworkInsightsAccessScopeContent: NetworkInsightsAccessScopeContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef(BaseModel):
    LoggingConfigurations: List[VerifiedAccessInstanceLoggingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef(BaseModel):
    LoggingConfiguration: VerifiedAccessInstanceLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef(BaseModel):
    NetworkInsightsAccessScopeAnalysisId: str
    AnalysisStatus: AnalysisStatusType
    AnalysisFindings: List[AccessScopeAnalysisFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeNetworkInsightsAnalysesResultTypeDef(BaseModel):
    NetworkInsightsAnalyses: List[NetworkInsightsAnalysisTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartNetworkInsightsAnalysisResultTypeDef(BaseModel):
    NetworkInsightsAnalysis: NetworkInsightsAnalysisTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVpnConnectionResultTypeDef(BaseModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVpnConnectionsResultTypeDef(BaseModel):
    VpnConnections: List[VpnConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnConnectionOptionsResultTypeDef(BaseModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnConnectionResultTypeDef(BaseModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnTunnelCertificateResultTypeDef(BaseModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyVpnTunnelOptionsResultTypeDef(BaseModel):
    VpnConnection: VpnConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSpotInstanceRequestsResultTypeDef(BaseModel):
    SpotInstanceRequests: List[SpotInstanceRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RequestSpotInstancesResultTypeDef(BaseModel):
    SpotInstanceRequests: List[SpotInstanceRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationResponseTypeDef(BaseModel):
    Groups: List[GroupIdentifierTypeDef]
    Instances: List[InstanceTypeDef]
    OwnerId: str
    RequesterId: str
    ReservationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReservationTypeDef(BaseModel):
    Groups: Optional[List[GroupIdentifierTypeDef]] = None
    Instances: Optional[List[InstanceTypeDef]] = None
    OwnerId: Optional[str] = None
    RequesterId: Optional[str] = None
    ReservationId: Optional[str] = None

class CreateFleetResultTypeDef(BaseModel):
    FleetId: str
    Errors: List[CreateFleetErrorTypeDef]
    Instances: List[CreateFleetInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FleetDataTypeDef(BaseModel):
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

class SpotFleetRequestConfigTypeDef(BaseModel):
    ActivityStatus: Optional[ActivityStatusType] = None
    CreateTime: Optional[datetime] = None
    SpotFleetRequestConfig: Optional[SpotFleetRequestConfigDataOutputTypeDef] = None
    SpotFleetRequestId: Optional[str] = None
    SpotFleetRequestState: Optional[BatchStateType] = None
    Tags: Optional[List[TagTypeDef]] = None

class ModifySpotFleetRequestRequestRequestTypeDef(BaseModel):
    SpotFleetRequestId: str
    ExcessCapacityTerminationPolicy: Optional[ExcessCapacityTerminationPolicyType] = None
    LaunchTemplateConfigs: Optional[Sequence[LaunchTemplateConfigUnionTypeDef]] = None
    TargetCapacity: Optional[int] = None
    OnDemandTargetCapacity: Optional[int] = None
    Context: Optional[str] = None

class RequestSpotFleetRequestRequestTypeDef(BaseModel):
    SpotFleetRequestConfig: SpotFleetRequestConfigDataTypeDef
    DryRun: Optional[bool] = None

class CreateLaunchTemplateVersionResultTypeDef(BaseModel):
    LaunchTemplateVersion: LaunchTemplateVersionTypeDef
    Warning: ValidationWarningTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLaunchTemplateVersionsResultTypeDef(BaseModel):
    LaunchTemplateVersions: List[LaunchTemplateVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeInstancesResultTypeDef(BaseModel):
    Reservations: List[ReservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeFleetsResultTypeDef(BaseModel):
    Fleets: List[FleetDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSpotFleetRequestsResponseTypeDef(BaseModel):
    SpotFleetRequestConfigs: List[SpotFleetRequestConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

