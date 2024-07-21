from datetime import datetime
from pydantic import BaseModel
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

class ActivityTaskCancelRequestedEventAttributesTypeDef(BaseModel):
    decisionTaskCompletedEventId: int
    activityId: str

class ActivityTaskCanceledEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    startedEventId: int
    details: Optional[str] = None
    latestCancelRequestedEventId: Optional[int] = None

class ActivityTaskCompletedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    startedEventId: int
    result: Optional[str] = None

class ActivityTaskFailedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None

class ActivityTypeTypeDef(BaseModel):
    name: str
    version: str

class TaskListTypeDef(BaseModel):
    name: str

class ActivityTaskStartedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    identity: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ActivityTaskTimedOutEventAttributesTypeDef(BaseModel):
    timeoutType: ActivityTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int
    details: Optional[str] = None

class WorkflowExecutionTypeDef(BaseModel):
    workflowId: str
    runId: str

class CancelTimerDecisionAttributesTypeDef(BaseModel):
    timerId: str

class CancelTimerFailedEventAttributesTypeDef(BaseModel):
    timerId: str
    cause: CancelTimerFailedCauseType
    decisionTaskCompletedEventId: int

class CancelWorkflowExecutionDecisionAttributesTypeDef(BaseModel):
    details: Optional[str] = None

class CancelWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    cause: CancelWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class WorkflowTypeTypeDef(BaseModel):
    name: str
    version: str

class CloseStatusFilterTypeDef(BaseModel):
    status: CloseStatusType

class CompleteWorkflowExecutionDecisionAttributesTypeDef(BaseModel):
    result: Optional[str] = None

class CompleteWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    cause: CompleteWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    cause: ContinueAsNewWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class TagFilterTypeDef(BaseModel):
    tag: str

class WorkflowExecutionFilterTypeDef(BaseModel):
    workflowId: str

class WorkflowTypeFilterTypeDef(BaseModel):
    name: str
    version: Optional[str] = None

class DecisionTaskStartedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    identity: Optional[str] = None

class DecisionTaskTimedOutEventAttributesTypeDef(BaseModel):
    timeoutType: DecisionTaskTimeoutTypeType
    scheduledEventId: int
    startedEventId: int

class FailWorkflowExecutionDecisionAttributesTypeDef(BaseModel):
    reason: Optional[str] = None
    details: Optional[str] = None

class RecordMarkerDecisionAttributesTypeDef(BaseModel):
    markerName: str
    details: Optional[str] = None

class RequestCancelActivityTaskDecisionAttributesTypeDef(BaseModel):
    activityId: str

class RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef(BaseModel):
    workflowId: str
    runId: Optional[str] = None
    control: Optional[str] = None

class ScheduleLambdaFunctionDecisionAttributesTypeDef(BaseModel):
    id: str
    name: str
    control: Optional[str] = None
    input: Optional[str] = None
    startToCloseTimeout: Optional[str] = None

class SignalExternalWorkflowExecutionDecisionAttributesTypeDef(BaseModel):
    workflowId: str
    signalName: str
    runId: Optional[str] = None
    input: Optional[str] = None
    control: Optional[str] = None

class StartTimerDecisionAttributesTypeDef(BaseModel):
    timerId: str
    startToFireTimeout: str
    control: Optional[str] = None

class DeprecateDomainInputRequestTypeDef(BaseModel):
    name: str

class DescribeDomainInputRequestTypeDef(BaseModel):
    name: str

class DomainConfigurationTypeDef(BaseModel):
    workflowExecutionRetentionPeriodInDays: str

class DomainInfoTypeDef(BaseModel):
    name: str
    status: RegistrationStatusType
    description: Optional[str] = None
    arn: Optional[str] = None

class FailWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    cause: FailWorkflowExecutionFailedCauseType
    decisionTaskCompletedEventId: int

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class LambdaFunctionCompletedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    startedEventId: int
    result: Optional[str] = None

class LambdaFunctionFailedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None

class LambdaFunctionScheduledEventAttributesTypeDef(BaseModel):
    id: str
    name: str
    decisionTaskCompletedEventId: int
    control: Optional[str] = None
    input: Optional[str] = None
    startToCloseTimeout: Optional[str] = None

class LambdaFunctionStartedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int

class LambdaFunctionTimedOutEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    startedEventId: int
    timeoutType: Optional[Literal["START_TO_CLOSE"]] = None

class MarkerRecordedEventAttributesTypeDef(BaseModel):
    markerName: str
    decisionTaskCompletedEventId: int
    details: Optional[str] = None

class RecordMarkerFailedEventAttributesTypeDef(BaseModel):
    markerName: str
    cause: Literal["OPERATION_NOT_PERMITTED"]
    decisionTaskCompletedEventId: int

class RequestCancelActivityTaskFailedEventAttributesTypeDef(BaseModel):
    activityId: str
    cause: RequestCancelActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int

class RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    workflowId: str
    cause: RequestCancelExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None

class RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef(BaseModel):
    workflowId: str
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None

class ScheduleLambdaFunctionFailedEventAttributesTypeDef(BaseModel):
    id: str
    name: str
    cause: ScheduleLambdaFunctionFailedCauseType
    decisionTaskCompletedEventId: int

class SignalExternalWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    workflowId: str
    cause: SignalExternalWorkflowExecutionFailedCauseType
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    control: Optional[str] = None

class SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef(BaseModel):
    workflowId: str
    signalName: str
    decisionTaskCompletedEventId: int
    runId: Optional[str] = None
    input: Optional[str] = None
    control: Optional[str] = None

class StartLambdaFunctionFailedEventAttributesTypeDef(BaseModel):
    scheduledEventId: Optional[int] = None
    cause: Optional[Literal["ASSUME_ROLE_FAILED"]] = None
    message: Optional[str] = None

class StartTimerFailedEventAttributesTypeDef(BaseModel):
    timerId: str
    cause: StartTimerFailedCauseType
    decisionTaskCompletedEventId: int

class TimerCanceledEventAttributesTypeDef(BaseModel):
    timerId: str
    startedEventId: int
    decisionTaskCompletedEventId: int

class TimerFiredEventAttributesTypeDef(BaseModel):
    timerId: str
    startedEventId: int

class TimerStartedEventAttributesTypeDef(BaseModel):
    timerId: str
    startToFireTimeout: str
    decisionTaskCompletedEventId: int
    control: Optional[str] = None

class WorkflowExecutionCanceledEventAttributesTypeDef(BaseModel):
    decisionTaskCompletedEventId: int
    details: Optional[str] = None

class WorkflowExecutionCompletedEventAttributesTypeDef(BaseModel):
    decisionTaskCompletedEventId: int
    result: Optional[str] = None

class WorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    decisionTaskCompletedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None

class WorkflowExecutionTerminatedEventAttributesTypeDef(BaseModel):
    childPolicy: ChildPolicyType
    reason: Optional[str] = None
    details: Optional[str] = None
    cause: Optional[WorkflowExecutionTerminatedCauseType] = None

class WorkflowExecutionTimedOutEventAttributesTypeDef(BaseModel):
    timeoutType: Literal["START_TO_CLOSE"]
    childPolicy: ChildPolicyType

