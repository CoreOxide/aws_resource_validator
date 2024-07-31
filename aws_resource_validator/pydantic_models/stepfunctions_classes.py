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
from aws_resource_validator.pydantic_models.stepfunctions_constants import *

class ActivityFailedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class ActivityListItemTypeDef(BaseModel):
    activityArn: str
    name: str
    creationDate: datetime

class ActivityScheduleFailedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class HistoryEventExecutionDataDetailsTypeDef(BaseModel):
    truncated: Optional[bool] = None

class ActivityStartedEventDetailsTypeDef(BaseModel):
    workerName: Optional[str] = None

class ActivityTimedOutEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class BillingDetailsTypeDef(BaseModel):
    billedMemoryUsedInMB: Optional[int] = None
    billedDurationInMilliseconds: Optional[int] = None

class CloudWatchEventsExecutionDataDetailsTypeDef(BaseModel):
    included: Optional[bool] = None

class CloudWatchLogsLogGroupTypeDef(BaseModel):
    logGroupArn: Optional[str] = None

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class RoutingConfigurationListItemTypeDef(BaseModel):
    stateMachineVersionArn: str
    weight: int

class TracingConfigurationTypeDef(BaseModel):
    enabled: Optional[bool] = None

class DeleteActivityInputRequestTypeDef(BaseModel):
    activityArn: str

class DeleteStateMachineAliasInputRequestTypeDef(BaseModel):
    stateMachineAliasArn: str

class DeleteStateMachineInputRequestTypeDef(BaseModel):
    stateMachineArn: str

class DeleteStateMachineVersionInputRequestTypeDef(BaseModel):
    stateMachineVersionArn: str

class DescribeActivityInputRequestTypeDef(BaseModel):
    activityArn: str

class DescribeExecutionInputRequestTypeDef(BaseModel):
    executionArn: str

class DescribeMapRunInputRequestTypeDef(BaseModel):
    mapRunArn: str

class MapRunExecutionCountsTypeDef(BaseModel):
    pending: int
    running: int
    succeeded: int
    failed: int
    timedOut: int
    aborted: int
    total: int
    resultsWritten: int
    failuresNotRedrivable: Optional[int] = None
    pendingRedrive: Optional[int] = None

class MapRunItemCountsTypeDef(BaseModel):
    pending: int
    running: int
    succeeded: int
    failed: int
    timedOut: int
    aborted: int
    total: int
    resultsWritten: int
    failuresNotRedrivable: Optional[int] = None
    pendingRedrive: Optional[int] = None

class DescribeStateMachineAliasInputRequestTypeDef(BaseModel):
    stateMachineAliasArn: str

class DescribeStateMachineForExecutionInputRequestTypeDef(BaseModel):
    executionArn: str

class DescribeStateMachineInputRequestTypeDef(BaseModel):
    stateMachineArn: str

class ExecutionAbortedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class ExecutionFailedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class ExecutionListItemTypeDef(BaseModel):
    executionArn: str
    stateMachineArn: str
    name: str
    status: ExecutionStatusType
    startDate: datetime
    stopDate: Optional[datetime] = None
    mapRunArn: Optional[str] = None
    itemCount: Optional[int] = None
    stateMachineVersionArn: Optional[str] = None
    stateMachineAliasArn: Optional[str] = None
    redriveCount: Optional[int] = None
    redriveDate: Optional[datetime] = None

class ExecutionRedrivenEventDetailsTypeDef(BaseModel):
    redriveCount: Optional[int] = None

class ExecutionTimedOutEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class GetActivityTaskInputRequestTypeDef(BaseModel):
    activityArn: str
    workerName: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetExecutionHistoryInputRequestTypeDef(BaseModel):
    executionArn: str
    maxResults: Optional[int] = None
    reverseOrder: Optional[bool] = None
    nextToken: Optional[str] = None
    includeExecutionData: Optional[bool] = None

class LambdaFunctionFailedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class LambdaFunctionScheduleFailedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class LambdaFunctionStartFailedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class LambdaFunctionTimedOutEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class MapIterationEventDetailsTypeDef(BaseModel):
    name: Optional[str] = None
    index: Optional[int] = None

