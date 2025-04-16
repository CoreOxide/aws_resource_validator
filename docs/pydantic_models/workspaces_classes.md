# Workspaces Classes

# AcceptAccountLinkInvitationRequest

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# AcceptAccountLinkInvitationResult

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLink'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# AccountLink

### AccountLinkId
- **Type**: typing.Optional[str]

### AccountLinkStatus
- **Type**: typing.Optional[typing.Literal['LINKED', 'LINKING_FAILED', 'LINK_NOT_FOUND', 'PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT', 'REJECTED']]

### SourceAccountId
- **Type**: typing.Optional[str]

### TargetAccountId
- **Type**: typing.Optional[str]


# AccountModification

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


# ActiveDirectoryConfig

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceAccountSecretArn
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationResourceAssociation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReason]


# ApplicationSettingsRequest

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### SettingsGroup
- **Type**: typing.Optional[str]


# ApplicationSettingsResponse

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### SettingsGroup
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]


# AssociateConnectionAliasRequest

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateConnectionAliasResult

### ConnectionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateIpGroupsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AssociateWorkspaceApplicationRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateWorkspaceApplicationResult

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# AssociationStateReason

### ErrorCode
- **Type**: typing.Optional[typing.Literal['DeploymentError.InternalServerError', 'DeploymentError.WorkspaceUnreachable', 'ValidationError.InsufficientDiskSpace', 'ValidationError.InsufficientMemory', 'ValidationError.UnsupportedOperatingSystem']]

### ErrorMessage
- **Type**: typing.Optional[str]


# AuthorizeIpRulesRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItem]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BundleResourceAssociation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReason]


# Capacity

### DesiredUserSessions
- **Type**: <class 'int'>
- **Required**: Yes


# CapacityStatus

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


# CertificateBasedAuthProperties

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### CertificateAuthorityArn
- **Type**: typing.Optional[str]


# ClientProperties

### ReconnectEnabled
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### LogUploadEnabled
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ClientPropertiesResult

### ResourceId
- **Type**: typing.Optional[str]

### ClientProperties
- **Type**: <class 'NoneType'>


# ComputeType

### Name
- **Type**: typing.Optional[typing.Literal['GENERALPURPOSE_4XLARGE', 'GENERALPURPOSE_8XLARGE', 'GRAPHICS', 'GRAPHICSPRO', 'GRAPHICSPRO_G4DN', 'GRAPHICS_G4DN', 'PERFORMANCE', 'POWER', 'POWERPRO', 'STANDARD', 'VALUE']]


# ConnectClientAddIn

### AddInId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### URL
- **Type**: typing.Optional[str]


# ConnectionAlias

### ConnectionString
- **Type**: typing.Optional[str]

### AliasId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'DELETING']]

### OwnerAccountId
- **Type**: typing.Optional[str]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAliasAssociation]]


# ConnectionAliasAssociation

### AssociationStatus
- **Type**: typing.Optional[typing.Literal['ASSOCIATED_WITH_OWNER_ACCOUNT', 'ASSOCIATED_WITH_SHARED_ACCOUNT', 'NOT_ASSOCIATED', 'PENDING_ASSOCIATION', 'PENDING_DISASSOCIATION']]

### AssociatedAccountId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### ConnectionIdentifier
- **Type**: typing.Optional[str]


# ConnectionAliasPermission

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AllowAssociation
- **Type**: <class 'bool'>
- **Required**: Yes


# CopyWorkspaceImageRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]


# CopyWorkspaceImageResult

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccountLinkInvitationRequest

### TargetAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateAccountLinkInvitationResult

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLink'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectClientAddInRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### URL
- **Type**: <class 'str'>
- **Required**: Yes


# CreateConnectClientAddInResult

### AddInId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConnectionAliasRequest

### ConnectionString
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]


# CreateConnectionAliasResult

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIpGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupDesc
- **Type**: typing.Optional[str]

### UserRules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItem]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]


# CreateIpGroupResult

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStandbyWorkspacesRequest

### PrimaryRegion
- **Type**: <class 'str'>
- **Required**: Yes

