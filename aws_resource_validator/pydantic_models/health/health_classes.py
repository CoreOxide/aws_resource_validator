from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.health.health_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountEntityAggregate(BaseValidatorModel):
    accountId: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[EntityStatusCodeType, int]] = None


class AffectedEntity(BaseValidatorModel):
    entityArn: Optional[str] = None
    eventArn: Optional[str] = None
    entityValue: Optional[str] = None
    entityUrl: Optional[str] = None
    awsAccountId: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[EntityStatusCodeType] = None
    tags: Optional[Dict[str, str]] = None
    entityMetadata: Optional[Dict[str, str]] = None

Timestamp = Union[datetime, str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_affected_accounts_for_organization' function.
class DescribeAffectedAccountsForOrganizationRequest(BaseValidatorModel):
    eventArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EntityAccountFilter(BaseValidatorModel):
    eventArn: str
    awsAccountId: Optional[str] = None
    statusCodes: Optional[List[EntityStatusCodeType]] = None


class EventAccountFilter(BaseValidatorModel):
    eventArn: str
    awsAccountId: Optional[str] = None


class OrganizationAffectedEntitiesErrorItem(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'describe_entity_aggregates_for_organization' function.
class DescribeEntityAggregatesForOrganizationRequest(BaseValidatorModel):
    eventArns: List[str]
    awsAccountIds: Optional[List[str]] = None


# This class is the input for the 'describe_entity_aggregates' function.
class DescribeEntityAggregatesRequest(BaseValidatorModel):
    eventArns: Optional[List[str]] = None


class EntityAggregate(BaseValidatorModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[EntityStatusCodeType, int]] = None


class EventAggregate(BaseValidatorModel):
    aggregateValue: Optional[str] = None
    count: Optional[int] = None


class OrganizationEventDetailsErrorItem(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


# This class is the input for the 'describe_event_details' function.
class DescribeEventDetailsRequest(BaseValidatorModel):
    eventArns: List[str]
    locale: Optional[str] = None


class EventDetailsErrorItem(BaseValidatorModel):
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


class EventTypeFilter(BaseValidatorModel):
    eventTypeCodes: Optional[List[str]] = None
    services: Optional[List[str]] = None
    eventTypeCategories: Optional[List[EventTypeCategoryType]] = None


class EventType(BaseValidatorModel):
    service: Optional[str] = None
    code: Optional[str] = None
    category: Optional[EventTypeCategoryType] = None


class OrganizationEvent(BaseValidatorModel):
    arn: Optional[str] = None
    service: Optional[str] = None
    eventTypeCode: Optional[str] = None
    eventTypeCategory: Optional[EventTypeCategoryType] = None
    eventScopeCode: Optional[EventScopeCodeType] = None
    region: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[EventStatusCodeType] = None


class Event(BaseValidatorModel):
    arn: Optional[str] = None
    service: Optional[str] = None
    eventTypeCode: Optional[str] = None
    eventTypeCategory: Optional[EventTypeCategoryType] = None
    region: Optional[str] = None
    availabilityZone: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[EventStatusCodeType] = None
    eventScopeCode: Optional[EventScopeCodeType] = None


class EventDescription(BaseValidatorModel):
    latestDescription: Optional[str] = None


class OrganizationEntityAggregate(BaseValidatorModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[EntityStatusCodeType, int]] = None
    accounts: Optional[List[AccountEntityAggregate]] = None


class DateTimeRange(BaseValidatorModel):
    from_: Optional[Timestamp] = None
    to: Optional[Timestamp] = None


class DescribeAffectedAccountsForOrganizationRequestPaginate(BaseValidatorModel):
    eventArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'describe_affected_accounts_for_organization' function.
class DescribeAffectedAccountsForOrganizationResponse(BaseValidatorModel):
    affectedAccounts: List[str]
    eventScopeCode: EventScopeCodeType
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_affected_entities' function.
class DescribeAffectedEntitiesResponse(BaseValidatorModel):
    entities: List[AffectedEntity]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeHealthServiceStatusForOrganizationResponse(BaseValidatorModel):
    healthServiceAccessStatusForOrganization: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class DescribeAffectedEntitiesForOrganizationRequestPaginate(BaseValidatorModel):
    organizationEntityFilters: Optional[List[EventAccountFilter]] = None
    locale: Optional[str] = None
    organizationEntityAccountFilters: Optional[List[EntityAccountFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_affected_entities_for_organization' function.
class DescribeAffectedEntitiesForOrganizationRequest(BaseValidatorModel):
    organizationEntityFilters: Optional[List[EventAccountFilter]] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    organizationEntityAccountFilters: Optional[List[EntityAccountFilter]] = None


# This class is the input for the 'describe_event_details_for_organization' function.
class DescribeEventDetailsForOrganizationRequest(BaseValidatorModel):
    organizationEventDetailFilters: List[EventAccountFilter]
    locale: Optional[str] = None


# This class is the output for the 'describe_affected_entities_for_organization' function.
class DescribeAffectedEntitiesForOrganizationResponse(BaseValidatorModel):
    entities: List[AffectedEntity]
    failedSet: List[OrganizationAffectedEntitiesErrorItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_entity_aggregates' function.
class DescribeEntityAggregatesResponse(BaseValidatorModel):
    entityAggregates: List[EntityAggregate]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_aggregates' function.
class DescribeEventAggregatesResponse(BaseValidatorModel):
    eventAggregates: List[EventAggregate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeEventTypesRequestPaginate(BaseValidatorModel):
    filter: Optional[EventTypeFilter] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_event_types' function.
class DescribeEventTypesRequest(BaseValidatorModel):
    filter: Optional[EventTypeFilter] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'describe_event_types' function.
class DescribeEventTypesResponse(BaseValidatorModel):
    eventTypes: List[EventType]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_events_for_organization' function.
class DescribeEventsForOrganizationResponse(BaseValidatorModel):
    events: List[OrganizationEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'describe_events' function.
class DescribeEventsResponse(BaseValidatorModel):
    events: List[Event]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EventDetails(BaseValidatorModel):
    event: Optional[Event] = None
    eventDescription: Optional[EventDescription] = None
    eventMetadata: Optional[Dict[str, str]] = None


class OrganizationEventDetails(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    event: Optional[Event] = None
    eventDescription: Optional[EventDescription] = None
    eventMetadata: Optional[Dict[str, str]] = None


# This class is the output for the 'describe_entity_aggregates_for_organization' function.
class DescribeEntityAggregatesForOrganizationResponse(BaseValidatorModel):
    organizationEntityAggregates: List[OrganizationEntityAggregate]
    ResponseMetadata: ResponseMetadata


class EntityFilter(BaseValidatorModel):
    eventArns: List[str]
    entityArns: Optional[List[str]] = None
    entityValues: Optional[List[str]] = None
    lastUpdatedTimes: Optional[List[DateTimeRange]] = None
    tags: Optional[List[Dict[str, str]]] = None
    statusCodes: Optional[List[EntityStatusCodeType]] = None


class EventFilter(BaseValidatorModel):
    eventArns: Optional[List[str]] = None
    eventTypeCodes: Optional[List[str]] = None
    services: Optional[List[str]] = None
    regions: Optional[List[str]] = None
    availabilityZones: Optional[List[str]] = None
    startTimes: Optional[List[DateTimeRange]] = None
    endTimes: Optional[List[DateTimeRange]] = None
    lastUpdatedTimes: Optional[List[DateTimeRange]] = None
    entityArns: Optional[List[str]] = None
    entityValues: Optional[List[str]] = None
    eventTypeCategories: Optional[List[EventTypeCategoryType]] = None
    tags: Optional[List[Dict[str, str]]] = None
    eventStatusCodes: Optional[List[EventStatusCodeType]] = None


class OrganizationEventFilter(BaseValidatorModel):
    eventTypeCodes: Optional[List[str]] = None
    awsAccountIds: Optional[List[str]] = None
    services: Optional[List[str]] = None
    regions: Optional[List[str]] = None
    startTime: Optional[DateTimeRange] = None
    endTime: Optional[DateTimeRange] = None
    lastUpdatedTime: Optional[DateTimeRange] = None
    entityArns: Optional[List[str]] = None
    entityValues: Optional[List[str]] = None
    eventTypeCategories: Optional[List[EventTypeCategoryType]] = None
    eventStatusCodes: Optional[List[EventStatusCodeType]] = None


# This class is the output for the 'describe_event_details' function.
class DescribeEventDetailsResponse(BaseValidatorModel):
    successfulSet: List[EventDetails]
    failedSet: List[EventDetailsErrorItem]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_details_for_organization' function.
class DescribeEventDetailsForOrganizationResponse(BaseValidatorModel):
    successfulSet: List[OrganizationEventDetails]
    failedSet: List[OrganizationEventDetailsErrorItem]
    ResponseMetadata: ResponseMetadata


class DescribeAffectedEntitiesRequestPaginate(BaseValidatorModel):
    filter: EntityFilter
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_affected_entities' function.
class DescribeAffectedEntitiesRequest(BaseValidatorModel):
    filter: EntityFilter
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeEventAggregatesRequestPaginate(BaseValidatorModel):
    aggregateField: Literal['eventTypeCategory']
    filter: Optional[EventFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_event_aggregates' function.
class DescribeEventAggregatesRequest(BaseValidatorModel):
    aggregateField: Literal['eventTypeCategory']
    filter: Optional[EventFilter] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeEventsRequestPaginate(BaseValidatorModel):
    filter: Optional[EventFilter] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_events' function.
class DescribeEventsRequest(BaseValidatorModel):
    filter: Optional[EventFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[str] = None


class DescribeEventsForOrganizationRequestPaginate(BaseValidatorModel):
    filter: Optional[OrganizationEventFilter] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_events_for_organization' function.
class DescribeEventsForOrganizationRequest(BaseValidatorModel):
    filter: Optional[OrganizationEventFilter] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[str] = None