# Kinesisanalytics Classes

# AddApplicationCloudWatchLoggingOptionRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOption
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.CloudWatchLoggingOptionTypeDef'>
- **Required**: Yes


# AddApplicationInputProcessingConfigurationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### InputProcessingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputProcessingConfigurationTypeDef'>
- **Required**: Yes


# AddApplicationInputRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputTypeDef'>
- **Required**: Yes


# AddApplicationOutputRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.OutputTypeDef'>
- **Required**: Yes


# AddApplicationReferenceDataSourceRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ReferenceDataSourceTypeDef'>
- **Required**: Yes


# ApplicationDetailTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationStatus
- **Type**: typing.Literal['DELETING', 'READY', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes

### ApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationDescription
- **Type**: typing.Optional[str]

### CreateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdateTimestamp
- **Type**: typing.Optional[datetime.datetime]

### InputDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputDescriptionTypeDef]]

### OutputDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics_classes.OutputDescriptionTypeDef]]

### ReferenceDataSourceDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics_classes.ReferenceDataSourceDescriptionTypeDef]]

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics_classes.CloudWatchLoggingOptionDescriptionTypeDef]]

### ApplicationCode
- **Type**: typing.Optional[str]


# ApplicationSummaryTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationStatus
- **Type**: typing.Literal['DELETING', 'READY', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes


# ApplicationUpdateTypeDef

### InputUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputUpdateTypeDef]]

### ApplicationCodeUpdate
- **Type**: typing.Optional[str]

### OutputUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.OutputUpdateTypeDef]]

### ReferenceDataSourceUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.ReferenceDataSourceUpdateTypeDef]]

### CloudWatchLoggingOptionUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.CloudWatchLoggingOptionUpdateTypeDef]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CSVMappingParametersTypeDef

### RecordRowDelimiter
- **Type**: <class 'str'>
- **Required**: Yes

### RecordColumnDelimiter
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLoggingOptionDescriptionTypeDef

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLoggingOptionId
- **Type**: typing.Optional[str]


# CloudWatchLoggingOptionTypeDef

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLoggingOptionUpdateTypeDef

### CloudWatchLoggingOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### LogStreamARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# CreateApplicationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationDescription
- **Type**: typing.Optional[str]

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputTypeDef]]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.OutputTypeDef]]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.CloudWatchLoggingOptionTypeDef]]

### ApplicationCode
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.TagTypeDef]]


# CreateApplicationResponseTypeDef

### ApplicationSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ApplicationSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationCloudWatchLoggingOptionRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOptionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationInputProcessingConfigurationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationOutputRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationReferenceDataSourceRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# DescribeApplicationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationResponseTypeDef

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ApplicationDetailTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationSchemaTypeDef

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# DiscoverInputSchemaRequestRequestTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### InputStartingPositionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputStartingPositionConfigurationTypeDef]

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.S3ConfigurationTypeDef]

### InputProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputProcessingConfigurationTypeDef]


# DiscoverInputSchemaResponseTypeDef

### InputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.SourceSchemaTypeDef'>
- **Required**: Yes

### ParsedInputRecords
- **Type**: typing.List[typing.List[str]]
- **Required**: Yes

### ProcessedInputRecords
- **Type**: typing.List[str]
- **Required**: Yes

### RawInputRecords
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InputConfigurationTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputStartingPositionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputStartingPositionConfigurationTypeDef'>
- **Required**: Yes


# InputDescriptionTypeDef

### InputId
- **Type**: typing.Optional[str]

### NamePrefix
- **Type**: typing.Optional[str]

### InAppStreamNames
- **Type**: typing.Optional[typing.List[str]]

### InputProcessingConfigurationDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputProcessingConfigurationDescriptionTypeDef]

### KinesisStreamsInputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisStreamsInputDescriptionTypeDef]

### KinesisFirehoseInputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisFirehoseInputDescriptionTypeDef]

### InputSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.SourceSchemaTypeDef]

### InputParallelism
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputParallelismTypeDef]

### InputStartingPositionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputStartingPositionConfigurationTypeDef]


# InputLambdaProcessorDescriptionTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# InputLambdaProcessorTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# InputLambdaProcessorUpdateTypeDef

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# InputParallelismTypeDef

### Count
- **Type**: typing.Optional[int]


# InputParallelismUpdateTypeDef

### CountUpdate
- **Type**: typing.Optional[int]


# InputProcessingConfigurationDescriptionTypeDef

### InputLambdaProcessorDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputLambdaProcessorDescriptionTypeDef]


# InputProcessingConfigurationTypeDef

### InputLambdaProcessor
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputLambdaProcessorTypeDef'>
- **Required**: Yes


# InputProcessingConfigurationUpdateTypeDef

### InputLambdaProcessorUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputLambdaProcessorUpdateTypeDef'>
- **Required**: Yes


# InputSchemaUpdateTypeDef

### RecordFormatUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.RecordFormatTypeDef]

### RecordEncodingUpdate
- **Type**: typing.Optional[str]

### RecordColumnUpdates
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.RecordColumnTypeDef]]


# InputStartingPositionConfigurationTypeDef

### InputStartingPosition
- **Type**: typing.Optional[typing.Literal['LAST_STOPPED_POINT', 'NOW', 'TRIM_HORIZON']]


# InputTypeDef

### NamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### InputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.SourceSchemaTypeDef'>
- **Required**: Yes

### InputProcessingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputProcessingConfigurationTypeDef]

### KinesisStreamsInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisStreamsInputTypeDef]

### KinesisFirehoseInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisFirehoseInputTypeDef]

### InputParallelism
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputParallelismTypeDef]


# InputUpdateTypeDef

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### NamePrefixUpdate
- **Type**: typing.Optional[str]

### InputProcessingConfigurationUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputProcessingConfigurationUpdateTypeDef]

### KinesisStreamsInputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisStreamsInputUpdateTypeDef]

### KinesisFirehoseInputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisFirehoseInputUpdateTypeDef]

### InputSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputSchemaUpdateTypeDef]

### InputParallelismUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputParallelismUpdateTypeDef]


# JSONMappingParametersTypeDef

### RecordRowPath
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInputDescriptionTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInputUpdateTypeDef

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# KinesisFirehoseOutputDescriptionTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseOutputUpdateTypeDef

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# KinesisStreamsInputDescriptionTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsInputUpdateTypeDef

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# KinesisStreamsOutputDescriptionTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsOutputUpdateTypeDef

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# LambdaOutputDescriptionTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# LambdaOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaOutputUpdateTypeDef

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# ListApplicationsRequestRequestTypeDef

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartApplicationName
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### ApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### HasMoreApplications
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MappingParametersTypeDef

### JSONMappingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.JSONMappingParametersTypeDef]

### CSVMappingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.CSVMappingParametersTypeDef]


# OutputDescriptionTypeDef

### OutputId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### KinesisStreamsOutputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisStreamsOutputDescriptionTypeDef]

### KinesisFirehoseOutputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisFirehoseOutputDescriptionTypeDef]

### LambdaOutputDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.LambdaOutputDescriptionTypeDef]

### DestinationSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.DestinationSchemaTypeDef]


# OutputTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.DestinationSchemaTypeDef'>
- **Required**: Yes

### KinesisStreamsOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisStreamsOutputTypeDef]

### KinesisFirehoseOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisFirehoseOutputTypeDef]

### LambdaOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.LambdaOutputTypeDef]


# OutputUpdateTypeDef

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes

### NameUpdate
- **Type**: typing.Optional[str]

### KinesisStreamsOutputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisStreamsOutputUpdateTypeDef]

### KinesisFirehoseOutputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.KinesisFirehoseOutputUpdateTypeDef]

### LambdaOutputUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.LambdaOutputUpdateTypeDef]

### DestinationSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.DestinationSchemaTypeDef]


# RecordColumnTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SqlType
- **Type**: <class 'str'>
- **Required**: Yes

### Mapping
- **Type**: typing.Optional[str]


# RecordFormatTypeDef

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### MappingParameters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.MappingParametersTypeDef]


# ReferenceDataSourceDescriptionTypeDef

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### S3ReferenceDataSourceDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.S3ReferenceDataSourceDescriptionTypeDef'>
- **Required**: Yes

### ReferenceSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.SourceSchemaTypeDef]


# ReferenceDataSourceTypeDef

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.SourceSchemaTypeDef'>
- **Required**: Yes

### S3ReferenceDataSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.S3ReferenceDataSourceTypeDef]


# ReferenceDataSourceUpdateTypeDef

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableNameUpdate
- **Type**: typing.Optional[str]

### S3ReferenceDataSourceUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.S3ReferenceDataSourceUpdateTypeDef]

### ReferenceSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics_classes.SourceSchemaTypeDef]


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


# S3ConfigurationTypeDef

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes


# S3ReferenceDataSourceDescriptionTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceRoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# S3ReferenceDataSourceTypeDef

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceRoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# S3ReferenceDataSourceUpdateTypeDef

### BucketARNUpdate
- **Type**: typing.Optional[str]

### FileKeyUpdate
- **Type**: typing.Optional[str]

### ReferenceRoleARNUpdate
- **Type**: typing.Optional[str]


# SourceSchemaTypeDef

### RecordFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.RecordFormatTypeDef'>
- **Required**: Yes

### RecordColumns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.RecordColumnTypeDef]
- **Required**: Yes

### RecordEncoding
- **Type**: typing.Optional[str]


# StartApplicationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.InputConfigurationTypeDef]
- **Required**: Yes


# StopApplicationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisanalytics_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics_classes.ApplicationUpdateTypeDef'>
- **Required**: Yes


