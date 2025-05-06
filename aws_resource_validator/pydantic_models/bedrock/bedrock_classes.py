from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bedrock.bedrock_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class BatchDeleteEvaluationJobError(BaseValidatorModel):
    jobIdentifier: str
    code: str
    message: Optional[str] = None


class BatchDeleteEvaluationJobItem(BaseValidatorModel):
    jobIdentifier: str
    jobStatus: EvaluationJobStatusType


class BatchDeleteEvaluationJobRequest(BaseValidatorModel):
    jobIdentifiers: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BedrockEvaluatorModel(BaseValidatorModel):
    modelIdentifier: str

Blob = Union[str, bytes, IO[Any], StreamingBody]


class ByteContentDocOutput(BaseValidatorModel):
    identifier: str
    contentType: str
    data: bytes


class S3Config(BaseValidatorModel):
    bucketName: str
    keyPrefix: Optional[str] = None


class EvaluationOutputDataConfig(BaseValidatorModel):
    s3Uri: str


class Tag(BaseValidatorModel):
    key: str
    value: str


class CreateGuardrailVersionRequest(BaseValidatorModel):
    guardrailIdentifier: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None


class InferenceProfileModelSource(BaseValidatorModel):
    copyFrom: Optional[str] = None


class OutputDataConfig(BaseValidatorModel):
    s3Uri: str


class PromptRouterTargetModel(BaseValidatorModel):
    modelArn: str


class RoutingCriteria(BaseValidatorModel):
    responseQualityDifference: float


class CustomModelSummary(BaseValidatorModel):
    modelArn: str
    modelName: str
    creationTime: datetime
    baseModelArn: str
    baseModelName: str
    customizationType: Optional[CustomizationTypeType] = None
    ownerAccountId: Optional[str] = None


class DeleteCustomModelRequest(BaseValidatorModel):
    modelIdentifier: str


