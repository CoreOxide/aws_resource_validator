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
from aws_resource_validator.pydantic_models.codepipeline_constants import *

class AWSSessionCredentialsTypeDef(BaseValidatorModel):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str

class AcknowledgeJobInputRequestTypeDef(BaseValidatorModel):
    jobId: str
    nonce: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AcknowledgeThirdPartyJobInputRequestTypeDef(BaseValidatorModel):
    jobId: str
    nonce: str
    clientToken: str

class ActionConfigurationPropertyTypeDef(BaseValidatorModel):
    name: str
    required: bool
    key: bool
    secret: bool
    queryable: Optional[bool] = None
    description: Optional[str] = None
    type: Optional[ActionConfigurationPropertyTypeType] = None

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

class InputArtifactTypeDef(BaseValidatorModel):
    name: str

class OutputArtifactTypeDef(BaseValidatorModel):
    name: str

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

class EncryptionKeyTypeDef(BaseValidatorModel):
    id: str
    type: Literal["KMS"]

class BlockerDeclarationTypeDef(BaseValidatorModel):
    name: str
    type: Literal["Schedule"]

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class DeleteCustomActionTypeInputRequestTypeDef(BaseValidatorModel):
    category: ActionCategoryType
    provider: str
    version: str

class DeletePipelineInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteWebhookInputRequestTypeDef(BaseValidatorModel):
    name: str

class DeregisterWebhookWithThirdPartyInputRequestTypeDef(BaseValidatorModel):
    webhookName: Optional[str] = None

class DisableStageTransitionInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    transitionType: StageTransitionTypeType
    reason: str

class EnableStageTransitionInputRequestTypeDef(BaseValidatorModel):
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

class FailureConditionsTypeDef(BaseValidatorModel):
    result: Optional[Literal["ROLLBACK"]] = None

class FailureDetailsTypeDef(BaseValidatorModel):
    type: FailureTypeType
    message: str
    externalExecutionId: Optional[str] = None

class GetActionTypeInputRequestTypeDef(BaseValidatorModel):
    category: ActionCategoryType
    owner: str
    provider: str
    version: str

class GetJobDetailsInputRequestTypeDef(BaseValidatorModel):
    jobId: str

class GetPipelineExecutionInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str

class GetPipelineInputRequestTypeDef(BaseValidatorModel):
    name: str
    version: Optional[int] = None

class PipelineMetadataTypeDef(BaseValidatorModel):
    pipelineArn: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None
    pollingDisabledAt: Optional[datetime] = None

class GetPipelineStateInputRequestTypeDef(BaseValidatorModel):
    name: str

class GetThirdPartyJobDetailsInputRequestTypeDef(BaseValidatorModel):
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

