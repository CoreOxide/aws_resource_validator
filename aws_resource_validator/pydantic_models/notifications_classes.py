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
from aws_resource_validator.pydantic_models.notifications_constants import *

class SummarizationDimensionDetailTypeDef(BaseValidatorModel):
    name: str
    value: str


class AggregationKeyTypeDef(BaseValidatorModel):
    name: str
    value: str


class SummarizationDimensionOverviewTypeDef(BaseValidatorModel):
    name: str
    count: int
    sampleValues: Optional[List[str]] = None


class AssociateChannelRequestTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str


class AssociateManagedNotificationAccountContactRequestTypeDef(BaseValidatorModel):
    contactIdentifier: AccountContactTypeType
    managedNotificationConfigurationArn: str


class AssociateManagedNotificationAdditionalChannelRequestTypeDef(BaseValidatorModel):
    channelArn: str
    managedNotificationConfigurationArn: str


class CreateEventRuleRequestTypeDef(BaseValidatorModel):
    notificationConfigurationArn: str
    source: str
    eventType: str
    regions: Sequence[str]
    eventPattern: Optional[str] = None


class EventRuleStatusSummaryTypeDef(BaseValidatorModel):
    status: EventRuleStatusType
    reason: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    name: str
    description: str
    aggregationDuration: Optional[AggregationDurationType] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteEventRuleRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class DeregisterNotificationHubRequestTypeDef(BaseValidatorModel):
    notificationHubRegion: str


class NotificationHubStatusSummaryTypeDef(BaseValidatorModel):
    status: NotificationHubStatusType
    reason: str


class DimensionTypeDef(BaseValidatorModel):
    name: str
    value: str


class DisassociateChannelRequestTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str


class DisassociateManagedNotificationAccountContactRequestTypeDef(BaseValidatorModel):
    contactIdentifier: AccountContactTypeType
    managedNotificationConfigurationArn: str


class DisassociateManagedNotificationAdditionalChannelRequestTypeDef(BaseValidatorModel):
    channelArn: str
    managedNotificationConfigurationArn: str


class GetEventRuleRequestTypeDef(BaseValidatorModel):
    arn: str


class GetManagedNotificationChildEventRequestTypeDef(BaseValidatorModel):
    arn: str
    locale: Optional[LocaleCodeType] = None


class GetManagedNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class GetManagedNotificationEventRequestTypeDef(BaseValidatorModel):
    arn: str
    locale: Optional[LocaleCodeType] = None


class GetNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class GetNotificationEventRequestTypeDef(BaseValidatorModel):
    arn: str
    locale: Optional[LocaleCodeType] = None


class NotificationsAccessForOrganizationTypeDef(BaseValidatorModel):
    accessStatus: AccessStatusType


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChannelsRequestTypeDef(BaseValidatorModel):
    notificationConfigurationArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEventRulesRequestTypeDef(BaseValidatorModel):
    notificationConfigurationArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListManagedNotificationChannelAssociationsRequestTypeDef(BaseValidatorModel):
    managedNotificationConfigurationArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedNotificationChannelAssociationSummaryTypeDef(BaseValidatorModel):
    channelIdentifier: str
    channelType: ChannelTypeType
    overrideOption: Optional[ChannelAssociationOverrideOptionType] = None


class ListManagedNotificationConfigurationsRequestTypeDef(BaseValidatorModel):
    channelIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedNotificationConfigurationStructureTypeDef(BaseValidatorModel):
    arn: str
    name: str
    description: str


