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
from aws_resource_validator.pydantic_models.frauddetector_constants import *

class ATIMetricDataPointTypeDef(BaseModel):
    cr: Optional[float] = None
    adr: Optional[float] = None
    threshold: Optional[float] = None
    atodr: Optional[float] = None

class ATIModelPerformanceTypeDef(BaseModel):
    asi: Optional[float] = None

class AggregatedLogOddsMetricTypeDef(BaseModel):
    variableNames: List[str]
    aggregatedVariablesImportance: float

class AggregatedVariablesImpactExplanationTypeDef(BaseModel):
    eventVariableNames: Optional[List[str]] = None
    relativeImpact: Optional[str] = None
    logOddsImpact: Optional[float] = None

class AllowDenyListTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    variableType: Optional[str] = None
    createdTime: Optional[str] = None
    updatedTime: Optional[str] = None
    arn: Optional[str] = None

class BatchCreateVariableErrorTypeDef(BaseModel):
    name: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class VariableEntryTypeDef(BaseModel):
    name: Optional[str] = None
    dataType: Optional[str] = None
    dataSource: Optional[str] = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchGetVariableErrorTypeDef(BaseModel):
    name: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None

class BatchGetVariableRequestRequestTypeDef(BaseModel):
    names: Sequence[str]

class VariableTypeDef(BaseModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    dataSource: Optional[DataSourceType] = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class BatchImportTypeDef(BaseModel):
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

class BatchPredictionTypeDef(BaseModel):
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

class CancelBatchImportJobRequestRequestTypeDef(BaseModel):
    jobId: str

class CancelBatchPredictionJobRequestRequestTypeDef(BaseModel):
    jobId: str

class ModelVersionTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    arn: Optional[str] = None

class RuleTypeDef(BaseModel):
    detectorId: str
    ruleId: str
    ruleVersion: str

class ExternalEventsDetailTypeDef(BaseModel):
    dataLocation: str
    dataAccessRoleArn: str

class FieldValidationMessageTypeDef(BaseModel):
    fieldName: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    type: Optional[str] = None

class FileValidationMessageTypeDef(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    type: Optional[str] = None

class DeleteBatchImportJobRequestRequestTypeDef(BaseModel):
    jobId: str

class DeleteBatchPredictionJobRequestRequestTypeDef(BaseModel):
    jobId: str

class DeleteDetectorRequestRequestTypeDef(BaseModel):
    detectorId: str

class DeleteDetectorVersionRequestRequestTypeDef(BaseModel):
    detectorId: str
    detectorVersionId: str

class DeleteEntityTypeRequestRequestTypeDef(BaseModel):
    name: str

class DeleteEventRequestRequestTypeDef(BaseModel):
    eventId: str
    eventTypeName: str
    deleteAuditHistory: Optional[bool] = None

class DeleteEventTypeRequestRequestTypeDef(BaseModel):
    name: str

class DeleteEventsByEventTypeRequestRequestTypeDef(BaseModel):
    eventTypeName: str

class DeleteExternalModelRequestRequestTypeDef(BaseModel):
    modelEndpoint: str

class DeleteLabelRequestRequestTypeDef(BaseModel):
    name: str

class DeleteListRequestRequestTypeDef(BaseModel):
    name: str

class DeleteModelRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType

class DeleteModelVersionRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str

class DeleteOutcomeRequestRequestTypeDef(BaseModel):
    name: str

class DeleteVariableRequestRequestTypeDef(BaseModel):
    name: str

class DescribeDetectorRequestRequestTypeDef(BaseModel):
    detectorId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DetectorVersionSummaryTypeDef(BaseModel):
    detectorVersionId: Optional[str] = None
    status: Optional[DetectorVersionStatusType] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None

class DescribeModelVersionsRequestRequestTypeDef(BaseModel):
    modelId: Optional[str] = None
    modelVersionNumber: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DetectorTypeDef(BaseModel):
    detectorId: Optional[str] = None
    description: Optional[str] = None
    eventTypeName: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class EntityTypeDef(BaseModel):
    entityType: str
    entityId: str

class EntityTypeTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class EvaluatedExternalModelTypeDef(BaseModel):
    modelEndpoint: Optional[str] = None
    useEventVariables: Optional[bool] = None
    inputVariables: Optional[Dict[str, str]] = None
    outputVariables: Optional[Dict[str, str]] = None

class EvaluatedRuleTypeDef(BaseModel):
    ruleId: Optional[str] = None
    ruleVersion: Optional[str] = None
    expression: Optional[str] = None
    expressionWithValues: Optional[str] = None
    outcomes: Optional[List[str]] = None
    evaluated: Optional[bool] = None
    matched: Optional[bool] = None

class EventOrchestrationTypeDef(BaseModel):
    eventBridgeEnabled: bool

class EventPredictionSummaryTypeDef(BaseModel):
    eventId: Optional[str] = None
    eventTypeName: Optional[str] = None
    eventTimestamp: Optional[str] = None
    predictionTimestamp: Optional[str] = None
    detectorId: Optional[str] = None
    detectorVersionId: Optional[str] = None

class IngestedEventStatisticsTypeDef(BaseModel):
    numberOfEvents: Optional[int] = None
    eventDataSizeInBytes: Optional[int] = None
    leastRecentEvent: Optional[str] = None
    mostRecentEvent: Optional[str] = None
    lastUpdatedTime: Optional[str] = None

class EventVariableSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None
    source: Optional[str] = None

class ExternalModelSummaryTypeDef(BaseModel):
    modelEndpoint: Optional[str] = None
    modelSource: Optional[Literal["SAGEMAKER"]] = None

class ModelInputConfigurationTypeDef(BaseModel):
    useEventVariables: bool
    eventTypeName: Optional[str] = None
    format: Optional[ModelInputDataFormatType] = None
    jsonInputTemplate: Optional[str] = None
    csvInputTemplate: Optional[str] = None

class ModelOutputConfigurationTypeDef(BaseModel):
    format: ModelOutputDataFormatType
    jsonKeyToVariableMap: Optional[Dict[str, str]] = None
    csvIndexToVariableMap: Optional[Dict[str, str]] = None

class FilterConditionTypeDef(BaseModel):
    value: Optional[str] = None

class GetBatchImportJobsRequestRequestTypeDef(BaseModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetBatchPredictionJobsRequestRequestTypeDef(BaseModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetDeleteEventsByEventTypeStatusRequestRequestTypeDef(BaseModel):
    eventTypeName: str

class GetDetectorVersionRequestRequestTypeDef(BaseModel):
    detectorId: str
    detectorVersionId: str

class GetDetectorsRequestRequestTypeDef(BaseModel):
    detectorId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEntityTypesRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetEventPredictionMetadataRequestRequestTypeDef(BaseModel):
    eventId: str
    eventTypeName: str
    detectorId: str
    detectorVersionId: str
    predictionTimestamp: str

class RuleResultTypeDef(BaseModel):
    ruleId: Optional[str] = None
    outcomes: Optional[List[str]] = None

class GetEventRequestRequestTypeDef(BaseModel):
    eventId: str
    eventTypeName: str

class GetEventTypesRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetExternalModelsRequestRequestTypeDef(BaseModel):
    modelEndpoint: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class KMSKeyTypeDef(BaseModel):
    kmsEncryptionKeyArn: Optional[str] = None

class GetLabelsRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LabelTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class GetListElementsRequestRequestTypeDef(BaseModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetListsMetadataRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetModelVersionRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str

class GetModelsRequestRequestTypeDef(BaseModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ModelTypeDef(BaseModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    description: Optional[str] = None
    eventTypeName: Optional[str] = None
    createdTime: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    arn: Optional[str] = None

class GetOutcomesRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class OutcomeTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class GetRulesRequestRequestTypeDef(BaseModel):
    detectorId: str
    ruleId: Optional[str] = None
    ruleVersion: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RuleDetailTypeDef(BaseModel):
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

class GetVariablesRequestRequestTypeDef(BaseModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class IngestedEventsTimeWindowTypeDef(BaseModel):
    startTime: str
    endTime: str

class LabelSchemaTypeDef(BaseModel):
    labelMapper: Optional[Mapping[str, Sequence[str]]] = None
    unlabeledEventsTreatment: Optional[UnlabeledEventsTreatmentType] = None

class PredictionTimeRangeTypeDef(BaseModel):
    startTime: str
    endTime: str

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class LogOddsMetricTypeDef(BaseModel):
    variableName: str
    variableType: str
    variableImportance: float

class MetricDataPointTypeDef(BaseModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None

class OFIMetricDataPointTypeDef(BaseModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None

class UncertaintyRangeTypeDef(BaseModel):
    lowerBoundValue: float
    upperBoundValue: float

class VariableImpactExplanationTypeDef(BaseModel):
    eventVariableName: Optional[str] = None
    relativeImpact: Optional[str] = None
    logOddsImpact: Optional[float] = None

class PutKMSEncryptionKeyRequestRequestTypeDef(BaseModel):
    kmsEncryptionKeyArn: str

class TFIMetricDataPointTypeDef(BaseModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tagKeys: Sequence[str]

class UpdateDetectorVersionMetadataRequestRequestTypeDef(BaseModel):
    detectorId: str
    detectorVersionId: str
    description: str

class UpdateDetectorVersionStatusRequestRequestTypeDef(BaseModel):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatusType

class UpdateEventLabelRequestRequestTypeDef(BaseModel):
    eventId: str
    eventTypeName: str
    assignedLabel: str
    labelTimestamp: str

class UpdateListRequestRequestTypeDef(BaseModel):
    name: str
    elements: Optional[Sequence[str]] = None
    description: Optional[str] = None
    updateMode: Optional[ListUpdateModeType] = None
    variableType: Optional[str] = None

class UpdateModelRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    description: Optional[str] = None

class UpdateModelVersionStatusRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: ModelVersionStatusType

class UpdateVariableRequestRequestTypeDef(BaseModel):
    name: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None

class ATITrainingMetricsValueTypeDef(BaseModel):
    metricDataPoints: Optional[List[ATIMetricDataPointTypeDef]] = None
    modelPerformance: Optional[ATIModelPerformanceTypeDef] = None

class AggregatedVariablesImportanceMetricsTypeDef(BaseModel):
    logOddsMetrics: Optional[List[AggregatedLogOddsMetricTypeDef]] = None

class CreateBatchImportJobRequestRequestTypeDef(BaseModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    iamRoleArn: str
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateBatchPredictionJobRequestRequestTypeDef(BaseModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    detectorName: str
    iamRoleArn: str
    detectorVersion: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateListRequestRequestTypeDef(BaseModel):
    name: str
    elements: Optional[Sequence[str]] = None
    variableType: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRuleRequestRequestTypeDef(BaseModel):
    ruleId: str
    detectorId: str
    expression: str
    language: Literal["DETECTORPL"]
    outcomes: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateVariableRequestRequestTypeDef(BaseModel):
    name: str
    dataType: DataTypeType
    dataSource: DataSourceType
    defaultValue: str
    description: Optional[str] = None
    variableType: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutDetectorRequestRequestTypeDef(BaseModel):
    detectorId: str
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutEntityTypeRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutLabelRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutOutcomeRequestRequestTypeDef(BaseModel):
    name: str
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]

class BatchCreateVariableRequestRequestTypeDef(BaseModel):
    variableEntries: Sequence[VariableEntryTypeDef]
    tags: Optional[Sequence[TagTypeDef]] = None

class BatchCreateVariableResultTypeDef(BaseModel):
    errors: List[BatchCreateVariableErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDetectorVersionResultTypeDef(BaseModel):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateModelVersionResultTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventsByEventTypeResultTypeDef(BaseModel):
    eventTypeName: str
    eventsDeletionStatus: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeleteEventsByEventTypeStatusResultTypeDef(BaseModel):
    eventTypeName: str
    eventsDeletionStatus: AsyncJobStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class GetListElementsResultTypeDef(BaseModel):
    elements: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetListsMetadataResultTypeDef(BaseModel):
    lists: List[AllowDenyListTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseModel):
    tags: List[TagTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelVersionResultTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetVariableResultTypeDef(BaseModel):
    variables: List[VariableTypeDef]
    errors: List[BatchGetVariableErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetVariablesResultTypeDef(BaseModel):
    variables: List[VariableTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBatchImportJobsResultTypeDef(BaseModel):
    batchImports: List[BatchImportTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetBatchPredictionJobsResultTypeDef(BaseModel):
    batchPredictions: List[BatchPredictionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModelEndpointDataBlobTypeDef(BaseModel):
    byteBuffer: Optional[BlobTypeDef] = None
    contentType: Optional[str] = None

class ModelScoresTypeDef(BaseModel):
    modelVersion: Optional[ModelVersionTypeDef] = None
    scores: Optional[Dict[str, float]] = None

class CreateDetectorVersionRequestRequestTypeDef(BaseModel):
    detectorId: str
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    externalModelEndpoints: Optional[Sequence[str]] = None
    modelVersions: Optional[Sequence[ModelVersionTypeDef]] = None
    ruleExecutionMode: Optional[RuleExecutionModeType] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateRuleResultTypeDef(BaseModel):
    rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRuleRequestRequestTypeDef(BaseModel):
    rule: RuleTypeDef

class GetDetectorVersionResultTypeDef(BaseModel):
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

class UpdateDetectorVersionRequestRequestTypeDef(BaseModel):
    detectorId: str
    detectorVersionId: str
    externalModelEndpoints: Sequence[str]
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    modelVersions: Optional[Sequence[ModelVersionTypeDef]] = None
    ruleExecutionMode: Optional[RuleExecutionModeType] = None

class UpdateRuleMetadataRequestRequestTypeDef(BaseModel):
    rule: RuleTypeDef
    description: str

class UpdateRuleVersionRequestRequestTypeDef(BaseModel):
    rule: RuleTypeDef
    expression: str
    language: Literal["DETECTORPL"]
    outcomes: Sequence[str]
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRuleVersionResultTypeDef(BaseModel):
    rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DataValidationMetricsTypeDef(BaseModel):
    fileLevelMessages: Optional[List[FileValidationMessageTypeDef]] = None
    fieldLevelMessages: Optional[List[FieldValidationMessageTypeDef]] = None

class DescribeDetectorResultTypeDef(BaseModel):
    detectorId: str
    detectorVersionSummaries: List[DetectorVersionSummaryTypeDef]
    nextToken: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDetectorsResultTypeDef(BaseModel):
    detectors: List[DetectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseModel):
    eventId: Optional[str] = None
    eventTypeName: Optional[str] = None
    eventTimestamp: Optional[str] = None
    eventVariables: Optional[Dict[str, str]] = None
    currentLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None
    entities: Optional[List[EntityTypeDef]] = None

class SendEventRequestRequestTypeDef(BaseModel):
    eventId: str
    eventTypeName: str
    eventTimestamp: str
    eventVariables: Mapping[str, str]
    entities: Sequence[EntityTypeDef]
    assignedLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None

class GetEntityTypesResultTypeDef(BaseModel):
    entityTypes: List[EntityTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventTypeRequestRequestTypeDef(BaseModel):
    name: str
    eventVariables: Sequence[str]
    entityTypes: Sequence[str]
    description: Optional[str] = None
    labels: Optional[Sequence[str]] = None
    eventIngestion: Optional[EventIngestionType] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    eventOrchestration: Optional[EventOrchestrationTypeDef] = None

class ListEventPredictionsResultTypeDef(BaseModel):
    eventPredictionSummaries: List[EventPredictionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeTypeDef(BaseModel):
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

class ExternalModelOutputsTypeDef(BaseModel):
    externalModel: Optional[ExternalModelSummaryTypeDef] = None
    outputs: Optional[Dict[str, str]] = None

class ExternalModelTypeDef(BaseModel):
    modelEndpoint: Optional[str] = None
    modelSource: Optional[Literal["SAGEMAKER"]] = None
    invokeModelEndpointRoleArn: Optional[str] = None
    inputConfiguration: Optional[ModelInputConfigurationTypeDef] = None
    outputConfiguration: Optional[ModelOutputConfigurationTypeDef] = None
    modelEndpointStatus: Optional[ModelEndpointStatusType] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None

class PutExternalModelRequestRequestTypeDef(BaseModel):
    modelEndpoint: str
    modelSource: Literal["SAGEMAKER"]
    invokeModelEndpointRoleArn: str
    inputConfiguration: ModelInputConfigurationTypeDef
    outputConfiguration: ModelOutputConfigurationTypeDef
    modelEndpointStatus: ModelEndpointStatusType
    tags: Optional[Sequence[TagTypeDef]] = None

class GetKMSEncryptionKeyResultTypeDef(BaseModel):
    kmsKey: KMSKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLabelsResultTypeDef(BaseModel):
    labels: List[LabelTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetModelsResultTypeDef(BaseModel):
    nextToken: str
    models: List[ModelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetOutcomesResultTypeDef(BaseModel):
    outcomes: List[OutcomeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRulesResultTypeDef(BaseModel):
    ruleDetails: List[RuleDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IngestedEventsDetailTypeDef(BaseModel):
    ingestedEventsTimeWindow: IngestedEventsTimeWindowTypeDef

class TrainingDataSchemaTypeDef(BaseModel):
    modelVariables: Sequence[str]
    labelSchema: Optional[LabelSchemaTypeDef] = None

class ListEventPredictionsRequestRequestTypeDef(BaseModel):
    eventId: Optional[FilterConditionTypeDef] = None
    eventType: Optional[FilterConditionTypeDef] = None
    detectorId: Optional[FilterConditionTypeDef] = None
    detectorVersionId: Optional[FilterConditionTypeDef] = None
    predictionTimeRange: Optional[PredictionTimeRangeTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class VariableImportanceMetricsTypeDef(BaseModel):
    logOddsMetrics: Optional[List[LogOddsMetricTypeDef]] = None

class TrainingMetricsTypeDef(BaseModel):
    auc: Optional[float] = None
    metricDataPoints: Optional[List[MetricDataPointTypeDef]] = None

class OFIModelPerformanceTypeDef(BaseModel):
    auc: Optional[float] = None
    uncertaintyRange: Optional[UncertaintyRangeTypeDef] = None

class TFIModelPerformanceTypeDef(BaseModel):
    auc: Optional[float] = None
    uncertaintyRange: Optional[UncertaintyRangeTypeDef] = None

class PredictionExplanationsTypeDef(BaseModel):
    variableImpactExplanations: Optional[List[VariableImpactExplanationTypeDef]] = None
    aggregatedVariablesImpactExplanations: Optional[       List[AggregatedVariablesImpactExplanationTypeDef]     ] = None

class GetEventPredictionRequestRequestTypeDef(BaseModel):
    detectorId: str
    eventId: str
    eventTypeName: str
    entities: Sequence[EntityTypeDef]
    eventTimestamp: str
    eventVariables: Mapping[str, str]
    detectorVersionId: Optional[str] = None
    externalModelEndpointDataBlobs: Optional[Mapping[str, ModelEndpointDataBlobTypeDef]] = None

class GetEventResultTypeDef(BaseModel):
    event: EventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventTypesResultTypeDef(BaseModel):
    eventTypes: List[EventTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventPredictionResultTypeDef(BaseModel):
    modelScores: List[ModelScoresTypeDef]
    ruleResults: List[RuleResultTypeDef]
    externalModelOutputs: List[ExternalModelOutputsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetExternalModelsResultTypeDef(BaseModel):
    externalModels: List[ExternalModelTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateModelVersionRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    majorVersionNumber: str
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreateModelVersionRequestRequestTypeDef(BaseModel):
    modelId: str
    modelType: ModelTypeEnumType
    trainingDataSource: TrainingDataSourceEnumType
    trainingDataSchema: TrainingDataSchemaTypeDef
    externalEventsDetail: Optional[ExternalEventsDetailTypeDef] = None
    ingestedEventsDetail: Optional[IngestedEventsDetailTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class GetModelVersionResultTypeDef(BaseModel):
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

class TrainingResultTypeDef(BaseModel):
    dataValidationMetrics: Optional[DataValidationMetricsTypeDef] = None
    trainingMetrics: Optional[TrainingMetricsTypeDef] = None
    variableImportanceMetrics: Optional[VariableImportanceMetricsTypeDef] = None

class OFITrainingMetricsValueTypeDef(BaseModel):
    metricDataPoints: Optional[List[OFIMetricDataPointTypeDef]] = None
    modelPerformance: Optional[OFIModelPerformanceTypeDef] = None

class TFITrainingMetricsValueTypeDef(BaseModel):
    metricDataPoints: Optional[List[TFIMetricDataPointTypeDef]] = None
    modelPerformance: Optional[TFIModelPerformanceTypeDef] = None

class ModelVersionEvaluationTypeDef(BaseModel):
    outputVariableName: Optional[str] = None
    evaluationScore: Optional[str] = None
    predictionExplanations: Optional[PredictionExplanationsTypeDef] = None

class TrainingMetricsV2TypeDef(BaseModel):
    ofi: Optional[OFITrainingMetricsValueTypeDef] = None
    tfi: Optional[TFITrainingMetricsValueTypeDef] = None
    ati: Optional[ATITrainingMetricsValueTypeDef] = None

class EvaluatedModelVersionTypeDef(BaseModel):
    modelId: Optional[str] = None
    modelVersion: Optional[str] = None
    modelType: Optional[str] = None
    evaluations: Optional[List[ModelVersionEvaluationTypeDef]] = None

class TrainingResultV2TypeDef(BaseModel):
    dataValidationMetrics: Optional[DataValidationMetricsTypeDef] = None
    trainingMetricsV2: Optional[TrainingMetricsV2TypeDef] = None
    variableImportanceMetrics: Optional[VariableImportanceMetricsTypeDef] = None
    aggregatedVariablesImportanceMetrics: Optional[       AggregatedVariablesImportanceMetricsTypeDef     ] = None

class GetEventPredictionMetadataResultTypeDef(BaseModel):
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

class ModelVersionDetailTypeDef(BaseModel):
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

class DescribeModelVersionsResultTypeDef(BaseModel):
    modelVersionDetails: List[ModelVersionDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

