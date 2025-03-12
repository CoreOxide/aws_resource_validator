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
from aws_resource_validator.pydantic_models.bedrock_constants import *

class BatchDeleteEvaluationJobErrorTypeDef(BaseValidatorModel):
    jobIdentifier: str
    code: str
    message: Optional[str] = None


class BatchDeleteEvaluationJobItemTypeDef(BaseValidatorModel):
    jobIdentifier: str
    jobStatus: EvaluationJobStatusType


class BatchDeleteEvaluationJobRequestTypeDef(BaseValidatorModel):
    jobIdentifiers: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BedrockEvaluatorModelTypeDef(BaseValidatorModel):
    modelIdentifier: str


class ByteContentDocOutputTypeDef(BaseValidatorModel):
    identifier: str
    contentType: str
    data: bytes


class S3ConfigTypeDef(BaseValidatorModel):
    bucketName: str
    keyPrefix: Optional[str] = None


class EvaluationOutputDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class CreateGuardrailVersionRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None


class InferenceProfileModelSourceTypeDef(BaseValidatorModel):
    copyFrom: Optional[str] = None


class OutputDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str


class PromptRouterTargetModelTypeDef(BaseValidatorModel):
    modelArn: str


class RoutingCriteriaTypeDef(BaseValidatorModel):
    responseQualityDifference: float


class CustomModelSummaryTypeDef(BaseValidatorModel):
    modelArn: str
    modelName: str
    creationTime: datetime
    baseModelArn: str
    baseModelName: str
    customizationType: Optional[CustomizationTypeType] = None
    ownerAccountId: Optional[str] = None


class DeleteCustomModelRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str


class DeleteGuardrailRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None


class DeleteImportedModelRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str


class DeleteInferenceProfileRequestTypeDef(BaseValidatorModel):
    inferenceProfileIdentifier: str


class DeleteMarketplaceModelEndpointRequestTypeDef(BaseValidatorModel):
    endpointArn: str


class DeletePromptRouterRequestTypeDef(BaseValidatorModel):
    promptRouterArn: str


class DeleteProvisionedModelThroughputRequestTypeDef(BaseValidatorModel):
    provisionedModelId: str


class DeregisterMarketplaceModelEndpointRequestTypeDef(BaseValidatorModel):
    endpointArn: str


class TeacherModelConfigTypeDef(BaseValidatorModel):
    teacherModelIdentifier: str
    maxResponseLengthForInference: Optional[int] = None


class PerformanceConfigurationTypeDef(BaseValidatorModel):
    latency: Optional[PerformanceConfigLatencyType] = None


class EvaluationDatasetLocationTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None


class EvaluationSummaryTypeDef(BaseValidatorModel):
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


class S3ObjectDocTypeDef(BaseValidatorModel):
    uri: str


class GuardrailConfigurationTypeDef(BaseValidatorModel):
    guardrailId: str
    guardrailVersion: str


class PromptTemplateTypeDef(BaseValidatorModel):
    textPromptTemplate: Optional[str] = None


class FilterAttributeOutputTypeDef(BaseValidatorModel):
    key: str
    value: Dict[str, Any]


class FilterAttributeTypeDef(BaseValidatorModel):
    key: str
    value: Mapping[str, Any]


class FoundationModelLifecycleTypeDef(BaseValidatorModel):
    status: FoundationModelLifecycleStatusType


class GetCustomModelRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str


class TrainingMetricsTypeDef(BaseValidatorModel):
    trainingLoss: Optional[float] = None


class ValidatorMetricTypeDef(BaseValidatorModel):
    validationLoss: Optional[float] = None


class GetEvaluationJobRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str


class GetFoundationModelRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str


class GetGuardrailRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None


class GetImportedModelRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str


class GetInferenceProfileRequestTypeDef(BaseValidatorModel):
    inferenceProfileIdentifier: str


class InferenceProfileModelTypeDef(BaseValidatorModel):
    modelArn: Optional[str] = None


class GetMarketplaceModelEndpointRequestTypeDef(BaseValidatorModel):
    endpointArn: str


class GetModelCopyJobRequestTypeDef(BaseValidatorModel):
    jobArn: str


class GetModelCustomizationJobRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str


class VpcConfigOutputTypeDef(BaseValidatorModel):
    subnetIds: List[str]
    securityGroupIds: List[str]


class GetModelImportJobRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str


class GetModelInvocationJobRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str


class GetPromptRouterRequestTypeDef(BaseValidatorModel):
    promptRouterArn: str


class GetProvisionedModelThroughputRequestTypeDef(BaseValidatorModel):
    provisionedModelId: str


class GuardrailRegexConfigTypeDef(BaseValidatorModel):
    name: str
    pattern: str
    action: GuardrailSensitiveInformationActionType
    description: Optional[str] = None


class GuardrailRegexTypeDef(BaseValidatorModel):
    name: str
    pattern: str
    action: GuardrailSensitiveInformationActionType
    description: Optional[str] = None


class GuardrailWordConfigTypeDef(BaseValidatorModel):
    text: str


