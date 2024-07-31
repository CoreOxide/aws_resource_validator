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
from aws_resource_validator.pydantic_models.workspaces_constants import *

class AcceptAccountLinkInvitationRequestRequestTypeDef(BaseModel):
    LinkId: str
    ClientToken: Optional[str] = None

class AccountLinkTypeDef(BaseModel):
    AccountLinkId: Optional[str] = None
    AccountLinkStatus: Optional[AccountLinkStatusEnumType] = None
    SourceAccountId: Optional[str] = None
    TargetAccountId: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AccountModificationTypeDef(BaseModel):
    ModificationState: Optional[DedicatedTenancyModificationStateEnumType] = None
    DedicatedTenancySupport: Optional[DedicatedTenancySupportResultEnumType] = None
    DedicatedTenancyManagementCidrRange: Optional[str] = None
    StartTime: Optional[datetime] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ActiveDirectoryConfigTypeDef(BaseModel):
    DomainName: str
    ServiceAccountSecretArn: str

class AssociationStateReasonTypeDef(BaseModel):
    ErrorCode: Optional[AssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ApplicationSettingsRequestTypeDef(BaseModel):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: Optional[str] = None

class ApplicationSettingsResponseTypeDef(BaseModel):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: Optional[str] = None
    S3BucketName: Optional[str] = None

class AssociateConnectionAliasRequestRequestTypeDef(BaseModel):
    AliasId: str
    ResourceId: str

class AssociateIpGroupsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    GroupIds: Sequence[str]

class AssociateWorkspaceApplicationRequestRequestTypeDef(BaseModel):
    WorkspaceId: str
    ApplicationId: str

class IpRuleItemTypeDef(BaseModel):
    ipRule: Optional[str] = None
    ruleDesc: Optional[str] = None

class CapacityStatusTypeDef(BaseModel):
    AvailableUserSessions: int
    DesiredUserSessions: int
    ActualUserSessions: int
    ActiveUserSessions: int

class CapacityTypeDef(BaseModel):
    DesiredUserSessions: int

class CertificateBasedAuthPropertiesTypeDef(BaseModel):
    Status: Optional[CertificateBasedAuthStatusEnumType] = None
    CertificateAuthorityArn: Optional[str] = None

class ClientPropertiesTypeDef(BaseModel):
    ReconnectEnabled: Optional[ReconnectEnumType] = None
    LogUploadEnabled: Optional[LogUploadEnumType] = None

class ComputeTypeTypeDef(BaseModel):
    Name: Optional[ComputeType] = None

class ConnectClientAddInTypeDef(BaseModel):
    AddInId: Optional[str] = None
    ResourceId: Optional[str] = None
    Name: Optional[str] = None
    URL: Optional[str] = None

class ConnectionAliasAssociationTypeDef(BaseModel):
    AssociationStatus: Optional[AssociationStatusType] = None
    AssociatedAccountId: Optional[str] = None
    ResourceId: Optional[str] = None
    ConnectionIdentifier: Optional[str] = None

class ConnectionAliasPermissionTypeDef(BaseModel):
    SharedAccountId: str
    AllowAssociation: bool

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class CreateAccountLinkInvitationRequestRequestTypeDef(BaseModel):
    TargetAccountId: str
    ClientToken: Optional[str] = None

class CreateConnectClientAddInRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Name: str
    URL: str

class PendingCreateStandbyWorkspacesRequestTypeDef(BaseModel):
    UserName: Optional[str] = None
    DirectoryId: Optional[str] = None
    State: Optional[WorkspaceStateType] = None
    WorkspaceId: Optional[str] = None

class RootStorageTypeDef(BaseModel):
    Capacity: str

class UserStorageTypeDef(BaseModel):
    Capacity: str

class OperatingSystemTypeDef(BaseModel):
    Type: Optional[OperatingSystemTypeType] = None

class TimeoutSettingsTypeDef(BaseModel):
    DisconnectTimeoutInSeconds: Optional[int] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    MaxUserDurationInSeconds: Optional[int] = None

class DataReplicationSettingsTypeDef(BaseModel):
    DataReplication: Optional[DataReplicationType] = None
    RecoverySnapshotTime: Optional[datetime] = None

class DefaultClientBrandingAttributesTypeDef(BaseModel):
    LogoUrl: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None

class DefaultWorkspaceCreationPropertiesTypeDef(BaseModel):
    EnableWorkDocs: Optional[bool] = None
    EnableInternetAccess: Optional[bool] = None
    DefaultOu: Optional[str] = None
    CustomSecurityGroupId: Optional[str] = None
    UserEnabledAsLocalAdministrator: Optional[bool] = None
    EnableMaintenanceMode: Optional[bool] = None
    InstanceIamRoleArn: Optional[str] = None

class DeleteAccountLinkInvitationRequestRequestTypeDef(BaseModel):
    LinkId: str
    ClientToken: Optional[str] = None

class DeleteClientBrandingRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Platforms: Sequence[ClientDeviceTypeType]

class DeleteConnectClientAddInRequestRequestTypeDef(BaseModel):
    AddInId: str
    ResourceId: str

class DeleteConnectionAliasRequestRequestTypeDef(BaseModel):
    AliasId: str

class DeleteIpGroupRequestRequestTypeDef(BaseModel):
    GroupId: str

class DeleteTagsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagKeys: Sequence[str]

class DeleteWorkspaceBundleRequestRequestTypeDef(BaseModel):
    BundleId: Optional[str] = None

class DeleteWorkspaceImageRequestRequestTypeDef(BaseModel):
    ImageId: str

class DeployWorkspaceApplicationsRequestRequestTypeDef(BaseModel):
    WorkspaceId: str
    Force: Optional[bool] = None

class DeregisterWorkspaceDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAccountModificationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class DescribeApplicationAssociationsRequestRequestTypeDef(BaseModel):
    ApplicationId: str
    AssociatedResourceTypes: Sequence[ApplicationAssociatedResourceTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeApplicationsRequestRequestTypeDef(BaseModel):
    ApplicationIds: Optional[Sequence[str]] = None
    ComputeTypeNames: Optional[Sequence[ComputeType]] = None
    LicenseType: Optional[WorkSpaceApplicationLicenseTypeType] = None
    OperatingSystemNames: Optional[Sequence[OperatingSystemNameType]] = None
    Owner: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class WorkSpaceApplicationTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    Created: Optional[datetime] = None
    Description: Optional[str] = None
    LicenseType: Optional[WorkSpaceApplicationLicenseTypeType] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    State: Optional[WorkSpaceApplicationStateType] = None
    SupportedComputeTypeNames: Optional[List[ComputeType]] = None
    SupportedOperatingSystemNames: Optional[List[OperatingSystemNameType]] = None

class DescribeBundleAssociationsRequestRequestTypeDef(BaseModel):
    BundleId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]

class DescribeClientBrandingRequestRequestTypeDef(BaseModel):
    ResourceId: str

class IosClientBrandingAttributesTypeDef(BaseModel):
    LogoUrl: Optional[str] = None
    Logo2xUrl: Optional[str] = None
    Logo3xUrl: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None

class DescribeClientPropertiesRequestRequestTypeDef(BaseModel):
    ResourceIds: Sequence[str]

class DescribeConnectClientAddInsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeConnectionAliasPermissionsRequestRequestTypeDef(BaseModel):
    AliasId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeConnectionAliasesRequestRequestTypeDef(BaseModel):
    AliasIds: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeImageAssociationsRequestRequestTypeDef(BaseModel):
    ImageId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]