### StandbyWorkspaces
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.StandbyWorkspaceUnion]
- **Required**: Yes


# CreateStandbyWorkspacesResult

### FailedStandbyRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedCreateStandbyWorkspacesRequest]
- **Required**: Yes

### PendingStandbyRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.PendingCreateStandbyWorkspacesRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTagsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]
- **Required**: Yes


# CreateUpdatedWorkspaceImageRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]


# CreateUpdatedWorkspaceImageResult

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspaceBundleResult

### WorkspaceBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceBundle'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspaceImageRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]


# CreateWorkspaceImageResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.OperatingSystem'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspacesPoolRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.Capacity'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationSettingsRequest]

### TimeoutSettings
- **Type**: <class 'NoneType'>


# CreateWorkspacesPoolResult

### WorkspacesPool
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspacesRequest

### Workspaces
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceRequestUnion]
- **Required**: Yes


# CreateWorkspacesResult

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedCreateWorkspaceRequest]
- **Required**: Yes

### PendingRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.Workspace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DataReplicationSettings

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]

### RecoverySnapshotTime
- **Type**: typing.Optional[datetime.datetime]


# DefaultClientBrandingAttributes

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


# DefaultImportClientBrandingAttributes

### Logo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.Blob]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportLink
- **Type**: typing.Optional[str]

### ForgotPasswordLink
- **Type**: typing.Optional[str]

### LoginMessage
- **Type**: typing.Optional[typing.Mapping[str, str]]


# DefaultWorkspaceCreationProperties

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


# DeleteAccountLinkInvitationRequest

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# DeleteAccountLinkInvitationResult

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLink'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteClientBrandingRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Platforms
- **Type**: typing.Sequence[typing.Literal['DeviceTypeAndroid', 'DeviceTypeIos', 'DeviceTypeLinux', 'DeviceTypeOsx', 'DeviceTypeWeb', 'DeviceTypeWindows']]
- **Required**: Yes


# DeleteConnectClientAddInRequest

### AddInId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConnectionAliasRequest

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIpGroupRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTagsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteWorkspaceBundleRequest

### BundleId
- **Type**: typing.Optional[str]


# DeleteWorkspaceImageRequest

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes


# DeployWorkspaceApplicationsRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### Force
- **Type**: typing.Optional[bool]


# DeployWorkspaceApplicationsResult

### Deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkSpaceApplicationDeployment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterWorkspaceDirectoryRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountModificationsRequest

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountModificationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# DescribeAccountModificationsResult

### AccountModifications
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.AccountModification]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountResult

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationAssociationsRequest

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


# DescribeApplicationAssociationsResult

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationResourceAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationsRequest

### ApplicationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ComputeTypeNames
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.ComputeType]]

### LicenseType
- **Type**: typing.Optional[typing.Literal['LICENSED', 'UNLICENSED']]

### OperatingSystemNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'ROCKY_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]]

### Owner
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeApplicationsResult

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkSpaceApplication]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBundleAssociationsRequest

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceTypes
- **Type**: typing.Sequence[typing.Literal['APPLICATION']]
- **Required**: Yes


# DescribeBundleAssociationsResult

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.BundleResourceAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClientBrandingRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeClientBrandingResult

### DeviceTypeWindows
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeOsx
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeAndroid
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeIos
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.IosClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeLinux
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeWeb
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClientPropertiesRequest

### ResourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeClientPropertiesResult

### ClientPropertiesList
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ClientPropertiesResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeConnectClientAddInsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeConnectClientAddInsResult

### AddIns
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectClientAddIn]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConnectionAliasPermissionsRequest

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeConnectionAliasPermissionsResult

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionAliasPermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAliasPermission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConnectionAliasesRequest

### AliasIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeConnectionAliasesResult

### ConnectionAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAlias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeImageAssociationsRequest

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceTypes
- **Type**: typing.Sequence[typing.Literal['APPLICATION']]
- **Required**: Yes


# DescribeImageAssociationsResult

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ImageResourceAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIpGroupsRequest

### GroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeIpGroupsRequestPaginate

### GroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# DescribeIpGroupsResult

