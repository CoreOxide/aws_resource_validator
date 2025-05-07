# Xray Classes

# Alias

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]


# AnnotationValue

### NumberValue
- **Type**: typing.Optional[float]

### BooleanValue
- **Type**: typing.Optional[bool]

### StringValue
- **Type**: typing.Optional[str]


# AnomalousService

### ServiceId
- **Type**: <class 'NoneType'>


# AvailabilityZoneDetail

### Name
- **Type**: typing.Optional[str]


# BackendConnectionErrors

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

# BatchGetTracesRequest

### TraceIds
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# BatchGetTracesRequestPaginate

### TraceIds
- **Type**: typing.List[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# BatchGetTracesResult

### Traces
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Trace]
- **Required**: Yes

### UnprocessedTraceIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CancelTraceRetrievalRequest

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Tag]]


# CreateGroupResult

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSamplingRuleRequest

### SamplingRule
- **Type**: typing.Union[aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRule, aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRuleOutput]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Tag]]


# CreateSamplingRuleResult

### SamplingRuleRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRuleRecord'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGroupRequest

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]


# DeleteResourcePolicyRequest

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyRevisionId
- **Type**: typing.Optional[str]


# DeleteSamplingRuleRequest

### RuleName
- **Type**: typing.Optional[str]

### RuleARN
- **Type**: typing.Optional[str]


# DeleteSamplingRuleResult

### SamplingRuleRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRuleRecord'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# Edge

### ReferenceId
- **Type**: typing.Optional[int]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### SummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.EdgeStatistics]

### ResponseTimeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.HistogramEntry]]

### Aliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Alias]]

### EdgeType
- **Type**: typing.Optional[str]

### ReceivedEventAgeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.HistogramEntry]]


# EdgeStatistics

### OkCount
- **Type**: typing.Optional[int]

### ErrorStatistics
- **Type**: <class 'NoneType'>

### FaultStatistics
- **Type**: <class 'NoneType'>

### TotalCount
- **Type**: typing.Optional[int]

### TotalResponseTime
- **Type**: typing.Optional[float]


# EncryptionConfig

### KeyId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'UPDATING']]

### Type
- **Type**: typing.Optional[typing.Literal['KMS', 'NONE']]


# ErrorRootCause

### Services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ErrorRootCauseService]]

### ClientImpacting
- **Type**: typing.Optional[bool]


# ErrorRootCauseEntity

### Name
- **Type**: typing.Optional[str]

### Exceptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.RootCauseException]]

### Remote
- **Type**: typing.Optional[bool]


# ErrorRootCauseService

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### EntityPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ErrorRootCauseEntity]]

### Inferred
- **Type**: typing.Optional[bool]


# ErrorStatistics

### ThrottleCount
- **Type**: typing.Optional[int]

### OtherCount
- **Type**: typing.Optional[int]

### TotalCount
- **Type**: typing.Optional[int]


# FaultRootCause

### Services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.FaultRootCauseService]]

### ClientImpacting
- **Type**: typing.Optional[bool]


# FaultRootCauseEntity

### Name
- **Type**: typing.Optional[str]

### Exceptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.RootCauseException]]

### Remote
- **Type**: typing.Optional[bool]


# FaultRootCauseService

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### EntityPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.FaultRootCauseEntity]]

### Inferred
- **Type**: typing.Optional[bool]


# FaultStatistics

### OtherCount
- **Type**: typing.Optional[int]

### TotalCount
- **Type**: typing.Optional[int]


# ForecastStatistics

### FaultCountHigh
- **Type**: typing.Optional[int]

### FaultCountLow
- **Type**: typing.Optional[int]


# GetEncryptionConfigResult

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.EncryptionConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupRequest

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]


# GetGroupResult

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupsRequest

### NextToken
- **Type**: typing.Optional[str]


# GetGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# GetGroupsResult

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.GroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetIndexingRulesRequest

### NextToken
- **Type**: typing.Optional[str]


