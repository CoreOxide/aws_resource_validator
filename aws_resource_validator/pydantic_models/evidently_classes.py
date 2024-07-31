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
from aws_resource_validator.pydantic_models.evidently_constants import *

class EvaluationRequestTypeDef(BaseModel):
    entityId: str
    feature: str
    evaluationContext: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CloudWatchLogsDestinationConfigTypeDef(BaseModel):
    logGroup: Optional[str] = None

class CloudWatchLogsDestinationTypeDef(BaseModel):
    logGroup: Optional[str] = None

class OnlineAbConfigTypeDef(BaseModel):
    controlTreatmentName: Optional[str] = None
    treatmentWeights: Optional[Mapping[str, int]] = None

class TreatmentConfigTypeDef(BaseModel):
    feature: str
    name: str
    variation: str
    description: Optional[str] = None

class LaunchGroupConfigTypeDef(BaseModel):
    feature: str
    name: str
    variation: str
    description: Optional[str] = None

class ProjectAppConfigResourceConfigTypeDef(BaseModel):
    applicationId: Optional[str] = None
    environmentId: Optional[str] = None

class CreateSegmentRequestRequestTypeDef(BaseModel):
    name: str
    pattern: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class SegmentTypeDef(BaseModel):
    arn: str
    createdTime: datetime
    lastUpdatedTime: datetime
    name: str
    pattern: str
    description: Optional[str] = None
    experimentCount: Optional[int] = None
    launchCount: Optional[int] = None
    tags: Optional[Dict[str, str]] = None

class DeleteExperimentRequestRequestTypeDef(BaseModel):
    experiment: str
    project: str

class DeleteFeatureRequestRequestTypeDef(BaseModel):
    feature: str
    project: str

class DeleteLaunchRequestRequestTypeDef(BaseModel):
    launch: str
    project: str

class DeleteProjectRequestRequestTypeDef(BaseModel):
    project: str

class DeleteSegmentRequestRequestTypeDef(BaseModel):
    segment: str

class EvaluateFeatureRequestRequestTypeDef(BaseModel):
    entityId: str
    feature: str
    project: str
    evaluationContext: Optional[str] = None

class VariableValueTypeDef(BaseModel):
    boolValue: Optional[bool] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    stringValue: Optional[str] = None

class EvaluationRuleTypeDef(BaseModel):
    type: str
    name: Optional[str] = None

class ExperimentExecutionTypeDef(BaseModel):
    endedTime: Optional[datetime] = None
    startedTime: Optional[datetime] = None

class ExperimentReportTypeDef(BaseModel):
    content: Optional[str] = None
    metricName: Optional[str] = None
    reportName: Optional[Literal["BayesianInference"]] = None
    treatmentName: Optional[str] = None

class ExperimentResultsDataTypeDef(BaseModel):
    metricName: Optional[str] = None
    resultStat: Optional[ExperimentResultResponseTypeType] = None
    treatmentName: Optional[str] = None
    values: Optional[List[float]] = None

class ExperimentScheduleTypeDef(BaseModel):
    analysisCompleteTime: Optional[datetime] = None

class OnlineAbDefinitionTypeDef(BaseModel):
    controlTreatmentName: Optional[str] = None
    treatmentWeights: Optional[Dict[str, int]] = None

class TreatmentTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    featureVariations: Optional[Dict[str, str]] = None

class GetExperimentRequestRequestTypeDef(BaseModel):
    experiment: str
    project: str

class GetFeatureRequestRequestTypeDef(BaseModel):
    feature: str
    project: str

class GetLaunchRequestRequestTypeDef(BaseModel):
    launch: str
    project: str

class GetProjectRequestRequestTypeDef(BaseModel):
    project: str

class GetSegmentRequestRequestTypeDef(BaseModel):
    segment: str

class LaunchExecutionTypeDef(BaseModel):
    endedTime: Optional[datetime] = None
    startedTime: Optional[datetime] = None

