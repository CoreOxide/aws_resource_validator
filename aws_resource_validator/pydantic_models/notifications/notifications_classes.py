from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.notifications.notifications_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class SummarizationDimensionDetail(BaseValidatorModel):
    name: str
    value: str


class AggregationKey(BaseValidatorModel):
    name: str
    value: str


class SummarizationDimensionOverview(BaseValidatorModel):
    name: str
    count: int
    sampleValues: Optional[List[str]] = None


class AssociateChannelRequest(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str


class AssociateManagedNotificationAccountContactRequest(BaseValidatorModel):
    contactIdentifier: AccountContactTypeType
    managedNotificationConfigurationArn: str


class AssociateManagedNotificationAdditionalChannelRequest(BaseValidatorModel):
    channelArn: str
    managedNotificationConfigurationArn: str


# This class is the input for the 'create_event_rule' function.
class CreateEventRuleRequest(BaseValidatorModel):
    notificationConfigurationArn: str
    source: str
    eventType: str
    regions: List[str]
    eventPattern: Optional[str] = None


class EventRuleStatusSummary(BaseValidatorModel):
    status: EventRuleStatusType
    reason: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'create_notification_configuration' function.
class CreateNotificationConfigurationRequest(BaseValidatorModel):
    name: str
    description: str
    aggregationDuration: Optional[AggregationDurationType] = None
    tags: Optional[Dict[str, str]] = None


class DeleteEventRuleRequest(BaseValidatorModel):
    arn: str


class DeleteNotificationConfigurationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'deregister_notification_hub' function.
class DeregisterNotificationHubRequest(BaseValidatorModel):
    notificationHubRegion: str


class NotificationHubStatusSummary(BaseValidatorModel):
    status: NotificationHubStatusType
    reason: str


class Dimension(BaseValidatorModel):
    name: str
    value: str


class DisassociateChannelRequest(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str


class DisassociateManagedNotificationAccountContactRequest(BaseValidatorModel):
    contactIdentifier: AccountContactTypeType
    managedNotificationConfigurationArn: str


class DisassociateManagedNotificationAdditionalChannelRequest(BaseValidatorModel):
    channelArn: str
    managedNotificationConfigurationArn: str


# This class is the input for the 'get_event_rule' function.
class GetEventRuleRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_managed_notification_child_event' function.
class GetManagedNotificationChildEventRequest(BaseValidatorModel):
    arn: str
    locale: Optional[LocaleCodeType] = None


# This class is the input for the 'get_managed_notification_configuration' function.
class GetManagedNotificationConfigurationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_managed_notification_event' function.
class GetManagedNotificationEventRequest(BaseValidatorModel):
    arn: str
    locale: Optional[LocaleCodeType] = None


# This class is the input for the 'get_notification_configuration' function.
class GetNotificationConfigurationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_notification_event' function.
class GetNotificationEventRequest(BaseValidatorModel):
    arn: str
    locale: Optional[LocaleCodeType] = None


class NotificationsAccessForOrganization(BaseValidatorModel):
    accessStatus: AccessStatusType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_channels' function.
class ListChannelsRequest(BaseValidatorModel):
    notificationConfigurationArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_event_rules' function.
class ListEventRulesRequest(BaseValidatorModel):
    notificationConfigurationArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_managed_notification_channel_associations' function.
class ListManagedNotificationChannelAssociationsRequest(BaseValidatorModel):
    managedNotificationConfigurationArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedNotificationChannelAssociationSummary(BaseValidatorModel):
    channelIdentifier: str
    channelType: ChannelTypeType
    overrideOption: Optional[ChannelAssociationOverrideOptionType] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'list_managed_notification_configurations' function.
class ListManagedNotificationConfigurationsRequest(BaseValidatorModel):
    channelIdentifier: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ManagedNotificationConfigurationStructure(BaseValidatorModel):
    arn: str
    name: str
    description: str


# This class is the input for the 'list_notification_configurations' function.
class ListNotificationConfigurationsRequest(BaseValidatorModel):
    eventRuleSource: Optional[str] = None
    channelArn: Optional[str] = None
    status: Optional[NotificationConfigurationStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class NotificationConfigurationStructure(BaseValidatorModel):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: Optional[AggregationDurationType] = None


# This class is the input for the 'list_notification_hubs' function.
class ListNotificationHubsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    arn: str


class ManagedSourceEventMetadataSummary(BaseValidatorModel):
    source: str
    eventType: str
    eventOriginRegion: Optional[str] = None


class MessageComponentsSummary(BaseValidatorModel):
    headline: str


class TextPartValue(BaseValidatorModel):
    type: TextPartTypeType
    displayText: Optional[str] = None
    textByLocale: Optional[Dict[LocaleCodeType, str]] = None
    url: Optional[str] = None


class MediaElement(BaseValidatorModel):
    mediaId: str
    type: Literal['IMAGE']
    url: str
    caption: str


class SourceEventMetadataSummary(BaseValidatorModel):
    source: str
    eventType: str
    eventOriginRegion: Optional[str] = None


# This class is the input for the 'register_notification_hub' function.
class RegisterNotificationHubRequest(BaseValidatorModel):
    notificationHubRegion: str


class Resource(BaseValidatorModel):
    id: Optional[str] = None
    arn: Optional[str] = None
    detailUrl: Optional[str] = None
    tags: Optional[List[str]] = None


class TagResourceRequest(BaseValidatorModel):
    arn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    arn: str
    tagKeys: List[str]


# This class is the input for the 'update_event_rule' function.
class UpdateEventRuleRequest(BaseValidatorModel):
    arn: str
    eventPattern: Optional[str] = None
    regions: Optional[List[str]] = None


# This class is the input for the 'update_notification_configuration' function.
class UpdateNotificationConfigurationRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    description: Optional[str] = None
    aggregationDuration: Optional[AggregationDurationType] = None


class AggregationDetail(BaseValidatorModel):
    summarizationDimensions: Optional[List[SummarizationDimensionDetail]] = None


class AggregationSummary(BaseValidatorModel):
    eventCount: int
    aggregatedBy: List[AggregationKey]
    aggregatedAccounts: SummarizationDimensionOverview
    aggregatedRegions: SummarizationDimensionOverview
    aggregatedOrganizationalUnits: Optional[SummarizationDimensionOverview] = None
    additionalSummarizationDimensions: Optional[List[SummarizationDimensionOverview]] = None


class EventRuleStructure(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: List[str]
    managedRules: List[str]
    statusSummaryByRegion: Dict[str, EventRuleStatusSummary]


# This class is the output for the 'create_event_rule' function.
class CreateEventRuleResponse(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: Dict[str, EventRuleStatusSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_notification_configuration' function.
class CreateNotificationConfigurationResponse(BaseValidatorModel):
    arn: str
    status: NotificationConfigurationStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_event_rule' function.
class GetEventRuleResponse(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    source: str
    eventType: str
    eventPattern: str
    regions: List[str]
    managedRules: List[str]
    statusSummaryByRegion: Dict[str, EventRuleStatusSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_managed_notification_configuration' function.
class GetManagedNotificationConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    description: str
    category: str
    subCategory: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_notification_configuration' function.
class GetNotificationConfigurationResponse(BaseValidatorModel):
    arn: str
    name: str
    description: str
    status: NotificationConfigurationStatusType
    creationTime: datetime
    aggregationDuration: AggregationDurationType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_channels' function.
class ListChannelsResponse(BaseValidatorModel):
    channels: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_event_rule' function.
class UpdateEventRuleResponse(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    statusSummaryByRegion: Dict[str, EventRuleStatusSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_notification_configuration' function.
class UpdateNotificationConfigurationResponse(BaseValidatorModel):
    arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_notification_hub' function.
class DeregisterNotificationHubResponse(BaseValidatorModel):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummary
    ResponseMetadata: ResponseMetadata


class NotificationHubOverview(BaseValidatorModel):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummary
    creationTime: datetime
    lastActivationTime: Optional[datetime] = None


# This class is the output for the 'register_notification_hub' function.
class RegisterNotificationHubResponse(BaseValidatorModel):
    notificationHubRegion: str
    statusSummary: NotificationHubStatusSummary
    creationTime: datetime
    lastActivationTime: datetime
    ResponseMetadata: ResponseMetadata


class MessageComponents(BaseValidatorModel):
    headline: Optional[str] = None
    paragraphSummary: Optional[str] = None
    completeDescription: Optional[str] = None
    dimensions: Optional[List[Dimension]] = None


class GetNotificationsAccessForOrganizationResponse(BaseValidatorModel):
    notificationsAccessForOrganization: NotificationsAccessForOrganization
    ResponseMetadata: ResponseMetadata


class ListChannelsRequestPaginate(BaseValidatorModel):
    notificationConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEventRulesRequestPaginate(BaseValidatorModel):
    notificationConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedNotificationChannelAssociationsRequestPaginate(BaseValidatorModel):
    managedNotificationConfigurationArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedNotificationConfigurationsRequestPaginate(BaseValidatorModel):
    channelIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationConfigurationsRequestPaginate(BaseValidatorModel):
    eventRuleSource: Optional[str] = None
    channelArn: Optional[str] = None
    status: Optional[NotificationConfigurationStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationHubsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_managed_notification_channel_associations' function.
class ListManagedNotificationChannelAssociationsResponse(BaseValidatorModel):
    channelAssociations: List[ManagedNotificationChannelAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListManagedNotificationChildEventsRequestPaginate(BaseValidatorModel):
    aggregateManagedNotificationEventArn: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    locale: Optional[LocaleCodeType] = None
    relatedAccount: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_managed_notification_child_events' function.
class ListManagedNotificationChildEventsRequest(BaseValidatorModel):
    aggregateManagedNotificationEventArn: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    locale: Optional[LocaleCodeType] = None
    maxResults: Optional[int] = None
    relatedAccount: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    nextToken: Optional[str] = None


class ListManagedNotificationEventsRequestPaginate(BaseValidatorModel):
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    relatedAccount: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_managed_notification_events' function.
class ListManagedNotificationEventsRequest(BaseValidatorModel):
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    organizationalUnitId: Optional[str] = None
    relatedAccount: Optional[str] = None


class ListNotificationEventsRequestPaginate(BaseValidatorModel):
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    includeChildEvents: Optional[bool] = None
    aggregateNotificationEventArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_notification_events' function.
class ListNotificationEventsRequest(BaseValidatorModel):
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    locale: Optional[LocaleCodeType] = None
    source: Optional[str] = None
    includeChildEvents: Optional[bool] = None
    aggregateNotificationEventArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_managed_notification_configurations' function.
class ListManagedNotificationConfigurationsResponse(BaseValidatorModel):
    managedNotificationConfigurations: List[ManagedNotificationConfigurationStructure]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_notification_configurations' function.
class ListNotificationConfigurationsResponse(BaseValidatorModel):
    notificationConfigurations: List[NotificationConfigurationStructure]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ManagedNotificationEventSummary(BaseValidatorModel):
    schemaVersion: Literal['v1.0']
    sourceEventMetadata: ManagedSourceEventMetadataSummary
    messageComponents: MessageComponentsSummary
    eventStatus: EventStatusType
    notificationType: NotificationTypeType


class NotificationEventSummary(BaseValidatorModel):
    schemaVersion: Literal['v1.0']
    sourceEventMetadata: SourceEventMetadataSummary
    messageComponents: MessageComponentsSummary
    eventStatus: EventStatusType
    notificationType: NotificationTypeType


class SourceEventMetadata(BaseValidatorModel):
    eventTypeVersion: str
    sourceEventId: str
    relatedAccount: str
    source: str
    eventOccurrenceTime: datetime
    eventType: str
    relatedResources: List[Resource]
    eventOriginRegion: Optional[str] = None


class ManagedNotificationChildEventSummary(BaseValidatorModel):
    schemaVersion: Literal['v1.0']
    sourceEventMetadata: ManagedSourceEventMetadataSummary
    messageComponents: MessageComponentsSummary
    aggregationDetail: AggregationDetail
    eventStatus: EventStatusType
    notificationType: NotificationTypeType


# This class is the output for the 'list_event_rules' function.
class ListEventRulesResponse(BaseValidatorModel):
    eventRules: List[EventRuleStructure]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_notification_hubs' function.
class ListNotificationHubsResponse(BaseValidatorModel):
    notificationHubs: List[NotificationHubOverview]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ManagedNotificationChildEvent(BaseValidatorModel):
    schemaVersion: Literal['v1.0']
    id: str
    messageComponents: MessageComponents
    notificationType: NotificationTypeType
    aggregateManagedNotificationEventArn: str
    textParts: Dict[str, TextPartValue]
    sourceEventDetailUrl: Optional[str] = None
    sourceEventDetailUrlDisplayText: Optional[str] = None
    eventStatus: Optional[EventStatusType] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    organizationalUnitId: Optional[str] = None
    aggregationDetail: Optional[AggregationDetail] = None


class ManagedNotificationEvent(BaseValidatorModel):
    schemaVersion: Literal['v1.0']
    id: str
    messageComponents: MessageComponents
    notificationType: NotificationTypeType
    textParts: Dict[str, TextPartValue]
    sourceEventDetailUrl: Optional[str] = None
    sourceEventDetailUrlDisplayText: Optional[str] = None
    eventStatus: Optional[EventStatusType] = None
    aggregationEventType: Optional[AggregationEventTypeType] = None
    aggregationSummary: Optional[AggregationSummary] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    organizationalUnitId: Optional[str] = None


class ManagedNotificationEventOverview(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    notificationEvent: ManagedNotificationEventSummary
    aggregationEventType: Optional[AggregationEventTypeType] = None
    organizationalUnitId: Optional[str] = None
    aggregationSummary: Optional[AggregationSummary] = None
    aggregatedNotificationRegions: Optional[List[str]] = None


class NotificationEventOverview(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    notificationEvent: NotificationEventSummary
    aggregationEventType: Optional[AggregationEventTypeType] = None
    aggregateNotificationEventArn: Optional[str] = None
    aggregationSummary: Optional[AggregationSummary] = None


class NotificationEvent(BaseValidatorModel):
    schemaVersion: Literal['v1.0']
    id: str
    sourceEventMetadata: SourceEventMetadata
    messageComponents: MessageComponents
    notificationType: NotificationTypeType
    textParts: Dict[str, TextPartValue]
    media: List[MediaElement]
    sourceEventDetailUrl: Optional[str] = None
    sourceEventDetailUrlDisplayText: Optional[str] = None
    eventStatus: Optional[EventStatusType] = None
    aggregationEventType: Optional[AggregationEventTypeType] = None
    aggregateNotificationEventArn: Optional[str] = None
    aggregationSummary: Optional[AggregationSummary] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class ManagedNotificationChildEventOverview(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    relatedAccount: str
    creationTime: datetime
    childEvent: ManagedNotificationChildEventSummary
    aggregateManagedNotificationEventArn: str
    organizationalUnitId: Optional[str] = None


# This class is the output for the 'get_managed_notification_child_event' function.
class GetManagedNotificationChildEventResponse(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    creationTime: datetime
    content: ManagedNotificationChildEvent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_managed_notification_event' function.
class GetManagedNotificationEventResponse(BaseValidatorModel):
    arn: str
    managedNotificationConfigurationArn: str
    creationTime: datetime
    content: ManagedNotificationEvent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_managed_notification_events' function.
class ListManagedNotificationEventsResponse(BaseValidatorModel):
    managedNotificationEvents: List[ManagedNotificationEventOverview]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_notification_events' function.
class ListNotificationEventsResponse(BaseValidatorModel):
    notificationEvents: List[NotificationEventOverview]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_notification_event' function.
class GetNotificationEventResponse(BaseValidatorModel):
    arn: str
    notificationConfigurationArn: str
    creationTime: datetime
    content: NotificationEvent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_managed_notification_child_events' function.
class ListManagedNotificationChildEventsResponse(BaseValidatorModel):
    managedNotificationChildEvents: List[ManagedNotificationChildEventOverview]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None