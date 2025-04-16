# Codeconnections Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Connection

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


# CreateConnectionInput

### ConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.Tag]]

### HostArn
- **Type**: typing.Optional[str]


# CreateConnectionOutput

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHostInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationUnion]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.Tag]]


# CreateHostOutput

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRepositoryLinkInput

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.Tag]]


# CreateRepositoryLinkOutput

### RepositoryLinkInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSyncConfigurationInput

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

### PullRequestComment
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateSyncConfigurationOutput

### SyncConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConnectionInput

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteHostInput

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRepositoryLinkInput

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSyncConfigurationInput

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionInput

### ConnectionArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionOutput

### Connection
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.Connection'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# GetHostInput

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetHostOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryLinkInput

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRepositoryLinkOutput

### RepositoryLinkInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositorySyncStatusInput

### Branch
- **Type**: <class 'str'>
- **Required**: Yes

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes


# GetRepositorySyncStatusOutput

### LatestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositorySyncAttempt'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceSyncStatusInput

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes


# GetResourceSyncStatusOutput

### DesiredState
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.Revision'>
- **Required**: Yes

### LatestSuccessfulSync
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResourceSyncAttempt'>
- **Required**: Yes

### LatestSync
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResourceSyncAttempt'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# GetSyncBlockerSummaryInput

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSyncBlockerSummaryOutput

### SyncBlockerSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncBlockerSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# GetSyncConfigurationInput

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSyncConfigurationOutput

### SyncConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# Host

### Name
- **Type**: typing.Optional[str]

### HostArn
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']]

### ProviderEndpoint
- **Type**: typing.Optional[str]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationOutput]

### Status
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]


# ListConnectionsInput

### ProviderTypeFilter
- **Type**: typing.Optional[typing.Literal['Bitbucket', 'GitHub', 'GitHubEnterpriseServer', 'GitLab', 'GitLabSelfManaged']]

### HostArnFilter
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConnectionsOutput

### Connections
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.Connection]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHostsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHostsOutput

### Hosts
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.Host]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRepositoryLinksInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRepositoryLinksOutput

### RepositoryLinks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRepositorySyncDefinitionsInput

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### SyncType
- **Type**: typing.Literal['CFN_STACK_SYNC']
- **Required**: Yes


# ListRepositorySyncDefinitionsOutput

### RepositorySyncDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.RepositorySyncDefinition]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSyncConfigurationsInput

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


# ListSyncConfigurationsOutput

### SyncConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# RepositoryLinkInfo

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


# RepositorySyncAttempt

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'INITIATED', 'IN_PROGRESS', 'QUEUED', 'SUCCEEDED']
- **Required**: Yes

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.RepositorySyncEvent]
- **Required**: Yes


# RepositorySyncDefinition

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


# RepositorySyncEvent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceSyncAttempt

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.ResourceSyncEvent]
- **Required**: Yes

### InitialRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.Revision'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'INITIATED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### TargetRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.Revision'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceSyncEvent

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


# Revision

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


# SyncBlocker

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SyncBlockerContext

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SyncBlockerSummary

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ParentResourceName
- **Type**: typing.Optional[str]

### LatestBlockers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeconnections_classes.SyncBlocker]]


# SyncConfiguration

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

### PullRequestComment
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeconnections_classes.Tag]
- **Required**: Yes


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateHostInput

### HostArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderEndpoint
- **Type**: typing.Optional[str]

### VpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeconnections_classes.VpcConfigurationUnion]


# UpdateRepositoryLinkInput

### RepositoryLinkId
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectionArn
- **Type**: typing.Optional[str]

### EncryptionKeyArn
- **Type**: typing.Optional[str]


# UpdateRepositoryLinkOutput

### RepositoryLinkInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.RepositoryLinkInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSyncBlockerInput

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


# UpdateSyncBlockerOutput

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ParentResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SyncBlocker
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncBlocker'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSyncConfigurationInput

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

### PullRequestComment
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateSyncConfigurationOutput

### SyncConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.SyncConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeconnections_classes.ResponseMetadata'>
- **Required**: Yes


# VpcConfiguration

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


# VpcConfigurationOutput

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### TlsCertificate
- **Type**: typing.Optional[str]


# VpcConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

