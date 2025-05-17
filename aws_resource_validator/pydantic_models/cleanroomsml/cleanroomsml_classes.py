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


# This class is the input for the 'cancel_trained_model_inference_job' function.
class CancelTrainedModelInferenceJobRequest(BaseValidatorModel):
    membershipIdentifier: str
    trainedModelInferenceJobArn: str


# This class is the input for the 'cancel_trained_model' function.
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


# This class is the input for the 'delete_audience_generation_job' function.
class DeleteAudienceGenerationJobRequest(BaseValidatorModel):
    audienceGenerationJobArn: str


# This class is the input for the 'delete_audience_model' function.
class DeleteAudienceModelRequest(BaseValidatorModel):
    audienceModelArn: str


# This class is the input for the 'delete_configured_audience_model_policy' function.
class DeleteConfiguredAudienceModelPolicyRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


# This class is the input for the 'delete_configured_audience_model' function.
class DeleteConfiguredAudienceModelRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


# This class is the input for the 'delete_configured_model_algorithm_association' function.
class DeleteConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str


# This class is the input for the 'delete_configured_model_algorithm' function.
class DeleteConfiguredModelAlgorithmRequest(BaseValidatorModel):
    configuredModelAlgorithmArn: str


# This class is the input for the 'delete_ml_configuration' function.
class DeleteMLConfigurationRequest(BaseValidatorModel):
    membershipIdentifier: str


# This class is the input for the 'delete_ml_input_channel_data' function.
class DeleteMLInputChannelDataRequest(BaseValidatorModel):
    mlInputChannelArn: str
    membershipIdentifier: str


# This class is the input for the 'delete_trained_model_output' function.
class DeleteTrainedModelOutputRequest(BaseValidatorModel):
    trainedModelArn: str
    membershipIdentifier: str


# This class is the input for the 'delete_training_dataset' function.
class DeleteTrainingDatasetRequest(BaseValidatorModel):
    trainingDatasetArn: str


# This class is the input for the 'get_audience_generation_job' function.
class GetAudienceGenerationJobRequest(BaseValidatorModel):
    audienceGenerationJobArn: str


# This class is the input for the 'get_audience_model' function.
class GetAudienceModelRequest(BaseValidatorModel):
    audienceModelArn: str


# This class is the input for the 'get_collaboration_configured_model_algorithm_association' function.
class GetCollaborationConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    collaborationIdentifier: str


# This class is the input for the 'get_collaboration_ml_input_channel' function.
class GetCollaborationMLInputChannelRequest(BaseValidatorModel):
    mlInputChannelArn: str
    collaborationIdentifier: str


# This class is the input for the 'get_collaboration_trained_model' function.
class GetCollaborationTrainedModelRequest(BaseValidatorModel):
    trainedModelArn: str
    collaborationIdentifier: str


# This class is the input for the 'get_configured_audience_model_policy' function.
class GetConfiguredAudienceModelPolicyRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


# This class is the input for the 'get_configured_audience_model' function.
class GetConfiguredAudienceModelRequest(BaseValidatorModel):
    configuredAudienceModelArn: str


# This class is the input for the 'get_configured_model_algorithm_association' function.
class GetConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    membershipIdentifier: str


# This class is the input for the 'get_configured_model_algorithm' function.
class GetConfiguredModelAlgorithmRequest(BaseValidatorModel):
    configuredModelAlgorithmArn: str


# This class is the input for the 'get_ml_configuration' function.
class GetMLConfigurationRequest(BaseValidatorModel):
    membershipIdentifier: str


# This class is the input for the 'get_ml_input_channel' function.
class GetMLInputChannelRequest(BaseValidatorModel):
    mlInputChannelArn: str
    membershipIdentifier: str


# This class is the input for the 'get_trained_model_inference_job' function.
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


# This class is the input for the 'get_trained_model' function.
class GetTrainedModelRequest(BaseValidatorModel):
    trainedModelArn: str
    membershipIdentifier: str


# This class is the input for the 'get_training_dataset' function.
class GetTrainingDatasetRequest(BaseValidatorModel):
    trainingDatasetArn: str


class InferenceReceiverMember(BaseValidatorModel):
    accountId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_audience_export_jobs' function.
class ListAudienceExportJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    audienceGenerationJobArn: Optional[str] = None


# This class is the input for the 'list_audience_generation_jobs' function.
class ListAudienceGenerationJobsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    configuredAudienceModelArn: Optional[str] = None
    collaborationId: Optional[str] = None


