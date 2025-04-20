from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.personalize.personalize_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AlgorithmImage(BaseValidatorModel):
    dockerURI: str
    name: Optional[str] = None


class AutoMLConfigOutput(BaseValidatorModel):
    metricName: Optional[str] = None
    recipeList: Optional[List[str]] = None


class AutoMLConfig(BaseValidatorModel):
    metricName: Optional[str] = None
    recipeList: Optional[List[str]] = None


class AutoMLResult(BaseValidatorModel):
    bestRecipeArn: Optional[str] = None


class AutoTrainingConfig(BaseValidatorModel):
    schedulingExpression: Optional[str] = None


class BatchInferenceJobConfigOutput(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None


class BatchInferenceJobConfig(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None


class S3DataConfig(BaseValidatorModel):
    path: str
    kmsKeyArn: Optional[str] = None


class BatchInferenceJobSummary(BaseValidatorModel):
    batchInferenceJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None


class BatchSegmentJobSummary(BaseValidatorModel):
    batchSegmentJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None


class CampaignConfigOutput(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    enableMetadataWithRecommendations: Optional[bool] = None
    syncWithLatestSolutionVersion: Optional[bool] = None


class CampaignConfig(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    enableMetadataWithRecommendations: Optional[bool] = None
    syncWithLatestSolutionVersion: Optional[bool] = None


class CampaignSummary(BaseValidatorModel):
    name: Optional[str] = None
    campaignArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class CategoricalHyperParameterRangeOutput(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class CategoricalHyperParameterRange(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class ContinuousHyperParameterRange(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None


class Tag(BaseValidatorModel):
    tagKey: str
    tagValue: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DataSource(BaseValidatorModel):
    dataLocation: Optional[str] = None


class MetricAttribute(BaseValidatorModel):
    eventType: str
    metricName: str
    expression: str


class CreateSchemaRequest(BaseValidatorModel):
    name: str
    schema: str
    domain: Optional[DomainType] = None


class DataDeletionJobSummary(BaseValidatorModel):
    dataDeletionJobArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class DatasetExportJobSummary(BaseValidatorModel):
    datasetExportJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class DatasetGroupSummary(BaseValidatorModel):
    name: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    domain: Optional[DomainType] = None


class DatasetGroup(BaseValidatorModel):
    name: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    roleArn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    domain: Optional[DomainType] = None


class DatasetImportJobSummary(BaseValidatorModel):
    datasetImportJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    importMode: Optional[ImportModeType] = None


class DatasetSchemaSummary(BaseValidatorModel):
    name: Optional[str] = None
    schemaArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None


class DatasetSchema(BaseValidatorModel):
    name: Optional[str] = None
    schemaArn: Optional[str] = None
    schema: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None


class DatasetSummary(BaseValidatorModel):
    name: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetType: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DatasetUpdateSummary(BaseValidatorModel):
    schemaArn: Optional[str] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DefaultCategoricalHyperParameterRange(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None
    isTunable: Optional[bool] = None


class DefaultContinuousHyperParameterRange(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    isTunable: Optional[bool] = None


class DefaultIntegerHyperParameterRange(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[int] = None
    maxValue: Optional[int] = None
    isTunable: Optional[bool] = None


class DeleteCampaignRequest(BaseValidatorModel):
    campaignArn: str


class DeleteDatasetGroupRequest(BaseValidatorModel):
    datasetGroupArn: str


class DeleteDatasetRequest(BaseValidatorModel):
    datasetArn: str


class DeleteEventTrackerRequest(BaseValidatorModel):
    eventTrackerArn: str


class DeleteFilterRequest(BaseValidatorModel):
    filterArn: str


class DeleteMetricAttributionRequest(BaseValidatorModel):
    metricAttributionArn: str


class DeleteRecommenderRequest(BaseValidatorModel):
    recommenderArn: str


class DeleteSchemaRequest(BaseValidatorModel):
    schemaArn: str


class DeleteSolutionRequest(BaseValidatorModel):
    solutionArn: str


class DescribeAlgorithmRequest(BaseValidatorModel):
    algorithmArn: str


class DescribeBatchInferenceJobRequest(BaseValidatorModel):
    batchInferenceJobArn: str


class DescribeBatchSegmentJobRequest(BaseValidatorModel):
    batchSegmentJobArn: str


class DescribeCampaignRequest(BaseValidatorModel):
    campaignArn: str


class DescribeDataDeletionJobRequest(BaseValidatorModel):
    dataDeletionJobArn: str


class DescribeDatasetExportJobRequest(BaseValidatorModel):
    datasetExportJobArn: str


class DescribeDatasetGroupRequest(BaseValidatorModel):
    datasetGroupArn: str


class DescribeDatasetImportJobRequest(BaseValidatorModel):
    datasetImportJobArn: str


class DescribeDatasetRequest(BaseValidatorModel):
    datasetArn: str


class DescribeEventTrackerRequest(BaseValidatorModel):
    eventTrackerArn: str


class EventTracker(BaseValidatorModel):
    name: Optional[str] = None
    eventTrackerArn: Optional[str] = None
    accountId: Optional[str] = None
    trackingId: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DescribeFeatureTransformationRequest(BaseValidatorModel):
    featureTransformationArn: str


class FeatureTransformation(BaseValidatorModel):
    name: Optional[str] = None
    featureTransformationArn: Optional[str] = None
    defaultParameters: Optional[Dict[str, str]] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None


class DescribeFilterRequest(BaseValidatorModel):
    filterArn: str


class Filter(BaseValidatorModel):
    name: Optional[str] = None
    filterArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    datasetGroupArn: Optional[str] = None
    failureReason: Optional[str] = None
    filterExpression: Optional[str] = None
    status: Optional[str] = None


class DescribeMetricAttributionRequest(BaseValidatorModel):
    metricAttributionArn: str


class DescribeRecipeRequest(BaseValidatorModel):
    recipeArn: str


class Recipe(BaseValidatorModel):
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    algorithmArn: Optional[str] = None
    featureTransformationArn: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    recipeType: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DescribeRecommenderRequest(BaseValidatorModel):
    recommenderArn: str


class DescribeSchemaRequest(BaseValidatorModel):
    schemaArn: str


class DescribeSolutionRequest(BaseValidatorModel):
    solutionArn: str


class DescribeSolutionVersionRequest(BaseValidatorModel):
    solutionVersionArn: str


class EventTrackerSummary(BaseValidatorModel):
    name: Optional[str] = None
    eventTrackerArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class FieldsForThemeGeneration(BaseValidatorModel):
    itemName: str


class FilterSummary(BaseValidatorModel):
    name: Optional[str] = None
    filterArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    datasetGroupArn: Optional[str] = None
    failureReason: Optional[str] = None
    status: Optional[str] = None


class GetSolutionMetricsRequest(BaseValidatorModel):
    solutionVersionArn: str


class HPOObjective(BaseValidatorModel):
    type: Optional[str] = None
    metricName: Optional[str] = None
    metricRegex: Optional[str] = None


class HPOResourceConfig(BaseValidatorModel):
    maxNumberOfTrainingJobs: Optional[str] = None
    maxParallelTrainingJobs: Optional[str] = None


class IntegerHyperParameterRange(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[int] = None
    maxValue: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBatchInferenceJobsRequest(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBatchSegmentJobsRequest(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCampaignsRequest(BaseValidatorModel):
    solutionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataDeletionJobsRequest(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetExportJobsRequest(BaseValidatorModel):
    datasetArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetGroupsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetImportJobsRequest(BaseValidatorModel):
    datasetArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequest(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEventTrackersRequest(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFiltersRequest(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMetricAttributionMetricsRequest(BaseValidatorModel):
    metricAttributionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMetricAttributionsRequest(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MetricAttributionSummary(BaseValidatorModel):
    name: Optional[str] = None
    metricAttributionArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class ListRecipesRequest(BaseValidatorModel):
    recipeProvider: Optional[Literal['SERVICE']] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    domain: Optional[DomainType] = None


class RecipeSummary(BaseValidatorModel):
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None


class ListRecommendersRequest(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSchemasRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSolutionVersionsRequest(BaseValidatorModel):
    solutionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SolutionVersionSummary(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    status: Optional[str] = None
    trainingMode: Optional[TrainingModeType] = None
    trainingType: Optional[TrainingTypeType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class ListSolutionsRequest(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SolutionSummary(BaseValidatorModel):
    name: Optional[str] = None
    solutionArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    recipeArn: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class OptimizationObjective(BaseValidatorModel):
    itemAttribute: Optional[str] = None
    objectiveSensitivity: Optional[ObjectiveSensitivityType] = None


class TrainingDataConfigOutput(BaseValidatorModel):
    excludedDatasetColumns: Optional[Dict[str, List[str]]] = None


class TrainingDataConfig(BaseValidatorModel):
    excludedDatasetColumns: Optional[Dict[str, List[str]]] = None


class TunedHPOParams(BaseValidatorModel):
    algorithmHyperParameters: Optional[Dict[str, str]] = None


class StartRecommenderRequest(BaseValidatorModel):
    recommenderArn: str


class StopRecommenderRequest(BaseValidatorModel):
    recommenderArn: str


class StopSolutionVersionCreationRequest(BaseValidatorModel):
    solutionVersionArn: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateDatasetRequest(BaseValidatorModel):
    datasetArn: str
    schemaArn: str


class SolutionUpdateConfig(BaseValidatorModel):
    autoTrainingConfig: Optional[AutoTrainingConfig] = None

BatchInferenceJobConfigUnion = Union[BatchInferenceJobConfig, BatchInferenceJobConfigOutput]


class BatchInferenceJobInput(BaseValidatorModel):
    s3DataSource: S3DataConfig


class BatchInferenceJobOutput(BaseValidatorModel):
    s3DataDestination: S3DataConfig


class BatchSegmentJobInput(BaseValidatorModel):
    s3DataSource: S3DataConfig


class BatchSegmentJobOutput(BaseValidatorModel):
    s3DataDestination: S3DataConfig


class DatasetExportJobOutput(BaseValidatorModel):
    s3DataDestination: S3DataConfig


class MetricAttributionOutput(BaseValidatorModel):
    roleArn: str
    s3DataDestination: Optional[S3DataConfig] = None


class CampaignUpdateSummary(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigOutput] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

CampaignConfigUnion = Union[CampaignConfig, CampaignConfigOutput]


class CreateDatasetGroupRequest(BaseValidatorModel):
    name: str
    roleArn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    domain: Optional[DomainType] = None
    tags: Optional[List[Tag]] = None


class CreateDatasetRequest(BaseValidatorModel):
    name: str
    schemaArn: str
    datasetGroupArn: str
    datasetType: str
    tags: Optional[List[Tag]] = None


class CreateEventTrackerRequest(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    tags: Optional[List[Tag]] = None


class CreateFilterRequest(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    filterExpression: str
    tags: Optional[List[Tag]] = None


class CreateSolutionVersionRequest(BaseValidatorModel):
    solutionArn: str
    name: Optional[str] = None
    trainingMode: Optional[TrainingModeType] = None
    tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class CreateBatchInferenceJobResponse(BaseValidatorModel):
    batchInferenceJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateBatchSegmentJobResponse(BaseValidatorModel):
    batchSegmentJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateCampaignResponse(BaseValidatorModel):
    campaignArn: str
    ResponseMetadata: ResponseMetadata


class CreateDataDeletionJobResponse(BaseValidatorModel):
    dataDeletionJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetExportJobResponse(BaseValidatorModel):
    datasetExportJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetGroupResponse(BaseValidatorModel):
    datasetGroupArn: str
    domain: DomainType
    ResponseMetadata: ResponseMetadata


class CreateDatasetImportJobResponse(BaseValidatorModel):
    datasetImportJobArn: str
    ResponseMetadata: ResponseMetadata


class CreateDatasetResponse(BaseValidatorModel):
    datasetArn: str
    ResponseMetadata: ResponseMetadata


class CreateEventTrackerResponse(BaseValidatorModel):
    eventTrackerArn: str
    trackingId: str
    ResponseMetadata: ResponseMetadata


class CreateFilterResponse(BaseValidatorModel):
    filterArn: str
    ResponseMetadata: ResponseMetadata


class CreateMetricAttributionResponse(BaseValidatorModel):
    metricAttributionArn: str
    ResponseMetadata: ResponseMetadata


class CreateRecommenderResponse(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadata


class CreateSchemaResponse(BaseValidatorModel):
    schemaArn: str
    ResponseMetadata: ResponseMetadata


class CreateSolutionResponse(BaseValidatorModel):
    solutionArn: str
    ResponseMetadata: ResponseMetadata


class CreateSolutionVersionResponse(BaseValidatorModel):
    solutionVersionArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetSolutionMetricsResponse(BaseValidatorModel):
    solutionVersionArn: str
    metrics: Dict[str, float]
    ResponseMetadata: ResponseMetadata


class ListBatchInferenceJobsResponse(BaseValidatorModel):
    batchInferenceJobs: List[BatchInferenceJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListBatchSegmentJobsResponse(BaseValidatorModel):
    batchSegmentJobs: List[BatchSegmentJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCampaignsResponse(BaseValidatorModel):
    campaigns: List[CampaignSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class StartRecommenderResponse(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadata


class StopRecommenderResponse(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadata


class UpdateCampaignResponse(BaseValidatorModel):
    campaignArn: str
    ResponseMetadata: ResponseMetadata


class UpdateDatasetResponse(BaseValidatorModel):
    datasetArn: str
    ResponseMetadata: ResponseMetadata


class UpdateMetricAttributionResponse(BaseValidatorModel):
    metricAttributionArn: str
    ResponseMetadata: ResponseMetadata


class UpdateRecommenderResponse(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadata


class UpdateSolutionResponse(BaseValidatorModel):
    solutionArn: str
    ResponseMetadata: ResponseMetadata


class CreateDataDeletionJobRequest(BaseValidatorModel):
    jobName: str
    datasetGroupArn: str
    dataSource: DataSource
    roleArn: str
    tags: Optional[List[Tag]] = None


class CreateDatasetImportJobRequest(BaseValidatorModel):
    jobName: str
    datasetArn: str
    dataSource: DataSource
    roleArn: str
    tags: Optional[List[Tag]] = None
    importMode: Optional[ImportModeType] = None
    publishAttributionMetricsToS3: Optional[bool] = None


class DataDeletionJob(BaseValidatorModel):
    jobName: Optional[str] = None
    dataDeletionJobArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    dataSource: Optional[DataSource] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    numDeleted: Optional[int] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class DatasetImportJob(BaseValidatorModel):
    jobName: Optional[str] = None
    datasetImportJobArn: Optional[str] = None
    datasetArn: Optional[str] = None
    dataSource: Optional[DataSource] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    importMode: Optional[ImportModeType] = None
    publishAttributionMetricsToS3: Optional[bool] = None


class ListMetricAttributionMetricsResponse(BaseValidatorModel):
    metrics: List[MetricAttribute]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDataDeletionJobsResponse(BaseValidatorModel):
    dataDeletionJobs: List[DataDeletionJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDatasetExportJobsResponse(BaseValidatorModel):
    datasetExportJobs: List[DatasetExportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDatasetGroupsResponse(BaseValidatorModel):
    datasetGroups: List[DatasetGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeDatasetGroupResponse(BaseValidatorModel):
    datasetGroup: DatasetGroup
    ResponseMetadata: ResponseMetadata


class ListDatasetImportJobsResponse(BaseValidatorModel):
    datasetImportJobs: List[DatasetImportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSchemasResponse(BaseValidatorModel):
    schemas: List[DatasetSchemaSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeSchemaResponse(BaseValidatorModel):
    schema: DatasetSchema
    ResponseMetadata: ResponseMetadata


class ListDatasetsResponse(BaseValidatorModel):
    datasets: List[DatasetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Dataset(BaseValidatorModel):
    name: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    datasetType: Optional[str] = None
    schemaArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    latestDatasetUpdate: Optional[DatasetUpdateSummary] = None
    trackingId: Optional[str] = None


class DefaultHyperParameterRanges(BaseValidatorModel):
    integerHyperParameterRanges: Optional[List[DefaultIntegerHyperParameterRange]] = None
    continuousHyperParameterRanges: Optional[List[DefaultContinuousHyperParameterRange]] = None
    categoricalHyperParameterRanges: Optional[List[DefaultCategoricalHyperParameterRange]] = None


class DescribeEventTrackerResponse(BaseValidatorModel):
    eventTracker: EventTracker
    ResponseMetadata: ResponseMetadata


class DescribeFeatureTransformationResponse(BaseValidatorModel):
    featureTransformation: FeatureTransformation
    ResponseMetadata: ResponseMetadata


class DescribeFilterResponse(BaseValidatorModel):
    filter: Filter
    ResponseMetadata: ResponseMetadata


class DescribeRecipeResponse(BaseValidatorModel):
    recipe: Recipe
    ResponseMetadata: ResponseMetadata


class ListEventTrackersResponse(BaseValidatorModel):
    eventTrackers: List[EventTrackerSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ThemeGenerationConfig(BaseValidatorModel):
    fieldsForThemeGeneration: FieldsForThemeGeneration


class ListFiltersResponse(BaseValidatorModel):
    Filters: List[FilterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class HyperParameterRangesOutput(BaseValidatorModel):
    integerHyperParameterRanges: Optional[List[IntegerHyperParameterRange]] = None
    continuousHyperParameterRanges: Optional[List[ContinuousHyperParameterRange]] = None
    categoricalHyperParameterRanges: Optional[List[CategoricalHyperParameterRangeOutput]] = None


class HyperParameterRanges(BaseValidatorModel):
    integerHyperParameterRanges: Optional[List[IntegerHyperParameterRange]] = None
    continuousHyperParameterRanges: Optional[List[ContinuousHyperParameterRange]] = None
    categoricalHyperParameterRanges: Optional[List[CategoricalHyperParameterRange]] = None


class ListBatchInferenceJobsRequestPaginate(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBatchSegmentJobsRequestPaginate(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCampaignsRequestPaginate(BaseValidatorModel):
    solutionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetExportJobsRequestPaginate(BaseValidatorModel):
    datasetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetGroupsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetImportJobsRequestPaginate(BaseValidatorModel):
    datasetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDatasetsRequestPaginate(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventTrackersRequestPaginate(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFiltersRequestPaginate(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMetricAttributionMetricsRequestPaginate(BaseValidatorModel):
    metricAttributionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMetricAttributionsRequestPaginate(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecipesRequestPaginate(BaseValidatorModel):
    recipeProvider: Optional[Literal['SERVICE']] = None
    domain: Optional[DomainType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecommendersRequestPaginate(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemasRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolutionVersionsRequestPaginate(BaseValidatorModel):
    solutionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSolutionsRequestPaginate(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMetricAttributionsResponse(BaseValidatorModel):
    metricAttributions: List[MetricAttributionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRecipesResponse(BaseValidatorModel):
    recipes: List[RecipeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolutionVersionsResponse(BaseValidatorModel):
    solutionVersions: List[SolutionVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSolutionsResponse(BaseValidatorModel):
    solutions: List[SolutionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RecommenderConfigOutput(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    minRecommendationRequestsPerSecond: Optional[int] = None
    trainingDataConfig: Optional[TrainingDataConfigOutput] = None
    enableMetadataWithRecommendations: Optional[bool] = None


class RecommenderConfig(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    minRecommendationRequestsPerSecond: Optional[int] = None
    trainingDataConfig: Optional[TrainingDataConfig] = None
    enableMetadataWithRecommendations: Optional[bool] = None


class SolutionUpdateSummary(BaseValidatorModel):
    solutionUpdateConfig: Optional[SolutionUpdateConfig] = None
    status: Optional[str] = None
    performAutoTraining: Optional[bool] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class UpdateSolutionRequest(BaseValidatorModel):
    solutionArn: str
    performAutoTraining: Optional[bool] = None
    solutionUpdateConfig: Optional[SolutionUpdateConfig] = None


class BatchSegmentJob(BaseValidatorModel):
    jobName: Optional[str] = None
    batchSegmentJobArn: Optional[str] = None
    filterArn: Optional[str] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    numResults: Optional[int] = None
    jobInput: Optional[BatchSegmentJobInput] = None
    jobOutput: Optional[BatchSegmentJobOutput] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class CreateBatchSegmentJobRequest(BaseValidatorModel):
    jobName: str
    solutionVersionArn: str
    jobInput: BatchSegmentJobInput
    jobOutput: BatchSegmentJobOutput
    roleArn: str
    filterArn: Optional[str] = None
    numResults: Optional[int] = None
    tags: Optional[List[Tag]] = None


class CreateDatasetExportJobRequest(BaseValidatorModel):
    jobName: str
    datasetArn: str
    roleArn: str
    jobOutput: DatasetExportJobOutput
    ingestionMode: Optional[IngestionModeType] = None
    tags: Optional[List[Tag]] = None


class DatasetExportJob(BaseValidatorModel):
    jobName: Optional[str] = None
    datasetExportJobArn: Optional[str] = None
    datasetArn: Optional[str] = None
    ingestionMode: Optional[IngestionModeType] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    jobOutput: Optional[DatasetExportJobOutput] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class CreateMetricAttributionRequest(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    metrics: List[MetricAttribute]
    metricsOutputConfig: MetricAttributionOutput


class MetricAttribution(BaseValidatorModel):
    name: Optional[str] = None
    metricAttributionArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    metricsOutputConfig: Optional[MetricAttributionOutput] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class UpdateMetricAttributionRequest(BaseValidatorModel):
    addMetrics: Optional[List[MetricAttribute]] = None
    removeMetrics: Optional[List[str]] = None
    metricsOutputConfig: Optional[MetricAttributionOutput] = None
    metricAttributionArn: Optional[str] = None


class Campaign(BaseValidatorModel):
    name: Optional[str] = None
    campaignArn: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigOutput] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    latestCampaignUpdate: Optional[CampaignUpdateSummary] = None


class CreateCampaignRequest(BaseValidatorModel):
    name: str
    solutionVersionArn: str
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigUnion] = None
    tags: Optional[List[Tag]] = None


class UpdateCampaignRequest(BaseValidatorModel):
    campaignArn: str
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigUnion] = None


class DescribeDataDeletionJobResponse(BaseValidatorModel):
    dataDeletionJob: DataDeletionJob
    ResponseMetadata: ResponseMetadata


class DescribeDatasetImportJobResponse(BaseValidatorModel):
    datasetImportJob: DatasetImportJob
    ResponseMetadata: ResponseMetadata


class DescribeDatasetResponse(BaseValidatorModel):
    dataset: Dataset
    ResponseMetadata: ResponseMetadata


class Algorithm(BaseValidatorModel):
    name: Optional[str] = None
    algorithmArn: Optional[str] = None
    algorithmImage: Optional[AlgorithmImage] = None
    defaultHyperParameters: Optional[Dict[str, str]] = None
    defaultHyperParameterRanges: Optional[DefaultHyperParameterRanges] = None
    defaultResourceConfig: Optional[Dict[str, str]] = None
    trainingInputMode: Optional[str] = None
    roleArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class BatchInferenceJob(BaseValidatorModel):
    jobName: Optional[str] = None
    batchInferenceJobArn: Optional[str] = None
    filterArn: Optional[str] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    numResults: Optional[int] = None
    jobInput: Optional[BatchInferenceJobInput] = None
    jobOutput: Optional[BatchInferenceJobOutput] = None
    batchInferenceJobConfig: Optional[BatchInferenceJobConfigOutput] = None
    roleArn: Optional[str] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None
    themeGenerationConfig: Optional[ThemeGenerationConfig] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class CreateBatchInferenceJobRequest(BaseValidatorModel):
    jobName: str
    solutionVersionArn: str
    jobInput: BatchInferenceJobInput
    jobOutput: BatchInferenceJobOutput
    roleArn: str
    filterArn: Optional[str] = None
    numResults: Optional[int] = None
    batchInferenceJobConfig: Optional[BatchInferenceJobConfigUnion] = None
    tags: Optional[List[Tag]] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None
    themeGenerationConfig: Optional[ThemeGenerationConfig] = None


class HPOConfigOutput(BaseValidatorModel):
    hpoObjective: Optional[HPOObjective] = None
    hpoResourceConfig: Optional[HPOResourceConfig] = None
    algorithmHyperParameterRanges: Optional[HyperParameterRangesOutput] = None


class HPOConfig(BaseValidatorModel):
    hpoObjective: Optional[HPOObjective] = None
    hpoResourceConfig: Optional[HPOResourceConfig] = None
    algorithmHyperParameterRanges: Optional[HyperParameterRanges] = None


class RecommenderSummary(BaseValidatorModel):
    name: Optional[str] = None
    recommenderArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    recipeArn: Optional[str] = None
    recommenderConfig: Optional[RecommenderConfigOutput] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class RecommenderUpdateSummary(BaseValidatorModel):
    recommenderConfig: Optional[RecommenderConfigOutput] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None

RecommenderConfigUnion = Union[RecommenderConfig, RecommenderConfigOutput]


class DescribeBatchSegmentJobResponse(BaseValidatorModel):
    batchSegmentJob: BatchSegmentJob
    ResponseMetadata: ResponseMetadata


class DescribeDatasetExportJobResponse(BaseValidatorModel):
    datasetExportJob: DatasetExportJob
    ResponseMetadata: ResponseMetadata


class DescribeMetricAttributionResponse(BaseValidatorModel):
    metricAttribution: MetricAttribution
    ResponseMetadata: ResponseMetadata


class DescribeCampaignResponse(BaseValidatorModel):
    campaign: Campaign
    ResponseMetadata: ResponseMetadata


class DescribeAlgorithmResponse(BaseValidatorModel):
    algorithm: Algorithm
    ResponseMetadata: ResponseMetadata


class DescribeBatchInferenceJobResponse(BaseValidatorModel):
    batchInferenceJob: BatchInferenceJob
    ResponseMetadata: ResponseMetadata


class SolutionConfigOutput(BaseValidatorModel):
    eventValueThreshold: Optional[str] = None
    hpoConfig: Optional[HPOConfigOutput] = None
    algorithmHyperParameters: Optional[Dict[str, str]] = None
    featureTransformationParameters: Optional[Dict[str, str]] = None
    autoMLConfig: Optional[AutoMLConfigOutput] = None
    optimizationObjective: Optional[OptimizationObjective] = None
    trainingDataConfig: Optional[TrainingDataConfigOutput] = None
    autoTrainingConfig: Optional[AutoTrainingConfig] = None


class SolutionConfig(BaseValidatorModel):
    eventValueThreshold: Optional[str] = None
    hpoConfig: Optional[HPOConfig] = None
    algorithmHyperParameters: Optional[Dict[str, str]] = None
    featureTransformationParameters: Optional[Dict[str, str]] = None
    autoMLConfig: Optional[AutoMLConfig] = None
    optimizationObjective: Optional[OptimizationObjective] = None
    trainingDataConfig: Optional[TrainingDataConfig] = None
    autoTrainingConfig: Optional[AutoTrainingConfig] = None


class ListRecommendersResponse(BaseValidatorModel):
    recommenders: List[RecommenderSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Recommender(BaseValidatorModel):
    recommenderArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    recommenderConfig: Optional[RecommenderConfigOutput] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    latestRecommenderUpdate: Optional[RecommenderUpdateSummary] = None
    modelMetrics: Optional[Dict[str, float]] = None


class CreateRecommenderRequest(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    recipeArn: str
    recommenderConfig: Optional[RecommenderConfigUnion] = None
    tags: Optional[List[Tag]] = None


class UpdateRecommenderRequest(BaseValidatorModel):
    recommenderArn: str
    recommenderConfig: RecommenderConfigUnion


class Solution(BaseValidatorModel):
    name: Optional[str] = None
    solutionArn: Optional[str] = None
    performHPO: Optional[bool] = None
    performAutoML: Optional[bool] = None
    performAutoTraining: Optional[bool] = None
    recipeArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    eventType: Optional[str] = None
    solutionConfig: Optional[SolutionConfigOutput] = None
    autoMLResult: Optional[AutoMLResult] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    latestSolutionVersion: Optional[SolutionVersionSummary] = None
    latestSolutionUpdate: Optional[SolutionUpdateSummary] = None


class SolutionVersion(BaseValidatorModel):
    name: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    solutionArn: Optional[str] = None
    performHPO: Optional[bool] = None
    performAutoML: Optional[bool] = None
    recipeArn: Optional[str] = None
    eventType: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    solutionConfig: Optional[SolutionConfigOutput] = None
    trainingHours: Optional[float] = None
    trainingMode: Optional[TrainingModeType] = None
    tunedHPOParams: Optional[TunedHPOParams] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    trainingType: Optional[TrainingTypeType] = None

SolutionConfigUnion = Union[SolutionConfig, SolutionConfigOutput]


class DescribeRecommenderResponse(BaseValidatorModel):
    recommender: Recommender
    ResponseMetadata: ResponseMetadata


class DescribeSolutionResponse(BaseValidatorModel):
    solution: Solution
    ResponseMetadata: ResponseMetadata


class DescribeSolutionVersionResponse(BaseValidatorModel):
    solutionVersion: SolutionVersion
    ResponseMetadata: ResponseMetadata


class CreateSolutionRequest(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    performHPO: Optional[bool] = None
    performAutoML: Optional[bool] = None
    performAutoTraining: Optional[bool] = None
    recipeArn: Optional[str] = None
    eventType: Optional[str] = None
    solutionConfig: Optional[SolutionConfigUnion] = None
    tags: Optional[List[Tag]] = None