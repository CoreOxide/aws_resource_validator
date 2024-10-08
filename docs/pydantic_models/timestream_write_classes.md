# Pydantic Models in timestream_write_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchLoadProgressReportTypeDef

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


# BatchLoadTaskDescriptionTypeDef

### TaskId
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### DataSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.DataSourceConfigurationTypeDef]

### ProgressReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.BatchLoadProgressReportTypeDef]

### ReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.ReportConfigurationTypeDef]

### DataModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.DataModelConfigurationTypeDef]

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


# BatchLoadTaskTypeDef

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


# CreateBatchLoadTaskRequestRequestTypeDef

### DataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.DataSourceConfigurationTypeDef'>
- **Required**: Yes

### ReportConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ReportConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.DataModelConfigurationTypeDef]

### RecordVersion
- **Type**: typing.Optional[int]


# CreateBatchLoadTaskResponseTypeDef

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDatabaseRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.TagTypeDef]]


# CreateDatabaseResponseTypeDef

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.DatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTableRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.RetentionPropertiesTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.TagTypeDef]]

### MagneticStoreWriteProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.MagneticStoreWritePropertiesTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.SchemaTypeDef]


# CreateTableResponseTypeDef

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.TableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CsvConfigurationTypeDef

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


# DataModelConfigurationTypeDef

### DataModel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.DataModelTypeDef]

### DataModelS3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.DataModelS3ConfigurationTypeDef]


# DataModelS3ConfigurationTypeDef

### BucketName
- **Type**: typing.Optional[str]

### ObjectKey
- **Type**: typing.Optional[str]


# DataModelTypeDef

### DimensionMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.DimensionMappingTypeDef]
- **Required**: Yes

### TimeColumn
- **Type**: typing.Optional[str]

### TimeUnit
- **Type**: typing.Optional[typing.Literal['MICROSECONDS', 'MILLISECONDS', 'NANOSECONDS', 'SECONDS']]

### MultiMeasureMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.MultiMeasureMappingsTypeDef]

### MixedMeasureMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.MixedMeasureMappingTypeDef]]

### MeasureNameColumn
- **Type**: typing.Optional[str]


# DataSourceConfigurationTypeDef

### DataSourceS3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.DataSourceS3ConfigurationTypeDef'>
- **Required**: Yes

### DataFormat
- **Type**: typing.Literal['CSV']
- **Required**: Yes

### CsvConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.CsvConfigurationTypeDef]


# DataSourceS3ConfigurationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]


# DatabaseTypeDef

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


# DeleteDatabaseRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTableRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchLoadTaskRequestRequestTypeDef

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBatchLoadTaskResponseTypeDef

### BatchLoadTaskDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.BatchLoadTaskDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDatabaseRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDatabaseResponseTypeDef

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.DatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointsResponseTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write_classes.EndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTableRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTableResponseTypeDef

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.TableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DimensionMappingTypeDef

### SourceColumn
- **Type**: typing.Optional[str]

### DestinationColumn
- **Type**: typing.Optional[str]


# DimensionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueType
- **Type**: typing.Optional[typing.Literal['VARCHAR']]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointTypeDef

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CachePeriodInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ListBatchLoadTasksRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### TaskStatus
- **Type**: typing.Optional[typing.Literal['CREATED', 'FAILED', 'IN_PROGRESS', 'PENDING_RESUME', 'PROGRESS_STOPPED', 'SUCCEEDED']]


# ListBatchLoadTasksResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### BatchLoadTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write_classes.BatchLoadTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDatabasesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListDatabasesResponseTypeDef

### Databases
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write_classes.DatabaseTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTablesRequestRequestTypeDef

### DatabaseName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTablesResponseTypeDef

### Tables
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write_classes.TableTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_write_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MagneticStoreRejectedDataLocationTypeDef

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.S3ConfigurationTypeDef]


# MagneticStoreWritePropertiesTypeDef

### EnableMagneticStoreWrites
- **Type**: <class 'bool'>
- **Required**: Yes

### MagneticStoreRejectedDataLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.MagneticStoreRejectedDataLocationTypeDef]


# MeasureValueTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'MULTI', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes


# MixedMeasureMappingTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.MultiMeasureAttributeMappingTypeDef]]


# MultiMeasureAttributeMappingTypeDef

### SourceColumn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetMultiMeasureAttributeName
- **Type**: typing.Optional[str]

### MeasureValueType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']]


# MultiMeasureMappingsTypeDef

### MultiMeasureAttributeMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.MultiMeasureAttributeMappingTypeDef]
- **Required**: Yes

### TargetMultiMeasureName
- **Type**: typing.Optional[str]


# PartitionKeyTypeDef

### Type
- **Type**: typing.Literal['DIMENSION', 'MEASURE']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### EnforcementInRecord
- **Type**: typing.Optional[typing.Literal['OPTIONAL', 'REQUIRED']]


# RecordTypeDef

### Dimensions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.DimensionTypeDef]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.MeasureValueTypeDef]]


# RecordsIngestedTypeDef

### Total
- **Type**: typing.Optional[int]

### MemoryStore
- **Type**: typing.Optional[int]

### MagneticStore
- **Type**: typing.Optional[int]


# ReportConfigurationTypeDef

### ReportS3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.ReportS3ConfigurationTypeDef]


# ReportS3ConfigurationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]

### KmsKeyId
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


# ResumeBatchLoadTaskRequestRequestTypeDef

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# RetentionPropertiesTypeDef

### MemoryStoreRetentionPeriodInHours
- **Type**: <class 'int'>
- **Required**: Yes

### MagneticStoreRetentionPeriodInDays
- **Type**: <class 'int'>
- **Required**: Yes


# S3ConfigurationTypeDef

### BucketName
- **Type**: typing.Optional[str]

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]

### KmsKeyId
- **Type**: typing.Optional[str]


# SchemaTypeDef

### CompositePartitionKey
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.PartitionKeyTypeDef]]


# TableTypeDef

### Arn
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### DatabaseName
- **Type**: typing.Optional[str]

### TableStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'RESTORING']]

### RetentionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.RetentionPropertiesTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### MagneticStoreWriteProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.MagneticStoreWritePropertiesTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.SchemaTypeDef]


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDatabaseRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateDatabaseResponseTypeDef

### Database
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.DatabaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTableRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.RetentionPropertiesTypeDef]

### MagneticStoreWriteProperties
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.MagneticStoreWritePropertiesTypeDef]

### Schema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.SchemaTypeDef]


# UpdateTableResponseTypeDef

### Table
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.TableTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WriteRecordsRequestRequestTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### Records
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.timestream_write_classes.RecordTypeDef]
- **Required**: Yes

### CommonAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_write_classes.RecordTypeDef]


# WriteRecordsResponseTypeDef

### RecordsIngested
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.RecordsIngestedTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_write_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


