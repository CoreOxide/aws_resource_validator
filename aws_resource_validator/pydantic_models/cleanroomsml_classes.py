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
from aws_resource_validator.pydantic_models.cleanroomsml_constants import *

class S3ConfigMapTypeDef(BaseModel):
    s3Uri: str

class AudienceSizeTypeDef(BaseModel):
    type: AudienceSizeTypeType
    value: int

class StatusDetailsTypeDef(BaseModel):
    message: Optional[str] = None
    statusCode: Optional[str] = None

class AudienceGenerationJobSummaryTypeDef(BaseModel):
    audienceGenerationJobArn: str
    configuredAudienceModelArn: str
    createTime: datetime
    name: str
    status: AudienceGenerationJobStatusType
    updateTime: datetime
    collaborationId: Optional[str] = None
    description: Optional[str] = None
    startedBy: Optional[str] = None

class AudienceModelSummaryTypeDef(BaseModel):
    audienceModelArn: str
    createTime: datetime
    name: str
    status: AudienceModelStatusType
    trainingDatasetArn: str
    updateTime: datetime
    description: Optional[str] = None

class AudienceSizeConfigTypeDef(BaseModel):
    audienceSizeBins: Sequence[int]
    audienceSizeType: AudienceSizeTypeType

class ColumnSchemaTypeDef(BaseModel):
    columnName: str
    columnTypes: Sequence[ColumnTypeType]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GlueDataSourceTypeDef(BaseModel):
    databaseName: str
    tableName: str
    catalogId: Optional[str] = None

class DeleteAudienceGenerationJobRequestRequestTypeDef(BaseModel):
    audienceGenerationJobArn: str

class DeleteAudienceModelRequestRequestTypeDef(BaseModel):
    audienceModelArn: str

class DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef(BaseModel):
    configuredAudienceModelArn: str

class DeleteConfiguredAudienceModelRequestRequestTypeDef(BaseModel):
    configuredAudienceModelArn: str

class DeleteTrainingDatasetRequestRequestTypeDef(BaseModel):
    trainingDatasetArn: str

class GetAudienceGenerationJobRequestRequestTypeDef(BaseModel):
    audienceGenerationJobArn: str

class GetAudienceModelRequestRequestTypeDef(BaseModel):
    audienceModelArn: str

class GetConfiguredAudienceModelPolicyRequestRequestTypeDef(BaseModel):
    configuredAudienceModelArn: str

class GetConfiguredAudienceModelRequestRequestTypeDef(BaseModel):
    configuredAudienceModelArn: str

class GetTrainingDatasetRequestRequestTypeDef(BaseModel):
    trainingDatasetArn: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAudienceExportJobsRequestRequestTypeDef(BaseModel):
    audienceGenerationJobArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAudienceGenerationJobsRequestRequestTypeDef(BaseModel):
    collaborationId: Optional[str] = None
    configuredAudienceModelArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAudienceModelsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListConfiguredAudienceModelsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTrainingDatasetsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TrainingDatasetSummaryTypeDef(BaseModel):
    createTime: datetime
    name: str
    status: Literal["ACTIVE"]
    trainingDatasetArn: str
    updateTime: datetime
    description: Optional[str] = None

