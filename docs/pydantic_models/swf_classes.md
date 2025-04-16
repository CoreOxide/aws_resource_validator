# Swf Classes

# ActivityTaskCancelRequestedEventAttributes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### activityId
- **Type**: <class 'str'>
- **Required**: Yes


# ActivityTaskCanceledEventAttributes

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


# ActivityTaskCompletedEventAttributes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# ActivityTaskFailedEventAttributes

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


# ActivityTaskScheduledEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActivityTaskStartedEventAttributes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]


# ActivityTaskStatus

### cancelRequested
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# ActivityTaskTimedOutEventAttributes

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


# ActivityType

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# ActivityTypeConfiguration

### defaultTaskStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultTaskHeartbeatTimeout
- **Type**: typing.Optional[str]

### defaultTaskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskList]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultTaskScheduleToStartTimeout
- **Type**: typing.Optional[str]

### defaultTaskScheduleToCloseTimeout
- **Type**: typing.Optional[str]


# ActivityTypeDetail

### typeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeInfo'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityTypeConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# ActivityTypeInfo

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityType'>
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


# ActivityTypeInfos

### typeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.ActivityTypeInfo]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTimerDecisionAttributes

### timerId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelTimerFailedEventAttributes

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'TIMER_ID_UNKNOWN']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# CancelWorkflowExecutionDecisionAttributes

### details
- **Type**: typing.Optional[str]


# CancelWorkflowExecutionFailedEventAttributes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ChildWorkflowExecutionCanceledEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# ChildWorkflowExecutionCompletedEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# ChildWorkflowExecutionFailedEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
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


# ChildWorkflowExecutionStartedEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ChildWorkflowExecutionTerminatedEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ChildWorkflowExecutionTimedOutEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
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


# CloseStatusFilter

### status
- **Type**: typing.Literal['CANCELED', 'COMPLETED', 'CONTINUED_AS_NEW', 'FAILED', 'TERMINATED', 'TIMED_OUT']
- **Required**: Yes


# CompleteWorkflowExecutionDecisionAttributes

### result
- **Type**: typing.Optional[str]


# CompleteWorkflowExecutionFailedEventAttributes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ContinueAsNewWorkflowExecutionDecisionAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContinueAsNewWorkflowExecutionFailedEventAttributes

### cause
- **Type**: typing.Literal['CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED', 'DEFAULT_CHILD_POLICY_UNDEFINED', 'DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED', 'DEFAULT_TASK_LIST_UNDEFINED', 'DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED', 'OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION', 'WORKFLOW_TYPE_DEPRECATED', 'WORKFLOW_TYPE_DOES_NOT_EXIST']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# CountClosedWorkflowExecutionsInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter]

### closeTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilter]

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilter]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilter]

### closeStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CloseStatusFilter]


# CountOpenWorkflowExecutionsInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter'>
- **Required**: Yes

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilter]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilter]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilter]


# CountPendingActivityTasksInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskList'>
- **Required**: Yes


# CountPendingDecisionTasksInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskList'>
- **Required**: Yes


# Decision

### decisionType
- **Type**: typing.Literal['CancelTimer', 'CancelWorkflowExecution', 'CompleteWorkflowExecution', 'ContinueAsNewWorkflowExecution', 'FailWorkflowExecution', 'RecordMarker', 'RequestCancelActivityTask', 'RequestCancelExternalWorkflowExecution', 'ScheduleActivityTask', 'ScheduleLambdaFunction', 'SignalExternalWorkflowExecution', 'StartChildWorkflowExecution', 'StartTimer']
- **Required**: Yes

### scheduleActivityTaskDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleActivityTaskDecisionAttributes]

### requestCancelActivityTaskDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelActivityTaskDecisionAttributes]

### completeWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CompleteWorkflowExecutionDecisionAttributes]

### failWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.FailWorkflowExecutionDecisionAttributes]

### cancelWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelWorkflowExecutionDecisionAttributes]

### continueAsNewWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ContinueAsNewWorkflowExecutionDecisionAttributes]

### recordMarkerDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RecordMarkerDecisionAttributes]

### startTimerDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartTimerDecisionAttributes]

### cancelTimerDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelTimerDecisionAttributes]

### signalExternalWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.SignalExternalWorkflowExecutionDecisionAttributes]

### requestCancelExternalWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelExternalWorkflowExecutionDecisionAttributes]

### startChildWorkflowExecutionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartChildWorkflowExecutionDecisionAttributes]

### scheduleLambdaFunctionDecisionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleLambdaFunctionDecisionAttributes]


# DecisionTask

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.HistoryEvent]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### previousStartedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# DecisionTaskCompletedEventAttributes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### executionContext
- **Type**: typing.Optional[str]

### taskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskList]

### taskListScheduleToStartTimeout
- **Type**: typing.Optional[str]


# DecisionTaskScheduledEventAttributes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskList'>
- **Required**: Yes

### taskPriority
- **Type**: typing.Optional[str]

### startToCloseTimeout
- **Type**: typing.Optional[str]

### scheduleToStartTimeout
- **Type**: typing.Optional[str]


# DecisionTaskStartedEventAttributes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]


# DecisionTaskTimedOutEventAttributes

### timeoutType
- **Type**: typing.Literal['SCHEDULE_TO_START', 'START_TO_CLOSE']
- **Required**: Yes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteActivityTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityType'>
- **Required**: Yes


# DeleteWorkflowTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes


# DeprecateActivityTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityType'>
- **Required**: Yes


# DeprecateDomainInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeprecateWorkflowTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes


# DescribeActivityTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityType'>
- **Required**: Yes


# DescribeDomainInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkflowExecutionInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes


# DescribeWorkflowTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes


# DomainConfiguration

### workflowExecutionRetentionPeriodInDays
- **Type**: <class 'str'>
- **Required**: Yes


# DomainDetail

### domainInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.DomainInfo'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.DomainConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# DomainInfo

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


# DomainInfos

### domainInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.DomainInfo]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# ExecutionTimeFilter

### oldestDate
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.Timestamp'>
- **Required**: Yes

### latestDate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.Timestamp]


# ExternalWorkflowExecutionCancelRequestedEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# ExternalWorkflowExecutionSignaledEventAttributes

### workflowExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### initiatedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# FailWorkflowExecutionDecisionAttributes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# FailWorkflowExecutionFailedEventAttributes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED', 'UNHANDLED_DECISION']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# GetWorkflowExecutionHistoryInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# GetWorkflowExecutionHistoryInputPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfig]


# History

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.HistoryEvent]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# HistoryEvent

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionStartedEventAttributes]

### workflowExecutionCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionCompletedEventAttributes]

### completeWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CompleteWorkflowExecutionFailedEventAttributes]

### workflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFailedEventAttributes]

### failWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.FailWorkflowExecutionFailedEventAttributes]

### workflowExecutionTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTimedOutEventAttributes]

### workflowExecutionCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionCanceledEventAttributes]

### cancelWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelWorkflowExecutionFailedEventAttributes]

### workflowExecutionContinuedAsNewEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionContinuedAsNewEventAttributes]

### continueAsNewWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ContinueAsNewWorkflowExecutionFailedEventAttributes]

### workflowExecutionTerminatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionTerminatedEventAttributes]

### workflowExecutionCancelRequestedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionCancelRequestedEventAttributes]

### decisionTaskScheduledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskScheduledEventAttributes]

### decisionTaskStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskStartedEventAttributes]

### decisionTaskCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskCompletedEventAttributes]

### decisionTaskTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.DecisionTaskTimedOutEventAttributes]

### activityTaskScheduledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskScheduledEventAttributes]

### activityTaskStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskStartedEventAttributes]

### activityTaskCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskCompletedEventAttributes]

### activityTaskFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskFailedEventAttributes]

### activityTaskTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskTimedOutEventAttributes]

### activityTaskCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskCanceledEventAttributes]

### activityTaskCancelRequestedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ActivityTaskCancelRequestedEventAttributes]

### workflowExecutionSignaledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionSignaledEventAttributes]

### markerRecordedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.MarkerRecordedEventAttributes]

### recordMarkerFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RecordMarkerFailedEventAttributes]

### timerStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TimerStartedEventAttributes]

### timerFiredEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TimerFiredEventAttributes]

### timerCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TimerCanceledEventAttributes]

### startChildWorkflowExecutionInitiatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartChildWorkflowExecutionInitiatedEventAttributes]

### childWorkflowExecutionStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionStartedEventAttributes]

### childWorkflowExecutionCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionCompletedEventAttributes]

### childWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionFailedEventAttributes]

### childWorkflowExecutionTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionTimedOutEventAttributes]

### childWorkflowExecutionCanceledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionCanceledEventAttributes]

### childWorkflowExecutionTerminatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ChildWorkflowExecutionTerminatedEventAttributes]

### signalExternalWorkflowExecutionInitiatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.SignalExternalWorkflowExecutionInitiatedEventAttributes]

### externalWorkflowExecutionSignaledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExternalWorkflowExecutionSignaledEventAttributes]

### signalExternalWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.SignalExternalWorkflowExecutionFailedEventAttributes]

### externalWorkflowExecutionCancelRequestedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExternalWorkflowExecutionCancelRequestedEventAttributes]

### requestCancelExternalWorkflowExecutionInitiatedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelExternalWorkflowExecutionInitiatedEventAttributes]

### requestCancelExternalWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelExternalWorkflowExecutionFailedEventAttributes]

### scheduleActivityTaskFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleActivityTaskFailedEventAttributes]

### requestCancelActivityTaskFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.RequestCancelActivityTaskFailedEventAttributes]

### startTimerFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartTimerFailedEventAttributes]

### cancelTimerFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CancelTimerFailedEventAttributes]

### startChildWorkflowExecutionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartChildWorkflowExecutionFailedEventAttributes]

### lambdaFunctionScheduledEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionScheduledEventAttributes]

### lambdaFunctionStartedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionStartedEventAttributes]

### lambdaFunctionCompletedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionCompletedEventAttributes]

### lambdaFunctionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionFailedEventAttributes]

### lambdaFunctionTimedOutEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.LambdaFunctionTimedOutEventAttributes]

### scheduleLambdaFunctionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ScheduleLambdaFunctionFailedEventAttributes]

### startLambdaFunctionFailedEventAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.StartLambdaFunctionFailedEventAttributes]


# LambdaFunctionCompletedEventAttributes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# LambdaFunctionFailedEventAttributes

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


# LambdaFunctionScheduledEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# LambdaFunctionStartedEventAttributes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes


# LambdaFunctionTimedOutEventAttributes

### scheduledEventId
- **Type**: <class 'int'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### timeoutType
- **Type**: typing.Optional[typing.Literal['START_TO_CLOSE']]


# ListActivityTypesInput

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


# ListActivityTypesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfig]


# ListClosedWorkflowExecutionsInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter]

### closeTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilter]

### closeStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CloseStatusFilter]

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilter]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilter]

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# ListClosedWorkflowExecutionsInputPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter]

### closeTimeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilter]

### closeStatusFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.CloseStatusFilter]

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilter]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilter]

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfig]


# ListDomainsInput

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]


# ListDomainsInputPaginate

### registrationStatus
- **Type**: typing.Literal['DEPRECATED', 'REGISTERED']
- **Required**: Yes

### reverseOrder
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfig]


# ListOpenWorkflowExecutionsInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter'>
- **Required**: Yes

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilter]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilter]

### nextPageToken
- **Type**: typing.Optional[str]

### maximumPageSize
- **Type**: typing.Optional[int]

### reverseOrder
- **Type**: typing.Optional[bool]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilter]


# ListOpenWorkflowExecutionsInputPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeFilter
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ExecutionTimeFilter'>
- **Required**: Yes

### typeFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeFilter]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TagFilter]

### reverseOrder
- **Type**: typing.Optional[bool]

### executionFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfig]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.ResourceTag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# ListWorkflowTypesInput

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


# ListWorkflowTypesInputPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfig]


# MarkerRecordedEventAttributes

### markerName
- **Type**: <class 'str'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PendingTaskCount

### count
- **Type**: <class 'int'>
- **Required**: Yes

### truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# PollForActivityTaskInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskList'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]


# PollForDecisionTaskInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskList'>
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


# PollForDecisionTaskInputPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskList'>
- **Required**: Yes

### identity
- **Type**: typing.Optional[str]

### reverseOrder
- **Type**: typing.Optional[bool]

### startAtPreviousStartedEvent
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.PaginatorConfig]


# RecordActivityTaskHeartbeatInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# RecordMarkerDecisionAttributes

### markerName
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# RecordMarkerFailedEventAttributes

### markerName
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPERATION_NOT_PERMITTED']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# RegisterActivityTypeInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskList]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultTaskScheduleToStartTimeout
- **Type**: typing.Optional[str]

### defaultTaskScheduleToCloseTimeout
- **Type**: typing.Optional[str]


# RegisterDomainInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workflowExecutionRetentionPeriodInDays
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.swf_classes.ResourceTag]]


# RegisterWorkflowTypeInput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskList]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultChildPolicy
- **Type**: typing.Optional[typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']]

### defaultLambdaRole
- **Type**: typing.Optional[str]


# RequestCancelActivityTaskDecisionAttributes

### activityId
- **Type**: <class 'str'>
- **Required**: Yes


# RequestCancelActivityTaskFailedEventAttributes

### activityId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['ACTIVITY_ID_UNKNOWN', 'OPERATION_NOT_PERMITTED']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# RequestCancelExternalWorkflowExecutionDecisionAttributes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]

### control
- **Type**: typing.Optional[str]


# RequestCancelExternalWorkflowExecutionFailedEventAttributes

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


# RequestCancelExternalWorkflowExecutionInitiatedEventAttributes

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


# RequestCancelWorkflowExecutionInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: typing.Optional[str]


# ResourceTag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# RespondActivityTaskCanceledInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# RespondActivityTaskCompletedInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# RespondActivityTaskFailedInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# RespondDecisionTaskCompletedInput

### taskToken
- **Type**: <class 'str'>
- **Required**: Yes

### decisions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.swf_classes.Decision]]

### executionContext
- **Type**: typing.Optional[str]

### taskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskList]

### taskListScheduleToStartTimeout
- **Type**: typing.Optional[str]


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


# Run

### runId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# ScheduleActivityTaskDecisionAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduleActivityTaskFailedEventAttributes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityType'>
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


# ScheduleLambdaFunctionDecisionAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ScheduleLambdaFunctionFailedEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalExternalWorkflowExecutionDecisionAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SignalExternalWorkflowExecutionFailedEventAttributes

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


# SignalExternalWorkflowExecutionInitiatedEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartChildWorkflowExecutionDecisionAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartChildWorkflowExecutionFailedEventAttributes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
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


# StartChildWorkflowExecutionInitiatedEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartLambdaFunctionFailedEventAttributes

### scheduledEventId
- **Type**: typing.Optional[int]

### cause
- **Type**: typing.Optional[typing.Literal['ASSUME_ROLE_FAILED']]

### message
- **Type**: typing.Optional[str]


# StartTimerDecisionAttributes

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### startToFireTimeout
- **Type**: <class 'str'>
- **Required**: Yes

### control
- **Type**: typing.Optional[str]


# StartTimerFailedEventAttributes

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### cause
- **Type**: typing.Literal['OPEN_TIMERS_LIMIT_EXCEEDED', 'OPERATION_NOT_PERMITTED', 'TIMER_CREATION_RATE_EXCEEDED', 'TIMER_ID_ALREADY_IN_USE']
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# TagFilter

### tag
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.swf_classes.ResourceTag]
- **Required**: Yes


