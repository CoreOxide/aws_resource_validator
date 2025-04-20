# Devops Guru Devops Guru Classes

# AccountHealth

### AccountId
- **Type**: typing.Optional[str]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AccountInsightHealth]


# AccountInsightHealth

### OpenProactiveInsights
- **Type**: typing.Optional[int]

### OpenReactiveInsights
- **Type**: typing.Optional[int]


# AddNotificationChannelRequest

### Config
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.NotificationChannelConfig, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.NotificationChannelConfigOutput]
- **Default**: <class 'aws_resource_validator.pydantic_models.base_validator_model.BaseValidatorModel.Config'>


# AddNotificationChannelResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# AmazonCodeGuruProfilerIntegration

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AnomalousLogGroup

### LogGroupName
- **Type**: typing.Optional[str]

### ImpactStartTime
- **Type**: typing.Optional[datetime.datetime]

### ImpactEndTime
- **Type**: typing.Optional[datetime.datetime]

### NumberOfLogLinesScanned
- **Type**: typing.Optional[int]

### LogAnomalyShowcases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.LogAnomalyShowcase]]


# AnomalyReportedTimeRange

### OpenTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CloseTime
- **Type**: typing.Optional[datetime.datetime]


# AnomalyResource

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# AnomalySourceDetails

### CloudWatchMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudWatchMetricsDetail]]

### PerformanceInsightsMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsMetricsDetail]]


# AnomalySourceMetadata

### Source
- **Type**: typing.Optional[str]

### SourceResourceName
- **Type**: typing.Optional[str]

### SourceResourceType
- **Type**: typing.Optional[str]


# AnomalyTimeRange

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudFormationCollection

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCollectionFilter

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCollectionOutput

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCostEstimationResourceCollectionFilter

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationCostEstimationResourceCollectionFilterOutput

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# CloudFormationHealth

### StackName
- **Type**: typing.Optional[str]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.InsightHealth]

### AnalyzedResourceCount
- **Type**: typing.Optional[int]


# CloudWatchMetricsDataSummary

### TimestampMetricValuePairList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TimestampMetricValuePair]]

### StatusCode
- **Type**: typing.Optional[typing.Literal['Complete', 'InternalError', 'PartialData']]


# CloudWatchMetricsDetail

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudWatchMetricsDimension]]

### Stat
- **Type**: typing.Optional[typing.Literal['Average', 'Maximum', 'Minimum', 'SampleCount', 'Sum', 'p50', 'p90', 'p99']]

### Unit
- **Type**: typing.Optional[str]

### Period
- **Type**: typing.Optional[int]

### MetricDataSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudWatchMetricsDataSummary]


# CloudWatchMetricsDimension

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# CostEstimationResourceCollectionFilter

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationCostEstimationResourceCollectionFilter]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagCostEstimationResourceCollectionFilter]]


# CostEstimationResourceCollectionFilterOutput

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationCostEstimationResourceCollectionFilterOutput]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagCostEstimationResourceCollectionFilterOutput]]


# CostEstimationTimeRange

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# DeleteInsightRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountHealthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountOverviewRequest

### FromTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DescribeAccountOverviewResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAnomalyRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeAnomalyResponse

### ProactiveAnomaly
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ProactiveAnomaly'>
- **Required**: Yes

### ReactiveAnomaly
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ReactiveAnomaly'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventSourcesConfigResponse

### EventSources
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.EventSourcesConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFeedbackRequest

### InsightId
- **Type**: typing.Optional[str]


# DescribeFeedbackResponse

### InsightFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.InsightFeedback'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInsightRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeInsightResponse

### ProactiveInsight
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ProactiveInsight'>
- **Required**: Yes

### ReactiveInsight
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ReactiveInsight'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationHealthRequest

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeOrganizationHealthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationOverviewRequest

### FromTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]


# DescribeOrganizationOverviewResponse

### ReactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### ProactiveInsights
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationResourceCollectionHealthRequest

### OrganizationResourceCollectionType
- **Type**: typing.Literal['AWS_ACCOUNT', 'AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeOrganizationResourceCollectionHealthRequestPaginate

### OrganizationResourceCollectionType
- **Type**: typing.Literal['AWS_ACCOUNT', 'AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# DescribeOrganizationResourceCollectionHealthResponse

### CloudFormation
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationHealth]
- **Required**: Yes

### Service
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceHealth]
- **Required**: Yes

