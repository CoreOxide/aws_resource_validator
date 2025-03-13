# Swf Classes

# ActivityTaskCancelRequestedEventAttributesTypeDef

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### activityId
- **Type**: <class 'str'>
- **Required**: Yes


# ActivityTaskCanceledEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]

### latestCancelRequestedEventId
- **Type**: typing.Optional[int]


# ActivityTaskCompletedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# ActivityTaskFailedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# ActivityTaskScheduledEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivityTaskStartedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]


# ActivityTaskStatusTypeDef

### cancelRequested
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActivityTaskTimedOutEventAttributesTypeDef

### timeoutType
- **Type**: typing.Literal['HEARTBEAT', 'SCHEDULE_TO_CLOSE', 'SCHEDULE_TO_START', 'START_TO_CLOSE']
- **Required**: Yes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# ActivityTypeConfigurationTypeDef

### defaultTaskStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultTaskHeartbeatTimeout
- **Type**: typing.Optional[str]

### defaultTaskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultTaskScheduleToStartTimeout
- **Type**: typing.Optional[str]

### defaultTaskScheduleToCloseTimeout
- **Type**: typing.Optional[str]


# ActivityTypeDetailTypeDef

### typeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeInfoTypeDef'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActivityTypeInfoTypeDef

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### deprecationDate
- **Type**: typing.Optional[datetime.datetime]


# ActivityTypeInfosTypeDef

### typeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.ActivityTypeInfoTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActivityTypeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTimerDecisionAttributesTypeDef

### timerId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelTimerFailedEventAttributesTypeDef

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'TIMER_ID_UNKNOWN']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# CancelWorkflowExecutionDecisionAttributesTypeDef

### details
- **Type**: typing.Optional[str]


# CancelWorkflowExecutionFailedEventAttributesTypeDef

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ChildWorkflowExecutionCanceledEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# ChildWorkflowExecutionCompletedEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# ChildWorkflowExecutionFailedEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# ChildWorkflowExecutionStartedEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ChildWorkflowExecutionTerminatedEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ChildWorkflowExecutionTimedOutEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### timeoutType
- **Type**: typing.Literal['START_TO_CLOSE']
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# CloseStatusFilterTypeDef

### status
- **Type**: typing.Literal['CANCELED', 'COMPLETED', 'CONTINUED_AS_NEW', 'FAILED', 'TERMINATED', 'TIMED_OUT']
- **Required**: Yes


# CompleteWorkflowExecutionDecisionAttributesTypeDef

### result
- **Type**: typing.Optional[str]


# CompleteWorkflowExecutionFailedEventAttributesTypeDef

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef

### cause
- **Type**: typing.Literal['CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED', 'DEFAULT_CHILD_POLICY_UNDEFINED', 'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED', 'DEFAULT_TASK_LIST_UNDEFINED', 'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED', 'OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION', 'WORKFLOW_TYPE_DEPRECATED', 'WORKFLOW_TYPE_DOES_NOT_EXIST']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# CountClosedWorkflowExecutionsInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef]

### closeTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilterTypeDef]

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilterTypeDef]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilterTypeDef]

### closeStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CloseStatusFilterTypeDef]


# CountOpenWorkflowExecutionsInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef'>
- **Required**: Yes

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilterTypeDef]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilterTypeDef]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilterTypeDef]


# CountPendingActivityTasksInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef'>
- **Required**: Yes


# CountPendingDecisionTasksInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef'>
- **Required**: Yes


# DecisionTaskCompletedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### executionContext
- **Type**: typing.Optional[str]

### taskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef]

### taskListScheduleToStartTimeout
- **Type**: typing.Optional[str]


# DecisionTaskScheduledEventAttributesTypeDef

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef'>
- **Required**: Yes

### taskPriority
- **Type**: typing.Optional[str]

### startToCloseTimeout
- **Type**: typing.Optional[str]

### scheduleToStartTimeout
- **Type**: typing.Optional[str]


# DecisionTaskStartedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]


