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
from aws_resource_validator.pydantic_models.cloudtrail_constants import *

class TagTypeDef(BaseModel):
    Key: str
    Value: Optional[str] = None

class AdvancedFieldSelectorOutputTypeDef(BaseModel):
    Field: str
    Equals: Optional[List[str]] = None
    StartsWith: Optional[List[str]] = None
    EndsWith: Optional[List[str]] = None
    NotEquals: Optional[List[str]] = None
    NotStartsWith: Optional[List[str]] = None
    NotEndsWith: Optional[List[str]] = None

class AdvancedFieldSelectorTypeDef(BaseModel):
    Field: str
    Equals: Optional[Sequence[str]] = None
    StartsWith: Optional[Sequence[str]] = None
    EndsWith: Optional[Sequence[str]] = None
    NotEquals: Optional[Sequence[str]] = None
    NotStartsWith: Optional[Sequence[str]] = None
    NotEndsWith: Optional[Sequence[str]] = None

class CancelQueryRequestRequestTypeDef(BaseModel):
    QueryId: str
    EventDataStore: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ChannelTypeDef(BaseModel):
    ChannelArn: Optional[str] = None
    Name: Optional[str] = None

class DestinationTypeDef(BaseModel):
    Type: DestinationTypeType
    Location: str

class DataResourceOutputTypeDef(BaseModel):
    Type: Optional[str] = None
    Values: Optional[List[str]] = None

class DataResourceTypeDef(BaseModel):
    Type: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DeleteChannelRequestRequestTypeDef(BaseModel):
    Channel: str

class DeleteEventDataStoreRequestRequestTypeDef(BaseModel):
    EventDataStore: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class DeleteTrailRequestRequestTypeDef(BaseModel):
    Name: str

class DeregisterOrganizationDelegatedAdminRequestRequestTypeDef(BaseModel):
    DelegatedAdminAccountId: str

class DescribeQueryRequestRequestTypeDef(BaseModel):
    EventDataStore: Optional[str] = None
    QueryId: Optional[str] = None
    QueryAlias: Optional[str] = None

class QueryStatisticsForDescribeQueryTypeDef(BaseModel):
    EventsMatched: Optional[int] = None
    EventsScanned: Optional[int] = None
    BytesScanned: Optional[int] = None
    ExecutionTimeInMillis: Optional[int] = None
    CreationTime: Optional[datetime] = None

class DescribeTrailsRequestRequestTypeDef(BaseModel):
    trailNameList: Optional[Sequence[str]] = None
    includeShadowTrails: Optional[bool] = None

class TrailTypeDef(BaseModel):
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

class DisableFederationRequestRequestTypeDef(BaseModel):
    EventDataStore: str

class EnableFederationRequestRequestTypeDef(BaseModel):
    EventDataStore: str
    FederationRoleArn: str

class ResourceTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    ResourceName: Optional[str] = None

class GetChannelRequestRequestTypeDef(BaseModel):
    Channel: str

class IngestionStatusTypeDef(BaseModel):
    LatestIngestionSuccessTime: Optional[datetime] = None
    LatestIngestionSuccessEventID: Optional[str] = None
    LatestIngestionErrorCode: Optional[str] = None
    LatestIngestionAttemptTime: Optional[datetime] = None
    LatestIngestionAttemptEventID: Optional[str] = None

class GetEventDataStoreRequestRequestTypeDef(BaseModel):
    EventDataStore: str

class PartitionKeyTypeDef(BaseModel):
    Name: str
    Type: str

class GetEventSelectorsRequestRequestTypeDef(BaseModel):
    TrailName: str

class GetImportRequestRequestTypeDef(BaseModel):
    ImportId: str

class ImportStatisticsTypeDef(BaseModel):
    PrefixesFound: Optional[int] = None
    PrefixesCompleted: Optional[int] = None
    FilesCompleted: Optional[int] = None
    EventsCompleted: Optional[int] = None
    FailedEntries: Optional[int] = None

