from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codepipeline.codepipeline_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AWSSessionCredentials(BaseValidatorModel):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str


# This class is the input for the 'acknowledge_job' function.
class AcknowledgeJobInput(BaseValidatorModel):
    jobId: str
    nonce: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'acknowledge_third_party_job' function.
class AcknowledgeThirdPartyJobInput(BaseValidatorModel):
    jobId: str
    nonce: str
    clientToken: str


class ActionConfigurationProperty(BaseValidatorModel):
    name: str
    required: bool
    key: bool
    secret: bool
    queryable: Optional[bool] = None
    description: Optional[str] = None
    type: Optional[ActionConfigurationPropertyTypeType] = None


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
    files: Optional[List[str]] = None


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

Timestamp = Union[datetime, str]


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
    allowedAccounts: List[str]


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


class EncryptionKey(BaseValidatorModel):
    id: str
    type: Literal['KMS']


class BlockerDeclaration(BaseValidatorModel):
    name: str
    type: Literal['Schedule']


class ConditionExecution(BaseValidatorModel):
    status: Optional[ConditionExecutionStatusType] = None
    summary: Optional[str] = None
    lastStatusChange: Optional[datetime] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


# This class is the input for the 'delete_custom_action_type' function.
class DeleteCustomActionTypeInput(BaseValidatorModel):
    category: ActionCategoryType
    provider: str
    version: str


# This class is the input for the 'delete_pipeline' function.
class DeletePipelineInput(BaseValidatorModel):
    name: str


class DeleteWebhookInput(BaseValidatorModel):
    name: str


class DeregisterWebhookWithThirdPartyInput(BaseValidatorModel):
    webhookName: Optional[str] = None


# This class is the input for the 'disable_stage_transition' function.
class DisableStageTransitionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType
    reason: str


# This class is the input for the 'enable_stage_transition' function.
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
    pollingAccounts: Optional[List[str]] = None
    pollingServicePrincipals: Optional[List[str]] = None


class RetryConfiguration(BaseValidatorModel):
    retryMode: Optional[StageRetryModeType] = None


class FailureDetails(BaseValidatorModel):
    type: FailureTypeType
    message: str
    externalExecutionId: Optional[str] = None


