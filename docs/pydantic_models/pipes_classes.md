# Pipes Classes

# AwsVpcConfigurationOutputTypeDef

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationTypeDef

### Subnets
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchArrayPropertiesTypeDef

### Size
- **Type**: typing.Optional[int]


# BatchContainerOverridesOutputTypeDef

### Command
- **Type**: typing.Optional[typing.List[str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.BatchEnvironmentVariableTypeDef]]

### InstanceType
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.BatchResourceRequirementTypeDef]]


# BatchContainerOverridesTypeDef

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### Environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.BatchEnvironmentVariableTypeDef]]

### InstanceType
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.BatchResourceRequirementTypeDef]]


# BatchEnvironmentVariableTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# BatchJobDependencyTypeDef

### JobId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['N_TO_N', 'SEQUENTIAL']]


# BatchResourceRequirementTypeDef

### Type
- **Type**: typing.Literal['GPU', 'MEMORY', 'VCPU']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# BatchRetryStrategyTypeDef

### Attempts
- **Type**: typing.Optional[int]


# CapacityProviderStrategyItemTypeDef

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# CloudwatchLogsLogDestinationParametersTypeDef

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# CloudwatchLogsLogDestinationTypeDef

### LogGroupArn
- **Type**: typing.Optional[str]


# CreatePipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DesiredState
- **Type**: typing.Optional[typing.Literal['RUNNING', 'STOPPED']]

### SourceParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceParametersTypeDef]

### Enrichment
- **Type**: typing.Optional[str]

### EnrichmentParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeEnrichmentParametersTypeDef]

### TargetParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetParametersTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeLogConfigurationParametersTypeDef]


# CreatePipeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### CurrentState
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeadLetterConfigTypeDef

### Arn
- **Type**: typing.Optional[str]


# DeletePipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['DELETED', 'RUNNING', 'STOPPED']
- **Required**: Yes

### CurrentState
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['DELETED', 'RUNNING', 'STOPPED']
- **Required**: Yes

### CurrentState
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']
- **Required**: Yes

### StateReason
- **Type**: <class 'str'>
- **Required**: Yes

### Source
- **Type**: <class 'str'>
- **Required**: Yes

### SourceParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.PipeSourceParametersOutputTypeDef'>
- **Required**: Yes

### Enrichment
- **Type**: <class 'str'>
- **Required**: Yes

### EnrichmentParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.PipeEnrichmentParametersOutputTypeDef'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### TargetParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.PipeTargetParametersOutputTypeDef'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.PipeLogConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DimensionMappingTypeDef

### DimensionValue
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueType
- **Type**: typing.Literal['VARCHAR']
- **Required**: Yes

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes


# EcsContainerOverrideOutputTypeDef

### Command
- **Type**: typing.Optional[typing.List[str]]

### Cpu
- **Type**: typing.Optional[int]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.EcsEnvironmentVariableTypeDef]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.EcsEnvironmentFileTypeDef]]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.EcsResourceRequirementTypeDef]]


# EcsContainerOverrideTypeDef

### Command
- **Type**: typing.Optional[typing.Sequence[str]]

### Cpu
- **Type**: typing.Optional[int]

### Environment
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.EcsEnvironmentVariableTypeDef]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.EcsEnvironmentFileTypeDef]]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.EcsResourceRequirementTypeDef]]


# EcsEnvironmentFileTypeDef

### type
- **Type**: typing.Literal['s3']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# EcsEnvironmentVariableTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EcsEphemeralStorageTypeDef

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# EcsInferenceAcceleratorOverrideTypeDef

### deviceName
- **Type**: typing.Optional[str]

### deviceType
- **Type**: typing.Optional[str]


# EcsResourceRequirementTypeDef

### type
- **Type**: typing.Literal['GPU', 'InferenceAccelerator']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# EcsTaskOverrideOutputTypeDef

### ContainerOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.EcsContainerOverrideOutputTypeDef]]

### Cpu
- **Type**: typing.Optional[str]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.EcsEphemeralStorageTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### InferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.EcsInferenceAcceleratorOverrideTypeDef]]

### Memory
- **Type**: typing.Optional[str]

### TaskRoleArn
- **Type**: typing.Optional[str]


# EcsTaskOverrideTypeDef

### ContainerOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.EcsContainerOverrideTypeDef]]

### Cpu
- **Type**: typing.Optional[str]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.EcsEphemeralStorageTypeDef]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### InferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.EcsInferenceAcceleratorOverrideTypeDef]]

### Memory
- **Type**: typing.Optional[str]

### TaskRoleArn
- **Type**: typing.Optional[str]


