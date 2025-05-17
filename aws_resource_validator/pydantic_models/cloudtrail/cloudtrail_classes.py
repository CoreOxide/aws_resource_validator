from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cloudtrail.cloudtrail_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    Equals: Optional[List[str]] = None
    StartsWith: Optional[List[str]] = None
    EndsWith: Optional[List[str]] = None
    NotEquals: Optional[List[str]] = None
    NotStartsWith: Optional[List[str]] = None
    NotEndsWith: Optional[List[str]] = None


# This class is the input for the 'cancel_query' function.
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


class Destination(BaseValidatorModel):
    Type: DestinationTypeType
    Location: str


class RequestWidget(BaseValidatorModel):
    QueryStatement: str
    ViewProperties: Dict[str, str]
    QueryParameters: Optional[List[str]] = None


class Widget(BaseValidatorModel):
    QueryAlias: Optional[str] = None
    QueryStatement: Optional[str] = None
    QueryParameters: Optional[List[str]] = None
    ViewProperties: Optional[Dict[str, str]] = None


class DashboardDetail(BaseValidatorModel):
    DashboardArn: Optional[str] = None
    Type: Optional[DashboardTypeType] = None


class DataResourceOutput(BaseValidatorModel):
    Type: Optional[str] = None
    Values: Optional[List[str]] = None


class DataResource(BaseValidatorModel):
    Type: Optional[str] = None
    Values: Optional[List[str]] = None


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


# This class is the input for the 'describe_query' function.
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


# This class is the input for the 'describe_trails' function.
class DescribeTrailsRequest(BaseValidatorModel):
    trailNameList: Optional[List[str]] = None
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


# This class is the input for the 'disable_federation' function.
class DisableFederationRequest(BaseValidatorModel):
    EventDataStore: str


# This class is the input for the 'enable_federation' function.
class EnableFederationRequest(BaseValidatorModel):
    EventDataStore: str
    FederationRoleArn: str


