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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchGetVariableErrorTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None

class BatchGetVariableRequestRequestTypeDef(BaseValidatorModel):
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

class CancelBatchImportJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class CancelBatchPredictionJobRequestRequestTypeDef(BaseValidatorModel):
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

class FieldValidationMessageTypeDef(BaseValidatorModel):
    fieldName: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    type: Optional[str] = None

class FileValidationMessageTypeDef(BaseValidatorModel):
    title: Optional[str] = None
    content: Optional[str] = None
    type: Optional[str] = None

class DeleteBatchImportJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class DeleteBatchPredictionJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str

class DeleteDetectorRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str

class DeleteDetectorVersionRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str

class DeleteEntityTypeRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteEventRequestRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    deleteAuditHistory: Optional[bool] = None

class DeleteEventTypeRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteEventsByEventTypeRequestRequestTypeDef(BaseValidatorModel):
    eventTypeName: str

class DeleteExternalModelRequestRequestTypeDef(BaseValidatorModel):
    modelEndpoint: str

class DeleteLabelRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteListRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteModelRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType

class DeleteModelVersionRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str

class DeleteOutcomeRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteVariableRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DescribeDetectorRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DetectorVersionSummaryTypeDef(BaseValidatorModel):
    detectorVersionId: Optional[str] = None
    status: Optional[DetectorVersionStatusType] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None

class DescribeModelVersionsRequestRequestTypeDef(BaseValidatorModel):
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

class ModelInputConfigurationTypeDef(BaseValidatorModel):
    useEventVariables: bool
    eventTypeName: Optional[str] = None
    format: Optional[ModelInputDataFormatType] = None
    jsonInputTemplate: Optional[str] = None
    csvInputTemplate: Optional[str] = None

class ModelOutputConfigurationTypeDef(BaseValidatorModel):
    format: ModelOutputDataFormatType
    jsonKeyToVariableMap: Optional[Dict[str, str]] = None
    csvIndexToVariableMap: Optional[Dict[str, str]] = None

class FilterConditionTypeDef(BaseValidatorModel):
    value: Optional[str] = None

class GetBatchImportJobsRequestRequestTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetBatchPredictionJobsRequestRequestTypeDef(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetDeleteEventsByEventTypeStatusRequestRequestTypeDef(BaseValidatorModel):
    eventTypeName: str

class GetDetectorVersionRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str

class GetDetectorsRequestRequestTypeDef(BaseValidatorModel):
    detectorId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEntityTypesRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEventPredictionMetadataRequestRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    detectorId: str
    detectorVersionId: str
    predictionTimestamp: str

class RuleResultTypeDef(BaseValidatorModel):
    ruleId: Optional[str] = None
    outcomes: Optional[List[str]] = None

class GetEventRequestRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str

class GetEventTypesRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetExternalModelsRequestRequestTypeDef(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class KMSKeyTypeDef(BaseValidatorModel):
    kmsEncryptionKeyArn: Optional[str] = None

class GetLabelsRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LabelTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class GetListElementsRequestRequestTypeDef(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetListsMetadataRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetModelVersionRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str

class GetModelsRequestRequestTypeDef(BaseValidatorModel):
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

class GetOutcomesRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class OutcomeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class GetRulesRequestRequestTypeDef(BaseValidatorModel):
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

class GetVariablesRequestRequestTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class IngestedEventsTimeWindowTypeDef(BaseValidatorModel):
    startTime: str
    endTime: str

class LabelSchemaTypeDef(BaseValidatorModel):
    labelMapper: Optional[Mapping[str, Sequence[str]]] = None
    unlabeledEventsTreatment: Optional[UnlabeledEventsTreatmentType] = None

class PredictionTimeRangeTypeDef(BaseValidatorModel):
    startTime: str
    endTime: str

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class PutKMSEncryptionKeyRequestRequestTypeDef(BaseValidatorModel):
    kmsEncryptionKeyArn: str

class TFIMetricDataPointTypeDef(BaseValidatorModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateDetectorVersionMetadataRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    description: str

class UpdateDetectorVersionStatusRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatusType

class UpdateEventLabelRequestRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    assignedLabel: str
    labelTimestamp: str

class UpdateListRequestRequestTypeDef(BaseValidatorModel):
    name: str
    elements: Optional[Sequence[str]] = None
    description: Optional[str] = None
    updateMode: Optional[ListUpdateModeType] = None
    variableType: Optional[str] = None

class UpdateModelRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    description: Optional[str] = None

class UpdateModelVersionStatusRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: ModelVersionStatusType

class UpdateVariableRequestRequestTypeDef(BaseValidatorModel):
    name: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None

class ATITrainingMetricsValueTypeDef(BaseValidatorModel):
    metricDataPoints: Optional[List[ATIMetricDataPointTypeDef]] = None
    modelPerformance: Optional[ATIModelPerformanceTypeDef] = None

class AggregatedVariablesImportanceMetricsTypeDef(BaseValidatorModel):
    logOddsMetrics: Optional[List[AggregatedLogOddsMetricTypeDef]] = None

class CreateBatchImportJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    iamRoleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateBatchPredictionJobRequestRequestTypeDef(BaseValidatorModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    detectorName: str
    iamRoleArn: str
    detectorVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateListRequestRequestTypeDef(BaseValidatorModel):
    name: str
    elements: Optional[Sequence[str]] = None
    variableType: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRuleRequestRequestTypeDef(BaseValidatorModel):
    ruleId: str
    detectorId: str
    expression: str
    language: Literal["DETECTORPL"]
    outcomes: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateVariableRequestRequestTypeDef(BaseValidatorModel):
    name: str
    dataType: DataTypeType
    dataSource: DataSourceType
    defaultValue: str
    description: Optional[str] = None
    variableType: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutDetectorRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutEntityTypeRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutLabelRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutOutcomeRequestRequestTypeDef(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]

class BatchCreateVariableRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetListsMetadataResultTypeDef(BaseValidatorModel):
    lists: List[AllowDenyListTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBatchImportJobsResultTypeDef(BaseValidatorModel):
    batchImports: List[BatchImportTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBatchPredictionJobsResultTypeDef(BaseValidatorModel):
    batchPredictions: List[BatchPredictionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModelEndpointDataBlobTypeDef(BaseValidatorModel):
    byteBuffer: Optional[BlobTypeDef] = None
    contentType: Optional[str] = None

class ModelScoresTypeDef(BaseValidatorModel):
    modelVersion: Optional[ModelVersionTypeDef] = None
    scores: Optional[Dict[str, float]] = None

class CreateDetectorVersionRequestRequestTypeDef(BaseValidatorModel):
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

class DeleteRuleRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateDetectorVersionRequestRequestTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    externalModelEndpoints: Sequence[str]
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    modelVersions: Optional[Sequence[ModelVersionTypeDef]] = None
    ruleExecutionMode: Optional[RuleExecutionModeType] = None

class UpdateRuleMetadataRequestRequestTypeDef(BaseValidatorModel):
    rule: RuleTypeDef
    description: str

class UpdateRuleVersionRequestRequestTypeDef(BaseValidatorModel):
    rule: RuleTypeDef
    expression: str
    language: Literal["DETECTORPL"]
    outcomes: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRuleVersionResultTypeDef(BaseValidatorModel):
    rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataValidationMetricsTypeDef(BaseValidatorModel):
    fileLevelMessages: Optional[List[FileValidationMessageTypeDef]] = None
    fieldLevelMessages: Optional[List[FieldValidationMessageTypeDef]] = None

class DescribeDetectorResultTypeDef(BaseValidatorModel):
    detectorId: str
    detectorVersionSummaries: List[DetectorVersionSummaryTypeDef]
    nextToken: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDetectorsResultTypeDef(BaseValidatorModel):
    detectors: List[DetectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseValidatorModel):
    eventId: Optional[str] = None
    eventTypeName: Optional[str] = None
    eventTimestamp: Optional[str] = None
    eventVariables: Optional[Dict[str, str]] = None
    currentLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None
    entities: Optional[List[EntityTypeDef]] = None

class SendEventRequestRequestTypeDef(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    eventTimestamp: str
    eventVariables: Mapping[str, str]
    entities: Sequence[EntityTypeDef]
    assignedLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None

class GetEntityTypesResultTypeDef(BaseValidatorModel):
    entityTypes: List[EntityTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventTypeRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ExternalModelTypeDef(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    modelSource: Optional[Literal["SAGEMAKER"]] = None
    invokeModelEndpointRoleArn: Optional[str] = None
    inputConfiguration: Optional[ModelInputConfigurationTypeDef] = None
    outputConfiguration: Optional[ModelOutputConfigurationTypeDef] = None
    modelEndpointStatus: Optional[ModelEndpointStatusType] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class PutExternalModelRequestRequestTypeDef(BaseValidatorModel):
    modelEndpoint: str
    modelSource: Literal["SAGEMAKER"]
    invokeModelEndpointRoleArn: str
    inputConfiguration: ModelInputConfigurationTypeDef
    outputConfiguration: ModelOutputConfigurationTypeDef
    modelEndpointStatus: ModelEndpointStatusType
    tags: Optional[Sequence[TagTypeDef]] = None

class GetKMSEncryptionKeyResultTypeDef(BaseValidatorModel):
    kmsKey: KMSKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLabelsResultTypeDef(BaseValidatorModel):
    labels: List[LabelTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelsResultTypeDef(BaseValidatorModel):
    nextToken: str
    models: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutcomesResultTypeDef(BaseValidatorModel):
    outcomes: List[OutcomeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRulesResultTypeDef(BaseValidatorModel):
    ruleDetails: List[RuleDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IngestedEventsDetailTypeDef(BaseValidatorModel):
    ingestedEventsTimeWindow: IngestedEventsTimeWindowTypeDef

class TrainingDataSchemaTypeDef(BaseValidatorModel):
    modelVariables: Sequence[str]
    labelSchema: Optional[LabelSchemaTypeDef] = None

class ListEventPredictionsRequestRequestTypeDef(BaseValidatorModel):
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
    aggregatedVariablesImpactExplanations: Optional[       List[AggregatedVariablesImpactExplanationTypeDef]     ] = None

class GetEventPredictionRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventPredictionResultTypeDef(BaseValidatorModel):
    modelScores: List[ModelScoresTypeDef]
    ruleResults: List[RuleResultTypeDef]
    externalModelOutputs: List[ExternalModelOutputsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetExternalModelsResultTypeDef(BaseValidatorModel):
    externalModels: List[ExternalModelTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelVersionRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    majorVersionNumber: str
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelVersionRequestRequestTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    trainingDataSource: TrainingDataSourceEnumType
    trainingDataSchema: TrainingDataSchemaTypeDef
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class GetModelVersionResultTypeDef(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    trainingDataSource: TrainingDataSourceEnumType
    trainingDataSchema: TrainingDataSchemaTypeDef
    externalEventsDetail: ExternalEventsDetailTypeDef
    ingestedEventsDetail: IngestedEventsDetailTypeDef
    status: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TrainingResultTypeDef(BaseValidatorModel):
    dataValidationMetrics: Optional[DataValidationMetricsTypeDef] = None
    trainingMetrics: Optional[TrainingMetricsTypeDef] = None
    variableImportanceMetrics: Optional[VariableImportanceMetricsTypeDef] = None

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
    aggregatedVariablesImportanceMetrics: Optional[       AggregatedVariablesImportanceMetricsTypeDef     ] = None

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
    trainingDataSchema: Optional[TrainingDataSchemaTypeDef] = None
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    trainingResult: Optional[TrainingResultTypeDef] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None
    trainingResultV2: Optional[TrainingResultV2TypeDef] = None

class DescribeModelVersionsResultTypeDef(BaseValidatorModel):
    modelVersionDetails: List[ModelVersionDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

