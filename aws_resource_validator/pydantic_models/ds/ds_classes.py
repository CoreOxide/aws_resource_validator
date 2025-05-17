from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ds.ds_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_shared_directory' function.
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


class CertificateInfo(BaseValidatorModel):
    CertificateId: Optional[str] = None
    CommonName: Optional[str] = None
    State: Optional[CertificateStateType] = None
    ExpiryDateTime: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None


class ClientCertAuthSettings(BaseValidatorModel):
    OCSPUrl: Optional[str] = None


class ClientAuthenticationSettingInfo(BaseValidatorModel):
    Type: Optional[ClientAuthenticationTypeType] = None
    Status: Optional[ClientAuthenticationStatusType] = None
    LastUpdatedDateTime: Optional[datetime] = None


class ConditionalForwarder(BaseValidatorModel):
    RemoteDomainName: Optional[str] = None
    DnsIpAddrs: Optional[List[str]] = None
    ReplicationScope: Optional[Literal['Domain']] = None


class DirectoryConnectSettings(BaseValidatorModel):
    VpcId: str
    SubnetIds: List[str]
    CustomerDnsIps: List[str]
    CustomerUserName: str


# This class is the input for the 'create_alias' function.
class CreateAliasRequest(BaseValidatorModel):
    DirectoryId: str
    Alias: str


class CreateConditionalForwarderRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: List[str]


class CreateLogSubscriptionRequest(BaseValidatorModel):
    DirectoryId: str
    LogGroupName: str


# This class is the input for the 'create_snapshot' function.
class CreateSnapshotRequest(BaseValidatorModel):
    DirectoryId: str
    Name: Optional[str] = None


# This class is the input for the 'create_trust' function.
class CreateTrustRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    TrustPassword: str
    TrustDirection: TrustDirectionType
    TrustType: Optional[TrustTypeType] = None
    ConditionalForwarderIpAddrs: Optional[List[str]] = None
    SelectiveAuth: Optional[SelectiveAuthType] = None


class DeleteConditionalForwarderRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str


# This class is the input for the 'delete_directory' function.
class DeleteDirectoryRequest(BaseValidatorModel):
    DirectoryId: str


class DeleteLogSubscriptionRequest(BaseValidatorModel):
    DirectoryId: str


# This class is the input for the 'delete_snapshot' function.
class DeleteSnapshotRequest(BaseValidatorModel):
    SnapshotId: str


# This class is the input for the 'delete_trust' function.
class DeleteTrustRequest(BaseValidatorModel):
    TrustId: str
    DeleteAssociatedConditionalForwarder: Optional[bool] = None


