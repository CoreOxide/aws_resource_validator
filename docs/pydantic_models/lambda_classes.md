# Pydantic Models in lambda_classes

# AccountLimitTypeDef

### TotalCodeSize
- **Type**: typing.Optional[int]

### CodeSizeUnzipped
- **Type**: typing.Optional[int]

### CodeSizeZipped
- **Type**: typing.Optional[int]

### ConcurrentExecutions
- **Type**: typing.Optional[int]

### UnreservedConcurrentExecutions
- **Type**: typing.Optional[int]


# AccountUsageTypeDef

### TotalCodeSize
- **Type**: typing.Optional[int]

### FunctionCount
- **Type**: typing.Optional[int]


# AddLayerVersionPermissionRequestRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### StatementId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# AddLayerVersionPermissionResponseTypeDef

### Statement
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddPermissionRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### StatementId
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'str'>
- **Required**: Yes

### Principal
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: typing.Optional[str]

### SourceAccount
- **Type**: typing.Optional[str]

### EventSourceToken
- **Type**: typing.Optional[str]

### Qualifier
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]

### PrincipalOrgID
- **Type**: typing.Optional[str]

### FunctionUrlAuthType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]


# AddPermissionResponseTypeDef

### Statement
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AliasConfigurationPaginatorTypeDef

### AliasArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationPaginatorTypeDef]

### RevisionId
- **Type**: typing.Optional[str]


# AliasConfigurationResponseTypeDef

### AliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RoutingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationTypeDef'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AliasConfigurationTypeDef

### AliasArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationTypeDef]

### RevisionId
- **Type**: typing.Optional[str]


# AliasRoutingConfigurationPaginatorTypeDef

### AdditionalVersionWeights
- **Type**: typing.Optional[typing.Dict[str, float]]


# AliasRoutingConfigurationTypeDef

### AdditionalVersionWeights
- **Type**: typing.Optional[typing.Mapping[str, float]]


# AllowedPublishersPaginatorTypeDef

### SigningProfileVersionArns
- **Type**: typing.List[str]
- **Required**: Yes


# AllowedPublishersTypeDef

### SigningProfileVersionArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AmazonManagedKafkaEventSourceConfigTypeDef

### ConsumerGroupId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeSigningConfigPaginatorTypeDef

### CodeSigningConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### AllowedPublishers
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AllowedPublishersPaginatorTypeDef'>
- **Required**: Yes

### CodeSigningPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CodeSigningPoliciesTypeDef'>
- **Required**: Yes

### LastModified
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CodeSigningConfigTypeDef

### CodeSigningConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### AllowedPublishers
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AllowedPublishersTypeDef'>
- **Required**: Yes

### CodeSigningPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CodeSigningPoliciesTypeDef'>
- **Required**: Yes

### LastModified
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CodeSigningPoliciesTypeDef

### UntrustedArtifactOnDeployment
- **Type**: typing.Optional[typing.Literal['Enforce', 'Warn']]


# ConcurrencyResponseTypeDef

### ReservedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConcurrencyTypeDef

### ReservedConcurrentExecutions
- **Type**: typing.Optional[int]


# CorsPaginatorTypeDef

### AllowCredentials
- **Type**: typing.Optional[bool]

### AllowHeaders
- **Type**: typing.Optional[typing.List[str]]

### AllowMethods
- **Type**: typing.Optional[typing.List[str]]

### AllowOrigins
- **Type**: typing.Optional[typing.List[str]]

### ExposeHeaders
- **Type**: typing.Optional[typing.List[str]]

### MaxAge
- **Type**: typing.Optional[int]


# CorsTypeDef

### AllowCredentials
- **Type**: typing.Optional[bool]

### AllowHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowMethods
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowOrigins
- **Type**: typing.Optional[typing.Sequence[str]]

### ExposeHeaders
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxAge
- **Type**: typing.Optional[int]


# CreateAliasRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationTypeDef]


# CreateCodeSigningConfigRequestRequestTypeDef

### AllowedPublishers
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AllowedPublishersTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CodeSigningPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CodeSigningPoliciesTypeDef]


# CreateCodeSigningConfigResponseTypeDef

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CodeSigningConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventSourceMappingRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceArn
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### BatchSize
- **Type**: typing.Optional[int]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaTypeDef]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### StartingPosition
- **Type**: typing.Optional[typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']]

### StartingPositionTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### BisectBatchOnFunctionError
- **Type**: typing.Optional[bool]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### TumblingWindowInSeconds
- **Type**: typing.Optional[int]

### Topics
- **Type**: typing.Optional[typing.Sequence[str]]

### Queues
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lambda_classes.SourceAccessConfigurationTypeDef]]

### SelfManagedEventSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedEventSourceTypeDef]

### FunctionResponseTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ReportBatchItemFailures']]]

### AmazonManagedKafkaEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AmazonManagedKafkaEventSourceConfigTypeDef]

### SelfManagedKafkaEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedKafkaEventSourceConfigTypeDef]

### ScalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ScalingConfigTypeDef]

### DocumentDBEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DocumentDBEventSourceConfigTypeDef]


# CreateFunctionRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.FunctionCodeTypeDef'>
- **Required**: Yes

### Runtime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### Handler
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### MemorySize
- **Type**: typing.Optional[int]

### Publish
- **Type**: typing.Optional[bool]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.VpcConfigTypeDef]

### PackageType
- **Type**: typing.Optional[typing.Literal['Image', 'Zip']]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DeadLetterConfigTypeDef]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EnvironmentTypeDef]

### KMSKeyArn
- **Type**: typing.Optional[str]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.TracingConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Layers
- **Type**: typing.Optional[typing.Sequence[str]]

### FileSystemConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lambda_classes.FileSystemConfigTypeDef]]

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigTypeDef]

### CodeSigningConfigArn
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['arm64', 'x86_64']]]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EphemeralStorageTypeDef]

### SnapStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SnapStartTypeDef]

### LoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.LoggingConfigTypeDef]


# CreateFunctionUrlConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### Cors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CorsTypeDef]

### InvokeMode
- **Type**: typing.Optional[typing.Literal['BUFFERED', 'RESPONSE_STREAM']]


# CreateFunctionUrlConfigResponseTypeDef

### FunctionUrl
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Cors
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CorsTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### InvokeMode
- **Type**: typing.Literal['BUFFERED', 'RESPONSE_STREAM']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeadLetterConfigTypeDef

### TargetArn
- **Type**: typing.Optional[str]


# DeleteAliasRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCodeSigningConfigRequestRequestTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSourceMappingRequestRequestTypeDef

### UUID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionCodeSigningConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionConcurrencyRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionEventInvokeConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteFunctionRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteFunctionUrlConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteLayerVersionRequestRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteProvisionedConcurrencyConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfigTypeDef

### OnSuccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.OnSuccessTypeDef]

### OnFailure
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.OnFailureTypeDef]


# DocumentDBEventSourceConfigTypeDef

### DatabaseName
- **Type**: typing.Optional[str]

### CollectionName
- **Type**: typing.Optional[str]

### FullDocument
- **Type**: typing.Optional[typing.Literal['Default', 'UpdateLookup']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# EnvironmentResponseTypeDef

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EnvironmentErrorTypeDef]


# EnvironmentTypeDef

### Variables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# EphemeralStorageTypeDef

### Size
- **Type**: <class 'int'>
- **Required**: Yes


# EventSourceMappingConfigurationPaginatorTypeDef

### UUID
- **Type**: typing.Optional[str]

### StartingPosition
- **Type**: typing.Optional[typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']]

### StartingPositionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### EventSourceArn
- **Type**: typing.Optional[str]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaPaginatorTypeDef]

### FunctionArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LastProcessingResult
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### StateTransitionReason
- **Type**: typing.Optional[str]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]

### Topics
- **Type**: typing.Optional[typing.List[str]]

### Queues
- **Type**: typing.Optional[typing.List[str]]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.SourceAccessConfigurationTypeDef]]

### SelfManagedEventSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedEventSourcePaginatorTypeDef]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### BisectBatchOnFunctionError
- **Type**: typing.Optional[bool]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### TumblingWindowInSeconds
- **Type**: typing.Optional[int]

### FunctionResponseTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ReportBatchItemFailures']]]

### AmazonManagedKafkaEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AmazonManagedKafkaEventSourceConfigTypeDef]

### SelfManagedKafkaEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedKafkaEventSourceConfigTypeDef]

### ScalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ScalingConfigTypeDef]

### DocumentDBEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DocumentDBEventSourceConfigTypeDef]


# EventSourceMappingConfigurationResponseTypeDef

### UUID
- **Type**: <class 'str'>
- **Required**: Yes

### StartingPosition
- **Type**: typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### StartingPositionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### BatchSize
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumBatchingWindowInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### ParallelizationFactor
- **Type**: <class 'int'>
- **Required**: Yes

### EventSourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### FilterCriteria
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaTypeDef'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastProcessingResult
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### StateTransitionReason
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef'>
- **Required**: Yes

