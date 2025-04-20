# Application Insights Application Insights Classes

# AddWorkloadRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.WorkloadConfiguration'>
- **Required**: Yes


# AddWorkloadResponse

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.WorkloadConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# ApplicationComponent

### ComponentName
- **Type**: typing.Optional[str]

### ComponentRemarks
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]

### OsType
- **Type**: typing.Optional[typing.Literal['LINUX', 'WINDOWS']]

### Tier
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE']]

### Monitor
- **Type**: typing.Optional[bool]

### DetectedWorkload
- **Type**: typing.Optional[typing.Dict[typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE'], typing.Dict[str, str]]]


# ApplicationInfo

### AccountId
- **Type**: typing.Optional[str]

### ResourceGroupName
- **Type**: typing.Optional[str]

### LifeCycle
- **Type**: typing.Optional[str]

### OpsItemSNSTopicArn
- **Type**: typing.Optional[str]

### SNSNotificationArn
- **Type**: typing.Optional[str]

### OpsCenterEnabled
- **Type**: typing.Optional[bool]

### CWEMonitorEnabled
- **Type**: typing.Optional[bool]

### Remarks
- **Type**: typing.Optional[str]

### AutoConfigEnabled
- **Type**: typing.Optional[bool]

### DiscoveryType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_BASED', 'RESOURCE_GROUP_BASED']]

### AttachMissingPermission
- **Type**: typing.Optional[bool]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationEvent

### ResourceGroupName
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### MonitoredResourceARN
- **Type**: typing.Optional[str]

### EventStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'WARN']]

### EventResourceType
- **Type**: typing.Optional[typing.Literal['CLOUDFORMATION', 'CLOUDWATCH_ALARM', 'CLOUDWATCH_LOG', 'SSM_ASSOCIATION']]

### EventTime
- **Type**: typing.Optional[datetime.datetime]

### EventDetail
- **Type**: typing.Optional[str]

### EventResourceName
- **Type**: typing.Optional[str]


# CreateApplicationRequest

### ResourceGroupName
- **Type**: typing.Optional[str]

### OpsCenterEnabled
- **Type**: typing.Optional[bool]

### CWEMonitorEnabled
- **Type**: typing.Optional[bool]

### OpsItemSNSTopicArn
- **Type**: typing.Optional[str]

### SNSNotificationArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Tag]]

### AutoConfigEnabled
- **Type**: typing.Optional[bool]

### AutoCreate
- **Type**: typing.Optional[bool]

### GroupingType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_BASED']]

### AttachMissingPermission
- **Type**: typing.Optional[bool]


# CreateApplicationResponse

### ApplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ApplicationInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# CreateComponentRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceList
- **Type**: typing.List[str]
- **Required**: Yes


# CreateLogPatternRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternSetName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternName
- **Type**: <class 'str'>
- **Required**: Yes

### Pattern
- **Type**: <class 'str'>
- **Required**: Yes

### Rank
- **Type**: <class 'int'>
- **Required**: Yes


# CreateLogPatternResponse

### LogPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.LogPattern'>
- **Required**: Yes

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogPatternRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternSetName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeApplicationResponse

### ApplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ApplicationInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeComponentConfigurationRecommendationRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### Tier
- **Type**: typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE']
- **Required**: Yes

### WorkloadName
- **Type**: typing.Optional[str]

### RecommendationType
- **Type**: typing.Optional[typing.Literal['ALL', 'INFRA_ONLY', 'WORKLOAD_ONLY']]


# DescribeComponentConfigurationRecommendationResponse

### ComponentConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeComponentConfigurationRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeComponentConfigurationResponse

### Monitor
- **Type**: <class 'bool'>
- **Required**: Yes

### Tier
- **Type**: typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE']
- **Required**: Yes

### ComponentConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeComponentRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeComponentResponse

### ApplicationComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ApplicationComponent'>
- **Required**: Yes

### ResourceList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLogPatternRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternSetName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeLogPatternResponse

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### LogPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.LogPattern'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeObservationRequest

### ObservationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeObservationResponse

### Observation
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Observation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProblemObservationsRequest

### ProblemId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeProblemObservationsResponse

### RelatedObservations
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.RelatedObservations'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProblemRequest

### ProblemId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeProblemResponse

### Problem
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Problem'>
- **Required**: Yes

### SNSNotificationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkloadRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeWorkloadResponse

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadRemarks
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.WorkloadConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# ListApplicationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListApplicationsResponse

### ApplicationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ApplicationInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComponentsRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListComponentsResponse

### ApplicationComponentList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ApplicationComponent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationHistoryRequest

### ResourceGroupName
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EventStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'WARN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListConfigurationHistoryResponse

### EventList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ConfigurationEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLogPatternSetsRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListLogPatternSetsResponse

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### LogPatternSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLogPatternsRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternSetName
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListLogPatternsResponse

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### LogPatterns
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.LogPattern]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProblemsRequest

### AccountId
- **Type**: typing.Optional[str]

### ResourceGroupName
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ComponentName
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['IGNORED', 'VISIBLE']]


# ListProblemsResponse

### ProblemList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Problem]
- **Required**: Yes

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# ListWorkloadsRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListWorkloadsResponse

### WorkloadList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Workload]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogPattern

### PatternSetName
- **Type**: typing.Optional[str]

### PatternName
- **Type**: typing.Optional[str]

### Pattern
- **Type**: typing.Optional[str]

### Rank
- **Type**: typing.Optional[int]


# Observation

### Id
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### SourceType
- **Type**: typing.Optional[str]

### SourceARN
- **Type**: typing.Optional[str]

### LogGroup
- **Type**: typing.Optional[str]

### LineTime
- **Type**: typing.Optional[datetime.datetime]