class ListActivityTypesInputRequestTypeDef(BaseModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None

class ListDomainsInputRequestTypeDef(BaseModel):
    registrationStatus: RegistrationStatusType
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class ResourceTagTypeDef(BaseModel):
    key: str
    value: Optional[str] = None

class ListWorkflowTypesInputRequestTypeDef(BaseModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None

class RecordActivityTaskHeartbeatInputRequestTypeDef(BaseModel):
    taskToken: str
    details: Optional[str] = None

class RequestCancelWorkflowExecutionInputRequestTypeDef(BaseModel):
    domain: str
    workflowId: str
    runId: Optional[str] = None

class RespondActivityTaskCanceledInputRequestTypeDef(BaseModel):
    taskToken: str
    details: Optional[str] = None

class RespondActivityTaskCompletedInputRequestTypeDef(BaseModel):
    taskToken: str
    result: Optional[str] = None

class RespondActivityTaskFailedInputRequestTypeDef(BaseModel):
    taskToken: str
    reason: Optional[str] = None
    details: Optional[str] = None

class SignalWorkflowExecutionInputRequestTypeDef(BaseModel):
    domain: str
    workflowId: str
    signalName: str
    runId: Optional[str] = None
    input: Optional[str] = None

class TerminateWorkflowExecutionInputRequestTypeDef(BaseModel):
    domain: str
    workflowId: str
    runId: Optional[str] = None
    reason: Optional[str] = None
    details: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None

class UndeprecateDomainInputRequestTypeDef(BaseModel):
    name: str

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class WorkflowExecutionOpenCountsTypeDef(BaseModel):
    openActivityTasks: int
    openDecisionTasks: int
    openTimers: int
    openChildWorkflowExecutions: int
    openLambdaFunctions: Optional[int] = None

class ActivityTypeInfoTypeDef(BaseModel):
    activityType: ActivityTypeTypeDef
    status: RegistrationStatusType
    creationDate: datetime
    description: Optional[str] = None
    deprecationDate: Optional[datetime] = None

class DeleteActivityTypeInputRequestTypeDef(BaseModel):
    domain: str
    activityType: ActivityTypeTypeDef

class DeprecateActivityTypeInputRequestTypeDef(BaseModel):
    domain: str
    activityType: ActivityTypeTypeDef

class DescribeActivityTypeInputRequestTypeDef(BaseModel):
    domain: str
    activityType: ActivityTypeTypeDef

class ScheduleActivityTaskFailedEventAttributesTypeDef(BaseModel):
    activityType: ActivityTypeTypeDef
    activityId: str
    cause: ScheduleActivityTaskFailedCauseType
    decisionTaskCompletedEventId: int

class UndeprecateActivityTypeInputRequestTypeDef(BaseModel):
    domain: str
    activityType: ActivityTypeTypeDef

class ActivityTaskScheduledEventAttributesTypeDef(BaseModel):
    activityType: ActivityTypeTypeDef
    activityId: str
    taskList: TaskListTypeDef
    decisionTaskCompletedEventId: int
    input: Optional[str] = None
    control: Optional[str] = None
    scheduleToStartTimeout: Optional[str] = None
    scheduleToCloseTimeout: Optional[str] = None
    startToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    heartbeatTimeout: Optional[str] = None

class ActivityTypeConfigurationTypeDef(BaseModel):
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultTaskHeartbeatTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskListTypeDef] = None
    defaultTaskPriority: Optional[str] = None
    defaultTaskScheduleToStartTimeout: Optional[str] = None
    defaultTaskScheduleToCloseTimeout: Optional[str] = None

class ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef(BaseModel):
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskList: Optional[TaskListTypeDef] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None
    tagList: Optional[Sequence[str]] = None
    workflowTypeVersion: Optional[str] = None
    lambdaRole: Optional[str] = None

class CountPendingActivityTasksInputRequestTypeDef(BaseModel):
    domain: str
    taskList: TaskListTypeDef

class CountPendingDecisionTasksInputRequestTypeDef(BaseModel):
    domain: str
    taskList: TaskListTypeDef

class DecisionTaskCompletedEventAttributesTypeDef(BaseModel):
    scheduledEventId: int
    startedEventId: int
    executionContext: Optional[str] = None
    taskList: Optional[TaskListTypeDef] = None
    taskListScheduleToStartTimeout: Optional[str] = None

class DecisionTaskScheduledEventAttributesTypeDef(BaseModel):
    taskList: TaskListTypeDef
    taskPriority: Optional[str] = None
    startToCloseTimeout: Optional[str] = None
    scheduleToStartTimeout: Optional[str] = None

class PollForActivityTaskInputRequestTypeDef(BaseModel):
    domain: str
    taskList: TaskListTypeDef
    identity: Optional[str] = None

class PollForDecisionTaskInputRequestTypeDef(BaseModel):
    domain: str
    taskList: TaskListTypeDef
    identity: Optional[str] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None
    startAtPreviousStartedEvent: Optional[bool] = None

class RegisterActivityTypeInputRequestTypeDef(BaseModel):
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

class RegisterWorkflowTypeInputRequestTypeDef(BaseModel):
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

class ScheduleActivityTaskDecisionAttributesTypeDef(BaseModel):
    activityType: ActivityTypeTypeDef
    activityId: str
    control: Optional[str] = None
    input: Optional[str] = None
    scheduleToCloseTimeout: Optional[str] = None
    taskList: Optional[TaskListTypeDef] = None
    taskPriority: Optional[str] = None
    scheduleToStartTimeout: Optional[str] = None
    startToCloseTimeout: Optional[str] = None
    heartbeatTimeout: Optional[str] = None

class WorkflowExecutionConfigurationTypeDef(BaseModel):
    taskStartToCloseTimeout: str
    executionStartToCloseTimeout: str
    taskList: TaskListTypeDef
    childPolicy: ChildPolicyType
    taskPriority: Optional[str] = None
    lambdaRole: Optional[str] = None

class WorkflowTypeConfigurationTypeDef(BaseModel):
    defaultTaskStartToCloseTimeout: Optional[str] = None
    defaultExecutionStartToCloseTimeout: Optional[str] = None
    defaultTaskList: Optional[TaskListTypeDef] = None
    defaultTaskPriority: Optional[str] = None
    defaultChildPolicy: Optional[ChildPolicyType] = None
    defaultLambdaRole: Optional[str] = None

class ActivityTaskStatusTypeDef(BaseModel):
    cancelRequested: bool
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class PendingTaskCountTypeDef(BaseModel):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class RunTypeDef(BaseModel):
    runId: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowExecutionCountTypeDef(BaseModel):
    count: int
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class ActivityTaskTypeDef(BaseModel):
    taskToken: str
    activityId: str
    startedEventId: int
    workflowExecution: WorkflowExecutionTypeDef
    activityType: ActivityTypeTypeDef
    input: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkflowExecutionInputRequestTypeDef(BaseModel):
    domain: str
    execution: WorkflowExecutionTypeDef

class ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    initiatedEventId: int

class ExternalWorkflowExecutionSignaledEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    initiatedEventId: int

class GetWorkflowExecutionHistoryInputRequestTypeDef(BaseModel):
    domain: str
    execution: WorkflowExecutionTypeDef
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None

class WorkflowExecutionCancelRequestedEventAttributesTypeDef(BaseModel):
    externalWorkflowExecution: Optional[WorkflowExecutionTypeDef] = None
    externalInitiatedEventId: Optional[int] = None
    cause: Optional[Literal["CHILD_POLICY_APPLIED"]] = None

class WorkflowExecutionSignaledEventAttributesTypeDef(BaseModel):
    signalName: str
    input: Optional[str] = None
    externalWorkflowExecution: Optional[WorkflowExecutionTypeDef] = None
    externalInitiatedEventId: Optional[int] = None

class ChildWorkflowExecutionCanceledEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    details: Optional[str] = None

class ChildWorkflowExecutionCompletedEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    result: Optional[str] = None

class ChildWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int
    reason: Optional[str] = None
    details: Optional[str] = None

class ChildWorkflowExecutionStartedEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int

class ChildWorkflowExecutionTerminatedEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    initiatedEventId: int
    startedEventId: int

class ChildWorkflowExecutionTimedOutEventAttributesTypeDef(BaseModel):
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    timeoutType: Literal["START_TO_CLOSE"]
    initiatedEventId: int
    startedEventId: int

class DeleteWorkflowTypeInputRequestTypeDef(BaseModel):
    domain: str
    workflowType: WorkflowTypeTypeDef

class DeprecateWorkflowTypeInputRequestTypeDef(BaseModel):
    domain: str
    workflowType: WorkflowTypeTypeDef

class DescribeWorkflowTypeInputRequestTypeDef(BaseModel):
    domain: str
    workflowType: WorkflowTypeTypeDef

class StartChildWorkflowExecutionDecisionAttributesTypeDef(BaseModel):
    workflowType: WorkflowTypeTypeDef
    workflowId: str
    control: Optional[str] = None
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskList: Optional[TaskListTypeDef] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None
    tagList: Optional[Sequence[str]] = None
    lambdaRole: Optional[str] = None

class StartChildWorkflowExecutionFailedEventAttributesTypeDef(BaseModel):
    workflowType: WorkflowTypeTypeDef
    cause: StartChildWorkflowExecutionFailedCauseType
    workflowId: str
    initiatedEventId: int
    decisionTaskCompletedEventId: int
    control: Optional[str] = None

class StartChildWorkflowExecutionInitiatedEventAttributesTypeDef(BaseModel):
    workflowId: str
    workflowType: WorkflowTypeTypeDef
    taskList: TaskListTypeDef
    decisionTaskCompletedEventId: int
    childPolicy: ChildPolicyType
    control: Optional[str] = None
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    tagList: Optional[List[str]] = None
    lambdaRole: Optional[str] = None

class StartWorkflowExecutionInputRequestTypeDef(BaseModel):
    domain: str
    workflowId: str
    workflowType: WorkflowTypeTypeDef
    taskList: Optional[TaskListTypeDef] = None
    taskPriority: Optional[str] = None
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    tagList: Optional[Sequence[str]] = None
    taskStartToCloseTimeout: Optional[str] = None
    childPolicy: Optional[ChildPolicyType] = None
    lambdaRole: Optional[str] = None

class UndeprecateWorkflowTypeInputRequestTypeDef(BaseModel):
    domain: str
    workflowType: WorkflowTypeTypeDef

class WorkflowExecutionContinuedAsNewEventAttributesTypeDef(BaseModel):
    decisionTaskCompletedEventId: int
    newExecutionRunId: str
    taskList: TaskListTypeDef
    childPolicy: ChildPolicyType
    workflowType: WorkflowTypeTypeDef
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    tagList: Optional[List[str]] = None
    lambdaRole: Optional[str] = None

class WorkflowExecutionInfoTypeDef(BaseModel):
    execution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    startTimestamp: datetime
    executionStatus: ExecutionStatusType
    closeTimestamp: Optional[datetime] = None
    closeStatus: Optional[CloseStatusType] = None
    parent: Optional[WorkflowExecutionTypeDef] = None
    tagList: Optional[List[str]] = None
    cancelRequested: Optional[bool] = None

class WorkflowExecutionStartedEventAttributesTypeDef(BaseModel):
    childPolicy: ChildPolicyType
    taskList: TaskListTypeDef
    workflowType: WorkflowTypeTypeDef
    input: Optional[str] = None
    executionStartToCloseTimeout: Optional[str] = None
    taskStartToCloseTimeout: Optional[str] = None
    taskPriority: Optional[str] = None
    tagList: Optional[List[str]] = None
    continuedExecutionRunId: Optional[str] = None
    parentWorkflowExecution: Optional[WorkflowExecutionTypeDef] = None
    parentInitiatedEventId: Optional[int] = None
    lambdaRole: Optional[str] = None

class WorkflowTypeInfoTypeDef(BaseModel):
    workflowType: WorkflowTypeTypeDef
    status: RegistrationStatusType
    creationDate: datetime
    description: Optional[str] = None
    deprecationDate: Optional[datetime] = None

class DomainDetailTypeDef(BaseModel):
    domainInfo: DomainInfoTypeDef
    configuration: DomainConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DomainInfosTypeDef(BaseModel):
    domainInfos: List[DomainInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecutionTimeFilterTypeDef(BaseModel):
    oldestDate: TimestampTypeDef
    latestDate: Optional[TimestampTypeDef] = None

class GetWorkflowExecutionHistoryInputGetWorkflowExecutionHistoryPaginateTypeDef(BaseModel):
    domain: str
    execution: WorkflowExecutionTypeDef
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListActivityTypesInputListActivityTypesPaginateTypeDef(BaseModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsInputListDomainsPaginateTypeDef(BaseModel):
    registrationStatus: RegistrationStatusType
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowTypesInputListWorkflowTypesPaginateTypeDef(BaseModel):
    domain: str
    registrationStatus: RegistrationStatusType
    name: Optional[str] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class PollForDecisionTaskInputPollForDecisionTaskPaginateTypeDef(BaseModel):
    domain: str
    taskList: TaskListTypeDef
    identity: Optional[str] = None
    reverseOrder: Optional[bool] = None
    startAtPreviousStartedEvent: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterDomainInputRequestTypeDef(BaseModel):
    name: str
    workflowExecutionRetentionPeriodInDays: str
    description: Optional[str] = None
    tags: Optional[Sequence[ResourceTagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[ResourceTagTypeDef]

class ActivityTypeInfosTypeDef(BaseModel):
    typeInfos: List[ActivityTypeInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActivityTypeDetailTypeDef(BaseModel):
    typeInfo: ActivityTypeInfoTypeDef
    configuration: ActivityTypeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecisionTypeDef(BaseModel):
    decisionType: DecisionTypeType
    scheduleActivityTaskDecisionAttributes: Optional[       ScheduleActivityTaskDecisionAttributesTypeDef     ] = None
    requestCancelActivityTaskDecisionAttributes: Optional[       RequestCancelActivityTaskDecisionAttributesTypeDef     ] = None
    completeWorkflowExecutionDecisionAttributes: Optional[       CompleteWorkflowExecutionDecisionAttributesTypeDef     ] = None
    failWorkflowExecutionDecisionAttributes: Optional[       FailWorkflowExecutionDecisionAttributesTypeDef     ] = None
    cancelWorkflowExecutionDecisionAttributes: Optional[       CancelWorkflowExecutionDecisionAttributesTypeDef     ] = None
    continueAsNewWorkflowExecutionDecisionAttributes: Optional[       ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef     ] = None
    recordMarkerDecisionAttributes: Optional[RecordMarkerDecisionAttributesTypeDef] = None
    startTimerDecisionAttributes: Optional[StartTimerDecisionAttributesTypeDef] = None
    cancelTimerDecisionAttributes: Optional[CancelTimerDecisionAttributesTypeDef] = None
    signalExternalWorkflowExecutionDecisionAttributes: Optional[       SignalExternalWorkflowExecutionDecisionAttributesTypeDef     ] = None
    requestCancelExternalWorkflowExecutionDecisionAttributes: Optional[       RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef     ] = None
    startChildWorkflowExecutionDecisionAttributes: Optional[       StartChildWorkflowExecutionDecisionAttributesTypeDef     ] = None
    scheduleLambdaFunctionDecisionAttributes: Optional[       ScheduleLambdaFunctionDecisionAttributesTypeDef     ] = None

class WorkflowExecutionDetailTypeDef(BaseModel):
    executionInfo: WorkflowExecutionInfoTypeDef
    executionConfiguration: WorkflowExecutionConfigurationTypeDef
    openCounts: WorkflowExecutionOpenCountsTypeDef
    latestActivityTaskTimestamp: datetime
    latestExecutionContext: str
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowExecutionInfosTypeDef(BaseModel):
    executionInfos: List[WorkflowExecutionInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class HistoryEventTypeDef(BaseModel):
    eventTimestamp: datetime
    eventType: EventTypeType
    eventId: int
    workflowExecutionStartedEventAttributes: Optional[       WorkflowExecutionStartedEventAttributesTypeDef     ] = None
    workflowExecutionCompletedEventAttributes: Optional[       WorkflowExecutionCompletedEventAttributesTypeDef     ] = None
    completeWorkflowExecutionFailedEventAttributes: Optional[       CompleteWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    workflowExecutionFailedEventAttributes: Optional[       WorkflowExecutionFailedEventAttributesTypeDef     ] = None
    failWorkflowExecutionFailedEventAttributes: Optional[       FailWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    workflowExecutionTimedOutEventAttributes: Optional[       WorkflowExecutionTimedOutEventAttributesTypeDef     ] = None
    workflowExecutionCanceledEventAttributes: Optional[       WorkflowExecutionCanceledEventAttributesTypeDef     ] = None
    cancelWorkflowExecutionFailedEventAttributes: Optional[       CancelWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    workflowExecutionContinuedAsNewEventAttributes: Optional[       WorkflowExecutionContinuedAsNewEventAttributesTypeDef     ] = None
    continueAsNewWorkflowExecutionFailedEventAttributes: Optional[       ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    workflowExecutionTerminatedEventAttributes: Optional[       WorkflowExecutionTerminatedEventAttributesTypeDef     ] = None
    workflowExecutionCancelRequestedEventAttributes: Optional[       WorkflowExecutionCancelRequestedEventAttributesTypeDef     ] = None
    decisionTaskScheduledEventAttributes: Optional[       DecisionTaskScheduledEventAttributesTypeDef     ] = None
    decisionTaskStartedEventAttributes: Optional[       DecisionTaskStartedEventAttributesTypeDef     ] = None
    decisionTaskCompletedEventAttributes: Optional[       DecisionTaskCompletedEventAttributesTypeDef     ] = None
    decisionTaskTimedOutEventAttributes: Optional[       DecisionTaskTimedOutEventAttributesTypeDef     ] = None
    activityTaskScheduledEventAttributes: Optional[       ActivityTaskScheduledEventAttributesTypeDef     ] = None
    activityTaskStartedEventAttributes: Optional[       ActivityTaskStartedEventAttributesTypeDef     ] = None
    activityTaskCompletedEventAttributes: Optional[       ActivityTaskCompletedEventAttributesTypeDef     ] = None
    activityTaskFailedEventAttributes: Optional[ActivityTaskFailedEventAttributesTypeDef] = None
    activityTaskTimedOutEventAttributes: Optional[       ActivityTaskTimedOutEventAttributesTypeDef     ] = None
    activityTaskCanceledEventAttributes: Optional[       ActivityTaskCanceledEventAttributesTypeDef     ] = None
    activityTaskCancelRequestedEventAttributes: Optional[       ActivityTaskCancelRequestedEventAttributesTypeDef     ] = None
    workflowExecutionSignaledEventAttributes: Optional[       WorkflowExecutionSignaledEventAttributesTypeDef     ] = None
    markerRecordedEventAttributes: Optional[MarkerRecordedEventAttributesTypeDef] = None
    recordMarkerFailedEventAttributes: Optional[RecordMarkerFailedEventAttributesTypeDef] = None
    timerStartedEventAttributes: Optional[TimerStartedEventAttributesTypeDef] = None
    timerFiredEventAttributes: Optional[TimerFiredEventAttributesTypeDef] = None
    timerCanceledEventAttributes: Optional[TimerCanceledEventAttributesTypeDef] = None
    startChildWorkflowExecutionInitiatedEventAttributes: Optional[       StartChildWorkflowExecutionInitiatedEventAttributesTypeDef     ] = None
    childWorkflowExecutionStartedEventAttributes: Optional[       ChildWorkflowExecutionStartedEventAttributesTypeDef     ] = None
    childWorkflowExecutionCompletedEventAttributes: Optional[       ChildWorkflowExecutionCompletedEventAttributesTypeDef     ] = None
    childWorkflowExecutionFailedEventAttributes: Optional[       ChildWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    childWorkflowExecutionTimedOutEventAttributes: Optional[       ChildWorkflowExecutionTimedOutEventAttributesTypeDef     ] = None
    childWorkflowExecutionCanceledEventAttributes: Optional[       ChildWorkflowExecutionCanceledEventAttributesTypeDef     ] = None
    childWorkflowExecutionTerminatedEventAttributes: Optional[       ChildWorkflowExecutionTerminatedEventAttributesTypeDef     ] = None
    signalExternalWorkflowExecutionInitiatedEventAttributes: Optional[       SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef     ] = None
    externalWorkflowExecutionSignaledEventAttributes: Optional[       ExternalWorkflowExecutionSignaledEventAttributesTypeDef     ] = None
    signalExternalWorkflowExecutionFailedEventAttributes: Optional[       SignalExternalWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    externalWorkflowExecutionCancelRequestedEventAttributes: Optional[       ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef     ] = None
    requestCancelExternalWorkflowExecutionInitiatedEventAttributes: Optional[       RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef     ] = None
    requestCancelExternalWorkflowExecutionFailedEventAttributes: Optional[       RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    scheduleActivityTaskFailedEventAttributes: Optional[       ScheduleActivityTaskFailedEventAttributesTypeDef     ] = None
    requestCancelActivityTaskFailedEventAttributes: Optional[       RequestCancelActivityTaskFailedEventAttributesTypeDef     ] = None
    startTimerFailedEventAttributes: Optional[StartTimerFailedEventAttributesTypeDef] = None
    cancelTimerFailedEventAttributes: Optional[CancelTimerFailedEventAttributesTypeDef] = None
    startChildWorkflowExecutionFailedEventAttributes: Optional[       StartChildWorkflowExecutionFailedEventAttributesTypeDef     ] = None
    lambdaFunctionScheduledEventAttributes: Optional[       LambdaFunctionScheduledEventAttributesTypeDef     ] = None
    lambdaFunctionStartedEventAttributes: Optional[       LambdaFunctionStartedEventAttributesTypeDef     ] = None
    lambdaFunctionCompletedEventAttributes: Optional[       LambdaFunctionCompletedEventAttributesTypeDef     ] = None
    lambdaFunctionFailedEventAttributes: Optional[       LambdaFunctionFailedEventAttributesTypeDef     ] = None
    lambdaFunctionTimedOutEventAttributes: Optional[       LambdaFunctionTimedOutEventAttributesTypeDef     ] = None
    scheduleLambdaFunctionFailedEventAttributes: Optional[       ScheduleLambdaFunctionFailedEventAttributesTypeDef     ] = None
    startLambdaFunctionFailedEventAttributes: Optional[       StartLambdaFunctionFailedEventAttributesTypeDef     ] = None

class WorkflowTypeDetailTypeDef(BaseModel):
    typeInfo: WorkflowTypeInfoTypeDef
    configuration: WorkflowTypeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowTypeInfosTypeDef(BaseModel):
    typeInfos: List[WorkflowTypeInfoTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CountClosedWorkflowExecutionsInputRequestTypeDef(BaseModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    closeTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    closeStatusFilter: Optional[CloseStatusFilterTypeDef] = None

class CountOpenWorkflowExecutionsInputRequestTypeDef(BaseModel):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None

class ListClosedWorkflowExecutionsInputListClosedWorkflowExecutionsPaginateTypeDef(BaseModel):
    domain: str
    startTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    closeTimeFilter: Optional[ExecutionTimeFilterTypeDef] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None
    closeStatusFilter: Optional[CloseStatusFilterTypeDef] = None
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    reverseOrder: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClosedWorkflowExecutionsInputRequestTypeDef(BaseModel):
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

class ListOpenWorkflowExecutionsInputListOpenWorkflowExecutionsPaginateTypeDef(BaseModel):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    reverseOrder: Optional[bool] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListOpenWorkflowExecutionsInputRequestTypeDef(BaseModel):
    domain: str
    startTimeFilter: ExecutionTimeFilterTypeDef
    typeFilter: Optional[WorkflowTypeFilterTypeDef] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    nextPageToken: Optional[str] = None
    maximumPageSize: Optional[int] = None
    reverseOrder: Optional[bool] = None
    executionFilter: Optional[WorkflowExecutionFilterTypeDef] = None

class RespondDecisionTaskCompletedInputRequestTypeDef(BaseModel):
    taskToken: str
    decisions: Optional[Sequence[DecisionTypeDef]] = None
    executionContext: Optional[str] = None
    taskList: Optional[TaskListTypeDef] = None
    taskListScheduleToStartTimeout: Optional[str] = None

class DecisionTaskTypeDef(BaseModel):
    taskToken: str
    startedEventId: int
    workflowExecution: WorkflowExecutionTypeDef
    workflowType: WorkflowTypeTypeDef
    events: List[HistoryEventTypeDef]
    nextPageToken: str
    previousStartedEventId: int
    ResponseMetadata: ResponseMetadataTypeDef

class HistoryTypeDef(BaseModel):
    events: List[HistoryEventTypeDef]
    nextPageToken: str
    ResponseMetadata: ResponseMetadataTypeDef

