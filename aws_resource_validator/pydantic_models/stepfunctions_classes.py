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
from aws_resource_validator.pydantic_models.stepfunctions_constants import *

class ActivityFailedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class ActivityListItem(BaseValidatorModel):
    activityArn: str
    name: str
    creationDate: datetime


class ActivityScheduleFailedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class HistoryEventExecutionDataDetails(BaseValidatorModel):
    truncated: Optional[bool] = None


class ActivityStartedEventDetails(BaseValidatorModel):
    workerName: Optional[str] = None


class ActivityTimedOutEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class AssignedVariablesDetails(BaseValidatorModel):
    truncated: Optional[bool] = None


class BillingDetails(BaseValidatorModel):
    billedMemoryUsedInMB: Optional[int] = None
    billedDurationInMilliseconds: Optional[int] = None


class CloudWatchEventsExecutionDataDetails(BaseValidatorModel):
    included: Optional[bool] = None


class CloudWatchLogsLogGroup(BaseValidatorModel):
    logGroupArn: Optional[str] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class RoutingConfigurationListItem(BaseValidatorModel):
    stateMachineVersionArn: str
    weight: int


class TracingConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None


class DeleteActivityInput(BaseValidatorModel):
    activityArn: str


class DeleteStateMachineAliasInput(BaseValidatorModel):
    stateMachineAliasArn: str


class DeleteStateMachineInput(BaseValidatorModel):
    stateMachineArn: str


class DeleteStateMachineVersionInput(BaseValidatorModel):
    stateMachineVersionArn: str


class DescribeActivityInput(BaseValidatorModel):
    activityArn: str


class DescribeExecutionInput(BaseValidatorModel):
    executionArn: str
    includedData: Optional[IncludedDataType] = None


class DescribeMapRunInput(BaseValidatorModel):
    mapRunArn: str


class MapRunExecutionCounts(BaseValidatorModel):
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


class MapRunItemCounts(BaseValidatorModel):
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


class DescribeStateMachineAliasInput(BaseValidatorModel):
    stateMachineAliasArn: str


class DescribeStateMachineForExecutionInput(BaseValidatorModel):
    executionArn: str
    includedData: Optional[IncludedDataType] = None


class DescribeStateMachineInput(BaseValidatorModel):
    stateMachineArn: str
    includedData: Optional[IncludedDataType] = None


class EvaluationFailedEventDetails(BaseValidatorModel):
    state: str
    error: Optional[str] = None
    cause: Optional[str] = None
    location: Optional[str] = None


class ExecutionAbortedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class ExecutionFailedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class ExecutionListItem(BaseValidatorModel):
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


class ExecutionRedrivenEventDetails(BaseValidatorModel):
    redriveCount: Optional[int] = None


class ExecutionTimedOutEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class GetActivityTaskInput(BaseValidatorModel):
    activityArn: str
    workerName: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetExecutionHistoryInput(BaseValidatorModel):
    executionArn: str
    maxResults: Optional[int] = None
    reverseOrder: Optional[bool] = None
    nextToken: Optional[str] = None
    includeExecutionData: Optional[bool] = None


class LambdaFunctionFailedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class LambdaFunctionScheduleFailedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class LambdaFunctionStartFailedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class LambdaFunctionTimedOutEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class MapIterationEventDetails(BaseValidatorModel):
    name: Optional[str] = None
    index: Optional[int] = None


class MapRunFailedEventDetails(BaseValidatorModel):
    error: Optional[str] = None
    cause: Optional[str] = None


class MapRunRedrivenEventDetails(BaseValidatorModel):
    mapRunArn: Optional[str] = None
    redriveCount: Optional[int] = None


class MapRunStartedEventDetails(BaseValidatorModel):
    mapRunArn: Optional[str] = None


class MapStateStartedEventDetails(BaseValidatorModel):
    length: Optional[int] = None


class TaskFailedEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None


class TaskStartFailedEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None


class TaskStartedEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str


class TaskSubmitFailedEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None


class TaskTimedOutEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str
    error: Optional[str] = None
    cause: Optional[str] = None


class InspectionDataRequest(BaseValidatorModel):
    protocol: Optional[str] = None
    method: Optional[str] = None
    url: Optional[str] = None
    headers: Optional[str] = None
    body: Optional[str] = None


