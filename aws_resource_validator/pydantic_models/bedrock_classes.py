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
from aws_resource_validator.pydantic_models.bedrock_constants import *

class S3ConfigTypeDef(BaseValidatorModel):
    bucketName: str
    keyPrefix: Optional[str] = None

class EvaluationOutputDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateGuardrailVersionRequestRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    description: Optional[str] = None
    clientRequestToken: Optional[str] = None

class OutputDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str

class TrainingDataConfigTypeDef(BaseValidatorModel):
    s3Uri: str

class VpcConfigTypeDef(BaseValidatorModel):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]

class CustomModelSummaryTypeDef(BaseValidatorModel):
    modelArn: str
    modelName: str
    creationTime: datetime
    BaseValidatorModelArn: str
    BaseValidatorModelName: str
    customizationType: Optional[CustomizationTypeType] = None

class DeleteCustomModelRequestRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str

class DeleteGuardrailRequestRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None

class DeleteProvisionedModelThroughputRequestRequestTypeDef(BaseValidatorModel):
    provisionedModelId: str

class EvaluationBedrockModelTypeDef(BaseValidatorModel):
    modelIdentifier: str
    inferenceParams: str

class EvaluationDatasetLocationTypeDef(BaseValidatorModel):
    s3Uri: Optional[str] = None

class EvaluationSummaryTypeDef(BaseValidatorModel):
    jobArn: str
    jobName: str
    status: EvaluationJobStatusType
    creationTime: datetime
    jobType: EvaluationJobTypeType
    evaluationTaskTypes: List[EvaluationTaskTypeType]
    modelIdentifiers: List[str]

class FoundationModelLifecycleTypeDef(BaseValidatorModel):
    status: FoundationModelLifecycleStatusType

class GetCustomModelRequestRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str

class TrainingMetricsTypeDef(BaseValidatorModel):
    trainingLoss: Optional[float] = None

class ValidatorMetricTypeDef(BaseValidatorModel):
    validationLoss: Optional[float] = None

class GetEvaluationJobRequestRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str

class GetFoundationModelRequestRequestTypeDef(BaseValidatorModel):
    modelIdentifier: str

class GetGuardrailRequestRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: str
    guardrailVersion: Optional[str] = None

class GetModelCustomizationJobRequestRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str

class VpcConfigOutputTypeDef(BaseValidatorModel):
    subnetIds: List[str]
    securityGroupIds: List[str]

class GetProvisionedModelThroughputRequestRequestTypeDef(BaseValidatorModel):
    provisionedModelId: str

class GuardrailContentFilterConfigTypeDef(BaseValidatorModel):
    type: GuardrailContentFilterTypeType
    inputStrength: GuardrailFilterStrengthType
    outputStrength: GuardrailFilterStrengthType

class GuardrailContentFilterTypeDef(BaseValidatorModel):
    type: GuardrailContentFilterTypeType
    inputStrength: GuardrailFilterStrengthType
    outputStrength: GuardrailFilterStrengthType

