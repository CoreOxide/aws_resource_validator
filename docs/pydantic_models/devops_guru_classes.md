# devops_guru_classes

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


# AddNotificationChannelRequestRequestTypeDef

### Config
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelConfigTypeDef'>
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

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


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


# CloudFormationCollectionTypeDef

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCostEstimationResourceCollectionFilterTypeDef

### StackNames
- **Type**: typing.Optional[typing.List[str]]


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


# CostEstimationResourceCollectionFilterTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCostEstimationResourceCollectionFilterTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagCostEstimationResourceCollectionFilterTypeDef]]


# CostEstimationTimeRangeTypeDef

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteInsightRequestRequestTypeDef

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


# DescribeAccountOverviewRequestRequestTypeDef

### FromTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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


# DescribeAnomalyRequestRequestTypeDef

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


# DescribeFeedbackRequestRequestTypeDef

### InsightId
- **Type**: typing.Optional[str]


# DescribeFeedbackResponseTypeDef

### InsightFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.InsightFeedbackTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInsightRequestRequestTypeDef

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


# DescribeOrganizationHealthRequestRequestTypeDef

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


# DescribeOrganizationOverviewRequestRequestTypeDef

### FromTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# DescribeOrganizationResourceCollectionHealthRequestDescribeOrganizationResourceCollectionHealthPaginateTypeDef

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


# DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagHealthTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceCollectionHealthRequestDescribeResourceCollectionHealthPaginateTypeDef

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# DescribeResourceCollectionHealthRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagHealthTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeServiceIntegrationResponseTypeDef

### ServiceIntegration
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ServiceIntegrationConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndTimeRangeTypeDef

### FromTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# EventResourceTypeDef

### Type
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# EventSourcesConfigTypeDef

### AmazonCodeGuruProfiler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AmazonCodeGuruProfilerIntegrationTypeDef]


# EventTimeRangeTypeDef

### FromTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# EventTypeDef

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

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


# GetCostEstimationRequestGetCostEstimationPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# GetCostEstimationRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# GetCostEstimationResponseTypeDef

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.CostEstimationResourceCollectionFilterTypeDef'>
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetResourceCollectionRequestGetResourceCollectionPaginateTypeDef

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# GetResourceCollectionRequestRequestTypeDef

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourceCollectionResponseTypeDef

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionFilterTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### KMSKeyId
- **Type**: typing.Optional[str]

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_MANAGED_KEY']]


# KMSServerSideEncryptionIntegrationTypeDef

### KMSKeyId
- **Type**: typing.Optional[str]

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_MANAGED_KEY']]


# ListAnomaliesForInsightFiltersTypeDef

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionTypeDef]


# ListAnomaliesForInsightRequestListAnomaliesForInsightPaginateTypeDef

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


# ListAnomaliesForInsightRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAnomalousLogGroupsRequestListAnomalousLogGroupsPaginateTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListAnomalousLogGroupsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]


# ListEventsRequestListEventsPaginateTypeDef

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListEventsFiltersTypeDef'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListEventsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInsightsAnyStatusFilterTypeDef

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.StartTimeRangeTypeDef'>
- **Required**: Yes


# ListInsightsClosedStatusFilterTypeDef

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### EndTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.EndTimeRangeTypeDef'>
- **Required**: Yes


# ListInsightsOngoingStatusFilterTypeDef

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes


# ListInsightsRequestListInsightsPaginateTypeDef

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsStatusFilterTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListInsightsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInsightsStatusFilterTypeDef

### Ongoing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsOngoingStatusFilterTypeDef]

### Closed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsClosedStatusFilterTypeDef]

### Any
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsAnyStatusFilterTypeDef]


# ListMonitoredResourcesFiltersTypeDef

### ResourcePermission
- **Type**: typing.Literal['FULL_PERMISSION', 'MISSING_PERMISSION']
- **Required**: Yes

