# Codecatalyst Classes

# AccessTokenSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessTokenRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expiresTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.Timestamp]


# CreateAccessTokenResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDevEnvironmentRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.PersistentStorageConfiguration'>
- **Required**: Yes

### repositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.RepositoryInput]]

### clientToken
- **Type**: typing.Optional[str]

### alias
- **Type**: typing.Optional[str]

### ides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.IdeConfiguration]]

### inactivityTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConnectionName
- **Type**: typing.Optional[str]


# CreateProjectRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateProjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSourceRepositoryBranchRequest

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


# CreateSourceRepositoryBranchResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSourceRepositoryRequest

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


# CreateSourceRepositoryResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProjectRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSourceRepositoryRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceRepositoryResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSpaceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSpaceResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# DevEnvironmentAccessDetails

### streamUrl
- **Type**: <class 'str'>
- **Required**: Yes

### tokenValue
- **Type**: <class 'str'>
- **Required**: Yes


# DevEnvironmentRepositorySummary

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: typing.Optional[str]


# DevEnvironmentSessionConfiguration

### sessionType
- **Type**: typing.Literal['SSH', 'SSM']
- **Required**: Yes

### executeCommandSessionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.ExecuteCommandSessionConfiguration]


# DevEnvironmentSessionSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DevEnvironmentSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EmailAddress

### email
- **Type**: typing.Optional[str]

### verified
- **Type**: typing.Optional[bool]


# EventLogEntry

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventPayload

### contentType
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[str]


# ExecuteCommandSessionConfiguration

### command
- **Type**: <class 'str'>
- **Required**: Yes

### arguments
- **Type**: typing.Optional[typing.Sequence[str]]


# Filter

### key
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Optional[str]


# GetProjectRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetProjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetSourceRepositoryCloneUrlsRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSourceRepositoryCloneUrlsResponse

### https
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetSourceRepositoryRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSourceRepositoryResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetSpaceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpaceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetSubscriptionRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriptionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserDetailsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.EmailAddress'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# Ide

### runtime
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# IdeConfiguration

### runtime
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ListAccessTokensRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessTokensRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListAccessTokensResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.AccessTokenSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevEnvironmentSessionsRequest

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


# ListDevEnvironmentSessionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListDevEnvironmentSessionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDevEnvironmentsRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.Filter]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListDevEnvironmentsRequestPaginate

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListDevEnvironmentsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEventLogsRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.Timestamp'>
- **Required**: Yes

### eventName
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEventLogsRequestPaginate

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.Timestamp'>
- **Required**: Yes

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.Timestamp'>
- **Required**: Yes

### eventName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListEventLogsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.EventLogEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProjectsRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectListFilter]]


# ListProjectsRequestPaginate

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectListFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListProjectsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceRepositoriesItem

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListSourceRepositoriesRequest

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


# ListSourceRepositoriesRequestPaginate

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListSourceRepositoriesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ListSourceRepositoriesItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceRepositoryBranchesItem

### ref
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### headCommitId
- **Type**: typing.Optional[str]


# ListSourceRepositoryBranchesRequest

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


# ListSourceRepositoryBranchesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListSourceRepositoryBranchesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ListSourceRepositoryBranchesItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesRequest

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListSpacesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.SpaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowRunsRequest

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


# ListWorkflowRunsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListWorkflowRunsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowRunSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowsRequest

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


# ListWorkflowsRequestPaginate

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfig]


# ListWorkflowsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PersistentStorage

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# PersistentStorageConfiguration

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# ProjectInformation

### name
- **Type**: typing.Optional[str]

### projectId
- **Type**: typing.Optional[str]


# ProjectListFilter

### key
- **Type**: typing.Literal['hasAccessTo', 'name']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH', 'EQ', 'GE', 'GT', 'LE', 'LT']]


# ProjectSummary

### name
- **Type**: <class 'str'>
- **Required**: Yes

### displayName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# RepositoryInput

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### branchName
- **Type**: typing.Optional[str]


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


# SpaceSummary

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


# StartWorkflowRunRequest

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


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateProjectRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateProjectResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSpaceRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateSpaceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# UserIdentity

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


# VerifySessionResponse

### identity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowDefinition

### path
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowDefinitionSummary

### path
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowRunSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