class GuardrailContextualGroundingFilterConfigTypeDef(BaseValidatorModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float

class GuardrailContextualGroundingFilterTypeDef(BaseValidatorModel):
    type: GuardrailContextualGroundingFilterTypeType
    threshold: float

class GuardrailManagedWordsConfigTypeDef(BaseValidatorModel):
    type: Literal["PROFANITY"]

class GuardrailManagedWordsTypeDef(BaseValidatorModel):
    type: Literal["PROFANITY"]

class GuardrailPiiEntityConfigTypeDef(BaseValidatorModel):
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationActionType

class GuardrailPiiEntityTypeDef(BaseValidatorModel):
    type: GuardrailPiiEntityTypeType
    action: GuardrailSensitiveInformationActionType

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

class GuardrailSummaryTypeDef(BaseValidatorModel):
    id: str
    arn: str
    status: GuardrailStatusType
    name: str
    version: str
    createdAt: datetime
    updatedAt: datetime
    description: Optional[str] = None

class GuardrailTopicConfigTypeDef(BaseValidatorModel):
    name: str
    definition: str
    type: Literal["DENY"]
    examples: Optional[Sequence[str]] = None

class GuardrailTopicTypeDef(BaseValidatorModel):
    name: str
    definition: str
    examples: Optional[List[str]] = None
    type: Optional[Literal["DENY"]] = None

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

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListFoundationModelsRequestRequestTypeDef(BaseValidatorModel):
    byProvider: Optional[str] = None
    byCustomizationType: Optional[ModelCustomizationType] = None
    byOutputModality: Optional[ModelModalityType] = None
    byInferenceType: Optional[InferenceTypeType] = None

class ListGuardrailsRequestRequestTypeDef(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ModelCustomizationJobSummaryTypeDef(BaseValidatorModel):
    jobArn: str
    BaseValidatorModelArn: str
    jobName: str
    status: ModelCustomizationJobStatusType
    creationTime: datetime
    lastModifiedTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    customModelArn: Optional[str] = None
    customModelName: Optional[str] = None
    customizationType: Optional[CustomizationTypeType] = None

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

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str

class StopEvaluationJobRequestRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str

class StopModelCustomizationJobRequestRequestTypeDef(BaseValidatorModel):
    jobIdentifier: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateProvisionedModelThroughputRequestRequestTypeDef(BaseValidatorModel):
    provisionedModelId: str
    desiredProvisionedModelName: Optional[str] = None
    desiredModelId: Optional[str] = None

class ValidatorTypeDef(BaseValidatorModel):
    s3Uri: str

class CloudWatchConfigTypeDef(BaseValidatorModel):
    logGroupName: str
    roleArn: str
    largeDataDeliveryS3Config: Optional[S3ConfigTypeDef] = None

class CreateProvisionedModelThroughputRequestRequestTypeDef(BaseValidatorModel):
    modelUnits: int
    provisionedModelName: str
    modelId: str
    clientRequestToken: Optional[str] = None
    commitmentDuration: Optional[CommitmentDurationType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]

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

class CreateModelCustomizationJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
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

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGuardrailResponseTypeDef(BaseValidatorModel):
    guardrailId: str
    guardrailArn: str
    version: str
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomModelsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    modelSummaries: List[CustomModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationModelConfigTypeDef(BaseValidatorModel):
    bedrockModel: Optional[EvaluationBedrockModelTypeDef] = None

class EvaluationDatasetTypeDef(BaseValidatorModel):
    name: str
    datasetLocation: Optional[EvaluationDatasetLocationTypeDef] = None

class ListEvaluationJobsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    jobSummaries: List[EvaluationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class GuardrailContentPolicyConfigTypeDef(BaseValidatorModel):
    filtersConfig: Sequence[GuardrailContentFilterConfigTypeDef]

class GuardrailContentPolicyTypeDef(BaseValidatorModel):
    filters: Optional[List[GuardrailContentFilterTypeDef]] = None

class GuardrailContextualGroundingPolicyConfigTypeDef(BaseValidatorModel):
    filtersConfig: Sequence[GuardrailContextualGroundingFilterConfigTypeDef]

class GuardrailContextualGroundingPolicyTypeDef(BaseValidatorModel):
    filters: List[GuardrailContextualGroundingFilterTypeDef]

class GuardrailSensitiveInformationPolicyConfigTypeDef(BaseValidatorModel):
    piiEntitiesConfig: Optional[Sequence[GuardrailPiiEntityConfigTypeDef]] = None
    regexesConfig: Optional[Sequence[GuardrailRegexConfigTypeDef]] = None

class GuardrailSensitiveInformationPolicyTypeDef(BaseValidatorModel):
    piiEntities: Optional[List[GuardrailPiiEntityTypeDef]] = None
    regexes: Optional[List[GuardrailRegexTypeDef]] = None

class ListGuardrailsResponseTypeDef(BaseValidatorModel):
    guardrails: List[GuardrailSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GuardrailTopicPolicyConfigTypeDef(BaseValidatorModel):
    topicsConfig: Sequence[GuardrailTopicConfigTypeDef]

class GuardrailTopicPolicyTypeDef(BaseValidatorModel):
    topics: List[GuardrailTopicTypeDef]

class GuardrailWordPolicyConfigTypeDef(BaseValidatorModel):
    wordsConfig: Optional[Sequence[GuardrailWordConfigTypeDef]] = None
    managedWordListsConfig: Optional[Sequence[GuardrailManagedWordsConfigTypeDef]] = None

class GuardrailWordPolicyTypeDef(BaseValidatorModel):
    words: Optional[List[GuardrailWordTypeDef]] = None
    managedWordLists: Optional[List[GuardrailManagedWordsTypeDef]] = None

class ListGuardrailsRequestListGuardrailsPaginateTypeDef(BaseValidatorModel):
    guardrailIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomModelsRequestListCustomModelsPaginateTypeDef(BaseValidatorModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    BaseValidatorModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCustomModelsRequestRequestTypeDef(BaseValidatorModel):
    creationTimeBefore: Optional[TimestampTypeDef] = None
    creationTimeAfter: Optional[TimestampTypeDef] = None
    nameContains: Optional[str] = None
    BaseValidatorModelArnEquals: Optional[str] = None
    foundationModelArnEquals: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListEvaluationJobsRequestListEvaluationJobsPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEvaluationJobsRequestRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[EvaluationJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListModelCustomizationJobsRequestListModelCustomizationJobsPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListModelCustomizationJobsRequestRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[FineTuningJobStatusType] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListProvisionedModelThroughputsRequestListProvisionedModelThroughputsPaginateTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListProvisionedModelThroughputsRequestRequestTypeDef(BaseValidatorModel):
    creationTimeAfter: Optional[TimestampTypeDef] = None
    creationTimeBefore: Optional[TimestampTypeDef] = None
    statusEquals: Optional[ProvisionedModelStatusType] = None
    modelArnEquals: Optional[str] = None
    nameContains: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    sortBy: Optional[Literal["CreationTime"]] = None
    sortOrder: Optional[SortOrderType] = None

class ListModelCustomizationJobsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    modelCustomizationJobSummaries: List[ModelCustomizationJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListProvisionedModelThroughputsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    provisionedModelSummaries: List[ProvisionedModelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ValidationDataConfigOutputTypeDef(BaseValidatorModel):
    validators: List[ValidatorTypeDef]

class ValidationDataConfigTypeDef(BaseValidatorModel):
    validators: Sequence[ValidatorTypeDef]

class LoggingConfigTypeDef(BaseValidatorModel):
    cloudWatchConfig: Optional[CloudWatchConfigTypeDef] = None
    s3Config: Optional[S3ConfigTypeDef] = None
    textDataDeliveryEnabled: Optional[bool] = None
    imageDataDeliveryEnabled: Optional[bool] = None
    embeddingDataDeliveryEnabled: Optional[bool] = None

class EvaluationInferenceConfigOutputTypeDef(BaseValidatorModel):
    models: Optional[List[EvaluationModelConfigTypeDef]] = None

class EvaluationInferenceConfigTypeDef(BaseValidatorModel):
    models: Optional[Sequence[EvaluationModelConfigTypeDef]] = None

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

class CreateGuardrailRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateGuardrailRequestRequestTypeDef(BaseValidatorModel):
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

class GetCustomModelResponseTypeDef(BaseValidatorModel):
    modelArn: str
    modelName: str
    jobName: str
    jobArn: str
    BaseValidatorModelArn: str
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
    BaseValidatorModelArn: str
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

class CreateModelCustomizationJobRequestRequestTypeDef(BaseValidatorModel):
    jobName: str
    customModelName: str
    roleArn: str
    BaseValidatorModelIdentifier: str
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

class GetModelInvocationLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    loggingConfig: LoggingConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutModelInvocationLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    loggingConfig: LoggingConfigTypeDef

class AutomatedEvaluationConfigOutputTypeDef(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutputTypeDef]

class HumanEvaluationConfigOutputTypeDef(BaseValidatorModel):
    datasetMetricConfigs: List[EvaluationDatasetMetricConfigOutputTypeDef]
    humanWorkflowConfig: Optional[HumanWorkflowConfigTypeDef] = None
    customMetrics: Optional[List[HumanEvaluationCustomMetricTypeDef]] = None

class AutomatedEvaluationConfigTypeDef(BaseValidatorModel):
    datasetMetricConfigs: Sequence[EvaluationDatasetMetricConfigTypeDef]

class HumanEvaluationConfigTypeDef(BaseValidatorModel):
    datasetMetricConfigs: Sequence[EvaluationDatasetMetricConfigTypeDef]
    humanWorkflowConfig: Optional[HumanWorkflowConfigTypeDef] = None
    customMetrics: Optional[Sequence[HumanEvaluationCustomMetricTypeDef]] = None

class EvaluationConfigOutputTypeDef(BaseValidatorModel):
    automated: Optional[AutomatedEvaluationConfigOutputTypeDef] = None
    human: Optional[HumanEvaluationConfigOutputTypeDef] = None

class EvaluationConfigTypeDef(BaseValidatorModel):
    automated: Optional[AutomatedEvaluationConfigTypeDef] = None
    human: Optional[HumanEvaluationConfigTypeDef] = None

class GetEvaluationJobResponseTypeDef(BaseValidatorModel):
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

class CreateEvaluationJobRequestRequestTypeDef(BaseValidatorModel):
    jobName: str
    roleArn: str
    evaluationConfig: EvaluationConfigTypeDef
    inferenceConfig: EvaluationInferenceConfigTypeDef
    outputDataConfig: EvaluationOutputDataConfigTypeDef
    jobDescription: Optional[str] = None
    clientRequestToken: Optional[str] = None
    customerEncryptionKeyId: Optional[str] = None
    jobTags: Optional[Sequence[TagTypeDef]] = None

