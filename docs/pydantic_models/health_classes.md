# Health Classes

# AccountEntityAggregateTypeDef

### accountId
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### statuses
- **Type**: typing.Optional[typing.Dict[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN'], int]]


# AffectedEntityTypeDef

### entityArn
- **Type**: typing.Optional[str]

### eventArn
- **Type**: typing.Optional[str]

### entityValue
- **Type**: typing.Optional[str]

### entityUrl
- **Type**: typing.Optional[str]

### awsAccountId
- **Type**: typing.Optional[str]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### statusCode
- **Type**: typing.Optional[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateTimeRangeTypeDef

### to
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# DescribeAffectedAccountsForOrganizationRequestDescribeAffectedAccountsForOrganizationPaginateTypeDef

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfigTypeDef]


# DescribeAffectedAccountsForOrganizationRequestRequestTypeDef

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeAffectedAccountsForOrganizationResponseTypeDef

### affectedAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### eventScopeCode
- **Type**: typing.Literal['ACCOUNT_SPECIFIC', 'NONE', 'PUBLIC']
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAffectedEntitiesForOrganizationRequestDescribeAffectedEntitiesForOrganizationPaginateTypeDef

### organizationEntityFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EventAccountFilterTypeDef]]

### locale
- **Type**: typing.Optional[str]

### organizationEntityAccountFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EntityAccountFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfigTypeDef]


# DescribeAffectedEntitiesForOrganizationRequestRequestTypeDef

### organizationEntityFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EventAccountFilterTypeDef]]

### locale
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### organizationEntityAccountFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EntityAccountFilterTypeDef]]


# DescribeAffectedEntitiesForOrganizationResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.AffectedEntityTypeDef]
- **Required**: Yes

### failedSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationAffectedEntitiesErrorItemTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAffectedEntitiesRequestDescribeAffectedEntitiesPaginateTypeDef

### filter
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.EntityFilterTypeDef'>
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfigTypeDef]


# DescribeAffectedEntitiesRequestRequestTypeDef

### filter
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.EntityFilterTypeDef'>
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeAffectedEntitiesResponseTypeDef

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.AffectedEntityTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntityAggregatesForOrganizationRequestRequestTypeDef

### eventArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### awsAccountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeEntityAggregatesForOrganizationResponseTypeDef

### organizationEntityAggregates
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEntityAggregateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntityAggregatesRequestRequestTypeDef

### eventArns
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeEntityAggregatesResponseTypeDef

### entityAggregates
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EntityAggregateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventAggregatesRequestDescribeEventAggregatesPaginateTypeDef

### aggregateField
- **Type**: typing.Literal['eventTypeCategory']
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfigTypeDef]


# DescribeEventAggregatesRequestRequestTypeDef

### aggregateField
- **Type**: typing.Literal['eventTypeCategory']
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventFilterTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# DescribeEventAggregatesResponseTypeDef

### eventAggregates
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventAggregateTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventDetailsForOrganizationRequestRequestTypeDef

### organizationEventDetailFilters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EventAccountFilterTypeDef]
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]


# DescribeEventDetailsForOrganizationResponseTypeDef

### successfulSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEventDetailsTypeDef]
- **Required**: Yes

### failedSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEventDetailsErrorItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventDetailsRequestRequestTypeDef

### eventArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]


# DescribeEventDetailsResponseTypeDef

### successfulSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventDetailsTypeDef]
- **Required**: Yes

### failedSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventDetailsErrorItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventTypesRequestDescribeEventTypesPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventTypeFilterTypeDef]

### locale
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfigTypeDef]


# DescribeEventTypesRequestRequestTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventTypeFilterTypeDef]

### locale
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeEventTypesResponseTypeDef

### eventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventTypeTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventsForOrganizationRequestDescribeEventsForOrganizationPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.OrganizationEventFilterTypeDef]

### locale
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfigTypeDef]


# DescribeEventsForOrganizationRequestRequestTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.OrganizationEventFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### locale
- **Type**: typing.Optional[str]


# DescribeEventsForOrganizationResponseTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEventTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEventsRequestDescribeEventsPaginateTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventFilterTypeDef]

### locale
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfigTypeDef]


# DescribeEventsRequestRequestTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### locale
- **Type**: typing.Optional[str]


# DescribeEventsResponseTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHealthServiceStatusForOrganizationResponseTypeDef

