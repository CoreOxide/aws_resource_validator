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
from aws_resource_validator.pydantic_models.ds_constants import *

class AcceptSharedDirectoryRequestTypeDef(BaseValidatorModel):
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


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class AttributeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class CancelSchemaExtensionRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    SchemaExtensionId: str


class ClientCertAuthSettingsTypeDef(BaseValidatorModel):
    OCSPUrl: Optional[str] = None


class ConditionalForwarderTypeDef(BaseValidatorModel):
    RemoteDomainName: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    ReplicationScope: Optional[Literal["Domain"]] = None


class DirectoryConnectSettingsTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]
    CustomerDnsIps: Sequence[str]
    CustomerUserName: str


class CreateAliasRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Alias: str


class CreateConditionalForwarderRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]


class CreateLogSubscriptionRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    LogGroupName: str


class CreateSnapshotRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Name: Optional[str] = None


class CreateTrustRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    TrustPassword: str
    TrustDirection: TrustDirectionType
    TrustType: Optional[TrustTypeType] = None
    ConditionalForwarderIpAddrs: Optional[Sequence[str]] = None
    SelectiveAuth: Optional[SelectiveAuthType] = None


class DeleteConditionalForwarderRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str


class DeleteDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class DeleteLogSubscriptionRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class DeleteSnapshotRequestTypeDef(BaseValidatorModel):
    SnapshotId: str


class DeleteTrustRequestTypeDef(BaseValidatorModel):
    TrustId: str
    DeleteAssociatedConditionalForwarder: Optional[bool] = None


class DeregisterCertificateRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str


class DeregisterEventTopicRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    TopicName: str


class DescribeCertificateRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeConditionalForwardersRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainNames: Optional[Sequence[str]] = None


