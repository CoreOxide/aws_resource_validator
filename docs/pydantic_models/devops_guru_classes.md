# Devops Guru Classes

# AccountHealthTypeDef

### AccountId
- **Type**: typing.Optional[str]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AccountInsightHealthTypeDef]


# AccountInsightHealthTypeDef

### OpenProactiveInsights
- **Type**: typing.Optional[int]

### OpenReactiveInsights
- **Type**: typing.Optional[int]


# AddNotificationChannelRequestTypeDef

### Config
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelConfigUnionTypeDef'>
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>


# AddNotificationChannelResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AmazonCodeGuruProfilerIntegrationTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AnomalousLogGroupTypeDef

### LogGroupName
- **Type**: typing.Optional[str]

### ImpactStartTime
- **Type**: typing.Optional[datetime.datetime]

### ImpactEndTime
- **Type**: typing.Optional[datetime.datetime]

### NumberOfLogLinesScanned
- **Type**: typing.Optional[int]

### LogAnomalyShowcases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.LogAnomalyShowcaseTypeDef]]


# AnomalyReportedTimeRangeTypeDef

### OpenTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CloseTime
- **Type**: typing.Optional[datetime.datetime]


# AnomalyResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnomalySourceDetailsTypeDef

### CloudWatchMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.CloudWatchMetricsDetailTypeDef]]

### PerformanceInsightsMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsMetricsDetailTypeDef]]


# AnomalySourceMetadataTypeDef

### Source
- **Type**: typing.Optional[str]

### SourceResourceName
- **Type**: typing.Optional[str]

### SourceResourceType
- **Type**: typing.Optional[str]


# AnomalyTimeRangeTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudFormationCollectionFilterTypeDef

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCollectionOutputTypeDef

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCollectionTypeDef

### StackNames
- **Type**: typing.Optional[typing.Sequence[str]]


# CloudFormationCollectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCostEstimationResourceCollectionFilterTypeDef

### StackNames
- **Type**: typing.Optional[typing.Sequence[str]]


# CloudFormationHealthTypeDef

### StackName
- **Type**: typing.Optional[str]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightHealthTypeDef]

### AnalyzedResourceCount
- **Type**: typing.Optional[int]


# CloudWatchMetricsDataSummaryTypeDef

### TimestampMetricValuePairList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TimestampMetricValuePairTypeDef]]

### StatusCode
- **Type**: typing.Optional[typing.Literal['Complete', 'InternalError', 'PartialData']]


# CloudWatchMetricsDetailTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.CloudWatchMetricsDimensionTypeDef]]

### Stat
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum', 'p50', 'p90', 'p99']]

### Unit
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### MetricDataSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudWatchMetricsDataSummaryTypeDef]


# CloudWatchMetricsDimensionTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# CostEstimationResourceCollectionFilterOutputTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCostEstimationResourceCollectionFilterOutputTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagCostEstimationResourceCollectionFilterOutputTypeDef]]


# CostEstimationResourceCollectionFilterTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCostEstimationResourceCollectionFilterTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devops_guru_classes.TagCostEstimationResourceCollectionFilterTypeDef]]


# CostEstimationResourceCollectionFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CostEstimationTimeRangeTypeDef

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteInsightRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountHealthResponseTypeDef

### OpenReactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### OpenProactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### MetricsAnalyzed
- **Type**: <class 'int'>
- **Required**: Yes

### ResourceHours
- **Type**: <class 'int'>
- **Required**: Yes

### AnalyzedResourceCount
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountOverviewRequestTypeDef

### FromTime
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef'>
- **Required**: Yes

### ToTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef]


# DescribeAccountOverviewResponseTypeDef

### ReactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### ProactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### MeanTimeToRecoverInMilliseconds
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAnomalyRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeAnomalyResponseTypeDef

### ProactiveAnomaly
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveAnomalyTypeDef'>
- **Required**: Yes

