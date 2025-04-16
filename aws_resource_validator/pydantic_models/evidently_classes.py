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
from aws_resource_validator.pydantic_models.evidently_constants import *

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
    treatmentWeights: Optional[Mapping[str, int]] = None


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


class CreateSegmentRequest(BaseValidatorModel):
    name: str
    pattern: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


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


class ExperimentExecution(BaseValidatorModel):
    endedTime: Optional[datetime] = None
    startedTime: Optional[datetime] = None


class ExperimentReport(BaseValidatorModel):
    content: Optional[str] = None
    metricName: Optional[str] = None
    reportName: Optional[Literal["BayesianInference"]] = None
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


class GetExperimentRequest(BaseValidatorModel):
    experiment: str
    project: str


class GetFeatureRequest(BaseValidatorModel):
    feature: str
    project: str


class GetLaunchRequest(BaseValidatorModel):
    launch: str
    project: str


class GetProjectRequest(BaseValidatorModel):
    project: str


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


class ListExperimentsRequest(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[ExperimentStatusType] = None


class ListFeaturesRequest(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLaunchesRequest(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[LaunchStatusType] = None


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


class ListSegmentsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


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
    weights: Mapping[str, int]


class StartLaunchRequest(BaseValidatorModel):
    launch: str
    project: str


class StopExperimentRequest(BaseValidatorModel):
    experiment: str
    project: str
    desiredState: Optional[ExperimentStopDesiredStateType] = None
    reason: Optional[str] = None


class StopLaunchRequest(BaseValidatorModel):
    launch: str
    project: str
    desiredState: Optional[LaunchStopDesiredStateType] = None
    reason: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestSegmentPatternRequest(BaseValidatorModel):
    pattern: str
    payload: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class BatchEvaluateFeatureRequest(BaseValidatorModel):
    project: str
    requests: Sequence[EvaluationRequest]


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartExperimentResponse(BaseValidatorModel):
    startedTime: datetime
    ResponseMetadata: ResponseMetadata


class StopExperimentResponse(BaseValidatorModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadata


class StopLaunchResponse(BaseValidatorModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadata


class TestSegmentPatternResponse(BaseValidatorModel):
    match: bool
    ResponseMetadata: ResponseMetadata


class UpdateProjectRequest(BaseValidatorModel):
    project: str
    appConfigResource: Optional[ProjectAppConfigResourceConfig] = None
    description: Optional[str] = None


class CreateSegmentResponse(BaseValidatorModel):
    segment: Segment
    ResponseMetadata: ResponseMetadata


class GetSegmentResponse(BaseValidatorModel):
    segment: Segment
    ResponseMetadata: ResponseMetadata


class ListSegmentsResponse(BaseValidatorModel):
    segments: List[Segment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class EvaluationRule(BaseValidatorModel):
    pass


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


class Timestamp(BaseValidatorModel):
    pass


class GetExperimentResultsRequest(BaseValidatorModel):
    experiment: str
    metricNames: Sequence[str]
    project: str
    treatmentNames: Sequence[str]
    baseStat: Optional[Literal["Mean"]] = None
    endTime: Optional[Timestamp] = None
    period: Optional[int] = None
    reportNames: Optional[Sequence[Literal["BayesianInference"]]] = None
    resultStats: Optional[Sequence[ExperimentResultRequestTypeType]] = None
    startTime: Optional[Timestamp] = None


class StartExperimentRequest(BaseValidatorModel):
    analysisCompleteTime: Timestamp
    experiment: str
    project: str


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


class ListSegmentsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProjectsResponse(BaseValidatorModel):
    projects: List[ProjectSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RefResource(BaseValidatorModel):
    pass


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


class UpdateProjectDataDeliveryRequest(BaseValidatorModel):
    project: str
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfig] = None
    s3Destination: Optional[S3DestinationConfig] = None


class ProjectDataDelivery(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestination] = None
    s3Destination: Optional[S3Destination] = None


class PutProjectEventsResponse(BaseValidatorModel):
    eventResults: List[PutProjectEventsResultEntry]
    failedEventCount: int
    ResponseMetadata: ResponseMetadata


class ScheduledSplit(BaseValidatorModel):
    startTime: datetime
    groupWeights: Optional[Dict[str, int]] = None
    segmentOverrides: Optional[List[SegmentOverrideOutput]] = None


class BatchEvaluateFeatureResponse(BaseValidatorModel):
    results: List[EvaluationResult]
    ResponseMetadata: ResponseMetadata


class CreateFeatureRequest(BaseValidatorModel):
    name: str
    project: str
    variations: Sequence[VariationConfig]
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Mapping[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFeatureRequest(BaseValidatorModel):
    feature: str
    project: str
    addOrUpdateVariations: Optional[Sequence[VariationConfig]] = None
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Mapping[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    removeVariations: Optional[Sequence[str]] = None


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


class ListFeaturesResponse(BaseValidatorModel):
    features: List[FeatureSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Event(BaseValidatorModel):
    pass


class PutProjectEventsRequest(BaseValidatorModel):
    events: Sequence[Event]
    project: str


class CreateExperimentRequest(BaseValidatorModel):
    metricGoals: Sequence[MetricGoalConfig]
    name: str
    project: str
    treatments: Sequence[TreatmentConfig]
    description: Optional[str] = None
    onlineAbConfig: Optional[OnlineAbConfig] = None
    randomizationSalt: Optional[str] = None
    samplingRate: Optional[int] = None
    segment: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateExperimentRequest(BaseValidatorModel):
    experiment: str
    project: str
    description: Optional[str] = None
    metricGoals: Optional[Sequence[MetricGoalConfig]] = None
    onlineAbConfig: Optional[OnlineAbConfig] = None
    randomizationSalt: Optional[str] = None
    removeSegment: Optional[bool] = None
    samplingRate: Optional[int] = None
    segment: Optional[str] = None
    treatments: Optional[Sequence[TreatmentConfig]] = None


class CreateProjectRequest(BaseValidatorModel):
    name: str
    appConfigResource: Optional[ProjectAppConfigResourceConfig] = None
    dataDelivery: Optional[ProjectDataDeliveryConfig] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


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


class SegmentOverrideUnion(BaseValidatorModel):
    pass


class ScheduledSplitConfig(BaseValidatorModel):
    groupWeights: Mapping[str, int]
    startTime: Timestamp
    segmentOverrides: Optional[Sequence[SegmentOverrideUnion]] = None


class CreateFeatureResponse(BaseValidatorModel):
    feature: Feature
    ResponseMetadata: ResponseMetadata


class GetFeatureResponse(BaseValidatorModel):
    feature: Feature
    ResponseMetadata: ResponseMetadata


class UpdateFeatureResponse(BaseValidatorModel):
    feature: Feature
    ResponseMetadata: ResponseMetadata


class Experiment(BaseValidatorModel):
    pass


class CreateExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


class GetExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


class ListExperimentsResponse(BaseValidatorModel):
    experiments: List[Experiment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdateExperimentResponse(BaseValidatorModel):
    experiment: Experiment
    ResponseMetadata: ResponseMetadata


class CreateProjectResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class GetProjectResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class UpdateProjectDataDeliveryResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class UpdateProjectResponse(BaseValidatorModel):
    project: Project
    ResponseMetadata: ResponseMetadata


class ScheduledSplitsLaunchConfig(BaseValidatorModel):
    steps: Sequence[ScheduledSplitConfig]


class Launch(BaseValidatorModel):
    pass


class CreateLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


class GetLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


class ListLaunchesResponse(BaseValidatorModel):
    launches: List[Launch]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


class UpdateLaunchResponse(BaseValidatorModel):
    launch: Launch
    ResponseMetadata: ResponseMetadata


class CreateLaunchRequest(BaseValidatorModel):
    groups: Sequence[LaunchGroupConfig]
    name: str
    project: str
    description: Optional[str] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfig]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfig] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateLaunchRequest(BaseValidatorModel):
    launch: str
    project: str
    description: Optional[str] = None
    groups: Optional[Sequence[LaunchGroupConfig]] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfig]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfig] = None


