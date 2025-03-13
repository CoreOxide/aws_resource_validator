from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel, EventStream
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
from aws_resource_validator.pydantic_models.logs_constants import *

class AccountPolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None
    policyType: Optional[PolicyTypeType] = None
    scope: Optional[Literal["ALL"]] = None
    selectionCriteria: Optional[str] = None
    accountId: Optional[str] = None


class AddKeyEntryTypeDef(BaseValidatorModel):
    key: str
    value: str
    overwriteIfExists: Optional[bool] = None


class AnomalyDetectorTypeDef(BaseValidatorModel):
    anomalyDetectorArn: Optional[str] = None
    detectorName: Optional[str] = None
    logGroupArnList: Optional[List[str]] = None
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    anomalyDetectorStatus: Optional[AnomalyDetectorStatusType] = None
    kmsKeyId: Optional[str] = None
    creationTimeStamp: Optional[int] = None
    lastModifiedTimeStamp: Optional[int] = None
    anomalyVisibilityTime: Optional[int] = None


class LogEventTypeDef(BaseValidatorModel):
    timestamp: Optional[int] = None
    message: Optional[str] = None


class PatternTokenTypeDef(BaseValidatorModel):
    dynamicTokenPosition: Optional[int] = None
    isDynamic: Optional[bool] = None
    tokenString: Optional[str] = None
    enumerations: Optional[Dict[str, int]] = None
    inferredTokenName: Optional[str] = None


class AssociateKmsKeyRequestTypeDef(BaseValidatorModel):
    kmsKeyId: str
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None


class CSVOutputTypeDef(BaseValidatorModel):
    quoteCharacter: Optional[str] = None
    delimiter: Optional[str] = None
    columns: Optional[List[str]] = None
    source: Optional[str] = None


class CSVTypeDef(BaseValidatorModel):
    quoteCharacter: Optional[str] = None
    delimiter: Optional[str] = None
    columns: Optional[Sequence[str]] = None
    source: Optional[str] = None


class CancelExportTaskRequestTypeDef(BaseValidatorModel):
    taskId: str


class S3DeliveryConfigurationTypeDef(BaseValidatorModel):
    suffixPath: Optional[str] = None
    enableHiveCompatiblePath: Optional[bool] = None


class RecordFieldTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    mandatory: Optional[bool] = None


class CopyValueEntryTypeDef(BaseValidatorModel):
    source: str
    target: str
    overwriteIfExists: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateExportTaskRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    fromTime: int
    to: int
    destination: str
    taskName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    destinationPrefix: Optional[str] = None


class CreateLogAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    logGroupArnList: Sequence[str]
    detectorName: Optional[str] = None
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    kmsKeyId: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None


class CreateLogGroupRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    logGroupClass: Optional[LogGroupClassType] = None


class CreateLogStreamRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    logStreamName: str


class DateTimeConverterOutputTypeDef(BaseValidatorModel):
    source: str
    target: str
    matchPatterns: List[str]
    targetFormat: Optional[str] = None
    sourceTimezone: Optional[str] = None
    targetTimezone: Optional[str] = None
    locale: Optional[str] = None


class DateTimeConverterTypeDef(BaseValidatorModel):
    source: str
    target: str
    matchPatterns: Sequence[str]
    targetFormat: Optional[str] = None
    sourceTimezone: Optional[str] = None
    targetTimezone: Optional[str] = None
    locale: Optional[str] = None


class DeleteAccountPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyType: PolicyTypeType


class DeleteDataProtectionPolicyRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str


class DeleteDeliveryDestinationPolicyRequestTypeDef(BaseValidatorModel):
    deliveryDestinationName: str


class DeleteDeliveryDestinationRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteDeliverySourceRequestTypeDef(BaseValidatorModel):
    name: str


class DeleteDestinationRequestTypeDef(BaseValidatorModel):
    destinationName: str


class DeleteIndexPolicyRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str


class DeleteIntegrationRequestTypeDef(BaseValidatorModel):
    integrationName: str
    force: Optional[bool] = None


class DeleteKeysOutputTypeDef(BaseValidatorModel):
    withKeys: List[str]


class DeleteKeysTypeDef(BaseValidatorModel):
    withKeys: Sequence[str]


class DeleteLogAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str


class DeleteLogGroupRequestTypeDef(BaseValidatorModel):
    logGroupName: str


class DeleteLogStreamRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    logStreamName: str


class DeleteMetricFilterRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str


class DeleteQueryDefinitionRequestTypeDef(BaseValidatorModel):
    queryDefinitionId: str


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None


class DeleteRetentionPolicyRequestTypeDef(BaseValidatorModel):
    logGroupName: str


class DeleteSubscriptionFilterRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str


class DeleteTransformerRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str


class DeliveryDestinationConfigurationTypeDef(BaseValidatorModel):
    destinationResourceArn: str


class DeliverySourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    service: Optional[str] = None
    logType: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DescribeAccountPoliciesRequestTypeDef(BaseValidatorModel):
    policyType: PolicyTypeType
    policyName: Optional[str] = None
    accountIdentifiers: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeConfigurationTemplatesRequestTypeDef(BaseValidatorModel):
    service: Optional[str] = None
    logTypes: Optional[Sequence[str]] = None
    resourceTypes: Optional[Sequence[str]] = None
    deliveryDestinationTypes: Optional[Sequence[DeliveryDestinationTypeType]] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class DescribeDeliveriesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class DescribeDeliveryDestinationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class DescribeDeliverySourcesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class DescribeDestinationsRequestTypeDef(BaseValidatorModel):
    DestinationNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class DestinationTypeDef(BaseValidatorModel):
    destinationName: Optional[str] = None
    targetArn: Optional[str] = None
    roleArn: Optional[str] = None
    accessPolicy: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[int] = None


class DescribeExportTasksRequestTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class DescribeFieldIndexesRequestTypeDef(BaseValidatorModel):
    logGroupIdentifiers: Sequence[str]
    nextToken: Optional[str] = None


class FieldIndexTypeDef(BaseValidatorModel):
    logGroupIdentifier: Optional[str] = None
    fieldIndexName: Optional[str] = None
    lastScanTime: Optional[int] = None
    firstEventTime: Optional[int] = None
    lastEventTime: Optional[int] = None


class DescribeIndexPoliciesRequestTypeDef(BaseValidatorModel):
    logGroupIdentifiers: Sequence[str]
    nextToken: Optional[str] = None


class IndexPolicyTypeDef(BaseValidatorModel):
    logGroupIdentifier: Optional[str] = None
    lastUpdateTime: Optional[int] = None
    policyDocument: Optional[str] = None
    policyName: Optional[str] = None
    source: Optional[IndexSourceType] = None


class DescribeLogGroupsRequestTypeDef(BaseValidatorModel):
    accountIdentifiers: Optional[Sequence[str]] = None
    logGroupNamePrefix: Optional[str] = None
    logGroupNamePattern: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    includeLinkedAccounts: Optional[bool] = None
    logGroupClass: Optional[LogGroupClassType] = None


class LogGroupTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    creationTime: Optional[int] = None
    retentionInDays: Optional[int] = None
    metricFilterCount: Optional[int] = None
    arn: Optional[str] = None
    storedBytes: Optional[int] = None
    kmsKeyId: Optional[str] = None
    dataProtectionStatus: Optional[DataProtectionStatusType] = None
    inheritedProperties: Optional[List[Literal["ACCOUNT_DATA_PROTECTION"]]] = None
    logGroupClass: Optional[LogGroupClassType] = None
    logGroupArn: Optional[str] = None


class DescribeLogStreamsRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    orderBy: Optional[OrderByType] = None
    descending: Optional[bool] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class LogStreamTypeDef(BaseValidatorModel):
    logStreamName: Optional[str] = None
    creationTime: Optional[int] = None
    firstEventTimestamp: Optional[int] = None
    lastEventTimestamp: Optional[int] = None
    lastIngestionTime: Optional[int] = None
    uploadSequenceToken: Optional[str] = None
    arn: Optional[str] = None
    storedBytes: Optional[int] = None


class DescribeMetricFiltersRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None


class DescribeQueriesRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    queryLanguage: Optional[QueryLanguageType] = None


class QueryInfoTypeDef(BaseValidatorModel):
    queryLanguage: Optional[QueryLanguageType] = None
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    status: Optional[QueryStatusType] = None
    createTime: Optional[int] = None
    logGroupName: Optional[str] = None


class DescribeQueryDefinitionsRequestTypeDef(BaseValidatorModel):
    queryLanguage: Optional[QueryLanguageType] = None
    queryDefinitionNamePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class QueryDefinitionTypeDef(BaseValidatorModel):
    queryLanguage: Optional[QueryLanguageType] = None
    queryDefinitionId: Optional[str] = None
    name: Optional[str] = None
    queryString: Optional[str] = None
    lastModified: Optional[int] = None
    logGroupNames: Optional[List[str]] = None


class DescribeResourcePoliciesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class ResourcePolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None


class DescribeSubscriptionFiltersRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class SubscriptionFilterTypeDef(BaseValidatorModel):
    filterName: Optional[str] = None
    logGroupName: Optional[str] = None
    filterPattern: Optional[str] = None
    destinationArn: Optional[str] = None
    roleArn: Optional[str] = None
    distribution: Optional[DistributionType] = None
    applyOnTransformedLogs: Optional[bool] = None
    creationTime: Optional[int] = None


class DisassociateKmsKeyRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None


class EntityTypeDef(BaseValidatorModel):
    keyAttributes: Optional[Mapping[str, str]] = None
    attributes: Optional[Mapping[str, str]] = None


class ExportTaskExecutionInfoTypeDef(BaseValidatorModel):
    creationTime: Optional[int] = None
    completionTime: Optional[int] = None


class ExportTaskStatusTypeDef(BaseValidatorModel):
    code: Optional[ExportTaskStatusCodeType] = None
    message: Optional[str] = None


class FilterLogEventsRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNames: Optional[Sequence[str]] = None
    logStreamNamePrefix: Optional[str] = None
    startTime: Optional[int] = None
    endTime: Optional[int] = None
    filterPattern: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    interleaved: Optional[bool] = None
    unmask: Optional[bool] = None


