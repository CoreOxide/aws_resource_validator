# Application Insights Classes

# AddWorkloadRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.WorkloadConfigurationTypeDef'>
- **Required**: Yes


# AddWorkloadResponseTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.WorkloadConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationComponentTypeDef

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


# ApplicationInfoTypeDef

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

# ConfigurationEventTypeDef

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


# CreateApplicationRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.application_insights_classes.TagTypeDef]]

### AutoConfigEnabled
- **Type**: typing.Optional[bool]

### AutoCreate
- **Type**: typing.Optional[bool]

### GroupingType
- **Type**: typing.Optional[typing.Literal['ACCOUNT_BASED']]

### AttachMissingPermission
- **Type**: typing.Optional[bool]


# CreateApplicationResponseTypeDef

### ApplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ApplicationInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateComponentRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreateLogPatternResponseTypeDef

### LogPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.LogPatternTypeDef'>
- **Required**: Yes

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteComponentRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLogPatternRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternSetName
- **Type**: <class 'str'>
- **Required**: Yes

### PatternName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeApplicationResponseTypeDef

### ApplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ApplicationInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeComponentConfigurationRecommendationRequestTypeDef

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


# DescribeComponentConfigurationRecommendationResponseTypeDef

### ComponentConfiguration
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeComponentConfigurationRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeComponentConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeComponentRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeComponentResponseTypeDef

### ApplicationComponent
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ApplicationComponentTypeDef'>
- **Required**: Yes

### ResourceList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLogPatternRequestTypeDef

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


# DescribeLogPatternResponseTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### LogPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.LogPatternTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeObservationRequestTypeDef

### ObservationId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeObservationResponseTypeDef

### Observation
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ObservationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProblemObservationsRequestTypeDef

### ProblemId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeProblemObservationsResponseTypeDef

### RelatedObservations
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.RelatedObservationsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProblemRequestTypeDef

### ProblemId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]


# DescribeProblemResponseTypeDef

### Problem
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ProblemTypeDef'>
- **Required**: Yes

### SNSNotificationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkloadRequestTypeDef

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


# DescribeWorkloadResponseTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadRemarks
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.WorkloadConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### ApplicationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights_classes.ApplicationInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListComponentsRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListComponentsResponseTypeDef

### ApplicationComponentList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights_classes.ApplicationComponentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationHistoryRequestTypeDef

### ResourceGroupName
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_insights_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_insights_classes.TimestampTypeDef]

### EventStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'INFO', 'WARN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListConfigurationHistoryResponseTypeDef

### EventList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights_classes.ConfigurationEventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLogPatternSetsRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# ListLogPatternSetsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLogPatternsRequestTypeDef

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


# ListLogPatternsResponseTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### LogPatterns
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights_classes.LogPatternTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListProblemsRequestTypeDef

### AccountId
- **Type**: typing.Optional[str]

### ResourceGroupName
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_insights_classes.TimestampTypeDef]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.application_insights_classes.TimestampTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ComponentName
- **Type**: typing.Optional[str]

### Visibility
- **Type**: typing.Optional[typing.Literal['IGNORED', 'VISIBLE']]


# ListProblemsResponseTypeDef

### ProblemList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights_classes.ProblemTypeDef]
- **Required**: Yes

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkloadsRequestTypeDef

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


# ListWorkloadsResponseTypeDef

### WorkloadList
- **Type**: typing.List[aws_resource_validator.pydantic_models.application_insights_classes.WorkloadTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogPatternTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ObservationTypeDef

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


# ProblemTypeDef

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


# RelatedObservationsTypeDef

### ObservationList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.application_insights_classes.ObservationTypeDef]]


# RemoveWorkloadRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes


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


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.application_insights_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestTypeDef

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


# UpdateApplicationResponseTypeDef

### ApplicationInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ApplicationInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateComponentConfigurationRequestTypeDef

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


# UpdateComponentRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### NewComponentName
- **Type**: typing.Optional[str]

### ResourceList
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLogPatternResponseTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### LogPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.LogPatternTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProblemRequestTypeDef

### ProblemId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Optional[typing.Literal['RESOLVED']]

### Visibility
- **Type**: typing.Optional[typing.Literal['IGNORED', 'VISIBLE']]


# UpdateWorkloadRequestTypeDef

### ResourceGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ComponentName
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.WorkloadConfigurationTypeDef'>
- **Required**: Yes

### WorkloadId
- **Type**: typing.Optional[str]


# UpdateWorkloadResponseTypeDef

### WorkloadId
- **Type**: <class 'str'>
- **Required**: Yes

### WorkloadConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.WorkloadConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.application_insights_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkloadConfigurationTypeDef

### WorkloadName
- **Type**: typing.Optional[str]

### Tier
- **Type**: typing.Optional[typing.Literal['ACTIVE_DIRECTORY', 'CUSTOM', 'DEFAULT', 'DOT_NET_CORE', 'DOT_NET_WEB', 'DOT_NET_WEB_TIER', 'DOT_NET_WORKER', 'JAVA_JMX', 'MYSQL', 'ORACLE', 'POSTGRESQL', 'SAP_ASE_HIGH_AVAILABILITY', 'SAP_ASE_SINGLE_NODE', 'SAP_HANA_HIGH_AVAILABILITY', 'SAP_HANA_MULTI_NODE', 'SAP_HANA_SINGLE_NODE', 'SAP_NETWEAVER_DISTRIBUTED', 'SAP_NETWEAVER_HIGH_AVAILABILITY', 'SAP_NETWEAVER_STANDARD', 'SHAREPOINT', 'SQL_SERVER', 'SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP', 'SQL_SERVER_FAILOVER_CLUSTER_INSTANCE']]

### Configuration
- **Type**: typing.Optional[str]


# WorkloadTypeDef

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


