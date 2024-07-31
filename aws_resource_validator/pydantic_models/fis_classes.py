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
from aws_resource_validator.pydantic_models.fis_constants import *

class ActionParameterTypeDef(BaseModel):
    description: Optional[str] = None
    required: Optional[bool] = None

class ActionTargetTypeDef(BaseModel):
    resourceType: Optional[str] = None

class CreateExperimentTemplateActionInputTypeDef(BaseModel):
    actionId: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None
    targets: Optional[Mapping[str, str]] = None
    startAfter: Optional[Sequence[str]] = None

class CreateExperimentTemplateExperimentOptionsInputTypeDef(BaseModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None

class ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef(BaseModel):
    logGroupArn: str

class ExperimentTemplateS3LogConfigurationInputTypeDef(BaseModel):
    bucketName: str
    prefix: Optional[str] = None

class CreateExperimentTemplateStopConditionInputTypeDef(BaseModel):
    source: str
    value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ExperimentTemplateTargetInputFilterTypeDef(BaseModel):
    path: str
    values: Sequence[str]

class CreateTargetAccountConfigurationRequestRequestTypeDef(BaseModel):
    experimentTemplateId: str
    accountId: str
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None

class TargetAccountConfigurationTypeDef(BaseModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class DeleteExperimentTemplateRequestRequestTypeDef(BaseModel):
    id: str

class DeleteTargetAccountConfigurationRequestRequestTypeDef(BaseModel):
    experimentTemplateId: str
    accountId: str

class ExperimentActionStateTypeDef(BaseModel):
    status: Optional[ExperimentActionStatusType] = None
    reason: Optional[str] = None

class ExperimentCloudWatchLogsLogConfigurationTypeDef(BaseModel):
    logGroupArn: Optional[str] = None

class ExperimentS3LogConfigurationTypeDef(BaseModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None

class ExperimentOptionsTypeDef(BaseModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None
    actionsMode: Optional[ActionsModeType] = None

class ExperimentStateTypeDef(BaseModel):
    status: Optional[ExperimentStatusType] = None
    reason: Optional[str] = None

class ExperimentStopConditionTypeDef(BaseModel):
    source: Optional[str] = None
    value: Optional[str] = None

class ExperimentTargetAccountConfigurationSummaryTypeDef(BaseModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class ExperimentTargetAccountConfigurationTypeDef(BaseModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class ExperimentTargetFilterTypeDef(BaseModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None

class ExperimentTemplateActionTypeDef(BaseModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None

class ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef(BaseModel):
    logGroupArn: Optional[str] = None

class ExperimentTemplateExperimentOptionsTypeDef(BaseModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None

class ExperimentTemplateS3LogConfigurationTypeDef(BaseModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None

class ExperimentTemplateStopConditionTypeDef(BaseModel):
    source: Optional[str] = None
    value: Optional[str] = None

class ExperimentTemplateSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

class ExperimentTemplateTargetFilterTypeDef(BaseModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None

class GetActionRequestRequestTypeDef(BaseModel):
    id: str

class GetExperimentRequestRequestTypeDef(BaseModel):
    id: str

class GetExperimentTargetAccountConfigurationRequestRequestTypeDef(BaseModel):
    experimentId: str
    accountId: str

class GetExperimentTemplateRequestRequestTypeDef(BaseModel):
    id: str

class GetTargetAccountConfigurationRequestRequestTypeDef(BaseModel):
    experimentTemplateId: str
    accountId: str

class GetTargetResourceTypeRequestRequestTypeDef(BaseModel):
    resourceType: str

class ListActionsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExperimentResolvedTargetsRequestRequestTypeDef(BaseModel):
    experimentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetName: Optional[str] = None

class ResolvedTargetTypeDef(BaseModel):
    resourceType: Optional[str] = None
    targetName: Optional[str] = None
    targetInformation: Optional[Dict[str, str]] = None

class ListExperimentTargetAccountConfigurationsRequestRequestTypeDef(BaseModel):
    experimentId: str
    nextToken: Optional[str] = None

class ListExperimentTemplatesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListExperimentsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    experimentTemplateId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTargetAccountConfigurationsRequestRequestTypeDef(BaseModel):
    experimentTemplateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TargetAccountConfigurationSummaryTypeDef(BaseModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None

class ListTargetResourceTypesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TargetResourceTypeSummaryTypeDef(BaseModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None

class StartExperimentExperimentOptionsInputTypeDef(BaseModel):
    actionsMode: Optional[ActionsModeType] = None

class StopExperimentRequestRequestTypeDef(BaseModel):
    id: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TargetResourceTypeParameterTypeDef(BaseModel):
    description: Optional[str] = None
    required: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Optional[Sequence[str]] = None

class UpdateExperimentTemplateActionInputItemTypeDef(BaseModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None
    targets: Optional[Mapping[str, str]] = None
    startAfter: Optional[Sequence[str]] = None

class UpdateExperimentTemplateExperimentOptionsInputTypeDef(BaseModel):
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None

class UpdateExperimentTemplateStopConditionInputTypeDef(BaseModel):
    source: str
    value: Optional[str] = None

class UpdateTargetAccountConfigurationRequestRequestTypeDef(BaseModel):
    experimentTemplateId: str
    accountId: str
    roleArn: Optional[str] = None
    description: Optional[str] = None

class ActionSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    targets: Optional[Dict[str, ActionTargetTypeDef]] = None
    tags: Optional[Dict[str, str]] = None

class ActionTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, ActionParameterTypeDef]] = None
    targets: Optional[Dict[str, ActionTargetTypeDef]] = None
    tags: Optional[Dict[str, str]] = None

class CreateExperimentTemplateLogConfigurationInputTypeDef(BaseModel):
    logSchemaVersion: int
    cloudWatchLogsConfiguration: Optional[       ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef     ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInputTypeDef] = None

class UpdateExperimentTemplateLogConfigurationInputTypeDef(BaseModel):
    cloudWatchLogsConfiguration: Optional[       ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef     ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInputTypeDef] = None
    logSchemaVersion: Optional[int] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateTargetInputTypeDef(BaseModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[Sequence[str]] = None
    resourceTags: Optional[Mapping[str, str]] = None
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilterTypeDef]] = None
    parameters: Optional[Mapping[str, str]] = None

class UpdateExperimentTemplateTargetInputTypeDef(BaseModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[Sequence[str]] = None
    resourceTags: Optional[Mapping[str, str]] = None
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilterTypeDef]] = None
    parameters: Optional[Mapping[str, str]] = None

class CreateTargetAccountConfigurationResponseTypeDef(BaseModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTargetAccountConfigurationResponseTypeDef(BaseModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTargetAccountConfigurationResponseTypeDef(BaseModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTargetAccountConfigurationResponseTypeDef(BaseModel):
    targetAccountConfiguration: TargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentActionTypeDef(BaseModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None
    state: Optional[ExperimentActionStateTypeDef] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class ExperimentLogConfigurationTypeDef(BaseModel):
    cloudWatchLogsConfiguration: Optional[ExperimentCloudWatchLogsLogConfigurationTypeDef] = None
    s3Configuration: Optional[ExperimentS3LogConfigurationTypeDef] = None
    logSchemaVersion: Optional[int] = None

class ExperimentSummaryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    experimentTemplateId: Optional[str] = None
    state: Optional[ExperimentStateTypeDef] = None
    creationTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    experimentOptions: Optional[ExperimentOptionsTypeDef] = None

class ListExperimentTargetAccountConfigurationsResponseTypeDef(BaseModel):
    targetAccountConfigurations: List[ExperimentTargetAccountConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentTargetAccountConfigurationResponseTypeDef(BaseModel):
    targetAccountConfiguration: ExperimentTargetAccountConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTargetTypeDef(BaseModel):
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTargetFilterTypeDef]] = None
    selectionMode: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None

class ExperimentTemplateLogConfigurationTypeDef(BaseModel):
    cloudWatchLogsConfiguration: Optional[       ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef     ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationTypeDef] = None
    logSchemaVersion: Optional[int] = None

class ListExperimentTemplatesResponseTypeDef(BaseModel):
    experimentTemplates: List[ExperimentTemplateSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTemplateTargetTypeDef(BaseModel):
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTemplateTargetFilterTypeDef]] = None
    selectionMode: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None

class ListExperimentResolvedTargetsResponseTypeDef(BaseModel):
    resolvedTargets: List[ResolvedTargetTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetAccountConfigurationsResponseTypeDef(BaseModel):
    targetAccountConfigurations: List[TargetAccountConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetResourceTypesResponseTypeDef(BaseModel):
    targetResourceTypes: List[TargetResourceTypeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExperimentRequestRequestTypeDef(BaseModel):
    clientToken: str
    experimentTemplateId: str
    experimentOptions: Optional[StartExperimentExperimentOptionsInputTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class TargetResourceTypeTypeDef(BaseModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, TargetResourceTypeParameterTypeDef]] = None

class ListActionsResponseTypeDef(BaseModel):
    actions: List[ActionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetActionResponseTypeDef(BaseModel):
    action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateRequestRequestTypeDef(BaseModel):
    clientToken: str
    description: str
    stopConditions: Sequence[CreateExperimentTemplateStopConditionInputTypeDef]
    actions: Mapping[str, CreateExperimentTemplateActionInputTypeDef]
    roleArn: str
    targets: Optional[Mapping[str, CreateExperimentTemplateTargetInputTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    logConfiguration: Optional[CreateExperimentTemplateLogConfigurationInputTypeDef] = None
    experimentOptions: Optional[CreateExperimentTemplateExperimentOptionsInputTypeDef] = None

class UpdateExperimentTemplateRequestRequestTypeDef(BaseModel):
    id: str
    description: Optional[str] = None
    stopConditions: Optional[Sequence[UpdateExperimentTemplateStopConditionInputTypeDef]] = None
    targets: Optional[Mapping[str, UpdateExperimentTemplateTargetInputTypeDef]] = None
    actions: Optional[Mapping[str, UpdateExperimentTemplateActionInputItemTypeDef]] = None
    roleArn: Optional[str] = None
    logConfiguration: Optional[UpdateExperimentTemplateLogConfigurationInputTypeDef] = None
    experimentOptions: Optional[UpdateExperimentTemplateExperimentOptionsInputTypeDef] = None

class ListExperimentsResponseTypeDef(BaseModel):
    experiments: List[ExperimentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExperimentTypeDef(BaseModel):
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

class ExperimentTemplateTypeDef(BaseModel):
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

class GetTargetResourceTypeResponseTypeDef(BaseModel):
    targetResourceType: TargetResourceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentResponseTypeDef(BaseModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartExperimentResponseTypeDef(BaseModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopExperimentResponseTypeDef(BaseModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentTemplateResponseTypeDef(BaseModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExperimentTemplateResponseTypeDef(BaseModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentTemplateResponseTypeDef(BaseModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExperimentTemplateResponseTypeDef(BaseModel):
    experimentTemplate: ExperimentTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