class DescribeIpGroupsRequestRequestTypeDef(BaseModel):
    GroupIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeTagsRequestRequestTypeDef(BaseModel):
    ResourceId: str

class DescribeWorkspaceAssociationsRequestRequestTypeDef(BaseModel):
    WorkspaceId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]

class DescribeWorkspaceBundlesRequestRequestTypeDef(BaseModel):
    BundleIds: Optional[Sequence[str]] = None
    Owner: Optional[str] = None
    NextToken: Optional[str] = None

class DescribeWorkspaceDirectoriesRequestRequestTypeDef(BaseModel):
    DirectoryIds: Optional[Sequence[str]] = None
    WorkspaceDirectoryNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeWorkspaceImagePermissionsRequestRequestTypeDef(BaseModel):
    ImageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ImagePermissionTypeDef(BaseModel):
    SharedAccountId: Optional[str] = None

class DescribeWorkspaceImagesRequestRequestTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    ImageType: Optional[ImageTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeWorkspaceSnapshotsRequestRequestTypeDef(BaseModel):
    WorkspaceId: str

class SnapshotTypeDef(BaseModel):
    SnapshotTime: Optional[datetime] = None

class DescribeWorkspacesConnectionStatusRequestRequestTypeDef(BaseModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None

class WorkspaceConnectionStatusTypeDef(BaseModel):
    WorkspaceId: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    ConnectionStateCheckTimestamp: Optional[datetime] = None
    LastKnownUserConnectionTimestamp: Optional[datetime] = None

class DescribeWorkspacesPoolSessionsRequestRequestTypeDef(BaseModel):
    PoolId: str
    UserId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeWorkspacesPoolsFilterTypeDef(BaseModel):
    Name: Literal["PoolName"]
    Values: Sequence[str]
    Operator: DescribeWorkspacesPoolsFilterOperatorType

class DescribeWorkspacesRequestRequestTypeDef(BaseModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    DirectoryId: Optional[str] = None
    UserName: Optional[str] = None
    BundleId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    WorkspaceName: Optional[str] = None

class DisassociateConnectionAliasRequestRequestTypeDef(BaseModel):
    AliasId: str

class DisassociateIpGroupsRequestRequestTypeDef(BaseModel):
    DirectoryId: str
    GroupIds: Sequence[str]

class DisassociateWorkspaceApplicationRequestRequestTypeDef(BaseModel):
    WorkspaceId: str
    ApplicationId: str

class ErrorDetailsTypeDef(BaseModel):
    ErrorCode: Optional[WorkspaceImageErrorDetailCodeType] = None
    ErrorMessage: Optional[str] = None

class FailedWorkspaceChangeRequestTypeDef(BaseModel):
    WorkspaceId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class GetAccountLinkRequestRequestTypeDef(BaseModel):
    LinkId: Optional[str] = None
    LinkedAccountId: Optional[str] = None

class ListAccountLinksRequestRequestTypeDef(BaseModel):
    LinkStatusFilter: Optional[Sequence[AccountLinkStatusEnumType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAvailableManagementCidrRangesRequestRequestTypeDef(BaseModel):
    ManagementCidrRangeConstraint: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MigrateWorkspaceRequestRequestTypeDef(BaseModel):
    SourceWorkspaceId: str
    BundleId: str

class ModificationStateTypeDef(BaseModel):
    Resource: Optional[ModificationResourceEnumType] = None
    State: Optional[ModificationStateEnumType] = None

class ModifyAccountRequestRequestTypeDef(BaseModel):
    DedicatedTenancySupport: Optional[Literal["ENABLED"]] = None
    DedicatedTenancyManagementCidrRange: Optional[str] = None

class SamlPropertiesTypeDef(BaseModel):
    Status: Optional[SamlStatusEnumType] = None
    UserAccessUrl: Optional[str] = None
    RelayStateParameterName: Optional[str] = None

class SelfservicePermissionsTypeDef(BaseModel):
    RestartWorkspace: Optional[ReconnectEnumType] = None
    IncreaseVolumeSize: Optional[ReconnectEnumType] = None
    ChangeComputeType: Optional[ReconnectEnumType] = None
    SwitchRunningMode: Optional[ReconnectEnumType] = None
    RebuildWorkspace: Optional[ReconnectEnumType] = None

class WorkspaceAccessPropertiesTypeDef(BaseModel):
    DeviceTypeWindows: Optional[AccessPropertyValueType] = None
    DeviceTypeOsx: Optional[AccessPropertyValueType] = None
    DeviceTypeWeb: Optional[AccessPropertyValueType] = None
    DeviceTypeIos: Optional[AccessPropertyValueType] = None
    DeviceTypeAndroid: Optional[AccessPropertyValueType] = None
    DeviceTypeChromeOs: Optional[AccessPropertyValueType] = None
    DeviceTypeZeroClient: Optional[AccessPropertyValueType] = None
    DeviceTypeLinux: Optional[AccessPropertyValueType] = None

class WorkspaceCreationPropertiesTypeDef(BaseModel):
    EnableWorkDocs: Optional[bool] = None
    EnableInternetAccess: Optional[bool] = None
    DefaultOu: Optional[str] = None
    CustomSecurityGroupId: Optional[str] = None
    UserEnabledAsLocalAdministrator: Optional[bool] = None
    EnableMaintenanceMode: Optional[bool] = None
    InstanceIamRoleArn: Optional[str] = None

class WorkspacePropertiesTypeDef(BaseModel):
    RunningMode: Optional[RunningModeType] = None
    RunningModeAutoStopTimeoutInMinutes: Optional[int] = None
    RootVolumeSizeGib: Optional[int] = None
    UserVolumeSizeGib: Optional[int] = None
    ComputeTypeName: Optional[ComputeType] = None
    Protocols: Optional[Sequence[ProtocolType]] = None
    OperatingSystemName: Optional[OperatingSystemNameType] = None

class ModifyWorkspaceStateRequestRequestTypeDef(BaseModel):
    WorkspaceId: str
    WorkspaceState: TargetWorkspaceStateType

class NetworkAccessConfigurationTypeDef(BaseModel):
    EniPrivateIpAddress: Optional[str] = None
    EniId: Optional[str] = None

class RebootRequestTypeDef(BaseModel):
    WorkspaceId: str

class RebuildRequestTypeDef(BaseModel):
    WorkspaceId: str

class RejectAccountLinkInvitationRequestRequestTypeDef(BaseModel):
    LinkId: str
    ClientToken: Optional[str] = None

class RelatedWorkspacePropertiesTypeDef(BaseModel):
    WorkspaceId: Optional[str] = None
    Region: Optional[str] = None
    State: Optional[WorkspaceStateType] = None
    Type: Optional[StandbyWorkspaceRelationshipTypeType] = None

class RestoreWorkspaceRequestRequestTypeDef(BaseModel):
    WorkspaceId: str

class RevokeIpRulesRequestRequestTypeDef(BaseModel):
    GroupId: str
    UserRules: Sequence[str]

class StandbyWorkspacesPropertiesTypeDef(BaseModel):
    StandbyWorkspaceId: Optional[str] = None
    DataReplication: Optional[DataReplicationType] = None
    RecoverySnapshotTime: Optional[datetime] = None

class StartRequestTypeDef(BaseModel):
    WorkspaceId: Optional[str] = None

class StartWorkspacesPoolRequestRequestTypeDef(BaseModel):
    PoolId: str

class StopRequestTypeDef(BaseModel):
    WorkspaceId: Optional[str] = None

class StopWorkspacesPoolRequestRequestTypeDef(BaseModel):
    PoolId: str

class StorageConnectorTypeDef(BaseModel):
    ConnectorType: Literal["HOME_FOLDER"]
    Status: StorageConnectorStatusEnumType

class UserSettingTypeDef(BaseModel):
    Action: UserSettingActionEnumType
    Permission: UserSettingPermissionEnumType
    MaximumLength: Optional[int] = None

class TerminateRequestTypeDef(BaseModel):
    WorkspaceId: str

class TerminateWorkspacesPoolRequestRequestTypeDef(BaseModel):
    PoolId: str

class TerminateWorkspacesPoolSessionRequestRequestTypeDef(BaseModel):
    SessionId: str

class UpdateConnectClientAddInRequestRequestTypeDef(BaseModel):
    AddInId: str
    ResourceId: str
    Name: Optional[str] = None
    URL: Optional[str] = None

class UpdateResultTypeDef(BaseModel):
    UpdateAvailable: Optional[bool] = None
    Description: Optional[str] = None

class UpdateWorkspaceBundleRequestRequestTypeDef(BaseModel):
    BundleId: Optional[str] = None
    ImageId: Optional[str] = None

class UpdateWorkspaceImagePermissionRequestRequestTypeDef(BaseModel):
    ImageId: str
    AllowCopyImage: bool
    SharedAccountId: str

class WorkspacePropertiesExtraOutputTypeDef(BaseModel):
    RunningMode: Optional[RunningModeType] = None
    RunningModeAutoStopTimeoutInMinutes: Optional[int] = None
    RootVolumeSizeGib: Optional[int] = None
    UserVolumeSizeGib: Optional[int] = None
    ComputeTypeName: Optional[ComputeType] = None
    Protocols: Optional[List[ProtocolType]] = None
    OperatingSystemName: Optional[OperatingSystemNameType] = None

class WorkspacePropertiesOutputTypeDef(BaseModel):
    RunningMode: Optional[RunningModeType] = None
    RunningModeAutoStopTimeoutInMinutes: Optional[int] = None
    RootVolumeSizeGib: Optional[int] = None
    UserVolumeSizeGib: Optional[int] = None
    ComputeTypeName: Optional[ComputeType] = None
    Protocols: Optional[List[ProtocolType]] = None
    OperatingSystemName: Optional[OperatingSystemNameType] = None

class WorkspacesPoolErrorTypeDef(BaseModel):
    ErrorCode: Optional[WorkspacesPoolErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class AcceptAccountLinkInvitationResultTypeDef(BaseModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateConnectionAliasResultTypeDef(BaseModel):
    ConnectionIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef

class CopyWorkspaceImageResultTypeDef(BaseModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccountLinkInvitationResultTypeDef(BaseModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectClientAddInResultTypeDef(BaseModel):
    AddInId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionAliasResultTypeDef(BaseModel):
    AliasId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIpGroupResultTypeDef(BaseModel):
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUpdatedWorkspaceImageResultTypeDef(BaseModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAccountLinkInvitationResultTypeDef(BaseModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountResultTypeDef(BaseModel):
    DedicatedTenancySupport: DedicatedTenancySupportResultEnumType
    DedicatedTenancyManagementCidrRange: str
    DedicatedTenancyAccountType: DedicatedTenancyAccountTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountLinkResultTypeDef(BaseModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportWorkspaceImageResultTypeDef(BaseModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountLinksResultTypeDef(BaseModel):
    AccountLinks: List[AccountLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListAvailableManagementCidrRangesResultTypeDef(BaseModel):
    ManagementCidrRanges: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MigrateWorkspaceResultTypeDef(BaseModel):
    SourceWorkspaceId: str
    TargetWorkspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterWorkspaceDirectoryResultTypeDef(BaseModel):
    DirectoryId: str
    State: WorkspaceDirectoryStateType
    ResponseMetadata: ResponseMetadataTypeDef

class RejectAccountLinkInvitationResultTypeDef(BaseModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountModificationsResultTypeDef(BaseModel):
    AccountModifications: List[AccountModificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ApplicationResourceAssociationTypeDef(BaseModel):
    ApplicationId: Optional[str] = None
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[ApplicationAssociatedResourceTypeType] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None

class BundleResourceAssociationTypeDef(BaseModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal["APPLICATION"]] = None
    BundleId: Optional[str] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None

class ImageResourceAssociationTypeDef(BaseModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal["APPLICATION"]] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ImageId: Optional[str] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None

class WorkspaceResourceAssociationTypeDef(BaseModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal["APPLICATION"]] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None
    WorkspaceId: Optional[str] = None

class AuthorizeIpRulesRequestRequestTypeDef(BaseModel):
    GroupId: str
    UserRules: Sequence[IpRuleItemTypeDef]

class UpdateRulesOfIpGroupRequestRequestTypeDef(BaseModel):
    GroupId: str
    UserRules: Sequence[IpRuleItemTypeDef]

class WorkspacesIpGroupTypeDef(BaseModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None
    groupDesc: Optional[str] = None
    userRules: Optional[List[IpRuleItemTypeDef]] = None

class DefaultImportClientBrandingAttributesTypeDef(BaseModel):
    Logo: Optional[BlobTypeDef] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Mapping[str, str]] = None

class IosImportClientBrandingAttributesTypeDef(BaseModel):
    Logo: Optional[BlobTypeDef] = None
    Logo2x: Optional[BlobTypeDef] = None
    Logo3x: Optional[BlobTypeDef] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Mapping[str, str]] = None

class ModifyCertificateBasedAuthPropertiesRequestRequestTypeDef(BaseModel):
    ResourceId: str
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None
    PropertiesToDelete: Optional[       Sequence[Literal["CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"]]     ] = None

class ClientPropertiesResultTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    ClientProperties: Optional[ClientPropertiesTypeDef] = None

class ModifyClientPropertiesRequestRequestTypeDef(BaseModel):
    ResourceId: str
    ClientProperties: ClientPropertiesTypeDef

class DescribeConnectClientAddInsResultTypeDef(BaseModel):
    AddIns: List[ConnectClientAddInTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ConnectionAliasTypeDef(BaseModel):
    ConnectionString: Optional[str] = None
    AliasId: Optional[str] = None
    State: Optional[ConnectionAliasStateType] = None
    OwnerAccountId: Optional[str] = None
    Associations: Optional[List[ConnectionAliasAssociationTypeDef]] = None

class DescribeConnectionAliasPermissionsResultTypeDef(BaseModel):
    AliasId: str
    ConnectionAliasPermissions: List[ConnectionAliasPermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateConnectionAliasPermissionRequestRequestTypeDef(BaseModel):
    AliasId: str
    ConnectionAliasPermission: ConnectionAliasPermissionTypeDef

class CopyWorkspaceImageRequestRequestTypeDef(BaseModel):
    Name: str
    SourceImageId: str
    SourceRegion: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateConnectionAliasRequestRequestTypeDef(BaseModel):
    ConnectionString: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateIpGroupRequestRequestTypeDef(BaseModel):
    GroupName: str
    GroupDesc: Optional[str] = None
    UserRules: Optional[Sequence[IpRuleItemTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateTagsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class CreateUpdatedWorkspaceImageRequestRequestTypeDef(BaseModel):
    Name: str
    Description: str
    SourceImageId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateWorkspaceImageRequestRequestTypeDef(BaseModel):
    Name: str
    Description: str
    WorkspaceId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class DescribeTagsResultTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ImportWorkspaceImageRequestRequestTypeDef(BaseModel):
    Ec2ImageId: str
    IngestionProcess: WorkspaceImageIngestionProcessType
    ImageName: str
    ImageDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    Applications: Optional[Sequence[ApplicationType]] = None

class RegisterWorkspaceDirectoryRequestRequestTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    EnableWorkDocs: Optional[bool] = None
    EnableSelfService: Optional[bool] = None
    Tenancy: Optional[TenancyType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkspaceDirectoryName: Optional[str] = None
    WorkspaceDirectoryDescription: Optional[str] = None
    UserIdentityType: Optional[UserIdentityTypeType] = None
    WorkspaceType: Optional[WorkspaceTypeType] = None
    ActiveDirectoryConfig: Optional[ActiveDirectoryConfigTypeDef] = None

class StandbyWorkspaceOutputTypeDef(BaseModel):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    DataReplication: Optional[DataReplicationType] = None

class StandbyWorkspaceTypeDef(BaseModel):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataReplication: Optional[DataReplicationType] = None

class CreateWorkspaceBundleRequestRequestTypeDef(BaseModel):
    BundleName: str
    BundleDescription: str
    ImageId: str
    ComputeType: ComputeTypeTypeDef
    UserStorage: UserStorageTypeDef
    RootStorage: Optional[RootStorageTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class WorkspaceBundleTypeDef(BaseModel):
    BundleId: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    Description: Optional[str] = None
    ImageId: Optional[str] = None
    RootStorage: Optional[RootStorageTypeDef] = None
    UserStorage: Optional[UserStorageTypeDef] = None
    ComputeType: Optional[ComputeTypeTypeDef] = None
    LastUpdatedTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    State: Optional[WorkspaceBundleStateType] = None
    BundleType: Optional[BundleTypeType] = None

class CreateWorkspaceImageResultTypeDef(BaseModel):
    ImageId: str
    Name: str
    Description: str
    OperatingSystem: OperatingSystemTypeDef
    State: WorkspaceImageStateType
    RequiredTenancy: WorkspaceImageRequiredTenancyType
    Created: datetime
    OwnerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspacesPoolRequestRequestTypeDef(BaseModel):
    PoolName: str
    Description: str
    BundleId: str
    DirectoryId: str
    Capacity: CapacityTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    ApplicationSettings: Optional[ApplicationSettingsRequestTypeDef] = None
    TimeoutSettings: Optional[TimeoutSettingsTypeDef] = None

class UpdateWorkspacesPoolRequestRequestTypeDef(BaseModel):
    PoolId: str
    Description: Optional[str] = None
    BundleId: Optional[str] = None
    DirectoryId: Optional[str] = None
    Capacity: Optional[CapacityTypeDef] = None
    ApplicationSettings: Optional[ApplicationSettingsRequestTypeDef] = None
    TimeoutSettings: Optional[TimeoutSettingsTypeDef] = None

class DescribeAccountModificationsRequestDescribeAccountModificationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeIpGroupsRequestDescribeIpGroupsPaginateTypeDef(BaseModel):
    GroupIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeWorkspaceBundlesRequestDescribeWorkspaceBundlesPaginateTypeDef(BaseModel):
    BundleIds: Optional[Sequence[str]] = None
    Owner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeWorkspaceDirectoriesRequestDescribeWorkspaceDirectoriesPaginateTypeDef(BaseModel):
    DirectoryIds: Optional[Sequence[str]] = None
    WorkspaceDirectoryNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeWorkspaceImagesRequestDescribeWorkspaceImagesPaginateTypeDef(BaseModel):
    ImageIds: Optional[Sequence[str]] = None
    ImageType: Optional[ImageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeWorkspacesConnectionStatusRequestDescribeWorkspacesConnectionStatusPaginateTypeDef(BaseModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeWorkspacesRequestDescribeWorkspacesPaginateTypeDef(BaseModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    DirectoryId: Optional[str] = None
    UserName: Optional[str] = None
    BundleId: Optional[str] = None
    WorkspaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAccountLinksRequestListAccountLinksPaginateTypeDef(BaseModel):
    LinkStatusFilter: Optional[Sequence[AccountLinkStatusEnumType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeApplicationsResultTypeDef(BaseModel):
    Applications: List[WorkSpaceApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeClientBrandingResultTypeDef(BaseModel):
    DeviceTypeWindows: DefaultClientBrandingAttributesTypeDef
    DeviceTypeOsx: DefaultClientBrandingAttributesTypeDef
    DeviceTypeAndroid: DefaultClientBrandingAttributesTypeDef
    DeviceTypeIos: IosClientBrandingAttributesTypeDef
    DeviceTypeLinux: DefaultClientBrandingAttributesTypeDef
    DeviceTypeWeb: DefaultClientBrandingAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportClientBrandingResultTypeDef(BaseModel):
    DeviceTypeWindows: DefaultClientBrandingAttributesTypeDef
    DeviceTypeOsx: DefaultClientBrandingAttributesTypeDef
    DeviceTypeAndroid: DefaultClientBrandingAttributesTypeDef
    DeviceTypeIos: IosClientBrandingAttributesTypeDef
    DeviceTypeLinux: DefaultClientBrandingAttributesTypeDef
    DeviceTypeWeb: DefaultClientBrandingAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceImagePermissionsResultTypeDef(BaseModel):
    ImageId: str
    ImagePermissions: List[ImagePermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeWorkspaceSnapshotsResultTypeDef(BaseModel):
    RebuildSnapshots: List[SnapshotTypeDef]
    RestoreSnapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspacesConnectionStatusResultTypeDef(BaseModel):
    WorkspacesConnectionStatus: List[WorkspaceConnectionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeWorkspacesPoolsRequestRequestTypeDef(BaseModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[DescribeWorkspacesPoolsFilterTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None

class RebootWorkspacesResultTypeDef(BaseModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RebuildWorkspacesResultTypeDef(BaseModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartWorkspacesResultTypeDef(BaseModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopWorkspacesResultTypeDef(BaseModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TerminateWorkspacesResultTypeDef(BaseModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifySamlPropertiesRequestRequestTypeDef(BaseModel):
    ResourceId: str
    SamlProperties: Optional[SamlPropertiesTypeDef] = None
    PropertiesToDelete: Optional[Sequence[DeletableSamlPropertyType]] = None

class ModifySelfservicePermissionsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    SelfservicePermissions: SelfservicePermissionsTypeDef

class ModifyWorkspaceAccessPropertiesRequestRequestTypeDef(BaseModel):
    ResourceId: str
    WorkspaceAccessProperties: WorkspaceAccessPropertiesTypeDef

class ModifyWorkspaceCreationPropertiesRequestRequestTypeDef(BaseModel):
    ResourceId: str
    WorkspaceCreationProperties: WorkspaceCreationPropertiesTypeDef

class ModifyWorkspacePropertiesRequestRequestTypeDef(BaseModel):
    WorkspaceId: str
    WorkspaceProperties: Optional[WorkspacePropertiesTypeDef] = None
    DataReplication: Optional[DataReplicationType] = None

class WorkspaceRequestTypeDef(BaseModel):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: Optional[str] = None
    UserVolumeEncryptionEnabled: Optional[bool] = None
    RootVolumeEncryptionEnabled: Optional[bool] = None
    WorkspaceProperties: Optional[WorkspacePropertiesTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkspaceName: Optional[str] = None

class WorkspacesPoolSessionTypeDef(BaseModel):
    SessionId: str
    PoolId: str
    UserId: str
    AuthenticationType: Optional[Literal["SAML"]] = None
    ConnectionState: Optional[SessionConnectionStateType] = None
    InstanceId: Optional[str] = None
    ExpirationTime: Optional[datetime] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfigurationTypeDef] = None
    StartTime: Optional[datetime] = None

class RebootWorkspacesRequestRequestTypeDef(BaseModel):
    RebootWorkspaceRequests: Sequence[RebootRequestTypeDef]

class RebuildWorkspacesRequestRequestTypeDef(BaseModel):
    RebuildWorkspaceRequests: Sequence[RebuildRequestTypeDef]

class StartWorkspacesRequestRequestTypeDef(BaseModel):
    StartWorkspaceRequests: Sequence[StartRequestTypeDef]

class StopWorkspacesRequestRequestTypeDef(BaseModel):
    StopWorkspaceRequests: Sequence[StopRequestTypeDef]

class StreamingPropertiesExtraOutputTypeDef(BaseModel):
    StreamingExperiencePreferredProtocol: Optional[       StreamingExperiencePreferredProtocolEnumType     ] = None
    UserSettings: Optional[List[UserSettingTypeDef]] = None
    StorageConnectors: Optional[List[StorageConnectorTypeDef]] = None

class StreamingPropertiesOutputTypeDef(BaseModel):
    StreamingExperiencePreferredProtocol: Optional[       StreamingExperiencePreferredProtocolEnumType     ] = None
    UserSettings: Optional[List[UserSettingTypeDef]] = None
    StorageConnectors: Optional[List[StorageConnectorTypeDef]] = None

class StreamingPropertiesTypeDef(BaseModel):
    StreamingExperiencePreferredProtocol: Optional[       StreamingExperiencePreferredProtocolEnumType     ] = None
    UserSettings: Optional[Sequence[UserSettingTypeDef]] = None
    StorageConnectors: Optional[Sequence[StorageConnectorTypeDef]] = None

class TerminateWorkspacesRequestRequestTypeDef(BaseModel):
    TerminateWorkspaceRequests: Sequence[TerminateRequestTypeDef]

class WorkspaceImageTypeDef(BaseModel):
    ImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    OperatingSystem: Optional[OperatingSystemTypeDef] = None
    State: Optional[WorkspaceImageStateType] = None
    RequiredTenancy: Optional[WorkspaceImageRequiredTenancyType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    Created: Optional[datetime] = None
    OwnerAccountId: Optional[str] = None
    Updates: Optional[UpdateResultTypeDef] = None
    ErrorDetails: Optional[List[ErrorDetailsTypeDef]] = None

class WorkspaceRequestOutputTypeDef(BaseModel):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: Optional[str] = None
    UserVolumeEncryptionEnabled: Optional[bool] = None
    RootVolumeEncryptionEnabled: Optional[bool] = None
    WorkspaceProperties: Optional[WorkspacePropertiesOutputTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    WorkspaceName: Optional[str] = None

class WorkspaceTypeDef(BaseModel):
    WorkspaceId: Optional[str] = None
    DirectoryId: Optional[str] = None
    UserName: Optional[str] = None
    IpAddress: Optional[str] = None
    State: Optional[WorkspaceStateType] = None
    BundleId: Optional[str] = None
    SubnetId: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    ComputerName: Optional[str] = None
    VolumeEncryptionKey: Optional[str] = None
    UserVolumeEncryptionEnabled: Optional[bool] = None
    RootVolumeEncryptionEnabled: Optional[bool] = None
    WorkspaceName: Optional[str] = None
    WorkspaceProperties: Optional[WorkspacePropertiesOutputTypeDef] = None
    ModificationStates: Optional[List[ModificationStateTypeDef]] = None
    RelatedWorkspaces: Optional[List[RelatedWorkspacePropertiesTypeDef]] = None
    DataReplicationSettings: Optional[DataReplicationSettingsTypeDef] = None
    StandbyWorkspacesProperties: Optional[List[StandbyWorkspacesPropertiesTypeDef]] = None

class WorkspacesPoolTypeDef(BaseModel):
    PoolId: str
    PoolArn: str
    CapacityStatus: CapacityStatusTypeDef
    PoolName: str
    State: WorkspacesPoolStateType
    CreatedAt: datetime
    BundleId: str
    DirectoryId: str
    Description: Optional[str] = None
    Errors: Optional[List[WorkspacesPoolErrorTypeDef]] = None
    ApplicationSettings: Optional[ApplicationSettingsResponseTypeDef] = None
    TimeoutSettings: Optional[TimeoutSettingsTypeDef] = None

class DescribeApplicationAssociationsResultTypeDef(BaseModel):
    Associations: List[ApplicationResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeBundleAssociationsResultTypeDef(BaseModel):
    Associations: List[BundleResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageAssociationsResultTypeDef(BaseModel):
    Associations: List[ImageResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateWorkspaceApplicationResultTypeDef(BaseModel):
    Association: WorkspaceResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceAssociationsResultTypeDef(BaseModel):
    Associations: List[WorkspaceResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateWorkspaceApplicationResultTypeDef(BaseModel):
    Association: WorkspaceResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WorkSpaceApplicationDeploymentTypeDef(BaseModel):
    Associations: Optional[List[WorkspaceResourceAssociationTypeDef]] = None

class DescribeIpGroupsResultTypeDef(BaseModel):
    Result: List[WorkspacesIpGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportClientBrandingRequestRequestTypeDef(BaseModel):
    ResourceId: str
    DeviceTypeWindows: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeOsx: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeAndroid: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeIos: Optional[IosImportClientBrandingAttributesTypeDef] = None
    DeviceTypeLinux: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeWeb: Optional[DefaultImportClientBrandingAttributesTypeDef] = None

class DescribeClientPropertiesResultTypeDef(BaseModel):
    ClientPropertiesList: List[ClientPropertiesResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeConnectionAliasesResultTypeDef(BaseModel):
    ConnectionAliases: List[ConnectionAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailedCreateStandbyWorkspacesRequestTypeDef(BaseModel):
    StandbyWorkspaceRequest: Optional[StandbyWorkspaceOutputTypeDef] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class CreateWorkspaceBundleResultTypeDef(BaseModel):
    WorkspaceBundle: WorkspaceBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspaceBundlesResultTypeDef(BaseModel):
    Bundles: List[WorkspaceBundleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeWorkspacesPoolSessionsResultTypeDef(BaseModel):
    Sessions: List[WorkspacesPoolSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class WorkspaceDirectoryTypeDef(BaseModel):
    DirectoryId: Optional[str] = None
    Alias: Optional[str] = None
    DirectoryName: Optional[str] = None
    RegistrationCode: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    DnsIpAddresses: Optional[List[str]] = None
    CustomerUserName: Optional[str] = None
    IamRoleId: Optional[str] = None
    DirectoryType: Optional[WorkspaceDirectoryTypeType] = None
    WorkspaceSecurityGroupId: Optional[str] = None
    State: Optional[WorkspaceDirectoryStateType] = None
    WorkspaceCreationProperties: Optional[DefaultWorkspaceCreationPropertiesTypeDef] = None
    ipGroupIds: Optional[List[str]] = None
    WorkspaceAccessProperties: Optional[WorkspaceAccessPropertiesTypeDef] = None
    Tenancy: Optional[TenancyType] = None
    SelfservicePermissions: Optional[SelfservicePermissionsTypeDef] = None
    SamlProperties: Optional[SamlPropertiesTypeDef] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None
    WorkspaceDirectoryName: Optional[str] = None
    WorkspaceDirectoryDescription: Optional[str] = None
    UserIdentityType: Optional[UserIdentityTypeType] = None
    WorkspaceType: Optional[WorkspaceTypeType] = None
    ActiveDirectoryConfig: Optional[ActiveDirectoryConfigTypeDef] = None
    StreamingProperties: Optional[StreamingPropertiesOutputTypeDef] = None
    ErrorMessage: Optional[str] = None

class ModifyStreamingPropertiesRequestRequestTypeDef(BaseModel):
    ResourceId: str
    StreamingProperties: Optional[StreamingPropertiesTypeDef] = None

class DescribeWorkspaceImagesResultTypeDef(BaseModel):
    Images: List[WorkspaceImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class FailedCreateWorkspaceRequestTypeDef(BaseModel):
    WorkspaceRequest: Optional[WorkspaceRequestOutputTypeDef] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class DescribeWorkspacesResultTypeDef(BaseModel):
    Workspaces: List[WorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateWorkspacesPoolResultTypeDef(BaseModel):
    WorkspacesPool: WorkspacesPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkspacesPoolsResultTypeDef(BaseModel):
    WorkspacesPools: List[WorkspacesPoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateWorkspacesPoolResultTypeDef(BaseModel):
    WorkspacesPool: WorkspacesPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeployWorkspaceApplicationsResultTypeDef(BaseModel):
    Deployment: WorkSpaceApplicationDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStandbyWorkspacesResultTypeDef(BaseModel):
    FailedStandbyRequests: List[FailedCreateStandbyWorkspacesRequestTypeDef]
    PendingStandbyRequests: List[PendingCreateStandbyWorkspacesRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStandbyWorkspacesRequestRequestTypeDef(BaseModel):
    PrimaryRegion: str
    StandbyWorkspaces: Sequence[StandbyWorkspaceUnionTypeDef]

class DescribeWorkspaceDirectoriesResultTypeDef(BaseModel):
    Directories: List[WorkspaceDirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateWorkspacesResultTypeDef(BaseModel):
    FailedRequests: List[FailedCreateWorkspaceRequestTypeDef]
    PendingRequests: List[WorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspacesRequestRequestTypeDef(BaseModel):
    Workspaces: Sequence[WorkspaceRequestUnionTypeDef]

