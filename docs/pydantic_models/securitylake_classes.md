# securitylake_classes

# AwsIdentityTypeDef

### externalId
- **Type**: <class 'str'>
- **Required**: Yes

### principal
- **Type**: <class 'str'>
- **Required**: Yes


# AwsLogSourceConfigurationTypeDef

### regions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### sourceName
- **Type**: typing.Literal['CLOUD_TRAIL_MGMT', 'EKS_AUDIT', 'LAMBDA_EXECUTION', 'ROUTE53', 'S3_DATA', 'SH_FINDINGS', 'VPC_FLOW', 'WAF']
- **Required**: Yes

### accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### sourceVersion
- **Type**: typing.Optional[str]


# AwsLogSourceResourceTypeDef

### sourceName
- **Type**: typing.Optional[typing.Literal['CLOUD_TRAIL_MGMT', 'EKS_AUDIT', 'LAMBDA_EXECUTION', 'ROUTE53', 'S3_DATA', 'SH_FINDINGS', 'VPC_FLOW', 'WAF']]

### sourceVersion
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAwsLogSourceRequestRequestTypeDef

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.AwsLogSourceConfigurationTypeDef]
- **Required**: Yes


# CreateAwsLogSourceResponseTypeDef

### failed
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCustomLogSourceRequestRequestTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.CustomLogSourceConfigurationTypeDef'>
- **Required**: Yes

### sourceName
- **Type**: <class 'str'>
- **Required**: Yes

### eventClasses
- **Type**: typing.Optional[typing.Sequence[str]]

### sourceVersion
- **Type**: typing.Optional[str]


# CreateCustomLogSourceResponseTypeDef

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.CustomLogSourceResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataLakeExceptionSubscriptionRequestRequestTypeDef

### notificationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionProtocol
- **Type**: <class 'str'>
- **Required**: Yes

### exceptionTimeToLive
- **Type**: typing.Optional[int]


# CreateDataLakeOrganizationConfigurationRequestRequestTypeDef

### autoEnableNewAccount
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationTypeDef, aws_resource_validator.pydantic_models.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationOutputTypeDef]]]


# CreateDataLakeRequestRequestTypeDef

### configurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeConfigurationTypeDef]
- **Required**: Yes

### metaStoreManagerRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.TagTypeDef]]


# CreateDataLakeResponseTypeDef

### dataLakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriberNotificationRequestRequestTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateSubscriberNotificationResponseTypeDef

### subscriberEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSubscriberRequestRequestTypeDef

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.LogSourceResourceTypeDef]
- **Required**: Yes

### subscriberIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.AwsIdentityTypeDef'>
- **Required**: Yes

### subscriberName
- **Type**: <class 'str'>
- **Required**: Yes

### accessTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LAKEFORMATION', 'S3']]]

### subscriberDescription
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.TagTypeDef]]


# CreateSubscriberResponseTypeDef

### subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.SubscriberResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomLogSourceAttributesTypeDef

### crawlerArn
- **Type**: typing.Optional[str]

### databaseArn
- **Type**: typing.Optional[str]

### tableArn
- **Type**: typing.Optional[str]


# CustomLogSourceConfigurationTypeDef

### crawlerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.CustomLogSourceCrawlerConfigurationTypeDef'>
- **Required**: Yes

### providerIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.AwsIdentityTypeDef'>
- **Required**: Yes


# CustomLogSourceCrawlerConfigurationTypeDef

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes


# CustomLogSourceProviderTypeDef

### location
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]


# CustomLogSourceResourceTypeDef

### attributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.CustomLogSourceAttributesTypeDef]

### provider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.CustomLogSourceProviderTypeDef]

### sourceName
- **Type**: typing.Optional[str]

### sourceVersion
- **Type**: typing.Optional[str]


# DataLakeAutoEnableNewAccountConfigurationOutputTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.AwsLogSourceResourceTypeDef]
- **Required**: Yes


# DataLakeAutoEnableNewAccountConfigurationTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.AwsLogSourceResourceTypeDef]
- **Required**: Yes


# DataLakeConfigurationTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeEncryptionConfigurationTypeDef]

### lifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeLifecycleConfigurationTypeDef]

### replicationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeReplicationConfigurationTypeDef]


# DataLakeEncryptionConfigurationTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]


# DataLakeExceptionTypeDef

### exception
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### remediation
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[datetime.datetime]


# DataLakeLifecycleConfigurationOutputTypeDef

### expiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeLifecycleExpirationTypeDef]

### transitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeLifecycleTransitionTypeDef]]


# DataLakeLifecycleConfigurationTypeDef

### expiration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeLifecycleExpirationTypeDef]

### transitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeLifecycleTransitionTypeDef]]


# DataLakeLifecycleExpirationTypeDef

### days
- **Type**: typing.Optional[int]


# DataLakeLifecycleTransitionTypeDef

### days
- **Type**: typing.Optional[int]

### storageClass
- **Type**: typing.Optional[str]


# DataLakeReplicationConfigurationOutputTypeDef

### regions
- **Type**: typing.Optional[typing.List[str]]

### roleArn
- **Type**: typing.Optional[str]


# DataLakeReplicationConfigurationTypeDef

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### roleArn
- **Type**: typing.Optional[str]


# DataLakeResourceTypeDef

