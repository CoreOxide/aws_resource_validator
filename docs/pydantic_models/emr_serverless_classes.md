# Emr Serverless Classes

# ApplicationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplicationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AutoStartConfigTypeDef

### enabled
- **Type**: typing.Optional[bool]


# AutoStopConfigTypeDef

### enabled
- **Type**: typing.Optional[bool]

### idleTimeoutMinutes
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRunRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobRunResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CloudWatchLoggingConfigurationOutputTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### logGroupName
- **Type**: typing.Optional[str]

### logStreamNamePrefix
- **Type**: typing.Optional[str]

### encryptionKeyArn
- **Type**: typing.Optional[str]

### logTypes
- **Type**: typing.Optional[typing.Dict[str, typing.List[str]]]


# CloudWatchLoggingConfigurationTypeDef

### enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### logGroupName
- **Type**: typing.Optional[str]

### logStreamNamePrefix
- **Type**: typing.Optional[str]

### encryptionKeyArn
- **Type**: typing.Optional[str]

### logTypes
- **Type**: typing.Optional[typing.Mapping[str, typing.Sequence[str]]]


# ConfigurationOutputTypeDef

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ConfigurationOverridesOutputTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationOutputTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MonitoringConfigurationOutputTypeDef]


# ConfigurationOverridesTypeDef

### applicationConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MonitoringConfigurationTypeDef]


# ConfigurationOverridesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationTypeDef

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### configurations
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, typing.Any]]]


# ConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponseTypeDef

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDashboardForJobRunRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### attempt
- **Type**: typing.Optional[int]

### accessSystemProfileLogs
- **Type**: typing.Optional[bool]


# GetDashboardForJobRunResponseTypeDef

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRunRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### attempt
- **Type**: typing.Optional[int]


# GetJobRunResponseTypeDef

### jobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.JobRunTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HiveTypeDef

### query
- **Type**: <class 'str'>
- **Required**: Yes

### initQueryFile
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[str]


# ImageConfigurationInputTypeDef

### imageUri
- **Type**: typing.Optional[str]


# ImageConfigurationTypeDef

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes

### resolvedImageDigest
- **Type**: typing.Optional[str]


# InitialCapacityConfigTypeDef

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes

### workerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.WorkerResourceConfigTypeDef]


# InteractiveConfigurationTypeDef

### studioEnabled
- **Type**: typing.Optional[bool]

### livyEndpointEnabled
- **Type**: typing.Optional[bool]


# JobDriverOutputTypeDef

### sparkSubmit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.SparkSubmitOutputTypeDef]

### hive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.HiveTypeDef]


# JobDriverTypeDef

### sparkSubmit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.SparkSubmitTypeDef]

### hive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.HiveTypeDef]


# JobDriverUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunAttemptSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobRunTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### executionRole
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'QUEUED', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']
- **Required**: Yes

### stateDetails
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.JobDriverOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationOverridesOutputTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### totalResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.TotalResourceUtilizationTypeDef]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.NetworkConfigurationOutputTypeDef]

### totalExecutionDurationSeconds
- **Type**: typing.Optional[int]

### executionTimeoutMinutes
- **Type**: typing.Optional[int]

### billedResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ResourceUtilizationTypeDef]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.RetryPolicyTypeDef]

### attempt
- **Type**: typing.Optional[int]

### attemptCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### attemptUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### startedAt
- **Type**: typing.Optional[datetime.datetime]

### endedAt
- **Type**: typing.Optional[datetime.datetime]

### queuedDurationMilliseconds
- **Type**: typing.Optional[int]


# ListApplicationsRequestPaginateTypeDef

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATED', 'CREATING', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'TERMINATED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATED', 'CREATING', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'TERMINATED']]]


# ListApplicationsResponseTypeDef

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_serverless_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunAttemptsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PaginatorConfigTypeDef]


# ListJobRunAttemptsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListJobRunAttemptsResponseTypeDef

### jobRunAttempts
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_serverless_classes.JobRunAttemptSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsRequestPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAtAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.TimestampTypeDef]

### createdAtBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.TimestampTypeDef]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'QUEUED', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']]]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PaginatorConfigTypeDef]


# ListJobRunsRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### createdAtAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.TimestampTypeDef]

### createdAtBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.TimestampTypeDef]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'QUEUED', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']]]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]


# ListJobRunsResponseTypeDef

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_serverless_classes.JobRunSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedPersistenceMonitoringConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]

### encryptionKeyArn
- **Type**: typing.Optional[str]


# MaximumAllowedResourcesTypeDef

### cpu
- **Type**: <class 'str'>
- **Required**: Yes

### memory
- **Type**: <class 'str'>
- **Required**: Yes

### disk
- **Type**: typing.Optional[str]


# MonitoringConfigurationOutputTypeDef

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.S3MonitoringConfigurationTypeDef]

### managedPersistenceMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ManagedPersistenceMonitoringConfigurationTypeDef]

### cloudWatchLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.CloudWatchLoggingConfigurationOutputTypeDef]

### prometheusMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PrometheusMonitoringConfigurationTypeDef]


# MonitoringConfigurationTypeDef

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.S3MonitoringConfigurationTypeDef]

### managedPersistenceMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ManagedPersistenceMonitoringConfigurationTypeDef]

### cloudWatchLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.CloudWatchLoggingConfigurationTypeDef]

### prometheusMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PrometheusMonitoringConfigurationTypeDef]


# MonitoringConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkConfigurationOutputTypeDef

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# NetworkConfigurationTypeDef

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# NetworkConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrometheusMonitoringConfigurationTypeDef

### remoteWriteUrl
- **Type**: typing.Optional[str]


# ResourceUtilizationTypeDef

### vCPUHour
- **Type**: typing.Optional[float]

### memoryGBHour
- **Type**: typing.Optional[float]

### storageGBHour
- **Type**: typing.Optional[float]


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


# RetryPolicyTypeDef

### maxAttempts
- **Type**: typing.Optional[int]

### maxFailedAttemptsPerHour
- **Type**: typing.Optional[int]


# S3MonitoringConfigurationTypeDef

### logUri
- **Type**: typing.Optional[str]

### encryptionKeyArn
- **Type**: typing.Optional[str]


# SchedulerConfigurationTypeDef

### queueTimeoutMinutes
- **Type**: typing.Optional[int]

### maxConcurrentRuns
- **Type**: typing.Optional[int]


# SparkSubmitOutputTypeDef

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.List[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# SparkSubmitTypeDef

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.Sequence[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# StartApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartJobRunRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### jobDriver
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.JobDriverUnionTypeDef]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationOverridesUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### executionTimeoutMinutes
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.RetryPolicyTypeDef]


# StartJobRunResponseTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TotalResourceUtilizationTypeDef

### vCPUHour
- **Type**: typing.Optional[float]

### memoryGBHour
- **Type**: typing.Optional[float]

### storageGBHour
- **Type**: typing.Optional[float]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### initialCapacity
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.emr_serverless_classes.InitialCapacityConfigTypeDef]]

### maximumCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MaximumAllowedResourcesTypeDef]

### autoStartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.AutoStartConfigTypeDef]

### autoStopConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.AutoStopConfigTypeDef]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.NetworkConfigurationUnionTypeDef]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ImageConfigurationInputTypeDef]

### workerTypeSpecifications
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.emr_serverless_classes.WorkerTypeSpecificationInputTypeDef]]

### interactiveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.InteractiveConfigurationTypeDef]

### releaseLabel
- **Type**: typing.Optional[str]

### runtimeConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationUnionTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MonitoringConfigurationUnionTypeDef]

### schedulerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.SchedulerConfigurationTypeDef]


# UpdateApplicationResponseTypeDef

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkerResourceConfigTypeDef

### cpu
- **Type**: <class 'str'>
- **Required**: Yes

### memory
- **Type**: <class 'str'>
- **Required**: Yes

### disk
- **Type**: typing.Optional[str]

### diskType
- **Type**: typing.Optional[str]


# WorkerTypeSpecificationInputTypeDef

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ImageConfigurationInputTypeDef]


# WorkerTypeSpecificationTypeDef

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ImageConfigurationTypeDef]