class DescribeDirectoriesRequestTypeDef(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeDirectoryDataAccessRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class DescribeDomainControllersRequestTypeDef(BaseValidatorModel):
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


class DescribeEventTopicsRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicNames: Optional[Sequence[str]] = None


class EventTopicTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicName: Optional[str] = None
    TopicArn: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    Status: Optional[TopicStatusType] = None


class LDAPSSettingInfoTypeDef(BaseValidatorModel):
    LDAPSStatus: Optional[LDAPSStatusType] = None
    LDAPSStatusReason: Optional[str] = None
    LastUpdatedDateTime: Optional[datetime] = None


class DescribeSettingsRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Status: Optional[DirectoryConfigurationStatusType] = None
    NextToken: Optional[str] = None


class DescribeSharedDirectoriesRequestTypeDef(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeSnapshotsRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeTrustsRequestTypeDef(BaseValidatorModel):
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


class DirectoryVpcSettingsOutputTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]


class DirectoryVpcSettingsTypeDef(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]


class DisableDirectoryDataAccessRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class DisableRadiusRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class DisableSsoRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None


class EnableDirectoryDataAccessRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class EnableSsoRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None


class GetSnapshotLimitsRequestTypeDef(BaseValidatorModel):
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


class ListCertificatesRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class ListIpRoutesRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class ListLogSubscriptionsRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class LogSubscriptionTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    LogGroupName: Optional[str] = None
    SubscriptionCreatedDateTime: Optional[datetime] = None


class ListSchemaExtensionsRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class OSUpdateSettingsTypeDef(BaseValidatorModel):
    OSVersion: Optional[OSVersionType] = None


class RadiusSettingsTypeDef(BaseValidatorModel):
    RadiusServers: Optional[Sequence[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None


class RegisterEventTopicRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    TopicName: str


class RejectSharedDirectoryRequestTypeDef(BaseValidatorModel):
    SharedDirectoryId: str


class RemoveIpRoutesRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CidrIps: Sequence[str]


class RemoveRegionRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class RemoveTagsFromResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]


class ResetUserPasswordRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    NewPassword: str


class RestoreFromSnapshotRequestTypeDef(BaseValidatorModel):
    SnapshotId: str


class SettingTypeDef(BaseValidatorModel):
    Name: str
    Value: str


class StartSchemaExtensionRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    CreateSnapshotBeforeSchemaExtension: bool
    LdifContent: str
    Description: str


class UpdateConditionalForwarderRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]


class UpdateNumberOfDomainControllersRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    DesiredNumber: int


class UpdateTrustRequestTypeDef(BaseValidatorModel):
    TrustId: str
    SelectiveAuth: Optional[SelectiveAuthType] = None


class VerifyTrustRequestTypeDef(BaseValidatorModel):
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


class DescribeDirectoryDataAccessResultTypeDef(BaseValidatorModel):
    DataAccessStatus: DataAccessStatusType
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


class AddIpRoutesRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    IpRoutes: Sequence[IpRouteTypeDef]
    UpdateSecurityGroupForDirectoryControllers: Optional[bool] = None


class AddTagsToResourceRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ComputerTypeDef(BaseValidatorModel):
    ComputerId: Optional[str] = None
    ComputerName: Optional[str] = None
    ComputerAttributes: Optional[List[AttributeTypeDef]] = None


class CreateComputerRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    ComputerName: str
    Password: str
    OrganizationalUnitDistinguishedName: Optional[str] = None
    ComputerAttributes: Optional[Sequence[AttributeTypeDef]] = None


class CertificateInfoTypeDef(BaseValidatorModel):
    pass


class ListCertificatesResultTypeDef(BaseValidatorModel):
    CertificatesInfo: List[CertificateInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ClientAuthenticationSettingInfoTypeDef(BaseValidatorModel):
    pass


class DescribeClientAuthenticationSettingsResultTypeDef(BaseValidatorModel):
    ClientAuthenticationSettingsInfo: List[ClientAuthenticationSettingInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeConditionalForwardersResultTypeDef(BaseValidatorModel):
    ConditionalForwarders: List[ConditionalForwarderTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ConnectDirectoryRequestTypeDef(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ConnectSettings: DirectoryConnectSettingsTypeDef
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeDirectoriesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDomainControllersRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    DomainControllerIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSharedDirectoriesRequestPaginateTypeDef(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeTrustsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCertificatesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIpRoutesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLogSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemaExtensionsRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
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


class SettingEntryTypeDef(BaseValidatorModel):
    pass


class DescribeSettingsResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    SettingEntries: List[SettingEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SnapshotTypeDef(BaseValidatorModel):
    pass


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


class UpdateDirectorySetupRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    OSUpdateSettings: Optional[OSUpdateSettingsTypeDef] = None
    CreateSnapshotBeforeUpdate: Optional[bool] = None


class UpdateValueTypeDef(BaseValidatorModel):
    OSUpdateSettings: Optional[OSUpdateSettingsTypeDef] = None


class UpdateSettingsRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    Settings: Sequence[SettingTypeDef]


class ShareTargetTypeDef(BaseValidatorModel):
    pass


class ShareDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    ShareTarget: ShareTargetTypeDef
    ShareMethod: ShareMethodType
    ShareNotes: Optional[str] = None


class UnshareTargetTypeDef(BaseValidatorModel):
    pass


class UnshareDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UnshareTarget: UnshareTargetTypeDef


class CreateComputerResultTypeDef(BaseValidatorModel):
    Computer: ComputerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CertificateTypeDef(BaseValidatorModel):
    pass


class DescribeCertificateResultTypeDef(BaseValidatorModel):
    Certificate: CertificateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RegionDescriptionTypeDef(BaseValidatorModel):
    pass


class DescribeRegionsResultTypeDef(BaseValidatorModel):
    RegionsDescription: List[RegionDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DirectoryVpcSettingsUnionTypeDef(BaseValidatorModel):
    pass


class CreateDirectoryRequestTypeDef(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    VpcSettings: Optional[DirectoryVpcSettingsUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateMicrosoftADRequestTypeDef(BaseValidatorModel):
    Name: str
    Password: str
    VpcSettings: DirectoryVpcSettingsUnionTypeDef
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Edition: Optional[DirectoryEditionType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class UpdateInfoEntryTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    Status: Optional[UpdateStatusType] = None
    StatusReason: Optional[str] = None
    InitiatedBy: Optional[str] = None
    NewValue: Optional[UpdateValueTypeDef] = None
    PreviousValue: Optional[UpdateValueTypeDef] = None
    StartTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None


class RadiusSettingsUnionTypeDef(BaseValidatorModel):
    pass


class EnableRadiusRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnionTypeDef


class UpdateRadiusRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnionTypeDef


class DirectoryDescriptionTypeDef(BaseValidatorModel):
    pass


class DescribeDirectoriesResultTypeDef(BaseValidatorModel):
    DirectoryDescriptions: List[DirectoryDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeUpdateDirectoryResultTypeDef(BaseValidatorModel):
    UpdateActivities: List[UpdateInfoEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


