# Pipes Classes

# AwsVpcConfiguration

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AwsVpcConfigurationOutput

### Subnets
- **Type**: typing.List[str]
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]

### AssignPublicIp
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchArrayProperties

### Size
- **Type**: typing.Optional[int]


# BatchContainerOverrides

### Command
- **Type**: typing.Optional[typing.List[str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchEnvironmentVariable]]

### InstanceType
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchResourceRequirement]]


# BatchContainerOverridesOutput

### Command
- **Type**: typing.Optional[typing.List[str]]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchEnvironmentVariable]]

### InstanceType
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchResourceRequirement]]


# BatchEnvironmentVariable

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# BatchJobDependency

### JobId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['N_TO_N', 'SEQUENTIAL']]


# BatchResourceRequirement

### Type
- **Type**: typing.Literal['GPU', 'MEMORY', 'VCPU']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# BatchRetryStrategy

### Attempts
- **Type**: typing.Optional[int]


# CapacityProviderStrategyItem

### capacityProvider
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: typing.Optional[int]

### base
- **Type**: typing.Optional[int]


# CloudwatchLogsLogDestination

### LogGroupArn
- **Type**: typing.Optional[str]


# CloudwatchLogsLogDestinationParameters

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreatePipeRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceParameters, aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceParametersOutput, NoneType]

### Enrichment
- **Type**: typing.Optional[str]

### EnrichmentParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeEnrichmentParameters, aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeEnrichmentParametersOutput, NoneType]

### TargetParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetParameters, aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetParametersOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeLogConfigurationParameters]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# CreatePipeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes


# DeadLetterConfig

### Arn
- **Type**: typing.Optional[str]


# DeletePipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePipeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceParametersOutput'>
- **Required**: Yes

### Enrichment
- **Type**: <class 'str'>
- **Required**: Yes

### EnrichmentParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeEnrichmentParametersOutput'>
- **Required**: Yes

### Target
- **Type**: <class 'str'>
- **Required**: Yes

### TargetParameters
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetParametersOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeLogConfiguration'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes


# DimensionMapping

### DimensionValue
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueType
- **Type**: typing.Literal['VARCHAR']
- **Required**: Yes

### DimensionName
- **Type**: <class 'str'>
- **Required**: Yes


# EcsContainerOverride

### Command
- **Type**: typing.Optional[typing.List[str]]

### Cpu
- **Type**: typing.Optional[int]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsEnvironmentVariable]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsEnvironmentFile]]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsResourceRequirement]]


# EcsContainerOverrideOutput

### Command
- **Type**: typing.Optional[typing.List[str]]

### Cpu
- **Type**: typing.Optional[int]

### Environment
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsEnvironmentVariable]]

### EnvironmentFiles
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsEnvironmentFile]]

### Memory
- **Type**: typing.Optional[int]

### MemoryReservation
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### ResourceRequirements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsResourceRequirement]]


# EcsEnvironmentFile

### type
- **Type**: typing.Literal['s3']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# EcsEnvironmentVariable

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EcsEphemeralStorage

### sizeInGiB
- **Type**: <class 'int'>
- **Required**: Yes


# EcsInferenceAcceleratorOverride

### deviceName
- **Type**: typing.Optional[str]

### deviceType
- **Type**: typing.Optional[str]


# EcsResourceRequirement

### type
- **Type**: typing.Literal['GPU', 'InferenceAccelerator']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# EcsTaskOverride

### ContainerOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsContainerOverride]]

### Cpu
- **Type**: typing.Optional[str]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsEphemeralStorage]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### InferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsInferenceAcceleratorOverride]]

### Memory
- **Type**: typing.Optional[str]

### TaskRoleArn
- **Type**: typing.Optional[str]


# EcsTaskOverrideOutput

### ContainerOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsContainerOverrideOutput]]

### Cpu
- **Type**: typing.Optional[str]

### EphemeralStorage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsEphemeralStorage]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### InferenceAcceleratorOverrides
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsInferenceAcceleratorOverride]]

### Memory
- **Type**: typing.Optional[str]

### TaskRoleArn
- **Type**: typing.Optional[str]


# Filter

### Pattern
- **Type**: typing.Optional[str]


# FilterCriteria

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.Filter]]


# FilterCriteriaOutput

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.Filter]]


# FirehoseLogDestination

### DeliveryStreamArn
- **Type**: typing.Optional[str]


# FirehoseLogDestinationParameters

### DeliveryStreamArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListPipesRequest

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


# ListPipesRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PaginatorConfig]


# ListPipesResponse

### Pipes
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.Pipe]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes


# MQBrokerAccessCredentials

### BasicAuth
- **Type**: typing.Optional[str]