### Result
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesIpGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTagsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTagsResult

### TagList
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkspaceAssociationsRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### AssociatedResourceTypes
- **Type**: typing.Sequence[typing.Literal['APPLICATION']]
- **Required**: Yes


# DescribeWorkspaceAssociationsResult

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkspaceBundlesRequest

### BundleIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Owner
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceBundlesRequestPaginate

### BundleIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Owner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# DescribeWorkspaceBundlesResult

### Bundles
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceBundle]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceDirectoriesFilter

### Name
- **Type**: typing.Literal['USER_IDENTITY_TYPE', 'WORKSPACE_TYPE']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeWorkspaceDirectoriesRequest

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WorkspaceDirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.DescribeWorkspaceDirectoriesFilter]]


# DescribeWorkspaceDirectoriesRequestPaginate

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### WorkspaceDirectoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.DescribeWorkspaceDirectoriesFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# DescribeWorkspaceDirectoriesResult

### Directories
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceDirectory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceImagePermissionsRequest

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeWorkspaceImagePermissionsResult

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ImagePermissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ImagePermission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceImagesRequest

### ImageIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ImageType
- **Type**: typing.Optional[typing.Literal['OWNED', 'SHARED']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeWorkspaceImagesRequestPaginate

### ImageIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ImageType
- **Type**: typing.Optional[typing.Literal['OWNED', 'SHARED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# DescribeWorkspaceImagesResult

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceImage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspaceSnapshotsRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceSnapshotsResult

### RebuildSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.Snapshot]
- **Required**: Yes

### RestoreSnapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.Snapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkspacesConnectionStatusRequest

### WorkspaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesConnectionStatusRequestPaginate

### WorkspaceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# DescribeWorkspacesConnectionStatusResult

### WorkspacesConnectionStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceConnectionStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolSessionsRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolSessionsResult

### Sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPoolSession]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolsFilter

### Name
- **Type**: typing.Literal['PoolName']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['CONTAINS', 'EQUALS', 'NOTCONTAINS', 'NOTEQUALS']
- **Required**: Yes


# DescribeWorkspacesPoolsRequest

### PoolIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.DescribeWorkspacesPoolsFilter]]

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesPoolsResult

### WorkspacesPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPool]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeWorkspacesRequest

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


# DescribeWorkspacesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# DescribeWorkspacesResult

### Workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.Workspace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateConnectionAliasRequest

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIpGroupsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociateWorkspaceApplicationRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateWorkspaceApplicationResult

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# ErrorDetails

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AdditionalDrivesAttached', 'AdditionalDrivesPresent', 'AmazonSsmAgentEnabled', 'AntiVirusInstalled', 'AppXPackagesInstalled', 'AutoLogonEnabled', 'AutoMountDisabled', 'AzureDomainJoined', 'DHCPDisabled', 'DiskFreeSpace', 'DiskSizeExceeded', 'DomainAccountServicesFound', 'DomainJoined', 'EnvironmentVariablesPathMissingEntries', 'FirewallEnabled', 'InPlaceUpgrade', 'IncompatiblePartitioning', 'InsufficientDiskSpace', 'InsufficientRearmCount', 'InvalidIp', 'MultipleBootPartition', 'MultipleUserProfiles', 'OSNotSupported', 'OfficeInstalled', 'OutdatedPowershellVersion', 'PCoIPAgentInstalled', 'PendingReboot', 'RealTimeUniversalDisabled', 'RemoteDesktopServicesDisabled', 'Requires64BitOS', 'ReservedStorageInUse', 'StagedAppxPackage', 'SysPrepFileMissing', 'UEFINotSupported', 'UnknownError', 'UnsupportedOsUpgrade', 'UnsupportedSecurityProtocol', 'UserProfileMissing', 'VMWareToolsInstalled', 'WindowsModulesInstallerDisabled', 'WindowsUpdatesEnabled', 'WindowsUpdatesRequired', 'WorkspacesBYOLAccountDisabled', 'WorkspacesBYOLAccountNotFound', 'ZeroRearmCount']]

### ErrorMessage
- **Type**: typing.Optional[str]


# FailedCreateStandbyWorkspacesRequest

### StandbyWorkspaceRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.StandbyWorkspaceOutput]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FailedCreateWorkspaceRequest

### WorkspaceRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceRequestOutput]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# FailedWorkspaceChangeRequest

### WorkspaceId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# GetAccountLinkRequest

### LinkId
- **Type**: typing.Optional[str]

### LinkedAccountId
- **Type**: typing.Optional[str]


# GetAccountLinkResult

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLink'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# GlobalAcceleratorForDirectory

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED_AUTO']
- **Required**: Yes

### PreferredProtocol
- **Type**: typing.Optional[typing.Literal['NONE', 'TCP']]


# GlobalAcceleratorForWorkSpace

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED_AUTO', 'INHERITED']
- **Required**: Yes

### PreferredProtocol
- **Type**: typing.Optional[typing.Literal['INHERITED', 'NONE', 'TCP']]


# IDCConfig

### InstanceArn
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]


# ImagePermission

### SharedAccountId
- **Type**: typing.Optional[str]


# ImageResourceAssociation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReason]


# ImportClientBrandingRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceTypeWindows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributes]

### DeviceTypeOsx
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributes]

### DeviceTypeAndroid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributes]

### DeviceTypeIos
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.IosImportClientBrandingAttributes]

