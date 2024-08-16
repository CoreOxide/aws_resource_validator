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
from aws_resource_validator.pydantic_models.evidently_constants import *

class EvaluationRequestTypeDef(BaseValidatorModel):
    entityId: str
    feature: str
    evaluationContext: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class CreateSegmentRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteExperimentRequestRequestTypeDef(BaseValidatorModel):
    experiment: str
    project: str

class DeleteFeatureRequestRequestTypeDef(BaseValidatorModel):
    feature: str
    project: str

class DeleteLaunchRequestRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str

class DeleteProjectRequestRequestTypeDef(BaseValidatorModel):
    project: str

class DeleteSegmentRequestRequestTypeDef(BaseValidatorModel):
    segment: str

class EvaluateFeatureRequestRequestTypeDef(BaseValidatorModel):
    entityId: str
    feature: str
    project: str
    evaluationContext: Optional[str] = None

class VariableValueTypeDef(BaseValidatorModel):
    boolValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None

class EvaluationRuleTypeDef(BaseValidatorModel):
    type: str
    name: Optional[str] = None

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

class GetExperimentRequestRequestTypeDef(BaseValidatorModel):
    experiment: str
    project: str

class GetFeatureRequestRequestTypeDef(BaseValidatorModel):
    feature: str
    project: str

class GetLaunchRequestRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str

class GetProjectRequestRequestTypeDef(BaseValidatorModel):
    project: str

class GetSegmentRequestRequestTypeDef(BaseValidatorModel):
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