class GetInsightSelectorsRequestRequestTypeDef(BaseModel):
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None

class InsightSelectorTypeDef(BaseModel):
    InsightType: Optional[InsightTypeType] = None

class GetQueryResultsRequestRequestTypeDef(BaseModel):
    QueryId: str
    EventDataStore: Optional[str] = None
    NextToken: Optional[str] = None
    MaxQueryResults: Optional[int] = None

class QueryStatisticsTypeDef(BaseModel):
    ResultsCount: Optional[int] = None
    TotalResultsCount: Optional[int] = None
    BytesScanned: Optional[int] = None

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetTrailRequestRequestTypeDef(BaseModel):
    Name: str

class GetTrailStatusRequestRequestTypeDef(BaseModel):
    Name: str

class ImportFailureListItemTypeDef(BaseModel):
    Location: Optional[str] = None
    Status: Optional[ImportFailureStatusType] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None

class S3ImportSourceTypeDef(BaseModel):
    S3LocationUri: str
    S3BucketRegion: str
    S3BucketAccessRoleArn: str

class ImportsListItemTypeDef(BaseModel):
    ImportId: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    Destinations: Optional[List[str]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEventDataStoresRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListImportFailuresRequestRequestTypeDef(BaseModel):
    ImportId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListImportsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    Destination: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    NextToken: Optional[str] = None

class PublicKeyTypeDef(BaseModel):
    Value: Optional[bytes] = None
    ValidityStartTime: Optional[datetime] = None
    ValidityEndTime: Optional[datetime] = None
    Fingerprint: Optional[str] = None

class QueryTypeDef(BaseModel):
    QueryId: Optional[str] = None
    QueryStatus: Optional[QueryStatusType] = None
    CreationTime: Optional[datetime] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    ResourceIdList: Sequence[str]
    NextToken: Optional[str] = None

class ListTrailsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None

class TrailInfoTypeDef(BaseModel):
    TrailARN: Optional[str] = None
    Name: Optional[str] = None
    HomeRegion: Optional[str] = None

class LookupAttributeTypeDef(BaseModel):
    AttributeKey: LookupAttributeKeyType
    AttributeValue: str

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ResourcePolicy: str

class RegisterOrganizationDelegatedAdminRequestRequestTypeDef(BaseModel):
    MemberAccountId: str

class RestoreEventDataStoreRequestRequestTypeDef(BaseModel):
    EventDataStore: str

class StartEventDataStoreIngestionRequestRequestTypeDef(BaseModel):
    EventDataStore: str

class StartLoggingRequestRequestTypeDef(BaseModel):
    Name: str

class StartQueryRequestRequestTypeDef(BaseModel):
    QueryStatement: Optional[str] = None
    DeliveryS3Uri: Optional[str] = None
    QueryAlias: Optional[str] = None
    QueryParameters: Optional[Sequence[str]] = None

class StopEventDataStoreIngestionRequestRequestTypeDef(BaseModel):
    EventDataStore: str

class StopImportRequestRequestTypeDef(BaseModel):
    ImportId: str

class StopLoggingRequestRequestTypeDef(BaseModel):
    Name: str

class UpdateTrailRequestRequestTypeDef(BaseModel):
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

class AddTagsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagsList: Sequence[TagTypeDef]

class CreateTrailRequestRequestTypeDef(BaseModel):
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
    TagsList: Optional[Sequence[TagTypeDef]] = None

class RemoveTagsRequestRequestTypeDef(BaseModel):
    ResourceId: str
    TagsList: Sequence[TagTypeDef]

class ResourceTagTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    TagsList: Optional[List[TagTypeDef]] = None

class AdvancedEventSelectorOutputTypeDef(BaseModel):
    FieldSelectors: List[AdvancedFieldSelectorOutputTypeDef]
    Name: Optional[str] = None

class AdvancedEventSelectorTypeDef(BaseModel):
    FieldSelectors: Sequence[AdvancedFieldSelectorTypeDef]
    Name: Optional[str] = None

class CancelQueryResponseTypeDef(BaseModel):
    QueryId: str
    QueryStatus: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrailResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class DisableFederationResponseTypeDef(BaseModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableFederationResponseTypeDef(BaseModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    ResourceArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrailStatusResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListInsightsMetricDataResponseTypeDef(BaseModel):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: str
    Timestamps: List[datetime]
    Values: List[float]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutResourcePolicyResponseTypeDef(BaseModel):
    ResourceArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryResponseTypeDef(BaseModel):
    QueryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrailResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsResponseTypeDef(BaseModel):
    Channels: List[ChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateChannelRequestRequestTypeDef(BaseModel):
    Name: str
    Source: str
    Destinations: Sequence[DestinationTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateChannelResponseTypeDef(BaseModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[DestinationTypeDef]
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelRequestRequestTypeDef(BaseModel):
    Channel: str
    Destinations: Optional[Sequence[DestinationTypeDef]] = None
    Name: Optional[str] = None

class UpdateChannelResponseTypeDef(BaseModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventSelectorOutputTypeDef(BaseModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[List[DataResourceOutputTypeDef]] = None
    ExcludeManagementEventSources: Optional[List[str]] = None

class EventSelectorTypeDef(BaseModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[Sequence[DataResourceTypeDef]] = None
    ExcludeManagementEventSources: Optional[Sequence[str]] = None

class DescribeQueryResponseTypeDef(BaseModel):
    QueryId: str
    QueryString: str
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatisticsForDescribeQueryTypeDef
    ErrorMessage: str
    DeliveryS3Uri: str
    DeliveryStatus: DeliveryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrailsResponseTypeDef(BaseModel):
    trailList: List[TrailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrailResponseTypeDef(BaseModel):
    Trail: TrailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseModel):
    EventId: Optional[str] = None
    EventName: Optional[str] = None
    ReadOnly: Optional[str] = None
    AccessKeyId: Optional[str] = None
    EventTime: Optional[datetime] = None
    EventSource: Optional[str] = None
    Username: Optional[str] = None
    Resources: Optional[List[ResourceTypeDef]] = None
    CloudTrailEvent: Optional[str] = None

class GetInsightSelectorsResponseTypeDef(BaseModel):
    TrailARN: str
    InsightSelectors: List[InsightSelectorTypeDef]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutInsightSelectorsRequestRequestTypeDef(BaseModel):
    InsightSelectors: Sequence[InsightSelectorTypeDef]
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None
    InsightsDestination: Optional[str] = None

class PutInsightSelectorsResponseTypeDef(BaseModel):
    TrailARN: str
    InsightSelectors: List[InsightSelectorTypeDef]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryResultsResponseTypeDef(BaseModel):
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatisticsTypeDef
    QueryResultRows: List[List[Dict[str, str]]]
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListImportFailuresResponseTypeDef(BaseModel):
    Failures: List[ImportFailureListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportSourceTypeDef(BaseModel):
    S3: S3ImportSourceTypeDef

class ListImportsResponseTypeDef(BaseModel):
    Imports: List[ImportsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListImportFailuresRequestListImportFailuresPaginateTypeDef(BaseModel):
    ImportId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportsRequestListImportsPaginateTypeDef(BaseModel):
    Destination: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseModel):
    ResourceIdList: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrailsRequestListTrailsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsMetricDataRequestRequestTypeDef(BaseModel):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: Optional[str] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Period: Optional[int] = None
    DataType: Optional[InsightsMetricDataTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListPublicKeysRequestListPublicKeysPaginateTypeDef(BaseModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPublicKeysRequestRequestTypeDef(BaseModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None

class ListQueriesRequestRequestTypeDef(BaseModel):
    EventDataStore: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    QueryStatus: Optional[QueryStatusType] = None

class ListPublicKeysResponseTypeDef(BaseModel):
    PublicKeyList: List[PublicKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueriesResponseTypeDef(BaseModel):
    Queries: List[QueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrailsResponseTypeDef(BaseModel):
    Trails: List[TrailInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LookupEventsRequestLookupEventsPaginateTypeDef(BaseModel):
    LookupAttributes: Optional[Sequence[LookupAttributeTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventCategory: Optional[Literal["insight"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LookupEventsRequestRequestTypeDef(BaseModel):
    LookupAttributes: Optional[Sequence[LookupAttributeTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventCategory: Optional[Literal["insight"]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsResponseTypeDef(BaseModel):
    ResourceTagList: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateEventDataStoreResponseTypeDef(BaseModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    TagsList: List[TagTypeDef]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    ResponseMetadata: ResponseMetadataTypeDef

class EventDataStoreTypeDef(BaseModel):
    EventDataStoreArn: Optional[str] = None
    Name: Optional[str] = None
    TerminationProtectionEnabled: Optional[bool] = None
    Status: Optional[EventDataStoreStatusType] = None
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorOutputTypeDef]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class GetEventDataStoreResponseTypeDef(BaseModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
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
    PartitionKeys: List[PartitionKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreEventDataStoreResponseTypeDef(BaseModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    MultiRegionEnabled: bool
    OrganizationEnabled: bool
    RetentionPeriod: int
    TerminationProtectionEnabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    KmsKeyId: str
    BillingMode: BillingModeType
    ResponseMetadata: ResponseMetadataTypeDef

class SourceConfigTypeDef(BaseModel):
    ApplyToAllRegions: Optional[bool] = None
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorOutputTypeDef]] = None

class UpdateEventDataStoreResponseTypeDef(BaseModel):
    EventDataStoreArn: str
    Name: str
    Status: EventDataStoreStatusType
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetEventSelectorsResponseTypeDef(BaseModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutputTypeDef]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventSelectorsResponseTypeDef(BaseModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutputTypeDef]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LookupEventsResponseTypeDef(BaseModel):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetImportResponseTypeDef(BaseModel):
    ImportId: str
    Destinations: List[str]
    ImportSource: ImportSourceTypeDef
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ImportStatistics: ImportStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportRequestRequestTypeDef(BaseModel):
    Destinations: Optional[Sequence[str]] = None
    ImportSource: Optional[ImportSourceTypeDef] = None
    StartEventTime: Optional[TimestampTypeDef] = None
    EndEventTime: Optional[TimestampTypeDef] = None
    ImportId: Optional[str] = None

class StartImportResponseTypeDef(BaseModel):
    ImportId: str
    Destinations: List[str]
    ImportSource: ImportSourceTypeDef
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopImportResponseTypeDef(BaseModel):
    ImportId: str
    ImportSource: ImportSourceTypeDef
    Destinations: List[str]
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatistics: ImportStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventDataStoresResponseTypeDef(BaseModel):
    EventDataStores: List[EventDataStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetChannelResponseTypeDef(BaseModel):
    ChannelArn: str
    Name: str
    Source: str
    SourceConfig: SourceConfigTypeDef
    Destinations: List[DestinationTypeDef]
    IngestionStatus: IngestionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventDataStoreRequestRequestTypeDef(BaseModel):
    Name: str
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnionTypeDef]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    TerminationProtectionEnabled: Optional[bool] = None
    TagsList: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    StartIngestion: Optional[bool] = None
    BillingMode: Optional[BillingModeType] = None

class UpdateEventDataStoreRequestRequestTypeDef(BaseModel):
    EventDataStore: str
    Name: Optional[str] = None
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnionTypeDef]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    TerminationProtectionEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    BillingMode: Optional[BillingModeType] = None

class PutEventSelectorsRequestRequestTypeDef(BaseModel):
    TrailName: str
    EventSelectors: Optional[Sequence[EventSelectorUnionTypeDef]] = None
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnionTypeDef]] = None

