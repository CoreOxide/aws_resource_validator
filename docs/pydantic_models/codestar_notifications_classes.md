# Codestar Notifications Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateNotificationRuleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventTypeIds
- **Type**: typing.List[str]
- **Required**: Yes

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.Target]
- **Required**: Yes

### DetailType
- **Type**: typing.Literal['BASIC', 'FULL']
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateNotificationRuleResult

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteNotificationRuleRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotificationRuleResult

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTargetRequest

### TargetAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ForceUnsubscribeAll
- **Type**: typing.Optional[bool]


# DescribeNotificationRuleRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotificationRuleResult

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.EventTypeSummary]
- **Required**: Yes

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.TargetSummary]
- **Required**: Yes

### DetailType
- **Type**: typing.Literal['BASIC', 'FULL']
- **Required**: Yes

### CreatedBy
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### CreatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastModifiedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes


# EventTypeSummary

### EventTypeId
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### EventTypeName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ListEventTypesFilter

### Name
- **Type**: typing.Literal['RESOURCE_TYPE', 'SERVICE_NAME']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListEventTypesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ListEventTypesFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventTypesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ListEventTypesFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.PaginatorConfig]


# ListEventTypesResult

### EventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.EventTypeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListNotificationRulesFilter

### Name
- **Type**: typing.Literal['CREATED_BY', 'EVENT_TYPE_ID', 'RESOURCE', 'TARGET_ADDRESS']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListNotificationRulesRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ListNotificationRulesFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNotificationRulesRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ListNotificationRulesFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.PaginatorConfig]


# ListNotificationRulesResult

### NotificationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.NotificationRuleSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResult

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes


# ListTargetsFilter

### Name
- **Type**: typing.Literal['TARGET_ADDRESS', 'TARGET_STATUS', 'TARGET_TYPE']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListTargetsRequest

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ListTargetsFilter]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTargetsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ListTargetsFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.PaginatorConfig]


# ListTargetsResult

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.TargetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# NotificationRuleSummary

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


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


# SubscribeRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.Target'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# SubscribeResult

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TagResourceResult

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes


# Target

### TargetType
- **Type**: typing.Optional[str]

### TargetAddress
- **Type**: typing.Optional[str]


# TargetSummary

### TargetAddress
- **Type**: typing.Optional[str]

### TargetType
- **Type**: typing.Optional[str]

### TargetStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEACTIVATED', 'INACTIVE', 'PENDING', 'UNREACHABLE']]


# UnsubscribeRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAddress
- **Type**: <class 'str'>
- **Required**: Yes


# UnsubscribeResult

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateNotificationRuleRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### EventTypeIds
- **Type**: typing.Optional[typing.List[str]]

### Targets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_classes.Target]]

### DetailType
- **Type**: typing.Optional[typing.Literal['BASIC', 'FULL']]