class FilteredLogEventTypeDef(BaseValidatorModel):
    logStreamName: Optional[str] = None
    timestamp: Optional[int] = None
    message: Optional[str] = None
    ingestionTime: Optional[int] = None
    eventId: Optional[str] = None


class SearchedLogStreamTypeDef(BaseValidatorModel):
    logStreamName: Optional[str] = None
    searchedCompletely: Optional[bool] = None


class GetDataProtectionPolicyRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str


class GetDeliveryDestinationPolicyRequestTypeDef(BaseValidatorModel):
    deliveryDestinationName: str


class PolicyTypeDef(BaseValidatorModel):
    deliveryDestinationPolicy: Optional[str] = None


class GetDeliveryDestinationRequestTypeDef(BaseValidatorModel):
    name: str


class GetDeliverySourceRequestTypeDef(BaseValidatorModel):
    name: str


class GetIntegrationRequestTypeDef(BaseValidatorModel):
    integrationName: str


class GetLogAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str


class GetLogEventsRequestTypeDef(BaseValidatorModel):
    logStreamName: str
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    startTime: Optional[int] = None
    endTime: Optional[int] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    startFromHead: Optional[bool] = None
    unmask: Optional[bool] = None


class OutputLogEventTypeDef(BaseValidatorModel):
    timestamp: Optional[int] = None
    message: Optional[str] = None
    ingestionTime: Optional[int] = None


class GetLogGroupFieldsRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    time: Optional[int] = None
    logGroupIdentifier: Optional[str] = None


class LogGroupFieldTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    percent: Optional[int] = None


class GetLogRecordRequestTypeDef(BaseValidatorModel):
    logRecordPointer: str
    unmask: Optional[bool] = None


class GetQueryResultsRequestTypeDef(BaseValidatorModel):
    queryId: str


class QueryStatisticsTypeDef(BaseValidatorModel):
    recordsMatched: Optional[float] = None
    recordsScanned: Optional[float] = None
    estimatedRecordsSkipped: Optional[float] = None
    bytesScanned: Optional[float] = None
    estimatedBytesSkipped: Optional[float] = None
    logGroupsScanned: Optional[float] = None


class ResultFieldTypeDef(BaseValidatorModel):
    field: Optional[str] = None
    value: Optional[str] = None


class GetTransformerRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str


class GrokTypeDef(BaseValidatorModel):
    match: str
    source: Optional[str] = None


class InputLogEventTypeDef(BaseValidatorModel):
    timestamp: int
    message: str


class IntegrationSummaryTypeDef(BaseValidatorModel):
    integrationName: Optional[str] = None
    integrationType: Optional[Literal["OPENSEARCH"]] = None
    integrationStatus: Optional[IntegrationStatusType] = None


class ListAnomaliesRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class ListIntegrationsRequestTypeDef(BaseValidatorModel):
    integrationNamePrefix: Optional[str] = None
    integrationType: Optional[Literal["OPENSEARCH"]] = None
    integrationStatus: Optional[IntegrationStatusType] = None


class ListLogAnomalyDetectorsRequestTypeDef(BaseValidatorModel):
    filterLogGroupArn: Optional[str] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None


class ListLogGroupsForQueryRequestTypeDef(BaseValidatorModel):
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTagsLogGroupRequestTypeDef(BaseValidatorModel):
    logGroupName: str


class ListToMapTypeDef(BaseValidatorModel):
    source: str
    key: str
    valueKey: Optional[str] = None
    target: Optional[str] = None
    flatten: Optional[bool] = None
    flattenedElement: Optional[FlattenedElementType] = None


class LiveTailSessionLogEventTypeDef(BaseValidatorModel):
    logStreamName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    message: Optional[str] = None
    timestamp: Optional[int] = None
    ingestionTime: Optional[int] = None


class LiveTailSessionMetadataTypeDef(BaseValidatorModel):
    sampled: Optional[bool] = None


class LiveTailSessionStartTypeDef(BaseValidatorModel):
    requestId: Optional[str] = None
    sessionId: Optional[str] = None
    logGroupIdentifiers: Optional[List[str]] = None
    logStreamNames: Optional[List[str]] = None
    logStreamNamePrefixes: Optional[List[str]] = None
    logEventFilterPattern: Optional[str] = None


class LowerCaseStringOutputTypeDef(BaseValidatorModel):
    withKeys: List[str]


class LowerCaseStringTypeDef(BaseValidatorModel):
    withKeys: Sequence[str]


class MetricFilterMatchRecordTypeDef(BaseValidatorModel):
    eventNumber: Optional[int] = None
    eventMessage: Optional[str] = None
    extractedValues: Optional[Dict[str, str]] = None


class MetricTransformationOutputTypeDef(BaseValidatorModel):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: Optional[float] = None
    dimensions: Optional[Dict[str, str]] = None
    unit: Optional[StandardUnitType] = None


class MetricTransformationTypeDef(BaseValidatorModel):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: Optional[float] = None
    dimensions: Optional[Mapping[str, str]] = None
    unit: Optional[StandardUnitType] = None