### DeviceTypeLinux
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributes]

### DeviceTypeWeb
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultImportClientBrandingAttributes]


# ImportClientBrandingResult

### DeviceTypeWindows
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeOsx
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeAndroid
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeIos
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.IosClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeLinux
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### DeviceTypeWeb
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.DefaultClientBrandingAttributes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# ImportWorkspaceImageRequest

### Ec2ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### IngestionProcess
- **Type**: typing.Literal['BYOL_GRAPHICS', 'BYOL_GRAPHICSPRO', 'BYOL_GRAPHICS_G4DN', 'BYOL_GRAPHICS_G4DN_BYOP', 'BYOL_GRAPHICS_G4DN_WSP', 'BYOL_REGULAR', 'BYOL_REGULAR_BYOP', 'BYOL_REGULAR_WSP']
- **Required**: Yes

### ImageName
- **Type**: <class 'str'>
- **Required**: Yes

### ImageDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]

### Applications
- **Type**: typing.Optional[typing.Sequence[typing.Literal['Microsoft_Office_2016', 'Microsoft_Office_2019']]]


# ImportWorkspaceImageResult

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# IosClientBrandingAttributes

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


# IosImportClientBrandingAttributes

### Logo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.Blob]

### Logo2x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.Blob]

### Logo3x
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.Blob]

### SupportEmail
- **Type**: typing.Optional[str]

### SupportLink
- **Type**: typing.Optional[str]

### ForgotPasswordLink
- **Type**: typing.Optional[str]

### LoginMessage
- **Type**: typing.Optional[typing.Mapping[str, str]]


# IpRuleItem

### ipRule
- **Type**: typing.Optional[str]

### ruleDesc
- **Type**: typing.Optional[str]


# ListAccountLinksRequest

### LinkStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LINKED', 'LINKING_FAILED', 'LINK_NOT_FOUND', 'PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT', 'REJECTED']]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountLinksRequestPaginate

### LinkStatusFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LINKED', 'LINKING_FAILED', 'LINK_NOT_FOUND', 'PENDING_ACCEPTANCE_BY_TARGET_ACCOUNT', 'REJECTED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# ListAccountLinksResult

### AccountLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.AccountLink]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAvailableManagementCidrRangesRequest

### ManagementCidrRangeConstraint
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAvailableManagementCidrRangesRequestPaginate

### ManagementCidrRangeConstraint
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.PaginatorConfig]


# ListAvailableManagementCidrRangesResult

### ManagementCidrRanges
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MicrosoftEntraConfig

### TenantId
- **Type**: typing.Optional[str]

### ApplicationConfigSecretArn
- **Type**: typing.Optional[str]


# MigrateWorkspaceRequest

### SourceWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### BundleId
- **Type**: <class 'str'>
- **Required**: Yes