### Topics
- **Type**: typing.List[str]
- **Required**: Yes

### Queues
- **Type**: typing.List[str]
- **Required**: Yes

### SourceAccessConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.SourceAccessConfigurationTypeDef]
- **Required**: Yes

### SelfManagedEventSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.SelfManagedEventSourceTypeDef'>
- **Required**: Yes

### MaximumRecordAgeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### BisectBatchOnFunctionError
- **Type**: <class 'bool'>
- **Required**: Yes

### MaximumRetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### TumblingWindowInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### FunctionResponseTypes
- **Type**: typing.List[typing.Literal['ReportBatchItemFailures']]
- **Required**: Yes

### AmazonManagedKafkaEventSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AmazonManagedKafkaEventSourceConfigTypeDef'>
- **Required**: Yes

### SelfManagedKafkaEventSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.SelfManagedKafkaEventSourceConfigTypeDef'>
- **Required**: Yes

### ScalingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ScalingConfigTypeDef'>
- **Required**: Yes

### DocumentDBEventSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.DocumentDBEventSourceConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventSourceMappingConfigurationTypeDef

### UUID
- **Type**: typing.Optional[str]

### StartingPosition
- **Type**: typing.Optional[typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']]

### StartingPositionTimestamp
- **Type**: typing.Optional[datetime.datetime]

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### EventSourceArn
- **Type**: typing.Optional[str]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaTypeDef]

### FunctionArn
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### LastProcessingResult
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### StateTransitionReason
- **Type**: typing.Optional[str]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]

### Topics
- **Type**: typing.Optional[typing.List[str]]

### Queues
- **Type**: typing.Optional[typing.List[str]]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.SourceAccessConfigurationTypeDef]]

### SelfManagedEventSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedEventSourceTypeDef]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### BisectBatchOnFunctionError
- **Type**: typing.Optional[bool]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### TumblingWindowInSeconds
- **Type**: typing.Optional[int]

### FunctionResponseTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ReportBatchItemFailures']]]

### AmazonManagedKafkaEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AmazonManagedKafkaEventSourceConfigTypeDef]

### SelfManagedKafkaEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedKafkaEventSourceConfigTypeDef]

### ScalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ScalingConfigTypeDef]

### DocumentDBEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DocumentDBEventSourceConfigTypeDef]


# FileSystemConfigTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LocalMountPath
- **Type**: <class 'str'>
- **Required**: Yes


# FilterCriteriaPaginatorTypeDef

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.FilterTypeDef]]


# FilterCriteriaTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lambda_classes.FilterTypeDef]]


# FilterTypeDef

### Pattern
- **Type**: typing.Optional[str]


# FunctionCodeLocationTypeDef

### RepositoryType
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### ImageUri
- **Type**: typing.Optional[str]

### ResolvedImageUri
- **Type**: typing.Optional[str]


# FunctionCodeTypeDef

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### ImageUri
- **Type**: typing.Optional[str]


# FunctionConfigurationPaginatorTypeDef

### FunctionName
- **Type**: typing.Optional[str]

### FunctionArn
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### Role
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### MemorySize
- **Type**: typing.Optional[int]

### LastModified
- **Type**: typing.Optional[str]

### CodeSha256
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.VpcConfigResponseTypeDef]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DeadLetterConfigTypeDef]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EnvironmentResponseTypeDef]

### KMSKeyArn
- **Type**: typing.Optional[str]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.TracingConfigResponseTypeDef]

### MasterArn
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.LayerTypeDef]]

### State
- **Type**: typing.Optional[typing.Literal['Active', 'Failed', 'Inactive', 'Pending']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonCode
- **Type**: typing.Optional[typing.Literal['Creating', 'DisabledKMSKey', 'EFSIOError', 'EFSMountConnectivityError', 'EFSMountFailure', 'EFSMountTimeout', 'EniLimitExceeded', 'FunctionError', 'Idle', 'ImageAccessDenied', 'ImageDeleted', 'InsufficientRolePermissions', 'InternalError', 'InvalidConfiguration', 'InvalidImage', 'InvalidRuntime', 'InvalidSecurityGroup', 'InvalidStateKMSKey', 'InvalidSubnet', 'InvalidZipFileException', 'KMSKeyAccessDenied', 'KMSKeyNotFound', 'Restoring', 'SubnetOutOfIPAddresses']]

### LastUpdateStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Successful']]

### LastUpdateStatusReason
- **Type**: typing.Optional[str]

### LastUpdateStatusReasonCode
- **Type**: typing.Optional[typing.Literal['DisabledKMSKey', 'EFSIOError', 'EFSMountConnectivityError', 'EFSMountFailure', 'EFSMountTimeout', 'EniLimitExceeded', 'FunctionError', 'ImageAccessDenied', 'ImageDeleted', 'InsufficientRolePermissions', 'InternalError', 'InvalidConfiguration', 'InvalidImage', 'InvalidRuntime', 'InvalidSecurityGroup', 'InvalidStateKMSKey', 'InvalidSubnet', 'InvalidZipFileException', 'KMSKeyAccessDenied', 'KMSKeyNotFound', 'SubnetOutOfIPAddresses']]

### FileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.FileSystemConfigTypeDef]]

### PackageType
- **Type**: typing.Optional[typing.Literal['Image', 'Zip']]

### ImageConfigResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigResponsePaginatorTypeDef]

### SigningProfileVersionArn
- **Type**: typing.Optional[str]

### SigningJobArn
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.List[typing.Literal['arm64', 'x86_64']]]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EphemeralStorageTypeDef]

### SnapStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SnapStartResponseTypeDef]

### RuntimeVersionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.RuntimeVersionConfigTypeDef]

### LoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.LoggingConfigTypeDef]


# FunctionConfigurationResponseTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Runtime
- **Type**: typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Handler
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSize
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Timeout
- **Type**: <class 'int'>
- **Required**: Yes

### MemorySize
- **Type**: <class 'int'>
- **Required**: Yes

### LastModified
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSha256
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### VpcConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.VpcConfigResponseTypeDef'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.DeadLetterConfigTypeDef'>
- **Required**: Yes

### Environment
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.EnvironmentResponseTypeDef'>
- **Required**: Yes

### KMSKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### TracingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.TracingConfigResponseTypeDef'>
- **Required**: Yes

### MasterArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.LayerTypeDef]
- **Required**: Yes

### State
- **Type**: typing.Literal['Active', 'Failed', 'Inactive', 'Pending']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### StateReasonCode
- **Type**: typing.Literal['Creating', 'DisabledKMSKey', 'EFSIOError', 'EFSMountConnectivityError', 'EFSMountFailure', 'EFSMountTimeout', 'EniLimitExceeded', 'FunctionError', 'Idle', 'ImageAccessDenied', 'ImageDeleted', 'InsufficientRolePermissions', 'InternalError', 'InvalidConfiguration', 'InvalidImage', 'InvalidRuntime', 'InvalidSecurityGroup', 'InvalidStateKMSKey', 'InvalidSubnet', 'InvalidZipFileException', 'KMSKeyAccessDenied', 'KMSKeyNotFound', 'Restoring', 'SubnetOutOfIPAddresses']
- **Required**: Yes

### LastUpdateStatus
- **Type**: typing.Literal['Failed', 'InProgress', 'Successful']
- **Required**: Yes

### LastUpdateStatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### LastUpdateStatusReasonCode
- **Type**: typing.Literal['DisabledKMSKey', 'EFSIOError', 'EFSMountConnectivityError', 'EFSMountFailure', 'EFSMountTimeout', 'EniLimitExceeded', 'FunctionError', 'ImageAccessDenied', 'ImageDeleted', 'InsufficientRolePermissions', 'InternalError', 'InvalidConfiguration', 'InvalidImage', 'InvalidRuntime', 'InvalidSecurityGroup', 'InvalidStateKMSKey', 'InvalidSubnet', 'InvalidZipFileException', 'KMSKeyAccessDenied', 'KMSKeyNotFound', 'SubnetOutOfIPAddresses']
- **Required**: Yes

### FileSystemConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FileSystemConfigTypeDef]
- **Required**: Yes

### PackageType
- **Type**: typing.Literal['Image', 'Zip']
- **Required**: Yes

### ImageConfigResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ImageConfigResponseTypeDef'>
- **Required**: Yes

### SigningProfileVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### SigningJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### Architectures
- **Type**: typing.List[typing.Literal['arm64', 'x86_64']]
- **Required**: Yes

### EphemeralStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.EphemeralStorageTypeDef'>
- **Required**: Yes

### SnapStart
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.SnapStartResponseTypeDef'>
- **Required**: Yes

### RuntimeVersionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.RuntimeVersionConfigTypeDef'>
- **Required**: Yes

### LoggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.LoggingConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FunctionConfigurationTypeDef

### FunctionName
- **Type**: typing.Optional[str]

### FunctionArn
- **Type**: typing.Optional[str]

### Runtime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### Role
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### MemorySize
- **Type**: typing.Optional[int]

### LastModified
- **Type**: typing.Optional[str]

