# Appfabric Classes

# ApiKeyCredentialTypeDef

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes


# AppAuthorizationSummaryTypeDef

### appAuthorizationArn
- **Type**: <class 'str'>
- **Required**: Yes

### appBundleArn
- **Type**: <class 'str'>
- **Required**: Yes

### app
- **Type**: <class 'str'>
- **Required**: Yes

### tenant
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.TenantTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Connected', 'ConnectionValidationFailed', 'PendingConnect', 'TokenAutoRotationFailed']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AppAuthorizationTypeDef

### appAuthorizationArn
- **Type**: <class 'str'>
- **Required**: Yes

### appBundleArn
- **Type**: <class 'str'>
- **Required**: Yes

### app
- **Type**: <class 'str'>
- **Required**: Yes

### tenant
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.TenantTypeDef'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['apiKey', 'oauth2']
- **Required**: Yes

### status
- **Type**: typing.Literal['Connected', 'ConnectionValidationFailed', 'PendingConnect', 'TokenAutoRotationFailed']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### persona
- **Type**: typing.Optional[typing.Literal['admin', 'endUser']]

### authUrl
- **Type**: typing.Optional[str]


# AppBundleSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# AppBundleTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### customerManagedKeyArn
- **Type**: typing.Optional[str]


# AuditLogDestinationConfigurationTypeDef

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.DestinationTypeDef'>
- **Required**: Yes


# AuditLogProcessingConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthRequestTypeDef

### redirectUri
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetUserAccessTasksRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### taskIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetUserAccessTasksResponseTypeDef

### userAccessResultsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric_classes.UserAccessResultItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConnectAppAuthorizationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### authRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.AuthRequestTypeDef]


# ConnectAppAuthorizationResponseTypeDef

### appAuthorizationSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.AppAuthorizationSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppAuthorizationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### app
- **Type**: <class 'str'>
- **Required**: Yes

### credential
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.CredentialTypeDef'>
- **Required**: Yes

### tenant
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.TenantTypeDef'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['apiKey', 'oauth2']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appfabric_classes.TagTypeDef]]


# CreateAppAuthorizationResponseTypeDef

### appAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.AppAuthorizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppBundleRequestTypeDef

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKeyIdentifier
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appfabric_classes.TagTypeDef]]


# CreateAppBundleResponseTypeDef

### appBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.AppBundleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIngestionDestinationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### processingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ProcessingConfigurationTypeDef'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appfabric_classes.TagTypeDef]]


# CreateIngestionDestinationResponseTypeDef

### ingestionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.IngestionDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIngestionRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### app
- **Type**: <class 'str'>
- **Required**: Yes

### tenantId
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionType
- **Type**: typing.Literal['auditLog']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appfabric_classes.TagTypeDef]]


# CreateIngestionResponseTypeDef

### ingestion
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.IngestionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialTypeDef

### oauth2Credential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.Oauth2CredentialTypeDef]

### apiKeyCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.ApiKeyCredentialTypeDef]


# DeleteAppAuthorizationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppBundleRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngestionDestinationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionDestinationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngestionRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfigurationTypeDef

### auditLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.AuditLogDestinationConfigurationTypeDef]


# DestinationTypeDef

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.S3BucketTypeDef]

### firehoseStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.FirehoseStreamTypeDef]


# FirehoseStreamTypeDef

### streamName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppAuthorizationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppAuthorizationResponseTypeDef

### appAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.AppAuthorizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppBundleRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppBundleResponseTypeDef

### appBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.AppBundleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIngestionDestinationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionDestinationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionDestinationResponseTypeDef

### ingestionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.IngestionDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIngestionRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionResponseTypeDef

### ingestion
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.IngestionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IngestionDestinationSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# IngestionDestinationTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionArn
- **Type**: <class 'str'>
- **Required**: Yes

### processingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ProcessingConfigurationTypeDef'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Failed']]

### statusReason
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# IngestionSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### app
- **Type**: <class 'str'>
- **Required**: Yes

### tenantId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['disabled', 'enabled']
- **Required**: Yes


# IngestionTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### appBundleArn
- **Type**: <class 'str'>
- **Required**: Yes

### app
- **Type**: <class 'str'>
- **Required**: Yes

### tenantId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### state
- **Type**: typing.Literal['disabled', 'enabled']
- **Required**: Yes

### ingestionType
- **Type**: typing.Literal['auditLog']
- **Required**: Yes


# ListAppAuthorizationsRequestPaginateTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.PaginatorConfigTypeDef]


# ListAppAuthorizationsRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppAuthorizationsResponseTypeDef

### appAuthorizationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric_classes.AppAuthorizationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppBundlesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.PaginatorConfigTypeDef]


# ListAppBundlesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppBundlesResponseTypeDef

### appBundleSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric_classes.AppBundleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionDestinationsRequestPaginateTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.PaginatorConfigTypeDef]


# ListIngestionDestinationsRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionDestinationsResponseTypeDef

### ingestionDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric_classes.IngestionDestinationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionsRequestPaginateTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.PaginatorConfigTypeDef]


# ListIngestionsRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionsResponseTypeDef

### ingestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric_classes.IngestionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# Oauth2CredentialTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProcessingConfigurationTypeDef

### auditLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.AuditLogProcessingConfigurationTypeDef]


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


# S3BucketTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# StartIngestionRequestTypeDef

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartUserAccessTasksRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes


# StartUserAccessTasksResponseTypeDef

### userAccessTasksList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric_classes.UserAccessTaskItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopIngestionRequestTypeDef

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.appfabric_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TaskErrorTypeDef

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# TenantTypeDef

### tenantIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### tenantDisplayName
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppAuthorizationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### credential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.CredentialTypeDef]

### tenant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.TenantTypeDef]


# UpdateAppAuthorizationResponseTypeDef

### appAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.AppAuthorizationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIngestionDestinationRequestTypeDef

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionDestinationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes


# UpdateIngestionDestinationResponseTypeDef

### ingestionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.IngestionDestinationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserAccessResultItemTypeDef

### app
- **Type**: typing.Optional[str]

### tenantId
- **Type**: typing.Optional[str]

### tenantDisplayName
- **Type**: typing.Optional[str]

### taskId
- **Type**: typing.Optional[str]

### resultStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'EXPIRED', 'FAILED', 'IN_PROGRESS']]

### email
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### userFullName
- **Type**: typing.Optional[str]

### userFirstName
- **Type**: typing.Optional[str]

### userLastName
- **Type**: typing.Optional[str]

### userStatus
- **Type**: typing.Optional[str]

### taskError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.TaskErrorTypeDef]


# UserAccessTaskItemTypeDef

### app
- **Type**: <class 'str'>
- **Required**: Yes

### tenantId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: typing.Optional[str]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric_classes.TaskErrorTypeDef]