### dataLakeArn
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### createStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZED', 'PENDING']]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeEncryptionConfigurationTypeDef]

### lifecycleConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeLifecycleConfigurationOutputTypeDef]

### replicationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeReplicationConfigurationOutputTypeDef]

### s3BucketArn
- **Type**: typing.Optional[str]

### updateStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeUpdateStatusTypeDef]


# DataLakeSourceStatusTypeDef

### resource
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COLLECTING', 'MISCONFIGURED', 'NOT_COLLECTING']]


# DataLakeSourceTypeDef

### account
- **Type**: typing.Optional[str]

### eventClasses
- **Type**: typing.Optional[typing.List[str]]

### sourceName
- **Type**: typing.Optional[str]

### sourceStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeSourceStatusTypeDef]]


# DataLakeUpdateExceptionTypeDef

### code
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# DataLakeUpdateStatusTypeDef

### exception
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeUpdateExceptionTypeDef]

### requestId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'INITIALIZED', 'PENDING']]


# DeleteAwsLogSourceRequestRequestTypeDef

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.AwsLogSourceConfigurationTypeDef]
- **Required**: Yes


# DeleteAwsLogSourceResponseTypeDef

### failed
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCustomLogSourceRequestRequestTypeDef

### sourceName
- **Type**: <class 'str'>
- **Required**: Yes

### sourceVersion
- **Type**: typing.Optional[str]


# DeleteDataLakeOrganizationConfigurationRequestRequestTypeDef

### autoEnableNewAccount
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationTypeDef, aws_resource_validator.pydantic_models.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationOutputTypeDef]]]


# DeleteDataLakeRequestRequestTypeDef

### regions
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteSubscriberNotificationRequestRequestTypeDef

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSubscriberRequestRequestTypeDef

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataLakeExceptionSubscriptionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataLakeOrganizationConfigurationResponseTypeDef

### autoEnableNewAccount
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeAutoEnableNewAccountConfigurationOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataLakeSourcesRequestGetDataLakeSourcesPaginateTypeDef

### accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.PaginatorConfigTypeDef]


# GetDataLakeSourcesRequestRequestTypeDef

### accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetDataLakeSourcesResponseTypeDef

### dataLakeArn
- **Type**: <class 'str'>
- **Required**: Yes

### dataLakeSources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeSourceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSubscriberRequestRequestTypeDef

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSubscriberResponseTypeDef

### subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.SubscriberResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HttpsNotificationConfigurationTypeDef

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


# ListDataLakeExceptionsRequestListDataLakeExceptionsPaginateTypeDef

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.PaginatorConfigTypeDef]


# ListDataLakeExceptionsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]


# ListDataLakeExceptionsResponseTypeDef

### exceptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeExceptionTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataLakesRequestRequestTypeDef

### regions
- **Type**: typing.Optional[typing.Sequence[str]]


# ListDataLakesResponseTypeDef

### dataLakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLogSourcesRequestListLogSourcesPaginateTypeDef

### accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.LogSourceResourceTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.PaginatorConfigTypeDef]


# ListLogSourcesRequestRequestTypeDef

### accounts
- **Type**: typing.Optional[typing.Sequence[str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.LogSourceResourceTypeDef]]


# ListLogSourcesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.LogSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubscribersRequestListSubscribersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.PaginatorConfigTypeDef]


# ListSubscribersRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSubscribersResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### subscribers
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.SubscriberResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogSourceResourceTypeDef

### awsLogSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.AwsLogSourceResourceTypeDef]

### customLogSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.CustomLogSourceResourceTypeDef]


# LogSourceTypeDef

### account
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.securitylake_classes.LogSourceResourceTypeDef]]


# NotificationConfigurationTypeDef

### httpsNotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.HttpsNotificationConfigurationTypeDef]

### sqsNotificationConfiguration
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterDataLakeDelegatedAdministratorRequestRequestTypeDef

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


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


# SubscriberResourceTypeDef

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.LogSourceResourceTypeDef]
- **Required**: Yes

### subscriberArn
- **Type**: <class 'str'>
- **Required**: Yes

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes

### subscriberIdentity
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.AwsIdentityTypeDef'>
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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDataLakeExceptionSubscriptionRequestRequestTypeDef

### notificationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### subscriptionProtocol
- **Type**: <class 'str'>
- **Required**: Yes

### exceptionTimeToLive
- **Type**: typing.Optional[int]


# UpdateDataLakeRequestRequestTypeDef

### configurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeConfigurationTypeDef]
- **Required**: Yes

### metaStoreManagerRoleArn
- **Type**: typing.Optional[str]


# UpdateDataLakeResponseTypeDef

### dataLakes
- **Type**: typing.List[aws_resource_validator.pydantic_models.securitylake_classes.DataLakeResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSubscriberNotificationRequestRequestTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSubscriberNotificationResponseTypeDef

### subscriberEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSubscriberRequestRequestTypeDef

### subscriberId
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.securitylake_classes.LogSourceResourceTypeDef]]

### subscriberDescription
- **Type**: typing.Optional[str]

### subscriberIdentity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.securitylake_classes.AwsIdentityTypeDef]

### subscriberName
- **Type**: typing.Optional[str]


# UpdateSubscriberResponseTypeDef

### subscriber
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.SubscriberResourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.securitylake_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


