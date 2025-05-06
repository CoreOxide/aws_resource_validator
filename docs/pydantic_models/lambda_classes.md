# Lambda Classes

# AccountLimit

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


# AccountUsage

### TotalCodeSize
- **Type**: typing.Optional[int]

### FunctionCount
- **Type**: typing.Optional[int]


# AddLayerVersionPermissionRequest

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


# AddLayerVersionPermissionResponse

### Statement
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# AddPermissionRequest

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


# AddPermissionResponse

### Statement
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# AliasConfiguration

### AliasArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoutingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.AliasRoutingConfigurationOutput]

### RevisionId
- **Type**: typing.Optional[str]


# AliasConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.AliasRoutingConfigurationOutput'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# AliasRoutingConfiguration

### AdditionalVersionWeights
- **Type**: typing.Optional[typing.Dict[str, float]]


# AliasRoutingConfigurationOutput

### AdditionalVersionWeights
- **Type**: typing.Optional[typing.Dict[str, float]]


# AllowedPublishers

### SigningProfileVersionArns
- **Type**: typing.List[str]
- **Required**: Yes


# AllowedPublishersOutput

### SigningProfileVersionArns
- **Type**: typing.List[str]
- **Required**: Yes


# AmazonManagedKafkaEventSourceConfig

### ConsumerGroupId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CodeSigningConfig

### CodeSigningConfigId
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### AllowedPublishers
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.AllowedPublishersOutput'>
- **Required**: Yes

### CodeSigningPolicies
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.CodeSigningPolicies'>
- **Required**: Yes

### LastModified
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# CodeSigningPolicies

### UntrustedArtifactOnDeployment
- **Type**: typing.Optional[typing.Literal['Enforce', 'Warn']]


# Concurrency

### ReservedConcurrentExecutions
- **Type**: typing.Optional[int]


# ConcurrencyResponse

### ReservedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# Cors

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


# CorsOutput

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


# CreateAliasRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.AliasRoutingConfiguration, aws_resource_validator.pydantic_models.lambda_.lambda_classes.AliasRoutingConfigurationOutput, NoneType]


# CreateCodeSigningConfigRequest

### AllowedPublishers
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.AllowedPublishers, aws_resource_validator.pydantic_models.lambda_.lambda_classes.AllowedPublishersOutput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CodeSigningPolicies
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateCodeSigningConfigResponse

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.CodeSigningConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEventSourceMappingRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FilterCriteria, aws_resource_validator.pydantic_models.lambda_.lambda_classes.FilterCriteriaOutput, NoneType]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### StartingPosition
- **Type**: typing.Optional[typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']]

### StartingPositionTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### DestinationConfig
- **Type**: <class 'NoneType'>

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### BisectBatchOnFunctionError
- **Type**: typing.Optional[bool]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TumblingWindowInSeconds
- **Type**: typing.Optional[int]

### Topics
- **Type**: typing.Optional[typing.List[str]]

### Queues
- **Type**: typing.Optional[typing.List[str]]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.SourceAccessConfiguration]]

### SelfManagedEventSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.SelfManagedEventSource, aws_resource_validator.pydantic_models.lambda_.lambda_classes.SelfManagedEventSourceOutput, NoneType]

### FunctionResponseTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ReportBatchItemFailures']]]

### AmazonManagedKafkaEventSourceConfig
- **Type**: <class 'NoneType'>

### SelfManagedKafkaEventSourceConfig
- **Type**: <class 'NoneType'>

### ScalingConfig
- **Type**: <class 'NoneType'>

### DocumentDBEventSourceConfig
- **Type**: <class 'NoneType'>

### KMSKeyArn
- **Type**: typing.Optional[str]

### MetricsConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.EventSourceMappingMetricsConfig, aws_resource_validator.pydantic_models.lambda_.lambda_classes.EventSourceMappingMetricsConfigOutput, NoneType]

### ProvisionedPollerConfig
- **Type**: <class 'NoneType'>


# CreateFunctionRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.FunctionCode'>
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
- **Type**: <class 'NoneType'>

### PackageType
- **Type**: typing.Optional[typing.Literal['Image', 'Zip']]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### Environment
- **Type**: <class 'NoneType'>

### KMSKeyArn
- **Type**: typing.Optional[str]

### TracingConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Layers
- **Type**: typing.Optional[typing.List[str]]

### FileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FileSystemConfig]]

### ImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.ImageConfig, aws_resource_validator.pydantic_models.lambda_.lambda_classes.ImageConfigOutput, NoneType]

### CodeSigningConfigArn
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.List[typing.Literal['arm64', 'x86_64']]]

### EphemeralStorage
- **Type**: <class 'NoneType'>

### SnapStart
- **Type**: <class 'NoneType'>

### LoggingConfig
- **Type**: <class 'NoneType'>


# CreateFunctionUrlConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### AuthType
- **Type**: typing.Literal['AWS_IAM', 'NONE']
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### Cors
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.Cors, aws_resource_validator.pydantic_models.lambda_.lambda_classes.CorsOutput, NoneType]

### InvokeMode
- **Type**: typing.Optional[typing.Literal['BUFFERED', 'RESPONSE_STREAM']]


# CreateFunctionUrlConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.CorsOutput'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### InvokeMode
- **Type**: typing.Literal['BUFFERED', 'RESPONSE_STREAM']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# DeadLetterConfig

### TargetArn
- **Type**: typing.Optional[str]


# DeleteAliasRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCodeSigningConfigRequest

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventSourceMappingRequest

### UUID
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionCodeSigningConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionConcurrencyRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFunctionEventInvokeConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteFunctionRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteFunctionUrlConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# DeleteLayerVersionRequest

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteProvisionedConcurrencyConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfig

### OnSuccess
- **Type**: <class 'NoneType'>

### OnFailure
- **Type**: <class 'NoneType'>


# DocumentDBEventSourceConfig

### DatabaseName
- **Type**: typing.Optional[str]

### CollectionName
- **Type**: typing.Optional[str]

### FullDocument
- **Type**: typing.Optional[typing.Literal['Default', 'UpdateLookup']]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# Environment

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]


# EnvironmentError

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# EnvironmentResponse

### Variables
- **Type**: typing.Optional[typing.Dict[str, str]]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.EnvironmentError]


# EphemeralStorage

### Size
- **Type**: <class 'int'>
- **Required**: Yes


# EventSourceMappingConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FilterCriteriaOutput]

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
- **Type**: <class 'NoneType'>

### Topics
- **Type**: typing.Optional[typing.List[str]]

### Queues
- **Type**: typing.Optional[typing.List[str]]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.SourceAccessConfiguration]]

### SelfManagedEventSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.SelfManagedEventSourceOutput]

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
- **Type**: <class 'NoneType'>

### SelfManagedKafkaEventSourceConfig
- **Type**: <class 'NoneType'>

### ScalingConfig
- **Type**: <class 'NoneType'>

### DocumentDBEventSourceConfig
- **Type**: <class 'NoneType'>

### KMSKeyArn
- **Type**: typing.Optional[str]

### FilterCriteriaError
- **Type**: <class 'NoneType'>

### EventSourceMappingArn
- **Type**: typing.Optional[str]

### MetricsConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.EventSourceMappingMetricsConfigOutput]

### ProvisionedPollerConfig
- **Type**: <class 'NoneType'>


# EventSourceMappingConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.FilterCriteriaOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.DestinationConfig'>
- **Required**: Yes

### Topics
- **Type**: typing.List[str]
- **Required**: Yes

### Queues
- **Type**: typing.List[str]
- **Required**: Yes

### SourceAccessConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.SourceAccessConfiguration]
- **Required**: Yes

### SelfManagedEventSource
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.SelfManagedEventSourceOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.AmazonManagedKafkaEventSourceConfig'>
- **Required**: Yes

### SelfManagedKafkaEventSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.SelfManagedKafkaEventSourceConfig'>
- **Required**: Yes

### ScalingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ScalingConfig'>
- **Required**: Yes

### DocumentDBEventSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.DocumentDBEventSourceConfig'>
- **Required**: Yes

### KMSKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### FilterCriteriaError
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.FilterCriteriaError'>
- **Required**: Yes

### EventSourceMappingArn
- **Type**: <class 'str'>
- **Required**: Yes

### MetricsConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.EventSourceMappingMetricsConfigOutput'>
- **Required**: Yes

### ProvisionedPollerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ProvisionedPollerConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# EventSourceMappingMetricsConfig

### Metrics
- **Type**: typing.Optional[typing.List[typing.Literal['EventCount']]]


# EventSourceMappingMetricsConfigOutput

