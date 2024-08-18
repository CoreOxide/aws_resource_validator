from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ActivityFailedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class ActivityListItemTypeDef(BaseValidatorModel):
    activityArn: str
    name: str
    creationDate: datetime

class ActivityScheduleFailedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class HistoryEventExecutionDataDetailsTypeDef(BaseValidatorModel):
    truncated: Optional[bool] = None

class ActivityStartedEventDetailsTypeDef(BaseValidatorModel):
    workerName: Optional[str] = None

class ActivityTimedOutEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class BillingDetailsTypeDef(BaseValidatorModel):
    billedMemoryUsedInMB: Optional[int] = None
    billedDurationInMilliseconds: Optional[int] = None

class CloudWatchEventsExecutionDataDetailsTypeDef(BaseValidatorModel):
    included: Optional[bool] = None

class CloudWatchLogsLogGroupTypeDef(BaseValidatorModel):
    logGroupArn: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class RoutingConfigurationListItemTypeDef(BaseValidatorModel):
    stateMachineVersionArn: str
    weight: int

class TracingConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None

class DeleteActivityInputRequestTypeDef(BaseValidatorModel):
    activityArn: str

class DeleteStateMachineAliasInputRequestTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str

class DeleteStateMachineInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str

class DeleteStateMachineVersionInputRequestTypeDef(BaseValidatorModel):
    stateMachineVersionArn: str

class DescribeActivityInputRequestTypeDef(BaseValidatorModel):
    activityArn: str

class DescribeExecutionInputRequestTypeDef(BaseValidatorModel):
    executionArn: str

class DescribeMapRunInputRequestTypeDef(BaseValidatorModel):
    mapRunArn: str

class MapRunExecutionCountsTypeDef(BaseValidatorModel):
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

class MapRunItemCountsTypeDef(BaseValidatorModel):
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

class DescribeStateMachineAliasInputRequestTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str

class DescribeStateMachineForExecutionInputRequestTypeDef(BaseValidatorModel):
    executionArn: str

class DescribeStateMachineInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str

class ExecutionAbortedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class ExecutionFailedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class ExecutionListItemTypeDef(BaseValidatorModel):
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

class ExecutionRedrivenEventDetailsTypeDef(BaseValidatorModel):
    redriveCount: Optional[int] = None

class ExecutionTimedOutEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class GetActivityTaskInputRequestTypeDef(BaseValidatorModel):
    activityArn: str
    workerName: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetExecutionHistoryInputRequestTypeDef(BaseValidatorModel):
    executionArn: str
    maxResults: Optional[int] = None
    reverseOrder: Optional[bool] = None
    nextToken: Optional[str] = None
    includeExecutionData: Optional[bool] = None

class LambdaFunctionFailedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class LambdaFunctionScheduleFailedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class LambdaFunctionStartFailedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class LambdaFunctionTimedOutEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class MapIterationEventDetailsTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    index: Optional[int] = None