### ReactiveAnomaly
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveAnomalyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventSourcesConfigResponseTypeDef

### EventSources
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.EventSourcesConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFeedbackRequestTypeDef

### InsightId
- **Type**: typing.Optional[str]


# DescribeFeedbackResponseTypeDef

### InsightFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.InsightFeedbackTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInsightRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeInsightResponseTypeDef

### ProactiveInsight
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveInsightTypeDef'>
- **Required**: Yes

### ReactiveInsight
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveInsightTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationHealthRequestTypeDef

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeOrganizationHealthResponseTypeDef

### OpenReactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### OpenProactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### MetricsAnalyzed
- **Type**: <class 'int'>
- **Required**: Yes

### ResourceHours
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationOverviewRequestTypeDef

### FromTime
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef'>
- **Required**: Yes

### ToTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeOrganizationOverviewResponseTypeDef

### ReactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### ProactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationResourceCollectionHealthRequestPaginateTypeDef

### OrganizationResourceCollectionType
- **Type**: typing.Literal['AWS_ACCOUNT', 'AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# DescribeOrganizationResourceCollectionHealthRequestTypeDef

### OrganizationResourceCollectionType
- **Type**: typing.Literal['AWS_ACCOUNT', 'AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeOrganizationResourceCollectionHealthResponseTypeDef

### CloudFormation
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationHealthTypeDef]
- **Required**: Yes

### Service
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceHealthTypeDef]
- **Required**: Yes

### Account
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.AccountHealthTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagHealthTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeResourceCollectionHealthRequestPaginateTypeDef

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# DescribeResourceCollectionHealthRequestTypeDef

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeResourceCollectionHealthResponseTypeDef

### CloudFormation
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationHealthTypeDef]
- **Required**: Yes

### Service
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceHealthTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagHealthTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceIntegrationResponseTypeDef

### ServiceIntegration
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ServiceIntegrationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndTimeRangeTypeDef

### FromTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef]

### ToTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef]


# EventResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EventSourcesConfigTypeDef

### AmazonCodeGuruProfiler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AmazonCodeGuruProfilerIntegrationTypeDef]


# EventTimeRangeTypeDef

### FromTime
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef'>
- **Required**: Yes

### ToTime
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef'>
- **Required**: Yes


# EventTypeDef

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### Id
- **Type**: typing.Optional[str]

### Time
- **Type**: typing.Optional[datetime.datetime]

### EventSource
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### DataSource
- **Type**: typing.Optional[typing.Literal['AWS_CLOUD_TRAIL', 'AWS_CODE_DEPLOY']]

### EventClass
- **Type**: typing.Optional[typing.Literal['CONFIG_CHANGE', 'DEPLOYMENT', 'INFRASTRUCTURE', 'SCHEMA_CHANGE', 'SECURITY_CHANGE']]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.EventResourceTypeDef]]


# GetCostEstimationRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# GetCostEstimationRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetCostEstimationResponseTypeDef

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.CostEstimationResourceCollectionFilterOutputTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'ONGOING']
- **Required**: Yes

### Costs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceResourceCostTypeDef]
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.CostEstimationTimeRangeTypeDef'>
- **Required**: Yes

### TotalCost
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourceCollectionRequestPaginateTypeDef

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# GetResourceCollectionRequestTypeDef

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourceCollectionResponseTypeDef

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionFilterTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# InsightFeedbackTypeDef

### Id
- **Type**: typing.Optional[str]

### Feedback
- **Type**: typing.Optional[typing.Literal['ALERT_TOO_SENSITIVE', 'DATA_INCORRECT', 'DATA_NOISY_ANOMALY', 'RECOMMENDATION_USEFUL', 'VALID_COLLECTION']]


# InsightHealthTypeDef

### OpenProactiveInsights
- **Type**: typing.Optional[int]

### OpenReactiveInsights
- **Type**: typing.Optional[int]

