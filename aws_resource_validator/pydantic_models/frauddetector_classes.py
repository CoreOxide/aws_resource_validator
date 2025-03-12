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
from aws_resource_validator.pydantic_models.frauddetector_constants import *

class ATIMetricDataPointTypeDef(BaseValidatorModel):
    cr: Optional[float] = None
    adr: Optional[float] = None
    threshold: Optional[float] = None
    atodr: Optional[float] = None


class ATIModelPerformanceTypeDef(BaseValidatorModel):
    asi: Optional[float] = None


class AggregatedLogOddsMetricTypeDef(BaseValidatorModel):
    variableNames: List[str]
    aggregatedVariablesImportance: float


class AggregatedVariablesImpactExplanationTypeDef(BaseValidatorModel):
    eventVariableNames: Optional[List[str]] = None
    relativeImpact: Optional[str] = None
    logOddsImpact: Optional[float] = None


class AllowDenyListTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    variableType: Optional[str] = None
    createdTime: Optional[str] = None
    updatedTime: Optional[str] = None
    arn: Optional[str] = None


class BatchCreateVariableErrorTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class VariableEntryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[str] = None
    dataSource: Optional[str] = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetVariableErrorTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None


class BatchGetVariableRequestTypeDef(BaseValidatorModel):
    names: Sequence[str]


class VariableTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    dataSource: Optional[DataSourceType] = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class BatchImportTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    status: Optional[AsyncJobStatusType] = None
    failureReason: Optional[str] = None
    startTime: Optional[str] = None
    completionTime: Optional[str] = None
    inputPath: Optional[str] = None
    outputPath: Optional[str] = None
    eventTypeName: Optional[str] = None
    iamRoleArn: Optional[str] = None
    arn: Optional[str] = None
    processedRecordsCount: Optional[int] = None
    failedRecordsCount: Optional[int] = None
    totalRecordsCount: Optional[int] = None


class BatchPredictionTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    status: Optional[AsyncJobStatusType] = None
    failureReason: Optional[str] = None
    startTime: Optional[str] = None
    completionTime: Optional[str] = None
    lastHeartbeatTime: Optional[str] = None
    inputPath: Optional[str] = None
    outputPath: Optional[str] = None
    eventTypeName: Optional[str] = None
    detectorName: Optional[str] = None
    detectorVersion: Optional[str] = None
    iamRoleArn: Optional[str] = None
    arn: Optional[str] = None
    processedRecordsCount: Optional[int] = None
    totalRecordsCount: Optional[int] = None


class CancelBatchImportJobRequestTypeDef(BaseValidatorModel):
    jobId: str


class CancelBatchPredictionJobRequestTypeDef(BaseValidatorModel):
    jobId: str


class ModelVersionTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    arn: Optional[str] = None


class RuleTypeDef(BaseValidatorModel):
    detectorId: str
    ruleId: str
    ruleVersion: str


class ExternalEventsDetailTypeDef(BaseValidatorModel):
    dataLocation: str
    dataAccessRoleArn: str


class DeleteBatchImportJobRequestTypeDef(BaseValidatorModel):
    jobId: str


class DeleteBatchPredictionJobRequestTypeDef(BaseValidatorModel):
    jobId: str


class DeleteDetectorRequestTypeDef(BaseValidatorModel):
    detectorId: str


class DeleteDetectorVersionRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str


class DeleteEntityTypeRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteEventRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    deleteAuditHistory: Optional[bool] = None


class DeleteEventTypeRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteEventsByEventTypeRequestTypeDef(BaseValidatorModel):
    eventTypeName: str


class DeleteExternalModelRequestTypeDef(BaseValidatorModel):
    modelEndpoint: str


class DeleteLabelRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteListRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteModelRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType


class DeleteModelVersionRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str


class DeleteOutcomeRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteVariableRequestTypeDef(BaseValidatorModel):
    name: str


class DescribeDetectorRequestTypeDef(BaseValidatorModel):
    detectorId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DetectorVersionSummaryTypeDef(BaseValidatorModel):
    detectorVersionId: Optional[str] = None
    status: Optional[DetectorVersionStatusType] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None


