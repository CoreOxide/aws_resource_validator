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


class AssignedVariablesDetailsTypeDef(BaseValidatorModel):
    truncated: Optional[bool] = None


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


class DeleteActivityInputTypeDef(BaseValidatorModel):
    activityArn: str


class DeleteStateMachineAliasInputTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str


class DeleteStateMachineInputTypeDef(BaseValidatorModel):
    stateMachineArn: str


class DeleteStateMachineVersionInputTypeDef(BaseValidatorModel):
    stateMachineVersionArn: str


class DescribeActivityInputTypeDef(BaseValidatorModel):
    activityArn: str


class DescribeExecutionInputTypeDef(BaseValidatorModel):
    executionArn: str
    includedData: Optional[IncludedDataType] = None


class DescribeMapRunInputTypeDef(BaseValidatorModel):
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


class DescribeStateMachineAliasInputTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str


class DescribeStateMachineForExecutionInputTypeDef(BaseValidatorModel):
    executionArn: str
    includedData: Optional[IncludedDataType] = None


class DescribeStateMachineInputTypeDef(BaseValidatorModel):
    stateMachineArn: str
    includedData: Optional[IncludedDataType] = None


class EvaluationFailedEventDetailsTypeDef(BaseValidatorModel):
    state: str
    error: Optional[str] = None
    cause: Optional[str] = None
    location: Optional[str] = None


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


class GetActivityTaskInputTypeDef(BaseValidatorModel):
    activityArn: str
    workerName: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetExecutionHistoryInputTypeDef(BaseValidatorModel):
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


class ListActivitiesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExecutionsInputTypeDef(BaseValidatorModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None


class ListMapRunsInputTypeDef(BaseValidatorModel):
    executionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MapRunListItemTypeDef(BaseValidatorModel):
    executionArn: str
    mapRunArn: str
    stateMachineArn: str
    startDate: datetime
    stopDate: Optional[datetime] = None


class ListStateMachineAliasesInputTypeDef(BaseValidatorModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StateMachineAliasListItemTypeDef(BaseValidatorModel):
    stateMachineAliasArn: str
    creationDate: datetime


class ListStateMachineVersionsInputTypeDef(BaseValidatorModel):
    stateMachineArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StateMachineVersionListItemTypeDef(BaseValidatorModel):
    stateMachineVersionArn: str
    creationDate: datetime


class ListStateMachinesInputTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class PublishStateMachineVersionInputTypeDef(BaseValidatorModel):
    stateMachineArn: str
    revisionId: Optional[str] = None
    description: Optional[str] = None


class RedriveExecutionInputTypeDef(BaseValidatorModel):
    executionArn: str
    clientToken: Optional[str] = None


class SendTaskFailureInputTypeDef(BaseValidatorModel):
    taskToken: str
    error: Optional[str] = None
    cause: Optional[str] = None


class SendTaskHeartbeatInputTypeDef(BaseValidatorModel):
    taskToken: str


class SendTaskSuccessInputTypeDef(BaseValidatorModel):
    taskToken: str
    output: str


class StopExecutionInputTypeDef(BaseValidatorModel):
    executionArn: str
    error: Optional[str] = None
    cause: Optional[str] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateMapRunInputTypeDef(BaseValidatorModel):
    mapRunArn: str
    maxConcurrency: Optional[int] = None
    toleratedFailurePercentage: Optional[float] = None
    toleratedFailureCount: Optional[int] = None


class ValidateStateMachineDefinitionDiagnosticTypeDef(BaseValidatorModel):
    severity: ValidateStateMachineDefinitionSeverityType
    code: str
    message: str
    location: Optional[str] = None


class ActivitySucceededEventDetailsTypeDef(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None


class ExecutionSucceededEventDetailsTypeDef(BaseValidatorModel):
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None


class LambdaFunctionSucceededEventDetailsTypeDef(BaseValidatorModel):
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


class StateExitedEventDetailsTypeDef(BaseValidatorModel):
    name: str
    output: Optional[str] = None
    outputDetails: Optional[HistoryEventExecutionDataDetailsTypeDef] = None
    assignedVariables: Optional[Dict[str, str]] = None
    assignedVariablesDetails: Optional[AssignedVariablesDetailsTypeDef] = None


class LogDestinationTypeDef(BaseValidatorModel):
    cloudWatchLogsLogGroup: Optional[CloudWatchLogsLogGroupTypeDef] = None


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    pass


class CreateActivityInputTypeDef(BaseValidatorModel):
    name: str
    tags: Optional[Sequence[TagTypeDef]] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class TagResourceInputTypeDef(BaseValidatorModel):
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
    encryptionConfiguration: EncryptionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListActivitiesOutputTypeDef(BaseValidatorModel):
    activities: List[ActivityListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class CreateStateMachineAliasInputTypeDef(BaseValidatorModel):
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


class UpdateStateMachineAliasInputTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetExecutionHistoryInputPaginateTypeDef(BaseValidatorModel):
    executionArn: str
    reverseOrder: Optional[bool] = None
    includeExecutionData: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListActivitiesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExecutionsInputPaginateTypeDef(BaseValidatorModel):
    stateMachineArn: Optional[str] = None
    statusFilter: Optional[ExecutionStatusType] = None
    mapRunArn: Optional[str] = None
    redriveFilter: Optional[ExecutionRedriveFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMapRunsInputPaginateTypeDef(BaseValidatorModel):
    executionArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStateMachinesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStateMachineAliasesOutputTypeDef(BaseValidatorModel):
    stateMachineAliases: List[StateMachineAliasListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStateMachineVersionsOutputTypeDef(BaseValidatorModel):
    stateMachineVersions: List[StateMachineVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StateMachineListItemTypeDef(BaseValidatorModel):
    pass


class ListStateMachinesOutputTypeDef(BaseValidatorModel):
    stateMachines: List[StateMachineListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ValidateStateMachineDefinitionOutputTypeDef(BaseValidatorModel):
    result: ValidateStateMachineDefinitionResultCodeType
    diagnostics: List[ValidateStateMachineDefinitionDiagnosticTypeDef]
    truncated: bool
    ResponseMetadata: ResponseMetadataTypeDef


class LoggingConfigurationOutputTypeDef(BaseValidatorModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[List[LogDestinationTypeDef]] = None


class LoggingConfigurationTypeDef(BaseValidatorModel):
    level: Optional[LogLevelType] = None
    includeExecutionData: Optional[bool] = None
    destinations: Optional[Sequence[LogDestinationTypeDef]] = None


class InspectionDataTypeDef(BaseValidatorModel):
    pass


class TestStateOutputTypeDef(BaseValidatorModel):
    output: str
    error: str
    cause: str
    inspectionData: InspectionDataTypeDef
    nextState: str
    status: TestExecutionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


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
    encryptionConfiguration: EncryptionConfigurationTypeDef
    variableReferences: Dict[str, List[str]]
    ResponseMetadata: ResponseMetadataTypeDef


class HistoryEventTypeDef(BaseValidatorModel):
    pass


class GetExecutionHistoryOutputTypeDef(BaseValidatorModel):
    events: List[HistoryEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LoggingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateStateMachineInputTypeDef(BaseValidatorModel):
    stateMachineArn: str
    definition: Optional[str] = None
    roleArn: Optional[str] = None
    loggingConfiguration: Optional[LoggingConfigurationUnionTypeDef] = None
    tracingConfiguration: Optional[TracingConfigurationTypeDef] = None
    publish: Optional[bool] = None
    versionDescription: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