# This class is the input for the 'list_audience_models' function.
class ListAudienceModelsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_configured_model_algorithm_associations' function.
class ListCollaborationConfiguredModelAlgorithmAssociationsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_ml_input_channels' function.
class ListCollaborationMLInputChannelsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_trained_model_export_jobs' function.
class ListCollaborationTrainedModelExportJobsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    trainedModelArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_collaboration_trained_model_inference_jobs' function.
class ListCollaborationTrainedModelInferenceJobsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    trainedModelArn: Optional[str] = None


# This class is the input for the 'list_collaboration_trained_models' function.
class ListCollaborationTrainedModelsRequest(BaseValidatorModel):
    collaborationIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_configured_audience_models' function.
class ListConfiguredAudienceModelsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_configured_model_algorithm_associations' function.
class ListConfiguredModelAlgorithmAssociationsRequest(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_configured_model_algorithms' function.
class ListConfiguredModelAlgorithmsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_ml_input_channels' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_trained_model_inference_jobs' function.
class ListTrainedModelInferenceJobsRequest(BaseValidatorModel):
    membershipIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    trainedModelArn: Optional[str] = None


# This class is the input for the 'list_trained_models' function.
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


# This class is the input for the 'list_training_datasets' function.
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


# This class is the input for the 'put_configured_audience_model_policy' function.
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


# This class is the input for the 'start_audience_export_job' function.
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


# This class is the input for the 'create_audience_model' function.
class CreateAudienceModelRequest(BaseValidatorModel):
    name: str
    trainingDatasetArn: str
    trainingDataStartTime: Optional[Timestamp] = None
    trainingDataEndTime: Optional[Timestamp] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    description: Optional[str] = None


# This class is the output for the 'create_audience_model' function.
class CreateAudienceModelResponse(BaseValidatorModel):
    audienceModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_configured_audience_model' function.
class CreateConfiguredAudienceModelResponse(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_configured_model_algorithm_association' function.
class CreateConfiguredModelAlgorithmAssociationResponse(BaseValidatorModel):
    configuredModelAlgorithmAssociationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_configured_model_algorithm' function.
class CreateConfiguredModelAlgorithmResponse(BaseValidatorModel):
    configuredModelAlgorithmArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ml_input_channel' function.
class CreateMLInputChannelResponse(BaseValidatorModel):
    mlInputChannelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_trained_model' function.
class CreateTrainedModelResponse(BaseValidatorModel):
    trainedModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_training_dataset' function.
class CreateTrainingDatasetResponse(BaseValidatorModel):
    trainingDatasetArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_trained_model_export_job' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_audience_model' function.
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


# This class is the output for the 'get_collaboration_ml_input_channel' function.
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


# This class is the output for the 'get_configured_audience_model_policy' function.
class GetConfiguredAudienceModelPolicyResponse(BaseValidatorModel):
    configuredAudienceModelArn: str
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_audience_generation_jobs' function.
class ListAudienceGenerationJobsResponse(BaseValidatorModel):
    audienceGenerationJobs: List[AudienceGenerationJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_audience_models' function.
class ListAudienceModelsResponse(BaseValidatorModel):
    audienceModels: List[AudienceModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_collaboration_configured_model_algorithm_associations' function.
class ListCollaborationConfiguredModelAlgorithmAssociationsResponse(BaseValidatorModel):
    collaborationConfiguredModelAlgorithmAssociations: List[CollaborationConfiguredModelAlgorithmAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_collaboration_ml_input_channels' function.
class ListCollaborationMLInputChannelsResponse(BaseValidatorModel):
    collaborationMLInputChannelsList: List[CollaborationMLInputChannelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_collaboration_trained_models' function.
class ListCollaborationTrainedModelsResponse(BaseValidatorModel):
    collaborationTrainedModels: List[CollaborationTrainedModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_configured_model_algorithm_associations' function.
class ListConfiguredModelAlgorithmAssociationsResponse(BaseValidatorModel):
    configuredModelAlgorithmAssociations: List[ConfiguredModelAlgorithmAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_configured_model_algorithms' function.
class ListConfiguredModelAlgorithmsResponse(BaseValidatorModel):
    configuredModelAlgorithms: List[ConfiguredModelAlgorithmSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_configured_audience_model_policy' function.
class PutConfiguredAudienceModelPolicyResponse(BaseValidatorModel):
    configuredAudienceModelPolicy: str
    policyHash: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_audience_generation_job' function.
class StartAudienceGenerationJobResponse(BaseValidatorModel):
    audienceGenerationJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_trained_model_inference_job' function.
class StartTrainedModelInferenceJobResponse(BaseValidatorModel):
    trainedModelInferenceJobArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_configured_audience_model' function.
class UpdateConfiguredAudienceModelResponse(BaseValidatorModel):
    configuredAudienceModelArn: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_trained_model' function.
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


# This class is the output for the 'get_collaboration_trained_model' function.
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


# This class is the output for the 'get_trained_model' function.
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


# This class is the output for the 'list_ml_input_channels' function.
class ListMLInputChannelsResponse(BaseValidatorModel):
    mlInputChannelsList: List[MLInputChannelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_trained_models' function.
class ListTrainedModelsResponse(BaseValidatorModel):
    trainedModels: List[TrainedModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_training_datasets' function.
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


# This class is the output for the 'list_audience_export_jobs' function.
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


# This class is the output for the 'get_configured_model_algorithm' function.
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


# This class is the output for the 'get_trained_model_inference_job' function.
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


# This class is the input for the 'create_configured_audience_model' function.
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


# This class is the output for the 'get_configured_audience_model' function.
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


# This class is the input for the 'update_configured_audience_model' function.
class UpdateConfiguredAudienceModelRequest(BaseValidatorModel):
    configuredAudienceModelArn: str
    outputConfig: Optional[ConfiguredAudienceModelOutputConfig] = None
    audienceModelArn: Optional[str] = None
    sharedAudienceMetrics: Optional[List[SharedAudienceMetricsType]] = None
    minMatchingSeedSize: Optional[int] = None
    audienceSizeConfig: Optional[AudienceSizeConfigUnion] = None
    description: Optional[str] = None


# This class is the output for the 'get_ml_configuration' function.
class GetMLConfigurationResponse(BaseValidatorModel):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfiguration
    createTime: datetime
    updateTime: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_ml_configuration' function.
class PutMLConfigurationRequest(BaseValidatorModel):
    membershipIdentifier: str
    defaultOutputLocation: MLOutputConfiguration


# This class is the output for the 'get_audience_generation_job' function.
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


# This class is the input for the 'create_configured_model_algorithm' function.
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


# This class is the output for the 'list_collaboration_trained_model_inference_jobs' function.
class ListCollaborationTrainedModelInferenceJobsResponse(BaseValidatorModel):
    collaborationTrainedModelInferenceJobs: List[CollaborationTrainedModelInferenceJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_trained_model_inference_jobs' function.
class ListTrainedModelInferenceJobsResponse(BaseValidatorModel):
    trainedModelInferenceJobs: List[TrainedModelInferenceJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'start_trained_model_inference_job' function.
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


# This class is the output for the 'list_collaboration_trained_model_export_jobs' function.
class ListCollaborationTrainedModelExportJobsResponse(BaseValidatorModel):
    collaborationTrainedModelExportJobs: List[CollaborationTrainedModelExportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'start_trained_model_export_job' function.
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


# This class is the output for the 'list_configured_audience_models' function.
class ListConfiguredAudienceModelsResponse(BaseValidatorModel):
    configuredAudienceModels: List[ConfiguredAudienceModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'start_audience_generation_job' function.
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


# This class is the output for the 'get_training_dataset' function.
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


# This class is the output for the 'get_collaboration_configured_model_algorithm_association' function.
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


# This class is the output for the 'get_configured_model_algorithm_association' function.
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


# This class is the output for the 'get_ml_input_channel' function.
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


# This class is the input for the 'create_configured_model_algorithm_association' function.
class CreateConfiguredModelAlgorithmAssociationRequest(BaseValidatorModel):
    membershipIdentifier: str
    configuredModelAlgorithmArn: str
    name: str
    description: Optional[str] = None
    privacyConfiguration: Optional[PrivacyConfigurationUnion] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_ml_input_channel' function.
class CreateMLInputChannelRequest(BaseValidatorModel):
    membershipIdentifier: str
    configuredModelAlgorithmAssociations: List[str]
    inputChannel: InputChannelUnion
    name: str
    retentionInDays: int
    description: Optional[str] = None
    kmsKeyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_training_dataset' function.
class CreateTrainingDatasetRequest(BaseValidatorModel):
    name: str
    roleArn: str
    trainingData: List[DatasetUnion]
    tags: Optional[Dict[str, str]] = None
    description: Optional[str] = None