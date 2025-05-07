# Emr Serverless Classes

# Application

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CREATED', 'CREATING', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'TERMINATED']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### stateDetails
- **Type**: typing.Optional[str]

### initialCapacity
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.InitialCapacityConfig]]

### maximumCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MaximumAllowedResources]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### autoStartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.AutoStartConfig]

### autoStopConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.AutoStopConfig]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.NetworkConfigurationOutput]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ImageConfiguration]

### workerTypeSpecifications
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.WorkerTypeSpecification]]

### runtimeConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ConfigurationOutput]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MonitoringConfigurationOutput]

### interactiveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.InteractiveConfiguration]

### schedulerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.SchedulerConfiguration]


# ApplicationSummary

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['CREATED', 'CREATING', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'TERMINATED']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### stateDetails
- **Type**: typing.Optional[str]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]


# AutoStartConfig

### enabled
- **Type**: typing.Optional[bool]


# AutoStopConfig

### enabled
- **Type**: typing.Optional[bool]

### idleTimeoutMinutes
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRunRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelJobRunResponse

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# CloudWatchLoggingConfiguration

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


# CloudWatchLoggingConfigurationOutput

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


# Configuration

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ConfigurationOutput

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Dict[str, str]]

### configurations
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# ConfigurationOverrides

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.Configuration]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MonitoringConfiguration]


# ConfigurationOverridesOutput

### applicationConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ConfigurationOutput]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MonitoringConfigurationOutput]


# CreateApplicationRequest

### releaseLabel
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### initialCapacity
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.InitialCapacityConfig]]

### maximumCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MaximumAllowedResources]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### autoStartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.AutoStartConfig]

### autoStopConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.AutoStopConfig]

### networkConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.NetworkConfiguration, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.NetworkConfigurationOutput, NoneType]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ImageConfigurationInput]

### workerTypeSpecifications
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.WorkerTypeSpecificationInput]]

### runtimeConfiguration
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.Configuration, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ConfigurationOutput]]]

### monitoringConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MonitoringConfiguration, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MonitoringConfigurationOutput, NoneType]

### interactiveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.InteractiveConfiguration]

### schedulerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.SchedulerConfiguration]


# CreateApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationResponse

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.Application'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetDashboardForJobRunRequest

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


# GetDashboardForJobRunResponse

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobRunRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### attempt
- **Type**: typing.Optional[int]


# GetJobRunResponse

### jobRun
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.JobRun'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# Hive

### query
- **Type**: <class 'str'>
- **Required**: Yes

### initQueryFile
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[str]


# ImageConfiguration

### imageUri
- **Type**: <class 'str'>
- **Required**: Yes

### resolvedImageDigest
- **Type**: typing.Optional[str]


# ImageConfigurationInput

### imageUri
- **Type**: typing.Optional[str]


# InitialCapacityConfig

### workerCount
- **Type**: <class 'int'>
- **Required**: Yes

### workerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.WorkerResourceConfig]


# InteractiveConfiguration

### studioEnabled
- **Type**: typing.Optional[bool]

### livyEndpointEnabled
- **Type**: typing.Optional[bool]


# JobDriver

### sparkSubmit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.SparkSubmit]

### hive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.Hive]


# JobDriverOutput

### sparkSubmit
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.SparkSubmitOutput]

### hive
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.Hive]


# JobRun

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.JobDriverOutput'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ConfigurationOverridesOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### totalResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.TotalResourceUtilization]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.NetworkConfigurationOutput]

### totalExecutionDurationSeconds
- **Type**: typing.Optional[int]

### executionTimeoutMinutes
- **Type**: typing.Optional[int]

### billedResourceUtilization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResourceUtilization]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.RetryPolicy]

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


# JobRunAttemptSummary

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdBy
- **Type**: <class 'str'>
- **Required**: Yes

### jobCreatedAt
- **Type**: <class 'datetime.datetime'>
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

### name
- **Type**: typing.Optional[str]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### type
- **Type**: typing.Optional[str]

### attempt
- **Type**: typing.Optional[int]


# JobRunSummary

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### id
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

### name
- **Type**: typing.Optional[str]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### type
- **Type**: typing.Optional[str]

### attempt
- **Type**: typing.Optional[int]

### attemptCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### attemptUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# ListApplicationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['CREATED', 'CREATING', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'TERMINATED']]]


# ListApplicationsRequestPaginate