# MSKAccessCredentials

### SaslScram512Auth
- **Type**: typing.Optional[str]

### ClientCertificateTlsAuth
- **Type**: typing.Optional[str]


# MultiMeasureAttributeMapping

### MeasureValue
- **Type**: <class 'str'>
- **Required**: Yes

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### MultiMeasureAttributeName
- **Type**: <class 'str'>
- **Required**: Yes


# MultiMeasureMapping

### MultiMeasureName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.MultiMeasureAttributeMapping]
- **Required**: Yes


# MultiMeasureMappingOutput

### MultiMeasureName
- **Type**: <class 'str'>
- **Required**: Yes

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.MultiMeasureAttributeMapping]
- **Required**: Yes


# NetworkConfiguration

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.AwsVpcConfiguration]


# NetworkConfigurationOutput

### awsvpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.AwsVpcConfigurationOutput]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Pipe

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


# PipeEnrichmentHttpParameters

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeEnrichmentHttpParametersOutput

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeEnrichmentParameters

### InputTemplate
- **Type**: typing.Optional[str]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeEnrichmentHttpParameters]


# PipeEnrichmentParametersOutput

### InputTemplate
- **Type**: typing.Optional[str]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeEnrichmentHttpParametersOutput]


# PipeLogConfiguration

### S3LogDestination
- **Type**: <class 'NoneType'>

### FirehoseLogDestination
- **Type**: <class 'NoneType'>

### CloudwatchLogsLogDestination
- **Type**: <class 'NoneType'>

### Level
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'OFF', 'TRACE']]

### IncludeExecutionData
- **Type**: typing.Optional[typing.List[typing.Literal['ALL']]]


# PipeLogConfigurationParameters

### Level
- **Type**: typing.Literal['ERROR', 'INFO', 'OFF', 'TRACE']
- **Required**: Yes

### S3LogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.S3LogDestinationParameters]

### FirehoseLogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.FirehoseLogDestinationParameters]

### CloudwatchLogsLogDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.CloudwatchLogsLogDestinationParameters]

### IncludeExecutionData
- **Type**: typing.Optional[typing.List[typing.Literal['ALL']]]


# PipeSourceActiveMQBrokerParameters

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.MQBrokerAccessCredentials'>
- **Required**: Yes

### QueueName
- **Type**: <class 'str'>
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# PipeSourceDynamoDBStreamParameters

### StartingPosition
- **Type**: typing.Literal['LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

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


# PipeSourceKinesisStreamParameters

### StartingPosition
- **Type**: typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

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


# PipeSourceKinesisStreamParametersOutput

### StartingPosition
- **Type**: typing.Literal['AT_TIMESTAMP', 'LATEST', 'TRIM_HORIZON']
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

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


# PipeSourceManagedStreamingKafkaParameters

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.MSKAccessCredentials]


# PipeSourceParameters

### FilterCriteria
- **Type**: <class 'NoneType'>

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceKinesisStreamParameters]

### DynamoDBStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceDynamoDBStreamParameters]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceSqsQueueParameters]

### ActiveMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceActiveMQBrokerParameters]

### RabbitMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceRabbitMQBrokerParameters]

### ManagedStreamingKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceManagedStreamingKafkaParameters]

### SelfManagedKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceSelfManagedKafkaParameters]


# PipeSourceParametersOutput

### FilterCriteria
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.FilterCriteriaOutput]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceKinesisStreamParametersOutput]

### DynamoDBStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceDynamoDBStreamParameters]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceSqsQueueParameters]

### ActiveMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceActiveMQBrokerParameters]

### RabbitMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceRabbitMQBrokerParameters]

### ManagedStreamingKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceManagedStreamingKafkaParameters]

### SelfManagedKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeSourceSelfManagedKafkaParametersOutput]


# PipeSourceRabbitMQBrokerParameters

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.MQBrokerAccessCredentials'>
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


# PipeSourceSelfManagedKafkaParameters

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.SelfManagedKafkaAccessConfigurationCredentials]

### ServerRootCaCertificate
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.SelfManagedKafkaAccessConfigurationVpc]


# PipeSourceSelfManagedKafkaParametersOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.SelfManagedKafkaAccessConfigurationCredentials]

### ServerRootCaCertificate
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.SelfManagedKafkaAccessConfigurationVpcOutput]


# PipeSourceSqsQueueParameters

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# PipeTargetBatchJobParameters

### JobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ArrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchArrayProperties]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchRetryStrategy]

### ContainerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchContainerOverrides]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchJobDependency]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeTargetBatchJobParametersOutput

### JobDefinition
- **Type**: <class 'str'>
- **Required**: Yes

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### ArrayProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchArrayProperties]

### RetryStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchRetryStrategy]

### ContainerOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchContainerOverridesOutput]

### DependsOn
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.BatchJobDependency]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeTargetCloudWatchLogsParameters

### LogStreamName
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[str]


# PipeTargetEcsTaskParameters

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: <class 'NoneType'>

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.CapacityProviderStrategyItem]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.PlacementConstraint]]

### PlacementStrategy
- **Type**: typing.Optional[typing.List[NoneType]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsTaskOverride]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.Tag]]


# PipeTargetEcsTaskParametersOutput

### TaskDefinitionArn
- **Type**: <class 'str'>
- **Required**: Yes

### TaskCount
- **Type**: typing.Optional[int]

### LaunchType
- **Type**: typing.Optional[typing.Literal['EC2', 'EXTERNAL', 'FARGATE']]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.NetworkConfigurationOutput]

### PlatformVersion
- **Type**: typing.Optional[str]

### Group
- **Type**: typing.Optional[str]

### CapacityProviderStrategy
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.CapacityProviderStrategyItem]]

### EnableECSManagedTags
- **Type**: typing.Optional[bool]

### EnableExecuteCommand
- **Type**: typing.Optional[bool]

### PlacementConstraints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.PlacementConstraint]]

### PlacementStrategy
- **Type**: typing.Optional[typing.List[NoneType]]

### PropagateTags
- **Type**: typing.Optional[typing.Literal['TASK_DEFINITION']]

### ReferenceId
- **Type**: typing.Optional[str]

### Overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.EcsTaskOverrideOutput]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.Tag]]


# PipeTargetEventBridgeEventBusParameters

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


# PipeTargetEventBridgeEventBusParametersOutput

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


# PipeTargetHttpParameters

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeTargetHttpParametersOutput

### PathParameterValues
- **Type**: typing.Optional[typing.List[str]]

### HeaderParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### QueryStringParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# PipeTargetKinesisStreamParameters

### PartitionKey
- **Type**: <class 'str'>
- **Required**: Yes


# PipeTargetLambdaFunctionParameters

### InvocationType
- **Type**: typing.Optional[typing.Literal['FIRE_AND_FORGET', 'REQUEST_RESPONSE']]


# PipeTargetParameters

### InputTemplate
- **Type**: typing.Optional[str]

### LambdaFunctionParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetLambdaFunctionParameters]

### StepFunctionStateMachineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetStateMachineParameters]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetKinesisStreamParameters]

### EcsTaskParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetEcsTaskParameters]

### BatchJobParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetBatchJobParameters]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetSqsQueueParameters]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetHttpParameters]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetRedshiftDataParameters]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetSageMakerPipelineParameters]

### EventBridgeEventBusParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetEventBridgeEventBusParameters]

### CloudWatchLogsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetCloudWatchLogsParameters]

### TimestreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetTimestreamParameters]


# PipeTargetParametersOutput

### InputTemplate
- **Type**: typing.Optional[str]

### LambdaFunctionParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetLambdaFunctionParameters]

### StepFunctionStateMachineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetStateMachineParameters]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetKinesisStreamParameters]

### EcsTaskParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetEcsTaskParametersOutput]

### BatchJobParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetBatchJobParametersOutput]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetSqsQueueParameters]

### HttpParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetHttpParametersOutput]

### RedshiftDataParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetRedshiftDataParametersOutput]

### SageMakerPipelineParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetSageMakerPipelineParametersOutput]

### EventBridgeEventBusParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetEventBridgeEventBusParametersOutput]

### CloudWatchLogsParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetCloudWatchLogsParameters]

### TimestreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetTimestreamParametersOutput]


# PipeTargetRedshiftDataParameters

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


# PipeTargetRedshiftDataParametersOutput

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


# PipeTargetSageMakerPipelineParameters

### PipelineParameterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.SageMakerPipelineParameter]]


# PipeTargetSageMakerPipelineParametersOutput

### PipelineParameterList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.SageMakerPipelineParameter]]


# PipeTargetSqsQueueParameters

### MessageGroupId
- **Type**: typing.Optional[str]

### MessageDeduplicationId
- **Type**: typing.Optional[str]


# PipeTargetStateMachineParameters

### InvocationType
- **Type**: typing.Optional[typing.Literal['FIRE_AND_FORGET', 'REQUEST_RESPONSE']]


# PipeTargetTimestreamParameters

### TimeValue
- **Type**: <class 'str'>
- **Required**: Yes

### VersionValue
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.DimensionMapping]
- **Required**: Yes

### EpochTimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### TimeFieldType
- **Type**: typing.Optional[typing.Literal['EPOCH', 'TIMESTAMP_FORMAT']]

