# Lambda Classes

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


# AddLayerVersionPermissionRequestTypeDef

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


# AddPermissionRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationOutputTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationOutputTypeDef]

### RevisionId
- **Type**: typing.Optional[str]


# AliasRoutingConfigurationOutputTypeDef

### AdditionalVersionWeights
- **Type**: typing.Optional[typing.Dict[str, float]]


# AliasRoutingConfigurationTypeDef

### AdditionalVersionWeights
- **Type**: typing.Optional[typing.Mapping[str, float]]


# AliasRoutingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AllowedPublishersOutputTypeDef

### SigningProfileVersionArns
- **Type**: typing.List[str]
- **Required**: Yes


# AllowedPublishersTypeDef

### SigningProfileVersionArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AllowedPublishersUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AmazonManagedKafkaEventSourceConfigTypeDef

### ConsumerGroupId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeSigningConfigTypeDef

### CodeSigningConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### AllowedPublishers
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AllowedPublishersOutputTypeDef'>
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


# CorsOutputTypeDef

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


# CorsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAliasRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationUnionTypeDef]


# CreateCodeSigningConfigRequestTypeDef

### AllowedPublishers
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.AllowedPublishersUnionTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CodeSigningPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CodeSigningPoliciesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateCodeSigningConfigResponseTypeDef

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CodeSigningConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEventSourceMappingRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaUnionTypeDef]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### StartingPosition
- **Type**: typing.Optional[typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']]

### StartingPositionTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.TimestampTypeDef]

### DestinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.DestinationConfigTypeDef]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### BisectBatchOnFunctionError
- **Type**: typing.Optional[bool]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TumblingWindowInSeconds
- **Type**: typing.Optional[int]

### Topics
- **Type**: typing.Optional[typing.Sequence[str]]

### Queues
- **Type**: typing.Optional[typing.Sequence[str]]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lambda_classes.SourceAccessConfigurationTypeDef]]

### SelfManagedEventSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedEventSourceUnionTypeDef]

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

### KMSKeyArn
- **Type**: typing.Optional[str]

### MetricsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EventSourceMappingMetricsConfigUnionTypeDef]

### ProvisionedPollerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ProvisionedPollerConfigTypeDef]


# CreateFunctionRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigUnionTypeDef]

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


# CreateFunctionUrlConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### Cors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CorsUnionTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CorsOutputTypeDef'>
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


# DeleteAliasRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCodeSigningConfigRequestTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSourceMappingRequestTypeDef

### UUID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionCodeSigningConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionConcurrencyRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionEventInvokeConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteFunctionRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteFunctionUrlConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteLayerVersionRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteProvisionedConcurrencyConfigRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.SelfManagedEventSourceOutputTypeDef'>
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

### KMSKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### FilterCriteriaError
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaErrorTypeDef'>
- **Required**: Yes

### EventSourceMappingArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.EventSourceMappingMetricsConfigOutputTypeDef'>
- **Required**: Yes

### ProvisionedPollerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ProvisionedPollerConfigTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SelfManagedEventSourceOutputTypeDef]

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

### KMSKeyArn
- **Type**: typing.Optional[str]

### FilterCriteriaError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaErrorTypeDef]

### EventSourceMappingArn
- **Type**: typing.Optional[str]

### MetricsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EventSourceMappingMetricsConfigOutputTypeDef]

### ProvisionedPollerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ProvisionedPollerConfigTypeDef]


# EventSourceMappingMetricsConfigOutputTypeDef

### Metrics
- **Type**: typing.Optional[typing.List[typing.Literal['EventCount']]]


# EventSourceMappingMetricsConfigTypeDef

### Metrics
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EventCount']]]


# EventSourceMappingMetricsConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FileSystemConfigTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LocalMountPath
- **Type**: <class 'str'>
- **Required**: Yes


# FilterCriteriaErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# FilterCriteriaOutputTypeDef

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_classes.FilterTypeDef]]


# FilterCriteriaTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.lambda_classes.FilterTypeDef]]


# FilterCriteriaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionCodeLocationTypeDef

### RepositoryType
- **Type**: typing.Optional[str]

### Location
- **Type**: typing.Optional[str]

### ImageUri
- **Type**: typing.Optional[str]

### ResolvedImageUri
- **Type**: typing.Optional[str]

### SourceKMSKeyArn
- **Type**: typing.Optional[str]


# FunctionCodeTypeDef

### ZipFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.BlobTypeDef]

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### ImageUri
- **Type**: typing.Optional[str]

### SourceKMSKeyArn
- **Type**: typing.Optional[str]


# FunctionConfigurationResponseTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Runtime
- **Type**: typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']
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
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CorsOutputTypeDef]

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


# GetAliasRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodeSigningConfigRequestTypeDef

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


# GetEventSourceMappingRequestTypeDef

### UUID
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionCodeSigningConfigRequestTypeDef

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


# GetFunctionConcurrencyRequestTypeDef

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


# GetFunctionConfigurationRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionConfigurationRequestWaitExtraExtraTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionConfigurationRequestWaitExtraTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionConfigurationRequestWaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionEventInvokeConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionRecursionConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionRecursionConfigResponseTypeDef

### RecursiveLoop
- **Type**: typing.Literal['Allow', 'Terminate']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionRequestWaitExtraExtraTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionRequestWaitExtraTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


# GetFunctionRequestWaitTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.WaiterConfigTypeDef]


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

### TagsError
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.TagsErrorTypeDef'>
- **Required**: Yes