### LogText
- **Type**: typing.Optional[str]

### LogFilter
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'WARN']]

### MetricNamespace
- **Type**: typing.Optional[str]

### MetricName
- **Type**: typing.Optional[str]

### Unit
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[float]

### CloudWatchEventId
- **Type**: typing.Optional[str]

### CloudWatchEventSource
- **Type**: typing.Optional[typing.Literal['CODE_DEPLOY', 'EC2', 'HEALTH', 'RDS']]

### CloudWatchEventDetailType
- **Type**: typing.Optional[str]

### HealthEventArn
- **Type**: typing.Optional[str]

### HealthService
- **Type**: typing.Optional[str]

### HealthEventTypeCode
- **Type**: typing.Optional[str]

### HealthEventTypeCategory
- **Type**: typing.Optional[str]

### HealthEventDescription
- **Type**: typing.Optional[str]

### CodeDeployDeploymentId
- **Type**: typing.Optional[str]

### CodeDeployDeploymentGroup
- **Type**: typing.Optional[str]

### CodeDeployState
- **Type**: typing.Optional[str]

### CodeDeployApplication
- **Type**: typing.Optional[str]

### CodeDeployInstanceGroupId
- **Type**: typing.Optional[str]

### Ec2State
- **Type**: typing.Optional[str]

### RdsEventCategories
- **Type**: typing.Optional[str]

### RdsEventMessage
- **Type**: typing.Optional[str]

### S3EventName
- **Type**: typing.Optional[str]

### StatesExecutionArn
- **Type**: typing.Optional[str]

### StatesArn
- **Type**: typing.Optional[str]

### StatesStatus
- **Type**: typing.Optional[str]

### StatesInput
- **Type**: typing.Optional[str]

### EbsEvent
- **Type**: typing.Optional[str]

### EbsResult
- **Type**: typing.Optional[str]

### EbsCause
- **Type**: typing.Optional[str]

### EbsRequestId
- **Type**: typing.Optional[str]

### XRayFaultPercent
- **Type**: typing.Optional[int]

### XRayThrottlePercent
- **Type**: typing.Optional[int]

### XRayErrorPercent
- **Type**: typing.Optional[int]

### XRayRequestCount
- **Type**: typing.Optional[int]

### XRayRequestAverageLatency
- **Type**: typing.Optional[int]

### XRayNodeName
- **Type**: typing.Optional[str]

### XRayNodeType
- **Type**: typing.Optional[str]


# Problem

### Id
- **Type**: typing.Optional[str]

### Title
- **Type**: typing.Optional[str]

### ShortName
- **Type**: typing.Optional[str]

### Insights
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['IGNORE', 'PENDING', 'RECOVERING', 'RECURRING', 'RESOLVED']]

### AffectedResource
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### SeverityLevel
- **Type**: typing.Optional[typing.Literal['High', 'Informative', 'Low', 'Medium']]

### AccountId
- **Type**: typing.Optional[str]

### ResourceGroupName
- **Type**: typing.Optional[str]

### Feedback
- **Type**: typing.Optional[typing.Dict[typing.Literal['INSIGHTS_FEEDBACK'], typing.Literal['NOT_SPECIFIED', 'NOT_USEFUL', 'USEFUL']]]

### RecurringCount
- **Type**: typing.Optional[int]

### LastRecurrenceTime
- **Type**: typing.Optional[datetime.datetime]

### Visibility
- **Type**: typing.Optional[typing.Literal['IGNORED', 'VISIBLE']]

### ResolutionMethod
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'MANUAL', 'UNRESOLVED']]


# RelatedObservations

### ObservationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Observation]]


# RemoveWorkloadRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights.application_insights_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateApplicationRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### OpsCenterEnabled
- **Type**: typing.Optional[bool]

### CWEMonitorEnabled
- **Type**: typing.Optional[bool]

### OpsItemSNSTopicArn
- **Type**: typing.Optional[str]

### SNSNotificationArn
- **Type**: typing.Optional[str]

### RemoveSNSTopic
- **Type**: typing.Optional[bool]

### AutoConfigEnabled
- **Type**: typing.Optional[bool]

### AttachMissingPermission
- **Type**: typing.Optional[bool]


# UpdateApplicationResponse

### ApplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ApplicationInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateComponentConfigurationRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### Monitor
- **Type**: typing.Optional[bool]

### Tier
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE']]

### ComponentConfiguration
- **Type**: typing.Optional[str]

### AutoConfigEnabled
- **Type**: typing.Optional[bool]


# UpdateComponentRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### NewComponentName
- **Type**: typing.Optional[str]

### ResourceList
- **Type**: typing.Optional[typing.List[str]]


# UpdateLogPatternRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternSetName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternName
- **Type**: <class 'str'>
- **Required**: Yes

### Pattern
- **Type**: typing.Optional[str]

### Rank
- **Type**: typing.Optional[int]


# UpdateLogPatternResponse

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LogPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.LogPattern'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProblemRequest

### ProblemId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['RESOLVED']]

### Visibility
- **Type**: typing.Optional[typing.Literal['IGNORED', 'VISIBLE']]


# UpdateWorkloadRequest

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.WorkloadConfiguration'>
- **Required**: Yes

### WorkloadId
- **Type**: typing.Optional[str]


# UpdateWorkloadResponse

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.WorkloadConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights.application_insights_classes.ResponseMetadata'>
- **Required**: Yes


# Workload

### WorkloadId
- **Type**: typing.Optional[str]

### ComponentName
- **Type**: typing.Optional[str]

### WorkloadName
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE']]

### WorkloadRemarks
- **Type**: typing.Optional[str]

### MissingWorkloadConfig
- **Type**: typing.Optional[bool]


# WorkloadConfiguration

### WorkloadName
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE']]

### Configuration
- **Type**: typing.Optional[str]