# MigrateWorkspaceResult

### SourceWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# ModificationState

### Resource
- **Type**: typing.Optional[typing.Literal['COMPUTE_TYPE', 'ROOT_VOLUME', 'USER_VOLUME']]

### State
- **Type**: typing.Optional[typing.Literal['UPDATE_INITIATED', 'UPDATE_IN_PROGRESS']]


# ModifyAccountRequest

### DedicatedTenancySupport
- **Type**: typing.Optional[typing.Literal['ENABLED']]

### DedicatedTenancyManagementCidrRange
- **Type**: typing.Optional[str]


# ModifyCertificateBasedAuthPropertiesRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateBasedAuthProperties
- **Type**: <class 'NoneType'>

### PropertiesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN']]]


# ModifyClientPropertiesRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ClientProperties'>
- **Required**: Yes


# ModifyEndpointEncryptionModeRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointEncryptionMode
- **Type**: typing.Literal['FIPS_VALIDATED', 'STANDARD_TLS']
- **Required**: Yes


# ModifySamlPropertiesRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### SamlProperties
- **Type**: <class 'NoneType'>

### PropertiesToDelete
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SAML_PROPERTIES_RELAY_STATE_PARAMETER_NAME', 'SAML_PROPERTIES_USER_ACCESS_URL']]]


# ModifySelfservicePermissionsRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### SelfservicePermissions
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.SelfservicePermissions'>
- **Required**: Yes


# ModifyStreamingPropertiesRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.StreamingPropertiesUnion]


# ModifyWorkspaceAccessPropertiesRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceAccessProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceAccessProperties'>
- **Required**: Yes


# ModifyWorkspaceCreationPropertiesRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceCreationProperties
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceCreationProperties'>
- **Required**: Yes


# ModifyWorkspacePropertiesRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesUnion]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]


# ModifyWorkspaceStateRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkspaceState
- **Type**: typing.Literal['ADMIN_MAINTENANCE', 'AVAILABLE']
- **Required**: Yes


# NetworkAccessConfiguration

### EniPrivateIpAddress
- **Type**: typing.Optional[str]

### EniId
- **Type**: typing.Optional[str]


# OperatingSystem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingCreateStandbyWorkspacesRequest

### UserName
- **Type**: typing.Optional[str]

### DirectoryId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ADMIN_MAINTENANCE', 'AVAILABLE', 'ERROR', 'IMPAIRED', 'MAINTENANCE', 'PENDING', 'REBOOTING', 'REBUILDING', 'RESTORING', 'STARTING', 'STOPPED', 'STOPPING', 'SUSPENDED', 'TERMINATED', 'TERMINATING', 'UNHEALTHY', 'UPDATING']]

### WorkspaceId
- **Type**: typing.Optional[str]


# RebootRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# RebootWorkspacesRequest

### RebootWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.RebootRequest]
- **Required**: Yes


# RebootWorkspacesResult

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# RebuildRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# RebuildWorkspacesRequest

### RebuildWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.RebuildRequest]
- **Required**: Yes


# RebuildWorkspacesResult

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterWorkspaceDirectoryRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]

### WorkspaceDirectoryName
- **Type**: typing.Optional[str]

### WorkspaceDirectoryDescription
- **Type**: typing.Optional[str]

### UserIdentityType
- **Type**: typing.Optional[typing.Literal['AWS_DIRECTORY_SERVICE', 'AWS_IAM_IDENTITY_CENTER', 'CUSTOMER_MANAGED']]

### IdcInstanceArn
- **Type**: typing.Optional[str]

### MicrosoftEntraConfig
- **Type**: <class 'NoneType'>

### WorkspaceType
- **Type**: typing.Optional[typing.Literal['PERSONAL', 'POOLS']]

### ActiveDirectoryConfig
- **Type**: <class 'NoneType'>


# RegisterWorkspaceDirectoryResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DEREGISTERED', 'DEREGISTERING', 'ERROR', 'REGISTERED', 'REGISTERING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# RejectAccountLinkInvitationRequest

### LinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# RejectAccountLinkInvitationResult