# FilterCriteriaOutputTypeDef

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.FilterTypeDef]]


# FilterCriteriaTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.FilterTypeDef]]


# FilterTypeDef

### Pattern
- **Type**: typing.Optional[str]


# FirehoseLogDestinationParametersTypeDef

### DeliveryStreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# FirehoseLogDestinationTypeDef

### DeliveryStreamArn
- **Type**: typing.Optional[str]


# ListPipesRequestListPipesPaginateTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### DesiredState
- **Type**: typing.Optional[typing.Literal['RUNNING', 'STOPPED']]

### CurrentState
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']]

### SourcePrefix
- **Type**: typing.Optional[str]

### TargetPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PaginatorConfigTypeDef]


# ListPipesRequestRequestTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### DesiredState
- **Type**: typing.Optional[typing.Literal['RUNNING', 'STOPPED']]

### CurrentState
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']]

### SourcePrefix
- **Type**: typing.Optional[str]

### TargetPrefix
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListPipesResponseTypeDef

### Pipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes_classes.PipeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MQBrokerAccessCredentialsTypeDef

### BasicAuth
- **Type**: typing.Optional[str]


# MSKAccessCredentialsTypeDef

### SaslScram512Auth
- **Type**: typing.Optional[str]

### ClientCertificateTlsAuth
- **Type**: typing.Optional[str]


# MultiMeasureAttributeMappingTypeDef

### MeasureValue
- **Type**: <class 'str'>
- **Required**: Yes

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### MultiMeasureAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# MultiMeasureMappingOutputTypeDef

### MultiMeasureName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes_classes.MultiMeasureAttributeMappingTypeDef]
- **Required**: Yes


# MultiMeasureMappingTypeDef

### MultiMeasureName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiMeasureAttributeMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.MultiMeasureAttributeMappingTypeDef]
- **Required**: Yes


# NetworkConfigurationOutputTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.AwsVpcConfigurationOutputTypeDef]


# NetworkConfigurationTypeDef

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.AwsVpcConfigurationTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PipeEnrichmentHttpParametersOutputTypeDef

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeEnrichmentHttpParametersTypeDef

### PathParameterValues
- **Type**: typing.Optional[typing.Sequence[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PipeEnrichmentParametersOutputTypeDef

### InputTemplate
- **Type**: typing.Optional[str]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeEnrichmentHttpParametersOutputTypeDef]


# PipeEnrichmentParametersTypeDef

### InputTemplate
- **Type**: typing.Optional[str]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeEnrichmentHttpParametersTypeDef]


# PipeLogConfigurationParametersTypeDef

### Level
- **Type**: typing.Literal['ERROR', 'INFO', 'OFF', 'TRACE']
- **Required**: Yes

### S3LogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.S3LogDestinationParametersTypeDef]

### FirehoseLogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.FirehoseLogDestinationParametersTypeDef]

### CloudwatchLogsLogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.CloudwatchLogsLogDestinationParametersTypeDef]

### IncludeExecutionData
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ALL']]]


# PipeLogConfigurationTypeDef

### S3LogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.S3LogDestinationTypeDef]

### FirehoseLogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.FirehoseLogDestinationTypeDef]

### CloudwatchLogsLogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.CloudwatchLogsLogDestinationTypeDef]

### Level
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'OFF', 'TRACE']]

### IncludeExecutionData
- **Type**: typing.Optional[typing.List[typing.Literal['ALL']]]


# PipeSourceActiveMQBrokerParametersTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.MQBrokerAccessCredentialsTypeDef'>
- **Required**: Yes

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# PipeSourceDynamoDBStreamParametersTypeDef

### StartingPosition
- **Type**: typing.Literal['LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.DeadLetterConfigTypeDef]

### OnPartialBatchItemFailure
- **Type**: typing.Optional[typing.Literal['AUTOMATIC_BISECT']]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]


# PipeSourceKinesisStreamParametersOutputTypeDef

### StartingPosition
- **Type**: typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.DeadLetterConfigTypeDef]

### OnPartialBatchItemFailure
- **Type**: typing.Optional[typing.Literal['AUTOMATIC_BISECT']]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### StartingPositionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PipeSourceKinesisStreamParametersTypeDef

### StartingPosition
- **Type**: typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.DeadLetterConfigTypeDef]

### OnPartialBatchItemFailure
- **Type**: typing.Optional[typing.Literal['AUTOMATIC_BISECT']]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]

### StartingPositionTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PipeSourceManagedStreamingKafkaParametersTypeDef

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### StartingPosition
- **Type**: typing.Optional[typing.Literal['LATEST', 'TRIM_HORIZON']]

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ConsumerGroupID
- **Type**: typing.Optional[str]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.MSKAccessCredentialsTypeDef]


