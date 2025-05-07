# Securitylake Classes

# AwsIdentity

### externalId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# AwsLogSourceConfiguration

### regions
- **Type**: typing.List[str]
- **Required**: Yes

### sourceName
- **Type**: typing.Literal['CLOUD_TRAIL_MGMT', 'EKS_AUDIT', 'LAMBDA_EXECUTION', 'ROUTE53', 'S3_DATA', 'SH_FINDINGS', 'VPC_FLOW', 'WAF']
- **Required**: Yes

### accounts
- **Type**: typing.Optional[typing.List[str]]

### sourceVersion
- **Type**: typing.Optional[str]


# AwsLogSourceResource

### sourceName
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL_MGMT', 'EKS_AUDIT', 'LAMBDA_EXECUTION', 'ROUTE53', 'S3_DATA', 'SH_FINDINGS', 'VPC_FLOW', 'WAF']]

### sourceVersion
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAwsLogSourceRequest

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsLogSourceConfiguration]
- **Required**: Yes


# CreateAwsLogSourceResponse

### failed
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCustomLogSourceRequest

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.CustomLogSourceConfiguration'>
- **Required**: Yes

### sourceName
- **Type**: <class 'str'>
- **Required**: Yes

### eventClasses
- **Type**: typing.Optional[typing.List[str]]

### sourceVersion
- **Type**: typing.Optional[str]


# CreateCustomLogSourceResponse

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.CustomLogSourceResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataLakeExceptionSubscriptionRequest

### notificationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionProtocol
- **Type**: <class 'str'>
- **Required**: Yes

### exceptionTimeToLive
- **Type**: typing.Optional[int]


# CreateDataLakeOrganizationConfigurationRequest

### autoEnableNewAccount
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeAutoEnableNewAccountConfiguration, aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationOutput]]]


# CreateDataLakeRequest

### configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeConfiguration]
- **Required**: Yes

### metaStoreManagerRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.Tag]]


# CreateDataLakeResponse

### dataLakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriberNotificationRequest

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.NotificationConfiguration'>
- **Required**: Yes

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSubscriberNotificationResponse

### subscriberEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSubscriberRequest

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.LogSourceResource]
- **Required**: Yes

### subscriberIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsIdentity'>
- **Required**: Yes

### subscriberName
- **Type**: <class 'str'>
- **Required**: Yes

### accessTypes
- **Type**: typing.Optional[typing.List[typing.Literal['LAKEFORMATION', 'S3']]]

### subscriberDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.Tag]]


# CreateSubscriberResponse

### subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.SubscriberResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# CustomLogSourceAttributes

### crawlerArn
- **Type**: typing.Optional[str]

### databaseArn
- **Type**: typing.Optional[str]

### tableArn
- **Type**: typing.Optional[str]


# CustomLogSourceConfiguration

### crawlerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.CustomLogSourceCrawlerConfiguration'>
- **Required**: Yes

### providerIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsIdentity'>
- **Required**: Yes


# CustomLogSourceCrawlerConfiguration

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# CustomLogSourceProvider

### location
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# CustomLogSourceResource

### attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.CustomLogSourceAttributes]

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.CustomLogSourceProvider]

### sourceName
- **Type**: typing.Optional[str]

### sourceVersion
- **Type**: typing.Optional[str]


# DataLakeAutoEnableNewAccountConfiguration

### region
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsLogSourceResource]
- **Required**: Yes


# DataLakeAutoEnableNewAccountConfigurationOutput

### region
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsLogSourceResource]
- **Required**: Yes


# DataLakeConfiguration

### region
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeEncryptionConfiguration]

### lifecycleConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeLifecycleConfiguration, aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeLifecycleConfigurationOutput, NoneType]

### replicationConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeReplicationConfiguration, aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeReplicationConfigurationOutput, NoneType]


# DataLakeEncryptionConfiguration

### kmsKeyId
- **Type**: typing.Optional[str]


# DataLakeException

### exception
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### remediation
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[datetime.datetime]


# DataLakeLifecycleConfiguration

### expiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeLifecycleExpiration]

### transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeLifecycleTransition]]


# DataLakeLifecycleConfigurationOutput

### expiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeLifecycleExpiration]

### transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeLifecycleTransition]]


# DataLakeLifecycleExpiration

### days
- **Type**: typing.Optional[int]


# DataLakeLifecycleTransition

### days
- **Type**: typing.Optional[int]

### storageClass
- **Type**: typing.Optional[str]


# DataLakeReplicationConfiguration

### regions
- **Type**: typing.Optional[typing.List[str]]

### roleArn
- **Type**: typing.Optional[str]


# DataLakeReplicationConfigurationOutput

### regions
- **Type**: typing.Optional[typing.List[str]]

### roleArn
- **Type**: typing.Optional[str]


# DataLakeResource

### dataLakeArn
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### createStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZED', 'PENDING']]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeEncryptionConfiguration]

### lifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeLifecycleConfigurationOutput]

### replicationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeReplicationConfigurationOutput]

### s3BucketArn
- **Type**: typing.Optional[str]

### updateStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeUpdateStatus]


# DataLakeSource

### account
- **Type**: typing.Optional[str]

### eventClasses
- **Type**: typing.Optional[typing.List[str]]

### sourceName
- **Type**: typing.Optional[str]

### sourceStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeSourceStatus]]


# DataLakeSourceStatus

### resource
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COLLECTING', 'MISCONFIGURED', 'NOT_COLLECTING']]


# DataLakeUpdateException

### code
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# DataLakeUpdateStatus

### exception
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeUpdateException]

### requestId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZED', 'PENDING']]


# DeleteAwsLogSourceRequest

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsLogSourceConfiguration]
- **Required**: Yes


# DeleteAwsLogSourceResponse

### failed
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCustomLogSourceRequest

### sourceName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceVersion
- **Type**: typing.Optional[str]


# DeleteDataLakeOrganizationConfigurationRequest

### autoEnableNewAccount
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeAutoEnableNewAccountConfiguration, aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationOutput]]]


# DeleteDataLakeRequest

### regions
- **Type**: typing.List[str]
- **Required**: Yes


# DeleteSubscriberNotificationRequest

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriberRequest

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataLakeExceptionSubscriptionResponse

### exceptionTimeToLive
- **Type**: <class 'int'>
- **Required**: Yes

### notificationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionProtocol
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataLakeOrganizationConfigurationResponse

### autoEnableNewAccount
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataLakeSourcesRequest

### accounts
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetDataLakeSourcesRequestPaginate

### accounts
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.PaginatorConfig]


# GetDataLakeSourcesResponse

### dataLakeArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataLakeSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetSubscriberRequest

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriberResponse

### subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.SubscriberResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# HttpsNotificationConfiguration

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### targetRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### authorizationApiKeyName
- **Type**: typing.Optional[str]

### authorizationApiKeyValue
- **Type**: typing.Optional[str]

### httpMethod
- **Type**: typing.Optional[typing.Literal['POST', 'PUT']]


# ListDataLakeExceptionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### regions
- **Type**: typing.Optional[typing.List[str]]


# ListDataLakeExceptionsRequestPaginate

### regions
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.PaginatorConfig]


# ListDataLakeExceptionsResponse

### exceptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeException]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataLakesRequest

### regions
- **Type**: typing.Optional[typing.List[str]]


# ListDataLakesResponse

### dataLakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# ListLogSourcesRequest

### accounts
- **Type**: typing.Optional[typing.List[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### regions
- **Type**: typing.Optional[typing.List[str]]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.LogSourceResource]]


# ListLogSourcesRequestPaginate

### accounts
- **Type**: typing.Optional[typing.List[str]]

### regions
- **Type**: typing.Optional[typing.List[str]]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.LogSourceResource]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.PaginatorConfig]


# ListLogSourcesResponse

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.LogSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubscribersRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSubscribersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.PaginatorConfig]


# ListSubscribersResponse

### subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.SubscriberResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# LogSource

### account
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.LogSourceResource]]


# LogSourceResource

### awsLogSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsLogSourceResource]

### customLogSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.CustomLogSourceResource]


# NotificationConfiguration

### httpsNotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.HttpsNotificationConfiguration]

### sqsNotificationConfiguration
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterDataLakeDelegatedAdministratorRequest

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


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


# SubscriberResource

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.LogSourceResource]
- **Required**: Yes

### subscriberArn
- **Type**: <class 'str'>
- **Required**: Yes

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriberIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsIdentity'>
- **Required**: Yes

### subscriberName
- **Type**: <class 'str'>
- **Required**: Yes

### accessTypes
- **Type**: typing.Optional[typing.List[typing.Literal['LAKEFORMATION', 'S3']]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### resourceShareArn
- **Type**: typing.Optional[str]

### resourceShareName
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### s3BucketArn
- **Type**: typing.Optional[str]

### subscriberDescription
- **Type**: typing.Optional[str]

### subscriberEndpoint
- **Type**: typing.Optional[str]

### subscriberStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEACTIVATED', 'PENDING', 'READY']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDataLakeExceptionSubscriptionRequest

### notificationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionProtocol
- **Type**: <class 'str'>
- **Required**: Yes

### exceptionTimeToLive
- **Type**: typing.Optional[int]


# UpdateDataLakeRequest

### configurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeConfiguration]
- **Required**: Yes

### metaStoreManagerRoleArn
- **Type**: typing.Optional[str]


# UpdateDataLakeResponse

### dataLakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.DataLakeResource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubscriberNotificationRequest

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.NotificationConfiguration'>
- **Required**: Yes

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSubscriberNotificationResponse

### subscriberEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSubscriberRequest

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.LogSourceResource]]

### subscriberDescription
- **Type**: typing.Optional[str]

### subscriberIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake.securitylake_classes.AwsIdentity]

### subscriberName
- **Type**: typing.Optional[str]


# UpdateSubscriberResponse

### subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.SubscriberResource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake.securitylake_classes.ResponseMetadata'>
- **Required**: Yes