### AccountLink
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.AccountLink'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# RelatedWorkspaceProperties

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseMetadata

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


# RestoreWorkspaceRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# RevokeIpRulesRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserRules
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RootStorage

### Capacity
- **Type**: <class 'str'>
- **Required**: Yes


# SamlProperties

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'ENABLED_WITH_DIRECTORY_LOGIN_FALLBACK']]

### UserAccessUrl
- **Type**: typing.Optional[str]

### RelayStateParameterName
- **Type**: typing.Optional[str]


# SelfservicePermissions

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


# Snapshot

### SnapshotTime
- **Type**: typing.Optional[datetime.datetime]


# StandbyWorkspace

### PrimaryWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeEncryptionKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]


# StandbyWorkspaceOutput

### PrimaryWorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeEncryptionKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]


# StandbyWorkspaceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StandbyWorkspacesProperties

### StandbyWorkspaceId
- **Type**: typing.Optional[str]

### DataReplication
- **Type**: typing.Optional[typing.Literal['NO_REPLICATION', 'PRIMARY_AS_SOURCE']]

### RecoverySnapshotTime
- **Type**: typing.Optional[datetime.datetime]


# StartRequest

### WorkspaceId
- **Type**: typing.Optional[str]


# StartWorkspacesPoolRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# StartWorkspacesRequest

### StartWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.StartRequest]
- **Required**: Yes


# StartWorkspacesResult

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# StopRequest

### WorkspaceId
- **Type**: typing.Optional[str]


# StopWorkspacesPoolRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# StopWorkspacesRequest

### StopWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.StopRequest]
- **Required**: Yes


# StopWorkspacesResult

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# StorageConnector

### ConnectorType
- **Type**: typing.Literal['HOME_FOLDER']
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


# StreamingProperties

### StreamingExperiencePreferredProtocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### UserSettings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.UserSetting]]

### StorageConnectors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.StorageConnector]]

### GlobalAccelerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.GlobalAcceleratorForDirectory]


# StreamingPropertiesOutput

### StreamingExperiencePreferredProtocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### UserSettings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.UserSetting]]

### StorageConnectors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.StorageConnector]]

### GlobalAccelerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.GlobalAcceleratorForDirectory]


# StreamingPropertiesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TerminateRequest

### WorkspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkspacesPoolRequest

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkspacesPoolSessionRequest

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkspacesRequest

### TerminateWorkspaceRequests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.TerminateRequest]
- **Required**: Yes


# TerminateWorkspacesResult

### FailedRequests
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_classes.FailedWorkspaceChangeRequest]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# TimeoutSettings

### DisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### IdleDisconnectTimeoutInSeconds
- **Type**: typing.Optional[int]

### MaxUserDurationInSeconds
- **Type**: typing.Optional[int]


# UpdateConnectClientAddInRequest

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


# UpdateConnectionAliasPermissionRequest

### AliasId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionAliasPermission
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ConnectionAliasPermission'>
- **Required**: Yes


# UpdateResult

### UpdateAvailable
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]


# UpdateRulesOfIpGroupRequest

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### UserRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItem]
- **Required**: Yes


# UpdateWorkspaceBundleRequest

### BundleId
- **Type**: typing.Optional[str]

### ImageId
- **Type**: typing.Optional[str]


# UpdateWorkspaceImagePermissionRequest

### ImageId
- **Type**: <class 'str'>
- **Required**: Yes

### AllowCopyImage
- **Type**: <class 'bool'>
- **Required**: Yes

### SharedAccountId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateWorkspacesPoolRequest

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
- **Type**: <class 'NoneType'>

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationSettingsRequest]

### TimeoutSettings
- **Type**: <class 'NoneType'>


# UpdateWorkspacesPoolResult

### WorkspacesPool
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.ResponseMetadata'>
- **Required**: Yes


# UserSetting

### Action
- **Type**: typing.Literal['CLIPBOARD_COPY_FROM_LOCAL_DEVICE', 'CLIPBOARD_COPY_TO_LOCAL_DEVICE', 'PRINTING_TO_LOCAL_DEVICE', 'SMART_CARD']
- **Required**: Yes