# PipeSourceParametersOutputTypeDef

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.FilterCriteriaOutputTypeDef]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceKinesisStreamParametersOutputTypeDef]

### DynamoDBStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceDynamoDBStreamParametersTypeDef]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceSqsQueueParametersTypeDef]

### ActiveMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceActiveMQBrokerParametersTypeDef]

### RabbitMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceRabbitMQBrokerParametersTypeDef]

### ManagedStreamingKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceManagedStreamingKafkaParametersTypeDef]

### SelfManagedKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceSelfManagedKafkaParametersOutputTypeDef]


# PipeSourceParametersTypeDef

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.FilterCriteriaTypeDef]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceKinesisStreamParametersTypeDef]

### DynamoDBStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceDynamoDBStreamParametersTypeDef]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceSqsQueueParametersTypeDef]

### ActiveMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceActiveMQBrokerParametersTypeDef]

### RabbitMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceRabbitMQBrokerParametersTypeDef]

### ManagedStreamingKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceManagedStreamingKafkaParametersTypeDef]

### SelfManagedKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeSourceSelfManagedKafkaParametersTypeDef]


# PipeSourceRabbitMQBrokerParametersTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.MQBrokerAccessCredentialsTypeDef'>
- **Required**: Yes

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### VirtualHost
- **Type**: typing.Optional[str]

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# PipeSourceSelfManagedKafkaParametersOutputTypeDef

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### StartingPosition
- **Type**: typing.Optional[typing.Literal['LATEST', 'TRIM_HORIZON']]

### AdditionalBootstrapServers
- **Type**: typing.Optional[typing.List[str]]

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ConsumerGroupID
- **Type**: typing.Optional[str]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.SelfManagedKafkaAccessConfigurationCredentialsTypeDef]

### ServerRootCaCertificate
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.SelfManagedKafkaAccessConfigurationVpcOutputTypeDef]


# PipeSourceSelfManagedKafkaParametersTypeDef

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes

### StartingPosition
- **Type**: typing.Optional[typing.Literal['LATEST', 'TRIM_HORIZON']]

### AdditionalBootstrapServers
- **Type**: typing.Optional[typing.Sequence[str]]

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### ConsumerGroupID
- **Type**: typing.Optional[str]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.SelfManagedKafkaAccessConfigurationCredentialsTypeDef]

### ServerRootCaCertificate
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.SelfManagedKafkaAccessConfigurationVpcTypeDef]


# PipeSourceSqsQueueParametersTypeDef

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# PipeTargetBatchJobParametersOutputTypeDef

### JobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ArrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.BatchArrayPropertiesTypeDef]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.BatchRetryStrategyTypeDef]

### ContainerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.BatchContainerOverridesOutputTypeDef]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.BatchJobDependencyTypeDef]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeTargetBatchJobParametersTypeDef

### JobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ArrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.BatchArrayPropertiesTypeDef]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.BatchRetryStrategyTypeDef]

### ContainerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.BatchContainerOverridesTypeDef]

### DependsOn
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.BatchJobDependencyTypeDef]]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PipeTargetCloudWatchLogsParametersTypeDef

### LogStreamName
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[str]


# PipeTargetEcsTaskParametersOutputTypeDef

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.NetworkConfigurationOutputTypeDef]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.CapacityProviderStrategyItemTypeDef]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.PlacementConstraintTypeDef]]

### PlacementStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.PlacementStrategyTypeDef]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.EcsTaskOverrideOutputTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.TagTypeDef]]


# PipeTargetEcsTaskParametersTypeDef

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.NetworkConfigurationTypeDef]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.CapacityProviderStrategyItemTypeDef]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.PlacementConstraintTypeDef]]

### PlacementStrategy
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.PlacementStrategyTypeDef]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.EcsTaskOverrideTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.TagTypeDef]]


# PipeTargetEventBridgeEventBusParametersOutputTypeDef

### EndpointId
- **Type**: typing.Optional[str]

### DetailType
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.List[str]]

### Time
- **Type**: typing.Optional[str]


# PipeTargetEventBridgeEventBusParametersTypeDef

### EndpointId
- **Type**: typing.Optional[str]

### DetailType
- **Type**: typing.Optional[str]

### Source
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.Sequence[str]]

### Time
- **Type**: typing.Optional[str]


# PipeTargetHttpParametersOutputTypeDef

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeTargetHttpParametersTypeDef

