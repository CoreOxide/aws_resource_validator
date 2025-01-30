# mwaa_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateCliTokenRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateCliTokenResponseTypeDef

### CliToken
- **Type**: <class 'str'>
- **Required**: Yes

### WebServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateEnvironmentInputRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.NetworkConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.LoggingConfigurationInputTypeDef]

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


# CreateEnvironmentOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWebLoginTokenRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWebLoginTokenResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEnvironmentInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# EnvironmentTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.NetworkConfigurationOutputTypeDef]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.LoggingConfigurationTypeDef]

### LastUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.LastUpdateTypeDef]

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


# GetEnvironmentInputRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentOutputTypeDef

### Environment
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.EnvironmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LastUpdateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCESS']]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### Error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.UpdateErrorTypeDef]

### Source
- **Type**: typing.Optional[str]


# ListEnvironmentsInputListEnvironmentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.PaginatorConfigTypeDef]


# ListEnvironmentsInputRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEnvironmentsOutputTypeDef

### Environments
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigurationInputTypeDef

### DagProcessingLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInputTypeDef]

### SchedulerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInputTypeDef]

### WebserverLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInputTypeDef]

### WorkerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInputTypeDef]

### TaskLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationInputTypeDef]


# LoggingConfigurationTypeDef

### DagProcessingLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationTypeDef]

### SchedulerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationTypeDef]

### WebserverLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationTypeDef]

### WorkerLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationTypeDef]

### TaskLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.ModuleLoggingConfigurationTypeDef]


# MetricDatumTypeDef

### MetricName
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mwaa_classes.DimensionTypeDef]]

### Value
- **Type**: typing.Optional[float]

### Unit
- **Type**: typing.Optional[typing.Literal['Bits', 'Bits/Second', 'Bytes', 'Bytes/Second', 'Count', 'Count/Second', 'Gigabits', 'Gigabits/Second', 'Gigabytes', 'Gigabytes/Second', 'Kilobits', 'Kilobits/Second', 'Kilobytes', 'Kilobytes/Second', 'Megabits', 'Megabits/Second', 'Megabytes', 'Megabytes/Second', 'Microseconds', 'Milliseconds', 'None', 'Percent', 'Seconds', 'Terabits', 'Terabits/Second', 'Terabytes', 'Terabytes/Second']]

### StatisticValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.StatisticSetTypeDef]


# ModuleLoggingConfigurationInputTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### LogLevel
- **Type**: typing.Literal['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'WARNING']
- **Required**: Yes


# ModuleLoggingConfigurationTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### LogLevel
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'WARNING']]

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]


# NetworkConfigurationOutputTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]


# NetworkConfigurationTypeDef

### SubnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishMetricsInputRequestTypeDef

### EnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### MetricData
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mwaa_classes.MetricDatumTypeDef]
- **Required**: Yes


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


# StatisticSetTypeDef

### SampleCount
- **Type**: typing.Optional[int]

### Sum
- **Type**: typing.Optional[float]

### Minimum
- **Type**: typing.Optional[float]

### Maximum
- **Type**: typing.Optional[float]


# TagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateEnvironmentInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.UpdateNetworkConfigurationInputTypeDef]

### LoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mwaa_classes.LoggingConfigurationInputTypeDef]

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


# UpdateEnvironmentOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mwaa_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateErrorTypeDef

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# UpdateNetworkConfigurationInputTypeDef

### SecurityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


