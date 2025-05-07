# Appfabric Classes

# ApiKeyCredential

### apiKey
- **Type**: <class 'str'>
- **Required**: Yes


# AppAuthorization

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tenant'>
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


# AppAuthorizationSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tenant'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Connected', 'ConnectionValidationFailed', 'PendingConnect', 'TokenAutoRotationFailed']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AppBundle

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### customerManagedKeyArn
- **Type**: typing.Optional[str]


# AppBundleSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# AuditLogDestinationConfiguration

### destination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Destination'>
- **Required**: Yes


# AuditLogProcessingConfiguration

### schema
- **Type**: typing.Literal['ocsf', 'raw']
- **Default**: <bound method BaseModel.schema of <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AuditLogProcessingConfiguration'>>

### format
- **Type**: typing.Literal['json', 'parquet']
- **Required**: Yes


# AuthRequest

### redirectUri
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetUserAccessTasksRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### taskIdList
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetUserAccessTasksResponse

### userAccessResultsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.UserAccessResultItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# ConnectAppAuthorizationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### authRequest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AuthRequest]


# ConnectAppAuthorizationResponse

### appAuthorizationSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppAuthorizationSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppAuthorizationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### app
- **Type**: <class 'str'>
- **Required**: Yes

### credential
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Credential'>
- **Required**: Yes

### tenant
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tenant'>
- **Required**: Yes

### authType
- **Type**: typing.Literal['apiKey', 'oauth2']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tag]]


# CreateAppAuthorizationResponse

### appAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppAuthorization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppBundleRequest

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKeyIdentifier
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tag]]


# CreateAppBundleResponse

### appBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppBundle'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIngestionDestinationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### processingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ProcessingConfiguration'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.DestinationConfiguration'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tag]]


# CreateIngestionDestinationResponse

### ingestionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.IngestionDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIngestionRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tag]]


# CreateIngestionResponse

### ingestion
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Ingestion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# Credential

### oauth2Credential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Oauth2Credential]

### apiKeyCredential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ApiKeyCredential]


# DeleteAppAuthorizationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppBundleRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngestionDestinationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionDestinationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngestionRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# Destination

### s3Bucket
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.S3Bucket]

### firehoseStream
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.FirehoseStream]


# DestinationConfiguration

### auditLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AuditLogDestinationConfiguration]


# FirehoseStream

### streamName
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppAuthorizationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppAuthorizationResponse

### appAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppAuthorization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# GetAppBundleRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppBundleResponse

### appBundle
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppBundle'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# GetIngestionDestinationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionDestinationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionDestinationResponse

### ingestionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.IngestionDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# GetIngestionRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionResponse

### ingestion
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Ingestion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# Ingestion

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


# IngestionDestination

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionArn
- **Type**: <class 'str'>
- **Required**: Yes

### processingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ProcessingConfiguration'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.DestinationConfiguration'>
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Failed']]

### statusReason
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# IngestionDestinationSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# IngestionSummary

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


# ListAppAuthorizationsRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppAuthorizationsRequestPaginate

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.PaginatorConfig]


# ListAppAuthorizationsResponse

### appAuthorizationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppAuthorizationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAppBundlesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAppBundlesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.PaginatorConfig]


# ListAppBundlesResponse

### appBundleSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppBundleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionDestinationsRequest

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


# ListIngestionDestinationsRequestPaginate

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.PaginatorConfig]


# ListIngestionDestinationsResponse

### ingestionDestinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.IngestionDestinationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionsRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionsRequestPaginate

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.PaginatorConfig]


# ListIngestionsResponse

### ingestions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.IngestionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# Oauth2Credential

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProcessingConfiguration

### auditLog
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AuditLogProcessingConfiguration]


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


# S3Bucket

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# StartIngestionRequest

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# StartUserAccessTasksRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### email
- **Type**: <class 'str'>
- **Required**: Yes


# StartUserAccessTasksResponse

### userAccessTasksList
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.UserAccessTaskItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# StopIngestionRequest

### ingestionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tag]
- **Required**: Yes


# TaskError

### errorCode
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# Tenant

### tenantIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### tenantDisplayName
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAppAuthorizationRequest

### appBundleIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### appAuthorizationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### credential
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Credential]

### tenant
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.Tenant]


# UpdateAppAuthorizationResponse

### appAuthorization
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.AppAuthorization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIngestionDestinationRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.DestinationConfiguration'>
- **Required**: Yes


# UpdateIngestionDestinationResponse

### ingestionDestination
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.IngestionDestination'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appfabric.appfabric_classes.ResponseMetadata'>
- **Required**: Yes


# UserAccessResultItem

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.TaskError]


# UserAccessTaskItem

### app
- **Type**: <class 'str'>
- **Required**: Yes

### tenantId
- **Type**: <class 'str'>
- **Required**: Yes

### taskId
- **Type**: typing.Optional[str]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appfabric.appfabric_classes.TaskError]