class MapRunFailedEventDetailsTypeDef(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None

class MapRunRedrivenEventDetailsTypeDef(BaseValidatorModel):
    mapRunArn: Optional[str] = None
    redriveCount: Optional[int] = None

class MapRunStartedEventDetailsTypeDef(BaseValidatorModel):
    mapRunArn: Optional[str] = None

class MapStateStartedEventDetailsTypeDef(BaseValidatorModel):
    length: Optional[int] = None

class TaskFailedEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TaskStartFailedEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TaskStartedEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str

class TaskSubmitFailedEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TaskTimedOutEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None

class InspectionDataRequestTypeDef(BaseValidatorModel):
    protocol: Optional[str] = None
    method: Optional[str] = None
    url: Optional[str] = None
    headers: Optional[str] = None
    body: Optional[str] = None

class InspectionDataResponseTypeDef(BaseValidatorModel):
    protocol: Optional[str] = None
    statusCode: Optional[str] = None
    statusMessage: Optional[str] = None
    headers: Optional[str] = None
    body: Optional[str] = None

class TaskCredentialsTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None

class ListActivitiesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExecutionsInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None

class ListMapRunsInputRequestTypeDef(BaseValidatorModel):
    executionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class MapRunListItemTypeDef(BaseValidatorModel):
    executionArn: str
    mapRunArn: str
    stateMachineArn: str
    startDate: datetime
    stopDate: Optional[datetime] = None

class ListStateMachineAliasesInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StateMachineAliasListItemTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str
    creationDate: datetime

class ListStateMachineVersionsInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class StateMachineVersionListItemTypeDef(BaseValidatorModel):
    stateMachineVersionArn: str
    creationDate: datetime

class ListStateMachinesInputRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StateMachineListItemTypeDef(BaseValidatorModel):
    stateMachineArn: str
    name: str
    type: StateMachineTypeType
    creationDate: datetime

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class PublishStateMachineVersionInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str
    revisionId: Optional[str] = None
    description: Optional[str] = None

class RedriveExecutionInputRequestTypeDef(BaseValidatorModel):
    executionArn: str
    clientToken: Optional[str] = None

class SendTaskFailureInputRequestTypeDef(BaseValidatorModel):
    taskToken: str
    error: Optional[str] = None
    cause: Optional[str] = None

class SendTaskHeartbeatInputRequestTypeDef(BaseValidatorModel):
    taskToken: str

class SendTaskSuccessInputRequestTypeDef(BaseValidatorModel):
    taskToken: str
    output: str

class StartExecutionInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str
    name: Optional[str] = None
    input: Optional[str] = None
    traceHeader: Optional[str] = None

class StartSyncExecutionInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str
    name: Optional[str] = None
    input: Optional[str] = None
    traceHeader: Optional[str] = None

class StopExecutionInputRequestTypeDef(BaseValidatorModel):
    executionArn: str
    error: Optional[str] = None
    cause: Optional[str] = None

class TestStateInputRequestTypeDef(BaseValidatorModel):
    definition: str
    roleArn: str
    input: Optional[str] = None
    inspectionLevel: Optional[InspectionLevelType] = None
    revealSecrets: Optional[bool] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateMapRunInputRequestTypeDef(BaseValidatorModel):
    mapRunArn: str
    maxConcurrency: Optional[int] = None
    toleratedFailurePercentage: Optional[float] = None
    toleratedFailureCount: Optional[int] = None

class ValidateStateMachineDefinitionDiagnosticTypeDef(BaseValidatorModel):
    severity: Literal["ERROR"]
    code: str
    message: str
    location: Optional[str] = None

class ValidateStateMachineDefinitionInputRequestTypeDef(BaseValidatorModel):
    definition: str
    type: Optional[StateMachineTypeType] = None

class ActivityScheduledEventDetailsTypeDef(BaseValidatorModel):
    resource: str
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None
    timeoutInSeconds: Optional[int] = None
    heartbeatInSeconds: Optional[int] = None

class ActivitySucceededEventDetailsTypeDef(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class ExecutionStartedEventDetailsTypeDef(BaseValidatorModel):
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None
    roleArn: Optional[str] = None
    stateMachineAliasArn: Optional[str] = None
    stateMachineVersionArn: Optional[str] = None

class ExecutionSucceededEventDetailsTypeDef(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class LambdaFunctionSucceededEventDetailsTypeDef(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class StateEnteredEventDetailsTypeDef(BaseValidatorModel):
    name: str
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class StateExitedEventDetailsTypeDef(BaseValidatorModel):
    name: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class TaskSubmittedEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class TaskSucceededEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None

class LogDestinationTypeDef(BaseValidatorModel):
    cloudWatchLogsLogGroup: Optional[CloudWatchLogsLogGroupTypeDef] = None

class CreateActivityInputRequestTypeDef(BaseValidatorModel):
    name: str
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateActivityOutputTypeDef(BaseValidatorModel):
    activityArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineAliasOutputTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineOutputTypeDef(BaseValidatorModel):
    stateMachineArn: str
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeActivityOutputTypeDef(BaseValidatorModel):
    activityArn: str
    name: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExecutionOutputTypeDef(BaseValidatorModel):
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

class GetActivityTaskOutputTypeDef(BaseValidatorModel):
    taskToken: str
    input: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListActivitiesOutputTypeDef(BaseValidatorModel):
    activities: List[ActivityListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishStateMachineVersionOutputTypeDef(BaseValidatorModel):
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class RedriveExecutionOutputTypeDef(BaseValidatorModel):
    redriveDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartExecutionOutputTypeDef(BaseValidatorModel):
    executionArn: str
    startDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StartSyncExecutionOutputTypeDef(BaseValidatorModel):
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

class StopExecutionOutputTypeDef(BaseValidatorModel):
    stopDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineAliasOutputTypeDef(BaseValidatorModel):
    updateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineOutputTypeDef(BaseValidatorModel):
    updateDate: datetime
    revisionId: str
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStateMachineAliasInputRequestTypeDef(BaseValidatorModel):
    name: str
    routingConfiguration: Sequence[RoutingConfigurationListItemTypeDef]
    description: Optional[str] = None

class DescribeStateMachineAliasOutputTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str
    name: str
    description: str
    routingConfiguration: List[RoutingConfigurationListItemTypeDef]
    creationDate: datetime
    updateDate: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateStateMachineAliasInputRequestTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str
    description: Optional[str] = None
    routingConfiguration: Optional[Sequence[RoutingConfigurationListItemTypeDef]] = None

class DescribeMapRunOutputTypeDef(BaseValidatorModel):
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

class ListExecutionsOutputTypeDef(BaseValidatorModel):
    executions: List[ExecutionListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef(BaseValidatorModel):
    executionArn: str
    reverseOrder: Optional[bool] = None
    includeExecutionData: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListActivitiesInputListActivitiesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExecutionsInputListExecutionsPaginateTypeDef(BaseValidatorModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMapRunsInputListMapRunsPaginateTypeDef(BaseValidatorModel):
    executionArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStateMachinesInputListStateMachinesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class InspectionDataTypeDef(BaseValidatorModel):
    input: Optional[str] = None
    afterInputPath: Optional[str] = None
    afterParameters: Optional[str] = None
    result: Optional[str] = None
    afterResultSelector: Optional[str] = None
    afterResultPath: Optional[str] = None
    request: Optional[InspectionDataRequestTypeDef] = None
    response: Optional[InspectionDataResponseTypeDef] = None

class LambdaFunctionScheduledEventDetailsTypeDef(BaseValidatorModel):
    resource: str
    input: Optional[str] = None
    inputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None
    timeoutInSeconds: Optional[int] = None
    taskCredentials: Optional[TaskCredentialsTypeDef] = None

class TaskScheduledEventDetailsTypeDef(BaseValidatorModel):
    resourceType: str
    resource: str
    region: str
    parameters: str
    timeoutInSeconds: Optional[int] = None
    heartbeatInSeconds: Optional[int] = None
    taskCredentials: Optional[TaskCredentialsTypeDef] = None

class ListMapRunsOutputTypeDef(BaseValidatorModel):
    mapRuns: List[MapRunListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStateMachineAliasesOutputTypeDef(BaseValidatorModel):
    stateMachineAliases: List[StateMachineAliasListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStateMachineVersionsOutputTypeDef(BaseValidatorModel):
    stateMachineVersions: List[StateMachineVersionListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListStateMachinesOutputTypeDef(BaseValidatorModel):
    stateMachines: List[StateMachineListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateStateMachineDefinitionOutputTypeDef(BaseValidatorModel):
    result: ValidateStateMachineDefinitionResultCodeType
    diagnostics: List[ValidateStateMachineDefinitionDiagnosticTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingConfigurationOutputTypeDef(BaseValidatorModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[List[LogDestinationTypeDef]] = None

class LoggingConfigurationTypeDef(BaseValidatorModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[Sequence[LogDestinationTypeDef]] = None

class TestStateOutputTypeDef(BaseValidatorModel):
    output: str
    error: str
    cause: str
    inspectionData: InspectionDataTypeDef
    nextState: str
    status: TestExecutionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class HistoryEventTypeDef(BaseValidatorModel):
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

class DescribeStateMachineForExecutionOutputTypeDef(BaseValidatorModel):
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

class DescribeStateMachineOutputTypeDef(BaseValidatorModel):
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

class CreateStateMachineInputRequestTypeDef(BaseValidatorModel):
    name: str
    definition: str
    roleArn: str
    type: Optional[StateMachineTypeType] = None
    loggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    tracingConfiguration: Optional[TracingConfigurationTypeDef] = None
    publish: Optional[bool] = None
    versionDescription: Optional[str] = None

class UpdateStateMachineInputRequestTypeDef(BaseValidatorModel):
    stateMachineArn: str
    definition: Optional[str] = None
    roleArn: Optional[str] = None
    loggingConfiguration: Optional[LoggingConfigurationTypeDef] = None
    tracingConfiguration: Optional[TracingConfigurationTypeDef] = None
    publish: Optional[bool] = None
    versionDescription: Optional[str] = None

class GetExecutionHistoryOutputTypeDef(BaseValidatorModel):
    events: List[HistoryEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

