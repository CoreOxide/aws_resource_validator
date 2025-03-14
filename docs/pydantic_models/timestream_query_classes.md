# Timestream Query Classes

# AccountSettingsNotificationConfigurationTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SnsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.SnsConfigurationTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelQueryRequestTypeDef

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


# ColumnInfoPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ColumnInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateScheduledQueryRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.TargetConfigurationUnionTypeDef]

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


# DatumPaginatorTypeDef

### ScalarValue
- **Type**: typing.Optional[str]

### TimeSeriesValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.TimeSeriesDataPointPaginatorTypeDef]]

### ArrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### RowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### NullValue
- **Type**: typing.Optional[bool]


# DatumTypeDef

### ScalarValue
- **Type**: typing.Optional[str]

### TimeSeriesValue
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.TimeSeriesDataPointTypeDef]]

### ArrayValue
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### RowValue
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### NullValue
- **Type**: typing.Optional[bool]


# DeleteScheduledQueryRequestTypeDef

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

### QueryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.QueryComputeResponseTypeDef'>
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


# DescribeScheduledQueryRequestTypeDef

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


# ExecuteScheduledQueryRequestTypeDef

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationTime
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.TimestampTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### QueryInsights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ScheduledQueryInsightsTypeDef]


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


# LastUpdateTypeDef

### TargetQueryTCU
- **Type**: typing.Optional[int]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'PENDING', 'SUCCEEDED']]

### StatusMessage
- **Type**: typing.Optional[str]


# ListScheduledQueriesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.PaginatorConfigTypeDef]


# ListScheduledQueriesRequestTypeDef

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


# ListTagsForResourceRequestPaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrepareQueryRequestTypeDef

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


# ProvisionedCapacityRequestTypeDef

### TargetQueryTCU
- **Type**: <class 'int'>
- **Required**: Yes

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.AccountSettingsNotificationConfigurationTypeDef]


# ProvisionedCapacityResponseTypeDef

### ActiveQueryTCU
- **Type**: typing.Optional[int]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.AccountSettingsNotificationConfigurationTypeDef]

### LastUpdate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.LastUpdateTypeDef]


# QueryComputeRequestTypeDef

### ComputeMode
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'PROVISIONED']]

### ProvisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ProvisionedCapacityRequestTypeDef]


# QueryComputeResponseTypeDef

### ComputeMode
- **Type**: typing.Optional[typing.Literal['ON_DEMAND', 'PROVISIONED']]

### ProvisionedCapacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ProvisionedCapacityResponseTypeDef]


# QueryInsightsResponseTypeDef

### QuerySpatialCoverage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QuerySpatialCoverageTypeDef]

### QueryTemporalRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QueryTemporalRangeTypeDef]

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


# QueryInsightsTypeDef

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED_WITH_RATE_CONTROL']
- **Required**: Yes


# QueryRequestPaginateTypeDef

### QueryString
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### QueryInsights
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QueryInsightsTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.PaginatorConfigTypeDef]


# QueryRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QueryInsightsTypeDef]


# QueryResponsePaginatorTypeDef

### QueryId
- **Type**: <class 'str'>
- **Required**: Yes

### Rows
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.RowPaginatorTypeDef]
- **Required**: Yes

### ColumnInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.ColumnInfoPaginatorTypeDef]
- **Required**: Yes

### QueryStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.QueryStatusTypeDef'>
- **Required**: Yes

### QueryInsightsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.QueryInsightsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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

### QueryInsightsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.QueryInsightsResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# QuerySpatialCoverageMaxTypeDef

### Value
- **Type**: typing.Optional[float]

### TableArn
- **Type**: typing.Optional[str]

### PartitionKey
- **Type**: typing.Optional[typing.List[str]]


# QuerySpatialCoverageTypeDef

### Max
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QuerySpatialCoverageMaxTypeDef]


# QueryStatusTypeDef

### ProgressPercentage
- **Type**: typing.Optional[float]

### CumulativeBytesScanned
- **Type**: typing.Optional[int]

### CumulativeBytesMetered
- **Type**: typing.Optional[int]


# QueryTemporalRangeMaxTypeDef

### Value
- **Type**: typing.Optional[int]

### TableArn
- **Type**: typing.Optional[str]


# QueryTemporalRangeTypeDef

### Max
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QueryTemporalRangeMaxTypeDef]


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


# RowPaginatorTypeDef

### Data
- **Type**: typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.DatumPaginatorTypeDef]
- **Required**: Yes


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


# ScheduledQueryInsightsResponseTypeDef

### QuerySpatialCoverage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QuerySpatialCoverageTypeDef]

### QueryTemporalRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QueryTemporalRangeTypeDef]

### QueryTableCount
- **Type**: typing.Optional[int]

### OutputRows
- **Type**: typing.Optional[int]

### OutputBytes
- **Type**: typing.Optional[int]


# ScheduledQueryInsightsTypeDef

### Mode
- **Type**: typing.Literal['DISABLED', 'ENABLED_WITH_RATE_CONTROL']
- **Required**: Yes


# ScheduledQueryRunSummaryTypeDef

### InvocationTime
- **Type**: typing.Optional[datetime.datetime]

### TriggerTime
- **Type**: typing.Optional[datetime.datetime]

### RunStatus
- **Type**: typing.Optional[typing.Literal['AUTO_TRIGGER_FAILURE', 'AUTO_TRIGGER_SUCCESS', 'MANUAL_TRIGGER_FAILURE', 'MANUAL_TRIGGER_SUCCESS']]

### ExecutionStats
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ExecutionStatsTypeDef]

### QueryInsightsResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.ScheduledQueryInsightsResponseTypeDef]

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnsConfigurationTypeDef

### TopicArn
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

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


# TargetConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TargetDestinationTypeDef

### TimestreamDestination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.TimestreamDestinationTypeDef]


# TimeSeriesDataPointPaginatorTypeDef

### Time
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# TimeSeriesDataPointTypeDef

### Time
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# TypePaginatorTypeDef

### ScalarType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DATE', 'DOUBLE', 'INTEGER', 'INTERVAL_DAY_TO_SECOND', 'INTERVAL_YEAR_TO_MONTH', 'TIME', 'TIMESTAMP', 'UNKNOWN', 'VARCHAR']]

### ArrayColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TimeSeriesMeasureValueColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RowColumnInfo
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# TypeTypeDef

### ScalarType
- **Type**: typing.Optional[typing.Literal['BIGINT', 'BOOLEAN', 'DATE', 'DOUBLE', 'INTEGER', 'INTERVAL_DAY_TO_SECOND', 'INTERVAL_YEAR_TO_MONTH', 'TIME', 'TIMESTAMP', 'UNKNOWN', 'VARCHAR']]

### ArrayColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TimeSeriesMeasureValueColumnInfo
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### RowColumnInfo
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.timestream_query_classes.ColumnInfoTypeDef]]


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountSettingsRequestTypeDef

### MaxQueryTCU
- **Type**: typing.Optional[int]

### QueryPricingModel
- **Type**: typing.Optional[typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']]

### QueryCompute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.timestream_query_classes.QueryComputeRequestTypeDef]


# UpdateAccountSettingsResponseTypeDef

### MaxQueryTCU
- **Type**: <class 'int'>
- **Required**: Yes

### QueryPricingModel
- **Type**: typing.Literal['BYTES_SCANNED', 'COMPUTE_UNITS']
- **Required**: Yes

### QueryCompute
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.QueryComputeResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.timestream_query_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateScheduledQueryRequestTypeDef

### ScheduledQueryArn
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes


