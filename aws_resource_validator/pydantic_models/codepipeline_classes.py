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
from aws_resource_validator.pydantic_models.codepipeline_constants import *

class AWSSessionCredentialsTypeDef(BaseModel):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str

class AcknowledgeJobInputRequestTypeDef(BaseModel):
    jobId: str
    nonce: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AcknowledgeThirdPartyJobInputRequestTypeDef(BaseModel):
    jobId: str
    nonce: str
    clientToken: str

class ActionConfigurationPropertyTypeDef(BaseModel):
    name: str
    required: bool
    key: bool
    secret: bool
    queryable: Optional[bool] = None
    description: Optional[str] = None
    type: Optional[ActionConfigurationPropertyTypeType] = None

class ActionConfigurationTypeDef(BaseModel):
    configuration: Optional[Dict[str, str]] = None

class ActionContextTypeDef(BaseModel):
    name: Optional[str] = None
    actionExecutionId: Optional[str] = None

class ActionTypeIdTypeDef(BaseModel):
    category: ActionCategoryType
    owner: ActionOwnerType
    provider: str
    version: str

class InputArtifactTypeDef(BaseModel):
    name: str

class OutputArtifactTypeDef(BaseModel):
    name: str

class LatestInPipelineExecutionFilterTypeDef(BaseModel):
    pipelineExecutionId: str
    startTimeRange: StartTimeRangeType

class ErrorDetailsTypeDef(BaseModel):
    code: Optional[str] = None
    message: Optional[str] = None

class ActionRevisionOutputTypeDef(BaseModel):
    revisionId: str
    revisionChangeId: str
    created: datetime

class ActionTypeArtifactDetailsTypeDef(BaseModel):
    minimumCount: int
    maximumCount: int

