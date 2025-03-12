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
from aws_resource_validator.pydantic_models.cleanroomsml_constants import *

class S3ConfigMapTypeDef(BaseValidatorModel):
    s3Uri: str


class StatusDetailsTypeDef(BaseValidatorModel):
    statusCode: Optional[str] = None
    message: Optional[str] = None


class ProtectedQuerySQLParametersOutputTypeDef(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class ProtectedQuerySQLParametersTypeDef(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Mapping[str, str]] = None


class AudienceGenerationJobSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    audienceGenerationJobArn: str
    name: str
    status: AudienceGenerationJobStatusType
    configuredAudienceModelArn: str
    description: Optional[str] = None
    collaborationId: Optional[str] = None
    startedBy: Optional[str] = None


class AudienceModelSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    audienceModelArn: str
    name: str
    trainingDatasetArn: str
    status: AudienceModelStatusType
    description: Optional[str] = None


class AudienceSizeConfigOutputTypeDef(BaseValidatorModel):
    audienceSizeType: AudienceSizeTypeType
    audienceSizeBins: List[int]


class AudienceSizeConfigTypeDef(BaseValidatorModel):
    audienceSizeType: AudienceSizeTypeType
    audienceSizeBins: Sequence[int]


class CancelTrainedModelInferenceJobRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelInferenceJobArn: str


class CancelTrainedModelRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelArn: str


class CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    creatorAccountId: str
    description: Optional[str] = None


class CollaborationMLInputChannelSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    membershipIdentifier: str
    collaborationIdentifier: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    mlInputChannelArn: str
    status: MLInputChannelStatusType
    creatorAccountId: str
    description: Optional[str] = None


class CollaborationTrainedModelSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainedModelArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    status: TrainedModelStatusType
    configuredModelAlgorithmAssociationArn: str
    creatorAccountId: str
    description: Optional[str] = None


class ColumnSchemaOutputTypeDef(BaseValidatorModel):
    columnName: str
    columnTypes: List[ColumnTypeType]


class ColumnSchemaTypeDef(BaseValidatorModel):
    columnName: str
    columnTypes: Sequence[ColumnTypeType]


class ConfiguredModelAlgorithmAssociationSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    configuredModelAlgorithmArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    description: Optional[str] = None


class ConfiguredModelAlgorithmSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmArn: str
    name: str
    description: Optional[str] = None


class MetricDefinitionTypeDef(BaseValidatorModel):
    name: str
    regex: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class InferenceContainerConfigTypeDef(BaseValidatorModel):
    imageUri: str


class ModelTrainingDataChannelTypeDef(BaseValidatorModel):
    mlInputChannelArn: str
    channelName: str


class ResourceConfigTypeDef(BaseValidatorModel):
    instanceType: InstanceTypeType
    volumeSizeInGB: int
    instanceCount: Optional[int] = None


class StoppingConditionTypeDef(BaseValidatorModel):
    maxRuntimeInSeconds: Optional[int] = None


class GlueDataSourceTypeDef(BaseValidatorModel):
    tableName: str
    databaseName: str
    catalogId: Optional[str] = None


class DeleteAudienceGenerationJobRequestTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str


class DeleteAudienceModelRequestTypeDef(BaseValidatorModel):
    audienceModelArn: str


class DeleteConfiguredAudienceModelPolicyRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str


class DeleteConfiguredAudienceModelRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str


class DeleteConfiguredModelAlgorithmAssociationRequestTypeDef(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str


class DeleteConfiguredModelAlgorithmRequestTypeDef(BaseValidatorModel):
    configuredModelAlgorithmArn: str


class DeleteMLConfigurationRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str


class DeleteMLInputChannelDataRequestTypeDef(BaseValidatorModel):
    mlInputChannelArn: str
    membershipIdentifier: str


class DeleteTrainedModelOutputRequestTypeDef(BaseValidatorModel):
    trainedModelArn: str
    membershipIdentifier: str


class DeleteTrainingDatasetRequestTypeDef(BaseValidatorModel):
    trainingDatasetArn: str


class GetAudienceGenerationJobRequestTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: str


class GetAudienceModelRequestTypeDef(BaseValidatorModel):
    audienceModelArn: str


class GetCollaborationConfiguredModelAlgorithmAssociationRequestTypeDef(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    collaborationIdentifier: str


class GetCollaborationMLInputChannelRequestTypeDef(BaseValidatorModel):
    mlInputChannelArn: str
    collaborationIdentifier: str


class GetCollaborationTrainedModelRequestTypeDef(BaseValidatorModel):
    trainedModelArn: str
    collaborationIdentifier: str


class GetConfiguredAudienceModelPolicyRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str


class GetConfiguredAudienceModelRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str


class GetConfiguredModelAlgorithmAssociationRequestTypeDef(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str


class GetConfiguredModelAlgorithmRequestTypeDef(BaseValidatorModel):
    configuredModelAlgorithmArn: str


class GetMLConfigurationRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str


class GetMLInputChannelRequestTypeDef(BaseValidatorModel):
    mlInputChannelArn: str
    membershipIdentifier: str


class GetTrainedModelInferenceJobRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelInferenceJobArn: str


class InferenceContainerExecutionParametersTypeDef(BaseValidatorModel):
    maxPayloadInMB: Optional[int] = None


class InferenceResourceConfigTypeDef(BaseValidatorModel):
    instanceType: InferenceInstanceTypeType
    instanceCount: Optional[int] = None


class ModelInferenceDataSourceTypeDef(BaseValidatorModel):
    mlInputChannelArn: str


class GetTrainedModelRequestTypeDef(BaseValidatorModel):
    trainedModelArn: str
    membershipIdentifier: str


class GetTrainingDatasetRequestTypeDef(BaseValidatorModel):
    trainingDatasetArn: str


class InferenceReceiverMemberTypeDef(BaseValidatorModel):
    accountId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAudienceExportJobsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    audienceGenerationJobArn: Optional[str] = None


class ListAudienceGenerationJobsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    configuredAudienceModelArn: Optional[str] = None
    collaborationId: Optional[str] = None


class ListAudienceModelsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationConfiguredModelAlgorithmAssociationsRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationMLInputChannelsRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationTrainedModelExportJobsRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    trainedModelArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationTrainedModelInferenceJobsRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    trainedModelArn: Optional[str] = None


class ListCollaborationTrainedModelsRequestTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredAudienceModelsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredModelAlgorithmAssociationsRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredModelAlgorithmsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMLInputChannelsRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MLInputChannelSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    membershipIdentifier: str
    collaborationIdentifier: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    mlInputChannelArn: str
    status: MLInputChannelStatusType
    protectedQueryIdentifier: Optional[str] = None
    description: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTrainedModelInferenceJobsRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    trainedModelArn: Optional[str] = None


class ListTrainedModelsRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TrainedModelSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainedModelArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    status: TrainedModelStatusType
    configuredModelAlgorithmAssociationArn: str
    description: Optional[str] = None


class ListTrainingDatasetsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TrainingDatasetSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainingDatasetArn: str
    name: str
    status: Literal["ACTIVE"]
    description: Optional[str] = None


class LogsConfigurationPolicyOutputTypeDef(BaseValidatorModel):
    allowedAccountIds: List[str]
    filterPattern: Optional[str] = None


class LogsConfigurationPolicyTypeDef(BaseValidatorModel):
    allowedAccountIds: Sequence[str]
    filterPattern: Optional[str] = None


class MetricsConfigurationPolicyTypeDef(BaseValidatorModel):
    noiseLevel: NoiseLevelTypeType


class PutConfiguredAudienceModelPolicyRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    previousPolicyHash: Optional[str] = None
    policyExistenceCondition: Optional[PolicyExistenceConditionType] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TrainedModelExportReceiverMemberTypeDef(BaseValidatorModel):
    accountId: str


class TrainedModelExportsMaxSizeTypeDef(BaseValidatorModel):
    unit: Literal["GB"]
    value: float


class TrainedModelInferenceMaxOutputSizeTypeDef(BaseValidatorModel):
    unit: Literal["GB"]
    value: float


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AudienceDestinationTypeDef(BaseValidatorModel):
    s3Destination: S3ConfigMapTypeDef


class DestinationTypeDef(BaseValidatorModel):
    s3Destination: S3ConfigMapTypeDef


class AudienceSizeTypeDef(BaseValidatorModel):
    pass


class RelevanceMetricTypeDef(BaseValidatorModel):
    audienceSize: AudienceSizeTypeDef
    score: Optional[float] = None


class StartAudienceExportJobRequestTypeDef(BaseValidatorModel):
    name: str
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    description: Optional[str] = None


class AudienceExportJobSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    name: str
    audienceGenerationJobArn: str
    audienceSize: AudienceSizeTypeDef
    status: AudienceExportJobStatusType
    description: Optional[str] = None
    statusDetails: Optional[StatusDetailsTypeDef] = None
    outputLocation: Optional[str] = None


class WorkerComputeConfigurationTypeDef(BaseValidatorModel):
    pass


class ComputeConfigurationTypeDef(BaseValidatorModel):
    worker: Optional[WorkerComputeConfigurationTypeDef] = None


class ContainerConfigOutputTypeDef(BaseValidatorModel):
    imageUri: str
    entrypoint: Optional[List[str]] = None
    arguments: Optional[List[str]] = None
    metricDefinitions: Optional[List[MetricDefinitionTypeDef]] = None


class ContainerConfigTypeDef(BaseValidatorModel):
    imageUri: str
    entrypoint: Optional[Sequence[str]] = None
    arguments: Optional[Sequence[str]] = None
    metricDefinitions: Optional[Sequence[MetricDefinitionTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateAudienceModelRequestTypeDef(BaseValidatorModel):
    name: str
    trainingDatasetArn: str
    trainingDataStartTime: Optional[TimestampTypeDef] = None
    trainingDataEndTime: Optional[TimestampTypeDef] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None


class CreateAudienceModelResponseTypeDef(BaseValidatorModel):
    audienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConfiguredAudienceModelResponseTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConfiguredModelAlgorithmAssociationResponseTypeDef(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConfiguredModelAlgorithmResponseTypeDef(BaseValidatorModel):
    configuredModelAlgorithmArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMLInputChannelResponseTypeDef(BaseValidatorModel):
    mlInputChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrainedModelResponseTypeDef(BaseValidatorModel):
    trainedModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrainingDatasetResponseTypeDef(BaseValidatorModel):
    trainingDatasetArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAudienceModelResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainingDataStartTime: datetime
    trainingDataEndTime: datetime
    audienceModelArn: str
    name: str
    trainingDatasetArn: str
    status: AudienceModelStatusType
    statusDetails: StatusDetailsTypeDef
    kmsKeyArn: str
    tags: Dict[str, str]
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCollaborationMLInputChannelResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    membershipIdentifier: str
    collaborationIdentifier: str
    mlInputChannelArn: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    status: MLInputChannelStatusType
    statusDetails: StatusDetailsTypeDef
    retentionInDays: int
    numberOfRecords: int
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfiguredAudienceModelPolicyResponseTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAudienceGenerationJobsResponseTypeDef(BaseValidatorModel):
    audienceGenerationJobs: List[AudienceGenerationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAudienceModelsResponseTypeDef(BaseValidatorModel):
    audienceModels: List[AudienceModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCollaborationConfiguredModelAlgorithmAssociationsResponseTypeDef(BaseValidatorModel):
    collaborationConfiguredModelAlgorithmAssociations: List[ CollaborationConfiguredModelAlgorithmAssociationSummaryTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCollaborationMLInputChannelsResponseTypeDef(BaseValidatorModel):
    collaborationMLInputChannelsList: List[CollaborationMLInputChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListCollaborationTrainedModelsResponseTypeDef(BaseValidatorModel):
    collaborationTrainedModels: List[CollaborationTrainedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListConfiguredModelAlgorithmAssociationsResponseTypeDef(BaseValidatorModel):
    configuredModelAlgorithmAssociations: List[ConfiguredModelAlgorithmAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListConfiguredModelAlgorithmsResponseTypeDef(BaseValidatorModel):
    configuredModelAlgorithms: List[ConfiguredModelAlgorithmSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class StartTrainedModelInferenceJobResponseTypeDef(BaseValidatorModel):
    trainedModelInferenceJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfiguredAudienceModelResponseTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTrainedModelRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfigTypeDef
    dataChannels: Sequence[ModelTrainingDataChannelTypeDef]
    hyperparameters: Optional[Mapping[str, str]] = None
    environment: Optional[Mapping[str, str]] = None
    stoppingCondition: Optional[StoppingConditionTypeDef] = None
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class GetCollaborationTrainedModelResponseTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    collaborationIdentifier: str
    trainedModelArn: str
    name: str
    description: str
    status: TrainedModelStatusType
    statusDetails: StatusDetailsTypeDef
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfigTypeDef
    stoppingCondition: StoppingConditionTypeDef
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    trainingContainerImageDigest: str
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTrainedModelResponseTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    collaborationIdentifier: str
    trainedModelArn: str
    name: str
    description: str
    status: TrainedModelStatusType
    statusDetails: StatusDetailsTypeDef
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfigTypeDef
    stoppingCondition: StoppingConditionTypeDef
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    trainingContainerImageDigest: str
    createTime: datetime
    updateTime: datetime
    hyperparameters: Dict[str, str]
    environment: Dict[str, str]
    kmsKeyArn: str
    tags: Dict[str, str]
    dataChannels: List[ModelTrainingDataChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DataSourceTypeDef(BaseValidatorModel):
    glueDataSource: GlueDataSourceTypeDef


class InferenceOutputConfigurationOutputTypeDef(BaseValidatorModel):
    members: List[InferenceReceiverMemberTypeDef]
    accept: Optional[str] = None


class InferenceOutputConfigurationTypeDef(BaseValidatorModel):
    members: Sequence[InferenceReceiverMemberTypeDef]
    accept: Optional[str] = None


class ListAudienceExportJobsRequestPaginateTypeDef(BaseValidatorModel):
    audienceGenerationJobArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAudienceGenerationJobsRequestPaginateTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: Optional[str] = None
    collaborationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAudienceModelsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationMLInputChannelsRequestPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationTrainedModelExportJobsRequestPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    trainedModelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationTrainedModelInferenceJobsRequestPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    trainedModelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCollaborationTrainedModelsRequestPaginateTypeDef(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfiguredAudienceModelsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfiguredModelAlgorithmAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConfiguredModelAlgorithmsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMLInputChannelsRequestPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrainedModelInferenceJobsRequestPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrainedModelsRequestPaginateTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrainingDatasetsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMLInputChannelsResponseTypeDef(BaseValidatorModel):
    mlInputChannelsList: List[MLInputChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTrainedModelsResponseTypeDef(BaseValidatorModel):
    trainedModels: List[TrainedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTrainingDatasetsResponseTypeDef(BaseValidatorModel):
    trainingDatasets: List[TrainingDatasetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TrainedModelsConfigurationPolicyOutputTypeDef(BaseValidatorModel):
    containerLogs: Optional[List[LogsConfigurationPolicyOutputTypeDef]] = None
    containerMetrics: Optional[MetricsConfigurationPolicyTypeDef] = None


class TrainedModelsConfigurationPolicyTypeDef(BaseValidatorModel):
    containerLogs: Optional[Sequence[LogsConfigurationPolicyTypeDef]] = None
    containerMetrics: Optional[MetricsConfigurationPolicyTypeDef] = None


class TrainedModelExportOutputConfigurationOutputTypeDef(BaseValidatorModel):
    members: List[TrainedModelExportReceiverMemberTypeDef]


class TrainedModelExportOutputConfigurationTypeDef(BaseValidatorModel):
    members: Sequence[TrainedModelExportReceiverMemberTypeDef]


class TrainedModelExportsConfigurationPolicyOutputTypeDef(BaseValidatorModel):
    maxSize: TrainedModelExportsMaxSizeTypeDef
    filesToExport: List[TrainedModelExportFileTypeType]


class TrainedModelExportsConfigurationPolicyTypeDef(BaseValidatorModel):
    maxSize: TrainedModelExportsMaxSizeTypeDef
    filesToExport: Sequence[TrainedModelExportFileTypeType]


class TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef(BaseValidatorModel):
    containerLogs: Optional[List[LogsConfigurationPolicyOutputTypeDef]] = None
    maxOutputSize: Optional[TrainedModelInferenceMaxOutputSizeTypeDef] = None


class TrainedModelInferenceJobsConfigurationPolicyTypeDef(BaseValidatorModel):
    containerLogs: Optional[Sequence[LogsConfigurationPolicyTypeDef]] = None
    maxOutputSize: Optional[TrainedModelInferenceMaxOutputSizeTypeDef] = None


class ConfiguredAudienceModelOutputConfigTypeDef(BaseValidatorModel):
    destination: AudienceDestinationTypeDef
    roleArn: str


class MLOutputConfigurationTypeDef(BaseValidatorModel):
    roleArn: str
    destination: Optional[DestinationTypeDef] = None


class AudienceQualityMetricsTypeDef(BaseValidatorModel):
    relevanceMetrics: List[RelevanceMetricTypeDef]
    recallMetric: Optional[float] = None


class ListAudienceExportJobsResponseTypeDef(BaseValidatorModel):
    audienceExportJobs: List[AudienceExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AudienceGenerationJobDataSourceOutputTypeDef(BaseValidatorModel):
    roleArn: str
    dataSource: Optional[S3ConfigMapTypeDef] = None
    sqlParameters: Optional[ProtectedQuerySQLParametersOutputTypeDef] = None
    sqlComputeConfiguration: Optional[ComputeConfigurationTypeDef] = None


class AudienceGenerationJobDataSourceTypeDef(BaseValidatorModel):
    roleArn: str
    dataSource: Optional[S3ConfigMapTypeDef] = None
    sqlParameters: Optional[ProtectedQuerySQLParametersTypeDef] = None
    sqlComputeConfiguration: Optional[ComputeConfigurationTypeDef] = None


class ProtectedQueryInputParametersOutputTypeDef(BaseValidatorModel):
    sqlParameters: ProtectedQuerySQLParametersOutputTypeDef
    computeConfiguration: Optional[ComputeConfigurationTypeDef] = None


class ProtectedQueryInputParametersTypeDef(BaseValidatorModel):
    sqlParameters: ProtectedQuerySQLParametersTypeDef
    computeConfiguration: Optional[ComputeConfigurationTypeDef] = None


class GetConfiguredModelAlgorithmResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmArn: str
    name: str
    trainingContainerConfig: ContainerConfigOutputTypeDef
    inferenceContainerConfig: InferenceContainerConfigTypeDef
    roleArn: str
    description: str
    tags: Dict[str, str]
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DatasetInputConfigOutputTypeDef(BaseValidatorModel):
    schema: List[ColumnSchemaOutputTypeDef]
    dataSource: DataSourceTypeDef


class ColumnSchemaUnionTypeDef(BaseValidatorModel):
    pass


class DatasetInputConfigTypeDef(BaseValidatorModel):
    schema: Sequence[ColumnSchemaUnionTypeDef]
    dataSource: DataSourceTypeDef


class CollaborationTrainedModelInferenceJobSummaryTypeDef(BaseValidatorModel):
    trainedModelInferenceJobArn: str
    membershipIdentifier: str
    trainedModelArn: str
    collaborationIdentifier: str
    status: TrainedModelInferenceJobStatusType
    outputConfiguration: InferenceOutputConfigurationOutputTypeDef
    name: str
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    configuredModelAlgorithmAssociationArn: Optional[str] = None
    description: Optional[str] = None
    metricsStatus: Optional[MetricsStatusType] = None
    metricsStatusDetails: Optional[str] = None
    logsStatus: Optional[LogsStatusType] = None
    logsStatusDetails: Optional[str] = None


class GetTrainedModelInferenceJobResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainedModelInferenceJobArn: str
    configuredModelAlgorithmAssociationArn: str
    name: str
    status: TrainedModelInferenceJobStatusType
    trainedModelArn: str
    resourceConfig: InferenceResourceConfigTypeDef
    outputConfiguration: InferenceOutputConfigurationOutputTypeDef
    membershipIdentifier: str
    dataSource: ModelInferenceDataSourceTypeDef
    containerExecutionParameters: InferenceContainerExecutionParametersTypeDef
    statusDetails: StatusDetailsTypeDef
    description: str
    inferenceContainerImageDigest: str
    environment: Dict[str, str]
    kmsKeyArn: str
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class TrainedModelInferenceJobSummaryTypeDef(BaseValidatorModel):
    trainedModelInferenceJobArn: str
    membershipIdentifier: str
    trainedModelArn: str
    collaborationIdentifier: str
    status: TrainedModelInferenceJobStatusType
    outputConfiguration: InferenceOutputConfigurationOutputTypeDef
    name: str
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: Optional[str] = None
    description: Optional[str] = None
    metricsStatus: Optional[MetricsStatusType] = None
    metricsStatusDetails: Optional[str] = None
    logsStatus: Optional[LogsStatusType] = None
    logsStatusDetails: Optional[str] = None


class CollaborationTrainedModelExportJobSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    name: str
    outputConfiguration: TrainedModelExportOutputConfigurationOutputTypeDef
    status: TrainedModelExportJobStatusType
    creatorAccountId: str
    trainedModelArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    statusDetails: Optional[StatusDetailsTypeDef] = None
    description: Optional[str] = None


class PrivacyConfigurationPoliciesOutputTypeDef(BaseValidatorModel):
    trainedModels: Optional[TrainedModelsConfigurationPolicyOutputTypeDef] = None
    trainedModelExports: Optional[TrainedModelExportsConfigurationPolicyOutputTypeDef] = None
    trainedModelInferenceJobs: Optional[ TrainedModelInferenceJobsConfigurationPolicyOutputTypeDef ] = None


class PrivacyConfigurationPoliciesTypeDef(BaseValidatorModel):
    trainedModels: Optional[TrainedModelsConfigurationPolicyTypeDef] = None
    trainedModelExports: Optional[TrainedModelExportsConfigurationPolicyTypeDef] = None
    trainedModelInferenceJobs: Optional[TrainedModelInferenceJobsConfigurationPolicyTypeDef] = None


class ConfiguredAudienceModelSummaryTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    configuredAudienceModelArn: str
    status: Literal["ACTIVE"]
    description: Optional[str] = None


class AudienceSizeConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredAudienceModelRequestTypeDef(BaseValidatorModel):
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    sharedAudienceMetrics: Sequence[SharedAudienceMetricsType]
    description: Optional[str] = None
    minMatchingSeedSize: Optional[int] = None
    audienceSizeConfig: Optional[AudienceSizeConfigUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    childResourceTagOnCreatePolicy: Optional[TagOnCreatePolicyType] = None


class GetConfiguredAudienceModelResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredAudienceModelArn: str
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfigTypeDef
    description: str
    status: Literal["ACTIVE"]
    sharedAudienceMetrics: List[SharedAudienceMetricsType]
    minMatchingSeedSize: int
    audienceSizeConfig: AudienceSizeConfigOutputTypeDef
    tags: Dict[str, str]
    childResourceTagOnCreatePolicy: TagOnCreatePolicyType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConfiguredAudienceModelRequestTypeDef(BaseValidatorModel):
    configuredAudienceModelArn: str
    outputConfig: Optional[ConfiguredAudienceModelOutputConfigTypeDef] = None
    audienceModelArn: Optional[str] = None
    sharedAudienceMetrics: Optional[Sequence[SharedAudienceMetricsType]] = None
    minMatchingSeedSize: Optional[int] = None
    audienceSizeConfig: Optional[AudienceSizeConfigUnionTypeDef] = None
    description: Optional[str] = None


class GetMLConfigurationResponseTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfigurationTypeDef
    createTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class PutMLConfigurationRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfigurationTypeDef


class GetAudienceGenerationJobResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    audienceGenerationJobArn: str
    name: str
    description: str
    status: AudienceGenerationJobStatusType
    statusDetails: StatusDetailsTypeDef
    configuredAudienceModelArn: str
    seedAudience: AudienceGenerationJobDataSourceOutputTypeDef
    includeSeedInOutput: bool
    collaborationId: str
    metrics: AudienceQualityMetricsTypeDef
    startedBy: str
    tags: Dict[str, str]
    protectedQueryIdentifier: str
    ResponseMetadata: ResponseMetadataTypeDef


class InputChannelDataSourceOutputTypeDef(BaseValidatorModel):
    protectedQueryInputParameters: Optional[ProtectedQueryInputParametersOutputTypeDef] = None


class InputChannelDataSourceTypeDef(BaseValidatorModel):
    protectedQueryInputParameters: Optional[ProtectedQueryInputParametersTypeDef] = None


class ContainerConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredModelAlgorithmRequestTypeDef(BaseValidatorModel):
    name: str
    roleArn: str
    description: Optional[str] = None
    trainingContainerConfig: Optional[ContainerConfigUnionTypeDef] = None
    inferenceContainerConfig: Optional[InferenceContainerConfigTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None


class ListCollaborationTrainedModelInferenceJobsResponseTypeDef(BaseValidatorModel):
    collaborationTrainedModelInferenceJobs: List[ CollaborationTrainedModelInferenceJobSummaryTypeDef ]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTrainedModelInferenceJobsResponseTypeDef(BaseValidatorModel):
    trainedModelInferenceJobs: List[TrainedModelInferenceJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class InferenceOutputConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class StartTrainedModelInferenceJobRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    trainedModelArn: str
    resourceConfig: InferenceResourceConfigTypeDef
    outputConfiguration: InferenceOutputConfigurationUnionTypeDef
    dataSource: ModelInferenceDataSourceTypeDef
    configuredModelAlgorithmAssociationArn: Optional[str] = None
    description: Optional[str] = None
    containerExecutionParameters: Optional[InferenceContainerExecutionParametersTypeDef] = None
    environment: Optional[Mapping[str, str]] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ListCollaborationTrainedModelExportJobsResponseTypeDef(BaseValidatorModel):
    collaborationTrainedModelExportJobs: List[CollaborationTrainedModelExportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TrainedModelExportOutputConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class StartTrainedModelExportJobRequestTypeDef(BaseValidatorModel):
    name: str
    trainedModelArn: str
    membershipIdentifier: str
    outputConfiguration: TrainedModelExportOutputConfigurationUnionTypeDef
    description: Optional[str] = None


class PrivacyConfigurationOutputTypeDef(BaseValidatorModel):
    policies: PrivacyConfigurationPoliciesOutputTypeDef


class PrivacyConfigurationTypeDef(BaseValidatorModel):
    policies: PrivacyConfigurationPoliciesTypeDef


class ListConfiguredAudienceModelsResponseTypeDef(BaseValidatorModel):
    configuredAudienceModels: List[ConfiguredAudienceModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AudienceGenerationJobDataSourceUnionTypeDef(BaseValidatorModel):
    pass


class StartAudienceGenerationJobRequestTypeDef(BaseValidatorModel):
    name: str
    configuredAudienceModelArn: str
    seedAudience: AudienceGenerationJobDataSourceUnionTypeDef
    includeSeedInOutput: Optional[bool] = None
    collaborationId: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class InputChannelOutputTypeDef(BaseValidatorModel):
    dataSource: InputChannelDataSourceOutputTypeDef
    roleArn: str


class InputChannelTypeDef(BaseValidatorModel):
    dataSource: InputChannelDataSourceTypeDef
    roleArn: str


class DatasetOutputTypeDef(BaseValidatorModel):
    pass


class GetTrainingDatasetResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainingDatasetArn: str
    name: str
    trainingData: List[DatasetOutputTypeDef]
    status: Literal["ACTIVE"]
    roleArn: str
    tags: Dict[str, str]
    description: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCollaborationConfiguredModelAlgorithmAssociationResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    description: str
    creatorAccountId: str
    privacyConfiguration: PrivacyConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConfiguredModelAlgorithmAssociationResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    privacyConfiguration: PrivacyConfigurationOutputTypeDef
    description: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetMLInputChannelResponseTypeDef(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    membershipIdentifier: str
    collaborationIdentifier: str
    inputChannel: InputChannelOutputTypeDef
    protectedQueryIdentifier: str
    mlInputChannelArn: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    status: MLInputChannelStatusType
    statusDetails: StatusDetailsTypeDef
    retentionInDays: int
    numberOfRecords: int
    numberOfFiles: float
    sizeInGb: float
    description: str
    kmsKeyArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PrivacyConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateConfiguredModelAlgorithmAssociationRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    description: Optional[str] = None
    privacyConfiguration: Optional[PrivacyConfigurationUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class InputChannelUnionTypeDef(BaseValidatorModel):
    pass


class CreateMLInputChannelRequestTypeDef(BaseValidatorModel):
    membershipIdentifier: str
    configuredModelAlgorithmAssociations: Sequence[str]
    inputChannel: InputChannelUnionTypeDef
    name: str
    retentionInDays: int
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DatasetUnionTypeDef(BaseValidatorModel):
    pass


class CreateTrainingDatasetRequestTypeDef(BaseValidatorModel):
    name: str
    roleArn: str
    trainingData: Sequence[DatasetUnionTypeDef]
    tags: Optional[Mapping[str, str]] = None
    description: Optional[str] = None


