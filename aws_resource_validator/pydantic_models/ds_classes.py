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
from aws_resource_validator.pydantic_models.ds_constants import *

class AcceptSharedDirectoryRequestRequestTypeDef(BaseValidatorModel):
    SharedDirectoryId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SharedDirectoryTypeDef(BaseValidatorModel):
    OwnerAccountId: Optional[str] = None
    OwnerDirectoryId: Optional[str] = None
    ShareMethod: Optional[ShareMethodType] = None
    SharedAccountId: Optional[str] = None
    SharedDirectoryId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None
    ShareNotes: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None

class IpRouteTypeDef(BaseValidatorModel):
    CidrIp: Optional[str] = None
    Description: Optional[str] = None

class DirectoryVpcSettingsTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class AttributeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class CancelSchemaExtensionRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SchemaExtensionId: str

class CertificateInfoTypeDef(BaseValidatorModel):
    CertificateId: Optional[str] = None
    CommonName: Optional[str] = None
    State: Optional[CertificateStateType] = None
    ExpiryDateTime: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None

class ClientCertAuthSettingsTypeDef(BaseValidatorModel):
    OCSPUrl: Optional[str] = None

class ClientAuthenticationSettingInfoTypeDef(BaseValidatorModel):
    Type: Optional[ClientAuthenticationTypeType] = None
    Status: Optional[ClientAuthenticationStatusType] = None
    LastUpdatedDateTime: Optional[datetime] = None

class ConditionalForwarderTypeDef(BaseValidatorModel):
    RemoteDomainName: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    ReplicationScope: Optional[Literal["Domain"]] = None

class DirectoryConnectSettingsTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]
    CustomerDnsIps: Sequence[str]
    CustomerUserName: str

class CreateAliasRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Alias: str

class CreateConditionalForwarderRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]

class CreateLogSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    LogGroupName: str

class CreateSnapshotRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Name: Optional[str] = None

class CreateTrustRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    TrustPassword: str
    TrustDirection: TrustDirectionType
    TrustType: Optional[TrustTypeType] = None
    ConditionalForwarderIpAddrs: Optional[Sequence[str]] = None
    SelectiveAuth: Optional[SelectiveAuthType] = None

class DeleteConditionalForwarderRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str

class DeleteDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str

class DeleteLogSubscriptionRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str

class DeleteSnapshotRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str

class DeleteTrustRequestRequestTypeDef(BaseValidatorModel):
    TrustId: str
    DeleteAssociatedConditionalForwarder: Optional[bool] = None

class DeregisterCertificateRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str

class DeregisterEventTopicRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    TopicName: str

class DescribeCertificateRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClientAuthenticationSettingsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[ClientAuthenticationTypeType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConditionalForwardersRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainNames: Optional[Sequence[str]] = None

class DescribeDirectoriesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeDomainControllersRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    DomainControllerIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DomainControllerTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    DomainControllerId: Optional[str] = None
    DnsIpAddr: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetId: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    Status: Optional[DomainControllerStatusType] = None
    StatusReason: Optional[str] = None
    LaunchTime: Optional[datetime] = None
    StatusLastUpdatedDateTime: Optional[datetime] = None

class DescribeEventTopicsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicNames: Optional[Sequence[str]] = None

class EventTopicTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicName: Optional[str] = None
    TopicArn: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    Status: Optional[TopicStatusType] = None

class DescribeLDAPSSettingsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[Literal["Client"]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class LDAPSSettingInfoTypeDef(BaseValidatorModel):
    LDAPSStatus: Optional[LDAPSStatusType] = None
    LDAPSStatusReason: Optional[str] = None
    LastUpdatedDateTime: Optional[datetime] = None

class DescribeRegionsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RegionName: Optional[str] = None
    NextToken: Optional[str] = None

class DescribeSettingsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Status: Optional[DirectoryConfigurationStatusType] = None
    NextToken: Optional[str] = None

class SettingEntryTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Name: Optional[str] = None
    AllowedValues: Optional[str] = None
    AppliedValue: Optional[str] = None
    RequestedValue: Optional[str] = None
    RequestStatus: Optional[DirectoryConfigurationStatusType] = None
    RequestDetailedStatus: Optional[Dict[str, DirectoryConfigurationStatusType]] = None
    RequestStatusMessage: Optional[str] = None
    LastUpdatedDateTime: Optional[datetime] = None
    LastRequestedDateTime: Optional[datetime] = None
    DataType: Optional[str] = None

class DescribeSharedDirectoriesRequestRequestTypeDef(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class SnapshotTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotId: Optional[str] = None
    Type: Optional[SnapshotTypeType] = None
    Name: Optional[str] = None
    Status: Optional[SnapshotStatusType] = None
    StartTime: Optional[datetime] = None

class DescribeTrustsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class TrustTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustId: Optional[str] = None
    RemoteDomainName: Optional[str] = None
    TrustType: Optional[TrustTypeType] = None
    TrustDirection: Optional[TrustDirectionType] = None
    TrustState: Optional[TrustStateType] = None
    CreatedDateTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None
    StateLastUpdatedDateTime: Optional[datetime] = None
    TrustStateReason: Optional[str] = None
    SelectiveAuth: Optional[SelectiveAuthType] = None

class DescribeUpdateDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    RegionName: Optional[str] = None
    NextToken: Optional[str] = None

class DirectoryConnectSettingsDescriptionTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    CustomerUserName: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    ConnectIps: Optional[List[str]] = None

class DirectoryVpcSettingsDescriptionTypeDef(BaseValidatorModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None

class RadiusSettingsOutputTypeDef(BaseValidatorModel):
    RadiusServers: Optional[List[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None

class RegionsInfoTypeDef(BaseValidatorModel):
    PrimaryRegion: Optional[str] = None
    AdditionalRegions: Optional[List[str]] = None

class DirectoryLimitsTypeDef(BaseValidatorModel):
    CloudOnlyDirectoriesLimit: Optional[int] = None
    CloudOnlyDirectoriesCurrentCount: Optional[int] = None
    CloudOnlyDirectoriesLimitReached: Optional[bool] = None
    CloudOnlyMicrosoftADLimit: Optional[int] = None
    CloudOnlyMicrosoftADCurrentCount: Optional[int] = None
    CloudOnlyMicrosoftADLimitReached: Optional[bool] = None
    ConnectedDirectoriesLimit: Optional[int] = None
    ConnectedDirectoriesCurrentCount: Optional[int] = None
    ConnectedDirectoriesLimitReached: Optional[bool] = None

class DirectoryVpcSettingsExtraOutputTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]

class DirectoryVpcSettingsOutputTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]

class DisableClientAuthenticationRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: ClientAuthenticationTypeType

class DisableLDAPSRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: Literal["Client"]

class DisableRadiusRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str

class DisableSsoRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None

class EnableClientAuthenticationRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: ClientAuthenticationTypeType

class EnableLDAPSRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: Literal["Client"]

class RadiusSettingsTypeDef(BaseValidatorModel):
    RadiusServers: Optional[Sequence[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None

class EnableSsoRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None

class GetSnapshotLimitsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str

class SnapshotLimitsTypeDef(BaseValidatorModel):
    ManualSnapshotsLimit: Optional[int] = None
    ManualSnapshotsCurrentCount: Optional[int] = None
    ManualSnapshotsLimitReached: Optional[bool] = None

class IpRouteInfoTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    CidrIp: Optional[str] = None
    IpRouteStatusMsg: Optional[IpRouteStatusMsgType] = None
    AddedDateTime: Optional[datetime] = None
    IpRouteStatusReason: Optional[str] = None
    Description: Optional[str] = None

class ListCertificatesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListIpRoutesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListLogSubscriptionsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class LogSubscriptionTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    LogGroupName: Optional[str] = None
    SubscriptionCreatedDateTime: Optional[datetime] = None

class ListSchemaExtensionsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class SchemaExtensionInfoTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SchemaExtensionId: Optional[str] = None
    Description: Optional[str] = None
    SchemaExtensionStatus: Optional[SchemaExtensionStatusType] = None
    SchemaExtensionStatusReason: Optional[str] = None
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class OSUpdateSettingsTypeDef(BaseValidatorModel):
    OSVersion: Optional[OSVersionType] = None

class RadiusSettingsExtraOutputTypeDef(BaseValidatorModel):
    RadiusServers: Optional[List[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None

class RegisterEventTopicRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    TopicName: str

class RejectSharedDirectoryRequestRequestTypeDef(BaseValidatorModel):
    SharedDirectoryId: str

class RemoveIpRoutesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CidrIps: Sequence[str]

class RemoveRegionRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str

class RemoveTagsFromResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]

class ResetUserPasswordRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    NewPassword: str

class RestoreFromSnapshotRequestRequestTypeDef(BaseValidatorModel):
    SnapshotId: str

class SettingTypeDef(BaseValidatorModel):
    Name: str
    Value: str

class ShareTargetTypeDef(BaseValidatorModel):
    Id: str
    Type: Literal["ACCOUNT"]

class StartSchemaExtensionRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CreateSnapshotBeforeSchemaExtension: bool
    LdifContent: str
    Description: str

class UnshareTargetTypeDef(BaseValidatorModel):
    Id: str
    Type: Literal["ACCOUNT"]

class UpdateConditionalForwarderRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]

class UpdateNumberOfDomainControllersRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    DesiredNumber: int

class UpdateTrustRequestRequestTypeDef(BaseValidatorModel):
    TrustId: str
    SelectiveAuth: Optional[SelectiveAuthType] = None

class VerifyTrustRequestRequestTypeDef(BaseValidatorModel):
    TrustId: str

class ConnectDirectoryResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAliasResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    Alias: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMicrosoftADResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResultTypeDef(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustResultTypeDef(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectoryResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResultTypeDef(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrustResultTypeDef(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCertificateResultTypeDef(BaseValidatorModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectSharedDirectoryResultTypeDef(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ShareDirectoryResultTypeDef(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaExtensionResultTypeDef(BaseValidatorModel):
    SchemaExtensionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UnshareDirectoryResultTypeDef(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustResultTypeDef(BaseValidatorModel):
    RequestId: str
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyTrustResultTypeDef(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptSharedDirectoryResultTypeDef(BaseValidatorModel):
    SharedDirectory: SharedDirectoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSharedDirectoriesResultTypeDef(BaseValidatorModel):
    SharedDirectories: List[SharedDirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AddIpRoutesRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    IpRoutes: Sequence[IpRouteTypeDef]
    UpdateSecurityGroupForDirectoryControllers: Optional[bool] = None

class AddRegionRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RegionName: str
    VPCSettings: DirectoryVpcSettingsTypeDef

class AddTagsToResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateDirectoryRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    VpcSettings: Optional[DirectoryVpcSettingsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMicrosoftADRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Password: str
    VpcSettings: DirectoryVpcSettingsTypeDef
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Edition: Optional[DirectoryEditionType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ComputerTypeDef(BaseValidatorModel):
    ComputerId: Optional[str] = None
    ComputerName: Optional[str] = None
    ComputerAttributes: Optional[List[AttributeTypeDef]] = None

class CreateComputerRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    ComputerName: str
    Password: str
    OrganizationalUnitDistinguishedName: Optional[str] = None
    ComputerAttributes: Optional[Sequence[AttributeTypeDef]] = None

class ListCertificatesResultTypeDef(BaseValidatorModel):
    CertificatesInfo: List[CertificateInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CertificateTypeDef(BaseValidatorModel):
    CertificateId: Optional[str] = None
    State: Optional[CertificateStateType] = None
    StateReason: Optional[str] = None
    CommonName: Optional[str] = None
    RegisteredDateTime: Optional[datetime] = None
    ExpiryDateTime: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None
    ClientCertAuthSettings: Optional[ClientCertAuthSettingsTypeDef] = None

class RegisterCertificateRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CertificateData: str
    Type: Optional[CertificateTypeType] = None
    ClientCertAuthSettings: Optional[ClientCertAuthSettingsTypeDef] = None

class DescribeClientAuthenticationSettingsResultTypeDef(BaseValidatorModel):
    ClientAuthenticationSettingsInfo: List[ClientAuthenticationSettingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConditionalForwardersResultTypeDef(BaseValidatorModel):
    ConditionalForwarders: List[ConditionalForwarderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectDirectoryRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ConnectSettings: DirectoryConnectSettingsTypeDef
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeClientAuthenticationSettingsRequestDescribeClientAuthenticationSettingsPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[ClientAuthenticationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDirectoriesRequestDescribeDirectoriesPaginateTypeDef(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDomainControllersRequestDescribeDomainControllersPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    DomainControllerIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLDAPSSettingsRequestDescribeLDAPSSettingsPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[Literal["Client"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegionsRequestDescribeRegionsPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    RegionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSharedDirectoriesRequestDescribeSharedDirectoriesPaginateTypeDef(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrustsRequestDescribeTrustsPaginateTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUpdateDirectoryRequestDescribeUpdateDirectoryPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    RegionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesRequestListCertificatesPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIpRoutesRequestListIpRoutesPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLogSubscriptionsRequestListLogSubscriptionsPaginateTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaExtensionsRequestListSchemaExtensionsPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDomainControllersResultTypeDef(BaseValidatorModel):
    DomainControllers: List[DomainControllerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEventTopicsResultTypeDef(BaseValidatorModel):
    EventTopics: List[EventTopicTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLDAPSSettingsResultTypeDef(BaseValidatorModel):
    LDAPSSettingsInfo: List[LDAPSSettingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSettingsResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    SettingEntries: List[SettingEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSnapshotsResultTypeDef(BaseValidatorModel):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeTrustsResultTypeDef(BaseValidatorModel):
    Trusts: List[TrustTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OwnerDirectoryDescriptionTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    AccountId: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    VpcSettings: Optional[DirectoryVpcSettingsDescriptionTypeDef] = None
    RadiusSettings: Optional[RadiusSettingsOutputTypeDef] = None
    RadiusStatus: Optional[RadiusStatusType] = None

class GetDirectoryLimitsResultTypeDef(BaseValidatorModel):
    DirectoryLimits: DirectoryLimitsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegionDescriptionTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    RegionName: Optional[str] = None
    RegionType: Optional[RegionTypeType] = None
    Status: Optional[DirectoryStageType] = None
    VpcSettings: Optional[DirectoryVpcSettingsOutputTypeDef] = None
    DesiredNumberOfDomainControllers: Optional[int] = None
    LaunchTime: Optional[datetime] = None
    StatusLastUpdatedDateTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None

class EnableRadiusRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsTypeDef

class UpdateRadiusRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsTypeDef

class GetSnapshotLimitsResultTypeDef(BaseValidatorModel):
    SnapshotLimits: SnapshotLimitsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIpRoutesResultTypeDef(BaseValidatorModel):
    IpRoutesInfo: List[IpRouteInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListLogSubscriptionsResultTypeDef(BaseValidatorModel):
    LogSubscriptions: List[LogSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSchemaExtensionsResultTypeDef(BaseValidatorModel):
    SchemaExtensionsInfo: List[SchemaExtensionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateDirectorySetupRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    OSUpdateSettings: Optional[OSUpdateSettingsTypeDef] = None
    CreateSnapshotBeforeUpdate: Optional[bool] = None

class UpdateValueTypeDef(BaseValidatorModel):
    OSUpdateSettings: Optional[OSUpdateSettingsTypeDef] = None

class UpdateSettingsRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Settings: Sequence[SettingTypeDef]

class ShareDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    ShareTarget: ShareTargetTypeDef
    ShareMethod: ShareMethodType
    ShareNotes: Optional[str] = None

class UnshareDirectoryRequestRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UnshareTarget: UnshareTargetTypeDef

class CreateComputerResultTypeDef(BaseValidatorModel):
    Computer: ComputerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateResultTypeDef(BaseValidatorModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DirectoryDescriptionTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    Name: Optional[str] = None
    ShortName: Optional[str] = None
    Size: Optional[DirectorySizeType] = None
    Edition: Optional[DirectoryEditionType] = None
    Alias: Optional[str] = None
    AccessUrl: Optional[str] = None
    Description: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    Stage: Optional[DirectoryStageType] = None
    ShareStatus: Optional[ShareStatusType] = None
    ShareMethod: Optional[ShareMethodType] = None
    ShareNotes: Optional[str] = None
    LaunchTime: Optional[datetime] = None
    StageLastUpdatedDateTime: Optional[datetime] = None
    Type: Optional[DirectoryTypeType] = None
    VpcSettings: Optional[DirectoryVpcSettingsDescriptionTypeDef] = None
    ConnectSettings: Optional[DirectoryConnectSettingsDescriptionTypeDef] = None
    RadiusSettings: Optional[RadiusSettingsOutputTypeDef] = None
    RadiusStatus: Optional[RadiusStatusType] = None
    StageReason: Optional[str] = None
    SsoEnabled: Optional[bool] = None
    DesiredNumberOfDomainControllers: Optional[int] = None
    OwnerDirectoryDescription: Optional[OwnerDirectoryDescriptionTypeDef] = None
    RegionsInfo: Optional[RegionsInfoTypeDef] = None
    OsVersion: Optional[OSVersionType] = None

class DescribeRegionsResultTypeDef(BaseValidatorModel):
    RegionsDescription: List[RegionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateInfoEntryTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    Status: Optional[UpdateStatusType] = None
    StatusReason: Optional[str] = None
    InitiatedBy: Optional[str] = None
    NewValue: Optional[UpdateValueTypeDef] = None
    PreviousValue: Optional[UpdateValueTypeDef] = None
    StartTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None

class DescribeDirectoriesResultTypeDef(BaseValidatorModel):
    DirectoryDescriptions: List[DirectoryDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeUpdateDirectoryResultTypeDef(BaseValidatorModel):
    UpdateActivities: List[UpdateInfoEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

