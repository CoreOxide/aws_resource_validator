# Timestream Query Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelQueryRequestRequestTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelQueryResponseTypeDef

### CancellationMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ColumnInfoTypeDef

### Type
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.TypeTypeDef'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# CreateScheduledQueryRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### NotificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### ScheduledQueryExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorReportConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ErrorReportConfigurationTypeDef'>
- **Required**: Yes

### TargetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.TargetConfigurationTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_query_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]


# CreateScheduledQueryResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DatumTypeDef

### ScalarValue
- **Type**: typing.Optional[str]

### TimeSeriesValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### ArrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### RowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### NullValue
- **Type**: typing.Optional[bool]


# DeleteScheduledQueryRequestRequestTypeDef

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountSettingsResponseTypeDef

### MaxQueryTCU
- **Type**: <class 'int'>
- **Required**: Yes

### QueryPricingModel
- **Type**: typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEndpointsResponseTypeDef

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.EndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeScheduledQueryRequestRequestTypeDef

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduledQueryResponseTypeDef

### ScheduledQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ScheduledQueryDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DimensionMappingTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueType
- **Type**: typing.Literal['VARCHAR']
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointTypeDef

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CachePeriodInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ErrorReportConfigurationTypeDef

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.S3ConfigurationTypeDef'>
- **Required**: Yes


# ErrorReportLocationTypeDef

### S3ReportLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.S3ReportLocationTypeDef]


# ExecuteScheduledQueryRequestRequestTypeDef

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# ExecutionStatsTypeDef

### ExecutionTimeInMillis
- **Type**: typing.Optional[int]

### DataWrites
- **Type**: typing.Optional[int]

### BytesMetered
- **Type**: typing.Optional[int]

### CumulativeBytesScanned
- **Type**: typing.Optional[int]

### RecordsIngested
- **Type**: typing.Optional[int]

### QueryResultRows
- **Type**: typing.Optional[int]


# ListScheduledQueriesRequestListScheduledQueriesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.PaginatorConfigTypeDef]


# ListScheduledQueriesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScheduledQueriesResponseTypeDef

### ScheduledQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.ScheduledQueryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MixedMeasureMappingOutputTypeDef

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'MULTI', 'VARCHAR']
- **Required**: Yes

### MeasureName
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[str]

### TargetMeasureName
- **Type**: typing.Optional[str]

### MultiMeasureAttributeMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.MultiMeasureAttributeMappingTypeDef]]


# MixedMeasureMappingTypeDef

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'MULTI', 'VARCHAR']
- **Required**: Yes

### MeasureName
- **Type**: typing.Optional[str]

### SourceColumn
- **Type**: typing.Optional[str]

### TargetMeasureName
- **Type**: typing.Optional[str]

### MultiMeasureAttributeMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_query_classes.MultiMeasureAttributeMappingTypeDef]]


# MultiMeasureAttributeMappingTypeDef

### SourceColumn
- **Type**: <class 'str'>
- **Required**: Yes

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### TargetMultiMeasureAttributeName
- **Type**: typing.Optional[str]


# MultiMeasureMappingsOutputTypeDef

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.MultiMeasureAttributeMappingTypeDef]
- **Required**: Yes

### TargetMultiMeasureName
- **Type**: typing.Optional[str]


# MultiMeasureMappingsTypeDef

### MultiMeasureAttributeMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.timestream_query_classes.MultiMeasureAttributeMappingTypeDef]
- **Required**: Yes

### TargetMultiMeasureName
- **Type**: typing.Optional[str]


# NotificationConfigurationTypeDef

### SnsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.SnsConfigurationTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterMappingTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.TypeTypeDef'>
- **Required**: Yes


# PrepareQueryRequestRequestTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ValidateOnly
- **Type**: typing.Optional[bool]


# PrepareQueryResponseTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.SelectColumnTypeDef]
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.ParameterMappingTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryRequestQueryPaginateTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.PaginatorConfigTypeDef]


# QueryRequestRequestTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxRows
- **Type**: typing.Optional[int]


# QueryResponseTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.RowTypeDef]
- **Required**: Yes

### ColumnInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.ColumnInfoTypeDef]
- **Required**: Yes

### QueryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.QueryStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# QueryStatusTypeDef

### ProgressPercentage
- **Type**: typing.Optional[float]

### CumulativeBytesScanned
- **Type**: typing.Optional[int]