class MapRunFailedEventDetailsTypeDef(BaseModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class MapRunRedrivenEventDetailsTypeDef(BaseModel):
    mapRunArn: Optional[str] = None
    redriveCount: Optional[int] = None

class MapRunStartedEventDetailsTypeDef(BaseModel):
    mapRunArn: Optional[str] = None

class MapStateStartedEventDetailsTypeDef(BaseModel):
    length: Optional[int] = None

class TaskFailedEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TaskStartFailedEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TaskStartedEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str

class TaskSubmitFailedEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TaskTimedOutEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class InspectionDataRequestTypeDef(BaseModel):
    protocol: Optional[str] = None
    method: Optional[str] = None
    url: Optional[str] = None
    headers: Optional[str] = None
    body: Optional[str] = None

class InspectionDataResponseTypeDef(BaseModel):
    protocol: Optional[str] = None
    statusCode: Optional[str] = None
    statusMessage: Optional[str] = None
    headers: Optional[str] = None
    body: Optional[str] = None

class TaskCredentialsTypeDef(BaseModel):
    roleArn: Optional[str] = None

class ListActivitiesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExecutionsInputRequestTypeDef(BaseModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None

class ListMapRunsInputRequestTypeDef(BaseModel):
    executionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MapRunListItemTypeDef(BaseModel):
    executionArn: str
    mapRunArn: str
    stateMachineArn: str
    startDate: datetime
    stopDate: Optional[datetime] = None

class ListStateMachineAliasesInputRequestTypeDef(BaseModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StateMachineAliasListItemTypeDef(BaseModel):
    stateMachineAliasArn: str
    creationDate: datetime

class ListStateMachineVersionsInputRequestTypeDef(BaseModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StateMachineVersionListItemTypeDef(BaseModel):
    stateMachineVersionArn: str
    creationDate: datetime

class ListStateMachinesInputRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StateMachineListItemTypeDef(BaseModel):
    stateMachineArn: str
    name: str
    type: StateMachineTypeType
    creationDate: datetime

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class PublishStateMachineVersionInputRequestTypeDef(BaseModel):
    stateMachineArn: str
    revisionId: Optional[str] = None
    description: Optional[str] = None

class RedriveExecutionInputRequestTypeDef(BaseModel):
    executionArn: str
    clientToken: Optional[str] = None

class SendTaskFailureInputRequestTypeDef(BaseModel):
    taskToken: str
    error: Optional[str] = None
    cause: Optional[str] = None

class SendTaskHeartbeatInputRequestTypeDef(BaseModel):
    taskToken: str

class SendTaskSuccessInputRequestTypeDef(BaseModel):
    taskToken: str
    output: str

class StartExecutionInputRequestTypeDef(BaseModel):
    stateMachineArn: str
    name: Optional[str] = None
    input: Optional[str] = None
    traceHeader: Optional[str] = None

class StartSyncExecutionInputRequestTypeDef(BaseModel):
    stateMachineArn: str
    name: Optional[str] = None
    input: Optional[str] = None
    traceHeader: Optional[str] = None

class StopExecutionInputRequestTypeDef(BaseModel):
    executionArn: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TestStateInputRequestTypeDef(BaseModel):
    definition: str
    roleArn: str
    input: Optional[str] = None
    inspectionLevel: Optional[InspectionLevelType] = None
    revealSecrets: Optional[bool] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateMapRunInputRequestTypeDef(BaseModel):
    mapRunArn: str
    maxConcurrency: Optional[int] = None
    toleratedFailurePercentage: Optional[float] = None
    toleratedFailureCount: Optional[int] = None

class ValidateStateMachineDefinitionDiagnosticTypeDef(BaseModel):
    severity: Literal["ERROR"]
    code: str
    message: str
    location: Optional[str] = None

class ValidateStateMachineDefinitionInputRequestTypeDef(BaseModel):
    definition: str
    type: Optional[StateMachineTypeType] = None

class ActivityScheduledEventDetailsTypeDef(BaseModel):
    resource: str
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None
    timeoutInSeconds: Optional[int] = None
    heartbeatInSeconds: Optional[int] = None

class ActivitySucceededEventDetailsTypeDef(BaseModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class ExecutionStartedEventDetailsTypeDef(BaseModel):
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None
    roleArn: Optional[str] = None
    stateMachineAliasArn: Optional[str] = None
    stateMachineVersionArn: Optional[str] = None

class ExecutionSucceededEventDetailsTypeDef(BaseModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class LambdaFunctionSucceededEventDetailsTypeDef(BaseModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class StateEnteredEventDetailsTypeDef(BaseModel):
    name: str
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class StateExitedEventDetailsTypeDef(BaseModel):
    name: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class TaskSubmittedEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class TaskSucceededEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class LogDestinationTypeDef(BaseModel):
    cloudWatchLogsLogGroup: Optional[CloudWatchLogsLogGroupTypeDef] = None

class CreateActivityInputRequestTypeDef(BaseModel):
    name: str
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateActivityOutputTypeDef(BaseModel):
    activityArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineAliasOutputTypeDef(BaseModel):
    stateMachineAliasArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineOutputTypeDef(BaseModel):
    stateMachineArn: str
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActivityOutputTypeDef(BaseModel):
    activityArn: str
    name: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExecutionOutputTypeDef(BaseModel):
    executionArn: str
    stateMachineArn: str
    name: str
    status: ExecutionStatusType
    startDate: datetime
    stopDate: datetime
    input: str
    inputDetails: CloudWatchEventsExecutionDataDetailsTypeDef
    output: str
    outputDetails: CloudWatchEventsExecutionDataDetailsTypeDef
    traceHeader: str
    mapRunArn: str
    error: str
    cause: str
    stateMachineVersionArn: str
    stateMachineAliasArn: str
    redriveCount: int
    redriveDate: datetime
    redriveStatus: ExecutionRedriveStatusType
    redriveStatusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetActivityTaskOutputTypeDef(BaseModel):
    taskToken: str
    input: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListActivitiesOutputTypeDef(BaseModel):
    activities: List[ActivityListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishStateMachineVersionOutputTypeDef(BaseModel):
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RedriveExecutionOutputTypeDef(BaseModel):
    redriveDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartExecutionOutputTypeDef(BaseModel):
    executionArn: str
    startDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartSyncExecutionOutputTypeDef(BaseModel):
    executionArn: str
    stateMachineArn: str
    name: str
    startDate: datetime
    stopDate: datetime
    status: SyncExecutionStatusType
    error: str
    cause: str
    input: str
    inputDetails: CloudWatchEventsExecutionDataDetailsTypeDef
    output: str
    outputDetails: CloudWatchEventsExecutionDataDetailsTypeDef
    traceHeader: str
    billingDetails: BillingDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopExecutionOutputTypeDef(BaseModel):
    stopDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineAliasOutputTypeDef(BaseModel):
    updateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineOutputTypeDef(BaseModel):
    updateDate: datetime
    revisionId: str
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineAliasInputRequestTypeDef(BaseModel):
    name: str
    routingConfiguration: Sequence[RoutingConfigurationListItemTypeDef]
    description: Optional[str] = None

class DescribeStateMachineAliasOutputTypeDef(BaseModel):
    stateMachineAliasArn: str
    name: str
    description: str
    routingConfiguration: List[RoutingConfigurationListItemTypeDef]
    creationDate: datetime
    updateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineAliasInputRequestTypeDef(BaseModel):
    stateMachineAliasArn: str
    description: Optional[str] = None
    routingConfiguration: Optional[Sequence[RoutingConfigurationListItemTypeDef]] = None

class DescribeMapRunOutputTypeDef(BaseModel):
    mapRunArn: str
    executionArn: str
    status: MapRunStatusType
    startDate: datetime
    stopDate: datetime
    maxConcurrency: int
    toleratedFailurePercentage: float
    toleratedFailureCount: int
    itemCounts: MapRunItemCountsTypeDef
    executionCounts: MapRunExecutionCountsTypeDef
    redriveCount: int
    redriveDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListExecutionsOutputTypeDef(BaseModel):
    executions: List[ExecutionListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef(BaseModel):
    executionArn: str
    reverseOrder: Optional[bool] = None
    includeExecutionData: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListActivitiesInputListActivitiesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExecutionsInputListExecutionsPaginateTypeDef(BaseModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMapRunsInputListMapRunsPaginateTypeDef(BaseModel):
    executionArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStateMachinesInputListStateMachinesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class InspectionDataTypeDef(BaseModel):
    input: Optional[str] = None
    afterInputPath: Optional[str] = None
    afterParameters: Optional[str] = None
    result: Optional[str] = None
    afterResultSelector: Optional[str] = None
    afterResultPath: Optional[str] = None
    request: Optional[InspectionDataRequestTypeDef] = None
    response: Optional[InspectionDataResponseTypeDef] = None

class LambdaFunctionScheduledEventDetailsTypeDef(BaseModel):
    resource: str
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None
    timeoutInSeconds: Optional[int] = None
    taskCredentials: Optional[TaskCredentialsTypeDef] = None

class TaskScheduledEventDetailsTypeDef(BaseModel):
    resourceType: str
    resource: str
    region: str
    parameters: str
    timeoutInSeconds: Optional[int] = None
    heartbeatInSeconds: Optional[int] = None
    taskCredentials: Optional[TaskCredentialsTypeDef] = None

class ListMapRunsOutputTypeDef(BaseModel):
    mapRuns: List[MapRunListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStateMachineAliasesOutputTypeDef(BaseModel):
    stateMachineAliases: List[StateMachineAliasListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStateMachineVersionsOutputTypeDef(BaseModel):
    stateMachineVersions: List[StateMachineVersionListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStateMachinesOutputTypeDef(BaseModel):
    stateMachines: List[StateMachineListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateStateMachineDefinitionOutputTypeDef(BaseModel):
    result: ValidateStateMachineDefinitionResultCodeType
    diagnostics: List[ValidateStateMachineDefinitionDiagnosticTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationOutputTypeDef(BaseModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[List[LogDestinationTypeDef]] = None

class LoggingConfigurationTypeDef(BaseModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[Sequence[LogDestinationTypeDef]] = None

class TestStateOutputTypeDef(BaseModel):
    output: str
    error: str
    cause: str
    inspectionData: InspectionDataTypeDef
    nextState: str
    status: TestExecutionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class HistoryEventTypeDef(BaseModel):
    timestamp: datetime
    type: HistoryEventTypeType
    id: int
    previousEventId: Optional[int] = None
    activityFailedEventDetails: Optional[ActivityFailedEventDetailsTypeDef] = None
    activityScheduleFailedEventDetails: Optional[       ActivityScheduleFailedEventDetailsTypeDef     ] = None
    activityScheduledEventDetails: Optional[ActivityScheduledEventDetailsTypeDef] = None
    activityStartedEventDetails: Optional[ActivityStartedEventDetailsTypeDef] = None
    activitySucceededEventDetails: Optional[ActivitySucceededEventDetailsTypeDef] = None
    activityTimedOutEventDetails: Optional[ActivityTimedOutEventDetailsTypeDef] = None
    taskFailedEventDetails: Optional[TaskFailedEventDetailsTypeDef] = None
    taskScheduledEventDetails: Optional[TaskScheduledEventDetailsTypeDef] = None
    taskStartFailedEventDetails: Optional[TaskStartFailedEventDetailsTypeDef] = None
    taskStartedEventDetails: Optional[TaskStartedEventDetailsTypeDef] = None
    taskSubmitFailedEventDetails: Optional[TaskSubmitFailedEventDetailsTypeDef] = None
    taskSubmittedEventDetails: Optional[TaskSubmittedEventDetailsTypeDef] = None
    taskSucceededEventDetails: Optional[TaskSucceededEventDetailsTypeDef] = None
    taskTimedOutEventDetails: Optional[TaskTimedOutEventDetailsTypeDef] = None
    executionFailedEventDetails: Optional[ExecutionFailedEventDetailsTypeDef] = None
    executionStartedEventDetails: Optional[ExecutionStartedEventDetailsTypeDef] = None
    executionSucceededEventDetails: Optional[ExecutionSucceededEventDetailsTypeDef] = None
    executionAbortedEventDetails: Optional[ExecutionAbortedEventDetailsTypeDef] = None
    executionTimedOutEventDetails: Optional[ExecutionTimedOutEventDetailsTypeDef] = None
    executionRedrivenEventDetails: Optional[ExecutionRedrivenEventDetailsTypeDef] = None
    mapStateStartedEventDetails: Optional[MapStateStartedEventDetailsTypeDef] = None
    mapIterationStartedEventDetails: Optional[MapIterationEventDetailsTypeDef] = None
    mapIterationSucceededEventDetails: Optional[MapIterationEventDetailsTypeDef] = None
    mapIterationFailedEventDetails: Optional[MapIterationEventDetailsTypeDef] = None
    mapIterationAbortedEventDetails: Optional[MapIterationEventDetailsTypeDef] = None
    lambdaFunctionFailedEventDetails: Optional[LambdaFunctionFailedEventDetailsTypeDef] = None
    lambdaFunctionScheduleFailedEventDetails: Optional[       LambdaFunctionScheduleFailedEventDetailsTypeDef     ] = None
    lambdaFunctionScheduledEventDetails: Optional[       LambdaFunctionScheduledEventDetailsTypeDef     ] = None
    lambdaFunctionStartFailedEventDetails: Optional[       LambdaFunctionStartFailedEventDetailsTypeDef     ] = None
    lambdaFunctionSucceededEventDetails: Optional[       LambdaFunctionSucceededEventDetailsTypeDef     ] = None
    lambdaFunctionTimedOutEventDetails: Optional[       LambdaFunctionTimedOutEventDetailsTypeDef     ] = None
    stateEnteredEventDetails: Optional[StateEnteredEventDetailsTypeDef] = None
    stateExitedEventDetails: Optional[StateExitedEventDetailsTypeDef] = None
    mapRunStartedEventDetails: Optional[MapRunStartedEventDetailsTypeDef] = None
    mapRunFailedEventDetails: Optional[MapRunFailedEventDetailsTypeDef] = None
    mapRunRedrivenEventDetails: Optional[MapRunRedrivenEventDetailsTypeDef] = None

class DescribeStateMachineForExecutionOutputTypeDef(BaseModel):
    stateMachineArn: str
    name: str
    definition: str
    roleArn: str
    updateDate: datetime
    loggingConfiguration: LoggingConfigurationOutputTypeDef
    tracingConfiguration: TracingConfigurationTypeDef
    mapRunArn: str
    label: str
    revisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStateMachineOutputTypeDef(BaseModel):
    stateMachineArn: str
    name: str
    status: StateMachineStatusType
    definition: str
    roleArn: str
    type: StateMachineTypeType
    creationDate: datetime
    loggingConfiguration: LoggingConfigurationOutputTypeDef
    tracingConfiguration: TracingConfigurationTypeDef
    label: str
    revisionId: str
    description: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineInputRequestTypeDef(BaseModel):
    name: str
    definition: str
    roleArn: str
    type: Optional[StateMachineTypeType] = None
    loggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    tracingConfiguration: Optional[TracingConfigurationTypeDef] = None
    publish: Optional[bool] = None
    versionDescription: Optional[str] = None

class UpdateStateMachineInputRequestTypeDef(BaseModel):
    stateMachineArn: str
    definition: Optional[str] = None
    roleArn: Optional[str] = None
    loggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    tracingConfiguration: Optional[TracingConfigurationTypeDef] = None
    publish: Optional[bool] = None
    versionDescription: Optional[str] = None

class GetExecutionHistoryOutputTypeDef(BaseModel):
    events: List[HistoryEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

