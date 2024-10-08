# Pydantic Models in braket_classes

# AlgorithmSpecificationTypeDef

### containerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket_classes.ContainerImageTypeDef]

### scriptModeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket_classes.ScriptModeConfigTypeDef]


# AssociationTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['RESERVATION_TIME_WINDOW_ARN']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequestRequestTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobResponseTypeDef

### cancellationStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING']
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelQuantumTaskRequestRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelQuantumTaskResponseTypeDef

### cancellationStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING']
- **Required**: Yes

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ContainerImageTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# CreateJobRequestRequestTypeDef

### algorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.AlgorithmSpecificationTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### deviceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.DeviceConfigTypeDef'>
- **Required**: Yes

### instanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.InstanceConfigTypeDef'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.JobOutputDataConfigTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### associations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.AssociationTypeDef]]

### checkpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket_classes.JobCheckpointConfigTypeDef]

### hyperParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### inputDataConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.InputFileConfigTypeDef]]

### stoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket_classes.JobStoppingConditionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateJobResponseTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQuantumTaskRequestRequestTypeDef

### action
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3KeyPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### shots
- **Type**: <class 'int'>
- **Required**: Yes

### associations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.AssociationTypeDef]]

### deviceParameters
- **Type**: typing.Optional[str]

### jobToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQuantumTaskResponseTypeDef

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataSourceTypeDef

### s3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.S3DataSourceTypeDef'>
- **Required**: Yes


# DeviceConfigTypeDef

### device
- **Type**: <class 'str'>
- **Required**: Yes


# DeviceQueueInfoTypeDef

### queue
- **Type**: typing.Literal['JOBS_QUEUE', 'QUANTUM_TASKS_QUEUE']
- **Required**: Yes

### queueSize
- **Type**: <class 'str'>
- **Required**: Yes

### queuePriority
- **Type**: typing.Optional[typing.Literal['Normal', 'Priority']]


# DeviceSummaryTypeDef

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### deviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deviceStatus
- **Type**: typing.Literal['OFFLINE', 'ONLINE', 'RETIRED']
- **Required**: Yes

### deviceType
- **Type**: typing.Literal['QPU', 'SIMULATOR']
- **Required**: Yes

### providerName
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceRequestRequestTypeDef

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceResponseTypeDef

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### deviceCapabilities
- **Type**: <class 'str'>
- **Required**: Yes

### deviceName
- **Type**: <class 'str'>
- **Required**: Yes

### deviceQueueInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.DeviceQueueInfoTypeDef]
- **Required**: Yes

### deviceStatus
- **Type**: typing.Literal['OFFLINE', 'ONLINE', 'RETIRED']
- **Required**: Yes

### deviceType
- **Type**: typing.Literal['QPU', 'SIMULATOR']
- **Required**: Yes

### providerName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRequestRequestTypeDef

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['QueueInfo']]]


# GetJobResponseTypeDef

### algorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.AlgorithmSpecificationTypeDef'>
- **Required**: Yes

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.AssociationTypeDef]
- **Required**: Yes

### billableDuration
- **Type**: <class 'int'>
- **Required**: Yes

### checkpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.JobCheckpointConfigTypeDef'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deviceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.DeviceConfigTypeDef'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.JobEventDetailsTypeDef]
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### hyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### inputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.InputFileConfigTypeDef]
- **Required**: Yes

### instanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.InstanceConfigTypeDef'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.JobOutputDataConfigTypeDef'>
- **Required**: Yes

### queueInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.HybridJobQueueInfoTypeDef'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### stoppingCondition
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.JobStoppingConditionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetQuantumTaskRequestRequestTypeDef

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributeNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['QueueInfo']]]


# GetQuantumTaskResponseTypeDef

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.AssociationTypeDef]
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### deviceParameters
- **Type**: <class 'str'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3Directory
- **Type**: <class 'str'>
- **Required**: Yes

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### queueInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.QuantumTaskQueueInfoTypeDef'>
- **Required**: Yes

### shots
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'CREATED', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HybridJobQueueInfoTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### queue
- **Type**: typing.Literal['JOBS_QUEUE', 'QUANTUM_TASKS_QUEUE']
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# InputFileConfigTypeDef

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.DataSourceTypeDef'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[str]


# InstanceConfigTypeDef

### instanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge']
- **Required**: Yes

### volumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes

### instanceCount
- **Type**: typing.Optional[int]


# JobCheckpointConfigTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### localPath
- **Type**: typing.Optional[str]


# JobEventDetailsTypeDef

### eventType
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DEPRIORITIZED_DUE_TO_INACTIVITY', 'DOWNLOADING_DATA', 'FAILED', 'MAX_RUNTIME_EXCEEDED', 'QUEUED_FOR_EXECUTION', 'RUNNING', 'STARTING_INSTANCE', 'UPLOADING_RESULTS', 'WAITING_FOR_PRIORITY']]

### message
- **Type**: typing.Optional[str]

### timeOfEvent
- **Type**: typing.Optional[datetime.datetime]


# JobOutputDataConfigTypeDef

### s3Path
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# JobStoppingConditionTypeDef

### maxRuntimeInSeconds
- **Type**: typing.Optional[int]


# JobSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### device
- **Type**: <class 'str'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QuantumTaskQueueInfoTypeDef

### position
- **Type**: <class 'str'>
- **Required**: Yes

### queue
- **Type**: typing.Literal['JOBS_QUEUE', 'QUANTUM_TASKS_QUEUE']
- **Required**: Yes

### message
- **Type**: typing.Optional[str]

### queuePriority
- **Type**: typing.Optional[typing.Literal['Normal', 'Priority']]


# QuantumTaskSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3Bucket
- **Type**: <class 'str'>
- **Required**: Yes

### outputS3Directory
- **Type**: <class 'str'>
- **Required**: Yes

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### shots
- **Type**: <class 'int'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'COMPLETED', 'CREATED', 'FAILED', 'QUEUED', 'RUNNING']
- **Required**: Yes

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# S3DataSourceTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# ScriptModeConfigTypeDef

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### compressionType
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]


# SearchDevicesFilterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SearchDevicesRequestRequestTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.SearchDevicesFilterTypeDef]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchDevicesRequestSearchDevicesPaginateTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.SearchDevicesFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket_classes.PaginatorConfigTypeDef]


# SearchDevicesResponseTypeDef

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.DeviceSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchJobsFilterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['BETWEEN', 'CONTAINS', 'EQUAL', 'GT', 'GTE', 'LT', 'LTE']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SearchJobsRequestRequestTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.SearchJobsFilterTypeDef]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchJobsRequestSearchJobsPaginateTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.SearchJobsFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket_classes.PaginatorConfigTypeDef]


# SearchJobsResponseTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.JobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchQuantumTasksFilterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['BETWEEN', 'EQUAL', 'GT', 'GTE', 'LT', 'LTE']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# SearchQuantumTasksRequestRequestTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.SearchQuantumTasksFilterTypeDef]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchQuantumTasksRequestSearchQuantumTasksPaginateTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.braket_classes.SearchQuantumTasksFilterTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket_classes.PaginatorConfigTypeDef]


# SearchQuantumTasksResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### quantumTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket_classes.QuantumTaskSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


