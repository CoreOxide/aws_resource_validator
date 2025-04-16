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

class AcceptSharedDirectoryRequest(BaseValidatorModel):
    SharedDirectoryId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class SharedDirectory(BaseValidatorModel):
    OwnerAccountId: Optional[str] = None
    OwnerDirectoryId: Optional[str] = None
    ShareMethod: Optional[ShareMethodType] = None
    SharedAccountId: Optional[str] = None
    SharedDirectoryId: Optional[str] = None
    ShareStatus: Optional[ShareStatusType] = None
    ShareNotes: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None


class IpRoute(BaseValidatorModel):
    CidrIp: Optional[str] = None
    Description: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class Attribute(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class CancelSchemaExtensionRequest(BaseValidatorModel):
    DirectoryId: str
    SchemaExtensionId: str


class ClientCertAuthSettings(BaseValidatorModel):
    OCSPUrl: Optional[str] = None


class ConditionalForwarder(BaseValidatorModel):
    RemoteDomainName: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    ReplicationScope: Optional[Literal["Domain"]] = None


class DirectoryConnectSettings(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]
    CustomerDnsIps: Sequence[str]
    CustomerUserName: str


class CreateAliasRequest(BaseValidatorModel):
    DirectoryId: str
    Alias: str


class CreateConditionalForwarderRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]


class CreateLogSubscriptionRequest(BaseValidatorModel):
    DirectoryId: str
    LogGroupName: str


class CreateSnapshotRequest(BaseValidatorModel):
    DirectoryId: str
    Name: Optional[str] = None


class CreateTrustRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    TrustPassword: str
    TrustDirection: TrustDirectionType
    TrustType: Optional[TrustTypeType] = None
    ConditionalForwarderIpAddrs: Optional[Sequence[str]] = None
    SelectiveAuth: Optional[SelectiveAuthType] = None


class DeleteConditionalForwarderRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str


class DeleteDirectoryRequest(BaseValidatorModel):
    DirectoryId: str


class DeleteLogSubscriptionRequest(BaseValidatorModel):
    DirectoryId: str


class DeleteSnapshotRequest(BaseValidatorModel):
    SnapshotId: str


class DeleteTrustRequest(BaseValidatorModel):
    TrustId: str
    DeleteAssociatedConditionalForwarder: Optional[bool] = None