### ResourceTypeFilters
- **Type**: typing.Sequence[typing.Literal['CLOUDFRONT_DISTRIBUTION', 'DYNAMODB_TABLE', 'EC2_NAT_GATEWAY', 'ECS_CLUSTER', 'ECS_SERVICE', 'EKS_CLUSTER', 'ELASTICACHE_CACHE_CLUSTER', 'ELASTICSEARCH_DOMAIN', 'ELASTIC_BEANSTALK_ENVIRONMENT', 'ELASTIC_LOAD_BALANCER_LOAD_BALANCER', 'ELASTIC_LOAD_BALANCING_V2_LOAD_BALANCER', 'ELASTIC_LOAD_BALANCING_V2_TARGET_GROUP', 'KINESIS_STREAM', 'LAMBDA_FUNCTION', 'LOG_GROUPS', 'OPEN_SEARCH_SERVICE_DOMAIN', 'RDS_DB_CLUSTER', 'RDS_DB_INSTANCE', 'REDSHIFT_CLUSTER', 'ROUTE53_HEALTH_CHECK', 'ROUTE53_HOSTED_ZONE', 'S3_BUCKET', 'SAGEMAKER_ENDPOINT', 'SNS_TOPIC', 'SQS_QUEUE', 'STEP_FUNCTIONS_ACTIVITY', 'STEP_FUNCTIONS_STATE_MACHINE']]
- **Required**: Yes


# ListMonitoredResourcesRequestListMonitoredResourcesPaginateTypeDef

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ListMonitoredResourcesFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListMonitoredResourcesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNotificationChannelsRequestListNotificationChannelsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListNotificationChannelsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationChannelsResponsePaginatorTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNotificationChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrganizationInsightsRequestListOrganizationInsightsPaginateTypeDef

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ListInsightsStatusFilterTypeDef'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListOrganizationInsightsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecommendationsRequestListRecommendationsPaginateTypeDef

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### Locale
- **Type**: typing.Optional[typing.Literal['DE_DE', 'EN_GB', 'EN_US', 'ES_ES', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### AccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# ListRecommendationsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### MonitoredResourceName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### ResourcePermission
- **Type**: typing.Optional[typing.Literal['FULL_PERMISSION', 'MISSING_PERMISSION']]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]


# NotificationChannelConfigPaginatorTypeDef

### Sns
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.SnsChannelConfigTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationFilterConfigPaginatorTypeDef]


# NotificationChannelConfigTypeDef

### Sns
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.SnsChannelConfigTypeDef'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationFilterConfigTypeDef]


# NotificationChannelPaginatorTypeDef

### Id
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelConfigPaginatorTypeDef]


# NotificationChannelTypeDef

### Id
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.NotificationChannelConfigTypeDef]


# NotificationFilterConfigPaginatorTypeDef

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

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionTypeDef]


# PutFeedbackRequestRequestTypeDef

### InsightFeedback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.InsightFeedbackTypeDef]


# ReactiveAnomalySummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### AnomalyTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyTimeRangeTypeDef]

### AnomalyReportedTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyReportedTimeRangeTypeDef]

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalySourceDetailsTypeDef]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['CAUSAL', 'CONTEXTUAL']]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CausalAnomalyId
- **Type**: typing.Optional[str]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyResourceTypeDef]]


# ReactiveAnomalyTypeDef

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### AnomalyTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyTimeRangeTypeDef]

### AnomalyReportedTimeRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyReportedTimeRangeTypeDef]

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalySourceDetailsTypeDef]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['CAUSAL', 'CONTEXTUAL']]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CausalAnomalyId
- **Type**: typing.Optional[str]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.AnomalyResourceTypeDef]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionTypeDef]


# RecommendationRelatedAnomalyResourceTypeDef

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


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

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


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


# RemoveNotificationChannelRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceCollectionFilterTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCollectionFilterTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagCollectionFilterTypeDef]]


# ResourceCollectionTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.CloudFormationCollectionTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.TagCollectionTypeDef]]


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


# SearchInsightsFiltersTypeDef

### Severities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### Statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOSED', 'ONGOING']]]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionTypeDef]


# SearchInsightsRequestRequestTypeDef

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.StartTimeRangeTypeDef'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.SearchInsightsFiltersTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchInsightsRequestSearchInsightsPaginateTypeDef

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.StartTimeRangeTypeDef'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.SearchInsightsFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# SearchInsightsResponseTypeDef

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveInsightSummaryTypeDef]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveInsightSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchOrganizationInsightsFiltersTypeDef

### Severities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### Statuses
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOSED', 'ONGOING']]]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ResourceCollectionTypeDef]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceCollectionTypeDef]


# SearchOrganizationInsightsRequestRequestTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.StartTimeRangeTypeDef'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.SearchOrganizationInsightsFiltersTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchOrganizationInsightsRequestSearchOrganizationInsightsPaginateTypeDef

### AccountIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.StartTimeRangeTypeDef'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.SearchOrganizationInsightsFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.PaginatorConfigTypeDef]


# SearchOrganizationInsightsResponseTypeDef

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ProactiveInsightSummaryTypeDef]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru_classes.ReactiveInsightSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServiceCollectionTypeDef

### ServiceNames
- **Type**: typing.Optional[typing.Sequence[typing.Literal['API_GATEWAY', 'APPLICATION_ELB', 'AUTO_SCALING_GROUP', 'CLOUD_FRONT', 'DYNAMO_DB', 'EC2', 'ECS', 'EKS', 'ELASTIC_BEANSTALK', 'ELASTI_CACHE', 'ELB', 'ES', 'KINESIS', 'LAMBDA', 'NAT_GATEWAY', 'NETWORK_ELB', 'RDS', 'REDSHIFT', 'ROUTE_53', 'S3', 'SAGE_MAKER', 'SNS', 'SQS', 'STEP_FUNCTIONS', 'SWF']]]


# ServiceHealthTypeDef

### ServiceName
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'APPLICATION_ELB', 'AUTO_SCALING_GROUP', 'CLOUD_FRONT', 'DYNAMO_DB', 'EC2', 'ECS', 'EKS', 'ELASTIC_BEANSTALK', 'ELASTI_CACHE', 'ELB', 'ES', 'KINESIS', 'LAMBDA', 'NAT_GATEWAY', 'NETWORK_ELB', 'RDS', 'REDSHIFT', 'ROUTE_53', 'S3', 'SAGE_MAKER', 'SNS', 'SQS', 'STEP_FUNCTIONS', 'SWF']]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.ServiceInsightHealthTypeDef]

### AnalyzedResourceCount
- **Type**: typing.Optional[int]


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

### Type
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### Count
- **Type**: typing.Optional[int]

### UnitCost
- **Type**: typing.Optional[float]

### Cost
- **Type**: typing.Optional[float]


# SnsChannelConfigTypeDef

### TopicArn
- **Type**: typing.Optional[str]


# StartCostEstimationRequestRequestTypeDef

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru_classes.CostEstimationResourceCollectionFilterTypeDef'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StartTimeRangeTypeDef

### FromTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TagCollectionFilterTypeDef

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
- **Type**: typing.List[str]
- **Required**: Yes


# TagCostEstimationResourceCollectionFilterTypeDef

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
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


# UpdateCloudFormationCollectionFilterTypeDef

### StackNames
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateEventSourcesConfigRequestRequestTypeDef

### EventSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.EventSourcesConfigTypeDef]


# UpdateResourceCollectionFilterTypeDef

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru_classes.UpdateCloudFormationCollectionFilterTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.devops_guru_classes.UpdateTagCollectionFilterTypeDef]]


# UpdateResourceCollectionRequestRequestTypeDef

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


# UpdateServiceIntegrationRequestRequestTypeDef

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


