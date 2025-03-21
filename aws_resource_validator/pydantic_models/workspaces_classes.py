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
from aws_resource_validator.pydantic_models.workspaces_constants import *

class AcceptAccountLinkInvitationRequestTypeDef(BaseValidatorModel):
    LinkId: str
    ClientToken: Optional[str] = None


class AccountLinkTypeDef(BaseValidatorModel):
    AccountLinkId: Optional[str] = None
    AccountLinkStatus: Optional[AccountLinkStatusEnumType] = None
    SourceAccountId: Optional[str] = None
    TargetAccountId: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AccountModificationTypeDef(BaseValidatorModel):
    ModificationState: Optional[DedicatedTenancyModificationStateEnumType] = None
    DedicatedTenancySupport: Optional[DedicatedTenancySupportResultEnumType] = None
    DedicatedTenancyManagementCidrRange: Optional[str] = None
    StartTime: Optional[datetime] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ActiveDirectoryConfigTypeDef(BaseValidatorModel):
    DomainName: str
    ServiceAccountSecretArn: str


class AssociationStateReasonTypeDef(BaseValidatorModel):
    ErrorCode: Optional[AssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ApplicationSettingsRequestTypeDef(BaseValidatorModel):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: Optional[str] = None


class ApplicationSettingsResponseTypeDef(BaseValidatorModel):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: Optional[str] = None
    S3BucketName: Optional[str] = None


class AssociateConnectionAliasRequestTypeDef(BaseValidatorModel):
    AliasId: str
    ResourceId: str


class AssociateIpGroupsRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    GroupIds: Sequence[str]


class AssociateWorkspaceApplicationRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str
    ApplicationId: str


class IpRuleItemTypeDef(BaseValidatorModel):
    ipRule: Optional[str] = None
    ruleDesc: Optional[str] = None


class CapacityStatusTypeDef(BaseValidatorModel):
    AvailableUserSessions: int
    DesiredUserSessions: int
    ActualUserSessions: int
    ActiveUserSessions: int


class CapacityTypeDef(BaseValidatorModel):
    DesiredUserSessions: int


class CertificateBasedAuthPropertiesTypeDef(BaseValidatorModel):
    Status: Optional[CertificateBasedAuthStatusEnumType] = None
    CertificateAuthorityArn: Optional[str] = None


class ClientPropertiesTypeDef(BaseValidatorModel):
    ReconnectEnabled: Optional[ReconnectEnumType] = None
    LogUploadEnabled: Optional[LogUploadEnumType] = None


class ComputeTypeTypeDef(BaseValidatorModel):
    Name: Optional[ComputeType] = None


class ConnectClientAddInTypeDef(BaseValidatorModel):
    AddInId: Optional[str] = None
    ResourceId: Optional[str] = None
    Name: Optional[str] = None
    URL: Optional[str] = None


class ConnectionAliasAssociationTypeDef(BaseValidatorModel):
    AssociationStatus: Optional[AssociationStatusType] = None
    AssociatedAccountId: Optional[str] = None
    ResourceId: Optional[str] = None
    ConnectionIdentifier: Optional[str] = None


class ConnectionAliasPermissionTypeDef(BaseValidatorModel):
    SharedAccountId: str
    AllowAssociation: bool


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class CreateAccountLinkInvitationRequestTypeDef(BaseValidatorModel):
    TargetAccountId: str
    ClientToken: Optional[str] = None


class CreateConnectClientAddInRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Name: str
    URL: str


class PendingCreateStandbyWorkspacesRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    DirectoryId: Optional[str] = None
    State: Optional[WorkspaceStateType] = None
    WorkspaceId: Optional[str] = None


class RootStorageTypeDef(BaseValidatorModel):
    Capacity: str


class UserStorageTypeDef(BaseValidatorModel):
    Capacity: str


class TimeoutSettingsTypeDef(BaseValidatorModel):
    DisconnectTimeoutInSeconds: Optional[int] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    MaxUserDurationInSeconds: Optional[int] = None


class DataReplicationSettingsTypeDef(BaseValidatorModel):
    DataReplication: Optional[DataReplicationType] = None
    RecoverySnapshotTime: Optional[datetime] = None


class DefaultClientBrandingAttributesTypeDef(BaseValidatorModel):
    LogoUrl: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None


class DefaultWorkspaceCreationPropertiesTypeDef(BaseValidatorModel):
    EnableWorkDocs: Optional[bool] = None
    EnableInternetAccess: Optional[bool] = None
    DefaultOu: Optional[str] = None
    CustomSecurityGroupId: Optional[str] = None
    UserEnabledAsLocalAdministrator: Optional[bool] = None
    EnableMaintenanceMode: Optional[bool] = None
    InstanceIamRoleArn: Optional[str] = None


class DeleteAccountLinkInvitationRequestTypeDef(BaseValidatorModel):
    LinkId: str
    ClientToken: Optional[str] = None


class DeleteClientBrandingRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Platforms: Sequence[ClientDeviceTypeType]


class DeleteConnectClientAddInRequestTypeDef(BaseValidatorModel):
    AddInId: str
    ResourceId: str


class DeleteConnectionAliasRequestTypeDef(BaseValidatorModel):
    AliasId: str


class DeleteIpGroupRequestTypeDef(BaseValidatorModel):
    GroupId: str


class DeleteTagsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagKeys: Sequence[str]


class DeleteWorkspaceBundleRequestTypeDef(BaseValidatorModel):
    BundleId: Optional[str] = None


class DeleteWorkspaceImageRequestTypeDef(BaseValidatorModel):
    ImageId: str


class DeployWorkspaceApplicationsRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str
    Force: Optional[bool] = None


class DeregisterWorkspaceDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAccountModificationsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None


class DescribeApplicationAssociationsRequestTypeDef(BaseValidatorModel):
    ApplicationId: str
    AssociatedResourceTypes: Sequence[ApplicationAssociatedResourceTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeApplicationsRequestTypeDef(BaseValidatorModel):
    ApplicationIds: Optional[Sequence[str]] = None
    ComputeTypeNames: Optional[Sequence[ComputeType]] = None
    LicenseType: Optional[WorkSpaceApplicationLicenseTypeType] = None
    OperatingSystemNames: Optional[Sequence[OperatingSystemNameType]] = None
    Owner: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class WorkSpaceApplicationTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    Created: Optional[datetime] = None
    Description: Optional[str] = None
    LicenseType: Optional[WorkSpaceApplicationLicenseTypeType] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    State: Optional[WorkSpaceApplicationStateType] = None
    SupportedComputeTypeNames: Optional[List[ComputeType]] = None
    SupportedOperatingSystemNames: Optional[List[OperatingSystemNameType]] = None


class DescribeBundleAssociationsRequestTypeDef(BaseValidatorModel):
    BundleId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]


class DescribeClientBrandingRequestTypeDef(BaseValidatorModel):
    ResourceId: str


class IosClientBrandingAttributesTypeDef(BaseValidatorModel):
    LogoUrl: Optional[str] = None
    Logo2xUrl: Optional[str] = None
    Logo3xUrl: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None


class DescribeClientPropertiesRequestTypeDef(BaseValidatorModel):
    ResourceIds: Sequence[str]


class DescribeConnectClientAddInsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeConnectionAliasPermissionsRequestTypeDef(BaseValidatorModel):
    AliasId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeConnectionAliasesRequestTypeDef(BaseValidatorModel):
    AliasIds: Optional[Sequence[str]] = None
    ResourceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeImageAssociationsRequestTypeDef(BaseValidatorModel):
    ImageId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]


