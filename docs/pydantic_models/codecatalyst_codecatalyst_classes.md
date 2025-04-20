# Codecatalyst Codecatalyst Classes

# AccessTokenSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expiresTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessTokenRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expiresTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PersistentStorageConfiguration'>
- **Required**: Yes

### repositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.RepositoryInput]]

### clientToken
- **Type**: typing.Optional[str]

### alias
- **Type**: typing.Optional[str]

### ides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.IdeConfiguration]]

### inactivityTimeoutMinutes
- **Type**: typing.Optional[int]

### vpcConnectionName
- **Type**: typing.Optional[str]


# CreateDevEnvironmentResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### vpcConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccessTokenRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDevEnvironmentRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDevEnvironmentResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ExecuteCommandSessionConfiguration]


# DevEnvironmentSessionSummary

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### devEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### startedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DevEnvironmentSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### creatorId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETED', 'DELETING', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.DevEnvironmentRepositorySummary]
- **Required**: Yes

### instanceType
- **Type**: typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']
- **Required**: Yes

### inactivityTimeoutMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### persistentStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PersistentStorage'>
- **Required**: Yes

### spaceName
- **Type**: typing.Optional[str]

### projectName
- **Type**: typing.Optional[str]

### statusReason
- **Type**: typing.Optional[str]

### alias
- **Type**: typing.Optional[str]

### ides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.Ide]]

### vpcConnectionName
- **Type**: typing.Optional[str]


# EmailAddress

### email
- **Type**: typing.Optional[str]

### verified
- **Type**: typing.Optional[bool]


# EventLogEntry

### id
- **Type**: <class 'str'>
- **Required**: Yes

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### eventCategory
- **Type**: <class 'str'>
- **Required**: Yes

### eventSource
- **Type**: <class 'str'>
- **Required**: Yes

### eventTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### operationType
- **Type**: typing.Literal['MUTATION', 'READONLY']
- **Required**: Yes

### userIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.UserIdentity'>
- **Required**: Yes

### projectInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ProjectInformation]

### requestId
- **Type**: typing.Optional[str]

### requestPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.EventPayload]

### responsePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.EventPayload]

### errorCode
- **Type**: typing.Optional[str]

### sourceIpAddress
- **Type**: typing.Optional[str]

### userAgent
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.List[str]]


# Filter

### key
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### comparisonOperator
- **Type**: typing.Optional[str]


# GetDevEnvironmentRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevEnvironmentResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### creatorId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETED', 'DELETING', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.DevEnvironmentRepositorySummary]
- **Required**: Yes

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### ides
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.Ide]
- **Required**: Yes

### instanceType
- **Type**: typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']
- **Required**: Yes

### inactivityTimeoutMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### persistentStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PersistentStorage'>
- **Required**: Yes

### vpcConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserDetailsRequest

### id
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.EmailAddress'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceBranchName
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.WorkflowDefinition'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### runMode
- **Type**: typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INVALID']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowRunRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowRunResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABANDONED', 'CANCELLED', 'FAILED', 'IN_PROGRESS', 'NOT_RUN', 'PROVISIONING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'SUPERSEDED', 'VALIDATING']
- **Required**: Yes

### statusReasons
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListAccessTokensResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.AccessTokenSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListDevEnvironmentSessionsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.DevEnvironmentSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.Filter]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListDevEnvironmentsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.DevEnvironmentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEventLogsRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### eventName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListEventLogsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.EventLogEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ProjectListFilter]]


# ListProjectsRequestPaginate

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ProjectListFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListProjectsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ProjectSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSourceRepositoriesItem

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListSourceRepositoriesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ListSourceRepositoriesItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListSourceRepositoryBranchesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ListSourceRepositoryBranchesItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesRequest

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListSpacesResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.SpaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


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
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListWorkflowRunsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.WorkflowRunSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ListWorkflowsRequestPaginate

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### sortBy
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.PaginatorConfig]


# ListWorkflowsResponse

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.WorkflowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: typing.List[str]
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


# StartDevEnvironmentRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.IdeConfiguration]]

### instanceType
- **Type**: typing.Optional[typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']]

### inactivityTimeoutMinutes
- **Type**: typing.Optional[int]


# StartDevEnvironmentResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETED', 'DELETING', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# StartDevEnvironmentSessionRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sessionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.DevEnvironmentSessionConfiguration'>
- **Required**: Yes


# StartDevEnvironmentSessionResponse

### accessDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.DevEnvironmentAccessDetails'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


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


# StartWorkflowRunResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# StopDevEnvironmentRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopDevEnvironmentResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETED', 'DELETING', 'FAILED', 'PENDING', 'RUNNING', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# StopDevEnvironmentSessionRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# StopDevEnvironmentSessionResponse

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDevEnvironmentRequest

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: typing.Optional[str]

### ides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.IdeConfiguration]]

### instanceType
- **Type**: typing.Optional[typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']]

### inactivityTimeoutMinutes
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]


# UpdateDevEnvironmentResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### ides
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.IdeConfiguration]
- **Required**: Yes

### instanceType
- **Type**: typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']
- **Required**: Yes

### inactivityTimeoutMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.ResponseMetadata'>
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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABANDONED', 'CANCELLED', 'FAILED', 'IN_PROGRESS', 'NOT_RUN', 'PROVISIONING', 'STOPPED', 'STOPPING', 'SUCCEEDED', 'SUPERSEDED', 'VALIDATING']
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### statusReasons
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# WorkflowSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceBranchName
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst.codecatalyst_classes.WorkflowDefinitionSummary'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### runMode
- **Type**: typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'INVALID']
- **Required**: Yes


