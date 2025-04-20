# Notifications Notifications Classes

# AggregationDetail

### summarizationDimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.SummarizationDimensionDetail]]


# AggregationKey

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# AggregationSummary

### eventCount
- **Type**: <class 'int'>
- **Required**: Yes

### aggregatedBy
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.AggregationKey]
- **Required**: Yes

### aggregatedAccounts
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.SummarizationDimensionOverview'>
- **Required**: Yes

### aggregatedRegions
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.SummarizationDimensionOverview'>
- **Required**: Yes

### aggregatedOrganizationalUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.SummarizationDimensionOverview]

### additionalSummarizationDimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.SummarizationDimensionOverview]]


# AssociateChannelRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateManagedNotificationAccountContactRequest

### contactIdentifier
- **Type**: typing.Literal['ACCOUNT_ALTERNATE_BILLING', 'ACCOUNT_ALTERNATE_OPERATIONS', 'ACCOUNT_ALTERNATE_SECURITY', 'ACCOUNT_PRIMARY']
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateManagedNotificationAdditionalChannelRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEventRuleRequest

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### regions
- **Type**: typing.List[str]
- **Required**: Yes

### eventPattern
- **Type**: typing.Optional[str]


# CreateEventRuleResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummaryByRegion
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.notifications.notifications_classes.EventRuleStatusSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNotificationConfigurationRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### aggregationDuration
- **Type**: typing.Optional[typing.Literal['LONG', 'NONE', 'SHORT']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateNotificationConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'INACTIVE', 'PARTIALLY_ACTIVE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEventRuleRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotificationConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterNotificationHubRequest

### notificationHubRegion
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterNotificationHubResponse

### notificationHubRegion
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationHubStatusSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# Dimension

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateChannelRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateManagedNotificationAccountContactRequest

### contactIdentifier
- **Type**: typing.Literal['ACCOUNT_ALTERNATE_BILLING', 'ACCOUNT_ALTERNATE_OPERATIONS', 'ACCOUNT_ALTERNATE_SECURITY', 'ACCOUNT_PRIMARY']
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateManagedNotificationAdditionalChannelRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes


# EventRuleStatusSummary

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'INACTIVE', 'UPDATING']
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# EventRuleStructure

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### eventPattern
- **Type**: <class 'str'>
- **Required**: Yes

### regions
- **Type**: typing.List[str]
- **Required**: Yes

### managedRules
- **Type**: typing.List[str]
- **Required**: Yes

### statusSummaryByRegion
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.notifications.notifications_classes.EventRuleStatusSummary]
- **Required**: Yes


# GetEventRuleRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventRuleResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### eventPattern
- **Type**: <class 'str'>
- **Required**: Yes

### regions
- **Type**: typing.List[str]
- **Required**: Yes

### managedRules
- **Type**: typing.List[str]
- **Required**: Yes

### statusSummaryByRegion
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.notifications.notifications_classes.EventRuleStatusSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedNotificationChildEventRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]


# GetManagedNotificationChildEventResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationChildEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedNotificationConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetManagedNotificationConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### category
- **Type**: <class 'str'>
- **Required**: Yes

### subCategory
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# GetManagedNotificationEventRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]


# GetManagedNotificationEventResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# GetNotificationConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNotificationConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'INACTIVE', 'PARTIALLY_ACTIVE']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### aggregationDuration
- **Type**: typing.Literal['LONG', 'NONE', 'SHORT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# GetNotificationEventRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]


# GetNotificationEventResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationEvent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# GetNotificationsAccessForOrganizationResponse

### notificationsAccessForOrganization
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationsAccessForOrganization'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# ListChannelsRequest

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginate

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListChannelsResponse

### channels
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEventRulesRequest

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListEventRulesRequestPaginate

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListEventRulesResponse

### eventRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.EventRuleStructure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedNotificationChannelAssociationsRequest

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedNotificationChannelAssociationsRequestPaginate

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListManagedNotificationChannelAssociationsResponse

### channelAssociations
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationChannelAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedNotificationChildEventsRequest

### aggregateManagedNotificationEventArn
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]

