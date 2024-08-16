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
from aws_resource_validator.pydantic_models.fis_constants import *

class ActionParameterTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    required: Optional[bool] = None

class ActionTargetTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None

class CreateExperimentTemplateActionInputTypeDef(BaseValidatorModel):
    actionId: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None
    targets: Optional[Mapping[str, str]] = None
    startAfter: Optional[Sequence[str]] = None

class CreateExperimentTemplateExperimentOptionsInputTypeDef(BaseValidatorModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None

class ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef(BaseValidatorModel):
    logGroupArn: str

class ExperimentTemplateS3LogConfigurationInputTypeDef(BaseValidatorModel):
    bucketName: str
    prefix: Optional[str] = None

class CreateExperimentTemplateStopConditionInputTypeDef(BaseValidatorModel):
    source: str
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ExperimentTemplateTargetInputFilterTypeDef(BaseValidatorModel):
    path: str
    values: Sequence[str]

class CreateTargetAccountConfigurationRequestRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class TargetAccountConfigurationTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class DeleteExperimentTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteTargetAccountConfigurationRequestRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str

class ExperimentActionStateTypeDef(BaseValidatorModel):
    status: Optional[ExperimentActionStatusType] = None
    reason: Optional[str] = None

class ExperimentCloudWatchLogsLogConfigurationTypeDef(BaseValidatorModel):
    logGroupArn: Optional[str] = None

class ExperimentS3LogConfigurationTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None

class ExperimentOptionsTypeDef(BaseValidatorModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None
    actionsMode: Optional[ActionsModeType] = None

class ExperimentStateTypeDef(BaseValidatorModel):
    status: Optional[ExperimentStatusType] = None
    reason: Optional[str] = None

class ExperimentStopConditionTypeDef(BaseValidatorModel):
    source: Optional[str] = None
    value: Optional[str] = None

class ExperimentTargetAccountConfigurationSummaryTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class ExperimentTargetAccountConfigurationTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class ExperimentTargetFilterTypeDef(BaseValidatorModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None

class ExperimentTemplateActionTypeDef(BaseValidatorModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None

class ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef(BaseValidatorModel):
    logGroupArn: Optional[str] = None

class ExperimentTemplateExperimentOptionsTypeDef(BaseValidatorModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None

class ExperimentTemplateS3LogConfigurationTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None

class ExperimentTemplateStopConditionTypeDef(BaseValidatorModel):
    source: Optional[str] = None
    value: Optional[str] = None

class ExperimentTemplateSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class ExperimentTemplateTargetFilterTypeDef(BaseValidatorModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None

class GetActionRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetExperimentRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetExperimentTargetAccountConfigurationRequestRequestTypeDef(BaseValidatorModel):
    experimentId: str
    accountId: str

class GetExperimentTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetTargetAccountConfigurationRequestRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str

class GetTargetResourceTypeRequestRequestTypeDef(BaseValidatorModel):
    resourceType: str

class ListActionsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExperimentResolvedTargetsRequestRequestTypeDef(BaseValidatorModel):
    experimentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetName: Optional[str] = None

class ResolvedTargetTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    targetName: Optional[str] = None
    targetInformation: Optional[Dict[str, str]] = None

class ListExperimentTargetAccountConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    experimentId: str
    nextToken: Optional[str] = None

class ListExperimentTemplatesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExperimentsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    experimentTemplateId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTargetAccountConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TargetAccountConfigurationSummaryTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class ListTargetResourceTypesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TargetResourceTypeSummaryTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None

class StartExperimentExperimentOptionsInputTypeDef(BaseValidatorModel):
    actionsMode: Optional[ActionsModeType] = None

class StopExperimentRequestRequestTypeDef(BaseValidatorModel):
    id: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TargetResourceTypeParameterTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    required: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Optional[Sequence[str]] = None

class UpdateExperimentTemplateActionInputItemTypeDef(BaseValidatorModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None
    targets: Optional[Mapping[str, str]] = None
    startAfter: Optional[Sequence[str]] = None

class UpdateExperimentTemplateExperimentOptionsInputTypeDef(BaseValidatorModel):
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None

class UpdateExperimentTemplateStopConditionInputTypeDef(BaseValidatorModel):
    source: str
    value: Optional[str] = None

class UpdateTargetAccountConfigurationRequestRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str
    roleArn: Optional[str] = None
    description: Optional[str] = None

class ActionSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    targets: Optional[Dict[str, ActionTargetTypeDef]] = None
    tags: Optional[Dict[str, str]] = None

class ActionTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, ActionParameterTypeDef]] = None
    targets: Optional[Dict[str, ActionTargetTypeDef]] = None
    tags: Optional[Dict[str, str]] = None

class CreateExperimentTemplateLogConfigurationInputTypeDef(BaseValidatorModel):
    logSchemaVersion: int
    cloudWatchLogsConfiguration: Optional[       ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef     ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInputTypeDef] = None

class UpdateExperimentTemplateLogConfigurationInputTypeDef(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[       ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef     ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInputTypeDef] = None
    logSchemaVersion: Optional[int] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateTargetInputTypeDef(BaseValidatorModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[Sequence[str]] = None
    resourceTags: Optional[Mapping[str, str]] = None
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilterTypeDef]] = None
    parameters: Optional[Mapping[str, str]] = None

class UpdateExperimentTemplateTargetInputTypeDef(BaseValidatorModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[Sequence[str]] = None
    resourceTags: Optional[Mapping[str, str]] = None
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilterTypeDef]] = None
    parameters: Optional[Mapping[str, str]] = None

class CreateTargetAccountConfigurationResponseTypeDef(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTargetAccountConfigurationResponseTypeDef(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTargetAccountConfigurationResponseTypeDef(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTargetAccountConfigurationResponseTypeDef(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentActionTypeDef(BaseValidatorModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None
    state: Optional[ExperimentActionStateTypeDef] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class ExperimentLogConfigurationTypeDef(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[ExperimentCloudWatchLogsLogConfigurationTypeDef] = None
    s3Configuration: Optional[ExperimentS3LogConfigurationTypeDef] = None
    logSchemaVersion: Optional[int] = None

class ExperimentSummaryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    experimentTemplateId: Optional[str] = None
    state: Optional[ExperimentStateTypeDef] = None
    creationTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    experimentOptions: Optional[ExperimentOptionsTypeDef] = None

class ListExperimentTargetAccountConfigurationsResponseTypeDef(BaseValidatorModel):
    targetAccountConfigurations: List[ExperimentTargetAccountConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentTargetAccountConfigurationResponseTypeDef(BaseValidatorModel):
    targetAccountConfiguration: ExperimentTargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTargetTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTargetFilterTypeDef]] = None
    selectionMode: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None

class ExperimentTemplateLogConfigurationTypeDef(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[       ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef     ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationTypeDef] = None
    logSchemaVersion: Optional[int] = None

class ListExperimentTemplatesResponseTypeDef(BaseValidatorModel):
    experimentTemplates: List[ExperimentTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTemplateTargetTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTemplateTargetFilterTypeDef]] = None
    selectionMode: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None

class ListExperimentResolvedTargetsResponseTypeDef(BaseValidatorModel):
    resolvedTargets: List[ResolvedTargetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetAccountConfigurationsResponseTypeDef(BaseValidatorModel):
    targetAccountConfigurations: List[TargetAccountConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetResourceTypesResponseTypeDef(BaseValidatorModel):
    targetResourceTypes: List[TargetResourceTypeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExperimentRequestRequestTypeDef(BaseValidatorModel):
    clientToken: str
    experimentTemplateId: str
    experimentOptions: Optional[StartExperimentExperimentOptionsInputTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class TargetResourceTypeTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, TargetResourceTypeParameterTypeDef]] = None

class ListActionsResponseTypeDef(BaseValidatorModel):
    actions: List[ActionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetActionResponseTypeDef(BaseValidatorModel):
    action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateRequestRequestTypeDef(BaseValidatorModel):
    clientToken: str
    description: str
    stopConditions: Sequence[CreateExperimentTemplateStopConditionInputTypeDef]
    actions: Mapping[str, CreateExperimentTemplateActionInputTypeDef]
    roleArn: str
    targets: Optional[Mapping[str, CreateExperimentTemplateTargetInputTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    logConfiguration: Optional[CreateExperimentTemplateLogConfigurationInputTypeDef] = None
    experimentOptions: Optional[CreateExperimentTemplateExperimentOptionsInputTypeDef] = None

class UpdateExperimentTemplateRequestRequestTypeDef(BaseValidatorModel):
    id: str
    description: Optional[str] = None
    stopConditions: Optional[Sequence[UpdateExperimentTemplateStopConditionInputTypeDef]] = None
    targets: Optional[Mapping[str, UpdateExperimentTemplateTargetInputTypeDef]] = None
    actions: Optional[Mapping[str, UpdateExperimentTemplateActionInputItemTypeDef]] = None
    roleArn: Optional[str] = None
    logConfiguration: Optional[UpdateExperimentTemplateLogConfigurationInputTypeDef] = None
    experimentOptions: Optional[UpdateExperimentTemplateExperimentOptionsInputTypeDef] = None

class ListExperimentsResponseTypeDef(BaseValidatorModel):
    experiments: List[ExperimentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    experimentTemplateId: Optional[str] = None
    roleArn: Optional[str] = None
    state: Optional[ExperimentStateTypeDef] = None
    targets: Optional[Dict[str, ExperimentTargetTypeDef]] = None
    actions: Optional[Dict[str, ExperimentActionTypeDef]] = None
    stopConditions: Optional[List[ExperimentStopConditionTypeDef]] = None
    creationTime: Optional[datetime] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    logConfiguration: Optional[ExperimentLogConfigurationTypeDef] = None
    experimentOptions: Optional[ExperimentOptionsTypeDef] = None
    targetAccountConfigurationsCount: Optional[int] = None

class ExperimentTemplateTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    targets: Optional[Dict[str, ExperimentTemplateTargetTypeDef]] = None
    actions: Optional[Dict[str, ExperimentTemplateActionTypeDef]] = None
    stopConditions: Optional[List[ExperimentTemplateStopConditionTypeDef]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    logConfiguration: Optional[ExperimentTemplateLogConfigurationTypeDef] = None
    experimentOptions: Optional[ExperimentTemplateExperimentOptionsTypeDef] = None
    targetAccountConfigurationsCount: Optional[int] = None

class GetTargetResourceTypeResponseTypeDef(BaseValidatorModel):
    targetResourceType: TargetResourceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateResponseTypeDef(BaseValidatorModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExperimentTemplateResponseTypeDef(BaseValidatorModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentTemplateResponseTypeDef(BaseValidatorModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExperimentTemplateResponseTypeDef(BaseValidatorModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