### MeanTimeToRecoverInMilliseconds
- **Type**: typing.Optional[int]


# InsightTimeRangeTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# KMSServerSideEncryptionIntegrationConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KMSServerSideEncryptionIntegrationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListAnomaliesForInsightFiltersTypeDef

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionUnionTypeDef]


# ListAnomaliesForInsightRequestPaginateTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.StartTimeRangeTypeDef]

### AccountId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListAnomaliesForInsightFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListAnomaliesForInsightRequestTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.StartTimeRangeTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListAnomaliesForInsightFiltersTypeDef]


# ListAnomaliesForInsightResponseTypeDef

### ProactiveAnomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveAnomalySummaryTypeDef]
- **Required**: Yes

### ReactiveAnomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveAnomalySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalousLogGroupsRequestPaginateTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListAnomalousLogGroupsRequestTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalousLogGroupsResponseTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalousLogGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalousLogGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventsFiltersTypeDef

### InsightId
- **Type**: typing.Optional[str]

### EventTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.EventTimeRangeTypeDef]

### EventClass
- **Type**: typing.Optional[typing.Literal['CONFIG_CHANGE', 'DEPLOYMENT', 'INFRASTRUCTURE', 'SCHEMA_CHANGE', 'SECURITY_CHANGE']]

### EventSource
- **Type**: typing.Optional[str]

### DataSource
- **Type**: typing.Optional[typing.Literal['AWS_CLOUD_TRAIL', 'AWS_CODE_DEPLOY']]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionUnionTypeDef]


# ListEventsRequestPaginateTypeDef

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListEventsFiltersTypeDef'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListEventsRequestTypeDef

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListEventsFiltersTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListEventsResponseTypeDef

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsRequestPaginateTypeDef

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsStatusFilterTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListInsightsRequestTypeDef

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsStatusFilterTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsResponseTypeDef

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveInsightSummaryTypeDef]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveInsightSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsStatusFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListMonitoredResourcesFiltersTypeDef

### ResourcePermission
- **Type**: typing.Literal['FULL_PERMISSION', 'MISSING_PERMISSION']
- **Required**: Yes

### ResourceTypeFilters
- **Type**: typing.Sequence[typing.Literal['CLOUDFRONT_DISTRIBUTION', 'DYNAMODB_TABLE', 'EC2_NAT_GATEWAY', 'ECS_CLUSTER', 'ECS_SERVICE', 'EKS_CLUSTER', 'ELASTICACHE_CACHE_CLUSTER', 'ELASTICSEARCH_DOMAIN', 'ELASTIC_BEANSTALK_ENVIRONMENT', 'ELASTIC_LOAD_BALANCER_LOAD_BALANCER', 'ELASTIC_LOAD_BALANCING_V2_LOAD_BALANCER', 'ELASTIC_LOAD_BALANCING_V2_TARGET_GROUP', 'KINESIS_STREAM', 'LAMBDA_FUNCTION', 'LOG_GROUPS', 'OPEN_SEARCH_SERVICE_DOMAIN', 'RDS_DB_CLUSTER', 'RDS_DB_INSTANCE', 'REDSHIFT_CLUSTER', 'ROUTE53_HEALTH_CHECK', 'ROUTE53_HOSTED_ZONE', 'S3_BUCKET', 'SAGEMAKER_ENDPOINT', 'SNS_TOPIC', 'SQS_QUEUE', 'STEP_FUNCTIONS_ACTIVITY', 'STEP_FUNCTIONS_STATE_MACHINE']]
- **Required**: Yes


# ListMonitoredResourcesRequestPaginateTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListMonitoredResourcesFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListMonitoredResourcesRequestTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListMonitoredResourcesFiltersTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoredResourcesResponseTypeDef

### MonitoredResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.MonitoredResourceIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationChannelsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListNotificationChannelsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationInsightsRequestPaginateTypeDef

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsStatusFilterTypeDef'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListOrganizationInsightsRequestTypeDef

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsStatusFilterTypeDef'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationInsightsResponseTypeDef

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveOrganizationInsightSummaryTypeDef]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveOrganizationInsightSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecommendationsRequestPaginateTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### Locale
- **Type**: typing.Optional[typing.Literal['DE_DE', 'EN_GB', 'EN_US', 'ES_ES', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### AccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListRecommendationsRequestTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[typing.Literal['DE_DE', 'EN_GB', 'EN_US', 'ES_ES', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### AccountId
- **Type**: typing.Optional[str]


# ListRecommendationsResponseTypeDef

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.RecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogAnomalyClassTypeDef

### LogStreamName
- **Type**: typing.Optional[str]

### LogAnomalyType
- **Type**: typing.Optional[typing.Literal['BLOCK_FORMAT', 'FORMAT', 'HTTP_CODE', 'KEYWORD', 'KEYWORD_TOKEN', 'NEW_FIELD_NAME', 'NUMERICAL_NAN', 'NUMERICAL_POINT']]

### LogAnomalyToken
- **Type**: typing.Optional[str]

### LogEventId
- **Type**: typing.Optional[str]

### Explanation
- **Type**: typing.Optional[str]

### NumberOfLogLinesOccurrences
- **Type**: typing.Optional[int]

### LogEventTimestamp
- **Type**: typing.Optional[datetime.datetime]


# LogAnomalyShowcaseTypeDef

### LogAnomalyClasses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.LogAnomalyClassTypeDef]]


# LogsAnomalyDetectionIntegrationConfigTypeDef

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# LogsAnomalyDetectionIntegrationTypeDef

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MonitoredResourceIdentifierTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationChannelConfigOutputTypeDef

### Sns
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.SnsChannelConfigTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationFilterConfigOutputTypeDef]


# NotificationChannelConfigTypeDef

### Sns
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.SnsChannelConfigTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationFilterConfigTypeDef]


# NotificationChannelConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationChannelTypeDef

### Id
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelConfigOutputTypeDef]


# NotificationFilterConfigOutputTypeDef

### Severities
- **Type**: typing.Optional[typing.List[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### MessageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED_INSIGHT', 'NEW_ASSOCIATION', 'NEW_INSIGHT', 'NEW_RECOMMENDATION', 'SEVERITY_UPGRADED']]]


# NotificationFilterConfigTypeDef

### Severities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### MessageTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOSED_INSIGHT', 'NEW_ASSOCIATION', 'NEW_INSIGHT', 'NEW_RECOMMENDATION', 'SEVERITY_UPGRADED']]]


# OpsCenterIntegrationConfigTypeDef

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# OpsCenterIntegrationTypeDef

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceInsightsMetricDimensionGroupTypeDef

### Group
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]


# PerformanceInsightsMetricQueryTypeDef

### Metric
- **Type**: typing.Optional[str]

### GroupBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsMetricDimensionGroupTypeDef]

### Filter
- **Type**: typing.Optional[typing.Dict[str, str]]


# PerformanceInsightsMetricsDetailTypeDef

### MetricDisplayName
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]

### MetricQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsMetricQueryTypeDef]

### ReferenceData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsReferenceDataTypeDef]]

### StatsAtAnomaly
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsStatTypeDef]]

### StatsAtBaseline
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsStatTypeDef]]


# PerformanceInsightsReferenceComparisonValuesTypeDef

### ReferenceScalar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsReferenceScalarTypeDef]

### ReferenceMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsReferenceMetricTypeDef]


# PerformanceInsightsReferenceDataTypeDef

### Name
- **Type**: typing.Optional[str]

### ComparisonValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsReferenceComparisonValuesTypeDef]


# PerformanceInsightsReferenceMetricTypeDef

### MetricQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PerformanceInsightsMetricQueryTypeDef]


