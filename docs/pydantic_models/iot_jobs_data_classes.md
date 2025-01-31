# iot_jobs_data_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeJobExecutionRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### includeJobDocument
- **Type**: typing.Optional[bool]

### executionNumber
- **Type**: typing.Optional[int]


# DescribeJobExecutionResponseTypeDef

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_jobs_data_classes.JobExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_jobs_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPendingJobExecutionsRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPendingJobExecutionsResponseTypeDef

### inProgressJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_jobs_data_classes.JobExecutionSummaryTypeDef]
- **Required**: Yes

### queuedJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_jobs_data_classes.JobExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_jobs_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# JobExecutionStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### statusDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionNumber
- **Type**: typing.Optional[int]


# JobExecutionSummaryTypeDef

### jobId
- **Type**: typing.Optional[str]

### queuedAt
- **Type**: typing.Optional[int]

### startedAt
- **Type**: typing.Optional[int]

### lastUpdatedAt
- **Type**: typing.Optional[int]

### versionNumber
- **Type**: typing.Optional[int]

### executionNumber
- **Type**: typing.Optional[int]


# JobExecutionTypeDef

### jobId
- **Type**: typing.Optional[str]

### thingName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']]

### statusDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### queuedAt
- **Type**: typing.Optional[int]

### startedAt
- **Type**: typing.Optional[int]

### lastUpdatedAt
- **Type**: typing.Optional[int]

### approximateSecondsBeforeTimedOut
- **Type**: typing.Optional[int]

### versionNumber
- **Type**: typing.Optional[int]

### executionNumber
- **Type**: typing.Optional[int]

### jobDocument
- **Type**: typing.Optional[str]


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


# StartNextPendingJobExecutionRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### statusDetails
- **Type**: typing.Optional[typing.Mapping[str, str]]

### stepTimeoutInMinutes
- **Type**: typing.Optional[int]


# StartNextPendingJobExecutionResponseTypeDef

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_jobs_data_classes.JobExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_jobs_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateJobExecutionRequestRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CANCELED', 'FAILED', 'IN_PROGRESS', 'QUEUED', 'REJECTED', 'REMOVED', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### statusDetails
- **Type**: typing.Optional[typing.Mapping[str, str]]

### stepTimeoutInMinutes
- **Type**: typing.Optional[int]

### expectedVersion
- **Type**: typing.Optional[int]

### includeJobExecutionState
- **Type**: typing.Optional[bool]

### includeJobDocument
- **Type**: typing.Optional[bool]

### executionNumber
- **Type**: typing.Optional[int]


# UpdateJobExecutionResponseTypeDef

### executionState
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_jobs_data_classes.JobExecutionStateTypeDef'>
- **Required**: Yes

### jobDocument
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_jobs_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


