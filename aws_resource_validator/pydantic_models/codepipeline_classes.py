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
from aws_resource_validator.pydantic_models.codepipeline_constants import *

class AWSSessionCredentials(BaseValidatorModel):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str


class AcknowledgeJobInput(BaseValidatorModel):
    jobId: str
    nonce: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AcknowledgeThirdPartyJobInput(BaseValidatorModel):
    jobId: str
    nonce: str
    clientToken: str


class ActionConfiguration(BaseValidatorModel):
    configuration: Optional[Dict[str, str]] = None


class ActionContext(BaseValidatorModel):
    name: Optional[str] = None
    actionExecutionId: Optional[str] = None


class ActionTypeId(BaseValidatorModel):
    category: ActionCategoryType
    owner: ActionOwnerType
    provider: str
    version: str


class EnvironmentVariable(BaseValidatorModel):
    name: str
    value: str


class InputArtifact(BaseValidatorModel):
    name: str


class OutputArtifactOutput(BaseValidatorModel):
    name: str
    files: Optional[List[str]] = None


class OutputArtifact(BaseValidatorModel):
    name: str
    files: Optional[Sequence[str]] = None


class LatestInPipelineExecutionFilter(BaseValidatorModel):
    pipelineExecutionId: str
    startTimeRange: StartTimeRangeType


