# Codeguruprofiler Classes

# AddNotificationChannelsRequest

### channels
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ChannelUnion]
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AddNotificationChannelsResponse

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.NotificationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# AgentConfiguration

### periodInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### shouldProfile
- **Type**: <class 'bool'>
- **Required**: Yes

### agentParameters
- **Type**: typing.Optional[typing.Dict[typing.Literal['MaxStackDepth', 'MemoryUsageLimitPercent', 'MinimumTimeForReportingInMilliseconds', 'ReportingIntervalInMilliseconds', 'SamplingIntervalInMilliseconds'], str]]


# AgentOrchestrationConfig

### profilingEnabled
- **Type**: <class 'bool'>
- **Required**: Yes


# AggregatedProfileTime

### period
- **Type**: typing.Optional[typing.Literal['P1D', 'PT1H', 'PT5M']]

### start
- **Type**: typing.Optional[datetime.datetime]


# Anomaly

### instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AnomalyInstance]
- **Required**: Yes

### metric
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Metric'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# AnomalyInstance

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetFrameMetricDataRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp]

### frameMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricUnion]]

### period
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp]

### targetResolution
- **Type**: typing.Optional[typing.Literal['P1D', 'PT1H', 'PT5M']]


# BatchGetFrameMetricDataResponse

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTimes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampStructure]
- **Required**: Yes

### frameMetricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricDatum]
- **Required**: Yes

### resolution
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### unprocessedEndTimes
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.TimestampStructure]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigureAgentRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### fleetInstanceId
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AgentId', 'AwsRequestId', 'ComputePlatform', 'ExecutionEnvironment', 'LambdaFunctionArn', 'LambdaMemoryLimitInMB', 'LambdaPreviousExecutionTimeInMilliseconds', 'LambdaRemainingTimeInMilliseconds', 'LambdaTimeGapBetweenInvokesInMilliseconds'], str]]


# ConfigureAgentResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfilingGroupRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### agentOrchestrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentOrchestrationConfig]

### computePlatform
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'Default']]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateProfilingGroupResponse

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteProfilingGroupRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProfilingGroupRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProfilingGroupResponse

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# FindingsReportSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FrameMetricDatum

### frameMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricOutput'>
- **Required**: Yes

### values
- **Type**: typing.List[float]
- **Required**: Yes


# FrameMetricOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FrameMetricUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetFindingsReportAccountSummaryRequest

### dailyReportsOnly
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFindingsReportAccountSummaryResponse

### reportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FindingsReportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetNotificationConfigurationRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetNotificationConfigurationResponse

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.NotificationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponse

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### accept
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp]

### maxDepth
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp]


# GetProfileResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommendationsRequest

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]


# GetRecommendationsResponse

### anomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.Anomaly]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.Recommendation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# ListFindingsReportsRequest

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### dailyReportsOnly
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsReportsResponse

### findingsReportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FindingsReportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfileTimesRequest

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### period
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]


# ListProfileTimesRequestPaginate

### endTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### period
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Timestamp'>
- **Required**: Yes

### orderBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.PaginatorConfig]


# ListProfileTimesResponse

### profileTimes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfileTime]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfilingGroupsRequest

### includeDescription
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProfilingGroupsResponse

### profilingGroupNames
- **Type**: typing.List[str]
- **Required**: Yes

### profilingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# Match

### frameAddress
- **Type**: typing.Optional[str]

### targetFramesIndex
- **Type**: typing.Optional[int]

### thresholdBreachValue
- **Type**: typing.Optional[float]


# Metric

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NotificationConfiguration

### channels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ChannelOutput]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Pattern

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PostAgentProfileRequest

### agentProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Blob'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### profileToken
- **Type**: typing.Optional[str]


# ProfileTime

### start
- **Type**: typing.Optional[datetime.datetime]


# ProfilingGroupDescription

### agentOrchestrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentOrchestrationConfig]

### arn
- **Type**: typing.Optional[str]

### computePlatform
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'Default']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### profilingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingStatus]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# ProfilingStatus

### latestAgentOrchestratedAt
- **Type**: typing.Optional[datetime.datetime]

### latestAgentProfileReportedAt
- **Type**: typing.Optional[datetime.datetime]

### latestAggregatedProfile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.AggregatedProfileTime]


# PutPermissionRequest

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


# PutPermissionResponse

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# Recommendation

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.Pattern'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### topMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.Match]
- **Required**: Yes


# RemoveNotificationChannelRequest

### channelId
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveNotificationChannelResponse

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.NotificationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# RemovePermissionRequest

### actionGroup
- **Type**: typing.Literal['agentPermissions']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes


# RemovePermissionResponse

### policy
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
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


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampStructure

### value
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateProfilingGroupRequest

### agentOrchestrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.AgentOrchestrationConfig'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateProfilingGroupResponse

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


