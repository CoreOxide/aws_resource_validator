# Pi Pi Classes

# AnalysisReport

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: typing.Optional[str]

### ServiceType
- **Type**: typing.Optional[typing.Literal['DOCDB', 'RDS']]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'SUCCEEDED']]

### Insights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Insight]]


# AnalysisReportSummary

### AnalysisReportId
- **Type**: typing.Optional[str]

### CreateTime
- **Type**: typing.Optional[datetime.datetime]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'RUNNING', 'SUCCEEDED']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Tag]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreatePerformanceAnalysisReportRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Tag]]


# CreatePerformanceAnalysisReportResponse

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes


# Data

### PerformanceInsightsMetric
- **Type**: <class 'NoneType'>


# DataPoint

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# DeletePerformanceAnalysisReportRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDimensionKeysRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### Metric
- **Type**: <class 'str'>
- **Required**: Yes

### GroupBy
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.DimensionGroup'>
- **Required**: Yes

### PeriodInSeconds
- **Type**: typing.Optional[int]

### AdditionalMetrics
- **Type**: typing.Optional[typing.List[str]]

### PartitionBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pi.pi_classes.DimensionGroup]

### Filter
- **Type**: typing.Optional[typing.Dict[str, str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDimensionKeysResponse

### AlignedStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlignedEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.ResponsePartitionKey]
- **Required**: Yes

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.DimensionKeyDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DimensionDetail

### Identifier
- **Type**: typing.Optional[str]


# DimensionGroup

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]


# DimensionGroupDetail

### Group
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.DimensionDetail]]


# DimensionKeyDescription

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### Total
- **Type**: typing.Optional[float]

### AdditionalMetrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### Partitions
- **Type**: typing.Optional[typing.List[float]]


# DimensionKeyDetail

### Value
- **Type**: typing.Optional[str]

### Dimension
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PROCESSING', 'UNAVAILABLE']]


# FeatureMetadata

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLED_PENDING_REBOOT', 'ENABLED', 'ENABLED_PENDING_REBOOT', 'UNKNOWN', 'UNSUPPORTED']]


# GetDimensionKeyDetailsRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### GroupIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### RequestedDimensions
- **Type**: typing.Optional[typing.List[str]]


# GetDimensionKeyDetailsResponse

### Dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.DimensionKeyDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes


# GetPerformanceAnalysisReportRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### TextFormat
- **Type**: typing.Optional[typing.Literal['MARKDOWN', 'PLAIN_TEXT']]

### AcceptLanguage
- **Type**: typing.Optional[typing.Literal['EN_US']]


# GetPerformanceAnalysisReportResponse

### AnalysisReport
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.AnalysisReport'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceMetadataRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceMetadataResponse

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Features
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pi.pi_classes.FeatureMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes


# GetResourceMetricsRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MetricQueries
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.MetricQuery]
- **Required**: Yes

### StartTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### PeriodInSeconds
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PeriodAlignment
- **Type**: typing.Optional[typing.Literal['END_TIME', 'START_TIME']]


# GetResourceMetricsResponse

### AlignedStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlignedEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MetricList
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.MetricKeyDataPoints]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Insight

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### InsightType
- **Type**: typing.Optional[str]

### Context
- **Type**: typing.Optional[typing.Literal['CAUSAL', 'CONTEXTUAL']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### SupportingInsights
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### Description
- **Type**: typing.Optional[str]

### Recommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Recommendation]]

### InsightData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Data]]

### BaselineData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Data]]


# ListAvailableResourceDimensionsRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.List[str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AuthorizedActions
- **Type**: typing.Optional[typing.List[typing.Literal['DescribeDimensionKeys', 'GetDimensionKeyDetails', 'GetResourceMetrics']]]


# ListAvailableResourceDimensionsResponse

### MetricDimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.MetricDimensionGroups]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAvailableResourceMetricsRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MetricTypes
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAvailableResourceMetricsResponse

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.ResponseResourceMetric]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPerformanceAnalysisReportsRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### ListTags
- **Type**: typing.Optional[bool]


# ListPerformanceAnalysisReportsResponse

### AnalysisReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.AnalysisReportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi.pi_classes.ResponseMetadata'>
- **Required**: Yes


# MetricDimensionGroups

### Metric
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.DimensionGroupDetail]]


# MetricKeyDataPoints

### Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pi.pi_classes.ResponseResourceMetricKey]

### DataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.DataPoint]]


# MetricQuery

### Metric
- **Type**: <class 'str'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pi.pi_classes.DimensionGroup]

### Filter
- **Type**: typing.Optional[typing.Dict[str, str]]


# PerformanceInsightsMetric

### Metric
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### Filter
- **Type**: typing.Optional[typing.Dict[str, str]]

### Value
- **Type**: typing.Optional[float]


# Recommendation

### RecommendationId
- **Type**: typing.Optional[str]

### RecommendationDescription
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


# ResponsePartitionKey

### Dimensions
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ResponseResourceMetric

### Metric
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# ResponseResourceMetricKey

### Metric
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi.pi_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