# TaskList

### name
- **Type**: <class 'str'>
- **Required**: Yes


# TerminateWorkflowExecutionInput

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


# TimerCanceledEventAttributes

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# TimerFiredEventAttributes

### timerId
- **Type**: <class 'str'>
- **Required**: Yes

### startedEventId
- **Type**: <class 'int'>
- **Required**: Yes


# TimerStartedEventAttributes

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


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UndeprecateActivityTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### activityType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ActivityType'>
- **Required**: Yes


# UndeprecateDomainInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# UndeprecateWorkflowTypeInput

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WorkflowExecution

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### runId
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowExecutionCancelRequestedEventAttributes

### externalWorkflowExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution]

### externalInitiatedEventId
- **Type**: typing.Optional[int]

### cause
- **Type**: typing.Optional[typing.Literal['CHILD_POLICY_APPLIED']]


# WorkflowExecutionCanceledEventAttributes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### details
- **Type**: typing.Optional[str]


# WorkflowExecutionCompletedEventAttributes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### result
- **Type**: typing.Optional[str]


# WorkflowExecutionConfiguration

### taskStartToCloseTimeout
- **Type**: <class 'str'>
- **Required**: Yes

### executionStartToCloseTimeout
- **Type**: <class 'str'>
- **Required**: Yes

### taskList
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.TaskList'>
- **Required**: Yes

### childPolicy
- **Type**: typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']
- **Required**: Yes

### taskPriority
- **Type**: typing.Optional[str]

### lambdaRole
- **Type**: typing.Optional[str]


# WorkflowExecutionContinuedAsNewEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionCount

### count
- **Type**: <class 'int'>
- **Required**: Yes

### truncated
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowExecutionDetail

### executionInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionInfo'>
- **Required**: Yes

### executionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionConfiguration'>
- **Required**: Yes

### openCounts
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionOpenCounts'>
- **Required**: Yes

### latestActivityTaskTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### latestExecutionContext
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowExecutionFailedEventAttributes

### decisionTaskCompletedEventId
- **Type**: <class 'int'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]


# WorkflowExecutionFilter

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowExecutionInfo

### execution
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution'>
- **Required**: Yes

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecution]

### tagList
- **Type**: typing.Optional[typing.List[str]]

### cancelRequested
- **Type**: typing.Optional[bool]


# WorkflowExecutionInfos

### executionInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.WorkflowExecutionInfo]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowExecutionOpenCounts

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


# WorkflowExecutionSignaledEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionStartedEventAttributes

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowExecutionTerminatedEventAttributes

### childPolicy
- **Type**: typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]

### details
- **Type**: typing.Optional[str]

### cause
- **Type**: typing.Optional[typing.Literal['CHILD_POLICY_APPLIED', 'EVENT_LIMIT_EXCEEDED', 'OPERATOR_INITIATED']]


# WorkflowExecutionTimedOutEventAttributes

### timeoutType
- **Type**: typing.Literal['START_TO_CLOSE']
- **Required**: Yes

### childPolicy
- **Type**: typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']
- **Required**: Yes


# WorkflowType

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# WorkflowTypeConfiguration

### defaultTaskStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultExecutionStartToCloseTimeout
- **Type**: typing.Optional[str]

### defaultTaskList
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.swf_classes.TaskList]

### defaultTaskPriority
- **Type**: typing.Optional[str]

### defaultChildPolicy
- **Type**: typing.Optional[typing.Literal['ABANDON', 'REQUEST_CANCEL', 'TERMINATE']]

### defaultLambdaRole
- **Type**: typing.Optional[str]


# WorkflowTypeDetail

### typeInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeInfo'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowTypeFilter

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[str]


# WorkflowTypeInfo

### workflowType
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.WorkflowType'>
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


# WorkflowTypeInfos

### typeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.swf_classes.WorkflowTypeInfo]
- **Required**: Yes

### nextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.swf_classes.ResponseMetadata'>
- **Required**: Yes