class ListNotificationConfigurationsRequestTypeDef(BaseValidatorModel):
    eventRuleSource: Optional[str] = None
    channelArn: Optional[str] = None
    status: Optional[NotificationConfigurationStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NotificationConfigurationStructureTypeDef(BaseValidatorModel):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: Optional[AggregationDurationType] = None


class ListNotificationHubsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    arn: str


class ManagedSourceEventMetadataSummaryTypeDef(BaseValidatorModel):
    source: str
    eventType: str
    eventOriginRegion: Optional[str] = None


class MessageComponentsSummaryTypeDef(BaseValidatorModel):
    headline: str


class SourceEventMetadataSummaryTypeDef(BaseValidatorModel):
    source: str
    eventType: str
    eventOriginRegion: Optional[str] = None


class RegisterNotificationHubRequestTypeDef(BaseValidatorModel):
    notificationHubRegion: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    arn: str
    tagKeys: Sequence[str]


class UpdateEventRuleRequestTypeDef(BaseValidatorModel):
    arn: str
    eventPattern: Optional[str] = None
    regions: Optional[Sequence[str]] = None


class UpdateNotificationConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    aggregationDuration: Optional[AggregationDurationType] = None


class AggregationDetailTypeDef(BaseValidatorModel):
    summarizationDimensions: Optional[List[SummarizationDimensionDetailTypeDef]] = None


class AggregationSummaryTypeDef(BaseValidatorModel):
    eventCount: int
    aggregatedBy: List[AggregationKeyTypeDef]
    aggregatedAccounts: SummarizationDimensionOverviewTypeDef
    aggregatedRegions: SummarizationDimensionOverviewTypeDef
    aggregatedOrganizationalUnits: Optional[SummarizationDimensionOverviewTypeDef] = None
    additionalSummarizationDimensions: Optional[List[SummarizationDimensionOverviewTypeDef]] = None


class EventRuleStructureTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: List[str]
    managedRules: List[str]
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]


class CreateEventRuleResponseTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    status: NotificationConfigurationStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class GetEventRuleResponseTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: List[str]
    managedRules: List[str]
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetManagedNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    description: str
    category: str
    subCategory: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: AggregationDurationType
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelsResponseTypeDef(BaseValidatorModel):
    channels: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateEventRuleResponseTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: Dict[str, EventRuleStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateNotificationConfigurationResponseTypeDef(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterNotificationHubResponseTypeDef(BaseValidatorModel):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class NotificationHubOverviewTypeDef(BaseValidatorModel):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    creationTime: datetime
    lastActivationTime: Optional[datetime] = None


class RegisterNotificationHubResponseTypeDef(BaseValidatorModel):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummaryTypeDef
    creationTime: datetime
    lastActivationTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class MessageComponentsTypeDef(BaseValidatorModel):
    headline: Optional[str] = None
    paragraphSummary: Optional[str] = None
    completeDescription: Optional[str] = None
    dimensions: Optional[List[DimensionTypeDef]] = None


class GetNotificationsAccessForOrganizationResponseTypeDef(BaseValidatorModel):
    notificationsAccessForOrganization: NotificationsAccessForOrganizationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListChannelsRequestPaginateTypeDef(BaseValidatorModel):
    notificationConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEventRulesRequestPaginateTypeDef(BaseValidatorModel):
    notificationConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedNotificationChannelAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    managedNotificationConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedNotificationConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    channelIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNotificationConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    eventRuleSource: Optional[str] = None
    channelArn: Optional[str] = None
    status: Optional[NotificationConfigurationStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNotificationHubsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedNotificationChannelAssociationsResponseTypeDef(BaseValidatorModel):
    channelAssociations: List[ManagedNotificationChannelAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ListManagedNotificationChildEventsRequestPaginateTypeDef(BaseValidatorModel):
    aggregateManagedNotificationEventArn: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    locale: Optional[LocaleCodeType] = None
    relatedAccount: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedNotificationChildEventsRequestTypeDef(BaseValidatorModel):
    aggregateManagedNotificationEventArn: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    locale: Optional[LocaleCodeType] = None
    maxResults: Optional[int] = None
    relatedAccount: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    nextToken: Optional[str] = None


class ListManagedNotificationEventsRequestPaginateTypeDef(BaseValidatorModel):
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    relatedAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedNotificationEventsRequestTypeDef(BaseValidatorModel):
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    relatedAccount: Optional[str] = None


class ListNotificationEventsRequestPaginateTypeDef(BaseValidatorModel):
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    includeChildEvents: Optional[bool] = None
    aggregateNotificationEventArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListNotificationEventsRequestTypeDef(BaseValidatorModel):
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    includeChildEvents: Optional[bool] = None
    aggregateNotificationEventArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListManagedNotificationConfigurationsResponseTypeDef(BaseValidatorModel):
    managedNotificationConfigurations: List[ManagedNotificationConfigurationStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListNotificationConfigurationsResponseTypeDef(BaseValidatorModel):
    notificationConfigurations: List[NotificationConfigurationStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ManagedNotificationEventSummaryTypeDef(BaseValidatorModel):
    schemaVersion: Literal["v1.0"]
    sourceEventMetadata: ManagedSourceEventMetadataSummaryTypeDef
    messageComponents: MessageComponentsSummaryTypeDef
    eventStatus: EventStatusType
    notificationType: NotificationTypeType


class NotificationEventSummaryTypeDef(BaseValidatorModel):
    schemaVersion: Literal["v1.0"]
    sourceEventMetadata: SourceEventMetadataSummaryTypeDef
    messageComponents: MessageComponentsSummaryTypeDef
    eventStatus: EventStatusType
    notificationType: NotificationTypeType


class ResourceTypeDef(BaseValidatorModel):
    pass


class SourceEventMetadataTypeDef(BaseValidatorModel):
    eventTypeVersion: str
    sourceEventId: str
    relatedAccount: str
    source: str
    eventOccurrenceTime: datetime
    eventType: str
    relatedResources: List[ResourceTypeDef]
    eventOriginRegion: Optional[str] = None


class ManagedNotificationChildEventSummaryTypeDef(BaseValidatorModel):
    schemaVersion: Literal["v1.0"]
    sourceEventMetadata: ManagedSourceEventMetadataSummaryTypeDef
    messageComponents: MessageComponentsSummaryTypeDef
    aggregationDetail: AggregationDetailTypeDef
    eventStatus: EventStatusType
    notificationType: NotificationTypeType


class ListEventRulesResponseTypeDef(BaseValidatorModel):
    eventRules: List[EventRuleStructureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListNotificationHubsResponseTypeDef(BaseValidatorModel):
    notificationHubs: List[NotificationHubOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ManagedNotificationEventOverviewTypeDef(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    notificationEvent: ManagedNotificationEventSummaryTypeDef
    aggregationEventType: Optional[AggregationEventTypeType] = None
    organizationalUnitId: Optional[str] = None
    aggregationSummary: Optional[AggregationSummaryTypeDef] = None
    aggregatedNotificationRegions: Optional[List[str]] = None


class NotificationEventOverviewTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    notificationEvent: NotificationEventSummaryTypeDef
    aggregationEventType: Optional[AggregationEventTypeType] = None
    aggregateNotificationEventArn: Optional[str] = None
    aggregationSummary: Optional[AggregationSummaryTypeDef] = None


class ManagedNotificationChildEventOverviewTypeDef(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    childEvent: ManagedNotificationChildEventSummaryTypeDef
    aggregateManagedNotificationEventArn: str
    organizationalUnitId: Optional[str] = None


class ManagedNotificationChildEventTypeDef(BaseValidatorModel):
    pass


class GetManagedNotificationChildEventResponseTypeDef(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    creationTime: datetime
    content: ManagedNotificationChildEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ManagedNotificationEventTypeDef(BaseValidatorModel):
    pass


class GetManagedNotificationEventResponseTypeDef(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    creationTime: datetime
    content: ManagedNotificationEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListManagedNotificationEventsResponseTypeDef(BaseValidatorModel):
    managedNotificationEvents: List[ManagedNotificationEventOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListNotificationEventsResponseTypeDef(BaseValidatorModel):
    notificationEvents: List[NotificationEventOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NotificationEventTypeDef(BaseValidatorModel):
    pass


class GetNotificationEventResponseTypeDef(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    content: NotificationEventTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListManagedNotificationChildEventsResponseTypeDef(BaseValidatorModel):
    managedNotificationChildEvents: List[ManagedNotificationChildEventOverviewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


