# Pydantic Models in codeconnections_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConnectionTypeDef

### ConnectionName
- **Type**: typing.Optional[str]

### ConnectionArn
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']]

### OwnerAccountId
- **Type**: typing.Optional[str]

### ConnectionStatus
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'ERROR', 'PENDING']]

### HostArn
- **Type**: typing.Optional[str]


# CreateConnectionInputRequestTypeDef

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.TagTypeDef]]

### HostArn
- **Type**: typing.Optional[str]


# CreateConnectionOutputTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHostInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']
- **Required**: Yes

### ProviderEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.TagTypeDef]]


# CreateHostOutputTypeDef

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRepositoryLinkInputRequestTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.TagTypeDef]]


# CreateRepositoryLinkOutputTypeDef

### RepositoryLinkInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSyncConfigurationInputRequestTypeDef

### Branch
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigFile
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### PublishDeploymentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TriggerResourceUpdateOn
- **Type**: typing.Optional[typing.Literal['ANY_CHANGE', 'FILE_CHANGE']]


# CreateSyncConfigurationOutputTypeDef

### SyncConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConnectionInputRequestTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostInputRequestTypeDef

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRepositoryLinkInputRequestTypeDef

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSyncConfigurationInputRequestTypeDef

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionInputRequestTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionOutputTypeDef

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ConnectionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHostInputRequestTypeDef

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetHostOutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']
- **Required**: Yes

### ProviderEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryLinkInputRequestTypeDef

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRepositoryLinkOutputTypeDef

### RepositoryLinkInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositorySyncStatusInputRequestTypeDef

### Branch
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes


# GetRepositorySyncStatusOutputTypeDef

### LatestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositorySyncAttemptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceSyncStatusInputRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes


# GetResourceSyncStatusOutputTypeDef

### DesiredState
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RevisionTypeDef'>
- **Required**: Yes

### LatestSuccessfulSync
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResourceSyncAttemptTypeDef'>
- **Required**: Yes

### LatestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResourceSyncAttemptTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSyncBlockerSummaryInputRequestTypeDef

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSyncBlockerSummaryOutputTypeDef

### SyncBlockerSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncBlockerSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSyncConfigurationInputRequestTypeDef

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSyncConfigurationOutputTypeDef

### SyncConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HostTypeDef

### Name
- **Type**: typing.Optional[str]

### HostArn
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']]

### ProviderEndpoint
- **Type**: typing.Optional[str]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationTypeDef]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# ListConnectionsInputRequestTypeDef

### ProviderTypeFilter
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']]

### HostArnFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsOutputTypeDef

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.ConnectionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHostsInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHostsOutputTypeDef

### Hosts
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.HostTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRepositoryLinksInputRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRepositoryLinksOutputTypeDef

### RepositoryLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfoTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRepositorySyncDefinitionsInputRequestTypeDef

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes


# ListRepositorySyncDefinitionsOutputTypeDef

### RepositorySyncDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.RepositorySyncDefinitionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSyncConfigurationsInputRequestTypeDef

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSyncConfigurationsOutputTypeDef

### SyncConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfigurationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RepositoryLinkInfoTypeDef

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']
- **Required**: Yes

### RepositoryLinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# RepositorySyncAttemptTypeDef

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'INITIATED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.RepositorySyncEventTypeDef]
- **Required**: Yes


# RepositorySyncDefinitionTypeDef

### Branch
- **Type**: <class 'str'>
- **Required**: Yes

### Directory
- **Type**: <class 'str'>
- **Required**: Yes

### Parent
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# RepositorySyncEventTypeDef

### Event
- **Type**: <class 'str'>
- **Required**: Yes

### Time
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: typing.Optional[str]


# ResourceSyncAttemptTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.ResourceSyncEventTypeDef]
- **Required**: Yes

### InitialRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RevisionTypeDef'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'INITIATED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### TargetRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RevisionTypeDef'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceSyncEventTypeDef

### Event
- **Type**: <class 'str'>
- **Required**: Yes

### Time
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: typing.Optional[str]


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


# RevisionTypeDef

### Branch
- **Type**: <class 'str'>
- **Required**: Yes

### Directory
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']
- **Required**: Yes

### Sha
- **Type**: <class 'str'>
- **Required**: Yes


# SyncBlockerContextTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SyncBlockerSummaryTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ParentResourceName
- **Type**: typing.Optional[str]

### LatestBlockers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.SyncBlockerTypeDef]]


# SyncBlockerTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['AUTOMATED']
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'RESOLVED']
- **Required**: Yes

### CreatedReason
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Contexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.SyncBlockerContextTypeDef]]

### ResolvedReason
- **Type**: typing.Optional[str]

### ResolvedAt
- **Type**: typing.Optional[datetime.datetime]


# SyncConfigurationTypeDef

### Branch
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']
- **Required**: Yes

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ConfigFile
- **Type**: typing.Optional[str]

### PublishDeploymentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TriggerResourceUpdateOn
- **Type**: typing.Optional[typing.Literal['ANY_CHANGE', 'FILE_CHANGE']]


# TagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateHostInputRequestTypeDef

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderEndpoint
- **Type**: typing.Optional[str]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationTypeDef]


# UpdateRepositoryLinkInputRequestTypeDef

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionArn
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# UpdateRepositoryLinkOutputTypeDef

### RepositoryLinkInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSyncBlockerInputRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResolvedReason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSyncBlockerOutputTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ParentResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncBlocker
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncBlockerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSyncConfigurationInputRequestTypeDef

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### Branch
- **Type**: typing.Optional[str]

### ConfigFile
- **Type**: typing.Optional[str]

### RepositoryLinkId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### PublishDeploymentStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### TriggerResourceUpdateOn
- **Type**: typing.Optional[typing.Literal['ANY_CHANGE', 'FILE_CHANGE']]


# UpdateSyncConfigurationOutputTypeDef

### SyncConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConfigurationTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### TlsCertificate
- **Type**: typing.Optional[str]