### Account
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AccountHealth]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagHealth]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeResourceCollectionHealthRequest

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeResourceCollectionHealthRequestPaginate

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# DescribeResourceCollectionHealthResponse

### CloudFormation
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationHealth]
- **Required**: Yes

### Service
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceHealth]
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagHealth]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeServiceIntegrationResponse

### ServiceIntegration
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceIntegrationConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes


# EndTimeRange

### FromTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# Event

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.EventResource]]


# EventResource

### Type
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


# EventSourcesConfig

### AmazonCodeGuruProfiler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AmazonCodeGuruProfilerIntegration]


# EventTimeRange

### FromTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### ToTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# GetCostEstimationRequest

### NextToken
- **Type**: typing.Optional[str]


# GetCostEstimationRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# GetCostEstimationResponse

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CostEstimationResourceCollectionFilterOutput'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'ONGOING']
- **Required**: Yes

### Costs
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceResourceCost]
- **Required**: Yes

### TimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CostEstimationTimeRange'>
- **Required**: Yes

### TotalCost
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourceCollectionRequest

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetResourceCollectionRequestPaginate

### ResourceCollectionType
- **Type**: typing.Literal['AWS_CLOUD_FORMATION', 'AWS_SERVICE', 'AWS_TAGS']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# GetResourceCollectionResponse

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionFilter'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# InsightFeedback

### Id
- **Type**: typing.Optional[str]

### Feedback
- **Type**: typing.Optional[typing.Literal['ALERT_TOO_SENSITIVE', 'DATA_INCORRECT', 'DATA_NOISY_ANOMALY', 'RECOMMENDATION_USEFUL', 'VALID_COLLECTION']]


# InsightHealth

### OpenProactiveInsights
- **Type**: typing.Optional[int]

### OpenReactiveInsights
- **Type**: typing.Optional[int]

### MeanTimeToRecoverInMilliseconds
- **Type**: typing.Optional[int]


# InsightTimeRange

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# KMSServerSideEncryptionIntegration

### KMSKeyId
- **Type**: typing.Optional[str]

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_MANAGED_KEY']]


# KMSServerSideEncryptionIntegrationConfig

### KMSKeyId
- **Type**: typing.Optional[str]

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Type
- **Type**: typing.Optional[typing.Literal['AWS_OWNED_KMS_KEY', 'CUSTOMER_MANAGED_KEY']]


# ListAnomaliesForInsightFilters

### ServiceCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollectionOutput, NoneType]


# ListAnomaliesForInsightRequest

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'NoneType'>

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListAnomaliesForInsightFilters]


# ListAnomaliesForInsightRequestPaginate

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'NoneType'>

### AccountId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListAnomaliesForInsightFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListAnomaliesForInsightResponse

### ProactiveAnomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ProactiveAnomalySummary]
- **Required**: Yes

### ReactiveAnomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ReactiveAnomalySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalousLogGroupsRequest

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAnomalousLogGroupsRequestPaginate

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListAnomalousLogGroupsResponse

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### AnomalousLogGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalousLogGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListEventsFilters

### InsightId
- **Type**: typing.Optional[str]

### EventTimeRange
- **Type**: <class 'NoneType'>

### EventClass
- **Type**: typing.Optional[typing.Literal['CONFIG_CHANGE', 'DEPLOYMENT', 'INFRASTRUCTURE', 'SCHEMA_CHANGE', 'SECURITY_CHANGE']]

### EventSource
- **Type**: typing.Optional[str]

### DataSource
- **Type**: typing.Optional[typing.Literal['AWS_CLOUD_TRAIL', 'AWS_CODE_DEPLOY']]

### ResourceCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput, NoneType]


# ListEventsRequest

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListEventsFilters'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListEventsRequestPaginate

### Filters
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListEventsFilters'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListEventsResponse

### Events
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsAnyStatusFilter

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.StartTimeRange'>
- **Required**: Yes


# ListInsightsClosedStatusFilter

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### EndTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.EndTimeRange'>
- **Required**: Yes


