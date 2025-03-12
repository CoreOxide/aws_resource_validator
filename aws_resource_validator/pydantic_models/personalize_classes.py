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
from aws_resource_validator.pydantic_models.personalize_constants import *

class AlgorithmImageTypeDef(BaseValidatorModel):
    dockerURI: str
    name: Optional[str] = None


class AutoMLConfigOutputTypeDef(BaseValidatorModel):
    metricName: Optional[str] = None
    recipeList: Optional[List[str]] = None


class AutoMLConfigTypeDef(BaseValidatorModel):
    metricName: Optional[str] = None
    recipeList: Optional[Sequence[str]] = None


class AutoMLResultTypeDef(BaseValidatorModel):
    bestRecipeArn: Optional[str] = None


class AutoTrainingConfigTypeDef(BaseValidatorModel):
    schedulingExpression: Optional[str] = None


class BatchInferenceJobConfigOutputTypeDef(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None


class BatchInferenceJobConfigTypeDef(BaseValidatorModel):
    itemExplorationConfig: Optional[Mapping[str, str]] = None


class S3DataConfigTypeDef(BaseValidatorModel):
    path: str
    kmsKeyArn: Optional[str] = None


class BatchInferenceJobSummaryTypeDef(BaseValidatorModel):
    batchInferenceJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None


class BatchSegmentJobSummaryTypeDef(BaseValidatorModel):
    batchSegmentJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None


class CampaignConfigOutputTypeDef(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    enableMetadataWithRecommendations: Optional[bool] = None
    syncWithLatestSolutionVersion: Optional[bool] = None


class CampaignConfigTypeDef(BaseValidatorModel):
    itemExplorationConfig: Optional[Mapping[str, str]] = None
    enableMetadataWithRecommendations: Optional[bool] = None
    syncWithLatestSolutionVersion: Optional[bool] = None


class CampaignSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    campaignArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class CategoricalHyperParameterRangeOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class CategoricalHyperParameterRangeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None


class ContinuousHyperParameterRangeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None


class TagTypeDef(BaseValidatorModel):
    tagKey: str
    tagValue: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DataSourceTypeDef(BaseValidatorModel):
    dataLocation: Optional[str] = None


class MetricAttributeTypeDef(BaseValidatorModel):
    eventType: str
    metricName: str
    expression: str


class CreateSchemaRequestTypeDef(BaseValidatorModel):
    name: str
    schema: str
    domain: Optional[DomainType] = None


class DataDeletionJobSummaryTypeDef(BaseValidatorModel):
    dataDeletionJobArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class DatasetExportJobSummaryTypeDef(BaseValidatorModel):
    datasetExportJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class DatasetGroupSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    domain: Optional[DomainType] = None


class DatasetGroupTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    roleArn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    domain: Optional[DomainType] = None


class DatasetImportJobSummaryTypeDef(BaseValidatorModel):
    datasetImportJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    importMode: Optional[ImportModeType] = None


class DatasetSchemaSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    schemaArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None


class DatasetSchemaTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    schemaArn: Optional[str] = None
    schema: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None


class DatasetSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetType: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DatasetUpdateSummaryTypeDef(BaseValidatorModel):
    schemaArn: Optional[str] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DefaultCategoricalHyperParameterRangeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None
    isTunable: Optional[bool] = None


class DefaultContinuousHyperParameterRangeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    isTunable: Optional[bool] = None


class DefaultIntegerHyperParameterRangeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[int] = None
    maxValue: Optional[int] = None
    isTunable: Optional[bool] = None


class DeleteCampaignRequestTypeDef(BaseValidatorModel):
    campaignArn: str


class DeleteDatasetGroupRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: str


class DeleteDatasetRequestTypeDef(BaseValidatorModel):
    datasetArn: str


class DeleteEventTrackerRequestTypeDef(BaseValidatorModel):
    eventTrackerArn: str


class DeleteFilterRequestTypeDef(BaseValidatorModel):
    filterArn: str


class DeleteMetricAttributionRequestTypeDef(BaseValidatorModel):
    metricAttributionArn: str


class DeleteRecommenderRequestTypeDef(BaseValidatorModel):
    recommenderArn: str


class DeleteSchemaRequestTypeDef(BaseValidatorModel):
    schemaArn: str


class DeleteSolutionRequestTypeDef(BaseValidatorModel):
    solutionArn: str


class DescribeAlgorithmRequestTypeDef(BaseValidatorModel):
    algorithmArn: str


class DescribeBatchInferenceJobRequestTypeDef(BaseValidatorModel):
    batchInferenceJobArn: str


class DescribeBatchSegmentJobRequestTypeDef(BaseValidatorModel):
    batchSegmentJobArn: str


class DescribeCampaignRequestTypeDef(BaseValidatorModel):
    campaignArn: str


class DescribeDataDeletionJobRequestTypeDef(BaseValidatorModel):
    dataDeletionJobArn: str


class DescribeDatasetExportJobRequestTypeDef(BaseValidatorModel):
    datasetExportJobArn: str


class DescribeDatasetGroupRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: str


class DescribeDatasetImportJobRequestTypeDef(BaseValidatorModel):
    datasetImportJobArn: str


class DescribeDatasetRequestTypeDef(BaseValidatorModel):
    datasetArn: str


class DescribeEventTrackerRequestTypeDef(BaseValidatorModel):
    eventTrackerArn: str


class EventTrackerTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    eventTrackerArn: Optional[str] = None
    accountId: Optional[str] = None
    trackingId: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DescribeFeatureTransformationRequestTypeDef(BaseValidatorModel):
    featureTransformationArn: str


class FeatureTransformationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    featureTransformationArn: Optional[str] = None
    defaultParameters: Optional[Dict[str, str]] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None


class DescribeFilterRequestTypeDef(BaseValidatorModel):
    filterArn: str


class FilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    filterArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    datasetGroupArn: Optional[str] = None
    failureReason: Optional[str] = None
    filterExpression: Optional[str] = None
    status: Optional[str] = None


class DescribeMetricAttributionRequestTypeDef(BaseValidatorModel):
    metricAttributionArn: str


class DescribeRecipeRequestTypeDef(BaseValidatorModel):
    recipeArn: str


class RecipeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    algorithmArn: Optional[str] = None
    featureTransformationArn: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    recipeType: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None


class DescribeRecommenderRequestTypeDef(BaseValidatorModel):
    recommenderArn: str


class DescribeSchemaRequestTypeDef(BaseValidatorModel):
    schemaArn: str


class DescribeSolutionRequestTypeDef(BaseValidatorModel):
    solutionArn: str


class DescribeSolutionVersionRequestTypeDef(BaseValidatorModel):
    solutionVersionArn: str


class EventTrackerSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    eventTrackerArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class FieldsForThemeGenerationTypeDef(BaseValidatorModel):
    itemName: str


class FilterSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    filterArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    datasetGroupArn: Optional[str] = None
    failureReason: Optional[str] = None
    status: Optional[str] = None


class GetSolutionMetricsRequestTypeDef(BaseValidatorModel):
    solutionVersionArn: str


class HPOResourceConfigTypeDef(BaseValidatorModel):
    maxNumberOfTrainingJobs: Optional[str] = None
    maxParallelTrainingJobs: Optional[str] = None


class IntegerHyperParameterRangeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    minValue: Optional[int] = None
    maxValue: Optional[int] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListBatchInferenceJobsRequestTypeDef(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListBatchSegmentJobsRequestTypeDef(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCampaignsRequestTypeDef(BaseValidatorModel):
    solutionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataDeletionJobsRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetExportJobsRequestTypeDef(BaseValidatorModel):
    datasetArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetGroupsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetImportJobsRequestTypeDef(BaseValidatorModel):
    datasetArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDatasetsRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEventTrackersRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListFiltersRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMetricAttributionMetricsRequestTypeDef(BaseValidatorModel):
    metricAttributionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMetricAttributionsRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MetricAttributionSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    metricAttributionArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class ListRecipesRequestTypeDef(BaseValidatorModel):
    recipeProvider: Optional[Literal["SERVICE"]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    domain: Optional[DomainType] = None


class RecipeSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None


class ListRecommendersRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSchemasRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSolutionVersionsRequestTypeDef(BaseValidatorModel):
    solutionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SolutionVersionSummaryTypeDef(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    status: Optional[str] = None
    trainingMode: Optional[TrainingModeType] = None
    trainingType: Optional[TrainingTypeType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class ListSolutionsRequestTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class SolutionSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    solutionArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    recipeArn: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class OptimizationObjectiveTypeDef(BaseValidatorModel):
    itemAttribute: Optional[str] = None
    objectiveSensitivity: Optional[ObjectiveSensitivityType] = None


class TrainingDataConfigOutputTypeDef(BaseValidatorModel):
    excludedDatasetColumns: Optional[Dict[str, List[str]]] = None


class TrainingDataConfigTypeDef(BaseValidatorModel):
    excludedDatasetColumns: Optional[Mapping[str, Sequence[str]]] = None


class TunedHPOParamsTypeDef(BaseValidatorModel):
    algorithmHyperParameters: Optional[Dict[str, str]] = None


class StartRecommenderRequestTypeDef(BaseValidatorModel):
    recommenderArn: str


class StopRecommenderRequestTypeDef(BaseValidatorModel):
    recommenderArn: str


class StopSolutionVersionCreationRequestTypeDef(BaseValidatorModel):
    solutionVersionArn: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateDatasetRequestTypeDef(BaseValidatorModel):
    datasetArn: str
    schemaArn: str


class SolutionUpdateConfigTypeDef(BaseValidatorModel):
    autoTrainingConfig: Optional[AutoTrainingConfigTypeDef] = None


class BatchInferenceJobInputTypeDef(BaseValidatorModel):
    s3DataSource: S3DataConfigTypeDef


class BatchInferenceJobOutputTypeDef(BaseValidatorModel):
    s3DataDestination: S3DataConfigTypeDef


class BatchSegmentJobInputTypeDef(BaseValidatorModel):
    s3DataSource: S3DataConfigTypeDef


class BatchSegmentJobOutputTypeDef(BaseValidatorModel):
    s3DataDestination: S3DataConfigTypeDef


class DatasetExportJobOutputTypeDef(BaseValidatorModel):
    s3DataDestination: S3DataConfigTypeDef


class MetricAttributionOutputTypeDef(BaseValidatorModel):
    roleArn: str
    s3DataDestination: Optional[S3DataConfigTypeDef] = None


class CampaignUpdateSummaryTypeDef(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigOutputTypeDef] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class CreateDatasetGroupRequestTypeDef(BaseValidatorModel):
    name: str
    roleArn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    domain: Optional[DomainType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateDatasetRequestTypeDef(BaseValidatorModel):
    name: str
    schemaArn: str
    datasetGroupArn: str
    datasetType: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateEventTrackerRequestTypeDef(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateFilterRequestTypeDef(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    filterExpression: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateSolutionVersionRequestTypeDef(BaseValidatorModel):
    solutionArn: str
    name: Optional[str] = None
    trainingMode: Optional[TrainingModeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class CreateBatchInferenceJobResponseTypeDef(BaseValidatorModel):
    batchInferenceJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBatchSegmentJobResponseTypeDef(BaseValidatorModel):
    batchSegmentJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCampaignResponseTypeDef(BaseValidatorModel):
    campaignArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataDeletionJobResponseTypeDef(BaseValidatorModel):
    dataDeletionJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetExportJobResponseTypeDef(BaseValidatorModel):
    datasetExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetGroupResponseTypeDef(BaseValidatorModel):
    datasetGroupArn: str
    domain: DomainType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetImportJobResponseTypeDef(BaseValidatorModel):
    datasetImportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDatasetResponseTypeDef(BaseValidatorModel):
    datasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEventTrackerResponseTypeDef(BaseValidatorModel):
    eventTrackerArn: str
    trackingId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateFilterResponseTypeDef(BaseValidatorModel):
    filterArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMetricAttributionResponseTypeDef(BaseValidatorModel):
    metricAttributionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRecommenderResponseTypeDef(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSchemaResponseTypeDef(BaseValidatorModel):
    schemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSolutionResponseTypeDef(BaseValidatorModel):
    solutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSolutionVersionResponseTypeDef(BaseValidatorModel):
    solutionVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetSolutionMetricsResponseTypeDef(BaseValidatorModel):
    solutionVersionArn: str
    metrics: Dict[str, float]
    ResponseMetadata: ResponseMetadataTypeDef


class ListBatchInferenceJobsResponseTypeDef(BaseValidatorModel):
    batchInferenceJobs: List[BatchInferenceJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListBatchSegmentJobsResponseTypeDef(BaseValidatorModel):
    batchSegmentJobs: List[BatchSegmentJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCampaignsResponseTypeDef(BaseValidatorModel):
    campaigns: List[CampaignSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartRecommenderResponseTypeDef(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopRecommenderResponseTypeDef(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateCampaignResponseTypeDef(BaseValidatorModel):
    campaignArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDatasetResponseTypeDef(BaseValidatorModel):
    datasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMetricAttributionResponseTypeDef(BaseValidatorModel):
    metricAttributionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRecommenderResponseTypeDef(BaseValidatorModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSolutionResponseTypeDef(BaseValidatorModel):
    solutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataDeletionJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    datasetGroupArn: str
    dataSource: DataSourceTypeDef
    roleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateDatasetImportJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    datasetArn: str
    dataSource: DataSourceTypeDef
    roleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None
    importMode: Optional[ImportModeType] = None
    publishAttributionMetricsToS3: Optional[bool] = None


class DataDeletionJobTypeDef(BaseValidatorModel):
    jobName: Optional[str] = None
    dataDeletionJobArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    dataSource: Optional[DataSourceTypeDef] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    numDeleted: Optional[int] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class DatasetImportJobTypeDef(BaseValidatorModel):
    jobName: Optional[str] = None
    datasetImportJobArn: Optional[str] = None
    datasetArn: Optional[str] = None
    dataSource: Optional[DataSourceTypeDef] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    importMode: Optional[ImportModeType] = None
    publishAttributionMetricsToS3: Optional[bool] = None


class ListMetricAttributionMetricsResponseTypeDef(BaseValidatorModel):
    metrics: List[MetricAttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDataDeletionJobsResponseTypeDef(BaseValidatorModel):
    dataDeletionJobs: List[DataDeletionJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDatasetExportJobsResponseTypeDef(BaseValidatorModel):
    datasetExportJobs: List[DatasetExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDatasetGroupsResponseTypeDef(BaseValidatorModel):
    datasetGroups: List[DatasetGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeDatasetGroupResponseTypeDef(BaseValidatorModel):
    datasetGroup: DatasetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDatasetImportJobsResponseTypeDef(BaseValidatorModel):
    datasetImportJobs: List[DatasetImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSchemasResponseTypeDef(BaseValidatorModel):
    schemas: List[DatasetSchemaSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeSchemaResponseTypeDef(BaseValidatorModel):
    schema: DatasetSchemaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListDatasetsResponseTypeDef(BaseValidatorModel):
    datasets: List[DatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DatasetTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    datasetType: Optional[str] = None
    schemaArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    latestDatasetUpdate: Optional[DatasetUpdateSummaryTypeDef] = None
    trackingId: Optional[str] = None


class DefaultHyperParameterRangesTypeDef(BaseValidatorModel):
    integerHyperParameterRanges: Optional[List[DefaultIntegerHyperParameterRangeTypeDef]] = None
    continuousHyperParameterRanges: Optional[List[DefaultContinuousHyperParameterRangeTypeDef]] = None
    categoricalHyperParameterRanges: Optional[List[DefaultCategoricalHyperParameterRangeTypeDef]] = None


class DescribeEventTrackerResponseTypeDef(BaseValidatorModel):
    eventTracker: EventTrackerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFeatureTransformationResponseTypeDef(BaseValidatorModel):
    featureTransformation: FeatureTransformationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRecipeResponseTypeDef(BaseValidatorModel):
    recipe: RecipeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListEventTrackersResponseTypeDef(BaseValidatorModel):
    eventTrackers: List[EventTrackerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ThemeGenerationConfigTypeDef(BaseValidatorModel):
    fieldsForThemeGeneration: FieldsForThemeGenerationTypeDef


class ListFiltersResponseTypeDef(BaseValidatorModel):
    Filters: List[FilterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class HyperParameterRangesOutputTypeDef(BaseValidatorModel):
    integerHyperParameterRanges: Optional[List[IntegerHyperParameterRangeTypeDef]] = None
    continuousHyperParameterRanges: Optional[List[ContinuousHyperParameterRangeTypeDef]] = None
    categoricalHyperParameterRanges: Optional[List[CategoricalHyperParameterRangeOutputTypeDef]] = None


class HyperParameterRangesTypeDef(BaseValidatorModel):
    integerHyperParameterRanges: Optional[Sequence[IntegerHyperParameterRangeTypeDef]] = None
    continuousHyperParameterRanges: Optional[Sequence[ContinuousHyperParameterRangeTypeDef]] = None
    categoricalHyperParameterRanges: Optional[Sequence[CategoricalHyperParameterRangeTypeDef]] = None


class ListBatchInferenceJobsRequestPaginateTypeDef(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBatchSegmentJobsRequestPaginateTypeDef(BaseValidatorModel):
    solutionVersionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCampaignsRequestPaginateTypeDef(BaseValidatorModel):
    solutionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetExportJobsRequestPaginateTypeDef(BaseValidatorModel):
    datasetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetGroupsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetImportJobsRequestPaginateTypeDef(BaseValidatorModel):
    datasetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventTrackersRequestPaginateTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFiltersRequestPaginateTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMetricAttributionMetricsRequestPaginateTypeDef(BaseValidatorModel):
    metricAttributionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMetricAttributionsRequestPaginateTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecipesRequestPaginateTypeDef(BaseValidatorModel):
    recipeProvider: Optional[Literal["SERVICE"]] = None
    domain: Optional[DomainType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecommendersRequestPaginateTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemasRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSolutionVersionsRequestPaginateTypeDef(BaseValidatorModel):
    solutionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSolutionsRequestPaginateTypeDef(BaseValidatorModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMetricAttributionsResponseTypeDef(BaseValidatorModel):
    metricAttributions: List[MetricAttributionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRecipesResponseTypeDef(BaseValidatorModel):
    recipes: List[RecipeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSolutionVersionsResponseTypeDef(BaseValidatorModel):
    solutionVersions: List[SolutionVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSolutionsResponseTypeDef(BaseValidatorModel):
    solutions: List[SolutionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecommenderConfigOutputTypeDef(BaseValidatorModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    minRecommendationRequestsPerSecond: Optional[int] = None
    trainingDataConfig: Optional[TrainingDataConfigOutputTypeDef] = None
    enableMetadataWithRecommendations: Optional[bool] = None


class RecommenderConfigTypeDef(BaseValidatorModel):
    itemExplorationConfig: Optional[Mapping[str, str]] = None
    minRecommendationRequestsPerSecond: Optional[int] = None
    trainingDataConfig: Optional[TrainingDataConfigTypeDef] = None
    enableMetadataWithRecommendations: Optional[bool] = None


class SolutionUpdateSummaryTypeDef(BaseValidatorModel):
    solutionUpdateConfig: Optional[SolutionUpdateConfigTypeDef] = None
    status: Optional[str] = None
    performAutoTraining: Optional[bool] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class UpdateSolutionRequestTypeDef(BaseValidatorModel):
    solutionArn: str
    performAutoTraining: Optional[bool] = None
    solutionUpdateConfig: Optional[SolutionUpdateConfigTypeDef] = None


class BatchSegmentJobTypeDef(BaseValidatorModel):
    jobName: Optional[str] = None
    batchSegmentJobArn: Optional[str] = None
    filterArn: Optional[str] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    numResults: Optional[int] = None
    jobInput: Optional[BatchSegmentJobInputTypeDef] = None
    jobOutput: Optional[BatchSegmentJobOutputTypeDef] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class CreateBatchSegmentJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    solutionVersionArn: str
    jobInput: BatchSegmentJobInputTypeDef
    jobOutput: BatchSegmentJobOutputTypeDef
    roleArn: str
    filterArn: Optional[str] = None
    numResults: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateDatasetExportJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    datasetArn: str
    roleArn: str
    jobOutput: DatasetExportJobOutputTypeDef
    ingestionMode: Optional[IngestionModeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class DatasetExportJobTypeDef(BaseValidatorModel):
    jobName: Optional[str] = None
    datasetExportJobArn: Optional[str] = None
    datasetArn: Optional[str] = None
    ingestionMode: Optional[IngestionModeType] = None
    roleArn: Optional[str] = None
    status: Optional[str] = None
    jobOutput: Optional[DatasetExportJobOutputTypeDef] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class CreateMetricAttributionRequestTypeDef(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    metrics: Sequence[MetricAttributeTypeDef]
    metricsOutputConfig: MetricAttributionOutputTypeDef


class MetricAttributionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    metricAttributionArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    metricsOutputConfig: Optional[MetricAttributionOutputTypeDef] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None


class UpdateMetricAttributionRequestTypeDef(BaseValidatorModel):
    addMetrics: Optional[Sequence[MetricAttributeTypeDef]] = None
    removeMetrics: Optional[Sequence[str]] = None
    metricsOutputConfig: Optional[MetricAttributionOutputTypeDef] = None
    metricAttributionArn: Optional[str] = None


class CampaignTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    campaignArn: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigOutputTypeDef] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    latestCampaignUpdate: Optional[CampaignUpdateSummaryTypeDef] = None


class CampaignConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateCampaignRequestTypeDef(BaseValidatorModel):
    name: str
    solutionVersionArn: str
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigUnionTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateCampaignRequestTypeDef(BaseValidatorModel):
    campaignArn: str
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigUnionTypeDef] = None


class DescribeDataDeletionJobResponseTypeDef(BaseValidatorModel):
    dataDeletionJob: DataDeletionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDatasetImportJobResponseTypeDef(BaseValidatorModel):
    datasetImportJob: DatasetImportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDatasetResponseTypeDef(BaseValidatorModel):
    dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AlgorithmTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    algorithmArn: Optional[str] = None
    algorithmImage: Optional[AlgorithmImageTypeDef] = None
    defaultHyperParameters: Optional[Dict[str, str]] = None
    defaultHyperParameterRanges: Optional[DefaultHyperParameterRangesTypeDef] = None
    defaultResourceConfig: Optional[Dict[str, str]] = None
    trainingInputMode: Optional[str] = None
    roleArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class BatchInferenceJobTypeDef(BaseValidatorModel):
    jobName: Optional[str] = None
    batchInferenceJobArn: Optional[str] = None
    filterArn: Optional[str] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    numResults: Optional[int] = None
    jobInput: Optional[BatchInferenceJobInputTypeDef] = None
    jobOutput: Optional[BatchInferenceJobOutputTypeDef] = None
    batchInferenceJobConfig: Optional[BatchInferenceJobConfigOutputTypeDef] = None
    roleArn: Optional[str] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None
    themeGenerationConfig: Optional[ThemeGenerationConfigTypeDef] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class BatchInferenceJobConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateBatchInferenceJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    solutionVersionArn: str
    jobInput: BatchInferenceJobInputTypeDef
    jobOutput: BatchInferenceJobOutputTypeDef
    roleArn: str
    filterArn: Optional[str] = None
    numResults: Optional[int] = None
    batchInferenceJobConfig: Optional[BatchInferenceJobConfigUnionTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None
    themeGenerationConfig: Optional[ThemeGenerationConfigTypeDef] = None


class HPOObjectiveTypeDef(BaseValidatorModel):
    pass


class HPOConfigOutputTypeDef(BaseValidatorModel):
    hpoObjective: Optional[HPOObjectiveTypeDef] = None
    hpoResourceConfig: Optional[HPOResourceConfigTypeDef] = None
    algorithmHyperParameterRanges: Optional[HyperParameterRangesOutputTypeDef] = None


class HPOConfigTypeDef(BaseValidatorModel):
    hpoObjective: Optional[HPOObjectiveTypeDef] = None
    hpoResourceConfig: Optional[HPOResourceConfigTypeDef] = None
    algorithmHyperParameterRanges: Optional[HyperParameterRangesTypeDef] = None


class RecommenderSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    recommenderArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    recipeArn: Optional[str] = None
    recommenderConfig: Optional[RecommenderConfigOutputTypeDef] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None


class RecommenderUpdateSummaryTypeDef(BaseValidatorModel):
    recommenderConfig: Optional[RecommenderConfigOutputTypeDef] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None


class DescribeBatchSegmentJobResponseTypeDef(BaseValidatorModel):
    batchSegmentJob: BatchSegmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDatasetExportJobResponseTypeDef(BaseValidatorModel):
    datasetExportJob: DatasetExportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMetricAttributionResponseTypeDef(BaseValidatorModel):
    metricAttribution: MetricAttributionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCampaignResponseTypeDef(BaseValidatorModel):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAlgorithmResponseTypeDef(BaseValidatorModel):
    algorithm: AlgorithmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeBatchInferenceJobResponseTypeDef(BaseValidatorModel):
    batchInferenceJob: BatchInferenceJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SolutionConfigOutputTypeDef(BaseValidatorModel):
    eventValueThreshold: Optional[str] = None
    hpoConfig: Optional[HPOConfigOutputTypeDef] = None
    algorithmHyperParameters: Optional[Dict[str, str]] = None
    featureTransformationParameters: Optional[Dict[str, str]] = None
    autoMLConfig: Optional[AutoMLConfigOutputTypeDef] = None
    optimizationObjective: Optional[OptimizationObjectiveTypeDef] = None
    trainingDataConfig: Optional[TrainingDataConfigOutputTypeDef] = None
    autoTrainingConfig: Optional[AutoTrainingConfigTypeDef] = None


class SolutionConfigTypeDef(BaseValidatorModel):
    eventValueThreshold: Optional[str] = None
    hpoConfig: Optional[HPOConfigTypeDef] = None
    algorithmHyperParameters: Optional[Mapping[str, str]] = None
    featureTransformationParameters: Optional[Mapping[str, str]] = None
    autoMLConfig: Optional[AutoMLConfigTypeDef] = None
    optimizationObjective: Optional[OptimizationObjectiveTypeDef] = None
    trainingDataConfig: Optional[TrainingDataConfigTypeDef] = None
    autoTrainingConfig: Optional[AutoTrainingConfigTypeDef] = None


class ListRecommendersResponseTypeDef(BaseValidatorModel):
    recommenders: List[RecommenderSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecommenderTypeDef(BaseValidatorModel):
    recommenderArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    recommenderConfig: Optional[RecommenderConfigOutputTypeDef] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    latestRecommenderUpdate: Optional[RecommenderUpdateSummaryTypeDef] = None
    modelMetrics: Optional[Dict[str, float]] = None


class RecommenderConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateRecommenderRequestTypeDef(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    recipeArn: str
    recommenderConfig: Optional[RecommenderConfigUnionTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateRecommenderRequestTypeDef(BaseValidatorModel):
    recommenderArn: str
    recommenderConfig: RecommenderConfigUnionTypeDef


class SolutionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    solutionArn: Optional[str] = None
    performHPO: Optional[bool] = None
    performAutoML: Optional[bool] = None
    performAutoTraining: Optional[bool] = None
    recipeArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    eventType: Optional[str] = None
    solutionConfig: Optional[SolutionConfigOutputTypeDef] = None
    autoMLResult: Optional[AutoMLResultTypeDef] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    latestSolutionVersion: Optional[SolutionVersionSummaryTypeDef] = None
    latestSolutionUpdate: Optional[SolutionUpdateSummaryTypeDef] = None


class SolutionVersionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    solutionArn: Optional[str] = None
    performHPO: Optional[bool] = None
    performAutoML: Optional[bool] = None
    recipeArn: Optional[str] = None
    eventType: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    solutionConfig: Optional[SolutionConfigOutputTypeDef] = None
    trainingHours: Optional[float] = None
    trainingMode: Optional[TrainingModeType] = None
    tunedHPOParams: Optional[TunedHPOParamsTypeDef] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    trainingType: Optional[TrainingTypeType] = None


class DescribeRecommenderResponseTypeDef(BaseValidatorModel):
    recommender: RecommenderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSolutionResponseTypeDef(BaseValidatorModel):
    solution: SolutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSolutionVersionResponseTypeDef(BaseValidatorModel):
    solutionVersion: SolutionVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SolutionConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateSolutionRequestTypeDef(BaseValidatorModel):
    name: str
    datasetGroupArn: str
    performHPO: Optional[bool] = None
    performAutoML: Optional[bool] = None
    performAutoTraining: Optional[bool] = None
    recipeArn: Optional[str] = None
    eventType: Optional[str] = None
    solutionConfig: Optional[SolutionConfigUnionTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


