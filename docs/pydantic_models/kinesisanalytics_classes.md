# Kinesisanalytics Classes

# AddApplicationCloudWatchLoggingOptionRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOption
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.CloudWatchLoggingOption'>
- **Required**: Yes


# AddApplicationInputProcessingConfigurationRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.InputProcessingConfiguration'>
- **Required**: Yes


# AddApplicationInputRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Input
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.Input'>
- **Required**: Yes


# AddApplicationOutputRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### Output
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.Output'>
- **Required**: Yes


# AddApplicationReferenceDataSourceRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceDataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ReferenceDataSource'>
- **Required**: Yes


# ApplicationDetail

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.InputDescription]]

### OutputDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.OutputDescription]]

### ReferenceDataSourceDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ReferenceDataSourceDescription]]

### CloudWatchLoggingOptionDescriptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.CloudWatchLoggingOptionDescription]]

### ApplicationCode
- **Type**: typing.Optional[str]


# ApplicationSummary

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationStatus
- **Type**: typing.Literal['DELETING', 'READY', 'RUNNING', 'STARTING', 'STOPPING', 'UPDATING']
- **Required**: Yes


# ApplicationUpdate

### InputUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.InputUpdate]]

### ApplicationCodeUpdate
- **Type**: typing.Optional[str]

### OutputUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.OutputUpdate]]

### ReferenceDataSourceUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ReferenceDataSourceUpdate]]

### CloudWatchLoggingOptionUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.CloudWatchLoggingOptionUpdate]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CSVMappingParameters

### RecordRowDelimiter
- **Type**: <class 'str'>
- **Required**: Yes

### RecordColumnDelimiter
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLoggingOption

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLoggingOptionDescription

### LogStreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLoggingOptionId
- **Type**: typing.Optional[str]


# CloudWatchLoggingOptionUpdate

### CloudWatchLoggingOptionId
- **Type**: <class 'str'>
- **Required**: Yes

### LogStreamARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# CreateApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationDescription
- **Type**: typing.Optional[str]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.Input]]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.Output]]

### CloudWatchLoggingOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.CloudWatchLoggingOption]]

### ApplicationCode
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.Tag]]


# CreateApplicationResponse

### ApplicationSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ApplicationSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationCloudWatchLoggingOptionRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### CloudWatchLoggingOptionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationInputProcessingConfigurationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### InputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationOutputRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationReferenceDataSourceRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# DescribeApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationResponse

### ApplicationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ApplicationDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationSchema

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes


# DiscoverInputSchemaRequest

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]

### InputStartingPositionConfiguration
- **Type**: <class 'NoneType'>

### S3Configuration
- **Type**: <class 'NoneType'>

### InputProcessingConfiguration
- **Type**: <class 'NoneType'>


# DiscoverInputSchemaResponse

### InputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchemaOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# Input

### NamePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### InputSchema
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchema, aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchemaOutput]
- **Required**: Yes

### InputProcessingConfiguration
- **Type**: <class 'NoneType'>

### KinesisStreamsInput
- **Type**: <class 'NoneType'>

### KinesisFirehoseInput
- **Type**: <class 'NoneType'>

### InputParallelism
- **Type**: <class 'NoneType'>


# InputConfiguration

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### InputStartingPositionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.InputStartingPositionConfiguration'>
- **Required**: Yes


# InputDescription

### InputId
- **Type**: typing.Optional[str]

### NamePrefix
- **Type**: typing.Optional[str]

### InAppStreamNames
- **Type**: typing.Optional[typing.List[str]]

### InputProcessingConfigurationDescription
- **Type**: <class 'NoneType'>

### KinesisStreamsInputDescription
- **Type**: <class 'NoneType'>

### KinesisFirehoseInputDescription
- **Type**: <class 'NoneType'>

### InputSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchemaOutput]

### InputParallelism
- **Type**: <class 'NoneType'>

### InputStartingPositionConfiguration
- **Type**: <class 'NoneType'>


# InputLambdaProcessor

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# InputLambdaProcessorDescription

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# InputLambdaProcessorUpdate

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# InputParallelism

### Count
- **Type**: typing.Optional[int]


# InputParallelismUpdate

### CountUpdate
- **Type**: typing.Optional[int]


# InputProcessingConfiguration

### InputLambdaProcessor
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.InputLambdaProcessor'>
- **Required**: Yes


# InputProcessingConfigurationDescription

### InputLambdaProcessorDescription
- **Type**: <class 'NoneType'>


# InputProcessingConfigurationUpdate

### InputLambdaProcessorUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.InputLambdaProcessorUpdate'>
- **Required**: Yes


# InputSchemaUpdate

### RecordFormatUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.RecordFormat]

### RecordEncodingUpdate
- **Type**: typing.Optional[str]

### RecordColumnUpdates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.RecordColumn]]


# InputStartingPositionConfiguration

### InputStartingPosition
- **Type**: typing.Optional[typing.Literal['LAST_STOPPED_POINT', 'NOW', 'TRIM_HORIZON']]


# InputUpdate

### InputId
- **Type**: <class 'str'>
- **Required**: Yes

