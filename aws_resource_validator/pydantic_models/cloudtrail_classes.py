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
from aws_resource_validator.pydantic_models.cloudtrail_constants import *

class Tag(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None


class AdvancedFieldSelectorOutput(BaseValidatorModel):
    Field: str
    Equals: Optional[List[str]] = None
    StartsWith: Optional[List[str]] = None
    EndsWith: Optional[List[str]] = None
    NotEquals: Optional[List[str]] = None
    NotStartsWith: Optional[List[str]] = None
    NotEndsWith: Optional[List[str]] = None


class AdvancedFieldSelector(BaseValidatorModel):
    Field: str
    Equals: Optional[Sequence[str]] = None
    StartsWith: Optional[Sequence[str]] = None
    EndsWith: Optional[Sequence[str]] = None
    NotEquals: Optional[Sequence[str]] = None
    NotStartsWith: Optional[Sequence[str]] = None
    NotEndsWith: Optional[Sequence[str]] = None


class CancelQueryRequest(BaseValidatorModel):
    QueryId: str
    EventDataStore: Optional[str] = None
    EventDataStoreOwnerAccountId: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Channel(BaseValidatorModel):
    ChannelArn: Optional[str] = None
    Name: Optional[str] = None


class RequestWidget(BaseValidatorModel):
    QueryStatement: str
    ViewProperties: Mapping[str, str]
    QueryParameters: Optional[Sequence[str]] = None


class Widget(BaseValidatorModel):
    QueryAlias: Optional[str] = None
    QueryStatement: Optional[str] = None
    QueryParameters: Optional[List[str]] = None
    ViewProperties: Optional[Dict[str, str]] = None


class DeleteChannelRequest(BaseValidatorModel):
    Channel: str


class DeleteDashboardRequest(BaseValidatorModel):
    DashboardId: str


class DeleteEventDataStoreRequest(BaseValidatorModel):
    EventDataStore: str


class DeleteResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class DeleteTrailRequest(BaseValidatorModel):
    Name: str


class DeregisterOrganizationDelegatedAdminRequest(BaseValidatorModel):
    DelegatedAdminAccountId: str


class DescribeQueryRequest(BaseValidatorModel):
    EventDataStore: Optional[str] = None
    QueryId: Optional[str] = None
    QueryAlias: Optional[str] = None
    RefreshId: Optional[str] = None
    EventDataStoreOwnerAccountId: Optional[str] = None


class QueryStatisticsForDescribeQuery(BaseValidatorModel):
    EventsMatched: Optional[int] = None
    EventsScanned: Optional[int] = None
    BytesScanned: Optional[int] = None
    ExecutionTimeInMillis: Optional[int] = None
    CreationTime: Optional[datetime] = None


class DescribeTrailsRequest(BaseValidatorModel):
    trailNameList: Optional[Sequence[str]] = None
    includeShadowTrails: Optional[bool] = None


class Trail(BaseValidatorModel):
    Name: Optional[str] = None
    S3BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    SnsTopicName: Optional[str] = None
    SnsTopicARN: Optional[str] = None
    IncludeGlobalServiceEvents: Optional[bool] = None
    IsMultiRegionTrail: Optional[bool] = None
    HomeRegion: Optional[str] = None
    TrailARN: Optional[str] = None
    LogFileValidationEnabled: Optional[bool] = None
    CloudWatchLogsLogGroupArn: Optional[str] = None
    CloudWatchLogsRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    HasCustomEventSelectors: Optional[bool] = None
    HasInsightSelectors: Optional[bool] = None
    IsOrganizationTrail: Optional[bool] = None


class DisableFederationRequest(BaseValidatorModel):
    EventDataStore: str


class EnableFederationRequest(BaseValidatorModel):
    EventDataStore: str
    FederationRoleArn: str


class Resource(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceName: Optional[str] = None


class GenerateQueryRequest(BaseValidatorModel):
    EventDataStores: Sequence[str]
    Prompt: str


class GetChannelRequest(BaseValidatorModel):
    Channel: str


class IngestionStatus(BaseValidatorModel):
    LatestIngestionSuccessTime: Optional[datetime] = None
    LatestIngestionSuccessEventID: Optional[str] = None
    LatestIngestionErrorCode: Optional[str] = None
    LatestIngestionAttemptTime: Optional[datetime] = None
    LatestIngestionAttemptEventID: Optional[str] = None


class GetDashboardRequest(BaseValidatorModel):
    DashboardId: str


class GetEventDataStoreRequest(BaseValidatorModel):
    EventDataStore: str


class GetEventSelectorsRequest(BaseValidatorModel):
    TrailName: str


class GetImportRequest(BaseValidatorModel):
    ImportId: str


class ImportStatistics(BaseValidatorModel):
    PrefixesFound: Optional[int] = None
    PrefixesCompleted: Optional[int] = None
    FilesCompleted: Optional[int] = None
    EventsCompleted: Optional[int] = None
    FailedEntries: Optional[int] = None


class GetInsightSelectorsRequest(BaseValidatorModel):
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None


class InsightSelector(BaseValidatorModel):
    InsightType: Optional[InsightTypeType] = None


class GetQueryResultsRequest(BaseValidatorModel):
    QueryId: str
    EventDataStore: Optional[str] = None
    NextToken: Optional[str] = None
    MaxQueryResults: Optional[int] = None
    EventDataStoreOwnerAccountId: Optional[str] = None


class QueryStatistics(BaseValidatorModel):
    ResultsCount: Optional[int] = None
    TotalResultsCount: Optional[int] = None
    BytesScanned: Optional[int] = None


class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


class GetTrailRequest(BaseValidatorModel):
    Name: str


class GetTrailStatusRequest(BaseValidatorModel):
    Name: str


class ImportFailureListItem(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[ImportFailureStatusType] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None


class S3ImportSource(BaseValidatorModel):
    S3LocationUri: str
    S3BucketRegion: str
    S3BucketAccessRoleArn: str


class ImportsListItem(BaseValidatorModel):
    ImportId: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    Destinations: Optional[List[str]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class ListChannelsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEventDataStoresRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListImportFailuresRequest(BaseValidatorModel):
    ImportId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListImportsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    Destination: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    NextToken: Optional[str] = None


class PublicKey(BaseValidatorModel):
    Value: Optional[bytes] = None
    ValidityStartTime: Optional[datetime] = None
    ValidityEndTime: Optional[datetime] = None
    Fingerprint: Optional[str] = None


class Query(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStatus: Optional[QueryStatusType] = None
    CreationTime: Optional[datetime] = None


class ListTagsRequest(BaseValidatorModel):
    ResourceIdList: Sequence[str]
    NextToken: Optional[str] = None


class ListTrailsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class TrailInfo(BaseValidatorModel):
    TrailARN: Optional[str] = None
    Name: Optional[str] = None
    HomeRegion: Optional[str] = None


class LookupAttribute(BaseValidatorModel):
    AttributeKey: LookupAttributeKeyType
    AttributeValue: str


class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str


class RefreshScheduleFrequency(BaseValidatorModel):
    Unit: Optional[RefreshScheduleFrequencyUnitType] = None
    Value: Optional[int] = None


class RegisterOrganizationDelegatedAdminRequest(BaseValidatorModel):
    MemberAccountId: str


class RestoreEventDataStoreRequest(BaseValidatorModel):
    EventDataStore: str


class SearchSampleQueriesRequest(BaseValidatorModel):
    SearchPhrase: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SearchSampleQueriesSearchResult(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    SQL: Optional[str] = None
    Relevance: Optional[float] = None


class StartDashboardRefreshRequest(BaseValidatorModel):
    DashboardId: str
    QueryParameterValues: Optional[Mapping[str, str]] = None


class StartEventDataStoreIngestionRequest(BaseValidatorModel):
    EventDataStore: str


class StartLoggingRequest(BaseValidatorModel):
    Name: str


class StartQueryRequest(BaseValidatorModel):
    QueryStatement: Optional[str] = None
    DeliveryS3Uri: Optional[str] = None
    QueryAlias: Optional[str] = None
    QueryParameters: Optional[Sequence[str]] = None
    EventDataStoreOwnerAccountId: Optional[str] = None


class StopEventDataStoreIngestionRequest(BaseValidatorModel):
    EventDataStore: str


class StopImportRequest(BaseValidatorModel):
    ImportId: str


class StopLoggingRequest(BaseValidatorModel):
    Name: str


class UpdateTrailRequest(BaseValidatorModel):
    Name: str
    S3BucketName: Optional[str] = None
    S3KeyPrefix: Optional[str] = None
    SnsTopicName: Optional[str] = None
    IncludeGlobalServiceEvents: Optional[bool] = None
    IsMultiRegionTrail: Optional[bool] = None
    EnableLogFileValidation: Optional[bool] = None
    CloudWatchLogsLogGroupArn: Optional[str] = None
    CloudWatchLogsRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    IsOrganizationTrail: Optional[bool] = None


class AddTagsRequest(BaseValidatorModel):
    ResourceId: str
    TagsList: Sequence[Tag]


class CreateTrailRequest(BaseValidatorModel):
    Name: str
    S3BucketName: str
    S3KeyPrefix: Optional[str] = None
    SnsTopicName: Optional[str] = None
    IncludeGlobalServiceEvents: Optional[bool] = None
    IsMultiRegionTrail: Optional[bool] = None
    EnableLogFileValidation: Optional[bool] = None
    CloudWatchLogsLogGroupArn: Optional[str] = None
    CloudWatchLogsRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    IsOrganizationTrail: Optional[bool] = None
    TagsList: Optional[Sequence[Tag]] = None


class RemoveTagsRequest(BaseValidatorModel):
    ResourceId: str
    TagsList: Sequence[Tag]


class ResourceTag(BaseValidatorModel):
    ResourceId: Optional[str] = None
    TagsList: Optional[List[Tag]] = None


class AdvancedEventSelectorOutput(BaseValidatorModel):
    FieldSelectors: List[AdvancedFieldSelectorOutput]
    Name: Optional[str] = None


class CancelQueryResponse(BaseValidatorModel):
    QueryId: str
    QueryStatus: QueryStatusType
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadata


class CreateTrailResponse(BaseValidatorModel):
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicName: str
    SnsTopicARN: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    TrailARN: str
    LogFileValidationEnabled: bool
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    KmsKeyId: str
    IsOrganizationTrail: bool
    ResponseMetadata: ResponseMetadata


class DisableFederationResponse(BaseValidatorModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    ResponseMetadata: ResponseMetadata


class EnableFederationResponse(BaseValidatorModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    ResponseMetadata: ResponseMetadata


class GenerateQueryResponse(BaseValidatorModel):
    QueryStatement: str
    QueryAlias: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    DelegatedAdminResourcePolicy: str
    ResponseMetadata: ResponseMetadata


class GetTrailStatusResponse(BaseValidatorModel):
    IsLogging: bool
    LatestDeliveryError: str
    LatestNotificationError: str
    LatestDeliveryTime: datetime
    LatestNotificationTime: datetime
    StartLoggingTime: datetime
    StopLoggingTime: datetime
    LatestCloudWatchLogsDeliveryError: str
    LatestCloudWatchLogsDeliveryTime: datetime
    LatestDigestDeliveryTime: datetime
    LatestDigestDeliveryError: str
    LatestDeliveryAttemptTime: str
    LatestNotificationAttemptTime: str
    LatestNotificationAttemptSucceeded: str
    LatestDeliveryAttemptSucceeded: str
    TimeLoggingStarted: str
    TimeLoggingStopped: str
    ResponseMetadata: ResponseMetadata


class ListInsightsMetricDataResponse(BaseValidatorModel):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: str
    Timestamps: List[datetime]
    Values: List[float]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    DelegatedAdminResourcePolicy: str
    ResponseMetadata: ResponseMetadata


class StartDashboardRefreshResponse(BaseValidatorModel):
    RefreshId: str
    ResponseMetadata: ResponseMetadata


class StartQueryResponse(BaseValidatorModel):
    QueryId: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadata


class UpdateTrailResponse(BaseValidatorModel):
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicName: str
    SnsTopicARN: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    TrailARN: str
    LogFileValidationEnabled: bool
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    KmsKeyId: str
    IsOrganizationTrail: bool
    ResponseMetadata: ResponseMetadata


class ListChannelsResponse(BaseValidatorModel):
    Channels: List[Channel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Destination(BaseValidatorModel):
    pass


class CreateChannelRequest(BaseValidatorModel):
    Name: str
    Source: str
    Destinations: Sequence[Destination]
    Tags: Optional[Sequence[Tag]] = None


class CreateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[Destination]
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UpdateChannelRequest(BaseValidatorModel):
    Channel: str
    Destinations: Optional[Sequence[Destination]] = None
    Name: Optional[str] = None


class UpdateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[Destination]
    ResponseMetadata: ResponseMetadata


class DashboardDetail(BaseValidatorModel):
    pass


class ListDashboardsResponse(BaseValidatorModel):
    Dashboards: List[DashboardDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DataResourceOutput(BaseValidatorModel):
    pass


class EventSelectorOutput(BaseValidatorModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[List[DataResourceOutput]] = None
    ExcludeManagementEventSources: Optional[List[str]] = None


class DescribeQueryResponse(BaseValidatorModel):
    QueryId: str
    QueryString: str
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatisticsForDescribeQuery
    ErrorMessage: str
    DeliveryS3Uri: str
    DeliveryStatus: DeliveryStatusType
    Prompt: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadata


class DescribeTrailsResponse(BaseValidatorModel):
    trailList: List[Trail]
    ResponseMetadata: ResponseMetadata


class GetTrailResponse(BaseValidatorModel):
    Trail: Trail
    ResponseMetadata: ResponseMetadata


class GetInsightSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    InsightSelectors: List[InsightSelector]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadata


class PutInsightSelectorsRequest(BaseValidatorModel):
    InsightSelectors: Sequence[InsightSelector]
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None
    InsightsDestination: Optional[str] = None


class PutInsightSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    InsightSelectors: List[InsightSelector]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadata


class GetQueryResultsResponse(BaseValidatorModel):
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatistics
    QueryResultRows: List[List[Dict[str, str]]]
    ErrorMessage: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListImportFailuresResponse(BaseValidatorModel):
    Failures: List[ImportFailureListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ImportSource(BaseValidatorModel):
    S3: S3ImportSource


class ListImportsResponse(BaseValidatorModel):
    Imports: List[ImportsListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListImportFailuresRequestPaginate(BaseValidatorModel):
    ImportId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportsRequestPaginate(BaseValidatorModel):
    Destination: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsRequestPaginate(BaseValidatorModel):
    ResourceIdList: Sequence[str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrailsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class ListInsightsMetricDataRequest(BaseValidatorModel):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: Optional[str] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Period: Optional[int] = None
    DataType: Optional[InsightsMetricDataTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPublicKeysRequestPaginate(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPublicKeysRequest(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None


class ListQueriesRequest(BaseValidatorModel):
    EventDataStore: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    QueryStatus: Optional[QueryStatusType] = None


class ListPublicKeysResponse(BaseValidatorModel):
    PublicKeyList: List[PublicKey]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListQueriesResponse(BaseValidatorModel):
    Queries: List[Query]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrailsResponse(BaseValidatorModel):
    Trails: List[TrailInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LookupEventsRequestPaginate(BaseValidatorModel):
    LookupAttributes: Optional[Sequence[LookupAttribute]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventCategory: Optional[Literal["insight"]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class LookupEventsRequest(BaseValidatorModel):
    LookupAttributes: Optional[Sequence[LookupAttribute]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventCategory: Optional[Literal["insight"]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RefreshSchedule(BaseValidatorModel):
    Frequency: Optional[RefreshScheduleFrequency] = None
    Status: Optional[RefreshScheduleStatusType] = None
    TimeOfDay: Optional[str] = None


class SearchSampleQueriesResponse(BaseValidatorModel):
    SearchResults: List[SearchSampleQueriesSearchResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsResponse(BaseValidatorModel):
    ResourceTagList: List[ResourceTag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateEventDataStoreResponse(BaseValidatorModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    TagsList: List[Tag]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    ResponseMetadata: ResponseMetadata


class EventDataStore(BaseValidatorModel):
    EventDataStoreArn: Optional[str] = None
    Name: Optional[str] = None
    TerminationProtectionEnabled: Optional[bool] = None
    Status: Optional[EventDataStoreStatusType] = None
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorOutput]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class PartitionKey(BaseValidatorModel):
    pass


class GetEventDataStoreResponse(BaseValidatorModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    PartitionKeys: List[PartitionKey]
    ResponseMetadata: ResponseMetadata


class RestoreEventDataStoreResponse(BaseValidatorModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    ResponseMetadata: ResponseMetadata


class SourceConfig(BaseValidatorModel):
    ApplyToAllRegions: Optional[bool] = None
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorOutput]] = None


class UpdateEventDataStoreResponse(BaseValidatorModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    ResponseMetadata: ResponseMetadata


class AdvancedFieldSelectorUnion(BaseValidatorModel):
    pass


class AdvancedEventSelector(BaseValidatorModel):
    FieldSelectors: Sequence[AdvancedFieldSelectorUnion]
    Name: Optional[str] = None


class GetEventSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutput]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    ResponseMetadata: ResponseMetadata


class PutEventSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutput]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    ResponseMetadata: ResponseMetadata


class DataResourceUnion(BaseValidatorModel):
    pass


class EventSelector(BaseValidatorModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[Sequence[DataResourceUnion]] = None
    ExcludeManagementEventSources: Optional[Sequence[str]] = None


class Event(BaseValidatorModel):
    pass


class LookupEventsResponse(BaseValidatorModel):
    Events: List[Event]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetImportResponse(BaseValidatorModel):
    ImportId: str
    Destinations: List[str]
    ImportSource: ImportSource
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ImportStatistics: ImportStatistics
    ResponseMetadata: ResponseMetadata


class StartImportRequest(BaseValidatorModel):
    Destinations: Optional[Sequence[str]] = None
    ImportSource: Optional[ImportSource] = None
    StartEventTime: Optional[Timestamp] = None
    EndEventTime: Optional[Timestamp] = None
    ImportId: Optional[str] = None


class StartImportResponse(BaseValidatorModel):
    ImportId: str
    Destinations: List[str]
    ImportSource: ImportSource
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class StopImportResponse(BaseValidatorModel):
    ImportId: str
    ImportSource: ImportSource
    Destinations: List[str]
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatistics: ImportStatistics
    ResponseMetadata: ResponseMetadata


class CreateDashboardRequest(BaseValidatorModel):
    Name: str
    RefreshSchedule: Optional[RefreshSchedule] = None
    TagsList: Optional[Sequence[Tag]] = None
    TerminationProtectionEnabled: Optional[bool] = None
    Widgets: Optional[Sequence[RequestWidget]] = None


class UpdateDashboardRequest(BaseValidatorModel):
    DashboardId: str
    Widgets: Optional[Sequence[RequestWidget]] = None
    RefreshSchedule: Optional[RefreshSchedule] = None
    TerminationProtectionEnabled: Optional[bool] = None


class ListEventDataStoresResponse(BaseValidatorModel):
    EventDataStores: List[EventDataStore]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetChannelResponse(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    SourceConfig: SourceConfig
    Destinations: List[Destination]
    IngestionStatus: IngestionStatus
    ResponseMetadata: ResponseMetadata


class AdvancedEventSelectorUnion(BaseValidatorModel):
    pass


class CreateEventDataStoreRequest(BaseValidatorModel):
    Name: str
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnion]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    TerminationProtectionEnabled: Optional[bool] = None
    TagsList: Optional[Sequence[Tag]] = None
    KmsKeyId: Optional[str] = None
    StartIngestion: Optional[bool] = None
    BillingMode: Optional[BillingModeType] = None


class UpdateEventDataStoreRequest(BaseValidatorModel):
    EventDataStore: str
    Name: Optional[str] = None
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnion]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    TerminationProtectionEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    BillingMode: Optional[BillingModeType] = None


class EventSelectorUnion(BaseValidatorModel):
    pass


class PutEventSelectorsRequest(BaseValidatorModel):
    TrailName: str
    EventSelectors: Optional[Sequence[EventSelectorUnion]] = None
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnion]] = None


