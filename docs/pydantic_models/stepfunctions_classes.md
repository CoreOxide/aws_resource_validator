# Stepfunctions Classes

# ActivityFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ActivityListItemTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ActivityScheduleFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ActivityScheduledEventDetailsTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Optional[str]

### inputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]

### timeoutInSeconds
- **Type**: typing.Optional[int]

### heartbeatInSeconds
- **Type**: typing.Optional[int]


# ActivityStartedEventDetailsTypeDef

### workerName
- **Type**: typing.Optional[str]


# ActivitySucceededEventDetailsTypeDef

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# ActivityTimedOutEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BillingDetailsTypeDef

### billedMemoryUsedInMB
- **Type**: typing.Optional[int]

### billedDurationInMilliseconds
- **Type**: typing.Optional[int]


# CloudWatchEventsExecutionDataDetailsTypeDef

### included
- **Type**: typing.Optional[bool]


# CloudWatchLogsLogGroupTypeDef

### logGroupArn
- **Type**: typing.Optional[str]


# CreateActivityInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.TagTypeDef]]


# CreateActivityOutputTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStateMachineAliasInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItemTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# CreateStateMachineAliasOutputTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStateMachineInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'STANDARD']]

### loggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.TagTypeDef]]

### tracingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfigurationTypeDef]

### publish
- **Type**: typing.Optional[bool]

### versionDescription
- **Type**: typing.Optional[str]


# CreateStateMachineOutputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteActivityInputRequestTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineAliasInputRequestTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStateMachineVersionInputRequestTypeDef

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActivityInputRequestTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeActivityOutputTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeExecutionInputRequestTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeExecutionOutputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### input
- **Type**: <class 'str'>
- **Required**: Yes

### inputDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.CloudWatchEventsExecutionDataDetailsTypeDef'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes

### outputDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.CloudWatchEventsExecutionDataDetailsTypeDef'>
- **Required**: Yes

### traceHeader
- **Type**: <class 'str'>
- **Required**: Yes

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### redriveCount
- **Type**: <class 'int'>
- **Required**: Yes

### redriveDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### redriveStatus
- **Type**: typing.Literal['NOT_REDRIVABLE', 'REDRIVABLE', 'REDRIVABLE_BY_MAP_RUN']
- **Required**: Yes

### redriveStatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMapRunInputRequestTypeDef

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMapRunOutputTypeDef

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABORTED', 'FAILED', 'RUNNING', 'SUCCEEDED']
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### maxConcurrency
- **Type**: <class 'int'>
- **Required**: Yes

### toleratedFailurePercentage
- **Type**: <class 'float'>
- **Required**: Yes

### toleratedFailureCount
- **Type**: <class 'int'>
- **Required**: Yes

### itemCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunItemCountsTypeDef'>
- **Required**: Yes

### executionCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunExecutionCountsTypeDef'>
- **Required**: Yes

### redriveCount
- **Type**: <class 'int'>
- **Required**: Yes

### redriveDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStateMachineAliasInputRequestTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStateMachineAliasOutputTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItemTypeDef]
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStateMachineForExecutionInputRequestTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStateMachineForExecutionOutputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### loggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### tracingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfigurationTypeDef'>
- **Required**: Yes

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### label
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStateMachineInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStateMachineOutputTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING']
- **Required**: Yes

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EXPRESS', 'STANDARD']
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### loggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationOutputTypeDef'>
- **Required**: Yes

### tracingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfigurationTypeDef'>
- **Required**: Yes

### label
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecutionAbortedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ExecutionFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ExecutionListItemTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: typing.Optional[datetime.datetime]

### mapRunArn
- **Type**: typing.Optional[str]

### itemCount
- **Type**: typing.Optional[int]

### stateMachineVersionArn
- **Type**: typing.Optional[str]

### stateMachineAliasArn
- **Type**: typing.Optional[str]

### redriveCount
- **Type**: typing.Optional[int]

### redriveDate
- **Type**: typing.Optional[datetime.datetime]


