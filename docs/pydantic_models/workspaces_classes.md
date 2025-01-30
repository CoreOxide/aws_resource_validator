# workspaces_classes

# AcceptAccountLinkInvitationRequestRequestTypeDef

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AcceptAccountLinkInvitationResultTypeDef

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccountLinkTypeDef

### AccountLinkId
- **Type**: typing.Optional[str]

### AccountLinkStatus
- **Type**: typing.Optional[typing.Literal['LINKED', 'LINKING_FAILED', 'LINK_NOT_FOUND', 'PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT', 'REJECTED']]

### SourceAccountId
- **Type**: typing.Optional[str]

### TargetAccountId
- **Type**: typing.Optional[str]


# AccountModificationTypeDef

### ModificationState
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'PENDING']]

### DedicatedTenancySupport
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### DedicatedTenancyManagementCidrRange
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# ActiveDirectoryConfigTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccountSecretArn
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationResourceAssociationTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### AssociatedResourceId
- **Type**: typing.Optional[str]

### AssociatedResourceType
- **Type**: typing.Optional[typing.Literal['BUNDLE', 'IMAGE', 'WORKSPACE']]

### Created
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'ERROR', 'INSTALLING', 'PENDING_INSTALL', 'PENDING_INSTALL_DEPLOYMENT', 'PENDING_UNINSTALL', 'PENDING_UNINSTALL_DEPLOYMENT', 'REMOVED', 'UNINSTALLING']]

### StateReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReasonTypeDef]


# ApplicationSettingsRequestTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### SettingsGroup
- **Type**: typing.Optional[str]


# ApplicationSettingsResponseTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### SettingsGroup
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]


# AssociateConnectionAliasRequestRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateConnectionAliasResultTypeDef

### ConnectionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateIpGroupsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociateWorkspaceApplicationRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWorkspaceApplicationResultTypeDef

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociationStateReasonTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DeploymentError.InternalServerError', 'DeploymentError.WorkspaceUnreachable', 'ValidationError.InsufficientDiskSpace', 'ValidationError.InsufficientMemory', 'ValidationError.UnsupportedOperatingSystem']]

### ErrorMessage
- **Type**: typing.Optional[str]


# AuthorizeIpRulesRequestRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItemTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BundleResourceAssociationTypeDef

### AssociatedResourceId
- **Type**: typing.Optional[str]

### AssociatedResourceType
- **Type**: typing.Optional[typing.Literal['APPLICATION']]

### BundleId
- **Type**: typing.Optional[str]

### Created
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'ERROR', 'INSTALLING', 'PENDING_INSTALL', 'PENDING_INSTALL_DEPLOYMENT', 'PENDING_UNINSTALL', 'PENDING_UNINSTALL_DEPLOYMENT', 'REMOVED', 'UNINSTALLING']]

### StateReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReasonTypeDef]


# CapacityStatusTypeDef

### AvailableUserSessions
- **Type**: <class 'int'>
- **Required**: Yes

### DesiredUserSessions
- **Type**: <class 'int'>
- **Required**: Yes

### ActualUserSessions
- **Type**: <class 'int'>
- **Required**: Yes

### ActiveUserSessions
- **Type**: <class 'int'>
- **Required**: Yes


# CapacityTypeDef

### DesiredUserSessions
- **Type**: <class 'int'>
- **Required**: Yes


# CertificateBasedAuthPropertiesTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]


# ClientPropertiesResultTypeDef

### ResourceId
- **Type**: typing.Optional[str]

### ClientProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ClientPropertiesTypeDef]


# ClientPropertiesTypeDef

### ReconnectEnabled
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### LogUploadEnabled
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ComputeTypeTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['GRAPHICS', 'GRAPHICSPRO', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G4DN', 'PERFORMANCE', 'POWER', 'POWERPRO', 'STANDARD', 'VALUE']]


# ConnectClientAddInTypeDef

### AddInId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### URL
- **Type**: typing.Optional[str]


# ConnectionAliasAssociationTypeDef

### AssociationStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED_WITH_OWNER_ACCOUNT', 'ASSOCIATED_WITH_SHARED_ACCOUNT', 'NOT_ASSOCIATED', 'PENDING_ASSOCIATION', 'PENDING_DISASSOCIATION']]

### AssociatedAccountId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ConnectionIdentifier
- **Type**: typing.Optional[str]


# ConnectionAliasPermissionTypeDef

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AllowAssociation
- **Type**: <class 'bool'>
- **Required**: Yes


# ConnectionAliasTypeDef

### ConnectionString
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'DELETING']]

### OwnerAccountId
- **Type**: typing.Optional[str]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAliasAssociationTypeDef]]


# CopyWorkspaceImageRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SourceImageId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]


# CopyWorkspaceImageResultTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccountLinkInvitationRequestRequestTypeDef

### TargetAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateAccountLinkInvitationResultTypeDef

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectClientAddInRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### URL
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectClientAddInResultTypeDef

### AddInId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConnectionAliasRequestRequestTypeDef

### ConnectionString
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]


# CreateConnectionAliasResultTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIpGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupDesc
- **Type**: typing.Optional[str]

### UserRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItemTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]


# CreateIpGroupResultTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStandbyWorkspacesRequestRequestTypeDef

### PrimaryRegion
- **Type**: <class 'str'>
- **Required**: Yes

### StandbyWorkspaces
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.workspaces_classes.StandbyWorkspaceTypeDef, aws_resource_validator.pydantic_models.workspaces_classes.StandbyWorkspaceOutputTypeDef]]
- **Required**: Yes


# CreateStandbyWorkspacesResultTypeDef

### FailedStandbyRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedCreateStandbyWorkspacesRequestTypeDef]
- **Required**: Yes

### PendingStandbyRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.PendingCreateStandbyWorkspacesRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTagsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]
- **Required**: Yes


# CreateUpdatedWorkspaceImageRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### SourceImageId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]


# CreateUpdatedWorkspaceImageResultTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspaceBundleRequestRequestTypeDef

### BundleName
- **Type**: <class 'str'>
- **Required**: Yes

### BundleDescription
- **Type**: <class 'str'>
- **Required**: Yes

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputeType
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ComputeTypeTypeDef'>
- **Required**: Yes

### UserStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.UserStorageTypeDef'>
- **Required**: Yes

### RootStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.RootStorageTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]


# CreateWorkspaceBundleResultTypeDef

### WorkspaceBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceBundleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspaceImageRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]


# CreateWorkspaceImageResultTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### OperatingSystem
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.OperatingSystemTypeDef'>
- **Required**: Yes

### State
- **Type**: typing.Literal['AVAILABLE', 'ERROR', 'PENDING']
- **Required**: Yes

### RequiredTenancy
- **Type**: typing.Literal['DEDICATED', 'DEFAULT']
- **Required**: Yes

### Created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspacesPoolRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Capacity
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.CapacityTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationSettingsRequestTypeDef]

### TimeoutSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.TimeoutSettingsTypeDef]


# CreateWorkspacesPoolResultTypeDef

### WorkspacesPool
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPoolTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspacesRequestRequestTypeDef

### Workspaces
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceRequestTypeDef, aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceRequestOutputTypeDef]]
- **Required**: Yes


# CreateWorkspacesResultTypeDef

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedCreateWorkspaceRequestTypeDef]
- **Required**: Yes

### PendingRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataReplicationSettingsTypeDef

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]

### RecoverySnapshotTime
- **Type**: typing.Optional[datetime.datetime]


# DefaultClientBrandingAttributesTypeDef

### LogoUrl
- **Type**: typing.Optional[str]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportLink
- **Type**: typing.Optional[str]

### ForgotPasswordLink
- **Type**: typing.Optional[str]

### LoginMessage
- **Type**: typing.Optional[typing.Dict[str, str]]


# DefaultImportClientBrandingAttributesTypeDef

### Logo
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportLink
- **Type**: typing.Optional[str]

### ForgotPasswordLink
- **Type**: typing.Optional[str]

### LoginMessage
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DefaultWorkspaceCreationPropertiesTypeDef

### EnableWorkDocs
- **Type**: typing.Optional[bool]

### EnableInternetAccess
- **Type**: typing.Optional[bool]

### DefaultOu
- **Type**: typing.Optional[str]

### CustomSecurityGroupId
- **Type**: typing.Optional[str]

### UserEnabledAsLocalAdministrator
- **Type**: typing.Optional[bool]

### EnableMaintenanceMode
- **Type**: typing.Optional[bool]

### InstanceIamRoleArn
- **Type**: typing.Optional[str]


# DeleteAccountLinkInvitationRequestRequestTypeDef

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteAccountLinkInvitationResultTypeDef

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteClientBrandingRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Platforms
- **Type**: typing.Sequence[typing.Literal['DeviceTypeAndroid', 'DeviceTypeIos', 'DeviceTypeLinux', 'DeviceTypeOsx', 'DeviceTypeWeb', 'DeviceTypeWindows']]
- **Required**: Yes


# DeleteConnectClientAddInRequestRequestTypeDef

### AddInId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionAliasRequestRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIpGroupRequestRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteWorkspaceBundleRequestRequestTypeDef

### BundleId
- **Type**: typing.Optional[str]


# DeleteWorkspaceImageRequestRequestTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes


# DeployWorkspaceApplicationsRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# DeployWorkspaceApplicationsResultTypeDef

### Deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkSpaceApplicationDeploymentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterWorkspaceDirectoryRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountModificationsRequestDescribeAccountModificationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# DescribeAccountModificationsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountModificationsResultTypeDef

### AccountModifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.AccountModificationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountResultTypeDef

### DedicatedTenancySupport
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DedicatedTenancyManagementCidrRange
- **Type**: <class 'str'>
- **Required**: Yes

