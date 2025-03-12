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


class CreateTargetAccountConfigurationRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class TargetAccountConfigurationTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None


class DeleteTargetAccountConfigurationRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str


class ExperimentActionStateTypeDef(BaseValidatorModel):
    status: Optional[ExperimentActionStatusType] = None
    reason: Optional[str] = None


class ExperimentCloudWatchLogsLogConfigurationTypeDef(BaseValidatorModel):
    logGroupArn: Optional[str] = None


class ExperimentErrorTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    code: Optional[str] = None
    location: Optional[str] = None


class ExperimentS3LogConfigurationTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ExperimentOptionsTypeDef(BaseValidatorModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None
    actionsMode: Optional[ActionsModeType] = None


class ExperimentReportConfigurationCloudWatchDashboardTypeDef(BaseValidatorModel):
    dashboardIdentifier: Optional[str] = None


class ExperimentReportConfigurationOutputsS3ConfigurationTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ExperimentReportErrorTypeDef(BaseValidatorModel):
    code: Optional[str] = None


class ExperimentReportS3ReportTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    reportType: Optional[str] = None


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


class ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef(BaseValidatorModel):
    dashboardIdentifier: Optional[str] = None


class ReportConfigurationCloudWatchDashboardInputTypeDef(BaseValidatorModel):
    dashboardIdentifier: Optional[str] = None


class ReportConfigurationS3OutputInputTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ReportConfigurationS3OutputTypeDef(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ExperimentTemplateStopConditionTypeDef(BaseValidatorModel):
    source: Optional[str] = None
    value: Optional[str] = None


class ExperimentTemplateTargetFilterTypeDef(BaseValidatorModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None


class GetExperimentTargetAccountConfigurationRequestTypeDef(BaseValidatorModel):
    experimentId: str
    accountId: str


class GetTargetAccountConfigurationRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str


class GetTargetResourceTypeRequestTypeDef(BaseValidatorModel):
    resourceType: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListActionsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExperimentResolvedTargetsRequestTypeDef(BaseValidatorModel):
    experimentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetName: Optional[str] = None


class ResolvedTargetTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    targetName: Optional[str] = None
    targetInformation: Optional[Dict[str, str]] = None


class ListExperimentTargetAccountConfigurationsRequestTypeDef(BaseValidatorModel):
    experimentId: str
    nextToken: Optional[str] = None


class ListExperimentTemplatesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExperimentsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    experimentTemplateId: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTargetAccountConfigurationsRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TargetAccountConfigurationSummaryTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None


class ListTargetResourceTypesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TargetResourceTypeSummaryTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None


class SafetyLeverStateTypeDef(BaseValidatorModel):
    status: Optional[SafetyLeverStatusType] = None
    reason: Optional[str] = None


class StartExperimentExperimentOptionsInputTypeDef(BaseValidatorModel):
    actionsMode: Optional[ActionsModeType] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TargetResourceTypeParameterTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    required: Optional[bool] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
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


class UpdateSafetyLeverStateInputTypeDef(BaseValidatorModel):
    status: SafetyLeverStatusInputType
    reason: str


class UpdateTargetAccountConfigurationRequestTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str
    roleArn: Optional[str] = None
    description: Optional[str] = None


class CreateExperimentTemplateLogConfigurationInputTypeDef(BaseValidatorModel):
    logSchemaVersion: int
    cloudWatchLogsConfiguration: Optional[ ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInputTypeDef] = None


class UpdateExperimentTemplateLogConfigurationInputTypeDef(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[ ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef ] = None
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


class ExperimentStateTypeDef(BaseValidatorModel):
    status: Optional[ExperimentStatusType] = None
    reason: Optional[str] = None
    error: Optional[ExperimentErrorTypeDef] = None


class ExperimentLogConfigurationTypeDef(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[ExperimentCloudWatchLogsLogConfigurationTypeDef] = None
    s3Configuration: Optional[ExperimentS3LogConfigurationTypeDef] = None
    logSchemaVersion: Optional[int] = None


class ExperimentReportConfigurationDataSourcesTypeDef(BaseValidatorModel):
    cloudWatchDashboards: Optional[List[ExperimentReportConfigurationCloudWatchDashboardTypeDef]] = None


class ExperimentReportConfigurationOutputsTypeDef(BaseValidatorModel):
    s3Configuration: Optional[ExperimentReportConfigurationOutputsS3ConfigurationTypeDef] = None


class ExperimentReportStateTypeDef(BaseValidatorModel):
    status: Optional[ExperimentReportStatusType] = None
    reason: Optional[str] = None
    error: Optional[ExperimentReportErrorTypeDef] = None


class ListExperimentTargetAccountConfigurationsResponseTypeDef(BaseValidatorModel):
    targetAccountConfigurations: List[ExperimentTargetAccountConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    cloudWatchLogsConfiguration: Optional[ ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationTypeDef] = None
    logSchemaVersion: Optional[int] = None


class ExperimentTemplateReportConfigurationDataSourcesTypeDef(BaseValidatorModel):
    cloudWatchDashboards: Optional[ List[ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef] ] = None


class ExperimentTemplateReportConfigurationDataSourcesInputTypeDef(BaseValidatorModel):
    cloudWatchDashboards: Optional[Sequence[ReportConfigurationCloudWatchDashboardInputTypeDef]] = None


class ExperimentTemplateReportConfigurationOutputsInputTypeDef(BaseValidatorModel):
    s3Configuration: Optional[ReportConfigurationS3OutputInputTypeDef] = None


class ExperimentTemplateReportConfigurationOutputsTypeDef(BaseValidatorModel):
    s3Configuration: Optional[ReportConfigurationS3OutputTypeDef] = None


class ExperimentTemplateSummaryTypeDef(BaseValidatorModel):
    pass


class ListExperimentTemplatesResponseTypeDef(BaseValidatorModel):
    experimentTemplates: List[ExperimentTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ExperimentTemplateTargetTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTemplateTargetFilterTypeDef]] = None
    selectionMode: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class ListActionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExperimentResolvedTargetsRequestPaginateTypeDef(BaseValidatorModel):
    experimentId: str
    targetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExperimentTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExperimentsRequestPaginateTypeDef(BaseValidatorModel):
    experimentTemplateId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTargetAccountConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    experimentTemplateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTargetResourceTypesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExperimentResolvedTargetsResponseTypeDef(BaseValidatorModel):
    resolvedTargets: List[ResolvedTargetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTargetAccountConfigurationsResponseTypeDef(BaseValidatorModel):
    targetAccountConfigurations: List[TargetAccountConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTargetResourceTypesResponseTypeDef(BaseValidatorModel):
    targetResourceTypes: List[TargetResourceTypeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartExperimentRequestTypeDef(BaseValidatorModel):
    clientToken: str
    experimentTemplateId: str
    experimentOptions: Optional[StartExperimentExperimentOptionsInputTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class TargetResourceTypeTypeDef(BaseValidatorModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, TargetResourceTypeParameterTypeDef]] = None


class ActionSummaryTypeDef(BaseValidatorModel):
    pass


class ListActionsResponseTypeDef(BaseValidatorModel):
    actions: List[ActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ActionTypeDef(BaseValidatorModel):
    pass


class GetActionResponseTypeDef(BaseValidatorModel):
    action: ActionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExperimentReportConfigurationTypeDef(BaseValidatorModel):
    outputs: Optional[ExperimentReportConfigurationOutputsTypeDef] = None
    dataSources: Optional[ExperimentReportConfigurationDataSourcesTypeDef] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class ExperimentReportTypeDef(BaseValidatorModel):
    state: Optional[ExperimentReportStateTypeDef] = None
    s3Reports: Optional[List[ExperimentReportS3ReportTypeDef]] = None


class CreateExperimentTemplateReportConfigurationInputTypeDef(BaseValidatorModel):
    outputs: Optional[ExperimentTemplateReportConfigurationOutputsInputTypeDef] = None
    dataSources: Optional[ExperimentTemplateReportConfigurationDataSourcesInputTypeDef] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class UpdateExperimentTemplateReportConfigurationInputTypeDef(BaseValidatorModel):
    outputs: Optional[ExperimentTemplateReportConfigurationOutputsInputTypeDef] = None
    dataSources: Optional[ExperimentTemplateReportConfigurationDataSourcesInputTypeDef] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class ExperimentTemplateReportConfigurationTypeDef(BaseValidatorModel):
    outputs: Optional[ExperimentTemplateReportConfigurationOutputsTypeDef] = None
    dataSources: Optional[ExperimentTemplateReportConfigurationDataSourcesTypeDef] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class SafetyLeverTypeDef(BaseValidatorModel):
    pass


class GetSafetyLeverResponseTypeDef(BaseValidatorModel):
    safetyLever: SafetyLeverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSafetyLeverStateResponseTypeDef(BaseValidatorModel):
    safetyLever: SafetyLeverTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTargetResourceTypeResponseTypeDef(BaseValidatorModel):
    targetResourceType: TargetResourceTypeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExperimentSummaryTypeDef(BaseValidatorModel):
    pass


class ListExperimentsResponseTypeDef(BaseValidatorModel):
    experiments: List[ExperimentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateExperimentTemplateRequestTypeDef(BaseValidatorModel):
    clientToken: str
    description: str
    stopConditions: Sequence[CreateExperimentTemplateStopConditionInputTypeDef]
    actions: Mapping[str, CreateExperimentTemplateActionInputTypeDef]
    roleArn: str
    targets: Optional[Mapping[str, CreateExperimentTemplateTargetInputTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    logConfiguration: Optional[CreateExperimentTemplateLogConfigurationInputTypeDef] = None
    experimentOptions: Optional[CreateExperimentTemplateExperimentOptionsInputTypeDef] = None
    experimentReportConfiguration: Optional[ CreateExperimentTemplateReportConfigurationInputTypeDef ] = None


class ExperimentTypeDef(BaseValidatorModel):
    pass


class GetExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExperimentTemplateTypeDef(BaseValidatorModel):
    pass


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


