# xray_classes

# AliasTypeDef

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]


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

# BatchGetTracesRequestBatchGetTracesPaginateTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# BatchGetTracesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateGroupRequestRequestTypeDef

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


# CreateSamplingRuleRequestRequestTypeDef

### SamplingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.SamplingRuleTypeDef'>
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


# DeleteGroupRequestRequestTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]


# DeleteResourcePolicyRequestRequestTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DeleteSamplingRuleRequestRequestTypeDef

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

### KeyId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'UPDATING']]

### Type
- **Type**: typing.Optional[typing.Literal['KMS', 'NONE']]


# ErrorRootCauseEntityTypeDef

### Name
- **Type**: typing.Optional[str]

### Exceptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.RootCauseExceptionTypeDef]]

### Remote
- **Type**: typing.Optional[bool]


# ErrorRootCauseServiceTypeDef

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### EntityPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ErrorRootCauseEntityTypeDef]]

### Inferred
- **Type**: typing.Optional[bool]


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

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### EntityPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.FaultRootCauseEntityTypeDef]]

### Inferred
- **Type**: typing.Optional[bool]


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


# GetGroupRequestRequestTypeDef

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


# GetGroupsRequestGetGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetGroupsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetGroupsResultTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.GroupSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightEventsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightImpactGraphRequestRequestTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInsightRequestRequestTypeDef

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


# GetInsightSummariesRequestRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSamplingRulesRequestGetSamplingRulesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetSamplingRulesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingRulesResultPaginatorTypeDef

### SamplingRuleRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.SamplingRuleRecordPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSamplingRulesResultTypeDef

### SamplingRuleRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.SamplingRuleRecordTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSamplingStatisticSummariesRequestGetSamplingStatisticSummariesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetSamplingStatisticSummariesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingStatisticSummariesResultTypeDef

### SamplingStatisticSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.SamplingStatisticSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSamplingTargetsRequestRequestTypeDef

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


# GetServiceGraphRequestGetServiceGraphPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetServiceGraphRequestRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTimeSeriesServiceStatisticsRequestGetTimeSeriesServiceStatisticsPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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


# GetTimeSeriesServiceStatisticsRequestRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTraceGraphRequestGetTraceGraphPaginateTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# GetTraceGraphRequestRequestTypeDef

### TraceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTraceGraphResultTypeDef

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.ServiceTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTraceSummariesRequestGetTraceSummariesPaginateTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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


# GetTraceSummariesRequestRequestTypeDef

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### ReferenceId
- **Type**: typing.Optional[int]

### Type
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### AccountId
- **Type**: typing.Optional[str]

### Edges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.InsightImpactGraphEdgeTypeDef]]


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


# ListResourcePoliciesRequestListResourcePoliciesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# ListResourcePoliciesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListResourcePoliciesResultTypeDef

### ResourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.ResourcePolicyTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray_classes.TagTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutEncryptionConfigRequestRequestTypeDef

### Type
- **Type**: typing.Literal['KMS', 'NONE']
- **Required**: Yes

### KeyId
- **Type**: typing.Optional[str]


# PutEncryptionConfigResultTypeDef

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.EncryptionConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutResourcePolicyRequestRequestTypeDef

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


# PutTelemetryRecordsRequestRequestTypeDef

### TelemetryRecords
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.xray_classes.TelemetryRecordTypeDef]
- **Required**: Yes

### EC2InstanceId
- **Type**: typing.Optional[str]

### Hostname
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]


# PutTraceSegmentsRequestRequestTypeDef

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


# ResponseTimeRootCauseEntityTypeDef

### Name
- **Type**: typing.Optional[str]

### Coverage
- **Type**: typing.Optional[float]

### Remote
- **Type**: typing.Optional[bool]


# ResponseTimeRootCauseServiceTypeDef

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### EntityPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ResponseTimeRootCauseEntityTypeDef]]

### Inferred
- **Type**: typing.Optional[bool]


# ResponseTimeRootCauseTypeDef

### Services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ResponseTimeRootCauseServiceTypeDef]]

### ClientImpacting
- **Type**: typing.Optional[bool]


# RootCauseExceptionTypeDef

### Name
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# SamplingRulePaginatorTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### FixedRate
- **Type**: <class 'float'>
- **Required**: Yes

### ReservoirSize
- **Type**: <class 'int'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceType
- **Type**: <class 'str'>
- **Required**: Yes

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPMethod
- **Type**: <class 'str'>
- **Required**: Yes

### URLPath
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### RuleName
- **Type**: typing.Optional[str]

### RuleARN
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# SamplingRuleRecordPaginatorTypeDef

### SamplingRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.SamplingRulePaginatorTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]


# SamplingRuleRecordTypeDef

### SamplingRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.SamplingRuleTypeDef]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]


# SamplingRuleTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### FixedRate
- **Type**: <class 'float'>
- **Required**: Yes

### ReservoirSize
- **Type**: <class 'int'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceType
- **Type**: <class 'str'>
- **Required**: Yes

### Host
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPMethod
- **Type**: <class 'str'>
- **Required**: Yes

### URLPath
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'int'>
- **Required**: Yes

### RuleName
- **Type**: typing.Optional[str]

### RuleARN
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SamplingRuleUpdateTypeDef

### RuleName
- **Type**: typing.Optional[str]

### RuleARN
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### FixedRate
- **Type**: typing.Optional[float]

### ReservoirSize
- **Type**: typing.Optional[int]

### Host
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### ServiceType
- **Type**: typing.Optional[str]

### HTTPMethod
- **Type**: typing.Optional[str]

### URLPath
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


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
- **Type**: typing.Union[datetime.datetime, str]
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

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### AccountId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


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

### ReferenceId
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Root
- **Type**: typing.Optional[bool]

### AccountId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Edges
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.EdgeTypeDef]]

### SummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.ServiceStatisticsTypeDef]

### DurationHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.HistogramEntryTypeDef]]

### ResponseTimeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.HistogramEntryTypeDef]]


# TagResourceRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str]
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


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateGroupRequestRequestTypeDef

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


# UpdateSamplingRuleRequestRequestTypeDef

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


# ValueWithServiceIdsTypeDef

### AnnotationValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray_classes.AnnotationValueTypeDef]

### ServiceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray_classes.ServiceIdTypeDef]]


