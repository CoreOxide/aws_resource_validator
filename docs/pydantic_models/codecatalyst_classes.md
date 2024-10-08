# Pydantic Models in codecatalyst_classes

# AccessTokenSummaryTypeDef

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

# CreateAccessTokenRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expiresTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# CreateDevEnvironmentRequestRequestTypeDef

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


# CreateDevEnvironmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProjectRequestRequestTypeDef

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


# CreateSourceRepositoryBranchRequestRequestTypeDef

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


# CreateSourceRepositoryRequestRequestTypeDef

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


# DeleteAccessTokenRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDevEnvironmentRequestRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDevEnvironmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProjectRequestRequestTypeDef

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


# DeleteSourceRepositoryRequestRequestTypeDef

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


# DeleteSpaceRequestRequestTypeDef

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


# DevEnvironmentSummaryTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentRepositorySummaryTypeDef]
- **Required**: Yes

### instanceType
- **Type**: typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']
- **Required**: Yes

### inactivityTimeoutMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### persistentStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.PersistentStorageTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.IdeTypeDef]]

### vpcConnectionName
- **Type**: typing.Optional[str]


# EmailAddressTypeDef

### email
- **Type**: typing.Optional[str]

### verified
- **Type**: typing.Optional[bool]


# EventLogEntryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.UserIdentityTypeDef'>
- **Required**: Yes

### projectInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectInformationTypeDef]

### requestId
- **Type**: typing.Optional[str]

### requestPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.EventPayloadTypeDef]

### responsePayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.EventPayloadTypeDef]

### errorCode
- **Type**: typing.Optional[str]

### sourceIpAddress
- **Type**: typing.Optional[str]

### userAgent
- **Type**: typing.Optional[str]


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


# GetDevEnvironmentRequestRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetDevEnvironmentResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentRepositorySummaryTypeDef]
- **Required**: Yes

### alias
- **Type**: <class 'str'>
- **Required**: Yes

### ides
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.IdeTypeDef]
- **Required**: Yes

### instanceType
- **Type**: typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']
- **Required**: Yes

### inactivityTimeoutMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### persistentStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.PersistentStorageTypeDef'>
- **Required**: Yes

### vpcConnectionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProjectRequestRequestTypeDef

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


# GetSourceRepositoryCloneUrlsRequestRequestTypeDef

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


# GetSourceRepositoryRequestRequestTypeDef

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


# GetSpaceRequestRequestTypeDef

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


# GetSubscriptionRequestRequestTypeDef

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


# GetUserDetailsRequestRequestTypeDef

### id
- **Type**: typing.Optional[str]

### userName
- **Type**: typing.Optional[str]


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


# GetWorkflowRequestRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowDefinitionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowRunRequestRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowRunResponseTypeDef

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


# ListAccessTokensRequestListAccessTokensPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListAccessTokensRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAccessTokensResponseTypeDef

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.AccessTokenSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevEnvironmentSessionsRequestListDevEnvironmentSessionsPaginateTypeDef

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


# ListDevEnvironmentSessionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDevEnvironmentsRequestListDevEnvironmentsPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: typing.Optional[str]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListDevEnvironmentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventLogsRequestListEventLogsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListEventLogsRequestRequestTypeDef

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


# ListEventLogsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.EventLogEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProjectsRequestListProjectsPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectListFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListProjectsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ProjectSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSourceRepositoriesItemTypeDef

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


# ListSourceRepositoriesRequestListSourceRepositoriesPaginateTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListSourceRepositoriesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSourceRepositoryBranchesItemTypeDef

### ref
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### headCommitId
- **Type**: typing.Optional[str]


# ListSourceRepositoryBranchesRequestListSourceRepositoryBranchesPaginateTypeDef

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


# ListSourceRepositoryBranchesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.ListSourceRepositoryBranchesItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSpacesRequestListSpacesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codecatalyst_classes.PaginatorConfigTypeDef]


# ListSpacesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]


# ListSpacesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.SpaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowRunsRequestListWorkflowRunsPaginateTypeDef

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


# ListWorkflowRunsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowRunSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowsRequestListWorkflowsPaginateTypeDef

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


# ListWorkflowsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### items
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StartDevEnvironmentRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.IdeConfigurationTypeDef]]

### instanceType
- **Type**: typing.Optional[typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']]

### inactivityTimeoutMinutes
- **Type**: typing.Optional[int]


# StartDevEnvironmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartDevEnvironmentSessionRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentSessionConfigurationTypeDef'>
- **Required**: Yes


# StartDevEnvironmentSessionResponseTypeDef

### accessDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.DevEnvironmentAccessDetailsTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartWorkflowRunRequestRequestTypeDef

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


# StartWorkflowRunResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDevEnvironmentRequestRequestTypeDef

### spaceName
- **Type**: <class 'str'>
- **Required**: Yes

### projectName
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopDevEnvironmentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDevEnvironmentSessionRequestRequestTypeDef

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


# StopDevEnvironmentSessionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDevEnvironmentRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codecatalyst_classes.IdeConfigurationTypeDef]]

### instanceType
- **Type**: typing.Optional[typing.Literal['dev.standard1.large', 'dev.standard1.medium', 'dev.standard1.small', 'dev.standard1.xlarge']]

### inactivityTimeoutMinutes
- **Type**: typing.Optional[int]

### clientToken
- **Type**: typing.Optional[str]


# UpdateDevEnvironmentResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codecatalyst_classes.IdeConfigurationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProjectRequestRequestTypeDef

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


# UpdateSpaceRequestRequestTypeDef

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


# WorkflowSummaryTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codecatalyst_classes.WorkflowDefinitionSummaryTypeDef'>
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


