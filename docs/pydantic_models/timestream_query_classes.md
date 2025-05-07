# Timestream Query Classes

# AccountSettingsNotificationConfiguration

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsConfiguration
- **Type**: <class 'NoneType'>


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelQueryRequest

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelQueryResponse

### CancellationMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# ColumnInfo

### Type
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# ColumnInfoPaginator

### Type
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TypePaginator'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# CreateScheduledQueryRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduleConfiguration'>
- **Required**: Yes

### NotificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.NotificationConfiguration'>
- **Required**: Yes

### ScheduledQueryExecutionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorReportConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ErrorReportConfiguration'>
- **Required**: Yes

### TargetConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TargetConfiguration, aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TargetConfigurationOutput, NoneType]

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]


# CreateScheduledQueryResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# Datum

### ScalarValue
- **Type**: typing.Optional[str]

### TimeSeriesValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TimeSeriesDataPoint]]

### ArrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### RowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### NullValue
- **Type**: typing.Optional[bool]


# DatumPaginator

### ScalarValue
- **Type**: typing.Optional[str]

### TimeSeriesValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TimeSeriesDataPointPaginator]]

### ArrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### RowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### NullValue
- **Type**: typing.Optional[bool]


# DeleteScheduledQueryRequest

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountSettingsResponse

### MaxQueryTCU
- **Type**: <class 'int'>
- **Required**: Yes

### QueryPricingModel
- **Type**: typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']
- **Required**: Yes

### QueryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryComputeResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEndpointsResponse

### Endpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.Endpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeScheduledQueryRequest

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeScheduledQueryResponse

### ScheduledQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduledQueryDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# DimensionMapping

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DimensionValueType
- **Type**: typing.Literal['VARCHAR']
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# Endpoint

### Address
- **Type**: <class 'str'>
- **Required**: Yes

### CachePeriodInMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# ErrorReportConfiguration

### S3Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.S3Configuration'>
- **Required**: Yes


# ErrorReportLocation

### S3ReportLocation
- **Type**: <class 'NoneType'>


# ExecuteScheduledQueryRequest

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### QueryInsights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduledQueryInsights]


# ExecutionStats

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


# LastUpdate

### TargetQueryTCU
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]


# ListScheduledQueriesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListScheduledQueriesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.PaginatorConfig]


# ListScheduledQueriesResponse

### ScheduledQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduledQuery]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MixedMeasureMapping

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.MultiMeasureAttributeMapping]]


# MixedMeasureMappingOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.MultiMeasureAttributeMapping]]


# MultiMeasureAttributeMapping

### SourceColumn
- **Type**: <class 'str'>
- **Required**: Yes

### MeasureValueType
- **Type**: typing.Literal['BIGINT', 'BOOLEAN', 'DOUBLE', 'TIMESTAMP', 'VARCHAR']
- **Required**: Yes

### TargetMultiMeasureAttributeName
- **Type**: typing.Optional[str]


# MultiMeasureMappings

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.MultiMeasureAttributeMapping]
- **Required**: Yes

### TargetMultiMeasureName
- **Type**: typing.Optional[str]


# MultiMeasureMappingsOutput

### MultiMeasureAttributeMappings
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.MultiMeasureAttributeMapping]
- **Required**: Yes

### TargetMultiMeasureName
- **Type**: typing.Optional[str]


# NotificationConfiguration

### SnsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.SnsConfiguration'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterMapping

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.Type'>
- **Required**: Yes


# PrepareQueryRequest

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ValidateOnly
- **Type**: typing.Optional[bool]


# PrepareQueryResponse

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### Columns
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.SelectColumn]
- **Required**: Yes

### Parameters
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ParameterMapping]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# ProvisionedCapacityRequest

### TargetQueryTCU
- **Type**: <class 'int'>
- **Required**: Yes

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.AccountSettingsNotificationConfiguration]


# ProvisionedCapacityResponse