### Permission
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### MaximumLength
- **Type**: typing.Optional[int]


# UserStorage

### Capacity
- **Type**: <class 'str'>
- **Required**: Yes


# WorkSpaceApplication

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ComputeType]]

### SupportedOperatingSystemNames
- **Type**: typing.Optional[typing.List[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'ROCKY_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]]


# WorkSpaceApplicationDeployment

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspaceResourceAssociation]]


# Workspace

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesOutput]

### ModificationStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.ModificationState]]

### RelatedWorkspaces
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.RelatedWorkspaceProperties]]

### DataReplicationSettings
- **Type**: <class 'NoneType'>

### StandbyWorkspacesProperties
- **Type**: typing.Optional[typing.List[NoneType]]


# WorkspaceAccessProperties

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

### DeviceTypeWorkSpacesThinClient
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


# WorkspaceBundle

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkspaceConnectionStatus

### WorkspaceId
- **Type**: typing.Optional[str]

### ConnectionState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED', 'UNKNOWN']]

### ConnectionStateCheckTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastKnownUserConnectionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# WorkspaceCreationProperties

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


# WorkspaceDirectory

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
- **Type**: typing.Optional[typing.Literal['AD_CONNECTOR', 'AWS_IAM_IDENTITY_CENTER', 'CUSTOMER_MANAGED', 'SIMPLE_AD']]

### WorkspaceSecurityGroupId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DEREGISTERED', 'DEREGISTERING', 'ERROR', 'REGISTERED', 'REGISTERING']]

### WorkspaceCreationProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.DefaultWorkspaceCreationProperties]

### ipGroupIds
- **Type**: typing.Optional[typing.List[str]]

### WorkspaceAccessProperties
- **Type**: <class 'NoneType'>

### Tenancy
- **Type**: typing.Optional[typing.Literal['DEDICATED', 'SHARED']]

### SelfservicePermissions
- **Type**: <class 'NoneType'>

### SamlProperties
- **Type**: <class 'NoneType'>

### CertificateBasedAuthProperties
- **Type**: <class 'NoneType'>

### EndpointEncryptionMode
- **Type**: typing.Optional[typing.Literal['FIPS_VALIDATED', 'STANDARD_TLS']]

### MicrosoftEntraConfig
- **Type**: <class 'NoneType'>

### WorkspaceDirectoryName
- **Type**: typing.Optional[str]

### WorkspaceDirectoryDescription
- **Type**: typing.Optional[str]

### UserIdentityType
- **Type**: typing.Optional[typing.Literal['AWS_DIRECTORY_SERVICE', 'AWS_IAM_IDENTITY_CENTER', 'CUSTOMER_MANAGED']]

### WorkspaceType
- **Type**: typing.Optional[typing.Literal['PERSONAL', 'POOLS']]

### IDCConfig
- **Type**: <class 'NoneType'>

### ActiveDirectoryConfig
- **Type**: <class 'NoneType'>

### StreamingProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.StreamingPropertiesOutput]

### ErrorMessage
- **Type**: typing.Optional[str]


# WorkspaceImage

### ImageId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### OperatingSystem
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.UpdateResult]

### ErrorDetails
- **Type**: typing.Optional[typing.List[NoneType]]


# WorkspaceProperties

### RunningMode
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'AUTO_STOP', 'MANUAL']]

### RunningModeAutoStopTimeoutInMinutes
- **Type**: typing.Optional[int]

### RootVolumeSizeGib
- **Type**: typing.Optional[int]

### UserVolumeSizeGib
- **Type**: typing.Optional[int]

### ComputeTypeName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ComputeType]

### Protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PCOIP', 'WSP']]]

### OperatingSystemName
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'ROCKY_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### GlobalAccelerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.GlobalAcceleratorForWorkSpace]


# WorkspacePropertiesOutput

### RunningMode
- **Type**: typing.Optional[typing.Literal['ALWAYS_ON', 'AUTO_STOP', 'MANUAL']]

### RunningModeAutoStopTimeoutInMinutes
- **Type**: typing.Optional[int]

### RootVolumeSizeGib
- **Type**: typing.Optional[int]

