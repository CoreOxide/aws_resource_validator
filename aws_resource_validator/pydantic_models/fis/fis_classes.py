from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.fis.fis_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActionParameter(BaseValidatorModel):
    description: Optional[str] = None
    required: Optional[bool] = None


class ActionTarget(BaseValidatorModel):
    resourceType: Optional[str] = None


class CreateExperimentTemplateActionInput(BaseValidatorModel):
    actionId: str
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None


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
    values: List[str]


# This class is the input for the 'create_target_account_configuration' function.
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


# This class is the input for the 'delete_experiment_template' function.
class DeleteExperimentTemplateRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_target_account_configuration' function.
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


class ExperimentTemplateSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class ExperimentTemplateTargetFilter(BaseValidatorModel):
    path: Optional[str] = None
    values: Optional[List[str]] = None


# This class is the input for the 'get_action' function.
class GetActionRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_experiment' function.
class GetExperimentRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_experiment_target_account_configuration' function.
class GetExperimentTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentId: str
    accountId: str


# This class is the input for the 'get_experiment_template' function.
class GetExperimentTemplateRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_safety_lever' function.
class GetSafetyLeverRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_target_account_configuration' function.
class GetTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str


# This class is the input for the 'get_target_resource_type' function.
class GetTargetResourceTypeRequest(BaseValidatorModel):
    resourceType: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_actions' function.
class ListActionsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_experiment_resolved_targets' function.
class ListExperimentResolvedTargetsRequest(BaseValidatorModel):
    experimentId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    targetName: Optional[str] = None


class ResolvedTarget(BaseValidatorModel):
    resourceType: Optional[str] = None
    targetName: Optional[str] = None
    targetInformation: Optional[Dict[str, str]] = None


# This class is the input for the 'list_experiment_target_account_configurations' function.
class ListExperimentTargetAccountConfigurationsRequest(BaseValidatorModel):
    experimentId: str
    nextToken: Optional[str] = None


# This class is the input for the 'list_experiment_templates' function.
class ListExperimentTemplatesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_experiments' function.
class ListExperimentsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    experimentTemplateId: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_target_account_configurations' function.
class ListTargetAccountConfigurationsRequest(BaseValidatorModel):
    experimentTemplateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TargetAccountConfigurationSummary(BaseValidatorModel):
    roleArn: Optional[str] = None
    accountId: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'list_target_resource_types' function.
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


# This class is the input for the 'stop_experiment' function.
class StopExperimentRequest(BaseValidatorModel):
    id: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TargetResourceTypeParameter(BaseValidatorModel):
    description: Optional[str] = None
    required: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Optional[List[str]] = None


class UpdateExperimentTemplateActionInputItem(BaseValidatorModel):
    actionId: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None
    targets: Optional[Dict[str, str]] = None
    startAfter: Optional[List[str]] = None


class UpdateExperimentTemplateExperimentOptionsInput(BaseValidatorModel):
    emptyTargetResolutionMode: Optional[EmptyTargetResolutionModeType] = None


class UpdateExperimentTemplateStopConditionInput(BaseValidatorModel):
    source: str
    value: Optional[str] = None


class UpdateSafetyLeverStateInput(BaseValidatorModel):
    status: SafetyLeverStatusInputType
    reason: str


# This class is the input for the 'update_target_account_configuration' function.
class UpdateTargetAccountConfigurationRequest(BaseValidatorModel):
    experimentTemplateId: str
    accountId: str
    roleArn: Optional[str] = None
    description: Optional[str] = None


class ActionSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    targets: Optional[Dict[str, ActionTarget]] = None
    tags: Optional[Dict[str, str]] = None


class Action(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, ActionParameter]] = None
    targets: Optional[Dict[str, ActionTarget]] = None
    tags: Optional[Dict[str, str]] = None


class CreateExperimentTemplateLogConfigurationInput(BaseValidatorModel):
    logSchemaVersion: int
    cloudWatchLogsConfiguration: Optional[ExperimentTemplateCloudWatchLogsLogConfigurationInput] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInput] = None


