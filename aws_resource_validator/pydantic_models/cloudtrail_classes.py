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
from aws_resource_validator.pydantic_models.cloudtrail_constants import *

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: Optional[str] = None

class AdvancedFieldSelectorOutputTypeDef(BaseValidatorModel):
    Field: str
    Equals: Optional[List[str]] = None
    StartsWith: Optional[List[str]] = None
    EndsWith: Optional[List[str]] = None
    NotEquals: Optional[List[str]] = None
    NotStartsWith: Optional[List[str]] = None
    NotEndsWith: Optional[List[str]] = None

class AdvancedFieldSelectorTypeDef(BaseValidatorModel):
    Field: str
    Equals: Optional[Sequence[str]] = None
    StartsWith: Optional[Sequence[str]] = None
    EndsWith: Optional[Sequence[str]] = None
    NotEquals: Optional[Sequence[str]] = None
    NotStartsWith: Optional[Sequence[str]] = None
    NotEndsWith: Optional[Sequence[str]] = None

class CancelQueryRequestRequestTypeDef(BaseValidatorModel):
    QueryId: str
    EventDataStore: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ChannelTypeDef(BaseValidatorModel):
    ChannelArn: Optional[str] = None
    Name: Optional[str] = None

class DestinationTypeDef(BaseValidatorModel):
    Type: DestinationTypeType
    Location: str

class DataResourceOutputTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Values: Optional[List[str]] = None

class DataResourceTypeDef(BaseValidatorModel):
    Type: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    Channel: str

class DeleteEventDataStoreRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class DeleteTrailRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeregisterOrganizationDelegatedAdminRequestRequestTypeDef(BaseValidatorModel):
    DelegatedAdminAccountId: str

class DescribeQueryRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: Optional[str] = None
    QueryId: Optional[str] = None
    QueryAlias: Optional[str] = None

class QueryStatisticsForDescribeQueryTypeDef(BaseValidatorModel):
    EventsMatched: Optional[int] = None
    EventsScanned: Optional[int] = None
    BytesScanned: Optional[int] = None
    ExecutionTimeInMillis: Optional[int] = None
    CreationTime: Optional[datetime] = None

class DescribeTrailsRequestRequestTypeDef(BaseValidatorModel):
    trailNameList: Optional[Sequence[str]] = None
    includeShadowTrails: Optional[bool] = None

class TrailTypeDef(BaseValidatorModel):
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

class DisableFederationRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str

class EnableFederationRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str
    FederationRoleArn: str

class ResourceTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    ResourceName: Optional[str] = None

class GetChannelRequestRequestTypeDef(BaseValidatorModel):
    Channel: str

class IngestionStatusTypeDef(BaseValidatorModel):
    LatestIngestionSuccessTime: Optional[datetime] = None
    LatestIngestionSuccessEventID: Optional[str] = None
    LatestIngestionErrorCode: Optional[str] = None
    LatestIngestionAttemptTime: Optional[datetime] = None
    LatestIngestionAttemptEventID: Optional[str] = None

class GetEventDataStoreRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str

class PartitionKeyTypeDef(BaseValidatorModel):
    Name: str
    Type: str

class GetEventSelectorsRequestRequestTypeDef(BaseValidatorModel):
    TrailName: str

class GetImportRequestRequestTypeDef(BaseValidatorModel):
    ImportId: str

class ImportStatisticsTypeDef(BaseValidatorModel):
    PrefixesFound: Optional[int] = None
    PrefixesCompleted: Optional[int] = None
    FilesCompleted: Optional[int] = None
    EventsCompleted: Optional[int] = None
    FailedEntries: Optional[int] = None

class GetInsightSelectorsRequestRequestTypeDef(BaseValidatorModel):
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None

class InsightSelectorTypeDef(BaseValidatorModel):
    InsightType: Optional[InsightTypeType] = None

class GetQueryResultsRequestRequestTypeDef(BaseValidatorModel):
    QueryId: str
    EventDataStore: Optional[str] = None
    NextToken: Optional[str] = None
    MaxQueryResults: Optional[int] = None

class QueryStatisticsTypeDef(BaseValidatorModel):
    ResultsCount: Optional[int] = None
    TotalResultsCount: Optional[int] = None
    BytesScanned: Optional[int] = None

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GetTrailRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetTrailStatusRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class ImportFailureListItemTypeDef(BaseValidatorModel):
    Location: Optional[str] = None
    Status: Optional[ImportFailureStatusType] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LastUpdatedTime: Optional[datetime] = None

class S3ImportSourceTypeDef(BaseValidatorModel):
    S3LocationUri: str
    S3BucketRegion: str
    S3BucketAccessRoleArn: str

