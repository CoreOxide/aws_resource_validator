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

class AccountEntityAggregateTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[EntityStatusCodeType, int]] = None


class AffectedEntityTypeDef(BaseValidatorModel):
    entityArn: Optional[str] = None
    eventArn: Optional[str] = None
    entityValue: Optional[str] = None
    entityUrl: Optional[str] = None
    awsAccountId: Optional[str] = None
    lastUpdatedTime: Optional[datetime] = None
    statusCode: Optional[EntityStatusCodeType] = None
    tags: Optional[Dict[str, str]] = None
    entityMetadata: Optional[Dict[str, str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeAffectedAccountsForOrganizationRequestTypeDef(BaseValidatorModel):
    eventArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EntityAccountFilterTypeDef(BaseValidatorModel):
    eventArn: str
    awsAccountId: Optional[str] = None
    statusCodes: Optional[Sequence[EntityStatusCodeType]] = None


class EventAccountFilterTypeDef(BaseValidatorModel):
    eventArn: str
    awsAccountId: Optional[str] = None


class OrganizationAffectedEntitiesErrorItemTypeDef(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


class DescribeEntityAggregatesForOrganizationRequestTypeDef(BaseValidatorModel):
    eventArns: Sequence[str]
    awsAccountIds: Optional[Sequence[str]] = None


class DescribeEntityAggregatesRequestTypeDef(BaseValidatorModel):
    eventArns: Optional[Sequence[str]] = None


class EntityAggregateTypeDef(BaseValidatorModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[EntityStatusCodeType, int]] = None


class EventAggregateTypeDef(BaseValidatorModel):
    aggregateValue: Optional[str] = None
    count: Optional[int] = None


class OrganizationEventDetailsErrorItemTypeDef(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


class DescribeEventDetailsRequestTypeDef(BaseValidatorModel):
    eventArns: Sequence[str]
    locale: Optional[str] = None


class EventDetailsErrorItemTypeDef(BaseValidatorModel):
    eventArn: Optional[str] = None
    errorName: Optional[str] = None
    errorMessage: Optional[str] = None


class EventTypeFilterTypeDef(BaseValidatorModel):
    eventTypeCodes: Optional[Sequence[str]] = None
    services: Optional[Sequence[str]] = None
    eventTypeCategories: Optional[Sequence[EventTypeCategoryType]] = None


class EventTypeTypeDef(BaseValidatorModel):
    service: Optional[str] = None
    code: Optional[str] = None
    category: Optional[EventTypeCategoryType] = None


class OrganizationEventTypeDef(BaseValidatorModel):
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


class EventTypeDef(BaseValidatorModel):
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


class EventDescriptionTypeDef(BaseValidatorModel):
    latestDescription: Optional[str] = None


class OrganizationEntityAggregateTypeDef(BaseValidatorModel):
    eventArn: Optional[str] = None
    count: Optional[int] = None
    statuses: Optional[Dict[EntityStatusCodeType, int]] = None
    accounts: Optional[List[AccountEntityAggregateTypeDef]] = None


class DescribeAffectedAccountsForOrganizationRequestPaginateTypeDef(BaseValidatorModel):
    eventArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAffectedAccountsForOrganizationResponseTypeDef(BaseValidatorModel):
    affectedAccounts: List[str]
    eventScopeCode: EventScopeCodeType
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeAffectedEntitiesResponseTypeDef(BaseValidatorModel):
    entities: List[AffectedEntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeHealthServiceStatusForOrganizationResponseTypeDef(BaseValidatorModel):
    healthServiceAccessStatusForOrganization: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeAffectedEntitiesForOrganizationRequestPaginateTypeDef(BaseValidatorModel):
    organizationEntityFilters: Optional[Sequence[EventAccountFilterTypeDef]] = None
    locale: Optional[str] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeAffectedEntitiesForOrganizationRequestTypeDef(BaseValidatorModel):
    organizationEntityFilters: Optional[Sequence[EventAccountFilterTypeDef]] = None
    locale: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    organizationEntityAccountFilters: Optional[Sequence[EntityAccountFilterTypeDef]] = None


class DescribeEventDetailsForOrganizationRequestTypeDef(BaseValidatorModel):
    organizationEventDetailFilters: Sequence[EventAccountFilterTypeDef]
    locale: Optional[str] = None


class DescribeAffectedEntitiesForOrganizationResponseTypeDef(BaseValidatorModel):
    entities: List[AffectedEntityTypeDef]
    failedSet: List[OrganizationAffectedEntitiesErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeEntityAggregatesResponseTypeDef(BaseValidatorModel):
    entityAggregates: List[EntityAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEventAggregatesResponseTypeDef(BaseValidatorModel):
    eventAggregates: List[EventAggregateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeEventTypesResponseTypeDef(BaseValidatorModel):
    eventTypes: List[EventTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeEventsForOrganizationResponseTypeDef(BaseValidatorModel):
    events: List[OrganizationEventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeEventsResponseTypeDef(BaseValidatorModel):
    events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class DateTimeRangeTypeDef(BaseValidatorModel):
    pass


class EntityFilterTypeDef(BaseValidatorModel):
    eventArns: Sequence[str]
    entityArns: Optional[Sequence[str]] = None
    entityValues: Optional[Sequence[str]] = None
    lastUpdatedTimes: Optional[Sequence[DateTimeRangeTypeDef]] = None
    tags: Optional[Sequence[Mapping[str, str]]] = None
    statusCodes: Optional[Sequence[EntityStatusCodeType]] = None


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
    eventTypeCategories: Optional[Sequence[EventTypeCategoryType]] = None
    tags: Optional[Sequence[Mapping[str, str]]] = None
    eventStatusCodes: Optional[Sequence[EventStatusCodeType]] = None


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
    eventTypeCategories: Optional[Sequence[EventTypeCategoryType]] = None
    eventStatusCodes: Optional[Sequence[EventStatusCodeType]] = None


class DescribeEventDetailsResponseTypeDef(BaseValidatorModel):
    successfulSet: List[EventDetailsTypeDef]
    failedSet: List[EventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEventDetailsForOrganizationResponseTypeDef(BaseValidatorModel):
    successfulSet: List[OrganizationEventDetailsTypeDef]
    failedSet: List[OrganizationEventDetailsErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