class PutConfiguredAudienceModelPolicyRequestRequestTypeDef(BaseModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyExistenceCondition: Optional[PolicyExistenceConditionType] = None
    previousPolicyHash: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AudienceDestinationTypeDef(BaseModel):
    s3Destination: S3ConfigMapTypeDef

class AudienceGenerationJobDataSourceTypeDef(BaseModel):
    dataSource: S3ConfigMapTypeDef
    roleArn: str

class RelevanceMetricTypeDef(BaseModel):
    audienceSize: AudienceSizeTypeDef
    score: Optional[float] = None

class StartAudienceExportJobRequestRequestTypeDef(BaseModel):
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    name: str
    description: Optional[str] = None

class AudienceExportJobSummaryTypeDef(BaseModel):
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    createTime: datetime
    name: str
    status: AudienceExportJobStatusType
    updateTime: datetime
    description: Optional[str] = None
    outputLocation: Optional[str] = None
    statusDetails: Optional[StatusDetailsTypeDef] = None

class CreateAudienceModelRequestRequestTypeDef(BaseModel):
    name: str
    trainingDatasetArn: str
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    trainingDataEndTime: Optional[TimestampTypeDef] = None
    trainingDataStartTime: Optional[TimestampTypeDef] = None

class CreateAudienceModelResponseTypeDef(BaseModel):
    audienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredAudienceModelResponseTypeDef(BaseModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainingDatasetResponseTypeDef(BaseModel):
    trainingDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAudienceModelResponseTypeDef(BaseModel):
    audienceModelArn: str
    createTime: datetime
    description: str
    kmsKeyArn: str
    name: str
    status: AudienceModelStatusType
    statusDetails: StatusDetailsTypeDef
    tags: Dict[str, str]
    trainingDataEndTime: datetime
    trainingDataStartTime: datetime
    trainingDatasetArn: str
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetConfiguredAudienceModelPolicyResponseTypeDef(BaseModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAudienceGenerationJobsResponseTypeDef(BaseModel):
    audienceGenerationJobs: List[AudienceGenerationJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAudienceModelsResponseTypeDef(BaseModel):
    audienceModels: List[AudienceModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfiguredAudienceModelPolicyResponseTypeDef(BaseModel):
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAudienceGenerationJobResponseTypeDef(BaseModel):
    audienceGenerationJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelResponseTypeDef(BaseModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceTypeDef(BaseModel):
    glueDataSource: GlueDataSourceTypeDef

class ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef(BaseModel):
    audienceGenerationJobArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef(BaseModel):
    collaborationId: Optional[str] = None
    configuredAudienceModelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAudienceModelsRequestListAudienceModelsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingDatasetsResponseTypeDef(BaseModel):
    nextToken: str
    trainingDatasets: List[TrainingDatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfiguredAudienceModelOutputConfigTypeDef(BaseModel):
    destination: AudienceDestinationTypeDef
    roleArn: str

class StartAudienceGenerationJobRequestRequestTypeDef(BaseModel):
    configuredAudienceModelArn: str
    name: str
    seedAudience: AudienceGenerationJobDataSourceTypeDef
    collaborationId: Optional[str] = None
    description: Optional[str] = None
    includeSeedInOutput: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class AudienceQualityMetricsTypeDef(BaseModel):
    relevanceMetrics: List[RelevanceMetricTypeDef]
    recallMetric: Optional[float] = None

class ListAudienceExportJobsResponseTypeDef(BaseModel):
    audienceExportJobs: List[AudienceExportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetInputConfigTypeDef(BaseModel):
    dataSource: DataSourceTypeDef
    schema: Sequence[ColumnSchemaTypeDef]

class ConfiguredAudienceModelSummaryTypeDef(BaseModel):
    audienceModelArn: str
    configuredAudienceModelArn: str
    createTime: datetime
    name: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    status: Literal["ACTIVE"]
    updateTime: datetime
    description: Optional[str] = None

class CreateConfiguredAudienceModelRequestRequestTypeDef(BaseModel):
    audienceModelArn: str
    name: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    sharedAudienceMetrics: Sequence[SharedAudienceMetricsType]
    audienceSizeConfig: Optional[AudienceSizeConfigTypeDef] = None
    childResourceTagOnCreatePolicy: Optional[TagOnCreatePolicyType] = None
    description: Optional[str] = None
    minMatchingSeedSize: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class GetConfiguredAudienceModelResponseTypeDef(BaseModel):
    audienceModelArn: str
    audienceSizeConfig: AudienceSizeConfigTypeDef
    childResourceTagOnCreatePolicy: TagOnCreatePolicyType
    configuredAudienceModelArn: str
    createTime: datetime
    description: str
    minMatchingSeedSize: int
    name: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    sharedAudienceMetrics: List[SharedAudienceMetricsType]
    status: Literal["ACTIVE"]
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelRequestRequestTypeDef(BaseModel):
    configuredAudienceModelArn: str
    audienceModelArn: Optional[str] = None
    audienceSizeConfig: Optional[AudienceSizeConfigTypeDef] = None
    description: Optional[str] = None
    minMatchingSeedSize: Optional[int] = None
    outputConfig: Optional[ConfiguredAudienceModelOutputConfigTypeDef] = None
    sharedAudienceMetrics: Optional[Sequence[SharedAudienceMetricsType]] = None

class GetAudienceGenerationJobResponseTypeDef(BaseModel):
    audienceGenerationJobArn: str
    collaborationId: str
    configuredAudienceModelArn: str
    createTime: datetime
    description: str
    includeSeedInOutput: bool
    metrics: AudienceQualityMetricsTypeDef
    name: str
    seedAudience: AudienceGenerationJobDataSourceTypeDef
    startedBy: str
    status: AudienceGenerationJobStatusType
    statusDetails: StatusDetailsTypeDef
    tags: Dict[str, str]
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetTypeDef(BaseModel):
    inputConfig: DatasetInputConfigTypeDef
    type: Literal["INTERACTIONS"]

class ListConfiguredAudienceModelsResponseTypeDef(BaseModel):
    configuredAudienceModels: List[ConfiguredAudienceModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainingDatasetRequestRequestTypeDef(BaseModel):
    name: str
    roleArn: str
    trainingData: Sequence[DatasetTypeDef]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetTrainingDatasetResponseTypeDef(BaseModel):
    createTime: datetime
    description: str
    name: str
    roleArn: str
    status: Literal["ACTIVE"]
    tags: Dict[str, str]
    trainingData: List[DatasetTypeDef]
    trainingDatasetArn: str
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

