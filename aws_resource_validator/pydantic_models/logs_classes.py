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
from aws_resource_validator.pydantic_models.logs_constants import *

class AccountPolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None
    policyType: Optional[PolicyTypeType] = None
    scope: Optional[Literal["ALL"]] = None
    selectionCriteria: Optional[str] = None
    accountId: Optional[str] = None

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

class AssociateKmsKeyRequestRequestTypeDef(BaseValidatorModel):
    kmsKeyId: str
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None

class CancelExportTaskRequestRequestTypeDef(BaseValidatorModel):
    taskId: str

class CreateDeliveryRequestRequestTypeDef(BaseValidatorModel):
    deliverySourceName: str
    deliveryDestinationArn: str
    tags: Optional[Mapping[str, str]] = None

class DeliveryTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    deliverySourceName: Optional[str] = None
    deliveryDestinationArn: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    tags: Optional[Dict[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateExportTaskRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    fromTime: int
    to: int
    destination: str
    taskName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    destinationPrefix: Optional[str] = None

class CreateLogAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    logGroupArnList: Sequence[str]
    detectorName: Optional[str] = None
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    kmsKeyId: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class CreateLogGroupRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    logGroupClass: Optional[LogGroupClassType] = None

class CreateLogStreamRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    logStreamName: str

class DeleteAccountPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyType: PolicyTypeType

class DeleteDataProtectionPolicyRequestRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str

class DeleteDeliveryDestinationPolicyRequestRequestTypeDef(BaseValidatorModel):
    deliveryDestinationName: str

class DeleteDeliveryDestinationRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteDeliveryRequestRequestTypeDef(BaseValidatorModel):
    id: str

class DeleteDeliverySourceRequestRequestTypeDef(BaseValidatorModel):
    name: str

class DeleteDestinationRequestRequestTypeDef(BaseValidatorModel):
    destinationName: str

class DeleteLogAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str

class DeleteLogGroupRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str

class DeleteLogStreamRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    logStreamName: str

class DeleteMetricFilterRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str

class DeleteQueryDefinitionRequestRequestTypeDef(BaseValidatorModel):
    queryDefinitionId: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None

class DeleteRetentionPolicyRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str

class DeleteSubscriptionFilterRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str

class DeliveryDestinationConfigurationTypeDef(BaseValidatorModel):
    destinationResourceArn: str

class DeliverySourceTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    service: Optional[str] = None
    logType: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class DescribeAccountPoliciesRequestRequestTypeDef(BaseValidatorModel):
    policyType: PolicyTypeType
    policyName: Optional[str] = None
    accountIdentifiers: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDeliveriesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeDeliveryDestinationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeDeliverySourcesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeDestinationsRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeExportTasksRequestRequestTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeLogGroupsRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeLogStreamsRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeMetricFiltersRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None

class DescribeQueriesRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueryInfoTypeDef(BaseValidatorModel):
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    status: Optional[QueryStatusType] = None
    createTime: Optional[int] = None
    logGroupName: Optional[str] = None

class DescribeQueryDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    queryDefinitionNamePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueryDefinitionTypeDef(BaseValidatorModel):
    queryDefinitionId: Optional[str] = None
    name: Optional[str] = None
    queryString: Optional[str] = None
    lastModified: Optional[int] = None
    logGroupNames: Optional[List[str]] = None

class DescribeResourcePoliciesRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class ResourcePolicyTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None

class DescribeSubscriptionFiltersRequestRequestTypeDef(BaseValidatorModel):
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
    creationTime: Optional[int] = None

class DisassociateKmsKeyRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None

class ExportTaskExecutionInfoTypeDef(BaseValidatorModel):
    creationTime: Optional[int] = None
    completionTime: Optional[int] = None

class ExportTaskStatusTypeDef(BaseValidatorModel):
    code: Optional[ExportTaskStatusCodeType] = None
    message: Optional[str] = None

class FilterLogEventsRequestRequestTypeDef(BaseValidatorModel):
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

class GetDataProtectionPolicyRequestRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str

class GetDeliveryDestinationPolicyRequestRequestTypeDef(BaseValidatorModel):
    deliveryDestinationName: str

class PolicyTypeDef(BaseValidatorModel):
    deliveryDestinationPolicy: Optional[str] = None

class GetDeliveryDestinationRequestRequestTypeDef(BaseValidatorModel):
    name: str

class GetDeliveryRequestRequestTypeDef(BaseValidatorModel):
    id: str

class GetDeliverySourceRequestRequestTypeDef(BaseValidatorModel):
    name: str

class GetLogAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str

class GetLogEventsRequestRequestTypeDef(BaseValidatorModel):
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

class GetLogGroupFieldsRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    time: Optional[int] = None
    logGroupIdentifier: Optional[str] = None

class LogGroupFieldTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    percent: Optional[int] = None

class GetLogRecordRequestRequestTypeDef(BaseValidatorModel):
    logRecordPointer: str
    unmask: Optional[bool] = None

class GetQueryResultsRequestRequestTypeDef(BaseValidatorModel):
    queryId: str

class QueryStatisticsTypeDef(BaseValidatorModel):
    recordsMatched: Optional[float] = None
    recordsScanned: Optional[float] = None
    bytesScanned: Optional[float] = None

class ResultFieldTypeDef(BaseValidatorModel):
    field: Optional[str] = None
    value: Optional[str] = None

class InputLogEventTypeDef(BaseValidatorModel):
    timestamp: int
    message: str

class ListAnomaliesRequestRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ListLogAnomalyDetectorsRequestRequestTypeDef(BaseValidatorModel):
    filterLogGroupArn: Optional[str] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTagsLogGroupRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str

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

class MetricFilterMatchRecordTypeDef(BaseValidatorModel):
    eventNumber: Optional[int] = None
    eventMessage: Optional[str] = None
    extractedValues: Optional[Dict[str, str]] = None

class MetricTransformationTypeDef(BaseValidatorModel):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: Optional[float] = None
    dimensions: Optional[Dict[str, str]] = None
    unit: Optional[StandardUnitType] = None

class PutAccountPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: str
    policyDocument: str
    policyType: PolicyTypeType
    scope: Optional[Literal["ALL"]] = None
    selectionCriteria: Optional[str] = None

class PutDataProtectionPolicyRequestRequestTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str

class PutDeliveryDestinationPolicyRequestRequestTypeDef(BaseValidatorModel):
    deliveryDestinationName: str
    deliveryDestinationPolicy: str

class PutDeliverySourceRequestRequestTypeDef(BaseValidatorModel):
    name: str
    resourceArn: str
    logType: str
    tags: Optional[Mapping[str, str]] = None

class PutDestinationPolicyRequestRequestTypeDef(BaseValidatorModel):
    destinationName: str
    accessPolicy: str
    forceUpdate: Optional[bool] = None

class PutDestinationRequestRequestTypeDef(BaseValidatorModel):
    destinationName: str
    targetArn: str
    roleArn: str
    tags: Optional[Mapping[str, str]] = None

class RejectedLogEventsInfoTypeDef(BaseValidatorModel):
    tooNewLogEventStartIndex: Optional[int] = None
    tooOldLogEventEndIndex: Optional[int] = None
    expiredLogEventEndIndex: Optional[int] = None

class PutQueryDefinitionRequestRequestTypeDef(BaseValidatorModel):
    name: str
    queryString: str
    queryDefinitionId: Optional[str] = None
    logGroupNames: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None

class PutRetentionPolicyRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    retentionInDays: int

class PutSubscriptionFilterRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    destinationArn: str
    roleArn: Optional[str] = None
    distribution: Optional[DistributionType] = None

class SessionStreamingExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class SessionTimeoutExceptionTypeDef(BaseValidatorModel):
    message: Optional[str] = None

class StartLiveTailRequestRequestTypeDef(BaseValidatorModel):
    logGroupIdentifiers: Sequence[str]
    logStreamNames: Optional[Sequence[str]] = None
    logStreamNamePrefixes: Optional[Sequence[str]] = None
    logEventFilterPattern: Optional[str] = None

class StartQueryRequestRequestTypeDef(BaseValidatorModel):
    startTime: int
    endTime: int
    queryString: str
    logGroupName: Optional[str] = None
    logGroupNames: Optional[Sequence[str]] = None
    logGroupIdentifiers: Optional[Sequence[str]] = None
    limit: Optional[int] = None

class StopQueryRequestRequestTypeDef(BaseValidatorModel):
    queryId: str

class SuppressionPeriodTypeDef(BaseValidatorModel):
    value: Optional[int] = None
    suppressionUnit: Optional[SuppressionUnitType] = None

class TagLogGroupRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    tags: Mapping[str, str]

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestMetricFilterRequestRequestTypeDef(BaseValidatorModel):
    filterPattern: str
    logEventMessages: Sequence[str]

class UntagLogGroupRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    tags: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLogAnomalyDetectorRequestRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str
    enabled: bool
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None

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

class CreateDeliveryResponseTypeDef(BaseValidatorModel):
    delivery: DeliveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class DescribeDeliveriesResponseTypeDef(BaseValidatorModel):
    deliveries: List[DeliveryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataProtectionPolicyResponseTypeDef(BaseValidatorModel):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliveryResponseTypeDef(BaseValidatorModel):
    delivery: DeliveryTypeDef
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class PutDeliveryDestinationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    deliveryDestinationConfiguration: DeliveryDestinationConfigurationTypeDef
    outputFormat: Optional[OutputFormatType] = None
    tags: Optional[Mapping[str, str]] = None

class DescribeDeliverySourcesResponseTypeDef(BaseValidatorModel):
    deliverySources: List[DeliverySourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliverySourceResponseTypeDef(BaseValidatorModel):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliverySourceResponseTypeDef(BaseValidatorModel):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeliveriesRequestDescribeDeliveriesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDeliveryDestinationsRequestDescribeDeliveryDestinationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDeliverySourcesRequestDescribeDeliverySourcesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDestinationsRequestDescribeDestinationsPaginateTypeDef(BaseValidatorModel):
    DestinationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLogGroupsRequestDescribeLogGroupsPaginateTypeDef(BaseValidatorModel):
    accountIdentifiers: Optional[Sequence[str]] = None
    logGroupNamePrefix: Optional[str] = None
    logGroupNamePattern: Optional[str] = None
    includeLinkedAccounts: Optional[bool] = None
    logGroupClass: Optional[LogGroupClassType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLogStreamsRequestDescribeLogStreamsPaginateTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    orderBy: Optional[OrderByType] = None
    descending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMetricFiltersRequestDescribeMetricFiltersPaginateTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeQueriesRequestDescribeQueriesPaginateTypeDef(BaseValidatorModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeResourcePoliciesRequestDescribeResourcePoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubscriptionFiltersRequestDescribeSubscriptionFiltersPaginateTypeDef(BaseValidatorModel):
    logGroupName: str
    filterNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class FilterLogEventsRequestFilterLogEventsPaginateTypeDef(BaseValidatorModel):
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

class ListAnomaliesRequestListAnomaliesPaginateTypeDef(BaseValidatorModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLogAnomalyDetectorsRequestListLogAnomalyDetectorsPaginateTypeDef(BaseValidatorModel):
    filterLogGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDestinationsResponseTypeDef(BaseValidatorModel):
    destinations: List[DestinationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutDestinationResponseTypeDef(BaseValidatorModel):
    destination: DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLogGroupsResponseTypeDef(BaseValidatorModel):
    logGroups: List[LogGroupTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLogStreamsResponseTypeDef(BaseValidatorModel):
    logStreams: List[LogStreamTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeQueriesResponseTypeDef(BaseValidatorModel):
    queries: List[QueryInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeQueryDefinitionsResponseTypeDef(BaseValidatorModel):
    queryDefinitions: List[QueryDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePoliciesResponseTypeDef(BaseValidatorModel):
    resourcePolicies: List[ResourcePolicyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubscriptionFiltersResponseTypeDef(BaseValidatorModel):
    subscriptionFilters: List[SubscriptionFilterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTaskTypeDef(BaseValidatorModel):
    taskId: Optional[str] = None
    taskName: Optional[str] = None
    logGroupName: Optional[str] = None
    _from: Optional[int] = None
    to: Optional[int] = None
    destination: Optional[str] = None
    destinationPrefix: Optional[str] = None
    status: Optional[ExportTaskStatusTypeDef] = None
    executionInfo: Optional[ExportTaskExecutionInfoTypeDef] = None

class FilterLogEventsResponseTypeDef(BaseValidatorModel):
    events: List[FilteredLogEventTypeDef]
    searchedLogStreams: List[SearchedLogStreamTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    results: List[List[ResultFieldTypeDef]]
    statistics: QueryStatisticsTypeDef
    status: QueryStatusType
    encryptionKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutLogEventsRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    logStreamName: str
    logEvents: Sequence[InputLogEventTypeDef]
    sequenceToken: Optional[str] = None

class LiveTailSessionUpdateTypeDef(BaseValidatorModel):
    sessionMetadata: Optional[LiveTailSessionMetadataTypeDef] = None
    sessionResults: Optional[List[LiveTailSessionLogEventTypeDef]] = None

class TestMetricFilterResponseTypeDef(BaseValidatorModel):
    matches: List[MetricFilterMatchRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricFilterTypeDef(BaseValidatorModel):
    filterName: Optional[str] = None
    filterPattern: Optional[str] = None
    metricTransformations: Optional[List[MetricTransformationTypeDef]] = None
    creationTime: Optional[int] = None
    logGroupName: Optional[str] = None

class PutMetricFilterRequestRequestTypeDef(BaseValidatorModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    metricTransformations: Sequence[MetricTransformationTypeDef]

class PutLogEventsResponseTypeDef(BaseValidatorModel):
    nextSequenceToken: str
    rejectedLogEventsInfo: RejectedLogEventsInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalyRequestRequestTypeDef(BaseValidatorModel):
    anomalyDetectorArn: str
    anomalyId: Optional[str] = None
    patternId: Optional[str] = None
    suppressionType: Optional[SuppressionTypeType] = None
    suppressionPeriod: Optional[SuppressionPeriodTypeDef] = None

class ListAnomaliesResponseTypeDef(BaseValidatorModel):
    anomalies: List[AnomalyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeliveryDestinationsResponseTypeDef(BaseValidatorModel):
    deliveryDestinations: List[DeliveryDestinationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliveryDestinationResponseTypeDef(BaseValidatorModel):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryDestinationResponseTypeDef(BaseValidatorModel):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportTasksResponseTypeDef(BaseValidatorModel):
    exportTasks: List[ExportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLiveTailResponseStreamTypeDef(BaseValidatorModel):
    sessionStart: Optional[LiveTailSessionStartTypeDef] = None
    sessionUpdate: Optional[LiveTailSessionUpdateTypeDef] = None
    SessionTimeoutException: Optional[SessionTimeoutExceptionTypeDef] = None
    SessionStreamingException: Optional[SessionStreamingExceptionTypeDef] = None

class DescribeMetricFiltersResponseTypeDef(BaseValidatorModel):
    metricFilters: List[MetricFilterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLiveTailResponseTypeDef(BaseValidatorModel):
    responseStream: "EventStream[StartLiveTailResponseStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