class UpdateExperimentTemplateLogConfigurationInput(BaseValidatorModel):
    cloudWatchLogsConfiguration: Optional[ExperimentTemplateCloudWatchLogsLogConfigurationInput] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfigurationInput] = None
    logSchemaVersion: Optional[int] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateExperimentTemplateTargetInput(BaseValidatorModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTemplateTargetInputFilter]] = None
    parameters: Optional[Dict[str, str]] = None


class UpdateExperimentTemplateTargetInput(BaseValidatorModel):
    resourceType: str
    selectionMode: str
    resourceArns: Optional[List[str]] = None
    resourceTags: Optional[Dict[str, str]] = None
    filters: Optional[List[ExperimentTemplateTargetInputFilter]] = None
    parameters: Optional[Dict[str, str]] = None


# This class is the output for the 'create_target_account_configuration' function.
class CreateTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_target_account_configuration' function.
class DeleteTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_target_account_configuration' function.
class GetTargetAccountConfigurationResponse(BaseValidatorModel):
    targetAccountConfiguration: TargetAccountConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_target_account_configuration' function.
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


# This class is the output for the 'list_experiment_target_account_configurations' function.
class ListExperimentTargetAccountConfigurationsResponse(BaseValidatorModel):
    targetAccountConfigurations: List[ExperimentTargetAccountConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_experiment_target_account_configuration' function.
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
    cloudWatchLogsConfiguration: Optional[ExperimentTemplateCloudWatchLogsLogConfiguration] = None
    s3Configuration: Optional[ExperimentTemplateS3LogConfiguration] = None
    logSchemaVersion: Optional[int] = None


class ExperimentTemplateReportConfigurationDataSources(BaseValidatorModel):
    cloudWatchDashboards: Optional[List[ExperimentTemplateReportConfigurationCloudWatchDashboard]] = None


class ExperimentTemplateReportConfigurationDataSourcesInput(BaseValidatorModel):
    cloudWatchDashboards: Optional[List[ReportConfigurationCloudWatchDashboardInput]] = None


class ExperimentTemplateReportConfigurationOutputsInput(BaseValidatorModel):
    s3Configuration: Optional[ReportConfigurationS3OutputInput] = None


class ExperimentTemplateReportConfigurationOutputs(BaseValidatorModel):
    s3Configuration: Optional[ReportConfigurationS3Output] = None


# This class is the output for the 'list_experiment_templates' function.
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


# This class is the output for the 'list_experiment_resolved_targets' function.
class ListExperimentResolvedTargetsResponse(BaseValidatorModel):
    resolvedTargets: List[ResolvedTarget]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_target_account_configurations' function.
class ListTargetAccountConfigurationsResponse(BaseValidatorModel):
    targetAccountConfigurations: List[TargetAccountConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_target_resource_types' function.
class ListTargetResourceTypesResponse(BaseValidatorModel):
    targetResourceTypes: List[TargetResourceTypeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SafetyLever(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    state: Optional[SafetyLeverState] = None


# This class is the input for the 'start_experiment' function.
class StartExperimentRequest(BaseValidatorModel):
    clientToken: str
    experimentTemplateId: str
    experimentOptions: Optional[StartExperimentExperimentOptionsInput] = None
    tags: Optional[Dict[str, str]] = None


class TargetResourceType(BaseValidatorModel):
    resourceType: Optional[str] = None
    description: Optional[str] = None
    parameters: Optional[Dict[str, TargetResourceTypeParameter]] = None


# This class is the input for the 'update_safety_lever_state' function.
class UpdateSafetyLeverStateRequest(BaseValidatorModel):
    id: str
    state: UpdateSafetyLeverStateInput


# This class is the output for the 'list_actions' function.
class ListActionsResponse(BaseValidatorModel):
    actions: List[ActionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_action' function.
class GetActionResponse(BaseValidatorModel):
    action: Action
    ResponseMetadata: ResponseMetadata


class ExperimentSummary(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    experimentTemplateId: Optional[str] = None
    state: Optional[ExperimentState] = None
    creationTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    experimentOptions: Optional[ExperimentOptions] = None


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


# This class is the output for the 'get_safety_lever' function.
class GetSafetyLeverResponse(BaseValidatorModel):
    safetyLever: SafetyLever
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_safety_lever_state' function.
class UpdateSafetyLeverStateResponse(BaseValidatorModel):
    safetyLever: SafetyLever
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_target_resource_type' function.
class GetTargetResourceTypeResponse(BaseValidatorModel):
    targetResourceType: TargetResourceType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_experiments' function.
class ListExperimentsResponse(BaseValidatorModel):
    experiments: List[ExperimentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Experiment(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    experimentTemplateId: Optional[str] = None
    roleArn: Optional[str] = None
    state: Optional[ExperimentState] = None
    targets: Optional[Dict[str, ExperimentTarget]] = None
    actions: Optional[Dict[str, ExperimentAction]] = None
    stopConditions: Optional[List[ExperimentStopCondition]] = None
    creationTime: Optional[datetime] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None
    logConfiguration: Optional[ExperimentLogConfiguration] = None
    experimentOptions: Optional[ExperimentOptions] = None
    targetAccountConfigurationsCount: Optional[int] = None
    experimentReportConfiguration: Optional[ExperimentReportConfiguration] = None
    experimentReport: Optional[ExperimentReport] = None


# This class is the input for the 'create_experiment_template' function.
class CreateExperimentTemplateRequest(BaseValidatorModel):
    clientToken: str
    description: str
    stopConditions: List[CreateExperimentTemplateStopConditionInput]
    actions: Dict[str, CreateExperimentTemplateActionInput]
    roleArn: str
    targets: Optional[Dict[str, CreateExperimentTemplateTargetInput]] = None
    tags: Optional[Dict[str, str]] = None
    logConfiguration: Optional[CreateExperimentTemplateLogConfigurationInput] = None
    experimentOptions: Optional[CreateExperimentTemplateExperimentOptionsInput] = None
    experimentReportConfiguration: Optional[CreateExperimentTemplateReportConfigurationInput] = None


# This class is the input for the 'update_experiment_template' function.
class UpdateExperimentTemplateRequest(BaseValidatorModel):
    id: str
    description: Optional[str] = None
    stopConditions: Optional[List[UpdateExperimentTemplateStopConditionInput]] = None
    targets: Optional[Dict[str, UpdateExperimentTemplateTargetInput]] = None
    actions: Optional[Dict[str, UpdateExperimentTemplateActionInputItem]] = None
    roleArn: Optional[str] = None
    logConfiguration: Optional[UpdateExperimentTemplateLogConfigurationInput] = None
    experimentOptions: Optional[UpdateExperimentTemplateExperimentOptionsInput] = None
    experimentReportConfiguration: Optional[UpdateExperimentTemplateReportConfigurationInput] = None


class ExperimentTemplate(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    targets: Optional[Dict[str, ExperimentTemplateTarget]] = None
    actions: Optional[Dict[str, ExperimentTemplateAction]] = None
    stopConditions: Optional[List[ExperimentTemplateStopCondition]] = None
    creationTime: Optional[datetime] = None
    lastUpdateTime: Optional[datetime] = None
    roleArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    logConfiguration: Optional[ExperimentTemplateLogConfiguration] = None
    experimentOptions: Optional[ExperimentTemplateExperimentOptions] = None
    targetAccountConfigurationsCount: Optional[int] = None
    experimentReportConfiguration: Optional[ExperimentTemplateReportConfiguration] = None


# This class is the output for the 'get_experiment' function.
class GetExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_experiment' function.
class StartExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_experiment' function.
class StopExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_experiment_template' function.
class CreateExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_experiment_template' function.
class DeleteExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_experiment_template' function.
class GetExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_experiment_template' function.
class UpdateExperimentTemplateResponse(BaseValidatorModel):
    experimentTemplate: ExperimentTemplate
    ResponseMetadata: ResponseMetadata