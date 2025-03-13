# Codeguruprofiler Classes

# AddNotificationChannelsRequestTypeDef

### channels
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ChannelUnionTypeDef]
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AddNotificationChannelsResponseTypeDef

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AgentConfigurationTypeDef

### periodInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### shouldProfile
- **Type**: <class 'bool'>
- **Required**: Yes

### agentParameters
- **Type**: typing.Optional[typing.Dict[typing.Literal['MaxStackDepth', 'MemoryUsageLimitPercent', 'MinimumTimeForReportingInMilliseconds', 'ReportingIntervalInMilliseconds', 'SamplingIntervalInMilliseconds'], str]]


# AgentOrchestrationConfigTypeDef

### profilingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# AggregatedProfileTimeTypeDef

### period
- **Type**: typing.Optional[typing.Literal['P1D', 'PT1H', 'PT5M']]

### start
- **Type**: typing.Optional[datetime.datetime]


# AnomalyInstanceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnomalyTypeDef

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AnomalyInstanceTypeDef]
- **Required**: Yes

### metric
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.MetricTypeDef'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetFrameMetricDataRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef]

### frameMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricUnionTypeDef]]

### period
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef]

### targetResolution
- **Type**: typing.Optional[typing.Literal['P1D', 'PT1H', 'PT5M']]


# BatchGetFrameMetricDataResponseTypeDef

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTimes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampStructureTypeDef]
- **Required**: Yes

### frameMetricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricDatumTypeDef]
- **Required**: Yes

### resolution
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### unprocessedEndTimes
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampStructureTypeDef]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigureAgentRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### fleetInstanceId
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AgentId', 'AwsRequestId', 'ComputePlatform', 'ExecutionEnvironment', 'LambdaFunctionArn', 'LambdaMemoryLimitInMB', 'LambdaPreviousExecutionTimeInMilliseconds', 'LambdaRemainingTimeInMilliseconds', 'LambdaTimeGapBetweenInvokesInMilliseconds'], str]]


# ConfigureAgentResponseTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProfilingGroupRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### agentOrchestrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentOrchestrationConfigTypeDef]

### computePlatform
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'Default']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProfilingGroupResponseTypeDef

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteProfilingGroupRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProfilingGroupRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProfilingGroupResponseTypeDef

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FindingsReportSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FrameMetricDatumTypeDef

### frameMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricOutputTypeDef'>
- **Required**: Yes

### values
- **Type**: typing.List[float]
- **Required**: Yes


# FrameMetricOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FrameMetricUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetFindingsReportAccountSummaryRequestTypeDef

### dailyReportsOnly
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFindingsReportAccountSummaryResponseTypeDef

### reportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FindingsReportSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetNotificationConfigurationRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetNotificationConfigurationResponseTypeDef

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponseTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetProfileRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### accept
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef]

### maxDepth
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef]


# GetProfileResponseTypeDef

### contentEncoding
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### profile
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommendationsRequestTypeDef

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]


# GetRecommendationsResponseTypeDef

### anomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AnomalyTypeDef]
- **Required**: Yes

### profileEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### profileStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.RecommendationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFindingsReportsRequestTypeDef

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### dailyReportsOnly
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsReportsResponseTypeDef

### findingsReportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FindingsReportSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfileTimesRequestPaginateTypeDef

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### period
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### orderBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.PaginatorConfigTypeDef]


# ListProfileTimesRequestTypeDef

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### period
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]


# ListProfileTimesResponseTypeDef

### profileTimes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfileTimeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfilingGroupsRequestTypeDef

### includeDescription
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProfilingGroupsResponseTypeDef

### profilingGroupNames
- **Type**: typing.List[str]
- **Required**: Yes

### profilingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MatchTypeDef

### frameAddress
- **Type**: typing.Optional[str]

### targetFramesIndex
- **Type**: typing.Optional[int]

### thresholdBreachValue
- **Type**: typing.Optional[float]


# MetricTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationConfigurationTypeDef

### channels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ChannelOutputTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PatternTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PostAgentProfileRequestTypeDef

### agentProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.BlobTypeDef'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### profileToken
- **Type**: typing.Optional[str]


# ProfileTimeTypeDef

### start
- **Type**: typing.Optional[datetime.datetime]


# ProfilingGroupDescriptionTypeDef

### agentOrchestrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentOrchestrationConfigTypeDef]

### arn
- **Type**: typing.Optional[str]

### computePlatform
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'Default']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### profilingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingStatusTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ProfilingStatusTypeDef

### latestAgentOrchestratedAt
- **Type**: typing.Optional[datetime.datetime]

### latestAgentProfileReportedAt
- **Type**: typing.Optional[datetime.datetime]

### latestAggregatedProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AggregatedProfileTimeTypeDef]


# PutPermissionRequestTypeDef

### actionGroup
- **Type**: typing.Literal['agentPermissions']
- **Required**: Yes

### principals
- **Type**: typing.Sequence[str]
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: typing.Optional[str]


# PutPermissionResponseTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecommendationTypeDef

### allMatchesCount
- **Type**: <class 'int'>
- **Required**: Yes

### allMatchesSum
- **Type**: <class 'float'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### pattern
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.PatternTypeDef'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### topMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.MatchTypeDef]
- **Required**: Yes


# RemoveNotificationChannelRequestTypeDef

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveNotificationChannelResponseTypeDef

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemovePermissionRequestTypeDef

### actionGroup
- **Type**: typing.Literal['agentPermissions']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionResponseTypeDef

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
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

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampStructureTypeDef

### value
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateProfilingGroupRequestTypeDef

### agentOrchestrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentOrchestrationConfigTypeDef'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateProfilingGroupResponseTypeDef

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