### CodeSha256
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.VpcConfigResponseTypeDef]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DeadLetterConfigTypeDef]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EnvironmentResponseTypeDef]

### KMSKeyArn
- **Type**: typing.Optional[str]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.TracingConfigResponseTypeDef]

### MasterArn
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.LayerTypeDef]]

### State
- **Type**: typing.Optional[typing.Literal['Active', 'Failed', 'Inactive', 'Pending']]

### StateReason
- **Type**: typing.Optional[str]

### StateReasonCode
- **Type**: typing.Optional[typing.Literal['Creating', 'DisabledKMSKey', 'EFSIOError', 'EFSMountConnectivityError', 'EFSMountFailure', 'EFSMountTimeout', 'EniLimitExceeded', 'FunctionError', 'Idle', 'ImageAccessDenied', 'ImageDeleted', 'InsufficientRolePermissions', 'InternalError', 'InvalidConfiguration', 'InvalidImage', 'InvalidRuntime', 'InvalidSecurityGroup', 'InvalidStateKMSKey', 'InvalidSubnet', 'InvalidZipFileException', 'KMSKeyAccessDenied', 'KMSKeyNotFound', 'Restoring', 'SubnetOutOfIPAddresses']]

### LastUpdateStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Successful']]

### LastUpdateStatusReason
- **Type**: typing.Optional[str]

### LastUpdateStatusReasonCode
- **Type**: typing.Optional[typing.Literal['DisabledKMSKey', 'EFSIOError', 'EFSMountConnectivityError', 'EFSMountFailure', 'EFSMountTimeout', 'EniLimitExceeded', 'FunctionError', 'ImageAccessDenied', 'ImageDeleted', 'InsufficientRolePermissions', 'InternalError', 'InvalidConfiguration', 'InvalidImage', 'InvalidRuntime', 'InvalidSecurityGroup', 'InvalidStateKMSKey', 'InvalidSubnet', 'InvalidZipFileException', 'KMSKeyAccessDenied', 'KMSKeyNotFound', 'SubnetOutOfIPAddresses']]

### FileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.FileSystemConfigTypeDef]]

### PackageType
- **Type**: typing.Optional[typing.Literal['Image', 'Zip']]

### ImageConfigResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigResponseTypeDef]

### SigningProfileVersionArn
- **Type**: typing.Optional[str]

### SigningJobArn
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.List[typing.Literal['arm64', 'x86_64']]]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EphemeralStorageTypeDef]

### SnapStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SnapStartResponseTypeDef]

### RuntimeVersionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.RuntimeVersionConfigTypeDef]

### LoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.LoggingConfigTypeDef]


# FunctionEventInvokeConfigResponseTypeDef

### LastModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaximumRetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### MaximumEventAgeInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FunctionEventInvokeConfigTypeDef

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### FunctionArn
- **Type**: typing.Optional[str]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]


# FunctionUrlConfigPaginatorTypeDef

### FunctionUrl
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Cors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CorsPaginatorTypeDef]

### InvokeMode
- **Type**: typing.Optional[typing.Literal['BUFFERED', 'RESPONSE_STREAM']]


# FunctionUrlConfigTypeDef

### FunctionUrl
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Cors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CorsTypeDef]

### InvokeMode
- **Type**: typing.Optional[typing.Literal['BUFFERED', 'RESPONSE_STREAM']]


# GetAccountSettingsResponseTypeDef

### AccountLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AccountLimitTypeDef'>
- **Required**: Yes

### AccountUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AccountUsageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAliasRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodeSigningConfigRequestRequestTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodeSigningConfigResponseTypeDef

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CodeSigningConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventSourceMappingRequestRequestTypeDef

### UUID
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionCodeSigningConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionCodeSigningConfigResponseTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionConcurrencyRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionConcurrencyResponseTypeDef

### ReservedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionConfigurationRequestFunctionActiveWaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionConfigurationRequestFunctionUpdatedWaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionConfigurationRequestPublishedVersionActiveWaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionConfigurationRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionEventInvokeConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionRequestFunctionActiveV2WaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionRequestFunctionExistsWaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionRequestFunctionUpdatedV2WaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionResponseTypeDef

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.FunctionConfigurationTypeDef'>
- **Required**: Yes

### Code
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.FunctionCodeLocationTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Concurrency
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ConcurrencyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionUrlConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionUrlConfigResponseTypeDef

### FunctionUrl
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Cors
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CorsTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'str'>
- **Required**: Yes