# PerformanceInsightsReferenceScalarTypeDef

### Value
- **Type**: typing.Optional[float]


# PerformanceInsightsStatTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PredictionTimeRangeTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# ProactiveAnomalySummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### AnomalyTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyTimeRangeTypeDef]

### AnomalyReportedTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyReportedTimeRangeTypeDef]

### PredictionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PredictionTimeRangeTypeDef]

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalySourceDetailsTypeDef]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### Limit
- **Type**: typing.Optional[float]

### SourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalySourceMetadataTypeDef]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyResourceTypeDef]]

### Description
- **Type**: typing.Optional[str]


# ProactiveAnomalyTypeDef

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### AnomalyTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyTimeRangeTypeDef]

### AnomalyReportedTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyReportedTimeRangeTypeDef]

### PredictionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PredictionTimeRangeTypeDef]

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalySourceDetailsTypeDef]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### Limit
- **Type**: typing.Optional[float]

### SourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalySourceMetadataTypeDef]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyResourceTypeDef]]

### Description
- **Type**: typing.Optional[str]


# ProactiveInsightSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightTimeRangeTypeDef]

### PredictionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PredictionTimeRangeTypeDef]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionOutputTypeDef]

### AssociatedResourceArns
- **Type**: typing.Optional[typing.List[str]]


# ProactiveInsightTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightTimeRangeTypeDef]

### PredictionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PredictionTimeRangeTypeDef]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### SsmOpsItemId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ProactiveOrganizationInsightSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightTimeRangeTypeDef]

### PredictionTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PredictionTimeRangeTypeDef]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionOutputTypeDef]


# PutFeedbackRequestTypeDef

### InsightFeedback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightFeedbackTypeDef]


# ReactiveAnomalySummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReactiveAnomalyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReactiveInsightSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightTimeRangeTypeDef]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionOutputTypeDef]

### AssociatedResourceArns
- **Type**: typing.Optional[typing.List[str]]


# ReactiveInsightTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightTimeRangeTypeDef]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### SsmOpsItemId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ReactiveOrganizationInsightSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### OrganizationalUnitId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightTimeRangeTypeDef]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionOutputTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionOutputTypeDef]


# RecommendationRelatedAnomalyResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationRelatedAnomalySourceDetailTypeDef

### CloudWatchMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef]]


# RecommendationRelatedAnomalyTypeDef

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.RecommendationRelatedAnomalyResourceTypeDef]]

### SourceDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.RecommendationRelatedAnomalySourceDetailTypeDef]]

### AnomalyId
- **Type**: typing.Optional[str]


# RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# RecommendationRelatedEventResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationRelatedEventTypeDef

### Name
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.RecommendationRelatedEventResourceTypeDef]]


# RecommendationTypeDef

### Description
- **Type**: typing.Optional[str]

### Link
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]

### RelatedEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.RecommendationRelatedEventTypeDef]]

### RelatedAnomalies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.RecommendationRelatedAnomalyTypeDef]]

### Category
- **Type**: typing.Optional[str]


# RemoveNotificationChannelRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceCollectionFilterTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCollectionFilterTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagCollectionFilterTypeDef]]


# ResourceCollectionOutputTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCollectionOutputTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagCollectionOutputTypeDef]]


# ResourceCollectionTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCollectionUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devops_guru_classes.TagCollectionUnionTypeDef]]


# ResourceCollectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# SearchInsightsFiltersTypeDef

### Severities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### Statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOSED', 'ONGOING']]]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionUnionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionUnionTypeDef]


# SearchInsightsResponseTypeDef

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveInsightSummaryTypeDef]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveInsightSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchOrganizationInsightsFiltersTypeDef

### Severities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### Statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOSED', 'ONGOING']]]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionUnionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionUnionTypeDef]


# SearchOrganizationInsightsResponseTypeDef

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveInsightSummaryTypeDef]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveInsightSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ServiceCollectionOutputTypeDef