### DedicatedTenancyAccountType
- **Type**: typing.Literal['SOURCE_ACCOUNT', 'TARGET_ACCOUNT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationAssociationsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceTypes
- **Type**: typing.Sequence[typing.Literal['BUNDLE', 'IMAGE', 'WORKSPACE']]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationAssociationsResultTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationResourceAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationsRequestRequestTypeDef

### ApplicationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ComputeTypeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['GRAPHICS', 'GRAPHICSPRO', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G4DN', 'PERFORMANCE', 'POWER', 'POWERPRO', 'STANDARD', 'VALUE']]]

### LicenseType
- **Type**: typing.Optional[typing.Literal['LICENSED', 'UNLICENSED']]

### OperatingSystemNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]]

### Owner
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationsResultTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkSpaceApplicationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBundleAssociationsRequestRequestTypeDef

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceTypes
- **Type**: typing.Sequence[typing.Literal['APPLICATION']]
- **Required**: Yes


# DescribeBundleAssociationsResultTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.BundleResourceAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClientBrandingRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClientBrandingResultTypeDef

### DeviceTypeWindows
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeOsx
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeAndroid
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeIos
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.IosClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeLinux
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeWeb
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClientPropertiesRequestRequestTypeDef

### ResourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeClientPropertiesResultTypeDef

### ClientPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ClientPropertiesResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeConnectClientAddInsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeConnectClientAddInsResultTypeDef

### AddIns
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectClientAddInTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConnectionAliasPermissionsRequestRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeConnectionAliasPermissionsResultTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionAliasPermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAliasPermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConnectionAliasesRequestRequestTypeDef

### AliasIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConnectionAliasesResultTypeDef

### ConnectionAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeImageAssociationsRequestRequestTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceTypes
- **Type**: typing.Sequence[typing.Literal['APPLICATION']]
- **Required**: Yes


# DescribeImageAssociationsResultTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ImageResourceAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIpGroupsRequestDescribeIpGroupsPaginateTypeDef

### GroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# DescribeIpGroupsRequestRequestTypeDef

### GroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeIpGroupsResultTypeDef

### Result
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesIpGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTagsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTagsResultTypeDef

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkspaceAssociationsRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceTypes
- **Type**: typing.Sequence[typing.Literal['APPLICATION']]
- **Required**: Yes


# DescribeWorkspaceAssociationsResultTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkspaceBundlesRequestDescribeWorkspaceBundlesPaginateTypeDef

### BundleIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Owner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# DescribeWorkspaceBundlesRequestRequestTypeDef

### BundleIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Owner
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceBundlesResultTypeDef

### Bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceBundleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceDirectoriesRequestDescribeWorkspaceDirectoriesPaginateTypeDef

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WorkspaceDirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# DescribeWorkspaceDirectoriesRequestRequestTypeDef

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WorkspaceDirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceDirectoriesResultTypeDef

### Directories
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceDirectoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceImagePermissionsRequestRequestTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeWorkspaceImagePermissionsResultTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ImagePermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ImagePermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceImagesRequestDescribeWorkspaceImagesPaginateTypeDef

### ImageIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ImageType
- **Type**: typing.Optional[typing.Literal['OWNED', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# DescribeWorkspaceImagesRequestRequestTypeDef

### ImageIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ImageType
- **Type**: typing.Optional[typing.Literal['OWNED', 'SHARED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeWorkspaceImagesResultTypeDef

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceImageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceSnapshotsRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceSnapshotsResultTypeDef

### RebuildSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.SnapshotTypeDef]
- **Required**: Yes

### RestoreSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkspacesConnectionStatusRequestDescribeWorkspacesConnectionStatusPaginateTypeDef

### WorkspaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# DescribeWorkspacesConnectionStatusRequestRequestTypeDef

### WorkspaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesConnectionStatusResultTypeDef

### WorkspacesConnectionStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceConnectionStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolSessionsRequestRequestTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolSessionsResultTypeDef

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPoolSessionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolsFilterTypeDef

### Name
- **Type**: typing.Literal['PoolName']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'NOTCONTAINS', 'NOTEQUALS']
- **Required**: Yes


# DescribeWorkspacesPoolsRequestRequestTypeDef

### PoolIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.DescribeWorkspacesPoolsFilterTypeDef]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolsResultTypeDef

### WorkspacesPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPoolTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesRequestDescribeWorkspacesPaginateTypeDef

### WorkspaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DirectoryId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### BundleId
- **Type**: typing.Optional[str]

### WorkspaceName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# DescribeWorkspacesRequestRequestTypeDef

### WorkspaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### DirectoryId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### BundleId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### WorkspaceName
- **Type**: typing.Optional[str]


# DescribeWorkspacesResultTypeDef

### Workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateConnectionAliasRequestRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIpGroupsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociateWorkspaceApplicationRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWorkspaceApplicationResultTypeDef

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ErrorDetailsTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AdditionalDrivesAttached', 'AntiVirusInstalled', 'AutoLogonEnabled', 'AutoMountDisabled', 'AzureDomainJoined', 'DHCPDisabled', 'DiskFreeSpace', 'DiskSizeExceeded', 'DomainJoined', 'FirewallEnabled', 'InPlaceUpgrade', 'IncompatiblePartitioning', 'MultipleBootPartition', 'OSNotSupported', 'OfficeInstalled', 'OutdatedPowershellVersion', 'PCoIPAgentInstalled', 'PendingReboot', 'RealTimeUniversalDisabled', 'Requires64BitOS', 'UEFINotSupported', 'VMWareToolsInstalled', 'WindowsUpdatesEnabled', 'WorkspacesBYOLAccountDisabled', 'WorkspacesBYOLAccountNotFound', 'ZeroRearmCount']]

### ErrorMessage
- **Type**: typing.Optional[str]


# FailedCreateStandbyWorkspacesRequestTypeDef

### StandbyWorkspaceRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.StandbyWorkspaceOutputTypeDef]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FailedCreateWorkspaceRequestTypeDef

### WorkspaceRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceRequestOutputTypeDef]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FailedWorkspaceChangeRequestTypeDef

### WorkspaceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetAccountLinkRequestRequestTypeDef

### LinkId
- **Type**: typing.Optional[str]

### LinkedAccountId
- **Type**: typing.Optional[str]


# GetAccountLinkResultTypeDef

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImagePermissionTypeDef

### SharedAccountId
- **Type**: typing.Optional[str]


# ImageResourceAssociationTypeDef

### AssociatedResourceId
- **Type**: typing.Optional[str]

### AssociatedResourceType
- **Type**: typing.Optional[typing.Literal['APPLICATION']]

### Created
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ImageId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'ERROR', 'INSTALLING', 'PENDING_INSTALL', 'PENDING_INSTALL_DEPLOYMENT', 'PENDING_UNINSTALL', 'PENDING_UNINSTALL_DEPLOYMENT', 'REMOVED', 'UNINSTALLING']]

### StateReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReasonTypeDef]


# ImportClientBrandingRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceTypeWindows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributesTypeDef]

### DeviceTypeOsx
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributesTypeDef]

### DeviceTypeAndroid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributesTypeDef]

### DeviceTypeIos
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.IosImportClientBrandingAttributesTypeDef]