### states
- **Type**: typing.Optional[typing.List[typing.Literal['CREATED', 'CREATING', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'TERMINATED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.PaginatorConfig]


# ListApplicationsResponse

### applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunAttemptsRequest

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


# ListJobRunAttemptsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.PaginatorConfig]


# ListJobRunAttemptsResponse

### jobRunAttempts
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.JobRunAttemptSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListJobRunsRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### createdAtAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAtBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'QUEUED', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']]]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]


# ListJobRunsRequestPaginate

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAtAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAtBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### states
- **Type**: typing.Optional[typing.List[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'QUEUED', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']]]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.PaginatorConfig]


# ListJobRunsResponse

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.JobRunSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# ManagedPersistenceMonitoringConfiguration

### enabled
- **Type**: typing.Optional[bool]

### encryptionKeyArn
- **Type**: typing.Optional[str]


# MaximumAllowedResources

### cpu
- **Type**: <class 'str'>
- **Required**: Yes

### memory
- **Type**: <class 'str'>
- **Required**: Yes

### disk
- **Type**: typing.Optional[str]


# MonitoringConfiguration

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.S3MonitoringConfiguration]

### managedPersistenceMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ManagedPersistenceMonitoringConfiguration]

### cloudWatchLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.CloudWatchLoggingConfiguration]

### prometheusMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.PrometheusMonitoringConfiguration]


# MonitoringConfigurationOutput

### s3MonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.S3MonitoringConfiguration]

### managedPersistenceMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ManagedPersistenceMonitoringConfiguration]

### cloudWatchLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.CloudWatchLoggingConfigurationOutput]

### prometheusMonitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.PrometheusMonitoringConfiguration]


# NetworkConfiguration

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# NetworkConfigurationOutput

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PrometheusMonitoringConfiguration

### remoteWriteUrl
- **Type**: typing.Optional[str]


# ResourceUtilization

### vCPUHour
- **Type**: typing.Optional[float]

### memoryGBHour
- **Type**: typing.Optional[float]

### storageGBHour
- **Type**: typing.Optional[float]


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


# RetryPolicy

### maxAttempts
- **Type**: typing.Optional[int]

### maxFailedAttemptsPerHour
- **Type**: typing.Optional[int]


# S3MonitoringConfiguration

### logUri
- **Type**: typing.Optional[str]

### encryptionKeyArn
- **Type**: typing.Optional[str]


# SchedulerConfiguration

### queueTimeoutMinutes
- **Type**: typing.Optional[int]

### maxConcurrentRuns
- **Type**: typing.Optional[int]


# SparkSubmit

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.List[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# SparkSubmitOutput

### entryPoint
- **Type**: <class 'str'>
- **Required**: Yes

### entryPointArguments
- **Type**: typing.Optional[typing.List[str]]

### sparkSubmitParameters
- **Type**: typing.Optional[str]


# StartApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartJobRunRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.JobDriver, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.JobDriverOutput, NoneType]

### configurationOverrides
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ConfigurationOverrides, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ConfigurationOverridesOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### executionTimeoutMinutes
- **Type**: typing.Optional[int]

### name
- **Type**: typing.Optional[str]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### retryPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.RetryPolicy]


# StartJobRunResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# StopApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TotalResourceUtilization

### vCPUHour
- **Type**: typing.Optional[float]

### memoryGBHour
- **Type**: typing.Optional[float]

### storageGBHour
- **Type**: typing.Optional[float]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationRequest

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### initialCapacity
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.InitialCapacityConfig]]

### maximumCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MaximumAllowedResources]

### autoStartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.AutoStartConfig]

### autoStopConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.AutoStopConfig]

### networkConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.NetworkConfiguration, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.NetworkConfigurationOutput, NoneType]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ImageConfigurationInput]

### workerTypeSpecifications
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.WorkerTypeSpecificationInput]]

### interactiveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.InteractiveConfiguration]

### releaseLabel
- **Type**: typing.Optional[str]

### runtimeConfiguration
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.Configuration, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ConfigurationOutput]]]

### monitoringConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MonitoringConfiguration, aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.MonitoringConfigurationOutput, NoneType]

### schedulerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.SchedulerConfiguration]


# UpdateApplicationResponse

### application
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.Application'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ResponseMetadata'>
- **Required**: Yes


# WorkerResourceConfig

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


# WorkerTypeSpecification

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ImageConfiguration]


# WorkerTypeSpecificationInput

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless.emr_serverless_classes.ImageConfigurationInput]


