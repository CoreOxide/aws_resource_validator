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
from aws_resource_validator.pydantic_models.bedrock_constants import *

class S3ConfigTypeDef(BaseModel):
    bucketName: str
    keyPrefix: Optional[str] = None

class EvaluationOutputDataConfigTypeDef(BaseModel):
    s3Uri: str

class TagTypeDef(BaseModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateGuardrailVersionRequestRequestTypeDef(BaseModel):
    guardrailIdentifier: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None

class OutputDataConfigTypeDef(BaseModel):
    s3Uri: str

class TrainingDataConfigTypeDef(BaseModel):
    s3Uri: str

class VpcConfigTypeDef(BaseModel):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]

class CustomModelSummaryTypeDef(BaseModel):
    modelArn: str
    modelName: str
    creationTime: datetime
    baseModelArn: str
    baseModelName: str
    customizationType: Optional[CustomizationTypeType] = None

class DeleteCustomModelRequestRequestTypeDef(BaseModel):
    modelIdentifier: str

class DeleteGuardrailRequestRequestTypeDef(BaseModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None

class DeleteProvisionedModelThroughputRequestRequestTypeDef(BaseModel):
    provisionedModelId: str

class EvaluationBedrockModelTypeDef(BaseModel):
    modelIdentifier: str
    inferenceParams: str

class EvaluationDatasetLocationTypeDef(BaseModel):
    s3Uri: Optional[str] = None

class EvaluationSummaryTypeDef(BaseModel):
    jobArn: str
    jobName: str
    status: EvaluationJobStatusType
    creationTime: datetime
    jobType: EvaluationJobTypeType
    evaluationTaskTypes: List[EvaluationTaskTypeType]
    modelIdentifiers: List[str]

class FoundationModelLifecycleTypeDef(BaseModel):
    status: FoundationModelLifecycleStatusType

class GetCustomModelRequestRequestTypeDef(BaseModel):
    modelIdentifier: str

class TrainingMetricsTypeDef(BaseModel):
    trainingLoss: Optional[float] = None

class ValidatorMetricTypeDef(BaseModel):
    validationLoss: Optional[float] = None

class GetEvaluationJobRequestRequestTypeDef(BaseModel):
    jobIdentifier: str

class GetFoundationModelRequestRequestTypeDef(BaseModel):
    modelIdentifier: str

class GetGuardrailRequestRequestTypeDef(BaseModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None

class GetModelCustomizationJobRequestRequestTypeDef(BaseModel):
    jobIdentifier: str

class VpcConfigOutputTypeDef(BaseModel):
    subnetIds: List[str]
    securityGroupIds: List[str]

class GetProvisionedModelThroughputRequestRequestTypeDef(BaseModel):
    provisionedModelId: str

class GuardrailContentFilterConfigTypeDef(BaseModel):
    type: GuardrailContentFilterTypeType
    inputStrength: GuardrailFilterStrengthType
    outputStrength: GuardrailFilterStrengthType

class GuardrailContentFilterTypeDef(BaseModel):
    type: GuardrailContentFilterTypeType
    inputStrength: GuardrailFilterStrengthType
    outputStrength: GuardrailFilterStrengthType

class GuardrailContextualGroundingFilterConfigTypeDef(BaseModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float

class GuardrailContextualGroundingFilterTypeDef(BaseModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float

class GuardrailManagedWordsConfigTypeDef(BaseModel):
    type: Literal["PROFANITY"]

class GuardrailManagedWordsTypeDef(BaseModel):
    type: Literal["PROFANITY"]

class GuardrailPiiEntityConfigTypeDef(BaseModel):
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationActionType

class GuardrailPiiEntityTypeDef(BaseModel):
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationActionType

class GuardrailRegexConfigTypeDef(BaseModel):
    name: str
    pattern: str
    action: GuardrailSensitiveInformationActionType
    description: Optional[str] = None

class GuardrailRegexTypeDef(BaseModel):
    name: str
    pattern: str
    action: GuardrailSensitiveInformationActionType
    description: Optional[str] = None

class GuardrailSummaryTypeDef(BaseModel):
    id: str
    arn: str
    status: GuardrailStatusType
    name: str
    version: str
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None

class GuardrailTopicConfigTypeDef(BaseModel):
    name: str
    definition: str
    type: Literal["DENY"]
    examples: Optional[Sequence[str]] = None

class GuardrailTopicTypeDef(BaseModel):
    name: str
    definition: str
    examples: Optional[List[str]] = None
    type: Optional[Literal["DENY"]] = None

class GuardrailWordConfigTypeDef(BaseModel):
    text: str

class GuardrailWordTypeDef(BaseModel):
    text: str

class HumanEvaluationCustomMetricTypeDef(BaseModel):
    name: str
    ratingMethod: str
    description: Optional[str] = None

class HumanWorkflowConfigTypeDef(BaseModel):
    flowDefinitionArn: str
    instructions: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListFoundationModelsRequestRequestTypeDef(BaseModel):
    byProvider: Optional[str] = None
    byCustomizationType: Optional[ModelCustomizationType] = None
    byOutputModality: Optional[ModelModalityType] = None
    byInferenceType: Optional[InferenceTypeType] = None

class ListGuardrailsRequestRequestTypeDef(BaseModel):
    guardrailIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ModelCustomizationJobSummaryTypeDef(BaseModel):
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

class ProvisionedModelSummaryTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str

class StopEvaluationJobRequestRequestTypeDef(BaseModel):
    jobIdentifier: str

class StopModelCustomizationJobRequestRequestTypeDef(BaseModel):
    jobIdentifier: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateProvisionedModelThroughputRequestRequestTypeDef(BaseModel):
    provisionedModelId: str
    desiredProvisionedModelName: Optional[str] = None
    desiredModelId: Optional[str] = None

class ValidatorTypeDef(BaseModel):
    s3Uri: str

class CloudWatchConfigTypeDef(BaseModel):
    logGroupName: str
    roleArn: str
    largeDataDeliveryS3Config: Optional[S3ConfigTypeDef] = None

class CreateProvisionedModelThroughputRequestRequestTypeDef(BaseModel):
    modelUnits: int
    provisionedModelName: str
    modelId: str
    clientRequestToken: Optional[str] = None
    commitmentDuration: Optional[CommitmentDurationType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]

class CreateEvaluationJobResponseTypeDef(BaseModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGuardrailResponseTypeDef(BaseModel):
    guardrailId: str
    guardrailArn: str
    version: str
    createdAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGuardrailVersionResponseTypeDef(BaseModel):
    guardrailId: str
    version: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelCustomizationJobResponseTypeDef(BaseModel):
    jobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProvisionedModelThroughputResponseTypeDef(BaseModel):
    provisionedModelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetProvisionedModelThroughputResponseTypeDef(BaseModel):
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

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGuardrailResponseTypeDef(BaseModel):
    guardrailId: str
    guardrailArn: str
    version: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomModelsResponseTypeDef(BaseModel):
    nextToken: str
    modelSummaries: List[CustomModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationModelConfigTypeDef(BaseModel):
    bedrockModel: Optional[EvaluationBedrockModelTypeDef] = None

class EvaluationDatasetTypeDef(BaseModel):
    name: str
    datasetLocation: Optional[EvaluationDatasetLocationTypeDef] = None

class ListEvaluationJobsResponseTypeDef(BaseModel):
    nextToken: str
    jobSummaries: List[EvaluationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FoundationModelDetailsTypeDef(BaseModel):
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

class FoundationModelSummaryTypeDef(BaseModel):
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

class GuardrailContentPolicyConfigTypeDef(BaseModel):
    filtersConfig: Sequence[GuardrailContentFilterConfigTypeDef]

class GuardrailContentPolicyTypeDef(BaseModel):
    filters: Optional[List[GuardrailContentFilterTypeDef]] = None

class GuardrailContextualGroundingPolicyConfigTypeDef(BaseModel):
    filtersConfig: Sequence[GuardrailContextualGroundingFilterConfigTypeDef]

class GuardrailContextualGroundingPolicyTypeDef(BaseModel):
    filters: List[GuardrailContextualGroundingFilterTypeDef]

class GuardrailSensitiveInformationPolicyConfigTypeDef(BaseModel):
    piiEntitiesConfig: Optional[Sequence[GuardrailPiiEntityConfigTypeDef]] = None
    regexesConfig: Optional[Sequence[GuardrailRegexConfigTypeDef]] = None

class GuardrailSensitiveInformationPolicyTypeDef(BaseModel):
    piiEntities: Optional[List[GuardrailPiiEntityTypeDef]] = None
    regexes: Optional[List[GuardrailRegexTypeDef]] = None

class ListGuardrailsResponseTypeDef(BaseModel):
    guardrails: List[GuardrailSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GuardrailTopicPolicyConfigTypeDef(BaseModel):
    topicsConfig: Sequence[GuardrailTopicConfigTypeDef]

class GuardrailTopicPolicyTypeDef(BaseModel):
    topics: List[GuardrailTopicTypeDef]

class GuardrailWordPolicyConfigTypeDef(BaseModel):
    wordsConfig: Optional[Sequence[GuardrailWordConfigTypeDef]] = None
    managedWordListsConfig: Optional[Sequence[GuardrailManagedWordsConfigTypeDef]] = None

class GuardrailWordPolicyTypeDef(BaseModel):
    words: Optional[List[GuardrailWordTypeDef]] = None
    managedWordLists: Optional[List[GuardrailManagedWordsTypeDef]] = None

class ListGuardrailsRequestListGuardrailsPaginateTypeDef(BaseModel):
    guardrailIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomModelsRequestListCustomModelsPaginateTypeDef(BaseModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    baseModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomModelsRequestRequestTypeDef(BaseModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    baseModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListEvaluationJobsRequestListEvaluationJobsPaginateTypeDef(BaseModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEvaluationJobsRequestRequestTypeDef(BaseModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef(BaseModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCustomizationJobsRequestRequestTypeDef(BaseModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef(BaseModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisionedModelThroughputsRequestRequestTypeDef(BaseModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListModelCustomizationJobsResponseTypeDef(BaseModel):
    nextToken: str
    modelCustomizationJobSummaries: List[ModelCustomizationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisionedModelThroughputsResponseTypeDef(BaseModel):
    nextToken: str
    provisionedModelSummaries: List[ProvisionedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ValidationDataConfigOutputTypeDef(BaseModel):
    validators: List[ValidatorTypeDef]

class ValidationDataConfigTypeDef(BaseModel):
    validators: Sequence[ValidatorTypeDef]

class LoggingConfigTypeDef(BaseModel):
    cloudWatchConfig: Optional[CloudWatchConfigTypeDef] = None
    s3Config: Optional[S3ConfigTypeDef] = None
    textDataDeliveryEnabled: Optional[bool] = None
    imageDataDeliveryEnabled: Optional[bool] = None
    embeddingDataDeliveryEnabled: Optional[bool] = None

class EvaluationInferenceConfigOutputTypeDef(BaseModel):
    models: Optional[List[EvaluationModelConfigTypeDef]] = None

class EvaluationInferenceConfigTypeDef(BaseModel):
    models: Optional[Sequence[EvaluationModelConfigTypeDef]] = None

class EvaluationDatasetMetricConfigOutputTypeDef(BaseModel):
    taskType: EvaluationTaskTypeType
    dataset: EvaluationDatasetTypeDef
    metricNames: List[str]

class EvaluationDatasetMetricConfigTypeDef(BaseModel):
    taskType: EvaluationTaskTypeType
    dataset: EvaluationDatasetTypeDef
    metricNames: Sequence[str]

class GetFoundationModelResponseTypeDef(BaseModel):
    modelDetails: FoundationModelDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListFoundationModelsResponseTypeDef(BaseModel):
    modelSummaries: List[FoundationModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGuardrailRequestRequestTypeDef(BaseModel):
    name: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    description: Optional[str] = None
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfigTypeDef] = None
    contentPolicyConfig: Optional[GuardrailContentPolicyConfigTypeDef] = None
    wordPolicyConfig: Optional[GuardrailWordPolicyConfigTypeDef] = None
    sensitiveInformationPolicyConfig: Optional[       GuardrailSensitiveInformationPolicyConfigTypeDef     ] = None
    contextualGroundingPolicyConfig: Optional[       GuardrailContextualGroundingPolicyConfigTypeDef     ] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientRequestToken: Optional[str] = None

class UpdateGuardrailRequestRequestTypeDef(BaseModel):
    guardrailIdentifier: str
    name: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    description: Optional[str] = None
    topicPolicyConfig: Optional[GuardrailTopicPolicyConfigTypeDef] = None
    contentPolicyConfig: Optional[GuardrailContentPolicyConfigTypeDef] = None
    wordPolicyConfig: Optional[GuardrailWordPolicyConfigTypeDef] = None
    sensitiveInformationPolicyConfig: Optional[       GuardrailSensitiveInformationPolicyConfigTypeDef     ] = None
    contextualGroundingPolicyConfig: Optional[       GuardrailContextualGroundingPolicyConfigTypeDef     ] = None
    kmsKeyId: Optional[str] = None

class GetGuardrailResponseTypeDef(BaseModel):
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

class GetCustomModelResponseTypeDef(BaseModel):
    modelArn: str
    modelName: str
    jobName: str
    jobArn: str
    baseModelArn: str
    customizationType: CustomizationTypeType
    modelKmsKeyArn: str
    hyperParameters: Dict[str, str]
    trainingDataConfig: TrainingDataConfigTypeDef
    validationDataConfig: ValidationDataConfigOutputTypeDef
    outputDataConfig: OutputDataConfigTypeDef
    trainingMetrics: TrainingMetricsTypeDef
    validationMetrics: List[ValidatorMetricTypeDef]
    creationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelCustomizationJobResponseTypeDef(BaseModel):
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
    trainingDataConfig: TrainingDataConfigTypeDef
    validationDataConfig: ValidationDataConfigOutputTypeDef
    outputDataConfig: OutputDataConfigTypeDef
    customizationType: CustomizationTypeType
    outputModelKmsKeyArn: str
    trainingMetrics: TrainingMetricsTypeDef
    validationMetrics: List[ValidatorMetricTypeDef]
    vpcConfig: VpcConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelCustomizationJobRequestRequestTypeDef(BaseModel):
    jobName: str
    customModelName: str
    roleArn: str
    baseModelIdentifier: str
    trainingDataConfig: TrainingDataConfigTypeDef
    outputDataConfig: OutputDataConfigTypeDef
    hyperParameters: Mapping[str, str]
    clientRequestToken: Optional[str] = None
    customizationType: Optional[CustomizationTypeType] = None
    customModelKmsKeyId: Optional[str] = None
    jobTags: Optional[Sequence[TagTypeDef]] = None
    customModelTags: Optional[Sequence[TagTypeDef]] = None
    validationDataConfig: Optional[ValidationDataConfigTypeDef] = None
    vpcConfig: Optional[VpcConfigTypeDef] = None

class GetModelInvocationLoggingConfigurationResponseTypeDef(BaseModel):
    loggingConfig: LoggingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutModelInvocationLoggingConfigurationRequestRequestTypeDef(BaseModel):
    loggingConfig: LoggingConfigTypeDef

class AutomatedEvaluationConfigOutputTypeDef(BaseModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutputTypeDef]

class HumanEvaluationConfigOutputTypeDef(BaseModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutputTypeDef]
    humanWorkflowConfig: Optional[HumanWorkflowConfigTypeDef] = None
    customMetrics: Optional[List[HumanEvaluationCustomMetricTypeDef]] = None

class AutomatedEvaluationConfigTypeDef(BaseModel):
    datasetMetricConfigs: Sequence[EvaluationDatasetMetricConfigTypeDef]

class HumanEvaluationConfigTypeDef(BaseModel):
    datasetMetricConfigs: Sequence[EvaluationDatasetMetricConfigTypeDef]
    humanWorkflowConfig: Optional[HumanWorkflowConfigTypeDef] = None
    customMetrics: Optional[Sequence[HumanEvaluationCustomMetricTypeDef]] = None

class EvaluationConfigOutputTypeDef(BaseModel):
    automated: Optional[AutomatedEvaluationConfigOutputTypeDef] = None
    human: Optional[HumanEvaluationConfigOutputTypeDef] = None

class EvaluationConfigTypeDef(BaseModel):
    automated: Optional[AutomatedEvaluationConfigTypeDef] = None
    human: Optional[HumanEvaluationConfigTypeDef] = None

class GetEvaluationJobResponseTypeDef(BaseModel):
    jobName: str
    status: EvaluationJobStatusType
    jobArn: str
    jobDescription: str
    roleArn: str
    customerEncryptionKeyId: str
    jobType: EvaluationJobTypeType
    evaluationConfig: EvaluationConfigOutputTypeDef
    inferenceConfig: EvaluationInferenceConfigOutputTypeDef
    outputDataConfig: EvaluationOutputDataConfigTypeDef
    creationTime: datetime
    lastModifiedTime: datetime
    failureMessages: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEvaluationJobRequestRequestTypeDef(BaseModel):
    jobName: str
    roleArn: str
    evaluationConfig: EvaluationConfigTypeDef
    inferenceConfig: EvaluationInferenceConfigTypeDef
    outputDataConfig: EvaluationOutputDataConfigTypeDef
    jobDescription: Optional[str] = None
    clientRequestToken: Optional[str] = None
    customerEncryptionKeyId: Optional[str] = None
    jobTags: Optional[Sequence[TagTypeDef]] = None