# DecisionTaskTimedOutEventAttributesTypeDef

### timeoutType
- **Type**: typing.Literal['SCHEDULE_TO_START', 'START_TO_CLOSE']
- **Required**: Yes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# DecisionTaskTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.HistoryEventTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### previousStartedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DecisionTypeDef

### decisionType
- **Type**: typing.Literal['CancelTimer', 'CancelWorkflowExecution', 'CompleteWorkflowExecution', 'ContinueAsNewWorkflowExecution', 'FailWorkflowExecution', 'RecordMarker', 'RequestCancelActivityTask', 'RequestCancelExternalWorkflowExecution', 'ScheduleActivityTask', 'ScheduleLambdaFunction', 'SignalExternalWorkflowExecution', 'StartChildWorkflowExecution', 'StartTimer']
- **Required**: Yes

### scheduleActivityTaskDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleActivityTaskDecisionAttributesTypeDef]

### requestCancelActivityTaskDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelActivityTaskDecisionAttributesTypeDef]

### completeWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CompleteWorkflowExecutionDecisionAttributesTypeDef]

### failWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.FailWorkflowExecutionDecisionAttributesTypeDef]

### cancelWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelWorkflowExecutionDecisionAttributesTypeDef]

### continueAsNewWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef]

### recordMarkerDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RecordMarkerDecisionAttributesTypeDef]

### startTimerDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartTimerDecisionAttributesTypeDef]

### cancelTimerDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelTimerDecisionAttributesTypeDef]

### signalExternalWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.SignalExternalWorkflowExecutionDecisionAttributesTypeDef]

### requestCancelExternalWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef]

### startChildWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartChildWorkflowExecutionDecisionAttributesTypeDef]

### scheduleLambdaFunctionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleLambdaFunctionDecisionAttributesTypeDef]


# DeleteActivityTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeTypeDef'>
- **Required**: Yes


# DeleteWorkflowTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes


# DeprecateActivityTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeTypeDef'>
- **Required**: Yes


# DeprecateDomainInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecateWorkflowTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes


# DescribeActivityTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeTypeDef'>
- **Required**: Yes


# DescribeDomainInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkflowExecutionInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes


# DescribeWorkflowTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes


# DomainConfigurationTypeDef

### workflowExecutionRetentionPeriodInDays
- **Type**: <class 'str'>
- **Required**: Yes


# DomainDetailTypeDef

### domainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.DomainInfoTypeDef'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.DomainConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainInfoTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]


# DomainInfosTypeDef

### domainInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.DomainInfoTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExecutionTimeFilterTypeDef

### oldestDate
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TimestampTypeDef'>
- **Required**: Yes

### latestDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TimestampTypeDef]


# ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ExternalWorkflowExecutionSignaledEventAttributesTypeDef

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# FailWorkflowExecutionDecisionAttributesTypeDef

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# FailWorkflowExecutionFailedEventAttributesTypeDef

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# GetWorkflowExecutionHistoryInputPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfigTypeDef]


# GetWorkflowExecutionHistoryInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# HistoryEventTypeDef

### eventTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### eventType
- **Type**: typing.Literal['ActivityTaskCancelRequested', 'ActivityTaskCanceled', 'ActivityTaskCompleted', 'ActivityTaskFailed', 'ActivityTaskScheduled', 'ActivityTaskStarted', 'ActivityTaskTimedOut', 'CancelTimerFailed', 'CancelWorkflowExecutionFailed', 'ChildWorkflowExecutionCanceled', 'ChildWorkflowExecutionCompleted', 'ChildWorkflowExecutionFailed', 'ChildWorkflowExecutionStarted', 'ChildWorkflowExecutionTerminated', 'ChildWorkflowExecutionTimedOut', 'CompleteWorkflowExecutionFailed', 'ContinueAsNewWorkflowExecutionFailed', 'DecisionTaskCompleted', 'DecisionTaskScheduled', 'DecisionTaskStarted', 'DecisionTaskTimedOut', 'ExternalWorkflowExecutionCancelRequested', 'ExternalWorkflowExecutionSignaled', 'FailWorkflowExecutionFailed', 'LambdaFunctionCompleted', 'LambdaFunctionFailed', 'LambdaFunctionScheduled', 'LambdaFunctionStarted', 'LambdaFunctionTimedOut', 'MarkerRecorded', 'RecordMarkerFailed', 'RequestCancelActivityTaskFailed', 'RequestCancelExternalWorkflowExecutionFailed', 'RequestCancelExternalWorkflowExecutionInitiated', 'ScheduleActivityTaskFailed', 'ScheduleLambdaFunctionFailed', 'SignalExternalWorkflowExecutionFailed', 'SignalExternalWorkflowExecutionInitiated', 'StartChildWorkflowExecutionFailed', 'StartChildWorkflowExecutionInitiated', 'StartLambdaFunctionFailed', 'StartTimerFailed', 'TimerCanceled', 'TimerFired', 'TimerStarted', 'WorkflowExecutionCancelRequested', 'WorkflowExecutionCanceled', 'WorkflowExecutionCompleted', 'WorkflowExecutionContinuedAsNew', 'WorkflowExecutionFailed', 'WorkflowExecutionSignaled', 'WorkflowExecutionStarted', 'WorkflowExecutionTerminated', 'WorkflowExecutionTimedOut']
- **Required**: Yes

### eventId
- **Type**: <class 'int'>
- **Required**: Yes

### workflowExecutionStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionStartedEventAttributesTypeDef]

### workflowExecutionCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionCompletedEventAttributesTypeDef]

### completeWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CompleteWorkflowExecutionFailedEventAttributesTypeDef]

### workflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFailedEventAttributesTypeDef]

### failWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.FailWorkflowExecutionFailedEventAttributesTypeDef]

### workflowExecutionTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTimedOutEventAttributesTypeDef]

### workflowExecutionCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionCanceledEventAttributesTypeDef]

### cancelWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelWorkflowExecutionFailedEventAttributesTypeDef]

### workflowExecutionContinuedAsNewEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionContinuedAsNewEventAttributesTypeDef]

### continueAsNewWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef]

### workflowExecutionTerminatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTerminatedEventAttributesTypeDef]

### workflowExecutionCancelRequestedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionCancelRequestedEventAttributesTypeDef]

### decisionTaskScheduledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskScheduledEventAttributesTypeDef]

### decisionTaskStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskStartedEventAttributesTypeDef]

### decisionTaskCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskCompletedEventAttributesTypeDef]

### decisionTaskTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskTimedOutEventAttributesTypeDef]

### activityTaskScheduledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskScheduledEventAttributesTypeDef]

### activityTaskStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskStartedEventAttributesTypeDef]

### activityTaskCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskCompletedEventAttributesTypeDef]

### activityTaskFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskFailedEventAttributesTypeDef]

### activityTaskTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskTimedOutEventAttributesTypeDef]

### activityTaskCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskCanceledEventAttributesTypeDef]

### activityTaskCancelRequestedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskCancelRequestedEventAttributesTypeDef]

### workflowExecutionSignaledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionSignaledEventAttributesTypeDef]

### markerRecordedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.MarkerRecordedEventAttributesTypeDef]

### recordMarkerFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RecordMarkerFailedEventAttributesTypeDef]

### timerStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TimerStartedEventAttributesTypeDef]

### timerFiredEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TimerFiredEventAttributesTypeDef]

### timerCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TimerCanceledEventAttributesTypeDef]

### startChildWorkflowExecutionInitiatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartChildWorkflowExecutionInitiatedEventAttributesTypeDef]

### childWorkflowExecutionStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionStartedEventAttributesTypeDef]

### childWorkflowExecutionCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionCompletedEventAttributesTypeDef]

### childWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionFailedEventAttributesTypeDef]

### childWorkflowExecutionTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionTimedOutEventAttributesTypeDef]

### childWorkflowExecutionCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionCanceledEventAttributesTypeDef]

### childWorkflowExecutionTerminatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionTerminatedEventAttributesTypeDef]

### signalExternalWorkflowExecutionInitiatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef]

### externalWorkflowExecutionSignaledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExternalWorkflowExecutionSignaledEventAttributesTypeDef]

### signalExternalWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.SignalExternalWorkflowExecutionFailedEventAttributesTypeDef]

### externalWorkflowExecutionCancelRequestedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef]

### requestCancelExternalWorkflowExecutionInitiatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef]

### requestCancelExternalWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef]

### scheduleActivityTaskFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleActivityTaskFailedEventAttributesTypeDef]

### requestCancelActivityTaskFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelActivityTaskFailedEventAttributesTypeDef]

### startTimerFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartTimerFailedEventAttributesTypeDef]

### cancelTimerFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelTimerFailedEventAttributesTypeDef]

### startChildWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartChildWorkflowExecutionFailedEventAttributesTypeDef]

### lambdaFunctionScheduledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionScheduledEventAttributesTypeDef]

### lambdaFunctionStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionStartedEventAttributesTypeDef]

### lambdaFunctionCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionCompletedEventAttributesTypeDef]

### lambdaFunctionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionFailedEventAttributesTypeDef]

### lambdaFunctionTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionTimedOutEventAttributesTypeDef]

### scheduleLambdaFunctionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleLambdaFunctionFailedEventAttributesTypeDef]

### startLambdaFunctionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartLambdaFunctionFailedEventAttributesTypeDef]


# HistoryTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.HistoryEventTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LambdaFunctionCompletedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# LambdaFunctionFailedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# LambdaFunctionScheduledEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LambdaFunctionStartedEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes


# LambdaFunctionTimedOutEventAttributesTypeDef

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### timeoutType
- **Type**: typing.Optional[typing.Literal['START_TO_CLOSE']]


# ListActivityTypesInputPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfigTypeDef]


# ListActivityTypesInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# ListClosedWorkflowExecutionsInputPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef]

### closeTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilterTypeDef]

### closeStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CloseStatusFilterTypeDef]

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilterTypeDef]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilterTypeDef]

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfigTypeDef]


# ListClosedWorkflowExecutionsInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef]

### closeTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilterTypeDef]

### closeStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CloseStatusFilterTypeDef]

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilterTypeDef]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilterTypeDef]

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# ListDomainsInputPaginateTypeDef

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfigTypeDef]


# ListDomainsInputTypeDef

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# ListOpenWorkflowExecutionsInputPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef'>
- **Required**: Yes

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilterTypeDef]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilterTypeDef]

### reverseOrder
- **Type**: typing.Optional[bool]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfigTypeDef]


# ListOpenWorkflowExecutionsInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilterTypeDef'>
- **Required**: Yes

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilterTypeDef]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilterTypeDef]

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilterTypeDef]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.ResourceTagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowTypesInputPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfigTypeDef]


# ListWorkflowTypesInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# MarkerRecordedEventAttributesTypeDef

### markerName
- **Type**: <class 'str'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingTaskCountTypeDef

### count
- **Type**: <class 'int'>
- **Required**: Yes

### truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PollForActivityTaskInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]


# PollForDecisionTaskInputPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]

### startAtPreviousStartedEvent
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfigTypeDef]


# PollForDecisionTaskInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]

### startAtPreviousStartedEvent
- **Type**: typing.Optional[bool]


# RecordActivityTaskHeartbeatInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# RecordMarkerDecisionAttributesTypeDef

### markerName
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# RecordMarkerFailedEventAttributesTypeDef

### markerName
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# RegisterActivityTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### defaultTaskStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultTaskHeartbeatTimeout
- **Type**: typing.Optional[str]

### defaultTaskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultTaskScheduleToStartTimeout
- **Type**: typing.Optional[str]

### defaultTaskScheduleToCloseTimeout
- **Type**: typing.Optional[str]


# RegisterDomainInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workflowExecutionRetentionPeriodInDays
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.swf_classes.ResourceTagTypeDef]]


# RegisterWorkflowTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### defaultTaskStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultExecutionStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultTaskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultChildPolicy
- **Type**: typing.Optional[typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']]

### defaultLambdaRole
- **Type**: typing.Optional[str]


# RequestCancelActivityTaskDecisionAttributesTypeDef

### activityId
- **Type**: <class 'str'>
- **Required**: Yes


# RequestCancelActivityTaskFailedEventAttributesTypeDef

### activityId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['ACTIVITY_ID_UNKNOWN', 'OPERATION_NOT_PERMITTED']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]

### control
- **Type**: typing.Optional[str]


# RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED', 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION']
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]

### control
- **Type**: typing.Optional[str]


# RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]

### control
- **Type**: typing.Optional[str]


# RequestCancelWorkflowExecutionInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]


# ResourceTagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# RespondActivityTaskCanceledInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# RespondActivityTaskCompletedInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# RespondActivityTaskFailedInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# RespondDecisionTaskCompletedInputTypeDef

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### decisions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.swf_classes.DecisionTypeDef]]

### executionContext
- **Type**: typing.Optional[str]

### taskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef]

### taskListScheduleToStartTimeout
- **Type**: typing.Optional[str]


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


# RunTypeDef

### runId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ScheduleActivityTaskDecisionAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduleActivityTaskFailedEventAttributesTypeDef

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeTypeDef'>
- **Required**: Yes

### activityId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['ACTIVITY_CREATION_RATE_EXCEEDED', 'ACTIVITY_ID_ALREADY_IN_USE', 'ACTIVITY_TYPE_DEPRECATED', 'ACTIVITY_TYPE_DOES_NOT_EXIST', 'DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED', 'DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED', 'DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED', 'DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED', 'DEFAULT_TASK_LIST_UNDEFINED', 'OPEN_ACTIVITIES_LIMIT_EXCEEDED', 'OPERATION_NOT_PERMITTED']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ScheduleLambdaFunctionDecisionAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduleLambdaFunctionFailedEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalExternalWorkflowExecutionDecisionAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalExternalWorkflowExecutionFailedEventAttributesTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED', 'UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION']
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]

### control
- **Type**: typing.Optional[str]


# SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartChildWorkflowExecutionDecisionAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartChildWorkflowExecutionFailedEventAttributesTypeDef

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['CHILD_CREATION_RATE_EXCEEDED', 'DEFAULT_CHILD_POLICY_UNDEFINED', 'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED', 'DEFAULT_TASK_LIST_UNDEFINED', 'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED', 'OPEN_CHILDREN_LIMIT_EXCEEDED', 'OPEN_WORKFLOWS_LIMIT_EXCEEDED', 'OPERATION_NOT_PERMITTED', 'WORKFLOW_ALREADY_RUNNING', 'WORKFLOW_TYPE_DEPRECATED', 'WORKFLOW_TYPE_DOES_NOT_EXIST']
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### control
- **Type**: typing.Optional[str]


# StartChildWorkflowExecutionInitiatedEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartLambdaFunctionFailedEventAttributesTypeDef

### scheduledEventId
- **Type**: typing.Optional[int]

### cause
- **Type**: typing.Optional[typing.Literal['ASSUME_ROLE_FAILED']]

### message
- **Type**: typing.Optional[str]


# StartTimerDecisionAttributesTypeDef

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### startToFireTimeout
- **Type**: <class 'str'>
- **Required**: Yes

### control
- **Type**: typing.Optional[str]


# StartTimerFailedEventAttributesTypeDef

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPEN_TIMERS_LIMIT_EXCEEDED', 'OPERATION_NOT_PERMITTED', 'TIMER_CREATION_RATE_EXCEEDED', 'TIMER_ID_ALREADY_IN_USE']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# TagFilterTypeDef

### tag
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.swf_classes.ResourceTagTypeDef]
- **Required**: Yes


# TaskListTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkflowExecutionInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]