class GuardrailWordTypeDef(BaseValidatorModel):
    text: str


class HumanEvaluationCustomMetricTypeDef(BaseValidatorModel):
    name: str
    ratingMethod: str
    description: Optional[str] = None


class HumanWorkflowConfigTypeDef(BaseValidatorModel):
    flowDefinitionArn: str
    instructions: Optional[str] = None


class ImportedModelSummaryTypeDef(BaseValidatorModel):
    modelArn: str
    modelName: str
    creationTime: datetime
    instructSupported: Optional[bool] = None
    modelArchitecture: Optional[str] = None


class InvocationLogSourceTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None


class TextInferenceConfigOutputTypeDef(BaseValidatorModel):
    temperature: Optional[float] = None
    topP: Optional[float] = None
    maxTokens: Optional[int] = None
    stopSequences: Optional[List[str]] = None


class TextInferenceConfigTypeDef(BaseValidatorModel):
    temperature: Optional[float] = None
    topP: Optional[float] = None
    maxTokens: Optional[int] = None
    stopSequences: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListFoundationModelsRequestTypeDef(BaseValidatorModel):
    byProvider: Optional[str] = None
    byCustomizationType: Optional[ModelCustomizationType] = None
    byOutputModality: Optional[ModelModalityType] = None
    byInferenceType: Optional[InferenceTypeType] = None


class ListGuardrailsRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInferenceProfilesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    typeEquals: Optional[InferenceProfileTypeType] = None


class ListMarketplaceModelEndpointsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    modelSourceEquals: Optional[str] = None


class MarketplaceModelEndpointSummaryTypeDef(BaseValidatorModel):
    endpointArn: str
    modelSourceIdentifier: str
    createdAt: datetime
    updatedAt: datetime
    status: Optional[StatusType] = None
    statusMessage: Optional[str] = None


class ModelCustomizationJobSummaryTypeDef(BaseValidatorModel):
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


class ModelImportJobSummaryTypeDef(BaseValidatorModel):
    jobArn: str
    jobName: str
    status: ModelImportJobStatusType
    creationTime: datetime
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    importedModelArn: Optional[str] = None
    importedModelName: Optional[str] = None


class ProvisionedModelSummaryTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str


class S3DataSourceTypeDef(BaseValidatorModel):
    s3Uri: str


class ModelInvocationJobS3InputDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str
    s3InputFormat: Optional[Literal["JSONL"]] = None
    s3BucketOwner: Optional[str] = None


class ModelInvocationJobS3OutputDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str
    s3EncryptionKeyId: Optional[str] = None
    s3BucketOwner: Optional[str] = None


class RegisterMarketplaceModelEndpointRequestTypeDef(BaseValidatorModel):
    endpointIdentifier: str
    modelSourceIdentifier: str


class RequestMetadataBaseFiltersOutputTypeDef(BaseValidatorModel):
    equals: Optional[Dict[str, str]] = None
    notEquals: Optional[Dict[str, str]] = None


class RequestMetadataBaseFiltersTypeDef(BaseValidatorModel):
    equals: Optional[Mapping[str, str]] = None
    notEquals: Optional[Mapping[str, str]] = None


class VpcConfigTypeDef(BaseValidatorModel):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]


class StopEvaluationJobRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str


class StopModelCustomizationJobRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str


class StopModelInvocationJobRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class UpdateProvisionedModelThroughputRequestTypeDef(BaseValidatorModel):
    provisionedModelId: str
    desiredProvisionedModelName: Optional[str] = None
    desiredModelId: Optional[str] = None


class ValidatorTypeDef(BaseValidatorModel):
    s3Uri: str