### DeviceTypeLinux
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributesTypeDef]

### DeviceTypeWeb
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributesTypeDef]


# ImportClientBrandingResultTypeDef

### DeviceTypeWindows
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeOsx
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeAndroid
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeIos
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.IosClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeLinux
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### DeviceTypeWeb
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportWorkspaceImageRequestRequestTypeDef

### Ec2ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionProcess
- **Type**: typing.Literal['BYOL_GRAPHICS', 'BYOL_GRAPHICSPRO', 'BYOL_GRAPHICS_G4DN', 'BYOL_GRAPHICS_G4DN_BYOP', 'BYOL_REGULAR', 'BYOL_REGULAR_BYOP', 'BYOL_REGULAR_WSP']
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]

### Applications
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Microsoft_Office_2016', 'Microsoft_Office_2019']]]


# ImportWorkspaceImageResultTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IosClientBrandingAttributesTypeDef

### LogoUrl
- **Type**: typing.Optional[str]

### Logo2xUrl
- **Type**: typing.Optional[str]

### Logo3xUrl
- **Type**: typing.Optional[str]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportLink
- **Type**: typing.Optional[str]

### ForgotPasswordLink
- **Type**: typing.Optional[str]

### LoginMessage
- **Type**: typing.Optional[typing.Dict[str, str]]


# IosImportClientBrandingAttributesTypeDef

### Logo
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### Logo2x
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### Logo3x
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportLink
- **Type**: typing.Optional[str]

### ForgotPasswordLink
- **Type**: typing.Optional[str]

### LoginMessage
- **Type**: typing.Optional[typing.Mapping[str, str]]


# IpRuleItemTypeDef

### ipRule
- **Type**: typing.Optional[str]

### ruleDesc
- **Type**: typing.Optional[str]


# ListAccountLinksRequestListAccountLinksPaginateTypeDef

### LinkStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LINKED', 'LINKING_FAILED', 'LINK_NOT_FOUND', 'PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT', 'REJECTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfigTypeDef]


# ListAccountLinksRequestRequestTypeDef

### LinkStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LINKED', 'LINKING_FAILED', 'LINK_NOT_FOUND', 'PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT', 'REJECTED']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountLinksResultTypeDef

### AccountLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.AccountLinkTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAvailableManagementCidrRangesRequestRequestTypeDef

### ManagementCidrRangeConstraint
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAvailableManagementCidrRangesResultTypeDef

### ManagementCidrRanges
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MigrateWorkspaceRequestRequestTypeDef

### SourceWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes


# MigrateWorkspaceResultTypeDef

### SourceWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModificationStateTypeDef

### Resource
- **Type**: typing.Optional[typing.Literal['COMPUTE_TYPE', 'ROOT_VOLUME', 'USER_VOLUME']]

### State
- **Type**: typing.Optional[typing.Literal['UPDATE_INITIATED', 'UPDATE_IN_PROGRESS']]


# ModifyAccountRequestRequestTypeDef

