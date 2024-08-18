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
from aws_resource_validator.pydantic_models.cleanroomsml_constants import *

class S3ConfigMapTypeDef(BaseValidatorModel):
    s3Uri: str

class AudienceSizeTypeDef(BaseValidatorModel):
    type: AudienceSizeTypeType
    value: int

class StatusDetailsTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    statusCode: Optional[str] = None

class AudienceGenerationJobSummaryTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str
    configuredAudienceModelArn: str
    createTime: datetime
    name: str
    status: AudienceGenerationJobStatusType
    updateTime: datetime
    collaborationId: Optional[str] = None
    description: Optional[str] = None
    startedBy: Optional[str] = None

class AudienceModelSummaryTypeDef(BaseValidatorModel):
    audienceModelArn: str
    createTime: datetime
    name: str
    status: AudienceModelStatusType
    trainingDatasetArn: str
    updateTime: datetime
    description: Optional[str] = None

class AudienceSizeConfigTypeDef(BaseValidatorModel):
    audienceSizeBins: Sequence[int]
    audienceSizeType: AudienceSizeTypeType

class ColumnSchemaTypeDef(BaseValidatorModel):
    columnName: str
    columnTypes: Sequence[ColumnTypeType]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class GlueDataSourceTypeDef(BaseValidatorModel):
    databaseName: str
    tableName: str
    catalogId: Optional[str] = None

class DeleteAudienceGenerationJobRequestRequestTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str

class DeleteAudienceModelRequestRequestTypeDef(BaseValidatorModel):
    audienceModelArn: str

class DeleteConfiguredAudienceModelPolicyRequestRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str

class DeleteConfiguredAudienceModelRequestRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str

class DeleteTrainingDatasetRequestRequestTypeDef(BaseValidatorModel):
    trainingDatasetArn: str

class GetAudienceGenerationJobRequestRequestTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str

class GetAudienceModelRequestRequestTypeDef(BaseValidatorModel):
    audienceModelArn: str

class GetConfiguredAudienceModelPolicyRequestRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str

class GetConfiguredAudienceModelRequestRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str

class GetTrainingDatasetRequestRequestTypeDef(BaseValidatorModel):
    trainingDatasetArn: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAudienceExportJobsRequestRequestTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAudienceGenerationJobsRequestRequestTypeDef(BaseValidatorModel):
    collaborationId: Optional[str] = None
    configuredAudienceModelArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAudienceModelsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListConfiguredAudienceModelsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTrainingDatasetsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class TrainingDatasetSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    name: str
    status: Literal["ACTIVE"]
    trainingDatasetArn: str
    updateTime: datetime
    description: Optional[str] = None

class PutConfiguredAudienceModelPolicyRequestRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyExistenceCondition: Optional[PolicyExistenceConditionType] = None
    previousPolicyHash: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AudienceDestinationTypeDef(BaseValidatorModel):
    s3Destination: S3ConfigMapTypeDef

class AudienceGenerationJobDataSourceTypeDef(BaseValidatorModel):
    dataSource: S3ConfigMapTypeDef
    roleArn: str

class RelevanceMetricTypeDef(BaseValidatorModel):
    audienceSize: AudienceSizeTypeDef
    score: Optional[float] = None

class StartAudienceExportJobRequestRequestTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    name: str
    description: Optional[str] = None

class AudienceExportJobSummaryTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    createTime: datetime
    name: str
    status: AudienceExportJobStatusType
    updateTime: datetime
    description: Optional[str] = None
    outputLocation: Optional[str] = None
    statusDetails: Optional[StatusDetailsTypeDef] = None

class CreateAudienceModelRequestRequestTypeDef(BaseValidatorModel):
    name: str
    trainingDatasetArn: str
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    trainingDataEndTime: Optional[TimestampTypeDef] = None
    trainingDataStartTime: Optional[TimestampTypeDef] = None

class CreateAudienceModelResponseTypeDef(BaseValidatorModel):
    audienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConfiguredAudienceModelResponseTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainingDatasetResponseTypeDef(BaseValidatorModel):
    trainingDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAudienceModelResponseTypeDef(BaseValidatorModel):
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