### Concurrency
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ConcurrencyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFunctionUrlConfigRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CorsOutputTypeDef'>
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


# GetLayerVersionByArnRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLayerVersionPolicyRequestTypeDef

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


# GetLayerVersionRequestTypeDef

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
- **Type**: typing.List[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]
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


# GetPolicyRequestTypeDef

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


# GetProvisionedConcurrencyConfigRequestTypeDef

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


# GetRuntimeManagementConfigRequestTypeDef

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


# ImageConfigOutputTypeDef

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### Command
- **Type**: typing.Optional[typing.List[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# ImageConfigResponseTypeDef

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigOutputTypeDef]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigErrorTypeDef]


# ImageConfigTypeDef

### EntryPoint
- **Type**: typing.Optional[typing.Sequence[str]]

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# ImageConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvocationRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.BlobTypeDef]

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


# InvokeAsyncRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### InvokeArgs
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.BlobTypeDef'>
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


# InvokeWithResponseStreamRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.BlobTypeDef]


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
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.lambda_classes.InvokeWithResponseStreamResponseEventTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.BlobTypeDef]


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
- **Type**: typing.Optional[typing.List[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]]

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


# ListAliasesRequestPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListAliasesRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


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


# ListCodeSigningConfigsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListCodeSigningConfigsRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


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


# ListEventSourceMappingsRequestPaginateTypeDef

### EventSourceArn
- **Type**: typing.Optional[str]

### FunctionName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListEventSourceMappingsRequestTypeDef

### EventSourceArn
- **Type**: typing.Optional[str]

### FunctionName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


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


# ListFunctionEventInvokeConfigsRequestPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionEventInvokeConfigsRequestTypeDef

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


# ListFunctionUrlConfigsRequestPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionUrlConfigsRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


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


# ListFunctionsByCodeSigningConfigRequestPaginateTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionsByCodeSigningConfigRequestTypeDef

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


# ListFunctionsRequestPaginateTypeDef

### MasterRegion
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[typing.Literal['ALL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListFunctionsRequestTypeDef

### MasterRegion
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[typing.Literal['ALL']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


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


# ListLayerVersionsRequestPaginateTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListLayerVersionsRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

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


# ListLayersRequestPaginateTypeDef

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListLayersRequestTypeDef

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

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


# ListProvisionedConcurrencyConfigsRequestPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListProvisionedConcurrencyConfigsRequestTypeDef

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


# ListTagsRequestTypeDef

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


# ListVersionsByFunctionRequestPaginateTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.PaginatorConfigTypeDef]


# ListVersionsByFunctionRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


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


# ProvisionedPollerConfigTypeDef

### MinimumPollers
- **Type**: typing.Optional[int]

### MaximumPollers
- **Type**: typing.Optional[int]


# PublishLayerVersionRequestTypeDef

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.LayerVersionContentInputTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]]

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
- **Type**: typing.List[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]
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


# PublishVersionRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSha256
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# PutFunctionCodeSigningConfigRequestTypeDef

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


# PutFunctionConcurrencyRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes


# PutFunctionEventInvokeConfigRequestTypeDef

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


# PutFunctionRecursionConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### RecursiveLoop
- **Type**: typing.Literal['Allow', 'Terminate']
- **Required**: Yes


# PutFunctionRecursionConfigResponseTypeDef

### RecursiveLoop
- **Type**: typing.Literal['Allow', 'Terminate']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutProvisionedConcurrencyConfigRequestTypeDef

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


# PutRuntimeManagementConfigRequestTypeDef

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


# RemoveLayerVersionPermissionRequestTypeDef

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


# RemovePermissionRequestTypeDef

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


# SelfManagedEventSourceOutputTypeDef

### Endpoints
- **Type**: typing.Optional[typing.Dict[typing.Literal['KAFKA_BOOTSTRAP_SERVERS'], typing.List[str]]]


# SelfManagedEventSourceTypeDef

### Endpoints
- **Type**: typing.Optional[typing.Mapping[typing.Literal['KAFKA_BOOTSTRAP_SERVERS'], typing.Sequence[str]]]


# SelfManagedEventSourceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagsErrorTypeDef

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TracingConfigResponseTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['Active', 'PassThrough']]


# TracingConfigTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['Active', 'PassThrough']]


# UntagResourceRequestTypeDef

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAliasRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AliasRoutingConfigurationUnionTypeDef]

### RevisionId
- **Type**: typing.Optional[str]


# UpdateCodeSigningConfigRequestTypeDef

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AllowedPublishers
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.AllowedPublishersUnionTypeDef]

### CodeSigningPolicies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CodeSigningPoliciesTypeDef]


# UpdateCodeSigningConfigResponseTypeDef

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CodeSigningConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateEventSourceMappingRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.FilterCriteriaUnionTypeDef]

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

### KMSKeyArn
- **Type**: typing.Optional[str]

### MetricsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EventSourceMappingMetricsConfigUnionTypeDef]

### ProvisionedPollerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ProvisionedPollerConfigTypeDef]


# UpdateFunctionCodeRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ZipFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.BlobTypeDef]

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

### SourceKMSKeyArn
- **Type**: typing.Optional[str]


# UpdateFunctionConfigurationRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.ImageConfigUnionTypeDef]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.EphemeralStorageTypeDef]

### SnapStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.SnapStartTypeDef]

### LoggingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.LoggingConfigTypeDef]


# UpdateFunctionEventInvokeConfigRequestTypeDef

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


# UpdateFunctionUrlConfigRequestTypeDef

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### AuthType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### Cors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_classes.CorsUnionTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_classes.CorsOutputTypeDef'>
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