class ErrorDetails(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class ActionRevisionOutput(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: datetime


class ActionTypeArtifactDetails(BaseValidatorModel):
    minimumCount: int
    maximumCount: int


class ActionTypeIdentifier(BaseValidatorModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str


class ActionTypePermissionsOutput(BaseValidatorModel):
    allowedAccounts: List[str]


class ActionTypeProperty(BaseValidatorModel):
    name: str
    optional: bool
    key: bool
    noEcho: bool
    queryable: Optional[bool] = None
    description: Optional[str] = None


class ActionTypeUrls(BaseValidatorModel):
    configurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None


class ActionTypePermissions(BaseValidatorModel):
    allowedAccounts: Sequence[str]


class ActionTypeSettings(BaseValidatorModel):
    thirdPartyConfigurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None


class ArtifactDetails(BaseValidatorModel):
    minimumCount: int
    maximumCount: int


class ApprovalResult(BaseValidatorModel):
    summary: str
    status: ApprovalStatusType


class S3Location(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None


class S3ArtifactLocation(BaseValidatorModel):
    bucketName: str
    objectKey: str


class ArtifactRevision(BaseValidatorModel):
    name: Optional[str] = None
    revisionId: Optional[str] = None
    revisionChangeIdentifier: Optional[str] = None
    revisionSummary: Optional[str] = None
    created: Optional[datetime] = None
    revisionUrl: Optional[str] = None


class ConditionExecution(BaseValidatorModel):
    status: Optional[ConditionExecutionStatusType] = None
    summary: Optional[str] = None
    lastStatusChange: Optional[datetime] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class DeleteCustomActionTypeInput(BaseValidatorModel):
    category: ActionCategoryType
    provider: str
    version: str


class DeletePipelineInput(BaseValidatorModel):
    name: str


class DeleteWebhookInput(BaseValidatorModel):
    name: str


class DeregisterWebhookWithThirdPartyInput(BaseValidatorModel):
    webhookName: Optional[str] = None


class DisableStageTransitionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType
    reason: str


class EnableStageTransitionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType


class ExecutionDetails(BaseValidatorModel):
    summary: Optional[str] = None
    externalExecutionId: Optional[str] = None
    percentComplete: Optional[int] = None


class ExecutionTrigger(BaseValidatorModel):
    triggerType: Optional[TriggerTypeType] = None
    triggerDetail: Optional[str] = None


class JobWorkerExecutorConfigurationOutput(BaseValidatorModel):
    pollingAccounts: Optional[List[str]] = None
    pollingServicePrincipals: Optional[List[str]] = None


class LambdaExecutorConfiguration(BaseValidatorModel):
    lambdaFunctionArn: str


class JobWorkerExecutorConfiguration(BaseValidatorModel):
    pollingAccounts: Optional[Sequence[str]] = None
    pollingServicePrincipals: Optional[Sequence[str]] = None


class RetryConfiguration(BaseValidatorModel):
    retryMode: Optional[StageRetryModeType] = None


class GetActionTypeInput(BaseValidatorModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str


class GetJobDetailsInput(BaseValidatorModel):
    jobId: str


class GetPipelineExecutionInput(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str


class GetPipelineInput(BaseValidatorModel):
    name: str
    version: Optional[int] = None


class PipelineMetadata(BaseValidatorModel):
    pipelineArn: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    pollingDisabledAt: Optional[datetime] = None


class GetPipelineStateInput(BaseValidatorModel):
    name: str


class GetThirdPartyJobDetailsInput(BaseValidatorModel):
    jobId: str
    clientToken: str


class GitBranchFilterCriteriaOutput(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitBranchFilterCriteria(BaseValidatorModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None


class GitFilePathFilterCriteriaOutput(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitFilePathFilterCriteria(BaseValidatorModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None


class GitTagFilterCriteriaOutput(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitTagFilterCriteria(BaseValidatorModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListActionTypesInput(BaseValidatorModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    nextToken: Optional[str] = None
    regionFilter: Optional[str] = None


class ListPipelinesInput(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PipelineSummary(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[int] = None
    pipelineType: Optional[PipelineTypeType] = None
    executionMode: Optional[ExecutionModeType] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class ListRuleTypesInput(BaseValidatorModel):
    ruleOwnerFilter: Optional[Literal["AWS"]] = None
    regionFilter: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWebhooksInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OverrideStageConditionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    conditionType: ConditionTypeType


class StageContext(BaseValidatorModel):
    name: Optional[str] = None


class PipelineVariableDeclaration(BaseValidatorModel):
    name: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None


class SucceededInStageFilter(BaseValidatorModel):
    stageName: Optional[str] = None


class PipelineRollbackMetadata(BaseValidatorModel):
    rollbackTargetPipelineExecutionId: Optional[str] = None


class SourceRevision(BaseValidatorModel):
    actionName: str
    revisionId: Optional[str] = None
    revisionSummary: Optional[str] = None
    revisionUrl: Optional[str] = None


class StopExecutionTrigger(BaseValidatorModel):
    reason: Optional[str] = None


class ResolvedPipelineVariable(BaseValidatorModel):
    name: Optional[str] = None
    resolvedValue: Optional[str] = None


class PipelineVariable(BaseValidatorModel):
    name: str
    value: str


class ThirdPartyJob(BaseValidatorModel):
    clientId: Optional[str] = None
    jobId: Optional[str] = None


class RegisterWebhookWithThirdPartyInput(BaseValidatorModel):
    webhookName: Optional[str] = None


class RetryStageExecutionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    retryMode: StageRetryModeType


class RetryStageMetadata(BaseValidatorModel):
    autoStageRetryAttempt: Optional[int] = None
    manualStageRetryAttempt: Optional[int] = None
    latestRetryTrigger: Optional[RetryTriggerType] = None


class RollbackStageInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    targetPipelineExecutionId: str


class RuleTypeId(BaseValidatorModel):
    category: Literal["Rule"]
    provider: str
    owner: Optional[Literal["AWS"]] = None
    version: Optional[str] = None


class RuleRevision(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: datetime


class RuleTypeSettings(BaseValidatorModel):
    thirdPartyConfigurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None


class SourceRevisionOverride(BaseValidatorModel):
    actionName: str
    revisionType: SourceRevisionTypeType
    revisionValue: str


class StageConditionsExecution(BaseValidatorModel):
    status: Optional[ConditionExecutionStatusType] = None
    summary: Optional[str] = None


class TransitionState(BaseValidatorModel):
    enabled: Optional[bool] = None
    lastChangedBy: Optional[str] = None
    lastChangedAt: Optional[datetime] = None
    disabledReason: Optional[str] = None


class StopPipelineExecutionInput(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str
    abandon: Optional[bool] = None
    reason: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class WebhookAuthConfiguration(BaseValidatorModel):
    AllowedIPRange: Optional[str] = None
    SecretToken: Optional[str] = None


class WebhookFilterRule(BaseValidatorModel):
    jsonPath: str
    matchEquals: Optional[str] = None


class AcknowledgeJobOutput(BaseValidatorModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadata


class AcknowledgeThirdPartyJobOutput(BaseValidatorModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class PutActionRevisionOutput(BaseValidatorModel):
    newRevision: bool
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


class PutApprovalResultOutput(BaseValidatorModel):
    approvedAt: datetime
    ResponseMetadata: ResponseMetadata


class RetryStageExecutionOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


class RollbackStageOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


class StartPipelineExecutionOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


class StopPipelineExecutionOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


class PollForJobsInput(BaseValidatorModel):
    actionTypeId: ActionTypeId
    maxBatchSize: Optional[int] = None
    queryParam: Optional[Mapping[str, str]] = None


class PollForThirdPartyJobsInput(BaseValidatorModel):
    actionTypeId: ActionTypeId
    maxBatchSize: Optional[int] = None


class ActionDeclarationOutput(BaseValidatorModel):
    name: str
    actionTypeId: ActionTypeId
    runOrder: Optional[int] = None
    configuration: Optional[Dict[str, str]] = None
    commands: Optional[List[str]] = None
    outputArtifacts: Optional[List[OutputArtifactOutput]] = None
    inputArtifacts: Optional[List[InputArtifact]] = None
    outputVariables: Optional[List[str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    namespace: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    environmentVariables: Optional[List[EnvironmentVariable]] = None


class ActionDeclaration(BaseValidatorModel):
    name: str
    actionTypeId: ActionTypeId
    runOrder: Optional[int] = None
    configuration: Optional[Mapping[str, str]] = None
    commands: Optional[Sequence[str]] = None
    outputArtifacts: Optional[Sequence[OutputArtifact]] = None
    inputArtifacts: Optional[Sequence[InputArtifact]] = None
    outputVariables: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    namespace: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    environmentVariables: Optional[Sequence[EnvironmentVariable]] = None


class ActionExecutionFilter(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilter] = None


class RuleExecutionFilter(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilter] = None


class ActionExecutionResult(BaseValidatorModel):
    externalExecutionId: Optional[str] = None
    externalExecutionSummary: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetails] = None
    logStreamARN: Optional[str] = None


class ActionExecution(BaseValidatorModel):
    actionExecutionId: Optional[str] = None
    status: Optional[ActionExecutionStatusType] = None
    summary: Optional[str] = None
    lastStatusChange: Optional[datetime] = None
    token: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    externalExecutionId: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    percentComplete: Optional[int] = None
    errorDetails: Optional[ErrorDetails] = None
    logStreamARN: Optional[str] = None


class RuleExecutionResult(BaseValidatorModel):
    externalExecutionId: Optional[str] = None
    externalExecutionSummary: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetails] = None


class RuleExecution(BaseValidatorModel):
    ruleExecutionId: Optional[str] = None
    status: Optional[RuleExecutionStatusType] = None
    summary: Optional[str] = None
    lastStatusChange: Optional[datetime] = None
    token: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    externalExecutionId: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetails] = None


class Timestamp(BaseValidatorModel):
    pass


class ActionRevision(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: Timestamp


class CurrentRevision(BaseValidatorModel):
    revision: str
    changeIdentifier: str
    created: Optional[Timestamp] = None
    revisionSummary: Optional[str] = None


class PutApprovalResultInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    result: ApprovalResult
    token: str


class ArtifactDetail(BaseValidatorModel):
    name: Optional[str] = None
    s3location: Optional[S3Location] = None


class ActionConfigurationProperty(BaseValidatorModel):
    pass


class CreateCustomActionTypeInput(BaseValidatorModel):
    category: ActionCategoryType
    provider: str
    version: str
    inputArtifactDetails: ArtifactDetails
    outputArtifactDetails: ArtifactDetails
    settings: Optional[ActionTypeSettings] = None
    configurationProperties: Optional[Sequence[ActionConfigurationProperty]] = None
    tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class ExecutorConfigurationOutput(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfiguration] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationOutput] = None


class ExecutorConfiguration(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfiguration] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfiguration] = None


class FailureDetails(BaseValidatorModel):
    pass


class PutJobFailureResultInput(BaseValidatorModel):
    jobId: str
    failureDetails: FailureDetails


class PutThirdPartyJobFailureResultInput(BaseValidatorModel):
    jobId: str
    clientToken: str
    failureDetails: FailureDetails


class GitPullRequestFilterOutput(BaseValidatorModel):
    events: Optional[List[GitPullRequestEventTypeType]] = None
    branches: Optional[GitBranchFilterCriteriaOutput] = None
    filePaths: Optional[GitFilePathFilterCriteriaOutput] = None


class GitPullRequestFilter(BaseValidatorModel):
    events: Optional[Sequence[GitPullRequestEventTypeType]] = None
    branches: Optional[GitBranchFilterCriteria] = None
    filePaths: Optional[GitFilePathFilterCriteria] = None


class GitPushFilterOutput(BaseValidatorModel):
    tags: Optional[GitTagFilterCriteriaOutput] = None
    branches: Optional[GitBranchFilterCriteriaOutput] = None
    filePaths: Optional[GitFilePathFilterCriteriaOutput] = None


class GitPushFilter(BaseValidatorModel):
    tags: Optional[GitTagFilterCriteria] = None
    branches: Optional[GitBranchFilterCriteria] = None
    filePaths: Optional[GitFilePathFilterCriteria] = None


class ListActionTypesInputPaginate(BaseValidatorModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    regionFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelinesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceInputPaginate(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWebhooksInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPipelinesOutput(BaseValidatorModel):
    pipelines: List[PipelineSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PipelineContext(BaseValidatorModel):
    pipelineName: Optional[str] = None
    stage: Optional[StageContext] = None
    action: Optional[ActionContext] = None
    pipelineArn: Optional[str] = None
    pipelineExecutionId: Optional[str] = None


class PipelineExecutionFilter(BaseValidatorModel):
    succeededInStage: Optional[SucceededInStageFilter] = None


class PipelineExecutionSummary(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    status: Optional[PipelineExecutionStatusType] = None
    statusSummary: Optional[str] = None
    startTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    sourceRevisions: Optional[List[SourceRevision]] = None
    trigger: Optional[ExecutionTrigger] = None
    stopTrigger: Optional[StopExecutionTrigger] = None
    executionMode: Optional[ExecutionModeType] = None
    executionType: Optional[ExecutionTypeType] = None
    rollbackMetadata: Optional[PipelineRollbackMetadata] = None


class PipelineExecution(BaseValidatorModel):
    pipelineName: Optional[str] = None
    pipelineVersion: Optional[int] = None
    pipelineExecutionId: Optional[str] = None
    status: Optional[PipelineExecutionStatusType] = None
    statusSummary: Optional[str] = None
    artifactRevisions: Optional[List[ArtifactRevision]] = None
    variables: Optional[List[ResolvedPipelineVariable]] = None
    trigger: Optional[ExecutionTrigger] = None
    executionMode: Optional[ExecutionModeType] = None
    executionType: Optional[ExecutionTypeType] = None
    rollbackMetadata: Optional[PipelineRollbackMetadata] = None


class PollForThirdPartyJobsOutput(BaseValidatorModel):
    jobs: List[ThirdPartyJob]
    ResponseMetadata: ResponseMetadata


class RuleDeclarationOutput(BaseValidatorModel):
    name: str
    ruleTypeId: RuleTypeId
    configuration: Optional[Dict[str, str]] = None
    commands: Optional[List[str]] = None
    inputArtifacts: Optional[List[InputArtifact]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    timeoutInMinutes: Optional[int] = None


class RuleDeclaration(BaseValidatorModel):
    name: str
    ruleTypeId: RuleTypeId
    configuration: Optional[Mapping[str, str]] = None
    commands: Optional[Sequence[str]] = None
    inputArtifacts: Optional[Sequence[InputArtifact]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    timeoutInMinutes: Optional[int] = None


class StartPipelineExecutionInput(BaseValidatorModel):
    name: str
    variables: Optional[Sequence[PipelineVariable]] = None
    clientRequestToken: Optional[str] = None
    sourceRevisions: Optional[Sequence[SourceRevisionOverride]] = None


class WebhookDefinitionOutput(BaseValidatorModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: List[WebhookFilterRule]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfiguration


class WebhookDefinition(BaseValidatorModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: Sequence[WebhookFilterRule]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfiguration


class ActionState(BaseValidatorModel):
    actionName: Optional[str] = None
    currentRevision: Optional[ActionRevisionOutput] = None
    latestExecution: Optional[ActionExecution] = None
    entityUrl: Optional[str] = None
    revisionUrl: Optional[str] = None


class RuleExecutionOutput(BaseValidatorModel):
    executionResult: Optional[RuleExecutionResult] = None


class RuleState(BaseValidatorModel):
    ruleName: Optional[str] = None
    currentRevision: Optional[RuleRevision] = None
    latestExecution: Optional[RuleExecution] = None
    entityUrl: Optional[str] = None
    revisionUrl: Optional[str] = None


class PutJobSuccessResultInput(BaseValidatorModel):
    jobId: str
    currentRevision: Optional[CurrentRevision] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetails] = None
    outputVariables: Optional[Mapping[str, str]] = None


class PutThirdPartyJobSuccessResultInput(BaseValidatorModel):
    jobId: str
    clientToken: str
    currentRevision: Optional[CurrentRevision] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetails] = None


class ActionType(BaseValidatorModel):
    pass


class CreateCustomActionTypeOutput(BaseValidatorModel):
    actionType: ActionType
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ListActionTypesOutput(BaseValidatorModel):
    actionTypes: List[ActionType]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ActionExecutionInput(BaseValidatorModel):
    actionTypeId: Optional[ActionTypeId] = None
    configuration: Optional[Dict[str, str]] = None
    resolvedConfiguration: Optional[Dict[str, str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    inputArtifacts: Optional[List[ArtifactDetail]] = None
    namespace: Optional[str] = None


class ActionExecutionOutput(BaseValidatorModel):
    outputArtifacts: Optional[List[ArtifactDetail]] = None
    executionResult: Optional[ActionExecutionResult] = None
    outputVariables: Optional[Dict[str, str]] = None


class RuleExecutionInput(BaseValidatorModel):
    ruleTypeId: Optional[RuleTypeId] = None
    configuration: Optional[Dict[str, str]] = None
    resolvedConfiguration: Optional[Dict[str, str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    inputArtifacts: Optional[List[ArtifactDetail]] = None


class ArtifactLocation(BaseValidatorModel):
    pass


class Artifact(BaseValidatorModel):
    name: Optional[str] = None
    revision: Optional[str] = None
    location: Optional[ArtifactLocation] = None


class GitConfigurationOutput(BaseValidatorModel):
    sourceActionName: str
    push: Optional[List[GitPushFilterOutput]] = None
    pullRequest: Optional[List[GitPullRequestFilterOutput]] = None


class GitConfiguration(BaseValidatorModel):
    sourceActionName: str
    push: Optional[Sequence[GitPushFilter]] = None
    pullRequest: Optional[Sequence[GitPullRequestFilter]] = None


class ListPipelineExecutionsOutput(BaseValidatorModel):
    pipelineExecutionSummaries: List[PipelineExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetPipelineExecutionOutput(BaseValidatorModel):
    pipelineExecution: PipelineExecution
    ResponseMetadata: ResponseMetadata


class ConditionOutput(BaseValidatorModel):
    result: Optional[ResultType] = None
    rules: Optional[List[RuleDeclarationOutput]] = None


class Condition(BaseValidatorModel):
    result: Optional[ResultType] = None
    rules: Optional[Sequence[RuleDeclaration]] = None


class RuleType(BaseValidatorModel):
    pass


class ListRuleTypesOutput(BaseValidatorModel):
    ruleTypes: List[RuleType]
    ResponseMetadata: ResponseMetadata


class ListWebhookItem(BaseValidatorModel):
    definition: WebhookDefinitionOutput
    url: str
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None
    lastTriggered: Optional[datetime] = None
    arn: Optional[str] = None
    tags: Optional[List[Tag]] = None


class ConditionState(BaseValidatorModel):
    latestExecution: Optional[ConditionExecution] = None
    ruleStates: Optional[List[RuleState]] = None


class ActionRevisionUnion(BaseValidatorModel):
    pass


class PutActionRevisionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    actionRevision: ActionRevisionUnion


class EncryptionKey(BaseValidatorModel):
    pass


class JobData(BaseValidatorModel):
    actionTypeId: Optional[ActionTypeId] = None
    actionConfiguration: Optional[ActionConfiguration] = None
    pipelineContext: Optional[PipelineContext] = None
    inputArtifacts: Optional[List[Artifact]] = None
    outputArtifacts: Optional[List[Artifact]] = None
    artifactCredentials: Optional[AWSSessionCredentials] = None
    continuationToken: Optional[str] = None
    encryptionKey: Optional[EncryptionKey] = None


class ThirdPartyJobData(BaseValidatorModel):
    actionTypeId: Optional[ActionTypeId] = None
    actionConfiguration: Optional[ActionConfiguration] = None
    pipelineContext: Optional[PipelineContext] = None
    inputArtifacts: Optional[List[Artifact]] = None
    outputArtifacts: Optional[List[Artifact]] = None
    artifactCredentials: Optional[AWSSessionCredentials] = None
    continuationToken: Optional[str] = None
    encryptionKey: Optional[EncryptionKey] = None


class PipelineTriggerDeclarationOutput(BaseValidatorModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationOutput


class PipelineTriggerDeclaration(BaseValidatorModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfiguration


class BeforeEntryConditionsOutput(BaseValidatorModel):
    conditions: List[ConditionOutput]


class FailureConditionsOutput(BaseValidatorModel):
    result: Optional[ResultType] = None
    retryConfiguration: Optional[RetryConfiguration] = None
    conditions: Optional[List[ConditionOutput]] = None


class SuccessConditionsOutput(BaseValidatorModel):
    conditions: List[ConditionOutput]


class BeforeEntryConditions(BaseValidatorModel):
    conditions: Sequence[Condition]


class FailureConditions(BaseValidatorModel):
    result: Optional[ResultType] = None
    retryConfiguration: Optional[RetryConfiguration] = None
    conditions: Optional[Sequence[Condition]] = None


class SuccessConditions(BaseValidatorModel):
    conditions: Sequence[Condition]


class ListWebhooksOutput(BaseValidatorModel):
    webhooks: List[ListWebhookItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutWebhookOutput(BaseValidatorModel):
    webhook: ListWebhookItem
    ResponseMetadata: ResponseMetadata


class WebhookDefinitionUnion(BaseValidatorModel):
    pass


class PutWebhookInput(BaseValidatorModel):
    webhook: WebhookDefinitionUnion
    tags: Optional[Sequence[Tag]] = None


class StageConditionState(BaseValidatorModel):
    latestExecution: Optional[StageConditionsExecution] = None
    conditionStates: Optional[List[ConditionState]] = None


class ActionExecutionDetail(BaseValidatorModel):
    pass


class ListActionExecutionsOutput(BaseValidatorModel):
    actionExecutionDetails: List[ActionExecutionDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RuleExecutionDetail(BaseValidatorModel):
    pass


class ListRuleExecutionsOutput(BaseValidatorModel):
    ruleExecutionDetails: List[RuleExecutionDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ActionTypeDeclarationOutput(BaseValidatorModel):
    pass


class GetActionTypeOutput(BaseValidatorModel):
    actionType: ActionTypeDeclarationOutput
    ResponseMetadata: ResponseMetadata


class BlockerDeclaration(BaseValidatorModel):
    pass


class StageDeclarationOutput(BaseValidatorModel):
    name: str
    actions: List[ActionDeclarationOutput]
    blockers: Optional[List[BlockerDeclaration]] = None
    onFailure: Optional[FailureConditionsOutput] = None
    onSuccess: Optional[SuccessConditionsOutput] = None
    beforeEntry: Optional[BeforeEntryConditionsOutput] = None


class StageDeclaration(BaseValidatorModel):
    name: str
    actions: Sequence[ActionDeclaration]
    blockers: Optional[Sequence[BlockerDeclaration]] = None
    onFailure: Optional[FailureConditions] = None
    onSuccess: Optional[SuccessConditions] = None
    beforeEntry: Optional[BeforeEntryConditions] = None


class StageExecution(BaseValidatorModel):
    pass


class StageState(BaseValidatorModel):
    stageName: Optional[str] = None
    inboundExecution: Optional[StageExecution] = None
    inboundExecutions: Optional[List[StageExecution]] = None
    inboundTransitionState: Optional[TransitionState] = None
    actionStates: Optional[List[ActionState]] = None
    latestExecution: Optional[StageExecution] = None
    beforeEntryConditionState: Optional[StageConditionState] = None
    onSuccessConditionState: Optional[StageConditionState] = None
    onFailureConditionState: Optional[StageConditionState] = None
    retryStageMetadata: Optional[RetryStageMetadata] = None


class JobDetails(BaseValidatorModel):
    pass


class GetJobDetailsOutput(BaseValidatorModel):
    jobDetails: JobDetails
    ResponseMetadata: ResponseMetadata


class Job(BaseValidatorModel):
    pass


class PollForJobsOutput(BaseValidatorModel):
    jobs: List[Job]
    ResponseMetadata: ResponseMetadata


class ThirdPartyJobDetails(BaseValidatorModel):
    pass


class GetThirdPartyJobDetailsOutput(BaseValidatorModel):
    jobDetails: ThirdPartyJobDetails
    ResponseMetadata: ResponseMetadata


class ActionTypeDeclarationUnion(BaseValidatorModel):
    pass


class UpdateActionTypeInput(BaseValidatorModel):
    actionType: ActionTypeDeclarationUnion


class ArtifactStore(BaseValidatorModel):
    pass


class PipelineDeclarationOutput(BaseValidatorModel):
    name: str
    roleArn: str
    stages: List[StageDeclarationOutput]
    artifactStore: Optional[ArtifactStore] = None
    artifactStores: Optional[Dict[str, ArtifactStore]] = None
    version: Optional[int] = None
    executionMode: Optional[ExecutionModeType] = None
    pipelineType: Optional[PipelineTypeType] = None
    variables: Optional[List[PipelineVariableDeclaration]] = None
    triggers: Optional[List[PipelineTriggerDeclarationOutput]] = None


class PipelineDeclaration(BaseValidatorModel):
    name: str
    roleArn: str
    stages: Sequence[StageDeclaration]
    artifactStore: Optional[ArtifactStore] = None
    artifactStores: Optional[Mapping[str, ArtifactStore]] = None
    version: Optional[int] = None
    executionMode: Optional[ExecutionModeType] = None
    pipelineType: Optional[PipelineTypeType] = None
    variables: Optional[Sequence[PipelineVariableDeclaration]] = None
    triggers: Optional[Sequence[PipelineTriggerDeclaration]] = None


class GetPipelineStateOutput(BaseValidatorModel):
    pipelineName: str
    pipelineVersion: int
    stageStates: List[StageState]
    created: datetime
    updated: datetime
    ResponseMetadata: ResponseMetadata


class CreatePipelineOutput(BaseValidatorModel):
    pipeline: PipelineDeclarationOutput
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class GetPipelineOutput(BaseValidatorModel):
    pipeline: PipelineDeclarationOutput
    metadata: PipelineMetadata
    ResponseMetadata: ResponseMetadata


class UpdatePipelineOutput(BaseValidatorModel):
    pipeline: PipelineDeclarationOutput
    ResponseMetadata: ResponseMetadata


class PipelineDeclarationUnion(BaseValidatorModel):
    pass


class CreatePipelineInput(BaseValidatorModel):
    pipeline: PipelineDeclarationUnion
    tags: Optional[Sequence[Tag]] = None


class UpdatePipelineInput(BaseValidatorModel):
    pipeline: PipelineDeclarationUnion