class LaunchGroupTypeDef(BaseModel):
    featureVariations: Dict[str, str]
    name: str
    description: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListExperimentsRequestRequestTypeDef(BaseModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[ExperimentStatusType] = None

class ListFeaturesRequestRequestTypeDef(BaseModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLaunchesRequestRequestTypeDef(BaseModel):
    project: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    status: Optional[LaunchStatusType] = None

class ListProjectsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ProjectSummaryTypeDef(BaseModel):
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

class ListSegmentReferencesRequestRequestTypeDef(BaseModel):
    segment: str
    type: SegmentReferenceResourceTypeType
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RefResourceTypeDef(BaseModel):
    name: str
    type: str
    arn: Optional[str] = None
    endTime: Optional[str] = None
    lastUpdatedOn: Optional[str] = None
    startTime: Optional[str] = None
    status: Optional[str] = None

class ListSegmentsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class MetricDefinitionConfigTypeDef(BaseModel):
    entityIdKey: str
    name: str
    valueKey: str
    eventPattern: Optional[str] = None
    unitLabel: Optional[str] = None

class MetricDefinitionTypeDef(BaseModel):
    entityIdKey: Optional[str] = None
    eventPattern: Optional[str] = None
    name: Optional[str] = None
    unitLabel: Optional[str] = None
    valueKey: Optional[str] = None

class ProjectAppConfigResourceTypeDef(BaseModel):
    applicationId: str
    configurationProfileId: str
    environmentId: str

class S3DestinationConfigTypeDef(BaseModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None

class S3DestinationTypeDef(BaseModel):
    bucket: Optional[str] = None
    prefix: Optional[str] = None

class PutProjectEventsResultEntryTypeDef(BaseModel):
    errorCode: Optional[str] = None
    errorMessage: Optional[str] = None
    eventId: Optional[str] = None

class SegmentOverrideTypeDef(BaseModel):
    evaluationOrder: int
    segment: str
    weights: Mapping[str, int]

class SegmentOverridePaginatorTypeDef(BaseModel):
    evaluationOrder: int
    segment: str
    weights: Dict[str, int]

class StartLaunchRequestRequestTypeDef(BaseModel):
    launch: str
    project: str

class StopExperimentRequestRequestTypeDef(BaseModel):
    experiment: str
    project: str
    desiredState: Optional[ExperimentStopDesiredStateType] = None
    reason: Optional[str] = None

class StopLaunchRequestRequestTypeDef(BaseModel):
    launch: str
    project: str
    desiredState: Optional[LaunchStopDesiredStateType] = None
    reason: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestSegmentPatternRequestRequestTypeDef(BaseModel):
    pattern: str
    payload: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchEvaluateFeatureRequestRequestTypeDef(BaseModel):
    project: str
    requests: Sequence[EvaluationRequestTypeDef]

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class StartExperimentResponseTypeDef(BaseModel):
    startedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopExperimentResponseTypeDef(BaseModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopLaunchResponseTypeDef(BaseModel):
    endedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class TestSegmentPatternResponseTypeDef(BaseModel):
    match: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectRequestRequestTypeDef(BaseModel):
    project: str
    appConfigResource: Optional[ProjectAppConfigResourceConfigTypeDef] = None
    description: Optional[str] = None

class CreateSegmentResponseTypeDef(BaseModel):
    segment: SegmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSegmentResponseTypeDef(BaseModel):
    segment: SegmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSegmentsResponseTypeDef(BaseModel):
    nextToken: str
    segments: List[SegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluateFeatureResponseTypeDef(BaseModel):
    details: str
    reason: str
    value: VariableValueTypeDef
    variation: str
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationResultTypeDef(BaseModel):
    entityId: str
    feature: str
    details: Optional[str] = None
    project: Optional[str] = None
    reason: Optional[str] = None
    value: Optional[VariableValueTypeDef] = None
    variation: Optional[str] = None

class VariationConfigTypeDef(BaseModel):
    name: str
    value: VariableValueTypeDef

class VariationTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[VariableValueTypeDef] = None

class FeatureSummaryTypeDef(BaseModel):
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

class EventTypeDef(BaseModel):
    data: str
    timestamp: TimestampTypeDef
    type: EventTypeType

class GetExperimentResultsRequestRequestTypeDef(BaseModel):
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

class StartExperimentRequestRequestTypeDef(BaseModel):
    analysisCompleteTime: TimestampTypeDef
    experiment: str
    project: str

class GetExperimentResultsResponseTypeDef(BaseModel):
    details: str
    reports: List[ExperimentReportTypeDef]
    resultsData: List[ExperimentResultsDataTypeDef]
    timestamps: List[datetime]
    ResponseMetadata: ResponseMetadataTypeDef

class ListExperimentsRequestListExperimentsPaginateTypeDef(BaseModel):
    project: str
    status: Optional[ExperimentStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFeaturesRequestListFeaturesPaginateTypeDef(BaseModel):
    project: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLaunchesRequestListLaunchesPaginateTypeDef(BaseModel):
    project: str
    status: Optional[LaunchStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsRequestListProjectsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSegmentReferencesRequestListSegmentReferencesPaginateTypeDef(BaseModel):
    segment: str
    type: SegmentReferenceResourceTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSegmentsRequestListSegmentsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProjectsResponseTypeDef(BaseModel):
    nextToken: str
    projects: List[ProjectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListSegmentReferencesResponseTypeDef(BaseModel):
    nextToken: str
    referencedBy: List[RefResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricGoalConfigTypeDef(BaseModel):
    metricDefinition: MetricDefinitionConfigTypeDef
    desiredChange: Optional[ChangeDirectionEnumType] = None

class MetricMonitorConfigTypeDef(BaseModel):
    metricDefinition: MetricDefinitionConfigTypeDef

class MetricGoalTypeDef(BaseModel):
    metricDefinition: MetricDefinitionTypeDef
    desiredChange: Optional[ChangeDirectionEnumType] = None

class MetricMonitorTypeDef(BaseModel):
    metricDefinition: MetricDefinitionTypeDef

class ProjectDataDeliveryConfigTypeDef(BaseModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfigTypeDef] = None
    s3Destination: Optional[S3DestinationConfigTypeDef] = None

class UpdateProjectDataDeliveryRequestRequestTypeDef(BaseModel):
    project: str
    cloudWatchLogs: Optional[CloudWatchLogsDestinationConfigTypeDef] = None
    s3Destination: Optional[S3DestinationConfigTypeDef] = None

class ProjectDataDeliveryTypeDef(BaseModel):
    cloudWatchLogs: Optional[CloudWatchLogsDestinationTypeDef] = None
    s3Destination: Optional[S3DestinationTypeDef] = None

class PutProjectEventsResponseTypeDef(BaseModel):
    eventResults: List[PutProjectEventsResultEntryTypeDef]
    failedEventCount: int
    ResponseMetadata: ResponseMetadataTypeDef

class ScheduledSplitConfigTypeDef(BaseModel):
    groupWeights: Mapping[str, int]
    startTime: TimestampTypeDef
    segmentOverrides: Optional[Sequence[SegmentOverrideTypeDef]] = None

class ScheduledSplitTypeDef(BaseModel):
    startTime: datetime
    groupWeights: Optional[Dict[str, int]] = None
    segmentOverrides: Optional[List[SegmentOverrideTypeDef]] = None

class ScheduledSplitPaginatorTypeDef(BaseModel):
    startTime: datetime
    groupWeights: Optional[Dict[str, int]] = None
    segmentOverrides: Optional[List[SegmentOverridePaginatorTypeDef]] = None

class BatchEvaluateFeatureResponseTypeDef(BaseModel):
    results: List[EvaluationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFeatureRequestRequestTypeDef(BaseModel):
    name: str
    project: str
    variations: Sequence[VariationConfigTypeDef]
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Mapping[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateFeatureRequestRequestTypeDef(BaseModel):
    feature: str
    project: str
    addOrUpdateVariations: Optional[Sequence[VariationConfigTypeDef]] = None
    defaultVariation: Optional[str] = None
    description: Optional[str] = None
    entityOverrides: Optional[Mapping[str, str]] = None
    evaluationStrategy: Optional[FeatureEvaluationStrategyType] = None
    removeVariations: Optional[Sequence[str]] = None

class FeatureTypeDef(BaseModel):
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

class ListFeaturesResponseTypeDef(BaseModel):
    features: List[FeatureSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutProjectEventsRequestRequestTypeDef(BaseModel):
    events: Sequence[EventTypeDef]
    project: str

class CreateExperimentRequestRequestTypeDef(BaseModel):
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

class UpdateExperimentRequestRequestTypeDef(BaseModel):
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

class ExperimentTypeDef(BaseModel):
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

class CreateProjectRequestRequestTypeDef(BaseModel):
    name: str
    appConfigResource: Optional[ProjectAppConfigResourceConfigTypeDef] = None
    dataDelivery: Optional[ProjectDataDeliveryConfigTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ProjectTypeDef(BaseModel):
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

class ScheduledSplitsLaunchConfigTypeDef(BaseModel):
    steps: Sequence[ScheduledSplitConfigTypeDef]

class ScheduledSplitsLaunchDefinitionTypeDef(BaseModel):
    steps: Optional[List[ScheduledSplitTypeDef]] = None

class ScheduledSplitsLaunchDefinitionPaginatorTypeDef(BaseModel):
    steps: Optional[List[ScheduledSplitPaginatorTypeDef]] = None

class CreateFeatureResponseTypeDef(BaseModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetFeatureResponseTypeDef(BaseModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFeatureResponseTypeDef(BaseModel):
    feature: FeatureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExperimentResponseTypeDef(BaseModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExperimentResponseTypeDef(BaseModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListExperimentsResponseTypeDef(BaseModel):
    experiments: List[ExperimentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExperimentResponseTypeDef(BaseModel):
    experiment: ExperimentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProjectResponseTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProjectResponseTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectDataDeliveryResponseTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProjectResponseTypeDef(BaseModel):
    project: ProjectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLaunchRequestRequestTypeDef(BaseModel):
    groups: Sequence[LaunchGroupConfigTypeDef]
    name: str
    project: str
    description: Optional[str] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfigTypeDef]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateLaunchRequestRequestTypeDef(BaseModel):
    launch: str
    project: str
    description: Optional[str] = None
    groups: Optional[Sequence[LaunchGroupConfigTypeDef]] = None
    metricMonitors: Optional[Sequence[MetricMonitorConfigTypeDef]] = None
    randomizationSalt: Optional[str] = None
    scheduledSplitsConfig: Optional[ScheduledSplitsLaunchConfigTypeDef] = None

class LaunchTypeDef(BaseModel):
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

class LaunchPaginatorTypeDef(BaseModel):
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

class CreateLaunchResponseTypeDef(BaseModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLaunchResponseTypeDef(BaseModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchesResponseTypeDef(BaseModel):
    launches: List[LaunchTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLaunchResponseTypeDef(BaseModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLaunchResponseTypeDef(BaseModel):
    launch: LaunchTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLaunchesResponsePaginatorTypeDef(BaseModel):
    launches: List[LaunchPaginatorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