# GetIndexingRulesResult

### IndexingRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.IndexingRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightEventsRequest

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetInsightEventsResult

### InsightEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.InsightEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightImpactGraphRequest

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


# GetInsightImpactGraphResult

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.InsightImpactGraphService]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetInsightRequest

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes


# GetInsightResult

### Insight
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.Insight'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# GetInsightSummariesRequest

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### States
- **Type**: typing.Optional[typing.List[typing.Literal['ACTIVE', 'CLOSED']]]

### GroupARN
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetInsightSummariesResult

### InsightSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.InsightSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRetrievedTracesGraphRequest

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetRetrievedTracesGraphResult

### RetrievalStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'RUNNING', 'SCHEDULED', 'TIMEOUT']
- **Required**: Yes

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.RetrievedService]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingRulesRequest

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingRulesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# GetSamplingRulesResult

### SamplingRuleRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRuleRecord]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingStatisticSummariesRequest

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingStatisticSummariesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# GetSamplingStatisticSummariesResult

### SamplingStatisticSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.SamplingStatisticSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetSamplingTargetsRequest

### SamplingStatisticsDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.SamplingStatisticsDocument]
- **Required**: Yes


# GetSamplingTargetsResult

### SamplingTargetDocuments
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.SamplingTargetDocument]
- **Required**: Yes

### LastRuleModification
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UnprocessedStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.UnprocessedStatistics]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceGraphRequest

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


# GetServiceGraphRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# GetServiceGraphResult

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Service]
- **Required**: Yes

### ContainsOldGroupVersions
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTimeSeriesServiceStatisticsRequest

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


# GetTimeSeriesServiceStatisticsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# GetTimeSeriesServiceStatisticsResult

### TimeSeriesServiceStatistics
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.TimeSeriesServiceStatistics]
- **Required**: Yes

### ContainsOldGroupVersions
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTraceGraphRequest

### TraceIds
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTraceGraphRequestPaginate

### TraceIds
- **Type**: typing.List[str]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# GetTraceGraphResult

### Services
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Service]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetTraceSegmentDestinationResult

### Destination
- **Type**: typing.Literal['CloudWatchLogs', 'XRay']
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# GetTraceSummariesRequest

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
- **Type**: <class 'NoneType'>

### FilterExpression
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# GetTraceSummariesRequestPaginate

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
- **Type**: <class 'NoneType'>

### FilterExpression
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# GetTraceSummariesResult

### TraceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.TraceSummary]
- **Required**: Yes

### ApproximateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### TracesProcessedCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GraphLink

### ReferenceType
- **Type**: typing.Optional[str]

### SourceTraceId
- **Type**: typing.Optional[str]

### DestinationTraceIds
- **Type**: typing.Optional[typing.List[str]]


# Group

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: <class 'NoneType'>


# GroupSummary

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: <class 'NoneType'>


# HistogramEntry

### Value
- **Type**: typing.Optional[float]

### Count
- **Type**: typing.Optional[int]


# Http

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


# IndexingRule

### Name
- **Type**: typing.Optional[str]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### Rule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.IndexingRuleValue]


# IndexingRuleValue

### Probabilistic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ProbabilisticRuleValue]


# IndexingRuleValueUpdate

### Probabilistic
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ProbabilisticRuleValueUpdate]


# Insight

### InsightId
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### RootCauseServiceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceId]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.RequestImpactStatistics]

### RootCauseServiceRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.RequestImpactStatistics]

### TopAnomalousServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.AnomalousService]]


# InsightEvent

### Summary
- **Type**: typing.Optional[str]

### EventTime
- **Type**: typing.Optional[datetime.datetime]

### ClientRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.RequestImpactStatistics]

### RootCauseServiceRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.RequestImpactStatistics]

### TopAnomalousServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.AnomalousService]]


# InsightImpactGraphEdge

### ReferenceId
- **Type**: typing.Optional[int]