# ExecutionRedrivenEventDetailsTypeDef

### redriveCount
- **Type**: typing.Optional[int]


# ExecutionStartedEventDetailsTypeDef

### input
- **Type**: typing.Optional[str]

### inputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]

### roleArn
- **Type**: typing.Optional[str]

### stateMachineAliasArn
- **Type**: typing.Optional[str]

### stateMachineVersionArn
- **Type**: typing.Optional[str]


# ExecutionSucceededEventDetailsTypeDef

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# ExecutionTimedOutEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# GetActivityTaskInputRequestTypeDef

### activityArn
- **Type**: <class 'str'>
- **Required**: Yes

### workerName
- **Type**: typing.Optional[str]


# GetActivityTaskOutputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### reverseOrder
- **Type**: typing.Optional[bool]

### includeExecutionData
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# GetExecutionHistoryInputRequestTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]

### nextToken
- **Type**: typing.Optional[str]

### includeExecutionData
- **Type**: typing.Optional[bool]


# GetExecutionHistoryOutputTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HistoryEventExecutionDataDetailsTypeDef

### truncated
- **Type**: typing.Optional[bool]


# HistoryEventTypeDef

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ActivityFailed', 'ActivityScheduleFailed', 'ActivityScheduled', 'ActivityStarted', 'ActivitySucceeded', 'ActivityTimedOut', 'ChoiceStateEntered', 'ChoiceStateExited', 'ExecutionAborted', 'ExecutionFailed', 'ExecutionRedriven', 'ExecutionStarted', 'ExecutionSucceeded', 'ExecutionTimedOut', 'FailStateEntered', 'LambdaFunctionFailed', 'LambdaFunctionScheduleFailed', 'LambdaFunctionScheduled', 'LambdaFunctionStartFailed', 'LambdaFunctionStarted', 'LambdaFunctionSucceeded', 'LambdaFunctionTimedOut', 'MapIterationAborted', 'MapIterationFailed', 'MapIterationStarted', 'MapIterationSucceeded', 'MapRunAborted', 'MapRunFailed', 'MapRunRedriven', 'MapRunStarted', 'MapRunSucceeded', 'MapStateAborted', 'MapStateEntered', 'MapStateExited', 'MapStateFailed', 'MapStateStarted', 'MapStateSucceeded', 'ParallelStateAborted', 'ParallelStateEntered', 'ParallelStateExited', 'ParallelStateFailed', 'ParallelStateStarted', 'ParallelStateSucceeded', 'PassStateEntered', 'PassStateExited', 'SucceedStateEntered', 'SucceedStateExited', 'TaskFailed', 'TaskScheduled', 'TaskStartFailed', 'TaskStarted', 'TaskStateAborted', 'TaskStateEntered', 'TaskStateExited', 'TaskSubmitFailed', 'TaskSubmitted', 'TaskSucceeded', 'TaskTimedOut', 'WaitStateAborted', 'WaitStateEntered', 'WaitStateExited']
- **Required**: Yes

### id
- **Type**: <class 'int'>
- **Required**: Yes

### previousEventId
- **Type**: typing.Optional[int]

### activityFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityFailedEventDetailsTypeDef]

### activityScheduleFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityScheduleFailedEventDetailsTypeDef]

### activityScheduledEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityScheduledEventDetailsTypeDef]

### activityStartedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityStartedEventDetailsTypeDef]

### activitySucceededEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivitySucceededEventDetailsTypeDef]

### activityTimedOutEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityTimedOutEventDetailsTypeDef]

### taskFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskFailedEventDetailsTypeDef]

### taskScheduledEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskScheduledEventDetailsTypeDef]

### taskStartFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskStartFailedEventDetailsTypeDef]

### taskStartedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskStartedEventDetailsTypeDef]

### taskSubmitFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskSubmitFailedEventDetailsTypeDef]

### taskSubmittedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskSubmittedEventDetailsTypeDef]

### taskSucceededEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskSucceededEventDetailsTypeDef]

### taskTimedOutEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskTimedOutEventDetailsTypeDef]

### executionFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionFailedEventDetailsTypeDef]

### executionStartedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionStartedEventDetailsTypeDef]

### executionSucceededEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionSucceededEventDetailsTypeDef]

### executionAbortedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionAbortedEventDetailsTypeDef]

### executionTimedOutEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionTimedOutEventDetailsTypeDef]

### executionRedrivenEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionRedrivenEventDetailsTypeDef]

### mapStateStartedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapStateStartedEventDetailsTypeDef]

### mapIterationStartedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapIterationEventDetailsTypeDef]

### mapIterationSucceededEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapIterationEventDetailsTypeDef]

### mapIterationFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapIterationEventDetailsTypeDef]

### mapIterationAbortedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapIterationEventDetailsTypeDef]

### lambdaFunctionFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LambdaFunctionFailedEventDetailsTypeDef]

### lambdaFunctionScheduleFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LambdaFunctionScheduleFailedEventDetailsTypeDef]

### lambdaFunctionScheduledEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LambdaFunctionScheduledEventDetailsTypeDef]

### lambdaFunctionStartFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LambdaFunctionStartFailedEventDetailsTypeDef]

### lambdaFunctionSucceededEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LambdaFunctionSucceededEventDetailsTypeDef]

### lambdaFunctionTimedOutEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LambdaFunctionTimedOutEventDetailsTypeDef]

### stateEnteredEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.StateEnteredEventDetailsTypeDef]

### stateExitedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.StateExitedEventDetailsTypeDef]

### mapRunStartedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunStartedEventDetailsTypeDef]

### mapRunFailedEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunFailedEventDetailsTypeDef]

### mapRunRedrivenEventDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunRedrivenEventDetailsTypeDef]


# InspectionDataRequestTypeDef

### protocol
- **Type**: typing.Optional[str]

### method
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]


# InspectionDataResponseTypeDef

### protocol
- **Type**: typing.Optional[str]

### statusCode
- **Type**: typing.Optional[str]

### statusMessage
- **Type**: typing.Optional[str]

### headers
- **Type**: typing.Optional[str]

### body
- **Type**: typing.Optional[str]


# InspectionDataTypeDef

### input
- **Type**: typing.Optional[str]

### afterInputPath
- **Type**: typing.Optional[str]

### afterParameters
- **Type**: typing.Optional[str]

### result
- **Type**: typing.Optional[str]

### afterResultSelector
- **Type**: typing.Optional[str]

### afterResultPath
- **Type**: typing.Optional[str]

### request
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.InspectionDataRequestTypeDef]

### response
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.InspectionDataResponseTypeDef]


# LambdaFunctionFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionScheduleFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionScheduledEventDetailsTypeDef

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Optional[str]

### inputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]

### timeoutInSeconds
- **Type**: typing.Optional[int]

### taskCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskCredentialsTypeDef]


# LambdaFunctionStartFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# LambdaFunctionSucceededEventDetailsTypeDef

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# LambdaFunctionTimedOutEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# ListActivitiesInputListActivitiesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListActivitiesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActivitiesOutputTypeDef

### activities
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ActivityListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExecutionsInputListExecutionsPaginateTypeDef

### stateMachineArn
- **Type**: typing.Optional[str]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']]

### mapRunArn
- **Type**: typing.Optional[str]