class DescribeModelVersionsRequestTypeDef(BaseValidatorModel):
    modelId: Optional[str] = None
    modelVersionNumber: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DetectorTypeDef(BaseValidatorModel):
    detectorId: Optional[str] = None
    description: Optional[str] = None
    eventTypeName: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class EntityTypeDef(BaseValidatorModel):
    entityType: str
    entityId: str


class EntityTypeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class EvaluatedExternalModelTypeDef(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    useEventVariables: Optional[bool] = None
    inputVariables: Optional[Dict[str, str]] = None
    outputVariables: Optional[Dict[str, str]] = None


class EvaluatedRuleTypeDef(BaseValidatorModel):
    ruleId: Optional[str] = None
    ruleVersion: Optional[str] = None
    expression: Optional[str] = None
    expressionWithValues: Optional[str] = None
    outcomes: Optional[List[str]] = None
    evaluated: Optional[bool] = None
    matched: Optional[bool] = None


class EventOrchestrationTypeDef(BaseValidatorModel):
    eventBridgeEnabled: bool


class EventPredictionSummaryTypeDef(BaseValidatorModel):
    eventId: Optional[str] = None
    eventTypeName: Optional[str] = None
    eventTimestamp: Optional[str] = None
    predictionTimestamp: Optional[str] = None
    detectorId: Optional[str] = None
    detectorVersionId: Optional[str] = None


class IngestedEventStatisticsTypeDef(BaseValidatorModel):
    numberOfEvents: Optional[int] = None
    eventDataSizeInBytes: Optional[int] = None
    leastRecentEvent: Optional[str] = None
    mostRecentEvent: Optional[str] = None
    lastUpdatedTime: Optional[str] = None


class EventVariableSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None
    source: Optional[str] = None


class ExternalModelSummaryTypeDef(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    modelSource: Optional[Literal["SAGEMAKER"]] = None


class FilterConditionTypeDef(BaseValidatorModel):
    value: Optional[str] = None


class GetBatchImportJobsRequestTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetBatchPredictionJobsRequestTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetDeleteEventsByEventTypeStatusRequestTypeDef(BaseValidatorModel):
    eventTypeName: str


class GetDetectorVersionRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str


class GetDetectorsRequestTypeDef(BaseValidatorModel):
    detectorId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEntityTypesRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetEventPredictionMetadataRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    detectorId: str
    detectorVersionId: str
    predictionTimestamp: str


class RuleResultTypeDef(BaseValidatorModel):
    ruleId: Optional[str] = None
    outcomes: Optional[List[str]] = None


class GetEventRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str


class GetEventTypesRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetExternalModelsRequestTypeDef(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class KMSKeyTypeDef(BaseValidatorModel):
    kmsEncryptionKeyArn: Optional[str] = None


class GetLabelsRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LabelTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class GetListElementsRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetListsMetadataRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetModelVersionRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str


class GetModelsRequestTypeDef(BaseValidatorModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ModelTypeDef(BaseValidatorModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    description: Optional[str] = None
    eventTypeName: Optional[str] = None
    createdTime: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    arn: Optional[str] = None


class GetOutcomesRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class OutcomeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class GetRulesRequestTypeDef(BaseValidatorModel):
    detectorId: str
    ruleId: Optional[str] = None
    ruleVersion: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RuleDetailTypeDef(BaseValidatorModel):
    ruleId: Optional[str] = None
    description: Optional[str] = None
    detectorId: Optional[str] = None
    ruleVersion: Optional[str] = None
    expression: Optional[str] = None
    language: Optional[Literal["DETECTORPL"]] = None
    outcomes: Optional[List[str]] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class GetVariablesRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class IngestedEventsTimeWindowTypeDef(BaseValidatorModel):
    startTime: str
    endTime: str


class LabelSchemaOutputTypeDef(BaseValidatorModel):
    labelMapper: Optional[Dict[str, List[str]]] = None
    unlabeledEventsTreatment: Optional[UnlabeledEventsTreatmentType] = None


class LabelSchemaTypeDef(BaseValidatorModel):
    labelMapper: Optional[Mapping[str, Sequence[str]]] = None
    unlabeledEventsTreatment: Optional[UnlabeledEventsTreatmentType] = None


class PredictionTimeRangeTypeDef(BaseValidatorModel):
    startTime: str
    endTime: str


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LogOddsMetricTypeDef(BaseValidatorModel):
    variableName: str
    variableType: str
    variableImportance: float


class MetricDataPointTypeDef(BaseValidatorModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None


class OFIMetricDataPointTypeDef(BaseValidatorModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None


class UncertaintyRangeTypeDef(BaseValidatorModel):
    lowerBoundValue: float
    upperBoundValue: float


class VariableImpactExplanationTypeDef(BaseValidatorModel):
    eventVariableName: Optional[str] = None
    relativeImpact: Optional[str] = None
    logOddsImpact: Optional[float] = None


class PutKMSEncryptionKeyRequestTypeDef(BaseValidatorModel):
    kmsEncryptionKeyArn: str


class TFIMetricDataPointTypeDef(BaseValidatorModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class UpdateDetectorVersionMetadataRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    description: str


class UpdateDetectorVersionStatusRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatusType


class UpdateEventLabelRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    assignedLabel: str
    labelTimestamp: str


class UpdateListRequestTypeDef(BaseValidatorModel):
    name: str
    elements: Optional[Sequence[str]] = None
    description: Optional[str] = None
    updateMode: Optional[ListUpdateModeType] = None
    variableType: Optional[str] = None


class UpdateModelRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    description: Optional[str] = None


class UpdateModelVersionStatusRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: ModelVersionStatusType


class UpdateVariableRequestTypeDef(BaseValidatorModel):
    name: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None


class ATITrainingMetricsValueTypeDef(BaseValidatorModel):
    metricDataPoints: Optional[List[ATIMetricDataPointTypeDef]] = None
    modelPerformance: Optional[ATIModelPerformanceTypeDef] = None


class AggregatedVariablesImportanceMetricsTypeDef(BaseValidatorModel):
    logOddsMetrics: Optional[List[AggregatedLogOddsMetricTypeDef]] = None


class CreateBatchImportJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    iamRoleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateBatchPredictionJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    detectorName: str
    iamRoleArn: str
    detectorVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateListRequestTypeDef(BaseValidatorModel):
    name: str
    elements: Optional[Sequence[str]] = None
    variableType: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateModelRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateRuleRequestTypeDef(BaseValidatorModel):
    ruleId: str
    detectorId: str
    expression: str
    language: Literal["DETECTORPL"]
    outcomes: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateVariableRequestTypeDef(BaseValidatorModel):
    name: str
    dataType: DataTypeType
    dataSource: DataSourceType
    defaultValue: str
    description: Optional[str] = None
    variableType: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class PutDetectorRequestTypeDef(BaseValidatorModel):
    detectorId: str
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class PutEntityTypeRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class PutLabelRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class PutOutcomeRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]


class BatchCreateVariableRequestTypeDef(BaseValidatorModel):
    variableEntries: Sequence[VariableEntryTypeDef]
    tags: Optional[Sequence[TagTypeDef]] = None


class BatchCreateVariableResultTypeDef(BaseValidatorModel):
    errors: List[BatchCreateVariableErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDetectorVersionResultTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateModelVersionResultTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEventsByEventTypeResultTypeDef(BaseValidatorModel):
    eventTypeName: str
    eventsDeletionStatus: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetDeleteEventsByEventTypeStatusResultTypeDef(BaseValidatorModel):
    eventTypeName: str
    eventsDeletionStatus: AsyncJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetListElementsResultTypeDef(BaseValidatorModel):
    elements: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetListsMetadataResultTypeDef(BaseValidatorModel):
    lists: List[AllowDenyListTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateModelVersionResultTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetVariableResultTypeDef(BaseValidatorModel):
    variables: List[VariableTypeDef]
    errors: List[BatchGetVariableErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetVariablesResultTypeDef(BaseValidatorModel):
    variables: List[VariableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetBatchImportJobsResultTypeDef(BaseValidatorModel):
    batchImports: List[BatchImportTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetBatchPredictionJobsResultTypeDef(BaseValidatorModel):
    batchPredictions: List[BatchPredictionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class ModelEndpointDataBlobTypeDef(BaseValidatorModel):
    byteBuffer: Optional[BlobTypeDef] = None
    contentType: Optional[str] = None


class ModelScoresTypeDef(BaseValidatorModel):
    modelVersion: Optional[ModelVersionTypeDef] = None
    scores: Optional[Dict[str, float]] = None


class CreateDetectorVersionRequestTypeDef(BaseValidatorModel):
    detectorId: str
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    externalModelEndpoints: Optional[Sequence[str]] = None
    modelVersions: Optional[Sequence[ModelVersionTypeDef]] = None
    ruleExecutionMode: Optional[RuleExecutionModeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreateRuleResultTypeDef(BaseValidatorModel):
    rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRuleRequestTypeDef(BaseValidatorModel):
    rule: RuleTypeDef


class GetDetectorVersionResultTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    description: str
    externalModelEndpoints: List[str]
    modelVersions: List[ModelVersionTypeDef]
    rules: List[RuleTypeDef]
    status: DetectorVersionStatusType
    lastUpdatedTime: str
    createdTime: str
    ruleExecutionMode: RuleExecutionModeType
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDetectorVersionRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    externalModelEndpoints: Sequence[str]
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    modelVersions: Optional[Sequence[ModelVersionTypeDef]] = None
    ruleExecutionMode: Optional[RuleExecutionModeType] = None


class UpdateRuleMetadataRequestTypeDef(BaseValidatorModel):
    rule: RuleTypeDef
    description: str


class UpdateRuleVersionRequestTypeDef(BaseValidatorModel):
    rule: RuleTypeDef
    expression: str
    language: Literal["DETECTORPL"]
    outcomes: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateRuleVersionResultTypeDef(BaseValidatorModel):
    rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FileValidationMessageTypeDef(BaseValidatorModel):
    pass


class FieldValidationMessageTypeDef(BaseValidatorModel):
    pass


class DataValidationMetricsTypeDef(BaseValidatorModel):
    fileLevelMessages: Optional[List[FileValidationMessageTypeDef]] = None
    fieldLevelMessages: Optional[List[FieldValidationMessageTypeDef]] = None


class DescribeDetectorResultTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionSummaries: List[DetectorVersionSummaryTypeDef]
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetDetectorsResultTypeDef(BaseValidatorModel):
    detectors: List[DetectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EventTypeDef(BaseValidatorModel):
    eventId: Optional[str] = None
    eventTypeName: Optional[str] = None
    eventTimestamp: Optional[str] = None
    eventVariables: Optional[Dict[str, str]] = None
    currentLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None
    entities: Optional[List[EntityTypeDef]] = None


class SendEventRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    eventTimestamp: str
    eventVariables: Mapping[str, str]
    entities: Sequence[EntityTypeDef]
    assignedLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None


class GetEntityTypesResultTypeDef(BaseValidatorModel):
    entityTypes: List[EntityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutEventTypeRequestTypeDef(BaseValidatorModel):
    name: str
    eventVariables: Sequence[str]
    entityTypes: Sequence[str]
    description: Optional[str] = None
    labels: Optional[Sequence[str]] = None
    eventIngestion: Optional[EventIngestionType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    eventOrchestration: Optional[EventOrchestrationTypeDef] = None


class ListEventPredictionsResultTypeDef(BaseValidatorModel):
    eventPredictionSummaries: List[EventPredictionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EventTypeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    eventVariables: Optional[List[str]] = None
    labels: Optional[List[str]] = None
    entityTypes: Optional[List[str]] = None
    eventIngestion: Optional[EventIngestionType] = None
    ingestedEventStatistics: Optional[IngestedEventStatisticsTypeDef] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None
    eventOrchestration: Optional[EventOrchestrationTypeDef] = None


class ExternalModelOutputsTypeDef(BaseValidatorModel):
    externalModel: Optional[ExternalModelSummaryTypeDef] = None
    outputs: Optional[Dict[str, str]] = None


class ModelOutputConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class ModelInputConfigurationTypeDef(BaseValidatorModel):
    pass


class ExternalModelTypeDef(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    modelSource: Optional[Literal["SAGEMAKER"]] = None
    invokeModelEndpointRoleArn: Optional[str] = None
    inputConfiguration: Optional[ModelInputConfigurationTypeDef] = None
    outputConfiguration: Optional[ModelOutputConfigurationOutputTypeDef] = None
    modelEndpointStatus: Optional[ModelEndpointStatusType] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class GetKMSEncryptionKeyResultTypeDef(BaseValidatorModel):
    kmsKey: KMSKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLabelsResultTypeDef(BaseValidatorModel):
    labels: List[LabelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetModelsResultTypeDef(BaseValidatorModel):
    models: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetOutcomesResultTypeDef(BaseValidatorModel):
    outcomes: List[OutcomeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetRulesResultTypeDef(BaseValidatorModel):
    ruleDetails: List[RuleDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IngestedEventsDetailTypeDef(BaseValidatorModel):
    ingestedEventsTimeWindow: IngestedEventsTimeWindowTypeDef


class TrainingDataSchemaOutputTypeDef(BaseValidatorModel):
    modelVariables: List[str]
    labelSchema: Optional[LabelSchemaOutputTypeDef] = None


class TrainingDataSchemaTypeDef(BaseValidatorModel):
    modelVariables: Sequence[str]
    labelSchema: Optional[LabelSchemaTypeDef] = None


class ListEventPredictionsRequestTypeDef(BaseValidatorModel):
    eventId: Optional[FilterConditionTypeDef] = None
    eventType: Optional[FilterConditionTypeDef] = None
    detectorId: Optional[FilterConditionTypeDef] = None
    detectorVersionId: Optional[FilterConditionTypeDef] = None
    predictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VariableImportanceMetricsTypeDef(BaseValidatorModel):
    logOddsMetrics: Optional[List[LogOddsMetricTypeDef]] = None


class TrainingMetricsTypeDef(BaseValidatorModel):
    auc: Optional[float] = None
    metricDataPoints: Optional[List[MetricDataPointTypeDef]] = None


class OFIModelPerformanceTypeDef(BaseValidatorModel):
    auc: Optional[float] = None
    uncertaintyRange: Optional[UncertaintyRangeTypeDef] = None


class TFIModelPerformanceTypeDef(BaseValidatorModel):
    auc: Optional[float] = None
    uncertaintyRange: Optional[UncertaintyRangeTypeDef] = None


class PredictionExplanationsTypeDef(BaseValidatorModel):
    variableImpactExplanations: Optional[List[VariableImpactExplanationTypeDef]] = None
    aggregatedVariablesImpactExplanations: Optional[ List[AggregatedVariablesImpactExplanationTypeDef] ] = None


class GetEventPredictionRequestTypeDef(BaseValidatorModel):
    detectorId: str
    eventId: str
    eventTypeName: str
    entities: Sequence[EntityTypeDef]
    eventTimestamp: str
    eventVariables: Mapping[str, str]
    detectorVersionId: Optional[str] = None
    externalModelEndpointDataBlobs: Optional[Mapping[str, ModelEndpointDataBlobTypeDef]] = None


class GetEventResultTypeDef(BaseValidatorModel):
    event: EventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetEventTypesResultTypeDef(BaseValidatorModel):
    eventTypes: List[EventTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetEventPredictionResultTypeDef(BaseValidatorModel):
    modelScores: List[ModelScoresTypeDef]
    ruleResults: List[RuleResultTypeDef]
    externalModelOutputs: List[ExternalModelOutputsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetExternalModelsResultTypeDef(BaseValidatorModel):
    externalModels: List[ExternalModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateModelVersionRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    majorVersionNumber: str
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class GetModelVersionResultTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    trainingDataSource: TrainingDataSourceEnumType
    trainingDataSchema: TrainingDataSchemaOutputTypeDef
    externalEventsDetail: ExternalEventsDetailTypeDef
    ingestedEventsDetail: IngestedEventsDetailTypeDef
    status: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class TrainingResultTypeDef(BaseValidatorModel):
    dataValidationMetrics: Optional[DataValidationMetricsTypeDef] = None
    trainingMetrics: Optional[TrainingMetricsTypeDef] = None
    variableImportanceMetrics: Optional[VariableImportanceMetricsTypeDef] = None


class ModelOutputConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutExternalModelRequestTypeDef(BaseValidatorModel):
    modelEndpoint: str
    modelSource: Literal["SAGEMAKER"]
    invokeModelEndpointRoleArn: str
    inputConfiguration: ModelInputConfigurationTypeDef
    outputConfiguration: ModelOutputConfigurationUnionTypeDef
    modelEndpointStatus: ModelEndpointStatusType
    tags: Optional[Sequence[TagTypeDef]] = None


class OFITrainingMetricsValueTypeDef(BaseValidatorModel):
    metricDataPoints: Optional[List[OFIMetricDataPointTypeDef]] = None
    modelPerformance: Optional[OFIModelPerformanceTypeDef] = None


class TFITrainingMetricsValueTypeDef(BaseValidatorModel):
    metricDataPoints: Optional[List[TFIMetricDataPointTypeDef]] = None
    modelPerformance: Optional[TFIModelPerformanceTypeDef] = None


class ModelVersionEvaluationTypeDef(BaseValidatorModel):
    outputVariableName: Optional[str] = None
    evaluationScore: Optional[str] = None
    predictionExplanations: Optional[PredictionExplanationsTypeDef] = None


class TrainingDataSchemaUnionTypeDef(BaseValidatorModel):
    pass


class CreateModelVersionRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    trainingDataSource: TrainingDataSourceEnumType
    trainingDataSchema: TrainingDataSchemaUnionTypeDef
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class TrainingMetricsV2TypeDef(BaseValidatorModel):
    ofi: Optional[OFITrainingMetricsValueTypeDef] = None
    tfi: Optional[TFITrainingMetricsValueTypeDef] = None
    ati: Optional[ATITrainingMetricsValueTypeDef] = None


class EvaluatedModelVersionTypeDef(BaseValidatorModel):
    modelId: Optional[str] = None
    modelVersion: Optional[str] = None
    modelType: Optional[str] = None
    evaluations: Optional[List[ModelVersionEvaluationTypeDef]] = None


class TrainingResultV2TypeDef(BaseValidatorModel):
    dataValidationMetrics: Optional[DataValidationMetricsTypeDef] = None
    trainingMetricsV2: Optional[TrainingMetricsV2TypeDef] = None
    variableImportanceMetrics: Optional[VariableImportanceMetricsTypeDef] = None
    aggregatedVariablesImportanceMetrics: Optional[AggregatedVariablesImportanceMetricsTypeDef] = None


class GetEventPredictionMetadataResultTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    entityId: str
    entityType: str
    eventTimestamp: str
    detectorId: str
    detectorVersionId: str
    detectorVersionStatus: str
    eventVariables: List[EventVariableSummaryTypeDef]
    rules: List[EvaluatedRuleTypeDef]
    ruleExecutionMode: RuleExecutionModeType
    outcomes: List[str]
    evaluatedModelVersions: List[EvaluatedModelVersionTypeDef]
    evaluatedExternalModels: List[EvaluatedExternalModelTypeDef]
    predictionTimestamp: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModelVersionDetailTypeDef(BaseValidatorModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    modelVersionNumber: Optional[str] = None
    status: Optional[str] = None
    trainingDataSource: Optional[TrainingDataSourceEnumType] = None
    trainingDataSchema: Optional[TrainingDataSchemaOutputTypeDef] = None
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    trainingResult: Optional[TrainingResultTypeDef] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None
    trainingResultV2: Optional[TrainingResultV2TypeDef] = None


class DescribeModelVersionsResultTypeDef(BaseValidatorModel):
    modelVersionDetails: List[ModelVersionDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


