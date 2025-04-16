# Health Classes

# AccountEntityAggregate

### accountId
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### statuses
- **Type**: typing.Optional[typing.Dict[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN'], int]]


# AffectedEntity

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

### entityMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DateTimeRange

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DescribeAffectedAccountsForOrganizationRequest

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeAffectedAccountsForOrganizationRequestPaginate

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfig]


# DescribeAffectedAccountsForOrganizationResponse

### affectedAccounts
- **Type**: typing.List[str]
- **Required**: Yes

### eventScopeCode
- **Type**: typing.Literal['ACCOUNT_SPECIFIC', 'NONE', 'PUBLIC']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeAffectedEntitiesForOrganizationRequest

### organizationEntityFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EventAccountFilter]]

### locale
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### organizationEntityAccountFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EntityAccountFilter]]


# DescribeAffectedEntitiesForOrganizationRequestPaginate

### organizationEntityFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EventAccountFilter]]

### locale
- **Type**: typing.Optional[str]

### organizationEntityAccountFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EntityAccountFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.PaginatorConfig]


# DescribeAffectedEntitiesForOrganizationResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.AffectedEntity]
- **Required**: Yes

### failedSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationAffectedEntitiesErrorItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeAffectedEntitiesResponse

### entities
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.AffectedEntity]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEntityAggregatesForOrganizationRequest

### eventArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### awsAccountIds
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeEntityAggregatesForOrganizationResponse

### organizationEntityAggregates
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEntityAggregate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEntityAggregatesRequest

### eventArns
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeEntityAggregatesResponse

### entityAggregates
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EntityAggregate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventAggregatesResponse

### eventAggregates
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventAggregate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEventDetailsForOrganizationRequest

### organizationEventDetailFilters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.health_classes.EventAccountFilter]
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]


# DescribeEventDetailsForOrganizationResponse

### successfulSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEventDetails]
- **Required**: Yes

### failedSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEventDetailsErrorItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventDetailsRequest

### eventArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### locale
- **Type**: typing.Optional[str]


# DescribeEventDetailsResponse

### successfulSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventDetails]
- **Required**: Yes

### failedSet
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventDetailsErrorItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEventTypesResponse

### eventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.EventType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEventsForOrganizationResponse

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.OrganizationEvent]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeEventsResponse

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.health_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeHealthServiceStatusForOrganizationResponse

### healthServiceAccessStatusForOrganization
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.health_classes.ResponseMetadata'>
- **Required**: Yes


# EntityAccountFilter

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]

### statusCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN']]]


# EntityAggregate

### eventArn
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### statuses
- **Type**: typing.Optional[typing.Dict[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN'], int]]


# EntityFilter

### eventArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### entityArns
- **Type**: typing.Optional[typing.Sequence[str]]

### entityValues
- **Type**: typing.Optional[typing.Sequence[str]]

### lastUpdatedTimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRange]]

### tags
- **Type**: typing.Optional[typing.Sequence[typing.Mapping[str, str]]]

### statusCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN']]]


# Event

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


# EventAccountFilter

### eventArn
- **Type**: <class 'str'>
- **Required**: Yes

### awsAccountId
- **Type**: typing.Optional[str]


# EventAggregate

### aggregateValue
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]


# EventDescription

### latestDescription
- **Type**: typing.Optional[str]


# EventDetails

### event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.Event]

### eventDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventDescription]

### eventMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventDetailsErrorItem

### eventArn
- **Type**: typing.Optional[str]

### errorName
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# EventFilter

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRange]]

### endTimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRange]]

### lastUpdatedTimes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.health_classes.DateTimeRange]]

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


# EventType

### service
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### category
- **Type**: typing.Optional[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]


# EventTypeFilter

### eventTypeCodes
- **Type**: typing.Optional[typing.Sequence[str]]

### services
- **Type**: typing.Optional[typing.Sequence[str]]

### eventTypeCategories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]]


# OrganizationAffectedEntitiesErrorItem

### awsAccountId
- **Type**: typing.Optional[str]

### eventArn
- **Type**: typing.Optional[str]

### errorName
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# OrganizationEntityAggregate

### eventArn
- **Type**: typing.Optional[str]

### count
- **Type**: typing.Optional[int]

### statuses
- **Type**: typing.Optional[typing.Dict[typing.Literal['IMPAIRED', 'PENDING', 'RESOLVED', 'UNIMPAIRED', 'UNKNOWN'], int]]

### accounts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.health_classes.AccountEntityAggregate]]


# OrganizationEvent

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


# OrganizationEventDetails

### awsAccountId
- **Type**: typing.Optional[str]

### event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.Event]

### eventDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.EventDescription]

### eventMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# OrganizationEventDetailsErrorItem

### awsAccountId
- **Type**: typing.Optional[str]

### eventArn
- **Type**: typing.Optional[str]

### errorName
- **Type**: typing.Optional[str]

### errorMessage
- **Type**: typing.Optional[str]


# OrganizationEventFilter

### eventTypeCodes
- **Type**: typing.Optional[typing.Sequence[str]]

### awsAccountIds
- **Type**: typing.Optional[typing.Sequence[str]]

### services
- **Type**: typing.Optional[typing.Sequence[str]]

### regions
- **Type**: typing.Optional[typing.Sequence[str]]

### startTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.DateTimeRange]

### endTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.DateTimeRange]

### lastUpdatedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.health_classes.DateTimeRange]

### entityArns
- **Type**: typing.Optional[typing.Sequence[str]]

### entityValues
- **Type**: typing.Optional[typing.Sequence[str]]

### eventTypeCategories
- **Type**: typing.Optional[typing.Sequence[typing.Literal['accountNotification', 'investigation', 'issue', 'scheduledChange']]]

### eventStatusCodes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['closed', 'open', 'upcoming']]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ResponseMetadata

### RequestId
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

### HostId
- **Type**: typing.Optional[str]