class MoveKeyEntryTypeDef(BaseValidatorModel):
    source: str
    target: str
    overwriteIfExists: Optional[bool] = None


class OpenSearchResourceStatusTypeDef(BaseValidatorModel):
    status: Optional[OpenSearchResourceStatusTypeType] = None
    statusMessage: Optional[str] = None


class OpenSearchResourceConfigTypeDef(BaseValidatorModel):
    dataSourceRoleArn: str
    dashboardViewerPrincipals: Sequence[str]
    retentionDays: int
    kmsKeyArn: Optional[str] = None
    applicationArn: Optional[str] = None


class ParseCloudfrontTypeDef(BaseValidatorModel):
    source: Optional[str] = None


class ParseJSONTypeDef(BaseValidatorModel):
    source: Optional[str] = None
    destination: Optional[str] = None


class ParseKeyValueTypeDef(BaseValidatorModel):
    source: Optional[str] = None
    destination: Optional[str] = None
    fieldDelimiter: Optional[str] = None
    keyValueDelimiter: Optional[str] = None
    keyPrefix: Optional[str] = None
    nonMatchValue: Optional[str] = None
    overwriteIfExists: Optional[bool] = None


class ParsePostgresTypeDef(BaseValidatorModel):
    source: Optional[str] = None


class ParseRoute53TypeDef(BaseValidatorModel):
    source: Optional[str] = None


class ParseVPCTypeDef(BaseValidatorModel):
    source: Optional[str] = None


class ParseWAFTypeDef(BaseValidatorModel):
    source: Optional[str] = None


class TrimStringOutputTypeDef(BaseValidatorModel):
    withKeys: List[str]


class UpperCaseStringOutputTypeDef(BaseValidatorModel):
    withKeys: List[str]


class PutAccountPolicyRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyDocument: str
    policyType: PolicyTypeType
    scope: Optional[Literal["ALL"]] = None
    selectionCriteria: Optional[str] = None


class PutDataProtectionPolicyRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str


class PutDeliveryDestinationPolicyRequestTypeDef(BaseValidatorModel):
    deliveryDestinationName: str
    deliveryDestinationPolicy: str


class PutDeliverySourceRequestTypeDef(BaseValidatorModel):
    name: str
    resourceArn: str
    logType: str
    tags: Optional[Mapping[str, str]] = None


class PutDestinationPolicyRequestTypeDef(BaseValidatorModel):
    destinationName: str
    accessPolicy: str
    forceUpdate: Optional[bool] = None


class PutDestinationRequestTypeDef(BaseValidatorModel):
    destinationName: str
    targetArn: str
    roleArn: str
    tags: Optional[Mapping[str, str]] = None


class PutIndexPolicyRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str


class RejectedEntityInfoTypeDef(BaseValidatorModel):
    errorType: EntityRejectionErrorTypeType


class RejectedLogEventsInfoTypeDef(BaseValidatorModel):
    tooNewLogEventStartIndex: Optional[int] = None
    tooOldLogEventEndIndex: Optional[int] = None
    expiredLogEventEndIndex: Optional[int] = None


class PutQueryDefinitionRequestTypeDef(BaseValidatorModel):
    name: str
    queryString: str
    queryLanguage: Optional[QueryLanguageType] = None
    queryDefinitionId: Optional[str] = None
    logGroupNames: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None


class PutRetentionPolicyRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    retentionInDays: int


class PutSubscriptionFilterRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    destinationArn: str
    roleArn: Optional[str] = None
    distribution: Optional[DistributionType] = None
    applyOnTransformedLogs: Optional[bool] = None


class RenameKeyEntryTypeDef(BaseValidatorModel):
    key: str
    renameTo: str
    overwriteIfExists: Optional[bool] = None


class SessionStreamingExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class SessionTimeoutExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None


class SplitStringEntryTypeDef(BaseValidatorModel):
    source: str
    delimiter: str


class StartLiveTailRequestTypeDef(BaseValidatorModel):
    logGroupIdentifiers: Sequence[str]
    logStreamNames: Optional[Sequence[str]] = None
    logStreamNamePrefixes: Optional[Sequence[str]] = None
    logEventFilterPattern: Optional[str] = None


class StartQueryRequestTypeDef(BaseValidatorModel):
    startTime: int
    endTime: int
    queryString: str
    queryLanguage: Optional[QueryLanguageType] = None
    logGroupName: Optional[str] = None
    logGroupNames: Optional[Sequence[str]] = None
    logGroupIdentifiers: Optional[Sequence[str]] = None
    limit: Optional[int] = None


class StopQueryRequestTypeDef(BaseValidatorModel):
    queryId: str


class SuppressionPeriodTypeDef(BaseValidatorModel):
    value: Optional[int] = None
    suppressionUnit: Optional[SuppressionUnitType] = None


class TagLogGroupRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    tags: Mapping[str, str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TestMetricFilterRequestTypeDef(BaseValidatorModel):
    filterPattern: str
    logEventMessages: Sequence[str]


class TransformedLogRecordTypeDef(BaseValidatorModel):
    eventNumber: Optional[int] = None
    eventMessage: Optional[str] = None
    transformedEventMessage: Optional[str] = None


class TrimStringTypeDef(BaseValidatorModel):
    withKeys: Sequence[str]


class UntagLogGroupRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    tags: Sequence[str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateLogAnomalyDetectorRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str
    enabled: bool
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None


class UpperCaseStringTypeDef(BaseValidatorModel):
    withKeys: Sequence[str]


class AddKeysOutputTypeDef(BaseValidatorModel):
    entries: List[AddKeyEntryTypeDef]


class AddKeysTypeDef(BaseValidatorModel):
    entries: Sequence[AddKeyEntryTypeDef]


class AnomalyTypeDef(BaseValidatorModel):
    anomalyId: str
    patternId: str
    anomalyDetectorArn: str
    patternString: str
    firstSeen: int
    lastSeen: int
    description: str
    active: bool
    state: StateType
    histogram: Dict[str, int]
    logSamples: List[LogEventTypeDef]
    patternTokens: List[PatternTokenTypeDef]
    logGroupArnList: List[str]
    patternRegex: Optional[str] = None
    priority: Optional[str] = None
    suppressed: Optional[bool] = None
    suppressedDate: Optional[int] = None
    suppressedUntil: Optional[int] = None
    isPatternLevelSuppression: Optional[bool] = None


class ConfigurationTemplateDeliveryConfigValuesTypeDef(BaseValidatorModel):
    recordFields: Optional[List[str]] = None
    fieldDelimiter: Optional[str] = None
    s3DeliveryConfiguration: Optional[S3DeliveryConfigurationTypeDef] = None


class CreateDeliveryRequestTypeDef(BaseValidatorModel):
    deliverySourceName: str
    deliveryDestinationArn: str
    recordFields: Optional[Sequence[str]] = None
    fieldDelimiter: Optional[str] = None
    s3DeliveryConfiguration: Optional[S3DeliveryConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class CopyValueOutputTypeDef(BaseValidatorModel):
    entries: List[CopyValueEntryTypeDef]


class CopyValueTypeDef(BaseValidatorModel):
    entries: Sequence[CopyValueEntryTypeDef]


class CreateExportTaskResponseTypeDef(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLogAnomalyDetectorResponseTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteQueryDefinitionResponseTypeDef(BaseValidatorModel):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAccountPoliciesResponseTypeDef(BaseValidatorModel):
    accountPolicies: List[AccountPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataProtectionPolicyResponseTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetLogAnomalyDetectorResponseTypeDef(BaseValidatorModel):
    detectorName: str
    logGroupArnList: List[str]
    evaluationFrequency: EvaluationFrequencyType
    filterPattern: str
    anomalyDetectorStatus: AnomalyDetectorStatusType
    kmsKeyId: str
    creationTimeStamp: int
    lastModifiedTimeStamp: int
    anomalyVisibilityTime: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetLogRecordResponseTypeDef(BaseValidatorModel):
    logRecord: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListLogAnomalyDetectorsResponseTypeDef(BaseValidatorModel):
    anomalyDetectors: List[AnomalyDetectorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListLogGroupsForQueryResponseTypeDef(BaseValidatorModel):
    logGroupIdentifiers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsLogGroupResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutAccountPolicyResponseTypeDef(BaseValidatorModel):
    accountPolicy: AccountPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutDataProtectionPolicyResponseTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadataTypeDef


class PutIntegrationResponseTypeDef(BaseValidatorModel):
    integrationName: str
    integrationStatus: IntegrationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class PutQueryDefinitionResponseTypeDef(BaseValidatorModel):
    queryDefinitionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartQueryResponseTypeDef(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopQueryResponseTypeDef(BaseValidatorModel):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef


class DeliveryDestinationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    outputFormat: Optional[OutputFormatType] = None
    deliveryDestinationConfiguration: Optional[DeliveryDestinationConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None


class PutDeliveryDestinationRequestTypeDef(BaseValidatorModel):
    name: str
    deliveryDestinationConfiguration: DeliveryDestinationConfigurationTypeDef
    outputFormat: Optional[OutputFormatType] = None
    tags: Optional[Mapping[str, str]] = None


class DescribeDeliverySourcesResponseTypeDef(BaseValidatorModel):
    deliverySources: List[DeliverySourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetDeliverySourceResponseTypeDef(BaseValidatorModel):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutDeliverySourceResponseTypeDef(BaseValidatorModel):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConfigurationTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    service: Optional[str] = None
    logTypes: Optional[Sequence[str]] = None
    resourceTypes: Optional[Sequence[str]] = None
    deliveryDestinationTypes: Optional[Sequence[DeliveryDestinationTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDeliveriesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDeliveryDestinationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDeliverySourcesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDestinationsRequestPaginateTypeDef(BaseValidatorModel):
    DestinationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeExportTasksRequestPaginateTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeLogGroupsRequestPaginateTypeDef(BaseValidatorModel):
    accountIdentifiers: Optional[Sequence[str]] = None
    logGroupNamePrefix: Optional[str] = None
    logGroupNamePattern: Optional[str] = None
    includeLinkedAccounts: Optional[bool] = None
    logGroupClass: Optional[LogGroupClassType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeLogStreamsRequestPaginateTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    orderBy: Optional[OrderByType] = None
    descending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMetricFiltersRequestPaginateTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeQueriesRequestPaginateTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    queryLanguage: Optional[QueryLanguageType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeResourcePoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSubscriptionFiltersRequestPaginateTypeDef(BaseValidatorModel):
    logGroupName: str
    filterNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class FilterLogEventsRequestPaginateTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNames: Optional[Sequence[str]] = None
    logStreamNamePrefix: Optional[str] = None
    startTime: Optional[int] = None
    endTime: Optional[int] = None
    filterPattern: Optional[str] = None
    interleaved: Optional[bool] = None
    unmask: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAnomaliesRequestPaginateTypeDef(BaseValidatorModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLogAnomalyDetectorsRequestPaginateTypeDef(BaseValidatorModel):
    filterLogGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLogGroupsForQueryRequestPaginateTypeDef(BaseValidatorModel):
    queryId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDestinationsResponseTypeDef(BaseValidatorModel):
    destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutDestinationResponseTypeDef(BaseValidatorModel):
    destination: DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeFieldIndexesResponseTypeDef(BaseValidatorModel):
    fieldIndexes: List[FieldIndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeIndexPoliciesResponseTypeDef(BaseValidatorModel):
    indexPolicies: List[IndexPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutIndexPolicyResponseTypeDef(BaseValidatorModel):
    indexPolicy: IndexPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeLogGroupsResponseTypeDef(BaseValidatorModel):
    logGroups: List[LogGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeLogStreamsResponseTypeDef(BaseValidatorModel):
    logStreams: List[LogStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeQueriesResponseTypeDef(BaseValidatorModel):
    queries: List[QueryInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeQueryDefinitionsResponseTypeDef(BaseValidatorModel):
    queryDefinitions: List[QueryDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeResourcePoliciesResponseTypeDef(BaseValidatorModel):
    resourcePolicies: List[ResourcePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSubscriptionFiltersResponseTypeDef(BaseValidatorModel):
    subscriptionFilters: List[SubscriptionFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FilterLogEventsResponseTypeDef(BaseValidatorModel):
    events: List[FilteredLogEventTypeDef]
    searchedLogStreams: List[SearchedLogStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetDeliveryDestinationPolicyResponseTypeDef(BaseValidatorModel):
    policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutDeliveryDestinationPolicyResponseTypeDef(BaseValidatorModel):
    policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLogEventsResponseTypeDef(BaseValidatorModel):
    events: List[OutputLogEventTypeDef]
    nextForwardToken: str
    nextBackwardToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetLogGroupFieldsResponseTypeDef(BaseValidatorModel):
    logGroupFields: List[LogGroupFieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueryResultsResponseTypeDef(BaseValidatorModel):
    queryLanguage: QueryLanguageType
    results: List[List[ResultFieldTypeDef]]
    statistics: QueryStatisticsTypeDef
    status: QueryStatusType
    encryptionKey: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutLogEventsRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    logStreamName: str
    logEvents: Sequence[InputLogEventTypeDef]
    sequenceToken: Optional[str] = None
    entity: Optional[EntityTypeDef] = None


class ListIntegrationsResponseTypeDef(BaseValidatorModel):
    integrationSummaries: List[IntegrationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LiveTailSessionUpdateTypeDef(BaseValidatorModel):
    sessionMetadata: Optional[LiveTailSessionMetadataTypeDef] = None
    sessionResults: Optional[List[LiveTailSessionLogEventTypeDef]] = None


class TestMetricFilterResponseTypeDef(BaseValidatorModel):
    matches: List[MetricFilterMatchRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class MetricFilterTypeDef(BaseValidatorModel):
    filterName: Optional[str] = None
    filterPattern: Optional[str] = None
    metricTransformations: Optional[List[MetricTransformationOutputTypeDef]] = None
    creationTime: Optional[int] = None
    logGroupName: Optional[str] = None
    applyOnTransformedLogs: Optional[bool] = None


class MoveKeysOutputTypeDef(BaseValidatorModel):
    entries: List[MoveKeyEntryTypeDef]


class MoveKeysTypeDef(BaseValidatorModel):
    entries: Sequence[MoveKeyEntryTypeDef]


class OpenSearchApplicationTypeDef(BaseValidatorModel):
    applicationEndpoint: Optional[str] = None
    applicationArn: Optional[str] = None
    applicationId: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class OpenSearchCollectionTypeDef(BaseValidatorModel):
    collectionEndpoint: Optional[str] = None
    collectionArn: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class OpenSearchDataAccessPolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class OpenSearchDataSourceTypeDef(BaseValidatorModel):
    dataSourceName: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class OpenSearchEncryptionPolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class OpenSearchLifecyclePolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class OpenSearchNetworkPolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class OpenSearchWorkspaceTypeDef(BaseValidatorModel):
    workspaceId: Optional[str] = None
    status: Optional[OpenSearchResourceStatusTypeDef] = None


class ResourceConfigTypeDef(BaseValidatorModel):
    openSearchResourceConfig: Optional[OpenSearchResourceConfigTypeDef] = None


class PutLogEventsResponseTypeDef(BaseValidatorModel):
    nextSequenceToken: str
    rejectedLogEventsInfo: RejectedLogEventsInfoTypeDef
    rejectedEntityInfo: RejectedEntityInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RenameKeysOutputTypeDef(BaseValidatorModel):
    entries: List[RenameKeyEntryTypeDef]


class RenameKeysTypeDef(BaseValidatorModel):
    entries: Sequence[RenameKeyEntryTypeDef]


class SplitStringOutputTypeDef(BaseValidatorModel):
    entries: List[SplitStringEntryTypeDef]


class SplitStringTypeDef(BaseValidatorModel):
    entries: Sequence[SplitStringEntryTypeDef]


class SubstituteStringEntryTypeDef(BaseValidatorModel):
    pass


class SubstituteStringOutputTypeDef(BaseValidatorModel):
    entries: List[SubstituteStringEntryTypeDef]


class SubstituteStringTypeDef(BaseValidatorModel):
    entries: Sequence[SubstituteStringEntryTypeDef]


class UpdateAnomalyRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str
    anomalyId: Optional[str] = None
    patternId: Optional[str] = None
    suppressionType: Optional[SuppressionTypeType] = None
    suppressionPeriod: Optional[SuppressionPeriodTypeDef] = None
    baseline: Optional[bool] = None


class TestTransformerResponseTypeDef(BaseValidatorModel):
    transformedLogs: List[TransformedLogRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TypeConverterEntryTypeDef(BaseValidatorModel):
    pass


class TypeConverterOutputTypeDef(BaseValidatorModel):
    entries: List[TypeConverterEntryTypeDef]


class TypeConverterTypeDef(BaseValidatorModel):
    entries: Sequence[TypeConverterEntryTypeDef]


class ListAnomaliesResponseTypeDef(BaseValidatorModel):
    anomalies: List[AnomalyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConfigurationTemplateTypeDef(BaseValidatorModel):
    service: Optional[str] = None
    logType: Optional[str] = None
    resourceType: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    defaultDeliveryConfigValues: Optional[ConfigurationTemplateDeliveryConfigValuesTypeDef] = None
    allowedFields: Optional[List[RecordFieldTypeDef]] = None
    allowedOutputFormats: Optional[List[OutputFormatType]] = None
    allowedActionForAllowVendedLogsDeliveryForResource: Optional[str] = None
    allowedFieldDelimiters: Optional[List[str]] = None
    allowedSuffixPathFields: Optional[List[str]] = None


class DeliveryTypeDef(BaseValidatorModel):
    pass


class CreateDeliveryResponseTypeDef(BaseValidatorModel):
    delivery: DeliveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDeliveriesResponseTypeDef(BaseValidatorModel):
    deliveries: List[DeliveryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetDeliveryResponseTypeDef(BaseValidatorModel):
    delivery: DeliveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDeliveryDestinationsResponseTypeDef(BaseValidatorModel):
    deliveryDestinations: List[DeliveryDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetDeliveryDestinationResponseTypeDef(BaseValidatorModel):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutDeliveryDestinationResponseTypeDef(BaseValidatorModel):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportTaskTypeDef(BaseValidatorModel):
    pass


class DescribeExportTasksResponseTypeDef(BaseValidatorModel):
    exportTasks: List[ExportTaskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartLiveTailResponseStreamTypeDef(BaseValidatorModel):
    sessionStart: Optional[LiveTailSessionStartTypeDef] = None
    sessionUpdate: Optional[LiveTailSessionUpdateTypeDef] = None
    SessionTimeoutException: Optional[SessionTimeoutExceptionTypeDef] = None
    SessionStreamingException: Optional[SessionStreamingExceptionTypeDef] = None


class DescribeMetricFiltersResponseTypeDef(BaseValidatorModel):
    metricFilters: List[MetricFilterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MetricTransformationUnionTypeDef(BaseValidatorModel):
    pass


class PutMetricFilterRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    metricTransformations: Sequence[MetricTransformationUnionTypeDef]
    applyOnTransformedLogs: Optional[bool] = None


class OpenSearchIntegrationDetailsTypeDef(BaseValidatorModel):
    dataSource: Optional[OpenSearchDataSourceTypeDef] = None
    application: Optional[OpenSearchApplicationTypeDef] = None
    collection: Optional[OpenSearchCollectionTypeDef] = None
    workspace: Optional[OpenSearchWorkspaceTypeDef] = None
    encryptionPolicy: Optional[OpenSearchEncryptionPolicyTypeDef] = None
    networkPolicy: Optional[OpenSearchNetworkPolicyTypeDef] = None
    accessPolicy: Optional[OpenSearchDataAccessPolicyTypeDef] = None
    lifecyclePolicy: Optional[OpenSearchLifecyclePolicyTypeDef] = None


class PutIntegrationRequestTypeDef(BaseValidatorModel):
    integrationName: str
    resourceConfig: ResourceConfigTypeDef
    integrationType: Literal["OPENSEARCH"]


class ProcessorOutputTypeDef(BaseValidatorModel):
    addKeys: Optional[AddKeysOutputTypeDef] = None
    copyValue: Optional[CopyValueOutputTypeDef] = None
    csv: Optional[CSVOutputTypeDef] = None
    dateTimeConverter: Optional[DateTimeConverterOutputTypeDef] = None
    deleteKeys: Optional[DeleteKeysOutputTypeDef] = None
    grok: Optional[GrokTypeDef] = None
    listToMap: Optional[ListToMapTypeDef] = None
    lowerCaseString: Optional[LowerCaseStringOutputTypeDef] = None
    moveKeys: Optional[MoveKeysOutputTypeDef] = None
    parseCloudfront: Optional[ParseCloudfrontTypeDef] = None
    parseJSON: Optional[ParseJSONTypeDef] = None
    parseKeyValue: Optional[ParseKeyValueTypeDef] = None
    parseRoute53: Optional[ParseRoute53TypeDef] = None
    parsePostgres: Optional[ParsePostgresTypeDef] = None
    parseVPC: Optional[ParseVPCTypeDef] = None
    parseWAF: Optional[ParseWAFTypeDef] = None
    renameKeys: Optional[RenameKeysOutputTypeDef] = None
    splitString: Optional[SplitStringOutputTypeDef] = None
    substituteString: Optional[SubstituteStringOutputTypeDef] = None
    trimString: Optional[TrimStringOutputTypeDef] = None
    typeConverter: Optional[TypeConverterOutputTypeDef] = None
    upperCaseString: Optional[UpperCaseStringOutputTypeDef] = None


class DescribeConfigurationTemplatesResponseTypeDef(BaseValidatorModel):
    configurationTemplates: List[ConfigurationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartLiveTailResponseTypeDef(BaseValidatorModel):
    responseStream: EventStream[StartLiveTailResponseStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class IntegrationDetailsTypeDef(BaseValidatorModel):
    openSearchIntegrationDetails: Optional[OpenSearchIntegrationDetailsTypeDef] = None


class GetTransformerResponseTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    creationTime: int
    lastModifiedTime: int
    transformerConfig: List[ProcessorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CSVUnionTypeDef(BaseValidatorModel):
    pass


class TypeConverterUnionTypeDef(BaseValidatorModel):
    pass


class SplitStringUnionTypeDef(BaseValidatorModel):
    pass


class SubstituteStringUnionTypeDef(BaseValidatorModel):
    pass


class LowerCaseStringUnionTypeDef(BaseValidatorModel):
    pass


class CopyValueUnionTypeDef(BaseValidatorModel):
    pass


class AddKeysUnionTypeDef(BaseValidatorModel):
    pass


class DeleteKeysUnionTypeDef(BaseValidatorModel):
    pass


class DateTimeConverterUnionTypeDef(BaseValidatorModel):
    pass


class TrimStringUnionTypeDef(BaseValidatorModel):
    pass


class RenameKeysUnionTypeDef(BaseValidatorModel):
    pass


class UpperCaseStringUnionTypeDef(BaseValidatorModel):
    pass


class MoveKeysUnionTypeDef(BaseValidatorModel):
    pass


class ProcessorTypeDef(BaseValidatorModel):
    addKeys: Optional[AddKeysUnionTypeDef] = None
    copyValue: Optional[CopyValueUnionTypeDef] = None
    csv: Optional[CSVUnionTypeDef] = None
    dateTimeConverter: Optional[DateTimeConverterUnionTypeDef] = None
    deleteKeys: Optional[DeleteKeysUnionTypeDef] = None
    grok: Optional[GrokTypeDef] = None
    listToMap: Optional[ListToMapTypeDef] = None
    lowerCaseString: Optional[LowerCaseStringUnionTypeDef] = None
    moveKeys: Optional[MoveKeysUnionTypeDef] = None
    parseCloudfront: Optional[ParseCloudfrontTypeDef] = None
    parseJSON: Optional[ParseJSONTypeDef] = None
    parseKeyValue: Optional[ParseKeyValueTypeDef] = None
    parseRoute53: Optional[ParseRoute53TypeDef] = None
    parsePostgres: Optional[ParsePostgresTypeDef] = None
    parseVPC: Optional[ParseVPCTypeDef] = None
    parseWAF: Optional[ParseWAFTypeDef] = None
    renameKeys: Optional[RenameKeysUnionTypeDef] = None
    splitString: Optional[SplitStringUnionTypeDef] = None
    substituteString: Optional[SubstituteStringUnionTypeDef] = None
    trimString: Optional[TrimStringUnionTypeDef] = None
    typeConverter: Optional[TypeConverterUnionTypeDef] = None
    upperCaseString: Optional[UpperCaseStringUnionTypeDef] = None


class GetIntegrationResponseTypeDef(BaseValidatorModel):
    integrationName: str
    integrationType: Literal["OPENSEARCH"]
    integrationStatus: IntegrationStatusType
    integrationDetails: IntegrationDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ProcessorUnionTypeDef(BaseValidatorModel):
    pass


class PutTransformerRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    transformerConfig: Sequence[ProcessorUnionTypeDef]


class TestTransformerRequestTypeDef(BaseValidatorModel):
    transformerConfig: Sequence[ProcessorUnionTypeDef]
    logEventMessages: Sequence[str]