### Metrics
- **Type**: typing.Optional[typing.List[typing.Literal['EventCount']]]


# FileSystemConfig

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### LocalMountPath
- **Type**: <class 'str'>
- **Required**: Yes


# Filter

### Pattern
- **Type**: typing.Optional[str]


# FilterCriteria

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.Filter]]


# FilterCriteriaError

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# FilterCriteriaOutput

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.Filter]]


# FunctionCode

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

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


# FunctionCodeLocation

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


# FunctionConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.VpcConfigResponse]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### Environment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.EnvironmentResponse]

### KMSKeyArn
- **Type**: typing.Optional[str]

### TracingConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.TracingConfigResponse]

### MasterArn
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.Layer]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FileSystemConfig]]

### PackageType
- **Type**: typing.Optional[typing.Literal['Image', 'Zip']]

### ImageConfigResponse
- **Type**: <class 'NoneType'>

### SigningProfileVersionArn
- **Type**: typing.Optional[str]

### SigningJobArn
- **Type**: typing.Optional[str]

### Architectures
- **Type**: typing.Optional[typing.List[typing.Literal['arm64', 'x86_64']]]

### EphemeralStorage
- **Type**: <class 'NoneType'>

### SnapStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.SnapStartResponse]

### RuntimeVersionConfig
- **Type**: <class 'NoneType'>

### LoggingConfig
- **Type**: <class 'NoneType'>


# FunctionConfigurationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.VpcConfigResponse'>
- **Required**: Yes

### DeadLetterConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.DeadLetterConfig'>
- **Required**: Yes

### Environment
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.EnvironmentResponse'>
- **Required**: Yes

### KMSKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### TracingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.TracingConfigResponse'>
- **Required**: Yes

### MasterArn
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### Layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.Layer]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FileSystemConfig]
- **Required**: Yes

### PackageType
- **Type**: typing.Literal['Image', 'Zip']
- **Required**: Yes

### ImageConfigResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ImageConfigResponse'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.EphemeralStorage'>
- **Required**: Yes

### SnapStart
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.SnapStartResponse'>
- **Required**: Yes

### RuntimeVersionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.RuntimeVersionConfig'>
- **Required**: Yes

### LoggingConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.LoggingConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# FunctionEventInvokeConfig

### LastModified
- **Type**: typing.Optional[datetime.datetime]

### FunctionArn
- **Type**: typing.Optional[str]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### MaximumEventAgeInSeconds
- **Type**: typing.Optional[int]

### DestinationConfig
- **Type**: <class 'NoneType'>


# FunctionEventInvokeConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.DestinationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# FunctionUrlConfig

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.CorsOutput]

### InvokeMode
- **Type**: typing.Optional[typing.Literal['BUFFERED', 'RESPONSE_STREAM']]


# GetAccountSettingsResponse

### AccountLimit
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.AccountLimit'>
- **Required**: Yes

### AccountUsage
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.AccountUsage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetAliasRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodeSigningConfigRequest

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCodeSigningConfigResponse

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.CodeSigningConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventSourceMappingRequest

### UUID
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionCodeSigningConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionCodeSigningConfigResponse

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetFunctionConcurrencyRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionConcurrencyResponse

### ReservedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetFunctionConfigurationRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionConfigurationRequestWait

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetFunctionConfigurationRequestWaitExtra

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetFunctionConfigurationRequestWaitExtraExtra

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetFunctionEventInvokeConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionRecursionConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# GetFunctionRecursionConfigResponse

### RecursiveLoop
- **Type**: typing.Literal['Allow', 'Terminate']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetFunctionRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionRequestWait

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetFunctionRequestWaitExtra

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetFunctionRequestWaitExtraExtra

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetFunctionResponse

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.FunctionConfiguration'>
- **Required**: Yes

### Code
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.FunctionCodeLocation'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TagsError
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.TagsError'>
- **Required**: Yes

### Concurrency
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.Concurrency'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetFunctionUrlConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetFunctionUrlConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.CorsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetLayerVersionByArnRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetLayerVersionPolicyRequest

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetLayerVersionPolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetLayerVersionRequest

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetLayerVersionResponse

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.LayerVersionContentOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetPolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### RevisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetProvisionedConcurrencyConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetProvisionedConcurrencyConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# GetRuntimeManagementConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]


# GetRuntimeManagementConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ImageConfig

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### Command
- **Type**: typing.Optional[typing.List[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# ImageConfigError

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ImageConfigOutput

### EntryPoint
- **Type**: typing.Optional[typing.List[str]]

### Command
- **Type**: typing.Optional[typing.List[str]]

### WorkingDirectory
- **Type**: typing.Optional[str]


# ImageConfigResponse

### ImageConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.ImageConfigOutput]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.ImageConfigError]


# InvocationRequest

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### Qualifier
- **Type**: typing.Optional[str]


# InvocationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeAsyncRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### InvokeArgs
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes


# InvokeAsyncResponse

### Status
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeResponseStreamUpdate

### Payload
- **Type**: typing.Optional[bytes]


# InvokeWithResponseStreamCompleteEvent

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorDetails
- **Type**: typing.Optional[str]

### LogResult
- **Type**: typing.Optional[str]


# InvokeWithResponseStreamRequest

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# InvokeWithResponseStreamResponse

### StatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### ExecutedVersion
- **Type**: <class 'str'>
- **Required**: Yes

### EventStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.lambda_.lambda_classes.InvokeWithResponseStreamResponseEvent]
- **Required**: Yes

### ResponseStreamContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeWithResponseStreamResponseEvent

### PayloadChunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.InvokeResponseStreamUpdate]

### InvokeComplete
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.InvokeWithResponseStreamCompleteEvent]


# Layer

### Arn
- **Type**: typing.Optional[str]

### CodeSize
- **Type**: typing.Optional[int]

### SigningProfileVersionArn
- **Type**: typing.Optional[str]

### SigningJobArn
- **Type**: typing.Optional[str]


# LayerVersionContentInput

### S3Bucket
- **Type**: typing.Optional[str]

### S3Key
- **Type**: typing.Optional[str]

### S3ObjectVersion
- **Type**: typing.Optional[str]

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# LayerVersionContentOutput

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


# LayerVersionsListItem

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


# LayersListItem

### LayerName
- **Type**: typing.Optional[str]

### LayerArn
- **Type**: typing.Optional[str]

### LatestMatchingVersion
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.LayerVersionsListItem]


# ListAliasesRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAliasesRequestPaginate

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListAliasesResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.AliasConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListCodeSigningConfigsRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListCodeSigningConfigsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListCodeSigningConfigsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSigningConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.CodeSigningConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListEventSourceMappingsRequest

### EventSourceArn
- **Type**: typing.Optional[str]

### FunctionName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListEventSourceMappingsRequestPaginate

### EventSourceArn
- **Type**: typing.Optional[str]

### FunctionName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListEventSourceMappingsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### EventSourceMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.EventSourceMappingConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListFunctionEventInvokeConfigsRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionEventInvokeConfigsRequestPaginate

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListFunctionEventInvokeConfigsResponse

### FunctionEventInvokeConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FunctionEventInvokeConfig]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListFunctionUrlConfigsRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionUrlConfigsRequestPaginate

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListFunctionUrlConfigsResponse

### FunctionUrlConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FunctionUrlConfig]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListFunctionsByCodeSigningConfigRequest

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionsByCodeSigningConfigRequestPaginate

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListFunctionsByCodeSigningConfigResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListFunctionsRequest

### MasterRegion
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[typing.Literal['ALL']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListFunctionsRequestPaginate

### MasterRegion
- **Type**: typing.Optional[str]

### FunctionVersion
- **Type**: typing.Optional[typing.Literal['ALL']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListFunctionsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Functions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FunctionConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListLayerVersionsRequest

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


# ListLayerVersionsRequestPaginate

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListLayerVersionsResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### LayerVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.LayerVersionsListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListLayersRequest

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]


# ListLayersRequestPaginate

### CompatibleRuntime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### CompatibleArchitecture
- **Type**: typing.Optional[typing.Literal['arm64', 'x86_64']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListLayersResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.LayersListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListProvisionedConcurrencyConfigsRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListProvisionedConcurrencyConfigsRequestPaginate

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListProvisionedConcurrencyConfigsResponse

### ProvisionedConcurrencyConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.ProvisionedConcurrencyConfigListItem]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# ListVersionsByFunctionRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListVersionsByFunctionRequestPaginate

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.PaginatorConfig]


# ListVersionsByFunctionResponse

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FunctionConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfig

### LogFormat
- **Type**: typing.Optional[typing.Literal['JSON', 'Text']]

### ApplicationLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'ERROR', 'FATAL', 'INFO', 'TRACE', 'WARN']]

### SystemLogLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'INFO', 'WARN']]

### LogGroup
- **Type**: typing.Optional[str]


# OnFailure

### Destination
- **Type**: typing.Optional[str]


# OnSuccess

### Destination
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProvisionedConcurrencyConfigListItem

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


# ProvisionedPollerConfig

### MinimumPollers
- **Type**: typing.Optional[int]

### MaximumPollers
- **Type**: typing.Optional[int]


# PublishLayerVersionRequest

### LayerName
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.LayerVersionContentInput'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CompatibleRuntimes
- **Type**: typing.Optional[typing.List[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]]

### LicenseInfo
- **Type**: typing.Optional[str]

### CompatibleArchitectures
- **Type**: typing.Optional[typing.List[typing.Literal['arm64', 'x86_64']]]


# PublishLayerVersionResponse

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.LayerVersionContentOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# PublishVersionRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### CodeSha256
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RevisionId
- **Type**: typing.Optional[str]


# PutFunctionCodeSigningConfigRequest

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes


# PutFunctionCodeSigningConfigResponse

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# PutFunctionConcurrencyRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ReservedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes


# PutFunctionEventInvokeConfigRequest

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
- **Type**: <class 'NoneType'>


# PutFunctionRecursionConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### RecursiveLoop
- **Type**: typing.Literal['Allow', 'Terminate']
- **Required**: Yes


# PutFunctionRecursionConfigResponse

### RecursiveLoop
- **Type**: typing.Literal['Allow', 'Terminate']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# PutProvisionedConcurrencyConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionedConcurrentExecutions
- **Type**: <class 'int'>
- **Required**: Yes


# PutProvisionedConcurrencyConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# PutRuntimeManagementConfigRequest

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


# PutRuntimeManagementConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveLayerVersionPermissionRequest

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


# RemovePermissionRequest

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


# RuntimeVersionConfig

### RuntimeVersionArn
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.lambda_.lambda_classes.RuntimeVersionError]


# RuntimeVersionError

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# ScalingConfig

### MaximumConcurrency
- **Type**: typing.Optional[int]


# SelfManagedEventSource

### Endpoints
- **Type**: typing.Optional[typing.Dict[typing.Literal['KAFKA_BOOTSTRAP_SERVERS'], typing.List[str]]]


# SelfManagedEventSourceOutput

### Endpoints
- **Type**: typing.Optional[typing.Dict[typing.Literal['KAFKA_BOOTSTRAP_SERVERS'], typing.List[str]]]


# SelfManagedKafkaEventSourceConfig

### ConsumerGroupId
- **Type**: typing.Optional[str]


# SnapStart

### ApplyOn
- **Type**: typing.Optional[typing.Literal['None', 'PublishedVersions']]


# SnapStartResponse

### ApplyOn
- **Type**: typing.Optional[typing.Literal['None', 'PublishedVersions']]

### OptimizationStatus
- **Type**: typing.Optional[typing.Literal['Off', 'On']]


# SourceAccessConfiguration

### Type
- **Type**: typing.Optional[typing.Literal['BASIC_AUTH', 'CLIENT_CERTIFICATE_TLS_AUTH', 'SASL_SCRAM_256_AUTH', 'SASL_SCRAM_512_AUTH', 'SERVER_ROOT_CA_CERTIFICATE', 'VIRTUAL_HOST', 'VPC_SECURITY_GROUP', 'VPC_SUBNET']]

### URI
- **Type**: typing.Optional[str]


# TagResourceRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagsError

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### Message
- **Type**: <class 'str'>
- **Required**: Yes


# TracingConfig

### Mode
- **Type**: typing.Optional[typing.Literal['Active', 'PassThrough']]


# TracingConfigResponse

### Mode
- **Type**: typing.Optional[typing.Literal['Active', 'PassThrough']]


# UntagResourceRequest

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAliasRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.AliasRoutingConfiguration, aws_resource_validator.pydantic_models.lambda_.lambda_classes.AliasRoutingConfigurationOutput, NoneType]

### RevisionId
- **Type**: typing.Optional[str]


# UpdateCodeSigningConfigRequest

### CodeSigningConfigArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### AllowedPublishers
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.AllowedPublishers, aws_resource_validator.pydantic_models.lambda_.lambda_classes.AllowedPublishersOutput, NoneType]

