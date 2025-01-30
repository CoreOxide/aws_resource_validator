# pi_classes

# AnalysisReportSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi_classes.TagTypeDef]]


# AnalysisReportTypeDef

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
- **Type**: typing.Optional[typing.List[ForwardRef('InsightTypeDef')]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreatePerformanceAnalysisReportRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.pi_classes.TagTypeDef]]


# CreatePerformanceAnalysisReportResponseTypeDef

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataPointTypeDef

### Timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Value
- **Type**: <class 'float'>
- **Required**: Yes


# DataTypeDef

### PerformanceInsightsMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pi_classes.PerformanceInsightsMetricTypeDef]


# DeletePerformanceAnalysisReportRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### AnalysisReportId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDimensionKeysRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.DimensionGroupTypeDef'>
- **Required**: Yes

### PeriodInSeconds
- **Type**: typing.Optional[int]

### AdditionalMetrics
- **Type**: typing.Optional[typing.Sequence[str]]

### PartitionBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pi_classes.DimensionGroupTypeDef]

### Filter
- **Type**: typing.Optional[typing.Mapping[str, str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDimensionKeysResponseTypeDef

### AlignedStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AlignedEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PartitionKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.ResponsePartitionKeyTypeDef]
- **Required**: Yes

### Keys
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.DimensionKeyDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DimensionDetailTypeDef

### Identifier
- **Type**: typing.Optional[str]


# DimensionGroupDetailTypeDef

### Group
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi_classes.DimensionDetailTypeDef]]


# DimensionGroupTypeDef

### Group
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]


# DimensionKeyDescriptionTypeDef

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### Total
- **Type**: typing.Optional[float]

### AdditionalMetrics
- **Type**: typing.Optional[typing.Dict[str, float]]

### Partitions
- **Type**: typing.Optional[typing.List[float]]


# DimensionKeyDetailTypeDef

### Value
- **Type**: typing.Optional[str]

### Dimension
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'PROCESSING', 'UNAVAILABLE']]


# FeatureMetadataTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'DISABLED_PENDING_REBOOT', 'ENABLED', 'ENABLED_PENDING_REBOOT', 'UNKNOWN', 'UNSUPPORTED']]


# GetDimensionKeyDetailsRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]


# GetDimensionKeyDetailsResponseTypeDef

### Dimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.DimensionKeyDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPerformanceAnalysisReportRequestRequestTypeDef

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


# GetPerformanceAnalysisReportResponseTypeDef

### AnalysisReport
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.AnalysisReportTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceMetadataRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetResourceMetadataResponseTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Features
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.pi_classes.FeatureMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceMetricsRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MetricQueries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pi_classes.MetricQueryTypeDef]
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


# GetResourceMetricsResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.MetricKeyDataPointsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# InsightTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi_classes.RecommendationTypeDef]]

### InsightData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi_classes.DataTypeDef]]

### BaselineData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi_classes.DataTypeDef]]


# ListAvailableResourceDimensionsRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Metrics
- **Type**: typing.Sequence[str]
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AuthorizedActions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DescribeDimensionKeys', 'GetDimensionKeyDetails', 'GetResourceMetrics']]]


# ListAvailableResourceDimensionsResponseTypeDef

### MetricDimensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.MetricDimensionGroupsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAvailableResourceMetricsRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### MetricTypes
- **Type**: typing.Sequence[str]
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAvailableResourceMetricsResponseTypeDef

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.ResponseResourceMetricTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPerformanceAnalysisReportsRequestRequestTypeDef

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


# ListPerformanceAnalysisReportsResponseTypeDef

### AnalysisReports
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.AnalysisReportSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.pi_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.pi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MetricDimensionGroupsTypeDef

### Metric
- **Type**: typing.Optional[str]

### Groups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi_classes.DimensionGroupDetailTypeDef]]


# MetricKeyDataPointsTypeDef

### Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pi_classes.ResponseResourceMetricKeyTypeDef]

### DataPoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.pi_classes.DataPointTypeDef]]


# MetricQueryTypeDef

### Metric
- **Type**: <class 'str'>
- **Required**: Yes

### GroupBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.pi_classes.DimensionGroupTypeDef]

### Filter
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PerformanceInsightsMetricTypeDef

### Metric
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]

### Value
- **Type**: typing.Optional[float]


# RecommendationTypeDef

### RecommendationId
- **Type**: typing.Optional[str]

### RecommendationDescription
- **Type**: typing.Optional[str]


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


# ResponsePartitionKeyTypeDef

### Dimensions
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ResponseResourceMetricKeyTypeDef

### Metric
- **Type**: <class 'str'>
- **Required**: Yes

### Dimensions
- **Type**: typing.Optional[typing.Dict[str, str]]


# ResponseResourceMetricTypeDef

### Metric
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.pi_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ServiceType
- **Type**: typing.Literal['DOCDB', 'RDS']
- **Required**: Yes

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