### PathParameterValues
- **Type**: typing.Optional[typing.Sequence[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PipeTargetKinesisStreamParametersTypeDef

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes


# PipeTargetLambdaFunctionParametersTypeDef

### InvocationType
- **Type**: typing.Optional[typing.Literal['FIRE_AND_FORGET', 'REQUEST_RESPONSE']]


# PipeTargetParametersOutputTypeDef

### InputTemplate
- **Type**: typing.Optional[str]

### LambdaFunctionParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetLambdaFunctionParametersTypeDef]

### StepFunctionStateMachineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetStateMachineParametersTypeDef]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetKinesisStreamParametersTypeDef]

### EcsTaskParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetEcsTaskParametersOutputTypeDef]

### BatchJobParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetBatchJobParametersOutputTypeDef]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetSqsQueueParametersTypeDef]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetHttpParametersOutputTypeDef]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetRedshiftDataParametersOutputTypeDef]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetSageMakerPipelineParametersOutputTypeDef]

### EventBridgeEventBusParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetEventBridgeEventBusParametersOutputTypeDef]

### CloudWatchLogsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetCloudWatchLogsParametersTypeDef]

### TimestreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetTimestreamParametersOutputTypeDef]


# PipeTargetParametersTypeDef

### InputTemplate
- **Type**: typing.Optional[str]

### LambdaFunctionParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetLambdaFunctionParametersTypeDef]

### StepFunctionStateMachineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetStateMachineParametersTypeDef]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetKinesisStreamParametersTypeDef]

### EcsTaskParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetEcsTaskParametersTypeDef]

### BatchJobParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetBatchJobParametersTypeDef]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetSqsQueueParametersTypeDef]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetHttpParametersTypeDef]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetRedshiftDataParametersTypeDef]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetSageMakerPipelineParametersTypeDef]

### EventBridgeEventBusParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetEventBridgeEventBusParametersTypeDef]

### CloudWatchLogsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetCloudWatchLogsParametersTypeDef]

### TimestreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetTimestreamParametersTypeDef]


# PipeTargetRedshiftDataParametersOutputTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Sqls
- **Type**: typing.List[str]
- **Required**: Yes

### SecretManagerArn
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### StatementName
- **Type**: typing.Optional[str]

### WithEvent
- **Type**: typing.Optional[bool]


# PipeTargetRedshiftDataParametersTypeDef

### Database
- **Type**: <class 'str'>
- **Required**: Yes

### Sqls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SecretManagerArn
- **Type**: typing.Optional[str]

### DbUser
- **Type**: typing.Optional[str]

### StatementName
- **Type**: typing.Optional[str]

### WithEvent
- **Type**: typing.Optional[bool]


# PipeTargetSageMakerPipelineParametersOutputTypeDef

### PipelineParameterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.SageMakerPipelineParameterTypeDef]]


# PipeTargetSageMakerPipelineParametersTypeDef

### PipelineParameterList
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.SageMakerPipelineParameterTypeDef]]


# PipeTargetSqsQueueParametersTypeDef

### MessageGroupId
- **Type**: typing.Optional[str]

### MessageDeduplicationId
- **Type**: typing.Optional[str]


# PipeTargetStateMachineParametersTypeDef

### InvocationType
- **Type**: typing.Optional[typing.Literal['FIRE_AND_FORGET', 'REQUEST_RESPONSE']]


# PipeTargetTimestreamParametersOutputTypeDef

### TimeValue
- **Type**: <class 'str'>
- **Required**: Yes

### VersionValue
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes_classes.DimensionMappingTypeDef]
- **Required**: Yes

### EpochTimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### TimeFieldType
- **Type**: typing.Optional[typing.Literal['EPOCH', 'TIMESTAMP_FORMAT']]

### TimestampFormat
- **Type**: typing.Optional[str]

### SingleMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.SingleMeasureMappingTypeDef]]

### MultiMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes_classes.MultiMeasureMappingOutputTypeDef]]


# PipeTargetTimestreamParametersTypeDef

### TimeValue
- **Type**: <class 'str'>
- **Required**: Yes

### VersionValue
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.DimensionMappingTypeDef]
- **Required**: Yes

### EpochTimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### TimeFieldType
- **Type**: typing.Optional[typing.Literal['EPOCH', 'TIMESTAMP_FORMAT']]

### TimestampFormat
- **Type**: typing.Optional[str]

### SingleMeasureMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.SingleMeasureMappingTypeDef]]

### MultiMeasureMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pipes_classes.MultiMeasureMappingTypeDef]]


# PipeTypeDef

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### DesiredState
- **Type**: typing.Optional[typing.Literal['RUNNING', 'STOPPED']]

### CurrentState
- **Type**: typing.Optional[typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']]

### StateReason
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Source
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]

### Enrichment
- **Type**: typing.Optional[str]