### healthServiceAccessStatusForOrganization
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntityAccountFilterTypeDef

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### statusCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN']]]


# EntityAggregateTypeDef

### eventArn
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### statuses
- **Type**: typing.Optional[typing.Dict[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN'], int]]


# EntityFilterTypeDef

### eventArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### entityArns
- **Type**: typing.Optional[typing.Sequence[str]]

### entityValues
- **Type**: typing.Optional[typing.Sequence[str]]

### lastUpdatedTimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRangeTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, str]]]

### statusCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN']]]


# EventAccountFilterTypeDef

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]


# EventAggregateTypeDef

### aggregateValue
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]


# EventDescriptionTypeDef

### latestDescription
- **Type**: typing.Optional[str]


# EventDetailsErrorItemTypeDef

### eventArn
- **Type**: typing.Optional[str]

### errorName
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# EventDetailsTypeDef

### event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventTypeDef]

### eventDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventDescriptionTypeDef]

### eventMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventFilterTypeDef

### eventArns
- **Type**: typing.Optional[typing.Sequence[str]]

### eventTypeCodes
- **Type**: typing.Optional[typing.Sequence[str]]

### services
- **Type**: typing.Optional[typing.Sequence[str]]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### availabilityZones
- **Type**: typing.Optional[typing.Sequence[str]]

### startTimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRangeTypeDef]]

### endTimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRangeTypeDef]]

### lastUpdatedTimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRangeTypeDef]]

### entityArns
- **Type**: typing.Optional[typing.Sequence[str]]

### entityValues
- **Type**: typing.Optional[typing.Sequence[str]]

### eventTypeCategories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]]

### tags
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, str]]]

### eventStatusCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['closed', 'open', 'upcoming']]]


# EventTypeDef

### arn
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### eventTypeCode
- **Type**: typing.Optional[str]

### eventTypeCategory
- **Type**: typing.Optional[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]

### region
- **Type**: typing.Optional[str]

### availabilityZone
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### statusCode
- **Type**: typing.Optional[typing.Literal['closed', 'open', 'upcoming']]

### eventScopeCode
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SPECIFIC', 'NONE', 'PUBLIC']]


# EventTypeFilterTypeDef

### eventTypeCodes
- **Type**: typing.Optional[typing.Sequence[str]]

### services
- **Type**: typing.Optional[typing.Sequence[str]]

### eventTypeCategories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]]


# EventTypeTypeDef

### service
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]


# OrganizationAffectedEntitiesErrorItemTypeDef

### awsAccountId
- **Type**: typing.Optional[str]

### eventArn
- **Type**: typing.Optional[str]

### errorName
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# OrganizationEntityAggregateTypeDef

### eventArn
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### statuses
- **Type**: typing.Optional[typing.Dict[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN'], int]]

### accounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.health_classes.AccountEntityAggregateTypeDef]]


# OrganizationEventDetailsErrorItemTypeDef

### awsAccountId
- **Type**: typing.Optional[str]

### eventArn
- **Type**: typing.Optional[str]

### errorName
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# OrganizationEventDetailsTypeDef

### awsAccountId
- **Type**: typing.Optional[str]

### event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventTypeDef]

### eventDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventDescriptionTypeDef]

### eventMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# OrganizationEventFilterTypeDef

### eventTypeCodes
- **Type**: typing.Optional[typing.Sequence[str]]

### awsAccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### services
- **Type**: typing.Optional[typing.Sequence[str]]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.DateTimeRangeTypeDef]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.DateTimeRangeTypeDef]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.DateTimeRangeTypeDef]

### entityArns
- **Type**: typing.Optional[typing.Sequence[str]]

### entityValues
- **Type**: typing.Optional[typing.Sequence[str]]

### eventTypeCategories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]]

### eventStatusCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['closed', 'open', 'upcoming']]]


# OrganizationEventTypeDef

### arn
- **Type**: typing.Optional[str]

### service
- **Type**: typing.Optional[str]

### eventTypeCode
- **Type**: typing.Optional[str]

### eventTypeCategory
- **Type**: typing.Optional[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]

### eventScopeCode
- **Type**: typing.Optional[typing.Literal['ACCOUNT_SPECIFIC', 'NONE', 'PUBLIC']]

### region
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### statusCode
- **Type**: typing.Optional[typing.Literal['closed', 'open', 'upcoming']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes


