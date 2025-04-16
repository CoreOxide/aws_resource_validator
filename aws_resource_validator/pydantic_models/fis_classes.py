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

class ActionParameter(BaseValidatorModel):
    description: Optional[str] = None
    required: Optional[bool] = None


class ActionTarget(BaseValidatorModel):
    resourceType: Optional[str] = None


class CreateExperimentTemplateActionInput(BaseValidatorModel):
    actionId: str
    description: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None
    targets: Optional[Mapping[str, str]] = None
    startAfter: Optional[Sequence[str]] = None


class CreateExperimentTemplateExperimentOptionsInput(BaseValidatorModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None


class ExperimentTemplateCloudWatchLogsLogConfigurationInput(BaseValidatorModel):
    logGroupArn: str


class ExperimentTemplateS3LogConfigurationInput(BaseValidatorModel):
    bucketName: str
    prefix: Optional[str] = None


class CreateExperimentTemplateStopConditionInput(BaseValidatorModel):
    source: str
    value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ExperimentTemplateTargetInputFilter(BaseValidatorModel):
    path: str
    values: Sequence[str]


class CreateTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str
    roleArn: str
    clientToken: Optional[str] = None
    description: Optional[str] = None


class TargetAccountConfiguration(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None


class DeleteTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str


class ExperimentActionState(BaseValidatorModel):
    status: Optional[ExperimentActionStatusType] = None
    reason: Optional[str] = None


class ExperimentCloudWatchLogsLogConfiguration(BaseValidatorModel):
    logGroupArn: Optional[str] = None


class ExperimentError(BaseValidatorModel):
    accountId: Optional[str] = None
    code: Optional[str] = None
    location: Optional[str] = None


class ExperimentS3LogConfiguration(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ExperimentOptions(BaseValidatorModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None
    actionsMode: Optional[ActionsModeType] = None


class ExperimentReportConfigurationCloudWatchDashboard(BaseValidatorModel):
    dashboardIdentifier: Optional[str] = None


class ExperimentReportConfigurationOutputsS3Configuration(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ExperimentReportError(BaseValidatorModel):
    code: Optional[str] = None


class ExperimentReportS3Report(BaseValidatorModel):
    arn: Optional[str] = None
    reportType: Optional[str] = None


class ExperimentStopCondition(BaseValidatorModel):
    source: Optional[str] = None
    value: Optional[str] = None


class ExperimentTargetAccountConfigurationSummary(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None


class ExperimentTargetAccountConfiguration(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None


class ExperimentTargetFilter(BaseValidatorModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None


class ExperimentTemplateAction(BaseValidatorModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None


class ExperimentTemplateCloudWatchLogsLogConfiguration(BaseValidatorModel):
    logGroupArn: Optional[str] = None


class ExperimentTemplateExperimentOptions(BaseValidatorModel):
    accountTargeting: Optional[AccountTargetingType] = None
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None


class ExperimentTemplateS3LogConfiguration(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ExperimentTemplateReportConfigurationCloudWatchDashboard(BaseValidatorModel):
    dashboardIdentifier: Optional[str] = None


class ReportConfigurationCloudWatchDashboardInput(BaseValidatorModel):
    dashboardIdentifier: Optional[str] = None


class ReportConfigurationS3OutputInput(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ReportConfigurationS3Output(BaseValidatorModel):
    bucketName: Optional[str] = None
    prefix: Optional[str] = None


class ExperimentTemplateStopCondition(BaseValidatorModel):
    source: Optional[str] = None
    value: Optional[str] = None


class ExperimentTemplateTargetFilter(BaseValidatorModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None


class GetExperimentTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentId: str
    accountId: str


class GetTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str


class GetTargetResourceTypeRequest(BaseValidatorModel):
    resourceType: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListActionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExperimentResolvedTargetsRequest(BaseValidatorModel):
    experimentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetName: Optional[str] = None


class ResolvedTarget(BaseValidatorModel):
    resourceType: Optional[str] = None
    targetName: Optional[str] = None
    targetInformation: Optional[Dict[str, str]] = None


class ListExperimentTargetAccountConfigurationsRequest(BaseValidatorModel):
    experimentId: str
    nextToken: Optional[str] = None


class ListExperimentTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListExperimentsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    experimentTemplateId: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTargetAccountConfigurationsRequest(BaseValidatorModel):
    experimentTemplateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TargetAccountConfigurationSummary(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None


class ListTargetResourceTypesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TargetResourceTypeSummary(BaseValidatorModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None


class SafetyLeverState(BaseValidatorModel):
    status: Optional[SafetyLeverStatusType] = None
    reason: Optional[str] = None


class StartExperimentExperimentOptionsInput(BaseValidatorModel):
    actionsMode: Optional[ActionsModeType] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TargetResourceTypeParameter(BaseValidatorModel):
    description: Optional[str] = None
    required: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Optional[Sequence[str]] = None


class UpdateExperimentTemplateActionInputItem(BaseValidatorModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None
    targets: Optional[Mapping[str, str]] = None
    startAfter: Optional[Sequence[str]] = None


class UpdateExperimentTemplateExperimentOptionsInput(BaseValidatorModel):
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None


class UpdateExperimentTemplateStopConditionInput(BaseValidatorModel):
    source: str
    value: Optional[str] = None


class UpdateSafetyLeverStateInput(BaseValidatorModel):
    status: SafetyLeverStatusInputType
    reason: str


class UpdateTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str
    roleArn: Optional[str] = None
    description: Optional[str] = None


class CreateExperimentTemplateLogConfigurationInput(BaseValidatorModel):
    logSchemaVersion: int
    cloudWatchLogsConfiguration: Optional[ ExperimentTemplateCloudWatchLogsLogConfigurationInput ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInput] = None


class UpdateExperimentTemplateLogConfigurationInput(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[ ExperimentTemplateCloudWatchLogsLogConfigurationInput ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInput] = None
    logSchemaVersion: Optional[int] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateExperimentTemplateTargetInput(BaseValidatorModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[Sequence[str]] = None
    resourceTags: Optional[Mapping[str, str]] = None
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilter]] = None
    parameters: Optional[Mapping[str, str]] = None


class UpdateExperimentTemplateTargetInput(BaseValidatorModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[Sequence[str]] = None
    resourceTags: Optional[Mapping[str, str]] = None
    filters: Optional[Sequence[ExperimentTemplateTargetInputFilter]] = None
    parameters: Optional[Mapping[str, str]] = None


class CreateTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


class DeleteTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


class GetTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


class ExperimentAction(BaseValidatorModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None
    state: Optional[ExperimentActionState] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class ExperimentState(BaseValidatorModel):
    status: Optional[ExperimentStatusType] = None
    reason: Optional[str] = None
    error: Optional[ExperimentError] = None


class ExperimentLogConfiguration(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[ExperimentCloudWatchLogsLogConfiguration] = None
    s3Configuration: Optional[ExperimentS3LogConfiguration] = None
    logSchemaVersion: Optional[int] = None


class ExperimentReportConfigurationDataSources(BaseValidatorModel):
    cloudWatchDashboards: Optional[List[ExperimentReportConfigurationCloudWatchDashboard]] = None


class ExperimentReportConfigurationOutputs(BaseValidatorModel):
    s3Configuration: Optional[ExperimentReportConfigurationOutputsS3Configuration] = None


class ExperimentReportState(BaseValidatorModel):
    status: Optional[ExperimentReportStatusType] = None
    reason: Optional[str] = None
    error: Optional[ExperimentReportError] = None


class ListExperimentTargetAccountConfigurationsResponse(BaseValidatorModel):
    targetAccountConfigurations: List[ExperimentTargetAccountConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetExperimentTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: ExperimentTargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


class ExperimentTarget(BaseValidatorModel):
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTargetFilter]] = None
    selectionMode: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class ExperimentTemplateLogConfiguration(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[ ExperimentTemplateCloudWatchLogsLogConfiguration ] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfiguration] = None
    logSchemaVersion: Optional[int] = None


class ExperimentTemplateReportConfigurationDataSources(BaseValidatorModel):
    cloudWatchDashboards: Optional[ List[ExperimentTemplateReportConfigurationCloudWatchDashboard] ] = None


class ExperimentTemplateReportConfigurationDataSourcesInput(BaseValidatorModel):
    cloudWatchDashboards: Optional[Sequence[ReportConfigurationCloudWatchDashboardInput]] = None


class ExperimentTemplateReportConfigurationOutputsInput(BaseValidatorModel):
    s3Configuration: Optional[ReportConfigurationS3OutputInput] = None


class ExperimentTemplateReportConfigurationOutputs(BaseValidatorModel):
    s3Configuration: Optional[ReportConfigurationS3Output] = None


class ExperimentTemplateSummary(BaseValidatorModel):
    pass


class ListExperimentTemplatesResponse(BaseValidatorModel):
    experimentTemplates: List[ExperimentTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExperimentTemplateTarget(BaseValidatorModel):
    resourceType: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTemplateTargetFilter]] = None
    selectionMode: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class ListActionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExperimentResolvedTargetsRequestPaginate(BaseValidatorModel):
    experimentId: str
    targetName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExperimentTemplatesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExperimentsRequestPaginate(BaseValidatorModel):
    experimentTemplateId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetAccountConfigurationsRequestPaginate(BaseValidatorModel):
    experimentTemplateId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetResourceTypesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExperimentResolvedTargetsResponse(BaseValidatorModel):
    resolvedTargets: List[ResolvedTarget]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTargetAccountConfigurationsResponse(BaseValidatorModel):
    targetAccountConfigurations: List[TargetAccountConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTargetResourceTypesResponse(BaseValidatorModel):
    targetResourceTypes: List[TargetResourceTypeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartExperimentRequest(BaseValidatorModel):
    clientToken: str
    experimentTemplateId: str
    experimentOptions: Optional[StartExperimentExperimentOptionsInput] = None
    tags: Optional[Mapping[str, str]] = None


class TargetResourceType(BaseValidatorModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, TargetResourceTypeParameter]] = None


class ActionSummary(BaseValidatorModel):
    pass


class ListActionsResponse(BaseValidatorModel):
    actions: List[ActionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Action(BaseValidatorModel):
    pass


class GetActionResponse(BaseValidatorModel):
    action: Action
    ResponseMetadata: ResponseMetadata


class ExperimentReportConfiguration(BaseValidatorModel):
    outputs: Optional[ExperimentReportConfigurationOutputs] = None
    dataSources: Optional[ExperimentReportConfigurationDataSources] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class ExperimentReport(BaseValidatorModel):
    state: Optional[ExperimentReportState] = None
    s3Reports: Optional[List[ExperimentReportS3Report]] = None


class CreateExperimentTemplateReportConfigurationInput(BaseValidatorModel):
    outputs: Optional[ExperimentTemplateReportConfigurationOutputsInput] = None
    dataSources: Optional[ExperimentTemplateReportConfigurationDataSourcesInput] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class UpdateExperimentTemplateReportConfigurationInput(BaseValidatorModel):
    outputs: Optional[ExperimentTemplateReportConfigurationOutputsInput] = None
    dataSources: Optional[ExperimentTemplateReportConfigurationDataSourcesInput] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class ExperimentTemplateReportConfiguration(BaseValidatorModel):
    outputs: Optional[ExperimentTemplateReportConfigurationOutputs] = None
    dataSources: Optional[ExperimentTemplateReportConfigurationDataSources] = None
    preExperimentDuration: Optional[str] = None
    postExperimentDuration: Optional[str] = None


class SafetyLever(BaseValidatorModel):
    pass


class GetSafetyLeverResponse(BaseValidatorModel):
    safetyLever: SafetyLever
    ResponseMetadata: ResponseMetadata


class UpdateSafetyLeverStateResponse(BaseValidatorModel):
    safetyLever: SafetyLever
    ResponseMetadata: ResponseMetadata


class GetTargetResourceTypeResponse(BaseValidatorModel):
    targetResourceType: TargetResourceType
    ResponseMetadata: ResponseMetadata


class ExperimentSummary(BaseValidatorModel):
    pass


class ListExperimentsResponse(BaseValidatorModel):
    experiments: List[ExperimentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateExperimentTemplateRequest(BaseValidatorModel):
    clientToken: str
    description: str
    stopConditions: Sequence[CreateExperimentTemplateStopConditionInput]
    actions: Mapping[str, CreateExperimentTemplateActionInput]
    roleArn: str
    targets: Optional[Mapping[str, CreateExperimentTemplateTargetInput]] = None
    tags: Optional[Mapping[str, str]] = None
    logConfiguration: Optional[CreateExperimentTemplateLogConfigurationInput] = None
    experimentOptions: Optional[CreateExperimentTemplateExperimentOptionsInput] = None
    experimentReportConfiguration: Optional[ CreateExperimentTemplateReportConfigurationInput ] = None


class Experiment(BaseValidatorModel):
    pass


class GetExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


class StartExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


class StopExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


class ExperimentTemplate(BaseValidatorModel):
    pass


class CreateExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata


class DeleteExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata


class GetExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata


class UpdateExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata


