# Xray Classes

# AliasTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnnotationValueTypeDef

### NumberValue
- **Type**: typing.Optional[float]

### BooleanValue
- **Type**: typing.Optional[bool]

### StringValue
- **Type**: typing.Optional[str]


# AnomalousServiceTypeDef

### ServiceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]


# AvailabilityZoneDetailTypeDef

### Name
- **Type**: typing.Optional[str]


# BackendConnectionErrorsTypeDef

### TimeoutCount
- **Type**: typing.Optional[int]

### ConnectionRefusedCount
- **Type**: typing.Optional[int]

### HTTPCode4XXCount
- **Type**: typing.Optional[int]

### HTTPCode5XXCount
- **Type**: typing.Optional[int]

### UnknownHostCount
- **Type**: typing.Optional[int]

### OtherCount
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetTracesRequestPaginateTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# BatchGetTracesRequestTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# BatchGetTracesResultTypeDef

### Traces
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.TraceTypeDef]
- **Required**: Yes

### UnprocessedTraceIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CancelTraceRetrievalRequestTypeDef

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.InsightsConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.xray_classes.TagTypeDef]]


# CreateGroupResultTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSamplingRuleRequestTypeDef

### SamplingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.SamplingRuleUnionTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.xray_classes.TagTypeDef]]


# CreateSamplingRuleResultTypeDef

### SamplingRuleRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.SamplingRuleRecordTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGroupRequestTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]


# DeleteResourcePolicyRequestTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DeleteSamplingRuleRequestTypeDef

### RuleName
- **Type**: typing.Optional[str]

### RuleARN
- **Type**: typing.Optional[str]


# DeleteSamplingRuleResultTypeDef

### SamplingRuleRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.SamplingRuleRecordTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EdgeStatisticsTypeDef

### OkCount
- **Type**: typing.Optional[int]

### ErrorStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ErrorStatisticsTypeDef]

### FaultStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.FaultStatisticsTypeDef]

### TotalCount
- **Type**: typing.Optional[int]

### TotalResponseTime
- **Type**: typing.Optional[float]


# EdgeTypeDef

### ReferenceId
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### SummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.EdgeStatisticsTypeDef]

### ResponseTimeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.HistogramEntryTypeDef]]

### Aliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.AliasTypeDef]]

### EdgeType
- **Type**: typing.Optional[str]

### ReceivedEventAgeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.HistogramEntryTypeDef]]


# EncryptionConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ErrorRootCauseEntityTypeDef

### Name
- **Type**: typing.Optional[str]

### Exceptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.RootCauseExceptionTypeDef]]

### Remote
- **Type**: typing.Optional[bool]


# ErrorRootCauseServiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ErrorRootCauseTypeDef

### Services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ErrorRootCauseServiceTypeDef]]

### ClientImpacting
- **Type**: typing.Optional[bool]


# ErrorStatisticsTypeDef

### ThrottleCount
- **Type**: typing.Optional[int]

### OtherCount
- **Type**: typing.Optional[int]

### TotalCount
- **Type**: typing.Optional[int]


# FaultRootCauseEntityTypeDef

### Name
- **Type**: typing.Optional[str]

### Exceptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.RootCauseExceptionTypeDef]]

### Remote
- **Type**: typing.Optional[bool]


# FaultRootCauseServiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FaultRootCauseTypeDef

### Services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.FaultRootCauseServiceTypeDef]]

### ClientImpacting
- **Type**: typing.Optional[bool]


# FaultStatisticsTypeDef

### OtherCount
- **Type**: typing.Optional[int]

### TotalCount
- **Type**: typing.Optional[int]


# ForecastStatisticsTypeDef

### FaultCountHigh
- **Type**: typing.Optional[int]

### FaultCountLow
- **Type**: typing.Optional[int]


# GetEncryptionConfigResultTypeDef

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupRequestTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]


# GetGroupResultTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetGroupsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetGroupsResultTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.GroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIndexingRulesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetIndexingRulesResultTypeDef

### IndexingRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.IndexingRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightEventsRequestTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetInsightEventsResultTypeDef

### InsightEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.InsightEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightImpactGraphRequestTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightImpactGraphResultTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceGraphStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceGraphEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.InsightImpactGraphServiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightRequestTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInsightResultTypeDef

### Insight
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.InsightTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightSummariesRequestTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### States
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ACTIVE', 'CLOSED']]]

### GroupARN
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetInsightSummariesResultTypeDef

### InsightSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.InsightSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRetrievedTracesGraphRequestTypeDef

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRetrievedTracesGraphResultTypeDef

### RetrievalStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'RUNNING', 'SCHEDULED', 'TIMEOUT']
- **Required**: Yes

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.RetrievedServiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingRulesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetSamplingRulesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingRulesResultTypeDef

### SamplingRuleRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.SamplingRuleRecordTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingStatisticSummariesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetSamplingStatisticSummariesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingStatisticSummariesResultTypeDef

### SamplingStatisticSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.SamplingStatisticSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingTargetsRequestTypeDef

### SamplingStatisticsDocuments
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.xray_classes.SamplingStatisticsDocumentTypeDef]
- **Required**: Yes


# GetSamplingTargetsResultTypeDef

### SamplingTargetDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.SamplingTargetDocumentTypeDef]
- **Required**: Yes

### LastRuleModification
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UnprocessedStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.UnprocessedStatisticsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceGraphRequestPaginateTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetServiceGraphRequestTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetServiceGraphResultTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.ServiceTypeDef]
- **Required**: Yes

### ContainsOldGroupVersions
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTimeSeriesServiceStatisticsRequestPaginateTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### EntitySelectorExpression
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### ForecastStatistics
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetTimeSeriesServiceStatisticsRequestTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### EntitySelectorExpression
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### ForecastStatistics
- **Type**: typing.Optional[bool]

### NextToken
- **Type**: typing.Optional[str]


# GetTimeSeriesServiceStatisticsResultTypeDef

### TimeSeriesServiceStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.TimeSeriesServiceStatisticsTypeDef]
- **Required**: Yes

### ContainsOldGroupVersions
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTraceGraphRequestPaginateTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetTraceGraphRequestTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTraceGraphResultTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.ServiceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTraceSegmentDestinationResultTypeDef

### Destination
- **Type**: typing.Literal['CloudWatchLogs', 'XRay']
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTraceSummariesRequestPaginateTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### TimeRangeType
- **Type**: typing.Optional[typing.Literal['Event', 'Service', 'TraceId']]

### Sampling
- **Type**: typing.Optional[bool]

### SamplingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.SamplingStrategyTypeDef]

### FilterExpression
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetTraceSummariesRequestTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### TimeRangeType
- **Type**: typing.Optional[typing.Literal['Event', 'Service', 'TraceId']]

### Sampling
- **Type**: typing.Optional[bool]

### SamplingStrategy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.SamplingStrategyTypeDef]

### FilterExpression
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetTraceSummariesResultTypeDef

### TraceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.TraceSummaryTypeDef]
- **Required**: Yes

### ApproximateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TracesProcessedCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GraphLinkTypeDef

### ReferenceType
- **Type**: typing.Optional[str]

### SourceTraceId
- **Type**: typing.Optional[str]

### DestinationTraceIds
- **Type**: typing.Optional[typing.List[str]]


# GroupSummaryTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.InsightsConfigurationTypeDef]


# GroupTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.InsightsConfigurationTypeDef]


# HistogramEntryTypeDef

### Value
- **Type**: typing.Optional[float]

### Count
- **Type**: typing.Optional[int]


# HttpTypeDef

### HttpURL
- **Type**: typing.Optional[str]

### HttpStatus
- **Type**: typing.Optional[int]

### HttpMethod
- **Type**: typing.Optional[str]

### UserAgent
- **Type**: typing.Optional[str]

### ClientIp
- **Type**: typing.Optional[str]


# IndexingRuleTypeDef

### Name
- **Type**: typing.Optional[str]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### Rule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.IndexingRuleValueTypeDef]


# IndexingRuleValueTypeDef

### Probabilistic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ProbabilisticRuleValueTypeDef]


# IndexingRuleValueUpdateTypeDef

### Probabilistic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ProbabilisticRuleValueUpdateTypeDef]


# InsightEventTypeDef

### Summary
- **Type**: typing.Optional[str]

### EventTime
- **Type**: typing.Optional[datetime.datetime]

### ClientRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.RequestImpactStatisticsTypeDef]

### RootCauseServiceRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.RequestImpactStatisticsTypeDef]

### TopAnomalousServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.AnomalousServiceTypeDef]]


# InsightImpactGraphEdgeTypeDef

### ReferenceId
- **Type**: typing.Optional[int]


# InsightImpactGraphServiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InsightSummaryTypeDef

### InsightId
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### RootCauseServiceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]

### Categories
- **Type**: typing.Optional[typing.List[typing.Literal['FAULT']]]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CLOSED']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Summary
- **Type**: typing.Optional[str]

### ClientRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.RequestImpactStatisticsTypeDef]

### RootCauseServiceRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.RequestImpactStatisticsTypeDef]

### TopAnomalousServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.AnomalousServiceTypeDef]]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# InsightTypeDef

### InsightId
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### RootCauseServiceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]

### Categories
- **Type**: typing.Optional[typing.List[typing.Literal['FAULT']]]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CLOSED']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Summary
- **Type**: typing.Optional[str]

### ClientRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.RequestImpactStatisticsTypeDef]

### RootCauseServiceRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.RequestImpactStatisticsTypeDef]

### TopAnomalousServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.AnomalousServiceTypeDef]]


# InsightsConfigurationTypeDef

### InsightsEnabled
- **Type**: typing.Optional[bool]

### NotificationsEnabled
- **Type**: typing.Optional[bool]


# InstanceIdDetailTypeDef

### Id
- **Type**: typing.Optional[str]


# ListResourcePoliciesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# ListResourcePoliciesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListResourcePoliciesResultTypeDef

### ResourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.ResourcePolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRetrievedTracesRequestTypeDef

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes

### TraceFormat
- **Type**: typing.Optional[typing.Literal['OTEL', 'XRAY']]

### NextToken
- **Type**: typing.Optional[str]


# ListRetrievedTracesResultTypeDef

### RetrievalStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'RUNNING', 'SCHEDULED', 'TIMEOUT']
- **Required**: Yes

### TraceFormat
- **Type**: typing.Literal['OTEL', 'XRAY']
- **Required**: Yes

### Traces
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.RetrievedTraceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProbabilisticRuleValueTypeDef

### DesiredSamplingPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### ActualSamplingPercentage
- **Type**: typing.Optional[float]


# ProbabilisticRuleValueUpdateTypeDef

### DesiredSamplingPercentage
- **Type**: <class 'float'>
- **Required**: Yes


# PutEncryptionConfigResultTypeDef

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]

### BypassPolicyLockoutCheck
- **Type**: typing.Optional[bool]


# PutResourcePolicyResultTypeDef

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutTelemetryRecordsRequestTypeDef

### TelemetryRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.xray_classes.TelemetryRecordTypeDef]
- **Required**: Yes

### EC2InstanceId
- **Type**: typing.Optional[str]

### Hostname
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]


# PutTraceSegmentsRequestTypeDef

### TraceSegmentDocuments
- **Type**: typing.Sequence[str]
- **Required**: Yes


# PutTraceSegmentsResultTypeDef

### UnprocessedTraceSegments
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.UnprocessedTraceSegmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequestImpactStatisticsTypeDef

### FaultCount
- **Type**: typing.Optional[int]

### OkCount
- **Type**: typing.Optional[int]

### TotalCount
- **Type**: typing.Optional[int]


# ResourceARNDetailTypeDef

### ARN
- **Type**: typing.Optional[str]


# ResourcePolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]

### PolicyDocument
- **Type**: typing.Optional[str]

### PolicyRevisionId
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


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


# ResponseTimeRootCauseEntityTypeDef

### Name
- **Type**: typing.Optional[str]

### Coverage
- **Type**: typing.Optional[float]

### Remote
- **Type**: typing.Optional[bool]


# ResponseTimeRootCauseServiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResponseTimeRootCauseTypeDef

### Services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ResponseTimeRootCauseServiceTypeDef]]

### ClientImpacting
- **Type**: typing.Optional[bool]


# RetrievedServiceTypeDef

### Service
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ServiceTypeDef]

### Links
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.GraphLinkTypeDef]]


# RetrievedTraceTypeDef

### Id
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[float]

### Spans
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.SpanTypeDef]]


# RootCauseExceptionTypeDef

### Name
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# SamplingRuleOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SamplingRuleRecordTypeDef

### SamplingRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.SamplingRuleOutputTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]


# SamplingRuleUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SamplingRuleUpdateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SamplingStatisticSummaryTypeDef

### RuleName
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### RequestCount
- **Type**: typing.Optional[int]

### BorrowCount
- **Type**: typing.Optional[int]

### SampledCount
- **Type**: typing.Optional[int]


# SamplingStatisticsDocumentTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientID
- **Type**: <class 'str'>
- **Required**: Yes

### Timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### RequestCount
- **Type**: <class 'int'>
- **Required**: Yes

### SampledCount
- **Type**: <class 'int'>
- **Required**: Yes

