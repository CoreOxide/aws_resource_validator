# Codeguruprofiler Classes

# AddNotificationChannelsRequestRequestTypeDef

### channels
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ChannelTypeDef]
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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: typing.Optional[datetime.datetime]

### userFeedback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.UserFeedbackTypeDef]


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

# BatchGetFrameMetricDataRequestRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### frameMetrics
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricTypeDef]]

### period
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ChannelTypeDef

### eventPublishers
- **Type**: typing.Sequence[typing.Literal['AnomalyDetection']]
- **Required**: Yes

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: typing.Optional[str]


# ConfigureAgentRequestRequestTypeDef

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


# CreateProfilingGroupRequestRequestTypeDef

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


# DeleteProfilingGroupRequestRequestTypeDef

### profilingGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProfilingGroupRequestRequestTypeDef

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


# FrameMetricDatumTypeDef

### frameMetric
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.FrameMetricTypeDef'>
- **Required**: Yes

### values
- **Type**: typing.List[float]
- **Required**: Yes


# FrameMetricTypeDef

### frameName
- **Type**: <class 'str'>
- **Required**: Yes

### threadStates
- **Type**: typing.Sequence[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['AggregatedRelativeTotalTime']
- **Required**: Yes


# GetFindingsReportAccountSummaryRequestRequestTypeDef

### dailyReportsOnly
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetFindingsReportAccountSummaryResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### reportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FindingsReportSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNotificationConfigurationRequestRequestTypeDef

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


# GetPolicyRequestRequestTypeDef

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


# GetProfileRequestRequestTypeDef

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


# GetRecommendationsRequestRequestTypeDef

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


# ListFindingsReportsRequestRequestTypeDef

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


# ListFindingsReportsResponseTypeDef

### findingsReportSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.FindingsReportSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfileTimesRequestListProfileTimesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeguruprofiler_classes.PaginatorConfigTypeDef]


# ListProfileTimesRequestRequestTypeDef

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


# ListProfileTimesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### profileTimes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfileTimeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProfilingGroupsRequestRequestTypeDef

### includeDescription
- **Type**: typing.Optional[bool]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListProfilingGroupsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### profilingGroupNames
- **Type**: typing.List[str]
- **Required**: Yes

### profilingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ProfilingGroupDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeguruprofiler_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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

### frameName
- **Type**: <class 'str'>
- **Required**: Yes

### threadStates
- **Type**: typing.List[str]
- **Required**: Yes

### type
- **Type**: typing.Literal['AggregatedRelativeTotalTime']
- **Required**: Yes


# NotificationConfigurationTypeDef

### channels
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeguruprofiler_classes.ChannelTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PatternTypeDef

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


# PostAgentProfileRequestRequestTypeDef

### agentProfile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# PutPermissionRequestRequestTypeDef

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


# RemoveNotificationChannelRequestRequestTypeDef

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


# RemovePermissionRequestRequestTypeDef

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


# SubmitFeedbackRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateProfilingGroupRequestRequestTypeDef

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


# UserFeedbackTypeDef

### type
- **Type**: typing.Literal['Negative', 'Positive']
- **Required**: Yes


