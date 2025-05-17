from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.logs.logs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountPolicy(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None
    policyType: Optional[PolicyTypeType] = None
    scope: Optional[Literal['ALL']] = None
    selectionCriteria: Optional[str] = None
    accountId: Optional[str] = None


class AddKeyEntry(BaseValidatorModel):
    key: str
    value: str
    overwriteIfExists: Optional[bool] = None


class AnomalyDetector(BaseValidatorModel):
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


class LogEvent(BaseValidatorModel):
    timestamp: Optional[int] = None
    message: Optional[str] = None


class PatternToken(BaseValidatorModel):
    dynamicTokenPosition: Optional[int] = None
    isDynamic: Optional[bool] = None
    tokenString: Optional[str] = None
    enumerations: Optional[Dict[str, int]] = None
    inferredTokenName: Optional[str] = None


# This class is the input for the 'associate_kms_key' function.
class AssociateKmsKeyRequest(BaseValidatorModel):
    kmsKeyId: str
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None


class CSVOutput(BaseValidatorModel):
    quoteCharacter: Optional[str] = None
    delimiter: Optional[str] = None
    columns: Optional[List[str]] = None
    source: Optional[str] = None


class CSV(BaseValidatorModel):
    quoteCharacter: Optional[str] = None
    delimiter: Optional[str] = None
    columns: Optional[List[str]] = None
    source: Optional[str] = None


# This class is the input for the 'cancel_export_task' function.
class CancelExportTaskRequest(BaseValidatorModel):
    taskId: str


class S3DeliveryConfiguration(BaseValidatorModel):
    suffixPath: Optional[str] = None
    enableHiveCompatiblePath: Optional[bool] = None


class RecordField(BaseValidatorModel):
    name: Optional[str] = None
    mandatory: Optional[bool] = None


class CopyValueEntry(BaseValidatorModel):
    source: str
    target: str
    overwriteIfExists: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_export_task' function.
class CreateExportTaskRequest(BaseValidatorModel):
    logGroupName: str
    fromTime: int
    to: int
    destination: str
    taskName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    destinationPrefix: Optional[str] = None


# This class is the input for the 'create_log_anomaly_detector' function.
class CreateLogAnomalyDetectorRequest(BaseValidatorModel):
    logGroupArnList: List[str]
    detectorName: Optional[str] = None
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    kmsKeyId: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_log_group' function.
class CreateLogGroupRequest(BaseValidatorModel):
    logGroupName: str
    kmsKeyId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    logGroupClass: Optional[LogGroupClassType] = None


# This class is the input for the 'create_log_stream' function.
class CreateLogStreamRequest(BaseValidatorModel):
    logGroupName: str
    logStreamName: str


class DateTimeConverterOutput(BaseValidatorModel):
    source: str
    target: str
    matchPatterns: List[str]
    targetFormat: Optional[str] = None
    sourceTimezone: Optional[str] = None
    targetTimezone: Optional[str] = None
    locale: Optional[str] = None


class DateTimeConverter(BaseValidatorModel):
    source: str
    target: str
    matchPatterns: List[str]
    targetFormat: Optional[str] = None
    sourceTimezone: Optional[str] = None
    targetTimezone: Optional[str] = None
    locale: Optional[str] = None


# This class is the input for the 'delete_account_policy' function.
class DeleteAccountPolicyRequest(BaseValidatorModel):
    policyName: str
    policyType: PolicyTypeType


# This class is the input for the 'delete_data_protection_policy' function.
class DeleteDataProtectionPolicyRequest(BaseValidatorModel):
    logGroupIdentifier: str


# This class is the input for the 'delete_delivery_destination_policy' function.
class DeleteDeliveryDestinationPolicyRequest(BaseValidatorModel):
    deliveryDestinationName: str


# This class is the input for the 'delete_delivery_destination' function.
class DeleteDeliveryDestinationRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_delivery' function.
class DeleteDeliveryRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'delete_delivery_source' function.
class DeleteDeliverySourceRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'delete_destination' function.
class DeleteDestinationRequest(BaseValidatorModel):
    destinationName: str


class DeleteIndexPolicyRequest(BaseValidatorModel):
    logGroupIdentifier: str


class DeleteIntegrationRequest(BaseValidatorModel):
    integrationName: str
    force: Optional[bool] = None


class DeleteKeysOutput(BaseValidatorModel):
    withKeys: List[str]


class DeleteKeys(BaseValidatorModel):
    withKeys: List[str]


# This class is the input for the 'delete_log_anomaly_detector' function.
class DeleteLogAnomalyDetectorRequest(BaseValidatorModel):
    anomalyDetectorArn: str


# This class is the input for the 'delete_log_group' function.
class DeleteLogGroupRequest(BaseValidatorModel):
    logGroupName: str


# This class is the input for the 'delete_log_stream' function.
class DeleteLogStreamRequest(BaseValidatorModel):
    logGroupName: str
    logStreamName: str


# This class is the input for the 'delete_metric_filter' function.
class DeleteMetricFilterRequest(BaseValidatorModel):
    logGroupName: str
    filterName: str


# This class is the input for the 'delete_query_definition' function.
class DeleteQueryDefinitionRequest(BaseValidatorModel):
    queryDefinitionId: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyRequest(BaseValidatorModel):
    policyName: Optional[str] = None


# This class is the input for the 'delete_retention_policy' function.
class DeleteRetentionPolicyRequest(BaseValidatorModel):
    logGroupName: str


# This class is the input for the 'delete_subscription_filter' function.
class DeleteSubscriptionFilterRequest(BaseValidatorModel):
    logGroupName: str
    filterName: str


# This class is the input for the 'delete_transformer' function.
class DeleteTransformerRequest(BaseValidatorModel):
    logGroupIdentifier: str


class DeliveryDestinationConfiguration(BaseValidatorModel):
    destinationResourceArn: str


class DeliverySource(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    service: Optional[str] = None
    logType: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'describe_account_policies' function.
class DescribeAccountPoliciesRequest(BaseValidatorModel):
    policyType: PolicyTypeType
    policyName: Optional[str] = None
    accountIdentifiers: Optional[List[str]] = None
    nextToken: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_configuration_templates' function.
class DescribeConfigurationTemplatesRequest(BaseValidatorModel):
    service: Optional[str] = None
    logTypes: Optional[List[str]] = None
    resourceTypes: Optional[List[str]] = None
    deliveryDestinationTypes: Optional[List[DeliveryDestinationTypeType]] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'describe_deliveries' function.
class DescribeDeliveriesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'describe_delivery_destinations' function.
class DescribeDeliveryDestinationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'describe_delivery_sources' function.
class DescribeDeliverySourcesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'describe_destinations' function.
class DescribeDestinationsRequest(BaseValidatorModel):
    DestinationNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class Destination(BaseValidatorModel):
    destinationName: Optional[str] = None
    targetArn: Optional[str] = None
    roleArn: Optional[str] = None
    accessPolicy: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[int] = None


# This class is the input for the 'describe_export_tasks' function.
class DescribeExportTasksRequest(BaseValidatorModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


# This class is the input for the 'describe_field_indexes' function.
class DescribeFieldIndexesRequest(BaseValidatorModel):
    logGroupIdentifiers: List[str]
    nextToken: Optional[str] = None


class FieldIndex(BaseValidatorModel):
    logGroupIdentifier: Optional[str] = None
    fieldIndexName: Optional[str] = None
    lastScanTime: Optional[int] = None
    firstEventTime: Optional[int] = None
    lastEventTime: Optional[int] = None


# This class is the input for the 'describe_index_policies' function.
class DescribeIndexPoliciesRequest(BaseValidatorModel):
    logGroupIdentifiers: List[str]
    nextToken: Optional[str] = None


class IndexPolicy(BaseValidatorModel):
    logGroupIdentifier: Optional[str] = None
    lastUpdateTime: Optional[int] = None
    policyDocument: Optional[str] = None
    policyName: Optional[str] = None
    source: Optional[IndexSourceType] = None


# This class is the input for the 'describe_log_groups' function.
class DescribeLogGroupsRequest(BaseValidatorModel):
    accountIdentifiers: Optional[List[str]] = None
    logGroupNamePrefix: Optional[str] = None
    logGroupNamePattern: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    includeLinkedAccounts: Optional[bool] = None
    logGroupClass: Optional[LogGroupClassType] = None


class LogGroup(BaseValidatorModel):
    logGroupName: Optional[str] = None
    creationTime: Optional[int] = None
    retentionInDays: Optional[int] = None
    metricFilterCount: Optional[int] = None
    arn: Optional[str] = None
    storedBytes: Optional[int] = None
    kmsKeyId: Optional[str] = None
    dataProtectionStatus: Optional[DataProtectionStatusType] = None
    inheritedProperties: Optional[List[Literal['ACCOUNT_DATA_PROTECTION']]] = None
    logGroupClass: Optional[LogGroupClassType] = None
    logGroupArn: Optional[str] = None


# This class is the input for the 'describe_log_streams' function.
class DescribeLogStreamsRequest(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    orderBy: Optional[OrderByType] = None
    descending: Optional[bool] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class LogStream(BaseValidatorModel):
    logStreamName: Optional[str] = None
    creationTime: Optional[int] = None
    firstEventTimestamp: Optional[int] = None
    lastEventTimestamp: Optional[int] = None
    lastIngestionTime: Optional[int] = None
    uploadSequenceToken: Optional[str] = None
    arn: Optional[str] = None
    storedBytes: Optional[int] = None


# This class is the input for the 'describe_metric_filters' function.
class DescribeMetricFiltersRequest(BaseValidatorModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None


# This class is the input for the 'describe_queries' function.
class DescribeQueriesRequest(BaseValidatorModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    queryLanguage: Optional[QueryLanguageType] = None


class QueryInfo(BaseValidatorModel):
    queryLanguage: Optional[QueryLanguageType] = None
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    status: Optional[QueryStatusType] = None
    createTime: Optional[int] = None
    logGroupName: Optional[str] = None


# This class is the input for the 'describe_query_definitions' function.
class DescribeQueryDefinitionsRequest(BaseValidatorModel):
    queryLanguage: Optional[QueryLanguageType] = None
    queryDefinitionNamePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class QueryDefinition(BaseValidatorModel):
    queryLanguage: Optional[QueryLanguageType] = None
    queryDefinitionId: Optional[str] = None
    name: Optional[str] = None
    queryString: Optional[str] = None
    lastModified: Optional[int] = None
    logGroupNames: Optional[List[str]] = None


# This class is the input for the 'describe_resource_policies' function.
class DescribeResourcePoliciesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class ResourcePolicy(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None


# This class is the input for the 'describe_subscription_filters' function.
class DescribeSubscriptionFiltersRequest(BaseValidatorModel):
    logGroupName: str
    filterNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None


class SubscriptionFilter(BaseValidatorModel):
    filterName: Optional[str] = None
    logGroupName: Optional[str] = None
    filterPattern: Optional[str] = None
    destinationArn: Optional[str] = None
    roleArn: Optional[str] = None
    distribution: Optional[DistributionType] = None
    applyOnTransformedLogs: Optional[bool] = None
    creationTime: Optional[int] = None


# This class is the input for the 'disassociate_kms_key' function.
class DisassociateKmsKeyRequest(BaseValidatorModel):
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None


class Entity(BaseValidatorModel):
    keyAttributes: Optional[Dict[str, str]] = None
    attributes: Optional[Dict[str, str]] = None


class ExportTaskExecutionInfo(BaseValidatorModel):
    creationTime: Optional[int] = None
    completionTime: Optional[int] = None


class ExportTaskStatus(BaseValidatorModel):
    code: Optional[ExportTaskStatusCodeType] = None
    message: Optional[str] = None


# This class is the input for the 'filter_log_events' function.
class FilterLogEventsRequest(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNames: Optional[List[str]] = None
    logStreamNamePrefix: Optional[str] = None
    startTime: Optional[int] = None
    endTime: Optional[int] = None
    filterPattern: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    interleaved: Optional[bool] = None
    unmask: Optional[bool] = None


class FilteredLogEvent(BaseValidatorModel):
    logStreamName: Optional[str] = None
    timestamp: Optional[int] = None
    message: Optional[str] = None
    ingestionTime: Optional[int] = None
    eventId: Optional[str] = None


class SearchedLogStream(BaseValidatorModel):
    logStreamName: Optional[str] = None
    searchedCompletely: Optional[bool] = None


# This class is the input for the 'get_data_protection_policy' function.
class GetDataProtectionPolicyRequest(BaseValidatorModel):
    logGroupIdentifier: str


# This class is the input for the 'get_delivery_destination_policy' function.
class GetDeliveryDestinationPolicyRequest(BaseValidatorModel):
    deliveryDestinationName: str


class Policy(BaseValidatorModel):
    deliveryDestinationPolicy: Optional[str] = None


# This class is the input for the 'get_delivery_destination' function.
class GetDeliveryDestinationRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'get_delivery' function.
class GetDeliveryRequest(BaseValidatorModel):
    id: str


# This class is the input for the 'get_delivery_source' function.
class GetDeliverySourceRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'get_integration' function.
class GetIntegrationRequest(BaseValidatorModel):
    integrationName: str


# This class is the input for the 'get_log_anomaly_detector' function.
class GetLogAnomalyDetectorRequest(BaseValidatorModel):
    anomalyDetectorArn: str


# This class is the input for the 'get_log_events' function.
class GetLogEventsRequest(BaseValidatorModel):
    logStreamName: str
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    startTime: Optional[int] = None
    endTime: Optional[int] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    startFromHead: Optional[bool] = None
    unmask: Optional[bool] = None


class OutputLogEvent(BaseValidatorModel):
    timestamp: Optional[int] = None
    message: Optional[str] = None
    ingestionTime: Optional[int] = None


# This class is the input for the 'get_log_group_fields' function.
class GetLogGroupFieldsRequest(BaseValidatorModel):
    logGroupName: Optional[str] = None
    time: Optional[int] = None
    logGroupIdentifier: Optional[str] = None


class LogGroupField(BaseValidatorModel):
    name: Optional[str] = None
    percent: Optional[int] = None


# This class is the input for the 'get_log_record' function.
class GetLogRecordRequest(BaseValidatorModel):
    logRecordPointer: str
    unmask: Optional[bool] = None


# This class is the input for the 'get_query_results' function.
class GetQueryResultsRequest(BaseValidatorModel):
    queryId: str


class QueryStatistics(BaseValidatorModel):
    recordsMatched: Optional[float] = None
    recordsScanned: Optional[float] = None
    estimatedRecordsSkipped: Optional[float] = None
    bytesScanned: Optional[float] = None
    estimatedBytesSkipped: Optional[float] = None
    logGroupsScanned: Optional[float] = None


class ResultField(BaseValidatorModel):
    field: Optional[str] = None
    value: Optional[str] = None


# This class is the input for the 'get_transformer' function.
class GetTransformerRequest(BaseValidatorModel):
    logGroupIdentifier: str


class Grok(BaseValidatorModel):
    match: str
    source: Optional[str] = None


class InputLogEvent(BaseValidatorModel):
    timestamp: int
    message: str


class IntegrationSummary(BaseValidatorModel):
    integrationName: Optional[str] = None
    integrationType: Optional[Literal['OPENSEARCH']] = None
    integrationStatus: Optional[IntegrationStatusType] = None


# This class is the input for the 'list_anomalies' function.
class ListAnomaliesRequest(BaseValidatorModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_integrations' function.
class ListIntegrationsRequest(BaseValidatorModel):
    integrationNamePrefix: Optional[str] = None
    integrationType: Optional[Literal['OPENSEARCH']] = None
    integrationStatus: Optional[IntegrationStatusType] = None


# This class is the input for the 'list_log_anomaly_detectors' function.
class ListLogAnomalyDetectorsRequest(BaseValidatorModel):
    filterLogGroupArn: Optional[str] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_log_groups_for_query' function.
class ListLogGroupsForQueryRequest(BaseValidatorModel):
    queryId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_tags_log_group' function.
class ListTagsLogGroupRequest(BaseValidatorModel):
    logGroupName: str


class ListToMap(BaseValidatorModel):
    source: str
    key: str
    valueKey: Optional[str] = None
    target: Optional[str] = None
    flatten: Optional[bool] = None
    flattenedElement: Optional[FlattenedElementType] = None


class LiveTailSessionLogEvent(BaseValidatorModel):
    logStreamName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    message: Optional[str] = None
    timestamp: Optional[int] = None
    ingestionTime: Optional[int] = None


class LiveTailSessionMetadata(BaseValidatorModel):
    sampled: Optional[bool] = None


class LiveTailSessionStart(BaseValidatorModel):
    requestId: Optional[str] = None
    sessionId: Optional[str] = None
    logGroupIdentifiers: Optional[List[str]] = None
    logStreamNames: Optional[List[str]] = None
    logStreamNamePrefixes: Optional[List[str]] = None
    logEventFilterPattern: Optional[str] = None


class LowerCaseStringOutput(BaseValidatorModel):
    withKeys: List[str]


class LowerCaseString(BaseValidatorModel):
    withKeys: List[str]


class MetricFilterMatchRecord(BaseValidatorModel):
    eventNumber: Optional[int] = None
    eventMessage: Optional[str] = None
    extractedValues: Optional[Dict[str, str]] = None


class MetricTransformationOutput(BaseValidatorModel):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: Optional[float] = None
    dimensions: Optional[Dict[str, str]] = None
    unit: Optional[StandardUnitType] = None


class MetricTransformation(BaseValidatorModel):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: Optional[float] = None
    dimensions: Optional[Dict[str, str]] = None
    unit: Optional[StandardUnitType] = None


class MoveKeyEntry(BaseValidatorModel):
    source: str
    target: str
    overwriteIfExists: Optional[bool] = None


class OpenSearchResourceStatus(BaseValidatorModel):
    status: Optional[OpenSearchResourceStatusTypeType] = None
    statusMessage: Optional[str] = None


class OpenSearchResourceConfig(BaseValidatorModel):
    dataSourceRoleArn: str
    dashboardViewerPrincipals: List[str]
    retentionDays: int
    kmsKeyArn: Optional[str] = None
    applicationArn: Optional[str] = None


class ParseCloudfront(BaseValidatorModel):
    source: Optional[str] = None


class ParseJSON(BaseValidatorModel):
    source: Optional[str] = None
    destination: Optional[str] = None


class ParseKeyValue(BaseValidatorModel):
    source: Optional[str] = None
    destination: Optional[str] = None
    fieldDelimiter: Optional[str] = None
    keyValueDelimiter: Optional[str] = None
    keyPrefix: Optional[str] = None
    nonMatchValue: Optional[str] = None
    overwriteIfExists: Optional[bool] = None


class ParsePostgres(BaseValidatorModel):
    source: Optional[str] = None


class ParseRoute53(BaseValidatorModel):
    source: Optional[str] = None


class ParseVPC(BaseValidatorModel):
    source: Optional[str] = None


class ParseWAF(BaseValidatorModel):
    source: Optional[str] = None


class TrimStringOutput(BaseValidatorModel):
    withKeys: List[str]


class UpperCaseStringOutput(BaseValidatorModel):
    withKeys: List[str]


# This class is the input for the 'put_account_policy' function.
class PutAccountPolicyRequest(BaseValidatorModel):
    policyName: str
    policyDocument: str
    policyType: PolicyTypeType
    scope: Optional[Literal['ALL']] = None
    selectionCriteria: Optional[str] = None


# This class is the input for the 'put_data_protection_policy' function.
class PutDataProtectionPolicyRequest(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str


# This class is the input for the 'put_delivery_destination_policy' function.
class PutDeliveryDestinationPolicyRequest(BaseValidatorModel):
    deliveryDestinationName: str
    deliveryDestinationPolicy: str


# This class is the input for the 'put_delivery_source' function.
class PutDeliverySourceRequest(BaseValidatorModel):
    name: str
    resourceArn: str
    logType: str
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'put_destination_policy' function.
class PutDestinationPolicyRequest(BaseValidatorModel):
    destinationName: str
    accessPolicy: str
    forceUpdate: Optional[bool] = None


# This class is the input for the 'put_destination' function.
class PutDestinationRequest(BaseValidatorModel):
    destinationName: str
    targetArn: str
    roleArn: str
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'put_index_policy' function.
class PutIndexPolicyRequest(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str


class RejectedEntityInfo(BaseValidatorModel):
    errorType: EntityRejectionErrorTypeType


class RejectedLogEventsInfo(BaseValidatorModel):
    tooNewLogEventStartIndex: Optional[int] = None
    tooOldLogEventEndIndex: Optional[int] = None
    expiredLogEventEndIndex: Optional[int] = None


# This class is the input for the 'put_query_definition' function.
class PutQueryDefinitionRequest(BaseValidatorModel):
    name: str
    queryString: str
    queryLanguage: Optional[QueryLanguageType] = None
    queryDefinitionId: Optional[str] = None
    logGroupNames: Optional[List[str]] = None
    clientToken: Optional[str] = None


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None


# This class is the input for the 'put_retention_policy' function.
class PutRetentionPolicyRequest(BaseValidatorModel):
    logGroupName: str
    retentionInDays: int


# This class is the input for the 'put_subscription_filter' function.
class PutSubscriptionFilterRequest(BaseValidatorModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    destinationArn: str
    roleArn: Optional[str] = None
    distribution: Optional[DistributionType] = None
    applyOnTransformedLogs: Optional[bool] = None


class RenameKeyEntry(BaseValidatorModel):
    key: str
    renameTo: str
    overwriteIfExists: Optional[bool] = None


class SessionStreamingException(BaseValidatorModel):
    message: Optional[str] = None


class SessionTimeoutException(BaseValidatorModel):
    message: Optional[str] = None


class SplitStringEntry(BaseValidatorModel):
    source: str
    delimiter: str


# This class is the input for the 'start_live_tail' function.
class StartLiveTailRequest(BaseValidatorModel):
    logGroupIdentifiers: List[str]
    logStreamNames: Optional[List[str]] = None
    logStreamNamePrefixes: Optional[List[str]] = None
    logEventFilterPattern: Optional[str] = None


# This class is the input for the 'start_query' function.
class StartQueryRequest(BaseValidatorModel):
    startTime: int
    endTime: int
    queryString: str
    queryLanguage: Optional[QueryLanguageType] = None
    logGroupName: Optional[str] = None
    logGroupNames: Optional[List[str]] = None
    logGroupIdentifiers: Optional[List[str]] = None
    limit: Optional[int] = None


# This class is the input for the 'stop_query' function.
class StopQueryRequest(BaseValidatorModel):
    queryId: str


class SubstituteStringEntry(BaseValidatorModel):
    source: str
    from_: str
    to: str


class SuppressionPeriod(BaseValidatorModel):
    value: Optional[int] = None
    suppressionUnit: Optional[SuppressionUnitType] = None


# This class is the input for the 'tag_log_group' function.
class TagLogGroupRequest(BaseValidatorModel):
    logGroupName: str
    tags: Dict[str, str]


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'test_metric_filter' function.
class TestMetricFilterRequest(BaseValidatorModel):
    filterPattern: str
    logEventMessages: List[str]


class TransformedLogRecord(BaseValidatorModel):
    eventNumber: Optional[int] = None
    eventMessage: Optional[str] = None
    transformedEventMessage: Optional[str] = None


class TrimString(BaseValidatorModel):
    withKeys: List[str]


class TypeConverterEntry(BaseValidatorModel):
    key: str
    type: TypeType


# This class is the input for the 'untag_log_group' function.
class UntagLogGroupRequest(BaseValidatorModel):
    logGroupName: str
    tags: List[str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_log_anomaly_detector' function.
class UpdateLogAnomalyDetectorRequest(BaseValidatorModel):
    anomalyDetectorArn: str
    enabled: bool
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None


class UpperCaseString(BaseValidatorModel):
    withKeys: List[str]


class AddKeysOutput(BaseValidatorModel):
    entries: List[AddKeyEntry]


class AddKeys(BaseValidatorModel):
    entries: List[AddKeyEntry]


class Anomaly(BaseValidatorModel):
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
    logSamples: List[LogEvent]
    patternTokens: List[PatternToken]
    logGroupArnList: List[str]
    patternRegex: Optional[str] = None
    priority: Optional[str] = None
    suppressed: Optional[bool] = None
    suppressedDate: Optional[int] = None
    suppressedUntil: Optional[int] = None
    isPatternLevelSuppression: Optional[bool] = None

CSVUnion = Union[CSV, CSVOutput]


class ConfigurationTemplateDeliveryConfigValues(BaseValidatorModel):
    recordFields: Optional[List[str]] = None
    fieldDelimiter: Optional[str] = None
    s3DeliveryConfiguration: Optional[S3DeliveryConfiguration] = None


# This class is the input for the 'create_delivery' function.
class CreateDeliveryRequest(BaseValidatorModel):
    deliverySourceName: str
    deliveryDestinationArn: str
    recordFields: Optional[List[str]] = None
    fieldDelimiter: Optional[str] = None
    s3DeliveryConfiguration: Optional[S3DeliveryConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class Delivery(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    deliverySourceName: Optional[str] = None
    deliveryDestinationArn: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    recordFields: Optional[List[str]] = None
    fieldDelimiter: Optional[str] = None
    s3DeliveryConfiguration: Optional[S3DeliveryConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class UpdateDeliveryConfigurationRequest(BaseValidatorModel):
    id: str
    recordFields: Optional[List[str]] = None
    fieldDelimiter: Optional[str] = None
    s3DeliveryConfiguration: Optional[S3DeliveryConfiguration] = None


class CopyValueOutput(BaseValidatorModel):
    entries: List[CopyValueEntry]


class CopyValue(BaseValidatorModel):
    entries: List[CopyValueEntry]


# This class is the output for the 'create_export_task' function.
class CreateExportTaskResponse(BaseValidatorModel):
    taskId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_log_anomaly_detector' function.
class CreateLogAnomalyDetectorResponse(BaseValidatorModel):
    anomalyDetectorArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_query_definition' function.
class DeleteQueryDefinitionResponse(BaseValidatorModel):
    success: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_account_policies' function.
class DescribeAccountPoliciesResponse(BaseValidatorModel):
    accountPolicies: List[AccountPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_log_anomaly_detector' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_data_protection_policy' function.
class GetDataProtectionPolicyResponse(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_log_anomaly_detector' function.
class GetLogAnomalyDetectorResponse(BaseValidatorModel):
    detectorName: str
    logGroupArnList: List[str]
    evaluationFrequency: EvaluationFrequencyType
    filterPattern: str
    anomalyDetectorStatus: AnomalyDetectorStatusType
    kmsKeyId: str
    creationTimeStamp: int
    lastModifiedTimeStamp: int
    anomalyVisibilityTime: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_log_record' function.
class GetLogRecordResponse(BaseValidatorModel):
    logRecord: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_log_anomaly_detectors' function.
class ListLogAnomalyDetectorsResponse(BaseValidatorModel):
    anomalyDetectors: List[AnomalyDetector]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_log_groups_for_query' function.
class ListLogGroupsForQueryResponse(BaseValidatorModel):
    logGroupIdentifiers: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_log_group' function.
class ListTagsLogGroupResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_account_policy' function.
class PutAccountPolicyResponse(BaseValidatorModel):
    accountPolicy: AccountPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_data_protection_policy' function.
class PutDataProtectionPolicyResponse(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_integration' function.
class PutIntegrationResponse(BaseValidatorModel):
    integrationName: str
    integrationStatus: IntegrationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_query_definition' function.
class PutQueryDefinitionResponse(BaseValidatorModel):
    queryDefinitionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_query' function.
class StartQueryResponse(BaseValidatorModel):
    queryId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_query' function.
class StopQueryResponse(BaseValidatorModel):
    success: bool
    ResponseMetadata: ResponseMetadata

DateTimeConverterUnion = Union[DateTimeConverter, DateTimeConverterOutput]

DeleteKeysUnion = Union[DeleteKeys, DeleteKeysOutput]


class DeliveryDestination(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    outputFormat: Optional[OutputFormatType] = None
    deliveryDestinationConfiguration: Optional[DeliveryDestinationConfiguration] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'put_delivery_destination' function.
class PutDeliveryDestinationRequest(BaseValidatorModel):
    name: str
    deliveryDestinationConfiguration: DeliveryDestinationConfiguration
    outputFormat: Optional[OutputFormatType] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_delivery_sources' function.
class DescribeDeliverySourcesResponse(BaseValidatorModel):
    deliverySources: List[DeliverySource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_delivery_source' function.
class GetDeliverySourceResponse(BaseValidatorModel):
    deliverySource: DeliverySource
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_delivery_source' function.
class PutDeliverySourceResponse(BaseValidatorModel):
    deliverySource: DeliverySource
    ResponseMetadata: ResponseMetadata


class DescribeConfigurationTemplatesRequestPaginate(BaseValidatorModel):
    service: Optional[str] = None
    logTypes: Optional[List[str]] = None
    resourceTypes: Optional[List[str]] = None
    deliveryDestinationTypes: Optional[List[DeliveryDestinationTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDeliveriesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDeliveryDestinationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDeliverySourcesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDestinationsRequestPaginate(BaseValidatorModel):
    DestinationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeExportTasksRequestPaginate(BaseValidatorModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLogGroupsRequestPaginate(BaseValidatorModel):
    accountIdentifiers: Optional[List[str]] = None
    logGroupNamePrefix: Optional[str] = None
    logGroupNamePattern: Optional[str] = None
    includeLinkedAccounts: Optional[bool] = None
    logGroupClass: Optional[LogGroupClassType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeLogStreamsRequestPaginate(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    orderBy: Optional[OrderByType] = None
    descending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMetricFiltersRequestPaginate(BaseValidatorModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeQueriesRequestPaginate(BaseValidatorModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    queryLanguage: Optional[QueryLanguageType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeResourcePoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSubscriptionFiltersRequestPaginate(BaseValidatorModel):
    logGroupName: str
    filterNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class FilterLogEventsRequestPaginate(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNames: Optional[List[str]] = None
    logStreamNamePrefix: Optional[str] = None
    startTime: Optional[int] = None
    endTime: Optional[int] = None
    filterPattern: Optional[str] = None
    interleaved: Optional[bool] = None
    unmask: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAnomaliesRequestPaginate(BaseValidatorModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLogAnomalyDetectorsRequestPaginate(BaseValidatorModel):
    filterLogGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLogGroupsForQueryRequestPaginate(BaseValidatorModel):
    queryId: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_destinations' function.
class DescribeDestinationsResponse(BaseValidatorModel):
    destinations: List[Destination]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_destination' function.
class PutDestinationResponse(BaseValidatorModel):
    destination: Destination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_field_indexes' function.
class DescribeFieldIndexesResponse(BaseValidatorModel):
    fieldIndexes: List[FieldIndex]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_index_policies' function.
class DescribeIndexPoliciesResponse(BaseValidatorModel):
    indexPolicies: List[IndexPolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_index_policy' function.
class PutIndexPolicyResponse(BaseValidatorModel):
    indexPolicy: IndexPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_log_groups' function.
class DescribeLogGroupsResponse(BaseValidatorModel):
    logGroups: List[LogGroup]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_log_streams' function.
class DescribeLogStreamsResponse(BaseValidatorModel):
    logStreams: List[LogStream]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_queries' function.
class DescribeQueriesResponse(BaseValidatorModel):
    queries: List[QueryInfo]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_query_definitions' function.
class DescribeQueryDefinitionsResponse(BaseValidatorModel):
    queryDefinitions: List[QueryDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_resource_policies' function.
class DescribeResourcePoliciesResponse(BaseValidatorModel):
    resourcePolicies: List[ResourcePolicy]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    resourcePolicy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_subscription_filters' function.
class DescribeSubscriptionFiltersResponse(BaseValidatorModel):
    subscriptionFilters: List[SubscriptionFilter]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExportTask(BaseValidatorModel):
    taskId: Optional[str] = None
    taskName: Optional[str] = None
    logGroupName: Optional[str] = None
    from_: Optional[int] = None
    to: Optional[int] = None
    destination: Optional[str] = None
    destinationPrefix: Optional[str] = None
    status: Optional[ExportTaskStatus] = None
    executionInfo: Optional[ExportTaskExecutionInfo] = None


# This class is the output for the 'filter_log_events' function.
class FilterLogEventsResponse(BaseValidatorModel):
    events: List[FilteredLogEvent]
    searchedLogStreams: List[SearchedLogStream]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_delivery_destination_policy' function.
class GetDeliveryDestinationPolicyResponse(BaseValidatorModel):
    policy: Policy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_delivery_destination_policy' function.
class PutDeliveryDestinationPolicyResponse(BaseValidatorModel):
    policy: Policy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_log_events' function.
class GetLogEventsResponse(BaseValidatorModel):
    events: List[OutputLogEvent]
    nextForwardToken: str
    nextBackwardToken: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_log_group_fields' function.
class GetLogGroupFieldsResponse(BaseValidatorModel):
    logGroupFields: List[LogGroupField]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_results' function.
class GetQueryResultsResponse(BaseValidatorModel):
    queryLanguage: QueryLanguageType
    results: List[List[ResultField]]
    statistics: QueryStatistics
    status: QueryStatusType
    encryptionKey: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_log_events' function.
class PutLogEventsRequest(BaseValidatorModel):
    logGroupName: str
    logStreamName: str
    logEvents: List[InputLogEvent]
    sequenceToken: Optional[str] = None
    entity: Optional[Entity] = None


# This class is the output for the 'list_integrations' function.
class ListIntegrationsResponse(BaseValidatorModel):
    integrationSummaries: List[IntegrationSummary]
    ResponseMetadata: ResponseMetadata


class LiveTailSessionUpdate(BaseValidatorModel):
    sessionMetadata: Optional[LiveTailSessionMetadata] = None
    sessionResults: Optional[List[LiveTailSessionLogEvent]] = None

LowerCaseStringUnion = Union[LowerCaseString, LowerCaseStringOutput]


# This class is the output for the 'test_metric_filter' function.
class TestMetricFilterResponse(BaseValidatorModel):
    matches: List[MetricFilterMatchRecord]
    ResponseMetadata: ResponseMetadata


class MetricFilter(BaseValidatorModel):
    filterName: Optional[str] = None
    filterPattern: Optional[str] = None
    metricTransformations: Optional[List[MetricTransformationOutput]] = None
    creationTime: Optional[int] = None
    logGroupName: Optional[str] = None
    applyOnTransformedLogs: Optional[bool] = None

MetricTransformationUnion = Union[MetricTransformation, MetricTransformationOutput]


class MoveKeysOutput(BaseValidatorModel):
    entries: List[MoveKeyEntry]


class MoveKeys(BaseValidatorModel):
    entries: List[MoveKeyEntry]


class OpenSearchApplication(BaseValidatorModel):
    applicationEndpoint: Optional[str] = None
    applicationArn: Optional[str] = None
    applicationId: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class OpenSearchCollection(BaseValidatorModel):
    collectionEndpoint: Optional[str] = None
    collectionArn: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class OpenSearchDataAccessPolicy(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class OpenSearchDataSource(BaseValidatorModel):
    dataSourceName: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class OpenSearchEncryptionPolicy(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class OpenSearchLifecyclePolicy(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class OpenSearchNetworkPolicy(BaseValidatorModel):
    policyName: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class OpenSearchWorkspace(BaseValidatorModel):
    workspaceId: Optional[str] = None
    status: Optional[OpenSearchResourceStatus] = None


class ResourceConfig(BaseValidatorModel):
    openSearchResourceConfig: Optional[OpenSearchResourceConfig] = None


# This class is the output for the 'put_log_events' function.
class PutLogEventsResponse(BaseValidatorModel):
    nextSequenceToken: str
    rejectedLogEventsInfo: RejectedLogEventsInfo
    rejectedEntityInfo: RejectedEntityInfo
    ResponseMetadata: ResponseMetadata


class RenameKeysOutput(BaseValidatorModel):
    entries: List[RenameKeyEntry]


class RenameKeys(BaseValidatorModel):
    entries: List[RenameKeyEntry]


class SplitStringOutput(BaseValidatorModel):
    entries: List[SplitStringEntry]


class SplitString(BaseValidatorModel):
    entries: List[SplitStringEntry]


class SubstituteStringOutput(BaseValidatorModel):
    entries: List[SubstituteStringEntry]


class SubstituteString(BaseValidatorModel):
    entries: List[SubstituteStringEntry]


# This class is the input for the 'update_anomaly' function.
class UpdateAnomalyRequest(BaseValidatorModel):
    anomalyDetectorArn: str
    anomalyId: Optional[str] = None
    patternId: Optional[str] = None
    suppressionType: Optional[SuppressionTypeType] = None
    suppressionPeriod: Optional[SuppressionPeriod] = None
    baseline: Optional[bool] = None


# This class is the output for the 'test_transformer' function.
class TestTransformerResponse(BaseValidatorModel):
    transformedLogs: List[TransformedLogRecord]
    ResponseMetadata: ResponseMetadata

TrimStringUnion = Union[TrimString, TrimStringOutput]


class TypeConverterOutput(BaseValidatorModel):
    entries: List[TypeConverterEntry]


class TypeConverter(BaseValidatorModel):
    entries: List[TypeConverterEntry]

UpperCaseStringUnion = Union[UpperCaseString, UpperCaseStringOutput]

AddKeysUnion = Union[AddKeys, AddKeysOutput]


# This class is the output for the 'list_anomalies' function.
class ListAnomaliesResponse(BaseValidatorModel):
    anomalies: List[Anomaly]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConfigurationTemplate(BaseValidatorModel):
    service: Optional[str] = None
    logType: Optional[str] = None
    resourceType: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    defaultDeliveryConfigValues: Optional[ConfigurationTemplateDeliveryConfigValues] = None
    allowedFields: Optional[List[RecordField]] = None
    allowedOutputFormats: Optional[List[OutputFormatType]] = None
    allowedActionForAllowVendedLogsDeliveryForResource: Optional[str] = None
    allowedFieldDelimiters: Optional[List[str]] = None
    allowedSuffixPathFields: Optional[List[str]] = None


# This class is the output for the 'create_delivery' function.
class CreateDeliveryResponse(BaseValidatorModel):
    delivery: Delivery
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_deliveries' function.
class DescribeDeliveriesResponse(BaseValidatorModel):
    deliveries: List[Delivery]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_delivery' function.
class GetDeliveryResponse(BaseValidatorModel):
    delivery: Delivery
    ResponseMetadata: ResponseMetadata

CopyValueUnion = Union[CopyValue, CopyValueOutput]


# This class is the output for the 'describe_delivery_destinations' function.
class DescribeDeliveryDestinationsResponse(BaseValidatorModel):
    deliveryDestinations: List[DeliveryDestination]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_delivery_destination' function.
class GetDeliveryDestinationResponse(BaseValidatorModel):
    deliveryDestination: DeliveryDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_delivery_destination' function.
class PutDeliveryDestinationResponse(BaseValidatorModel):
    deliveryDestination: DeliveryDestination
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_export_tasks' function.
class DescribeExportTasksResponse(BaseValidatorModel):
    exportTasks: List[ExportTask]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartLiveTailResponseStream(BaseValidatorModel):
    sessionStart: Optional[LiveTailSessionStart] = None
    sessionUpdate: Optional[LiveTailSessionUpdate] = None
    SessionTimeoutException: Optional[SessionTimeoutException] = None
    SessionStreamingException: Optional[SessionStreamingException] = None


# This class is the output for the 'describe_metric_filters' function.
class DescribeMetricFiltersResponse(BaseValidatorModel):
    metricFilters: List[MetricFilter]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'put_metric_filter' function.
class PutMetricFilterRequest(BaseValidatorModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    metricTransformations: List[MetricTransformationUnion]
    applyOnTransformedLogs: Optional[bool] = None

MoveKeysUnion = Union[MoveKeys, MoveKeysOutput]


class OpenSearchIntegrationDetails(BaseValidatorModel):
    dataSource: Optional[OpenSearchDataSource] = None
    application: Optional[OpenSearchApplication] = None
    collection: Optional[OpenSearchCollection] = None
    workspace: Optional[OpenSearchWorkspace] = None
    encryptionPolicy: Optional[OpenSearchEncryptionPolicy] = None
    networkPolicy: Optional[OpenSearchNetworkPolicy] = None
    accessPolicy: Optional[OpenSearchDataAccessPolicy] = None
    lifecyclePolicy: Optional[OpenSearchLifecyclePolicy] = None


# This class is the input for the 'put_integration' function.
class PutIntegrationRequest(BaseValidatorModel):
    integrationName: str
    resourceConfig: ResourceConfig
    integrationType: Literal['OPENSEARCH']

RenameKeysUnion = Union[RenameKeys, RenameKeysOutput]

SplitStringUnion = Union[SplitString, SplitStringOutput]

SubstituteStringUnion = Union[SubstituteString, SubstituteStringOutput]


class ProcessorOutput(BaseValidatorModel):
    addKeys: Optional[AddKeysOutput] = None
    copyValue: Optional[CopyValueOutput] = None
    csv: Optional[CSVOutput] = None
    dateTimeConverter: Optional[DateTimeConverterOutput] = None
    deleteKeys: Optional[DeleteKeysOutput] = None
    grok: Optional[Grok] = None
    listToMap: Optional[ListToMap] = None
    lowerCaseString: Optional[LowerCaseStringOutput] = None
    moveKeys: Optional[MoveKeysOutput] = None
    parseCloudfront: Optional[ParseCloudfront] = None
    parseJSON: Optional[ParseJSON] = None
    parseKeyValue: Optional[ParseKeyValue] = None
    parseRoute53: Optional[ParseRoute53] = None
    parsePostgres: Optional[ParsePostgres] = None
    parseVPC: Optional[ParseVPC] = None
    parseWAF: Optional[ParseWAF] = None
    renameKeys: Optional[RenameKeysOutput] = None
    splitString: Optional[SplitStringOutput] = None
    substituteString: Optional[SubstituteStringOutput] = None
    trimString: Optional[TrimStringOutput] = None
    typeConverter: Optional[TypeConverterOutput] = None
    upperCaseString: Optional[UpperCaseStringOutput] = None

TypeConverterUnion = Union[TypeConverter, TypeConverterOutput]


# This class is the output for the 'describe_configuration_templates' function.
class DescribeConfigurationTemplatesResponse(BaseValidatorModel):
    configurationTemplates: List[ConfigurationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'start_live_tail' function.
class StartLiveTailResponse(BaseValidatorModel):
    responseStream: EventStream[StartLiveTailResponseStream]
    ResponseMetadata: ResponseMetadata


class IntegrationDetails(BaseValidatorModel):
    openSearchIntegrationDetails: Optional[OpenSearchIntegrationDetails] = None


# This class is the output for the 'get_transformer' function.
class GetTransformerResponse(BaseValidatorModel):
    logGroupIdentifier: str
    creationTime: int
    lastModifiedTime: int
    transformerConfig: List[ProcessorOutput]
    ResponseMetadata: ResponseMetadata


class Processor(BaseValidatorModel):
    addKeys: Optional[AddKeysUnion] = None
    copyValue: Optional[CopyValueUnion] = None
    csv: Optional[CSVUnion] = None
    dateTimeConverter: Optional[DateTimeConverterUnion] = None
    deleteKeys: Optional[DeleteKeysUnion] = None
    grok: Optional[Grok] = None
    listToMap: Optional[ListToMap] = None
    lowerCaseString: Optional[LowerCaseStringUnion] = None
    moveKeys: Optional[MoveKeysUnion] = None
    parseCloudfront: Optional[ParseCloudfront] = None
    parseJSON: Optional[ParseJSON] = None
    parseKeyValue: Optional[ParseKeyValue] = None
    parseRoute53: Optional[ParseRoute53] = None
    parsePostgres: Optional[ParsePostgres] = None
    parseVPC: Optional[ParseVPC] = None
    parseWAF: Optional[ParseWAF] = None
    renameKeys: Optional[RenameKeysUnion] = None
    splitString: Optional[SplitStringUnion] = None
    substituteString: Optional[SubstituteStringUnion] = None
    trimString: Optional[TrimStringUnion] = None
    typeConverter: Optional[TypeConverterUnion] = None
    upperCaseString: Optional[UpperCaseStringUnion] = None


# This class is the output for the 'get_integration' function.
class GetIntegrationResponse(BaseValidatorModel):
    integrationName: str
    integrationType: Literal['OPENSEARCH']
    integrationStatus: IntegrationStatusType
    integrationDetails: IntegrationDetails
    ResponseMetadata: ResponseMetadata

ProcessorUnion = Union[Processor, ProcessorOutput]


# This class is the input for the 'put_transformer' function.
class PutTransformerRequest(BaseValidatorModel):
    logGroupIdentifier: str
    transformerConfig: List[ProcessorUnion]


# This class is the input for the 'test_transformer' function.
class TestTransformerRequest(BaseValidatorModel):
    transformerConfig: List[ProcessorUnion]
    logEventMessages: List[str]