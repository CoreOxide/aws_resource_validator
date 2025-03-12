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

class EvaluationRequestTypeDef(BaseValidatorModel):
    entityId: str
    feature: str
    evaluationContext: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CloudWatchLogsDestinationConfigTypeDef(BaseValidatorModel):
    logGroup: Optional[str] = None


class CloudWatchLogsDestinationTypeDef(BaseValidatorModel):
    logGroup: Optional[str] = None


class OnlineAbConfigTypeDef(BaseValidatorModel):
    controlTreatmentName: Optional[str] = None
    treatmentWeights: Optional[Mapping[str, int]] = None


class TreatmentConfigTypeDef(BaseValidatorModel):
    feature: str
    name: str
    variation: str
    description: Optional[str] = None


class LaunchGroupConfigTypeDef(BaseValidatorModel):
    feature: str
    name: str
    variation: str
    description: Optional[str] = None


class ProjectAppConfigResourceConfigTypeDef(BaseValidatorModel):
    applicationId: Optional[str] = None
    environmentId: Optional[str] = None


class CreateSegmentRequestTypeDef(BaseValidatorModel):
    name: str
    pattern: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class SegmentTypeDef(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    pattern: str
    description: Optional[str] = None
    experimentCount: Optional[int] = None
    launchCount: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class DeleteExperimentRequestTypeDef(BaseValidatorModel):
    experiment: str
    project: str


class DeleteFeatureRequestTypeDef(BaseValidatorModel):
    feature: str
    project: str


class DeleteLaunchRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str


class DeleteProjectRequestTypeDef(BaseValidatorModel):
    project: str


class DeleteSegmentRequestTypeDef(BaseValidatorModel):
    segment: str


class EvaluateFeatureRequestTypeDef(BaseValidatorModel):
    entityId: str
    feature: str
    project: str
    evaluationContext: Optional[str] = None


class VariableValueTypeDef(BaseValidatorModel):
    boolValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None


class ExperimentExecutionTypeDef(BaseValidatorModel):
    endedTime: Optional[datetime] = None
    startedTime: Optional[datetime] = None


class ExperimentReportTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    metricName: Optional[str] = None
    reportName: Optional[Literal["BayesianInference"]] = None
    treatmentName: Optional[str] = None


class ExperimentResultsDataTypeDef(BaseValidatorModel):
    metricName: Optional[str] = None
    resultStat: Optional[ExperimentResultResponseTypeType] = None
    treatmentName: Optional[str] = None
    values: Optional[List[float]] = None


class ExperimentScheduleTypeDef(BaseValidatorModel):
    analysisCompleteTime: Optional[datetime] = None


class OnlineAbDefinitionTypeDef(BaseValidatorModel):
    controlTreatmentName: Optional[str] = None
    treatmentWeights: Optional[Dict[str, int]] = None


class TreatmentTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    featureVariations: Optional[Dict[str, str]] = None


class GetExperimentRequestTypeDef(BaseValidatorModel):
    experiment: str
    project: str


class GetFeatureRequestTypeDef(BaseValidatorModel):
    feature: str
    project: str


class GetLaunchRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str


class GetProjectRequestTypeDef(BaseValidatorModel):
    project: str


class GetSegmentRequestTypeDef(BaseValidatorModel):
    segment: str


class LaunchExecutionTypeDef(BaseValidatorModel):
    endedTime: Optional[datetime] = None
    startedTime: Optional[datetime] = None


class LaunchGroupTypeDef(BaseValidatorModel):
    featureVariations: Dict[str, str]
    name: str
    description: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListExperimentsRequestTypeDef(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[ExperimentStatusType] = None


class ListFeaturesRequestTypeDef(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLaunchesRequestTypeDef(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[LaunchStatusType] = None


class ListProjectsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ProjectSummaryTypeDef(BaseValidatorModel):
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


class ListSegmentsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class MetricDefinitionConfigTypeDef(BaseValidatorModel):
    entityIdKey: str
    name: str
    valueKey: str
    eventPattern: Optional[str] = None
    unitLabel: Optional[str] = None


class MetricDefinitionTypeDef(BaseValidatorModel):
    entityIdKey: Optional[str] = None
    eventPattern: Optional[str] = None
    name: Optional[str] = None
    unitLabel: Optional[str] = None
    valueKey: Optional[str] = None


class ProjectAppConfigResourceTypeDef(BaseValidatorModel):
    applicationId: str
    configurationProfileId: str
    environmentId: str


class S3DestinationConfigTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class S3DestinationTypeDef(BaseValidatorModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None


class PutProjectEventsResultEntryTypeDef(BaseValidatorModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    eventId: Optional[str] = None


class SegmentOverrideOutputTypeDef(BaseValidatorModel):
    evaluationOrder: int
    segment: str
    weights: Dict[str, int]


class SegmentOverrideTypeDef(BaseValidatorModel):
    evaluationOrder: int
    segment: str
    weights: Mapping[str, int]


class StartLaunchRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str


class StopExperimentRequestTypeDef(BaseValidatorModel):
    experiment: str
    project: str
    desiredState: Optional[ExperimentStopDesiredStateType] = None
    reason: Optional[str] = None


class StopLaunchRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str
    desiredState: Optional[LaunchStopDesiredStateType] = None
    reason: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestSegmentPatternRequestTypeDef(BaseValidatorModel):
    pattern: str
    payload: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class BatchEvaluateFeatureRequestTypeDef(BaseValidatorModel):
    project: str
    requests: Sequence[EvaluationRequestTypeDef]


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartExperimentResponseTypeDef(BaseValidatorModel):
    startedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class StopExperimentResponseTypeDef(BaseValidatorModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class StopLaunchResponseTypeDef(BaseValidatorModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class TestSegmentPatternResponseTypeDef(BaseValidatorModel):
    match: bool
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProjectRequestTypeDef(BaseValidatorModel):
    project: str
    appConfigResource: Optional[ProjectAppConfigResourceConfigTypeDef] = None
    description: Optional[str] = None


class CreateSegmentResponseTypeDef(BaseValidatorModel):
    segment: SegmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSegmentResponseTypeDef(BaseValidatorModel):
    segment: SegmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSegmentsResponseTypeDef(BaseValidatorModel):
    segments: List[SegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EvaluateFeatureResponseTypeDef(BaseValidatorModel):
    details: str
    reason: str
    value: VariableValueTypeDef
    variation: str
    ResponseMetadata: ResponseMetadataTypeDef


class EvaluationResultTypeDef(BaseValidatorModel):
    entityId: str
    feature: str
    details: Optional[str] = None
    project: Optional[str] = None
    reason: Optional[str] = None
    value: Optional[VariableValueTypeDef] = None
    variation: Optional[str] = None


class VariationConfigTypeDef(BaseValidatorModel):
    name: str
    value: VariableValueTypeDef


class VariationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[VariableValueTypeDef] = None


class EvaluationRuleTypeDef(BaseValidatorModel):
    pass


class FeatureSummaryTypeDef(BaseValidatorModel):
    arn: str
    createdTime: datetime
    evaluationStrategy: FeatureEvaluationStrategyType
    lastUpdatedTime: datetime
    name: str
    status: FeatureStatusType
    defaultVariation: Optional[str] = None
    evaluationRules: Optional[List[EvaluationRuleTypeDef]] = None
    project: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class GetExperimentResultsRequestTypeDef(BaseValidatorModel):
    experiment: str
    metricNames: Sequence[str]
    project: str
    treatmentNames: Sequence[str]
    baseStat: Optional[Literal["Mean"]] = None
    endTime: Optional[TimestampTypeDef] = None
    period: Optional[int] = None
    reportNames: Optional[Sequence[Literal["BayesianInference"]]] = None
    resultStats: Optional[Sequence[ExperimentResultRequestTypeType]] = None
    startTime: Optional[TimestampTypeDef] = None


class StartExperimentRequestTypeDef(BaseValidatorModel):
    analysisCompleteTime: TimestampTypeDef
    experiment: str
    project: str


class GetExperimentResultsResponseTypeDef(BaseValidatorModel):
    details: str
    reports: List[ExperimentReportTypeDef]
    resultsData: List[ExperimentResultsDataTypeDef]
    timestamps: List[datetime]
    ResponseMetadata: ResponseMetadataTypeDef


class ListExperimentsRequestPaginateTypeDef(BaseValidatorModel):
    project: str
    status: Optional[ExperimentStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFeaturesRequestPaginateTypeDef(BaseValidatorModel):
    project: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLaunchesRequestPaginateTypeDef(BaseValidatorModel):
    project: str
    status: Optional[LaunchStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSegmentsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProjectsResponseTypeDef(BaseValidatorModel):
    projects: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RefResourceTypeDef(BaseValidatorModel):
    pass


class ListSegmentReferencesResponseTypeDef(BaseValidatorModel):
    referencedBy: List[RefResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MetricGoalConfigTypeDef(BaseValidatorModel):
    metricDefinition: MetricDefinitionConfigTypeDef
    desiredChange: Optional[ChangeDirectionEnumType] = None


class MetricMonitorConfigTypeDef(BaseValidatorModel):
    metricDefinition: MetricDefinitionConfigTypeDef


class MetricGoalTypeDef(BaseValidatorModel):
    metricDefinition: MetricDefinitionTypeDef
    desiredChange: Optional[ChangeDirectionEnumType] = None


class MetricMonitorTypeDef(BaseValidatorModel):
    metricDefinition: MetricDefinitionTypeDef


class ProjectDataDeliveryConfigTypeDef(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfigTypeDef] = None
    s3Destination: Optional[S3DestinationConfigTypeDef] = None


class UpdateProjectDataDeliveryRequestTypeDef(BaseValidatorModel):
    project: str
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfigTypeDef] = None
    s3Destination: Optional[S3DestinationConfigTypeDef] = None


class ProjectDataDeliveryTypeDef(BaseValidatorModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestinationTypeDef] = None
    s3Destination: Optional[S3DestinationTypeDef] = None


class PutProjectEventsResponseTypeDef(BaseValidatorModel):
    eventResults: List[PutProjectEventsResultEntryTypeDef]
    failedEventCount: int
    ResponseMetadata: ResponseMetadataTypeDef


class ScheduledSplitTypeDef(BaseValidatorModel):
    startTime: datetime
    groupWeights: Optional[Dict[str, int]] = None
    segmentOverrides: Optional[List[SegmentOverrideOutputTypeDef]] = None


class BatchEvaluateFeatureResponseTypeDef(BaseValidatorModel):
    results: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFeatureRequestTypeDef(BaseValidatorModel):
    name: str
    project: str
    variations: Sequence[VariationConfigTypeDef]
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Mapping[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateFeatureRequestTypeDef(BaseValidatorModel):
    feature: str
    project: str
    addOrUpdateVariations: Optional[Sequence[VariationConfigTypeDef]] = None
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Mapping[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    removeVariations: Optional[Sequence[str]] = None


class FeatureTypeDef(BaseValidatorModel):
    arn: str
    createdTime: datetime
    evaluationStrategy: FeatureEvaluationStrategyType
    lastUpdatedTime: datetime
    name: str
    status: FeatureStatusType
    valueType: VariationValueTypeType
    variations: List[VariationTypeDef]
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Dict[str, str]] = None
    evaluationRules: Optional[List[EvaluationRuleTypeDef]] = None
    project: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListFeaturesResponseTypeDef(BaseValidatorModel):
    features: List[FeatureSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EventTypeDef(BaseValidatorModel):
    pass


class PutProjectEventsRequestTypeDef(BaseValidatorModel):
    events: Sequence[EventTypeDef]
    project: str


class CreateExperimentRequestTypeDef(BaseValidatorModel):
    metricGoals: Sequence[MetricGoalConfigTypeDef]
    name: str
    project: str
    treatments: Sequence[TreatmentConfigTypeDef]
    description: Optional[str] = None
    onlineAbConfig: Optional[OnlineAbConfigTypeDef] = None
    randomizationSalt: Optional[str] = None
    samplingRate: Optional[int] = None
    segment: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateExperimentRequestTypeDef(BaseValidatorModel):
    experiment: str
    project: str
    description: Optional[str] = None
    metricGoals: Optional[Sequence[MetricGoalConfigTypeDef]] = None
    onlineAbConfig: Optional[OnlineAbConfigTypeDef] = None
    randomizationSalt: Optional[str] = None
    removeSegment: Optional[bool] = None
    samplingRate: Optional[int] = None
    segment: Optional[str] = None
    treatments: Optional[Sequence[TreatmentConfigTypeDef]] = None


class CreateProjectRequestTypeDef(BaseValidatorModel):
    name: str
    appConfigResource: Optional[ProjectAppConfigResourceConfigTypeDef] = None
    dataDelivery: Optional[ProjectDataDeliveryConfigTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ProjectTypeDef(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: ProjectStatusType
    activeExperimentCount: Optional[int] = None
    activeLaunchCount: Optional[int] = None
    appConfigResource: Optional[ProjectAppConfigResourceTypeDef] = None
    dataDelivery: Optional[ProjectDataDeliveryTypeDef] = None
    description: Optional[str] = None
    experimentCount: Optional[int] = None
    featureCount: Optional[int] = None
    launchCount: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


class ScheduledSplitsLaunchDefinitionTypeDef(BaseValidatorModel):
    steps: Optional[List[ScheduledSplitTypeDef]] = None


class SegmentOverrideUnionTypeDef(BaseValidatorModel):
    pass


class ScheduledSplitConfigTypeDef(BaseValidatorModel):
    groupWeights: Mapping[str, int]
    startTime: TimestampTypeDef
    segmentOverrides: Optional[Sequence[SegmentOverrideUnionTypeDef]] = None


class CreateFeatureResponseTypeDef(BaseValidatorModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetFeatureResponseTypeDef(BaseValidatorModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateFeatureResponseTypeDef(BaseValidatorModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExperimentTypeDef(BaseValidatorModel):
    pass


class CreateExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListExperimentsResponseTypeDef(BaseValidatorModel):
    experiments: List[ExperimentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProjectResponseTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetProjectResponseTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProjectDataDeliveryResponseTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateProjectResponseTypeDef(BaseValidatorModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ScheduledSplitsLaunchConfigTypeDef(BaseValidatorModel):
    steps: Sequence[ScheduledSplitConfigTypeDef]


class LaunchTypeDef(BaseValidatorModel):
    pass


class CreateLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLaunchesResponseTypeDef(BaseValidatorModel):
    launches: List[LaunchTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLaunchRequestTypeDef(BaseValidatorModel):
    groups: Sequence[LaunchGroupConfigTypeDef]
    name: str
    project: str
    description: Optional[str] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfigTypeDef]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateLaunchRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str
    description: Optional[str] = None
    groups: Optional[Sequence[LaunchGroupConfigTypeDef]] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfigTypeDef]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfigTypeDef] = None