class DeregisterCertificateRequest(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str


class DeregisterEventTopicRequest(BaseValidatorModel):
    DirectoryId: str
    TopicName: str


class DescribeCertificateRequest(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeConditionalForwardersRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainNames: Optional[Sequence[str]] = None


class DescribeDirectoriesRequest(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeDirectoryDataAccessRequest(BaseValidatorModel):
    DirectoryId: str


class DescribeDomainControllersRequest(BaseValidatorModel):
    DirectoryId: str
    DomainControllerIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DomainController(BaseValidatorModel):
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


class DescribeEventTopicsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicNames: Optional[Sequence[str]] = None


class EventTopic(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicName: Optional[str] = None
    TopicArn: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    Status: Optional[TopicStatusType] = None


class LDAPSSettingInfo(BaseValidatorModel):
    LDAPSStatus: Optional[LDAPSStatusType] = None
    LDAPSStatusReason: Optional[str] = None
    LastUpdatedDateTime: Optional[datetime] = None


class DescribeSettingsRequest(BaseValidatorModel):
    DirectoryId: str
    Status: Optional[DirectoryConfigurationStatusType] = None
    NextToken: Optional[str] = None


class DescribeSharedDirectoriesRequest(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeSnapshotsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class DescribeTrustsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class Trust(BaseValidatorModel):
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


class DirectoryConnectSettingsDescription(BaseValidatorModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    CustomerUserName: Optional[str] = None
    SecurityGroupId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None
    ConnectIps: Optional[List[str]] = None


class DirectoryVpcSettingsDescription(BaseValidatorModel):
    VpcId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SecurityGroupId: Optional[str] = None
    AvailabilityZones: Optional[List[str]] = None


class RadiusSettingsOutput(BaseValidatorModel):
    RadiusServers: Optional[List[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None


class RegionsInfo(BaseValidatorModel):
    PrimaryRegion: Optional[str] = None
    AdditionalRegions: Optional[List[str]] = None


class DirectoryLimits(BaseValidatorModel):
    CloudOnlyDirectoriesLimit: Optional[int] = None
    CloudOnlyDirectoriesCurrentCount: Optional[int] = None
    CloudOnlyDirectoriesLimitReached: Optional[bool] = None
    CloudOnlyMicrosoftADLimit: Optional[int] = None
    CloudOnlyMicrosoftADCurrentCount: Optional[int] = None
    CloudOnlyMicrosoftADLimitReached: Optional[bool] = None
    ConnectedDirectoriesLimit: Optional[int] = None
    ConnectedDirectoriesCurrentCount: Optional[int] = None
    ConnectedDirectoriesLimitReached: Optional[bool] = None


class DirectoryVpcSettingsOutput(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]


class DirectoryVpcSettings(BaseValidatorModel):
    VpcId: str
    SubnetIds: Sequence[str]


class DisableDirectoryDataAccessRequest(BaseValidatorModel):
    DirectoryId: str


class DisableRadiusRequest(BaseValidatorModel):
    DirectoryId: str


class DisableSsoRequest(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None


class EnableDirectoryDataAccessRequest(BaseValidatorModel):
    DirectoryId: str


class EnableSsoRequest(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None


class GetSnapshotLimitsRequest(BaseValidatorModel):
    DirectoryId: str


class SnapshotLimits(BaseValidatorModel):
    ManualSnapshotsLimit: Optional[int] = None
    ManualSnapshotsCurrentCount: Optional[int] = None
    ManualSnapshotsLimitReached: Optional[bool] = None


class IpRouteInfo(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    CidrIp: Optional[str] = None
    IpRouteStatusMsg: Optional[IpRouteStatusMsgType] = None
    AddedDateTime: Optional[datetime] = None
    IpRouteStatusReason: Optional[str] = None
    Description: Optional[str] = None


class ListCertificatesRequest(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class ListIpRoutesRequest(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class ListLogSubscriptionsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class LogSubscription(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    LogGroupName: Optional[str] = None
    SubscriptionCreatedDateTime: Optional[datetime] = None


class ListSchemaExtensionsRequest(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class SchemaExtensionInfo(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SchemaExtensionId: Optional[str] = None
    Description: Optional[str] = None
    SchemaExtensionStatus: Optional[SchemaExtensionStatusType] = None
    SchemaExtensionStatusReason: Optional[str] = None
    StartDateTime: Optional[datetime] = None
    EndDateTime: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class OSUpdateSettings(BaseValidatorModel):
    OSVersion: Optional[OSVersionType] = None


class RadiusSettings(BaseValidatorModel):
    RadiusServers: Optional[Sequence[str]] = None
    RadiusPort: Optional[int] = None
    RadiusTimeout: Optional[int] = None
    RadiusRetries: Optional[int] = None
    SharedSecret: Optional[str] = None
    AuthenticationProtocol: Optional[RadiusAuthenticationProtocolType] = None
    DisplayLabel: Optional[str] = None
    UseSameUsername: Optional[bool] = None


class RegisterEventTopicRequest(BaseValidatorModel):
    DirectoryId: str
    TopicName: str


class RejectSharedDirectoryRequest(BaseValidatorModel):
    SharedDirectoryId: str


class RemoveIpRoutesRequest(BaseValidatorModel):
    DirectoryId: str
    CidrIps: Sequence[str]


class RemoveRegionRequest(BaseValidatorModel):
    DirectoryId: str


class RemoveTagsFromResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]


class ResetUserPasswordRequest(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    NewPassword: str


class RestoreFromSnapshotRequest(BaseValidatorModel):
    SnapshotId: str


class Setting(BaseValidatorModel):
    Name: str
    Value: str


class StartSchemaExtensionRequest(BaseValidatorModel):
    DirectoryId: str
    CreateSnapshotBeforeSchemaExtension: bool
    LdifContent: str
    Description: str


class UpdateConditionalForwarderRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: Sequence[str]


class UpdateNumberOfDomainControllersRequest(BaseValidatorModel):
    DirectoryId: str
    DesiredNumber: int


class UpdateTrustRequest(BaseValidatorModel):
    TrustId: str
    SelectiveAuth: Optional[SelectiveAuthType] = None


class VerifyTrustRequest(BaseValidatorModel):
    TrustId: str


class ConnectDirectoryResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


class CreateAliasResult(BaseValidatorModel):
    DirectoryId: str
    Alias: str
    ResponseMetadata: ResponseMetadata


class CreateDirectoryResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


class CreateMicrosoftADResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


class CreateSnapshotResult(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


class CreateTrustResult(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadata


class DeleteDirectoryResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


class DeleteSnapshotResult(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


class DeleteTrustResult(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadata


class DescribeDirectoryDataAccessResult(BaseValidatorModel):
    DataAccessStatus: DataAccessStatusType
    ResponseMetadata: ResponseMetadata


class RegisterCertificateResult(BaseValidatorModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadata


class RejectSharedDirectoryResult(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadata


class ShareDirectoryResult(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadata


class StartSchemaExtensionResult(BaseValidatorModel):
    SchemaExtensionId: str
    ResponseMetadata: ResponseMetadata


class UnshareDirectoryResult(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadata


class UpdateSettingsResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


class UpdateTrustResult(BaseValidatorModel):
    RequestId: str
    TrustId: str
    ResponseMetadata: ResponseMetadata


class VerifyTrustResult(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadata


class AcceptSharedDirectoryResult(BaseValidatorModel):
    SharedDirectory: SharedDirectory
    ResponseMetadata: ResponseMetadata


class DescribeSharedDirectoriesResult(BaseValidatorModel):
    SharedDirectories: List[SharedDirectory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AddIpRoutesRequest(BaseValidatorModel):
    DirectoryId: str
    IpRoutes: Sequence[IpRoute]
    UpdateSecurityGroupForDirectoryControllers: Optional[bool] = None


class AddTagsToResourceRequest(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[Tag]


class ListTagsForResourceResult(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Computer(BaseValidatorModel):
    ComputerId: Optional[str] = None
    ComputerName: Optional[str] = None
    ComputerAttributes: Optional[List[Attribute]] = None


class CreateComputerRequest(BaseValidatorModel):
    DirectoryId: str
    ComputerName: str
    Password: str
    OrganizationalUnitDistinguishedName: Optional[str] = None
    ComputerAttributes: Optional[Sequence[Attribute]] = None


class CertificateInfo(BaseValidatorModel):
    pass


class ListCertificatesResult(BaseValidatorModel):
    CertificatesInfo: List[CertificateInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClientAuthenticationSettingInfo(BaseValidatorModel):
    pass


class DescribeClientAuthenticationSettingsResult(BaseValidatorModel):
    ClientAuthenticationSettingsInfo: List[ClientAuthenticationSettingInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeConditionalForwardersResult(BaseValidatorModel):
    ConditionalForwarders: List[ConditionalForwarder]
    ResponseMetadata: ResponseMetadata


class ConnectDirectoryRequest(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ConnectSettings: DirectoryConnectSettings
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class DescribeDirectoriesRequestPaginate(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDomainControllersRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    DomainControllerIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSharedDirectoriesRequestPaginate(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotsRequestPaginate(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTrustsRequestPaginate(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCertificatesRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIpRoutesRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLogSubscriptionsRequestPaginate(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemaExtensionsRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDomainControllersResult(BaseValidatorModel):
    DomainControllers: List[DomainController]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEventTopicsResult(BaseValidatorModel):
    EventTopics: List[EventTopic]
    ResponseMetadata: ResponseMetadata


class DescribeLDAPSSettingsResult(BaseValidatorModel):
    LDAPSSettingsInfo: List[LDAPSSettingInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SettingEntry(BaseValidatorModel):
    pass


class DescribeSettingsResult(BaseValidatorModel):
    DirectoryId: str
    SettingEntries: List[SettingEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Snapshot(BaseValidatorModel):
    pass


class DescribeSnapshotsResult(BaseValidatorModel):
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeTrustsResult(BaseValidatorModel):
    Trusts: List[Trust]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class OwnerDirectoryDescription(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    AccountId: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    VpcSettings: Optional[DirectoryVpcSettingsDescription] = None
    RadiusSettings: Optional[RadiusSettingsOutput] = None
    RadiusStatus: Optional[RadiusStatusType] = None


class GetDirectoryLimitsResult(BaseValidatorModel):
    DirectoryLimits: DirectoryLimits
    ResponseMetadata: ResponseMetadata


class GetSnapshotLimitsResult(BaseValidatorModel):
    SnapshotLimits: SnapshotLimits
    ResponseMetadata: ResponseMetadata


class ListIpRoutesResult(BaseValidatorModel):
    IpRoutesInfo: List[IpRouteInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLogSubscriptionsResult(BaseValidatorModel):
    LogSubscriptions: List[LogSubscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSchemaExtensionsResult(BaseValidatorModel):
    SchemaExtensionsInfo: List[SchemaExtensionInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateDirectorySetupRequest(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal["OS"]
    OSUpdateSettings: Optional[OSUpdateSettings] = None
    CreateSnapshotBeforeUpdate: Optional[bool] = None


class UpdateValue(BaseValidatorModel):
    OSUpdateSettings: Optional[OSUpdateSettings] = None


class UpdateSettingsRequest(BaseValidatorModel):
    DirectoryId: str
    Settings: Sequence[Setting]


class ShareTarget(BaseValidatorModel):
    pass


class ShareDirectoryRequest(BaseValidatorModel):
    DirectoryId: str
    ShareTarget: ShareTarget
    ShareMethod: ShareMethodType
    ShareNotes: Optional[str] = None


class UnshareTarget(BaseValidatorModel):
    pass


class UnshareDirectoryRequest(BaseValidatorModel):
    DirectoryId: str
    UnshareTarget: UnshareTarget


class CreateComputerResult(BaseValidatorModel):
    Computer: Computer
    ResponseMetadata: ResponseMetadata


class Certificate(BaseValidatorModel):
    pass


class DescribeCertificateResult(BaseValidatorModel):
    Certificate: Certificate
    ResponseMetadata: ResponseMetadata


class RegionDescription(BaseValidatorModel):
    pass


class DescribeRegionsResult(BaseValidatorModel):
    RegionsDescription: List[RegionDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DirectoryVpcSettingsUnion(BaseValidatorModel):
    pass


class CreateDirectoryRequest(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    VpcSettings: Optional[DirectoryVpcSettingsUnion] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateMicrosoftADRequest(BaseValidatorModel):
    Name: str
    Password: str
    VpcSettings: DirectoryVpcSettingsUnion
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Edition: Optional[DirectoryEditionType] = None
    Tags: Optional[Sequence[Tag]] = None


class UpdateInfoEntry(BaseValidatorModel):
    Region: Optional[str] = None
    Status: Optional[UpdateStatusType] = None
    StatusReason: Optional[str] = None
    InitiatedBy: Optional[str] = None
    NewValue: Optional[UpdateValue] = None
    PreviousValue: Optional[UpdateValue] = None
    StartTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None


class RadiusSettingsUnion(BaseValidatorModel):
    pass


class EnableRadiusRequest(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnion


class UpdateRadiusRequest(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnion


class DirectoryDescription(BaseValidatorModel):
    pass


class DescribeDirectoriesResult(BaseValidatorModel):
    DirectoryDescriptions: List[DirectoryDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeUpdateDirectoryResult(BaseValidatorModel):
    UpdateActivities: List[UpdateInfoEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


