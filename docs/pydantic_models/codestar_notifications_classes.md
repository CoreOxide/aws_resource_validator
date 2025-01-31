# Codestar Notifications Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateNotificationRuleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventTypeIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.TargetTypeDef]
- **Required**: Yes

### DetailType
- **Type**: typing.Literal['BASIC', 'FULL']
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# CreateNotificationRuleResultTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteNotificationRuleRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNotificationRuleResultTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTargetRequestRequestTypeDef

### TargetAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ForceUnsubscribeAll
- **Type**: typing.Optional[bool]


# DescribeNotificationRuleRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeNotificationRuleResultTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### EventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications_classes.EventTypeSummaryTypeDef]
- **Required**: Yes

### Resource
- **Type**: <class 'str'>
- **Required**: Yes

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications_classes.TargetSummaryTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventTypeSummaryTypeDef

### EventTypeId
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]

### EventTypeName
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[str]


# ListEventTypesFilterTypeDef

### Name
- **Type**: typing.Literal['RESOURCE_TYPE', 'SERVICE_NAME']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListEventTypesRequestListEventTypesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.ListEventTypesFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_notifications_classes.PaginatorConfigTypeDef]


# ListEventTypesRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.ListEventTypesFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListEventTypesResultTypeDef

### EventTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications_classes.EventTypeSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNotificationRulesFilterTypeDef

### Name
- **Type**: typing.Literal['CREATED_BY', 'EVENT_TYPE_ID', 'RESOURCE', 'TARGET_ADDRESS']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListNotificationRulesRequestListNotificationRulesPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.ListNotificationRulesFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_notifications_classes.PaginatorConfigTypeDef]


# ListNotificationRulesRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.ListNotificationRulesFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListNotificationRulesResultTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications_classes.NotificationRuleSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetsFilterTypeDef

### Name
- **Type**: typing.Literal['TARGET_ADDRESS', 'TARGET_STATUS', 'TARGET_TYPE']
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListTargetsRequestListTargetsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.ListTargetsFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codestar_notifications_classes.PaginatorConfigTypeDef]


# ListTargetsRequestRequestTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.ListTargetsFilterTypeDef]]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListTargetsResultTypeDef

### Targets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codestar_notifications_classes.TargetSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotificationRuleSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]


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


# SubscribeRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Target
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.TargetTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# SubscribeResultTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TagResourceResultTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TargetSummaryTypeDef

### TargetAddress
- **Type**: typing.Optional[str]

### TargetType
- **Type**: typing.Optional[str]

### TargetStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DEACTIVATED', 'INACTIVE', 'PENDING', 'UNREACHABLE']]


# TargetTypeDef

### TargetType
- **Type**: typing.Optional[str]

### TargetAddress
- **Type**: typing.Optional[str]


# UnsubscribeRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetAddress
- **Type**: <class 'str'>
- **Required**: Yes


# UnsubscribeResultTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codestar_notifications_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateNotificationRuleRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### EventTypeIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Targets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codestar_notifications_classes.TargetTypeDef]]

### DetailType
- **Type**: typing.Optional[typing.Literal['BASIC', 'FULL']]