class DeleteGuardrailRequest(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None


class DeleteImportedModelRequest(BaseValidatorModel):
    modelIdentifier: str


class DeleteInferenceProfileRequest(BaseValidatorModel):
    inferenceProfileIdentifier: str


class DeleteMarketplaceModelEndpointRequest(BaseValidatorModel):
    endpointArn: str


class DeletePromptRouterRequest(BaseValidatorModel):
    promptRouterArn: str


class DeleteProvisionedModelThroughputRequest(BaseValidatorModel):
    provisionedModelId: str


class DeregisterMarketplaceModelEndpointRequest(BaseValidatorModel):
    endpointArn: str


class TeacherModelConfig(BaseValidatorModel):
    teacherModelIdentifier: str
    maxResponseLengthForInference: Optional[int] = None


class PerformanceConfiguration(BaseValidatorModel):
    latency: Optional[PerformanceConfigLatencyType] = None


class EvaluationDatasetLocation(BaseValidatorModel):
    s3Uri: Optional[str] = None


class EvaluationSummary(BaseValidatorModel):
    jobArn: str
    jobName: str
    status: EvaluationJobStatusType
    creationTime: datetime
    jobType: EvaluationJobTypeType
    evaluationTaskTypes: List[EvaluationTaskTypeType]
    modelIdentifiers: Optional[List[str]] = None
    ragIdentifiers: Optional[List[str]] = None
    evaluatorModelIdentifiers: Optional[List[str]] = None
    applicationType: Optional[ApplicationTypeType] = None


class S3ObjectDoc(BaseValidatorModel):
    uri: str


class GuardrailConfiguration(BaseValidatorModel):
    guardrailId: str
    guardrailVersion: str


class PromptTemplate(BaseValidatorModel):
    textPromptTemplate: Optional[str] = None


class FilterAttributeOutput(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class FilterAttribute(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class FoundationModelLifecycle(BaseValidatorModel):
    status: FoundationModelLifecycleStatusType


class GetCustomModelRequest(BaseValidatorModel):
    modelIdentifier: str


class TrainingMetrics(BaseValidatorModel):
    trainingLoss: Optional[float] = None


class ValidatorMetric(BaseValidatorModel):
    validationLoss: Optional[float] = None


class GetEvaluationJobRequest(BaseValidatorModel):
    jobIdentifier: str


class GetFoundationModelRequest(BaseValidatorModel):
    modelIdentifier: str


class GetGuardrailRequest(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None


class GetImportedModelRequest(BaseValidatorModel):
    modelIdentifier: str


class GetInferenceProfileRequest(BaseValidatorModel):
    inferenceProfileIdentifier: str


class InferenceProfileModel(BaseValidatorModel):
    modelArn: Optional[str] = None


class GetMarketplaceModelEndpointRequest(BaseValidatorModel):
    endpointArn: str


class GetModelCopyJobRequest(BaseValidatorModel):
    jobArn: str


class GetModelCustomizationJobRequest(BaseValidatorModel):
    jobIdentifier: str


class VpcConfigOutput(BaseValidatorModel):
    subnetIds: List[str]
    securityGroupIds: List[str]


class GetModelImportJobRequest(BaseValidatorModel):
    jobIdentifier: str


class GetModelInvocationJobRequest(BaseValidatorModel):
    jobIdentifier: str


class GetPromptRouterRequest(BaseValidatorModel):
    promptRouterArn: str


class GetProvisionedModelThroughputRequest(BaseValidatorModel):
    provisionedModelId: str


class GuardrailContentFilterConfig(BaseValidatorModel):
    type: GuardrailContentFilterTypeType
    inputStrength: GuardrailFilterStrengthType
    outputStrength: GuardrailFilterStrengthType
    inputModalities: Optional[List[GuardrailModalityType]] = None
    outputModalities: Optional[List[GuardrailModalityType]] = None


class GuardrailContentFilter(BaseValidatorModel):
    type: GuardrailContentFilterTypeType
    inputStrength: GuardrailFilterStrengthType
    outputStrength: GuardrailFilterStrengthType
    inputModalities: Optional[List[GuardrailModalityType]] = None
    outputModalities: Optional[List[GuardrailModalityType]] = None


class GuardrailContextualGroundingFilterConfig(BaseValidatorModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float


class GuardrailContextualGroundingFilter(BaseValidatorModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float


class GuardrailManagedWordsConfig(BaseValidatorModel):
    type: Literal['PROFANITY']


class GuardrailManagedWords(BaseValidatorModel):
    type: Literal['PROFANITY']


class GuardrailPiiEntityConfig(BaseValidatorModel):
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationActionType


class GuardrailPiiEntity(BaseValidatorModel):
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationActionType


class GuardrailRegexConfig(BaseValidatorModel):
    name: str
    pattern: str
    action: GuardrailSensitiveInformationActionType
    description: Optional[str] = None


class GuardrailRegex(BaseValidatorModel):
    name: str
    pattern: str
    action: GuardrailSensitiveInformationActionType
    description: Optional[str] = None


class GuardrailSummary(BaseValidatorModel):
    id: str
    arn: str
    status: GuardrailStatusType
    name: str
    version: str
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None


class GuardrailTopicConfig(BaseValidatorModel):
    name: str
    definition: str
    type: Literal['DENY']
    examples: Optional[List[str]] = None


class GuardrailTopic(BaseValidatorModel):
    name: str
    definition: str
    examples: Optional[List[str]] = None
    type: Optional[Literal['DENY']] = None


class GuardrailWordConfig(BaseValidatorModel):
    text: str


class GuardrailWord(BaseValidatorModel):
    text: str


class HumanEvaluationCustomMetric(BaseValidatorModel):
    name: str
    ratingMethod: str
    description: Optional[str] = None


class HumanWorkflowConfig(BaseValidatorModel):
    flowDefinitionArn: str
    instructions: Optional[str] = None


class ImportedModelSummary(BaseValidatorModel):
    modelArn: str
    modelName: str
    creationTime: datetime
    instructSupported: Optional[bool] = None
    modelArchitecture: Optional[str] = None


class InvocationLogSource(BaseValidatorModel):
    s3Uri: Optional[str] = None


class TextInferenceConfigOutput(BaseValidatorModel):
    temperature: Optional[float] = None
    topP: Optional[float] = None
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None


class TextInferenceConfig(BaseValidatorModel):
    temperature: Optional[float] = None
    topP: Optional[float] = None
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

Timestamp = Union[datetime, str]


class ListFoundationModelsRequest(BaseValidatorModel):
    byProvider: Optional[str] = None
    byCustomizationType: Optional[ModelCustomizationType] = None
    byOutputModality: Optional[ModelModalityType] = None
    byInferenceType: Optional[InferenceTypeType] = None


class ListGuardrailsRequest(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInferenceProfilesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    typeEquals: Optional[InferenceProfileTypeType] = None


class ListMarketplaceModelEndpointsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    modelSourceEquals: Optional[str] = None


class MarketplaceModelEndpointSummary(BaseValidatorModel):
    endpointArn: str
    modelSourceIdentifier: str
    createdAt: datetime
    updatedAt: datetime
    status: Optional[StatusType] = None
    statusMessage: Optional[str] = None


class ModelCustomizationJobSummary(BaseValidatorModel):
    jobArn: str
    baseModelArn: str
    jobName: str
    status: ModelCustomizationJobStatusType
    creationTime: datetime
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    customModelArn: Optional[str] = None
    customModelName: Optional[str] = None
    customizationType: Optional[CustomizationTypeType] = None


class ModelImportJobSummary(BaseValidatorModel):
    jobArn: str
    jobName: str
    status: ModelImportJobStatusType
    creationTime: datetime
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    importedModelArn: Optional[str] = None
    importedModelName: Optional[str] = None


class ListPromptRoutersRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    type: Optional[PromptRouterTypeType] = None


class ProvisionedModelSummary(BaseValidatorModel):
    provisionedModelName: str
    provisionedModelArn: str
    modelArn: str
    desiredModelArn: str
    foundationModelArn: str
    modelUnits: int
    desiredModelUnits: int
    status: ProvisionedModelStatusType
    creationTime: datetime
    lastModifiedTime: datetime
    commitmentDuration: Optional[CommitmentDurationType] = None
    commitmentExpirationTime: Optional[datetime] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str


class S3DataSource(BaseValidatorModel):
    s3Uri: str


class ModelInvocationJobS3InputDataConfig(BaseValidatorModel):
    s3Uri: str
    s3InputFormat: Optional[Literal['JSONL']] = None
    s3BucketOwner: Optional[str] = None


class ModelInvocationJobS3OutputDataConfig(BaseValidatorModel):
    s3Uri: str
    s3EncryptionKeyId: Optional[str] = None
    s3BucketOwner: Optional[str] = None


class QueryTransformationConfiguration(BaseValidatorModel):
    type: Literal['QUERY_DECOMPOSITION']


class RegisterMarketplaceModelEndpointRequest(BaseValidatorModel):
    endpointIdentifier: str
    modelSourceIdentifier: str


class RequestMetadataBaseFiltersOutput(BaseValidatorModel):
    equals: Optional[Dict[str, str]] = None
    notEquals: Optional[Dict[str, str]] = None


class RequestMetadataBaseFilters(BaseValidatorModel):
    equals: Optional[Dict[str, str]] = None
    notEquals: Optional[Dict[str, str]] = None


class VpcConfig(BaseValidatorModel):
    subnetIds: List[str]
    securityGroupIds: List[str]


class StopEvaluationJobRequest(BaseValidatorModel):
    jobIdentifier: str


class StopModelCustomizationJobRequest(BaseValidatorModel):
    jobIdentifier: str


class StopModelInvocationJobRequest(BaseValidatorModel):
    jobIdentifier: str


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: List[str]


class UpdateProvisionedModelThroughputRequest(BaseValidatorModel):
    provisionedModelId: str
    desiredProvisionedModelName: Optional[str] = None
    desiredModelId: Optional[str] = None


class Validator(BaseValidatorModel):
    s3Uri: str


class BatchDeleteEvaluationJobResponse(BaseValidatorModel):
    errors: List[BatchDeleteEvaluationJobError]
    evaluationJobs: List[BatchDeleteEvaluationJobItem]
    ResponseMetadata: ResponseMetadata


class CreateEvaluationJobResponse(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadata


class CreateGuardrailResponse(BaseValidatorModel):
    guardrailId: str
    guardrailArn: str
    version: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadata


class CreateGuardrailVersionResponse(BaseValidatorModel):
    guardrailId: str
    version: str
    ResponseMetadata: ResponseMetadata


class CreateInferenceProfileResponse(BaseValidatorModel):
    inferenceProfileArn: str
    status: Literal['ACTIVE']
    ResponseMetadata: ResponseMetadata


class CreateModelCopyJobResponse(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelCustomizationJobResponse(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelImportJobResponse(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadata


class CreateModelInvocationJobResponse(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadata


class CreatePromptRouterResponse(BaseValidatorModel):
    promptRouterArn: str
    ResponseMetadata: ResponseMetadata


class CreateProvisionedModelThroughputResponse(BaseValidatorModel):
    provisionedModelArn: str
    ResponseMetadata: ResponseMetadata


class GetProvisionedModelThroughputResponse(BaseValidatorModel):
    modelUnits: int
    desiredModelUnits: int
    provisionedModelName: str
    provisionedModelArn: str
    modelArn: str
    desiredModelArn: str
    foundationModelArn: str
    status: ProvisionedModelStatusType
    creationTime: datetime
    lastModifiedTime: datetime
    failureMessage: str
    commitmentDuration: CommitmentDurationType
    commitmentExpirationTime: datetime
    ResponseMetadata: ResponseMetadata


class UpdateGuardrailResponse(BaseValidatorModel):
    guardrailId: str
    guardrailArn: str
    version: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class EvaluatorModelConfigOutput(BaseValidatorModel):
    bedrockEvaluatorModels: Optional[List[BedrockEvaluatorModel]] = None


class EvaluatorModelConfig(BaseValidatorModel):
    bedrockEvaluatorModels: Optional[List[BedrockEvaluatorModel]] = None


class ByteContentDoc(BaseValidatorModel):
    identifier: str
    contentType: str
    data: Blob


class CloudWatchConfig(BaseValidatorModel):
    logGroupName: str
    roleArn: str
    largeDataDeliveryS3Config: Optional[S3Config] = None


class CreateModelCopyJobRequest(BaseValidatorModel):
    sourceModelArn: str
    targetModelName: str
    modelKmsKeyId: Optional[str] = None
    targetModelTags: Optional[List[Tag]] = None
    clientRequestToken: Optional[str] = None


class CreateProvisionedModelThroughputRequest(BaseValidatorModel):
    modelUnits: int
    provisionedModelName: str
    modelId: str
    clientRequestToken: Optional[str] = None
    commitmentDuration: Optional[CommitmentDurationType] = None
    tags: Optional[List[Tag]] = None


class GetModelCopyJobResponse(BaseValidatorModel):
    jobArn: str
    status: ModelCopyJobStatusType
    creationTime: datetime
    targetModelArn: str
    targetModelName: str
    sourceAccountId: str
    sourceModelArn: str
    targetModelKmsKeyArn: str
    targetModelTags: List[Tag]
    failureMessage: str
    sourceModelName: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class ModelCopyJobSummary(BaseValidatorModel):
    jobArn: str
    status: ModelCopyJobStatusType
    creationTime: datetime
    targetModelArn: str
    sourceAccountId: str
    sourceModelArn: str
    targetModelName: Optional[str] = None
    targetModelKmsKeyArn: Optional[str] = None
    targetModelTags: Optional[List[Tag]] = None
    failureMessage: Optional[str] = None
    sourceModelName: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: List[Tag]


class CreateInferenceProfileRequest(BaseValidatorModel):
    inferenceProfileName: str
    modelSource: InferenceProfileModelSource
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreatePromptRouterRequest(BaseValidatorModel):
    promptRouterName: str
    models: List[PromptRouterTargetModel]
    routingCriteria: RoutingCriteria
    fallbackModel: PromptRouterTargetModel
    clientRequestToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class GetPromptRouterResponse(BaseValidatorModel):
    promptRouterName: str
    routingCriteria: RoutingCriteria
    description: str
    createdAt: datetime
    updatedAt: datetime
    promptRouterArn: str
    models: List[PromptRouterTargetModel]
    fallbackModel: PromptRouterTargetModel
    status: Literal['AVAILABLE']
    type: PromptRouterTypeType
    ResponseMetadata: ResponseMetadata


class PromptRouterSummary(BaseValidatorModel):
    promptRouterName: str
    routingCriteria: RoutingCriteria
    promptRouterArn: str
    models: List[PromptRouterTargetModel]
    fallbackModel: PromptRouterTargetModel
    status: Literal['AVAILABLE']
    type: PromptRouterTypeType
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class ListCustomModelsResponse(BaseValidatorModel):
    modelSummaries: List[CustomModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DistillationConfig(BaseValidatorModel):
    teacherModelConfig: TeacherModelConfig


class EvaluationBedrockModel(BaseValidatorModel):
    modelIdentifier: str
    inferenceParams: Optional[str] = None
    performanceConfig: Optional[PerformanceConfiguration] = None


class EvaluationDataset(BaseValidatorModel):
    name: str
    datasetLocation: Optional[EvaluationDatasetLocation] = None


class ListEvaluationJobsResponse(BaseValidatorModel):
    jobSummaries: List[EvaluationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExternalSourceOutput(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    s3Location: Optional[S3ObjectDoc] = None
    byteContent: Optional[ByteContentDocOutput] = None


class RetrievalFilterOutput(BaseValidatorModel):
    equals: Optional[FilterAttributeOutput] = None
    notEquals: Optional[FilterAttributeOutput] = None
    greaterThan: Optional[FilterAttributeOutput] = None
    greaterThanOrEquals: Optional[FilterAttributeOutput] = None
    lessThan: Optional[FilterAttributeOutput] = None
    lessThanOrEquals: Optional[FilterAttributeOutput] = None
    in_: Optional[FilterAttributeOutput] = None
    notIn: Optional[FilterAttributeOutput] = None
    startsWith: Optional[FilterAttributeOutput] = None
    listContains: Optional[FilterAttributeOutput] = None
    stringContains: Optional[FilterAttributeOutput] = None
    andAll: Optional[List[Dict[str, Any]]] = None
    orAll: Optional[List[Dict[str, Any]]] = None


class RetrievalFilter(BaseValidatorModel):
    equals: Optional[FilterAttribute] = None
    notEquals: Optional[FilterAttribute] = None
    greaterThan: Optional[FilterAttribute] = None
    greaterThanOrEquals: Optional[FilterAttribute] = None
    lessThan: Optional[FilterAttribute] = None
    lessThanOrEquals: Optional[FilterAttribute] = None
    in_: Optional[FilterAttribute] = None
    notIn: Optional[FilterAttribute] = None
    startsWith: Optional[FilterAttribute] = None
    listContains: Optional[FilterAttribute] = None
    stringContains: Optional[FilterAttribute] = None
    andAll: Optional[List[Dict[str, Any]]] = None
    orAll: Optional[List[Dict[str, Any]]] = None


class FoundationModelDetails(BaseValidatorModel):
    modelArn: str
    modelId: str
    modelName: Optional[str] = None
    providerName: Optional[str] = None
    inputModalities: Optional[List[ModelModalityType]] = None
    outputModalities: Optional[List[ModelModalityType]] = None
    responseStreamingSupported: Optional[bool] = None
    customizationsSupported: Optional[List[ModelCustomizationType]] = None
    inferenceTypesSupported: Optional[List[InferenceTypeType]] = None
    modelLifecycle: Optional[FoundationModelLifecycle] = None


class FoundationModelSummary(BaseValidatorModel):
    modelArn: str
    modelId: str
    modelName: Optional[str] = None
    providerName: Optional[str] = None
    inputModalities: Optional[List[ModelModalityType]] = None
    outputModalities: Optional[List[ModelModalityType]] = None
    responseStreamingSupported: Optional[bool] = None
    customizationsSupported: Optional[List[ModelCustomizationType]] = None
    inferenceTypesSupported: Optional[List[InferenceTypeType]] = None
    modelLifecycle: Optional[FoundationModelLifecycle] = None


class GetInferenceProfileResponse(BaseValidatorModel):
    inferenceProfileName: str
    description: str
    createdAt: datetime
    updatedAt: datetime
    inferenceProfileArn: str
    models: List[InferenceProfileModel]
    inferenceProfileId: str
    status: Literal['ACTIVE']
    type: InferenceProfileTypeType
    ResponseMetadata: ResponseMetadata


class InferenceProfileSummary(BaseValidatorModel):
    inferenceProfileName: str
    inferenceProfileArn: str
    models: List[InferenceProfileModel]
    inferenceProfileId: str
    status: Literal['ACTIVE']
    type: InferenceProfileTypeType
    description: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class SageMakerEndpointOutput(BaseValidatorModel):
    initialInstanceCount: int
    instanceType: str
    executionRole: str
    kmsEncryptionKey: Optional[str] = None
    vpc: Optional[VpcConfigOutput] = None


class GuardrailContentPolicyConfig(BaseValidatorModel):
    filtersConfig: List[GuardrailContentFilterConfig]


class GuardrailContentPolicy(BaseValidatorModel):
    filters: Optional[List[GuardrailContentFilter]] = None


class GuardrailContextualGroundingPolicyConfig(BaseValidatorModel):
    filtersConfig: List[GuardrailContextualGroundingFilterConfig]


class GuardrailContextualGroundingPolicy(BaseValidatorModel):
    filters: List[GuardrailContextualGroundingFilter]


class GuardrailSensitiveInformationPolicyConfig(BaseValidatorModel):
    piiEntitiesConfig: Optional[List[GuardrailPiiEntityConfig]] = None
    regexesConfig: Optional[List[GuardrailRegexConfig]] = None


class GuardrailSensitiveInformationPolicy(BaseValidatorModel):
    piiEntities: Optional[List[GuardrailPiiEntity]] = None
    regexes: Optional[List[GuardrailRegex]] = None


class ListGuardrailsResponse(BaseValidatorModel):
    guardrails: List[GuardrailSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GuardrailTopicPolicyConfig(BaseValidatorModel):
    topicsConfig: List[GuardrailTopicConfig]


class GuardrailTopicPolicy(BaseValidatorModel):
    topics: List[GuardrailTopic]


class GuardrailWordPolicyConfig(BaseValidatorModel):
    wordsConfig: Optional[List[GuardrailWordConfig]] = None
    managedWordListsConfig: Optional[List[GuardrailManagedWordsConfig]] = None


class GuardrailWordPolicy(BaseValidatorModel):
    words: Optional[List[GuardrailWord]] = None
    managedWordLists: Optional[List[GuardrailManagedWords]] = None


class ListImportedModelsResponse(BaseValidatorModel):
    modelSummaries: List[ImportedModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class KbInferenceConfigOutput(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfigOutput] = None


class KbInferenceConfig(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfig] = None


class ListGuardrailsRequestPaginate(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInferenceProfilesRequestPaginate(BaseValidatorModel):
    typeEquals: Optional[InferenceProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMarketplaceModelEndpointsRequestPaginate(BaseValidatorModel):
    modelSourceEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPromptRoutersRequestPaginate(BaseValidatorModel):
    type: Optional[PromptRouterTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomModelsRequestPaginate(BaseValidatorModel):
    creationTimeBefore: Optional[Timestamp] = None
    creationTimeAfter: Optional[Timestamp] = None
    nameContains: Optional[str] = None
    baseModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    isOwned: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCustomModelsRequest(BaseValidatorModel):
    creationTimeBefore: Optional[Timestamp] = None
    creationTimeAfter: Optional[Timestamp] = None
    nameContains: Optional[str] = None
    baseModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    isOwned: Optional[bool] = None


class ListEvaluationJobsRequestPaginate(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    applicationTypeEquals: Optional[ApplicationTypeType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEvaluationJobsRequest(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    applicationTypeEquals: Optional[ApplicationTypeType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None


class ListImportedModelsRequestPaginate(BaseValidatorModel):
    creationTimeBefore: Optional[Timestamp] = None
    creationTimeAfter: Optional[Timestamp] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportedModelsRequest(BaseValidatorModel):
    creationTimeBefore: Optional[Timestamp] = None
    creationTimeAfter: Optional[Timestamp] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelCopyJobsRequestPaginate(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ModelCopyJobStatusType] = None
    sourceAccountEquals: Optional[str] = None
    sourceModelArnEquals: Optional[str] = None
    targetModelNameContains: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelCopyJobsRequest(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ModelCopyJobStatusType] = None
    sourceAccountEquals: Optional[str] = None
    sourceModelArnEquals: Optional[str] = None
    targetModelNameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelCustomizationJobsRequestPaginate(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelCustomizationJobsRequest(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelImportJobsRequestPaginate(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ModelImportJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelImportJobsRequest(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ModelImportJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelInvocationJobsRequestPaginate(BaseValidatorModel):
    submitTimeAfter: Optional[Timestamp] = None
    submitTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ModelInvocationJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListModelInvocationJobsRequest(BaseValidatorModel):
    submitTimeAfter: Optional[Timestamp] = None
    submitTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ModelInvocationJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None


class ListProvisionedModelThroughputsRequestPaginate(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListProvisionedModelThroughputsRequest(BaseValidatorModel):
    creationTimeAfter: Optional[Timestamp] = None
    creationTimeBefore: Optional[Timestamp] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal['CreationTime']] = None
    sortOrder: Optional[SortOrderType] = None


class ListMarketplaceModelEndpointsResponse(BaseValidatorModel):
    marketplaceModelEndpoints: List[MarketplaceModelEndpointSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListModelCustomizationJobsResponse(BaseValidatorModel):
    modelCustomizationJobSummaries: List[ModelCustomizationJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListModelImportJobsResponse(BaseValidatorModel):
    modelImportJobSummaries: List[ModelImportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListProvisionedModelThroughputsResponse(BaseValidatorModel):
    provisionedModelSummaries: List[ProvisionedModelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ModelDataSource(BaseValidatorModel):
    s3DataSource: Optional[S3DataSource] = None


class ModelInvocationJobInputDataConfig(BaseValidatorModel):
    s3InputDataConfig: Optional[ModelInvocationJobS3InputDataConfig] = None


class ModelInvocationJobOutputDataConfig(BaseValidatorModel):
    s3OutputDataConfig: Optional[ModelInvocationJobS3OutputDataConfig] = None


class OrchestrationConfiguration(BaseValidatorModel):
    queryTransformationConfiguration: QueryTransformationConfiguration


class RequestMetadataFiltersOutput(BaseValidatorModel):
    equals: Optional[Dict[str, str]] = None
    notEquals: Optional[Dict[str, str]] = None
    andAll: Optional[List[RequestMetadataBaseFiltersOutput]] = None
    orAll: Optional[List[RequestMetadataBaseFiltersOutput]] = None


class RequestMetadataFilters(BaseValidatorModel):
    equals: Optional[Dict[str, str]] = None
    notEquals: Optional[Dict[str, str]] = None
    andAll: Optional[List[RequestMetadataBaseFilters]] = None
    orAll: Optional[List[RequestMetadataBaseFilters]] = None


class SageMakerEndpoint(BaseValidatorModel):
    initialInstanceCount: int
    instanceType: str
    executionRole: str
    kmsEncryptionKey: Optional[str] = None
    vpc: Optional[VpcConfig] = None

VpcConfigUnion = Union[VpcConfig, VpcConfigOutput]


class ValidationDataConfigOutput(BaseValidatorModel):
    validators: List[Validator]


class ValidationDataConfig(BaseValidatorModel):
    validators: List[Validator]


class ExternalSource(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    s3Location: Optional[S3ObjectDoc] = None
    byteContent: Optional[ByteContentDoc] = None


class LoggingConfig(BaseValidatorModel):
    cloudWatchConfig: Optional[CloudWatchConfig] = None
    s3Config: Optional[S3Config] = None
    textDataDeliveryEnabled: Optional[bool] = None
    imageDataDeliveryEnabled: Optional[bool] = None
    embeddingDataDeliveryEnabled: Optional[bool] = None
    videoDataDeliveryEnabled: Optional[bool] = None


class ListModelCopyJobsResponse(BaseValidatorModel):
    modelCopyJobSummaries: List[ModelCopyJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPromptRoutersResponse(BaseValidatorModel):
    promptRouterSummaries: List[PromptRouterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CustomizationConfig(BaseValidatorModel):
    distillationConfig: Optional[DistillationConfig] = None


class EvaluationModelConfig(BaseValidatorModel):
    bedrockModel: Optional[EvaluationBedrockModel] = None


class EvaluationDatasetMetricConfigOutput(BaseValidatorModel):
    taskType: EvaluationTaskTypeType
    dataset: EvaluationDataset
    metricNames: List[str]


class EvaluationDatasetMetricConfig(BaseValidatorModel):
    taskType: EvaluationTaskTypeType
    dataset: EvaluationDataset
    metricNames: List[str]


class KnowledgeBaseVectorSearchConfigurationOutput(BaseValidatorModel):
    numberOfResults: Optional[int] = None
    overrideSearchType: Optional[SearchTypeType] = None
    filter: Optional[RetrievalFilterOutput] = None


class KnowledgeBaseVectorSearchConfiguration(BaseValidatorModel):
    numberOfResults: Optional[int] = None
    overrideSearchType: Optional[SearchTypeType] = None
    filter: Optional[RetrievalFilter] = None


class GetFoundationModelResponse(BaseValidatorModel):
    modelDetails: FoundationModelDetails
    ResponseMetadata: ResponseMetadata


class ListFoundationModelsResponse(BaseValidatorModel):
    modelSummaries: List[FoundationModelSummary]
    ResponseMetadata: ResponseMetadata


class ListInferenceProfilesResponse(BaseValidatorModel):
    inferenceProfileSummaries: List[InferenceProfileSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EndpointConfigOutput(BaseValidatorModel):
    sageMaker: Optional[SageMakerEndpointOutput] = None


class CreateGuardrailRequest(BaseValidatorModel):
    name: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    description: Optional[str] = None
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfig] = None
    contentPolicyConfig: Optional[GuardrailContentPolicyConfig] = None
    wordPolicyConfig: Optional[GuardrailWordPolicyConfig] = None
    sensitiveInformationPolicyConfig: Optional[GuardrailSensitiveInformationPolicyConfig] = None
    contextualGroundingPolicyConfig: Optional[GuardrailContextualGroundingPolicyConfig] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    clientRequestToken: Optional[str] = None


class UpdateGuardrailRequest(BaseValidatorModel):
    guardrailIdentifier: str
    name: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    description: Optional[str] = None
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfig] = None
    contentPolicyConfig: Optional[GuardrailContentPolicyConfig] = None
    wordPolicyConfig: Optional[GuardrailWordPolicyConfig] = None
    sensitiveInformationPolicyConfig: Optional[GuardrailSensitiveInformationPolicyConfig] = None
    contextualGroundingPolicyConfig: Optional[GuardrailContextualGroundingPolicyConfig] = None
    kmsKeyId: Optional[str] = None


class GetGuardrailResponse(BaseValidatorModel):
    name: str
    description: str
    guardrailId: str
    guardrailArn: str
    version: str
    status: GuardrailStatusType
    topicPolicy: GuardrailTopicPolicy
    contentPolicy: GuardrailContentPolicy
    wordPolicy: GuardrailWordPolicy
    sensitiveInformationPolicy: GuardrailSensitiveInformationPolicy
    contextualGroundingPolicy: GuardrailContextualGroundingPolicy
    createdAt: datetime
    updatedAt: datetime
    statusReasons: List[str]
    failureRecommendations: List[str]
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadata


class ExternalSourcesGenerationConfigurationOutput(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplate] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    kbInferenceConfig: Optional[KbInferenceConfigOutput] = None
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None


class GenerationConfigurationOutput(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplate] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    kbInferenceConfig: Optional[KbInferenceConfigOutput] = None
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None


class ExternalSourcesGenerationConfiguration(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplate] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    kbInferenceConfig: Optional[KbInferenceConfig] = None
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None


class GenerationConfiguration(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplate] = None
    guardrailConfiguration: Optional[GuardrailConfiguration] = None
    kbInferenceConfig: Optional[KbInferenceConfig] = None
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None


class GetImportedModelResponse(BaseValidatorModel):
    modelArn: str
    modelName: str
    jobName: str
    jobArn: str
    modelDataSource: ModelDataSource
    creationTime: datetime
    modelArchitecture: str
    modelKmsKeyArn: str
    instructSupported: bool
    ResponseMetadata: ResponseMetadata


class GetModelImportJobResponse(BaseValidatorModel):
    jobArn: str
    jobName: str
    importedModelName: str
    importedModelArn: str
    roleArn: str
    modelDataSource: ModelDataSource
    status: ModelImportJobStatusType
    failureMessage: str
    creationTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    vpcConfig: VpcConfigOutput
    importedModelKmsKeyArn: str
    ResponseMetadata: ResponseMetadata


class GetModelInvocationJobResponse(BaseValidatorModel):
    jobArn: str
    jobName: str
    modelId: str
    clientRequestToken: str
    roleArn: str
    status: ModelInvocationJobStatusType
    message: str
    submitTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    inputDataConfig: ModelInvocationJobInputDataConfig
    outputDataConfig: ModelInvocationJobOutputDataConfig
    vpcConfig: VpcConfigOutput
    timeoutDurationInHours: int
    jobExpirationTime: datetime
    ResponseMetadata: ResponseMetadata


class ModelInvocationJobSummary(BaseValidatorModel):
    jobArn: str
    jobName: str
    modelId: str
    roleArn: str
    submitTime: datetime
    inputDataConfig: ModelInvocationJobInputDataConfig
    outputDataConfig: ModelInvocationJobOutputDataConfig
    clientRequestToken: Optional[str] = None
    status: Optional[ModelInvocationJobStatusType] = None
    message: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    vpcConfig: Optional[VpcConfigOutput] = None
    timeoutDurationInHours: Optional[int] = None
    jobExpirationTime: Optional[datetime] = None


class InvocationLogsConfigOutput(BaseValidatorModel):
    invocationLogSource: InvocationLogSource
    usePromptResponse: Optional[bool] = None
    requestMetadataFilters: Optional[RequestMetadataFiltersOutput] = None


class InvocationLogsConfig(BaseValidatorModel):
    invocationLogSource: InvocationLogSource
    usePromptResponse: Optional[bool] = None
    requestMetadataFilters: Optional[RequestMetadataFilters] = None


class EndpointConfig(BaseValidatorModel):
    sageMaker: Optional[SageMakerEndpoint] = None


class CreateModelImportJobRequest(BaseValidatorModel):
    jobName: str
    importedModelName: str
    roleArn: str
    modelDataSource: ModelDataSource
    jobTags: Optional[List[Tag]] = None
    importedModelTags: Optional[List[Tag]] = None
    clientRequestToken: Optional[str] = None
    vpcConfig: Optional[VpcConfigUnion] = None
    importedModelKmsKeyId: Optional[str] = None


class CreateModelInvocationJobRequest(BaseValidatorModel):
    jobName: str
    roleArn: str
    modelId: str
    inputDataConfig: ModelInvocationJobInputDataConfig
    outputDataConfig: ModelInvocationJobOutputDataConfig
    clientRequestToken: Optional[str] = None
    vpcConfig: Optional[VpcConfigUnion] = None
    timeoutDurationInHours: Optional[int] = None
    tags: Optional[List[Tag]] = None

ValidationDataConfigUnion = Union[ValidationDataConfig, ValidationDataConfigOutput]


class GetModelInvocationLoggingConfigurationResponse(BaseValidatorModel):
    loggingConfig: LoggingConfig
    ResponseMetadata: ResponseMetadata


class PutModelInvocationLoggingConfigurationRequest(BaseValidatorModel):
    loggingConfig: LoggingConfig


class AutomatedEvaluationConfigOutput(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutput]
    evaluatorModelConfig: Optional[EvaluatorModelConfigOutput] = None


class HumanEvaluationConfigOutput(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutput]
    humanWorkflowConfig: Optional[HumanWorkflowConfig] = None
    customMetrics: Optional[List[HumanEvaluationCustomMetric]] = None


class AutomatedEvaluationConfig(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfig]
    evaluatorModelConfig: Optional[EvaluatorModelConfig] = None


class HumanEvaluationConfig(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfig]
    humanWorkflowConfig: Optional[HumanWorkflowConfig] = None
    customMetrics: Optional[List[HumanEvaluationCustomMetric]] = None


class KnowledgeBaseRetrievalConfigurationOutput(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationOutput


class KnowledgeBaseRetrievalConfiguration(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfiguration


class MarketplaceModelEndpoint(BaseValidatorModel):
    endpointArn: str
    modelSourceIdentifier: str
    createdAt: datetime
    updatedAt: datetime
    endpointConfig: EndpointConfigOutput
    endpointStatus: str
    status: Optional[StatusType] = None
    statusMessage: Optional[str] = None
    endpointStatusMessage: Optional[str] = None


class ExternalSourcesRetrieveAndGenerateConfigurationOutput(BaseValidatorModel):
    modelArn: str
    sources: List[ExternalSourceOutput]
    generationConfiguration: Optional[ExternalSourcesGenerationConfigurationOutput] = None


class ExternalSourcesRetrieveAndGenerateConfiguration(BaseValidatorModel):
    modelArn: str
    sources: List[ExternalSource]
    generationConfiguration: Optional[ExternalSourcesGenerationConfiguration] = None


class ListModelInvocationJobsResponse(BaseValidatorModel):
    invocationJobSummaries: List[ModelInvocationJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class TrainingDataConfigOutput(BaseValidatorModel):
    s3Uri: Optional[str] = None
    invocationLogsConfig: Optional[InvocationLogsConfigOutput] = None


class TrainingDataConfig(BaseValidatorModel):
    s3Uri: Optional[str] = None
    invocationLogsConfig: Optional[InvocationLogsConfig] = None

EndpointConfigUnion = Union[EndpointConfig, EndpointConfigOutput]


class EvaluationConfigOutput(BaseValidatorModel):
    automated: Optional[AutomatedEvaluationConfigOutput] = None
    human: Optional[HumanEvaluationConfigOutput] = None


class EvaluationConfig(BaseValidatorModel):
    automated: Optional[AutomatedEvaluationConfig] = None
    human: Optional[HumanEvaluationConfig] = None


class KnowledgeBaseRetrieveAndGenerateConfigurationOutput(BaseValidatorModel):
    knowledgeBaseId: str
    modelArn: str
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationOutput] = None
    generationConfiguration: Optional[GenerationConfigurationOutput] = None
    orchestrationConfiguration: Optional[OrchestrationConfiguration] = None


class RetrieveConfigOutput(BaseValidatorModel):
    knowledgeBaseId: str
    knowledgeBaseRetrievalConfiguration: KnowledgeBaseRetrievalConfigurationOutput


class KnowledgeBaseRetrieveAndGenerateConfiguration(BaseValidatorModel):
    knowledgeBaseId: str
    modelArn: str
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfiguration] = None
    generationConfiguration: Optional[GenerationConfiguration] = None
    orchestrationConfiguration: Optional[OrchestrationConfiguration] = None


class RetrieveConfig(BaseValidatorModel):
    knowledgeBaseId: str
    knowledgeBaseRetrievalConfiguration: KnowledgeBaseRetrievalConfiguration


class CreateMarketplaceModelEndpointResponse(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpoint
    ResponseMetadata: ResponseMetadata


class GetMarketplaceModelEndpointResponse(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpoint
    ResponseMetadata: ResponseMetadata


class RegisterMarketplaceModelEndpointResponse(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpoint
    ResponseMetadata: ResponseMetadata


class UpdateMarketplaceModelEndpointResponse(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpoint
    ResponseMetadata: ResponseMetadata


class GetCustomModelResponse(BaseValidatorModel):
    modelArn: str
    modelName: str
    jobName: str
    jobArn: str
    baseModelArn: str
    customizationType: CustomizationTypeType
    modelKmsKeyArn: str
    hyperParameters: Dict[str, str]
    trainingDataConfig: TrainingDataConfigOutput
    validationDataConfig: ValidationDataConfigOutput
    outputDataConfig: OutputDataConfig
    trainingMetrics: TrainingMetrics
    validationMetrics: List[ValidatorMetric]
    creationTime: datetime
    customizationConfig: CustomizationConfig
    ResponseMetadata: ResponseMetadata


class GetModelCustomizationJobResponse(BaseValidatorModel):
    jobArn: str
    jobName: str
    outputModelName: str
    outputModelArn: str
    clientRequestToken: str
    roleArn: str
    status: ModelCustomizationJobStatusType
    failureMessage: str
    creationTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    baseModelArn: str
    hyperParameters: Dict[str, str]
    trainingDataConfig: TrainingDataConfigOutput
    validationDataConfig: ValidationDataConfigOutput
    outputDataConfig: OutputDataConfig
    customizationType: CustomizationTypeType
    outputModelKmsKeyArn: str
    trainingMetrics: TrainingMetrics
    validationMetrics: List[ValidatorMetric]
    vpcConfig: VpcConfigOutput
    customizationConfig: CustomizationConfig
    ResponseMetadata: ResponseMetadata

TrainingDataConfigUnion = Union[TrainingDataConfig, TrainingDataConfigOutput]


class CreateMarketplaceModelEndpointRequest(BaseValidatorModel):
    modelSourceIdentifier: str
    endpointConfig: EndpointConfigUnion
    endpointName: str
    acceptEula: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class UpdateMarketplaceModelEndpointRequest(BaseValidatorModel):
    endpointArn: str
    endpointConfig: EndpointConfigUnion
    clientRequestToken: Optional[str] = None

EvaluationConfigUnion = Union[EvaluationConfig, EvaluationConfigOutput]


class RetrieveAndGenerateConfigurationOutput(BaseValidatorModel):
    type: RetrieveAndGenerateTypeType
    knowledgeBaseConfiguration: Optional[KnowledgeBaseRetrieveAndGenerateConfigurationOutput] = None
    externalSourcesConfiguration: Optional[ExternalSourcesRetrieveAndGenerateConfigurationOutput] = None


class RetrieveAndGenerateConfiguration(BaseValidatorModel):
    type: RetrieveAndGenerateTypeType
    knowledgeBaseConfiguration: Optional[KnowledgeBaseRetrieveAndGenerateConfiguration] = None
    externalSourcesConfiguration: Optional[ExternalSourcesRetrieveAndGenerateConfiguration] = None


class CreateModelCustomizationJobRequest(BaseValidatorModel):
    jobName: str
    customModelName: str
    roleArn: str
    baseModelIdentifier: str
    trainingDataConfig: TrainingDataConfigUnion
    outputDataConfig: OutputDataConfig
    clientRequestToken: Optional[str] = None
    customizationType: Optional[CustomizationTypeType] = None
    customModelKmsKeyId: Optional[str] = None
    jobTags: Optional[List[Tag]] = None
    customModelTags: Optional[List[Tag]] = None
    validationDataConfig: Optional[ValidationDataConfigUnion] = None
    hyperParameters: Optional[Dict[str, str]] = None
    vpcConfig: Optional[VpcConfigUnion] = None
    customizationConfig: Optional[CustomizationConfig] = None


class KnowledgeBaseConfigOutput(BaseValidatorModel):
    retrieveConfig: Optional[RetrieveConfigOutput] = None
    retrieveAndGenerateConfig: Optional[RetrieveAndGenerateConfigurationOutput] = None


class KnowledgeBaseConfig(BaseValidatorModel):
    retrieveConfig: Optional[RetrieveConfig] = None
    retrieveAndGenerateConfig: Optional[RetrieveAndGenerateConfiguration] = None


class RAGConfigOutput(BaseValidatorModel):
    knowledgeBaseConfig: Optional[KnowledgeBaseConfigOutput] = None


class RAGConfig(BaseValidatorModel):
    knowledgeBaseConfig: Optional[KnowledgeBaseConfig] = None


class EvaluationInferenceConfigOutput(BaseValidatorModel):
    models: Optional[List[EvaluationModelConfig]] = None
    ragConfigs: Optional[List[RAGConfigOutput]] = None


class EvaluationInferenceConfig(BaseValidatorModel):
    models: Optional[List[EvaluationModelConfig]] = None
    ragConfigs: Optional[List[RAGConfig]] = None


class GetEvaluationJobResponse(BaseValidatorModel):
    jobName: str
    status: EvaluationJobStatusType
    jobArn: str
    jobDescription: str
    roleArn: str
    customerEncryptionKeyId: str
    jobType: EvaluationJobTypeType
    applicationType: ApplicationTypeType
    evaluationConfig: EvaluationConfigOutput
    inferenceConfig: EvaluationInferenceConfigOutput
    outputDataConfig: EvaluationOutputDataConfig
    creationTime: datetime
    lastModifiedTime: datetime
    failureMessages: List[str]
    ResponseMetadata: ResponseMetadata

EvaluationInferenceConfigUnion = Union[EvaluationInferenceConfig, EvaluationInferenceConfigOutput]


class CreateEvaluationJobRequest(BaseValidatorModel):
    jobName: str
    roleArn: str
    evaluationConfig: EvaluationConfigUnion
    inferenceConfig: EvaluationInferenceConfigUnion
    outputDataConfig: EvaluationOutputDataConfig
    jobDescription: Optional[str] = None
    clientRequestToken: Optional[str] = None
    customerEncryptionKeyId: Optional[str] = None
    jobTags: Optional[List[Tag]] = None
    applicationType: Optional[ApplicationTypeType] = None