### childPolicy
- **Type**: typing.Optional[typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']]


# TimerCanceledEventAttributesTypeDef

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# TimerFiredEventAttributesTypeDef

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# TimerStartedEventAttributesTypeDef

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### startToFireTimeout
- **Type**: <class 'str'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### control
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UndeprecateActivityTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeTypeDef'>
- **Required**: Yes


# UndeprecateDomainInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# UndeprecateWorkflowTypeInputTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WorkflowExecutionCancelRequestedEventAttributesTypeDef

### externalWorkflowExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef]

### externalInitiatedEventId
- **Type**: typing.Optional[int]

### cause
- **Type**: typing.Optional[typing.Literal['CHILD_POLICY_APPLIED']]


# WorkflowExecutionCanceledEventAttributesTypeDef

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# WorkflowExecutionCompletedEventAttributesTypeDef

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# WorkflowExecutionConfigurationTypeDef

### taskStartToCloseTimeout
- **Type**: <class 'str'>
- **Required**: Yes

### executionStartToCloseTimeout
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef'>
- **Required**: Yes

### childPolicy
- **Type**: typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']
- **Required**: Yes

### taskPriority
- **Type**: typing.Optional[str]

### lambdaRole
- **Type**: typing.Optional[str]


# WorkflowExecutionContinuedAsNewEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionCountTypeDef

### count
- **Type**: <class 'int'>
- **Required**: Yes

### truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowExecutionDetailTypeDef

### executionInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionInfoTypeDef'>
- **Required**: Yes

### executionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionConfigurationTypeDef'>
- **Required**: Yes

### openCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionOpenCountsTypeDef'>
- **Required**: Yes

### latestActivityTaskTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### latestExecutionContext
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowExecutionFailedEventAttributesTypeDef

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# WorkflowExecutionFilterTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowExecutionInfoTypeDef

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### startTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### executionStatus
- **Type**: typing.Literal['CLOSED', 'OPEN']
- **Required**: Yes

### closeTimestamp
- **Type**: typing.Optional[datetime.datetime]

### closeStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'CONTINUED_AS_NEW', 'FAILED', 'TERMINATED', 'TIMED_OUT']]

### parent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTypeDef]

### tagList
- **Type**: typing.Optional[typing.List[str]]

### cancelRequested
- **Type**: typing.Optional[bool]


# WorkflowExecutionInfosTypeDef

### executionInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionInfoTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowExecutionOpenCountsTypeDef

### openActivityTasks
- **Type**: <class 'int'>
- **Required**: Yes

### openDecisionTasks
- **Type**: <class 'int'>
- **Required**: Yes

### openTimers
- **Type**: <class 'int'>
- **Required**: Yes

### openChildWorkflowExecutions
- **Type**: <class 'int'>
- **Required**: Yes

### openLambdaFunctions
- **Type**: typing.Optional[int]


# WorkflowExecutionSignaledEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionStartedEventAttributesTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionTerminatedEventAttributesTypeDef

### childPolicy
- **Type**: typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[typing.Literal['CHILD_POLICY_APPLIED', 'EVENT_LIMIT_EXCEEDED', 'OPERATOR_INITIATED']]


# WorkflowExecutionTimedOutEventAttributesTypeDef

### timeoutType
- **Type**: typing.Literal['START_TO_CLOSE']
- **Required**: Yes

### childPolicy
- **Type**: typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']
- **Required**: Yes


# WorkflowExecutionTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowTypeConfigurationTypeDef

### defaultTaskStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultExecutionStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultTaskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskListTypeDef]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultChildPolicy
- **Type**: typing.Optional[typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']]

### defaultLambdaRole
- **Type**: typing.Optional[str]


# WorkflowTypeDetailTypeDef

### typeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeInfoTypeDef'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowTypeFilterTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]


# WorkflowTypeInfoTypeDef

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeTypeDef'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### creationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### deprecationDate
- **Type**: typing.Optional[datetime.datetime]


# WorkflowTypeInfosTypeDef

### typeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeInfoTypeDef]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowTypeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