# InsightImpactGraphService

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.InsightImpactGraphEdge]]


# InsightSummary

### InsightId
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### RootCauseServiceId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceId]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.RequestImpactStatistics]

### RootCauseServiceRequestImpactStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.RequestImpactStatistics]

### TopAnomalousServices
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.AnomalousService]]

### LastUpdateTime
- **Type**: typing.Optional[datetime.datetime]


# InsightsConfiguration

### InsightsEnabled
- **Type**: typing.Optional[bool]

### NotificationsEnabled
- **Type**: typing.Optional[bool]


# InstanceIdDetail

### Id
- **Type**: typing.Optional[str]


# ListResourcePoliciesRequest

### NextToken
- **Type**: typing.Optional[str]


# ListResourcePoliciesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# ListResourcePoliciesResult

### ResourcePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ResourcePolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRetrievedTracesRequest

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes

### TraceFormat
- **Type**: typing.Optional[typing.Literal['OTEL', 'XRAY']]

### NextToken
- **Type**: typing.Optional[str]


# ListRetrievedTracesResult

### RetrievalStatus
- **Type**: typing.Literal['CANCELLED', 'COMPLETE', 'FAILED', 'RUNNING', 'SCHEDULED', 'TIMEOUT']
- **Required**: Yes

### TraceFormat
- **Type**: typing.Literal['OTEL', 'XRAY']
- **Required**: Yes

### Traces
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.RetrievedTrace]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ProbabilisticRuleValue

### DesiredSamplingPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### ActualSamplingPercentage
- **Type**: typing.Optional[float]


# ProbabilisticRuleValueUpdate

### DesiredSamplingPercentage
- **Type**: <class 'float'>
- **Required**: Yes


# PutEncryptionConfigRequest

### Type
- **Type**: typing.Literal['KMS', 'NONE']
- **Required**: Yes

### KeyId
- **Type**: typing.Optional[str]


# PutEncryptionConfigResult

### EncryptionConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.EncryptionConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# PutResourcePolicyRequest

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


# PutResourcePolicyResult

### ResourcePolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# PutTelemetryRecordsRequest

### TelemetryRecords
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.TelemetryRecord]
- **Required**: Yes

### EC2InstanceId
- **Type**: typing.Optional[str]

### Hostname
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]


# PutTraceSegmentsRequest

### TraceSegmentDocuments
- **Type**: typing.List[str]
- **Required**: Yes


# PutTraceSegmentsResult

### UnprocessedTraceSegments
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.UnprocessedTraceSegment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# RequestImpactStatistics

### FaultCount
- **Type**: typing.Optional[int]

### OkCount
- **Type**: typing.Optional[int]

### TotalCount
- **Type**: typing.Optional[int]


# ResourceARNDetail

### ARN
- **Type**: typing.Optional[str]


# ResourcePolicy

### PolicyName
- **Type**: typing.Optional[str]

### PolicyDocument
- **Type**: typing.Optional[str]

### PolicyRevisionId
- **Type**: typing.Optional[str]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]


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


# ResponseTimeRootCause

### Services
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ResponseTimeRootCauseService]]

### ClientImpacting
- **Type**: typing.Optional[bool]


# ResponseTimeRootCauseEntity

### Name
- **Type**: typing.Optional[str]

### Coverage
- **Type**: typing.Optional[float]

### Remote
- **Type**: typing.Optional[bool]


# ResponseTimeRootCauseService

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### Type
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### EntityPath
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ResponseTimeRootCauseEntity]]

### Inferred
- **Type**: typing.Optional[bool]


# RetrievedService

### Service
- **Type**: <class 'NoneType'>

### Links
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.GraphLink]]


# RetrievedTrace

### Id
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[float]

### Spans
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Span]]


# RootCauseException

### Name
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# SamplingRule

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


# SamplingRuleOutput

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


# SamplingRuleRecord

### SamplingRule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRuleOutput]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]