### NamePrefixUpdate
- **Type**: typing.Optional[str]

### InputProcessingConfigurationUpdate
- **Type**: <class 'NoneType'>

### KinesisStreamsInputUpdate
- **Type**: <class 'NoneType'>

### KinesisFirehoseInputUpdate
- **Type**: <class 'NoneType'>

### InputSchemaUpdate
- **Type**: <class 'NoneType'>

### InputParallelismUpdate
- **Type**: <class 'NoneType'>


# JSONMappingParameters

### RecordRowPath
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseInputDescription

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseInputUpdate

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# KinesisFirehoseOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisFirehoseOutputDescription

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisFirehoseOutputUpdate

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# KinesisStreamsInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsInputDescription

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsInputUpdate

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# KinesisStreamsOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# KinesisStreamsOutputDescription

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# KinesisStreamsOutputUpdate

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# LambdaOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# LambdaOutputDescription

### ResourceARN
- **Type**: typing.Optional[str]

### RoleARN
- **Type**: typing.Optional[str]


# LambdaOutputUpdate

### ResourceARNUpdate
- **Type**: typing.Optional[str]

### RoleARNUpdate
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### Limit
- **Type**: typing.Optional[int]

### ExclusiveStartApplicationName
- **Type**: typing.Optional[str]


# ListApplicationsResponse

### ApplicationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ApplicationSummary]
- **Required**: Yes

### HasMoreApplications
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ResponseMetadata'>
- **Required**: Yes


# MappingParameters

### JSONMappingParameters
- **Type**: <class 'NoneType'>

### CSVMappingParameters
- **Type**: <class 'NoneType'>


# Output

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.DestinationSchema'>
- **Required**: Yes

### KinesisStreamsOutput
- **Type**: <class 'NoneType'>

### KinesisFirehoseOutput
- **Type**: <class 'NoneType'>

### LambdaOutput
- **Type**: <class 'NoneType'>


# OutputDescription

### OutputId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### KinesisStreamsOutputDescription
- **Type**: <class 'NoneType'>

### KinesisFirehoseOutputDescription
- **Type**: <class 'NoneType'>

### LambdaOutputDescription
- **Type**: <class 'NoneType'>

### DestinationSchema
- **Type**: <class 'NoneType'>


# OutputUpdate

### OutputId
- **Type**: <class 'str'>
- **Required**: Yes

### NameUpdate
- **Type**: typing.Optional[str]

### KinesisStreamsOutputUpdate
- **Type**: <class 'NoneType'>

### KinesisFirehoseOutputUpdate
- **Type**: <class 'NoneType'>

### LambdaOutputUpdate
- **Type**: <class 'NoneType'>

### DestinationSchemaUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.DestinationSchema]


# RecordColumn

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SqlType
- **Type**: <class 'str'>
- **Required**: Yes

### Mapping
- **Type**: typing.Optional[str]


# RecordFormat

### RecordFormatType
- **Type**: typing.Literal['CSV', 'JSON']
- **Required**: Yes

### MappingParameters
- **Type**: <class 'NoneType'>


# ReferenceDataSource

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceSchema
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchema, aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchemaOutput]
- **Required**: Yes

### S3ReferenceDataSource
- **Type**: <class 'NoneType'>


# ReferenceDataSourceDescription

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### S3ReferenceDataSourceDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.S3ReferenceDataSourceDescription'>
- **Required**: Yes

### ReferenceSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchemaOutput]


# ReferenceDataSourceUpdate

### ReferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### TableNameUpdate
- **Type**: typing.Optional[str]

### S3ReferenceDataSourceUpdate
- **Type**: <class 'NoneType'>

### ReferenceSchemaUpdate
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchema, aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.SourceSchemaOutput, NoneType]


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


# S3Configuration

### RoleARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes


# S3ReferenceDataSource

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceRoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# S3ReferenceDataSourceDescription

### BucketARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileKey
- **Type**: <class 'str'>
- **Required**: Yes

### ReferenceRoleARN
- **Type**: <class 'str'>
- **Required**: Yes


# S3ReferenceDataSourceUpdate

### BucketARNUpdate
- **Type**: typing.Optional[str]

### FileKeyUpdate
- **Type**: typing.Optional[str]

### ReferenceRoleARNUpdate
- **Type**: typing.Optional[str]


# SourceSchema

### RecordFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.RecordFormat'>
- **Required**: Yes

### RecordColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.RecordColumn]
- **Required**: Yes

### RecordEncoding
- **Type**: typing.Optional[str]


# SourceSchemaOutput

### RecordFormat
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.RecordFormat'>
- **Required**: Yes

### RecordColumns
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.RecordColumn]
- **Required**: Yes

### RecordEncoding
- **Type**: typing.Optional[str]


# StartApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### InputConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.InputConfiguration]
- **Required**: Yes


# StopApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationRequest

### ApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentApplicationVersionId
- **Type**: <class 'int'>
- **Required**: Yes

### ApplicationUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisanalytics.kinesisanalytics_classes.ApplicationUpdate'>
- **Required**: Yes