# ListInsightsOngoingStatusFilter

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes


# ListInsightsRequest

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListInsightsStatusFilter'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsRequestPaginate

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListInsightsStatusFilter'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListInsightsResponse

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ProactiveInsightSummary]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ReactiveInsightSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInsightsStatusFilter

### Ongoing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListInsightsOngoingStatusFilter]

### Closed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListInsightsClosedStatusFilter]

### Any
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListInsightsAnyStatusFilter]


# ListMonitoredResourcesFilters

### ResourcePermission
- **Type**: typing.Literal['FULL_PERMISSION', 'MISSING_PERMISSION']
- **Required**: Yes

### ResourceTypeFilters
- **Type**: typing.List[typing.Literal['CLOUDFRONT_DISTRIBUTION', 'DYNAMODB_TABLE', 'EC2_NAT_GATEWAY', 'ECS_CLUSTER', 'ECS_SERVICE', 'EKS_CLUSTER', 'ELASTICACHE_CACHE_CLUSTER', 'ELASTICSEARCH_DOMAIN', 'ELASTIC_BEANSTALK_ENVIRONMENT', 'ELASTIC_LOAD_BALANCER_LOAD_BALANCER', 'ELASTIC_LOAD_BALANCING_V2_LOAD_BALANCER', 'ELASTIC_LOAD_BALANCING_V2_TARGET_GROUP', 'KINESIS_STREAM', 'LAMBDA_FUNCTION', 'LOG_GROUPS', 'OPEN_SEARCH_SERVICE_DOMAIN', 'RDS_DB_CLUSTER', 'RDS_DB_INSTANCE', 'REDSHIFT_CLUSTER', 'ROUTE53_HEALTH_CHECK', 'ROUTE53_HOSTED_ZONE', 'S3_BUCKET', 'SAGEMAKER_ENDPOINT', 'SNS_TOPIC', 'SQS_QUEUE', 'STEP_FUNCTIONS_ACTIVITY', 'STEP_FUNCTIONS_STATE_MACHINE']]
- **Required**: Yes


# ListMonitoredResourcesRequest

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListMonitoredResourcesFilters]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMonitoredResourcesRequestPaginate

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListMonitoredResourcesFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListMonitoredResourcesResponse

### MonitoredResourceIdentifiers
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.MonitoredResourceIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationChannelsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationChannelsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListNotificationChannelsResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.NotificationChannel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationInsightsRequest

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListInsightsStatusFilter'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### NextToken
- **Type**: typing.Optional[str]


# ListOrganizationInsightsRequestPaginate

### StatusFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ListInsightsStatusFilter'>
- **Required**: Yes

### AccountIds
- **Type**: typing.Optional[typing.List[str]]

### OrganizationalUnitIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListOrganizationInsightsResponse

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ProactiveOrganizationInsightSummary]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ReactiveOrganizationInsightSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRecommendationsRequest

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Locale
- **Type**: typing.Optional[typing.Literal['DE_DE', 'EN_GB', 'EN_US', 'ES_ES', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### AccountId
- **Type**: typing.Optional[str]


# ListRecommendationsRequestPaginate

### InsightId
- **Type**: <class 'str'>
- **Required**: Yes

### Locale
- **Type**: typing.Optional[typing.Literal['DE_DE', 'EN_GB', 'EN_US', 'ES_ES', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW']]

### AccountId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# ListRecommendationsResponse

### Recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.Recommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogAnomalyClass

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


# LogAnomalyShowcase

### LogAnomalyClasses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.LogAnomalyClass]]


# LogsAnomalyDetectionIntegration

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# LogsAnomalyDetectionIntegrationConfig

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# MonitoredResourceIdentifier

### MonitoredResourceName
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### ResourcePermission
- **Type**: typing.Optional[typing.Literal['FULL_PERMISSION', 'MISSING_PERMISSION']]

### LastUpdated
- **Type**: typing.Optional[datetime.datetime]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]


# NotificationChannel

### Id
- **Type**: typing.Optional[str]

### Config
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.NotificationChannelConfigOutput]


# NotificationChannelConfig

### Sns
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.SnsChannelConfig'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.NotificationFilterConfig]


# NotificationChannelConfigOutput

### Sns
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.SnsChannelConfig'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.NotificationFilterConfigOutput]


# NotificationFilterConfig

### Severities
- **Type**: typing.Optional[typing.List[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### MessageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED_INSIGHT', 'NEW_ASSOCIATION', 'NEW_INSIGHT', 'NEW_RECOMMENDATION', 'SEVERITY_UPGRADED']]]


# NotificationFilterConfigOutput

### Severities
- **Type**: typing.Optional[typing.List[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### MessageTypes
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED_INSIGHT', 'NEW_ASSOCIATION', 'NEW_INSIGHT', 'NEW_RECOMMENDATION', 'SEVERITY_UPGRADED']]]


# OpsCenterIntegration

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# OpsCenterIntegrationConfig

### OptInStatus
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PerformanceInsightsMetricDimensionGroup

### Group
- **Type**: typing.Optional[str]

### Dimensions
- **Type**: typing.Optional[typing.List[str]]

### Limit
- **Type**: typing.Optional[int]


# PerformanceInsightsMetricQuery

### Metric
- **Type**: typing.Optional[str]

### GroupBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsMetricDimensionGroup]

### Filter
- **Type**: typing.Optional[typing.Dict[str, str]]


# PerformanceInsightsMetricsDetail

### MetricDisplayName
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]

### MetricQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsMetricQuery]

### ReferenceData
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsReferenceData]]

### StatsAtAnomaly
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsStat]]

### StatsAtBaseline
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsStat]]