# SamplingRuleUpdate

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# SamplingStatisticSummary

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


# SamplingStatisticsDocument

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


# SamplingStrategy

### Name
- **Type**: typing.Optional[typing.Literal['FixedRate', 'PartialScan']]

### Value
- **Type**: typing.Optional[float]


# SamplingTargetDocument

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


# Segment

### Id
- **Type**: typing.Optional[str]

### Document
- **Type**: typing.Optional[str]


# Service

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Edge]]

### SummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceStatistics]

### DurationHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.HistogramEntry]]

### ResponseTimeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.HistogramEntry]]


# ServiceId

### Name
- **Type**: typing.Optional[str]

### Names
- **Type**: typing.Optional[typing.List[str]]

### AccountId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# ServiceStatistics

### OkCount
- **Type**: typing.Optional[int]

### ErrorStatistics
- **Type**: <class 'NoneType'>

### FaultStatistics
- **Type**: <class 'NoneType'>

### TotalCount
- **Type**: typing.Optional[int]

### TotalResponseTime
- **Type**: typing.Optional[float]


# Span

### Id
- **Type**: typing.Optional[str]

### Document
- **Type**: typing.Optional[str]


# StartTraceRetrievalRequest

### TraceIds
- **Type**: typing.List[str]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# StartTraceRetrievalResult

### RetrievalToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Tag]
- **Required**: Yes


# TelemetryRecord

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
- **Type**: <class 'NoneType'>


# TimeSeriesServiceStatistics

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### EdgeSummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.EdgeStatistics]

### ServiceSummaryStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceStatistics]

### ServiceForecastStatistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ForecastStatistics]

### ResponseTimeHistogram
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.HistogramEntry]]


# Trace

### Id
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[float]

### LimitExceeded
- **Type**: typing.Optional[bool]

### Segments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.Segment]]


# TraceSummary

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
- **Type**: <class 'NoneType'>

### Annotations
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ValueWithServiceIds]]]

### Users
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.TraceUser]]

### ServiceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceId]]

### ResourceARNs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ResourceARNDetail]]

### InstanceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.InstanceIdDetail]]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.AvailabilityZoneDetail]]

### EntryPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceId]

### FaultRootCauses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.FaultRootCause]]

### ErrorRootCauses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ErrorRootCause]]

### ResponseTimeRootCauses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ResponseTimeRootCause]]

### Revision
- **Type**: typing.Optional[int]

### MatchedEventTime
- **Type**: typing.Optional[datetime.datetime]


# TraceUser

### UserName
- **Type**: typing.Optional[str]

### ServiceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceId]]


# UnprocessedStatistics

### RuleName
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# UnprocessedTraceSegment

### Id
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateGroupRequest

### GroupName
- **Type**: typing.Optional[str]

### GroupARN
- **Type**: typing.Optional[str]

### FilterExpression
- **Type**: typing.Optional[str]

### InsightsConfiguration
- **Type**: <class 'NoneType'>


# UpdateGroupResult

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIndexingRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Rule
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.IndexingRuleValueUpdate'>
- **Required**: Yes


# UpdateIndexingRuleResult

### IndexingRule
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.IndexingRule'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSamplingRuleRequest

### SamplingRuleUpdate
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRuleUpdate'>
- **Required**: Yes


# UpdateSamplingRuleResult

### SamplingRuleRecord
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.SamplingRuleRecord'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTraceSegmentDestinationRequest

### Destination
- **Type**: typing.Optional[typing.Literal['CloudWatchLogs', 'XRay']]


# UpdateTraceSegmentDestinationResult

### Destination
- **Type**: typing.Literal['CloudWatchLogs', 'XRay']
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.xray.xray_classes.ResponseMetadata'>
- **Required**: Yes


# ValueWithServiceIds

### AnnotationValue
- **Type**: <class 'NoneType'>

### ServiceIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.xray.xray_classes.ServiceId]]