# PlacementConstraintTypeDef

### type
- **Type**: typing.Optional[typing.Literal['distinctInstance', 'memberOf']]

### expression
- **Type**: typing.Optional[str]


# PlacementStrategyTypeDef

### type
- **Type**: typing.Optional[typing.Literal['binpack', 'random', 'spread']]

### field
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


# S3LogDestinationParametersTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### BucketOwner
- **Type**: <class 'str'>
- **Required**: Yes

### OutputFormat
- **Type**: typing.Optional[typing.Literal['json', 'plain', 'w3c']]

### Prefix
- **Type**: typing.Optional[str]


# S3LogDestinationTypeDef

### BucketName
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### BucketOwner
- **Type**: typing.Optional[str]

### OutputFormat
- **Type**: typing.Optional[typing.Literal['json', 'plain', 'w3c']]


# SageMakerPipelineParameterTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SelfManagedKafkaAccessConfigurationCredentialsTypeDef

### BasicAuth
- **Type**: typing.Optional[str]

### SaslScram512Auth
- **Type**: typing.Optional[str]

### SaslScram256Auth
- **Type**: typing.Optional[str]

### ClientCertificateTlsAuth
- **Type**: typing.Optional[str]


# SelfManagedKafkaAccessConfigurationVpcOutputTypeDef

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroup
- **Type**: typing.Optional[typing.List[str]]


# SelfManagedKafkaAccessConfigurationVpcTypeDef

### Subnets
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroup
- **Type**: typing.Optional[typing.Sequence[str]]


# SingleMeasureMappingTypeDef

### MeasureValue
- **Type**: <class 'str'>
- **Required**: Yes

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### MeasureName
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### CurrentState
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopPipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### CurrentState
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdatePipeRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DesiredState
- **Type**: typing.Optional[typing.Literal['RUNNING', 'STOPPED']]

### SourceParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceParametersTypeDef]

### Enrichment
- **Type**: typing.Optional[str]

### EnrichmentParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeEnrichmentParametersTypeDef]

### Target
- **Type**: typing.Optional[str]

### TargetParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeTargetParametersTypeDef]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.PipeLogConfigurationParametersTypeDef]


# UpdatePipeResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredState
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### CurrentState
- **Type**: typing.Literal['CREATE_FAILED', 'CREATE_ROLLBACK_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETE_ROLLBACK_FAILED', 'DELETING', 'RUNNING', 'STARTING', 'START_FAILED', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'UPDATE_FAILED', 'UPDATE_ROLLBACK_FAILED', 'UPDATING']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePipeSourceActiveMQBrokerParametersTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.MQBrokerAccessCredentialsTypeDef'>
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# UpdatePipeSourceDynamoDBStreamParametersTypeDef

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.DeadLetterConfigTypeDef]

### OnPartialBatchItemFailure
- **Type**: typing.Optional[typing.Literal['AUTOMATIC_BISECT']]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]


# UpdatePipeSourceKinesisStreamParametersTypeDef

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.DeadLetterConfigTypeDef]

### OnPartialBatchItemFailure
- **Type**: typing.Optional[typing.Literal['AUTOMATIC_BISECT']]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### MaximumRecordAgeInSeconds
- **Type**: typing.Optional[int]

### MaximumRetryAttempts
- **Type**: typing.Optional[int]

### ParallelizationFactor
- **Type**: typing.Optional[int]


# UpdatePipeSourceManagedStreamingKafkaParametersTypeDef

### BatchSize
- **Type**: typing.Optional[int]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.MSKAccessCredentialsTypeDef]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# UpdatePipeSourceParametersTypeDef

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.FilterCriteriaTypeDef]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceKinesisStreamParametersTypeDef]

### DynamoDBStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceDynamoDBStreamParametersTypeDef]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceSqsQueueParametersTypeDef]

### ActiveMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceActiveMQBrokerParametersTypeDef]

### RabbitMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceRabbitMQBrokerParametersTypeDef]

### ManagedStreamingKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceManagedStreamingKafkaParametersTypeDef]

### SelfManagedKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.UpdatePipeSourceSelfManagedKafkaParametersTypeDef]


# UpdatePipeSourceRabbitMQBrokerParametersTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes_classes.MQBrokerAccessCredentialsTypeDef'>
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# UpdatePipeSourceSelfManagedKafkaParametersTypeDef

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.SelfManagedKafkaAccessConfigurationCredentialsTypeDef]

### ServerRootCaCertificate
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes_classes.SelfManagedKafkaAccessConfigurationVpcTypeDef]


# UpdatePipeSourceSqsQueueParametersTypeDef

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