### InvokeMode
- **Type**: typing.Literal['BUFFERED', 'RESPONSE_STREAM']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLayerVersionByArnRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLayerVersionPolicyRequestRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetLayerVersionPolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLayerVersionRequestRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetLayerVersionResponseTypeDef

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.LayerVersionContentOutputTypeDef'>
- **Required**: Yes

### LayerArn
- **Type**: <class 'str'>
- **Required**: Yes

### LayerVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### CompatibleRuntimes
- **Type**: typing.List[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]
- **Required**: Yes

### LicenseInfo
- **Type**: <class 'str'>
- **Required**: Yes

### CompatibleArchitectures
- **Type**: typing.List[typing.Literal['arm64', 'x86_64']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetPolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProvisionedConcurrencyConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProvisionedConcurrencyConfigResponseTypeDef

### RequestedProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### AvailableProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### AllocatedProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'READY']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRuntimeManagementConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetRuntimeManagementConfigResponseTypeDef

### UpdateRuntimeOn
- **Type**: typing.Literal['Auto', 'FunctionUpdate', 'Manual']
- **Required**: Yes

### RuntimeVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImageConfigErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ImageConfigPaginatorTypeDef

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### Command
- **Type**: typing.Optional[typing.List[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# ImageConfigResponsePaginatorTypeDef

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigPaginatorTypeDef]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigErrorTypeDef]


# ImageConfigResponseTypeDef

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigTypeDef]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigErrorTypeDef]


# ImageConfigTypeDef

### EntryPoint
- **Type**: typing.Optional[typing.Sequence[str]]

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# InvocationRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationType
- **Type**: typing.Optional[typing.Literal['DryRun', 'Event', 'RequestResponse']]

### LogType
- **Type**: typing.Optional[typing.Literal['None', 'Tail']]

### ClientContext
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### Qualifier
- **Type**: typing.Optional[str]


# InvocationResponseTypeDef

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### FunctionError
- **Type**: <class 'str'>
- **Required**: Yes

### LogResult
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ExecutedVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeAsyncRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### InvokeArgs
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes


# InvokeAsyncResponseTypeDef

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeResponseStreamUpdateTypeDef

### Payload
- **Type**: typing.Optional[bytes]


# InvokeWithResponseStreamCompleteEventTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorDetails
- **Type**: typing.Optional[str]

### LogResult
- **Type**: typing.Optional[str]


# InvokeWithResponseStreamRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationType
- **Type**: typing.Optional[typing.Literal['DryRun', 'RequestResponse']]

### LogType
- **Type**: typing.Optional[typing.Literal['None', 'Tail']]

### ClientContext
- **Type**: typing.Optional[str]

### Qualifier
- **Type**: typing.Optional[str]

### Payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# InvokeWithResponseStreamResponseEventTypeDef

### PayloadChunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.InvokeResponseStreamUpdateTypeDef]

### InvokeComplete
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.InvokeWithResponseStreamCompleteEventTypeDef]


# InvokeWithResponseStreamResponseTypeDef

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ExecutedVersion
- **Type**: <class 'str'>
- **Required**: Yes

### EventStream
- **Type**: ForwardRef('EventStream[InvokeWithResponseStreamResponseEventTypeDef]')
- **Required**: Yes

### ResponseStreamContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LayerTypeDef

### Arn
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]

### SigningProfileVersionArn
- **Type**: typing.Optional[str]

### SigningJobArn
- **Type**: typing.Optional[str]


# LayerVersionContentInputTypeDef

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# LayerVersionContentOutputTypeDef

### Location
- **Type**: typing.Optional[str]

### CodeSha256
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]

### SigningProfileVersionArn
- **Type**: typing.Optional[str]

### SigningJobArn
- **Type**: typing.Optional[str]


# LayerVersionsListItemTypeDef

### LayerVersionArn
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[str]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.List[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]]

### LicenseInfo
- **Type**: typing.Optional[str]

### CompatibleArchitectures
- **Type**: typing.Optional[typing.List[typing.Literal['arm64', 'x86_64']]]


# LayersListItemTypeDef

### LayerName
- **Type**: typing.Optional[str]

### LayerArn
- **Type**: typing.Optional[str]

### LatestMatchingVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.LayerVersionsListItemTypeDef]


# ListAliasesRequestListAliasesPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListAliasesRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAliasesResponsePaginatorTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.AliasConfigurationPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAliasesResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.AliasConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCodeSigningConfigsRequestListCodeSigningConfigsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListCodeSigningConfigsRequestRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListCodeSigningConfigsResponsePaginatorTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSigningConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.CodeSigningConfigPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCodeSigningConfigsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSigningConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.CodeSigningConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventSourceMappingsRequestListEventSourceMappingsPaginateTypeDef

