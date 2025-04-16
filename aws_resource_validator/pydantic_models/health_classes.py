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
from aws_resource_validator.pydantic_models.health_constants import *

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


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


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
    statusCodes: Optional[Sequence[EntityStatusCodeType]] = None


class EventAccountFilter(BaseValidatorModel):
    eventArn: str
    awsAccountId: Optional[str] = None


class OrganizationAffectedEntitiesErrorItem(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


class DescribeEntityAggregatesForOrganizationRequest(BaseValidatorModel):
    eventArns: Sequence[str]
    awsAccountIds: Optional[Sequence[str]] = None


class DescribeEntityAggregatesRequest(BaseValidatorModel):
    eventArns: Optional[Sequence[str]] = None


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


class DescribeEventDetailsRequest(BaseValidatorModel):
    eventArns: Sequence[str]
    locale: Optional[str] = None


class EventDetailsErrorItem(BaseValidatorModel):
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


class EventTypeFilter(BaseValidatorModel):
    eventTypeCodes: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[EventTypeCategoryType]] = None


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


class DescribeAffectedAccountsForOrganizationRequestPaginate(BaseValidatorModel):
    eventArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAffectedAccountsForOrganizationResponse(BaseValidatorModel):
    affectedAccounts: List[str]
    eventScopeCode: EventScopeCodeType
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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
    organizationEntityFilters: Optional[Sequence[EventAccountFilter]] = None
    locale: Optional[str] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeAffectedEntitiesForOrganizationRequest(BaseValidatorModel):
    organizationEntityFilters: Optional[Sequence[EventAccountFilter]] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilter]] = None


class DescribeEventDetailsForOrganizationRequest(BaseValidatorModel):
    organizationEventDetailFilters: Sequence[EventAccountFilter]
    locale: Optional[str] = None


class DescribeAffectedEntitiesForOrganizationResponse(BaseValidatorModel):
    entities: List[AffectedEntity]
    failedSet: List[OrganizationAffectedEntitiesErrorItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeEntityAggregatesResponse(BaseValidatorModel):
    entityAggregates: List[EntityAggregate]
    ResponseMetadata: ResponseMetadata


class DescribeEventAggregatesResponse(BaseValidatorModel):
    eventAggregates: List[EventAggregate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeEventTypesResponse(BaseValidatorModel):
    eventTypes: List[EventType]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeEventsForOrganizationResponse(BaseValidatorModel):
    events: List[OrganizationEvent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class DescribeEntityAggregatesForOrganizationResponse(BaseValidatorModel):
    organizationEntityAggregates: List[OrganizationEntityAggregate]
    ResponseMetadata: ResponseMetadata


class DateTimeRange(BaseValidatorModel):
    pass


class EntityFilter(BaseValidatorModel):
    eventArns: Sequence[str]
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    lastUpdatedTimes: Optional[Sequence[DateTimeRange]] = None
    tags: Optional[Sequence[Mapping[str, str]]] = None
    statusCodes: Optional[Sequence[EntityStatusCodeType]] = None


class EventFilter(BaseValidatorModel):
    eventArns: Optional[Sequence[str]] = None
    eventTypeCodes: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    availabilityZones: Optional[Sequence[str]] = None
    startTimes: Optional[Sequence[DateTimeRange]] = None
    endTimes: Optional[Sequence[DateTimeRange]] = None
    lastUpdatedTimes: Optional[Sequence[DateTimeRange]] = None
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[EventTypeCategoryType]] = None
    tags: Optional[Sequence[Mapping[str, str]]] = None
    eventStatusCodes: Optional[Sequence[EventStatusCodeType]] = None


class OrganizationEventFilter(BaseValidatorModel):
    eventTypeCodes: Optional[Sequence[str]] = None
    awsAccountIds: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    startTime: Optional[DateTimeRange] = None
    endTime: Optional[DateTimeRange] = None
    lastUpdatedTime: Optional[DateTimeRange] = None
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[EventTypeCategoryType]] = None
    eventStatusCodes: Optional[Sequence[EventStatusCodeType]] = None


class DescribeEventDetailsResponse(BaseValidatorModel):
    successfulSet: List[EventDetails]
    failedSet: List[EventDetailsErrorItem]
    ResponseMetadata: ResponseMetadata


class DescribeEventDetailsForOrganizationResponse(BaseValidatorModel):
    successfulSet: List[OrganizationEventDetails]
    failedSet: List[OrganizationEventDetailsErrorItem]
    ResponseMetadata: ResponseMetadata