# PerformanceInsightsReferenceComparisonValues

### ReferenceScalar
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsReferenceScalar]

### ReferenceMetric
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsReferenceMetric]


# PerformanceInsightsReferenceData

### Name
- **Type**: typing.Optional[str]

### ComparisonValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsReferenceComparisonValues]


# PerformanceInsightsReferenceMetric

### MetricQuery
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PerformanceInsightsMetricQuery]


# PerformanceInsightsReferenceScalar

### Value
- **Type**: typing.Optional[float]


# PerformanceInsightsStat

### Type
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]


# PredictionTimeRange

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# ProactiveAnomaly

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### AnomalyTimeRange
- **Type**: <class 'NoneType'>

### AnomalyReportedTimeRange
- **Type**: <class 'NoneType'>

### PredictionTimeRange
- **Type**: <class 'NoneType'>

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalySourceDetails]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### Limit
- **Type**: typing.Optional[float]

### SourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalySourceMetadata]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalyResource]]

### Description
- **Type**: typing.Optional[str]


# ProactiveAnomalySummary

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### UpdateTime
- **Type**: typing.Optional[datetime.datetime]

### AnomalyTimeRange
- **Type**: <class 'NoneType'>

### AnomalyReportedTimeRange
- **Type**: <class 'NoneType'>

### PredictionTimeRange
- **Type**: <class 'NoneType'>

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalySourceDetails]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### Limit
- **Type**: typing.Optional[float]

### SourceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalySourceMetadata]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalyResource]]

### Description
- **Type**: typing.Optional[str]


# ProactiveInsight

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: <class 'NoneType'>

### PredictionTimeRange
- **Type**: <class 'NoneType'>

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### SsmOpsItemId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ProactiveInsightSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: <class 'NoneType'>

### PredictionTimeRange
- **Type**: <class 'NoneType'>

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollectionOutput]

### AssociatedResourceArns
- **Type**: typing.Optional[typing.List[str]]


# ProactiveOrganizationInsightSummary

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
- **Type**: <class 'NoneType'>

### PredictionTimeRange
- **Type**: <class 'NoneType'>

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollectionOutput]


# PutFeedbackRequest

### InsightFeedback
- **Type**: <class 'NoneType'>


# ReactiveAnomaly

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### AnomalyTimeRange
- **Type**: <class 'NoneType'>

### AnomalyReportedTimeRange
- **Type**: <class 'NoneType'>

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalySourceDetails]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### Type
- **Type**: typing.Optional[typing.Literal['CAUSAL', 'CONTEXTUAL']]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CausalAnomalyId
- **Type**: typing.Optional[str]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalyResource]]


# ReactiveAnomalySummary

### Id
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### AnomalyTimeRange
- **Type**: <class 'NoneType'>

