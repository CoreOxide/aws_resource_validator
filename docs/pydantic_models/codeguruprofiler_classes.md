# Codeguruprofiler Classes

# AddNotificationChannelsRequest

### channels
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.Channel, aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ChannelOutput]]
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AddNotificationChannelsResponse

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.NotificationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.AnomalyInstance]
- **Required**: Yes

### metric
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.Metric'>
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# AnomalyInstance

### id
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]

### userFeedback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.UserFeedback]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchGetFrameMetricDataRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### frameMetrics
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.FrameMetric, aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.FrameMetricOutput]]]

### period
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### targetResolution
- **Type**: typing.Optional[typing.Literal['P1D', 'PT1H', 'PT5M']]


# BatchGetFrameMetricDataResponse

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTimes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.TimestampStructure]
- **Required**: Yes

### frameMetricData
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.FrameMetricDatum]
- **Required**: Yes

### resolution
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### unprocessedEndTimes
- **Type**: typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.TimestampStructure]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# Channel

### eventPublishers
- **Type**: typing.List[typing.Literal['AnomalyDetection']]
- **Required**: Yes

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]


# ChannelOutput

### eventPublishers
- **Type**: typing.List[typing.Literal['AnomalyDetection']]
- **Required**: Yes

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]


# ConfigureAgentRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### fleetInstanceId
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[typing.Dict[typing.Literal['AgentId', 'AwsRequestId', 'ComputePlatform', 'ExecutionEnvironment', 'LambdaFunctionArn', 'LambdaMemoryLimitInMB', 'LambdaPreviousExecutionTimeInMilliseconds', 'LambdaRemainingTimeInMilliseconds', 'LambdaTimeGapBetweenInvokesInMilliseconds'], str]]


# ConfigureAgentResponse

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.AgentConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProfilingGroupRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### agentOrchestrationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.AgentOrchestrationConfig]

### computePlatform
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'Default']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateProfilingGroupResponse

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ProfilingGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ProfilingGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# FindingsReportSummary

### id
- **Type**: typing.Optional[str]

### profileEndTime
- **Type**: typing.Optional[datetime.datetime]

### profileStartTime
- **Type**: typing.Optional[datetime.datetime]

### profilingGroupName
- **Type**: typing.Optional[str]

### totalNumberOfFindings
- **Type**: typing.Optional[int]


# FrameMetric

### frameName
- **Type**: <class 'str'>
- **Required**: Yes

### threadStates
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['AggregatedRelativeTotalTime']
- **Required**: Yes


# FrameMetricDatum

### frameMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.FrameMetricOutput'>
- **Required**: Yes

### values
- **Type**: typing.List[float]
- **Required**: Yes


# FrameMetricOutput

### frameName
- **Type**: <class 'str'>
- **Required**: Yes

### threadStates
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['AggregatedRelativeTotalTime']
- **Required**: Yes


# GetFindingsReportAccountSummaryRequest

### dailyReportsOnly
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFindingsReportAccountSummaryResponse

### reportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.FindingsReportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetNotificationConfigurationRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetNotificationConfigurationResponse

### notificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.NotificationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# GetProfileRequest

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### accept
- **Type**: typing.Optional[str]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### maxDepth
- **Type**: typing.Optional[int]

### period
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommendationsRequest

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]


# GetRecommendationsResponse

### anomalies
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.Anomaly]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.Recommendation]
- **Required**: Yes


# ListFindingsReportsRequest

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### dailyReportsOnly
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFindingsReportsResponse

### findingsReportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.FindingsReportSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListProfileTimesRequest

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### period
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### orderBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]


# ListProfileTimesRequestPaginate

### endTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### period
- **Type**: typing.Literal['P1D', 'PT1H', 'PT5M']
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### orderBy
- **Type**: typing.Optional[typing.Literal['TimestampAscending', 'TimestampDescending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.PaginatorConfig]


# ListProfileTimesResponse

### profileTimes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ProfileTime]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ProfilingGroupDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# Match

### frameAddress
- **Type**: typing.Optional[str]

### targetFramesIndex
- **Type**: typing.Optional[int]

### thresholdBreachValue
- **Type**: typing.Optional[float]


# Metric

### frameName
- **Type**: <class 'str'>
- **Required**: Yes

### threadStates
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['AggregatedRelativeTotalTime']
- **Required**: Yes


# NotificationConfiguration

### channels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ChannelOutput]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Pattern

### countersToAggregate
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### resolutionSteps
- **Type**: typing.Optional[str]

### targetFrames
- **Type**: typing.Optional[typing.List[typing.List[str]]]

### thresholdPercent
- **Type**: typing.Optional[float]


# PostAgentProfileRequest

### agentProfile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.AgentOrchestrationConfig]

### arn
- **Type**: typing.Optional[str]

### computePlatform
- **Type**: typing.Optional[typing.Literal['AWSLambda', 'Default']]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### profilingStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ProfilingStatus]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.AggregatedProfileTime]


# PutPermissionRequest

### actionGroup
- **Type**: typing.Literal['agentPermissions']
- **Required**: Yes

### principals
- **Type**: typing.List[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.Pattern'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### topMatches
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.Match]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.NotificationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
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


# SubmitFeedbackRequest

### anomalyInstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Negative', 'Positive']
- **Required**: Yes

### comment
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TimestampStructure

### value
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateProfilingGroupRequest

### agentOrchestrationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.AgentOrchestrationConfig'>
- **Required**: Yes

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateProfilingGroupResponse

### profilingGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ProfilingGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler.codeguruprofiler_classes.ResponseMetadata'>
- **Required**: Yes


# UserFeedback

### type
- **Type**: typing.Literal['Negative', 'Positive']
- **Required**: Yes