class ListActionTypesInputRequestTypeDef(BaseValidatorModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    nextToken: Optional[str] = None
    regionFilter: Optional[str] = None

class ListPipelinesInputRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PipelineSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[int] = None
    pipelineType: Optional[PipelineTypeType] = None
    executionMode: Optional[ExecutionModeType] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListWebhooksInputRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

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

class RegisterWebhookWithThirdPartyInputRequestTypeDef(BaseValidatorModel):
    webhookName: Optional[str] = None

class RetryStageExecutionInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    pipelineExecutionId: str
    retryMode: StageRetryModeType

class RollbackStageInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    targetPipelineExecutionId: str

class SourceRevisionOverrideTypeDef(BaseValidatorModel):
    actionName: str
    revisionType: SourceRevisionTypeType
    revisionValue: str

class StageExecutionTypeDef(BaseValidatorModel):
    pipelineExecutionId: str
    status: StageExecutionStatusType
    type: Optional[ExecutionTypeType] = None

class TransitionStateTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    lastChangedBy: Optional[str] = None
    lastChangedAt: Optional[datetime] = None
    disabledReason: Optional[str] = None

class StopPipelineExecutionInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineExecutionId: str
    abandon: Optional[bool] = None
    reason: Optional[str] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
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

class PollForJobsInputRequestTypeDef(BaseValidatorModel):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: Optional[int] = None
    queryParam: Optional[Mapping[str, str]] = None

class PollForThirdPartyJobsInputRequestTypeDef(BaseValidatorModel):
    actionTypeId: ActionTypeIdTypeDef
    maxBatchSize: Optional[int] = None

class ActionDeclarationOutputTypeDef(BaseValidatorModel):
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

class ActionDeclarationTypeDef(BaseValidatorModel):
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

class ActionExecutionFilterTypeDef(BaseValidatorModel):
    pipelineExecutionId: Optional[str] = None
    latestInPipelineExecution: Optional[LatestInPipelineExecutionFilterTypeDef] = None

class ActionExecutionResultTypeDef(BaseValidatorModel):
    externalExecutionId: Optional[str] = None
    externalExecutionSummary: Optional[str] = None
    externalExecutionUrl: Optional[str] = None
    errorDetails: Optional[ErrorDetailsTypeDef] = None

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

class ActionRevisionTypeDef(BaseValidatorModel):
    revisionId: str
    revisionChangeId: str
    created: TimestampTypeDef

class CurrentRevisionTypeDef(BaseValidatorModel):
    revision: str
    changeIdentifier: str
    created: Optional[TimestampTypeDef] = None
    revisionSummary: Optional[str] = None

class ActionTypeTypeDef(BaseValidatorModel):
    id: ActionTypeIdTypeDef
    inputArtifactDetails: ArtifactDetailsTypeDef
    outputArtifactDetails: ArtifactDetailsTypeDef
    settings: Optional[ActionTypeSettingsTypeDef] = None
    actionConfigurationProperties: Optional[List[ActionConfigurationPropertyTypeDef]] = None

class PutApprovalResultInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    result: ApprovalResultTypeDef
    token: str

class ArtifactDetailTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    s3location: Optional[S3LocationTypeDef] = None

class ArtifactLocationTypeDef(BaseValidatorModel):
    type: Optional[Literal["S3"]] = None
    s3Location: Optional[S3ArtifactLocationTypeDef] = None

class ArtifactStoreTypeDef(BaseValidatorModel):
    type: Literal["S3"]
    location: str
    encryptionKey: Optional[EncryptionKeyTypeDef] = None

class CreateCustomActionTypeInputRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class ExecutorConfigurationOutputTypeDef(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfigurationTypeDef] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationOutputTypeDef] = None

class ExecutorConfigurationTypeDef(BaseValidatorModel):
    lambdaExecutorConfiguration: Optional[LambdaExecutorConfigurationTypeDef] = None
    jobWorkerExecutorConfiguration: Optional[JobWorkerExecutorConfigurationTypeDef] = None

class PutJobFailureResultInputRequestTypeDef(BaseValidatorModel):
    jobId: str
    failureDetails: FailureDetailsTypeDef

class PutThirdPartyJobFailureResultInputRequestTypeDef(BaseValidatorModel):
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