### ServiceNames
- **Type**: typing.Optional[typing.List[typing.Literal['API_GATEWAY', 'APPLICATION_ELB', 'AUTO_SCALING_GROUP', 'CLOUD_FRONT', 'DYNAMO_DB', 'EC2', 'ECS', 'EKS', 'ELASTIC_BEANSTALK', 'ELASTI_CACHE', 'ELB', 'ES', 'KINESIS', 'LAMBDA', 'NAT_GATEWAY', 'NETWORK_ELB', 'RDS', 'REDSHIFT', 'ROUTE_53', 'S3', 'SAGE_MAKER', 'SNS', 'SQS', 'STEP_FUNCTIONS', 'SWF']]]


# ServiceCollectionTypeDef

### ServiceNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['API_GATEWAY', 'APPLICATION_ELB', 'AUTO_SCALING_GROUP', 'CLOUD_FRONT', 'DYNAMO_DB', 'EC2', 'ECS', 'EKS', 'ELASTIC_BEANSTALK', 'ELASTI_CACHE', 'ELB', 'ES', 'KINESIS', 'LAMBDA', 'NAT_GATEWAY', 'NETWORK_ELB', 'RDS', 'REDSHIFT', 'ROUTE_53', 'S3', 'SAGE_MAKER', 'SNS', 'SQS', 'STEP_FUNCTIONS', 'SWF']]]


# ServiceCollectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceHealthTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceInsightHealthTypeDef

### OpenProactiveInsights
- **Type**: typing.Optional[int]

### OpenReactiveInsights
- **Type**: typing.Optional[int]


# ServiceIntegrationConfigTypeDef

### OpsCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.OpsCenterIntegrationTypeDef]

### LogsAnomalyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.LogsAnomalyDetectionIntegrationTypeDef]

### KMSServerSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.KMSServerSideEncryptionIntegrationTypeDef]


# ServiceResourceCostTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnsChannelConfigTypeDef

### TopicArn
- **Type**: typing.Optional[str]


# StartCostEstimationRequestTypeDef

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.CostEstimationResourceCollectionFilterUnionTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StartTimeRangeTypeDef

### FromTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef]

### ToTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.TimestampTypeDef]


# TagCollectionFilterTypeDef

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagCollectionOutputTypeDef

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagCollectionTypeDef

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TagCollectionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagCostEstimationResourceCollectionFilterOutputTypeDef

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagCostEstimationResourceCollectionFilterTypeDef

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TagHealthTypeDef

### AppBoundaryKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightHealthTypeDef]

### AnalyzedResourceCount
- **Type**: typing.Optional[int]


# TimestampMetricValuePairTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### MetricValue
- **Type**: typing.Optional[float]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateCloudFormationCollectionFilterTypeDef

### StackNames
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateEventSourcesConfigRequestTypeDef

### EventSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.EventSourcesConfigTypeDef]


# UpdateResourceCollectionFilterTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.UpdateCloudFormationCollectionFilterTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devops_guru_classes.UpdateTagCollectionFilterTypeDef]]


# UpdateResourceCollectionRequestTypeDef

### Action
- **Type**: typing.Literal['ADD', 'REMOVE']
- **Required**: Yes

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.UpdateResourceCollectionFilterTypeDef'>
- **Required**: Yes


# UpdateServiceIntegrationConfigTypeDef

### OpsCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.OpsCenterIntegrationConfigTypeDef]

### LogsAnomalyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.LogsAnomalyDetectionIntegrationConfigTypeDef]

### KMSServerSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.KMSServerSideEncryptionIntegrationConfigTypeDef]


# UpdateServiceIntegrationRequestTypeDef

### ServiceIntegration
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.UpdateServiceIntegrationConfigTypeDef'>
- **Required**: Yes


# UpdateTagCollectionFilterTypeDef

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.Sequence[str]
- **Required**: Yes


