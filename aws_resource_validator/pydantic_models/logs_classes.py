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
from aws_resource_validator.pydantic_models.logs_constants import *

class AccountPolicyTypeDef(BaseModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None
    policyType: Optional[PolicyTypeType] = None
    scope: Optional[Literal["ALL"]] = None
    selectionCriteria: Optional[str] = None
    accountId: Optional[str] = None

class AnomalyDetectorTypeDef(BaseModel):
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

class LogEventTypeDef(BaseModel):
    timestamp: Optional[int] = None
    message: Optional[str] = None

class PatternTokenTypeDef(BaseModel):
    dynamicTokenPosition: Optional[int] = None
    isDynamic: Optional[bool] = None
    tokenString: Optional[str] = None
    enumerations: Optional[Dict[str, int]] = None

class AssociateKmsKeyRequestRequestTypeDef(BaseModel):
    kmsKeyId: str
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None

class CancelExportTaskRequestRequestTypeDef(BaseModel):
    taskId: str

class CreateDeliveryRequestRequestTypeDef(BaseModel):
    deliverySourceName: str
    deliveryDestinationArn: str
    tags: Optional[Mapping[str, str]] = None

class DeliveryTypeDef(BaseModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    deliverySourceName: Optional[str] = None
    deliveryDestinationArn: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    tags: Optional[Dict[str, str]] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateExportTaskRequestRequestTypeDef(BaseModel):
    logGroupName: str
    fromTime: int
    to: int
    destination: str
    taskName: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    destinationPrefix: Optional[str] = None

class CreateLogAnomalyDetectorRequestRequestTypeDef(BaseModel):
    logGroupArnList: Sequence[str]
    detectorName: Optional[str] = None
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    kmsKeyId: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None
    tags: Optional[Mapping[str, str]] = None

class CreateLogGroupRequestRequestTypeDef(BaseModel):
    logGroupName: str
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    logGroupClass: Optional[LogGroupClassType] = None

class CreateLogStreamRequestRequestTypeDef(BaseModel):
    logGroupName: str
    logStreamName: str

class DeleteAccountPolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    policyType: PolicyTypeType

class DeleteDataProtectionPolicyRequestRequestTypeDef(BaseModel):
    logGroupIdentifier: str

class DeleteDeliveryDestinationPolicyRequestRequestTypeDef(BaseModel):
    deliveryDestinationName: str

class DeleteDeliveryDestinationRequestRequestTypeDef(BaseModel):
    name: str

class DeleteDeliveryRequestRequestTypeDef(BaseModel):
    id: str

class DeleteDeliverySourceRequestRequestTypeDef(BaseModel):
    name: str

class DeleteDestinationRequestRequestTypeDef(BaseModel):
    destinationName: str

class DeleteLogAnomalyDetectorRequestRequestTypeDef(BaseModel):
    anomalyDetectorArn: str

class DeleteLogGroupRequestRequestTypeDef(BaseModel):
    logGroupName: str

class DeleteLogStreamRequestRequestTypeDef(BaseModel):
    logGroupName: str
    logStreamName: str

class DeleteMetricFilterRequestRequestTypeDef(BaseModel):
    logGroupName: str
    filterName: str

class DeleteQueryDefinitionRequestRequestTypeDef(BaseModel):
    queryDefinitionId: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    policyName: Optional[str] = None

class DeleteRetentionPolicyRequestRequestTypeDef(BaseModel):
    logGroupName: str

class DeleteSubscriptionFilterRequestRequestTypeDef(BaseModel):
    logGroupName: str
    filterName: str

class DeliveryDestinationConfigurationTypeDef(BaseModel):
    destinationResourceArn: str

class DeliverySourceTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    resourceArns: Optional[List[str]] = None
    service: Optional[str] = None
    logType: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class DescribeAccountPoliciesRequestRequestTypeDef(BaseModel):
    policyType: PolicyTypeType
    policyName: Optional[str] = None
    accountIdentifiers: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDeliveriesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeDeliveryDestinationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeDeliverySourcesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeDestinationsRequestRequestTypeDef(BaseModel):
    DestinationNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DestinationTypeDef(BaseModel):
    destinationName: Optional[str] = None
    targetArn: Optional[str] = None
    roleArn: Optional[str] = None
    accessPolicy: Optional[str] = None
    arn: Optional[str] = None
    creationTime: Optional[int] = None

class DescribeExportTasksRequestRequestTypeDef(BaseModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class DescribeLogGroupsRequestRequestTypeDef(BaseModel):
    accountIdentifiers: Optional[Sequence[str]] = None
    logGroupNamePrefix: Optional[str] = None
    logGroupNamePattern: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    includeLinkedAccounts: Optional[bool] = None
    logGroupClass: Optional[LogGroupClassType] = None

class LogGroupTypeDef(BaseModel):
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

class DescribeLogStreamsRequestRequestTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    orderBy: Optional[OrderByType] = None
    descending: Optional[bool] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class LogStreamTypeDef(BaseModel):
    logStreamName: Optional[str] = None
    creationTime: Optional[int] = None
    firstEventTimestamp: Optional[int] = None
    lastEventTimestamp: Optional[int] = None
    lastIngestionTime: Optional[int] = None
    uploadSequenceToken: Optional[str] = None
    arn: Optional[str] = None
    storedBytes: Optional[int] = None

class DescribeMetricFiltersRequestRequestTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None

class DescribeQueriesRequestRequestTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueryInfoTypeDef(BaseModel):
    queryId: Optional[str] = None
    queryString: Optional[str] = None
    status: Optional[QueryStatusType] = None
    createTime: Optional[int] = None
    logGroupName: Optional[str] = None

class DescribeQueryDefinitionsRequestRequestTypeDef(BaseModel):
    queryDefinitionNamePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QueryDefinitionTypeDef(BaseModel):
    queryDefinitionId: Optional[str] = None
    name: Optional[str] = None
    queryString: Optional[str] = None
    lastModified: Optional[int] = None
    logGroupNames: Optional[List[str]] = None

class DescribeResourcePoliciesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class ResourcePolicyTypeDef(BaseModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None
    lastUpdatedTime: Optional[int] = None

class DescribeSubscriptionFiltersRequestRequestTypeDef(BaseModel):
    logGroupName: str
    filterNamePrefix: Optional[str] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None

class SubscriptionFilterTypeDef(BaseModel):
    filterName: Optional[str] = None
    logGroupName: Optional[str] = None
    filterPattern: Optional[str] = None
    destinationArn: Optional[str] = None
    roleArn: Optional[str] = None
    distribution: Optional[DistributionType] = None
    creationTime: Optional[int] = None

class DisassociateKmsKeyRequestRequestTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    resourceIdentifier: Optional[str] = None

class ExportTaskExecutionInfoTypeDef(BaseModel):
    creationTime: Optional[int] = None
    completionTime: Optional[int] = None

class ExportTaskStatusTypeDef(BaseModel):
    code: Optional[ExportTaskStatusCodeType] = None
    message: Optional[str] = None

class FilterLogEventsRequestRequestTypeDef(BaseModel):
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

class FilteredLogEventTypeDef(BaseModel):
    logStreamName: Optional[str] = None
    timestamp: Optional[int] = None
    message: Optional[str] = None
    ingestionTime: Optional[int] = None
    eventId: Optional[str] = None

class SearchedLogStreamTypeDef(BaseModel):
    logStreamName: Optional[str] = None
    searchedCompletely: Optional[bool] = None

class GetDataProtectionPolicyRequestRequestTypeDef(BaseModel):
    logGroupIdentifier: str

class GetDeliveryDestinationPolicyRequestRequestTypeDef(BaseModel):
    deliveryDestinationName: str

class PolicyTypeDef(BaseModel):
    deliveryDestinationPolicy: Optional[str] = None

class GetDeliveryDestinationRequestRequestTypeDef(BaseModel):
    name: str

class GetDeliveryRequestRequestTypeDef(BaseModel):
    id: str

class GetDeliverySourceRequestRequestTypeDef(BaseModel):
    name: str

class GetLogAnomalyDetectorRequestRequestTypeDef(BaseModel):
    anomalyDetectorArn: str

class GetLogEventsRequestRequestTypeDef(BaseModel):
    logStreamName: str
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    startTime: Optional[int] = None
    endTime: Optional[int] = None
    nextToken: Optional[str] = None
    limit: Optional[int] = None
    startFromHead: Optional[bool] = None
    unmask: Optional[bool] = None

class OutputLogEventTypeDef(BaseModel):
    timestamp: Optional[int] = None
    message: Optional[str] = None
    ingestionTime: Optional[int] = None

class GetLogGroupFieldsRequestRequestTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    time: Optional[int] = None
    logGroupIdentifier: Optional[str] = None

class LogGroupFieldTypeDef(BaseModel):
    name: Optional[str] = None
    percent: Optional[int] = None

class GetLogRecordRequestRequestTypeDef(BaseModel):
    logRecordPointer: str
    unmask: Optional[bool] = None

class GetQueryResultsRequestRequestTypeDef(BaseModel):
    queryId: str

class QueryStatisticsTypeDef(BaseModel):
    recordsMatched: Optional[float] = None
    recordsScanned: Optional[float] = None
    bytesScanned: Optional[float] = None

class ResultFieldTypeDef(BaseModel):
    field: Optional[str] = None
    value: Optional[str] = None

class InputLogEventTypeDef(BaseModel):
    timestamp: int
    message: str

class ListAnomaliesRequestRequestTypeDef(BaseModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ListLogAnomalyDetectorsRequestRequestTypeDef(BaseModel):
    filterLogGroupArn: Optional[str] = None
    limit: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTagsLogGroupRequestRequestTypeDef(BaseModel):
    logGroupName: str

class LiveTailSessionLogEventTypeDef(BaseModel):
    logStreamName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    message: Optional[str] = None
    timestamp: Optional[int] = None
    ingestionTime: Optional[int] = None

class LiveTailSessionMetadataTypeDef(BaseModel):
    sampled: Optional[bool] = None

class LiveTailSessionStartTypeDef(BaseModel):
    requestId: Optional[str] = None
    sessionId: Optional[str] = None
    logGroupIdentifiers: Optional[List[str]] = None
    logStreamNames: Optional[List[str]] = None
    logStreamNamePrefixes: Optional[List[str]] = None
    logEventFilterPattern: Optional[str] = None

class MetricFilterMatchRecordTypeDef(BaseModel):
    eventNumber: Optional[int] = None
    eventMessage: Optional[str] = None
    extractedValues: Optional[Dict[str, str]] = None

class MetricTransformationTypeDef(BaseModel):
    metricName: str
    metricNamespace: str
    metricValue: str
    defaultValue: Optional[float] = None
    dimensions: Optional[Dict[str, str]] = None
    unit: Optional[StandardUnitType] = None

class PutAccountPolicyRequestRequestTypeDef(BaseModel):
    policyName: str
    policyDocument: str
    policyType: PolicyTypeType
    scope: Optional[Literal["ALL"]] = None
    selectionCriteria: Optional[str] = None

class PutDataProtectionPolicyRequestRequestTypeDef(BaseModel):
    logGroupIdentifier: str
    policyDocument: str

class PutDeliveryDestinationPolicyRequestRequestTypeDef(BaseModel):
    deliveryDestinationName: str
    deliveryDestinationPolicy: str

class PutDeliverySourceRequestRequestTypeDef(BaseModel):
    name: str
    resourceArn: str
    logType: str
    tags: Optional[Mapping[str, str]] = None

class PutDestinationPolicyRequestRequestTypeDef(BaseModel):
    destinationName: str
    accessPolicy: str
    forceUpdate: Optional[bool] = None

class PutDestinationRequestRequestTypeDef(BaseModel):
    destinationName: str
    targetArn: str
    roleArn: str
    tags: Optional[Mapping[str, str]] = None

class RejectedLogEventsInfoTypeDef(BaseModel):
    tooNewLogEventStartIndex: Optional[int] = None
    tooOldLogEventEndIndex: Optional[int] = None
    expiredLogEventEndIndex: Optional[int] = None

class PutQueryDefinitionRequestRequestTypeDef(BaseModel):
    name: str
    queryString: str
    queryDefinitionId: Optional[str] = None
    logGroupNames: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    policyName: Optional[str] = None
    policyDocument: Optional[str] = None

class PutRetentionPolicyRequestRequestTypeDef(BaseModel):
    logGroupName: str
    retentionInDays: int

class PutSubscriptionFilterRequestRequestTypeDef(BaseModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    destinationArn: str
    roleArn: Optional[str] = None
    distribution: Optional[DistributionType] = None

class SessionStreamingExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class SessionTimeoutExceptionTypeDef(BaseModel):
    message: Optional[str] = None

class StartLiveTailRequestRequestTypeDef(BaseModel):
    logGroupIdentifiers: Sequence[str]
    logStreamNames: Optional[Sequence[str]] = None
    logStreamNamePrefixes: Optional[Sequence[str]] = None
    logEventFilterPattern: Optional[str] = None

class StartQueryRequestRequestTypeDef(BaseModel):
    startTime: int
    endTime: int
    queryString: str
    logGroupName: Optional[str] = None
    logGroupNames: Optional[Sequence[str]] = None
    logGroupIdentifiers: Optional[Sequence[str]] = None
    limit: Optional[int] = None

class StopQueryRequestRequestTypeDef(BaseModel):
    queryId: str

class SuppressionPeriodTypeDef(BaseModel):
    value: Optional[int] = None
    suppressionUnit: Optional[SuppressionUnitType] = None

class TagLogGroupRequestRequestTypeDef(BaseModel):
    logGroupName: str
    tags: Mapping[str, str]

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TestMetricFilterRequestRequestTypeDef(BaseModel):
    filterPattern: str
    logEventMessages: Sequence[str]

class UntagLogGroupRequestRequestTypeDef(BaseModel):
    logGroupName: str
    tags: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateLogAnomalyDetectorRequestRequestTypeDef(BaseModel):
    anomalyDetectorArn: str
    enabled: bool
    evaluationFrequency: Optional[EvaluationFrequencyType] = None
    filterPattern: Optional[str] = None
    anomalyVisibilityTime: Optional[int] = None

class AnomalyTypeDef(BaseModel):
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

class CreateDeliveryResponseTypeDef(BaseModel):
    delivery: DeliveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateExportTaskResponseTypeDef(BaseModel):
    taskId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLogAnomalyDetectorResponseTypeDef(BaseModel):
    anomalyDetectorArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteQueryDefinitionResponseTypeDef(BaseModel):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountPoliciesResponseTypeDef(BaseModel):
    accountPolicies: List[AccountPolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeliveriesResponseTypeDef(BaseModel):
    deliveries: List[DeliveryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataProtectionPolicyResponseTypeDef(BaseModel):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliveryResponseTypeDef(BaseModel):
    delivery: DeliveryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLogAnomalyDetectorResponseTypeDef(BaseModel):
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

class GetLogRecordResponseTypeDef(BaseModel):
    logRecord: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListLogAnomalyDetectorsResponseTypeDef(BaseModel):
    anomalyDetectors: List[AnomalyDetectorTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsLogGroupResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountPolicyResponseTypeDef(BaseModel):
    accountPolicy: AccountPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataProtectionPolicyResponseTypeDef(BaseModel):
    logGroupIdentifier: str
    policyDocument: str
    lastUpdatedTime: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutQueryDefinitionResponseTypeDef(BaseModel):
    queryDefinitionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryResponseTypeDef(BaseModel):
    queryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopQueryResponseTypeDef(BaseModel):
    success: bool
    ResponseMetadata: ResponseMetadataTypeDef

class DeliveryDestinationTypeDef(BaseModel):
    name: Optional[str] = None
    arn: Optional[str] = None
    deliveryDestinationType: Optional[DeliveryDestinationTypeType] = None
    outputFormat: Optional[OutputFormatType] = None
    deliveryDestinationConfiguration: Optional[DeliveryDestinationConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class PutDeliveryDestinationRequestRequestTypeDef(BaseModel):
    name: str
    deliveryDestinationConfiguration: DeliveryDestinationConfigurationTypeDef
    outputFormat: Optional[OutputFormatType] = None
    tags: Optional[Mapping[str, str]] = None

class DescribeDeliverySourcesResponseTypeDef(BaseModel):
    deliverySources: List[DeliverySourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliverySourceResponseTypeDef(BaseModel):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliverySourceResponseTypeDef(BaseModel):
    deliverySource: DeliverySourceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeliveriesRequestDescribeDeliveriesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDeliveryDestinationsRequestDescribeDeliveryDestinationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDeliverySourcesRequestDescribeDeliverySourcesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDestinationsRequestDescribeDestinationsPaginateTypeDef(BaseModel):
    DestinationNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeExportTasksRequestDescribeExportTasksPaginateTypeDef(BaseModel):
    taskId: Optional[str] = None
    statusCode: Optional[ExportTaskStatusCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLogGroupsRequestDescribeLogGroupsPaginateTypeDef(BaseModel):
    accountIdentifiers: Optional[Sequence[str]] = None
    logGroupNamePrefix: Optional[str] = None
    logGroupNamePattern: Optional[str] = None
    includeLinkedAccounts: Optional[bool] = None
    logGroupClass: Optional[LogGroupClassType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeLogStreamsRequestDescribeLogStreamsPaginateTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    logGroupIdentifier: Optional[str] = None
    logStreamNamePrefix: Optional[str] = None
    orderBy: Optional[OrderByType] = None
    descending: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeMetricFiltersRequestDescribeMetricFiltersPaginateTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    filterNamePrefix: Optional[str] = None
    metricName: Optional[str] = None
    metricNamespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeQueriesRequestDescribeQueriesPaginateTypeDef(BaseModel):
    logGroupName: Optional[str] = None
    status: Optional[QueryStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeResourcePoliciesRequestDescribeResourcePoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubscriptionFiltersRequestDescribeSubscriptionFiltersPaginateTypeDef(BaseModel):
    logGroupName: str
    filterNamePrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class FilterLogEventsRequestFilterLogEventsPaginateTypeDef(BaseModel):
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

class ListAnomaliesRequestListAnomaliesPaginateTypeDef(BaseModel):
    anomalyDetectorArn: Optional[str] = None
    suppressionState: Optional[SuppressionStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLogAnomalyDetectorsRequestListLogAnomalyDetectorsPaginateTypeDef(BaseModel):
    filterLogGroupArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDestinationsResponseTypeDef(BaseModel):
    destinations: List[DestinationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutDestinationResponseTypeDef(BaseModel):
    destination: DestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLogGroupsResponseTypeDef(BaseModel):
    logGroups: List[LogGroupTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLogStreamsResponseTypeDef(BaseModel):
    logStreams: List[LogStreamTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeQueriesResponseTypeDef(BaseModel):
    queries: List[QueryInfoTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeQueryDefinitionsResponseTypeDef(BaseModel):
    queryDefinitions: List[QueryDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeResourcePoliciesResponseTypeDef(BaseModel):
    resourcePolicies: List[ResourcePolicyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyResponseTypeDef(BaseModel):
    resourcePolicy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubscriptionFiltersResponseTypeDef(BaseModel):
    subscriptionFilters: List[SubscriptionFilterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTaskTypeDef(BaseModel):
    taskId: Optional[str] = None
    taskName: Optional[str] = None
    logGroupName: Optional[str] = None
    from: Optional[int] = None
    to: Optional[int] = None
    destination: Optional[str] = None
    destinationPrefix: Optional[str] = None
    status: Optional[ExportTaskStatusTypeDef] = None
    executionInfo: Optional[ExportTaskExecutionInfoTypeDef] = None

class FilterLogEventsResponseTypeDef(BaseModel):
    events: List[FilteredLogEventTypeDef]
    searchedLogStreams: List[SearchedLogStreamTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliveryDestinationPolicyResponseTypeDef(BaseModel):
    policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryDestinationPolicyResponseTypeDef(BaseModel):
    policy: PolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLogEventsResponseTypeDef(BaseModel):
    events: List[OutputLogEventTypeDef]
    nextForwardToken: str
    nextBackwardToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLogGroupFieldsResponseTypeDef(BaseModel):
    logGroupFields: List[LogGroupFieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryResultsResponseTypeDef(BaseModel):
    results: List[List[ResultFieldTypeDef]]
    statistics: QueryStatisticsTypeDef
    status: QueryStatusType
    encryptionKey: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutLogEventsRequestRequestTypeDef(BaseModel):
    logGroupName: str
    logStreamName: str
    logEvents: Sequence[InputLogEventTypeDef]
    sequenceToken: Optional[str] = None

class LiveTailSessionUpdateTypeDef(BaseModel):
    sessionMetadata: Optional[LiveTailSessionMetadataTypeDef] = None
    sessionResults: Optional[List[LiveTailSessionLogEventTypeDef]] = None

class TestMetricFilterResponseTypeDef(BaseModel):
    matches: List[MetricFilterMatchRecordTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MetricFilterTypeDef(BaseModel):
    filterName: Optional[str] = None
    filterPattern: Optional[str] = None
    metricTransformations: Optional[List[MetricTransformationTypeDef]] = None
    creationTime: Optional[int] = None
    logGroupName: Optional[str] = None

class PutMetricFilterRequestRequestTypeDef(BaseModel):
    logGroupName: str
    filterName: str
    filterPattern: str
    metricTransformations: Sequence[MetricTransformationTypeDef]

class PutLogEventsResponseTypeDef(BaseModel):
    nextSequenceToken: str
    rejectedLogEventsInfo: RejectedLogEventsInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAnomalyRequestRequestTypeDef(BaseModel):
    anomalyDetectorArn: str
    anomalyId: Optional[str] = None
    patternId: Optional[str] = None
    suppressionType: Optional[SuppressionTypeType] = None
    suppressionPeriod: Optional[SuppressionPeriodTypeDef] = None

class ListAnomaliesResponseTypeDef(BaseModel):
    anomalies: List[AnomalyTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDeliveryDestinationsResponseTypeDef(BaseModel):
    deliveryDestinations: List[DeliveryDestinationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetDeliveryDestinationResponseTypeDef(BaseModel):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDeliveryDestinationResponseTypeDef(BaseModel):
    deliveryDestination: DeliveryDestinationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeExportTasksResponseTypeDef(BaseModel):
    exportTasks: List[ExportTaskTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLiveTailResponseStreamTypeDef(BaseModel):
    sessionStart: Optional[LiveTailSessionStartTypeDef] = None
    sessionUpdate: Optional[LiveTailSessionUpdateTypeDef] = None
    SessionTimeoutException: Optional[SessionTimeoutExceptionTypeDef] = None
    SessionStreamingException: Optional[SessionStreamingExceptionTypeDef] = None

class DescribeMetricFiltersResponseTypeDef(BaseModel):
    metricFilters: List[MetricFilterTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLiveTailResponseTypeDef(BaseModel):
    responseStream: "EventStream[StartLiveTailResponseStreamTypeDef]"
    ResponseMetadata: ResponseMetadataTypeDef

