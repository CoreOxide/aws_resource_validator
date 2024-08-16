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
from aws_resource_validator.pydantic_models.health_constants import *

class AccountEntityAggregateTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[entityStatusCodeType, int]] = None

class AffectedEntityTypeDef(BaseValidatorModel):
    entityArn: Optional[str] = None
    eventArn: Optional[str] = None
    entityValue: Optional[str] = None
    entityUrl: Optional[str] = None
    awsAccountId: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[entityStatusCodeType] = None
    tags: Optional[Dict[str, str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeAffectedAccountsForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    eventArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class EntityAccountFilterTypeDef(BaseValidatorModel):
    eventArn: str
    awsAccountId: Optional[str] = None
    statusCodes: Optional[Sequence[entityStatusCodeType]] = None

class EventAccountFilterTypeDef(BaseValidatorModel):
    eventArn: str
    awsAccountId: Optional[str] = None

class OrganizationAffectedEntitiesErrorItemTypeDef(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None

class DescribeEntityAggregatesForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    eventArns: Sequence[str]
    awsAccountIds: Optional[Sequence[str]] = None

class DescribeEntityAggregatesRequestRequestTypeDef(BaseValidatorModel):
    eventArns: Optional[Sequence[str]] = None

class EntityAggregateTypeDef(BaseValidatorModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[entityStatusCodeType, int]] = None

class EventAggregateTypeDef(BaseValidatorModel):
    aggregateValue: Optional[str] = None
    count: Optional[int] = None

class OrganizationEventDetailsErrorItemTypeDef(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None

class DescribeEventDetailsRequestRequestTypeDef(BaseValidatorModel):
    eventArns: Sequence[str]
    locale: Optional[str] = None

class EventDetailsErrorItemTypeDef(BaseValidatorModel):
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None

class EventTypeFilterTypeDef(BaseValidatorModel):
    eventTypeCodes: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[eventTypeCategoryType]] = None

class EventTypeTypeDef(BaseValidatorModel):
    service: Optional[str] = None
    code: Optional[str] = None
    category: Optional[eventTypeCategoryType] = None

class OrganizationEventTypeDef(BaseValidatorModel):
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

class EventTypeDef(BaseValidatorModel):
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

class EventDescriptionTypeDef(BaseValidatorModel):
    latestDescription: Optional[str] = None

class OrganizationEntityAggregateTypeDef(BaseValidatorModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[entityStatusCodeType, int]] = None
    accounts: Optional[List[AccountEntityAggregateTypeDef]] = None

class DateTimeRangeTypeDef(BaseValidatorModel):
    from: Optional[TimestampTypeDef] = None
    to: Optional[TimestampTypeDef] = None

class DescribeAffectedAccountsForOrganizationRequestDescribeAffectedAccountsForOrganizationPaginateTypeDef(BaseValidatorModel):
    eventArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAffectedAccountsForOrganizationResponseTypeDef(BaseValidatorModel):
    affectedAccounts: List[str]
    eventScopeCode: eventScopeCodeType
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAffectedEntitiesResponseTypeDef(BaseValidatorModel):
    entities: List[AffectedEntityTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeHealthServiceStatusForOrganizationResponseTypeDef(BaseValidatorModel):
    healthServiceAccessStatusForOrganization: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAffectedEntitiesForOrganizationRequestDescribeAffectedEntitiesForOrganizationPaginateTypeDef(BaseValidatorModel):
    organizationEntityFilters: Optional[Sequence[EventAccountFilterTypeDef]] = None
    locale: Optional[str] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    organizationEntityFilters: Optional[Sequence[EventAccountFilterTypeDef]] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilterTypeDef]] = None

class DescribeEventDetailsForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    organizationEventDetailFilters: Sequence[EventAccountFilterTypeDef]
    locale: Optional[str] = None

class DescribeAffectedEntitiesForOrganizationResponseTypeDef(BaseValidatorModel):
    entities: List[AffectedEntityTypeDef]
    failedSet: List[OrganizationAffectedEntitiesErrorItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEntityAggregatesResponseTypeDef(BaseValidatorModel):
    entityAggregates: List[EntityAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventAggregatesResponseTypeDef(BaseValidatorModel):
    eventAggregates: List[EventAggregateTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventTypesRequestDescribeEventTypesPaginateTypeDef(BaseValidatorModel):
    filter: Optional[EventTypeFilterTypeDef] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventTypesRequestRequestTypeDef(BaseValidatorModel):
    filter: Optional[EventTypeFilterTypeDef] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeEventTypesResponseTypeDef(BaseValidatorModel):
    eventTypes: List[EventTypeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsForOrganizationResponseTypeDef(BaseValidatorModel):
    events: List[OrganizationEventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsResponseTypeDef(BaseValidatorModel):
    events: List[EventTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EventDetailsTypeDef(BaseValidatorModel):
    event: Optional[EventTypeDef] = None
    eventDescription: Optional[EventDescriptionTypeDef] = None
    eventMetadata: Optional[Dict[str, str]] = None

class OrganizationEventDetailsTypeDef(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    event: Optional[EventTypeDef] = None
    eventDescription: Optional[EventDescriptionTypeDef] = None
    eventMetadata: Optional[Dict[str, str]] = None

class DescribeEntityAggregatesForOrganizationResponseTypeDef(BaseValidatorModel):
    organizationEntityAggregates: List[OrganizationEntityAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EntityFilterTypeDef(BaseValidatorModel):
    eventArns: Sequence[str]
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    lastUpdatedTimes: Optional[Sequence[DateTimeRangeTypeDef]] = None
    tags: Optional[Sequence[Mapping[str, str]]] = None
    statusCodes: Optional[Sequence[entityStatusCodeType]] = None

class EventFilterTypeDef(BaseValidatorModel):
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

class OrganizationEventFilterTypeDef(BaseValidatorModel):
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

class DescribeEventDetailsResponseTypeDef(BaseValidatorModel):
    successfulSet: List[EventDetailsTypeDef]
    failedSet: List[EventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventDetailsForOrganizationResponseTypeDef(BaseValidatorModel):
    successfulSet: List[OrganizationEventDetailsTypeDef]
    failedSet: List[OrganizationEventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAffectedEntitiesRequestDescribeAffectedEntitiesPaginateTypeDef(BaseValidatorModel):
    filter: EntityFilterTypeDef
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeAffectedEntitiesRequestRequestTypeDef(BaseValidatorModel):
    filter: EntityFilterTypeDef
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeEventAggregatesRequestDescribeEventAggregatesPaginateTypeDef(BaseValidatorModel):
    aggregateField: Literal["eventTypeCategory"]
    filter: Optional[EventFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventAggregatesRequestRequestTypeDef(BaseValidatorModel):
    aggregateField: Literal["eventTypeCategory"]
    filter: Optional[EventFilterTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeEventsRequestDescribeEventsPaginateTypeDef(BaseValidatorModel):
    filter: Optional[EventFilterTypeDef] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsRequestRequestTypeDef(BaseValidatorModel):
    filter: Optional[EventFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[str] = None

class DescribeEventsForOrganizationRequestDescribeEventsForOrganizationPaginateTypeDef(BaseValidatorModel):
    filter: Optional[OrganizationEventFilterTypeDef] = None
    locale: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsForOrganizationRequestRequestTypeDef(BaseValidatorModel):
    filter: Optional[OrganizationEventFilterTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    locale: Optional[str] = None