### CumulativeBytesMetered
- **Type**: typing.Optional[int]


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


# RowTypeDef

### Data
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.DatumTypeDef]
- **Required**: Yes


# S3ConfigurationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]


# S3ReportLocationTypeDef

### BucketName
- **Type**: typing.Optional[str]

### ObjectKey
- **Type**: typing.Optional[str]


# ScheduleConfigurationTypeDef

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes


# ScheduledQueryDescriptionTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### NotificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### PreviousInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### NextInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### TargetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.TargetConfigurationOutputTypeDef]

### ScheduledQueryExecutionRoleArn
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### ErrorReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ErrorReportConfigurationTypeDef]

### LastRunSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ScheduledQueryRunSummaryTypeDef]

### RecentlyFailedRuns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.ScheduledQueryRunSummaryTypeDef]]


# ScheduledQueryRunSummaryTypeDef

### InvocationTime
- **Type**: typing.Optional[datetime.datetime]

### TriggerTime
- **Type**: typing.Optional[datetime.datetime]

### RunStatus
- **Type**: typing.Optional[typing.Literal['AUTO_TRIGGER_FAILURE', 'AUTO_TRIGGER_SUCCESS', 'MANUAL_TRIGGER_FAILURE', 'MANUAL_TRIGGER_SUCCESS']]

### ExecutionStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ExecutionStatsTypeDef]

### ErrorReportLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ErrorReportLocationTypeDef]

### FailureReason
- **Type**: typing.Optional[str]


# ScheduledQueryTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### PreviousInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### NextInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### ErrorReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ErrorReportConfigurationTypeDef]

### TargetDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.TargetDestinationTypeDef]

### LastRunStatus
- **Type**: typing.Optional[typing.Literal['AUTO_TRIGGER_FAILURE', 'AUTO_TRIGGER_SUCCESS', 'MANUAL_TRIGGER_FAILURE', 'MANUAL_TRIGGER_SUCCESS']]


# SelectColumnTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.TypeTypeDef]

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Aliased
- **Type**: typing.Optional[bool]


# SnsConfigurationTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.timestream_query_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetConfigurationOutputTypeDef

### TimestreamConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.TimestreamConfigurationOutputTypeDef'>
- **Required**: Yes


# TargetConfigurationTypeDef

### TimestreamConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.TimestreamConfigurationTypeDef'>
- **Required**: Yes


# TargetDestinationTypeDef

### TimestreamDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.TimestreamDestinationTypeDef]


# TimeSeriesDataPointTypeDef

### Time
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: ForwardRef('DatumTypeDef')
- **Required**: Yes


# TimestreamConfigurationOutputTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeColumn
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.DimensionMappingTypeDef]
- **Required**: Yes

### MultiMeasureMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.MultiMeasureMappingsOutputTypeDef]

### MixedMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.MixedMeasureMappingOutputTypeDef]]

### MeasureNameColumn
- **Type**: typing.Optional[str]


# TimestreamConfigurationTypeDef

### DatabaseName
- **Type**: <class 'str'>
- **Required**: Yes

### TableName
- **Type**: <class 'str'>
- **Required**: Yes

### TimeColumn
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionMappings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.timestream_query_classes.DimensionMappingTypeDef]
- **Required**: Yes

### MultiMeasureMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.MultiMeasureMappingsTypeDef]

### MixedMeasureMappings
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.timestream_query_classes.MixedMeasureMappingTypeDef]]

### MeasureNameColumn
- **Type**: typing.Optional[str]


# TimestreamDestinationTypeDef

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]


# TypeTypeDef

### ScalarType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DATE', 'DOUBLE', 'INTEGER', 'INTERVAL_DAY_TO_SECOND', 'INTERVAL_YEAR_TO_MONTH', 'TIME', 'TIMESTAMP', 'UNKNOWN', 'VARCHAR']]

### ArrayColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TimeSeriesMeasureValueColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RowColumnInfo
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountSettingsRequestRequestTypeDef

### MaxQueryTCU
- **Type**: typing.Optional[int]

### QueryPricingModel
- **Type**: typing.Optional[typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']]


# UpdateAccountSettingsResponseTypeDef

### MaxQueryTCU
- **Type**: <class 'int'>
- **Required**: Yes

### QueryPricingModel
- **Type**: typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScheduledQueryRequestRequestTypeDef

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