# This class is the input for the 'get_action_type' function.
class GetActionTypeInput(BaseValidatorModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str


# This class is the input for the 'get_job_details' function.
class GetJobDetailsInput(BaseValidatorModel):
    jobId: str


# This class is the input for the 'get_pipeline_execution' function.
class GetPipelineExecutionInput(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str


# This class is the input for the 'get_pipeline' function.
class GetPipelineInput(BaseValidatorModel):
    name: str
    version: Optional[int] = None


class PipelineMetadata(BaseValidatorModel):
    pipelineArn: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    pollingDisabledAt: Optional[datetime] = None


# This class is the input for the 'get_pipeline_state' function.
class GetPipelineStateInput(BaseValidatorModel):
    name: str


# This class is the input for the 'get_third_party_job_details' function.
class GetThirdPartyJobDetailsInput(BaseValidatorModel):
    jobId: str
    clientToken: str


class GitBranchFilterCriteriaOutput(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitBranchFilterCriteria(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitFilePathFilterCriteriaOutput(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitFilePathFilterCriteria(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitTagFilterCriteriaOutput(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitTagFilterCriteria(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_action_types' function.
class ListActionTypesInput(BaseValidatorModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    nextToken: Optional[str] = None
    regionFilter: Optional[str] = None


# This class is the input for the 'list_pipelines' function.
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


# This class is the input for the 'list_rule_types' function.
class ListRuleTypesInput(BaseValidatorModel):
    ruleOwnerFilter: Optional[Literal['AWS']] = None
    regionFilter: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_webhooks' function.
class ListWebhooksInput(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'override_stage_condition' function.
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


# This class is the input for the 'retry_stage_execution' function.
class RetryStageExecutionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    retryMode: StageRetryModeType


class RetryStageMetadata(BaseValidatorModel):
    autoStageRetryAttempt: Optional[int] = None
    manualStageRetryAttempt: Optional[int] = None
    latestRetryTrigger: Optional[RetryTriggerType] = None


# This class is the input for the 'rollback_stage' function.
class RollbackStageInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    targetPipelineExecutionId: str


class RuleConfigurationProperty(BaseValidatorModel):
    name: str
    required: bool
    key: bool
    secret: bool
    queryable: Optional[bool] = None
    description: Optional[str] = None
    type: Optional[RuleConfigurationPropertyTypeType] = None


class RuleTypeId(BaseValidatorModel):
    category: Literal['Rule']
    provider: str
    owner: Optional[Literal['AWS']] = None
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


class StageExecution(BaseValidatorModel):
    pipelineExecutionId: str
    status: StageExecutionStatusType
    type: Optional[ExecutionTypeType] = None


class TransitionState(BaseValidatorModel):
    enabled: Optional[bool] = None
    lastChangedBy: Optional[str] = None
    lastChangedAt: Optional[datetime] = None
    disabledReason: Optional[str] = None


# This class is the input for the 'stop_pipeline_execution' function.
class StopPipelineExecutionInput(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str
    abandon: Optional[bool] = None
    reason: Optional[str] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class WebhookAuthConfiguration(BaseValidatorModel):
    AllowedIPRange: Optional[str] = None
    SecretToken: Optional[str] = None


class WebhookFilterRule(BaseValidatorModel):
    jsonPath: str
    matchEquals: Optional[str] = None


# This class is the output for the 'acknowledge_job' function.
class AcknowledgeJobOutput(BaseValidatorModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'acknowledge_third_party_job' function.
class AcknowledgeThirdPartyJobOutput(BaseValidatorModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_action_type' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_action_revision' function.
class PutActionRevisionOutput(BaseValidatorModel):
    newRevision: bool
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_approval_result' function.
class PutApprovalResultOutput(BaseValidatorModel):
    approvedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'retry_stage_execution' function.
class RetryStageExecutionOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rollback_stage' function.
class RollbackStageOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_pipeline_execution' function.
class StartPipelineExecutionOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_pipeline_execution' function.
class StopPipelineExecutionOutput(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'poll_for_jobs' function.
class PollForJobsInput(BaseValidatorModel):
    actionTypeId: ActionTypeId
    maxBatchSize: Optional[int] = None
    queryParam: Optional[Dict[str, str]] = None


# This class is the input for the 'poll_for_third_party_jobs' function.
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
    configuration: Optional[Dict[str, str]] = None
    commands: Optional[List[str]] = None
    outputArtifacts: Optional[List[OutputArtifact]] = None
    inputArtifacts: Optional[List[InputArtifact]] = None
    outputVariables: Optional[List[str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    namespace: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    environmentVariables: Optional[List[EnvironmentVariable]] = None


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


class ActionRevision(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: Timestamp


class CurrentRevision(BaseValidatorModel):
    revision: str
    changeIdentifier: str
    created: Optional[Timestamp] = None
    revisionSummary: Optional[str] = None


class ActionType(BaseValidatorModel):
    id: ActionTypeId
    inputArtifactDetails: ArtifactDetails
    outputArtifactDetails: ArtifactDetails
    settings: Optional[ActionTypeSettings] = None
    actionConfigurationProperties: Optional[List[ActionConfigurationProperty]] = None


# This class is the input for the 'put_approval_result' function.
class PutApprovalResultInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    result: ApprovalResult
    token: str


class ArtifactDetail(BaseValidatorModel):
    name: Optional[str] = None
    s3location: Optional[S3Location] = None


class ArtifactLocation(BaseValidatorModel):
    type: Optional[Literal['S3']] = None
    s3Location: Optional[S3ArtifactLocation] = None


class ArtifactStore(BaseValidatorModel):
    type: Literal['S3']
    location: str
    encryptionKey: Optional[EncryptionKey] = None


# This class is the input for the 'create_custom_action_type' function.
class CreateCustomActionTypeInput(BaseValidatorModel):
    category: ActionCategoryType
    provider: str
    version: str
    inputArtifactDetails: ArtifactDetails
    outputArtifactDetails: ArtifactDetails
    settings: Optional[ActionTypeSettings] = None
    configurationProperties: Optional[List[ActionConfigurationProperty]] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class ExecutorConfigurationOutput(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfiguration] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationOutput] = None


class ExecutorConfiguration(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfiguration] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfiguration] = None


# This class is the input for the 'put_job_failure_result' function.
class PutJobFailureResultInput(BaseValidatorModel):
    jobId: str
    failureDetails: FailureDetails


# This class is the input for the 'put_third_party_job_failure_result' function.
class PutThirdPartyJobFailureResultInput(BaseValidatorModel):
    jobId: str
    clientToken: str
    failureDetails: FailureDetails


class GitPullRequestFilterOutput(BaseValidatorModel):
    events: Optional[List[GitPullRequestEventTypeType]] = None
    branches: Optional[GitBranchFilterCriteriaOutput] = None
    filePaths: Optional[GitFilePathFilterCriteriaOutput] = None


class GitPullRequestFilter(BaseValidatorModel):
    events: Optional[List[GitPullRequestEventTypeType]] = None
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


# This class is the output for the 'list_pipelines' function.
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


# This class is the output for the 'poll_for_third_party_jobs' function.
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
    configuration: Optional[Dict[str, str]] = None
    commands: Optional[List[str]] = None
    inputArtifacts: Optional[List[InputArtifact]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    timeoutInMinutes: Optional[int] = None


class RuleType(BaseValidatorModel):
    id: RuleTypeId
    inputArtifactDetails: ArtifactDetails
    settings: Optional[RuleTypeSettings] = None
    ruleConfigurationProperties: Optional[List[RuleConfigurationProperty]] = None


# This class is the input for the 'start_pipeline_execution' function.
class StartPipelineExecutionInput(BaseValidatorModel):
    name: str
    variables: Optional[List[PipelineVariable]] = None
    clientRequestToken: Optional[str] = None
    sourceRevisions: Optional[List[SourceRevisionOverride]] = None


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
    filters: List[WebhookFilterRule]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfiguration


class ListActionExecutionsInputPaginate(BaseValidatorModel):
    pipelineName: str
    filter: Optional[ActionExecutionFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_action_executions' function.
class ListActionExecutionsInput(BaseValidatorModel):
    pipelineName: str
    filter: Optional[ActionExecutionFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListRuleExecutionsInputPaginate(BaseValidatorModel):
    pipelineName: str
    filter: Optional[RuleExecutionFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_rule_executions' function.
class ListRuleExecutionsInput(BaseValidatorModel):
    pipelineName: str
    filter: Optional[RuleExecutionFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


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

ActionRevisionUnion = Union[ActionRevision, ActionRevisionOutput]


# This class is the input for the 'put_job_success_result' function.
class PutJobSuccessResultInput(BaseValidatorModel):
    jobId: str
    currentRevision: Optional[CurrentRevision] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetails] = None
    outputVariables: Optional[Dict[str, str]] = None


# This class is the input for the 'put_third_party_job_success_result' function.
class PutThirdPartyJobSuccessResultInput(BaseValidatorModel):
    jobId: str
    clientToken: str
    currentRevision: Optional[CurrentRevision] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetails] = None


# This class is the output for the 'create_custom_action_type' function.
class CreateCustomActionTypeOutput(BaseValidatorModel):
    actionType: ActionType
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_action_types' function.
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


class Artifact(BaseValidatorModel):
    name: Optional[str] = None
    revision: Optional[str] = None
    location: Optional[ArtifactLocation] = None


class ActionTypeExecutorOutput(BaseValidatorModel):
    configuration: ExecutorConfigurationOutput
    type: ExecutorTypeType
    policyStatementsTemplate: Optional[str] = None
    jobTimeout: Optional[int] = None


class ActionTypeExecutor(BaseValidatorModel):
    configuration: ExecutorConfiguration
    type: ExecutorTypeType
    policyStatementsTemplate: Optional[str] = None
    jobTimeout: Optional[int] = None


class GitConfigurationOutput(BaseValidatorModel):
    sourceActionName: str
    push: Optional[List[GitPushFilterOutput]] = None
    pullRequest: Optional[List[GitPullRequestFilterOutput]] = None


class GitConfiguration(BaseValidatorModel):
    sourceActionName: str
    push: Optional[List[GitPushFilter]] = None
    pullRequest: Optional[List[GitPullRequestFilter]] = None


class ListPipelineExecutionsInputPaginate(BaseValidatorModel):
    pipelineName: str
    filter: Optional[PipelineExecutionFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_pipeline_executions' function.
class ListPipelineExecutionsInput(BaseValidatorModel):
    pipelineName: str
    maxResults: Optional[int] = None
    filter: Optional[PipelineExecutionFilter] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_pipeline_executions' function.
class ListPipelineExecutionsOutput(BaseValidatorModel):
    pipelineExecutionSummaries: List[PipelineExecutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_pipeline_execution' function.
class GetPipelineExecutionOutput(BaseValidatorModel):
    pipelineExecution: PipelineExecution
    ResponseMetadata: ResponseMetadata


class ConditionOutput(BaseValidatorModel):
    result: Optional[ResultType] = None
    rules: Optional[List[RuleDeclarationOutput]] = None


class Condition(BaseValidatorModel):
    result: Optional[ResultType] = None
    rules: Optional[List[RuleDeclaration]] = None


# This class is the output for the 'list_rule_types' function.
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

WebhookDefinitionUnion = Union[WebhookDefinition, WebhookDefinitionOutput]


class ConditionState(BaseValidatorModel):
    latestExecution: Optional[ConditionExecution] = None
    ruleStates: Optional[List[RuleState]] = None


# This class is the input for the 'put_action_revision' function.
class PutActionRevisionInput(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    actionRevision: ActionRevisionUnion


class ActionExecutionDetail(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    actionExecutionId: Optional[str] = None
    pipelineVersion: Optional[int] = None
    stageName: Optional[str] = None
    actionName: Optional[str] = None
    startTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    updatedBy: Optional[str] = None
    status: Optional[ActionExecutionStatusType] = None
    input: Optional[ActionExecutionInput] = None
    output: Optional[ActionExecutionOutput] = None


class RuleExecutionDetail(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    ruleExecutionId: Optional[str] = None
    pipelineVersion: Optional[int] = None
    stageName: Optional[str] = None
    ruleName: Optional[str] = None
    startTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    updatedBy: Optional[str] = None
    status: Optional[RuleExecutionStatusType] = None
    input: Optional[RuleExecutionInput] = None
    output: Optional[RuleExecutionOutput] = None


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


class ActionTypeDeclarationOutput(BaseValidatorModel):
    executor: ActionTypeExecutorOutput
    id: ActionTypeIdentifier
    inputArtifactDetails: ActionTypeArtifactDetails
    outputArtifactDetails: ActionTypeArtifactDetails
    description: Optional[str] = None
    permissions: Optional[ActionTypePermissionsOutput] = None
    properties: Optional[List[ActionTypeProperty]] = None
    urls: Optional[ActionTypeUrls] = None


class ActionTypeDeclaration(BaseValidatorModel):
    executor: ActionTypeExecutor
    id: ActionTypeIdentifier
    inputArtifactDetails: ActionTypeArtifactDetails
    outputArtifactDetails: ActionTypeArtifactDetails
    description: Optional[str] = None
    permissions: Optional[ActionTypePermissions] = None
    properties: Optional[List[ActionTypeProperty]] = None
    urls: Optional[ActionTypeUrls] = None


class PipelineTriggerDeclarationOutput(BaseValidatorModel):
    providerType: Literal['CodeStarSourceConnection']
    gitConfiguration: GitConfigurationOutput


class PipelineTriggerDeclaration(BaseValidatorModel):
    providerType: Literal['CodeStarSourceConnection']
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
    conditions: List[Condition]


class FailureConditions(BaseValidatorModel):
    result: Optional[ResultType] = None
    retryConfiguration: Optional[RetryConfiguration] = None
    conditions: Optional[List[Condition]] = None


class SuccessConditions(BaseValidatorModel):
    conditions: List[Condition]


# This class is the output for the 'list_webhooks' function.
class ListWebhooksOutput(BaseValidatorModel):
    webhooks: List[ListWebhookItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_webhook' function.
class PutWebhookOutput(BaseValidatorModel):
    webhook: ListWebhookItem
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_webhook' function.
class PutWebhookInput(BaseValidatorModel):
    webhook: WebhookDefinitionUnion
    tags: Optional[List[Tag]] = None


class StageConditionState(BaseValidatorModel):
    latestExecution: Optional[StageConditionsExecution] = None
    conditionStates: Optional[List[ConditionState]] = None


# This class is the output for the 'list_action_executions' function.
class ListActionExecutionsOutput(BaseValidatorModel):
    actionExecutionDetails: List[ActionExecutionDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_rule_executions' function.
class ListRuleExecutionsOutput(BaseValidatorModel):
    ruleExecutionDetails: List[RuleExecutionDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class JobDetails(BaseValidatorModel):
    id: Optional[str] = None
    data: Optional[JobData] = None
    accountId: Optional[str] = None


class Job(BaseValidatorModel):
    id: Optional[str] = None
    data: Optional[JobData] = None
    nonce: Optional[str] = None
    accountId: Optional[str] = None


class ThirdPartyJobDetails(BaseValidatorModel):
    id: Optional[str] = None
    data: Optional[ThirdPartyJobData] = None
    nonce: Optional[str] = None


# This class is the output for the 'get_action_type' function.
class GetActionTypeOutput(BaseValidatorModel):
    actionType: ActionTypeDeclarationOutput
    ResponseMetadata: ResponseMetadata

ActionTypeDeclarationUnion = Union[ActionTypeDeclaration, ActionTypeDeclarationOutput]


class StageDeclarationOutput(BaseValidatorModel):
    name: str
    actions: List[ActionDeclarationOutput]
    blockers: Optional[List[BlockerDeclaration]] = None
    onFailure: Optional[FailureConditionsOutput] = None
    onSuccess: Optional[SuccessConditionsOutput] = None
    beforeEntry: Optional[BeforeEntryConditionsOutput] = None


class StageDeclaration(BaseValidatorModel):
    name: str
    actions: List[ActionDeclaration]
    blockers: Optional[List[BlockerDeclaration]] = None
    onFailure: Optional[FailureConditions] = None
    onSuccess: Optional[SuccessConditions] = None
    beforeEntry: Optional[BeforeEntryConditions] = None


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


# This class is the output for the 'get_job_details' function.
class GetJobDetailsOutput(BaseValidatorModel):
    jobDetails: JobDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'poll_for_jobs' function.
class PollForJobsOutput(BaseValidatorModel):
    jobs: List[Job]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_third_party_job_details' function.
class GetThirdPartyJobDetailsOutput(BaseValidatorModel):
    jobDetails: ThirdPartyJobDetails
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_action_type' function.
class UpdateActionTypeInput(BaseValidatorModel):
    actionType: ActionTypeDeclarationUnion


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
    stages: List[StageDeclaration]
    artifactStore: Optional[ArtifactStore] = None
    artifactStores: Optional[Dict[str, ArtifactStore]] = None
    version: Optional[int] = None
    executionMode: Optional[ExecutionModeType] = None
    pipelineType: Optional[PipelineTypeType] = None
    variables: Optional[List[PipelineVariableDeclaration]] = None
    triggers: Optional[List[PipelineTriggerDeclaration]] = None


# This class is the output for the 'get_pipeline_state' function.
class GetPipelineStateOutput(BaseValidatorModel):
    pipelineName: str
    pipelineVersion: int
    stageStates: List[StageState]
    created: datetime
    updated: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_pipeline' function.
class CreatePipelineOutput(BaseValidatorModel):
    pipeline: PipelineDeclarationOutput
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_pipeline' function.
class GetPipelineOutput(BaseValidatorModel):
    pipeline: PipelineDeclarationOutput
    metadata: PipelineMetadata
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pipeline' function.
class UpdatePipelineOutput(BaseValidatorModel):
    pipeline: PipelineDeclarationOutput
    ResponseMetadata: ResponseMetadata

PipelineDeclarationUnion = Union[PipelineDeclaration, PipelineDeclarationOutput]


# This class is the input for the 'create_pipeline' function.
class CreatePipelineInput(BaseValidatorModel):
    pipeline: PipelineDeclarationUnion
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_pipeline' function.
class UpdatePipelineInput(BaseValidatorModel):
    pipeline: PipelineDeclarationUnion