### AnomalyReportedTimeRange
- **Type**: <class 'NoneType'>

### SourceDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalySourceDetails]

### AssociatedInsightId
- **Type**: typing.Optional[str]

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### Type
- **Type**: typing.Optional[typing.Literal['CAUSAL', 'CONTEXTUAL']]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### CausalAnomalyId
- **Type**: typing.Optional[str]

### AnomalyResources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.AnomalyResource]]


# ReactiveInsight

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: <class 'NoneType'>

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### SsmOpsItemId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ReactiveInsightSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Severity
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### Status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'ONGOING']]

### InsightTimeRange
- **Type**: <class 'NoneType'>

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollectionOutput]

### AssociatedResourceArns
- **Type**: typing.Optional[typing.List[str]]


# ReactiveOrganizationInsightSummary

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
- **Type**: <class 'NoneType'>

### ResourceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput]

### ServiceCollection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollectionOutput]


# Recommendation

### Description
- **Type**: typing.Optional[str]

### Link
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Reason
- **Type**: typing.Optional[str]

### RelatedEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.RecommendationRelatedEvent]]

### RelatedAnomalies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.RecommendationRelatedAnomaly]]

### Category
- **Type**: typing.Optional[str]


# RecommendationRelatedAnomaly

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.RecommendationRelatedAnomalyResource]]

### SourceDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.RecommendationRelatedAnomalySourceDetail]]

### AnomalyId
- **Type**: typing.Optional[str]


# RecommendationRelatedAnomalyResource

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# RecommendationRelatedAnomalySourceDetail

### CloudWatchMetrics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.RecommendationRelatedCloudWatchMetricsSourceDetail]]


# RecommendationRelatedCloudWatchMetricsSourceDetail

### MetricName
- **Type**: typing.Optional[str]

### Namespace
- **Type**: typing.Optional[str]


# RecommendationRelatedEvent

### Name
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.RecommendationRelatedEventResource]]


# RecommendationRelatedEventResource

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# RemoveNotificationChannelRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceCollection

### CloudFormation
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationCollectionOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagCollectionOutput]]]


# ResourceCollectionFilter

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationCollectionFilter]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagCollectionFilter]]


# ResourceCollectionOutput

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CloudFormationCollectionOutput]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.TagCollectionOutput]]


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


# SearchInsightsFilters

### Severities
- **Type**: typing.Optional[typing.List[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### Statuses
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED', 'ONGOING']]]

### ResourceCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput, NoneType]

### ServiceCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollectionOutput, NoneType]


# SearchInsightsRequest

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.StartTimeRange'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.SearchInsightsFilters]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchInsightsRequestPaginate

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.StartTimeRange'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.SearchInsightsFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# SearchInsightsResponse

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ProactiveInsightSummary]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ReactiveInsightSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchOrganizationInsightsFilters

### Severities
- **Type**: typing.Optional[typing.List[typing.Literal['HIGH', 'LOW', 'MEDIUM']]]

### Statuses
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED', 'ONGOING']]]

### ResourceCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResourceCollectionOutput, NoneType]

### ServiceCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollection, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceCollectionOutput, NoneType]


# SearchOrganizationInsightsRequest

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.StartTimeRange'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.SearchOrganizationInsightsFilters]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchOrganizationInsightsRequestPaginate

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### StartTimeRange
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.StartTimeRange'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['PROACTIVE', 'REACTIVE']
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.SearchOrganizationInsightsFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.PaginatorConfig]


# SearchOrganizationInsightsResponse

### ProactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ProactiveInsightSummary]
- **Required**: Yes

### ReactiveInsights
- **Type**: typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ReactiveInsightSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ServiceCollection

### ServiceNames
- **Type**: typing.Optional[typing.List[typing.Literal['API_GATEWAY', 'APPLICATION_ELB', 'AUTO_SCALING_GROUP', 'CLOUD_FRONT', 'DYNAMO_DB', 'EC2', 'ECS', 'EKS', 'ELASTIC_BEANSTALK', 'ELASTI_CACHE', 'ELB', 'ES', 'KINESIS', 'LAMBDA', 'NAT_GATEWAY', 'NETWORK_ELB', 'RDS', 'REDSHIFT', 'ROUTE_53', 'S3', 'SAGE_MAKER', 'SNS', 'SQS', 'STEP_FUNCTIONS', 'SWF']]]


