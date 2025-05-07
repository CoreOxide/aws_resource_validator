# Timestream Write Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchLoadProgressReport

### RecordsProcessed
- **Type**: typing.Optional[int]

### RecordsIngested
- **Type**: typing.Optional[int]

### ParseFailures
- **Type**: typing.Optional[int]

### RecordIngestionFailures
- **Type**: typing.Optional[int]

### FileFailures
- **Type**: typing.Optional[int]

### BytesMetered
- **Type**: typing.Optional[int]


# BatchLoadTask

### TaskId
- **Type**: typing.Optional[str]

### TaskStatus
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'PENDING_RESUME', 'PROGRESS_STOPPED', 'SUCCEEDED']]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ResumableUntil
- **Type**: typing.Optional[datetime.datetime]


# BatchLoadTaskDescription

### TaskId
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### DataSourceConfiguration
- **Type**: <class 'NoneType'>

### ProgressReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.BatchLoadProgressReport]

### ReportConfiguration
- **Type**: <class 'NoneType'>

### DataModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DataModelConfigurationOutput]

### TargetDatabaseName
- **Type**: typing.Optional[str]

### TargetTableName
- **Type**: typing.Optional[str]

### TaskStatus
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'PENDING_RESUME', 'PROGRESS_STOPPED', 'SUCCEEDED']]

### RecordVersion
- **Type**: typing.Optional[int]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ResumableUntil
- **Type**: typing.Optional[datetime.datetime]


# CreateBatchLoadTaskRequest

### DataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DataSourceConfiguration'>
- **Required**: Yes

### ReportConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ReportConfiguration'>
- **Required**: Yes

### TargetDatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetTableName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### DataModelConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DataModelConfiguration, aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DataModelConfigurationOutput, NoneType]

### RecordVersion
- **Type**: typing.Optional[int]


# CreateBatchLoadTaskResponse

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDatabaseRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Tag]]


# CreateDatabaseResponse

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Database'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionProperties
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Tag]]

### MagneticStoreWriteProperties
- **Type**: <class 'NoneType'>

### Schema
- **Type**: typing.Union[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Schema, aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.SchemaOutput, NoneType]


# CreateTableResponse

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Table'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# CsvConfiguration

### ColumnSeparator
- **Type**: typing.Optional[str]

### EscapeChar
- **Type**: typing.Optional[str]

### QuoteChar
- **Type**: typing.Optional[str]

### NullValue
- **Type**: typing.Optional[str]

### TrimWhiteSpace
- **Type**: typing.Optional[bool]


# DataModel

### DimensionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DimensionMapping]
- **Required**: Yes

### TimeColumn
- **Type**: typing.Optional[str]

### TimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### MultiMeasureMappings
- **Type**: <class 'NoneType'>

### MixedMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.MixedMeasureMapping]]

### MeasureNameColumn
- **Type**: typing.Optional[str]


# DataModelConfiguration

### DataModel
- **Type**: <class 'NoneType'>

### DataModelS3Configuration
- **Type**: <class 'NoneType'>


# DataModelConfigurationOutput

### DataModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DataModelOutput]

### DataModelS3Configuration
- **Type**: <class 'NoneType'>


# DataModelOutput

### DimensionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DimensionMapping]
- **Required**: Yes

### TimeColumn
- **Type**: typing.Optional[str]

### TimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### MultiMeasureMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.MultiMeasureMappingsOutput]

### MixedMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.MixedMeasureMappingOutput]]

### MeasureNameColumn
- **Type**: typing.Optional[str]


# DataModelS3Configuration

### BucketName
- **Type**: typing.Optional[str]

### ObjectKey
- **Type**: typing.Optional[str]


# DataSourceConfiguration

### DataSourceS3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.DataSourceS3Configuration'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['CSV']
- **Required**: Yes

### CsvConfiguration
- **Type**: <class 'NoneType'>


# DataSourceS3Configuration

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]


# Database

### Arn
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableCount
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteDatabaseRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchLoadTaskRequest

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchLoadTaskResponse

### BatchLoadTaskDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.BatchLoadTaskDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDatabaseRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatabaseResponse

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Database'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointsResponse

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTableResponse

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Table'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# Dimension

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueType
- **Type**: typing.Optional[typing.Literal['VARCHAR']]


