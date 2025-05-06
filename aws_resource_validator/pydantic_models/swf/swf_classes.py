from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.swf.swf_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActivityTaskCancelRequestedEventAttributes(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    activityId: str


class ActivityTaskCanceledEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    details: Optional[str] = None
    latestCancelRequestedEventId: Optional[int] = None


class ActivityTaskCompletedEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    result: Optional[str] = None


class ActivityTaskFailedEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class ActivityType(BaseValidatorModel):
    name: str
    version: str


class TaskList(BaseValidatorModel):
    name: str


class ActivityTaskStartedEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    identity: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActivityTaskTimedOutEventAttributes(BaseValidatorModel):
    timeoutType: ActivityTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int
    details: Optional[str] = None


class WorkflowExecution(BaseValidatorModel):
    workflowId: str
    runId: str


class CancelTimerDecisionAttributes(BaseValidatorModel):
    timerId: str


class CancelTimerFailedEventAttributes(BaseValidatorModel):
    timerId: str
    cause: CancelTimerFailedCauseType
    decisionTaskCompletedEventId: int


class CancelWorkflowExecutionDecisionAttributes(BaseValidatorModel):
    details: Optional[str] = None


class CancelWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    cause: CancelWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class WorkflowType(BaseValidatorModel):
    name: str
    version: str


class CloseStatusFilter(BaseValidatorModel):
    status: CloseStatusType


class CompleteWorkflowExecutionDecisionAttributes(BaseValidatorModel):
    result: Optional[str] = None


class CompleteWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    cause: CompleteWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class ContinueAsNewWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    cause: ContinueAsNewWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class TagFilter(BaseValidatorModel):
    tag: str


class WorkflowExecutionFilter(BaseValidatorModel):
    workflowId: str


class WorkflowTypeFilter(BaseValidatorModel):
    name: str
    version: Optional[str] = None


class DecisionTaskStartedEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    identity: Optional[str] = None


class DecisionTaskTimedOutEventAttributes(BaseValidatorModel):
    timeoutType: DecisionTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int


class FailWorkflowExecutionDecisionAttributes(BaseValidatorModel):
    reason: Optional[str] = None
    details: Optional[str] = None


class RecordMarkerDecisionAttributes(BaseValidatorModel):
    markerName: str
    details: Optional[str] = None


class RequestCancelActivityTaskDecisionAttributes(BaseValidatorModel):
    activityId: str


class RequestCancelExternalWorkflowExecutionDecisionAttributes(BaseValidatorModel):
    workflowId: str
    runId: Optional[str] = None
    control: Optional[str] = None


class ScheduleLambdaFunctionDecisionAttributes(BaseValidatorModel):
    id: str
    name: str
    control: Optional[str] = None
    input: Optional[str] = None
    startToCloseTimeout: Optional[str] = None


class SignalExternalWorkflowExecutionDecisionAttributes(BaseValidatorModel):
    workflowId: str
    signalName: str
    runId: Optional[str] = None
    input: Optional[str] = None
    control: Optional[str] = None


class StartTimerDecisionAttributes(BaseValidatorModel):
    timerId: str
    startToFireTimeout: str
    control: Optional[str] = None


class DeprecateDomainInput(BaseValidatorModel):
    name: str


class DescribeDomainInput(BaseValidatorModel):
    name: str


class DomainConfiguration(BaseValidatorModel):
    workflowExecutionRetentionPeriodInDays: str


class DomainInfo(BaseValidatorModel):
    name: str
    status: RegistrationStatusType
    description: Optional[str] = None
    arn: Optional[str] = None

Timestamp = Union[datetime, str]


class FailWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    cause: FailWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class LambdaFunctionCompletedEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    result: Optional[str] = None


class LambdaFunctionFailedEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class LambdaFunctionScheduledEventAttributes(BaseValidatorModel):
    id: str
    name: str
    decisionTaskCompletedEventId: int
    control: Optional[str] = None
    input: Optional[str] = None
    startToCloseTimeout: Optional[str] = None


class LambdaFunctionStartedEventAttributes(BaseValidatorModel):
    scheduledEventId: int


class LambdaFunctionTimedOutEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    timeoutType: Optional[Literal['START_TO_CLOSE']] = None


class MarkerRecordedEventAttributes(BaseValidatorModel):
    markerName: str
    decisionTaskCompletedEventId: int
    details: Optional[str] = None


class RecordMarkerFailedEventAttributes(BaseValidatorModel):
    markerName: str
    cause: Literal['OPERATION_NOT_PERMITTED']
    decisionTaskCompletedEventId: int


class RequestCancelActivityTaskFailedEventAttributes(BaseValidatorModel):
    activityId: str
    cause: RequestCancelActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int


class RequestCancelExternalWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    workflowId: str
    cause: RequestCancelExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributes(BaseValidatorModel):
    workflowId: str
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None


class ScheduleLambdaFunctionFailedEventAttributes(BaseValidatorModel):
    id: str
    name: str
    cause: ScheduleLambdaFunctionFailedCauseType
    decisionTaskCompletedEventId: int


class SignalExternalWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    workflowId: str
    cause: SignalExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None


class SignalExternalWorkflowExecutionInitiatedEventAttributes(BaseValidatorModel):
    workflowId: str
    signalName: str
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    input: Optional[str] = None
    control: Optional[str] = None


class StartLambdaFunctionFailedEventAttributes(BaseValidatorModel):
    scheduledEventId: Optional[int] = None
    cause: Optional[Literal['ASSUME_ROLE_FAILED']] = None
    message: Optional[str] = None


class StartTimerFailedEventAttributes(BaseValidatorModel):
    timerId: str
    cause: StartTimerFailedCauseType
    decisionTaskCompletedEventId: int


class TimerCanceledEventAttributes(BaseValidatorModel):
    timerId: str
    startedEventId: int
    decisionTaskCompletedEventId: int


class TimerFiredEventAttributes(BaseValidatorModel):
    timerId: str
    startedEventId: int


class TimerStartedEventAttributes(BaseValidatorModel):
    timerId: str
    startToFireTimeout: str
    decisionTaskCompletedEventId: int
    control: Optional[str] = None


class WorkflowExecutionCanceledEventAttributes(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    details: Optional[str] = None


class WorkflowExecutionCompletedEventAttributes(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    result: Optional[str] = None


class WorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class WorkflowExecutionTerminatedEventAttributes(BaseValidatorModel):
    childPolicy: ChildPolicyType
    reason: Optional[str] = None
    details: Optional[str] = None
    cause: Optional[WorkflowExecutionTerminatedCauseType] = None


class WorkflowExecutionTimedOutEventAttributes(BaseValidatorModel):
    timeoutType: Literal['START_TO_CLOSE']
    childPolicy: ChildPolicyType


class ListActivityTypesInput(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class ListDomainsInput(BaseValidatorModel):
    registrationStatus: RegistrationStatusType
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class ResourceTag(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class ListWorkflowTypesInput(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class RecordActivityTaskHeartbeatInput(BaseValidatorModel):
    taskToken: str
    details: Optional[str] = None


class RequestCancelWorkflowExecutionInput(BaseValidatorModel):
    domain: str
    workflowId: str
    runId: Optional[str] = None


class RespondActivityTaskCanceledInput(BaseValidatorModel):
    taskToken: str
    details: Optional[str] = None


class RespondActivityTaskCompletedInput(BaseValidatorModel):
    taskToken: str
    result: Optional[str] = None


class RespondActivityTaskFailedInput(BaseValidatorModel):
    taskToken: str
    reason: Optional[str] = None
    details: Optional[str] = None


class SignalWorkflowExecutionInput(BaseValidatorModel):
    domain: str
    workflowId: str
    signalName: str
    runId: Optional[str] = None
    input: Optional[str] = None


class TerminateWorkflowExecutionInput(BaseValidatorModel):
    domain: str
    workflowId: str
    runId: Optional[str] = None
    reason: Optional[str] = None
    details: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None


class UndeprecateDomainInput(BaseValidatorModel):
    name: str


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class WorkflowExecutionOpenCounts(BaseValidatorModel):
    openActivityTasks: int
    openDecisionTasks: int
    openTimers: int
    openChildWorkflowExecutions: int
    openLambdaFunctions: Optional[int] = None


class ActivityTypeInfo(BaseValidatorModel):
    activityType: ActivityType
    status: RegistrationStatusType
    creationDate: datetime
    description: Optional[str] = None
    deprecationDate: Optional[datetime] = None


class DeleteActivityTypeInput(BaseValidatorModel):
    domain: str
    activityType: ActivityType


class DeprecateActivityTypeInput(BaseValidatorModel):
    domain: str
    activityType: ActivityType


class DescribeActivityTypeInput(BaseValidatorModel):
    domain: str
    activityType: ActivityType


class ScheduleActivityTaskFailedEventAttributes(BaseValidatorModel):
    activityType: ActivityType
    activityId: str
    cause: ScheduleActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int


class UndeprecateActivityTypeInput(BaseValidatorModel):
    domain: str
    activityType: ActivityType


class ActivityTaskScheduledEventAttributes(BaseValidatorModel):
    activityType: ActivityType
    activityId: str
    taskList: TaskList
    decisionTaskCompletedEventId: int
    input: Optional[str] = None
    control: Optional[str] = None
    scheduleToStartTimeout: Optional[str] = None
    scheduleToCloseTimeout: Optional[str] = None
    startToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    heartbeatTimeout: Optional[str] = None


class ActivityTypeConfiguration(BaseValidatorModel):
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultTaskHeartbeatTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskList] = None
    defaultTaskPriority: Optional[str] = None
    defaultTaskScheduleToStartTimeout: Optional[str] = None
    defaultTaskScheduleToCloseTimeout: Optional[str] = None


class ContinueAsNewWorkflowExecutionDecisionAttributes(BaseValidatorModel):
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskList: Optional[TaskList] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None
    tagList: Optional[List[str]] = None
    workflowTypeVersion: Optional[str] = None
    lambdaRole: Optional[str] = None


class CountPendingActivityTasksInput(BaseValidatorModel):
    domain: str
    taskList: TaskList


class CountPendingDecisionTasksInput(BaseValidatorModel):
    domain: str
    taskList: TaskList


class DecisionTaskCompletedEventAttributes(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    executionContext: Optional[str] = None
    taskList: Optional[TaskList] = None
    taskListScheduleToStartTimeout: Optional[str] = None


class DecisionTaskScheduledEventAttributes(BaseValidatorModel):
    taskList: TaskList
    taskPriority: Optional[str] = None
    startToCloseTimeout: Optional[str] = None
    scheduleToStartTimeout: Optional[str] = None


class PollForActivityTaskInput(BaseValidatorModel):
    domain: str
    taskList: TaskList
    identity: Optional[str] = None


class PollForDecisionTaskInput(BaseValidatorModel):
    domain: str
    taskList: TaskList
    identity: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None
    startAtPreviousStartedEvent: Optional[bool] = None


class RegisterActivityTypeInput(BaseValidatorModel):
    domain: str
    name: str
    version: str
    description: Optional[str] = None
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultTaskHeartbeatTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskList] = None
    defaultTaskPriority: Optional[str] = None
    defaultTaskScheduleToStartTimeout: Optional[str] = None
    defaultTaskScheduleToCloseTimeout: Optional[str] = None


class RegisterWorkflowTypeInput(BaseValidatorModel):
    domain: str
    name: str
    version: str
    description: Optional[str] = None
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultExecutionStartToCloseTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskList] = None
    defaultTaskPriority: Optional[str] = None
    defaultChildPolicy: Optional[ChildPolicyType] = None
    defaultLambdaRole: Optional[str] = None


class ScheduleActivityTaskDecisionAttributes(BaseValidatorModel):
    activityType: ActivityType
    activityId: str
    control: Optional[str] = None
    input: Optional[str] = None
    scheduleToCloseTimeout: Optional[str] = None
    taskList: Optional[TaskList] = None
    taskPriority: Optional[str] = None
    scheduleToStartTimeout: Optional[str] = None
    startToCloseTimeout: Optional[str] = None
    heartbeatTimeout: Optional[str] = None


class WorkflowExecutionConfiguration(BaseValidatorModel):
    taskStartToCloseTimeout: str
    executionStartToCloseTimeout: str
    taskList: TaskList
    childPolicy: ChildPolicyType
    taskPriority: Optional[str] = None
    lambdaRole: Optional[str] = None


class WorkflowTypeConfiguration(BaseValidatorModel):
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultExecutionStartToCloseTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskList] = None
    defaultTaskPriority: Optional[str] = None
    defaultChildPolicy: Optional[ChildPolicyType] = None
    defaultLambdaRole: Optional[str] = None


class ActivityTaskStatus(BaseValidatorModel):
    cancelRequested: bool
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class PendingTaskCount(BaseValidatorModel):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadata


class Run(BaseValidatorModel):
    runId: str
    ResponseMetadata: ResponseMetadata


class WorkflowExecutionCount(BaseValidatorModel):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadata


class ActivityTask(BaseValidatorModel):
    taskToken: str
    activityId: str
    startedEventId: int
    workflowExecution: WorkflowExecution
    activityType: ActivityType
    input: str
    ResponseMetadata: ResponseMetadata


class DescribeWorkflowExecutionInput(BaseValidatorModel):
    domain: str
    execution: WorkflowExecution


class ExternalWorkflowExecutionCancelRequestedEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    initiatedEventId: int


class ExternalWorkflowExecutionSignaledEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    initiatedEventId: int


class GetWorkflowExecutionHistoryInput(BaseValidatorModel):
    domain: str
    execution: WorkflowExecution
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class WorkflowExecutionCancelRequestedEventAttributes(BaseValidatorModel):
    externalWorkflowExecution: Optional[WorkflowExecution] = None
    externalInitiatedEventId: Optional[int] = None
    cause: Optional[Literal['CHILD_POLICY_APPLIED']] = None


class WorkflowExecutionSignaledEventAttributes(BaseValidatorModel):
    signalName: str
    input: Optional[str] = None
    externalWorkflowExecution: Optional[WorkflowExecution] = None
    externalInitiatedEventId: Optional[int] = None


class ChildWorkflowExecutionCanceledEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    workflowType: WorkflowType
    initiatedEventId: int
    startedEventId: int
    details: Optional[str] = None


class ChildWorkflowExecutionCompletedEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    workflowType: WorkflowType
    initiatedEventId: int
    startedEventId: int
    result: Optional[str] = None


class ChildWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    workflowType: WorkflowType
    initiatedEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class ChildWorkflowExecutionStartedEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    workflowType: WorkflowType
    initiatedEventId: int


class ChildWorkflowExecutionTerminatedEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    workflowType: WorkflowType
    initiatedEventId: int
    startedEventId: int


class ChildWorkflowExecutionTimedOutEventAttributes(BaseValidatorModel):
    workflowExecution: WorkflowExecution
    workflowType: WorkflowType
    timeoutType: Literal['START_TO_CLOSE']
    initiatedEventId: int
    startedEventId: int


class DeleteWorkflowTypeInput(BaseValidatorModel):
    domain: str
    workflowType: WorkflowType


class DeprecateWorkflowTypeInput(BaseValidatorModel):
    domain: str
    workflowType: WorkflowType


class DescribeWorkflowTypeInput(BaseValidatorModel):
    domain: str
    workflowType: WorkflowType


class StartChildWorkflowExecutionDecisionAttributes(BaseValidatorModel):
    workflowType: WorkflowType
    workflowId: str
    control: Optional[str] = None
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskList: Optional[TaskList] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None
    tagList: Optional[List[str]] = None
    lambdaRole: Optional[str] = None


class StartChildWorkflowExecutionFailedEventAttributes(BaseValidatorModel):
    workflowType: WorkflowType
    cause: StartChildWorkflowExecutionFailedCauseType
    workflowId: str
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    control: Optional[str] = None


class StartChildWorkflowExecutionInitiatedEventAttributes(BaseValidatorModel):
    workflowId: str
    workflowType: WorkflowType
    taskList: TaskList
    decisionTaskCompletedEventId: int
    childPolicy: ChildPolicyType
    control: Optional[str] = None
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    tagList: Optional[List[str]] = None
    lambdaRole: Optional[str] = None


class StartWorkflowExecutionInput(BaseValidatorModel):
    domain: str
    workflowId: str
    workflowType: WorkflowType
    taskList: Optional[TaskList] = None
    taskPriority: Optional[str] = None
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    tagList: Optional[List[str]] = None
    taskStartToCloseTimeout: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None
    lambdaRole: Optional[str] = None


class UndeprecateWorkflowTypeInput(BaseValidatorModel):
    domain: str
    workflowType: WorkflowType


class WorkflowExecutionContinuedAsNewEventAttributes(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    newExecutionRunId: str
    taskList: TaskList
    childPolicy: ChildPolicyType
    workflowType: WorkflowType
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    tagList: Optional[List[str]] = None
    lambdaRole: Optional[str] = None


class WorkflowExecutionInfo(BaseValidatorModel):
    execution: WorkflowExecution
    workflowType: WorkflowType
    startTimestamp: datetime
    executionStatus: ExecutionStatusType
    closeTimestamp: Optional[datetime] = None
    closeStatus: Optional[CloseStatusType] = None
    parent: Optional[WorkflowExecution] = None
    tagList: Optional[List[str]] = None
    cancelRequested: Optional[bool] = None


class WorkflowExecutionStartedEventAttributes(BaseValidatorModel):
    childPolicy: ChildPolicyType
    taskList: TaskList
    workflowType: WorkflowType
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    tagList: Optional[List[str]] = None
    continuedExecutionRunId: Optional[str] = None
    parentWorkflowExecution: Optional[WorkflowExecution] = None
    parentInitiatedEventId: Optional[int] = None
    lambdaRole: Optional[str] = None


class WorkflowTypeInfo(BaseValidatorModel):
    workflowType: WorkflowType
    status: RegistrationStatusType
    creationDate: datetime
    description: Optional[str] = None
    deprecationDate: Optional[datetime] = None


class DomainDetail(BaseValidatorModel):
    domainInfo: DomainInfo
    configuration: DomainConfiguration
    ResponseMetadata: ResponseMetadata


class DomainInfos(BaseValidatorModel):
    domainInfos: List[DomainInfo]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class ExecutionTimeFilter(BaseValidatorModel):
    oldestDate: Timestamp
    latestDate: Optional[Timestamp] = None


class GetWorkflowExecutionHistoryInputPaginate(BaseValidatorModel):
    domain: str
    execution: WorkflowExecution
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListActivityTypesInputPaginate(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainsInputPaginate(BaseValidatorModel):
    registrationStatus: RegistrationStatusType
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowTypesInputPaginate(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class PollForDecisionTaskInputPaginate(BaseValidatorModel):
    domain: str
    taskList: TaskList
    identity: Optional[str] = None
    reverseOrder: Optional[bool] = None
    startAtPreviousStartedEvent: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata


class RegisterDomainInput(BaseValidatorModel):
    name: str
    workflowExecutionRetentionPeriodInDays: str
    description: Optional[str] = None
    tags: Optional[List[ResourceTag]] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: List[ResourceTag]


class ActivityTypeInfos(BaseValidatorModel):
    typeInfos: List[ActivityTypeInfo]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class ActivityTypeDetail(BaseValidatorModel):
    typeInfo: ActivityTypeInfo
    configuration: ActivityTypeConfiguration
    ResponseMetadata: ResponseMetadata


class Decision(BaseValidatorModel):
    decisionType: DecisionTypeType
    scheduleActivityTaskDecisionAttributes: Optional[ScheduleActivityTaskDecisionAttributes] = None
    requestCancelActivityTaskDecisionAttributes: Optional[RequestCancelActivityTaskDecisionAttributes] = None
    completeWorkflowExecutionDecisionAttributes: Optional[CompleteWorkflowExecutionDecisionAttributes] = None
    failWorkflowExecutionDecisionAttributes: Optional[FailWorkflowExecutionDecisionAttributes] = None
    cancelWorkflowExecutionDecisionAttributes: Optional[CancelWorkflowExecutionDecisionAttributes] = None
    continueAsNewWorkflowExecutionDecisionAttributes: Optional[ContinueAsNewWorkflowExecutionDecisionAttributes] = None
    recordMarkerDecisionAttributes: Optional[RecordMarkerDecisionAttributes] = None
    startTimerDecisionAttributes: Optional[StartTimerDecisionAttributes] = None
    cancelTimerDecisionAttributes: Optional[CancelTimerDecisionAttributes] = None
    signalExternalWorkflowExecutionDecisionAttributes: Optional[SignalExternalWorkflowExecutionDecisionAttributes] = None
    requestCancelExternalWorkflowExecutionDecisionAttributes: Optional[RequestCancelExternalWorkflowExecutionDecisionAttributes] = None
    startChildWorkflowExecutionDecisionAttributes: Optional[StartChildWorkflowExecutionDecisionAttributes] = None
    scheduleLambdaFunctionDecisionAttributes: Optional[ScheduleLambdaFunctionDecisionAttributes] = None


class WorkflowExecutionDetail(BaseValidatorModel):
    executionInfo: WorkflowExecutionInfo
    executionConfiguration: WorkflowExecutionConfiguration
    openCounts: WorkflowExecutionOpenCounts
    latestActivityTaskTimestamp: datetime
    latestExecutionContext: str
    ResponseMetadata: ResponseMetadata


class WorkflowExecutionInfos(BaseValidatorModel):
    executionInfos: List[WorkflowExecutionInfo]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class HistoryEvent(BaseValidatorModel):
    eventTimestamp: datetime
    eventType: EventTypeType
    eventId: int
    workflowExecutionStartedEventAttributes: Optional[WorkflowExecutionStartedEventAttributes] = None
    workflowExecutionCompletedEventAttributes: Optional[WorkflowExecutionCompletedEventAttributes] = None
    completeWorkflowExecutionFailedEventAttributes: Optional[CompleteWorkflowExecutionFailedEventAttributes] = None
    workflowExecutionFailedEventAttributes: Optional[WorkflowExecutionFailedEventAttributes] = None
    failWorkflowExecutionFailedEventAttributes: Optional[FailWorkflowExecutionFailedEventAttributes] = None
    workflowExecutionTimedOutEventAttributes: Optional[WorkflowExecutionTimedOutEventAttributes] = None
    workflowExecutionCanceledEventAttributes: Optional[WorkflowExecutionCanceledEventAttributes] = None
    cancelWorkflowExecutionFailedEventAttributes: Optional[CancelWorkflowExecutionFailedEventAttributes] = None
    workflowExecutionContinuedAsNewEventAttributes: Optional[WorkflowExecutionContinuedAsNewEventAttributes] = None
    continueAsNewWorkflowExecutionFailedEventAttributes: Optional[ContinueAsNewWorkflowExecutionFailedEventAttributes] = None
    workflowExecutionTerminatedEventAttributes: Optional[WorkflowExecutionTerminatedEventAttributes] = None
    workflowExecutionCancelRequestedEventAttributes: Optional[WorkflowExecutionCancelRequestedEventAttributes] = None
    decisionTaskScheduledEventAttributes: Optional[DecisionTaskScheduledEventAttributes] = None
    decisionTaskStartedEventAttributes: Optional[DecisionTaskStartedEventAttributes] = None
    decisionTaskCompletedEventAttributes: Optional[DecisionTaskCompletedEventAttributes] = None
    decisionTaskTimedOutEventAttributes: Optional[DecisionTaskTimedOutEventAttributes] = None
    activityTaskScheduledEventAttributes: Optional[ActivityTaskScheduledEventAttributes] = None
    activityTaskStartedEventAttributes: Optional[ActivityTaskStartedEventAttributes] = None
    activityTaskCompletedEventAttributes: Optional[ActivityTaskCompletedEventAttributes] = None
    activityTaskFailedEventAttributes: Optional[ActivityTaskFailedEventAttributes] = None
    activityTaskTimedOutEventAttributes: Optional[ActivityTaskTimedOutEventAttributes] = None
    activityTaskCanceledEventAttributes: Optional[ActivityTaskCanceledEventAttributes] = None
    activityTaskCancelRequestedEventAttributes: Optional[ActivityTaskCancelRequestedEventAttributes] = None
    workflowExecutionSignaledEventAttributes: Optional[WorkflowExecutionSignaledEventAttributes] = None
    markerRecordedEventAttributes: Optional[MarkerRecordedEventAttributes] = None
    recordMarkerFailedEventAttributes: Optional[RecordMarkerFailedEventAttributes] = None
    timerStartedEventAttributes: Optional[TimerStartedEventAttributes] = None
    timerFiredEventAttributes: Optional[TimerFiredEventAttributes] = None
    timerCanceledEventAttributes: Optional[TimerCanceledEventAttributes] = None
    startChildWorkflowExecutionInitiatedEventAttributes: Optional[StartChildWorkflowExecutionInitiatedEventAttributes] = None
    childWorkflowExecutionStartedEventAttributes: Optional[ChildWorkflowExecutionStartedEventAttributes] = None
    childWorkflowExecutionCompletedEventAttributes: Optional[ChildWorkflowExecutionCompletedEventAttributes] = None
    childWorkflowExecutionFailedEventAttributes: Optional[ChildWorkflowExecutionFailedEventAttributes] = None
    childWorkflowExecutionTimedOutEventAttributes: Optional[ChildWorkflowExecutionTimedOutEventAttributes] = None
    childWorkflowExecutionCanceledEventAttributes: Optional[ChildWorkflowExecutionCanceledEventAttributes] = None
    childWorkflowExecutionTerminatedEventAttributes: Optional[ChildWorkflowExecutionTerminatedEventAttributes] = None
    signalExternalWorkflowExecutionInitiatedEventAttributes: Optional[SignalExternalWorkflowExecutionInitiatedEventAttributes] = None
    externalWorkflowExecutionSignaledEventAttributes: Optional[ExternalWorkflowExecutionSignaledEventAttributes] = None
    signalExternalWorkflowExecutionFailedEventAttributes: Optional[SignalExternalWorkflowExecutionFailedEventAttributes] = None
    externalWorkflowExecutionCancelRequestedEventAttributes: Optional[ExternalWorkflowExecutionCancelRequestedEventAttributes] = None
    requestCancelExternalWorkflowExecutionInitiatedEventAttributes: Optional[RequestCancelExternalWorkflowExecutionInitiatedEventAttributes] = None
    requestCancelExternalWorkflowExecutionFailedEventAttributes: Optional[RequestCancelExternalWorkflowExecutionFailedEventAttributes] = None
    scheduleActivityTaskFailedEventAttributes: Optional[ScheduleActivityTaskFailedEventAttributes] = None
    requestCancelActivityTaskFailedEventAttributes: Optional[RequestCancelActivityTaskFailedEventAttributes] = None
    startTimerFailedEventAttributes: Optional[StartTimerFailedEventAttributes] = None
    cancelTimerFailedEventAttributes: Optional[CancelTimerFailedEventAttributes] = None
    startChildWorkflowExecutionFailedEventAttributes: Optional[StartChildWorkflowExecutionFailedEventAttributes] = None
    lambdaFunctionScheduledEventAttributes: Optional[LambdaFunctionScheduledEventAttributes] = None
    lambdaFunctionStartedEventAttributes: Optional[LambdaFunctionStartedEventAttributes] = None
    lambdaFunctionCompletedEventAttributes: Optional[LambdaFunctionCompletedEventAttributes] = None
    lambdaFunctionFailedEventAttributes: Optional[LambdaFunctionFailedEventAttributes] = None
    lambdaFunctionTimedOutEventAttributes: Optional[LambdaFunctionTimedOutEventAttributes] = None
    scheduleLambdaFunctionFailedEventAttributes: Optional[ScheduleLambdaFunctionFailedEventAttributes] = None
    startLambdaFunctionFailedEventAttributes: Optional[StartLambdaFunctionFailedEventAttributes] = None


class WorkflowTypeDetail(BaseValidatorModel):
    typeInfo: WorkflowTypeInfo
    configuration: WorkflowTypeConfiguration
    ResponseMetadata: ResponseMetadata


class WorkflowTypeInfos(BaseValidatorModel):
    typeInfos: List[WorkflowTypeInfo]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata


class CountClosedWorkflowExecutionsInput(BaseValidatorModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilter] = None
    closeTimeFilter: Optional[ExecutionTimeFilter] = None
    executionFilter: Optional[WorkflowExecutionFilter] = None
    typeFilter: Optional[WorkflowTypeFilter] = None
    tagFilter: Optional[TagFilter] = None
    closeStatusFilter: Optional[CloseStatusFilter] = None


class CountOpenWorkflowExecutionsInput(BaseValidatorModel):
    domain: str
    startTimeFilter: ExecutionTimeFilter
    typeFilter: Optional[WorkflowTypeFilter] = None
    tagFilter: Optional[TagFilter] = None
    executionFilter: Optional[WorkflowExecutionFilter] = None


class ListClosedWorkflowExecutionsInputPaginate(BaseValidatorModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilter] = None
    closeTimeFilter: Optional[ExecutionTimeFilter] = None
    executionFilter: Optional[WorkflowExecutionFilter] = None
    closeStatusFilter: Optional[CloseStatusFilter] = None
    typeFilter: Optional[WorkflowTypeFilter] = None
    tagFilter: Optional[TagFilter] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClosedWorkflowExecutionsInput(BaseValidatorModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilter] = None
    closeTimeFilter: Optional[ExecutionTimeFilter] = None
    executionFilter: Optional[WorkflowExecutionFilter] = None
    closeStatusFilter: Optional[CloseStatusFilter] = None
    typeFilter: Optional[WorkflowTypeFilter] = None
    tagFilter: Optional[TagFilter] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class ListOpenWorkflowExecutionsInputPaginate(BaseValidatorModel):
    domain: str
    startTimeFilter: ExecutionTimeFilter
    typeFilter: Optional[WorkflowTypeFilter] = None
    tagFilter: Optional[TagFilter] = None
    reverseOrder: Optional[bool] = None
    executionFilter: Optional[WorkflowExecutionFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListOpenWorkflowExecutionsInput(BaseValidatorModel):
    domain: str
    startTimeFilter: ExecutionTimeFilter
    typeFilter: Optional[WorkflowTypeFilter] = None
    tagFilter: Optional[TagFilter] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None
    executionFilter: Optional[WorkflowExecutionFilter] = None


class RespondDecisionTaskCompletedInput(BaseValidatorModel):
    taskToken: str
    decisions: Optional[List[Decision]] = None
    executionContext: Optional[str] = None
    taskList: Optional[TaskList] = None
    taskListScheduleToStartTimeout: Optional[str] = None


class DecisionTask(BaseValidatorModel):
    taskToken: str
    startedEventId: int
    workflowExecution: WorkflowExecution
    workflowType: WorkflowType
    events: List[HistoryEvent]
    nextPageToken: str
    previousStartedEventId: int
    ResponseMetadata: ResponseMetadata


class History(BaseValidatorModel):
    events: List[HistoryEvent]
    nextPageToken: str
    ResponseMetadata: ResponseMetadata