### UserVolumeSizeGib
- **Type**: typing.Optional[int]

### ComputeTypeName
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ComputeType]

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['PCOIP', 'WSP']]]

### OperatingSystemName
- **Type**: typing.Optional[typing.Literal['AMAZON_LINUX_2', 'RHEL_8', 'ROCKY_8', 'UBUNTU_18_04', 'UBUNTU_20_04', 'UBUNTU_22_04', 'UNKNOWN', 'WINDOWS_10', 'WINDOWS_11', 'WINDOWS_7', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022']]

### GlobalAccelerator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.GlobalAcceleratorForWorkSpace]


# WorkspacePropertiesUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkspaceRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesUnion]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]

### WorkspaceName
- **Type**: typing.Optional[str]


# WorkspaceRequestOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacePropertiesOutput]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.Tag]]

### WorkspaceName
- **Type**: typing.Optional[str]


# WorkspaceRequestUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkspaceResourceAssociation

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.AssociationStateReason]

### WorkspaceId
- **Type**: typing.Optional[str]


# WorkspacesIpGroup

### groupId
- **Type**: typing.Optional[str]

### groupName
- **Type**: typing.Optional[str]

### groupDesc
- **Type**: typing.Optional[str]

### userRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.IpRuleItem]]


# WorkspacesPool

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PoolArn
- **Type**: <class 'str'>
- **Required**: Yes

### CapacityStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_classes.CapacityStatus'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_classes.WorkspacesPoolError]]

### ApplicationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_classes.ApplicationSettingsResponse]

### TimeoutSettings
- **Type**: <class 'NoneType'>


# WorkspacesPoolError

### ErrorCode
- **Type**: typing.Optional[typing.Literal['BUNDLE_NOT_FOUND', 'DEFAULT_OU_IS_MISSING', 'DIRECTORY_NOT_FOUND', 'DOMAIN_JOIN_ERROR_ACCESS_DENIED', 'DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED', 'DOMAIN_JOIN_ERROR_FILE_NOT_FOUND', 'DOMAIN_JOIN_ERROR_INVALID_PARAMETER', 'DOMAIN_JOIN_ERROR_LOGON_FAILURE', 'DOMAIN_JOIN_ERROR_MORE_DATA', 'DOMAIN_JOIN_ERROR_NOT_SUPPORTED', 'DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN', 'DOMAIN_JOIN_ERROR_SECRET_ACTION_PERMISSION_IS_MISSING', 'DOMAIN_JOIN_ERROR_SECRET_DECRYPTION_FAILURE', 'DOMAIN_JOIN_ERROR_SECRET_INVALID', 'DOMAIN_JOIN_ERROR_SECRET_NOT_FOUND', 'DOMAIN_JOIN_ERROR_SECRET_STATE_INVALID', 'DOMAIN_JOIN_ERROR_SECRET_VALUE_KEY_NOT_FOUND', 'DOMAIN_JOIN_INTERNAL_SERVICE_ERROR', 'DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME', 'DOMAIN_JOIN_NERR_PASSWORD_EXPIRED', 'DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED', 'IAM_SERVICE_ROLE_IS_MISSING', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION', 'IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION', 'IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION', 'IGW_NOT_ATTACHED', 'IMAGE_NOT_FOUND', 'INSUFFICIENT_PERMISSIONS_ERROR', 'INTERNAL_SERVICE_ERROR', 'INVALID_SUBNET_CONFIGURATION', 'MACHINE_ROLE_IS_MISSING', 'NETWORK_INTERFACE_LIMIT_EXCEEDED', 'SECURITY_GROUPS_NOT_FOUND', 'STS_DISABLED_IN_REGION', 'SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES', 'SUBNET_NOT_FOUND', 'WORKSPACES_POOL_INSTANCE_PROVISIONING_FAILURE', 'WORKSPACES_POOL_STOPPED']]

### ErrorMessage
- **Type**: typing.Optional[str]


# WorkspacesPoolSession

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
- **Type**: <class 'NoneType'>

### StartTime
- **Type**: typing.Optional[datetime.datetime]