# ServiceCollectionOutput

### ServiceNames
- **Type**: typing.Optional[typing.List[typing.Literal['API_GATEWAY', 'APPLICATION_ELB', 'AUTO_SCALING_GROUP', 'CLOUD_FRONT', 'DYNAMO_DB', 'EC2', 'ECS', 'EKS', 'ELASTIC_BEANSTALK', 'ELASTI_CACHE', 'ELB', 'ES', 'KINESIS', 'LAMBDA', 'NAT_GATEWAY', 'NETWORK_ELB', 'RDS', 'REDSHIFT', 'ROUTE_53', 'S3', 'SAGE_MAKER', 'SNS', 'SQS', 'STEP_FUNCTIONS', 'SWF']]]


# ServiceHealth

### ServiceName
- **Type**: typing.Optional[typing.Literal['API_GATEWAY', 'APPLICATION_ELB', 'AUTO_SCALING_GROUP', 'CLOUD_FRONT', 'DYNAMO_DB', 'EC2', 'ECS', 'EKS', 'ELASTIC_BEANSTALK', 'ELASTI_CACHE', 'ELB', 'ES', 'KINESIS', 'LAMBDA', 'NAT_GATEWAY', 'NETWORK_ELB', 'RDS', 'REDSHIFT', 'ROUTE_53', 'S3', 'SAGE_MAKER', 'SNS', 'SQS', 'STEP_FUNCTIONS', 'SWF']]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.ServiceInsightHealth]

### AnalyzedResourceCount
- **Type**: typing.Optional[int]


# ServiceInsightHealth

### OpenProactiveInsights
- **Type**: typing.Optional[int]

### OpenReactiveInsights
- **Type**: typing.Optional[int]


# ServiceIntegrationConfig

### OpsCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.OpsCenterIntegration]

### LogsAnomalyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.LogsAnomalyDetectionIntegration]

### KMSServerSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.KMSServerSideEncryptionIntegration]


# ServiceResourceCost

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


# SnsChannelConfig

### TopicArn
- **Type**: typing.Optional[str]


# StartCostEstimationRequest

### ResourceCollection
- **Type**: typing.Union[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CostEstimationResourceCollectionFilter, aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.CostEstimationResourceCollectionFilterOutput]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# StartTimeRange

### FromTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ToTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# TagCollection

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagCollectionFilter

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagCollectionOutput

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagCostEstimationResourceCollectionFilter

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagCostEstimationResourceCollectionFilterOutput

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


# TagHealth

### AppBoundaryKey
- **Type**: typing.Optional[str]

### TagValue
- **Type**: typing.Optional[str]

### Insight
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.InsightHealth]

### AnalyzedResourceCount
- **Type**: typing.Optional[int]


# TimestampMetricValuePair

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### MetricValue
- **Type**: typing.Optional[float]


# UpdateCloudFormationCollectionFilter

### StackNames
- **Type**: typing.Optional[typing.List[str]]


# UpdateEventSourcesConfigRequest

### EventSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.EventSourcesConfig]


# UpdateResourceCollectionFilter

### CloudFormation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.UpdateCloudFormationCollectionFilter]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.UpdateTagCollectionFilter]]


# UpdateResourceCollectionRequest

### Action
- **Type**: typing.Literal['ADD', 'REMOVE']
- **Required**: Yes

### ResourceCollection
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.UpdateResourceCollectionFilter'>
- **Required**: Yes


# UpdateServiceIntegrationConfig

### OpsCenter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.OpsCenterIntegrationConfig]

### LogsAnomalyDetection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.LogsAnomalyDetectionIntegrationConfig]

### KMSServerSideEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.KMSServerSideEncryptionIntegrationConfig]


# UpdateServiceIntegrationRequest

### ServiceIntegration
- **Type**: <class 'aws_resource_validator.pydantic_models.devops_guru.devops_guru_classes.UpdateServiceIntegrationConfig'>
- **Required**: Yes


# UpdateTagCollectionFilter

### AppBoundaryKey
- **Type**: <class 'str'>
- **Required**: Yes

### TagValues
- **Type**: typing.List[str]
- **Required**: Yes