class ImportsListItemTypeDef(BaseValidatorModel):
    ImportId: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    Destinations: Optional[List[str]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEventDataStoresRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListImportFailuresRequestRequestTypeDef(BaseValidatorModel):
    ImportId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListImportsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    Destination: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    NextToken: Optional[str] = None

class PublicKeyTypeDef(BaseValidatorModel):
    Value: Optional[bytes] = None
    ValidityStartTime: Optional[datetime] = None
    ValidityEndTime: Optional[datetime] = None
    Fingerprint: Optional[str] = None

class QueryTypeDef(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStatus: Optional[QueryStatusType] = None
    CreationTime: Optional[datetime] = None

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceIdList: Sequence[str]
    NextToken: Optional[str] = None

class ListTrailsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None

class TrailInfoTypeDef(BaseValidatorModel):
    TrailARN: Optional[str] = None
    Name: Optional[str] = None
    HomeRegion: Optional[str] = None

class LookupAttributeTypeDef(BaseValidatorModel):
    AttributeKey: LookupAttributeKeyType
    AttributeValue: str

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str

class RegisterOrganizationDelegatedAdminRequestRequestTypeDef(BaseValidatorModel):
    MemberAccountId: str

class RestoreEventDataStoreRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str

class StartEventDataStoreIngestionRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str

class StartLoggingRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StartQueryRequestRequestTypeDef(BaseValidatorModel):
    QueryStatement: Optional[str] = None
    DeliveryS3Uri: Optional[str] = None
    QueryAlias: Optional[str] = None
    QueryParameters: Optional[Sequence[str]] = None

class StopEventDataStoreIngestionRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str

class StopImportRequestRequestTypeDef(BaseValidatorModel):
    ImportId: str

class StopLoggingRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class UpdateTrailRequestRequestTypeDef(BaseValidatorModel):
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

class AddTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagsList: Sequence[TagTypeDef]

class CreateTrailRequestRequestTypeDef(BaseValidatorModel):
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

class RemoveTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceId: str
    TagsList: Sequence[TagTypeDef]

class ResourceTagTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    TagsList: Optional[List[TagTypeDef]] = None

class AdvancedEventSelectorOutputTypeDef(BaseValidatorModel):
    FieldSelectors: List[AdvancedFieldSelectorOutputTypeDef]
    Name: Optional[str] = None

class AdvancedEventSelectorTypeDef(BaseValidatorModel):
    FieldSelectors: Sequence[AdvancedFieldSelectorTypeDef]
    Name: Optional[str] = None

class CancelQueryResponseTypeDef(BaseValidatorModel):
    QueryId: str
    QueryStatus: QueryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrailResponseTypeDef(BaseValidatorModel):
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

class DisableFederationResponseTypeDef(BaseValidatorModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class EnableFederationResponseTypeDef(BaseValidatorModel):
    EventDataStoreArn: str
    FederationStatus: FederationStatusType
    FederationRoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrailStatusResponseTypeDef(BaseValidatorModel):
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

class ListInsightsMetricDataResponseTypeDef(BaseValidatorModel):
    EventSource: str
    EventName: str
    InsightType: InsightTypeType
    ErrorCode: str
    Timestamps: List[datetime]
    Values: List[float]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourcePolicy: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartQueryResponseTypeDef(BaseValidatorModel):
    QueryId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrailResponseTypeDef(BaseValidatorModel):
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

class ListChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Source: str
    Destinations: Sequence[DestinationTypeDef]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateChannelResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[DestinationTypeDef]
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    Channel: str
    Destinations: Optional[Sequence[DestinationTypeDef]] = None
    Name: Optional[str] = None

class UpdateChannelResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    Destinations: List[DestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventSelectorOutputTypeDef(BaseValidatorModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[List[DataResourceOutputTypeDef]] = None
    ExcludeManagementEventSources: Optional[List[str]] = None

class EventSelectorTypeDef(BaseValidatorModel):
    ReadWriteType: Optional[ReadWriteTypeType] = None
    IncludeManagementEvents: Optional[bool] = None
    DataResources: Optional[Sequence[DataResourceTypeDef]] = None
    ExcludeManagementEventSources: Optional[Sequence[str]] = None

class DescribeQueryResponseTypeDef(BaseValidatorModel):
    QueryId: str
    QueryString: str
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatisticsForDescribeQueryTypeDef
    ErrorMessage: str
    DeliveryS3Uri: str
    DeliveryStatus: DeliveryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrailsResponseTypeDef(BaseValidatorModel):
    trailList: List[TrailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTrailResponseTypeDef(BaseValidatorModel):
    Trail: TrailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseValidatorModel):
    EventId: Optional[str] = None
    EventName: Optional[str] = None
    ReadOnly: Optional[str] = None
    AccessKeyId: Optional[str] = None
    EventTime: Optional[datetime] = None
    EventSource: Optional[str] = None
    Username: Optional[str] = None
    Resources: Optional[List[ResourceTypeDef]] = None
    CloudTrailEvent: Optional[str] = None

class GetInsightSelectorsResponseTypeDef(BaseValidatorModel):
    TrailARN: str
    InsightSelectors: List[InsightSelectorTypeDef]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutInsightSelectorsRequestRequestTypeDef(BaseValidatorModel):
    InsightSelectors: Sequence[InsightSelectorTypeDef]
    TrailName: Optional[str] = None
    EventDataStore: Optional[str] = None
    InsightsDestination: Optional[str] = None

class PutInsightSelectorsResponseTypeDef(BaseValidatorModel):
    TrailARN: str
    InsightSelectors: List[InsightSelectorTypeDef]
    EventDataStoreArn: str
    InsightsDestination: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetQueryResultsResponseTypeDef(BaseValidatorModel):
    QueryStatus: QueryStatusType
    QueryStatistics: QueryStatisticsTypeDef
    QueryResultRows: List[List[Dict[str, str]]]
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListImportFailuresResponseTypeDef(BaseValidatorModel):
    Failures: List[ImportFailureListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ImportSourceTypeDef(BaseValidatorModel):
    S3: S3ImportSourceTypeDef

class ListImportsResponseTypeDef(BaseValidatorModel):
    Imports: List[ImportsListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListImportFailuresRequestListImportFailuresPaginateTypeDef(BaseValidatorModel):
    ImportId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportsRequestListImportsPaginateTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseValidatorModel):
    ResourceIdList: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrailsRequestListTrailsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInsightsMetricDataRequestRequestTypeDef(BaseValidatorModel):
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

class ListPublicKeysRequestListPublicKeysPaginateTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPublicKeysRequestRequestTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    NextToken: Optional[str] = None

class ListQueriesRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    QueryStatus: Optional[QueryStatusType] = None

class ListPublicKeysResponseTypeDef(BaseValidatorModel):
    PublicKeyList: List[PublicKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueriesResponseTypeDef(BaseValidatorModel):
    Queries: List[QueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrailsResponseTypeDef(BaseValidatorModel):
    Trails: List[TrailInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LookupEventsRequestLookupEventsPaginateTypeDef(BaseValidatorModel):
    LookupAttributes: Optional[Sequence[LookupAttributeTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventCategory: Optional[Literal["insight"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class LookupEventsRequestRequestTypeDef(BaseValidatorModel):
    LookupAttributes: Optional[Sequence[LookupAttributeTypeDef]] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    EventCategory: Optional[Literal["insight"]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsResponseTypeDef(BaseValidatorModel):
    ResourceTagList: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateEventDataStoreResponseTypeDef(BaseValidatorModel):
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

class EventDataStoreTypeDef(BaseValidatorModel):
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

class GetEventDataStoreResponseTypeDef(BaseValidatorModel):
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

class RestoreEventDataStoreResponseTypeDef(BaseValidatorModel):
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

class SourceConfigTypeDef(BaseValidatorModel):
    ApplyToAllRegions: Optional[bool] = None
    AdvancedEventSelectors: Optional[List[AdvancedEventSelectorOutputTypeDef]] = None

class UpdateEventDataStoreResponseTypeDef(BaseValidatorModel):
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

class GetEventSelectorsResponseTypeDef(BaseValidatorModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutputTypeDef]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventSelectorsResponseTypeDef(BaseValidatorModel):
    TrailARN: str
    EventSelectors: List[EventSelectorOutputTypeDef]
    AdvancedEventSelectors: List[AdvancedEventSelectorOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LookupEventsResponseTypeDef(BaseValidatorModel):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetImportResponseTypeDef(BaseValidatorModel):
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

class StartImportRequestRequestTypeDef(BaseValidatorModel):
    Destinations: Optional[Sequence[str]] = None
    ImportSource: Optional[ImportSourceTypeDef] = None
    StartEventTime: Optional[TimestampTypeDef] = None
    EndEventTime: Optional[TimestampTypeDef] = None
    ImportId: Optional[str] = None

class StartImportResponseTypeDef(BaseValidatorModel):
    ImportId: str
    Destinations: List[str]
    ImportSource: ImportSourceTypeDef
    StartEventTime: datetime
    EndEventTime: datetime
    ImportStatus: ImportStatusType
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StopImportResponseTypeDef(BaseValidatorModel):
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

class ListEventDataStoresResponseTypeDef(BaseValidatorModel):
    EventDataStores: List[EventDataStoreTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetChannelResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Source: str
    SourceConfig: SourceConfigTypeDef
    Destinations: List[DestinationTypeDef]
    IngestionStatus: IngestionStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventDataStoreRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateEventDataStoreRequestRequestTypeDef(BaseValidatorModel):
    EventDataStore: str
    Name: Optional[str] = None
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnionTypeDef]] = None
    MultiRegionEnabled: Optional[bool] = None
    OrganizationEnabled: Optional[bool] = None
    RetentionPeriod: Optional[int] = None
    TerminationProtectionEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    BillingMode: Optional[BillingModeType] = None

class PutEventSelectorsRequestRequestTypeDef(BaseValidatorModel):
    TrailName: str
    EventSelectors: Optional[Sequence[EventSelectorUnionTypeDef]] = None
    AdvancedEventSelectors: Optional[Sequence[AdvancedEventSelectorUnionTypeDef]] = None

