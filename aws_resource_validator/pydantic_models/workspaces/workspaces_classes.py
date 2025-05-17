from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.workspaces.workspaces_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'accept_account_link_invitation' function.
class AcceptAccountLinkInvitationRequest(BaseValidatorModel):
    LinkId: str
    ClientToken: Optional[str] = None


class AccountLink(BaseValidatorModel):
    AccountLinkId: Optional[str] = None
    AccountLinkStatus: Optional[AccountLinkStatusEnumType] = None
    SourceAccountId: Optional[str] = None
    TargetAccountId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AccountModification(BaseValidatorModel):
    ModificationState: Optional[DedicatedTenancyModificationStateEnumType] = None
    DedicatedTenancySupport: Optional[DedicatedTenancySupportResultEnumType] = None
    DedicatedTenancyManagementCidrRange: Optional[str] = None
    StartTime: Optional[datetime] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ActiveDirectoryConfig(BaseValidatorModel):
    DomainName: str
    ServiceAccountSecretArn: str


class AssociationStateReason(BaseValidatorModel):
    ErrorCode: Optional[AssociationErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ApplicationSettingsRequest(BaseValidatorModel):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: Optional[str] = None


class ApplicationSettingsResponse(BaseValidatorModel):
    Status: ApplicationSettingsStatusEnumType
    SettingsGroup: Optional[str] = None
    S3BucketName: Optional[str] = None


# This class is the input for the 'associate_connection_alias' function.
class AssociateConnectionAliasRequest(BaseValidatorModel):
    AliasId: str
    ResourceId: str


class AssociateIpGroupsRequest(BaseValidatorModel):
    DirectoryId: str
    GroupIds: List[str]


# This class is the input for the 'associate_workspace_application' function.
class AssociateWorkspaceApplicationRequest(BaseValidatorModel):
    WorkspaceId: str
    ApplicationId: str


class IpRuleItem(BaseValidatorModel):
    ipRule: Optional[str] = None
    ruleDesc: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CapacityStatus(BaseValidatorModel):
    AvailableUserSessions: int
    DesiredUserSessions: int
    ActualUserSessions: int
    ActiveUserSessions: int


class Capacity(BaseValidatorModel):
    DesiredUserSessions: int


class CertificateBasedAuthProperties(BaseValidatorModel):
    Status: Optional[CertificateBasedAuthStatusEnumType] = None
    CertificateAuthorityArn: Optional[str] = None


class ClientProperties(BaseValidatorModel):
    ReconnectEnabled: Optional[ReconnectEnumType] = None
    LogUploadEnabled: Optional[LogUploadEnumType] = None


class ComputeType(BaseValidatorModel):
    Name: Optional[ComputeType] = None


class ConnectClientAddIn(BaseValidatorModel):
    AddInId: Optional[str] = None
    ResourceId: Optional[str] = None
    Name: Optional[str] = None
    URL: Optional[str] = None


class ConnectionAliasAssociation(BaseValidatorModel):
    AssociationStatus: Optional[AssociationStatusType] = None
    AssociatedAccountId: Optional[str] = None
    ResourceId: Optional[str] = None
    ConnectionIdentifier: Optional[str] = None


class ConnectionAliasPermission(BaseValidatorModel):
    SharedAccountId: str
    AllowAssociation: bool


class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


# This class is the input for the 'create_account_link_invitation' function.
class CreateAccountLinkInvitationRequest(BaseValidatorModel):
    TargetAccountId: str
    ClientToken: Optional[str] = None


# This class is the input for the 'create_connect_client_add_in' function.
class CreateConnectClientAddInRequest(BaseValidatorModel):
    ResourceId: str
    Name: str
    URL: str


class PendingCreateStandbyWorkspacesRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    DirectoryId: Optional[str] = None
    State: Optional[WorkspaceStateType] = None
    WorkspaceId: Optional[str] = None


class RootStorage(BaseValidatorModel):
    Capacity: str


class UserStorage(BaseValidatorModel):
    Capacity: str


class OperatingSystem(BaseValidatorModel):
    Type: Optional[OperatingSystemTypeType] = None


class TimeoutSettings(BaseValidatorModel):
    DisconnectTimeoutInSeconds: Optional[int] = None
    IdleDisconnectTimeoutInSeconds: Optional[int] = None
    MaxUserDurationInSeconds: Optional[int] = None


class DataReplicationSettings(BaseValidatorModel):
    DataReplication: Optional[DataReplicationType] = None
    RecoverySnapshotTime: Optional[datetime] = None


class DefaultClientBrandingAttributes(BaseValidatorModel):
    LogoUrl: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None


class DefaultWorkspaceCreationProperties(BaseValidatorModel):
    EnableWorkDocs: Optional[bool] = None
    EnableInternetAccess: Optional[bool] = None
    DefaultOu: Optional[str] = None
    CustomSecurityGroupId: Optional[str] = None
    UserEnabledAsLocalAdministrator: Optional[bool] = None
    EnableMaintenanceMode: Optional[bool] = None
    InstanceIamRoleArn: Optional[str] = None


# This class is the input for the 'delete_account_link_invitation' function.
class DeleteAccountLinkInvitationRequest(BaseValidatorModel):
    LinkId: str
    ClientToken: Optional[str] = None


class DeleteClientBrandingRequest(BaseValidatorModel):
    ResourceId: str
    Platforms: List[ClientDeviceTypeType]


class DeleteConnectClientAddInRequest(BaseValidatorModel):
    AddInId: str
    ResourceId: str


class DeleteConnectionAliasRequest(BaseValidatorModel):
    AliasId: str


class DeleteIpGroupRequest(BaseValidatorModel):
    GroupId: str


class DeleteTagsRequest(BaseValidatorModel):
    ResourceId: str
    TagKeys: List[str]


class DeleteWorkspaceBundleRequest(BaseValidatorModel):
    BundleId: Optional[str] = None


class DeleteWorkspaceImageRequest(BaseValidatorModel):
    ImageId: str


# This class is the input for the 'deploy_workspace_applications' function.
class DeployWorkspaceApplicationsRequest(BaseValidatorModel):
    WorkspaceId: str
    Force: Optional[bool] = None


class DeregisterWorkspaceDirectoryRequest(BaseValidatorModel):
    DirectoryId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_account_modifications' function.
class DescribeAccountModificationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


# This class is the input for the 'describe_application_associations' function.
class DescribeApplicationAssociationsRequest(BaseValidatorModel):
    ApplicationId: str
    AssociatedResourceTypes: List[ApplicationAssociatedResourceTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_applications' function.
class DescribeApplicationsRequest(BaseValidatorModel):
    ApplicationIds: Optional[List[str]] = None
    ComputeTypeNames: Optional[List[ComputeType]] = None
    LicenseType: Optional[WorkSpaceApplicationLicenseTypeType] = None
    OperatingSystemNames: Optional[List[OperatingSystemNameType]] = None
    Owner: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class WorkSpaceApplication(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    Created: Optional[datetime] = None
    Description: Optional[str] = None
    LicenseType: Optional[WorkSpaceApplicationLicenseTypeType] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    State: Optional[WorkSpaceApplicationStateType] = None
    SupportedComputeTypeNames: Optional[List[ComputeType]] = None
    SupportedOperatingSystemNames: Optional[List[OperatingSystemNameType]] = None


# This class is the input for the 'describe_bundle_associations' function.
class DescribeBundleAssociationsRequest(BaseValidatorModel):
    BundleId: str
    AssociatedResourceTypes: List[Literal['APPLICATION']]


# This class is the input for the 'describe_client_branding' function.
class DescribeClientBrandingRequest(BaseValidatorModel):
    ResourceId: str


class IosClientBrandingAttributes(BaseValidatorModel):
    LogoUrl: Optional[str] = None
    Logo2xUrl: Optional[str] = None
    Logo3xUrl: Optional[str] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None


# This class is the input for the 'describe_client_properties' function.
class DescribeClientPropertiesRequest(BaseValidatorModel):
    ResourceIds: List[str]


# This class is the input for the 'describe_connect_client_add_ins' function.
class DescribeConnectClientAddInsRequest(BaseValidatorModel):
    ResourceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_connection_alias_permissions' function.
class DescribeConnectionAliasPermissionsRequest(BaseValidatorModel):
    AliasId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_connection_aliases' function.
class DescribeConnectionAliasesRequest(BaseValidatorModel):
    AliasIds: Optional[List[str]] = None
    ResourceId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_image_associations' function.
class DescribeImageAssociationsRequest(BaseValidatorModel):
    ImageId: str
    AssociatedResourceTypes: List[Literal['APPLICATION']]


# This class is the input for the 'describe_ip_groups' function.
class DescribeIpGroupsRequest(BaseValidatorModel):
    GroupIds: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_tags' function.
class DescribeTagsRequest(BaseValidatorModel):
    ResourceId: str


# This class is the input for the 'describe_workspace_associations' function.
class DescribeWorkspaceAssociationsRequest(BaseValidatorModel):
    WorkspaceId: str
    AssociatedResourceTypes: List[Literal['APPLICATION']]


# This class is the input for the 'describe_workspace_bundles' function.
class DescribeWorkspaceBundlesRequest(BaseValidatorModel):
    BundleIds: Optional[List[str]] = None
    Owner: Optional[str] = None
    NextToken: Optional[str] = None


class DescribeWorkspaceDirectoriesFilter(BaseValidatorModel):
    Name: DescribeWorkspaceDirectoriesFilterNameType
    Values: List[str]


# This class is the input for the 'describe_workspace_image_permissions' function.
class DescribeWorkspaceImagePermissionsRequest(BaseValidatorModel):
    ImageId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ImagePermission(BaseValidatorModel):
    SharedAccountId: Optional[str] = None


# This class is the input for the 'describe_workspace_images' function.
class DescribeWorkspaceImagesRequest(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    ImageType: Optional[ImageTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_workspace_snapshots' function.
class DescribeWorkspaceSnapshotsRequest(BaseValidatorModel):
    WorkspaceId: str


class Snapshot(BaseValidatorModel):
    SnapshotTime: Optional[datetime] = None


# This class is the input for the 'describe_workspaces_connection_status' function.
class DescribeWorkspacesConnectionStatusRequest(BaseValidatorModel):
    WorkspaceIds: Optional[List[str]] = None
    NextToken: Optional[str] = None


class WorkspaceConnectionStatus(BaseValidatorModel):
    WorkspaceId: Optional[str] = None
    ConnectionState: Optional[ConnectionStateType] = None
    ConnectionStateCheckTimestamp: Optional[datetime] = None
    LastKnownUserConnectionTimestamp: Optional[datetime] = None


# This class is the input for the 'describe_workspaces_pool_sessions' function.
class DescribeWorkspacesPoolSessionsRequest(BaseValidatorModel):
    PoolId: str
    UserId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeWorkspacesPoolsFilter(BaseValidatorModel):
    Name: Literal['PoolName']
    Values: List[str]
    Operator: DescribeWorkspacesPoolsFilterOperatorType


# This class is the input for the 'describe_workspaces' function.
class DescribeWorkspacesRequest(BaseValidatorModel):
    WorkspaceIds: Optional[List[str]] = None
    DirectoryId: Optional[str] = None
    UserName: Optional[str] = None
    BundleId: Optional[str] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    WorkspaceName: Optional[str] = None


class DisassociateConnectionAliasRequest(BaseValidatorModel):
    AliasId: str


class DisassociateIpGroupsRequest(BaseValidatorModel):
    DirectoryId: str
    GroupIds: List[str]


# This class is the input for the 'disassociate_workspace_application' function.
class DisassociateWorkspaceApplicationRequest(BaseValidatorModel):
    WorkspaceId: str
    ApplicationId: str


class ErrorDetails(BaseValidatorModel):
    ErrorCode: Optional[WorkspaceImageErrorDetailCodeType] = None
    ErrorMessage: Optional[str] = None


class FailedWorkspaceChangeRequest(BaseValidatorModel):
    WorkspaceId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'get_account_link' function.
class GetAccountLinkRequest(BaseValidatorModel):
    LinkId: Optional[str] = None
    LinkedAccountId: Optional[str] = None


class GlobalAcceleratorForDirectory(BaseValidatorModel):
    Mode: AGAModeForDirectoryEnumType
    PreferredProtocol: Optional[AGAPreferredProtocolForDirectoryType] = None


class GlobalAcceleratorForWorkSpace(BaseValidatorModel):
    Mode: AGAModeForWorkSpaceEnumType
    PreferredProtocol: Optional[AGAPreferredProtocolForWorkSpaceType] = None


class IDCConfig(BaseValidatorModel):
    InstanceArn: Optional[str] = None
    ApplicationArn: Optional[str] = None


# This class is the input for the 'list_account_links' function.
class ListAccountLinksRequest(BaseValidatorModel):
    LinkStatusFilter: Optional[List[AccountLinkStatusEnumType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_available_management_cidr_ranges' function.
class ListAvailableManagementCidrRangesRequest(BaseValidatorModel):
    ManagementCidrRangeConstraint: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MicrosoftEntraConfig(BaseValidatorModel):
    TenantId: Optional[str] = None
    ApplicationConfigSecretArn: Optional[str] = None


# This class is the input for the 'migrate_workspace' function.
class MigrateWorkspaceRequest(BaseValidatorModel):
    SourceWorkspaceId: str
    BundleId: str


class ModificationState(BaseValidatorModel):
    Resource: Optional[ModificationResourceEnumType] = None
    State: Optional[ModificationStateEnumType] = None


class ModifyAccountRequest(BaseValidatorModel):
    DedicatedTenancySupport: Optional[Literal['ENABLED']] = None
    DedicatedTenancyManagementCidrRange: Optional[str] = None


class ModifyEndpointEncryptionModeRequest(BaseValidatorModel):
    DirectoryId: str
    EndpointEncryptionMode: EndpointEncryptionModeType


class SamlProperties(BaseValidatorModel):
    Status: Optional[SamlStatusEnumType] = None
    UserAccessUrl: Optional[str] = None
    RelayStateParameterName: Optional[str] = None


class SelfservicePermissions(BaseValidatorModel):
    RestartWorkspace: Optional[ReconnectEnumType] = None
    IncreaseVolumeSize: Optional[ReconnectEnumType] = None
    ChangeComputeType: Optional[ReconnectEnumType] = None
    SwitchRunningMode: Optional[ReconnectEnumType] = None
    RebuildWorkspace: Optional[ReconnectEnumType] = None


class WorkspaceAccessProperties(BaseValidatorModel):
    DeviceTypeWindows: Optional[AccessPropertyValueType] = None
    DeviceTypeOsx: Optional[AccessPropertyValueType] = None
    DeviceTypeWeb: Optional[AccessPropertyValueType] = None
    DeviceTypeIos: Optional[AccessPropertyValueType] = None
    DeviceTypeAndroid: Optional[AccessPropertyValueType] = None
    DeviceTypeChromeOs: Optional[AccessPropertyValueType] = None
    DeviceTypeZeroClient: Optional[AccessPropertyValueType] = None
    DeviceTypeLinux: Optional[AccessPropertyValueType] = None
    DeviceTypeWorkSpacesThinClient: Optional[AccessPropertyValueType] = None


class WorkspaceCreationProperties(BaseValidatorModel):
    EnableWorkDocs: Optional[bool] = None
    EnableInternetAccess: Optional[bool] = None
    DefaultOu: Optional[str] = None
    CustomSecurityGroupId: Optional[str] = None
    UserEnabledAsLocalAdministrator: Optional[bool] = None
    EnableMaintenanceMode: Optional[bool] = None
    InstanceIamRoleArn: Optional[str] = None


class ModifyWorkspaceStateRequest(BaseValidatorModel):
    WorkspaceId: str
    WorkspaceState: TargetWorkspaceStateType


class NetworkAccessConfiguration(BaseValidatorModel):
    EniPrivateIpAddress: Optional[str] = None
    EniId: Optional[str] = None


class RebootRequest(BaseValidatorModel):
    WorkspaceId: str


class RebuildRequest(BaseValidatorModel):
    WorkspaceId: str


# This class is the input for the 'reject_account_link_invitation' function.
class RejectAccountLinkInvitationRequest(BaseValidatorModel):
    LinkId: str
    ClientToken: Optional[str] = None


class RelatedWorkspaceProperties(BaseValidatorModel):
    WorkspaceId: Optional[str] = None
    Region: Optional[str] = None
    State: Optional[WorkspaceStateType] = None
    Type: Optional[StandbyWorkspaceRelationshipTypeType] = None


class RestoreWorkspaceRequest(BaseValidatorModel):
    WorkspaceId: str


class RevokeIpRulesRequest(BaseValidatorModel):
    GroupId: str
    UserRules: List[str]


class StandbyWorkspacesProperties(BaseValidatorModel):
    StandbyWorkspaceId: Optional[str] = None
    DataReplication: Optional[DataReplicationType] = None
    RecoverySnapshotTime: Optional[datetime] = None


class StartRequest(BaseValidatorModel):
    WorkspaceId: Optional[str] = None


class StartWorkspacesPoolRequest(BaseValidatorModel):
    PoolId: str


class StopRequest(BaseValidatorModel):
    WorkspaceId: Optional[str] = None


class StopWorkspacesPoolRequest(BaseValidatorModel):
    PoolId: str


class StorageConnector(BaseValidatorModel):
    ConnectorType: Literal['HOME_FOLDER']
    Status: StorageConnectorStatusEnumType


class UserSetting(BaseValidatorModel):
    Action: UserSettingActionEnumType
    Permission: UserSettingPermissionEnumType
    MaximumLength: Optional[int] = None


class TerminateRequest(BaseValidatorModel):
    WorkspaceId: str


class TerminateWorkspacesPoolRequest(BaseValidatorModel):
    PoolId: str


class TerminateWorkspacesPoolSessionRequest(BaseValidatorModel):
    SessionId: str


class UpdateConnectClientAddInRequest(BaseValidatorModel):
    AddInId: str
    ResourceId: str
    Name: Optional[str] = None
    URL: Optional[str] = None


class UpdateResult(BaseValidatorModel):
    UpdateAvailable: Optional[bool] = None
    Description: Optional[str] = None


class UpdateWorkspaceBundleRequest(BaseValidatorModel):
    BundleId: Optional[str] = None
    ImageId: Optional[str] = None


class UpdateWorkspaceImagePermissionRequest(BaseValidatorModel):
    ImageId: str
    AllowCopyImage: bool
    SharedAccountId: str


class WorkspacesPoolError(BaseValidatorModel):
    ErrorCode: Optional[WorkspacesPoolErrorCodeType] = None
    ErrorMessage: Optional[str] = None


# This class is the output for the 'accept_account_link_invitation' function.
class AcceptAccountLinkInvitationResult(BaseValidatorModel):
    AccountLink: AccountLink
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_connection_alias' function.
class AssociateConnectionAliasResult(BaseValidatorModel):
    ConnectionIdentifier: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_workspace_image' function.
class CopyWorkspaceImageResult(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_account_link_invitation' function.
class CreateAccountLinkInvitationResult(BaseValidatorModel):
    AccountLink: AccountLink
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_connect_client_add_in' function.
class CreateConnectClientAddInResult(BaseValidatorModel):
    AddInId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_connection_alias' function.
class CreateConnectionAliasResult(BaseValidatorModel):
    AliasId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ip_group' function.
class CreateIpGroupResult(BaseValidatorModel):
    GroupId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_updated_workspace_image' function.
class CreateUpdatedWorkspaceImageResult(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_account_link_invitation' function.
class DeleteAccountLinkInvitationResult(BaseValidatorModel):
    AccountLink: AccountLink
    ResponseMetadata: ResponseMetadata


class DescribeAccountResult(BaseValidatorModel):
    DedicatedTenancySupport: DedicatedTenancySupportResultEnumType
    DedicatedTenancyManagementCidrRange: str
    DedicatedTenancyAccountType: DedicatedTenancyAccountTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_account_link' function.
class GetAccountLinkResult(BaseValidatorModel):
    AccountLink: AccountLink
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_workspace_image' function.
class ImportWorkspaceImageResult(BaseValidatorModel):
    ImageId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_account_links' function.
class ListAccountLinksResult(BaseValidatorModel):
    AccountLinks: List[AccountLink]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_available_management_cidr_ranges' function.
class ListAvailableManagementCidrRangesResult(BaseValidatorModel):
    ManagementCidrRanges: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'migrate_workspace' function.
class MigrateWorkspaceResult(BaseValidatorModel):
    SourceWorkspaceId: str
    TargetWorkspaceId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_workspace_directory' function.
class RegisterWorkspaceDirectoryResult(BaseValidatorModel):
    DirectoryId: str
    State: WorkspaceDirectoryStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reject_account_link_invitation' function.
class RejectAccountLinkInvitationResult(BaseValidatorModel):
    AccountLink: AccountLink
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_account_modifications' function.
class DescribeAccountModificationsResult(BaseValidatorModel):
    AccountModifications: List[AccountModification]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ApplicationResourceAssociation(BaseValidatorModel):
    ApplicationId: Optional[str] = None
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[ApplicationAssociatedResourceTypeType] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReason] = None


class BundleResourceAssociation(BaseValidatorModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal['APPLICATION']] = None
    BundleId: Optional[str] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReason] = None


class ImageResourceAssociation(BaseValidatorModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal['APPLICATION']] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    ImageId: Optional[str] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReason] = None


class WorkspaceResourceAssociation(BaseValidatorModel):
    AssociatedResourceId: Optional[str] = None
    AssociatedResourceType: Optional[Literal['APPLICATION']] = None
    Created: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    State: Optional[AssociationStateType] = None
    StateReason: Optional[AssociationStateReason] = None
    WorkspaceId: Optional[str] = None


class AuthorizeIpRulesRequest(BaseValidatorModel):
    GroupId: str
    UserRules: List[IpRuleItem]


class UpdateRulesOfIpGroupRequest(BaseValidatorModel):
    GroupId: str
    UserRules: List[IpRuleItem]


class WorkspacesIpGroup(BaseValidatorModel):
    groupId: Optional[str] = None
    groupName: Optional[str] = None
    groupDesc: Optional[str] = None
    userRules: Optional[List[IpRuleItem]] = None


class DefaultImportClientBrandingAttributes(BaseValidatorModel):
    Logo: Optional[Blob] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None


class IosImportClientBrandingAttributes(BaseValidatorModel):
    Logo: Optional[Blob] = None
    Logo2x: Optional[Blob] = None
    Logo3x: Optional[Blob] = None
    SupportEmail: Optional[str] = None
    SupportLink: Optional[str] = None
    ForgotPasswordLink: Optional[str] = None
    LoginMessage: Optional[Dict[str, str]] = None


class ModifyCertificateBasedAuthPropertiesRequest(BaseValidatorModel):
    ResourceId: str
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthProperties] = None
    PropertiesToDelete: Optional[List[Literal['CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN']]] = None


class ClientPropertiesResult(BaseValidatorModel):
    ResourceId: Optional[str] = None
    ClientProperties: Optional[ClientProperties] = None


class ModifyClientPropertiesRequest(BaseValidatorModel):
    ResourceId: str
    ClientProperties: ClientProperties


# This class is the output for the 'describe_connect_client_add_ins' function.
class DescribeConnectClientAddInsResult(BaseValidatorModel):
    AddIns: List[ConnectClientAddIn]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ConnectionAlias(BaseValidatorModel):
    ConnectionString: Optional[str] = None
    AliasId: Optional[str] = None
    State: Optional[ConnectionAliasStateType] = None
    OwnerAccountId: Optional[str] = None
    Associations: Optional[List[ConnectionAliasAssociation]] = None


# This class is the output for the 'describe_connection_alias_permissions' function.
class DescribeConnectionAliasPermissionsResult(BaseValidatorModel):
    AliasId: str
    ConnectionAliasPermissions: List[ConnectionAliasPermission]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateConnectionAliasPermissionRequest(BaseValidatorModel):
    AliasId: str
    ConnectionAliasPermission: ConnectionAliasPermission


# This class is the input for the 'copy_workspace_image' function.
class CopyWorkspaceImageRequest(BaseValidatorModel):
    Name: str
    SourceImageId: str
    SourceRegion: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_connection_alias' function.
class CreateConnectionAliasRequest(BaseValidatorModel):
    ConnectionString: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_ip_group' function.
class CreateIpGroupRequest(BaseValidatorModel):
    GroupName: str
    GroupDesc: Optional[str] = None
    UserRules: Optional[List[IpRuleItem]] = None
    Tags: Optional[List[Tag]] = None


class CreateTagsRequest(BaseValidatorModel):
    ResourceId: str
    Tags: List[Tag]


# This class is the input for the 'create_updated_workspace_image' function.
class CreateUpdatedWorkspaceImageRequest(BaseValidatorModel):
    Name: str
    Description: str
    SourceImageId: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_workspace_image' function.
class CreateWorkspaceImageRequest(BaseValidatorModel):
    Name: str
    Description: str
    WorkspaceId: str
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'describe_tags' function.
class DescribeTagsResult(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'import_workspace_image' function.
class ImportWorkspaceImageRequest(BaseValidatorModel):
    Ec2ImageId: str
    IngestionProcess: WorkspaceImageIngestionProcessType
    ImageName: str
    ImageDescription: str
    Tags: Optional[List[Tag]] = None
    Applications: Optional[List[ApplicationType]] = None


class StandbyWorkspaceOutput(BaseValidatorModel):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DataReplication: Optional[DataReplicationType] = None


class StandbyWorkspace(BaseValidatorModel):
    PrimaryWorkspaceId: str
    DirectoryId: str
    VolumeEncryptionKey: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    DataReplication: Optional[DataReplicationType] = None


# This class is the input for the 'create_workspace_bundle' function.
class CreateWorkspaceBundleRequest(BaseValidatorModel):
    BundleName: str
    BundleDescription: str
    ImageId: str
    ComputeType: ComputeType
    UserStorage: UserStorage
    RootStorage: Optional[RootStorage] = None
    Tags: Optional[List[Tag]] = None


class WorkspaceBundle(BaseValidatorModel):
    BundleId: Optional[str] = None
    Name: Optional[str] = None
    Owner: Optional[str] = None
    Description: Optional[str] = None
    ImageId: Optional[str] = None
    RootStorage: Optional[RootStorage] = None
    UserStorage: Optional[UserStorage] = None
    ComputeType: Optional[ComputeType] = None
    LastUpdatedTime: Optional[datetime] = None
    CreationTime: Optional[datetime] = None
    State: Optional[WorkspaceBundleStateType] = None
    BundleType: Optional[BundleTypeType] = None


# This class is the output for the 'create_workspace_image' function.
class CreateWorkspaceImageResult(BaseValidatorModel):
    ImageId: str
    Name: str
    Description: str
    OperatingSystem: OperatingSystem
    State: WorkspaceImageStateType
    RequiredTenancy: WorkspaceImageRequiredTenancyType
    Created: datetime
    OwnerAccountId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_workspaces_pool' function.
class CreateWorkspacesPoolRequest(BaseValidatorModel):
    PoolName: str
    Description: str
    BundleId: str
    DirectoryId: str
    Capacity: Capacity
    Tags: Optional[List[Tag]] = None
    ApplicationSettings: Optional[ApplicationSettingsRequest] = None
    TimeoutSettings: Optional[TimeoutSettings] = None


# This class is the input for the 'update_workspaces_pool' function.
class UpdateWorkspacesPoolRequest(BaseValidatorModel):
    PoolId: str
    Description: Optional[str] = None
    BundleId: Optional[str] = None
    DirectoryId: Optional[str] = None
    Capacity: Optional[Capacity] = None
    ApplicationSettings: Optional[ApplicationSettingsRequest] = None
    TimeoutSettings: Optional[TimeoutSettings] = None


class DescribeAccountModificationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeIpGroupsRequestPaginate(BaseValidatorModel):
    GroupIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeWorkspaceBundlesRequestPaginate(BaseValidatorModel):
    BundleIds: Optional[List[str]] = None
    Owner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeWorkspaceImagesRequestPaginate(BaseValidatorModel):
    ImageIds: Optional[List[str]] = None
    ImageType: Optional[ImageTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeWorkspacesConnectionStatusRequestPaginate(BaseValidatorModel):
    WorkspaceIds: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeWorkspacesRequestPaginate(BaseValidatorModel):
    WorkspaceIds: Optional[List[str]] = None
    DirectoryId: Optional[str] = None
    UserName: Optional[str] = None
    BundleId: Optional[str] = None
    WorkspaceName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAccountLinksRequestPaginate(BaseValidatorModel):
    LinkStatusFilter: Optional[List[AccountLinkStatusEnumType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAvailableManagementCidrRangesRequestPaginate(BaseValidatorModel):
    ManagementCidrRangeConstraint: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_applications' function.
class DescribeApplicationsResult(BaseValidatorModel):
    Applications: List[WorkSpaceApplication]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_client_branding' function.
class DescribeClientBrandingResult(BaseValidatorModel):
    DeviceTypeWindows: DefaultClientBrandingAttributes
    DeviceTypeOsx: DefaultClientBrandingAttributes
    DeviceTypeAndroid: DefaultClientBrandingAttributes
    DeviceTypeIos: IosClientBrandingAttributes
    DeviceTypeLinux: DefaultClientBrandingAttributes
    DeviceTypeWeb: DefaultClientBrandingAttributes
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_client_branding' function.
class ImportClientBrandingResult(BaseValidatorModel):
    DeviceTypeWindows: DefaultClientBrandingAttributes
    DeviceTypeOsx: DefaultClientBrandingAttributes
    DeviceTypeAndroid: DefaultClientBrandingAttributes
    DeviceTypeIos: IosClientBrandingAttributes
    DeviceTypeLinux: DefaultClientBrandingAttributes
    DeviceTypeWeb: DefaultClientBrandingAttributes
    ResponseMetadata: ResponseMetadata


class DescribeWorkspaceDirectoriesRequestPaginate(BaseValidatorModel):
    DirectoryIds: Optional[List[str]] = None
    WorkspaceDirectoryNames: Optional[List[str]] = None
    Limit: Optional[int] = None
    Filters: Optional[List[DescribeWorkspaceDirectoriesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_workspace_directories' function.
class DescribeWorkspaceDirectoriesRequest(BaseValidatorModel):
    DirectoryIds: Optional[List[str]] = None
    WorkspaceDirectoryNames: Optional[List[str]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None
    Filters: Optional[List[DescribeWorkspaceDirectoriesFilter]] = None


# This class is the output for the 'describe_workspace_image_permissions' function.
class DescribeWorkspaceImagePermissionsResult(BaseValidatorModel):
    ImageId: str
    ImagePermissions: List[ImagePermission]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_workspace_snapshots' function.
class DescribeWorkspaceSnapshotsResult(BaseValidatorModel):
    RebuildSnapshots: List[Snapshot]
    RestoreSnapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_workspaces_connection_status' function.
class DescribeWorkspacesConnectionStatusResult(BaseValidatorModel):
    WorkspacesConnectionStatus: List[WorkspaceConnectionStatus]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'describe_workspaces_pools' function.
class DescribeWorkspacesPoolsRequest(BaseValidatorModel):
    PoolIds: Optional[List[str]] = None
    Filters: Optional[List[DescribeWorkspacesPoolsFilter]] = None
    Limit: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'reboot_workspaces' function.
class RebootWorkspacesResult(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequest]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rebuild_workspaces' function.
class RebuildWorkspacesResult(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequest]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_workspaces' function.
class StartWorkspacesResult(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequest]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_workspaces' function.
class StopWorkspacesResult(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequest]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'terminate_workspaces' function.
class TerminateWorkspacesResult(BaseValidatorModel):
    FailedRequests: List[FailedWorkspaceChangeRequest]
    ResponseMetadata: ResponseMetadata


class WorkspacePropertiesOutput(BaseValidatorModel):
    RunningMode: Optional[RunningModeType] = None
    RunningModeAutoStopTimeoutInMinutes: Optional[int] = None
    RootVolumeSizeGib: Optional[int] = None
    UserVolumeSizeGib: Optional[int] = None
    ComputeTypeName: Optional[ComputeType] = None
    Protocols: Optional[List[ProtocolType]] = None
    OperatingSystemName: Optional[OperatingSystemNameType] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForWorkSpace] = None


class WorkspaceProperties(BaseValidatorModel):
    RunningMode: Optional[RunningModeType] = None
    RunningModeAutoStopTimeoutInMinutes: Optional[int] = None
    RootVolumeSizeGib: Optional[int] = None
    UserVolumeSizeGib: Optional[int] = None
    ComputeTypeName: Optional[ComputeType] = None
    Protocols: Optional[List[ProtocolType]] = None
    OperatingSystemName: Optional[OperatingSystemNameType] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForWorkSpace] = None


# This class is the input for the 'register_workspace_directory' function.
class RegisterWorkspaceDirectoryRequest(BaseValidatorModel):
    DirectoryId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    EnableWorkDocs: Optional[bool] = None
    EnableSelfService: Optional[bool] = None
    Tenancy: Optional[TenancyType] = None
    Tags: Optional[List[Tag]] = None
    WorkspaceDirectoryName: Optional[str] = None
    WorkspaceDirectoryDescription: Optional[str] = None
    UserIdentityType: Optional[UserIdentityTypeType] = None
    IdcInstanceArn: Optional[str] = None
    MicrosoftEntraConfig: Optional[MicrosoftEntraConfig] = None
    WorkspaceType: Optional[WorkspaceTypeType] = None
    ActiveDirectoryConfig: Optional[ActiveDirectoryConfig] = None


class ModifySamlPropertiesRequest(BaseValidatorModel):
    ResourceId: str
    SamlProperties: Optional[SamlProperties] = None
    PropertiesToDelete: Optional[List[DeletableSamlPropertyType]] = None


class ModifySelfservicePermissionsRequest(BaseValidatorModel):
    ResourceId: str
    SelfservicePermissions: SelfservicePermissions


class ModifyWorkspaceAccessPropertiesRequest(BaseValidatorModel):
    ResourceId: str
    WorkspaceAccessProperties: WorkspaceAccessProperties


class ModifyWorkspaceCreationPropertiesRequest(BaseValidatorModel):
    ResourceId: str
    WorkspaceCreationProperties: WorkspaceCreationProperties


class WorkspacesPoolSession(BaseValidatorModel):
    SessionId: str
    PoolId: str
    UserId: str
    AuthenticationType: Optional[Literal['SAML']] = None
    ConnectionState: Optional[SessionConnectionStateType] = None
    InstanceId: Optional[str] = None
    ExpirationTime: Optional[datetime] = None
    NetworkAccessConfiguration: Optional[NetworkAccessConfiguration] = None
    StartTime: Optional[datetime] = None


# This class is the input for the 'reboot_workspaces' function.
class RebootWorkspacesRequest(BaseValidatorModel):
    RebootWorkspaceRequests: List[RebootRequest]


# This class is the input for the 'rebuild_workspaces' function.
class RebuildWorkspacesRequest(BaseValidatorModel):
    RebuildWorkspaceRequests: List[RebuildRequest]


# This class is the input for the 'start_workspaces' function.
class StartWorkspacesRequest(BaseValidatorModel):
    StartWorkspaceRequests: List[StartRequest]


# This class is the input for the 'stop_workspaces' function.
class StopWorkspacesRequest(BaseValidatorModel):
    StopWorkspaceRequests: List[StopRequest]


class StreamingPropertiesOutput(BaseValidatorModel):
    StreamingExperiencePreferredProtocol: Optional[StreamingExperiencePreferredProtocolEnumType] = None
    UserSettings: Optional[List[UserSetting]] = None
    StorageConnectors: Optional[List[StorageConnector]] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForDirectory] = None


class StreamingProperties(BaseValidatorModel):
    StreamingExperiencePreferredProtocol: Optional[StreamingExperiencePreferredProtocolEnumType] = None
    UserSettings: Optional[List[UserSetting]] = None
    StorageConnectors: Optional[List[StorageConnector]] = None
    GlobalAccelerator: Optional[GlobalAcceleratorForDirectory] = None


# This class is the input for the 'terminate_workspaces' function.
class TerminateWorkspacesRequest(BaseValidatorModel):
    TerminateWorkspaceRequests: List[TerminateRequest]


class WorkspaceImage(BaseValidatorModel):
    ImageId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    OperatingSystem: Optional[OperatingSystem] = None
    State: Optional[WorkspaceImageStateType] = None
    RequiredTenancy: Optional[WorkspaceImageRequiredTenancyType] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    Created: Optional[datetime] = None
    OwnerAccountId: Optional[str] = None
    Updates: Optional[UpdateResult] = None
    ErrorDetails: Optional[List[ErrorDetails]] = None


class WorkspacesPool(BaseValidatorModel):
    PoolId: str
    PoolArn: str
    CapacityStatus: CapacityStatus
    PoolName: str
    State: WorkspacesPoolStateType
    CreatedAt: datetime
    BundleId: str
    DirectoryId: str
    Description: Optional[str] = None
    Errors: Optional[List[WorkspacesPoolError]] = None
    ApplicationSettings: Optional[ApplicationSettingsResponse] = None
    TimeoutSettings: Optional[TimeoutSettings] = None


# This class is the output for the 'describe_application_associations' function.
class DescribeApplicationAssociationsResult(BaseValidatorModel):
    Associations: List[ApplicationResourceAssociation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_bundle_associations' function.
class DescribeBundleAssociationsResult(BaseValidatorModel):
    Associations: List[BundleResourceAssociation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_image_associations' function.
class DescribeImageAssociationsResult(BaseValidatorModel):
    Associations: List[ImageResourceAssociation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_workspace_application' function.
class AssociateWorkspaceApplicationResult(BaseValidatorModel):
    Association: WorkspaceResourceAssociation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_workspace_associations' function.
class DescribeWorkspaceAssociationsResult(BaseValidatorModel):
    Associations: List[WorkspaceResourceAssociation]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_workspace_application' function.
class DisassociateWorkspaceApplicationResult(BaseValidatorModel):
    Association: WorkspaceResourceAssociation
    ResponseMetadata: ResponseMetadata


class WorkSpaceApplicationDeployment(BaseValidatorModel):
    Associations: Optional[List[WorkspaceResourceAssociation]] = None


# This class is the output for the 'describe_ip_groups' function.
class DescribeIpGroupsResult(BaseValidatorModel):
    Result: List[WorkspacesIpGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'import_client_branding' function.
class ImportClientBrandingRequest(BaseValidatorModel):
    ResourceId: str
    DeviceTypeWindows: Optional[DefaultImportClientBrandingAttributes] = None
    DeviceTypeOsx: Optional[DefaultImportClientBrandingAttributes] = None
    DeviceTypeAndroid: Optional[DefaultImportClientBrandingAttributes] = None
    DeviceTypeIos: Optional[IosImportClientBrandingAttributes] = None
    DeviceTypeLinux: Optional[DefaultImportClientBrandingAttributes] = None
    DeviceTypeWeb: Optional[DefaultImportClientBrandingAttributes] = None


# This class is the output for the 'describe_client_properties' function.
class DescribeClientPropertiesResult(BaseValidatorModel):
    ClientPropertiesList: List[ClientPropertiesResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_connection_aliases' function.
class DescribeConnectionAliasesResult(BaseValidatorModel):
    ConnectionAliases: List[ConnectionAlias]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FailedCreateStandbyWorkspacesRequest(BaseValidatorModel):
    StandbyWorkspaceRequest: Optional[StandbyWorkspaceOutput] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

StandbyWorkspaceUnion = Union[StandbyWorkspace, StandbyWorkspaceOutput]


# This class is the output for the 'create_workspace_bundle' function.
class CreateWorkspaceBundleResult(BaseValidatorModel):
    WorkspaceBundle: WorkspaceBundle
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_workspace_bundles' function.
class DescribeWorkspaceBundlesResult(BaseValidatorModel):
    Bundles: List[WorkspaceBundle]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class WorkspaceRequestOutput(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: Optional[str] = None
    UserVolumeEncryptionEnabled: Optional[bool] = None
    RootVolumeEncryptionEnabled: Optional[bool] = None
    WorkspaceProperties: Optional[WorkspacePropertiesOutput] = None
    Tags: Optional[List[Tag]] = None
    WorkspaceName: Optional[str] = None


class Workspace(BaseValidatorModel):
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
    WorkspaceProperties: Optional[WorkspacePropertiesOutput] = None
    ModificationStates: Optional[List[ModificationState]] = None
    RelatedWorkspaces: Optional[List[RelatedWorkspaceProperties]] = None
    DataReplicationSettings: Optional[DataReplicationSettings] = None
    StandbyWorkspacesProperties: Optional[List[StandbyWorkspacesProperties]] = None

WorkspacePropertiesUnion = Union[WorkspaceProperties, WorkspacePropertiesOutput]


# This class is the output for the 'describe_workspaces_pool_sessions' function.
class DescribeWorkspacesPoolSessionsResult(BaseValidatorModel):
    Sessions: List[WorkspacesPoolSession]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class WorkspaceDirectory(BaseValidatorModel):
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
    WorkspaceCreationProperties: Optional[DefaultWorkspaceCreationProperties] = None
    ipGroupIds: Optional[List[str]] = None
    WorkspaceAccessProperties: Optional[WorkspaceAccessProperties] = None
    Tenancy: Optional[TenancyType] = None
    SelfservicePermissions: Optional[SelfservicePermissions] = None
    SamlProperties: Optional[SamlProperties] = None
    CertificateBasedAuthProperties: Optional[CertificateBasedAuthProperties] = None
    EndpointEncryptionMode: Optional[EndpointEncryptionModeType] = None
    MicrosoftEntraConfig: Optional[MicrosoftEntraConfig] = None
    WorkspaceDirectoryName: Optional[str] = None
    WorkspaceDirectoryDescription: Optional[str] = None
    UserIdentityType: Optional[UserIdentityTypeType] = None
    WorkspaceType: Optional[WorkspaceTypeType] = None
    IDCConfig: Optional[IDCConfig] = None
    ActiveDirectoryConfig: Optional[ActiveDirectoryConfig] = None
    StreamingProperties: Optional[StreamingPropertiesOutput] = None
    ErrorMessage: Optional[str] = None

StreamingPropertiesUnion = Union[StreamingProperties, StreamingPropertiesOutput]


# This class is the output for the 'describe_workspace_images' function.
class DescribeWorkspaceImagesResult(BaseValidatorModel):
    Images: List[WorkspaceImage]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_workspaces_pool' function.
class CreateWorkspacesPoolResult(BaseValidatorModel):
    WorkspacesPool: WorkspacesPool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_workspaces_pools' function.
class DescribeWorkspacesPoolsResult(BaseValidatorModel):
    WorkspacesPools: List[WorkspacesPool]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_workspaces_pool' function.
class UpdateWorkspacesPoolResult(BaseValidatorModel):
    WorkspacesPool: WorkspacesPool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deploy_workspace_applications' function.
class DeployWorkspaceApplicationsResult(BaseValidatorModel):
    Deployment: WorkSpaceApplicationDeployment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_standby_workspaces' function.
class CreateStandbyWorkspacesResult(BaseValidatorModel):
    FailedStandbyRequests: List[FailedCreateStandbyWorkspacesRequest]
    PendingStandbyRequests: List[PendingCreateStandbyWorkspacesRequest]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_standby_workspaces' function.
class CreateStandbyWorkspacesRequest(BaseValidatorModel):
    PrimaryRegion: str
    StandbyWorkspaces: List[StandbyWorkspaceUnion]


class FailedCreateWorkspaceRequest(BaseValidatorModel):
    WorkspaceRequest: Optional[WorkspaceRequestOutput] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


# This class is the output for the 'describe_workspaces' function.
class DescribeWorkspacesResult(BaseValidatorModel):
    Workspaces: List[Workspace]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyWorkspacePropertiesRequest(BaseValidatorModel):
    WorkspaceId: str
    WorkspaceProperties: Optional[WorkspacePropertiesUnion] = None
    DataReplication: Optional[DataReplicationType] = None


class WorkspaceRequest(BaseValidatorModel):
    DirectoryId: str
    UserName: str
    BundleId: str
    VolumeEncryptionKey: Optional[str] = None
    UserVolumeEncryptionEnabled: Optional[bool] = None
    RootVolumeEncryptionEnabled: Optional[bool] = None
    WorkspaceProperties: Optional[WorkspacePropertiesUnion] = None
    Tags: Optional[List[Tag]] = None
    WorkspaceName: Optional[str] = None


# This class is the output for the 'describe_workspace_directories' function.
class DescribeWorkspaceDirectoriesResult(BaseValidatorModel):
    Directories: List[WorkspaceDirectory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyStreamingPropertiesRequest(BaseValidatorModel):
    ResourceId: str
    StreamingProperties: Optional[StreamingPropertiesUnion] = None


# This class is the output for the 'create_workspaces' function.
class CreateWorkspacesResult(BaseValidatorModel):
    FailedRequests: List[FailedCreateWorkspaceRequest]
    PendingRequests: List[Workspace]
    ResponseMetadata: ResponseMetadata

WorkspaceRequestUnion = Union[WorkspaceRequest, WorkspaceRequestOutput]


# This class is the input for the 'create_workspaces' function.
class CreateWorkspacesRequest(BaseValidatorModel):
    Workspaces: List[WorkspaceRequestUnion]