class DescribeIpGroupsRequestTypeDef(BaseValidatorModel):
    GroupIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeTagsRequestTypeDef(BaseValidatorModel):
    ResourceId: str


class DescribeWorkspaceAssociationsRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str
    AssociatedResourceTypes: Sequence[Literal["APPLICATION"]]


class DescribeWorkspaceBundlesRequestTypeDef(BaseValidatorModel):
    BundleIds: Optional[Sequence[str]] = None
    Owner: Optional[str] = None
    NextToken: Optional[str] = None


class DescribeWorkspaceDirectoriesFilterTypeDef(BaseValidatorModel):
    Name: DescribeWorkspaceDirectoriesFilterNameType
    Values: Sequence[str]


class DescribeWorkspaceImagePermissionsRequestTypeDef(BaseValidatorModel):
    ImageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ImagePermissionTypeDef(BaseValidatorModel):
    SharedAccountId: Optional[str] = None


class DescribeWorkspaceImagesRequestTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    ImageType: Optional[ImageTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeWorkspaceSnapshotsRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str


class SnapshotTypeDef(BaseValidatorModel):
    SnapshotTime: Optional[datetime] = None


class DescribeWorkspacesConnectionStatusRequestTypeDef(BaseValidatorModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None


class WorkspaceConnectionStatusTypeDef(BaseValidatorModel):
    WorkspaceId: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    ConnectionStateCheckTimestamp: Optional[datetime] = None
    LastKnownUserConnectionTimestamp: Optional[datetime] = None


class DescribeWorkspacesPoolSessionsRequestTypeDef(BaseValidatorModel):
    PoolId: str
    UserId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeWorkspacesPoolsFilterTypeDef(BaseValidatorModel):
    Name: Literal["PoolName"]
    Values: Sequence[str]
    Operator: DescribeWorkspacesPoolsFilterOperatorType


class DescribeWorkspacesRequestTypeDef(BaseValidatorModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    DirectoryId: Optional[str] = None
    UserName: Optional[str] = None
    BundleId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    WorkspaceName: Optional[str] = None


class DisassociateConnectionAliasRequestTypeDef(BaseValidatorModel):
    AliasId: str


class DisassociateIpGroupsRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    GroupIds: Sequence[str]


class DisassociateWorkspaceApplicationRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str
    ApplicationId: str


class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorCode: Optional[WorkspaceImageErrorDetailCodeType] = None
    ErrorMessage: Optional[str] = None


class FailedWorkspaceChangeRequestTypeDef(BaseValidatorModel):
    WorkspaceId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class GetAccountLinkRequestTypeDef(BaseValidatorModel):
    LinkId: Optional[str] = None
    LinkedAccountId: Optional[str] = None


class GlobalAcceleratorForDirectoryTypeDef(BaseValidatorModel):
    Mode: AGAModeForDirectoryEnumType
    PreferredProtocol: Optional[AGAPreferredProtocolForDirectoryType] = None


class GlobalAcceleratorForWorkSpaceTypeDef(BaseValidatorModel):
    Mode: AGAModeForWorkSpaceEnumType
    PreferredProtocol: Optional[AGAPreferredProtocolForWorkSpaceType] = None


class IDCConfigTypeDef(BaseValidatorModel):
    InstanceArn: Optional[str] = None
    ApplicationArn: Optional[str] = None


class ListAccountLinksRequestTypeDef(BaseValidatorModel):
    LinkStatusFilter: Optional[Sequence[AccountLinkStatusEnumType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAvailableManagementCidrRangesRequestTypeDef(BaseValidatorModel):
    ManagementCidrRangeConstraint: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MicrosoftEntraConfigTypeDef(BaseValidatorModel):
    TenantId: Optional[str] = None
    ApplicationConfigSecretArn: Optional[str] = None


class MigrateWorkspaceRequestTypeDef(BaseValidatorModel):
    SourceWorkspaceId: str
    BundleId: str


class ModificationStateTypeDef(BaseValidatorModel):
    Resource: Optional[ModificationResourceEnumType] = None
    State: Optional[ModificationStateEnumType] = None


class ModifyAccountRequestTypeDef(BaseValidatorModel):
    DedicatedTenancySupport: Optional[Literal["ENABLED"]] = None
    DedicatedTenancyManagementCidrRange: Optional[str] = None


class ModifyEndpointEncryptionModeRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    EndpointEncryptionMode: EndpointEncryptionModeType


class SamlPropertiesTypeDef(BaseValidatorModel):
    Status: Optional[SamlStatusEnumType] = None
    UserAccessUrl: Optional[str] = None
    RelayStateParameterName: Optional[str] = None


class SelfservicePermissionsTypeDef(BaseValidatorModel):
    RestartWorkspace: Optional[ReconnectEnumType] = None
    IncreaseVolumeSize: Optional[ReconnectEnumType] = None
    ChangeComputeType: Optional[ReconnectEnumType] = None
    SwitchRunningMode: Optional[ReconnectEnumType] = None
    RebuildWorkspace: Optional[ReconnectEnumType] = None


class WorkspaceAccessPropertiesTypeDef(BaseValidatorModel):
    DeviceTypeWindows: Optional[AccessPropertyValueType] = None
    DeviceTypeOsx: Optional[AccessPropertyValueType] = None
    DeviceTypeWeb: Optional[AccessPropertyValueType] = None
    DeviceTypeIos: Optional[AccessPropertyValueType] = None
    DeviceTypeAndroid: Optional[AccessPropertyValueType] = None
    DeviceTypeChromeOs: Optional[AccessPropertyValueType] = None
    DeviceTypeZeroClient: Optional[AccessPropertyValueType] = None
    DeviceTypeLinux: Optional[AccessPropertyValueType] = None
    DeviceTypeWorkSpacesThinClient: Optional[AccessPropertyValueType] = None


class WorkspaceCreationPropertiesTypeDef(BaseValidatorModel):
    EnableWorkDocs: Optional[bool] = None
    EnableInternetAccess: Optional[bool] = None
    DefaultOu: Optional[str] = None
    CustomSecurityGroupId: Optional[str] = None
    UserEnabledAsLocalAdministrator: Optional[bool] = None
    EnableMaintenanceMode: Optional[bool] = None
    InstanceIamRoleArn: Optional[str] = None


class ModifyWorkspaceStateRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str
    WorkspaceState: TargetWorkspaceStateType


class NetworkAccessConfigurationTypeDef(BaseValidatorModel):
    EniPrivateIpAddress: Optional[str] = None
    EniId: Optional[str] = None


class RebootRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str


class RebuildRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str


class RejectAccountLinkInvitationRequestTypeDef(BaseValidatorModel):
    LinkId: str
    ClientToken: Optional[str] = None


class RestoreWorkspaceRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str


class RevokeIpRulesRequestTypeDef(BaseValidatorModel):
    GroupId: str
    UserRules: Sequence[str]


class StandbyWorkspacesPropertiesTypeDef(BaseValidatorModel):
    StandbyWorkspaceId: Optional[str] = None
    DataReplication: Optional[DataReplicationType] = None
    RecoverySnapshotTime: Optional[datetime] = None


class StartRequestTypeDef(BaseValidatorModel):
    WorkspaceId: Optional[str] = None


class StartWorkspacesPoolRequestTypeDef(BaseValidatorModel):
    PoolId: str


class StopRequestTypeDef(BaseValidatorModel):
    WorkspaceId: Optional[str] = None


class StopWorkspacesPoolRequestTypeDef(BaseValidatorModel):
    PoolId: str


class StorageConnectorTypeDef(BaseValidatorModel):
    ConnectorType: Literal["HOME_FOLDER"]
    Status: StorageConnectorStatusEnumType


class UserSettingTypeDef(BaseValidatorModel):
    Action: UserSettingActionEnumType
    Permission: UserSettingPermissionEnumType
    MaximumLength: Optional[int] = None


class TerminateRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str


class TerminateWorkspacesPoolRequestTypeDef(BaseValidatorModel):
    PoolId: str


class TerminateWorkspacesPoolSessionRequestTypeDef(BaseValidatorModel):
    SessionId: str


class UpdateConnectClientAddInRequestTypeDef(BaseValidatorModel):
    AddInId: str
    ResourceId: str
    Name: Optional[str] = None
    URL: Optional[str] = None


class UpdateResultTypeDef(BaseValidatorModel):
    UpdateAvailable: Optional[bool] = None
    Description: Optional[str] = None


class UpdateWorkspaceBundleRequestTypeDef(BaseValidatorModel):
    BundleId: Optional[str] = None
    ImageId: Optional[str] = None


class UpdateWorkspaceImagePermissionRequestTypeDef(BaseValidatorModel):
    ImageId: str
    AllowCopyImage: bool
    SharedAccountId: str


class WorkspacesPoolErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[WorkspacesPoolErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class AcceptAccountLinkInvitationResultTypeDef(BaseValidatorModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateConnectionAliasResultTypeDef(BaseValidatorModel):
    ConnectionIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class CopyWorkspaceImageResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAccountLinkInvitationResultTypeDef(BaseValidatorModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConnectClientAddInResultTypeDef(BaseValidatorModel):
    AddInId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConnectionAliasResultTypeDef(BaseValidatorModel):
    AliasId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIpGroupResultTypeDef(BaseValidatorModel):
    GroupId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUpdatedWorkspaceImageResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteAccountLinkInvitationResultTypeDef(BaseValidatorModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountResultTypeDef(BaseValidatorModel):
    DedicatedTenancySupport: DedicatedTenancySupportResultEnumType
    DedicatedTenancyManagementCidrRange: str
    DedicatedTenancyAccountType: DedicatedTenancyAccountTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountLinkResultTypeDef(BaseValidatorModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImportWorkspaceImageResultTypeDef(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountLinksResultTypeDef(BaseValidatorModel):
    AccountLinks: List[AccountLinkTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAvailableManagementCidrRangesResultTypeDef(BaseValidatorModel):
    ManagementCidrRanges: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MigrateWorkspaceResultTypeDef(BaseValidatorModel):
    SourceWorkspaceId: str
    TargetWorkspaceId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterWorkspaceDirectoryResultTypeDef(BaseValidatorModel):
    DirectoryId: str
    State: WorkspaceDirectoryStateType
    ResponseMetadata: ResponseMetadataTypeDef


class RejectAccountLinkInvitationResultTypeDef(BaseValidatorModel):
    AccountLink: AccountLinkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountModificationsResultTypeDef(BaseValidatorModel):
    AccountModifications: List[AccountModificationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ApplicationResourceAssociationTypeDef(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[ApplicationAssociatedResourceTypeType] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None


class BundleResourceAssociationTypeDef(BaseValidatorModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal["APPLICATION"]] = None
    BundleId: Optional[str] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None


class ImageResourceAssociationTypeDef(BaseValidatorModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal["APPLICATION"]] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ImageId: Optional[str] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None


class WorkspaceResourceAssociationTypeDef(BaseValidatorModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal["APPLICATION"]] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReasonTypeDef] = None
    WorkspaceId: Optional[str] = None


class AuthorizeIpRulesRequestTypeDef(BaseValidatorModel):
    GroupId: str
    UserRules: Sequence[IpRuleItemTypeDef]


class UpdateRulesOfIpGroupRequestTypeDef(BaseValidatorModel):
    GroupId: str
    UserRules: Sequence[IpRuleItemTypeDef]


class WorkspacesIpGroupTypeDef(BaseValidatorModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None
    groupDesc: Optional[str] = None
    userRules: Optional[List[IpRuleItemTypeDef]] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class DefaultImportClientBrandingAttributesTypeDef(BaseValidatorModel):
    Logo: Optional[BlobTypeDef] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Mapping[str, str]] = None


class IosImportClientBrandingAttributesTypeDef(BaseValidatorModel):
    Logo: Optional[BlobTypeDef] = None
    Logo2x: Optional[BlobTypeDef] = None
    Logo3x: Optional[BlobTypeDef] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Mapping[str, str]] = None


class ModifyCertificateBasedAuthPropertiesRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthPropertiesTypeDef] = None
    PropertiesToDelete: Optional[ Sequence[Literal["CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN"]] ] = None


class ClientPropertiesResultTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ClientProperties: Optional[ClientPropertiesTypeDef] = None


class ModifyClientPropertiesRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    ClientProperties: ClientPropertiesTypeDef


class DescribeConnectClientAddInsResultTypeDef(BaseValidatorModel):
    AddIns: List[ConnectClientAddInTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ConnectionAliasTypeDef(BaseValidatorModel):
    ConnectionString: Optional[str] = None
    AliasId: Optional[str] = None
    State: Optional[ConnectionAliasStateType] = None
    OwnerAccountId: Optional[str] = None
    Associations: Optional[List[ConnectionAliasAssociationTypeDef]] = None


class DescribeConnectionAliasPermissionsResultTypeDef(BaseValidatorModel):
    AliasId: str
    ConnectionAliasPermissions: List[ConnectionAliasPermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateConnectionAliasPermissionRequestTypeDef(BaseValidatorModel):
    AliasId: str
    ConnectionAliasPermission: ConnectionAliasPermissionTypeDef


class CopyWorkspaceImageRequestTypeDef(BaseValidatorModel):
    Name: str
    SourceImageId: str
    SourceRegion: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateConnectionAliasRequestTypeDef(BaseValidatorModel):
    ConnectionString: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateIpGroupRequestTypeDef(BaseValidatorModel):
    GroupName: str
    GroupDesc: Optional[str] = None
    UserRules: Optional[Sequence[IpRuleItemTypeDef]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateTagsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    Tags: Sequence[TagTypeDef]


class CreateUpdatedWorkspaceImageRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    SourceImageId: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateWorkspaceImageRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    WorkspaceId: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class DescribeTagsResultTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ImportWorkspaceImageRequestTypeDef(BaseValidatorModel):
    Ec2ImageId: str
    IngestionProcess: WorkspaceImageIngestionProcessType
    ImageName: str
    ImageDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None
    Applications: Optional[Sequence[ApplicationType]] = None


class StandbyWorkspaceOutputTypeDef(BaseValidatorModel):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    DataReplication: Optional[DataReplicationType] = None


class StandbyWorkspaceTypeDef(BaseValidatorModel):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    DataReplication: Optional[DataReplicationType] = None


class OperatingSystemTypeDef(BaseValidatorModel):
    pass


class CreateWorkspaceImageResultTypeDef(BaseValidatorModel):
    ImageId: str
    Name: str
    Description: str
    OperatingSystem: OperatingSystemTypeDef
    State: WorkspaceImageStateType
    RequiredTenancy: WorkspaceImageRequiredTenancyType
    Created: datetime
    OwnerAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkspacesPoolRequestTypeDef(BaseValidatorModel):
    PoolName: str
    Description: str
    BundleId: str
    DirectoryId: str
    Capacity: CapacityTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None
    ApplicationSettings: Optional[ApplicationSettingsRequestTypeDef] = None
    TimeoutSettings: Optional[TimeoutSettingsTypeDef] = None


class UpdateWorkspacesPoolRequestTypeDef(BaseValidatorModel):
    PoolId: str
    Description: Optional[str] = None
    BundleId: Optional[str] = None
    DirectoryId: Optional[str] = None
    Capacity: Optional[CapacityTypeDef] = None
    ApplicationSettings: Optional[ApplicationSettingsRequestTypeDef] = None
    TimeoutSettings: Optional[TimeoutSettingsTypeDef] = None


class DescribeAccountModificationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeIpGroupsRequestPaginateTypeDef(BaseValidatorModel):
    GroupIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeWorkspaceBundlesRequestPaginateTypeDef(BaseValidatorModel):
    BundleIds: Optional[Sequence[str]] = None
    Owner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeWorkspaceImagesRequestPaginateTypeDef(BaseValidatorModel):
    ImageIds: Optional[Sequence[str]] = None
    ImageType: Optional[ImageTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeWorkspacesConnectionStatusRequestPaginateTypeDef(BaseValidatorModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeWorkspacesRequestPaginateTypeDef(BaseValidatorModel):
    WorkspaceIds: Optional[Sequence[str]] = None
    DirectoryId: Optional[str] = None
    UserName: Optional[str] = None
    BundleId: Optional[str] = None
    WorkspaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAccountLinksRequestPaginateTypeDef(BaseValidatorModel):
    LinkStatusFilter: Optional[Sequence[AccountLinkStatusEnumType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAvailableManagementCidrRangesRequestPaginateTypeDef(BaseValidatorModel):
    ManagementCidrRangeConstraint: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeApplicationsResultTypeDef(BaseValidatorModel):
    Applications: List[WorkSpaceApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeClientBrandingResultTypeDef(BaseValidatorModel):
    DeviceTypeWindows: DefaultClientBrandingAttributesTypeDef
    DeviceTypeOsx: DefaultClientBrandingAttributesTypeDef
    DeviceTypeAndroid: DefaultClientBrandingAttributesTypeDef
    DeviceTypeIos: IosClientBrandingAttributesTypeDef
    DeviceTypeLinux: DefaultClientBrandingAttributesTypeDef
    DeviceTypeWeb: DefaultClientBrandingAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImportClientBrandingResultTypeDef(BaseValidatorModel):
    DeviceTypeWindows: DefaultClientBrandingAttributesTypeDef
    DeviceTypeOsx: DefaultClientBrandingAttributesTypeDef
    DeviceTypeAndroid: DefaultClientBrandingAttributesTypeDef
    DeviceTypeIos: IosClientBrandingAttributesTypeDef
    DeviceTypeLinux: DefaultClientBrandingAttributesTypeDef
    DeviceTypeWeb: DefaultClientBrandingAttributesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkspaceDirectoriesRequestPaginateTypeDef(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    WorkspaceDirectoryNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    Filters: Optional[Sequence[DescribeWorkspaceDirectoriesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeWorkspaceDirectoriesRequestTypeDef(BaseValidatorModel):
    DirectoryIds: Optional[Sequence[str]] = None
    WorkspaceDirectoryNames: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[DescribeWorkspaceDirectoriesFilterTypeDef]] = None


class DescribeWorkspaceImagePermissionsResultTypeDef(BaseValidatorModel):
    ImageId: str
    ImagePermissions: List[ImagePermissionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeWorkspaceSnapshotsResultTypeDef(BaseValidatorModel):
    RebuildSnapshots: List[SnapshotTypeDef]
    RestoreSnapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkspacesConnectionStatusResultTypeDef(BaseValidatorModel):
    WorkspacesConnectionStatus: List[WorkspaceConnectionStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeWorkspacesPoolsRequestTypeDef(BaseValidatorModel):
    PoolIds: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[DescribeWorkspacesPoolsFilterTypeDef]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class RebootWorkspacesResultTypeDef(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RebuildWorkspacesResultTypeDef(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartWorkspacesResultTypeDef(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StopWorkspacesResultTypeDef(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TerminateWorkspacesResultTypeDef(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class WorkspacePropertiesOutputTypeDef(BaseValidatorModel):
    RunningMode: Optional[RunningModeType] = None
    RunningModeAutoStopTimeoutInMinutes: Optional[int] = None
    RootVolumeSizeGib: Optional[int] = None
    UserVolumeSizeGib: Optional[int] = None
    ComputeTypeName: Optional[ComputeType] = None
    Protocols: Optional[List[ProtocolType]] = None
    OperatingSystemName: Optional[OperatingSystemNameType] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForWorkSpaceTypeDef] = None


class WorkspacePropertiesTypeDef(BaseValidatorModel):
    RunningMode: Optional[RunningModeType] = None
    RunningModeAutoStopTimeoutInMinutes: Optional[int] = None
    RootVolumeSizeGib: Optional[int] = None
    UserVolumeSizeGib: Optional[int] = None
    ComputeTypeName: Optional[ComputeType] = None
    Protocols: Optional[Sequence[ProtocolType]] = None
    OperatingSystemName: Optional[OperatingSystemNameType] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForWorkSpaceTypeDef] = None


class RegisterWorkspaceDirectoryRequestTypeDef(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    EnableWorkDocs: Optional[bool] = None
    EnableSelfService: Optional[bool] = None
    Tenancy: Optional[TenancyType] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkspaceDirectoryName: Optional[str] = None
    WorkspaceDirectoryDescription: Optional[str] = None
    UserIdentityType: Optional[UserIdentityTypeType] = None
    IdcInstanceArn: Optional[str] = None
    MicrosoftEntraConfig: Optional[MicrosoftEntraConfigTypeDef] = None
    WorkspaceType: Optional[WorkspaceTypeType] = None
    ActiveDirectoryConfig: Optional[ActiveDirectoryConfigTypeDef] = None


class ModifySamlPropertiesRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    SamlProperties: Optional[SamlPropertiesTypeDef] = None
    PropertiesToDelete: Optional[Sequence[DeletableSamlPropertyType]] = None


class ModifySelfservicePermissionsRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    SelfservicePermissions: SelfservicePermissionsTypeDef


class ModifyWorkspaceAccessPropertiesRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    WorkspaceAccessProperties: WorkspaceAccessPropertiesTypeDef


class ModifyWorkspaceCreationPropertiesRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    WorkspaceCreationProperties: WorkspaceCreationPropertiesTypeDef


class WorkspacesPoolSessionTypeDef(BaseValidatorModel):
    SessionId: str
    PoolId: str
    UserId: str
    AuthenticationType: Optional[Literal["SAML"]] = None
    ConnectionState: Optional[SessionConnectionStateType] = None
    InstanceId: Optional[str] = None
    ExpirationTime: Optional[datetime] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfigurationTypeDef] = None
    StartTime: Optional[datetime] = None


class RebootWorkspacesRequestTypeDef(BaseValidatorModel):
    RebootWorkspaceRequests: Sequence[RebootRequestTypeDef]


class RebuildWorkspacesRequestTypeDef(BaseValidatorModel):
    RebuildWorkspaceRequests: Sequence[RebuildRequestTypeDef]


class StartWorkspacesRequestTypeDef(BaseValidatorModel):
    StartWorkspaceRequests: Sequence[StartRequestTypeDef]


class StopWorkspacesRequestTypeDef(BaseValidatorModel):
    StopWorkspaceRequests: Sequence[StopRequestTypeDef]


class StreamingPropertiesOutputTypeDef(BaseValidatorModel):
    StreamingExperiencePreferredProtocol: Optional[StreamingExperiencePreferredProtocolEnumType] = None
    UserSettings: Optional[List[UserSettingTypeDef]] = None
    StorageConnectors: Optional[List[StorageConnectorTypeDef]] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForDirectoryTypeDef] = None


class StreamingPropertiesTypeDef(BaseValidatorModel):
    StreamingExperiencePreferredProtocol: Optional[StreamingExperiencePreferredProtocolEnumType] = None
    UserSettings: Optional[Sequence[UserSettingTypeDef]] = None
    StorageConnectors: Optional[Sequence[StorageConnectorTypeDef]] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForDirectoryTypeDef] = None


class TerminateWorkspacesRequestTypeDef(BaseValidatorModel):
    TerminateWorkspaceRequests: Sequence[TerminateRequestTypeDef]


class WorkspaceImageTypeDef(BaseValidatorModel):
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


class WorkspacesPoolTypeDef(BaseValidatorModel):
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


class DescribeApplicationAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[ApplicationResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeBundleAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[BundleResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeImageAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[ImageResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AssociateWorkspaceApplicationResultTypeDef(BaseValidatorModel):
    Association: WorkspaceResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkspaceAssociationsResultTypeDef(BaseValidatorModel):
    Associations: List[WorkspaceResourceAssociationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateWorkspaceApplicationResultTypeDef(BaseValidatorModel):
    Association: WorkspaceResourceAssociationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WorkSpaceApplicationDeploymentTypeDef(BaseValidatorModel):
    Associations: Optional[List[WorkspaceResourceAssociationTypeDef]] = None


class DescribeIpGroupsResultTypeDef(BaseValidatorModel):
    Result: List[WorkspacesIpGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ImportClientBrandingRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    DeviceTypeWindows: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeOsx: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeAndroid: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeIos: Optional[IosImportClientBrandingAttributesTypeDef] = None
    DeviceTypeLinux: Optional[DefaultImportClientBrandingAttributesTypeDef] = None
    DeviceTypeWeb: Optional[DefaultImportClientBrandingAttributesTypeDef] = None


class DescribeClientPropertiesResultTypeDef(BaseValidatorModel):
    ClientPropertiesList: List[ClientPropertiesResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConnectionAliasesResultTypeDef(BaseValidatorModel):
    ConnectionAliases: List[ConnectionAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class FailedCreateStandbyWorkspacesRequestTypeDef(BaseValidatorModel):
    StandbyWorkspaceRequest: Optional[StandbyWorkspaceOutputTypeDef] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class WorkspaceBundleTypeDef(BaseValidatorModel):
    pass


class CreateWorkspaceBundleResultTypeDef(BaseValidatorModel):
    WorkspaceBundle: WorkspaceBundleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkspaceBundlesResultTypeDef(BaseValidatorModel):
    Bundles: List[WorkspaceBundleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class WorkspaceRequestOutputTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: Optional[str] = None
    UserVolumeEncryptionEnabled: Optional[bool] = None
    RootVolumeEncryptionEnabled: Optional[bool] = None
    WorkspaceProperties: Optional[WorkspacePropertiesOutputTypeDef] = None
    Tags: Optional[List[TagTypeDef]] = None
    WorkspaceName: Optional[str] = None


class RelatedWorkspacePropertiesTypeDef(BaseValidatorModel):
    pass


class WorkspaceTypeDef(BaseValidatorModel):
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


class DescribeWorkspacesPoolSessionsResultTypeDef(BaseValidatorModel):
    Sessions: List[WorkspacesPoolSessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class WorkspaceDirectoryTypeDef(BaseValidatorModel):
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
    EndpointEncryptionMode: Optional[EndpointEncryptionModeType] = None
    MicrosoftEntraConfig: Optional[MicrosoftEntraConfigTypeDef] = None
    WorkspaceDirectoryName: Optional[str] = None
    WorkspaceDirectoryDescription: Optional[str] = None
    UserIdentityType: Optional[UserIdentityTypeType] = None
    WorkspaceType: Optional[WorkspaceTypeType] = None
    IDCConfig: Optional[IDCConfigTypeDef] = None
    ActiveDirectoryConfig: Optional[ActiveDirectoryConfigTypeDef] = None
    StreamingProperties: Optional[StreamingPropertiesOutputTypeDef] = None
    ErrorMessage: Optional[str] = None


class DescribeWorkspaceImagesResultTypeDef(BaseValidatorModel):
    Images: List[WorkspaceImageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateWorkspacesPoolResultTypeDef(BaseValidatorModel):
    WorkspacesPool: WorkspacesPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkspacesPoolsResultTypeDef(BaseValidatorModel):
    WorkspacesPools: List[WorkspacesPoolTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateWorkspacesPoolResultTypeDef(BaseValidatorModel):
    WorkspacesPool: WorkspacesPoolTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeployWorkspaceApplicationsResultTypeDef(BaseValidatorModel):
    Deployment: WorkSpaceApplicationDeploymentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateStandbyWorkspacesResultTypeDef(BaseValidatorModel):
    FailedStandbyRequests: List[FailedCreateStandbyWorkspacesRequestTypeDef]
    PendingStandbyRequests: List[PendingCreateStandbyWorkspacesRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StandbyWorkspaceUnionTypeDef(BaseValidatorModel):
    pass


class CreateStandbyWorkspacesRequestTypeDef(BaseValidatorModel):
    PrimaryRegion: str
    StandbyWorkspaces: Sequence[StandbyWorkspaceUnionTypeDef]


class FailedCreateWorkspaceRequestTypeDef(BaseValidatorModel):
    WorkspaceRequest: Optional[WorkspaceRequestOutputTypeDef] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class DescribeWorkspacesResultTypeDef(BaseValidatorModel):
    Workspaces: List[WorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class WorkspacePropertiesUnionTypeDef(BaseValidatorModel):
    pass


class ModifyWorkspacePropertiesRequestTypeDef(BaseValidatorModel):
    WorkspaceId: str
    WorkspaceProperties: Optional[WorkspacePropertiesUnionTypeDef] = None
    DataReplication: Optional[DataReplicationType] = None


class WorkspaceRequestTypeDef(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: Optional[str] = None
    UserVolumeEncryptionEnabled: Optional[bool] = None
    RootVolumeEncryptionEnabled: Optional[bool] = None
    WorkspaceProperties: Optional[WorkspacePropertiesUnionTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    WorkspaceName: Optional[str] = None


class DescribeWorkspaceDirectoriesResultTypeDef(BaseValidatorModel):
    Directories: List[WorkspaceDirectoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class StreamingPropertiesUnionTypeDef(BaseValidatorModel):
    pass


class ModifyStreamingPropertiesRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    StreamingProperties: Optional[StreamingPropertiesUnionTypeDef] = None


class CreateWorkspacesResultTypeDef(BaseValidatorModel):
    FailedRequests: List[FailedCreateWorkspaceRequestTypeDef]
    PendingRequests: List[WorkspaceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class WorkspaceRequestUnionTypeDef(BaseValidatorModel):
    pass


class CreateWorkspacesRequestTypeDef(BaseValidatorModel):
    Workspaces: Sequence[WorkspaceRequestUnionTypeDef]


