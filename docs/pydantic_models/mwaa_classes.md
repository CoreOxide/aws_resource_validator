# Mwaa Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCliTokenRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCliTokenResponse

### CliToken
- **Type**: <class 'str'>
- **Required**: Yes

### WebServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes


# CreateEnvironmentInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceBucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### DagS3Path
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.NetworkConfigurationUnion'>
- **Required**: Yes

### PluginsS3Path
- **Type**: typing.Optional[str]

### PluginsS3ObjectVersion
- **Type**: typing.Optional[str]

### RequirementsS3Path
- **Type**: typing.Optional[str]

### RequirementsS3ObjectVersion
- **Type**: typing.Optional[str]

### StartupScriptS3Path
- **Type**: typing.Optional[str]

### StartupScriptS3ObjectVersion
- **Type**: typing.Optional[str]

### AirflowConfigurationOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EnvironmentClass
- **Type**: typing.Optional[str]

### MaxWorkers
- **Type**: typing.Optional[int]

### KmsKey
- **Type**: typing.Optional[str]

### AirflowVersion
- **Type**: typing.Optional[str]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.LoggingConfigurationInput]

### WeeklyMaintenanceWindowStart
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### WebserverAccessMode
- **Type**: typing.Optional[typing.Literal['PRIVATE_ONLY', 'PUBLIC_ONLY']]

### MinWorkers
- **Type**: typing.Optional[int]

### Schedulers
- **Type**: typing.Optional[int]

### EndpointManagement
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]

### MinWebservers
- **Type**: typing.Optional[int]

### MaxWebservers
- **Type**: typing.Optional[int]


# CreateEnvironmentOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWebLoginTokenRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWebLoginTokenResponse

### WebToken
- **Type**: <class 'str'>
- **Required**: Yes

### WebServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### IamIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### AirflowIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEnvironmentInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# Dimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# Environment

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'CREATING_SNAPSHOT', 'DELETED', 'DELETING', 'MAINTENANCE', 'PENDING', 'ROLLING_BACK', 'UNAVAILABLE', 'UPDATE_FAILED', 'UPDATING']]

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### WebserverUrl
- **Type**: typing.Optional[str]

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### ServiceRoleArn
- **Type**: typing.Optional[str]

### KmsKey
- **Type**: typing.Optional[str]

### AirflowVersion
- **Type**: typing.Optional[str]

### SourceBucketArn
- **Type**: typing.Optional[str]

### DagS3Path
- **Type**: typing.Optional[str]

### PluginsS3Path
- **Type**: typing.Optional[str]

### PluginsS3ObjectVersion
- **Type**: typing.Optional[str]

### RequirementsS3Path
- **Type**: typing.Optional[str]

### RequirementsS3ObjectVersion
- **Type**: typing.Optional[str]

### StartupScriptS3Path
- **Type**: typing.Optional[str]

### StartupScriptS3ObjectVersion
- **Type**: typing.Optional[str]

### AirflowConfigurationOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### EnvironmentClass
- **Type**: typing.Optional[str]

### MaxWorkers
- **Type**: typing.Optional[int]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.NetworkConfigurationOutput]

### LoggingConfiguration
- **Type**: <class 'NoneType'>

### LastUpdate
- **Type**: <class 'NoneType'>

### WeeklyMaintenanceWindowStart
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### WebserverAccessMode
- **Type**: typing.Optional[typing.Literal['PRIVATE_ONLY', 'PUBLIC_ONLY']]

### MinWorkers
- **Type**: typing.Optional[int]

### Schedulers
- **Type**: typing.Optional[int]

### WebserverVpcEndpointService
- **Type**: typing.Optional[str]

### DatabaseVpcEndpointService
- **Type**: typing.Optional[str]

### CeleryExecutorQueue
- **Type**: typing.Optional[str]

### EndpointManagement
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SERVICE']]

### MinWebservers
- **Type**: typing.Optional[int]

### MaxWebservers
- **Type**: typing.Optional[int]


# GetEnvironmentInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentOutput

### Environment
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.Environment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeRestApiRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### Method
- **Type**: typing.Literal['DELETE', 'GET', 'PATCH', 'POST', 'PUT']
- **Required**: Yes

### QueryParameters
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Body
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# InvokeRestApiResponse

### RestApiStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### RestApiResponse
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes


# LastUpdate

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.UpdateError]

### Source
- **Type**: typing.Optional[str]


# ListEnvironmentsInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.PaginatorConfig]


# ListEnvironmentsOutput

### Environments
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfiguration

### DagProcessingLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfiguration]

### SchedulerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfiguration]

### WebserverLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfiguration]

### WorkerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfiguration]

### TaskLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfiguration]


# LoggingConfigurationInput

### DagProcessingLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInput]

### SchedulerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInput]

### WebserverLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInput]

### WorkerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInput]

### TaskLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInput]


# MetricDatum

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.Timestamp'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mwaa_classes.Dimension]]

### Value
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### StatisticValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.StatisticSet]


# ModuleLoggingConfiguration

### Enabled
- **Type**: typing.Optional[bool]

### LogLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'WARNING']]

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]


# ModuleLoggingConfigurationInput

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes


# NetworkConfiguration

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# NetworkConfigurationOutput

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# NetworkConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishMetricsInput

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricData
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mwaa_classes.MetricDatum]
- **Required**: Yes


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


# StatisticSet

### SampleCount
- **Type**: typing.Optional[int]

### Sum
- **Type**: typing.Optional[float]

### Minimum
- **Type**: typing.Optional[float]

### Maximum
- **Type**: typing.Optional[float]


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnvironmentInput

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ExecutionRoleArn
- **Type**: typing.Optional[str]

### AirflowVersion
- **Type**: typing.Optional[str]

### SourceBucketArn
- **Type**: typing.Optional[str]

### DagS3Path
- **Type**: typing.Optional[str]

### PluginsS3Path
- **Type**: typing.Optional[str]

### PluginsS3ObjectVersion
- **Type**: typing.Optional[str]

### RequirementsS3Path
- **Type**: typing.Optional[str]

### RequirementsS3ObjectVersion
- **Type**: typing.Optional[str]

### StartupScriptS3Path
- **Type**: typing.Optional[str]

### StartupScriptS3ObjectVersion
- **Type**: typing.Optional[str]

### AirflowConfigurationOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### EnvironmentClass
- **Type**: typing.Optional[str]

### MaxWorkers
- **Type**: typing.Optional[int]

### NetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.UpdateNetworkConfigurationInput]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.LoggingConfigurationInput]

### WeeklyMaintenanceWindowStart
- **Type**: typing.Optional[str]

### WebserverAccessMode
- **Type**: typing.Optional[typing.Literal['PRIVATE_ONLY', 'PUBLIC_ONLY']]

### MinWorkers
- **Type**: typing.Optional[int]

### Schedulers
- **Type**: typing.Optional[int]

### MinWebservers
- **Type**: typing.Optional[int]

### MaxWebservers
- **Type**: typing.Optional[int]


# UpdateEnvironmentOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateError

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UpdateNetworkConfigurationInput

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