### DedicatedTenancySupport
- **Type**: typing.Optional[typing.Literal['ENABLED']]

### DedicatedTenancyManagementCidrRange
- **Type**: typing.Optional[str]


# ModifyCertificateBasedAuthPropertiesRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateBasedAuthProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.CertificateBasedAuthPropertiesTypeDef]

### PropertiesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN']]]


# ModifyClientPropertiesRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ClientPropertiesTypeDef'>
- **Required**: Yes


# ModifySamlPropertiesRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### SamlProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.SamlPropertiesTypeDef]

### PropertiesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME', 'SAML_PROPERTIES_USER_ACCESS_URL']]]


# ModifySelfservicePermissionsRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### SelfservicePermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.SelfservicePermissionsTypeDef'>
- **Required**: Yes


# ModifyStreamingPropertiesRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.StreamingPropertiesTypeDef]


# ModifyWorkspaceAccessPropertiesRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceAccessProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceAccessPropertiesTypeDef'>
- **Required**: Yes


# ModifyWorkspaceCreationPropertiesRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceCreationProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceCreationPropertiesTypeDef'>
- **Required**: Yes


# ModifyWorkspacePropertiesRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesTypeDef]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]


# ModifyWorkspaceStateRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceState
- **Type**: typing.Literal['ADMIN_MAINTENANCE', 'AVAILABLE']
- **Required**: Yes


# NetworkAccessConfigurationTypeDef

### EniPrivateIpAddress
- **Type**: typing.Optional[str]

### EniId
- **Type**: typing.Optional[str]


# OperatingSystemTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingCreateStandbyWorkspacesRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ADMIN_MAINTENANCE', 'AVAILABLE', 'ERROR', 'IMPAIRED', 'MAINTENANCE', 'PENDING', 'REBOOTING', 'REBUILDING', 'RESTORING', 'STARTING', 'STOPPED', 'STOPPING', 'SUSPENDED', 'TERMINATED', 'TERMINATING', 'UNHEALTHY', 'UPDATING']]

### WorkspaceId
- **Type**: typing.Optional[str]


# RebootRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# RebootWorkspacesRequestRequestTypeDef

### RebootWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.RebootRequestTypeDef]
- **Required**: Yes


# RebootWorkspacesResultTypeDef

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RebuildRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# RebuildWorkspacesRequestRequestTypeDef

### RebuildWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.RebuildRequestTypeDef]
- **Required**: Yes


# RebuildWorkspacesResultTypeDef

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterWorkspaceDirectoryRequestRequestTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### EnableWorkDocs
- **Type**: typing.Optional[bool]

### EnableSelfService
- **Type**: typing.Optional[bool]

### Tenancy
- **Type**: typing.Optional[typing.Literal['DEDICATED', 'SHARED']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]

### WorkspaceDirectoryName
- **Type**: typing.Optional[str]

### WorkspaceDirectoryDescription
- **Type**: typing.Optional[str]

### UserIdentityType
- **Type**: typing.Optional[typing.Literal['AWS_DIRECTORY_SERVICE', 'CUSTOMER_MANAGED']]

### WorkspaceType
- **Type**: typing.Optional[typing.Literal['PERSONAL', 'POOLS']]

### ActiveDirectoryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ActiveDirectoryConfigTypeDef]


# RegisterWorkspaceDirectoryResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DEREGISTERED', 'DEREGISTERING', 'ERROR', 'REGISTERED', 'REGISTERING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RejectAccountLinkInvitationRequestRequestTypeDef

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# RejectAccountLinkInvitationResultTypeDef

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLinkTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RelatedWorkspacePropertiesTypeDef

### WorkspaceId
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ADMIN_MAINTENANCE', 'AVAILABLE', 'ERROR', 'IMPAIRED', 'MAINTENANCE', 'PENDING', 'REBOOTING', 'REBUILDING', 'RESTORING', 'STARTING', 'STOPPED', 'STOPPING', 'SUSPENDED', 'TERMINATED', 'TERMINATING', 'UNHEALTHY', 'UPDATING']]

### Type
- **Type**: typing.Optional[typing.Literal['PRIMARY', 'STANDBY']]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RestoreWorkspaceRequestRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeIpRulesRequestRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserRules
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RootStorageTypeDef

### Capacity
- **Type**: <class 'str'>
- **Required**: Yes


# SamlPropertiesTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK']]

### UserAccessUrl
- **Type**: typing.Optional[str]

### RelayStateParameterName
- **Type**: typing.Optional[str]


# SelfservicePermissionsTypeDef

### RestartWorkspace
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### IncreaseVolumeSize
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### ChangeComputeType
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### SwitchRunningMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### RebuildWorkspace
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# SnapshotTypeDef

### SnapshotTime
- **Type**: typing.Optional[datetime.datetime]


# StandbyWorkspaceOutputTypeDef

### PrimaryWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeEncryptionKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]


# StandbyWorkspaceTypeDef

### PrimaryWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeEncryptionKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]


# StandbyWorkspacesPropertiesTypeDef

### StandbyWorkspaceId
- **Type**: typing.Optional[str]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]

### RecoverySnapshotTime
- **Type**: typing.Optional[datetime.datetime]


# StartRequestTypeDef

### WorkspaceId
- **Type**: typing.Optional[str]


# StartWorkspacesPoolRequestRequestTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# StartWorkspacesRequestRequestTypeDef

### StartWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.StartRequestTypeDef]
- **Required**: Yes


# StartWorkspacesResultTypeDef

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopRequestTypeDef

### WorkspaceId
- **Type**: typing.Optional[str]


# StopWorkspacesPoolRequestRequestTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# StopWorkspacesRequestRequestTypeDef

### StopWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.StopRequestTypeDef]
- **Required**: Yes


# StopWorkspacesResultTypeDef

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StorageConnectorTypeDef

### ConnectorType
- **Type**: typing.Literal['HOME_FOLDER']
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# StreamingPropertiesExtraOutputTypeDef

### StreamingExperiencePreferredProtocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### UserSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.UserSettingTypeDef]]

### StorageConnectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.StorageConnectorTypeDef]]


# StreamingPropertiesOutputTypeDef

### StreamingExperiencePreferredProtocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### UserSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.UserSettingTypeDef]]

### StorageConnectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.StorageConnectorTypeDef]]


# StreamingPropertiesTypeDef

### StreamingExperiencePreferredProtocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### UserSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.UserSettingTypeDef]]

### StorageConnectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.StorageConnectorTypeDef]]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TerminateRequestTypeDef

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkspacesPoolRequestRequestTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkspacesPoolSessionRequestRequestTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkspacesRequestRequestTypeDef

### TerminateWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TerminateRequestTypeDef]
- **Required**: Yes


# TerminateWorkspacesResultTypeDef

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequestTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TimeoutSettingsTypeDef

### DisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### MaxUserDurationInSeconds
- **Type**: typing.Optional[int]


# UpdateConnectClientAddInRequestRequestTypeDef

### AddInId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### URL
- **Type**: typing.Optional[str]


# UpdateConnectionAliasPermissionRequestRequestTypeDef

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionAliasPermission
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAliasPermissionTypeDef'>
- **Required**: Yes


# UpdateResultTypeDef

### UpdateAvailable
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]


# UpdateRulesOfIpGroupRequestRequestTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItemTypeDef]
- **Required**: Yes


# UpdateWorkspaceBundleRequestRequestTypeDef

### BundleId
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]


# UpdateWorkspaceImagePermissionRequestRequestTypeDef

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### AllowCopyImage
- **Type**: <class 'bool'>
- **Required**: Yes

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateWorkspacesPoolRequestRequestTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### BundleId
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### Capacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.CapacityTypeDef]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationSettingsRequestTypeDef]

### TimeoutSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.TimeoutSettingsTypeDef]


# UpdateWorkspacesPoolResultTypeDef

### WorkspacesPool
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPoolTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserSettingTypeDef

### Action
- **Type**: typing.Literal['CLIPBOARD_COPY_FROM_LOCAL_DEVICE', 'CLIPBOARD_COPY_TO_LOCAL_DEVICE', 'PRINTING_TO_LOCAL_DEVICE', 'SMART_CARD']
- **Required**: Yes

### Permission
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MaximumLength
- **Type**: typing.Optional[int]


# UserStorageTypeDef

### Capacity
- **Type**: <class 'str'>
- **Required**: Yes


# WorkSpaceApplicationDeploymentTypeDef

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociationTypeDef]]


# WorkSpaceApplicationTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### Created
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### LicenseType
- **Type**: typing.Optional[typing.Literal['LICENSED', 'UNLICENSED']]

### Name
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'ERROR', 'PENDING', 'UNINSTALL_ONLY']]

