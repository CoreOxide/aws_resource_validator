# Braket Classes

# AlgorithmSpecification

### containerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket.braket_classes.ContainerImage]

### scriptModeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket.braket_classes.ScriptModeConfig]


# Association

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['RESERVATION_TIME_WINDOW_ARN']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequest

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobResponse

### cancellationStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING']
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# CancelQuantumTaskRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# CancelQuantumTaskResponse

### cancellationStatus
- **Type**: typing.Literal['CANCELLED', 'CANCELLING']
- **Required**: Yes

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# ContainerImage

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# CreateJobRequest

### algorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.AlgorithmSpecification'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### deviceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.DeviceConfig'>
- **Required**: Yes

### instanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.InstanceConfig'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.JobOutputDataConfig'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.Association]]

### checkpointConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket.braket_classes.JobCheckpointConfig]

### hyperParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### inputDataConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.InputFileConfig]]

### stoppingCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket.braket_classes.JobStoppingCondition]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateJobResponse

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQuantumTaskRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.Association]]

### deviceParameters
- **Type**: typing.Optional[str]

### jobToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateQuantumTaskResponse

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# DataSource

### s3DataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.S3DataSource'>
- **Required**: Yes


# DeviceConfig

### device
- **Type**: <class 'str'>
- **Required**: Yes


# DeviceQueueInfo

### queue
- **Type**: typing.Literal['JOBS_QUEUE', 'QUANTUM_TASKS_QUEUE']
- **Required**: Yes

### queueSize
- **Type**: <class 'str'>
- **Required**: Yes

### queuePriority
- **Type**: typing.Optional[typing.Literal['Normal', 'Priority']]


# DeviceSummary

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


# GetDeviceRequest

### deviceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeviceResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.DeviceQueueInfo]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRequest

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributeNames
- **Type**: typing.Optional[typing.List[typing.Literal['QueueInfo']]]


# GetJobResponse

### algorithmSpecification
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.AlgorithmSpecification'>
- **Required**: Yes

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.Association]
- **Required**: Yes

### billableDuration
- **Type**: <class 'int'>
- **Required**: Yes

### checkpointConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.JobCheckpointConfig'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### deviceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.DeviceConfig'>
- **Required**: Yes

### endedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.JobEventDetails]
- **Required**: Yes

### failureReason
- **Type**: <class 'str'>
- **Required**: Yes

### hyperParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### inputDataConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.InputFileConfig]
- **Required**: Yes

### instanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.InstanceConfig'>
- **Required**: Yes

### jobArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobName
- **Type**: <class 'str'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.JobOutputDataConfig'>
- **Required**: Yes

### queueInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.HybridJobQueueInfo'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.JobStoppingCondition'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# GetQuantumTaskRequest

### quantumTaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalAttributeNames
- **Type**: typing.Optional[typing.List[typing.Literal['QueueInfo']]]


# GetQuantumTaskResponse

### associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.Association]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.QuantumTaskQueueInfo'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# HybridJobQueueInfo

### position
- **Type**: <class 'str'>
- **Required**: Yes

### queue
- **Type**: typing.Literal['JOBS_QUEUE', 'QUANTUM_TASKS_QUEUE']
- **Required**: Yes

### message
- **Type**: typing.Optional[str]


# InputFileConfig

### channelName
- **Type**: <class 'str'>
- **Required**: Yes

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.DataSource'>
- **Required**: Yes

### contentType
- **Type**: typing.Optional[str]


# InstanceConfig

### instanceType
- **Type**: typing.Literal['ml.c4.2xlarge', 'ml.c4.4xlarge', 'ml.c4.8xlarge', 'ml.c4.xlarge', 'ml.c5.18xlarge', 'ml.c5.2xlarge', 'ml.c5.4xlarge', 'ml.c5.9xlarge', 'ml.c5.xlarge', 'ml.c5n.18xlarge', 'ml.c5n.2xlarge', 'ml.c5n.4xlarge', 'ml.c5n.9xlarge', 'ml.c5n.xlarge', 'ml.g4dn.12xlarge', 'ml.g4dn.16xlarge', 'ml.g4dn.2xlarge', 'ml.g4dn.4xlarge', 'ml.g4dn.8xlarge', 'ml.g4dn.xlarge', 'ml.m4.10xlarge', 'ml.m4.16xlarge', 'ml.m4.2xlarge', 'ml.m4.4xlarge', 'ml.m4.xlarge', 'ml.m5.12xlarge', 'ml.m5.24xlarge', 'ml.m5.2xlarge', 'ml.m5.4xlarge', 'ml.m5.large', 'ml.m5.xlarge', 'ml.p2.16xlarge', 'ml.p2.8xlarge', 'ml.p2.xlarge', 'ml.p3.16xlarge', 'ml.p3.2xlarge', 'ml.p3.8xlarge', 'ml.p3dn.24xlarge', 'ml.p4d.24xlarge']
- **Required**: Yes

### volumeSizeInGb
- **Type**: <class 'int'>
- **Required**: Yes

### instanceCount
- **Type**: typing.Optional[int]


# JobCheckpointConfig

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### localPath
- **Type**: typing.Optional[str]


# JobEventDetails

### eventType
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'DEPRIORITIZED_DUE_TO_INACTIVITY', 'DOWNLOADING_DATA', 'FAILED', 'MAX_RUNTIME_EXCEEDED', 'QUEUED_FOR_EXECUTION', 'RUNNING', 'STARTING_INSTANCE', 'UPLOADING_RESULTS', 'WAITING_FOR_PRIORITY']]

### message
- **Type**: typing.Optional[str]

### timeOfEvent
- **Type**: typing.Optional[datetime.datetime]


# JobOutputDataConfig

### s3Path
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]


# JobStoppingCondition

### maxRuntimeInSeconds
- **Type**: typing.Optional[int]


# JobSummary

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


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QuantumTaskQueueInfo

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


# QuantumTaskSummary

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


# S3DataSource

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes


# ScriptModeConfig

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### compressionType
- **Type**: typing.Optional[typing.Literal['GZIP', 'NONE']]


# SearchDevicesFilter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# SearchDevicesRequest

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.SearchDevicesFilter]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchDevicesRequestPaginate

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.SearchDevicesFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket.braket_classes.PaginatorConfig]


# SearchDevicesResponse

### devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.DeviceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchJobsFilter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['BETWEEN', 'CONTAINS', 'EQUAL', 'GT', 'GTE', 'LT', 'LTE']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# SearchJobsRequest

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.SearchJobsFilter]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchJobsRequestPaginate

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.SearchJobsFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket.braket_classes.PaginatorConfig]


# SearchJobsResponse

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.JobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchQuantumTasksFilter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['BETWEEN', 'EQUAL', 'GT', 'GTE', 'LT', 'LTE']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# SearchQuantumTasksRequest

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.SearchQuantumTasksFilter]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchQuantumTasksRequestPaginate

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.SearchQuantumTasksFilter]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.braket.braket_classes.PaginatorConfig]


# SearchQuantumTasksResponse

### quantumTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.braket.braket_classes.QuantumTaskSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.braket.braket_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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