class ListExperimentsRequestRequestTypeDef(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[ExperimentStatusType] = None

class ListFeaturesRequestRequestTypeDef(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLaunchesRequestRequestTypeDef(BaseValidatorModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[LaunchStatusType] = None

class ListProjectsRequestRequestTypeDef(BaseValidatorModel):
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

class ListSegmentReferencesRequestRequestTypeDef(BaseValidatorModel):
    segment: str
    type: SegmentReferenceResourceTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RefResourceTypeDef(BaseValidatorModel):
    name: str
    type: str
    arn: Optional[str] = None
    endTime: Optional[str] = None
    lastUpdatedOn: Optional[str] = None
    startTime: Optional[str] = None
    status: Optional[str] = None

class ListSegmentsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class SegmentOverrideTypeDef(BaseValidatorModel):
    evaluationOrder: int
    segment: str
    weights: Mapping[str, int]

class SegmentOverridePaginatorTypeDef(BaseValidatorModel):
    evaluationOrder: int
    segment: str
    weights: Dict[str, int]

class StartLaunchRequestRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str

class StopExperimentRequestRequestTypeDef(BaseValidatorModel):
    experiment: str
    project: str
    desiredState: Optional[ExperimentStopDesiredStateType] = None
    reason: Optional[str] = None

class StopLaunchRequestRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str
    desiredState: Optional[LaunchStopDesiredStateType] = None
    reason: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestSegmentPatternRequestRequestTypeDef(BaseValidatorModel):
    pattern: str
    payload: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchEvaluateFeatureRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateProjectRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    segments: List[SegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class EventTypeDef(BaseValidatorModel):
    data: str
    timestamp: TimestampTypeDef
    type: EventTypeType

class GetExperimentResultsRequestRequestTypeDef(BaseValidatorModel):
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

class StartExperimentRequestRequestTypeDef(BaseValidatorModel):
    analysisCompleteTime: TimestampTypeDef
    experiment: str
    project: str

class GetExperimentResultsResponseTypeDef(BaseValidatorModel):
    details: str
    reports: List[ExperimentReportTypeDef]
    resultsData: List[ExperimentResultsDataTypeDef]
    timestamps: List[datetime]
    ResponseMetadata: ResponseMetadataTypeDef

class ListExperimentsRequestListExperimentsPaginateTypeDef(BaseValidatorModel):
    project: str
    status: Optional[ExperimentStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFeaturesRequestListFeaturesPaginateTypeDef(BaseValidatorModel):
    project: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchesRequestListLaunchesPaginateTypeDef(BaseValidatorModel):
    project: str
    status: Optional[LaunchStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef(BaseValidatorModel):
    segment: str
    type: SegmentReferenceResourceTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSegmentsRequestListSegmentsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    projects: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSegmentReferencesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    referencedBy: List[RefResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class UpdateProjectDataDeliveryRequestRequestTypeDef(BaseValidatorModel):
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

class ScheduledSplitConfigTypeDef(BaseValidatorModel):
    groupWeights: Mapping[str, int]
    startTime: TimestampTypeDef
    segmentOverrides: Optional[Sequence[SegmentOverrideTypeDef]] = None

class ScheduledSplitTypeDef(BaseValidatorModel):
    startTime: datetime
    groupWeights: Optional[Dict[str, int]] = None
    segmentOverrides: Optional[List[SegmentOverrideTypeDef]] = None

class ScheduledSplitPaginatorTypeDef(BaseValidatorModel):
    startTime: datetime
    groupWeights: Optional[Dict[str, int]] = None
    segmentOverrides: Optional[List[SegmentOverridePaginatorTypeDef]] = None

class BatchEvaluateFeatureResponseTypeDef(BaseValidatorModel):
    results: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFeatureRequestRequestTypeDef(BaseValidatorModel):
    name: str
    project: str
    variations: Sequence[VariationConfigTypeDef]
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Mapping[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateFeatureRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutProjectEventsRequestRequestTypeDef(BaseValidatorModel):
    events: Sequence[EventTypeDef]
    project: str

class CreateExperimentRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateExperimentRequestRequestTypeDef(BaseValidatorModel):
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

class ExperimentTypeDef(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: ExperimentStatusType
    type: Literal["aws.evidently.onlineab"]
    description: Optional[str] = None
    execution: Optional[ExperimentExecutionTypeDef] = None
    metricGoals: Optional[List[MetricGoalTypeDef]] = None
    onlineAbDefinition: Optional[OnlineAbDefinitionTypeDef] = None
    project: Optional[str] = None
    randomizationSalt: Optional[str] = None
    samplingRate: Optional[int] = None
    schedule: Optional[ExperimentScheduleTypeDef] = None
    segment: Optional[str] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    treatments: Optional[List[TreatmentTypeDef]] = None

class CreateProjectRequestRequestTypeDef(BaseValidatorModel):
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

class ScheduledSplitsLaunchConfigTypeDef(BaseValidatorModel):
    steps: Sequence[ScheduledSplitConfigTypeDef]

class ScheduledSplitsLaunchDefinitionTypeDef(BaseValidatorModel):
    steps: Optional[List[ScheduledSplitTypeDef]] = None

class ScheduledSplitsLaunchDefinitionPaginatorTypeDef(BaseValidatorModel):
    steps: Optional[List[ScheduledSplitPaginatorTypeDef]] = None

class CreateFeatureResponseTypeDef(BaseValidatorModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFeatureResponseTypeDef(BaseValidatorModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFeatureResponseTypeDef(BaseValidatorModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentResponseTypeDef(BaseValidatorModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListExperimentsResponseTypeDef(BaseValidatorModel):
    experiments: List[ExperimentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class CreateLaunchRequestRequestTypeDef(BaseValidatorModel):
    groups: Sequence[LaunchGroupConfigTypeDef]
    name: str
    project: str
    description: Optional[str] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfigTypeDef]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateLaunchRequestRequestTypeDef(BaseValidatorModel):
    launch: str
    project: str
    description: Optional[str] = None
    groups: Optional[Sequence[LaunchGroupConfigTypeDef]] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfigTypeDef]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfigTypeDef] = None

class LaunchTypeDef(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: LaunchStatusType
    type: Literal["aws.evidently.splits"]
    description: Optional[str] = None
    execution: Optional[LaunchExecutionTypeDef] = None
    groups: Optional[List[LaunchGroupTypeDef]] = None
    metricMonitors: Optional[List[MetricMonitorTypeDef]] = None
    project: Optional[str] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsDefinition: Optional[ScheduledSplitsLaunchDefinitionTypeDef] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class LaunchPaginatorTypeDef(BaseValidatorModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    status: LaunchStatusType
    type: Literal["aws.evidently.splits"]
    description: Optional[str] = None
    execution: Optional[LaunchExecutionTypeDef] = None
    groups: Optional[List[LaunchGroupTypeDef]] = None
    metricMonitors: Optional[List[MetricMonitorTypeDef]] = None
    project: Optional[str] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsDefinition: Optional[ScheduledSplitsLaunchDefinitionPaginatorTypeDef] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class CreateLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchesResponseTypeDef(BaseValidatorModel):
    launches: List[LaunchTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchResponseTypeDef(BaseValidatorModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchesResponsePaginatorTypeDef(BaseValidatorModel):
    launches: List[LaunchPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