### SupportedComputeTypeNames
- **Type**: typing.Optional[typing.List[typing.Literal['GRAPHICS', 'GRAPHICSPRO', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G4DN', 'PERFORMANCE', 'POWER', 'POWERPRO', 'STANDARD', 'VALUE']]]

### SupportedOperatingSystemNames
- **Type**: typing.Optional[typing.List[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]]


# WorkspaceAccessPropertiesTypeDef

### DeviceTypeWindows
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypeOsx
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypeWeb
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypeIos
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypeAndroid
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypeChromeOs
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypeZeroClient
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypeLinux
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# WorkspaceBundleTypeDef

### BundleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Owner
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]

### RootStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.RootStorageTypeDef]

### UserStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.UserStorageTypeDef]

### ComputeType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ComputeTypeTypeDef]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'ERROR', 'PENDING']]

### BundleType
- **Type**: typing.Optional[typing.Literal['REGULAR', 'STANDBY']]


# WorkspaceConnectionStatusTypeDef

### WorkspaceId
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED', 'UNKNOWN']]

### ConnectionStateCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastKnownUserConnectionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# WorkspaceCreationPropertiesTypeDef

### EnableWorkDocs
- **Type**: typing.Optional[bool]

### EnableInternetAccess
- **Type**: typing.Optional[bool]

### DefaultOu
- **Type**: typing.Optional[str]

### CustomSecurityGroupId
- **Type**: typing.Optional[str]

### UserEnabledAsLocalAdministrator
- **Type**: typing.Optional[bool]

### EnableMaintenanceMode
- **Type**: typing.Optional[bool]

### InstanceIamRoleArn
- **Type**: typing.Optional[str]


# WorkspaceDirectoryTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### DirectoryName
- **Type**: typing.Optional[str]

### RegistrationCode
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### DnsIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### CustomerUserName
- **Type**: typing.Optional[str]

### IamRoleId
- **Type**: typing.Optional[str]

### DirectoryType
- **Type**: typing.Optional[typing.Literal['AD_CONNECTOR', 'CUSTOMER_MANAGED', 'SIMPLE_AD']]

### WorkspaceSecurityGroupId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DEREGISTERED', 'DEREGISTERING', 'ERROR', 'REGISTERED', 'REGISTERING']]

### WorkspaceCreationProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultWorkspaceCreationPropertiesTypeDef]

### ipGroupIds
- **Type**: typing.Optional[typing.List[str]]

### WorkspaceAccessProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceAccessPropertiesTypeDef]

### Tenancy
- **Type**: typing.Optional[typing.Literal['DEDICATED', 'SHARED']]

### SelfservicePermissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.SelfservicePermissionsTypeDef]

### SamlProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.SamlPropertiesTypeDef]

### CertificateBasedAuthProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.CertificateBasedAuthPropertiesTypeDef]

### WorkspaceDirectoryName
- **Type**: typing.Optional[str]

### WorkspaceDirectoryDescription
- **Type**: typing.Optional[str]

### UserIdentityType
- **Type**: typing.Optional[typing.Literal['AWS_DIRECTORY_SERVICE', 'CUSTOMER_MANAGED']]

### WorkspaceType
- **Type**: typing.Optional[typing.Literal['PERSONAL', 'POOLS']]

### ActiveDirectoryConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ActiveDirectoryConfigTypeDef]

### StreamingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.StreamingPropertiesOutputTypeDef]

### ErrorMessage
- **Type**: typing.Optional[str]


# WorkspaceImageTypeDef

### ImageId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.OperatingSystemTypeDef]

### State
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'ERROR', 'PENDING']]

### RequiredTenancy
- **Type**: typing.Optional[typing.Literal['DEDICATED', 'DEFAULT']]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### Created
- **Type**: typing.Optional[datetime.datetime]

### OwnerAccountId
- **Type**: typing.Optional[str]

### Updates
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.UpdateResultTypeDef]

### ErrorDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ErrorDetailsTypeDef]]


# WorkspacePropertiesExtraOutputTypeDef

### RunningMode
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'AUTO_STOP', 'MANUAL']]

### RunningModeAutoStopTimeoutInMinutes
- **Type**: typing.Optional[int]

### RootVolumeSizeGib
- **Type**: typing.Optional[int]

### UserVolumeSizeGib
- **Type**: typing.Optional[int]

### ComputeTypeName
- **Type**: typing.Optional[typing.Literal['GRAPHICS', 'GRAPHICSPRO', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G4DN', 'PERFORMANCE', 'POWER', 'POWERPRO', 'STANDARD', 'VALUE']]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['PCOIP', 'WSP']]]

### OperatingSystemName
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]


# WorkspacePropertiesOutputTypeDef

### RunningMode
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'AUTO_STOP', 'MANUAL']]

### RunningModeAutoStopTimeoutInMinutes
- **Type**: typing.Optional[int]

### RootVolumeSizeGib
- **Type**: typing.Optional[int]

### UserVolumeSizeGib
- **Type**: typing.Optional[int]

### ComputeTypeName
- **Type**: typing.Optional[typing.Literal['GRAPHICS', 'GRAPHICSPRO', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G4DN', 'PERFORMANCE', 'POWER', 'POWERPRO', 'STANDARD', 'VALUE']]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['PCOIP', 'WSP']]]

### OperatingSystemName
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]


# WorkspacePropertiesTypeDef

### RunningMode
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'AUTO_STOP', 'MANUAL']]

### RunningModeAutoStopTimeoutInMinutes
- **Type**: typing.Optional[int]

### RootVolumeSizeGib
- **Type**: typing.Optional[int]

### UserVolumeSizeGib
- **Type**: typing.Optional[int]