### ActiveQueryTCU
- **Type**: typing.Optional[int]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.AccountSettingsNotificationConfiguration]

### LastUpdate
- **Type**: <class 'NoneType'>


# QueryComputeRequest

### ComputeMode
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'PROVISIONED']]

### ProvisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ProvisionedCapacityRequest]


# QueryComputeResponse

### ComputeMode
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'PROVISIONED']]

### ProvisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ProvisionedCapacityResponse]


# QueryInsights

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED_WITH_RATE_CONTROL']
- **Required**: Yes


# QueryInsightsResponse

### QuerySpatialCoverage
- **Type**: <class 'NoneType'>

### QueryTemporalRange
- **Type**: <class 'NoneType'>

### QueryTableCount
- **Type**: typing.Optional[int]

### OutputRows
- **Type**: typing.Optional[int]

### OutputBytes
- **Type**: typing.Optional[int]

### UnloadPartitionCount
- **Type**: typing.Optional[int]

### UnloadWrittenRows
- **Type**: typing.Optional[int]

### UnloadWrittenBytes
- **Type**: typing.Optional[int]


# QueryRequest

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxRows
- **Type**: typing.Optional[int]

### QueryInsights
- **Type**: <class 'NoneType'>


# QueryRequestPaginate

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### QueryInsights
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.PaginatorConfig]


# QueryResponse

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.Row]
- **Required**: Yes

### ColumnInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ColumnInfo]
- **Required**: Yes

### QueryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryStatus'>
- **Required**: Yes

### QueryInsightsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryInsightsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# QueryResponsePaginator

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.RowPaginator]
- **Required**: Yes

### ColumnInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ColumnInfoPaginator]
- **Required**: Yes

### QueryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryStatus'>
- **Required**: Yes

### QueryInsightsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryInsightsResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# QuerySpatialCoverage

### Max
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QuerySpatialCoverageMax]


# QuerySpatialCoverageMax

### Value
- **Type**: typing.Optional[float]

### TableArn
- **Type**: typing.Optional[str]

### PartitionKey
- **Type**: typing.Optional[typing.List[str]]


# QueryStatus

### ProgressPercentage
- **Type**: typing.Optional[float]

### CumulativeBytesScanned
- **Type**: typing.Optional[int]

### CumulativeBytesMetered
- **Type**: typing.Optional[int]


# QueryTemporalRange

### Max
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryTemporalRangeMax]


# QueryTemporalRangeMax

### Value
- **Type**: typing.Optional[int]

### TableArn
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


# Row

### Data
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.Datum]
- **Required**: Yes


# RowPaginator

### Data
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.DatumPaginator]
- **Required**: Yes


# S3Configuration

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ObjectKeyPrefix
- **Type**: typing.Optional[str]

### EncryptionOption
- **Type**: typing.Optional[typing.Literal['SSE_KMS', 'SSE_S3']]


# S3ReportLocation

### BucketName
- **Type**: typing.Optional[str]

### ObjectKey
- **Type**: typing.Optional[str]


# ScheduleConfiguration

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes


# ScheduledQuery

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
- **Type**: <class 'NoneType'>

### TargetDestination
- **Type**: <class 'NoneType'>

### LastRunStatus
- **Type**: typing.Optional[typing.Literal['AUTO_TRIGGER_FAILURE', 'AUTO_TRIGGER_SUCCESS', 'MANUAL_TRIGGER_FAILURE', 'MANUAL_TRIGGER_SUCCESS']]


# ScheduledQueryDescription

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
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduleConfiguration'>
- **Required**: Yes

### NotificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.NotificationConfiguration'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### PreviousInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### NextInvocationTime
- **Type**: typing.Optional[datetime.datetime]

### TargetConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TargetConfigurationOutput]

### ScheduledQueryExecutionRoleArn
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### ErrorReportConfiguration
- **Type**: <class 'NoneType'>

### LastRunSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduledQueryRunSummary]

### RecentlyFailedRuns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduledQueryRunSummary]]


# ScheduledQueryInsights

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED_WITH_RATE_CONTROL']
- **Required**: Yes


# ScheduledQueryInsightsResponse

### QuerySpatialCoverage
- **Type**: <class 'NoneType'>

### QueryTemporalRange
- **Type**: <class 'NoneType'>

### QueryTableCount
- **Type**: typing.Optional[int]

### OutputRows
- **Type**: typing.Optional[int]

### OutputBytes
- **Type**: typing.Optional[int]


# ScheduledQueryRunSummary

### InvocationTime
- **Type**: typing.Optional[datetime.datetime]

### TriggerTime
- **Type**: typing.Optional[datetime.datetime]

### RunStatus
- **Type**: typing.Optional[typing.Literal['AUTO_TRIGGER_FAILURE', 'AUTO_TRIGGER_SUCCESS', 'MANUAL_TRIGGER_FAILURE', 'MANUAL_TRIGGER_SUCCESS']]

### ExecutionStats
- **Type**: <class 'NoneType'>

### QueryInsightsResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ScheduledQueryInsightsResponse]

### ErrorReportLocation
- **Type**: <class 'NoneType'>

### FailureReason
- **Type**: typing.Optional[str]


# SelectColumn

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: <class 'NoneType'>

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]

### Aliased
- **Type**: typing.Optional[bool]


# SnsConfiguration

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.Tag]
- **Required**: Yes


# TargetConfiguration

### TimestreamConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TimestreamConfiguration'>
- **Required**: Yes


# TargetConfigurationOutput

### TimestreamConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.TimestreamConfigurationOutput'>
- **Required**: Yes


# TargetDestination

### TimestreamDestination
- **Type**: <class 'NoneType'>


# TimeSeriesDataPoint

### Time
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# TimeSeriesDataPointPaginator

### Time
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# TimestreamConfiguration

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.DimensionMapping]
- **Required**: Yes

### MultiMeasureMappings
- **Type**: <class 'NoneType'>

### MixedMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.MixedMeasureMapping]]

### MeasureNameColumn
- **Type**: typing.Optional[str]


# TimestreamConfigurationOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.DimensionMapping]
- **Required**: Yes

### MultiMeasureMappings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.MultiMeasureMappingsOutput]

### MixedMeasureMappings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.MixedMeasureMappingOutput]]

### MeasureNameColumn
- **Type**: typing.Optional[str]


# TimestreamDestination

### DatabaseName
- **Type**: typing.Optional[str]

### TableName
- **Type**: typing.Optional[str]


# Type

### ScalarType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DATE', 'DOUBLE', 'INTEGER', 'INTERVAL_DAY_TO_SECOND', 'INTERVAL_YEAR_TO_MONTH', 'TIME', 'TIMESTAMP', 'UNKNOWN', 'VARCHAR']]

### ArrayColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TimeSeriesMeasureValueColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RowColumnInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ColumnInfo]]


# TypePaginator

### ScalarType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DATE', 'DOUBLE', 'INTEGER', 'INTERVAL_DAY_TO_SECOND', 'INTERVAL_YEAR_TO_MONTH', 'TIME', 'TIMESTAMP', 'UNKNOWN', 'VARCHAR']]

### ArrayColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TimeSeriesMeasureValueColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RowColumnInfo
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccountSettingsRequest

### MaxQueryTCU
- **Type**: typing.Optional[int]

### QueryPricingModel
- **Type**: typing.Optional[typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']]

### QueryCompute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryComputeRequest]


# UpdateAccountSettingsResponse

### MaxQueryTCU
- **Type**: <class 'int'>
- **Required**: Yes

### QueryPricingModel
- **Type**: typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']
- **Required**: Yes

### QueryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.QueryComputeResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query.timestream_query_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateScheduledQueryRequest

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


