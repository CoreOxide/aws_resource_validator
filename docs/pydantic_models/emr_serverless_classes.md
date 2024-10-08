# Pydantic Models in emr_serverless_classes

# ApplicationSummaryTypeDef

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


# ApplicationTypeDef

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless_classes.InitialCapacityConfigTypeDef]]

### maximumCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MaximumAllowedResourcesTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### autoStartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.AutoStartConfigTypeDef]

### autoStopConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.AutoStopConfigTypeDef]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.NetworkConfigurationOutputTypeDef]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ImageConfigurationTypeDef]

### workerTypeSpecifications
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.emr_serverless_classes.WorkerTypeSpecificationTypeDef]]

### runtimeConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationOutputTypeDef]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MonitoringConfigurationOutputTypeDef]

### interactiveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.InteractiveConfigurationTypeDef]


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

# CancelJobRunRequestRequestTypeDef

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


# ConfigurationTypeDef

### classification
- **Type**: <class 'str'>
- **Required**: Yes

### properties
- **Type**: typing.Optional[typing.Mapping[str, str]]

### configurations
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]


# CreateApplicationRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.emr_serverless_classes.InitialCapacityConfigTypeDef]]

### maximumCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MaximumAllowedResourcesTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### autoStartConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.AutoStartConfigTypeDef]

### autoStopConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.AutoStopConfigTypeDef]

### networkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.NetworkConfigurationTypeDef]

### architecture
- **Type**: typing.Optional[typing.Literal['ARM64', 'X86_64']]

### imageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ImageConfigurationInputTypeDef]

### workerTypeSpecifications
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.emr_serverless_classes.WorkerTypeSpecificationInputTypeDef]]

### runtimeConfiguration
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationTypeDef, aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationOutputTypeDef]]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MonitoringConfigurationTypeDef]

### interactiveConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.InteractiveConfigurationTypeDef]


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


# DeleteApplicationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationRequestRequestTypeDef

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


# GetDashboardForJobRunRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### attempt
- **Type**: typing.Optional[int]


# GetDashboardForJobRunResponseTypeDef

### url
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobRunRequestRequestTypeDef

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


# JobRunAttemptSummaryTypeDef

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
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']
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


# JobRunSummaryTypeDef

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
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']
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
- **Type**: typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']
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


# ListApplicationsRequestListApplicationsPaginateTypeDef

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATED', 'CREATING', 'STARTED', 'STARTING', 'STOPPED', 'STOPPING', 'TERMINATED']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobRunAttemptsRequestListJobRunAttemptsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### jobRunId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PaginatorConfigTypeDef]


# ListJobRunAttemptsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobRunsRequestListJobRunsPaginateTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAtAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### createdAtBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### states
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']]]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.PaginatorConfigTypeDef]


# ListJobRunsRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CANCELLED', 'CANCELLING', 'FAILED', 'PENDING', 'RUNNING', 'SCHEDULED', 'SUBMITTED', 'SUCCESS']]]

### mode
- **Type**: typing.Optional[typing.Literal['BATCH', 'STREAMING']]


# ListJobRunsResponseTypeDef

### jobRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.emr_serverless_classes.JobRunSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.emr_serverless_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# StartApplicationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# StartJobRunRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.JobDriverTypeDef]

### configurationOverrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationOverridesTypeDef]

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


# StopApplicationRequestRequestTypeDef

### applicationId
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TotalResourceUtilizationTypeDef

### vCPUHour
- **Type**: typing.Optional[float]

### memoryGBHour
- **Type**: typing.Optional[float]

### storageGBHour
- **Type**: typing.Optional[float]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.NetworkConfigurationTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationTypeDef, aws_resource_validator.pydantic_models.emr_serverless_classes.ConfigurationOutputTypeDef]]]

### monitoringConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.emr_serverless_classes.MonitoringConfigurationTypeDef]


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