### CodeSigningPolicies
- **Type**: <class 'NoneType'>


# UpdateCodeSigningConfigResponse

### CodeSigningConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.CodeSigningConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateEventSourceMappingRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FilterCriteria, aws_resource_validator.pydantic_models.lambda_.lambda_classes.FilterCriteriaOutput, NoneType]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### DestinationConfig
- **Type**: <class 'NoneType'>

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### BisectBatchOnFunctionError
- **Type**: typing.Optional[bool]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### SourceAccessConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.SourceAccessConfiguration]]

### TumblingWindowInSeconds
- **Type**: typing.Optional[int]

### FunctionResponseTypes
- **Type**: typing.Optional[typing.List[typing.Literal['ReportBatchItemFailures']]]

### ScalingConfig
- **Type**: <class 'NoneType'>

### DocumentDBEventSourceConfig
- **Type**: <class 'NoneType'>

### KMSKeyArn
- **Type**: typing.Optional[str]

### MetricsConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.EventSourceMappingMetricsConfig, aws_resource_validator.pydantic_models.lambda_.lambda_classes.EventSourceMappingMetricsConfigOutput, NoneType]

### ProvisionedPollerConfig
- **Type**: <class 'NoneType'>


# UpdateFunctionCodeRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### ZipFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

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
- **Type**: typing.Optional[typing.List[typing.Literal['arm64', 'x86_64']]]

### SourceKMSKeyArn
- **Type**: typing.Optional[str]


# UpdateFunctionConfigurationRequest

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
- **Type**: <class 'NoneType'>

### Environment
- **Type**: <class 'NoneType'>

### Runtime
- **Type**: typing.Optional[typing.Literal['dotnet6', 'dotnet8', 'dotnetcore1.0', 'dotnetcore2.0', 'dotnetcore2.1', 'dotnetcore3.1', 'go1.x', 'java11', 'java17', 'java21', 'java8', 'java8.al2', 'nodejs', 'nodejs10.x', 'nodejs12.x', 'nodejs14.x', 'nodejs16.x', 'nodejs18.x', 'nodejs20.x', 'nodejs22.x', 'nodejs4.3', 'nodejs4.3-edge', 'nodejs6.10', 'nodejs8.10', 'provided', 'provided.al2', 'provided.al2023', 'python2.7', 'python3.10', 'python3.11', 'python3.12', 'python3.13', 'python3.6', 'python3.7', 'python3.8', 'python3.9', 'ruby2.5', 'ruby2.7', 'ruby3.2', 'ruby3.3']]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

### KMSKeyArn
- **Type**: typing.Optional[str]

### TracingConfig
- **Type**: <class 'NoneType'>

### RevisionId
- **Type**: typing.Optional[str]

### Layers
- **Type**: typing.Optional[typing.List[str]]

### FileSystemConfigs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.lambda_.lambda_classes.FileSystemConfig]]

### ImageConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.ImageConfig, aws_resource_validator.pydantic_models.lambda_.lambda_classes.ImageConfigOutput, NoneType]

### EphemeralStorage
- **Type**: <class 'NoneType'>

### SnapStart
- **Type**: <class 'NoneType'>

### LoggingConfig
- **Type**: <class 'NoneType'>


# UpdateFunctionEventInvokeConfigRequest

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
- **Type**: <class 'NoneType'>


# UpdateFunctionUrlConfigRequest

### FunctionName
- **Type**: <class 'str'>
- **Required**: Yes

### Qualifier
- **Type**: typing.Optional[str]

### AuthType
- **Type**: typing.Optional[typing.Literal['AWS_IAM', 'NONE']]

### Cors
- **Type**: typing.Union[aws_resource_validator.pydantic_models.lambda_.lambda_classes.Cors, aws_resource_validator.pydantic_models.lambda_.lambda_classes.CorsOutput, NoneType]

### InvokeMode
- **Type**: typing.Optional[typing.Literal['BUFFERED', 'RESPONSE_STREAM']]


# UpdateFunctionUrlConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.CorsOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.lambda_.lambda_classes.ResponseMetadata'>
- **Required**: Yes


# VpcConfig

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


# VpcConfigResponse

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### VpcId
- **Type**: typing.Optional[str]

### Ipv6AllowedForDualStack
- **Type**: typing.Optional[bool]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


