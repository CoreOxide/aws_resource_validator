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

class AWSSessionCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str


class AcknowledgeJobInputTypeDef(BaseValidatorModel):
    jobId: str
    nonce: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AcknowledgeThirdPartyJobInputTypeDef(BaseValidatorModel):
    jobId: str
    nonce: str
    clientToken: str


class ActionConfigurationTypeDef(BaseValidatorModel):
    configuration: Optional[Dict[str, str]] = None


class ActionContextTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    actionExecutionId: Optional[str] = None


class ActionTypeIdTypeDef(BaseValidatorModel):
    category: ActionCategoryType
    owner: ActionOwnerType
    provider: str
    version: str


class EnvironmentVariableTypeDef(BaseValidatorModel):
    name: str
    value: str


class InputArtifactTypeDef(BaseValidatorModel):
    name: str


class OutputArtifactOutputTypeDef(BaseValidatorModel):
    name: str
    files: Optional[List[str]] = None


class OutputArtifactTypeDef(BaseValidatorModel):
    name: str
    files: Optional[Sequence[str]] = None


class LatestInPipelineExecutionFilterTypeDef(BaseValidatorModel):
    pipelineExecutionId: str
    startTimeRange: StartTimeRangeType


class ErrorDetailsTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class ActionRevisionOutputTypeDef(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: datetime


class ActionTypeArtifactDetailsTypeDef(BaseValidatorModel):
    minimumCount: int
    maximumCount: int


class ActionTypeIdentifierTypeDef(BaseValidatorModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str


class ActionTypePermissionsOutputTypeDef(BaseValidatorModel):
    allowedAccounts: List[str]


class ActionTypePropertyTypeDef(BaseValidatorModel):
    name: str
    optional: bool
    key: bool
    noEcho: bool
    queryable: Optional[bool] = None
    description: Optional[str] = None


class ActionTypeUrlsTypeDef(BaseValidatorModel):
    configurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None


class ActionTypePermissionsTypeDef(BaseValidatorModel):
    allowedAccounts: Sequence[str]


class ActionTypeSettingsTypeDef(BaseValidatorModel):
    thirdPartyConfigurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None


class ArtifactDetailsTypeDef(BaseValidatorModel):
    minimumCount: int
    maximumCount: int


class ApprovalResultTypeDef(BaseValidatorModel):
    summary: str
    status: ApprovalStatusType


class S3LocationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    key: Optional[str] = None


class S3ArtifactLocationTypeDef(BaseValidatorModel):
    bucketName: str
    objectKey: str


class ArtifactRevisionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    revisionId: Optional[str] = None
    revisionChangeIdentifier: Optional[str] = None
    revisionSummary: Optional[str] = None
    created: Optional[datetime] = None
    revisionUrl: Optional[str] = None


class ConditionExecutionTypeDef(BaseValidatorModel):
    status: Optional[ConditionExecutionStatusType] = None
    summary: Optional[str] = None
    lastStatusChange: Optional[datetime] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class DeleteCustomActionTypeInputTypeDef(BaseValidatorModel):
    category: ActionCategoryType
    provider: str
    version: str


class DeletePipelineInputTypeDef(BaseValidatorModel):
    name: str


class DeleteWebhookInputTypeDef(BaseValidatorModel):
    name: str


class DeregisterWebhookWithThirdPartyInputTypeDef(BaseValidatorModel):
    webhookName: Optional[str] = None


class DisableStageTransitionInputTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType
    reason: str


class EnableStageTransitionInputTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType


class ExecutionDetailsTypeDef(BaseValidatorModel):
    summary: Optional[str] = None
    externalExecutionId: Optional[str] = None
    percentComplete: Optional[int] = None


class ExecutionTriggerTypeDef(BaseValidatorModel):
    triggerType: Optional[TriggerTypeType] = None
    triggerDetail: Optional[str] = None


class JobWorkerExecutorConfigurationOutputTypeDef(BaseValidatorModel):
    pollingAccounts: Optional[List[str]] = None
    pollingServicePrincipals: Optional[List[str]] = None


class LambdaExecutorConfigurationTypeDef(BaseValidatorModel):
    lambdaFunctionArn: str


class JobWorkerExecutorConfigurationTypeDef(BaseValidatorModel):
    pollingAccounts: Optional[Sequence[str]] = None
    pollingServicePrincipals: Optional[Sequence[str]] = None


class RetryConfigurationTypeDef(BaseValidatorModel):
    retryMode: Optional[StageRetryModeType] = None


class GetActionTypeInputTypeDef(BaseValidatorModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str


class GetJobDetailsInputTypeDef(BaseValidatorModel):
    jobId: str


class GetPipelineExecutionInputTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str


class GetPipelineInputTypeDef(BaseValidatorModel):
    name: str
    version: Optional[int] = None


class PipelineMetadataTypeDef(BaseValidatorModel):
    pipelineArn: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    pollingDisabledAt: Optional[datetime] = None


class GetPipelineStateInputTypeDef(BaseValidatorModel):
    name: str


class GetThirdPartyJobDetailsInputTypeDef(BaseValidatorModel):
    jobId: str
    clientToken: str


class GitBranchFilterCriteriaOutputTypeDef(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitBranchFilterCriteriaTypeDef(BaseValidatorModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None


class GitFilePathFilterCriteriaOutputTypeDef(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitFilePathFilterCriteriaTypeDef(BaseValidatorModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None


class GitTagFilterCriteriaOutputTypeDef(BaseValidatorModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None


class GitTagFilterCriteriaTypeDef(BaseValidatorModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListActionTypesInputTypeDef(BaseValidatorModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    nextToken: Optional[str] = None
    regionFilter: Optional[str] = None


class ListPipelinesInputTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PipelineSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[int] = None
    pipelineType: Optional[PipelineTypeType] = None
    executionMode: Optional[ExecutionModeType] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None


class ListRuleTypesInputTypeDef(BaseValidatorModel):
    ruleOwnerFilter: Optional[Literal["AWS"]] = None
    regionFilter: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListWebhooksInputTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class OverrideStageConditionInputTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    conditionType: ConditionTypeType


class StageContextTypeDef(BaseValidatorModel):
    name: Optional[str] = None


class PipelineVariableDeclarationTypeDef(BaseValidatorModel):
    name: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None


class SucceededInStageFilterTypeDef(BaseValidatorModel):
    stageName: Optional[str] = None


class PipelineRollbackMetadataTypeDef(BaseValidatorModel):
    rollbackTargetPipelineExecutionId: Optional[str] = None


class SourceRevisionTypeDef(BaseValidatorModel):
    actionName: str
    revisionId: Optional[str] = None
    revisionSummary: Optional[str] = None
    revisionUrl: Optional[str] = None


class StopExecutionTriggerTypeDef(BaseValidatorModel):
    reason: Optional[str] = None


class ResolvedPipelineVariableTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    resolvedValue: Optional[str] = None


class PipelineVariableTypeDef(BaseValidatorModel):
    name: str
    value: str


class ThirdPartyJobTypeDef(BaseValidatorModel):
    clientId: Optional[str] = None
    jobId: Optional[str] = None


class RegisterWebhookWithThirdPartyInputTypeDef(BaseValidatorModel):
    webhookName: Optional[str] = None


class RetryStageExecutionInputTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    retryMode: StageRetryModeType


class RetryStageMetadataTypeDef(BaseValidatorModel):
    autoStageRetryAttempt: Optional[int] = None
    manualStageRetryAttempt: Optional[int] = None
    latestRetryTrigger: Optional[RetryTriggerType] = None


class RollbackStageInputTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    targetPipelineExecutionId: str


class RuleTypeIdTypeDef(BaseValidatorModel):
    category: Literal["Rule"]
    provider: str
    owner: Optional[Literal["AWS"]] = None
    version: Optional[str] = None


class RuleRevisionTypeDef(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: datetime


class RuleTypeSettingsTypeDef(BaseValidatorModel):
    thirdPartyConfigurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None


class SourceRevisionOverrideTypeDef(BaseValidatorModel):
    actionName: str
    revisionType: SourceRevisionTypeType
    revisionValue: str


class StageConditionsExecutionTypeDef(BaseValidatorModel):
    status: Optional[ConditionExecutionStatusType] = None
    summary: Optional[str] = None


class TransitionStateTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    lastChangedBy: Optional[str] = None
    lastChangedAt: Optional[datetime] = None
    disabledReason: Optional[str] = None


class StopPipelineExecutionInputTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str
    abandon: Optional[bool] = None
    reason: Optional[str] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class WebhookAuthConfigurationTypeDef(BaseValidatorModel):
    AllowedIPRange: Optional[str] = None
    SecretToken: Optional[str] = None


class WebhookFilterRuleTypeDef(BaseValidatorModel):
    jsonPath: str
    matchEquals: Optional[str] = None


class AcknowledgeJobOutputTypeDef(BaseValidatorModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class AcknowledgeThirdPartyJobOutputTypeDef(BaseValidatorModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class PutActionRevisionOutputTypeDef(BaseValidatorModel):
    newRevision: bool
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutApprovalResultOutputTypeDef(BaseValidatorModel):
    approvedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class RetryStageExecutionOutputTypeDef(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class RollbackStageOutputTypeDef(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartPipelineExecutionOutputTypeDef(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopPipelineExecutionOutputTypeDef(BaseValidatorModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PollForJobsInputTypeDef(BaseValidatorModel):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: Optional[int] = None
    queryParam: Optional[Mapping[str, str]] = None


class PollForThirdPartyJobsInputTypeDef(BaseValidatorModel):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: Optional[int] = None


class ActionDeclarationOutputTypeDef(BaseValidatorModel):
    name: str
    actionTypeId: ActionTypeIdTypeDef
    runOrder: Optional[int] = None
    configuration: Optional[Dict[str, str]] = None
    commands: Optional[List[str]] = None
    outputArtifacts: Optional[List[OutputArtifactOutputTypeDef]] = None
    inputArtifacts: Optional[List[InputArtifactTypeDef]] = None
    outputVariables: Optional[List[str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    namespace: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    environmentVariables: Optional[List[EnvironmentVariableTypeDef]] = None


class ActionDeclarationTypeDef(BaseValidatorModel):
    name: str
    actionTypeId: ActionTypeIdTypeDef
    runOrder: Optional[int] = None
    configuration: Optional[Mapping[str, str]] = None
    commands: Optional[Sequence[str]] = None
    outputArtifacts: Optional[Sequence[OutputArtifactTypeDef]] = None
    inputArtifacts: Optional[Sequence[InputArtifactTypeDef]] = None
    outputVariables: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    namespace: Optional[str] = None
    timeoutInMinutes: Optional[int] = None
    environmentVariables: Optional[Sequence[EnvironmentVariableTypeDef]] = None


class ActionExecutionFilterTypeDef(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilterTypeDef] = None


class RuleExecutionFilterTypeDef(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilterTypeDef] = None


class ActionExecutionResultTypeDef(BaseValidatorModel):
    externalExecutionId: Optional[str] = None
    externalExecutionSummary: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetailsTypeDef] = None
    logStreamARN: Optional[str] = None


class ActionExecutionTypeDef(BaseValidatorModel):
    actionExecutionId: Optional[str] = None
    status: Optional[ActionExecutionStatusType] = None
    summary: Optional[str] = None
    lastStatusChange: Optional[datetime] = None
    token: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    externalExecutionId: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    percentComplete: Optional[int] = None
    errorDetails: Optional[ErrorDetailsTypeDef] = None
    logStreamARN: Optional[str] = None


class RuleExecutionResultTypeDef(BaseValidatorModel):
    externalExecutionId: Optional[str] = None
    externalExecutionSummary: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetailsTypeDef] = None


class RuleExecutionTypeDef(BaseValidatorModel):
    ruleExecutionId: Optional[str] = None
    status: Optional[RuleExecutionStatusType] = None
    summary: Optional[str] = None
    lastStatusChange: Optional[datetime] = None
    token: Optional[str] = None
    lastUpdatedBy: Optional[str] = None
    externalExecutionId: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetailsTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ActionRevisionTypeDef(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: TimestampTypeDef


class CurrentRevisionTypeDef(BaseValidatorModel):
    revision: str
    changeIdentifier: str
    created: Optional[TimestampTypeDef] = None
    revisionSummary: Optional[str] = None


class PutApprovalResultInputTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    result: ApprovalResultTypeDef
    token: str


class ArtifactDetailTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    s3location: Optional[S3LocationTypeDef] = None


class ActionConfigurationPropertyTypeDef(BaseValidatorModel):
    pass


class CreateCustomActionTypeInputTypeDef(BaseValidatorModel):
    category: ActionCategoryType
    provider: str
    version: str
    inputArtifactDetails: ArtifactDetailsTypeDef
    outputArtifactDetails: ArtifactDetailsTypeDef
    settings: Optional[ActionTypeSettingsTypeDef] = None
    configurationProperties: Optional[Sequence[ActionConfigurationPropertyTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class ExecutorConfigurationOutputTypeDef(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfigurationTypeDef] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationOutputTypeDef] = None


class ExecutorConfigurationTypeDef(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfigurationTypeDef] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationTypeDef] = None


class FailureDetailsTypeDef(BaseValidatorModel):
    pass


class PutJobFailureResultInputTypeDef(BaseValidatorModel):
    jobId: str
    failureDetails: FailureDetailsTypeDef


class PutThirdPartyJobFailureResultInputTypeDef(BaseValidatorModel):
    jobId: str
    clientToken: str
    failureDetails: FailureDetailsTypeDef


class GitPullRequestFilterOutputTypeDef(BaseValidatorModel):
    events: Optional[List[GitPullRequestEventTypeType]] = None
    branches: Optional[GitBranchFilterCriteriaOutputTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaOutputTypeDef] = None


class GitPullRequestFilterTypeDef(BaseValidatorModel):
    events: Optional[Sequence[GitPullRequestEventTypeType]] = None
    branches: Optional[GitBranchFilterCriteriaTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaTypeDef] = None


class GitPushFilterOutputTypeDef(BaseValidatorModel):
    tags: Optional[GitTagFilterCriteriaOutputTypeDef] = None
    branches: Optional[GitBranchFilterCriteriaOutputTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaOutputTypeDef] = None


class GitPushFilterTypeDef(BaseValidatorModel):
    tags: Optional[GitTagFilterCriteriaTypeDef] = None
    branches: Optional[GitBranchFilterCriteriaTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaTypeDef] = None


class ListActionTypesInputPaginateTypeDef(BaseValidatorModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    regionFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPipelinesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceInputPaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWebhooksInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPipelinesOutputTypeDef(BaseValidatorModel):
    pipelines: List[PipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PipelineContextTypeDef(BaseValidatorModel):
    pipelineName: Optional[str] = None
    stage: Optional[StageContextTypeDef] = None
    action: Optional[ActionContextTypeDef] = None
    pipelineArn: Optional[str] = None
    pipelineExecutionId: Optional[str] = None


class PipelineExecutionFilterTypeDef(BaseValidatorModel):
    succeededInStage: Optional[SucceededInStageFilterTypeDef] = None


class PipelineExecutionSummaryTypeDef(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    status: Optional[PipelineExecutionStatusType] = None
    statusSummary: Optional[str] = None
    startTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    sourceRevisions: Optional[List[SourceRevisionTypeDef]] = None
    trigger: Optional[ExecutionTriggerTypeDef] = None
    stopTrigger: Optional[StopExecutionTriggerTypeDef] = None
    executionMode: Optional[ExecutionModeType] = None
    executionType: Optional[ExecutionTypeType] = None
    rollbackMetadata: Optional[PipelineRollbackMetadataTypeDef] = None


class PipelineExecutionTypeDef(BaseValidatorModel):
    pipelineName: Optional[str] = None
    pipelineVersion: Optional[int] = None
    pipelineExecutionId: Optional[str] = None
    status: Optional[PipelineExecutionStatusType] = None
    statusSummary: Optional[str] = None
    artifactRevisions: Optional[List[ArtifactRevisionTypeDef]] = None
    variables: Optional[List[ResolvedPipelineVariableTypeDef]] = None
    trigger: Optional[ExecutionTriggerTypeDef] = None
    executionMode: Optional[ExecutionModeType] = None
    executionType: Optional[ExecutionTypeType] = None
    rollbackMetadata: Optional[PipelineRollbackMetadataTypeDef] = None


class PollForThirdPartyJobsOutputTypeDef(BaseValidatorModel):
    jobs: List[ThirdPartyJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RuleDeclarationOutputTypeDef(BaseValidatorModel):
    name: str
    ruleTypeId: RuleTypeIdTypeDef
    configuration: Optional[Dict[str, str]] = None
    commands: Optional[List[str]] = None
    inputArtifacts: Optional[List[InputArtifactTypeDef]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    timeoutInMinutes: Optional[int] = None


class RuleDeclarationTypeDef(BaseValidatorModel):
    name: str
    ruleTypeId: RuleTypeIdTypeDef
    configuration: Optional[Mapping[str, str]] = None
    commands: Optional[Sequence[str]] = None
    inputArtifacts: Optional[Sequence[InputArtifactTypeDef]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    timeoutInMinutes: Optional[int] = None


class StartPipelineExecutionInputTypeDef(BaseValidatorModel):
    name: str
    variables: Optional[Sequence[PipelineVariableTypeDef]] = None
    clientRequestToken: Optional[str] = None
    sourceRevisions: Optional[Sequence[SourceRevisionOverrideTypeDef]] = None


class WebhookDefinitionOutputTypeDef(BaseValidatorModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: List[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef


class WebhookDefinitionTypeDef(BaseValidatorModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: Sequence[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef


class ActionStateTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    currentRevision: Optional[ActionRevisionOutputTypeDef] = None
    latestExecution: Optional[ActionExecutionTypeDef] = None
    entityUrl: Optional[str] = None
    revisionUrl: Optional[str] = None


class RuleExecutionOutputTypeDef(BaseValidatorModel):
    executionResult: Optional[RuleExecutionResultTypeDef] = None


class RuleStateTypeDef(BaseValidatorModel):
    ruleName: Optional[str] = None
    currentRevision: Optional[RuleRevisionTypeDef] = None
    latestExecution: Optional[RuleExecutionTypeDef] = None
    entityUrl: Optional[str] = None
    revisionUrl: Optional[str] = None


class PutJobSuccessResultInputTypeDef(BaseValidatorModel):
    jobId: str
    currentRevision: Optional[CurrentRevisionTypeDef] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetailsTypeDef] = None
    outputVariables: Optional[Mapping[str, str]] = None


class PutThirdPartyJobSuccessResultInputTypeDef(BaseValidatorModel):
    jobId: str
    clientToken: str
    currentRevision: Optional[CurrentRevisionTypeDef] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetailsTypeDef] = None


class ActionTypeTypeDef(BaseValidatorModel):
    pass


class CreateCustomActionTypeOutputTypeDef(BaseValidatorModel):
    actionType: ActionTypeTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListActionTypesOutputTypeDef(BaseValidatorModel):
    actionTypes: List[ActionTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ActionExecutionInputTypeDef(BaseValidatorModel):
    actionTypeId: Optional[ActionTypeIdTypeDef] = None
    configuration: Optional[Dict[str, str]] = None
    resolvedConfiguration: Optional[Dict[str, str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    inputArtifacts: Optional[List[ArtifactDetailTypeDef]] = None
    namespace: Optional[str] = None


class ActionExecutionOutputTypeDef(BaseValidatorModel):
    outputArtifacts: Optional[List[ArtifactDetailTypeDef]] = None
    executionResult: Optional[ActionExecutionResultTypeDef] = None
    outputVariables: Optional[Dict[str, str]] = None


class RuleExecutionInputTypeDef(BaseValidatorModel):
    ruleTypeId: Optional[RuleTypeIdTypeDef] = None
    configuration: Optional[Dict[str, str]] = None
    resolvedConfiguration: Optional[Dict[str, str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    inputArtifacts: Optional[List[ArtifactDetailTypeDef]] = None


class ArtifactLocationTypeDef(BaseValidatorModel):
    pass


class ArtifactTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    revision: Optional[str] = None
    location: Optional[ArtifactLocationTypeDef] = None


class GitConfigurationOutputTypeDef(BaseValidatorModel):
    sourceActionName: str
    push: Optional[List[GitPushFilterOutputTypeDef]] = None
    pullRequest: Optional[List[GitPullRequestFilterOutputTypeDef]] = None


class GitConfigurationTypeDef(BaseValidatorModel):
    sourceActionName: str
    push: Optional[Sequence[GitPushFilterTypeDef]] = None
    pullRequest: Optional[Sequence[GitPullRequestFilterTypeDef]] = None


class ListPipelineExecutionsOutputTypeDef(BaseValidatorModel):
    pipelineExecutionSummaries: List[PipelineExecutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetPipelineExecutionOutputTypeDef(BaseValidatorModel):
    pipelineExecution: PipelineExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ConditionOutputTypeDef(BaseValidatorModel):
    result: Optional[ResultType] = None
    rules: Optional[List[RuleDeclarationOutputTypeDef]] = None


class ConditionTypeDef(BaseValidatorModel):
    result: Optional[ResultType] = None
    rules: Optional[Sequence[RuleDeclarationTypeDef]] = None


class RuleTypeTypeDef(BaseValidatorModel):
    pass


class ListRuleTypesOutputTypeDef(BaseValidatorModel):
    ruleTypes: List[RuleTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListWebhookItemTypeDef(BaseValidatorModel):
    definition: WebhookDefinitionOutputTypeDef
    url: str
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None
    lastTriggered: Optional[datetime] = None
    arn: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None


class ConditionStateTypeDef(BaseValidatorModel):
    latestExecution: Optional[ConditionExecutionTypeDef] = None
    ruleStates: Optional[List[RuleStateTypeDef]] = None


class ActionRevisionUnionTypeDef(BaseValidatorModel):
    pass


class PutActionRevisionInputTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    actionRevision: ActionRevisionUnionTypeDef


class EncryptionKeyTypeDef(BaseValidatorModel):
    pass


class JobDataTypeDef(BaseValidatorModel):
    actionTypeId: Optional[ActionTypeIdTypeDef] = None
    actionConfiguration: Optional[ActionConfigurationTypeDef] = None
    pipelineContext: Optional[PipelineContextTypeDef] = None
    inputArtifacts: Optional[List[ArtifactTypeDef]] = None
    outputArtifacts: Optional[List[ArtifactTypeDef]] = None
    artifactCredentials: Optional[AWSSessionCredentialsTypeDef] = None
    continuationToken: Optional[str] = None
    encryptionKey: Optional[EncryptionKeyTypeDef] = None


class ThirdPartyJobDataTypeDef(BaseValidatorModel):
    actionTypeId: Optional[ActionTypeIdTypeDef] = None
    actionConfiguration: Optional[ActionConfigurationTypeDef] = None
    pipelineContext: Optional[PipelineContextTypeDef] = None
    inputArtifacts: Optional[List[ArtifactTypeDef]] = None
    outputArtifacts: Optional[List[ArtifactTypeDef]] = None
    artifactCredentials: Optional[AWSSessionCredentialsTypeDef] = None
    continuationToken: Optional[str] = None
    encryptionKey: Optional[EncryptionKeyTypeDef] = None


class PipelineTriggerDeclarationOutputTypeDef(BaseValidatorModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationOutputTypeDef


class PipelineTriggerDeclarationTypeDef(BaseValidatorModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationTypeDef


class BeforeEntryConditionsOutputTypeDef(BaseValidatorModel):
    conditions: List[ConditionOutputTypeDef]


class FailureConditionsOutputTypeDef(BaseValidatorModel):
    result: Optional[ResultType] = None
    retryConfiguration: Optional[RetryConfigurationTypeDef] = None
    conditions: Optional[List[ConditionOutputTypeDef]] = None


class SuccessConditionsOutputTypeDef(BaseValidatorModel):
    conditions: List[ConditionOutputTypeDef]


class BeforeEntryConditionsTypeDef(BaseValidatorModel):
    conditions: Sequence[ConditionTypeDef]


class FailureConditionsTypeDef(BaseValidatorModel):
    result: Optional[ResultType] = None
    retryConfiguration: Optional[RetryConfigurationTypeDef] = None
    conditions: Optional[Sequence[ConditionTypeDef]] = None


class SuccessConditionsTypeDef(BaseValidatorModel):
    conditions: Sequence[ConditionTypeDef]


class ListWebhooksOutputTypeDef(BaseValidatorModel):
    webhooks: List[ListWebhookItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutWebhookOutputTypeDef(BaseValidatorModel):
    webhook: ListWebhookItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class WebhookDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class PutWebhookInputTypeDef(BaseValidatorModel):
    webhook: WebhookDefinitionUnionTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None


class StageConditionStateTypeDef(BaseValidatorModel):
    latestExecution: Optional[StageConditionsExecutionTypeDef] = None
    conditionStates: Optional[List[ConditionStateTypeDef]] = None


class ActionExecutionDetailTypeDef(BaseValidatorModel):
    pass


class ListActionExecutionsOutputTypeDef(BaseValidatorModel):
    actionExecutionDetails: List[ActionExecutionDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RuleExecutionDetailTypeDef(BaseValidatorModel):
    pass


class ListRuleExecutionsOutputTypeDef(BaseValidatorModel):
    ruleExecutionDetails: List[RuleExecutionDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ActionTypeDeclarationOutputTypeDef(BaseValidatorModel):
    pass


class GetActionTypeOutputTypeDef(BaseValidatorModel):
    actionType: ActionTypeDeclarationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BlockerDeclarationTypeDef(BaseValidatorModel):
    pass


class StageDeclarationOutputTypeDef(BaseValidatorModel):
    name: str
    actions: List[ActionDeclarationOutputTypeDef]
    blockers: Optional[List[BlockerDeclarationTypeDef]] = None
    onFailure: Optional[FailureConditionsOutputTypeDef] = None
    onSuccess: Optional[SuccessConditionsOutputTypeDef] = None
    beforeEntry: Optional[BeforeEntryConditionsOutputTypeDef] = None


class StageDeclarationTypeDef(BaseValidatorModel):
    name: str
    actions: Sequence[ActionDeclarationTypeDef]
    blockers: Optional[Sequence[BlockerDeclarationTypeDef]] = None
    onFailure: Optional[FailureConditionsTypeDef] = None
    onSuccess: Optional[SuccessConditionsTypeDef] = None
    beforeEntry: Optional[BeforeEntryConditionsTypeDef] = None


class StageExecutionTypeDef(BaseValidatorModel):
    pass


class StageStateTypeDef(BaseValidatorModel):
    stageName: Optional[str] = None
    inboundExecution: Optional[StageExecutionTypeDef] = None
    inboundExecutions: Optional[List[StageExecutionTypeDef]] = None
    inboundTransitionState: Optional[TransitionStateTypeDef] = None
    actionStates: Optional[List[ActionStateTypeDef]] = None
    latestExecution: Optional[StageExecutionTypeDef] = None
    beforeEntryConditionState: Optional[StageConditionStateTypeDef] = None
    onSuccessConditionState: Optional[StageConditionStateTypeDef] = None
    onFailureConditionState: Optional[StageConditionStateTypeDef] = None
    retryStageMetadata: Optional[RetryStageMetadataTypeDef] = None


class JobDetailsTypeDef(BaseValidatorModel):
    pass


class GetJobDetailsOutputTypeDef(BaseValidatorModel):
    jobDetails: JobDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JobTypeDef(BaseValidatorModel):
    pass


class PollForJobsOutputTypeDef(BaseValidatorModel):
    jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ThirdPartyJobDetailsTypeDef(BaseValidatorModel):
    pass


class GetThirdPartyJobDetailsOutputTypeDef(BaseValidatorModel):
    jobDetails: ThirdPartyJobDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ActionTypeDeclarationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateActionTypeInputTypeDef(BaseValidatorModel):
    actionType: ActionTypeDeclarationUnionTypeDef


class ArtifactStoreTypeDef(BaseValidatorModel):
    pass


class PipelineDeclarationOutputTypeDef(BaseValidatorModel):
    name: str
    roleArn: str
    stages: List[StageDeclarationOutputTypeDef]
    artifactStore: Optional[ArtifactStoreTypeDef] = None
    artifactStores: Optional[Dict[str, ArtifactStoreTypeDef]] = None
    version: Optional[int] = None
    executionMode: Optional[ExecutionModeType] = None
    pipelineType: Optional[PipelineTypeType] = None
    variables: Optional[List[PipelineVariableDeclarationTypeDef]] = None
    triggers: Optional[List[PipelineTriggerDeclarationOutputTypeDef]] = None


class PipelineDeclarationTypeDef(BaseValidatorModel):
    name: str
    roleArn: str
    stages: Sequence[StageDeclarationTypeDef]
    artifactStore: Optional[ArtifactStoreTypeDef] = None
    artifactStores: Optional[Mapping[str, ArtifactStoreTypeDef]] = None
    version: Optional[int] = None
    executionMode: Optional[ExecutionModeType] = None
    pipelineType: Optional[PipelineTypeType] = None
    variables: Optional[Sequence[PipelineVariableDeclarationTypeDef]] = None
    triggers: Optional[Sequence[PipelineTriggerDeclarationTypeDef]] = None


class GetPipelineStateOutputTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineVersion: int
    stageStates: List[StageStateTypeDef]
    created: datetime
    updated: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePipelineOutputTypeDef(BaseValidatorModel):
    pipeline: PipelineDeclarationOutputTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetPipelineOutputTypeDef(BaseValidatorModel):
    pipeline: PipelineDeclarationOutputTypeDef
    metadata: PipelineMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePipelineOutputTypeDef(BaseValidatorModel):
    pipeline: PipelineDeclarationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PipelineDeclarationUnionTypeDef(BaseValidatorModel):
    pass


class CreatePipelineInputTypeDef(BaseValidatorModel):
    pipeline: PipelineDeclarationUnionTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdatePipelineInputTypeDef(BaseValidatorModel):
    pipeline: PipelineDeclarationUnionTypeDef