# DimensionMapping

### SourceColumn
- **Type**: typing.Optional[str]

### DestinationColumn
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CachePeriodInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ListBatchLoadTasksRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### TaskStatus
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'PENDING_RESUME', 'PROGRESS_STOPPED', 'SUCCEEDED']]


# ListBatchLoadTasksResponse

### BatchLoadTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.BatchLoadTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDatabasesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatabasesResponse

### Databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Database]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTablesRequest

### DatabaseName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTablesResponse

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Table]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# MagneticStoreRejectedDataLocation

### S3Configuration
- **Type**: <class 'NoneType'>


# MagneticStoreWriteProperties

### EnableMagneticStoreWrites
- **Type**: <class 'bool'>
- **Required**: Yes

### MagneticStoreRejectedDataLocation
- **Type**: <class 'NoneType'>


# MeasureValue

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'MULTI', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes


# MixedMeasureMapping

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'MULTI', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### MeasureName
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[str]

### TargetMeasureName
- **Type**: typing.Optional[str]

### MultiMeasureAttributeMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.MultiMeasureAttributeMapping]]


# MixedMeasureMappingOutput

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'MULTI', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### MeasureName
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[str]

### TargetMeasureName
- **Type**: typing.Optional[str]

### MultiMeasureAttributeMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.MultiMeasureAttributeMapping]]


# MultiMeasureAttributeMapping

### SourceColumn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetMultiMeasureAttributeName
- **Type**: typing.Optional[str]

### MeasureValueType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']]


# MultiMeasureMappings

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.MultiMeasureAttributeMapping]
- **Required**: Yes

### TargetMultiMeasureName
- **Type**: typing.Optional[str]


# MultiMeasureMappingsOutput

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.MultiMeasureAttributeMapping]
- **Required**: Yes

### TargetMultiMeasureName
- **Type**: typing.Optional[str]


# PartitionKey

### Type
- **Type**: typing.Literal['DIMENSION', 'MEASURE']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### EnforcementInRecord
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRED']]


# Record

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Dimension]]

### MeasureName
- **Type**: typing.Optional[str]

### MeasureValue
- **Type**: typing.Optional[str]

### MeasureValueType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'MULTI', 'TIMESTAMP', 'VARCHAR']]

### Time
- **Type**: typing.Optional[str]

### TimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### Version
- **Type**: typing.Optional[int]

### MeasureValues
- **Type**: typing.Optional[typing.List[NoneType]]


# RecordsIngested

### Total
- **Type**: typing.Optional[int]

### MemoryStore
- **Type**: typing.Optional[int]

### MagneticStore
- **Type**: typing.Optional[int]


# ReportConfiguration

### ReportS3Configuration
- **Type**: <class 'NoneType'>


# ReportS3Configuration

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]

### KmsKeyId
- **Type**: typing.Optional[str]


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


# ResumeBatchLoadTaskRequest

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# RetentionProperties

### MemoryStoreRetentionPeriodInHours
- **Type**: <class 'int'>
- **Required**: Yes

### MagneticStoreRetentionPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes


# S3Configuration

### BucketName
- **Type**: typing.Optional[str]

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]

### KmsKeyId
- **Type**: typing.Optional[str]


# Schema

### CompositePartitionKey
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.PartitionKey]]


# SchemaOutput

### CompositePartitionKey
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.PartitionKey]]


# Table

### Arn
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'RESTORING']]

### RetentionProperties
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### MagneticStoreWriteProperties
- **Type**: <class 'NoneType'>

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.SchemaOutput]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDatabaseRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDatabaseResponse

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Database'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTableRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionProperties
- **Type**: <class 'NoneType'>

### MagneticStoreWriteProperties
- **Type**: <class 'NoneType'>

### Schema
- **Type**: typing.Union[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Schema, aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.SchemaOutput, NoneType]


# UpdateTableResponse

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Table'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


# WriteRecordsRequest

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Record]
- **Required**: Yes

### CommonAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.Record]


# WriteRecordsResponse

### RecordsIngested
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.RecordsIngested'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write.timestream_write_classes.ResponseMetadata'>
- **Required**: Yes


