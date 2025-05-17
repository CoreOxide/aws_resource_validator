from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.frauddetector.frauddetector_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ATIMetricDataPoint(BaseValidatorModel):
    cr: Optional[float] = None
    adr: Optional[float] = None
    threshold: Optional[float] = None
    atodr: Optional[float] = None


class ATIModelPerformance(BaseValidatorModel):
    asi: Optional[float] = None


class AggregatedLogOddsMetric(BaseValidatorModel):
    variableNames: List[str]
    aggregatedVariablesImportance: float


class AggregatedVariablesImpactExplanation(BaseValidatorModel):
    eventVariableNames: Optional[List[str]] = None
    relativeImpact: Optional[str] = None
    logOddsImpact: Optional[float] = None


class AllowDenyList(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    variableType: Optional[str] = None
    createdTime: Optional[str] = None
    updatedTime: Optional[str] = None
    arn: Optional[str] = None


class BatchCreateVariableError(BaseValidatorModel):
    name: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class VariableEntry(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[str] = None
    dataSource: Optional[str] = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetVariableError(BaseValidatorModel):
    name: Optional[str] = None
    code: Optional[int] = None
    message: Optional[str] = None


# This class is the input for the 'batch_get_variable' function.
class BatchGetVariableRequest(BaseValidatorModel):
    names: List[str]


class Variable(BaseValidatorModel):
    name: Optional[str] = None
    dataType: Optional[DataTypeType] = None
    dataSource: Optional[DataSourceType] = None
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class BatchImport(BaseValidatorModel):
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


class BatchPrediction(BaseValidatorModel):
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

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CancelBatchImportJobRequest(BaseValidatorModel):
    jobId: str


class CancelBatchPredictionJobRequest(BaseValidatorModel):
    jobId: str


class ModelVersion(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    arn: Optional[str] = None


class Rule(BaseValidatorModel):
    detectorId: str
    ruleId: str
    ruleVersion: str


class ExternalEventsDetail(BaseValidatorModel):
    dataLocation: str
    dataAccessRoleArn: str


class FieldValidationMessage(BaseValidatorModel):
    fieldName: Optional[str] = None
    identifier: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    type: Optional[str] = None


class FileValidationMessage(BaseValidatorModel):
    title: Optional[str] = None
    content: Optional[str] = None
    type: Optional[str] = None


class DeleteBatchImportJobRequest(BaseValidatorModel):
    jobId: str


class DeleteBatchPredictionJobRequest(BaseValidatorModel):
    jobId: str


class DeleteDetectorRequest(BaseValidatorModel):
    detectorId: str


class DeleteDetectorVersionRequest(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str


class DeleteEntityTypeRequest(BaseValidatorModel):
    name: str


class DeleteEventRequest(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    deleteAuditHistory: Optional[bool] = None


class DeleteEventTypeRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_events_by_event_type' function.
class DeleteEventsByEventTypeRequest(BaseValidatorModel):
    eventTypeName: str


class DeleteExternalModelRequest(BaseValidatorModel):
    modelEndpoint: str


class DeleteLabelRequest(BaseValidatorModel):
    name: str


class DeleteListRequest(BaseValidatorModel):
    name: str


class DeleteModelRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType


class DeleteModelVersionRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str


class DeleteOutcomeRequest(BaseValidatorModel):
    name: str


class DeleteVariableRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'describe_detector' function.
class DescribeDetectorRequest(BaseValidatorModel):
    detectorId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DetectorVersionSummary(BaseValidatorModel):
    detectorVersionId: Optional[str] = None
    status: Optional[DetectorVersionStatusType] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None


# This class is the input for the 'describe_model_versions' function.
class DescribeModelVersionsRequest(BaseValidatorModel):
    modelId: Optional[str] = None
    modelVersionNumber: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class Detector(BaseValidatorModel):
    detectorId: Optional[str] = None
    description: Optional[str] = None
    eventTypeName: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class Entity(BaseValidatorModel):
    entityType: str
    entityId: str


class EntityType(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class EvaluatedExternalModel(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    useEventVariables: Optional[bool] = None
    inputVariables: Optional[Dict[str, str]] = None
    outputVariables: Optional[Dict[str, str]] = None


class EvaluatedRule(BaseValidatorModel):
    ruleId: Optional[str] = None
    ruleVersion: Optional[str] = None
    expression: Optional[str] = None
    expressionWithValues: Optional[str] = None
    outcomes: Optional[List[str]] = None
    evaluated: Optional[bool] = None
    matched: Optional[bool] = None


class EventOrchestration(BaseValidatorModel):
    eventBridgeEnabled: bool


class EventPredictionSummary(BaseValidatorModel):
    eventId: Optional[str] = None
    eventTypeName: Optional[str] = None
    eventTimestamp: Optional[str] = None
    predictionTimestamp: Optional[str] = None
    detectorId: Optional[str] = None
    detectorVersionId: Optional[str] = None


class IngestedEventStatistics(BaseValidatorModel):
    numberOfEvents: Optional[int] = None
    eventDataSizeInBytes: Optional[int] = None
    leastRecentEvent: Optional[str] = None
    mostRecentEvent: Optional[str] = None
    lastUpdatedTime: Optional[str] = None


class EventVariableSummary(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None
    source: Optional[str] = None


class ExternalModelSummary(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    modelSource: Optional[Literal['SAGEMAKER']] = None


class ModelInputConfiguration(BaseValidatorModel):
    useEventVariables: bool
    eventTypeName: Optional[str] = None
    format: Optional[ModelInputDataFormatType] = None
    jsonInputTemplate: Optional[str] = None
    csvInputTemplate: Optional[str] = None


class ModelOutputConfigurationOutput(BaseValidatorModel):
    format: ModelOutputDataFormatType
    jsonKeyToVariableMap: Optional[Dict[str, str]] = None
    csvIndexToVariableMap: Optional[Dict[str, str]] = None


class FilterCondition(BaseValidatorModel):
    value: Optional[str] = None


# This class is the input for the 'get_batch_import_jobs' function.
class GetBatchImportJobsRequest(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'get_batch_prediction_jobs' function.
class GetBatchPredictionJobsRequest(BaseValidatorModel):
    jobId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'get_delete_events_by_event_type_status' function.
class GetDeleteEventsByEventTypeStatusRequest(BaseValidatorModel):
    eventTypeName: str


# This class is the input for the 'get_detector_version' function.
class GetDetectorVersionRequest(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str


# This class is the input for the 'get_detectors' function.
class GetDetectorsRequest(BaseValidatorModel):
    detectorId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_entity_types' function.
class GetEntityTypesRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_event_prediction_metadata' function.
class GetEventPredictionMetadataRequest(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    detectorId: str
    detectorVersionId: str
    predictionTimestamp: str


class RuleResult(BaseValidatorModel):
    ruleId: Optional[str] = None
    outcomes: Optional[List[str]] = None


# This class is the input for the 'get_event' function.
class GetEventRequest(BaseValidatorModel):
    eventId: str
    eventTypeName: str


# This class is the input for the 'get_event_types' function.
class GetEventTypesRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_external_models' function.
class GetExternalModelsRequest(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class KMSKey(BaseValidatorModel):
    kmsEncryptionKeyArn: Optional[str] = None


# This class is the input for the 'get_labels' function.
class GetLabelsRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class Label(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


# This class is the input for the 'get_list_elements' function.
class GetListElementsRequest(BaseValidatorModel):
    name: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_lists_metadata' function.
class GetListsMetadataRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_model_version' function.
class GetModelVersionRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str


# This class is the input for the 'get_models' function.
class GetModelsRequest(BaseValidatorModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class Model(BaseValidatorModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    description: Optional[str] = None
    eventTypeName: Optional[str] = None
    createdTime: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    arn: Optional[str] = None


# This class is the input for the 'get_outcomes' function.
class GetOutcomesRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class Outcome(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


# This class is the input for the 'get_rules' function.
class GetRulesRequest(BaseValidatorModel):
    detectorId: str
    ruleId: Optional[str] = None
    ruleVersion: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RuleDetail(BaseValidatorModel):
    ruleId: Optional[str] = None
    description: Optional[str] = None
    detectorId: Optional[str] = None
    ruleVersion: Optional[str] = None
    expression: Optional[str] = None
    language: Optional[Literal['DETECTORPL']] = None
    outcomes: Optional[List[str]] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


# This class is the input for the 'get_variables' function.
class GetVariablesRequest(BaseValidatorModel):
    name: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class IngestedEventsTimeWindow(BaseValidatorModel):
    startTime: str
    endTime: str


class LabelSchemaOutput(BaseValidatorModel):
    labelMapper: Optional[Dict[str, List[str]]] = None
    unlabeledEventsTreatment: Optional[UnlabeledEventsTreatmentType] = None


class LabelSchema(BaseValidatorModel):
    labelMapper: Optional[Dict[str, List[str]]] = None
    unlabeledEventsTreatment: Optional[UnlabeledEventsTreatmentType] = None


class PredictionTimeRange(BaseValidatorModel):
    startTime: str
    endTime: str


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class LogOddsMetric(BaseValidatorModel):
    variableName: str
    variableType: str
    variableImportance: float


class MetricDataPoint(BaseValidatorModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None


class ModelOutputConfiguration(BaseValidatorModel):
    format: ModelOutputDataFormatType
    jsonKeyToVariableMap: Optional[Dict[str, str]] = None
    csvIndexToVariableMap: Optional[Dict[str, str]] = None


class OFIMetricDataPoint(BaseValidatorModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None


class UncertaintyRange(BaseValidatorModel):
    lowerBoundValue: float
    upperBoundValue: float


class VariableImpactExplanation(BaseValidatorModel):
    eventVariableName: Optional[str] = None
    relativeImpact: Optional[str] = None
    logOddsImpact: Optional[float] = None


class PutKMSEncryptionKeyRequest(BaseValidatorModel):
    kmsEncryptionKeyArn: str


class TFIMetricDataPoint(BaseValidatorModel):
    fpr: Optional[float] = None
    precision: Optional[float] = None
    tpr: Optional[float] = None
    threshold: Optional[float] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: List[str]


class UpdateDetectorVersionMetadataRequest(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    description: str


class UpdateDetectorVersionStatusRequest(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatusType


class UpdateEventLabelRequest(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    assignedLabel: str
    labelTimestamp: str


class UpdateListRequest(BaseValidatorModel):
    name: str
    elements: Optional[List[str]] = None
    description: Optional[str] = None
    updateMode: Optional[ListUpdateModeType] = None
    variableType: Optional[str] = None


class UpdateModelRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    description: Optional[str] = None


class UpdateModelVersionStatusRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: ModelVersionStatusType


class UpdateVariableRequest(BaseValidatorModel):
    name: str
    defaultValue: Optional[str] = None
    description: Optional[str] = None
    variableType: Optional[str] = None


class ATITrainingMetricsValue(BaseValidatorModel):
    metricDataPoints: Optional[List[ATIMetricDataPoint]] = None
    modelPerformance: Optional[ATIModelPerformance] = None


class AggregatedVariablesImportanceMetrics(BaseValidatorModel):
    logOddsMetrics: Optional[List[AggregatedLogOddsMetric]] = None


class CreateBatchImportJobRequest(BaseValidatorModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    iamRoleArn: str
    tags: Optional[List[Tag]] = None


class CreateBatchPredictionJobRequest(BaseValidatorModel):
    jobId: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    detectorName: str
    iamRoleArn: str
    detectorVersion: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateListRequest(BaseValidatorModel):
    name: str
    elements: Optional[List[str]] = None
    variableType: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateModelRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_rule' function.
class CreateRuleRequest(BaseValidatorModel):
    ruleId: str
    detectorId: str
    expression: str
    language: Literal['DETECTORPL']
    outcomes: List[str]
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class CreateVariableRequest(BaseValidatorModel):
    name: str
    dataType: DataTypeType
    dataSource: DataSourceType
    defaultValue: str
    description: Optional[str] = None
    variableType: Optional[str] = None
    tags: Optional[List[Tag]] = None


class PutDetectorRequest(BaseValidatorModel):
    detectorId: str
    eventTypeName: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class PutEntityTypeRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class PutLabelRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class PutOutcomeRequest(BaseValidatorModel):
    name: str
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: List[Tag]


# This class is the input for the 'batch_create_variable' function.
class BatchCreateVariableRequest(BaseValidatorModel):
    variableEntries: List[VariableEntry]
    tags: Optional[List[Tag]] = None


# This class is the output for the 'batch_create_variable' function.
class BatchCreateVariableResult(BaseValidatorModel):
    errors: List[BatchCreateVariableError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_detector_version' function.
class CreateDetectorVersionResult(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_model_version' function.
class CreateModelVersionResult(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_events_by_event_type' function.
class DeleteEventsByEventTypeResult(BaseValidatorModel):
    eventTypeName: str
    eventsDeletionStatus: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_delete_events_by_event_type_status' function.
class GetDeleteEventsByEventTypeStatusResult(BaseValidatorModel):
    eventTypeName: str
    eventsDeletionStatus: AsyncJobStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_list_elements' function.
class GetListElementsResult(BaseValidatorModel):
    elements: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_lists_metadata' function.
class GetListsMetadataResult(BaseValidatorModel):
    lists: List[AllowDenyList]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResult(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_model_version' function.
class UpdateModelVersionResult(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    status: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_variable' function.
class BatchGetVariableResult(BaseValidatorModel):
    variables: List[Variable]
    errors: List[BatchGetVariableError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_variables' function.
class GetVariablesResult(BaseValidatorModel):
    variables: List[Variable]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_batch_import_jobs' function.
class GetBatchImportJobsResult(BaseValidatorModel):
    batchImports: List[BatchImport]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_batch_prediction_jobs' function.
class GetBatchPredictionJobsResult(BaseValidatorModel):
    batchPredictions: List[BatchPrediction]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ModelEndpointDataBlob(BaseValidatorModel):
    byteBuffer: Optional[Blob] = None
    contentType: Optional[str] = None


class ModelScores(BaseValidatorModel):
    modelVersion: Optional[ModelVersion] = None
    scores: Optional[Dict[str, float]] = None


# This class is the input for the 'create_detector_version' function.
class CreateDetectorVersionRequest(BaseValidatorModel):
    detectorId: str
    rules: List[Rule]
    description: Optional[str] = None
    externalModelEndpoints: Optional[List[str]] = None
    modelVersions: Optional[List[ModelVersion]] = None
    ruleExecutionMode: Optional[RuleExecutionModeType] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'create_rule' function.
class CreateRuleResult(BaseValidatorModel):
    rule: Rule
    ResponseMetadata: ResponseMetadata


class DeleteRuleRequest(BaseValidatorModel):
    rule: Rule


# This class is the output for the 'get_detector_version' function.
class GetDetectorVersionResult(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    description: str
    externalModelEndpoints: List[str]
    modelVersions: List[ModelVersion]
    rules: List[Rule]
    status: DetectorVersionStatusType
    lastUpdatedTime: str
    createdTime: str
    ruleExecutionMode: RuleExecutionModeType
    arn: str
    ResponseMetadata: ResponseMetadata


class UpdateDetectorVersionRequest(BaseValidatorModel):
    detectorId: str
    detectorVersionId: str
    externalModelEndpoints: List[str]
    rules: List[Rule]
    description: Optional[str] = None
    modelVersions: Optional[List[ModelVersion]] = None
    ruleExecutionMode: Optional[RuleExecutionModeType] = None


class UpdateRuleMetadataRequest(BaseValidatorModel):
    rule: Rule
    description: str


# This class is the input for the 'update_rule_version' function.
class UpdateRuleVersionRequest(BaseValidatorModel):
    rule: Rule
    expression: str
    language: Literal['DETECTORPL']
    outcomes: List[str]
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'update_rule_version' function.
class UpdateRuleVersionResult(BaseValidatorModel):
    rule: Rule
    ResponseMetadata: ResponseMetadata


class DataValidationMetrics(BaseValidatorModel):
    fileLevelMessages: Optional[List[FileValidationMessage]] = None
    fieldLevelMessages: Optional[List[FieldValidationMessage]] = None


# This class is the output for the 'describe_detector' function.
class DescribeDetectorResult(BaseValidatorModel):
    detectorId: str
    detectorVersionSummaries: List[DetectorVersionSummary]
    arn: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_detectors' function.
class GetDetectorsResult(BaseValidatorModel):
    detectors: List[Detector]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Event(BaseValidatorModel):
    eventId: Optional[str] = None
    eventTypeName: Optional[str] = None
    eventTimestamp: Optional[str] = None
    eventVariables: Optional[Dict[str, str]] = None
    currentLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None
    entities: Optional[List[Entity]] = None


class SendEventRequest(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    eventTimestamp: str
    eventVariables: Dict[str, str]
    entities: List[Entity]
    assignedLabel: Optional[str] = None
    labelTimestamp: Optional[str] = None


# This class is the output for the 'get_entity_types' function.
class GetEntityTypesResult(BaseValidatorModel):
    entityTypes: List[EntityType]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PutEventTypeRequest(BaseValidatorModel):
    name: str
    eventVariables: List[str]
    entityTypes: List[str]
    description: Optional[str] = None
    labels: Optional[List[str]] = None
    eventIngestion: Optional[EventIngestionType] = None
    tags: Optional[List[Tag]] = None
    eventOrchestration: Optional[EventOrchestration] = None


# This class is the output for the 'list_event_predictions' function.
class ListEventPredictionsResult(BaseValidatorModel):
    eventPredictionSummaries: List[EventPredictionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EventType(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    eventVariables: Optional[List[str]] = None
    labels: Optional[List[str]] = None
    entityTypes: Optional[List[str]] = None
    eventIngestion: Optional[EventIngestionType] = None
    ingestedEventStatistics: Optional[IngestedEventStatistics] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None
    eventOrchestration: Optional[EventOrchestration] = None


class ExternalModelOutputs(BaseValidatorModel):
    externalModel: Optional[ExternalModelSummary] = None
    outputs: Optional[Dict[str, str]] = None


class ExternalModel(BaseValidatorModel):
    modelEndpoint: Optional[str] = None
    modelSource: Optional[Literal['SAGEMAKER']] = None
    invokeModelEndpointRoleArn: Optional[str] = None
    inputConfiguration: Optional[ModelInputConfiguration] = None
    outputConfiguration: Optional[ModelOutputConfigurationOutput] = None
    modelEndpointStatus: Optional[ModelEndpointStatusType] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None


class GetKMSEncryptionKeyResult(BaseValidatorModel):
    kmsKey: KMSKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_labels' function.
class GetLabelsResult(BaseValidatorModel):
    labels: List[Label]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_models' function.
class GetModelsResult(BaseValidatorModel):
    models: List[Model]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_outcomes' function.
class GetOutcomesResult(BaseValidatorModel):
    outcomes: List[Outcome]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_rules' function.
class GetRulesResult(BaseValidatorModel):
    ruleDetails: List[RuleDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IngestedEventsDetail(BaseValidatorModel):
    ingestedEventsTimeWindow: IngestedEventsTimeWindow


class TrainingDataSchemaOutput(BaseValidatorModel):
    modelVariables: List[str]
    labelSchema: Optional[LabelSchemaOutput] = None


class TrainingDataSchema(BaseValidatorModel):
    modelVariables: List[str]
    labelSchema: Optional[LabelSchema] = None


# This class is the input for the 'list_event_predictions' function.
class ListEventPredictionsRequest(BaseValidatorModel):
    eventId: Optional[FilterCondition] = None
    eventType: Optional[FilterCondition] = None
    detectorId: Optional[FilterCondition] = None
    detectorVersionId: Optional[FilterCondition] = None
    predictionTimeRange: Optional[PredictionTimeRange] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class VariableImportanceMetrics(BaseValidatorModel):
    logOddsMetrics: Optional[List[LogOddsMetric]] = None


class TrainingMetrics(BaseValidatorModel):
    auc: Optional[float] = None
    metricDataPoints: Optional[List[MetricDataPoint]] = None

ModelOutputConfigurationUnion = Union[ModelOutputConfiguration, ModelOutputConfigurationOutput]


class OFIModelPerformance(BaseValidatorModel):
    auc: Optional[float] = None
    uncertaintyRange: Optional[UncertaintyRange] = None


class TFIModelPerformance(BaseValidatorModel):
    auc: Optional[float] = None
    uncertaintyRange: Optional[UncertaintyRange] = None


class PredictionExplanations(BaseValidatorModel):
    variableImpactExplanations: Optional[List[VariableImpactExplanation]] = None
    aggregatedVariablesImpactExplanations: Optional[List[AggregatedVariablesImpactExplanation]] = None


# This class is the input for the 'get_event_prediction' function.
class GetEventPredictionRequest(BaseValidatorModel):
    detectorId: str
    eventId: str
    eventTypeName: str
    entities: List[Entity]
    eventTimestamp: str
    eventVariables: Dict[str, str]
    detectorVersionId: Optional[str] = None
    externalModelEndpointDataBlobs: Optional[Dict[str, ModelEndpointDataBlob]] = None


# This class is the output for the 'get_event' function.
class GetEventResult(BaseValidatorModel):
    event: Event
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_event_types' function.
class GetEventTypesResult(BaseValidatorModel):
    eventTypes: List[EventType]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_event_prediction' function.
class GetEventPredictionResult(BaseValidatorModel):
    modelScores: List[ModelScores]
    ruleResults: List[RuleResult]
    externalModelOutputs: List[ExternalModelOutputs]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_external_models' function.
class GetExternalModelsResult(BaseValidatorModel):
    externalModels: List[ExternalModel]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'update_model_version' function.
class UpdateModelVersionRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    majorVersionNumber: str
    externalEventsDetail: Optional[ExternalEventsDetail] = None
    ingestedEventsDetail: Optional[IngestedEventsDetail] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'get_model_version' function.
class GetModelVersionResult(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    modelVersionNumber: str
    trainingDataSource: TrainingDataSourceEnumType
    trainingDataSchema: TrainingDataSchemaOutput
    externalEventsDetail: ExternalEventsDetail
    ingestedEventsDetail: IngestedEventsDetail
    status: str
    arn: str
    ResponseMetadata: ResponseMetadata

TrainingDataSchemaUnion = Union[TrainingDataSchema, TrainingDataSchemaOutput]


class TrainingResult(BaseValidatorModel):
    dataValidationMetrics: Optional[DataValidationMetrics] = None
    trainingMetrics: Optional[TrainingMetrics] = None
    variableImportanceMetrics: Optional[VariableImportanceMetrics] = None


class PutExternalModelRequest(BaseValidatorModel):
    modelEndpoint: str
    modelSource: Literal['SAGEMAKER']
    invokeModelEndpointRoleArn: str
    inputConfiguration: ModelInputConfiguration
    outputConfiguration: ModelOutputConfigurationUnion
    modelEndpointStatus: ModelEndpointStatusType
    tags: Optional[List[Tag]] = None


class OFITrainingMetricsValue(BaseValidatorModel):
    metricDataPoints: Optional[List[OFIMetricDataPoint]] = None
    modelPerformance: Optional[OFIModelPerformance] = None


class TFITrainingMetricsValue(BaseValidatorModel):
    metricDataPoints: Optional[List[TFIMetricDataPoint]] = None
    modelPerformance: Optional[TFIModelPerformance] = None


class ModelVersionEvaluation(BaseValidatorModel):
    outputVariableName: Optional[str] = None
    evaluationScore: Optional[str] = None
    predictionExplanations: Optional[PredictionExplanations] = None


# This class is the input for the 'create_model_version' function.
class CreateModelVersionRequest(BaseValidatorModel):
    modelId: str
    modelType: ModelTypeEnumType
    trainingDataSource: TrainingDataSourceEnumType
    trainingDataSchema: TrainingDataSchemaUnion
    externalEventsDetail: Optional[ExternalEventsDetail] = None
    ingestedEventsDetail: Optional[IngestedEventsDetail] = None
    tags: Optional[List[Tag]] = None


class TrainingMetricsV2(BaseValidatorModel):
    ofi: Optional[OFITrainingMetricsValue] = None
    tfi: Optional[TFITrainingMetricsValue] = None
    ati: Optional[ATITrainingMetricsValue] = None


class EvaluatedModelVersion(BaseValidatorModel):
    modelId: Optional[str] = None
    modelVersion: Optional[str] = None
    modelType: Optional[str] = None
    evaluations: Optional[List[ModelVersionEvaluation]] = None


class TrainingResultV2(BaseValidatorModel):
    dataValidationMetrics: Optional[DataValidationMetrics] = None
    trainingMetricsV2: Optional[TrainingMetricsV2] = None
    variableImportanceMetrics: Optional[VariableImportanceMetrics] = None
    aggregatedVariablesImportanceMetrics: Optional[AggregatedVariablesImportanceMetrics] = None


# This class is the output for the 'get_event_prediction_metadata' function.
class GetEventPredictionMetadataResult(BaseValidatorModel):
    eventId: str
    eventTypeName: str
    entityId: str
    entityType: str
    eventTimestamp: str
    detectorId: str
    detectorVersionId: str
    detectorVersionStatus: str
    eventVariables: List[EventVariableSummary]
    rules: List[EvaluatedRule]
    ruleExecutionMode: RuleExecutionModeType
    outcomes: List[str]
    evaluatedModelVersions: List[EvaluatedModelVersion]
    evaluatedExternalModels: List[EvaluatedExternalModel]
    predictionTimestamp: str
    ResponseMetadata: ResponseMetadata


class ModelVersionDetail(BaseValidatorModel):
    modelId: Optional[str] = None
    modelType: Optional[ModelTypeEnumType] = None
    modelVersionNumber: Optional[str] = None
    status: Optional[str] = None
    trainingDataSource: Optional[TrainingDataSourceEnumType] = None
    trainingDataSchema: Optional[TrainingDataSchemaOutput] = None
    externalEventsDetail: Optional[ExternalEventsDetail] = None
    ingestedEventsDetail: Optional[IngestedEventsDetail] = None
    trainingResult: Optional[TrainingResult] = None
    lastUpdatedTime: Optional[str] = None
    createdTime: Optional[str] = None
    arn: Optional[str] = None
    trainingResultV2: Optional[TrainingResultV2] = None


# This class is the output for the 'describe_model_versions' function.
class DescribeModelVersionsResult(BaseValidatorModel):
    modelVersionDetails: List[ModelVersionDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None