### ComputeTypeName
- **Type**: typing.Optional[typing.Literal['GRAPHICS', 'GRAPHICSPRO', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G4DN', 'PERFORMANCE', 'POWER', 'POWERPRO', 'STANDARD', 'VALUE']]

### Protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PCOIP', 'WSP']]]

### OperatingSystemName
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]


# WorkspaceRequestOutputTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeEncryptionKey
- **Type**: typing.Optional[str]

### UserVolumeEncryptionEnabled
- **Type**: typing.Optional[bool]

### RootVolumeEncryptionEnabled
- **Type**: typing.Optional[bool]

### WorkspaceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesOutputTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]

### WorkspaceName
- **Type**: typing.Optional[str]


# WorkspaceRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeEncryptionKey
- **Type**: typing.Optional[str]

### UserVolumeEncryptionEnabled
- **Type**: typing.Optional[bool]

### RootVolumeEncryptionEnabled
- **Type**: typing.Optional[bool]

### WorkspaceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TagTypeDef]]

### WorkspaceName
- **Type**: typing.Optional[str]


# WorkspaceResourceAssociationTypeDef

### AssociatedResourceId
- **Type**: typing.Optional[str]

### AssociatedResourceType
- **Type**: typing.Optional[typing.Literal['APPLICATION']]

### Created
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### State
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'ERROR', 'INSTALLING', 'PENDING_INSTALL', 'PENDING_INSTALL_DEPLOYMENT', 'PENDING_UNINSTALL', 'PENDING_UNINSTALL_DEPLOYMENT', 'REMOVED', 'UNINSTALLING']]

### StateReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReasonTypeDef]

### WorkspaceId
- **Type**: typing.Optional[str]


# WorkspaceTypeDef

### WorkspaceId
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ADMIN_MAINTENANCE', 'AVAILABLE', 'ERROR', 'IMPAIRED', 'MAINTENANCE', 'PENDING', 'REBOOTING', 'REBUILDING', 'RESTORING', 'STARTING', 'STOPPED', 'STOPPING', 'SUSPENDED', 'TERMINATED', 'TERMINATING', 'UNHEALTHY', 'UPDATING']]

### BundleId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ComputerName
- **Type**: typing.Optional[str]

### VolumeEncryptionKey
- **Type**: typing.Optional[str]

### UserVolumeEncryptionEnabled
- **Type**: typing.Optional[bool]

### RootVolumeEncryptionEnabled
- **Type**: typing.Optional[bool]

### WorkspaceName
- **Type**: typing.Optional[str]

### WorkspaceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesOutputTypeDef]

### ModificationStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ModificationStateTypeDef]]

### RelatedWorkspaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.RelatedWorkspacePropertiesTypeDef]]

### DataReplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DataReplicationSettingsTypeDef]

### StandbyWorkspacesProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.StandbyWorkspacesPropertiesTypeDef]]


# WorkspacesIpGroupTypeDef

### groupId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]

### groupDesc
- **Type**: typing.Optional[str]

### userRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItemTypeDef]]


# WorkspacesPoolErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[typing.Literal['BUNDLE_NOT_FOUND', 'DEFAULT_OU_IS_MISSING', 'DIRECTORY_NOT_FOUND', 'DOMAIN_JOIN_ERROR_ACCESS_DENIED', 'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED', 'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND', 'DOMAIN_JOIN_ERROR_INVALID_PARAMETER', 'DOMAIN_JOIN_ERROR_LOGON_FAILURE', 'DOMAIN_JOIN_ERROR_MORE_DATA', 'DOMAIN_JOIN_ERROR_NOT_SUPPORTED', 'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN', 'DOMAIN_JOIN_ERROR_SECRET_ACTION_PERMISSION_IS_MISSING', 'DOMAIN_JOIN_ERROR_SECRET_DECRYPTION_FAILURE', 'DOMAIN_JOIN_ERROR_SECRET_INVALID', 'DOMAIN_JOIN_ERROR_SECRET_NOT_FOUND', 'DOMAIN_JOIN_ERROR_SECRET_STATE_INVALID', 'DOMAIN_JOIN_ERROR_SECRET_VALUE_KEY_NOT_FOUND', 'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR', 'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME', 'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED', 'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED', 'IAM_SERVICE_ROLE_IS_MISSING', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION', 'IGW_NOT_ATTACHED', 'IMAGE_NOT_FOUND', 'INSUFFICIENT_PERMISSIONS_ERROR', 'INTERNAL_SERVICE_ERROR', 'INVALID_SUBNET_CONFIGURATION', 'MACHINE_ROLE_IS_MISSING', 'NETWORK_INTERFACE_LIMIT_EXCEEDED', 'SECURITY_GROUPS_NOT_FOUND', 'STS_DISABLED_IN_REGION', 'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES', 'SUBNET_NOT_FOUND', 'WORKSPACES_POOL_INSTANCE_PROVISIONING_FAILURE', 'WORKSPACES_POOL_STOPPED']]

### ErrorMessage
- **Type**: typing.Optional[str]


# WorkspacesPoolSessionTypeDef

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['SAML']]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'NOT_CONNECTED']]

### InstanceId
- **Type**: typing.Optional[str]

### ExpirationTime
- **Type**: typing.Optional[datetime.datetime]

### NetworkAccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.NetworkAccessConfigurationTypeDef]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# WorkspacesPoolTypeDef

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.CapacityStatusTypeDef'>
- **Required**: Yes

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CREATING', 'DELETING', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING', 'UPDATING']
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Errors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPoolErrorTypeDef]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationSettingsResponseTypeDef]

### TimeoutSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.TimeoutSettingsTypeDef]


