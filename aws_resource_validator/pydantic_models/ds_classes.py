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
from aws_resource_validator.pydantic_models.ds_constants import *

class AcceptSharedDirectoryRequestRequestTypeDef(BaseModel):
    SharedDirectoryId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class SharedDirectoryTypeDef(BaseModel):
    OwnerAccountId: Optional[str] = None
    OwnerDirectoryId: Optional[str] = None
    ShareMethod: Optional[ShareMethodType] = None
    SharedAccountId: Optional[str] = None
    SharedDirectoryId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None
    ShareNotes: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None

class IpRouteTypeDef(BaseModel):
    CidrIp: Optional[str] = None
    Description: Optional[str] = None

class DirectoryVpcSettingsTypeDef(BaseModel):
    VpcId: str
    SubnetIds: Sequence[str]

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class AttributeTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class CancelSchemaExtensionRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    SchemaExtensionId: str

class CertificateInfoTypeDef(BaseModel):
    CertificateId: Optional[str] = None
    CommonName: Optional[str] = None
    State: Optional[CertificateStateType] = None
    ExpiryDateTime: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None

class ClientCertAuthSettingsTypeDef(BaseModel):
    OCSPUrl: Optional[str] = None

class ClientAuthenticationSettingInfoTypeDef(BaseModel):
    Type: Optional[ClientAuthenticationTypeType] = None
    Status: Optional[ClientAuthenticationStatusType] = None
    LastUpdatedDateTime: Optional[datetime] = None

class ConditionalForwarderTypeDef(BaseModel):
    RemoteDomainName: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    ReplicationScope: Optional[Literal["Domain"]] = None

class DirectoryConnectSettingsTypeDef(BaseModel):
    VpcId: str
    SubnetIds: Sequence[str]
    CustomerDnsIps: Sequence[str]
    CustomerUserName: str

class CreateAliasRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Alias: str

class CreateConditionalForwarderRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]

class CreateLogSubscriptionRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    LogGroupName: str

class CreateSnapshotRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Name: Optional[str] = None

class CreateTrustRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RemoteDomainName: str
    TrustPassword: str
    TrustDirection: TrustDirectionType
    TrustType: Optional[TrustTypeType] = None
    ConditionalForwarderIpAddrs: Optional[Sequence[str]] = None
    SelectiveAuth: Optional[SelectiveAuthType] = None

class DeleteConditionalForwarderRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RemoteDomainName: str

class DeleteDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryId: str

class DeleteLogSubscriptionRequestRequestTypeDef(BaseModel):
    DirectoryId: str

class DeleteSnapshotRequestRequestTypeDef(BaseModel):
    SnapshotId: str

class DeleteTrustRequestRequestTypeDef(BaseModel):
    TrustId: str
    DeleteAssociatedConditionalForwarder: Optional[bool] = None

class DeregisterCertificateRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    CertificateId: str

class DeregisterEventTopicRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    TopicName: str

class DescribeCertificateRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    CertificateId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClientAuthenticationSettingsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Type: Optional[ClientAuthenticationTypeType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeConditionalForwardersRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RemoteDomainNames: Optional[Sequence[str]] = None

class DescribeDirectoriesRequestRequestTypeDef(BaseModel):
    DirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeDomainControllersRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    DomainControllerIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DomainControllerTypeDef(BaseModel):
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

class DescribeEventTopicsRequestRequestTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    TopicNames: Optional[Sequence[str]] = None

class EventTopicTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    TopicName: Optional[str] = None
    TopicArn: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    Status: Optional[TopicStatusType] = None

class DescribeLDAPSSettingsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Type: Optional[Literal["Client"]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class LDAPSSettingInfoTypeDef(BaseModel):
    LDAPSStatus: Optional[LDAPSStatusType] = None
    LDAPSStatusReason: Optional[str] = None
    LastUpdatedDateTime: Optional[datetime] = None

class DescribeRegionsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RegionName: Optional[str] = None
    NextToken: Optional[str] = None

class DescribeSettingsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Status: Optional[DirectoryConfigurationStatusType] = None
    NextToken: Optional[str] = None

class SettingEntryTypeDef(BaseModel):
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

class DescribeSharedDirectoriesRequestRequestTypeDef(BaseModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class DescribeSnapshotsRequestRequestTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class SnapshotTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    SnapshotId: Optional[str] = None
    Type: Optional[SnapshotTypeType] = None
    Name: Optional[str] = None
    Status: Optional[SnapshotStatusType] = None
    StartTime: Optional[datetime] = None

class DescribeTrustsRequestRequestTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class TrustTypeDef(BaseModel):
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

class DescribeUpdateDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    RegionName: Optional[str] = None
    NextToken: Optional[str] = None

class DirectoryConnectSettingsDescriptionTypeDef(BaseModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    CustomerUserName: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    ConnectIps: Optional[List[str]] = None

class DirectoryVpcSettingsDescriptionTypeDef(BaseModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None

class RadiusSettingsOutputTypeDef(BaseModel):
    RadiusServers: Optional[List[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None

class RegionsInfoTypeDef(BaseModel):
    PrimaryRegion: Optional[str] = None
    AdditionalRegions: Optional[List[str]] = None

class DirectoryLimitsTypeDef(BaseModel):
    CloudOnlyDirectoriesLimit: Optional[int] = None
    CloudOnlyDirectoriesCurrentCount: Optional[int] = None
    CloudOnlyDirectoriesLimitReached: Optional[bool] = None
    CloudOnlyMicrosoftADLimit: Optional[int] = None
    CloudOnlyMicrosoftADCurrentCount: Optional[int] = None
    CloudOnlyMicrosoftADLimitReached: Optional[bool] = None
    ConnectedDirectoriesLimit: Optional[int] = None
    ConnectedDirectoriesCurrentCount: Optional[int] = None
    ConnectedDirectoriesLimitReached: Optional[bool] = None

class DirectoryVpcSettingsExtraOutputTypeDef(BaseModel):
    VpcId: str
    SubnetIds: List[str]

class DirectoryVpcSettingsOutputTypeDef(BaseModel):
    VpcId: str
    SubnetIds: List[str]

class DisableClientAuthenticationRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Type: ClientAuthenticationTypeType

class DisableLDAPSRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Type: Literal["Client"]

class DisableRadiusRequestRequestTypeDef(BaseModel):
    DirectoryId: str

class DisableSsoRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None

class EnableClientAuthenticationRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Type: ClientAuthenticationTypeType

class EnableLDAPSRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Type: Literal["Client"]

class RadiusSettingsTypeDef(BaseModel):
    RadiusServers: Optional[Sequence[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None

class EnableSsoRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None

class GetSnapshotLimitsRequestRequestTypeDef(BaseModel):
    DirectoryId: str

class SnapshotLimitsTypeDef(BaseModel):
    ManualSnapshotsLimit: Optional[int] = None
    ManualSnapshotsCurrentCount: Optional[int] = None
    ManualSnapshotsLimitReached: Optional[bool] = None

class IpRouteInfoTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    CidrIp: Optional[str] = None
    IpRouteStatusMsg: Optional[IpRouteStatusMsgType] = None
    AddedDateTime: Optional[datetime] = None
    IpRouteStatusReason: Optional[str] = None
    Description: Optional[str] = None

class ListCertificatesRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListIpRoutesRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class ListLogSubscriptionsRequestRequestTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class LogSubscriptionTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    LogGroupName: Optional[str] = None
    SubscriptionCreatedDateTime: Optional[datetime] = None

class ListSchemaExtensionsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class SchemaExtensionInfoTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    SchemaExtensionId: Optional[str] = None
    Description: Optional[str] = None
    SchemaExtensionStatus: Optional[SchemaExtensionStatusType] = None
    SchemaExtensionStatusReason: Optional[str] = None
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None

class OSUpdateSettingsTypeDef(BaseModel):
    OSVersion: Optional[OSVersionType] = None

class RadiusSettingsExtraOutputTypeDef(BaseModel):
    RadiusServers: Optional[List[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None

class RegisterEventTopicRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    TopicName: str

class RejectSharedDirectoryRequestRequestTypeDef(BaseModel):
    SharedDirectoryId: str

class RemoveIpRoutesRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    CidrIps: Sequence[str]

class RemoveRegionRequestRequestTypeDef(BaseModel):
    DirectoryId: str

class RemoveTagsFromResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagKeys: Sequence[str]

class ResetUserPasswordRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    UserName: str
    NewPassword: str

class RestoreFromSnapshotRequestRequestTypeDef(BaseModel):
    SnapshotId: str

class SettingTypeDef(BaseModel):
    Name: str
    Value: str

class ShareTargetTypeDef(BaseModel):
    Id: str
    Type: Literal["ACCOUNT"]

class StartSchemaExtensionRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    CreateSnapshotBeforeSchemaExtension: bool
    LdifContent: str
    Description: str

class UnshareTargetTypeDef(BaseModel):
    Id: str
    Type: Literal["ACCOUNT"]

class UpdateConditionalForwarderRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]

class UpdateNumberOfDomainControllersRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    DesiredNumber: int

class UpdateTrustRequestRequestTypeDef(BaseModel):
    TrustId: str
    SelectiveAuth: Optional[SelectiveAuthType] = None

class VerifyTrustRequestRequestTypeDef(BaseModel):
    TrustId: str

class ConnectDirectoryResultTypeDef(BaseModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAliasResultTypeDef(BaseModel):
    DirectoryId: str
    Alias: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDirectoryResultTypeDef(BaseModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMicrosoftADResultTypeDef(BaseModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResultTypeDef(BaseModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrustResultTypeDef(BaseModel):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDirectoryResultTypeDef(BaseModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResultTypeDef(BaseModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTrustResultTypeDef(BaseModel):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterCertificateResultTypeDef(BaseModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RejectSharedDirectoryResultTypeDef(BaseModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ShareDirectoryResultTypeDef(BaseModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartSchemaExtensionResultTypeDef(BaseModel):
    SchemaExtensionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UnshareDirectoryResultTypeDef(BaseModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSettingsResultTypeDef(BaseModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrustResultTypeDef(BaseModel):
    RequestId: str
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class VerifyTrustResultTypeDef(BaseModel):
    TrustId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AcceptSharedDirectoryResultTypeDef(BaseModel):
    SharedDirectory: SharedDirectoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSharedDirectoriesResultTypeDef(BaseModel):
    SharedDirectories: List[SharedDirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AddIpRoutesRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    IpRoutes: Sequence[IpRouteTypeDef]
    UpdateSecurityGroupForDirectoryControllers: Optional[bool] = None

class AddRegionRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RegionName: str
    VPCSettings: DirectoryVpcSettingsTypeDef

class AddTagsToResourceRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateDirectoryRequestRequestTypeDef(BaseModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    VpcSettings: Optional[DirectoryVpcSettingsTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateMicrosoftADRequestRequestTypeDef(BaseModel):
    Name: str
    Password: str
    VpcSettings: DirectoryVpcSettingsTypeDef
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Edition: Optional[DirectoryEditionType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResultTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ComputerTypeDef(BaseModel):
    ComputerId: Optional[str] = None
    ComputerName: Optional[str] = None
    ComputerAttributes: Optional[List[AttributeTypeDef]] = None

class CreateComputerRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    ComputerName: str
    Password: str
    OrganizationalUnitDistinguishedName: Optional[str] = None
    ComputerAttributes: Optional[Sequence[AttributeTypeDef]] = None

class ListCertificatesResultTypeDef(BaseModel):
    CertificatesInfo: List[CertificateInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CertificateTypeDef(BaseModel):
    CertificateId: Optional[str] = None
    State: Optional[CertificateStateType] = None
    StateReason: Optional[str] = None
    CommonName: Optional[str] = None
    RegisteredDateTime: Optional[datetime] = None
    ExpiryDateTime: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None
    ClientCertAuthSettings: Optional[ClientCertAuthSettingsTypeDef] = None

class RegisterCertificateRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    CertificateData: str
    Type: Optional[CertificateTypeType] = None
    ClientCertAuthSettings: Optional[ClientCertAuthSettingsTypeDef] = None

class DescribeClientAuthenticationSettingsResultTypeDef(BaseModel):
    ClientAuthenticationSettingsInfo: List[ClientAuthenticationSettingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeConditionalForwardersResultTypeDef(BaseModel):
    ConditionalForwarders: List[ConditionalForwarderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConnectDirectoryRequestRequestTypeDef(BaseModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ConnectSettings: DirectoryConnectSettingsTypeDef
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeClientAuthenticationSettingsRequestDescribeClientAuthenticationSettingsPaginateTypeDef(BaseModel):
    DirectoryId: str
    Type: Optional[ClientAuthenticationTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDirectoriesRequestDescribeDirectoriesPaginateTypeDef(BaseModel):
    DirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDomainControllersRequestDescribeDomainControllersPaginateTypeDef(BaseModel):
    DirectoryId: str
    DomainControllerIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLDAPSSettingsRequestDescribeLDAPSSettingsPaginateTypeDef(BaseModel):
    DirectoryId: str
    Type: Optional[Literal["Client"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegionsRequestDescribeRegionsPaginateTypeDef(BaseModel):
    DirectoryId: str
    RegionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSharedDirectoriesRequestDescribeSharedDirectoriesPaginateTypeDef(BaseModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeTrustsRequestDescribeTrustsPaginateTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUpdateDirectoryRequestDescribeUpdateDirectoryPaginateTypeDef(BaseModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    RegionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCertificatesRequestListCertificatesPaginateTypeDef(BaseModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIpRoutesRequestListIpRoutesPaginateTypeDef(BaseModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLogSubscriptionsRequestListLogSubscriptionsPaginateTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaExtensionsRequestListSchemaExtensionsPaginateTypeDef(BaseModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDomainControllersResultTypeDef(BaseModel):
    DomainControllers: List[DomainControllerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEventTopicsResultTypeDef(BaseModel):
    EventTopics: List[EventTopicTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLDAPSSettingsResultTypeDef(BaseModel):
    LDAPSSettingsInfo: List[LDAPSSettingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSettingsResultTypeDef(BaseModel):
    DirectoryId: str
    SettingEntries: List[SettingEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSnapshotsResultTypeDef(BaseModel):
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeTrustsResultTypeDef(BaseModel):
    Trusts: List[TrustTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class OwnerDirectoryDescriptionTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    AccountId: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    VpcSettings: Optional[DirectoryVpcSettingsDescriptionTypeDef] = None
    RadiusSettings: Optional[RadiusSettingsOutputTypeDef] = None
    RadiusStatus: Optional[RadiusStatusType] = None

class GetDirectoryLimitsResultTypeDef(BaseModel):
    DirectoryLimits: DirectoryLimitsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegionDescriptionTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    RegionName: Optional[str] = None
    RegionType: Optional[RegionTypeType] = None
    Status: Optional[DirectoryStageType] = None
    VpcSettings: Optional[DirectoryVpcSettingsOutputTypeDef] = None
    DesiredNumberOfDomainControllers: Optional[int] = None
    LaunchTime: Optional[datetime] = None
    StatusLastUpdatedDateTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None

class EnableRadiusRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsTypeDef

class UpdateRadiusRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsTypeDef

class GetSnapshotLimitsResultTypeDef(BaseModel):
    SnapshotLimits: SnapshotLimitsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIpRoutesResultTypeDef(BaseModel):
    IpRoutesInfo: List[IpRouteInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListLogSubscriptionsResultTypeDef(BaseModel):
    LogSubscriptions: List[LogSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSchemaExtensionsResultTypeDef(BaseModel):
    SchemaExtensionsInfo: List[SchemaExtensionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateDirectorySetupRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    OSUpdateSettings: Optional[OSUpdateSettingsTypeDef] = None
    CreateSnapshotBeforeUpdate: Optional[bool] = None

class UpdateValueTypeDef(BaseModel):
    OSUpdateSettings: Optional[OSUpdateSettingsTypeDef] = None

class UpdateSettingsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    Settings: Sequence[SettingTypeDef]

class ShareDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    ShareTarget: ShareTargetTypeDef
    ShareMethod: ShareMethodType
    ShareNotes: Optional[str] = None

class UnshareDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    UnshareTarget: UnshareTargetTypeDef

class CreateComputerResultTypeDef(BaseModel):
    Computer: ComputerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCertificateResultTypeDef(BaseModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DirectoryDescriptionTypeDef(BaseModel):
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

class DescribeRegionsResultTypeDef(BaseModel):
    RegionsDescription: List[RegionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateInfoEntryTypeDef(BaseModel):
    Region: Optional[str] = None
    Status: Optional[UpdateStatusType] = None
    StatusReason: Optional[str] = None
    InitiatedBy: Optional[str] = None
    NewValue: Optional[UpdateValueTypeDef] = None
    PreviousValue: Optional[UpdateValueTypeDef] = None
    StartTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None

class DescribeDirectoriesResultTypeDef(BaseModel):
    DirectoryDescriptions: List[DirectoryDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeUpdateDirectoryResultTypeDef(BaseModel):
    UpdateActivities: List[UpdateInfoEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

