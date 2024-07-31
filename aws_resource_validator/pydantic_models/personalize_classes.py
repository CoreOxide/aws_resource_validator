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
from aws_resource_validator.pydantic_models.personalize_constants import *

class AlgorithmImageTypeDef(BaseModel):
    dockerURI: str
    name: Optional[str] = None

class AutoMLConfigOutputTypeDef(BaseModel):
    metricName: Optional[str] = None
    recipeList: Optional[List[str]] = None

class AutoMLConfigTypeDef(BaseModel):
    metricName: Optional[str] = None
    recipeList: Optional[Sequence[str]] = None

class AutoMLResultTypeDef(BaseModel):
    bestRecipeArn: Optional[str] = None

class AutoTrainingConfigTypeDef(BaseModel):
    schedulingExpression: Optional[str] = None

class BatchInferenceJobConfigOutputTypeDef(BaseModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None

class BatchInferenceJobConfigTypeDef(BaseModel):
    itemExplorationConfig: Optional[Mapping[str, str]] = None

class S3DataConfigTypeDef(BaseModel):
    path: str
    kmsKeyArn: Optional[str] = None

class BatchInferenceJobSummaryTypeDef(BaseModel):
    batchInferenceJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None

class BatchSegmentJobSummaryTypeDef(BaseModel):
    batchSegmentJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    solutionVersionArn: Optional[str] = None

class CampaignConfigOutputTypeDef(BaseModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    enableMetadataWithRecommendations: Optional[bool] = None
    syncWithLatestSolutionVersion: Optional[bool] = None

class CampaignConfigTypeDef(BaseModel):
    itemExplorationConfig: Optional[Mapping[str, str]] = None
    enableMetadataWithRecommendations: Optional[bool] = None
    syncWithLatestSolutionVersion: Optional[bool] = None

class CampaignSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    campaignArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None

class CategoricalHyperParameterRangeOutputTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None

class CategoricalHyperParameterRangeTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class ContinuousHyperParameterRangeTypeDef(BaseModel):
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None

class TagTypeDef(BaseModel):
    tagKey: str
    tagValue: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DataSourceTypeDef(BaseModel):
    dataLocation: Optional[str] = None

class MetricAttributeTypeDef(BaseModel):
    eventType: str
    metricName: str
    expression: str

class CreateSchemaRequestRequestTypeDef(BaseModel):
    name: str
    schema: str
    domain: Optional[DomainType] = None

class DataDeletionJobSummaryTypeDef(BaseModel):
    dataDeletionJobArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None

class DatasetExportJobSummaryTypeDef(BaseModel):
    datasetExportJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None

class DatasetGroupSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    domain: Optional[DomainType] = None

class DatasetGroupTypeDef(BaseModel):
    name: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    roleArn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    domain: Optional[DomainType] = None

class DatasetImportJobSummaryTypeDef(BaseModel):
    datasetImportJobArn: Optional[str] = None
    jobName: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None
    importMode: Optional[ImportModeType] = None

class DatasetSchemaSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    schemaArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None

class DatasetSchemaTypeDef(BaseModel):
    name: Optional[str] = None
    schemaArn: Optional[str] = None
    schema: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None

class DatasetSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    datasetArn: Optional[str] = None
    datasetType: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class DatasetUpdateSummaryTypeDef(BaseModel):
    schemaArn: Optional[str] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class DefaultCategoricalHyperParameterRangeTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None
    isTunable: Optional[bool] = None

class DefaultContinuousHyperParameterRangeTypeDef(BaseModel):
    name: Optional[str] = None
    minValue: Optional[float] = None
    maxValue: Optional[float] = None
    isTunable: Optional[bool] = None

class DefaultIntegerHyperParameterRangeTypeDef(BaseModel):
    name: Optional[str] = None
    minValue: Optional[int] = None
    maxValue: Optional[int] = None
    isTunable: Optional[bool] = None

class DeleteCampaignRequestRequestTypeDef(BaseModel):
    campaignArn: str

class DeleteDatasetGroupRequestRequestTypeDef(BaseModel):
    datasetGroupArn: str

class DeleteDatasetRequestRequestTypeDef(BaseModel):
    datasetArn: str

class DeleteEventTrackerRequestRequestTypeDef(BaseModel):
    eventTrackerArn: str

class DeleteFilterRequestRequestTypeDef(BaseModel):
    filterArn: str

class DeleteMetricAttributionRequestRequestTypeDef(BaseModel):
    metricAttributionArn: str

class DeleteRecommenderRequestRequestTypeDef(BaseModel):
    recommenderArn: str

class DeleteSchemaRequestRequestTypeDef(BaseModel):
    schemaArn: str

class DeleteSolutionRequestRequestTypeDef(BaseModel):
    solutionArn: str

class DescribeAlgorithmRequestRequestTypeDef(BaseModel):
    algorithmArn: str

class DescribeBatchInferenceJobRequestRequestTypeDef(BaseModel):
    batchInferenceJobArn: str

class DescribeBatchSegmentJobRequestRequestTypeDef(BaseModel):
    batchSegmentJobArn: str

class DescribeCampaignRequestRequestTypeDef(BaseModel):
    campaignArn: str

class DescribeDataDeletionJobRequestRequestTypeDef(BaseModel):
    dataDeletionJobArn: str

class DescribeDatasetExportJobRequestRequestTypeDef(BaseModel):
    datasetExportJobArn: str

class DescribeDatasetGroupRequestRequestTypeDef(BaseModel):
    datasetGroupArn: str

class DescribeDatasetImportJobRequestRequestTypeDef(BaseModel):
    datasetImportJobArn: str

class DescribeDatasetRequestRequestTypeDef(BaseModel):
    datasetArn: str

class DescribeEventTrackerRequestRequestTypeDef(BaseModel):
    eventTrackerArn: str

class EventTrackerTypeDef(BaseModel):
    name: Optional[str] = None
    eventTrackerArn: Optional[str] = None
    accountId: Optional[str] = None
    trackingId: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class DescribeFeatureTransformationRequestRequestTypeDef(BaseModel):
    featureTransformationArn: str

class FeatureTransformationTypeDef(BaseModel):
    name: Optional[str] = None
    featureTransformationArn: Optional[str] = None
    defaultParameters: Optional[Dict[str, str]] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None

class DescribeFilterRequestRequestTypeDef(BaseModel):
    filterArn: str

class FilterTypeDef(BaseModel):
    name: Optional[str] = None
    filterArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    datasetGroupArn: Optional[str] = None
    failureReason: Optional[str] = None
    filterExpression: Optional[str] = None
    status: Optional[str] = None

class DescribeMetricAttributionRequestRequestTypeDef(BaseModel):
    metricAttributionArn: str

class DescribeRecipeRequestRequestTypeDef(BaseModel):
    recipeArn: str

class RecipeTypeDef(BaseModel):
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    algorithmArn: Optional[str] = None
    featureTransformationArn: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    recipeType: Optional[str] = None
    lastUpdatedDateTime: Optional[datetime] = None

class DescribeRecommenderRequestRequestTypeDef(BaseModel):
    recommenderArn: str

class DescribeSchemaRequestRequestTypeDef(BaseModel):
    schemaArn: str

class DescribeSolutionRequestRequestTypeDef(BaseModel):
    solutionArn: str

class DescribeSolutionVersionRequestRequestTypeDef(BaseModel):
    solutionVersionArn: str

class EventTrackerSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    eventTrackerArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class FieldsForThemeGenerationTypeDef(BaseModel):
    itemName: str

class FilterSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    filterArn: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    datasetGroupArn: Optional[str] = None
    failureReason: Optional[str] = None
    status: Optional[str] = None

class GetSolutionMetricsRequestRequestTypeDef(BaseModel):
    solutionVersionArn: str

class HPOObjectiveTypeDef(BaseModel):
    type: Optional[str] = None
    metricName: Optional[str] = None
    metricRegex: Optional[str] = None

class HPOResourceConfigTypeDef(BaseModel):
    maxNumberOfTrainingJobs: Optional[str] = None
    maxParallelTrainingJobs: Optional[str] = None

class IntegerHyperParameterRangeTypeDef(BaseModel):
    name: Optional[str] = None
    minValue: Optional[int] = None
    maxValue: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListBatchInferenceJobsRequestRequestTypeDef(BaseModel):
    solutionVersionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListBatchSegmentJobsRequestRequestTypeDef(BaseModel):
    solutionVersionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListCampaignsRequestRequestTypeDef(BaseModel):
    solutionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDataDeletionJobsRequestRequestTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetExportJobsRequestRequestTypeDef(BaseModel):
    datasetArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetGroupsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetImportJobsRequestRequestTypeDef(BaseModel):
    datasetArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDatasetsRequestRequestTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListEventTrackersRequestRequestTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListFiltersRequestRequestTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMetricAttributionMetricsRequestRequestTypeDef(BaseModel):
    metricAttributionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMetricAttributionsRequestRequestTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class MetricAttributionSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    metricAttributionArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None

class ListRecipesRequestRequestTypeDef(BaseModel):
    recipeProvider: Optional[Literal["SERVICE"]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    domain: Optional[DomainType] = None

class RecipeSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    recipeArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    domain: Optional[DomainType] = None

class ListRecommendersRequestRequestTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSchemasRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListSolutionVersionsRequestRequestTypeDef(BaseModel):
    solutionArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SolutionVersionSummaryTypeDef(BaseModel):
    solutionVersionArn: Optional[str] = None
    status: Optional[str] = None
    trainingMode: Optional[TrainingModeType] = None
    trainingType: Optional[TrainingTypeType] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None

class ListSolutionsRequestRequestTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class SolutionSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    solutionArn: Optional[str] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    recipeArn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class OptimizationObjectiveTypeDef(BaseModel):
    itemAttribute: Optional[str] = None
    objectiveSensitivity: Optional[ObjectiveSensitivityType] = None

class TrainingDataConfigExtraOutputTypeDef(BaseModel):
    excludedDatasetColumns: Optional[Dict[str, List[str]]] = None

class TrainingDataConfigOutputTypeDef(BaseModel):
    excludedDatasetColumns: Optional[Dict[str, List[str]]] = None

class TrainingDataConfigTypeDef(BaseModel):
    excludedDatasetColumns: Optional[Mapping[str, Sequence[str]]] = None

class TunedHPOParamsTypeDef(BaseModel):
    algorithmHyperParameters: Optional[Dict[str, str]] = None

class StartRecommenderRequestRequestTypeDef(BaseModel):
    recommenderArn: str

class StopRecommenderRequestRequestTypeDef(BaseModel):
    recommenderArn: str

class StopSolutionVersionCreationRequestRequestTypeDef(BaseModel):
    solutionVersionArn: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateDatasetRequestRequestTypeDef(BaseModel):
    datasetArn: str
    schemaArn: str

class BatchInferenceJobInputTypeDef(BaseModel):
    s3DataSource: S3DataConfigTypeDef

class BatchInferenceJobOutputTypeDef(BaseModel):
    s3DataDestination: S3DataConfigTypeDef

class BatchSegmentJobInputTypeDef(BaseModel):
    s3DataSource: S3DataConfigTypeDef

class BatchSegmentJobOutputTypeDef(BaseModel):
    s3DataDestination: S3DataConfigTypeDef

class DatasetExportJobOutputTypeDef(BaseModel):
    s3DataDestination: S3DataConfigTypeDef

class MetricAttributionOutputTypeDef(BaseModel):
    roleArn: str
    s3DataDestination: Optional[S3DataConfigTypeDef] = None

class CampaignUpdateSummaryTypeDef(BaseModel):
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigOutputTypeDef] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class UpdateCampaignRequestRequestTypeDef(BaseModel):
    campaignArn: str
    solutionVersionArn: Optional[str] = None
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigTypeDef] = None

class CreateCampaignRequestRequestTypeDef(BaseModel):
    name: str
    solutionVersionArn: str
    minProvisionedTPS: Optional[int] = None
    campaignConfig: Optional[CampaignConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDatasetGroupRequestRequestTypeDef(BaseModel):
    name: str
    roleArn: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    domain: Optional[DomainType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDatasetRequestRequestTypeDef(BaseModel):
    name: str
    schemaArn: str
    datasetGroupArn: str
    datasetType: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateEventTrackerRequestRequestTypeDef(BaseModel):
    name: str
    datasetGroupArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateFilterRequestRequestTypeDef(BaseModel):
    name: str
    datasetGroupArn: str
    filterExpression: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateSolutionVersionRequestRequestTypeDef(BaseModel):
    solutionArn: str
    name: Optional[str] = None
    trainingMode: Optional[TrainingModeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateBatchInferenceJobResponseTypeDef(BaseModel):
    batchInferenceJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBatchSegmentJobResponseTypeDef(BaseModel):
    batchSegmentJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCampaignResponseTypeDef(BaseModel):
    campaignArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataDeletionJobResponseTypeDef(BaseModel):
    dataDeletionJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetExportJobResponseTypeDef(BaseModel):
    datasetExportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetGroupResponseTypeDef(BaseModel):
    datasetGroupArn: str
    domain: DomainType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetImportJobResponseTypeDef(BaseModel):
    datasetImportJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDatasetResponseTypeDef(BaseModel):
    datasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventTrackerResponseTypeDef(BaseModel):
    eventTrackerArn: str
    trackingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFilterResponseTypeDef(BaseModel):
    filterArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMetricAttributionResponseTypeDef(BaseModel):
    metricAttributionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecommenderResponseTypeDef(BaseModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaResponseTypeDef(BaseModel):
    schemaArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSolutionResponseTypeDef(BaseModel):
    solutionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSolutionVersionResponseTypeDef(BaseModel):
    solutionVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetSolutionMetricsResponseTypeDef(BaseModel):
    solutionVersionArn: str
    metrics: Dict[str, float]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBatchInferenceJobsResponseTypeDef(BaseModel):
    batchInferenceJobs: List[BatchInferenceJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListBatchSegmentJobsResponseTypeDef(BaseModel):
    batchSegmentJobs: List[BatchSegmentJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListCampaignsResponseTypeDef(BaseModel):
    campaigns: List[CampaignSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartRecommenderResponseTypeDef(BaseModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopRecommenderResponseTypeDef(BaseModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCampaignResponseTypeDef(BaseModel):
    campaignArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDatasetResponseTypeDef(BaseModel):
    datasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMetricAttributionResponseTypeDef(BaseModel):
    metricAttributionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRecommenderResponseTypeDef(BaseModel):
    recommenderArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataDeletionJobRequestRequestTypeDef(BaseModel):
    jobName: str
    datasetGroupArn: str
    dataSource: DataSourceTypeDef
    roleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDatasetImportJobRequestRequestTypeDef(BaseModel):
    jobName: str
    datasetArn: str
    dataSource: DataSourceTypeDef
    roleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None
    importMode: Optional[ImportModeType] = None
    publishAttributionMetricsToS3: Optional[bool] = None

class DataDeletionJobTypeDef(BaseModel):
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

class DatasetImportJobTypeDef(BaseModel):
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

class ListMetricAttributionMetricsResponseTypeDef(BaseModel):
    metrics: List[MetricAttributeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDataDeletionJobsResponseTypeDef(BaseModel):
    dataDeletionJobs: List[DataDeletionJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetExportJobsResponseTypeDef(BaseModel):
    datasetExportJobs: List[DatasetExportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetGroupsResponseTypeDef(BaseModel):
    datasetGroups: List[DatasetGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetGroupResponseTypeDef(BaseModel):
    datasetGroup: DatasetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetImportJobsResponseTypeDef(BaseModel):
    datasetImportJobs: List[DatasetImportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSchemasResponseTypeDef(BaseModel):
    schemas: List[DatasetSchemaSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSchemaResponseTypeDef(BaseModel):
    schema: DatasetSchemaTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListDatasetsResponseTypeDef(BaseModel):
    datasets: List[DatasetSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetTypeDef(BaseModel):
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

class DefaultHyperParameterRangesTypeDef(BaseModel):
    integerHyperParameterRanges: Optional[List[DefaultIntegerHyperParameterRangeTypeDef]] = None
    continuousHyperParameterRanges: Optional[       List[DefaultContinuousHyperParameterRangeTypeDef]     ] = None
    categoricalHyperParameterRanges: Optional[       List[DefaultCategoricalHyperParameterRangeTypeDef]     ] = None

class DescribeEventTrackerResponseTypeDef(BaseModel):
    eventTracker: EventTrackerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFeatureTransformationResponseTypeDef(BaseModel):
    featureTransformation: FeatureTransformationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeFilterResponseTypeDef(BaseModel):
    filter: FilterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRecipeResponseTypeDef(BaseModel):
    recipe: RecipeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventTrackersResponseTypeDef(BaseModel):
    eventTrackers: List[EventTrackerSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ThemeGenerationConfigTypeDef(BaseModel):
    fieldsForThemeGeneration: FieldsForThemeGenerationTypeDef

class ListFiltersResponseTypeDef(BaseModel):
    Filters: List[FilterSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class HyperParameterRangesOutputTypeDef(BaseModel):
    integerHyperParameterRanges: Optional[List[IntegerHyperParameterRangeTypeDef]] = None
    continuousHyperParameterRanges: Optional[List[ContinuousHyperParameterRangeTypeDef]] = None
    categoricalHyperParameterRanges: Optional[       List[CategoricalHyperParameterRangeOutputTypeDef]     ] = None

class HyperParameterRangesTypeDef(BaseModel):
    integerHyperParameterRanges: Optional[Sequence[IntegerHyperParameterRangeTypeDef]] = None
    continuousHyperParameterRanges: Optional[       Sequence[ContinuousHyperParameterRangeTypeDef]     ] = None
    categoricalHyperParameterRanges: Optional[       Sequence[CategoricalHyperParameterRangeTypeDef]     ] = None

class ListBatchInferenceJobsRequestListBatchInferenceJobsPaginateTypeDef(BaseModel):
    solutionVersionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBatchSegmentJobsRequestListBatchSegmentJobsPaginateTypeDef(BaseModel):
    solutionVersionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCampaignsRequestListCampaignsPaginateTypeDef(BaseModel):
    solutionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetExportJobsRequestListDatasetExportJobsPaginateTypeDef(BaseModel):
    datasetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetGroupsRequestListDatasetGroupsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetImportJobsRequestListDatasetImportJobsPaginateTypeDef(BaseModel):
    datasetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDatasetsRequestListDatasetsPaginateTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEventTrackersRequestListEventTrackersPaginateTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFiltersRequestListFiltersPaginateTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetricAttributionMetricsRequestListMetricAttributionMetricsPaginateTypeDef(BaseModel):
    metricAttributionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetricAttributionsRequestListMetricAttributionsPaginateTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecipesRequestListRecipesPaginateTypeDef(BaseModel):
    recipeProvider: Optional[Literal["SERVICE"]] = None
    domain: Optional[DomainType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecommendersRequestListRecommendersPaginateTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasRequestListSchemasPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolutionVersionsRequestListSolutionVersionsPaginateTypeDef(BaseModel):
    solutionArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSolutionsRequestListSolutionsPaginateTypeDef(BaseModel):
    datasetGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMetricAttributionsResponseTypeDef(BaseModel):
    metricAttributions: List[MetricAttributionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRecipesResponseTypeDef(BaseModel):
    recipes: List[RecipeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolutionVersionsResponseTypeDef(BaseModel):
    solutionVersions: List[SolutionVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSolutionsResponseTypeDef(BaseModel):
    solutions: List[SolutionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecommenderConfigExtraOutputTypeDef(BaseModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    minRecommendationRequestsPerSecond: Optional[int] = None
    trainingDataConfig: Optional[TrainingDataConfigExtraOutputTypeDef] = None
    enableMetadataWithRecommendations: Optional[bool] = None

class RecommenderConfigOutputTypeDef(BaseModel):
    itemExplorationConfig: Optional[Dict[str, str]] = None
    minRecommendationRequestsPerSecond: Optional[int] = None
    trainingDataConfig: Optional[TrainingDataConfigOutputTypeDef] = None
    enableMetadataWithRecommendations: Optional[bool] = None

class RecommenderConfigTypeDef(BaseModel):
    itemExplorationConfig: Optional[Mapping[str, str]] = None
    minRecommendationRequestsPerSecond: Optional[int] = None
    trainingDataConfig: Optional[TrainingDataConfigTypeDef] = None
    enableMetadataWithRecommendations: Optional[bool] = None

class BatchSegmentJobTypeDef(BaseModel):
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

class CreateBatchSegmentJobRequestRequestTypeDef(BaseModel):
    jobName: str
    solutionVersionArn: str
    jobInput: BatchSegmentJobInputTypeDef
    jobOutput: BatchSegmentJobOutputTypeDef
    roleArn: str
    filterArn: Optional[str] = None
    numResults: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateDatasetExportJobRequestRequestTypeDef(BaseModel):
    jobName: str
    datasetArn: str
    roleArn: str
    jobOutput: DatasetExportJobOutputTypeDef
    ingestionMode: Optional[IngestionModeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class DatasetExportJobTypeDef(BaseModel):
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

class CreateMetricAttributionRequestRequestTypeDef(BaseModel):
    name: str
    datasetGroupArn: str
    metrics: Sequence[MetricAttributeTypeDef]
    metricsOutputConfig: MetricAttributionOutputTypeDef

class MetricAttributionTypeDef(BaseModel):
    name: Optional[str] = None
    metricAttributionArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    metricsOutputConfig: Optional[MetricAttributionOutputTypeDef] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    failureReason: Optional[str] = None

class UpdateMetricAttributionRequestRequestTypeDef(BaseModel):
    addMetrics: Optional[Sequence[MetricAttributeTypeDef]] = None
    removeMetrics: Optional[Sequence[str]] = None
    metricsOutputConfig: Optional[MetricAttributionOutputTypeDef] = None
    metricAttributionArn: Optional[str] = None

class CampaignTypeDef(BaseModel):
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

class DescribeDataDeletionJobResponseTypeDef(BaseModel):
    dataDeletionJob: DataDeletionJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetImportJobResponseTypeDef(BaseModel):
    datasetImportJob: DatasetImportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetResponseTypeDef(BaseModel):
    dataset: DatasetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AlgorithmTypeDef(BaseModel):
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

class BatchInferenceJobTypeDef(BaseModel):
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

class CreateBatchInferenceJobRequestRequestTypeDef(BaseModel):
    jobName: str
    solutionVersionArn: str
    jobInput: BatchInferenceJobInputTypeDef
    jobOutput: BatchInferenceJobOutputTypeDef
    roleArn: str
    filterArn: Optional[str] = None
    numResults: Optional[int] = None
    batchInferenceJobConfig: Optional[BatchInferenceJobConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    batchInferenceJobMode: Optional[BatchInferenceJobModeType] = None
    themeGenerationConfig: Optional[ThemeGenerationConfigTypeDef] = None

class HPOConfigOutputTypeDef(BaseModel):
    hpoObjective: Optional[HPOObjectiveTypeDef] = None
    hpoResourceConfig: Optional[HPOResourceConfigTypeDef] = None
    algorithmHyperParameterRanges: Optional[HyperParameterRangesOutputTypeDef] = None

class HPOConfigTypeDef(BaseModel):
    hpoObjective: Optional[HPOObjectiveTypeDef] = None
    hpoResourceConfig: Optional[HPOResourceConfigTypeDef] = None
    algorithmHyperParameterRanges: Optional[HyperParameterRangesTypeDef] = None

class RecommenderSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    recommenderArn: Optional[str] = None
    datasetGroupArn: Optional[str] = None
    recipeArn: Optional[str] = None
    recommenderConfig: Optional[RecommenderConfigOutputTypeDef] = None
    status: Optional[str] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None

class RecommenderUpdateSummaryTypeDef(BaseModel):
    recommenderConfig: Optional[RecommenderConfigOutputTypeDef] = None
    creationDateTime: Optional[datetime] = None
    lastUpdatedDateTime: Optional[datetime] = None
    status: Optional[str] = None
    failureReason: Optional[str] = None

class CreateRecommenderRequestRequestTypeDef(BaseModel):
    name: str
    datasetGroupArn: str
    recipeArn: str
    recommenderConfig: Optional[RecommenderConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRecommenderRequestRequestTypeDef(BaseModel):
    recommenderArn: str
    recommenderConfig: RecommenderConfigTypeDef

class DescribeBatchSegmentJobResponseTypeDef(BaseModel):
    batchSegmentJob: BatchSegmentJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDatasetExportJobResponseTypeDef(BaseModel):
    datasetExportJob: DatasetExportJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMetricAttributionResponseTypeDef(BaseModel):
    metricAttribution: MetricAttributionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCampaignResponseTypeDef(BaseModel):
    campaign: CampaignTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAlgorithmResponseTypeDef(BaseModel):
    algorithm: AlgorithmTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBatchInferenceJobResponseTypeDef(BaseModel):
    batchInferenceJob: BatchInferenceJobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SolutionConfigOutputTypeDef(BaseModel):
    eventValueThreshold: Optional[str] = None
    hpoConfig: Optional[HPOConfigOutputTypeDef] = None
    algorithmHyperParameters: Optional[Dict[str, str]] = None
    featureTransformationParameters: Optional[Dict[str, str]] = None
    autoMLConfig: Optional[AutoMLConfigOutputTypeDef] = None
    optimizationObjective: Optional[OptimizationObjectiveTypeDef] = None
    trainingDataConfig: Optional[TrainingDataConfigOutputTypeDef] = None
    autoTrainingConfig: Optional[AutoTrainingConfigTypeDef] = None

class SolutionConfigTypeDef(BaseModel):
    eventValueThreshold: Optional[str] = None
    hpoConfig: Optional[HPOConfigTypeDef] = None
    algorithmHyperParameters: Optional[Mapping[str, str]] = None
    featureTransformationParameters: Optional[Mapping[str, str]] = None
    autoMLConfig: Optional[AutoMLConfigTypeDef] = None
    optimizationObjective: Optional[OptimizationObjectiveTypeDef] = None
    trainingDataConfig: Optional[TrainingDataConfigTypeDef] = None
    autoTrainingConfig: Optional[AutoTrainingConfigTypeDef] = None

class ListRecommendersResponseTypeDef(BaseModel):
    recommenders: List[RecommenderSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RecommenderTypeDef(BaseModel):
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

class SolutionTypeDef(BaseModel):
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

class SolutionVersionTypeDef(BaseModel):
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

class CreateSolutionRequestRequestTypeDef(BaseModel):
    name: str
    datasetGroupArn: str
    performHPO: Optional[bool] = None
    performAutoML: Optional[bool] = None
    performAutoTraining: Optional[bool] = None
    recipeArn: Optional[str] = None
    eventType: Optional[str] = None
    solutionConfig: Optional[SolutionConfigTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class DescribeRecommenderResponseTypeDef(BaseModel):
    recommender: RecommenderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSolutionResponseTypeDef(BaseModel):
    solution: SolutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSolutionVersionResponseTypeDef(BaseModel):
    solutionVersion: SolutionVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

