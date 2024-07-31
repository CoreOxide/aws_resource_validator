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
from aws_resource_validator.pydantic_models.health_constants import *

class AccountEntityAggregateTypeDef(BaseModel):
    accountId: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[entityStatusCodeType, int]] = None

class AffectedEntityTypeDef(BaseModel):
    entityArn: Optional[str] = None
    eventArn: Optional[str] = None
    entityValue: Optional[str] = None
    entityUrl: Optional[str] = None
    awsAccountId: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[entityStatusCodeType] = None
    tags: Optional[Dict[str, str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAffectedAccountsForOrganizationRequestRequestTypeDef(BaseModel):
    eventArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class EntityAccountFilterTypeDef(BaseModel):
    eventArn: str
    awsAccountId: Optional[str] = None
    statusCodes: Optional[Sequence[entityStatusCodeType]] = None

class EventAccountFilterTypeDef(BaseModel):
    eventArn: str
    awsAccountId: Optional[str] = None

class OrganizationAffectedEntitiesErrorItemTypeDef(BaseModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None

class DescribeEntityAggregatesForOrganizationRequestRequestTypeDef(BaseModel):
    eventArns: Sequence[str]
    awsAccountIds: Optional[Sequence[str]] = None

class DescribeEntityAggregatesRequestRequestTypeDef(BaseModel):
    eventArns: Optional[Sequence[str]] = None

class EntityAggregateTypeDef(BaseModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[entityStatusCodeType, int]] = None

class EventAggregateTypeDef(BaseModel):
    aggregateValue: Optional[str] = None
    count: Optional[int] = None

class OrganizationEventDetailsErrorItemTypeDef(BaseModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None

class DescribeEventDetailsRequestRequestTypeDef(BaseModel):
    eventArns: Sequence[str]
    locale: Optional[str] = None

class EventDetailsErrorItemTypeDef(BaseModel):
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None

class EventTypeFilterTypeDef(BaseModel):
    eventTypeCodes: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[eventTypeCategoryType]] = None

class EventTypeTypeDef(BaseModel):
    service: Optional[str] = None
    code: Optional[str] = None
    category: Optional[eventTypeCategoryType] = None

class OrganizationEventTypeDef(BaseModel):
    arn: Optional[str] = None
    service: Optional[str] = None
    eventTypeCode: Optional[str] = None
    eventTypeCategory: Optional[eventTypeCategoryType] = None
    eventScopeCode: Optional[eventScopeCodeType] = None
    region: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[eventStatusCodeType] = None

class EventTypeDef(BaseModel):
    arn: Optional[str] = None
    service: Optional[str] = None
    eventTypeCode: Optional[str] = None
    eventTypeCategory: Optional[eventTypeCategoryType] = None
    region: Optional[str] = None
    availabilityZone: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[eventStatusCodeType] = None
    eventScopeCode: Optional[eventScopeCodeType] = None

class EventDescriptionTypeDef(BaseModel):
    latestDescription: Optional[str] = None

class OrganizationEntityAggregateTypeDef(BaseModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[entityStatusCodeType, int]] = None
    accounts: Optional[List[AccountEntityAggregateTypeDef]] = None

class DateTimeRangeTypeDef(BaseModel):
    from: Optional[TimestampTypeDef] = None
    to: Optional[TimestampTypeDef] = None

class DescribeAffectedAccountsForOrganizationRequestDescribeAffectedAccountsForOrganizationPaginateTypeDef(BaseModel):
    eventArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAffectedAccountsForOrganizationResponseTypeDef(BaseModel):
    affectedAccounts: List[str]
    eventScopeCode: eventScopeCodeType
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAffectedEntitiesResponseTypeDef(BaseModel):
    entities: List[AffectedEntityTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHealthServiceStatusForOrganizationResponseTypeDef(BaseModel):
    healthServiceAccessStatusForOrganization: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAffectedEntitiesForOrganizationRequestDescribeAffectedEntitiesForOrganizationPaginateTypeDef(BaseModel):
    organizationEntityFilters: Optional[Sequence[EventAccountFilterTypeDef]] = None
    locale: Optional[str] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef(BaseModel):
    organizationEntityFilters: Optional[Sequence[EventAccountFilterTypeDef]] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilterTypeDef]] = None

class DescribeEventDetailsForOrganizationRequestRequestTypeDef(BaseModel):
    organizationEventDetailFilters: Sequence[EventAccountFilterTypeDef]
    locale: Optional[str] = None

class DescribeAffectedEntitiesForOrganizationResponseTypeDef(BaseModel):
    entities: List[AffectedEntityTypeDef]
    failedSet: List[OrganizationAffectedEntitiesErrorItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntityAggregatesResponseTypeDef(BaseModel):
    entityAggregates: List[EntityAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventAggregatesResponseTypeDef(BaseModel):
    eventAggregates: List[EventAggregateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventTypesRequestDescribeEventTypesPaginateTypeDef(BaseModel):
    filter: Optional[EventTypeFilterTypeDef] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventTypesRequestRequestTypeDef(BaseModel):
    filter: Optional[EventTypeFilterTypeDef] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeEventTypesResponseTypeDef(BaseModel):
    eventTypes: List[EventTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsForOrganizationResponseTypeDef(BaseModel):
    events: List[OrganizationEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsResponseTypeDef(BaseModel):
    events: List[EventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventDetailsTypeDef(BaseModel):
    event: Optional[EventTypeDef] = None
    eventDescription: Optional[EventDescriptionTypeDef] = None
    eventMetadata: Optional[Dict[str, str]] = None

class OrganizationEventDetailsTypeDef(BaseModel):
    awsAccountId: Optional[str] = None
    event: Optional[EventTypeDef] = None
    eventDescription: Optional[EventDescriptionTypeDef] = None
    eventMetadata: Optional[Dict[str, str]] = None

class DescribeEntityAggregatesForOrganizationResponseTypeDef(BaseModel):
    organizationEntityAggregates: List[OrganizationEntityAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EntityFilterTypeDef(BaseModel):
    eventArns: Sequence[str]
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    lastUpdatedTimes: Optional[Sequence[DateTimeRangeTypeDef]] = None
    tags: Optional[Sequence[Mapping[str, str]]] = None
    statusCodes: Optional[Sequence[entityStatusCodeType]] = None

class EventFilterTypeDef(BaseModel):
    eventArns: Optional[Sequence[str]] = None
    eventTypeCodes: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    availabilityZones: Optional[Sequence[str]] = None
    startTimes: Optional[Sequence[DateTimeRangeTypeDef]] = None
    endTimes: Optional[Sequence[DateTimeRangeTypeDef]] = None
    lastUpdatedTimes: Optional[Sequence[DateTimeRangeTypeDef]] = None
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[eventTypeCategoryType]] = None
    tags: Optional[Sequence[Mapping[str, str]]] = None
    eventStatusCodes: Optional[Sequence[eventStatusCodeType]] = None

class OrganizationEventFilterTypeDef(BaseModel):
    eventTypeCodes: Optional[Sequence[str]] = None
    awsAccountIds: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    regions: Optional[Sequence[str]] = None
    startTime: Optional[DateTimeRangeTypeDef] = None
    endTime: Optional[DateTimeRangeTypeDef] = None
    lastUpdatedTime: Optional[DateTimeRangeTypeDef] = None
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[eventTypeCategoryType]] = None
    eventStatusCodes: Optional[Sequence[eventStatusCodeType]] = None

class DescribeEventDetailsResponseTypeDef(BaseModel):
    successfulSet: List[EventDetailsTypeDef]
    failedSet: List[EventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventDetailsForOrganizationResponseTypeDef(BaseModel):
    successfulSet: List[OrganizationEventDetailsTypeDef]
    failedSet: List[OrganizationEventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAffectedEntitiesRequestDescribeAffectedEntitiesPaginateTypeDef(BaseModel):
    filter: EntityFilterTypeDef
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAffectedEntitiesRequestRequestTypeDef(BaseModel):
    filter: EntityFilterTypeDef
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeEventAggregatesRequestDescribeEventAggregatesPaginateTypeDef(BaseModel):
    aggregateField: Literal["eventTypeCategory"]
    filter: Optional[EventFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventAggregatesRequestRequestTypeDef(BaseModel):
    aggregateField: Literal["eventTypeCategory"]
    filter: Optional[EventFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeEventsRequestDescribeEventsPaginateTypeDef(BaseModel):
    filter: Optional[EventFilterTypeDef] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsRequestRequestTypeDef(BaseModel):
    filter: Optional[EventFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[str] = None

class DescribeEventsForOrganizationRequestDescribeEventsForOrganizationPaginateTypeDef(BaseModel):
    filter: Optional[OrganizationEventFilterTypeDef] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsForOrganizationRequestRequestTypeDef(BaseModel):
    filter: Optional[OrganizationEventFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[str] = None