class DeregisterCertificateRequest(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str


class DeregisterEventTopicRequest(BaseValidatorModel):
    DirectoryId: str
    TopicName: str


# This class is the input for the 'describe_certificate' function.
class DescribeCertificateRequest(BaseValidatorModel):
    DirectoryId: str
    CertificateId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_client_authentication_settings' function.
class DescribeClientAuthenticationSettingsRequest(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[ClientAuthenticationTypeType] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_conditional_forwarders' function.
class DescribeConditionalForwardersRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainNames: Optional[List[str]] = None


# This class is the input for the 'describe_directories' function.
class DescribeDirectoriesRequest(BaseValidatorModel):
    DirectoryIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_directory_data_access' function.
class DescribeDirectoryDataAccessRequest(BaseValidatorModel):
    DirectoryId: str


# This class is the input for the 'describe_domain_controllers' function.
class DescribeDomainControllersRequest(BaseValidatorModel):
    DirectoryId: str
    DomainControllerIds: Optional[List[str]] = None
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


# This class is the input for the 'describe_event_topics' function.
class DescribeEventTopicsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicNames: Optional[List[str]] = None


class EventTopic(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TopicName: Optional[str] = None
    TopicArn: Optional[str] = None
    CreatedDateTime: Optional[datetime] = None
    Status: Optional[TopicStatusType] = None


# This class is the input for the 'describe_ldaps_settings' function.
class DescribeLDAPSSettingsRequest(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[Literal['Client']] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class LDAPSSettingInfo(BaseValidatorModel):
    LDAPSStatus: Optional[LDAPSStatusType] = None
    LDAPSStatusReason: Optional[str] = None
    LastUpdatedDateTime: Optional[datetime] = None


# This class is the input for the 'describe_regions' function.
class DescribeRegionsRequest(BaseValidatorModel):
    DirectoryId: str
    RegionName: Optional[str] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_settings' function.
class DescribeSettingsRequest(BaseValidatorModel):
    DirectoryId: str
    Status: Optional[DirectoryConfigurationStatusType] = None
    NextToken: Optional[str] = None


class SettingEntry(BaseValidatorModel):
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


# This class is the input for the 'describe_shared_directories' function.
class DescribeSharedDirectoriesRequest(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'describe_snapshots' function.
class DescribeSnapshotsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class Snapshot(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotId: Optional[str] = None
    Type: Optional[SnapshotTypeType] = None
    Name: Optional[str] = None
    Status: Optional[SnapshotStatusType] = None
    StartTime: Optional[datetime] = None


# This class is the input for the 'describe_trusts' function.
class DescribeTrustsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[List[str]] = None
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


# This class is the input for the 'describe_update_directory' function.
class DescribeUpdateDirectoryRequest(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal['OS']
    RegionName: Optional[str] = None
    NextToken: Optional[str] = None


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
    SubnetIds: List[str]


class DisableClientAuthenticationRequest(BaseValidatorModel):
    DirectoryId: str
    Type: ClientAuthenticationTypeType


class DisableDirectoryDataAccessRequest(BaseValidatorModel):
    DirectoryId: str


class DisableLDAPSRequest(BaseValidatorModel):
    DirectoryId: str
    Type: Literal['Client']


class DisableRadiusRequest(BaseValidatorModel):
    DirectoryId: str


class DisableSsoRequest(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None


class EnableClientAuthenticationRequest(BaseValidatorModel):
    DirectoryId: str
    Type: ClientAuthenticationTypeType


class EnableDirectoryDataAccessRequest(BaseValidatorModel):
    DirectoryId: str


class EnableLDAPSRequest(BaseValidatorModel):
    DirectoryId: str
    Type: Literal['Client']


class EnableSsoRequest(BaseValidatorModel):
    DirectoryId: str
    UserName: Optional[str] = None
    Password: Optional[str] = None


# This class is the input for the 'get_snapshot_limits' function.
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


# This class is the input for the 'list_certificates' function.
class ListCertificatesRequest(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_ip_routes' function.
class ListIpRoutesRequest(BaseValidatorModel):
    DirectoryId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_log_subscriptions' function.
class ListLogSubscriptionsRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class LogSubscription(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    LogGroupName: Optional[str] = None
    SubscriptionCreatedDateTime: Optional[datetime] = None


# This class is the input for the 'list_schema_extensions' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    Limit: Optional[int] = None


class OSUpdateSettings(BaseValidatorModel):
    OSVersion: Optional[OSVersionType] = None


class RadiusSettings(BaseValidatorModel):
    RadiusServers: Optional[List[str]] = None
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


# This class is the input for the 'reject_shared_directory' function.
class RejectSharedDirectoryRequest(BaseValidatorModel):
    SharedDirectoryId: str


class RemoveIpRoutesRequest(BaseValidatorModel):
    DirectoryId: str
    CidrIps: List[str]


class RemoveRegionRequest(BaseValidatorModel):
    DirectoryId: str


class RemoveTagsFromResourceRequest(BaseValidatorModel):
    ResourceId: str
    TagKeys: List[str]


class ResetUserPasswordRequest(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    NewPassword: str


class RestoreFromSnapshotRequest(BaseValidatorModel):
    SnapshotId: str


class Setting(BaseValidatorModel):
    Name: str
    Value: str


class ShareTarget(BaseValidatorModel):
    Id: str
    Type: Literal['ACCOUNT']


# This class is the input for the 'start_schema_extension' function.
class StartSchemaExtensionRequest(BaseValidatorModel):
    DirectoryId: str
    CreateSnapshotBeforeSchemaExtension: bool
    LdifContent: str
    Description: str


class UnshareTarget(BaseValidatorModel):
    Id: str
    Type: Literal['ACCOUNT']


class UpdateConditionalForwarderRequest(BaseValidatorModel):
    DirectoryId: str
    RemoteDomainName: str
    DnsIpAddrs: List[str]


class UpdateNumberOfDomainControllersRequest(BaseValidatorModel):
    DirectoryId: str
    DesiredNumber: int


# This class is the input for the 'update_trust' function.
class UpdateTrustRequest(BaseValidatorModel):
    TrustId: str
    SelectiveAuth: Optional[SelectiveAuthType] = None


# This class is the input for the 'verify_trust' function.
class VerifyTrustRequest(BaseValidatorModel):
    TrustId: str


# This class is the output for the 'connect_directory' function.
class ConnectDirectoryResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_alias' function.
class CreateAliasResult(BaseValidatorModel):
    DirectoryId: str
    Alias: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_directory' function.
class CreateDirectoryResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_microsoft_ad' function.
class CreateMicrosoftADResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_snapshot' function.
class CreateSnapshotResult(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_trust' function.
class CreateTrustResult(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_directory' function.
class DeleteDirectoryResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_snapshot' function.
class DeleteSnapshotResult(BaseValidatorModel):
    SnapshotId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_trust' function.
class DeleteTrustResult(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_directory_data_access' function.
class DescribeDirectoryDataAccessResult(BaseValidatorModel):
    DataAccessStatus: DataAccessStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_certificate' function.
class RegisterCertificateResult(BaseValidatorModel):
    CertificateId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_shared_directory' function.
class RejectSharedDirectoryResult(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'share_directory' function.
class ShareDirectoryResult(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_schema_extension' function.
class StartSchemaExtensionResult(BaseValidatorModel):
    SchemaExtensionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unshare_directory' function.
class UnshareDirectoryResult(BaseValidatorModel):
    SharedDirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_settings' function.
class UpdateSettingsResult(BaseValidatorModel):
    DirectoryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_trust' function.
class UpdateTrustResult(BaseValidatorModel):
    RequestId: str
    TrustId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'verify_trust' function.
class VerifyTrustResult(BaseValidatorModel):
    TrustId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'accept_shared_directory' function.
class AcceptSharedDirectoryResult(BaseValidatorModel):
    SharedDirectory: SharedDirectory
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_shared_directories' function.
class DescribeSharedDirectoriesResult(BaseValidatorModel):
    SharedDirectories: List[SharedDirectory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AddIpRoutesRequest(BaseValidatorModel):
    DirectoryId: str
    IpRoutes: List[IpRoute]
    UpdateSecurityGroupForDirectoryControllers: Optional[bool] = None


class AddTagsToResourceRequest(BaseValidatorModel):
    ResourceId: str
    Tags: List[Tag]


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResult(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Computer(BaseValidatorModel):
    ComputerId: Optional[str] = None
    ComputerName: Optional[str] = None
    ComputerAttributes: Optional[List[Attribute]] = None


# This class is the input for the 'create_computer' function.
class CreateComputerRequest(BaseValidatorModel):
    DirectoryId: str
    ComputerName: str
    Password: str
    OrganizationalUnitDistinguishedName: Optional[str] = None
    ComputerAttributes: Optional[List[Attribute]] = None


# This class is the output for the 'list_certificates' function.
class ListCertificatesResult(BaseValidatorModel):
    CertificatesInfo: List[CertificateInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Certificate(BaseValidatorModel):
    CertificateId: Optional[str] = None
    State: Optional[CertificateStateType] = None
    StateReason: Optional[str] = None
    CommonName: Optional[str] = None
    RegisteredDateTime: Optional[datetime] = None
    ExpiryDateTime: Optional[datetime] = None
    Type: Optional[CertificateTypeType] = None
    ClientCertAuthSettings: Optional[ClientCertAuthSettings] = None


# This class is the input for the 'register_certificate' function.
class RegisterCertificateRequest(BaseValidatorModel):
    DirectoryId: str
    CertificateData: str
    Type: Optional[CertificateTypeType] = None
    ClientCertAuthSettings: Optional[ClientCertAuthSettings] = None


# This class is the output for the 'describe_client_authentication_settings' function.
class DescribeClientAuthenticationSettingsResult(BaseValidatorModel):
    ClientAuthenticationSettingsInfo: List[ClientAuthenticationSettingInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_conditional_forwarders' function.
class DescribeConditionalForwardersResult(BaseValidatorModel):
    ConditionalForwarders: List[ConditionalForwarder]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'connect_directory' function.
class ConnectDirectoryRequest(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ConnectSettings: DirectoryConnectSettings
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


class DescribeClientAuthenticationSettingsRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[ClientAuthenticationTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDirectoriesRequestPaginate(BaseValidatorModel):
    DirectoryIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDomainControllersRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    DomainControllerIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLDAPSSettingsRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    Type: Optional[Literal['Client']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegionsRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    RegionName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSharedDirectoriesRequestPaginate(BaseValidatorModel):
    OwnerDirectoryId: str
    SharedDirectoryIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotsRequestPaginate(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SnapshotIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeTrustsRequestPaginate(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    TrustIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUpdateDirectoryRequestPaginate(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal['OS']
    RegionName: Optional[str] = None
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


# This class is the output for the 'describe_domain_controllers' function.
class DescribeDomainControllersResult(BaseValidatorModel):
    DomainControllers: List[DomainController]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_event_topics' function.
class DescribeEventTopicsResult(BaseValidatorModel):
    EventTopics: List[EventTopic]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_ldaps_settings' function.
class DescribeLDAPSSettingsResult(BaseValidatorModel):
    LDAPSSettingsInfo: List[LDAPSSettingInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_settings' function.
class DescribeSettingsResult(BaseValidatorModel):
    DirectoryId: str
    SettingEntries: List[SettingEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_snapshots' function.
class DescribeSnapshotsResult(BaseValidatorModel):
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_trusts' function.
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


class RegionDescription(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    RegionName: Optional[str] = None
    RegionType: Optional[RegionTypeType] = None
    Status: Optional[DirectoryStageType] = None
    VpcSettings: Optional[DirectoryVpcSettingsOutput] = None
    DesiredNumberOfDomainControllers: Optional[int] = None
    LaunchTime: Optional[datetime] = None
    StatusLastUpdatedDateTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None

DirectoryVpcSettingsUnion = Union[DirectoryVpcSettings, DirectoryVpcSettingsOutput]


# This class is the output for the 'get_snapshot_limits' function.
class GetSnapshotLimitsResult(BaseValidatorModel):
    SnapshotLimits: SnapshotLimits
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_ip_routes' function.
class ListIpRoutesResult(BaseValidatorModel):
    IpRoutesInfo: List[IpRouteInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_log_subscriptions' function.
class ListLogSubscriptionsResult(BaseValidatorModel):
    LogSubscriptions: List[LogSubscription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_schema_extensions' function.
class ListSchemaExtensionsResult(BaseValidatorModel):
    SchemaExtensionsInfo: List[SchemaExtensionInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateDirectorySetupRequest(BaseValidatorModel):
    DirectoryId: str
    UpdateType: Literal['OS']
    OSUpdateSettings: Optional[OSUpdateSettings] = None
    CreateSnapshotBeforeUpdate: Optional[bool] = None


class UpdateValue(BaseValidatorModel):
    OSUpdateSettings: Optional[OSUpdateSettings] = None

RadiusSettingsUnion = Union[RadiusSettings, RadiusSettingsOutput]


# This class is the input for the 'update_settings' function.
class UpdateSettingsRequest(BaseValidatorModel):
    DirectoryId: str
    Settings: List[Setting]


# This class is the input for the 'share_directory' function.
class ShareDirectoryRequest(BaseValidatorModel):
    DirectoryId: str
    ShareTarget: ShareTarget
    ShareMethod: ShareMethodType
    ShareNotes: Optional[str] = None


# This class is the input for the 'unshare_directory' function.
class UnshareDirectoryRequest(BaseValidatorModel):
    DirectoryId: str
    UnshareTarget: UnshareTarget


# This class is the output for the 'create_computer' function.
class CreateComputerResult(BaseValidatorModel):
    Computer: Computer
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_certificate' function.
class DescribeCertificateResult(BaseValidatorModel):
    Certificate: Certificate
    ResponseMetadata: ResponseMetadata


class DirectoryDescription(BaseValidatorModel):
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
    VpcSettings: Optional[DirectoryVpcSettingsDescription] = None
    ConnectSettings: Optional[DirectoryConnectSettingsDescription] = None
    RadiusSettings: Optional[RadiusSettingsOutput] = None
    RadiusStatus: Optional[RadiusStatusType] = None
    StageReason: Optional[str] = None
    SsoEnabled: Optional[bool] = None
    DesiredNumberOfDomainControllers: Optional[int] = None
    OwnerDirectoryDescription: Optional[OwnerDirectoryDescription] = None
    RegionsInfo: Optional[RegionsInfo] = None
    OsVersion: Optional[OSVersionType] = None


# This class is the output for the 'describe_regions' function.
class DescribeRegionsResult(BaseValidatorModel):
    RegionsDescription: List[RegionDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AddRegionRequest(BaseValidatorModel):
    DirectoryId: str
    RegionName: str
    VPCSettings: DirectoryVpcSettingsUnion


# This class is the input for the 'create_directory' function.
class CreateDirectoryRequest(BaseValidatorModel):
    Name: str
    Password: str
    Size: DirectorySizeType
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    VpcSettings: Optional[DirectoryVpcSettingsUnion] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_microsoft_ad' function.
class CreateMicrosoftADRequest(BaseValidatorModel):
    Name: str
    Password: str
    VpcSettings: DirectoryVpcSettingsUnion
    ShortName: Optional[str] = None
    Description: Optional[str] = None
    Edition: Optional[DirectoryEditionType] = None
    Tags: Optional[List[Tag]] = None


class UpdateInfoEntry(BaseValidatorModel):
    Region: Optional[str] = None
    Status: Optional[UpdateStatusType] = None
    StatusReason: Optional[str] = None
    InitiatedBy: Optional[str] = None
    NewValue: Optional[UpdateValue] = None
    PreviousValue: Optional[UpdateValue] = None
    StartTime: Optional[datetime] = None
    LastUpdatedDateTime: Optional[datetime] = None


class EnableRadiusRequest(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnion


class UpdateRadiusRequest(BaseValidatorModel):
    DirectoryId: str
    RadiusSettings: RadiusSettingsUnion


# This class is the output for the 'describe_directories' function.
class DescribeDirectoriesResult(BaseValidatorModel):
    DirectoryDescriptions: List[DirectoryDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_update_directory' function.
class DescribeUpdateDirectoryResult(BaseValidatorModel):
    UpdateActivities: List[UpdateInfoEntry]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None