### EventSourceArn
- **Type**: typing.Optional[str]

### FunctionName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListEventSourceMappingsRequestRequestTypeDef

### EventSourceArn
- **Type**: typing.Optional[str]

### FunctionName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListEventSourceMappingsResponsePaginatorTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.EventSourceMappingConfigurationPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEventSourceMappingsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.EventSourceMappingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionEventInvokeConfigsRequestListFunctionEventInvokeConfigsPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionEventInvokeConfigsRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionEventInvokeConfigsResponseTypeDef

### FunctionEventInvokeConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FunctionEventInvokeConfigTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionUrlConfigsRequestListFunctionUrlConfigsPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionUrlConfigsRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionUrlConfigsResponsePaginatorTypeDef

### FunctionUrlConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FunctionUrlConfigPaginatorTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionUrlConfigsResponseTypeDef

### FunctionUrlConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FunctionUrlConfigTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionsByCodeSigningConfigRequestListFunctionsByCodeSigningConfigPaginateTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionsByCodeSigningConfigRequestRequestTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionsByCodeSigningConfigResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionsRequestListFunctionsPaginateTypeDef

### MasterRegion
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[typing.Literal['ALL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionsRequestRequestTypeDef

### MasterRegion
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[typing.Literal['ALL']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionsResponsePaginatorTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Functions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FunctionConfigurationPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFunctionsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Functions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FunctionConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLayerVersionsRequestListLayerVersionsPaginateTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListLayerVersionsRequestRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]


# ListLayerVersionsResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### LayerVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.LayerVersionsListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLayersRequestListLayersPaginateTypeDef

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListLayersRequestRequestTypeDef

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]


# ListLayersResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.LayersListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProvisionedConcurrencyConfigsRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListProvisionedConcurrencyConfigsResponseTypeDef

### ProvisionedConcurrencyConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.ProvisionedConcurrencyConfigListItemTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsRequestRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVersionsByFunctionRequestListVersionsByFunctionPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListVersionsByFunctionRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListVersionsByFunctionResponsePaginatorTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FunctionConfigurationPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVersionsByFunctionResponseTypeDef

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_classes.FunctionConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigTypeDef

### LogFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'Text']]

### ApplicationLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'FATAL', 'INFO', 'TRACE', 'WARN']]

### SystemLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'INFO', 'WARN']]

### LogGroup
- **Type**: typing.Optional[str]


# OnFailureTypeDef

### Destination
- **Type**: typing.Optional[str]


# OnSuccessTypeDef

### Destination
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProvisionedConcurrencyConfigListItemTypeDef

### FunctionArn
- **Type**: typing.Optional[str]

### RequestedProvisionedConcurrentExecutions
- **Type**: typing.Optional[int]

### AvailableProvisionedConcurrentExecutions
- **Type**: typing.Optional[int]

### AllocatedProvisionedConcurrentExecutions
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'READY']]

### StatusReason
- **Type**: typing.Optional[str]

### LastModified
- **Type**: typing.Optional[str]


# PublishLayerVersionRequestRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.LayerVersionContentInputTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]]

### LicenseInfo
- **Type**: typing.Optional[str]

### CompatibleArchitectures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['arm64', 'x86_64']]]


# PublishLayerVersionResponseTypeDef

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.LayerVersionContentOutputTypeDef'>
- **Required**: Yes

### LayerArn
- **Type**: <class 'str'>
- **Required**: Yes

### LayerVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### CompatibleRuntimes
- **Type**: typing.List[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]
- **Required**: Yes

### LicenseInfo
- **Type**: <class 'str'>
- **Required**: Yes