### maxResults
- **Type**: typing.Optional[int]

### relatedAccount
- **Type**: typing.Optional[str]

### organizationalUnitId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedNotificationChildEventsRequestPaginate

### aggregateManagedNotificationEventArn
- **Type**: <class 'str'>
- **Required**: Yes

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]

### relatedAccount
- **Type**: typing.Optional[str]

### organizationalUnitId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListManagedNotificationChildEventsResponse

### managedNotificationChildEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationChildEventOverview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedNotificationConfigurationsRequest

### channelIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListManagedNotificationConfigurationsRequestPaginate

### channelIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListManagedNotificationConfigurationsResponse

### managedNotificationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationConfigurationStructure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListManagedNotificationEventsRequest

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]

### source
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### organizationalUnitId
- **Type**: typing.Optional[str]

### relatedAccount
- **Type**: typing.Optional[str]


# ListManagedNotificationEventsRequestPaginate

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]

### source
- **Type**: typing.Optional[str]

### organizationalUnitId
- **Type**: typing.Optional[str]

### relatedAccount
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListManagedNotificationEventsResponse

### managedNotificationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationEventOverview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationConfigurationsRequest

### eventRuleSource
- **Type**: typing.Optional[str]

### channelArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'INACTIVE', 'PARTIALLY_ACTIVE']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationConfigurationsRequestPaginate

### eventRuleSource
- **Type**: typing.Optional[str]

### channelArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETING', 'INACTIVE', 'PARTIALLY_ACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListNotificationConfigurationsResponse

### notificationConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationConfigurationStructure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationEventsRequest

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]

### source
- **Type**: typing.Optional[str]

### includeChildEvents
- **Type**: typing.Optional[bool]

### aggregateNotificationEventArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationEventsRequestPaginate

### startTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### endTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### locale
- **Type**: typing.Optional[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW']]

### source
- **Type**: typing.Optional[str]

### includeChildEvents
- **Type**: typing.Optional[bool]

### aggregateNotificationEventArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListNotificationEventsResponse

### notificationEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationEventOverview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationHubsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNotificationHubsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.PaginatorConfig]


# ListNotificationHubsResponse

### notificationHubs
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationHubOverview]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# ManagedNotificationChannelAssociationSummary

### channelIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### channelType
- **Type**: typing.Literal['ACCOUNT_CONTACT', 'CHATBOT', 'EMAIL', 'MOBILE']
- **Required**: Yes

### overrideOption
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ManagedNotificationChildEvent

### schemaVersion
- **Type**: typing.Literal['v1.0']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### messageComponents
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.MessageComponents'>
- **Required**: Yes

### notificationType
- **Type**: typing.Literal['ALERT', 'ANNOUNCEMENT', 'INFORMATIONAL', 'WARNING']
- **Required**: Yes

### aggregateManagedNotificationEventArn
- **Type**: <class 'str'>
- **Required**: Yes

### textParts
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.notifications.notifications_classes.TextPartValue]
- **Required**: Yes

### sourceEventDetailUrl
- **Type**: typing.Optional[str]

### sourceEventDetailUrlDisplayText
- **Type**: typing.Optional[str]

### eventStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### organizationalUnitId
- **Type**: typing.Optional[str]

### aggregationDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.AggregationDetail]


# ManagedNotificationChildEventOverview

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedAccount
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### childEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationChildEventSummary'>
- **Required**: Yes

### aggregateManagedNotificationEventArn
- **Type**: <class 'str'>
- **Required**: Yes

### organizationalUnitId
- **Type**: typing.Optional[str]


# ManagedNotificationChildEventSummary

### schemaVersion
- **Type**: typing.Literal['v1.0']
- **Required**: Yes

### sourceEventMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedSourceEventMetadataSummary'>
- **Required**: Yes

### messageComponents
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.MessageComponentsSummary'>
- **Required**: Yes

### aggregationDetail
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.AggregationDetail'>
- **Required**: Yes

### eventStatus
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes

### notificationType
- **Type**: typing.Literal['ALERT', 'ANNOUNCEMENT', 'INFORMATIONAL', 'WARNING']
- **Required**: Yes


# ManagedNotificationConfigurationStructure

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes


# ManagedNotificationEvent

### schemaVersion
- **Type**: typing.Literal['v1.0']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### messageComponents
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.MessageComponents'>
- **Required**: Yes

### notificationType
- **Type**: typing.Literal['ALERT', 'ANNOUNCEMENT', 'INFORMATIONAL', 'WARNING']
- **Required**: Yes

### textParts
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.notifications.notifications_classes.TextPartValue]
- **Required**: Yes

### sourceEventDetailUrl
- **Type**: typing.Optional[str]

### sourceEventDetailUrlDisplayText
- **Type**: typing.Optional[str]

### eventStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### aggregationEventType
- **Type**: typing.Optional[typing.Literal['AGGREGATE', 'CHILD', 'NONE']]

### aggregationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.AggregationSummary]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### organizationalUnitId
- **Type**: typing.Optional[str]


# ManagedNotificationEventOverview

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### managedNotificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedAccount
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### notificationEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedNotificationEventSummary'>
- **Required**: Yes

### aggregationEventType
- **Type**: typing.Optional[typing.Literal['AGGREGATE', 'CHILD', 'NONE']]

### organizationalUnitId
- **Type**: typing.Optional[str]

### aggregationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.AggregationSummary]

### aggregatedNotificationRegions
- **Type**: typing.Optional[typing.List[str]]


# ManagedNotificationEventSummary

### schemaVersion
- **Type**: typing.Literal['v1.0']
- **Required**: Yes

### sourceEventMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ManagedSourceEventMetadataSummary'>
- **Required**: Yes

### messageComponents
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.MessageComponentsSummary'>
- **Required**: Yes

### eventStatus
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes

### notificationType
- **Type**: typing.Literal['ALERT', 'ANNOUNCEMENT', 'INFORMATIONAL', 'WARNING']
- **Required**: Yes


# ManagedSourceEventMetadataSummary

### source
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### eventOriginRegion
- **Type**: typing.Optional[str]


# MediaElement

### mediaId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['IMAGE']
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### caption
- **Type**: <class 'str'>
- **Required**: Yes


# MessageComponents

### headline
- **Type**: typing.Optional[str]

### paragraphSummary
- **Type**: typing.Optional[str]

### completeDescription
- **Type**: typing.Optional[str]

### dimensions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.Dimension]]


# MessageComponentsSummary

### headline
- **Type**: <class 'str'>
- **Required**: Yes


# NotificationConfigurationStructure

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'DELETING', 'INACTIVE', 'PARTIALLY_ACTIVE']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### aggregationDuration
- **Type**: typing.Optional[typing.Literal['LONG', 'NONE', 'SHORT']]


# NotificationEvent

### schemaVersion
- **Type**: typing.Literal['v1.0']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### sourceEventMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.SourceEventMetadata'>
- **Required**: Yes

### messageComponents
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.MessageComponents'>
- **Required**: Yes

### notificationType
- **Type**: typing.Literal['ALERT', 'ANNOUNCEMENT', 'INFORMATIONAL', 'WARNING']
- **Required**: Yes

### textParts
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.notifications.notifications_classes.TextPartValue]
- **Required**: Yes

### media
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.MediaElement]
- **Required**: Yes

### sourceEventDetailUrl
- **Type**: typing.Optional[str]

### sourceEventDetailUrlDisplayText
- **Type**: typing.Optional[str]

### eventStatus
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### aggregationEventType
- **Type**: typing.Optional[typing.Literal['AGGREGATE', 'CHILD', 'NONE']]