class GetConfiguredAudienceModelPolicyResponseTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAudienceGenerationJobsResponseTypeDef(BaseValidatorModel):
    audienceGenerationJobs: List[AudienceGenerationJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAudienceModelsResponseTypeDef(BaseValidatorModel):
    audienceModels: List[AudienceModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutConfiguredAudienceModelPolicyResponseTypeDef(BaseValidatorModel):
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAudienceGenerationJobResponseTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConfiguredAudienceModelResponseTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceTypeDef(BaseValidatorModel):
    glueDataSource: GlueDataSourceTypeDef

class ListAudienceExportJobsRequestListAudienceExportJobsPaginateTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAudienceGenerationJobsRequestListAudienceGenerationJobsPaginateTypeDef(BaseValidatorModel):
    collaborationId: Optional[str] = None
    configuredAudienceModelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAudienceModelsRequestListAudienceModelsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConfiguredAudienceModelsRequestListConfiguredAudienceModelsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingDatasetsRequestListTrainingDatasetsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrainingDatasetsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    trainingDatasets: List[TrainingDatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ConfiguredAudienceModelOutputConfigTypeDef(BaseValidatorModel):
    destination: AudienceDestinationTypeDef
    roleArn: str

class StartAudienceGenerationJobRequestRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    name: str
    seedAudience: AudienceGenerationJobDataSourceTypeDef
    collaborationId: Optional[str] = None
    description: Optional[str] = None
    includeSeedInOutput: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None

class AudienceQualityMetricsTypeDef(BaseValidatorModel):
    relevanceMetrics: List[RelevanceMetricTypeDef]
    recallMetric: Optional[float] = None

class ListAudienceExportJobsResponseTypeDef(BaseValidatorModel):
    audienceExportJobs: List[AudienceExportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DatasetInputConfigTypeDef(BaseValidatorModel):
    dataSource: DataSourceTypeDef
    schema: Sequence[ColumnSchemaTypeDef]

class ConfiguredAudienceModelSummaryTypeDef(BaseValidatorModel):
    audienceModelArn: str
    configuredAudienceModelArn: str
    createTime: datetime
    name: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    status: Literal["ACTIVE"]
    updateTime: datetime
    description: Optional[str] = None

class CreateConfiguredAudienceModelRequestRequestTypeDef(BaseValidatorModel):
    audienceModelArn: str
    name: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    sharedAudienceMetrics: Sequence[SharedAudienceMetricsType]
    audienceSizeConfig: Optional[AudienceSizeConfigTypeDef] = None
    childResourceTagOnCreatePolicy: Optional[TagOnCreatePolicyType] = None
    description: Optional[str] = None
    minMatchingSeedSize: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class GetConfiguredAudienceModelResponseTypeDef(BaseValidatorModel):
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

class UpdateConfiguredAudienceModelRequestRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    audienceModelArn: Optional[str] = None
    audienceSizeConfig: Optional[AudienceSizeConfigTypeDef] = None
    description: Optional[str] = None
    minMatchingSeedSize: Optional[int] = None
    outputConfig: Optional[ConfiguredAudienceModelOutputConfigTypeDef] = None
    sharedAudienceMetrics: Optional[Sequence[SharedAudienceMetricsType]] = None

class GetAudienceGenerationJobResponseTypeDef(BaseValidatorModel):
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

class DatasetTypeDef(BaseValidatorModel):
    inputConfig: DatasetInputConfigTypeDef
    type: Literal["INTERACTIONS"]

class ListConfiguredAudienceModelsResponseTypeDef(BaseValidatorModel):
    configuredAudienceModels: List[ConfiguredAudienceModelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrainingDatasetRequestRequestTypeDef(BaseValidatorModel):
    name: str
    roleArn: str
    trainingData: Sequence[DatasetTypeDef]
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class GetTrainingDatasetResponseTypeDef(BaseValidatorModel):
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

