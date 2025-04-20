from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cleanroomsml.cleanroomsml_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class S3ConfigMap(BaseValidatorModel):
    s3Uri: str


class AudienceSize(BaseValidatorModel):
    type: AudienceSizeTypeType
    value: int


class StatusDetails(BaseValidatorModel):
    statusCode: Optional[str] = None
    message: Optional[str] = None


class ProtectedQuerySQLParametersOutput(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class ProtectedQuerySQLParameters(BaseValidatorModel):
    queryString: Optional[str] = None
    analysisTemplateArn: Optional[str] = None
    parameters: Optional[Dict[str, str]] = None


class AudienceGenerationJobSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    audienceGenerationJobArn: str
    name: str
    status: AudienceGenerationJobStatusType
    configuredAudienceModelArn: str
    description: Optional[str] = None
    collaborationId: Optional[str] = None
    startedBy: Optional[str] = None


class AudienceModelSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    audienceModelArn: str
    name: str
    trainingDatasetArn: str
    status: AudienceModelStatusType
    description: Optional[str] = None


class AudienceSizeConfigOutput(BaseValidatorModel):
    audienceSizeType: AudienceSizeTypeType
    audienceSizeBins: List[int]


class AudienceSizeConfig(BaseValidatorModel):
    audienceSizeType: AudienceSizeTypeType
    audienceSizeBins: List[int]


class CancelTrainedModelInferenceJobRequest(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelInferenceJobArn: str


class CancelTrainedModelRequest(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelArn: str


class CollaborationConfiguredModelAlgorithmAssociationSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    creatorAccountId: str
    description: Optional[str] = None


class CollaborationMLInputChannelSummary(BaseValidatorModel):
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


class CollaborationTrainedModelSummary(BaseValidatorModel):
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


class ColumnSchemaOutput(BaseValidatorModel):
    columnName: str
    columnTypes: List[ColumnTypeType]


class ColumnSchema(BaseValidatorModel):
    columnName: str
    columnTypes: List[ColumnTypeType]


class WorkerComputeConfiguration(BaseValidatorModel):
    type: Optional[WorkerComputeTypeType] = None
    number: Optional[int] = None


class ConfiguredModelAlgorithmAssociationSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    configuredModelAlgorithmArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    description: Optional[str] = None


class ConfiguredModelAlgorithmSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmArn: str
    name: str
    description: Optional[str] = None


class MetricDefinition(BaseValidatorModel):
    name: str
    regex: str

Timestamp = Union[datetime, str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class InferenceContainerConfig(BaseValidatorModel):
    imageUri: str


class ModelTrainingDataChannel(BaseValidatorModel):
    mlInputChannelArn: str
    channelName: str


class ResourceConfig(BaseValidatorModel):
    instanceType: InstanceTypeType
    volumeSizeInGB: int
    instanceCount: Optional[int] = None


class StoppingCondition(BaseValidatorModel):
    maxRuntimeInSeconds: Optional[int] = None


class GlueDataSource(BaseValidatorModel):
    tableName: str
    databaseName: str
    catalogId: Optional[str] = None


class DeleteAudienceGenerationJobRequest(BaseValidatorModel):
    audienceGenerationJobArn: str


class DeleteAudienceModelRequest(BaseValidatorModel):
    audienceModelArn: str


class DeleteConfiguredAudienceModelPolicyRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


class DeleteConfiguredAudienceModelRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


class DeleteConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str


class DeleteConfiguredModelAlgorithmRequest(BaseValidatorModel):
    configuredModelAlgorithmArn: str


class DeleteMLConfigurationRequest(BaseValidatorModel):
    membershipIdentifier: str


class DeleteMLInputChannelDataRequest(BaseValidatorModel):
    mlInputChannelArn: str
    membershipIdentifier: str


class DeleteTrainedModelOutputRequest(BaseValidatorModel):
    trainedModelArn: str
    membershipIdentifier: str


class DeleteTrainingDatasetRequest(BaseValidatorModel):
    trainingDatasetArn: str


class GetAudienceGenerationJobRequest(BaseValidatorModel):
    audienceGenerationJobArn: str


class GetAudienceModelRequest(BaseValidatorModel):
    audienceModelArn: str


class GetCollaborationConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    collaborationIdentifier: str


class GetCollaborationMLInputChannelRequest(BaseValidatorModel):
    mlInputChannelArn: str
    collaborationIdentifier: str


class GetCollaborationTrainedModelRequest(BaseValidatorModel):
    trainedModelArn: str
    collaborationIdentifier: str


class GetConfiguredAudienceModelPolicyRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


class GetConfiguredAudienceModelRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


class GetConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str


class GetConfiguredModelAlgorithmRequest(BaseValidatorModel):
    configuredModelAlgorithmArn: str


class GetMLConfigurationRequest(BaseValidatorModel):
    membershipIdentifier: str


class GetMLInputChannelRequest(BaseValidatorModel):
    mlInputChannelArn: str
    membershipIdentifier: str


class GetTrainedModelInferenceJobRequest(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelInferenceJobArn: str


class InferenceContainerExecutionParameters(BaseValidatorModel):
    maxPayloadInMB: Optional[int] = None


class InferenceResourceConfig(BaseValidatorModel):
    instanceType: InferenceInstanceTypeType
    instanceCount: Optional[int] = None


class ModelInferenceDataSource(BaseValidatorModel):
    mlInputChannelArn: str


class GetTrainedModelRequest(BaseValidatorModel):
    trainedModelArn: str
    membershipIdentifier: str


class GetTrainingDatasetRequest(BaseValidatorModel):
    trainingDatasetArn: str


class InferenceReceiverMember(BaseValidatorModel):
    accountId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAudienceExportJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    audienceGenerationJobArn: Optional[str] = None


class ListAudienceGenerationJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    configuredAudienceModelArn: Optional[str] = None
    collaborationId: Optional[str] = None


class ListAudienceModelsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationConfiguredModelAlgorithmAssociationsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationMLInputChannelsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationTrainedModelExportJobsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    trainedModelArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListCollaborationTrainedModelInferenceJobsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    trainedModelArn: Optional[str] = None


class ListCollaborationTrainedModelsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredAudienceModelsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredModelAlgorithmAssociationsRequest(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConfiguredModelAlgorithmsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMLInputChannelsRequest(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MLInputChannelSummary(BaseValidatorModel):
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


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTrainedModelInferenceJobsRequest(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    trainedModelArn: Optional[str] = None


class ListTrainedModelsRequest(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TrainedModelSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainedModelArn: str
    name: str
    membershipIdentifier: str
    collaborationIdentifier: str
    status: TrainedModelStatusType
    configuredModelAlgorithmAssociationArn: str
    description: Optional[str] = None


class ListTrainingDatasetsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class TrainingDatasetSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainingDatasetArn: str
    name: str
    status: Literal['ACTIVE']
    description: Optional[str] = None


class LogsConfigurationPolicyOutput(BaseValidatorModel):
    allowedAccountIds: List[str]
    filterPattern: Optional[str] = None


class LogsConfigurationPolicy(BaseValidatorModel):
    allowedAccountIds: List[str]
    filterPattern: Optional[str] = None


class MetricsConfigurationPolicy(BaseValidatorModel):
    noiseLevel: NoiseLevelTypeType


class PutConfiguredAudienceModelPolicyRequest(BaseValidatorModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    previousPolicyHash: Optional[str] = None
    policyExistenceCondition: Optional[PolicyExistenceConditionType] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TrainedModelExportReceiverMember(BaseValidatorModel):
    accountId: str


class TrainedModelExportsMaxSize(BaseValidatorModel):
    unit: Literal['GB']
    value: float


class TrainedModelInferenceMaxOutputSize(BaseValidatorModel):
    unit: Literal['GB']
    value: float


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class AudienceDestination(BaseValidatorModel):
    s3Destination: S3ConfigMap


class Destination(BaseValidatorModel):
    s3Destination: S3ConfigMap


class RelevanceMetric(BaseValidatorModel):
    audienceSize: AudienceSize
    score: Optional[float] = None


class StartAudienceExportJobRequest(BaseValidatorModel):
    name: str
    audienceGenerationJobArn: str
    audienceSize: AudienceSize
    description: Optional[str] = None


class AudienceExportJobSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    name: str
    audienceGenerationJobArn: str
    audienceSize: AudienceSize
    status: AudienceExportJobStatusType
    description: Optional[str] = None
    statusDetails: Optional[StatusDetails] = None
    outputLocation: Optional[str] = None

AudienceSizeConfigUnion = Union[AudienceSizeConfig, AudienceSizeConfigOutput]

ColumnSchemaUnion = Union[ColumnSchema, ColumnSchemaOutput]


class ComputeConfiguration(BaseValidatorModel):
    worker: Optional[WorkerComputeConfiguration] = None


class ContainerConfigOutput(BaseValidatorModel):
    imageUri: str
    entrypoint: Optional[List[str]] = None
    arguments: Optional[List[str]] = None
    metricDefinitions: Optional[List[MetricDefinition]] = None


class ContainerConfig(BaseValidatorModel):
    imageUri: str
    entrypoint: Optional[List[str]] = None
    arguments: Optional[List[str]] = None
    metricDefinitions: Optional[List[MetricDefinition]] = None


class CreateAudienceModelRequest(BaseValidatorModel):
    name: str
    trainingDatasetArn: str
    trainingDataStartTime: Optional[Timestamp] = None
    trainingDataEndTime: Optional[Timestamp] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    description: Optional[str] = None


class CreateAudienceModelResponse(BaseValidatorModel):
    audienceModelArn: str
    ResponseMetadata: ResponseMetadata


class CreateConfiguredAudienceModelResponse(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadata


class CreateConfiguredModelAlgorithmAssociationResponse(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    ResponseMetadata: ResponseMetadata


class CreateConfiguredModelAlgorithmResponse(BaseValidatorModel):
    configuredModelAlgorithmArn: str
    ResponseMetadata: ResponseMetadata


class CreateMLInputChannelResponse(BaseValidatorModel):
    mlInputChannelArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrainedModelResponse(BaseValidatorModel):
    trainedModelArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrainingDatasetResponse(BaseValidatorModel):
    trainingDatasetArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAudienceModelResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainingDataStartTime: datetime
    trainingDataEndTime: datetime
    audienceModelArn: str
    name: str
    trainingDatasetArn: str
    status: AudienceModelStatusType
    statusDetails: StatusDetails
    kmsKeyArn: str
    tags: Dict[str, str]
    description: str
    ResponseMetadata: ResponseMetadata


class GetCollaborationMLInputChannelResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    membershipIdentifier: str
    collaborationIdentifier: str
    mlInputChannelArn: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    status: MLInputChannelStatusType
    statusDetails: StatusDetails
    retentionInDays: int
    numberOfRecords: int
    description: str
    ResponseMetadata: ResponseMetadata


class GetConfiguredAudienceModelPolicyResponse(BaseValidatorModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadata


class ListAudienceGenerationJobsResponse(BaseValidatorModel):
    audienceGenerationJobs: List[AudienceGenerationJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAudienceModelsResponse(BaseValidatorModel):
    audienceModels: List[AudienceModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCollaborationConfiguredModelAlgorithmAssociationsResponse(BaseValidatorModel):
    collaborationConfiguredModelAlgorithmAssociations: List[CollaborationConfiguredModelAlgorithmAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCollaborationMLInputChannelsResponse(BaseValidatorModel):
    collaborationMLInputChannelsList: List[CollaborationMLInputChannelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListCollaborationTrainedModelsResponse(BaseValidatorModel):
    collaborationTrainedModels: List[CollaborationTrainedModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListConfiguredModelAlgorithmAssociationsResponse(BaseValidatorModel):
    configuredModelAlgorithmAssociations: List[ConfiguredModelAlgorithmAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListConfiguredModelAlgorithmsResponse(BaseValidatorModel):
    configuredModelAlgorithms: List[ConfiguredModelAlgorithmSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutConfiguredAudienceModelPolicyResponse(BaseValidatorModel):
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadata


class StartAudienceGenerationJobResponse(BaseValidatorModel):
    audienceGenerationJobArn: str
    ResponseMetadata: ResponseMetadata


class StartTrainedModelInferenceJobResponse(BaseValidatorModel):
    trainedModelInferenceJobArn: str
    ResponseMetadata: ResponseMetadata


class UpdateConfiguredAudienceModelResponse(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadata


class CreateTrainedModelRequest(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfig
    dataChannels: List[ModelTrainingDataChannel]
    hyperparameters: Optional[Dict[str, str]] = None
    environment: Optional[Dict[str, str]] = None
    stoppingCondition: Optional[StoppingCondition] = None
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class GetCollaborationTrainedModelResponse(BaseValidatorModel):
    membershipIdentifier: str
    collaborationIdentifier: str
    trainedModelArn: str
    name: str
    description: str
    status: TrainedModelStatusType
    statusDetails: StatusDetails
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfig
    stoppingCondition: StoppingCondition
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    trainingContainerImageDigest: str
    createTime: datetime
    updateTime: datetime
    creatorAccountId: str
    ResponseMetadata: ResponseMetadata


class GetTrainedModelResponse(BaseValidatorModel):
    membershipIdentifier: str
    collaborationIdentifier: str
    trainedModelArn: str
    name: str
    description: str
    status: TrainedModelStatusType
    statusDetails: StatusDetails
    configuredModelAlgorithmAssociationArn: str
    resourceConfig: ResourceConfig
    stoppingCondition: StoppingCondition
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
    dataChannels: List[ModelTrainingDataChannel]
    ResponseMetadata: ResponseMetadata


class DataSource(BaseValidatorModel):
    glueDataSource: GlueDataSource


class InferenceOutputConfigurationOutput(BaseValidatorModel):
    members: List[InferenceReceiverMember]
    accept: Optional[str] = None


class InferenceOutputConfiguration(BaseValidatorModel):
    members: List[InferenceReceiverMember]
    accept: Optional[str] = None


class ListAudienceExportJobsRequestPaginate(BaseValidatorModel):
    audienceGenerationJobArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAudienceGenerationJobsRequestPaginate(BaseValidatorModel):
    configuredAudienceModelArn: Optional[str] = None
    collaborationId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAudienceModelsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationConfiguredModelAlgorithmAssociationsRequestPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationMLInputChannelsRequestPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationTrainedModelExportJobsRequestPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    trainedModelArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationTrainedModelInferenceJobsRequestPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    trainedModelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCollaborationTrainedModelsRequestPaginate(BaseValidatorModel):
    collaborationIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfiguredAudienceModelsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfiguredModelAlgorithmAssociationsRequestPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConfiguredModelAlgorithmsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMLInputChannelsRequestPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrainedModelInferenceJobsRequestPaginate(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrainedModelsRequestPaginate(BaseValidatorModel):
    membershipIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrainingDatasetsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMLInputChannelsResponse(BaseValidatorModel):
    mlInputChannelsList: List[MLInputChannelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTrainedModelsResponse(BaseValidatorModel):
    trainedModels: List[TrainedModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTrainingDatasetsResponse(BaseValidatorModel):
    trainingDatasets: List[TrainingDatasetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TrainedModelsConfigurationPolicyOutput(BaseValidatorModel):
    containerLogs: Optional[List[LogsConfigurationPolicyOutput]] = None
    containerMetrics: Optional[MetricsConfigurationPolicy] = None


class TrainedModelsConfigurationPolicy(BaseValidatorModel):
    containerLogs: Optional[List[LogsConfigurationPolicy]] = None
    containerMetrics: Optional[MetricsConfigurationPolicy] = None


class TrainedModelExportOutputConfigurationOutput(BaseValidatorModel):
    members: List[TrainedModelExportReceiverMember]


class TrainedModelExportOutputConfiguration(BaseValidatorModel):
    members: List[TrainedModelExportReceiverMember]


class TrainedModelExportsConfigurationPolicyOutput(BaseValidatorModel):
    maxSize: TrainedModelExportsMaxSize
    filesToExport: List[TrainedModelExportFileTypeType]


class TrainedModelExportsConfigurationPolicy(BaseValidatorModel):
    maxSize: TrainedModelExportsMaxSize
    filesToExport: List[TrainedModelExportFileTypeType]


class TrainedModelInferenceJobsConfigurationPolicyOutput(BaseValidatorModel):
    containerLogs: Optional[List[LogsConfigurationPolicyOutput]] = None
    maxOutputSize: Optional[TrainedModelInferenceMaxOutputSize] = None


class TrainedModelInferenceJobsConfigurationPolicy(BaseValidatorModel):
    containerLogs: Optional[List[LogsConfigurationPolicy]] = None
    maxOutputSize: Optional[TrainedModelInferenceMaxOutputSize] = None


class ConfiguredAudienceModelOutputConfig(BaseValidatorModel):
    destination: AudienceDestination
    roleArn: str


class MLOutputConfiguration(BaseValidatorModel):
    roleArn: str
    destination: Optional[Destination] = None


class AudienceQualityMetrics(BaseValidatorModel):
    relevanceMetrics: List[RelevanceMetric]
    recallMetric: Optional[float] = None


class ListAudienceExportJobsResponse(BaseValidatorModel):
    audienceExportJobs: List[AudienceExportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AudienceGenerationJobDataSourceOutput(BaseValidatorModel):
    roleArn: str
    dataSource: Optional[S3ConfigMap] = None
    sqlParameters: Optional[ProtectedQuerySQLParametersOutput] = None
    sqlComputeConfiguration: Optional[ComputeConfiguration] = None


class AudienceGenerationJobDataSource(BaseValidatorModel):
    roleArn: str
    dataSource: Optional[S3ConfigMap] = None
    sqlParameters: Optional[ProtectedQuerySQLParameters] = None
    sqlComputeConfiguration: Optional[ComputeConfiguration] = None


class ProtectedQueryInputParametersOutput(BaseValidatorModel):
    sqlParameters: ProtectedQuerySQLParametersOutput
    computeConfiguration: Optional[ComputeConfiguration] = None


class ProtectedQueryInputParameters(BaseValidatorModel):
    sqlParameters: ProtectedQuerySQLParameters
    computeConfiguration: Optional[ComputeConfiguration] = None


class GetConfiguredModelAlgorithmResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmArn: str
    name: str
    trainingContainerConfig: ContainerConfigOutput
    inferenceContainerConfig: InferenceContainerConfig
    roleArn: str
    description: str
    tags: Dict[str, str]
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadata

ContainerConfigUnion = Union[ContainerConfig, ContainerConfigOutput]


class DatasetInputConfigOutput(BaseValidatorModel):
    schema: List[ColumnSchemaOutput]
    dataSource: DataSource


class DatasetInputConfig(BaseValidatorModel):
    schema: List[ColumnSchemaUnion]
    dataSource: DataSource


class CollaborationTrainedModelInferenceJobSummary(BaseValidatorModel):
    trainedModelInferenceJobArn: str
    membershipIdentifier: str
    trainedModelArn: str
    collaborationIdentifier: str
    status: TrainedModelInferenceJobStatusType
    outputConfiguration: InferenceOutputConfigurationOutput
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


class GetTrainedModelInferenceJobResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainedModelInferenceJobArn: str
    configuredModelAlgorithmAssociationArn: str
    name: str
    status: TrainedModelInferenceJobStatusType
    trainedModelArn: str
    resourceConfig: InferenceResourceConfig
    outputConfiguration: InferenceOutputConfigurationOutput
    membershipIdentifier: str
    dataSource: ModelInferenceDataSource
    containerExecutionParameters: InferenceContainerExecutionParameters
    statusDetails: StatusDetails
    description: str
    inferenceContainerImageDigest: str
    environment: Dict[str, str]
    kmsKeyArn: str
    metricsStatus: MetricsStatusType
    metricsStatusDetails: str
    logsStatus: LogsStatusType
    logsStatusDetails: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class TrainedModelInferenceJobSummary(BaseValidatorModel):
    trainedModelInferenceJobArn: str
    membershipIdentifier: str
    trainedModelArn: str
    collaborationIdentifier: str
    status: TrainedModelInferenceJobStatusType
    outputConfiguration: InferenceOutputConfigurationOutput
    name: str
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: Optional[str] = None
    description: Optional[str] = None
    metricsStatus: Optional[MetricsStatusType] = None
    metricsStatusDetails: Optional[str] = None
    logsStatus: Optional[LogsStatusType] = None
    logsStatusDetails: Optional[str] = None

InferenceOutputConfigurationUnion = Union[InferenceOutputConfiguration, InferenceOutputConfigurationOutput]


class CollaborationTrainedModelExportJobSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    name: str
    outputConfiguration: TrainedModelExportOutputConfigurationOutput
    status: TrainedModelExportJobStatusType
    creatorAccountId: str
    trainedModelArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    statusDetails: Optional[StatusDetails] = None
    description: Optional[str] = None

TrainedModelExportOutputConfigurationUnion = Union[TrainedModelExportOutputConfiguration, TrainedModelExportOutputConfigurationOutput]


class PrivacyConfigurationPoliciesOutput(BaseValidatorModel):
    trainedModels: Optional[TrainedModelsConfigurationPolicyOutput] = None
    trainedModelExports: Optional[TrainedModelExportsConfigurationPolicyOutput] = None
    trainedModelInferenceJobs: Optional[TrainedModelInferenceJobsConfigurationPolicyOutput] = None


class PrivacyConfigurationPolicies(BaseValidatorModel):
    trainedModels: Optional[TrainedModelsConfigurationPolicy] = None
    trainedModelExports: Optional[TrainedModelExportsConfigurationPolicy] = None
    trainedModelInferenceJobs: Optional[TrainedModelInferenceJobsConfigurationPolicy] = None


class ConfiguredAudienceModelSummary(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfig
    configuredAudienceModelArn: str
    status: Literal['ACTIVE']
    description: Optional[str] = None


class CreateConfiguredAudienceModelRequest(BaseValidatorModel):
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfig
    sharedAudienceMetrics: List[SharedAudienceMetricsType]
    description: Optional[str] = None
    minMatchingSeedSize: Optional[int] = None
    audienceSizeConfig: Optional[AudienceSizeConfigUnion] = None
    tags: Optional[Dict[str, str]] = None
    childResourceTagOnCreatePolicy: Optional[TagOnCreatePolicyType] = None


class GetConfiguredAudienceModelResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredAudienceModelArn: str
    name: str
    audienceModelArn: str
    outputConfig: ConfiguredAudienceModelOutputConfig
    description: str
    status: Literal['ACTIVE']
    sharedAudienceMetrics: List[SharedAudienceMetricsType]
    minMatchingSeedSize: int
    audienceSizeConfig: AudienceSizeConfigOutput
    tags: Dict[str, str]
    childResourceTagOnCreatePolicy: TagOnCreatePolicyType
    ResponseMetadata: ResponseMetadata


class UpdateConfiguredAudienceModelRequest(BaseValidatorModel):
    configuredAudienceModelArn: str
    outputConfig: Optional[ConfiguredAudienceModelOutputConfig] = None
    audienceModelArn: Optional[str] = None
    sharedAudienceMetrics: Optional[List[SharedAudienceMetricsType]] = None
    minMatchingSeedSize: Optional[int] = None
    audienceSizeConfig: Optional[AudienceSizeConfigUnion] = None
    description: Optional[str] = None


class GetMLConfigurationResponse(BaseValidatorModel):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfiguration
    createTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadata


class PutMLConfigurationRequest(BaseValidatorModel):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfiguration


class GetAudienceGenerationJobResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    audienceGenerationJobArn: str
    name: str
    description: str
    status: AudienceGenerationJobStatusType
    statusDetails: StatusDetails
    configuredAudienceModelArn: str
    seedAudience: AudienceGenerationJobDataSourceOutput
    includeSeedInOutput: bool
    collaborationId: str
    metrics: AudienceQualityMetrics
    startedBy: str
    tags: Dict[str, str]
    protectedQueryIdentifier: str
    ResponseMetadata: ResponseMetadata

AudienceGenerationJobDataSourceUnion = Union[AudienceGenerationJobDataSource, AudienceGenerationJobDataSourceOutput]


class InputChannelDataSourceOutput(BaseValidatorModel):
    protectedQueryInputParameters: Optional[ProtectedQueryInputParametersOutput] = None


class InputChannelDataSource(BaseValidatorModel):
    protectedQueryInputParameters: Optional[ProtectedQueryInputParameters] = None


class CreateConfiguredModelAlgorithmRequest(BaseValidatorModel):
    name: str
    roleArn: str
    description: Optional[str] = None
    trainingContainerConfig: Optional[ContainerConfigUnion] = None
    inferenceContainerConfig: Optional[InferenceContainerConfig] = None
    tags: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None


class DatasetOutput(BaseValidatorModel):
    type: Literal['INTERACTIONS']
    inputConfig: DatasetInputConfigOutput

DatasetInputConfigUnion = Union[DatasetInputConfig, DatasetInputConfigOutput]


class ListCollaborationTrainedModelInferenceJobsResponse(BaseValidatorModel):
    collaborationTrainedModelInferenceJobs: List[CollaborationTrainedModelInferenceJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTrainedModelInferenceJobsResponse(BaseValidatorModel):
    trainedModelInferenceJobs: List[TrainedModelInferenceJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartTrainedModelInferenceJobRequest(BaseValidatorModel):
    membershipIdentifier: str
    name: str
    trainedModelArn: str
    resourceConfig: InferenceResourceConfig
    outputConfiguration: InferenceOutputConfigurationUnion
    dataSource: ModelInferenceDataSource
    configuredModelAlgorithmAssociationArn: Optional[str] = None
    description: Optional[str] = None
    containerExecutionParameters: Optional[InferenceContainerExecutionParameters] = None
    environment: Optional[Dict[str, str]] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListCollaborationTrainedModelExportJobsResponse(BaseValidatorModel):
    collaborationTrainedModelExportJobs: List[CollaborationTrainedModelExportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartTrainedModelExportJobRequest(BaseValidatorModel):
    name: str
    trainedModelArn: str
    membershipIdentifier: str
    outputConfiguration: TrainedModelExportOutputConfigurationUnion
    description: Optional[str] = None


class PrivacyConfigurationOutput(BaseValidatorModel):
    policies: PrivacyConfigurationPoliciesOutput


class PrivacyConfiguration(BaseValidatorModel):
    policies: PrivacyConfigurationPolicies


class ListConfiguredAudienceModelsResponse(BaseValidatorModel):
    configuredAudienceModels: List[ConfiguredAudienceModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartAudienceGenerationJobRequest(BaseValidatorModel):
    name: str
    configuredAudienceModelArn: str
    seedAudience: AudienceGenerationJobDataSourceUnion
    includeSeedInOutput: Optional[bool] = None
    collaborationId: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class InputChannelOutput(BaseValidatorModel):
    dataSource: InputChannelDataSourceOutput
    roleArn: str


class InputChannel(BaseValidatorModel):
    dataSource: InputChannelDataSource
    roleArn: str


class GetTrainingDatasetResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    trainingDatasetArn: str
    name: str
    trainingData: List[DatasetOutput]
    status: Literal['ACTIVE']
    roleArn: str
    tags: Dict[str, str]
    description: str
    ResponseMetadata: ResponseMetadata


class Dataset(BaseValidatorModel):
    type: Literal['INTERACTIONS']
    inputConfig: DatasetInputConfigUnion


class GetCollaborationConfiguredModelAlgorithmAssociationResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    description: str
    creatorAccountId: str
    privacyConfiguration: PrivacyConfigurationOutput
    ResponseMetadata: ResponseMetadata


class GetConfiguredModelAlgorithmAssociationResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str
    collaborationIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    privacyConfiguration: PrivacyConfigurationOutput
    description: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

PrivacyConfigurationUnion = Union[PrivacyConfiguration, PrivacyConfigurationOutput]


class GetMLInputChannelResponse(BaseValidatorModel):
    createTime: datetime
    updateTime: datetime
    membershipIdentifier: str
    collaborationIdentifier: str
    inputChannel: InputChannelOutput
    protectedQueryIdentifier: str
    mlInputChannelArn: str
    name: str
    configuredModelAlgorithmAssociations: List[str]
    status: MLInputChannelStatusType
    statusDetails: StatusDetails
    retentionInDays: int
    numberOfRecords: int
    numberOfFiles: float
    sizeInGb: float
    description: str
    kmsKeyArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

InputChannelUnion = Union[InputChannel, InputChannelOutput]

DatasetUnion = Union[Dataset, DatasetOutput]


class CreateConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    membershipIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    description: Optional[str] = None
    privacyConfiguration: Optional[PrivacyConfigurationUnion] = None
    tags: Optional[Dict[str, str]] = None


class CreateMLInputChannelRequest(BaseValidatorModel):
    membershipIdentifier: str
    configuredModelAlgorithmAssociations: List[str]
    inputChannel: InputChannelUnion
    name: str
    retentionInDays: int
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateTrainingDatasetRequest(BaseValidatorModel):
    name: str
    roleArn: str
    trainingData: List[DatasetUnion]
    tags: Optional[Dict[str, str]] = None
    description: Optional[str] = None