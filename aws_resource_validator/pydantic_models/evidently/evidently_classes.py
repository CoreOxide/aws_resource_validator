from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.evidently.evidently_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class EvaluationRequest(BaseValidatorModel):
    entityId: str
    feature: str
    evaluationContext: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CloudWatchLogsDestinationConfig(BaseValidatorModel):
    logGroup: Optional[str] = None


class CloudWatchLogsDestination(BaseValidatorModel):
    logGroup: Optional[str] = None


class OnlineAbConfig(BaseValidatorModel):
    controlTreatmentName: Optional[str] = None
    treatmentWeights: Optional[Dict[str, int]] = None


class TreatmentConfig(BaseValidatorModel):
    feature: str
    name: str
    variation: str
    description: Optional[str] = None


class LaunchGroupConfig(BaseValidatorModel):
    feature: str
    name: str
    variation: str
    description: Optional[str] = None


class ProjectAppConfigResourceConfig(BaseValidatorModel):
    applicationId: Optional[str] = None
    environmentId: Optional[str] = None


# This class is the input for the 'create_segment' function.
class CreateSegmentRequest(BaseValidatorModel):
    name: str
    pattern: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Segment(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    pattern: str
    description: Optional[str] = None
    experimentCount: Optional[int] = None
    launchCount: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class DeleteExperimentRequest(BaseValidatorModel):
    experiment: str
    project: str


class DeleteFeatureRequest(BaseValidatorModel):
    feature: str
    project: str


class DeleteLaunchRequest(BaseValidatorModel):
    launch: str
    project: str


class DeleteProjectRequest(BaseValidatorModel):
    project: str


class DeleteSegmentRequest(BaseValidatorModel):
    segment: str


# This class is the input for the 'evaluate_feature' function.
class EvaluateFeatureRequest(BaseValidatorModel):
    entityId: str
    feature: str
    project: str
    evaluationContext: Optional[str] = None


class VariableValue(BaseValidatorModel):
    boolValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None


class EvaluationRule(BaseValidatorModel):
    type: str
    name: Optional[str] = None

Timestamp = Union[datetime, str]


class ExperimentExecution(BaseValidatorModel):
    endedTime: Optional[datetime] = None
    startedTime: Optional[datetime] = None


class ExperimentReport(BaseValidatorModel):
    content: Optional[str] = None
    metricName: Optional[str] = None
    reportName: Optional[Literal['BayesianInference']] = None
    treatmentName: Optional[str] = None


class ExperimentResultsData(BaseValidatorModel):
    metricName: Optional[str] = None
    resultStat: Optional[ExperimentResultResponseTypeType] = None
    treatmentName: Optional[str] = None
    values: Optional[List[float]] = None


class ExperimentSchedule(BaseValidatorModel):
    analysisCompleteTime: Optional[datetime] = None


class OnlineAbDefinition(BaseValidatorModel):
    controlTreatmentName: Optional[str] = None
    treatmentWeights: Optional[Dict[str, int]] = None


class Treatment(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    featureVariations: Optional[Dict[str, str]] = None


# This class is the input for the 'get_experiment' function.
class GetExperimentRequest(BaseValidatorModel):
    experiment: str
    project: str


# This class is the input for the 'get_feature' function.
class GetFeatureRequest(BaseValidatorModel):
    feature: str
    project: str


# This class is the input for the 'get_launch' function.
class GetLaunchRequest(BaseValidatorModel):
    launch: str
    project: str


# This class is the input for the 'get_project' function.
class GetProjectRequest(BaseValidatorModel):
    project: str


# This class is the input for the 'get_segment' function.
class GetSegmentRequest(BaseValidatorModel):
    segment: str


class LaunchExecution(BaseValidatorModel):
    endedTime: Optional[datetime] = None
    startedTime: Optional[datetime] = None


class LaunchGroup(BaseValidatorModel):
    featureVariations: Dict[str, str]
    name: str
    description: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_experiments' function.
class ListExperimentsRequest(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[ExperimentStatusType] = None


# This class is the input for the 'list_features' function.
class ListFeaturesRequest(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_launches' function.
class ListLaunchesRequest(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[LaunchStatusType] = None


# This class is the input for the 'list_projects' function.
class ListProjectsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ProjectSummary(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: ProjectStatusType
    activeExperimentCount: Optional[int] = None
    activeLaunchCount: Optional[int] = None
    description: Optional[str] = None
    experimentCount: Optional[int] = None
    featureCount: Optional[int] = None
    launchCount: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_segment_references' function.
class ListSegmentReferencesRequest(BaseValidatorModel):
    segment: str
    type: SegmentReferenceResourceTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RefResource(BaseValidatorModel):
    name: str
    type: str
    arn: Optional[str] = None
    endTime: Optional[str] = None
    lastUpdatedOn: Optional[str] = None
    startTime: Optional[str] = None
    status: Optional[str] = None


# This class is the input for the 'list_segments' function.
class ListSegmentsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class MetricDefinitionConfig(BaseValidatorModel):
    entityIdKey: str
    name: str
    valueKey: str
    eventPattern: Optional[str] = None
    unitLabel: Optional[str] = None


class MetricDefinition(BaseValidatorModel):
    entityIdKey: Optional[str] = None
    eventPattern: Optional[str] = None
    name: Optional[str] = None
    unitLabel: Optional[str] = None
    valueKey: Optional[str] = None


class ProjectAppConfigResource(BaseValidatorModel):
    applicationId: str
    configurationProfileId: str
    environmentId: str


class S3DestinationConfig(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class S3Destination(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class PutProjectEventsResultEntry(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    eventId: Optional[str] = None


class SegmentOverrideOutput(BaseValidatorModel):
    evaluationOrder: int
    segment: str
    weights: Dict[str, int]


class SegmentOverride(BaseValidatorModel):
    evaluationOrder: int
    segment: str
    weights: Dict[str, int]


# This class is the input for the 'start_launch' function.
class StartLaunchRequest(BaseValidatorModel):
    launch: str
    project: str


# This class is the input for the 'stop_experiment' function.
class StopExperimentRequest(BaseValidatorModel):
    experiment: str
    project: str
    desiredState: Optional[ExperimentStopDesiredStateType] = None
    reason: Optional[str] = None


# This class is the input for the 'stop_launch' function.
class StopLaunchRequest(BaseValidatorModel):
    launch: str
    project: str
    desiredState: Optional[LaunchStopDesiredStateType] = None
    reason: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'test_segment_pattern' function.
class TestSegmentPatternRequest(BaseValidatorModel):
    pattern: str
    payload: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'batch_evaluate_feature' function.
class BatchEvaluateFeatureRequest(BaseValidatorModel):
    project: str
    requests: List[EvaluationRequest]


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_experiment' function.
class StartExperimentResponse(BaseValidatorModel):
    startedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_experiment' function.
class StopExperimentResponse(BaseValidatorModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_launch' function.
class StopLaunchResponse(BaseValidatorModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_segment_pattern' function.
class TestSegmentPatternResponse(BaseValidatorModel):
    match: bool
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_project' function.
class UpdateProjectRequest(BaseValidatorModel):
    project: str
    appConfigResource: Optional[ProjectAppConfigResourceConfig] = None
    description: Optional[str] = None


# This class is the output for the 'create_segment' function.
class CreateSegmentResponse(BaseValidatorModel):
    segment: Segment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_segment' function.
class GetSegmentResponse(BaseValidatorModel):
    segment: Segment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_segments' function.
class ListSegmentsResponse(BaseValidatorModel):
    segments: List[Segment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'evaluate_feature' function.
class EvaluateFeatureResponse(BaseValidatorModel):
    details: str
    reason: str
    value: VariableValue
    variation: str
    ResponseMetadata: ResponseMetadata


class EvaluationResult(BaseValidatorModel):
    entityId: str
    feature: str
    details: Optional[str] = None
    project: Optional[str] = None
    reason: Optional[str] = None
    value: Optional[VariableValue] = None
    variation: Optional[str] = None


class VariationConfig(BaseValidatorModel):
    name: str
    value: VariableValue


class Variation(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[VariableValue] = None


class FeatureSummary(BaseValidatorModel):
    arn: str
    createdTime: datetime
    evaluationStrategy: FeatureEvaluationStrategyType
    lastUpdatedTime: datetime
    name: str
    status: FeatureStatusType
    defaultVariation: Optional[str] = None
    evaluationRules: Optional[List[EvaluationRule]] = None
    project: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Event(BaseValidatorModel):
    data: str
    timestamp: Timestamp
    type: EventTypeType


# This class is the input for the 'get_experiment_results' function.
class GetExperimentResultsRequest(BaseValidatorModel):
    experiment: str
    metricNames: List[str]
    project: str
    treatmentNames: List[str]
    baseStat: Optional[Literal['Mean']] = None
    endTime: Optional[Timestamp] = None
    period: Optional[int] = None
    reportNames: Optional[List[Literal['BayesianInference']]] = None
    resultStats: Optional[List[ExperimentResultRequestTypeType]] = None
    startTime: Optional[Timestamp] = None


# This class is the input for the 'start_experiment' function.
class StartExperimentRequest(BaseValidatorModel):
    analysisCompleteTime: Timestamp
    experiment: str
    project: str


# This class is the output for the 'get_experiment_results' function.
class GetExperimentResultsResponse(BaseValidatorModel):
    details: str
    reports: List[ExperimentReport]
    resultsData: List[ExperimentResultsData]
    timestamps: List[datetime]
    ResponseMetadata: ResponseMetadata


class ListExperimentsRequestPaginate(BaseValidatorModel):
    project: str
    status: Optional[ExperimentStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFeaturesRequestPaginate(BaseValidatorModel):
    project: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLaunchesRequestPaginate(BaseValidatorModel):
    project: str
    status: Optional[LaunchStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSegmentReferencesRequestPaginate(BaseValidatorModel):
    segment: str
    type: SegmentReferenceResourceTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSegmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_projects' function.
class ListProjectsResponse(BaseValidatorModel):
    projects: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_segment_references' function.
class ListSegmentReferencesResponse(BaseValidatorModel):
    referencedBy: List[RefResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MetricGoalConfig(BaseValidatorModel):
    metricDefinition: MetricDefinitionConfig
    desiredChange: Optional[ChangeDirectionEnumType] = None


class MetricMonitorConfig(BaseValidatorModel):
    metricDefinition: MetricDefinitionConfig


class MetricGoal(BaseValidatorModel):
    metricDefinition: MetricDefinition
    desiredChange: Optional[ChangeDirectionEnumType] = None


class MetricMonitor(BaseValidatorModel):
    metricDefinition: MetricDefinition


class ProjectDataDeliveryConfig(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfig] = None
    s3Destination: Optional[S3DestinationConfig] = None


# This class is the input for the 'update_project_data_delivery' function.
class UpdateProjectDataDeliveryRequest(BaseValidatorModel):
    project: str
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfig] = None
    s3Destination: Optional[S3DestinationConfig] = None


class ProjectDataDelivery(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestination] = None
    s3Destination: Optional[S3Destination] = None


# This class is the output for the 'put_project_events' function.
class PutProjectEventsResponse(BaseValidatorModel):
    eventResults: List[PutProjectEventsResultEntry]
    failedEventCount: int
    ResponseMetadata: ResponseMetadata


class ScheduledSplit(BaseValidatorModel):
    startTime: datetime
    groupWeights: Optional[Dict[str, int]] = None
    segmentOverrides: Optional[List[SegmentOverrideOutput]] = None

SegmentOverrideUnion = Union[SegmentOverride, SegmentOverrideOutput]


# This class is the output for the 'batch_evaluate_feature' function.
class BatchEvaluateFeatureResponse(BaseValidatorModel):
    results: List[EvaluationResult]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_feature' function.
class CreateFeatureRequest(BaseValidatorModel):
    name: str
    project: str
    variations: List[VariationConfig]
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Dict[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_feature' function.
class UpdateFeatureRequest(BaseValidatorModel):
    feature: str
    project: str
    addOrUpdateVariations: Optional[List[VariationConfig]] = None
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Dict[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    removeVariations: Optional[List[str]] = None


class Feature(BaseValidatorModel):
    arn: str
    createdTime: datetime
    evaluationStrategy: FeatureEvaluationStrategyType
    lastUpdatedTime: datetime
    name: str
    status: FeatureStatusType
    valueType: VariationValueTypeType
    variations: List[Variation]
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Dict[str, str]] = None
    evaluationRules: Optional[List[EvaluationRule]] = None
    project: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'list_features' function.
class ListFeaturesResponse(BaseValidatorModel):
    features: List[FeatureSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'put_project_events' function.
class PutProjectEventsRequest(BaseValidatorModel):
    events: List[Event]
    project: str


# This class is the input for the 'create_experiment' function.
class CreateExperimentRequest(BaseValidatorModel):
    metricGoals: List[MetricGoalConfig]
    name: str
    project: str
    treatments: List[TreatmentConfig]
    description: Optional[str] = None
    onlineAbConfig: Optional[OnlineAbConfig] = None
    randomizationSalt: Optional[str] = None
    samplingRate: Optional[int] = None
    segment: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_experiment' function.
class UpdateExperimentRequest(BaseValidatorModel):
    experiment: str
    project: str
    description: Optional[str] = None
    metricGoals: Optional[List[MetricGoalConfig]] = None
    onlineAbConfig: Optional[OnlineAbConfig] = None
    randomizationSalt: Optional[str] = None
    removeSegment: Optional[bool] = None
    samplingRate: Optional[int] = None
    segment: Optional[str] = None
    treatments: Optional[List[TreatmentConfig]] = None


class Experiment(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: ExperimentStatusType
    type: Literal['aws.evidently.onlineab']
    description: Optional[str] = None
    execution: Optional[ExperimentExecution] = None
    metricGoals: Optional[List[MetricGoal]] = None
    onlineAbDefinition: Optional[OnlineAbDefinition] = None
    project: Optional[str] = None
    randomizationSalt: Optional[str] = None
    samplingRate: Optional[int] = None
    schedule: Optional[ExperimentSchedule] = None
    segment: Optional[str] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    treatments: Optional[List[Treatment]] = None


# This class is the input for the 'create_project' function.
class CreateProjectRequest(BaseValidatorModel):
    name: str
    appConfigResource: Optional[ProjectAppConfigResourceConfig] = None
    dataDelivery: Optional[ProjectDataDeliveryConfig] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Project(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: ProjectStatusType
    activeExperimentCount: Optional[int] = None
    activeLaunchCount: Optional[int] = None
    appConfigResource: Optional[ProjectAppConfigResource] = None
    dataDelivery: Optional[ProjectDataDelivery] = None
    description: Optional[str] = None
    experimentCount: Optional[int] = None
    featureCount: Optional[int] = None
    launchCount: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class ScheduledSplitsLaunchDefinition(BaseValidatorModel):
    steps: Optional[List[ScheduledSplit]] = None


class ScheduledSplitConfig(BaseValidatorModel):
    groupWeights: Dict[str, int]
    startTime: Timestamp
    segmentOverrides: Optional[List[SegmentOverrideUnion]] = None


# This class is the output for the 'create_feature' function.
class CreateFeatureResponse(BaseValidatorModel):
    feature: Feature
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_feature' function.
class GetFeatureResponse(BaseValidatorModel):
    feature: Feature
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_feature' function.
class UpdateFeatureResponse(BaseValidatorModel):
    feature: Feature
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_experiment' function.
class CreateExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_experiment' function.
class GetExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_experiments' function.
class ListExperimentsResponse(BaseValidatorModel):
    experiments: List[Experiment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_experiment' function.
class UpdateExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_project' function.
class CreateProjectResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_project' function.
class GetProjectResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_project_data_delivery' function.
class UpdateProjectDataDeliveryResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_project' function.
class UpdateProjectResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class Launch(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: LaunchStatusType
    type: Literal['aws.evidently.splits']
    description: Optional[str] = None
    execution: Optional[LaunchExecution] = None
    groups: Optional[List[LaunchGroup]] = None
    metricMonitors: Optional[List[MetricMonitor]] = None
    project: Optional[str] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsDefinition: Optional[ScheduledSplitsLaunchDefinition] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ScheduledSplitsLaunchConfig(BaseValidatorModel):
    steps: List[ScheduledSplitConfig]


# This class is the output for the 'create_launch' function.
class CreateLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_launch' function.
class GetLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_launches' function.
class ListLaunchesResponse(BaseValidatorModel):
    launches: List[Launch]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_launch' function.
class StartLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_launch' function.
class UpdateLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_launch' function.
class CreateLaunchRequest(BaseValidatorModel):
    groups: List[LaunchGroupConfig]
    name: str
    project: str
    description: Optional[str] = None
    metricMonitors: Optional[List[MetricMonitorConfig]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfig] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_launch' function.
class UpdateLaunchRequest(BaseValidatorModel):
    launch: str
    project: str
    description: Optional[str] = None
    groups: Optional[List[LaunchGroupConfig]] = None
    metricMonitors: Optional[List[MetricMonitorConfig]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfig] = None