### CompatibleArchitectures
- **Type**: typing.List[typing.Literal['arm64', 'x86_64']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PublishVersionRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSha256
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# PutFunctionCodeSigningConfigRequestRequestTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# PutFunctionCodeSigningConfigResponseTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutFunctionConcurrencyRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes


# PutFunctionEventInvokeConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]


# PutProvisionedConcurrencyConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes


# PutProvisionedConcurrencyConfigResponseTypeDef

### RequestedProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### AvailableProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### AllocatedProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'READY']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### LastModified
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRuntimeManagementConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateRuntimeOn
- **Type**: typing.Literal['Auto', 'FunctionUpdate', 'Manual']
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### RuntimeVersionArn
- **Type**: typing.Optional[str]


# PutRuntimeManagementConfigResponseTypeDef

### UpdateRuntimeOn
- **Type**: typing.Literal['Auto', 'FunctionUpdate', 'Manual']
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### RuntimeVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveLayerVersionPermissionRequestRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### StatementId
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: typing.Optional[str]


# RemovePermissionRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### StatementId
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### RevisionId
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


# RuntimeVersionConfigTypeDef

### RuntimeVersionArn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.RuntimeVersionErrorTypeDef]


# RuntimeVersionErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ScalingConfigTypeDef

### MaximumConcurrency
- **Type**: typing.Optional[int]


# SelfManagedEventSourcePaginatorTypeDef

### Endpoints
- **Type**: typing.Optional[typing.Dict[typing.Literal['KAFKA_BOOTSTRAP_SERVERS'], typing.List[str]]]


# SelfManagedEventSourceTypeDef

### Endpoints
- **Type**: typing.Optional[typing.Mapping[typing.Literal['KAFKA_BOOTSTRAP_SERVERS'], typing.Sequence[str]]]


# SelfManagedKafkaEventSourceConfigTypeDef

### ConsumerGroupId
- **Type**: typing.Optional[str]


# SnapStartResponseTypeDef

### ApplyOn
- **Type**: typing.Optional[typing.Literal['None', 'PublishedVersions']]

### OptimizationStatus
- **Type**: typing.Optional[typing.Literal['Off', 'On']]


# SnapStartTypeDef

### ApplyOn
- **Type**: typing.Optional[typing.Literal['None', 'PublishedVersions']]


# SourceAccessConfigurationTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['BASIC_AUTH', 'CLIENT_CERTIFICATE_TLS_AUTH', 'SASL_SCRAM_256_AUTH', 'SASL_SCRAM_512_AUTH', 'SERVER_ROOT_CA_CERTIFICATE', 'VIRTUAL_HOST', 'VPC_SECURITY_GROUP', 'VPC_SUBNET']]

### URI
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TracingConfigResponseTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['Active', 'PassThrough']]


# TracingConfigTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['Active', 'PassThrough']]


# UntagResourceRequestRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAliasRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationTypeDef]

### RevisionId
- **Type**: typing.Optional[str]


# UpdateCodeSigningConfigRequestRequestTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AllowedPublishers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AllowedPublishersTypeDef]

### CodeSigningPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CodeSigningPoliciesTypeDef]


# UpdateCodeSigningConfigResponseTypeDef

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CodeSigningConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventSourceMappingRequestRequestTypeDef

### UUID
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: typing.Optional[str]

### Enabled
- **Type**: typing.Optional[bool]

### BatchSize
- **Type**: typing.Optional[int]

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaTypeDef]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### BisectBatchOnFunctionError
- **Type**: typing.Optional[bool]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lambda_classes.SourceAccessConfigurationTypeDef]]

### TumblingWindowInSeconds
- **Type**: typing.Optional[int]

### FunctionResponseTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ReportBatchItemFailures']]]

### ScalingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ScalingConfigTypeDef]

### DocumentDBEventSourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DocumentDBEventSourceConfigTypeDef]


# UpdateFunctionCodeRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### ImageUri
- **Type**: typing.Optional[str]

### Publish
- **Type**: typing.Optional[bool]

### DryRun
- **Type**: typing.Optional[bool]

### RevisionId
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.Sequence[typing.Literal['arm64', 'x86_64']]]


# UpdateFunctionConfigurationRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[str]

### Handler
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Timeout
- **Type**: typing.Optional[int]

### MemorySize
- **Type**: typing.Optional[int]

### VpcConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.VpcConfigTypeDef]

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EnvironmentTypeDef]

### Runtime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DeadLetterConfigTypeDef]

### KMSKeyArn
- **Type**: typing.Optional[str]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.TracingConfigTypeDef]

### RevisionId
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.Sequence[str]]

### FileSystemConfigs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lambda_classes.FileSystemConfigTypeDef]]

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigTypeDef]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EphemeralStorageTypeDef]

### SnapStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SnapStartTypeDef]

### LoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.LoggingConfigTypeDef]


# UpdateFunctionEventInvokeConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]


# UpdateFunctionUrlConfigRequestRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### AuthType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### Cors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CorsTypeDef]

### InvokeMode
- **Type**: typing.Optional[typing.Literal['BUFFERED', 'RESPONSE_STREAM']]


# UpdateFunctionUrlConfigResponseTypeDef

### FunctionUrl
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Cors
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CorsTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'str'>
- **Required**: Yes

### InvokeMode
- **Type**: typing.Literal['BUFFERED', 'RESPONSE_STREAM']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VpcConfigResponseTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


# VpcConfigTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