### BorrowCount
- **Type**: typing.Optional[int]


# SamplingStrategyTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['FixedRate', 'PartialScan']]

### Value
- **Type**: typing.Optional[float]


# SamplingTargetDocumentTypeDef

### RuleName
- **Type**: typing.Optional[str]

### FixedRate
- **Type**: typing.Optional[float]

### ReservoirQuota
- **Type**: typing.Optional[int]

### ReservoirQuotaTTL
- **Type**: typing.Optional[datetime.datetime]

### Interval
- **Type**: typing.Optional[int]


# SegmentTypeDef

### Id
- **Type**: typing.Optional[str]

### Document
- **Type**: typing.Optional[str]


# ServiceIdTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceStatisticsTypeDef

### OkCount
- **Type**: typing.Optional[int]

### ErrorStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ErrorStatisticsTypeDef]

### FaultStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.FaultStatisticsTypeDef]

### TotalCount
- **Type**: typing.Optional[int]

### TotalResponseTime
- **Type**: typing.Optional[float]


# ServiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SpanTypeDef

### Id
- **Type**: typing.Optional[str]

### Document
- **Type**: typing.Optional[str]


# StartTraceRetrievalRequestTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes


# StartTraceRetrievalResultTypeDef

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.xray_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TelemetryRecordTypeDef

### Timestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.TimestampTypeDef'>
- **Required**: Yes

### SegmentsReceivedCount
- **Type**: typing.Optional[int]

### SegmentsSentCount
- **Type**: typing.Optional[int]

### SegmentsSpilloverCount
- **Type**: typing.Optional[int]

### SegmentsRejectedCount
- **Type**: typing.Optional[int]

### BackendConnectionErrors
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.BackendConnectionErrorsTypeDef]


# TimeSeriesServiceStatisticsTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### EdgeSummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.EdgeStatisticsTypeDef]

### ServiceSummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ServiceStatisticsTypeDef]

### ServiceForecastStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ForecastStatisticsTypeDef]

### ResponseTimeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.HistogramEntryTypeDef]]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TraceSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### Duration
- **Type**: typing.Optional[float]

### ResponseTime
- **Type**: typing.Optional[float]

### HasFault
- **Type**: typing.Optional[bool]

### HasError
- **Type**: typing.Optional[bool]

### HasThrottle
- **Type**: typing.Optional[bool]

### IsPartial
- **Type**: typing.Optional[bool]

### Http
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.HttpTypeDef]

### Annotations
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.xray_classes.ValueWithServiceIdsTypeDef]]]

### Users
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.TraceUserTypeDef]]

### ServiceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]]

### ResourceARNs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ResourceARNDetailTypeDef]]

### InstanceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.InstanceIdDetailTypeDef]]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.AvailabilityZoneDetailTypeDef]]

### EntryPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]

### FaultRootCauses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.FaultRootCauseTypeDef]]

### ErrorRootCauses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ErrorRootCauseTypeDef]]

### ResponseTimeRootCauses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ResponseTimeRootCauseTypeDef]]

### Revision
- **Type**: typing.Optional[int]

### MatchedEventTime
- **Type**: typing.Optional[datetime.datetime]


# TraceTypeDef

### Id
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[float]

### LimitExceeded
- **Type**: typing.Optional[bool]

### Segments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.SegmentTypeDef]]


# TraceUserTypeDef

### UserName
- **Type**: typing.Optional[str]

### ServiceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]]


# UnprocessedStatisticsTypeDef

### RuleName
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# UnprocessedTraceSegmentTypeDef

### Id
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGroupRequestTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.InsightsConfigurationTypeDef]


# UpdateGroupResultTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIndexingRuleRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.IndexingRuleValueUpdateTypeDef'>
- **Required**: Yes


# UpdateIndexingRuleResultTypeDef

### IndexingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.IndexingRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSamplingRuleRequestTypeDef

### SamplingRuleUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.SamplingRuleUpdateTypeDef'>
- **Required**: Yes


# UpdateSamplingRuleResultTypeDef

### SamplingRuleRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.SamplingRuleRecordTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTraceSegmentDestinationRequestTypeDef

### Destination
- **Type**: typing.Optional[typing.Literal['CloudWatchLogs', 'XRay']]


# UpdateTraceSegmentDestinationResultTypeDef

### Destination
- **Type**: typing.Literal['CloudWatchLogs', 'XRay']
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValueWithServiceIdsTypeDef

### AnnotationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.AnnotationValueTypeDef]

### ServiceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]]


