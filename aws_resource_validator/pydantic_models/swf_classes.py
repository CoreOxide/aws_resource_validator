from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.swf_constants import *

class ActivityTaskCancelRequestedEventAttributesTypeDef(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    activityId: str


class ActivityTaskCanceledEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    details: Optional[str] = None
    latestCancelRequestedEventId: Optional[int] = None


class ActivityTaskCompletedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    result: Optional[str] = None


class ActivityTaskFailedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class ActivityTypeTypeDef(BaseValidatorModel):
    name: str
    version: str


class TaskListTypeDef(BaseValidatorModel):
    name: str


class ActivityTaskStartedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    identity: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ActivityTaskTimedOutEventAttributesTypeDef(BaseValidatorModel):
    timeoutType: ActivityTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int
    details: Optional[str] = None


class WorkflowExecutionTypeDef(BaseValidatorModel):
    workflowId: str
    runId: str


class CancelTimerDecisionAttributesTypeDef(BaseValidatorModel):
    timerId: str


class CancelTimerFailedEventAttributesTypeDef(BaseValidatorModel):
    timerId: str
    cause: CancelTimerFailedCauseType
    decisionTaskCompletedEventId: int


class CancelWorkflowExecutionDecisionAttributesTypeDef(BaseValidatorModel):
    details: Optional[str] = None


class CancelWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    cause: CancelWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class WorkflowTypeTypeDef(BaseValidatorModel):
    name: str
    version: str


class CloseStatusFilterTypeDef(BaseValidatorModel):
    status: CloseStatusType


class CompleteWorkflowExecutionDecisionAttributesTypeDef(BaseValidatorModel):
    result: Optional[str] = None


class CompleteWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    cause: CompleteWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    cause: ContinueAsNewWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class TagFilterTypeDef(BaseValidatorModel):
    tag: str


class WorkflowExecutionFilterTypeDef(BaseValidatorModel):
    workflowId: str


class WorkflowTypeFilterTypeDef(BaseValidatorModel):
    name: str
    version: Optional[str] = None


class DecisionTaskStartedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    identity: Optional[str] = None


class DecisionTaskTimedOutEventAttributesTypeDef(BaseValidatorModel):
    timeoutType: DecisionTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int


class FailWorkflowExecutionDecisionAttributesTypeDef(BaseValidatorModel):
    reason: Optional[str] = None
    details: Optional[str] = None


class RecordMarkerDecisionAttributesTypeDef(BaseValidatorModel):
    markerName: str
    details: Optional[str] = None


class RequestCancelActivityTaskDecisionAttributesTypeDef(BaseValidatorModel):
    activityId: str


class RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef(BaseValidatorModel):
    workflowId: str
    runId: Optional[str] = None
    control: Optional[str] = None


class StartTimerDecisionAttributesTypeDef(BaseValidatorModel):
    timerId: str
    startToFireTimeout: str
    control: Optional[str] = None


class DeprecateDomainInputTypeDef(BaseValidatorModel):
    name: str


class DescribeDomainInputTypeDef(BaseValidatorModel):
    name: str


class DomainConfigurationTypeDef(BaseValidatorModel):
    workflowExecutionRetentionPeriodInDays: str


class DomainInfoTypeDef(BaseValidatorModel):
    name: str
    status: RegistrationStatusType
    description: Optional[str] = None
    arn: Optional[str] = None


class FailWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    cause: FailWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class LambdaFunctionCompletedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    result: Optional[str] = None


class LambdaFunctionFailedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class LambdaFunctionStartedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int


class LambdaFunctionTimedOutEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    timeoutType: Optional[Literal["START_TO_CLOSE"]] = None


class MarkerRecordedEventAttributesTypeDef(BaseValidatorModel):
    markerName: str
    decisionTaskCompletedEventId: int
    details: Optional[str] = None


class RecordMarkerFailedEventAttributesTypeDef(BaseValidatorModel):
    markerName: str
    cause: Literal["OPERATION_NOT_PERMITTED"]
    decisionTaskCompletedEventId: int


class RequestCancelActivityTaskFailedEventAttributesTypeDef(BaseValidatorModel):
    activityId: str
    cause: RequestCancelActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int


class RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    workflowId: str
    cause: RequestCancelExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef(BaseValidatorModel):
    workflowId: str
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None


class SignalExternalWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    workflowId: str
    cause: SignalExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None


class StartLambdaFunctionFailedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: Optional[int] = None
    cause: Optional[Literal["ASSUME_ROLE_FAILED"]] = None
    message: Optional[str] = None


class StartTimerFailedEventAttributesTypeDef(BaseValidatorModel):
    timerId: str
    cause: StartTimerFailedCauseType
    decisionTaskCompletedEventId: int


class TimerCanceledEventAttributesTypeDef(BaseValidatorModel):
    timerId: str
    startedEventId: int
    decisionTaskCompletedEventId: int


class TimerFiredEventAttributesTypeDef(BaseValidatorModel):
    timerId: str
    startedEventId: int


class TimerStartedEventAttributesTypeDef(BaseValidatorModel):
    timerId: str
    startToFireTimeout: str
    decisionTaskCompletedEventId: int
    control: Optional[str] = None


class WorkflowExecutionCanceledEventAttributesTypeDef(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    details: Optional[str] = None


class WorkflowExecutionCompletedEventAttributesTypeDef(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    result: Optional[str] = None


class WorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    decisionTaskCompletedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class WorkflowExecutionTerminatedEventAttributesTypeDef(BaseValidatorModel):
    childPolicy: ChildPolicyType
    reason: Optional[str] = None
    details: Optional[str] = None
    cause: Optional[WorkflowExecutionTerminatedCauseType] = None


class WorkflowExecutionTimedOutEventAttributesTypeDef(BaseValidatorModel):
    timeoutType: Literal["START_TO_CLOSE"]
    childPolicy: ChildPolicyType


class ListActivityTypesInputTypeDef(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class ListDomainsInputTypeDef(BaseValidatorModel):
    registrationStatus: RegistrationStatusType
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class ResourceTagTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class ListWorkflowTypesInputTypeDef(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class RecordActivityTaskHeartbeatInputTypeDef(BaseValidatorModel):
    taskToken: str
    details: Optional[str] = None


class RequestCancelWorkflowExecutionInputTypeDef(BaseValidatorModel):
    domain: str
    workflowId: str
    runId: Optional[str] = None


class RespondActivityTaskCanceledInputTypeDef(BaseValidatorModel):
    taskToken: str
    details: Optional[str] = None


class RespondActivityTaskCompletedInputTypeDef(BaseValidatorModel):
    taskToken: str
    result: Optional[str] = None


class RespondActivityTaskFailedInputTypeDef(BaseValidatorModel):
    taskToken: str
    reason: Optional[str] = None
    details: Optional[str] = None


class TerminateWorkflowExecutionInputTypeDef(BaseValidatorModel):
    domain: str
    workflowId: str
    runId: Optional[str] = None
    reason: Optional[str] = None
    details: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None


class UndeprecateDomainInputTypeDef(BaseValidatorModel):
    name: str


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class WorkflowExecutionOpenCountsTypeDef(BaseValidatorModel):
    openActivityTasks: int
    openDecisionTasks: int
    openTimers: int
    openChildWorkflowExecutions: int
    openLambdaFunctions: Optional[int] = None


class ActivityTypeInfoTypeDef(BaseValidatorModel):
    activityType: ActivityTypeTypeDef
    status: RegistrationStatusType
    creationDate: datetime
    description: Optional[str] = None
    deprecationDate: Optional[datetime] = None


class DeleteActivityTypeInputTypeDef(BaseValidatorModel):
    domain: str
    activityType: ActivityTypeTypeDef


class DeprecateActivityTypeInputTypeDef(BaseValidatorModel):
    domain: str
    activityType: ActivityTypeTypeDef


class DescribeActivityTypeInputTypeDef(BaseValidatorModel):
    domain: str
    activityType: ActivityTypeTypeDef


class ScheduleActivityTaskFailedEventAttributesTypeDef(BaseValidatorModel):
    activityType: ActivityTypeTypeDef
    activityId: str
    cause: ScheduleActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int


class UndeprecateActivityTypeInputTypeDef(BaseValidatorModel):
    domain: str
    activityType: ActivityTypeTypeDef


class ActivityTypeConfigurationTypeDef(BaseValidatorModel):
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultTaskHeartbeatTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskListTypeDef] = None
    defaultTaskPriority: Optional[str] = None
    defaultTaskScheduleToStartTimeout: Optional[str] = None
    defaultTaskScheduleToCloseTimeout: Optional[str] = None


class CountPendingActivityTasksInputTypeDef(BaseValidatorModel):
    domain: str
    taskList: TaskListTypeDef


class CountPendingDecisionTasksInputTypeDef(BaseValidatorModel):
    domain: str
    taskList: TaskListTypeDef


class DecisionTaskCompletedEventAttributesTypeDef(BaseValidatorModel):
    scheduledEventId: int
    startedEventId: int
    executionContext: Optional[str] = None
    taskList: Optional[TaskListTypeDef] = None
    taskListScheduleToStartTimeout: Optional[str] = None


class DecisionTaskScheduledEventAttributesTypeDef(BaseValidatorModel):
    taskList: TaskListTypeDef
    taskPriority: Optional[str] = None
    startToCloseTimeout: Optional[str] = None
    scheduleToStartTimeout: Optional[str] = None


class PollForActivityTaskInputTypeDef(BaseValidatorModel):
    domain: str
    taskList: TaskListTypeDef
    identity: Optional[str] = None


class PollForDecisionTaskInputTypeDef(BaseValidatorModel):
    domain: str
    taskList: TaskListTypeDef
    identity: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None
    startAtPreviousStartedEvent: Optional[bool] = None


class RegisterActivityTypeInputTypeDef(BaseValidatorModel):
    domain: str
    name: str
    version: str
    description: Optional[str] = None
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultTaskHeartbeatTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskListTypeDef] = None
    defaultTaskPriority: Optional[str] = None
    defaultTaskScheduleToStartTimeout: Optional[str] = None
    defaultTaskScheduleToCloseTimeout: Optional[str] = None


class RegisterWorkflowTypeInputTypeDef(BaseValidatorModel):
    domain: str
    name: str
    version: str
    description: Optional[str] = None
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultExecutionStartToCloseTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskListTypeDef] = None
    defaultTaskPriority: Optional[str] = None
    defaultChildPolicy: Optional[ChildPolicyType] = None
    defaultLambdaRole: Optional[str] = None


class WorkflowExecutionConfigurationTypeDef(BaseValidatorModel):
    taskStartToCloseTimeout: str
    executionStartToCloseTimeout: str
    taskList: TaskListTypeDef
    childPolicy: ChildPolicyType
    taskPriority: Optional[str] = None
    lambdaRole: Optional[str] = None


class WorkflowTypeConfigurationTypeDef(BaseValidatorModel):
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultExecutionStartToCloseTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskListTypeDef] = None
    defaultTaskPriority: Optional[str] = None
    defaultChildPolicy: Optional[ChildPolicyType] = None
    defaultLambdaRole: Optional[str] = None


class ActivityTaskStatusTypeDef(BaseValidatorModel):
    cancelRequested: bool
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class PendingTaskCountTypeDef(BaseValidatorModel):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef


class RunTypeDef(BaseValidatorModel):
    runId: str
    ResponseMetadata: ResponseMetadataTypeDef


class WorkflowExecutionCountTypeDef(BaseValidatorModel):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeWorkflowExecutionInputTypeDef(BaseValidatorModel):
    domain: str
    execution: WorkflowExecutionTypeDef


class ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    initiatedEventId: int


class ExternalWorkflowExecutionSignaledEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    initiatedEventId: int


class GetWorkflowExecutionHistoryInputTypeDef(BaseValidatorModel):
    domain: str
    execution: WorkflowExecutionTypeDef
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class WorkflowExecutionCancelRequestedEventAttributesTypeDef(BaseValidatorModel):
    externalWorkflowExecution: Optional[WorkflowExecutionTypeDef] = None
    externalInitiatedEventId: Optional[int] = None
    cause: Optional[Literal["CHILD_POLICY_APPLIED"]] = None


class ChildWorkflowExecutionCanceledEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    details: Optional[str] = None


class ChildWorkflowExecutionCompletedEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    result: Optional[str] = None


class ChildWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None


class ChildWorkflowExecutionStartedEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int


class ChildWorkflowExecutionTerminatedEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int


class ChildWorkflowExecutionTimedOutEventAttributesTypeDef(BaseValidatorModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    timeoutType: Literal["START_TO_CLOSE"]
    initiatedEventId: int
    startedEventId: int


class DeleteWorkflowTypeInputTypeDef(BaseValidatorModel):
    domain: str
    workflowType: WorkflowTypeTypeDef


class DeprecateWorkflowTypeInputTypeDef(BaseValidatorModel):
    domain: str
    workflowType: WorkflowTypeTypeDef


class DescribeWorkflowTypeInputTypeDef(BaseValidatorModel):
    domain: str
    workflowType: WorkflowTypeTypeDef


class StartChildWorkflowExecutionFailedEventAttributesTypeDef(BaseValidatorModel):
    workflowType: WorkflowTypeTypeDef
    cause: StartChildWorkflowExecutionFailedCauseType
    workflowId: str
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    control: Optional[str] = None


class UndeprecateWorkflowTypeInputTypeDef(BaseValidatorModel):
    domain: str
    workflowType: WorkflowTypeTypeDef


class WorkflowExecutionInfoTypeDef(BaseValidatorModel):
    execution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    startTimestamp: datetime
    executionStatus: ExecutionStatusType
    closeTimestamp: Optional[datetime] = None
    closeStatus: Optional[CloseStatusType] = None
    parent: Optional[WorkflowExecutionTypeDef] = None
    tagList: Optional[List[str]] = None
    cancelRequested: Optional[bool] = None


class WorkflowTypeInfoTypeDef(BaseValidatorModel):
    workflowType: WorkflowTypeTypeDef
    status: RegistrationStatusType
    creationDate: datetime
    description: Optional[str] = None
    deprecationDate: Optional[datetime] = None


class DomainDetailTypeDef(BaseValidatorModel):
    domainInfo: DomainInfoTypeDef
    configuration: DomainConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DomainInfosTypeDef(BaseValidatorModel):
    domainInfos: List[DomainInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class ExecutionTimeFilterTypeDef(BaseValidatorModel):
    oldestDate: TimestampTypeDef
    latestDate: Optional[TimestampTypeDef] = None


class GetWorkflowExecutionHistoryInputPaginateTypeDef(BaseValidatorModel):
    domain: str
    execution: WorkflowExecutionTypeDef
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListActivityTypesInputPaginateTypeDef(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainsInputPaginateTypeDef(BaseValidatorModel):
    registrationStatus: RegistrationStatusType
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkflowTypesInputPaginateTypeDef(BaseValidatorModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class PollForDecisionTaskInputPaginateTypeDef(BaseValidatorModel):
    domain: str
    taskList: TaskListTypeDef
    identity: Optional[str] = None
    reverseOrder: Optional[bool] = None
    startAtPreviousStartedEvent: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterDomainInputTypeDef(BaseValidatorModel):
    name: str
    workflowExecutionRetentionPeriodInDays: str
    description: Optional[str] = None
    tags: Optional[Sequence[ResourceTagTypeDef]] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[ResourceTagTypeDef]


class ActivityTypeInfosTypeDef(BaseValidatorModel):
    typeInfos: List[ActivityTypeInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ActivityTypeDetailTypeDef(BaseValidatorModel):
    typeInfo: ActivityTypeInfoTypeDef
    configuration: ActivityTypeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SignalExternalWorkflowExecutionDecisionAttributesTypeDef(BaseValidatorModel):
    pass


class StartChildWorkflowExecutionDecisionAttributesTypeDef(BaseValidatorModel):
    pass


class ScheduleLambdaFunctionDecisionAttributesTypeDef(BaseValidatorModel):
    pass


class ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef(BaseValidatorModel):
    pass


class ScheduleActivityTaskDecisionAttributesTypeDef(BaseValidatorModel):
    pass


class DecisionTypeDef(BaseValidatorModel):
    decisionType: DecisionTypeType
    scheduleActivityTaskDecisionAttributes: Optional[ ScheduleActivityTaskDecisionAttributesTypeDef ] = None
    requestCancelActivityTaskDecisionAttributes: Optional[ RequestCancelActivityTaskDecisionAttributesTypeDef ] = None
    completeWorkflowExecutionDecisionAttributes: Optional[ CompleteWorkflowExecutionDecisionAttributesTypeDef ] = None
    failWorkflowExecutionDecisionAttributes: Optional[ FailWorkflowExecutionDecisionAttributesTypeDef ] = None
    cancelWorkflowExecutionDecisionAttributes: Optional[ CancelWorkflowExecutionDecisionAttributesTypeDef ] = None
    continueAsNewWorkflowExecutionDecisionAttributes: Optional[ ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef ] = None
    recordMarkerDecisionAttributes: Optional[RecordMarkerDecisionAttributesTypeDef] = None
    startTimerDecisionAttributes: Optional[StartTimerDecisionAttributesTypeDef] = None
    cancelTimerDecisionAttributes: Optional[CancelTimerDecisionAttributesTypeDef] = None
    signalExternalWorkflowExecutionDecisionAttributes: Optional[ SignalExternalWorkflowExecutionDecisionAttributesTypeDef ] = None
    requestCancelExternalWorkflowExecutionDecisionAttributes: Optional[ RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef ] = None
    startChildWorkflowExecutionDecisionAttributes: Optional[ StartChildWorkflowExecutionDecisionAttributesTypeDef ] = None
    scheduleLambdaFunctionDecisionAttributes: Optional[ ScheduleLambdaFunctionDecisionAttributesTypeDef ] = None


class WorkflowExecutionDetailTypeDef(BaseValidatorModel):
    executionInfo: WorkflowExecutionInfoTypeDef
    executionConfiguration: WorkflowExecutionConfigurationTypeDef
    openCounts: WorkflowExecutionOpenCountsTypeDef
    latestActivityTaskTimestamp: datetime
    latestExecutionContext: str
    ResponseMetadata: ResponseMetadataTypeDef


class WorkflowExecutionInfosTypeDef(BaseValidatorModel):
    executionInfos: List[WorkflowExecutionInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class WorkflowExecutionContinuedAsNewEventAttributesTypeDef(BaseValidatorModel):
    pass


class ScheduleLambdaFunctionFailedEventAttributesTypeDef(BaseValidatorModel):
    pass


class StartChildWorkflowExecutionInitiatedEventAttributesTypeDef(BaseValidatorModel):
    pass


class WorkflowExecutionSignaledEventAttributesTypeDef(BaseValidatorModel):
    pass


class SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef(BaseValidatorModel):
    pass


class LambdaFunctionScheduledEventAttributesTypeDef(BaseValidatorModel):
    pass


class WorkflowExecutionStartedEventAttributesTypeDef(BaseValidatorModel):
    pass


class ActivityTaskScheduledEventAttributesTypeDef(BaseValidatorModel):
    pass


class HistoryEventTypeDef(BaseValidatorModel):
    eventTimestamp: datetime
    eventType: EventTypeType
    eventId: int
    workflowExecutionStartedEventAttributes: Optional[ WorkflowExecutionStartedEventAttributesTypeDef ] = None
    workflowExecutionCompletedEventAttributes: Optional[ WorkflowExecutionCompletedEventAttributesTypeDef ] = None
    completeWorkflowExecutionFailedEventAttributes: Optional[ CompleteWorkflowExecutionFailedEventAttributesTypeDef ] = None
    workflowExecutionFailedEventAttributes: Optional[ WorkflowExecutionFailedEventAttributesTypeDef ] = None
    failWorkflowExecutionFailedEventAttributes: Optional[ FailWorkflowExecutionFailedEventAttributesTypeDef ] = None
    workflowExecutionTimedOutEventAttributes: Optional[ WorkflowExecutionTimedOutEventAttributesTypeDef ] = None
    workflowExecutionCanceledEventAttributes: Optional[ WorkflowExecutionCanceledEventAttributesTypeDef ] = None
    cancelWorkflowExecutionFailedEventAttributes: Optional[ CancelWorkflowExecutionFailedEventAttributesTypeDef ] = None
    workflowExecutionContinuedAsNewEventAttributes: Optional[ WorkflowExecutionContinuedAsNewEventAttributesTypeDef ] = None
    continueAsNewWorkflowExecutionFailedEventAttributes: Optional[ ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef ] = None
    workflowExecutionTerminatedEventAttributes: Optional[ WorkflowExecutionTerminatedEventAttributesTypeDef ] = None
    workflowExecutionCancelRequestedEventAttributes: Optional[ WorkflowExecutionCancelRequestedEventAttributesTypeDef ] = None
    decisionTaskScheduledEventAttributes: Optional[DecisionTaskScheduledEventAttributesTypeDef] = None
    decisionTaskStartedEventAttributes: Optional[DecisionTaskStartedEventAttributesTypeDef] = None
    decisionTaskCompletedEventAttributes: Optional[DecisionTaskCompletedEventAttributesTypeDef] = None
    decisionTaskTimedOutEventAttributes: Optional[DecisionTaskTimedOutEventAttributesTypeDef] = None
    activityTaskScheduledEventAttributes: Optional[ActivityTaskScheduledEventAttributesTypeDef] = None
    activityTaskStartedEventAttributes: Optional[ActivityTaskStartedEventAttributesTypeDef] = None
    activityTaskCompletedEventAttributes: Optional[ActivityTaskCompletedEventAttributesTypeDef] = None
    activityTaskFailedEventAttributes: Optional[ActivityTaskFailedEventAttributesTypeDef] = None
    activityTaskTimedOutEventAttributes: Optional[ActivityTaskTimedOutEventAttributesTypeDef] = None
    activityTaskCanceledEventAttributes: Optional[ActivityTaskCanceledEventAttributesTypeDef] = None
    activityTaskCancelRequestedEventAttributes: Optional[ ActivityTaskCancelRequestedEventAttributesTypeDef ] = None
    workflowExecutionSignaledEventAttributes: Optional[ WorkflowExecutionSignaledEventAttributesTypeDef ] = None
    markerRecordedEventAttributes: Optional[MarkerRecordedEventAttributesTypeDef] = None
    recordMarkerFailedEventAttributes: Optional[RecordMarkerFailedEventAttributesTypeDef] = None
    timerStartedEventAttributes: Optional[TimerStartedEventAttributesTypeDef] = None
    timerFiredEventAttributes: Optional[TimerFiredEventAttributesTypeDef] = None
    timerCanceledEventAttributes: Optional[TimerCanceledEventAttributesTypeDef] = None
    startChildWorkflowExecutionInitiatedEventAttributes: Optional[ StartChildWorkflowExecutionInitiatedEventAttributesTypeDef ] = None
    childWorkflowExecutionStartedEventAttributes: Optional[ ChildWorkflowExecutionStartedEventAttributesTypeDef ] = None
    childWorkflowExecutionCompletedEventAttributes: Optional[ ChildWorkflowExecutionCompletedEventAttributesTypeDef ] = None
    childWorkflowExecutionFailedEventAttributes: Optional[ ChildWorkflowExecutionFailedEventAttributesTypeDef ] = None
    childWorkflowExecutionTimedOutEventAttributes: Optional[ ChildWorkflowExecutionTimedOutEventAttributesTypeDef ] = None
    childWorkflowExecutionCanceledEventAttributes: Optional[ ChildWorkflowExecutionCanceledEventAttributesTypeDef ] = None
    childWorkflowExecutionTerminatedEventAttributes: Optional[ ChildWorkflowExecutionTerminatedEventAttributesTypeDef ] = None
    signalExternalWorkflowExecutionInitiatedEventAttributes: Optional[ SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef ] = None
    externalWorkflowExecutionSignaledEventAttributes: Optional[ ExternalWorkflowExecutionSignaledEventAttributesTypeDef ] = None
    signalExternalWorkflowExecutionFailedEventAttributes: Optional[ SignalExternalWorkflowExecutionFailedEventAttributesTypeDef ] = None
    externalWorkflowExecutionCancelRequestedEventAttributes: Optional[ ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef ] = None
    requestCancelExternalWorkflowExecutionInitiatedEventAttributes: Optional[ RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef ] = None
    requestCancelExternalWorkflowExecutionFailedEventAttributes: Optional[ RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef ] = None
    scheduleActivityTaskFailedEventAttributes: Optional[ ScheduleActivityTaskFailedEventAttributesTypeDef ] = None
    requestCancelActivityTaskFailedEventAttributes: Optional[ RequestCancelActivityTaskFailedEventAttributesTypeDef ] = None
    startTimerFailedEventAttributes: Optional[StartTimerFailedEventAttributesTypeDef] = None
    cancelTimerFailedEventAttributes: Optional[CancelTimerFailedEventAttributesTypeDef] = None
    startChildWorkflowExecutionFailedEventAttributes: Optional[ StartChildWorkflowExecutionFailedEventAttributesTypeDef ] = None
    lambdaFunctionScheduledEventAttributes: Optional[ LambdaFunctionScheduledEventAttributesTypeDef ] = None
    lambdaFunctionStartedEventAttributes: Optional[LambdaFunctionStartedEventAttributesTypeDef] = None
    lambdaFunctionCompletedEventAttributes: Optional[ LambdaFunctionCompletedEventAttributesTypeDef ] = None
    lambdaFunctionFailedEventAttributes: Optional[LambdaFunctionFailedEventAttributesTypeDef] = None
    lambdaFunctionTimedOutEventAttributes: Optional[LambdaFunctionTimedOutEventAttributesTypeDef] = None
    scheduleLambdaFunctionFailedEventAttributes: Optional[ ScheduleLambdaFunctionFailedEventAttributesTypeDef ] = None
    startLambdaFunctionFailedEventAttributes: Optional[ StartLambdaFunctionFailedEventAttributesTypeDef ] = None


class WorkflowTypeDetailTypeDef(BaseValidatorModel):
    typeInfo: WorkflowTypeInfoTypeDef
    configuration: WorkflowTypeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WorkflowTypeInfosTypeDef(BaseValidatorModel):
    typeInfos: List[WorkflowTypeInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class CountClosedWorkflowExecutionsInputTypeDef(BaseValidatorModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    closeTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    closeStatusFilter: Optional[CloseStatusFilterTypeDef] = None


class CountOpenWorkflowExecutionsInputTypeDef(BaseValidatorModel):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None


class ListClosedWorkflowExecutionsInputPaginateTypeDef(BaseValidatorModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    closeTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None
    closeStatusFilter: Optional[CloseStatusFilterTypeDef] = None
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClosedWorkflowExecutionsInputTypeDef(BaseValidatorModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    closeTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None
    closeStatusFilter: Optional[CloseStatusFilterTypeDef] = None
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None


class ListOpenWorkflowExecutionsInputPaginateTypeDef(BaseValidatorModel):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    reverseOrder: Optional[bool] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListOpenWorkflowExecutionsInputTypeDef(BaseValidatorModel):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None


class RespondDecisionTaskCompletedInputTypeDef(BaseValidatorModel):
    taskToken: str
    decisions: Optional[Sequence[DecisionTypeDef]] = None
    executionContext: Optional[str] = None
    taskList: Optional[TaskListTypeDef] = None
    taskListScheduleToStartTimeout: Optional[str] = None


class DecisionTaskTypeDef(BaseValidatorModel):
    taskToken: str
    startedEventId: int
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    events: List[HistoryEventTypeDef]
    nextPageToken: str
    previousStartedEventId: int
    ResponseMetadata: ResponseMetadataTypeDef


class HistoryTypeDef(BaseValidatorModel):
    events: List[HistoryEventTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef


