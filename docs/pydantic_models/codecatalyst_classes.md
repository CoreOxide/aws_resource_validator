# Codecatalyst Classes

# AccessTokenSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessTokenRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expiresTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.TimestampTypeDef]


# CreateAccessTokenResponseTypeDef

### secret
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expiresTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### accessTokenId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDevEnvironmentRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### instanceType
- **Type**: typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']
- **Required**: Yes

### persistentStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.PersistentStorageConfigurationTypeDef'>
- **Required**: Yes

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.RepositoryInputTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### alias
- **Type**: typing.Optional[str]

### ides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.IdeConfigurationTypeDef]]

### inactivityTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConnectionName
- **Type**: typing.Optional[str]


# CreateProjectRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateProjectResponseTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSourceRepositoryBranchRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### headCommitId
- **Type**: typing.Optional[str]


# CreateSourceRepositoryBranchResponseTypeDef

### ref
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### headCommitId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSourceRepositoryRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateSourceRepositoryResponseTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectResponseTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSourceRepositoryRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceRepositoryResponseTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSpaceRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSpaceResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DevEnvironmentAccessDetailsTypeDef

### streamUrl
- **Type**: <class 'str'>
- **Required**: Yes

### tokenValue
- **Type**: <class 'str'>
- **Required**: Yes


# DevEnvironmentRepositorySummaryTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: typing.Optional[str]


# DevEnvironmentSessionConfigurationTypeDef

### sessionType
- **Type**: typing.Literal['SSH', 'SSM']
- **Required**: Yes

### executeCommandSessionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.ExecuteCommandSessionConfigurationTypeDef]


# DevEnvironmentSessionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DevEnvironmentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmailAddressTypeDef

### email
- **Type**: typing.Optional[str]

### verified
- **Type**: typing.Optional[bool]


# EventLogEntryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventPayloadTypeDef

### contentType
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]


# ExecuteCommandSessionConfigurationTypeDef

### command
- **Type**: <class 'str'>
- **Required**: Yes

### arguments
- **Type**: typing.Optional[typing.Sequence[str]]


# FilterTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Optional[str]


# GetProjectRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectResponseTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSourceRepositoryCloneUrlsRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSourceRepositoryCloneUrlsResponseTypeDef

### https
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSourceRepositoryRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSourceRepositoryResponseTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSpaceRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpaceResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### regionName
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriptionRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionResponseTypeDef

### subscriptionType
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountName
- **Type**: <class 'str'>
- **Required**: Yes

### pendingSubscriptionType
- **Type**: <class 'str'>
- **Required**: Yes

### pendingSubscriptionStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserDetailsResponseTypeDef

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### userName
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### primaryEmail
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.EmailAddressTypeDef'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdeConfigurationTypeDef

### runtime
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# IdeTypeDef

### runtime
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ListAccessTokensRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListAccessTokensRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessTokensResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.AccessTokenSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevEnvironmentSessionsRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### devEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListDevEnvironmentSessionsRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### devEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDevEnvironmentSessionsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentSessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevEnvironmentsRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListDevEnvironmentsRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.FilterTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDevEnvironmentsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEventLogsRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.TimestampTypeDef'>
- **Required**: Yes

### eventName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListEventLogsRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.TimestampTypeDef'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.TimestampTypeDef'>
- **Required**: Yes

### eventName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventLogsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.EventLogEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectListFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListProjectsRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectListFilterTypeDef]]


# ListProjectsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceRepositoriesItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListSourceRepositoriesRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListSourceRepositoriesRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSourceRepositoriesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ListSourceRepositoriesItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceRepositoryBranchesItemTypeDef

### ref
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### headCommitId
- **Type**: typing.Optional[str]


# ListSourceRepositoryBranchesRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListSourceRepositoryBranchesRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListSourceRepositoryBranchesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ListSourceRepositoryBranchesItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListSpacesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.SpaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowRunsRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListWorkflowRunsRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### sortBy
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# ListWorkflowRunsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowRunSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequestPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListWorkflowsRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### sortBy
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# ListWorkflowsResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PersistentStorageConfigurationTypeDef

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# PersistentStorageTypeDef

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# ProjectInformationTypeDef

### name
- **Type**: typing.Optional[str]

### projectId
- **Type**: typing.Optional[str]


# ProjectListFilterTypeDef

### key
- **Type**: typing.Literal['hasAccessTo', 'name']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'EQ', 'GE', 'GT', 'LE', 'LT']]


# ProjectSummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# RepositoryInputTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
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


# SpaceSummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### regionName
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# StartWorkflowRunRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateProjectRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateProjectResponseTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSpaceRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateSpaceResponseTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserIdentityTypeDef

### userType
- **Type**: typing.Literal['AWS_ACCOUNT', 'UNKNOWN', 'USER']
- **Required**: Yes

### principalId
- **Type**: <class 'str'>
- **Required**: Yes

### userName
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]


# VerifySessionResponseTypeDef

### identity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowDefinitionSummaryTypeDef

### path
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowDefinitionTypeDef

### path
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowRunSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