class InspectionDataResponse(BaseValidatorModel):
    protocol: Optional[str] = None
    statusCode: Optional[str] = None
    statusMessage: Optional[str] = None
    headers: Optional[str] = None
    body: Optional[str] = None


class TaskCredentials(BaseValidatorModel):
    roleArn: Optional[str] = None


class ListActivitiesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExecutionsInput(BaseValidatorModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None


class ListMapRunsInput(BaseValidatorModel):
    executionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MapRunListItem(BaseValidatorModel):
    executionArn: str
    mapRunArn: str
    stateMachineArn: str
    startDate: datetime
    stopDate: Optional[datetime] = None


class ListStateMachineAliasesInput(BaseValidatorModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StateMachineAliasListItem(BaseValidatorModel):
    stateMachineAliasArn: str
    creationDate: datetime


class ListStateMachineVersionsInput(BaseValidatorModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StateMachineVersionListItem(BaseValidatorModel):
    stateMachineVersionArn: str
    creationDate: datetime


class ListStateMachinesInput(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


class PublishStateMachineVersionInput(BaseValidatorModel):
    stateMachineArn: str
    revisionId: Optional[str] = None
    description: Optional[str] = None


class RedriveExecutionInput(BaseValidatorModel):
    executionArn: str
    clientToken: Optional[str] = None


class SendTaskFailureInput(BaseValidatorModel):
    taskToken: str
    error: Optional[str] = None
    cause: Optional[str] = None


class SendTaskHeartbeatInput(BaseValidatorModel):
    taskToken: str


class SendTaskSuccessInput(BaseValidatorModel):
    taskToken: str
    output: str


class StopExecutionInput(BaseValidatorModel):
    executionArn: str
    error: Optional[str] = None
    cause: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateMapRunInput(BaseValidatorModel):
    mapRunArn: str
    maxConcurrency: Optional[int] = None
    toleratedFailurePercentage: Optional[float] = None
    toleratedFailureCount: Optional[int] = None


class ValidateStateMachineDefinitionDiagnostic(BaseValidatorModel):
    severity: ValidateStateMachineDefinitionSeverityType
    code: str
    message: str
    location: Optional[str] = None


class ActivitySucceededEventDetails(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetails] = None


class ExecutionSucceededEventDetails(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetails] = None


class LambdaFunctionSucceededEventDetails(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetails] = None


class TaskSubmittedEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetails] = None


class TaskSucceededEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetails] = None


class StateExitedEventDetails(BaseValidatorModel):
    name: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetails] = None
    assignedVariables: Optional[Dict[str, str]] = None
    assignedVariablesDetails: Optional[AssignedVariablesDetails] = None


class LogDestination(BaseValidatorModel):
    cloudWatchLogsLogGroup: Optional[CloudWatchLogsLogGroup] = None


class EncryptionConfiguration(BaseValidatorModel):
    pass


class CreateActivityInput(BaseValidatorModel):
    name: str
    tags: Optional[Sequence[Tag]] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class CreateActivityOutput(BaseValidatorModel):
    activityArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadata


class CreateStateMachineAliasOutput(BaseValidatorModel):
    stateMachineAliasArn: str
    creationDate: datetime
    ResponseMetadata: ResponseMetadata


class CreateStateMachineOutput(BaseValidatorModel):
    stateMachineArn: str
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadata


class DescribeActivityOutput(BaseValidatorModel):
    activityArn: str
    name: str
    creationDate: datetime
    encryptionConfiguration: EncryptionConfiguration
    ResponseMetadata: ResponseMetadata


class ListActivitiesOutput(BaseValidatorModel):
    activities: List[ActivityListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class PublishStateMachineVersionOutput(BaseValidatorModel):
    creationDate: datetime
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadata


class RedriveExecutionOutput(BaseValidatorModel):
    redriveDate: datetime
    ResponseMetadata: ResponseMetadata


class StartExecutionOutput(BaseValidatorModel):
    executionArn: str
    startDate: datetime
    ResponseMetadata: ResponseMetadata


class StopExecutionOutput(BaseValidatorModel):
    stopDate: datetime
    ResponseMetadata: ResponseMetadata


class UpdateStateMachineAliasOutput(BaseValidatorModel):
    updateDate: datetime
    ResponseMetadata: ResponseMetadata


class UpdateStateMachineOutput(BaseValidatorModel):
    updateDate: datetime
    revisionId: str
    stateMachineVersionArn: str
    ResponseMetadata: ResponseMetadata


class CreateStateMachineAliasInput(BaseValidatorModel):
    name: str
    routingConfiguration: Sequence[RoutingConfigurationListItem]
    description: Optional[str] = None


class DescribeStateMachineAliasOutput(BaseValidatorModel):
    stateMachineAliasArn: str
    name: str
    description: str
    routingConfiguration: List[RoutingConfigurationListItem]
    creationDate: datetime
    updateDate: datetime
    ResponseMetadata: ResponseMetadata


class UpdateStateMachineAliasInput(BaseValidatorModel):
    stateMachineAliasArn: str
    description: Optional[str] = None
    routingConfiguration: Optional[Sequence[RoutingConfigurationListItem]] = None


class DescribeMapRunOutput(BaseValidatorModel):
    mapRunArn: str
    executionArn: str
    status: MapRunStatusType
    startDate: datetime
    stopDate: datetime
    maxConcurrency: int
    toleratedFailurePercentage: float
    toleratedFailureCount: int
    itemCounts: MapRunItemCounts
    executionCounts: MapRunExecutionCounts
    redriveCount: int
    redriveDate: datetime
    ResponseMetadata: ResponseMetadata


class ListExecutionsOutput(BaseValidatorModel):
    executions: List[ExecutionListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetExecutionHistoryInputPaginate(BaseValidatorModel):
    executionArn: str
    reverseOrder: Optional[bool] = None
    includeExecutionData: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListActivitiesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExecutionsInputPaginate(BaseValidatorModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMapRunsInputPaginate(BaseValidatorModel):
    executionArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStateMachinesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class TaskScheduledEventDetails(BaseValidatorModel):
    resourceType: str
    resource: str
    region: str
    parameters: str
    timeoutInSeconds: Optional[int] = None
    heartbeatInSeconds: Optional[int] = None
    taskCredentials: Optional[TaskCredentials] = None


class ListMapRunsOutput(BaseValidatorModel):
    mapRuns: List[MapRunListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStateMachineAliasesOutput(BaseValidatorModel):
    stateMachineAliases: List[StateMachineAliasListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStateMachineVersionsOutput(BaseValidatorModel):
    stateMachineVersions: List[StateMachineVersionListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StateMachineListItem(BaseValidatorModel):
    pass


class ListStateMachinesOutput(BaseValidatorModel):
    stateMachines: List[StateMachineListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ValidateStateMachineDefinitionOutput(BaseValidatorModel):
    result: ValidateStateMachineDefinitionResultCodeType
    diagnostics: List[ValidateStateMachineDefinitionDiagnostic]
    truncated: bool
    ResponseMetadata: ResponseMetadata


class LoggingConfigurationOutput(BaseValidatorModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[List[LogDestination]] = None


class LoggingConfiguration(BaseValidatorModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[Sequence[LogDestination]] = None


class InspectionData(BaseValidatorModel):
    pass


class TestStateOutput(BaseValidatorModel):
    output: str
    error: str
    cause: str
    inspectionData: InspectionData
    nextState: str
    status: TestExecutionStatusType
    ResponseMetadata: ResponseMetadata


class DescribeStateMachineForExecutionOutput(BaseValidatorModel):
    stateMachineArn: str
    name: str
    definition: str
    roleArn: str
    updateDate: datetime
    loggingConfiguration: LoggingConfigurationOutput
    tracingConfiguration: TracingConfiguration
    mapRunArn: str
    label: str
    revisionId: str
    encryptionConfiguration: EncryptionConfiguration
    variableReferences: Dict[str, List[str]]
    ResponseMetadata: ResponseMetadata


class HistoryEvent(BaseValidatorModel):
    pass


class GetExecutionHistoryOutput(BaseValidatorModel):
    events: List[HistoryEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LoggingConfigurationUnion(BaseValidatorModel):
    pass


class UpdateStateMachineInput(BaseValidatorModel):
    stateMachineArn: str
    definition: Optional[str] = None
    roleArn: Optional[str] = None
    loggingConfiguration: Optional[LoggingConfigurationUnion] = None
    tracingConfiguration: Optional[TracingConfiguration] = None
    publish: Optional[bool] = None
    versionDescription: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None