class BatchDeleteEvaluationJobResponseTypeDef(BaseValidatorModel):
    errors: List[BatchDeleteEvaluationJobErrorTypeDef]
    evaluationJobs: List[BatchDeleteEvaluationJobItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEvaluationJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGuardrailResponseTypeDef(BaseValidatorModel):
    guardrailId: str
    guardrailArn: str
    version: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGuardrailVersionResponseTypeDef(BaseValidatorModel):
    guardrailId: str
    version: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInferenceProfileResponseTypeDef(BaseValidatorModel):
    inferenceProfileArn: str
    status: Literal["ACTIVE"]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelCopyJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelCustomizationJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelImportJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelInvocationJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePromptRouterResponseTypeDef(BaseValidatorModel):
    promptRouterArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateProvisionedModelThroughputResponseTypeDef(BaseValidatorModel):
    provisionedModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetProvisionedModelThroughputResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGuardrailResponseTypeDef(BaseValidatorModel):
    guardrailId: str
    guardrailArn: str
    version: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class EvaluatorModelConfigOutputTypeDef(BaseValidatorModel):
    bedrockEvaluatorModels: Optional[List[BedrockEvaluatorModelTypeDef]] = None


class EvaluatorModelConfigTypeDef(BaseValidatorModel):
    bedrockEvaluatorModels: Optional[Sequence[BedrockEvaluatorModelTypeDef]] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class ByteContentDocTypeDef(BaseValidatorModel):
    identifier: str
    contentType: str
    data: BlobTypeDef


class CloudWatchConfigTypeDef(BaseValidatorModel):
    logGroupName: str
    roleArn: str
    largeDataDeliveryS3Config: Optional[S3ConfigTypeDef] = None


class CreateModelCopyJobRequestTypeDef(BaseValidatorModel):
    sourceModelArn: str
    targetModelName: str
    modelKmsKeyId: Optional[str] = None
    targetModelTags: Optional[Sequence[TagTypeDef]] = None
    clientRequestToken: Optional[str] = None


class CreateProvisionedModelThroughputRequestTypeDef(BaseValidatorModel):
    modelUnits: int
    provisionedModelName: str
    modelId: str
    clientRequestToken: Optional[str] = None
    commitmentDuration: Optional[CommitmentDurationType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class GetModelCopyJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    status: ModelCopyJobStatusType
    creationTime: datetime
    targetModelArn: str
    targetModelName: str
    sourceAccountId: str
    sourceModelArn: str
    targetModelKmsKeyArn: str
    targetModelTags: List[TagTypeDef]
    failureMessage: str
    sourceModelName: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModelCopyJobSummaryTypeDef(BaseValidatorModel):
    jobArn: str
    status: ModelCopyJobStatusType
    creationTime: datetime
    targetModelArn: str
    sourceAccountId: str
    sourceModelArn: str
    targetModelName: Optional[str] = None
    targetModelKmsKeyArn: Optional[str] = None
    targetModelTags: Optional[List[TagTypeDef]] = None
    failureMessage: Optional[str] = None
    sourceModelName: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]


class CreateInferenceProfileRequestTypeDef(BaseValidatorModel):
    inferenceProfileName: str
    modelSource: InferenceProfileModelSourceTypeDef
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreatePromptRouterRequestTypeDef(BaseValidatorModel):
    promptRouterName: str
    models: Sequence[PromptRouterTargetModelTypeDef]
    routingCriteria: RoutingCriteriaTypeDef
    fallbackModel: PromptRouterTargetModelTypeDef
    clientRequestToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListCustomModelsResponseTypeDef(BaseValidatorModel):
    modelSummaries: List[CustomModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DistillationConfigTypeDef(BaseValidatorModel):
    teacherModelConfig: TeacherModelConfigTypeDef


class EvaluationBedrockModelTypeDef(BaseValidatorModel):
    modelIdentifier: str
    inferenceParams: Optional[str] = None
    performanceConfig: Optional[PerformanceConfigurationTypeDef] = None


class EvaluationDatasetTypeDef(BaseValidatorModel):
    name: str
    datasetLocation: Optional[EvaluationDatasetLocationTypeDef] = None


class ListEvaluationJobsResponseTypeDef(BaseValidatorModel):
    jobSummaries: List[EvaluationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ExternalSourceOutputTypeDef(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    s3Location: Optional[S3ObjectDocTypeDef] = None
    byteContent: Optional[ByteContentDocOutputTypeDef] = None


class FoundationModelDetailsTypeDef(BaseValidatorModel):
    modelArn: str
    modelId: str
    modelName: Optional[str] = None
    providerName: Optional[str] = None
    inputModalities: Optional[List[ModelModalityType]] = None
    outputModalities: Optional[List[ModelModalityType]] = None
    responseStreamingSupported: Optional[bool] = None
    customizationsSupported: Optional[List[ModelCustomizationType]] = None
    inferenceTypesSupported: Optional[List[InferenceTypeType]] = None
    modelLifecycle: Optional[FoundationModelLifecycleTypeDef] = None


class FoundationModelSummaryTypeDef(BaseValidatorModel):
    modelArn: str
    modelId: str
    modelName: Optional[str] = None
    providerName: Optional[str] = None
    inputModalities: Optional[List[ModelModalityType]] = None
    outputModalities: Optional[List[ModelModalityType]] = None
    responseStreamingSupported: Optional[bool] = None
    customizationsSupported: Optional[List[ModelCustomizationType]] = None
    inferenceTypesSupported: Optional[List[InferenceTypeType]] = None
    modelLifecycle: Optional[FoundationModelLifecycleTypeDef] = None


class SageMakerEndpointOutputTypeDef(BaseValidatorModel):
    initialInstanceCount: int
    instanceType: str
    executionRole: str
    kmsEncryptionKey: Optional[str] = None
    vpc: Optional[VpcConfigOutputTypeDef] = None


class GuardrailContentFilterConfigTypeDef(BaseValidatorModel):
    pass


class GuardrailContentPolicyConfigTypeDef(BaseValidatorModel):
    filtersConfig: Sequence[GuardrailContentFilterConfigTypeDef]


class GuardrailContentFilterTypeDef(BaseValidatorModel):
    pass


class GuardrailContentPolicyTypeDef(BaseValidatorModel):
    filters: Optional[List[GuardrailContentFilterTypeDef]] = None


class GuardrailContextualGroundingFilterConfigTypeDef(BaseValidatorModel):
    pass


class GuardrailContextualGroundingPolicyConfigTypeDef(BaseValidatorModel):
    filtersConfig: Sequence[GuardrailContextualGroundingFilterConfigTypeDef]


class GuardrailContextualGroundingFilterTypeDef(BaseValidatorModel):
    pass


class GuardrailContextualGroundingPolicyTypeDef(BaseValidatorModel):
    filters: List[GuardrailContextualGroundingFilterTypeDef]


class GuardrailPiiEntityConfigTypeDef(BaseValidatorModel):
    pass


class GuardrailSensitiveInformationPolicyConfigTypeDef(BaseValidatorModel):
    piiEntitiesConfig: Optional[Sequence[GuardrailPiiEntityConfigTypeDef]] = None
    regexesConfig: Optional[Sequence[GuardrailRegexConfigTypeDef]] = None


class GuardrailPiiEntityTypeDef(BaseValidatorModel):
    pass


class GuardrailSensitiveInformationPolicyTypeDef(BaseValidatorModel):
    piiEntities: Optional[List[GuardrailPiiEntityTypeDef]] = None
    regexes: Optional[List[GuardrailRegexTypeDef]] = None


class GuardrailSummaryTypeDef(BaseValidatorModel):
    pass


class ListGuardrailsResponseTypeDef(BaseValidatorModel):
    guardrails: List[GuardrailSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GuardrailTopicConfigTypeDef(BaseValidatorModel):
    pass


class GuardrailTopicPolicyConfigTypeDef(BaseValidatorModel):
    topicsConfig: Sequence[GuardrailTopicConfigTypeDef]


class GuardrailTopicTypeDef(BaseValidatorModel):
    pass


class GuardrailTopicPolicyTypeDef(BaseValidatorModel):
    topics: List[GuardrailTopicTypeDef]


class GuardrailManagedWordsConfigTypeDef(BaseValidatorModel):
    pass


class GuardrailWordPolicyConfigTypeDef(BaseValidatorModel):
    wordsConfig: Optional[Sequence[GuardrailWordConfigTypeDef]] = None
    managedWordListsConfig: Optional[Sequence[GuardrailManagedWordsConfigTypeDef]] = None


class GuardrailManagedWordsTypeDef(BaseValidatorModel):
    pass


class GuardrailWordPolicyTypeDef(BaseValidatorModel):
    words: Optional[List[GuardrailWordTypeDef]] = None
    managedWordLists: Optional[List[GuardrailManagedWordsTypeDef]] = None


class ListImportedModelsResponseTypeDef(BaseValidatorModel):
    modelSummaries: List[ImportedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class KbInferenceConfigOutputTypeDef(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfigOutputTypeDef] = None


class KbInferenceConfigTypeDef(BaseValidatorModel):
    textInferenceConfig: Optional[TextInferenceConfigTypeDef] = None


class ListGuardrailsRequestPaginateTypeDef(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInferenceProfilesRequestPaginateTypeDef(BaseValidatorModel):
    typeEquals: Optional[InferenceProfileTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMarketplaceModelEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    modelSourceEquals: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListCustomModelsRequestPaginateTypeDef(BaseValidatorModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    baseModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    isOwned: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListCustomModelsRequestTypeDef(BaseValidatorModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    baseModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    isOwned: Optional[bool] = None


class ListEvaluationJobsRequestPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    applicationTypeEquals: Optional[ApplicationTypeType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEvaluationJobsRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    applicationTypeEquals: Optional[ApplicationTypeType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListImportedModelsRequestPaginateTypeDef(BaseValidatorModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListImportedModelsRequestTypeDef(BaseValidatorModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelCopyJobsRequestPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ModelCopyJobStatusType] = None
    sourceAccountEquals: Optional[str] = None
    sourceModelArnEquals: Optional[str] = None
    targetModelNameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListModelCopyJobsRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ModelCopyJobStatusType] = None
    sourceAccountEquals: Optional[str] = None
    sourceModelArnEquals: Optional[str] = None
    targetModelNameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelCustomizationJobsRequestPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListModelCustomizationJobsRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelImportJobsRequestPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ModelImportJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListModelImportJobsRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ModelImportJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListModelInvocationJobsRequestPaginateTypeDef(BaseValidatorModel):
    submitTimeAfter: Optional[TimestampTypeDef] = None
    submitTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ModelInvocationJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListModelInvocationJobsRequestTypeDef(BaseValidatorModel):
    submitTimeAfter: Optional[TimestampTypeDef] = None
    submitTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ModelInvocationJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListProvisionedModelThroughputsRequestPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListProvisionedModelThroughputsRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None


class ListMarketplaceModelEndpointsResponseTypeDef(BaseValidatorModel):
    marketplaceModelEndpoints: List[MarketplaceModelEndpointSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListModelCustomizationJobsResponseTypeDef(BaseValidatorModel):
    modelCustomizationJobSummaries: List[ModelCustomizationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListModelImportJobsResponseTypeDef(BaseValidatorModel):
    modelImportJobSummaries: List[ModelImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListProvisionedModelThroughputsResponseTypeDef(BaseValidatorModel):
    provisionedModelSummaries: List[ProvisionedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ModelDataSourceTypeDef(BaseValidatorModel):
    s3DataSource: Optional[S3DataSourceTypeDef] = None


class ModelInvocationJobInputDataConfigTypeDef(BaseValidatorModel):
    s3InputDataConfig: Optional[ModelInvocationJobS3InputDataConfigTypeDef] = None


class ModelInvocationJobOutputDataConfigTypeDef(BaseValidatorModel):
    s3OutputDataConfig: Optional[ModelInvocationJobS3OutputDataConfigTypeDef] = None


class QueryTransformationConfigurationTypeDef(BaseValidatorModel):
    pass


class OrchestrationConfigurationTypeDef(BaseValidatorModel):
    queryTransformationConfiguration: QueryTransformationConfigurationTypeDef


class RequestMetadataFiltersOutputTypeDef(BaseValidatorModel):
    equals: Optional[Dict[str, str]] = None
    notEquals: Optional[Dict[str, str]] = None
    andAll: Optional[List[RequestMetadataBaseFiltersOutputTypeDef]] = None
    orAll: Optional[List[RequestMetadataBaseFiltersOutputTypeDef]] = None


class RequestMetadataFiltersTypeDef(BaseValidatorModel):
    equals: Optional[Mapping[str, str]] = None
    notEquals: Optional[Mapping[str, str]] = None
    andAll: Optional[Sequence[RequestMetadataBaseFiltersTypeDef]] = None
    orAll: Optional[Sequence[RequestMetadataBaseFiltersTypeDef]] = None


class SageMakerEndpointTypeDef(BaseValidatorModel):
    initialInstanceCount: int
    instanceType: str
    executionRole: str
    kmsEncryptionKey: Optional[str] = None
    vpc: Optional[VpcConfigTypeDef] = None


class ValidationDataConfigOutputTypeDef(BaseValidatorModel):
    validators: List[ValidatorTypeDef]


class ValidationDataConfigTypeDef(BaseValidatorModel):
    validators: Sequence[ValidatorTypeDef]


class ExternalSourceTypeDef(BaseValidatorModel):
    sourceType: ExternalSourceTypeType
    s3Location: Optional[S3ObjectDocTypeDef] = None
    byteContent: Optional[ByteContentDocTypeDef] = None


class LoggingConfigTypeDef(BaseValidatorModel):
    cloudWatchConfig: Optional[CloudWatchConfigTypeDef] = None
    s3Config: Optional[S3ConfigTypeDef] = None
    textDataDeliveryEnabled: Optional[bool] = None
    imageDataDeliveryEnabled: Optional[bool] = None
    embeddingDataDeliveryEnabled: Optional[bool] = None
    videoDataDeliveryEnabled: Optional[bool] = None


class ListModelCopyJobsResponseTypeDef(BaseValidatorModel):
    modelCopyJobSummaries: List[ModelCopyJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PromptRouterSummaryTypeDef(BaseValidatorModel):
    pass


class ListPromptRoutersResponseTypeDef(BaseValidatorModel):
    promptRouterSummaries: List[PromptRouterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CustomizationConfigTypeDef(BaseValidatorModel):
    distillationConfig: Optional[DistillationConfigTypeDef] = None


class EvaluationModelConfigTypeDef(BaseValidatorModel):
    bedrockModel: Optional[EvaluationBedrockModelTypeDef] = None


class EvaluationDatasetMetricConfigOutputTypeDef(BaseValidatorModel):
    taskType: EvaluationTaskTypeType
    dataset: EvaluationDatasetTypeDef
    metricNames: List[str]


class EvaluationDatasetMetricConfigTypeDef(BaseValidatorModel):
    taskType: EvaluationTaskTypeType
    dataset: EvaluationDatasetTypeDef
    metricNames: Sequence[str]


class GetFoundationModelResponseTypeDef(BaseValidatorModel):
    modelDetails: FoundationModelDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListFoundationModelsResponseTypeDef(BaseValidatorModel):
    modelSummaries: List[FoundationModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class InferenceProfileSummaryTypeDef(BaseValidatorModel):
    pass


class ListInferenceProfilesResponseTypeDef(BaseValidatorModel):
    inferenceProfileSummaries: List[InferenceProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EndpointConfigOutputTypeDef(BaseValidatorModel):
    sageMaker: Optional[SageMakerEndpointOutputTypeDef] = None


class CreateGuardrailRequestTypeDef(BaseValidatorModel):
    name: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    description: Optional[str] = None
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfigTypeDef] = None
    contentPolicyConfig: Optional[GuardrailContentPolicyConfigTypeDef] = None
    wordPolicyConfig: Optional[GuardrailWordPolicyConfigTypeDef] = None
    sensitiveInformationPolicyConfig: Optional[GuardrailSensitiveInformationPolicyConfigTypeDef] = None
    contextualGroundingPolicyConfig: Optional[GuardrailContextualGroundingPolicyConfigTypeDef] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientRequestToken: Optional[str] = None


class UpdateGuardrailRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    name: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    description: Optional[str] = None
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfigTypeDef] = None
    contentPolicyConfig: Optional[GuardrailContentPolicyConfigTypeDef] = None
    wordPolicyConfig: Optional[GuardrailWordPolicyConfigTypeDef] = None
    sensitiveInformationPolicyConfig: Optional[GuardrailSensitiveInformationPolicyConfigTypeDef] = None
    contextualGroundingPolicyConfig: Optional[GuardrailContextualGroundingPolicyConfigTypeDef] = None
    kmsKeyId: Optional[str] = None


class GetGuardrailResponseTypeDef(BaseValidatorModel):
    name: str
    description: str
    guardrailId: str
    guardrailArn: str
    version: str
    status: GuardrailStatusType
    topicPolicy: GuardrailTopicPolicyTypeDef
    contentPolicy: GuardrailContentPolicyTypeDef
    wordPolicy: GuardrailWordPolicyTypeDef
    sensitiveInformationPolicy: GuardrailSensitiveInformationPolicyTypeDef
    contextualGroundingPolicy: GuardrailContextualGroundingPolicyTypeDef
    createdAt: datetime
    updatedAt: datetime
    statusReasons: List[str]
    failureRecommendations: List[str]
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    kmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ExternalSourcesGenerationConfigurationOutputTypeDef(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplateTypeDef] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    kbInferenceConfig: Optional[KbInferenceConfigOutputTypeDef] = None
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None


class GenerationConfigurationOutputTypeDef(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplateTypeDef] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    kbInferenceConfig: Optional[KbInferenceConfigOutputTypeDef] = None
    additionalModelRequestFields: Optional[Dict[str, Dict[str, Any]]] = None


class ExternalSourcesGenerationConfigurationTypeDef(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplateTypeDef] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    kbInferenceConfig: Optional[KbInferenceConfigTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None


class GenerationConfigurationTypeDef(BaseValidatorModel):
    promptTemplate: Optional[PromptTemplateTypeDef] = None
    guardrailConfiguration: Optional[GuardrailConfigurationTypeDef] = None
    kbInferenceConfig: Optional[KbInferenceConfigTypeDef] = None
    additionalModelRequestFields: Optional[Mapping[str, Mapping[str, Any]]] = None


class GetImportedModelResponseTypeDef(BaseValidatorModel):
    modelArn: str
    modelName: str
    jobName: str
    jobArn: str
    modelDataSource: ModelDataSourceTypeDef
    creationTime: datetime
    modelArchitecture: str
    modelKmsKeyArn: str
    instructSupported: bool
    ResponseMetadata: ResponseMetadataTypeDef


class GetModelImportJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    jobName: str
    importedModelName: str
    importedModelArn: str
    roleArn: str
    modelDataSource: ModelDataSourceTypeDef
    status: ModelImportJobStatusType
    failureMessage: str
    creationTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    vpcConfig: VpcConfigOutputTypeDef
    importedModelKmsKeyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetModelInvocationJobResponseTypeDef(BaseValidatorModel):
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
    inputDataConfig: ModelInvocationJobInputDataConfigTypeDef
    outputDataConfig: ModelInvocationJobOutputDataConfigTypeDef
    vpcConfig: VpcConfigOutputTypeDef
    timeoutDurationInHours: int
    jobExpirationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ModelInvocationJobSummaryTypeDef(BaseValidatorModel):
    jobArn: str
    jobName: str
    modelId: str
    roleArn: str
    submitTime: datetime
    inputDataConfig: ModelInvocationJobInputDataConfigTypeDef
    outputDataConfig: ModelInvocationJobOutputDataConfigTypeDef
    clientRequestToken: Optional[str] = None
    status: Optional[ModelInvocationJobStatusType] = None
    message: Optional[str] = None
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    vpcConfig: Optional[VpcConfigOutputTypeDef] = None
    timeoutDurationInHours: Optional[int] = None
    jobExpirationTime: Optional[datetime] = None


class InvocationLogsConfigOutputTypeDef(BaseValidatorModel):
    invocationLogSource: InvocationLogSourceTypeDef
    usePromptResponse: Optional[bool] = None
    requestMetadataFilters: Optional[RequestMetadataFiltersOutputTypeDef] = None


class InvocationLogsConfigTypeDef(BaseValidatorModel):
    invocationLogSource: InvocationLogSourceTypeDef
    usePromptResponse: Optional[bool] = None
    requestMetadataFilters: Optional[RequestMetadataFiltersTypeDef] = None


class EndpointConfigTypeDef(BaseValidatorModel):
    sageMaker: Optional[SageMakerEndpointTypeDef] = None


class VpcConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateModelImportJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    importedModelName: str
    roleArn: str
    modelDataSource: ModelDataSourceTypeDef
    jobTags: Optional[Sequence[TagTypeDef]] = None
    importedModelTags: Optional[Sequence[TagTypeDef]] = None
    clientRequestToken: Optional[str] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None
    importedModelKmsKeyId: Optional[str] = None


class CreateModelInvocationJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    roleArn: str
    modelId: str
    inputDataConfig: ModelInvocationJobInputDataConfigTypeDef
    outputDataConfig: ModelInvocationJobOutputDataConfigTypeDef
    clientRequestToken: Optional[str] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None
    timeoutDurationInHours: Optional[int] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class GetModelInvocationLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    loggingConfig: LoggingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutModelInvocationLoggingConfigurationRequestTypeDef(BaseValidatorModel):
    loggingConfig: LoggingConfigTypeDef


class AutomatedEvaluationConfigOutputTypeDef(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutputTypeDef]
    evaluatorModelConfig: Optional[EvaluatorModelConfigOutputTypeDef] = None


class HumanEvaluationConfigOutputTypeDef(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutputTypeDef]
    humanWorkflowConfig: Optional[HumanWorkflowConfigTypeDef] = None
    customMetrics: Optional[List[HumanEvaluationCustomMetricTypeDef]] = None


class AutomatedEvaluationConfigTypeDef(BaseValidatorModel):
    datasetMetricConfigs: Sequence[EvaluationDatasetMetricConfigTypeDef]
    evaluatorModelConfig: Optional[EvaluatorModelConfigTypeDef] = None


class HumanEvaluationConfigTypeDef(BaseValidatorModel):
    datasetMetricConfigs: Sequence[EvaluationDatasetMetricConfigTypeDef]
    humanWorkflowConfig: Optional[HumanWorkflowConfigTypeDef] = None
    customMetrics: Optional[Sequence[HumanEvaluationCustomMetricTypeDef]] = None


class KnowledgeBaseVectorSearchConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalConfigurationOutputTypeDef(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationOutputTypeDef


class KnowledgeBaseVectorSearchConfigurationTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseRetrievalConfigurationTypeDef(BaseValidatorModel):
    vectorSearchConfiguration: KnowledgeBaseVectorSearchConfigurationTypeDef


class MarketplaceModelEndpointTypeDef(BaseValidatorModel):
    endpointArn: str
    modelSourceIdentifier: str
    createdAt: datetime
    updatedAt: datetime
    endpointConfig: EndpointConfigOutputTypeDef
    endpointStatus: str
    status: Optional[StatusType] = None
    statusMessage: Optional[str] = None
    endpointStatusMessage: Optional[str] = None


class ExternalSourcesRetrieveAndGenerateConfigurationOutputTypeDef(BaseValidatorModel):
    modelArn: str
    sources: List[ExternalSourceOutputTypeDef]
    generationConfiguration: Optional[ExternalSourcesGenerationConfigurationOutputTypeDef] = None


class ExternalSourcesRetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    modelArn: str
    sources: Sequence[ExternalSourceTypeDef]
    generationConfiguration: Optional[ExternalSourcesGenerationConfigurationTypeDef] = None


class ListModelInvocationJobsResponseTypeDef(BaseValidatorModel):
    invocationJobSummaries: List[ModelInvocationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TrainingDataConfigOutputTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None
    invocationLogsConfig: Optional[InvocationLogsConfigOutputTypeDef] = None


class TrainingDataConfigTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None
    invocationLogsConfig: Optional[InvocationLogsConfigTypeDef] = None


class EvaluationConfigOutputTypeDef(BaseValidatorModel):
    automated: Optional[AutomatedEvaluationConfigOutputTypeDef] = None
    human: Optional[HumanEvaluationConfigOutputTypeDef] = None


class EvaluationConfigTypeDef(BaseValidatorModel):
    automated: Optional[AutomatedEvaluationConfigTypeDef] = None
    human: Optional[HumanEvaluationConfigTypeDef] = None


class KnowledgeBaseRetrieveAndGenerateConfigurationOutputTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    modelArn: str
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationOutputTypeDef] = None
    generationConfiguration: Optional[GenerationConfigurationOutputTypeDef] = None
    orchestrationConfiguration: Optional[OrchestrationConfigurationTypeDef] = None


class RetrieveConfigOutputTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    knowledgeBaseRetrievalConfiguration: KnowledgeBaseRetrievalConfigurationOutputTypeDef


class KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    modelArn: str
    retrievalConfiguration: Optional[KnowledgeBaseRetrievalConfigurationTypeDef] = None
    generationConfiguration: Optional[GenerationConfigurationTypeDef] = None
    orchestrationConfiguration: Optional[OrchestrationConfigurationTypeDef] = None


class RetrieveConfigTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    knowledgeBaseRetrievalConfiguration: KnowledgeBaseRetrievalConfigurationTypeDef


class CreateMarketplaceModelEndpointResponseTypeDef(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMarketplaceModelEndpointResponseTypeDef(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterMarketplaceModelEndpointResponseTypeDef(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMarketplaceModelEndpointResponseTypeDef(BaseValidatorModel):
    marketplaceModelEndpoint: MarketplaceModelEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCustomModelResponseTypeDef(BaseValidatorModel):
    modelArn: str
    modelName: str
    jobName: str
    jobArn: str
    baseModelArn: str
    customizationType: CustomizationTypeType
    modelKmsKeyArn: str
    hyperParameters: Dict[str, str]
    trainingDataConfig: TrainingDataConfigOutputTypeDef
    validationDataConfig: ValidationDataConfigOutputTypeDef
    outputDataConfig: OutputDataConfigTypeDef
    trainingMetrics: TrainingMetricsTypeDef
    validationMetrics: List[ValidatorMetricTypeDef]
    creationTime: datetime
    customizationConfig: CustomizationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetModelCustomizationJobResponseTypeDef(BaseValidatorModel):
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
    trainingDataConfig: TrainingDataConfigOutputTypeDef
    validationDataConfig: ValidationDataConfigOutputTypeDef
    outputDataConfig: OutputDataConfigTypeDef
    customizationType: CustomizationTypeType
    outputModelKmsKeyArn: str
    trainingMetrics: TrainingMetricsTypeDef
    validationMetrics: List[ValidatorMetricTypeDef]
    vpcConfig: VpcConfigOutputTypeDef
    customizationConfig: CustomizationConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateMarketplaceModelEndpointRequestTypeDef(BaseValidatorModel):
    modelSourceIdentifier: str
    endpointConfig: EndpointConfigUnionTypeDef
    endpointName: str
    acceptEula: Optional[bool] = None
    clientRequestToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateMarketplaceModelEndpointRequestTypeDef(BaseValidatorModel):
    endpointArn: str
    endpointConfig: EndpointConfigUnionTypeDef
    clientRequestToken: Optional[str] = None


class ValidationDataConfigUnionTypeDef(BaseValidatorModel):
    pass


class TrainingDataConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateModelCustomizationJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    customModelName: str
    roleArn: str
    baseModelIdentifier: str
    trainingDataConfig: TrainingDataConfigUnionTypeDef
    outputDataConfig: OutputDataConfigTypeDef
    clientRequestToken: Optional[str] = None
    customizationType: Optional[CustomizationTypeType] = None
    customModelKmsKeyId: Optional[str] = None
    jobTags: Optional[Sequence[TagTypeDef]] = None
    customModelTags: Optional[Sequence[TagTypeDef]] = None
    validationDataConfig: Optional[ValidationDataConfigUnionTypeDef] = None
    hyperParameters: Optional[Mapping[str, str]] = None
    vpcConfig: Optional[VpcConfigUnionTypeDef] = None
    customizationConfig: Optional[CustomizationConfigTypeDef] = None


class RetrieveAndGenerateConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseConfigOutputTypeDef(BaseValidatorModel):
    retrieveConfig: Optional[RetrieveConfigOutputTypeDef] = None
    retrieveAndGenerateConfig: Optional[RetrieveAndGenerateConfigurationOutputTypeDef] = None


class RetrieveAndGenerateConfigurationTypeDef(BaseValidatorModel):
    pass


class KnowledgeBaseConfigTypeDef(BaseValidatorModel):
    retrieveConfig: Optional[RetrieveConfigTypeDef] = None
    retrieveAndGenerateConfig: Optional[RetrieveAndGenerateConfigurationTypeDef] = None


class RAGConfigOutputTypeDef(BaseValidatorModel):
    knowledgeBaseConfig: Optional[KnowledgeBaseConfigOutputTypeDef] = None


class RAGConfigTypeDef(BaseValidatorModel):
    knowledgeBaseConfig: Optional[KnowledgeBaseConfigTypeDef] = None


class EvaluationInferenceConfigOutputTypeDef(BaseValidatorModel):
    models: Optional[List[EvaluationModelConfigTypeDef]] = None
    ragConfigs: Optional[List[RAGConfigOutputTypeDef]] = None


class EvaluationInferenceConfigTypeDef(BaseValidatorModel):
    models: Optional[Sequence[EvaluationModelConfigTypeDef]] = None
    ragConfigs: Optional[Sequence[RAGConfigTypeDef]] = None


class GetEvaluationJobResponseTypeDef(BaseValidatorModel):
    jobName: str
    status: EvaluationJobStatusType
    jobArn: str
    jobDescription: str
    roleArn: str
    customerEncryptionKeyId: str
    jobType: EvaluationJobTypeType
    applicationType: ApplicationTypeType
    evaluationConfig: EvaluationConfigOutputTypeDef
    inferenceConfig: EvaluationInferenceConfigOutputTypeDef
    outputDataConfig: EvaluationOutputDataConfigTypeDef
    creationTime: datetime
    lastModifiedTime: datetime
    failureMessages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class EvaluationConfigUnionTypeDef(BaseValidatorModel):
    pass


class EvaluationInferenceConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateEvaluationJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    roleArn: str
    evaluationConfig: EvaluationConfigUnionTypeDef
    inferenceConfig: EvaluationInferenceConfigUnionTypeDef
    outputDataConfig: EvaluationOutputDataConfigTypeDef
    jobDescription: Optional[str] = None
    clientRequestToken: Optional[str] = None
    customerEncryptionKeyId: Optional[str] = None
    jobTags: Optional[Sequence[TagTypeDef]] = None
    applicationType: Optional[ApplicationTypeType] = None