### TimestampFormat
- **Type**: typing.Optional[str]

### SingleMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.SingleMeasureMapping]]

### MultiMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.MultiMeasureMapping]]


# PipeTargetTimestreamParametersOutput

### TimeValue
- **Type**: <class 'str'>
- **Required**: Yes

### VersionValue
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.DimensionMapping]
- **Required**: Yes

### EpochTimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### TimeFieldType
- **Type**: typing.Optional[typing.Literal['EPOCH', 'TIMESTAMP_FORMAT']]

### TimestampFormat
- **Type**: typing.Optional[str]

### SingleMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.SingleMeasureMapping]]

### MultiMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pipes.pipes_classes.MultiMeasureMappingOutput]]


# PlacementConstraint

### type
- **Type**: typing.Optional[typing.Literal['distinctInstance', 'memberOf']]

### expression
- **Type**: typing.Optional[str]


# PlacementStrategy

### type
- **Type**: typing.Optional[typing.Literal['binpack', 'random', 'spread']]

### field
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


# S3LogDestination

### BucketName
- **Type**: typing.Optional[str]

### Prefix
- **Type**: typing.Optional[str]

### BucketOwner
- **Type**: typing.Optional[str]

### OutputFormat
- **Type**: typing.Optional[typing.Literal['json', 'plain', 'w3c']]


# S3LogDestinationParameters

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


# SageMakerPipelineParameter

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SelfManagedKafkaAccessConfigurationCredentials

### BasicAuth
- **Type**: typing.Optional[str]

### SaslScram512Auth
- **Type**: typing.Optional[str]

### SaslScram256Auth
- **Type**: typing.Optional[str]

### ClientCertificateTlsAuth
- **Type**: typing.Optional[str]


# SelfManagedKafkaAccessConfigurationVpc

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroup
- **Type**: typing.Optional[typing.List[str]]


# SelfManagedKafkaAccessConfigurationVpcOutput

### Subnets
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroup
- **Type**: typing.Optional[typing.List[str]]


# SingleMeasureMapping

### MeasureValue
- **Type**: <class 'str'>
- **Required**: Yes

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### MeasureName
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StartPipeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes


# StopPipeRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# StopPipeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdatePipeRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceParameters]

### Enrichment
- **Type**: typing.Optional[str]

### EnrichmentParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeEnrichmentParameters, aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeEnrichmentParametersOutput, NoneType]

### Target
- **Type**: typing.Optional[str]

### TargetParameters
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetParameters, aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeTargetParametersOutput, NoneType]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.PipeLogConfigurationParameters]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# UpdatePipeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePipeSourceActiveMQBrokerParameters

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.MQBrokerAccessCredentials'>
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# UpdatePipeSourceDynamoDBStreamParameters

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

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


# UpdatePipeSourceKinesisStreamParameters

### BatchSize
- **Type**: typing.Optional[int]

### DeadLetterConfig
- **Type**: <class 'NoneType'>

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


# UpdatePipeSourceManagedStreamingKafkaParameters

### BatchSize
- **Type**: typing.Optional[int]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.MSKAccessCredentials]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# UpdatePipeSourceParameters

### FilterCriteria
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pipes.pipes_classes.FilterCriteria, aws_resource_validator.pydantic_models.pipes.pipes_classes.FilterCriteriaOutput, NoneType]

### KinesisStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceKinesisStreamParameters]

### DynamoDBStreamParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceDynamoDBStreamParameters]

### SqsQueueParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceSqsQueueParameters]

### ActiveMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceActiveMQBrokerParameters]

### RabbitMQBrokerParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceRabbitMQBrokerParameters]

### ManagedStreamingKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceManagedStreamingKafkaParameters]

### SelfManagedKafkaParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.UpdatePipeSourceSelfManagedKafkaParameters]


# UpdatePipeSourceRabbitMQBrokerParameters

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.pipes.pipes_classes.MQBrokerAccessCredentials'>
- **Required**: Yes

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


# UpdatePipeSourceSelfManagedKafkaParameters

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pipes.pipes_classes.SelfManagedKafkaAccessConfigurationCredentials]

### ServerRootCaCertificate
- **Type**: typing.Optional[str]

### Vpc
- **Type**: typing.Union[aws_resource_validator.pydantic_models.pipes.pipes_classes.SelfManagedKafkaAccessConfigurationVpc, aws_resource_validator.pydantic_models.pipes.pipes_classes.SelfManagedKafkaAccessConfigurationVpcOutput, NoneType]


# UpdatePipeSourceSqsQueueParameters

### BatchSize
- **Type**: typing.Optional[int]

### MaximumBatchingWindowInSeconds
- **Type**: typing.Optional[int]