class ListActionTypesInputListActionTypesPaginateTypeDef(BaseValidatorModel):
    actionOwnerFilter: Optional[ActionOwnerType] = None
    regionFilter: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesInputListPipelinesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceInputListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    resourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWebhooksInputListWebhooksPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelinesOutputTypeDef(BaseValidatorModel):
    pipelines: List[PipelineSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class StartPipelineExecutionInputRequestTypeDef(BaseValidatorModel):
    name: str
    variables: Optional[Sequence[PipelineVariableTypeDef]] = None
    clientRequestToken: Optional[str] = None
    sourceRevisions: Optional[Sequence[SourceRevisionOverrideTypeDef]] = None

class WebhookDefinitionExtraOutputTypeDef(BaseValidatorModel):
    name: str
    targetPipeline: str
    targetAction: str
    filters: List[WebhookFilterRuleTypeDef]
    authentication: WebhookAuthenticationTypeType
    authenticationConfiguration: WebhookAuthConfigurationTypeDef

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

class StageDeclarationOutputTypeDef(BaseValidatorModel):
    name: str
    actions: List[ActionDeclarationOutputTypeDef]
    blockers: Optional[List[BlockerDeclarationTypeDef]] = None
    onFailure: Optional[FailureConditionsTypeDef] = None

class StageDeclarationTypeDef(BaseValidatorModel):
    name: str
    actions: Sequence[ActionDeclarationTypeDef]
    blockers: Optional[Sequence[BlockerDeclarationTypeDef]] = None
    onFailure: Optional[FailureConditionsTypeDef] = None

class ListActionExecutionsInputListActionExecutionsPaginateTypeDef(BaseValidatorModel):
    pipelineName: str
    filter: Optional[ActionExecutionFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListActionExecutionsInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    filter: Optional[ActionExecutionFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ActionStateTypeDef(BaseValidatorModel):
    actionName: Optional[str] = None
    currentRevision: Optional[ActionRevisionOutputTypeDef] = None
    latestExecution: Optional[ActionExecutionTypeDef] = None
    entityUrl: Optional[str] = None
    revisionUrl: Optional[str] = None

class PutActionRevisionInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    stageName: str
    actionName: str
    actionRevision: ActionRevisionTypeDef

class PutJobSuccessResultInputRequestTypeDef(BaseValidatorModel):
    jobId: str
    currentRevision: Optional[CurrentRevisionTypeDef] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetailsTypeDef] = None
    outputVariables: Optional[Mapping[str, str]] = None

class PutThirdPartyJobSuccessResultInputRequestTypeDef(BaseValidatorModel):
    jobId: str
    clientToken: str
    currentRevision: Optional[CurrentRevisionTypeDef] = None
    continuationToken: Optional[str] = None
    executionDetails: Optional[ExecutionDetailsTypeDef] = None

class CreateCustomActionTypeOutputTypeDef(BaseValidatorModel):
    actionType: ActionTypeTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListActionTypesOutputTypeDef(BaseValidatorModel):
    actionTypes: List[ActionTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ArtifactTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    revision: Optional[str] = None
    location: Optional[ArtifactLocationTypeDef] = None

class ActionTypeExecutorOutputTypeDef(BaseValidatorModel):
    configuration: ExecutorConfigurationOutputTypeDef
    type: ExecutorTypeType
    policyStatementsTemplate: Optional[str] = None
    jobTimeout: Optional[int] = None

class ActionTypeExecutorTypeDef(BaseValidatorModel):
    configuration: ExecutorConfigurationTypeDef
    type: ExecutorTypeType
    policyStatementsTemplate: Optional[str] = None
    jobTimeout: Optional[int] = None

class GitConfigurationOutputTypeDef(BaseValidatorModel):
    sourceActionName: str
    push: Optional[List[GitPushFilterOutputTypeDef]] = None
    pullRequest: Optional[List[GitPullRequestFilterOutputTypeDef]] = None

class GitConfigurationTypeDef(BaseValidatorModel):
    sourceActionName: str
    push: Optional[Sequence[GitPushFilterTypeDef]] = None
    pullRequest: Optional[Sequence[GitPullRequestFilterTypeDef]] = None

class ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef(BaseValidatorModel):
    pipelineName: str
    filter: Optional[PipelineExecutionFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPipelineExecutionsInputRequestTypeDef(BaseValidatorModel):
    pipelineName: str
    maxResults: Optional[int] = None
    filter: Optional[PipelineExecutionFilterTypeDef] = None
    nextToken: Optional[str] = None

class ListPipelineExecutionsOutputTypeDef(BaseValidatorModel):
    pipelineExecutionSummaries: List[PipelineExecutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineExecutionOutputTypeDef(BaseValidatorModel):
    pipelineExecution: PipelineExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebhookItemTypeDef(BaseValidatorModel):
    definition: WebhookDefinitionOutputTypeDef
    url: str
    errorMessage: Optional[str] = None
    errorCode: Optional[str] = None
    lastTriggered: Optional[datetime] = None
    arn: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None

class PutWebhookInputRequestTypeDef(BaseValidatorModel):
    webhook: WebhookDefinitionTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class StageStateTypeDef(BaseValidatorModel):
    stageName: Optional[str] = None
    inboundExecution: Optional[StageExecutionTypeDef] = None
    inboundExecutions: Optional[List[StageExecutionTypeDef]] = None
    inboundTransitionState: Optional[TransitionStateTypeDef] = None
    actionStates: Optional[List[ActionStateTypeDef]] = None
    latestExecution: Optional[StageExecutionTypeDef] = None

class ActionExecutionDetailTypeDef(BaseValidatorModel):
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

class ActionTypeDeclarationOutputTypeDef(BaseValidatorModel):
    executor: ActionTypeExecutorOutputTypeDef
    id: ActionTypeIdentifierTypeDef
    inputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    outputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    description: Optional[str] = None
    permissions: Optional[ActionTypePermissionsOutputTypeDef] = None
    properties: Optional[List[ActionTypePropertyTypeDef]] = None
    urls: Optional[ActionTypeUrlsTypeDef] = None

class ActionTypeDeclarationTypeDef(BaseValidatorModel):
    executor: ActionTypeExecutorTypeDef
    id: ActionTypeIdentifierTypeDef
    inputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    outputArtifactDetails: ActionTypeArtifactDetailsTypeDef
    description: Optional[str] = None
    permissions: Optional[ActionTypePermissionsTypeDef] = None
    properties: Optional[Sequence[ActionTypePropertyTypeDef]] = None
    urls: Optional[ActionTypeUrlsTypeDef] = None

class PipelineTriggerDeclarationOutputTypeDef(BaseValidatorModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationOutputTypeDef

class PipelineTriggerDeclarationTypeDef(BaseValidatorModel):
    providerType: Literal["CodeStarSourceConnection"]
    gitConfiguration: GitConfigurationTypeDef

class ListWebhooksOutputTypeDef(BaseValidatorModel):
    webhooks: List[ListWebhookItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutWebhookOutputTypeDef(BaseValidatorModel):
    webhook: ListWebhookItemTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPipelineStateOutputTypeDef(BaseValidatorModel):
    pipelineName: str
    pipelineVersion: int
    stageStates: List[StageStateTypeDef]
    created: datetime
    updated: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListActionExecutionsOutputTypeDef(BaseValidatorModel):
    actionExecutionDetails: List[ActionExecutionDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class JobDetailsTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    data: Optional[JobDataTypeDef] = None
    accountId: Optional[str] = None

class JobTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    data: Optional[JobDataTypeDef] = None
    nonce: Optional[str] = None
    accountId: Optional[str] = None

class ThirdPartyJobDetailsTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    data: Optional[ThirdPartyJobDataTypeDef] = None
    nonce: Optional[str] = None

class GetActionTypeOutputTypeDef(BaseValidatorModel):
    actionType: ActionTypeDeclarationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActionTypeInputRequestTypeDef(BaseValidatorModel):
    actionType: ActionTypeDeclarationTypeDef

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

class GetJobDetailsOutputTypeDef(BaseValidatorModel):
    jobDetails: JobDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PollForJobsOutputTypeDef(BaseValidatorModel):
    jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetThirdPartyJobDetailsOutputTypeDef(BaseValidatorModel):
    jobDetails: ThirdPartyJobDetailsTypeDef
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

class CreatePipelineInputRequestTypeDef(BaseValidatorModel):
    pipeline: PipelineDeclarationTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdatePipelineInputRequestTypeDef(BaseValidatorModel):
    pipeline: PipelineDeclarationTypeDef