class Resource(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceName: Optional[str] = None


# This class is the input for the 'generate_query' function.
class GenerateQueryRequest(BaseValidatorModel):
    EventDataStores: List[str]
    Prompt: str


# This class is the input for the 'get_channel' function.
class GetChannelRequest(BaseValidatorModel):
    Channel: str


class IngestionStatus(BaseValidatorModel):
    LatestIngestionSuccessTime: Optional[datetime] = None
    LatestIngestionSuccessEventID: Optional[str] = None
    LatestIngestionErrorCode: Optional[str] = None
    LatestIngestionAttemptTime: Optional[datetime] = None
    LatestIngestionAttemptEventID: Optional[str] = None


# This class is the input for the 'get_dashboard' function.
class GetDashboardRequest(BaseValidatorModel):
    DashboardId: str


# This class is the input for the 'get_event_data_store' function.
class GetEventDataStoreRequest(BaseValidatorModel):
    EventDataStore: str


class PartitionKey(BaseValidatorModel):
    Name: str
    Type: str


# This class is the input for the 'get_event_selectors' function.
class GetEventSelectorsRequest(BaseValidatorModel):
    TrailName: str


# This class is the input for the 'get_import' function.
class GetImportRequest(BaseValidatorModel):
    ImportId: str


class ImportStatistics(BaseValidatorModel):
    PrefixesFound: Optional[int] = None
    PrefixesCompleted: Optional[int] = None
    FilesCompleted: Optional[int] = None
    EventsCompleted: Optional[int] = None
    FailedEntries: Optional[int] = None


# This class is the input for the 'get_insight_selectors' function.
class GetInsightSelectorsRequest(BaseValidatorModel):
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None


class InsightSelector(BaseValidatorModel):
    InsightType: Optional[InsightTypeType] = None


# This class is the input for the 'get_query_results' function.
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


# This class is the input for the 'get_resource_policy' function.
class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str


# This class is the input for the 'get_trail' function.
class GetTrailRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'get_trail_status' function.
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


# This class is the input for the 'list_channels' function.
class ListChannelsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_dashboards' function.
class ListDashboardsRequest(BaseValidatorModel):
    NamePrefix: Optional[str] = None
    Type: Optional[DashboardTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_event_data_stores' function.
class ListEventDataStoresRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_import_failures' function.
class ListImportFailuresRequest(BaseValidatorModel):
    ImportId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_imports' function.
class ListImportsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    Destination: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    NextToken: Optional[str] = None

Timestamp = Union[datetime, str]


class PublicKey(BaseValidatorModel):
    Value: Optional[bytes] = None
    ValidityStartTime: Optional[datetime] = None
    ValidityEndTime: Optional[datetime] = None
    Fingerprint: Optional[str] = None


class Query(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStatus: Optional[QueryStatusType] = None
    CreationTime: Optional[datetime] = None


# This class is the input for the 'list_tags' function.
class ListTagsRequest(BaseValidatorModel):
    ResourceIdList: List[str]
    NextToken: Optional[str] = None


# This class is the input for the 'list_trails' function.
class ListTrailsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None


class TrailInfo(BaseValidatorModel):
    TrailARN: Optional[str] = None
    Name: Optional[str] = None
    HomeRegion: Optional[str] = None


class LookupAttribute(BaseValidatorModel):
    AttributeKey: LookupAttributeKeyType
    AttributeValue: str


# This class is the input for the 'put_resource_policy' function.
class PutResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str


class RefreshScheduleFrequency(BaseValidatorModel):
    Unit: Optional[RefreshScheduleFrequencyUnitType] = None
    Value: Optional[int] = None


class RegisterOrganizationDelegatedAdminRequest(BaseValidatorModel):
    MemberAccountId: str


# This class is the input for the 'restore_event_data_store' function.
class RestoreEventDataStoreRequest(BaseValidatorModel):
    EventDataStore: str


# This class is the input for the 'search_sample_queries' function.
class SearchSampleQueriesRequest(BaseValidatorModel):
    SearchPhrase: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SearchSampleQueriesSearchResult(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    SQL: Optional[str] = None
    Relevance: Optional[float] = None


# This class is the input for the 'start_dashboard_refresh' function.
class StartDashboardRefreshRequest(BaseValidatorModel):
    DashboardId: str
    QueryParameterValues: Optional[Dict[str, str]] = None


class StartEventDataStoreIngestionRequest(BaseValidatorModel):
    EventDataStore: str


class StartLoggingRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'start_query' function.
class StartQueryRequest(BaseValidatorModel):
    QueryStatement: Optional[str] = None
    DeliveryS3Uri: Optional[str] = None
    QueryAlias: Optional[str] = None
    QueryParameters: Optional[List[str]] = None
    EventDataStoreOwnerAccountId: Optional[str] = None


class StopEventDataStoreIngestionRequest(BaseValidatorModel):
    EventDataStore: str


# This class is the input for the 'stop_import' function.
class StopImportRequest(BaseValidatorModel):
    ImportId: str


class StopLoggingRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'update_trail' function.
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
    TagsList: List[Tag]


# This class is the input for the 'create_trail' function.
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
    TagsList: Optional[List[Tag]] = None


class RemoveTagsRequest(BaseValidatorModel):
    ResourceId: str
    TagsList: List[Tag]


class ResourceTag(BaseValidatorModel):
    ResourceId: Optional[str] = None
    TagsList: Optional[List[Tag]] = None


class AdvancedEventSelectorOutput(BaseValidatorModel):
    FieldSelectors: List[AdvancedFieldSelectorOutput]
    Name: Optional[str] = None

AdvancedFieldSelectorUnion = Union[AdvancedFieldSelector, AdvancedFieldSelectorOutput]


# This class is the output for the 'cancel_query' function.
class CancelQueryResponse(BaseValidatorModel):
    QueryId: str
    QueryStatus: QueryStatusType
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_trail' function.
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


# This class is the output for the 'disable_federation' function.
class DisableFederationResponse(BaseValidatorModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'enable_federation' function.
class EnableFederationResponse(BaseValidatorModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'generate_query' function.
class GenerateQueryResponse(BaseValidatorModel):
    QueryStatement: str
    QueryAlias: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    DelegatedAdminResourcePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_trail_status' function.
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


# This class is the output for the 'list_insights_metric_data' function.
class ListInsightsMetricDataResponse(BaseValidatorModel):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: str
    Timestamps: List[datetime]
    Values: List[float]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyResponse(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    DelegatedAdminResourcePolicy: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_dashboard_refresh' function.
class StartDashboardRefreshResponse(BaseValidatorModel):
    RefreshId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_query' function.
class StartQueryResponse(BaseValidatorModel):
    QueryId: str
    EventDataStoreOwnerAccountId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_trail' function.
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


# This class is the output for the 'list_channels' function.
class ListChannelsResponse(BaseValidatorModel):
    Channels: List[Channel]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_channel' function.
class CreateChannelRequest(BaseValidatorModel):
    Name: str
    Source: str
    Destinations: List[Destination]
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'create_channel' function.
class CreateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[Destination]
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_channel' function.
class UpdateChannelRequest(BaseValidatorModel):
    Channel: str
    Destinations: Optional[List[Destination]] = None
    Name: Optional[str] = None


# This class is the output for the 'update_channel' function.
class UpdateChannelResponse(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[Destination]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_dashboards' function.
class ListDashboardsResponse(BaseValidatorModel):
    Dashboards: List[DashboardDetail]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EventSelectorOutput(BaseValidatorModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[List[DataResourceOutput]] = None
    ExcludeManagementEventSources: Optional[List[str]] = None

DataResourceUnion = Union[DataResource, DataResourceOutput]


# This class is the output for the 'describe_query' function.
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


# This class is the output for the 'describe_trails' function.
class DescribeTrailsResponse(BaseValidatorModel):
    trailList: List[Trail]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_trail' function.
class GetTrailResponse(BaseValidatorModel):
    Trail: Trail
    ResponseMetadata: ResponseMetadata


class Event(BaseValidatorModel):
    EventId: Optional[str] = None
    EventName: Optional[str] = None
    ReadOnly: Optional[str] = None
    AccessKeyId: Optional[str] = None
    EventTime: Optional[datetime] = None
    EventSource: Optional[str] = None
    Username: Optional[str] = None
    Resources: Optional[List[Resource]] = None
    CloudTrailEvent: Optional[str] = None


# This class is the output for the 'get_insight_selectors' function.
class GetInsightSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    InsightSelectors: List[InsightSelector]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_insight_selectors' function.
class PutInsightSelectorsRequest(BaseValidatorModel):
    InsightSelectors: List[InsightSelector]
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None
    InsightsDestination: Optional[str] = None


# This class is the output for the 'put_insight_selectors' function.
class PutInsightSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    InsightSelectors: List[InsightSelector]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_query_results' function.
class GetQueryResultsResponse(BaseValidatorModel):
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatistics
    QueryResultRows: List[List[Dict[str, str]]]
    ErrorMessage: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_import_failures' function.
class ListImportFailuresResponse(BaseValidatorModel):
    Failures: List[ImportFailureListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ImportSource(BaseValidatorModel):
    S3: S3ImportSource


# This class is the output for the 'list_imports' function.
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
    ResourceIdList: List[str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrailsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_insights_metric_data' function.
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


# This class is the input for the 'list_public_keys' function.
class ListPublicKeysRequest(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_queries' function.
class ListQueriesRequest(BaseValidatorModel):
    EventDataStore: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    QueryStatus: Optional[QueryStatusType] = None


# This class is the output for the 'list_public_keys' function.
class ListPublicKeysResponse(BaseValidatorModel):
    PublicKeyList: List[PublicKey]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_queries' function.
class ListQueriesResponse(BaseValidatorModel):
    Queries: List[Query]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_trails' function.
class ListTrailsResponse(BaseValidatorModel):
    Trails: List[TrailInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LookupEventsRequestPaginate(BaseValidatorModel):
    LookupAttributes: Optional[List[LookupAttribute]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventCategory: Optional[Literal['insight']] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'lookup_events' function.
class LookupEventsRequest(BaseValidatorModel):
    LookupAttributes: Optional[List[LookupAttribute]] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    EventCategory: Optional[Literal['insight']] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RefreshSchedule(BaseValidatorModel):
    Frequency: Optional[RefreshScheduleFrequency] = None
    Status: Optional[RefreshScheduleStatusType] = None
    TimeOfDay: Optional[str] = None


# This class is the output for the 'search_sample_queries' function.
class SearchSampleQueriesResponse(BaseValidatorModel):
    SearchResults: List[SearchSampleQueriesSearchResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags' function.
class ListTagsResponse(BaseValidatorModel):
    ResourceTagList: List[ResourceTag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_event_data_store' function.
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


# This class is the output for the 'get_event_data_store' function.
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


# This class is the output for the 'restore_event_data_store' function.
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


# This class is the output for the 'update_event_data_store' function.
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


class AdvancedEventSelector(BaseValidatorModel):
    FieldSelectors: List[AdvancedFieldSelectorUnion]
    Name: Optional[str] = None


# This class is the output for the 'get_event_selectors' function.
class GetEventSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutput]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_event_selectors' function.
class PutEventSelectorsResponse(BaseValidatorModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutput]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutput]
    ResponseMetadata: ResponseMetadata


class EventSelector(BaseValidatorModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[List[DataResourceUnion]] = None
    ExcludeManagementEventSources: Optional[List[str]] = None


# This class is the output for the 'lookup_events' function.
class LookupEventsResponse(BaseValidatorModel):
    Events: List[Event]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_import' function.
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


# This class is the input for the 'start_import' function.
class StartImportRequest(BaseValidatorModel):
    Destinations: Optional[List[str]] = None
    ImportSource: Optional[ImportSource] = None
    StartEventTime: Optional[Timestamp] = None
    EndEventTime: Optional[Timestamp] = None
    ImportId: Optional[str] = None


# This class is the output for the 'start_import' function.
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


# This class is the output for the 'stop_import' function.
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


# This class is the input for the 'create_dashboard' function.
class CreateDashboardRequest(BaseValidatorModel):
    Name: str
    RefreshSchedule: Optional[RefreshSchedule] = None
    TagsList: Optional[List[Tag]] = None
    TerminationProtectionEnabled: Optional[bool] = None
    Widgets: Optional[List[RequestWidget]] = None


# This class is the output for the 'create_dashboard' function.
class CreateDashboardResponse(BaseValidatorModel):
    DashboardArn: str
    Name: str
    Type: DashboardTypeType
    Widgets: List[Widget]
    TagsList: List[Tag]
    RefreshSchedule: RefreshSchedule
    TerminationProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_dashboard' function.
class GetDashboardResponse(BaseValidatorModel):
    DashboardArn: str
    Type: DashboardTypeType
    Status: DashboardStatusType
    Widgets: List[Widget]
    RefreshSchedule: RefreshSchedule
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    LastRefreshId: str
    LastRefreshFailureReason: str
    TerminationProtectionEnabled: bool
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_dashboard' function.
class UpdateDashboardRequest(BaseValidatorModel):
    DashboardId: str
    Widgets: Optional[List[RequestWidget]] = None
    RefreshSchedule: Optional[RefreshSchedule] = None
    TerminationProtectionEnabled: Optional[bool] = None


# This class is the output for the 'update_dashboard' function.
class UpdateDashboardResponse(BaseValidatorModel):
    DashboardArn: str
    Name: str
    Type: DashboardTypeType
    Widgets: List[Widget]
    RefreshSchedule: RefreshSchedule
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_event_data_stores' function.
class ListEventDataStoresResponse(BaseValidatorModel):
    EventDataStores: List[EventDataStore]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_channel' function.
class GetChannelResponse(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    SourceConfig: SourceConfig
    Destinations: List[Destination]
    IngestionStatus: IngestionStatus
    ResponseMetadata: ResponseMetadata

AdvancedEventSelectorUnion = Union[AdvancedEventSelector, AdvancedEventSelectorOutput]

EventSelectorUnion = Union[EventSelector, EventSelectorOutput]


# This class is the input for the 'create_event_data_store' function.
class CreateEventDataStoreRequest(BaseValidatorModel):
    Name: str
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorUnion]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    TerminationProtectionEnabled: Optional[bool] = None
    TagsList: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    StartIngestion: Optional[bool] = None
    BillingMode: Optional[BillingModeType] = None


# This class is the input for the 'update_event_data_store' function.
class UpdateEventDataStoreRequest(BaseValidatorModel):
    EventDataStore: str
    Name: Optional[str] = None
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorUnion]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    TerminationProtectionEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    BillingMode: Optional[BillingModeType] = None


# This class is the input for the 'put_event_selectors' function.
class PutEventSelectorsRequest(BaseValidatorModel):
    TrailName: str
    EventSelectors: Optional[List[EventSelectorUnion]] = None
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorUnion]] = None