### redriveFilter
- **Type**: typing.Optional[typing.Literal['NOT_REDRIVEN', 'REDRIVEN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListExecutionsInputRequestTypeDef

### stateMachineArn
- **Type**: typing.Optional[str]

### statusFilter
- **Type**: typing.Optional[typing.Literal['ABORTED', 'FAILED', 'PENDING_REDRIVE', 'RUNNING', 'SUCCEEDED', 'TIMED_OUT']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### mapRunArn
- **Type**: typing.Optional[str]

### redriveFilter
- **Type**: typing.Optional[typing.Literal['NOT_REDRIVEN', 'REDRIVEN']]


# ListExecutionsOutputTypeDef

### executions
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ExecutionListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMapRunsInputListMapRunsPaginateTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListMapRunsInputRequestTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMapRunsOutputTypeDef

### mapRuns
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.MapRunListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStateMachineAliasesInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStateMachineAliasesOutputTypeDef

### stateMachineAliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineAliasListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStateMachineVersionsInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStateMachineVersionsOutputTypeDef

### stateMachineVersions
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineVersionListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStateMachinesInputListStateMachinesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.PaginatorConfigTypeDef]


# ListStateMachinesInputRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStateMachinesOutputTypeDef

### stateMachines
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.StateMachineListItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogDestinationTypeDef

### cloudWatchLogsLogGroup
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.CloudWatchLogsLogGroupTypeDef]


# LoggingConfigurationOutputTypeDef

### level
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### includeExecutionData
- **Type**: typing.Optional[bool]

### destinations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.LogDestinationTypeDef]]


# LoggingConfigurationTypeDef

### level
- **Type**: typing.Optional[typing.Literal['ALL', 'ERROR', 'FATAL', 'OFF']]

### includeExecutionData
- **Type**: typing.Optional[bool]

### destinations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.LogDestinationTypeDef]]


# MapIterationEventDetailsTypeDef

### name
- **Type**: typing.Optional[str]

### index
- **Type**: typing.Optional[int]


# MapRunExecutionCountsTypeDef

### pending
- **Type**: <class 'int'>
- **Required**: Yes

### running
- **Type**: <class 'int'>
- **Required**: Yes

### succeeded
- **Type**: <class 'int'>
- **Required**: Yes

### failed
- **Type**: <class 'int'>
- **Required**: Yes

### timedOut
- **Type**: <class 'int'>
- **Required**: Yes

### aborted
- **Type**: <class 'int'>
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes

### resultsWritten
- **Type**: <class 'int'>
- **Required**: Yes

### failuresNotRedrivable
- **Type**: typing.Optional[int]

### pendingRedrive
- **Type**: typing.Optional[int]


# MapRunFailedEventDetailsTypeDef

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# MapRunItemCountsTypeDef

### pending
- **Type**: <class 'int'>
- **Required**: Yes

### running
- **Type**: <class 'int'>
- **Required**: Yes

### succeeded
- **Type**: <class 'int'>
- **Required**: Yes

### failed
- **Type**: <class 'int'>
- **Required**: Yes

### timedOut
- **Type**: <class 'int'>
- **Required**: Yes

### aborted
- **Type**: <class 'int'>
- **Required**: Yes

### total
- **Type**: <class 'int'>
- **Required**: Yes

### resultsWritten
- **Type**: <class 'int'>
- **Required**: Yes

### failuresNotRedrivable
- **Type**: typing.Optional[int]

### pendingRedrive
- **Type**: typing.Optional[int]


# MapRunListItemTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: typing.Optional[datetime.datetime]


# MapRunRedrivenEventDetailsTypeDef

### mapRunArn
- **Type**: typing.Optional[str]

### redriveCount
- **Type**: typing.Optional[int]


# MapRunStartedEventDetailsTypeDef

### mapRunArn
- **Type**: typing.Optional[str]


# MapStateStartedEventDetailsTypeDef

### length
- **Type**: typing.Optional[int]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishStateMachineVersionInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# PublishStateMachineVersionOutputTypeDef

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RedriveExecutionInputRequestTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# RedriveExecutionOutputTypeDef

### redriveDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
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


# RoutingConfigurationListItemTypeDef

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### weight
- **Type**: <class 'int'>
- **Required**: Yes


# SendTaskFailureInputRequestTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# SendTaskHeartbeatInputRequestTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes


# SendTaskSuccessInputRequestTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# StartExecutionInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### input
- **Type**: typing.Optional[str]

### traceHeader
- **Type**: typing.Optional[str]


# StartExecutionOutputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartSyncExecutionInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### input
- **Type**: typing.Optional[str]

### traceHeader
- **Type**: typing.Optional[str]


# StartSyncExecutionOutputTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### startDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### stopDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['FAILED', 'SUCCEEDED', 'TIMED_OUT']
- **Required**: Yes

### error
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: <class 'str'>
- **Required**: Yes

### inputDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.CloudWatchEventsExecutionDataDetailsTypeDef'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes

### outputDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.CloudWatchEventsExecutionDataDetailsTypeDef'>
- **Required**: Yes

### traceHeader
- **Type**: <class 'str'>
- **Required**: Yes

### billingDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.BillingDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StateEnteredEventDetailsTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Optional[str]

### inputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# StateExitedEventDetailsTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# StateMachineAliasListItemTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StateMachineListItemTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['EXPRESS', 'STANDARD']
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StateMachineVersionListItemTypeDef

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# StopExecutionInputRequestTypeDef

### executionArn
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# StopExecutionOutputTypeDef

### stopDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# TaskCredentialsTypeDef

### roleArn
- **Type**: typing.Optional[str]


# TaskFailedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TaskScheduledEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### region
- **Type**: <class 'str'>
- **Required**: Yes

### parameters
- **Type**: <class 'str'>
- **Required**: Yes

### timeoutInSeconds
- **Type**: typing.Optional[int]

### heartbeatInSeconds
- **Type**: typing.Optional[int]

### taskCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TaskCredentialsTypeDef]


# TaskStartFailedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TaskStartedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes


# TaskSubmitFailedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TaskSubmittedEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# TaskSucceededEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: typing.Optional[str]

### outputDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.HistoryEventExecutionDataDetailsTypeDef]


# TaskTimedOutEventDetailsTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### resource
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[str]


# TestStateInputRequestTypeDef

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Optional[str]

### inspectionLevel
- **Type**: typing.Optional[typing.Literal['DEBUG', 'INFO', 'TRACE']]

### revealSecrets
- **Type**: typing.Optional[bool]


# TestStateOutputTypeDef

### output
- **Type**: <class 'str'>
- **Required**: Yes

### error
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: <class 'str'>
- **Required**: Yes

### inspectionData
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.InspectionDataTypeDef'>
- **Required**: Yes

### nextState
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CAUGHT_ERROR', 'FAILED', 'RETRIABLE', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TracingConfigurationTypeDef

### enabled
- **Type**: typing.Optional[bool]


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMapRunInputRequestTypeDef

### mapRunArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxConcurrency
- **Type**: typing.Optional[int]

### toleratedFailurePercentage
- **Type**: typing.Optional[float]

### toleratedFailureCount
- **Type**: typing.Optional[int]


# UpdateStateMachineAliasInputRequestTypeDef

### stateMachineAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### routingConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.stepfunctions_classes.RoutingConfigurationListItemTypeDef]]


# UpdateStateMachineAliasOutputTypeDef

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStateMachineInputRequestTypeDef

### stateMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### loggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.LoggingConfigurationTypeDef]

### tracingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.stepfunctions_classes.TracingConfigurationTypeDef]

### publish
- **Type**: typing.Optional[bool]

### versionDescription
- **Type**: typing.Optional[str]


# UpdateStateMachineOutputTypeDef

### updateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### stateMachineVersionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidateStateMachineDefinitionDiagnosticTypeDef

### severity
- **Type**: typing.Literal['ERROR']
- **Required**: Yes

### code
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### location
- **Type**: typing.Optional[str]


# ValidateStateMachineDefinitionInputRequestTypeDef

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['EXPRESS', 'STANDARD']]


# ValidateStateMachineDefinitionOutputTypeDef

### result
- **Type**: typing.Literal['FAIL', 'OK']
- **Required**: Yes

### diagnostics
- **Type**: typing.List[aws_resource_validator.pydantic_models.stepfunctions_classes.ValidateStateMachineDefinitionDiagnosticTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.stepfunctions_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