### aggregateNotificationEventArn
- **Type**: typing.Optional[str]

### aggregationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.AggregationSummary]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# NotificationEventOverview

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### relatedAccount
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### notificationEvent
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationEventSummary'>
- **Required**: Yes

### aggregationEventType
- **Type**: typing.Optional[typing.Literal['AGGREGATE', 'CHILD', 'NONE']]

### aggregateNotificationEventArn
- **Type**: typing.Optional[str]

### aggregationSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.notifications.notifications_classes.AggregationSummary]


# NotificationEventSummary

### schemaVersion
- **Type**: typing.Literal['v1.0']
- **Required**: Yes

### sourceEventMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.SourceEventMetadataSummary'>
- **Required**: Yes

### messageComponents
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.MessageComponentsSummary'>
- **Required**: Yes

### eventStatus
- **Type**: typing.Literal['HEALTHY', 'UNHEALTHY']
- **Required**: Yes

### notificationType
- **Type**: typing.Literal['ALERT', 'ANNOUNCEMENT', 'INFORMATIONAL', 'WARNING']
- **Required**: Yes


# NotificationHubOverview

### notificationHubRegion
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationHubStatusSummary'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastActivationTime
- **Type**: typing.Optional[datetime.datetime]


# NotificationHubStatusSummary

### status
- **Type**: typing.Literal['ACTIVE', 'DEREGISTERING', 'INACTIVE', 'REGISTERING']
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# NotificationsAccessForOrganization

### accessStatus
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'PENDING']
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RegisterNotificationHubRequest

### notificationHubRegion
- **Type**: <class 'str'>
- **Required**: Yes


# RegisterNotificationHubResponse

### notificationHubRegion
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.NotificationHubStatusSummary'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastActivationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# Resource

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### detailUrl
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[str]]


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


# SourceEventMetadata

### eventTypeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### sourceEventId
- **Type**: <class 'str'>
- **Required**: Yes

### relatedAccount
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### eventOccurrenceTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### relatedResources
- **Type**: typing.List[aws_resource_validator.pydantic_models.notifications.notifications_classes.Resource]
- **Required**: Yes

### eventOriginRegion
- **Type**: typing.Optional[str]


# SourceEventMetadataSummary

### source
- **Type**: <class 'str'>
- **Required**: Yes

### eventType
- **Type**: <class 'str'>
- **Required**: Yes

### eventOriginRegion
- **Type**: typing.Optional[str]


# SummarizationDimensionDetail

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# SummarizationDimensionOverview

### name
- **Type**: <class 'str'>
- **Required**: Yes

### count
- **Type**: <class 'int'>
- **Required**: Yes

### sampleValues
- **Type**: typing.Optional[typing.List[str]]


# TagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TextPartValue

### type
- **Type**: typing.Literal['LOCALIZED_TEXT', 'PLAIN_TEXT', 'URL']
- **Required**: Yes

### displayText
- **Type**: typing.Optional[str]

### textByLocale
- **Type**: typing.Optional[typing.Dict[typing.Literal['de_DE', 'en_CA', 'en_UK', 'en_US', 'es_ES', 'fr_CA', 'fr_FR', 'id_ID', 'it_IT', 'ja_JP', 'ko_KR', 'pt_BR', 'tr_TR', 'zh_CN', 'zh_TW'], str]]

### url
- **Type**: typing.Optional[str]


# UntagResourceRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateEventRuleRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### eventPattern
- **Type**: typing.Optional[str]

### regions
- **Type**: typing.Optional[typing.List[str]]


# UpdateEventRuleResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### notificationConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### statusSummaryByRegion
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.notifications.notifications_classes.EventRuleStatusSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNotificationConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### aggregationDuration
- **Type**: typing.Optional[typing.Literal['LONG', 'NONE', 'SHORT']]


# UpdateNotificationConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.notifications.notifications_classes.ResponseMetadata'>
- **Required**: Yes