class ActionTypeIdentifierTypeDef(BaseModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str

class ActionTypePermissionsOutputTypeDef(BaseModel):
    allowedAccounts: List[str]

class ActionTypePropertyTypeDef(BaseModel):
    name: str
    optional: bool
    key: bool
    noEcho: bool
    queryable: Optional[bool] = None
    description: Optional[str] = None

class ActionTypeUrlsTypeDef(BaseModel):
    configurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None

class ActionTypePermissionsTypeDef(BaseModel):
    allowedAccounts: Sequence[str]

class ActionTypeSettingsTypeDef(BaseModel):
    thirdPartyConfigurationUrl: Optional[str] = None
    entityUrlTemplate: Optional[str] = None
    executionUrlTemplate: Optional[str] = None
    revisionUrlTemplate: Optional[str] = None

class ArtifactDetailsTypeDef(BaseModel):
    minimumCount: int
    maximumCount: int

class ApprovalResultTypeDef(BaseModel):
    summary: str
    status: ApprovalStatusType

class S3LocationTypeDef(BaseModel):
    bucket: Optional[str] = None
    key: Optional[str] = None

class S3ArtifactLocationTypeDef(BaseModel):
    bucketName: str
    objectKey: str

class ArtifactRevisionTypeDef(BaseModel):
    name: Optional[str] = None
    revisionId: Optional[str] = None
    revisionChangeIdentifier: Optional[str] = None
    revisionSummary: Optional[str] = None
    created: Optional[datetime] = None
    revisionUrl: Optional[str] = None

class EncryptionKeyTypeDef(BaseModel):
    id: str
    type: Literal["KMS"]

class BlockerDeclarationTypeDef(BaseModel):
    name: str
    type: Literal["Schedule"]

class TagTypeDef(BaseModel):
    key: str
    value: str

class DeleteCustomActionTypeInputRequestTypeDef(BaseModel):
    category: ActionCategoryType
    provider: str
    version: str

class DeletePipelineInputRequestTypeDef(BaseModel):
    name: str

class DeleteWebhookInputRequestTypeDef(BaseModel):
    name: str

class DeregisterWebhookWithThirdPartyInputRequestTypeDef(BaseModel):
    webhookName: Optional[str] = None

class DisableStageTransitionInputRequestTypeDef(BaseModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType
    reason: str

class EnableStageTransitionInputRequestTypeDef(BaseModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType

class ExecutionDetailsTypeDef(BaseModel):
    summary: Optional[str] = None
    externalExecutionId: Optional[str] = None
    percentComplete: Optional[int] = None

class ExecutionTriggerTypeDef(BaseModel):
    triggerType: Optional[TriggerTypeType] = None
    triggerDetail: Optional[str] = None

class JobWorkerExecutorConfigurationOutputTypeDef(BaseModel):
    pollingAccounts: Optional[List[str]] = None
    pollingServicePrincipals: Optional[List[str]] = None

class LambdaExecutorConfigurationTypeDef(BaseModel):
    lambdaFunctionArn: str

class JobWorkerExecutorConfigurationTypeDef(BaseModel):
    pollingAccounts: Optional[Sequence[str]] = None
    pollingServicePrincipals: Optional[Sequence[str]] = None

class FailureConditionsTypeDef(BaseModel):
    result: Optional[Literal["ROLLBACK"]] = None

class FailureDetailsTypeDef(BaseModel):
    type: FailureTypeType
    message: str
    externalExecutionId: Optional[str] = None

class GetActionTypeInputRequestTypeDef(BaseModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str

class GetJobDetailsInputRequestTypeDef(BaseModel):
    jobId: str

class GetPipelineExecutionInputRequestTypeDef(BaseModel):
    pipelineName: str
    pipelineExecutionId: str

class GetPipelineInputRequestTypeDef(BaseModel):
    name: str
    version: Optional[int] = None

class PipelineMetadataTypeDef(BaseModel):
    pipelineArn: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    pollingDisabledAt: Optional[datetime] = None

class GetPipelineStateInputRequestTypeDef(BaseModel):
    name: str

class GetThirdPartyJobDetailsInputRequestTypeDef(BaseModel):
    jobId: str
    clientToken: str

class GitBranchFilterCriteriaOutputTypeDef(BaseModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None

class GitBranchFilterCriteriaTypeDef(BaseModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None

class GitFilePathFilterCriteriaOutputTypeDef(BaseModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None

class GitFilePathFilterCriteriaTypeDef(BaseModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None

class GitTagFilterCriteriaOutputTypeDef(BaseModel):
    includes: Optional[List[str]] = None
    excludes: Optional[List[str]] = None

class GitTagFilterCriteriaTypeDef(BaseModel):
    includes: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListActionTypesInputRequestTypeDef(BaseModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    nextToken: Optional[str] = None
    regionFilter: Optional[str] = None

class ListPipelinesInputRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PipelineSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    version: Optional[int] = None
    pipelineType: Optional[PipelineTypeType] = None
    executionMode: Optional[ExecutionModeType] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListWebhooksInputRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StageContextTypeDef(BaseModel):
    name: Optional[str] = None

class PipelineVariableDeclarationTypeDef(BaseModel):
    name: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None

class SucceededInStageFilterTypeDef(BaseModel):
    stageName: Optional[str] = None

class PipelineRollbackMetadataTypeDef(BaseModel):
    rollbackTargetPipelineExecutionId: Optional[str] = None

class SourceRevisionTypeDef(BaseModel):
    actionName: str
    revisionId: Optional[str] = None
    revisionSummary: Optional[str] = None
    revisionUrl: Optional[str] = None

class StopExecutionTriggerTypeDef(BaseModel):
    reason: Optional[str] = None

class ResolvedPipelineVariableTypeDef(BaseModel):
    name: Optional[str] = None
    resolvedValue: Optional[str] = None

class PipelineVariableTypeDef(BaseModel):
    name: str
    value: str

class ThirdPartyJobTypeDef(BaseModel):
    clientId: Optional[str] = None
    jobId: Optional[str] = None

class RegisterWebhookWithThirdPartyInputRequestTypeDef(BaseModel):
    webhookName: Optional[str] = None

class RetryStageExecutionInputRequestTypeDef(BaseModel):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    retryMode: StageRetryModeType

class RollbackStageInputRequestTypeDef(BaseModel):
    pipelineName: str
    stageName: str
    targetPipelineExecutionId: str

class SourceRevisionOverrideTypeDef(BaseModel):
    actionName: str
    revisionType: SourceRevisionTypeType
    revisionValue: str

class StageExecutionTypeDef(BaseModel):
    pipelineExecutionId: str
    status: StageExecutionStatusType
    type: Optional[ExecutionTypeType] = None

class TransitionStateTypeDef(BaseModel):
    enabled: Optional[bool] = None
    lastChangedBy: Optional[str] = None
    lastChangedAt: Optional[datetime] = None
    disabledReason: Optional[str] = None

class StopPipelineExecutionInputRequestTypeDef(BaseModel):
    pipelineName: str
    pipelineExecutionId: str
    abandon: Optional[bool] = None
    reason: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class WebhookAuthConfigurationTypeDef(BaseModel):
    AllowedIPRange: Optional[str] = None
    SecretToken: Optional[str] = None

class WebhookFilterRuleTypeDef(BaseModel):
    jsonPath: str
    matchEquals: Optional[str] = None

class AcknowledgeJobOutputTypeDef(BaseModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class AcknowledgeThirdPartyJobOutputTypeDef(BaseModel):
    status: JobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class PutActionRevisionOutputTypeDef(BaseModel):
    newRevision: bool
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutApprovalResultOutputTypeDef(BaseModel):
    approvedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class RetryStageExecutionOutputTypeDef(BaseModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RollbackStageOutputTypeDef(BaseModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineExecutionOutputTypeDef(BaseModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopPipelineExecutionOutputTypeDef(BaseModel):
    pipelineExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PollForJobsInputRequestTypeDef(BaseModel):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: Optional[int] = None
    queryParam: Optional[Mapping[str, str]] = None

class PollForThirdPartyJobsInputRequestTypeDef(BaseModel):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: Optional[int] = None

class ActionDeclarationOutputTypeDef(BaseModel):
    name: str
    actionTypeId: ActionTypeIdTypeDef
    runOrder: Optional[int] = None
    configuration: Optional[Dict[str, str]] = None
    outputArtifacts: Optional[List[OutputArtifactTypeDef]] = None
    inputArtifacts: Optional[List[InputArtifactTypeDef]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    namespace: Optional[str] = None
    timeoutInMinutes: Optional[int] = None

class ActionDeclarationTypeDef(BaseModel):
    name: str
    actionTypeId: ActionTypeIdTypeDef
    runOrder: Optional[int] = None
    configuration: Optional[Mapping[str, str]] = None
    outputArtifacts: Optional[Sequence[OutputArtifactTypeDef]] = None
    inputArtifacts: Optional[Sequence[InputArtifactTypeDef]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    namespace: Optional[str] = None
    timeoutInMinutes: Optional[int] = None

class ActionExecutionFilterTypeDef(BaseModel):
    pipelineExecutionId: Optional[str] = None
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilterTypeDef] = None

class ActionExecutionResultTypeDef(BaseModel):
    externalExecutionId: Optional[str] = None
    externalExecutionSummary: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetailsTypeDef] = None

class ActionExecutionTypeDef(BaseModel):
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

class ActionRevisionTypeDef(BaseModel):
    revisionId: str
    revisionChangeId: str
    created: TimestampTypeDef

class CurrentRevisionTypeDef(BaseModel):
    revision: str
    changeIdentifier: str
    created: Optional[TimestampTypeDef] = None
    revisionSummary: Optional[str] = None

class ActionTypeTypeDef(BaseModel):
    id: ActionTypeIdTypeDef
    inputArtifactDetails: ArtifactDetailsTypeDef
    outputArtifactDetails: ArtifactDetailsTypeDef
    settings: Optional[ActionTypeSettingsTypeDef] = None
    actionConfigurationProperties: Optional[List[ActionConfigurationPropertyTypeDef]] = None

class PutApprovalResultInputRequestTypeDef(BaseModel):
    pipelineName: str
    stageName: str
    actionName: str
    result: ApprovalResultTypeDef
    token: str

class ArtifactDetailTypeDef(BaseModel):
    name: Optional[str] = None
    s3location: Optional[S3LocationTypeDef] = None

class ArtifactLocationTypeDef(BaseModel):
    type: Optional[Literal["S3"]] = None
    s3Location: Optional[S3ArtifactLocationTypeDef] = None

class ArtifactStoreTypeDef(BaseModel):
    type: Literal["S3"]
    location: str
    encryptionKey: Optional[EncryptionKeyTypeDef] = None

class CreateCustomActionTypeInputRequestTypeDef(BaseModel):
    category: ActionCategoryType
    provider: str
    version: str
    inputArtifactDetails: ArtifactDetailsTypeDef
    outputArtifactDetails: ArtifactDetailsTypeDef
    settings: Optional[ActionTypeSettingsTypeDef] = None
    configurationProperties: Optional[Sequence[ActionConfigurationPropertyTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceOutputTypeDef(BaseModel):
    tags: List[TagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class ExecutorConfigurationOutputTypeDef(BaseModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfigurationTypeDef] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationOutputTypeDef] = None

class ExecutorConfigurationTypeDef(BaseModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfigurationTypeDef] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationTypeDef] = None

class PutJobFailureResultInputRequestTypeDef(BaseModel):
    jobId: str
    failureDetails: FailureDetailsTypeDef

class PutThirdPartyJobFailureResultInputRequestTypeDef(BaseModel):
    jobId: str
    clientToken: str
    failureDetails: FailureDetailsTypeDef

class GitPullRequestFilterOutputTypeDef(BaseModel):
    events: Optional[List[GitPullRequestEventTypeType]] = None
    branches: Optional[GitBranchFilterCriteriaOutputTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaOutputTypeDef] = None

class GitPullRequestFilterTypeDef(BaseModel):
    events: Optional[Sequence[GitPullRequestEventTypeType]] = None
    branches: Optional[GitBranchFilterCriteriaTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaTypeDef] = None

class GitPushFilterOutputTypeDef(BaseModel):
    tags: Optional[GitTagFilterCriteriaOutputTypeDef] = None
    branches: Optional[GitBranchFilterCriteriaOutputTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaOutputTypeDef] = None

class GitPushFilterTypeDef(BaseModel):
    tags: Optional[GitTagFilterCriteriaTypeDef] = None
    branches: Optional[GitBranchFilterCriteriaTypeDef] = None
    filePaths: Optional[GitFilePathFilterCriteriaTypeDef] = None

class ListActionTypesInputListActionTypesPaginateTypeDef(BaseModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    regionFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesInputListPipelinesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWebhooksInputListWebhooksPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesOutputTypeDef(BaseModel):
    pipelines: List[PipelineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PipelineContextTypeDef(BaseModel):
    pipelineName: Optional[str] = None
    stage: Optional[StageContextTypeDef] = None
    action: Optional[ActionContextTypeDef] = None
    pipelineArn: Optional[str] = None
    pipelineExecutionId: Optional[str] = None

class PipelineExecutionFilterTypeDef(BaseModel):
    succeededInStage: Optional[SucceededInStageFilterTypeDef] = None

class PipelineExecutionSummaryTypeDef(BaseModel):
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

class PipelineExecutionTypeDef(BaseModel):
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

class PollForThirdPartyJobsOutputTypeDef(BaseModel):
    jobs: List[ThirdPartyJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartPipelineExecutionInputRequestTypeDef(BaseModel):
    name: str
    variables: Optional[Sequence[PipelineVariableTypeDef]] = None
    clientRequestToken: Optional[str] = None
    sourceRevisions: Optional[Sequence[SourceRevisionOverrideTypeDef]] = None

class WebhookDefinitionExtraOutputTypeDef(BaseModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: List[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef

class WebhookDefinitionOutputTypeDef(BaseModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: List[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef

class WebhookDefinitionTypeDef(BaseModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: Sequence[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef

class StageDeclarationOutputTypeDef(BaseModel):
    name: str
    actions: List[ActionDeclarationOutputTypeDef]
    blockers: Optional[List[BlockerDeclarationTypeDef]] = None
    onFailure: Optional[FailureConditionsTypeDef] = None

class StageDeclarationTypeDef(BaseModel):
    name: str
    actions: Sequence[ActionDeclarationTypeDef]
    blockers: Optional[Sequence[BlockerDeclarationTypeDef]] = None
    onFailure: Optional[FailureConditionsTypeDef] = None

class ListActionExecutionsInputListActionExecutionsPaginateTypeDef(BaseModel):
    pipelineName: str
    filter: Optional[ActionExecutionFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListActionExecutionsInputRequestTypeDef(BaseModel):
    pipelineName: str
    filter: Optional[ActionExecutionFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ActionStateTypeDef(BaseModel):
    actionName: Optional[str] = None
    currentRevision: Optional[ActionRevisionOutputTypeDef] = None
    latestExecution: Optional[ActionExecutionTypeDef] = None
    entityUrl: Optional[str] = None
    revisionUrl: Optional[str] = None

class PutActionRevisionInputRequestTypeDef(BaseModel):
    pipelineName: str
    stageName: str
    actionName: str
    actionRevision: ActionRevisionTypeDef

class PutJobSuccessResultInputRequestTypeDef(BaseModel):
    jobId: str
    currentRevision: Optional[CurrentRevisionTypeDef] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetailsTypeDef] = None
    outputVariables: Optional[Mapping[str, str]] = None

class PutThirdPartyJobSuccessResultInputRequestTypeDef(BaseModel):
    jobId: str
    clientToken: str
    currentRevision: Optional[CurrentRevisionTypeDef] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetailsTypeDef] = None

class CreateCustomActionTypeOutputTypeDef(BaseModel):
    actionType: ActionTypeTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListActionTypesOutputTypeDef(BaseModel):
    actionTypes: List[ActionTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ActionExecutionInputTypeDef(BaseModel):
    actionTypeId: Optional[ActionTypeIdTypeDef] = None
    configuration: Optional[Dict[str, str]] = None
    resolvedConfiguration: Optional[Dict[str, str]] = None
    roleArn: Optional[str] = None
    region: Optional[str] = None
    inputArtifacts: Optional[List[ArtifactDetailTypeDef]] = None
    namespace: Optional[str] = None

class ActionExecutionOutputTypeDef(BaseModel):
    outputArtifacts: Optional[List[ArtifactDetailTypeDef]] = None
    executionResult: Optional[ActionExecutionResultTypeDef] = None
    outputVariables: Optional[Dict[str, str]] = None

class ArtifactTypeDef(BaseModel):
    name: Optional[str] = None
    revision: Optional[str] = None
    location: Optional[ArtifactLocationTypeDef] = None

class ActionTypeExecutorOutputTypeDef(BaseModel):
    configuration: ExecutorConfigurationOutputTypeDef
    type: ExecutorTypeType
    policyStatementsTemplate: Optional[str] = None
    jobTimeout: Optional[int] = None

class ActionTypeExecutorTypeDef(BaseModel):
    configuration: ExecutorConfigurationTypeDef
    type: ExecutorTypeType
    policyStatementsTemplate: Optional[str] = None
    jobTimeout: Optional[int] = None

class GitConfigurationOutputTypeDef(BaseModel):
    sourceActionName: str
    push: Optional[List[GitPushFilterOutputTypeDef]] = None
    pullRequest: Optional[List[GitPullRequestFilterOutputTypeDef]] = None

class GitConfigurationTypeDef(BaseModel):
    sourceActionName: str
    push: Optional[Sequence[GitPushFilterTypeDef]] = None
    pullRequest: Optional[Sequence[GitPullRequestFilterTypeDef]] = None

class ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef(BaseModel):
    pipelineName: str
    filter: Optional[PipelineExecutionFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelineExecutionsInputRequestTypeDef(BaseModel):
    pipelineName: str
    maxResults: Optional[int] = None
    filter: Optional[PipelineExecutionFilterTypeDef] = None
    nextToken: Optional[str] = None

class ListPipelineExecutionsOutputTypeDef(BaseModel):
    pipelineExecutionSummaries: List[PipelineExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineExecutionOutputTypeDef(BaseModel):
    pipelineExecution: PipelineExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebhookItemTypeDef(BaseModel):
    definition: WebhookDefinitionOutputTypeDef
    url: str
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None
    lastTriggered: Optional[datetime] = None
    arn: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None

class PutWebhookInputRequestTypeDef(BaseModel):
    webhook: WebhookDefinitionTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class StageStateTypeDef(BaseModel):
    stageName: Optional[str] = None
    inboundExecution: Optional[StageExecutionTypeDef] = None
    inboundExecutions: Optional[List[StageExecutionTypeDef]] = None
    inboundTransitionState: Optional[TransitionStateTypeDef] = None
    actionStates: Optional[List[ActionStateTypeDef]] = None
    latestExecution: Optional[StageExecutionTypeDef] = None

class ActionExecutionDetailTypeDef(BaseModel):
    pipelineExecutionId: Optional[str] = None
    actionExecutionId: Optional[str] = None
    pipelineVersion: Optional[int] = None
    stageName: Optional[str] = None
    actionName: Optional[str] = None
    startTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    updatedBy: Optional[str] = None
    status: Optional[ActionExecutionStatusType] = None
    input: Optional[ActionExecutionInputTypeDef] = None
    output: Optional[ActionExecutionOutputTypeDef] = None

class JobDataTypeDef(BaseModel):
    actionTypeId: Optional[ActionTypeIdTypeDef] = None
    actionConfiguration: Optional[ActionConfigurationTypeDef] = None
    pipelineContext: Optional[PipelineContextTypeDef] = None
    inputArtifacts: Optional[List[ArtifactTypeDef]] = None
    outputArtifacts: Optional[List[ArtifactTypeDef]] = None
    artifactCredentials: Optional[AWSSessionCredentialsTypeDef] = None
    continuationToken: Optional[str] = None
    encryptionKey: Optional[EncryptionKeyTypeDef] = None

class ThirdPartyJobDataTypeDef(BaseModel):
    actionTypeId: Optional[ActionTypeIdTypeDef] = None
    actionConfiguration: Optional[ActionConfigurationTypeDef] = None
    pipelineContext: Optional[PipelineContextTypeDef] = None
    inputArtifacts: Optional[List[ArtifactTypeDef]] = None
    outputArtifacts: Optional[List[ArtifactTypeDef]] = None
    artifactCredentials: Optional[AWSSessionCredentialsTypeDef] = None
    continuationToken: Optional[str] = None
    encryptionKey: Optional[EncryptionKeyTypeDef] = None

class ActionTypeDeclarationOutputTypeDef(BaseModel):
    executor: ActionTypeExecutorOutputTypeDef
    id: ActionTypeIdentifierTypeDef
    inputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    outputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    description: Optional[str] = None
    permissions: Optional[ActionTypePermissionsOutputTypeDef] = None
    properties: Optional[List[ActionTypePropertyTypeDef]] = None
    urls: Optional[ActionTypeUrlsTypeDef] = None

class ActionTypeDeclarationTypeDef(BaseModel):
    executor: ActionTypeExecutorTypeDef
    id: ActionTypeIdentifierTypeDef
    inputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    outputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    description: Optional[str] = None
    permissions: Optional[ActionTypePermissionsTypeDef] = None
    properties: Optional[Sequence[ActionTypePropertyTypeDef]] = None
    urls: Optional[ActionTypeUrlsTypeDef] = None

class PipelineTriggerDeclarationOutputTypeDef(BaseModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationOutputTypeDef

class PipelineTriggerDeclarationTypeDef(BaseModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationTypeDef

class ListWebhooksOutputTypeDef(BaseModel):
    webhooks: List[ListWebhookItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutWebhookOutputTypeDef(BaseModel):
    webhook: ListWebhookItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineStateOutputTypeDef(BaseModel):
    pipelineName: str
    pipelineVersion: int
    stageStates: List[StageStateTypeDef]
    created: datetime
    updated: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListActionExecutionsOutputTypeDef(BaseModel):
    actionExecutionDetails: List[ActionExecutionDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobDetailsTypeDef(BaseModel):
    id: Optional[str] = None
    data: Optional[JobDataTypeDef] = None
    accountId: Optional[str] = None

class JobTypeDef(BaseModel):
    id: Optional[str] = None
    data: Optional[JobDataTypeDef] = None
    nonce: Optional[str] = None
    accountId: Optional[str] = None

class ThirdPartyJobDetailsTypeDef(BaseModel):
    id: Optional[str] = None
    data: Optional[ThirdPartyJobDataTypeDef] = None
    nonce: Optional[str] = None

class GetActionTypeOutputTypeDef(BaseModel):
    actionType: ActionTypeDeclarationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActionTypeInputRequestTypeDef(BaseModel):
    actionType: ActionTypeDeclarationTypeDef

class PipelineDeclarationOutputTypeDef(BaseModel):
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

class PipelineDeclarationTypeDef(BaseModel):
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

class GetJobDetailsOutputTypeDef(BaseModel):
    jobDetails: JobDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PollForJobsOutputTypeDef(BaseModel):
    jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetThirdPartyJobDetailsOutputTypeDef(BaseModel):
    jobDetails: ThirdPartyJobDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipelineOutputTypeDef(BaseModel):
    pipeline: PipelineDeclarationOutputTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineOutputTypeDef(BaseModel):
    pipeline: PipelineDeclarationOutputTypeDef
    metadata: PipelineMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePipelineOutputTypeDef(BaseModel):
    pipeline: PipelineDeclarationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePipelineInputRequestTypeDef(BaseModel):
    pipeline: PipelineDeclarationTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdatePipelineInputRequestTypeDef(BaseModel):
    pipeline: PipelineDeclarationTypeDef

